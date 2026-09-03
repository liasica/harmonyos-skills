---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-stability-memory-uaf-fault-mode
title: 内存释放后访问故障模式说明
breadcrumb: 最佳实践 > 稳定性 > 稳定性分析 > 稳定性故障模式说明 > 地址越界故障模式说明 > 内存释放后访问故障模式说明
category: best-practices
scraped_at: 2026-09-04T06:33:24+08:00
doc_updated_at: 2026-09-03
content_hash: sha256:c05867419ae02c198d690a07333df1cbd34931dba6100b5378af860014caf2c2
---

堆内存释放后或栈变量生命周期结束后，原有指针将失效，若程序继续通过失效指针读写内存，将导致内存释放后访问。此类问题可能表现为读取错误数据，导致业务异常；也可能破坏其他有效内存，使应用后续在其他位置崩溃，问题通常难以定位。开启检测能力后，可在访问失效内存时检测异常，并记录异常访问、内存分配和释放等调用栈。

本文结合HWASan（Hardware-assisted AddressSanitizer）、ASan（AddressSanitizer）和GWP-ASan（GWP-ASan Will Provide Allocation SANity）典型案例，介绍内存释放后访问的日志特征与定位方法，具体包括：

* [HWASan堆内存释放后访问](bpta-stability-memory-uaf-fault-mode.md#section6313643164617)
* [ASan堆内存释放后访问](bpta-stability-memory-uaf-fault-mode.md#section9625174510509)
* [GWP-ASan堆内存释放后访问](bpta-stability-memory-uaf-fault-mode.md#section198186274546)
* [HWASan局部变量在代码块返回后被访问](bpta-stability-memory-uaf-fault-mode.md#section96190175307)
* [ASan局部变量在代码块返回后被访问](bpta-stability-memory-uaf-fault-mode.md#section152491045244)
* [HWASan局部变量在函数返回后被访问](bpta-stability-memory-uaf-fault-mode.md#section183181832195814)

## HWASan堆内存释放后访问

### 根因描述

堆内存释放后访问的本质是内存生命周期管理错误。堆内存已释放，但程序仍持有指向该内存的指针，并继续通过该指针进行读写。应用[开启HWASan](../harmonyos-guides/ide-hwasan.md#section38898177587)检测能力后，运行时会对指针标签和内存标签进行校验。一旦检测到程序访问已经释放的堆内存，HWASan会报告use-after-free异常。

### 问题分析思路

此类问题通常有以下几种可能：

1. 释放后直接继续使用指针。

2. 多个指针指向同一块内存，其中一个释放后另一个继续访问。

3. 对象所有权不清晰导致提前释放。

4. 异步回调中访问已经释放的对象。

5. 引用计数或智能指针使用错误。

6. 多线程竞争导致访问释放并发发生。

问题分析步骤如下：

1. 查看HWASan故障日志，确认故障类型。重点关注是否包含关键字use-after-free，若存在则可初步确认属于堆内存释放后访问。
2. 分析报错栈、释放栈和分配栈，通过llvm-addr2line（参考：[C++堆栈解析流程](../harmonyos-guides/ide-exception-stack-parsing-principle.md#section1735713501344)中对于llvm-addr2line的使用）等解析工具，定位到具体业务代码行。
3. 结合报错栈、释放栈和分配栈，还原内存对象生命周期，确认问题根因。
4. 若步骤1~3仍无法定位根因，且发现分配栈/释放栈和报错栈没有关联，可以查看是否存在环形缓冲区（ringbuffer）满了的情况。HWASan依赖ringbuffer记录分配栈，在高频malloc()/free()的场景下，ringbuffer可能已写满并覆盖历史记录。建议修改ringbuffer上限大小并重新复现压测。

### 关键字

此类问题通常可通过use-after-free确认故障类型。重点关注报错栈和释放栈，结合代码还原内存对象生命周期。

### 案例分析

**案例一：**堆内存释放后直接访问

**问题现象**

应用运行过程中触发HWASan检测，检测到堆内存释放后访问应用闪退。

**问题分析**

1. 查看日志内容，确认故障类型。

   ```screen
   Module name:xxxx
   Version:1.0.1
   Pid:8815
   Uid:20020212
   Reason:use-after-free
   ==appspawn==8815==ERROR: HWAddressSanitizer: tag-mismatch on address 0x000100585aa0 at pc 0x005bc94cb204
   READ of size 4 at 0x000100585aa0 tags: da/2f (ptr/mem) in thread 8815
       #0 0x5bc94cb204  (/data/storage/el1/bundle/libs/arm64/libentry.so+0x14b204) (BuildId: 09b439232284296fea0d1ef34ebeae9a9a90bb42)
       #1 0x5babb28070  (/system/lib64/platformsdk/libace_napi.z.so+0x68070) (BuildId: 1c8eca94c70551effe8255c9acf481a8)
    
   [0x000100585aa0,0x000100585ac0) is a small unallocated heap chunk; size: 32 offset: 0, Allocated By 8815
    
   Potential Cause: use-after-free
   0x000100585aa0 (rb[1022999] tags:da) is located 0 bytes inside of 4-byte region [0x000100585aa0,0x000100585aa4)
   freed by thread 8815 here:
       #0 0x5b16a6c77c  (/system/lib64/libclang_rt.hwasan.so+0x2c77c) (BuildId: fbf2bf42dacf79aa5727291d84299c62620655ef)
       #1 0x5bc94cb1e4  (/data/storage/el1/bundle/libs/arm64/libentry.so+0x14b1e4) (BuildId: 09b439232284296fea0d1ef34ebeae9a9a90bb42)
       #2 0x5babb28070  (/system/lib64/platformsdk/libace_napi.z.so+0x68070) (BuildId: 1c8eca94c70551effe8255c9acf481a8)
       #3 0x5bc04e5488  (/system/lib64/module/arkcompiler/stub.an+0xe8b488)
       #4 0x5bbfad7d94  (/system/lib64/module/arkcompiler/stub.an+0x47dd94)
    
   previously allocated by thread 8815 here:
       #0 0x5b16a6c3ac  (/system/lib64/libclang_rt.hwasan.so+0x2c3ac) (BuildId: fbf2bf42dacf79aa5727291d84299c62620655ef)
       #1 0x5bc94cb1a0  (/data/storage/el1/bundle/libs/arm64/libentry.so+0x14b1a0) (BuildId: 09b439232284296fea0d1ef34ebeae9a9a90bb42)
       #2 0x5babb28070  (/system/lib64/platformsdk/libace_napi.z.so+0x68070) (BuildId: 1c8eca94c70551effe8255c9acf481a8)
       #3 0x5bc04e5488  (/system/lib64/module/arkcompiler/stub.an+0xe8b488)
       #4 0x5bbfad7d94  (/system/lib64/module/arkcompiler/stub.an+0x47dd94)
    
   hwasan_dev_note_heap_rb_distance: 1023000 1023000
   Thread: T0 0x005c00002000 stack: [0x007e56ee2000,0x007e576e1000) sz: 8384512 tls: [0x005b15864cb0,0x005b158653ab) rb:(1023000/1023000/1023000) records(1407139/o:0) tid: 8815
   Searched 1031802 records, find 1 with same addr 0x000100585aa0
   ```

   证据1：日志中明确给出use-after-free，可初步确认该问题属于堆内存释放后访问。READ of size 4表明线程8815对异常地址执行了4字节读操作，且分配、释放和报错栈均发生在线程8815，是一个同线程下的释放后访问问题。

   ```screen
   Reason:use-after-free
   ==appspawn==8815==ERROR: HWAddressSanitizer: tag-mismatch on address 0x000100585aa0 at pc 0x005bc94cb204
   READ of size 4 at 0x000100585aa0 tags: da/2f (ptr/mem) in thread 8815
   ...
   Potential Cause: use-after-free
   0x000100585aa0 (rb[1022999] tags:da) is located 0 bytes inside of 4-byte region [0x000100585aa0,0x000100585aa4)
   freed by thread 8815 here:
   ...
   previously allocated by thread 8815 here:
   ```

   证据2：日志显示异常地址所在区域为small unallocated heap chunk，说明程序访问该地址时，对应堆内存已经处于释放状态，可进一步确认该问题属于堆内存释放后访问。

   ```screen
   [0x000100585aa0,0x000100585ac0) is a small unallocated heap chunk; size: 32 offset: 0, Allocated By 8815
   ```
2. 分析报错栈、释放栈和分配栈，定位对应的业务代码。

   通过llvm-addr2line（参考：[C++堆栈解析流程](../harmonyos-guides/ide-exception-stack-parsing-principle.md#section1735713501344)中对于llvm-addr2line的使用）等解析工具，定位到具体业务代码行，如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c4/v3/3K-EFsFBRl6vgEuFaoPF3Q/zh-cn_image_0000002729491381.png)

   1号位置对应分配栈，通过new int(42)申请堆内存；2号位置对应释放栈，通过delete ptr释放堆内存；3号位置对应报错栈，通过\*ptr读取堆内存。
3. 还原内存对象生命周期，确认问题根因。

   结合三个栈可以还原该内存的生命周期：程序先通过new int(42)申请堆内存，并将地址保存到ptr中，随后通过delete ptr释放该内存。内存释放后，ptr仍保留原地址并成为悬空指针，后续代码继续通过\*ptr访问已经释放的内存，最终触发use-after-free异常。

**问题结论与总结**

该问题的根本原因是：TriggerUseAfterFree()中，ptr指向的堆内存释放后，程序仍继续通过ptr访问该内存。由于内存生命周期管理不当，最终发生堆内存释放后访问。

**案例二**：异步回调中访问已经释放的堆内存对象

**问题现象**

应用运行过程中触发HWASan检测，检测到堆内存释放后访问应用闪退。

**问题分析**

1. 查看日志内容，确认故障类型。

   ```screen
   Module name:com.example.myapplication
   Version:1.0.0
   Pid:13222
   Uid:20020212
   Reason:use-after-free
   ==appspawn==13222==ERROR: HWAddressSanitizer: tag-mismatch on address 0x000201510400 at pc 0x005bbecc3148
   WRITE of size 1 at 0x000201510400 tags: 93/57 (ptr/mem) in thread 13222
       #0 0x5bbecc3148  (/data/storage/el1/bundle/libs/arm64/libentry.so+0xc3148) (BuildId: 3b6dbbd8e245271e9270d5d2958dfcbf0d5cdb9c)
       #1 0x5ba131bd10  (/system/lib64/platformsdk/libuv.so+0x1bd10) (BuildId: 736f600fc1ccf9b9d3388de5ff19abd1)
       #2 0x5ba1331d70  (/system/lib64/platformsdk/libuv.so+0x31d70) (BuildId: 736f600fc1ccf9b9d3388de5ff19abd1)
       #3 0x5ba131ce68  (/system/lib64/platformsdk/libuv.so+0x1ce68) (BuildId: 736f600fc1ccf9b9d3388de5ff19abd1)

   [0x000201510400,0x000201510440) is a small unallocated heap chunk; size: 64 offset: 0, Allocated By 13222

   hwasan_dev_note_heap_rb_distance: 101763 102300
   Thread: T0 0x005c00002000 stack: [0x007e0eaa9000,0x007e0f2a8000) sz: 8384512 tls: [0x005b156fa8f0,0x005b156fafeb) rb:(102300/102300/102300) records(1286423/o:0) tid: 13222

   Potential Cause: use-after-free
   0x000201510400 (rb[101922] tags:93) is located 0 bytes inside of 50-byte region [0x000201510400,0x000201510432)
   freed by thread 13222 here:
       #0 0x5b178acea4  (/system/lib64/libclang_rt.hwasan.so+0x2cea4) (BuildId: 29cd839fde93692a63b6bd1b64b35830f6de6e33)
       #1 0x5bbecb8030  (/data/storage/el1/bundle/libs/arm64/libentry.so+0xb8030) (BuildId: 3b6dbbd8e245271e9270d5d2958dfcbf0d5cdb9c)
       #2 0x5ba0e3010c  (/system/lib64/platformsdk/libace_napi.z.so+0x7010c) (BuildId: 226dc0ffc65e2899a5e810b4acb58e65)
       #3 0x5bbbf351e8  (/system/lib64/module/arkcompiler/stub.an+0xe8b1e8)
       #4 0x5bbb527dac  (/system/lib64/module/arkcompiler/stub.an+0x47ddac)

   previously allocated by thread 13222 here:
       #0 0x5b178acae0  (/system/lib64/libclang_rt.hwasan.so+0x2cae0) (BuildId: 29cd839fde93692a63b6bd1b64b35830f6de6e33)
       #1 0x5bbecb7f2c  (/data/storage/el1/bundle/libs/arm64/libentry.so+0xb7f2c) (BuildId: 3b6dbbd8e245271e9270d5d2958dfcbf0d5cdb9c)
       #2 0x5ba0e3010c  (/system/lib64/platformsdk/libace_napi.z.so+0x7010c) (BuildId: 226dc0ffc65e2899a5e810b4acb58e65)
       #3 0x5bbbf351e8  (/system/lib64/module/arkcompiler/stub.an+0xe8b1e8)
       #4 0x5bbb527dac  (/system/lib64/module/arkcompiler/stub.an+0x47ddac)
   ```

   证据1：日志中明确给出use-after-free，可初步确认该问题属于堆内存释放后访问。WRITE of size 1表明线程13222对异常地址执行了1字节写操作，且内存分配、释放和异常访问均发生在线程13222。

   ```screen
   Reason:use-after-free
   ==appspawn==13222==ERROR: HWAddressSanitizer: tag-mismatch on address 0x000201510400 at pc 0x005bbecc3148
   WRITE of size 1 at 0x000201510400 tags: 93/57 (ptr/mem) in thread 13222
   ...
   Potential Cause: use-after-free
   0x000201510400 (rb[101922] tags:93) is located 0 bytes inside of 50-byte region [0x000201510400,0x000201510432)
   freed by thread 13222 here:
   ...
   previously allocated by thread 13222 here:
   ...
   ```

   证据2：日志显示异常地址所在区域为small unallocated heap chunk，说明程序执行写操作时，该堆内存已经处于释放状态，可进一步确认该问题属于堆内存释放后访问。

   ```screen
   [0x000201510400,0x000201510440) is a small unallocated heap chunk; size: 64 offset: 0, Allocated By 13222
   ```
2. 分析报错栈、释放栈和分配栈，定位对应的业务代码。

   通过llvm-addr2line（参考：[C++堆栈解析流程](../harmonyos-guides/ide-exception-stack-parsing-principle.md#section1735713501344)中对于llvm-addr2line的使用）等解析工具，定位到具体业务代码行，如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a4/v3/8RpmwCoCRl6vs51FmK4KPw/zh-cn_image_0000002699892008.png "点击放大")

   1号位置对应报错栈，通过ptr[0] = 42写入堆内存；2号位置对应分配栈，通过new char[50]申请堆内存；3号位置提交异步任务；4号位置对应释放栈，通过delete[] buffer释放堆内存。
3. 还原内存对象生命周期，确认问题根因。

   程序首先通过new char[50]为buffer申请50字节堆内存，并将其地址保存到async->data中。随后通过uv\_async\_send()提交异步任务，但主流程没有等待异步回调执行完成，而是继续执行delete[] buffer释放该内存。本案例中，异步回调在内存释放后才开始执行，回调函数从handle->data中获取已经失效的地址，并通过ptr[0] = 42继续写入，最终触发HWASan的use-after-free异常。

**问题结论与总结**

该问题的根本原因是：InjectHeapUseAfterFree()提交异步任务后提前释放了buffer指向的堆内存，而异步回调仍持有该地址并继续访问。由于异步任务的执行周期超过了buffer的有效生命周期，最终发生堆内存释放后访问。

**修复建议**

此类释放后访问问题常见修复方案如下：

1. 使用智能指针管理生命周期。

2. 实现一个delete析构器来保证指针的重置。

3. 访问前判断对象是否有效。

4. 多线程访问加锁或引用计数保护。

## ASan堆内存释放后访问

### 根因描述

堆内存释放后访问的本质是内存生命周期管理错误。堆内存已释放，但程序仍持有指向该内存的指针，并继续通过该指针进行读写。当应用[开启ASan](../harmonyos-guides/ide-asan.md#section111599216114)检测能力后，内存释放时会将对应区域标记为不可访问状态，并通过影子内存（Shadow Memory）记录内存的可访问状态。一旦检测到程序访问已经释放的堆内存，ASan会报告heap-use-after-free异常。

### 问题分析思路

此类问题的常见原因与[HWASan堆内存释放后访问](bpta-stability-memory-uaf-fault-mode.md#section6313643164617)一致，通常由内存生命周期管理不当导致，此处就不再赘述。对于ASan，问题分析步骤如下：

1. 查看ASan故障日志，确认故障类型。重点关注是否包含关键字heap-use-after-free，若存在则可确认是堆内存释放后访问。
2. 分析报错栈、释放栈和分配栈，通过llvm-addr2line（参考：[C++堆栈解析流程](../harmonyos-guides/ide-exception-stack-parsing-principle.md#section1735713501344)中对于llvm-addr2line的使用）等解析工具，定位到具体业务代码行。
3. 结合报错栈、释放栈和分配栈，还原内存对象生命周期，确认问题根因。
4. 结合ASan Shadow信息辅助确认。ASan日志中的Shadow bytes可辅助判断异常地址所处内存状态。

### 关键字

此类问题通常可通过heap-use-after-free确认故障类型。重点关注报错栈和释放栈，结合代码还原内存对象生命周期。

### 案例分析

**案例一**：堆内存释放后直接访问

**问题现象**

应用运行过程中触发ASan检测，检测到堆内存释放后访问应用闪退。

**问题分析**

1. 查看日志内容，确认故障类型。

   ```screen
   Module name:xxxx
   Version:1.0.1
   Pid:12615
   Uid:20020209
   Reason:heap-use-after-free
   ==appspawn==12615==AddressSanitizer: WARNING: unexpected format specifier in printf interceptor: %{ (reported once per process)
   =================================================================
   ==appspawn==12615==ERROR: AddressSanitizer: heap-use-after-free on address 0x005b2e4c5f30 at pc 0x007b53057ae0 bp 0x007e6395c170 sp 0x007e6395c168
   READ of size 4 at 0x005b2e4c5f30 thread T0 (xample.dfx_test)
       #0 0x7b53057adc  (/data/storage/el1/bundle/libs/arm64/libentry.so+0x257adc) (BuildId: 6e3d4674182d9620a90dd40754f2a4923bf00313)
       #1 0x7a33328070  (/system/lib64/platformsdk/libace_napi.z.so+0x68070) (BuildId: 1c8eca94c70551effe8255c9acf481a8)

   0x005b2e4c5f30 is located 0 bytes inside of 4-byte region [0x005b2e4c5f30,0x005b2e4c5f34)
   freed by thread T0 (xample.dfx_test) here:
       #0 0x59ab2ec368  (/system/lib64/libclang_rt.asan.so+0xec368) (BuildId: d6b3ed928d4dd75066c98e027215a2800cb9c838)
       #1 0x7b53057a80  (/data/storage/el1/bundle/libs/arm64/libentry.so+0x257a80) (BuildId: 6e3d4674182d9620a90dd40754f2a4923bf00313)
       #2 0x7a33328070  (/system/lib64/platformsdk/libace_napi.z.so+0x68070) (BuildId: 1c8eca94c70551effe8255c9acf481a8)

   previously allocated by thread T0 (xample.dfx_test) here:
       #0 0x59ab2eb9c8  (/system/lib64/libclang_rt.asan.so+0xeb9c8) (BuildId: d6b3ed928d4dd75066c98e027215a2800cb9c838)
       #1 0x7b530579f4  (/data/storage/el1/bundle/libs/arm64/libentry.so+0x2579f4) (BuildId: 6e3d4674182d9620a90dd40754f2a4923bf00313)
       #2 0x7a33328070  (/system/lib64/platformsdk/libace_napi.z.so+0x68070) (BuildId: 1c8eca94c70551effe8255c9acf481a8)

   SUMMARY: AddressSanitizer: heap-use-after-free (/data/storage/el1/bundle/libs/arm64/libentry.so+0x257adc) (BuildId: 6e3d4674182d9620a90dd40754f2a4923bf00313) 
   Shadow bytes around the buggy address:
     0x001b90705410: fa fa fa fa fa fa fa fa fa fa fa fa fa fa 00 00
     0x001b90705420: fa fa 00 00 fa fa 00 00 fa fa 00 00 fa fa 00 00
     0x001b90705430: fa fa 00 00 fa fa 00 00 fa fa 00 00 fa fa 00 00
     0x001b90705440: fa fa 00 00 fa fa 00 00 fa fa 00 00 fa fa 00 00
     0x001b90705450: fa fa 00 00 fa fa 00 00 fa fa 00 00 fa fa 00 fa
   =>0x001b90705460: fa fa[fd]fa fa fa fa fa fa fa fa fa fa fa fa fa
     0x001b90705470: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
     0x001b90705480: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
     0x001b90705490: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
     0x001b907054a0: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
     0x001b907054b0: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
   Shadow byte legend (one shadow byte represents 8 application bytes):
     Addressable:           00
     Partially addressable: 01 02 03 04 05 06 07 
     Heap left redzone:       fa
     Freed heap region:       fd
     Stack left redzone:      f1
     Stack mid redzone:       f2
     Stack right redzone:     f3
     Stack after return:      f5
     Stack use after scope:   f8
     Global redzone:          f9
     Global init order:       f6
     Poisoned by user:        f7
     Container overflow:      fc
     Array cookie:            ac
     Intra object redzone:    bb
     ASan internal:           fe
     Left alloca redzone:     ca
     Right alloca redzone:    cb
   ```

   证据1：日志中明确给出heap-use-after-free，可确认该问题属于堆内存释放后访问。READ of size 4表明线程T0对异常地址0x005b2e4c5f30执行了4字节读操作。内存分配、释放和异常访问均发生在线程T0。

   ```screen
   Reason:heap-use-after-free
   ==appspawn==12615==ERROR: AddressSanitizer: heap-use-after-free on address 0x005b2e4c5f30 at pc 0x007b53057ae0 bp 0x007e6395c170 sp 0x007e6395c168
   READ of size 4 at 0x005b2e4c5f30 thread T0 (xample.dfx_test)
   ...
   0x005b2e4c5f30 is located 0 bytes inside of 4-byte region [0x005b2e4c5f30,0x005b2e4c5f34)
   freed by thread T0 (xample.dfx_test) here:
   ...
   previously allocated by thread T0 (xample.dfx_test) here:
   ...
   ```
2. 分析报错栈、释放栈和分配栈，定位对应的业务代码。

   通过llvm-addr2line（参考：[C++堆栈解析流程](../harmonyos-guides/ide-exception-stack-parsing-principle.md#section1735713501344)中对于llvm-addr2line的使用）等解析工具，定位到具体业务代码行，如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/32/v3/0AIIBq5aQwaP0K4a7lQwSA/zh-cn_image_0000002729611335.png)

   1号位置对应分配栈，通过new int(42)申请堆内存；2号位置对应释放栈，通过delete ptr释放堆内存；3号位置对应报错栈，通过\*ptr读取堆内存。
3. 还原内存对象生命周期，确认问题根因。

   结合上述三个堆栈，可以还原该内存的生命周期：程序首先通过new int(42)申请堆内存，并将地址保存到ptr中，随后通过delete ptr释放该内存。内存释放后，ptr成为悬空指针，后续代码继续通过\*ptr访问已经释放的内存，最终触发ASan的heap-use-after-free异常。
4. 结合ASan Shadow信息辅助确认。

   证据2：ASan日志中异常地址对应的Shadow byte为fd。根据Shadow byte legend，fd表示Freed heap region，说明该地址对应的堆内存已释放。此外，基于指针与Shadow内存1:8的对齐映射关系，本案例中申请的 4字节int变量小于8字节，因此在Shadow内存中仅且恰好占用1个fd标记。结合上述信息，可进一步确认该问题属于堆内存释放后访问，且释放的内存大小在8字节以内。

   ```screen
   Shadow bytes around the buggy address:
     ...
     0x001b90705450: fa fa 00 00 fa fa 00 00 fa fa 00 00 fa fa 00 fa
   =>0x001b90705460: fa fa[fd]fa fa fa fa fa fa fa fa fa fa fa fa fa
     ...
   Shadow byte legend (one shadow byte represents 8 application bytes):
   Freed heap region:       fd
   ```

**问题结论与总结**

该问题的根本原因是：TriggerUseAfterFree()中，ptr指向的堆内存释放后，程序仍继续通过ptr访问该内存。由于内存生命周期管理不当，ptr成为悬空指针并继续使用，最终发生堆内存释放后访问。

**案例二**：异步回调中访问已经释放的堆内存对象

**问题现象**

应用运行过程中触发ASan检测，检测到堆内存释放后访问应用闪退。

**问题分析**

1. 查看日志内容，确认故障类型。

   ```screen
   Module name:com.example.myapplication
   Version:1.0.0
   Pid:21855
   Uid:20020212
   Reason:heap-use-after-free
   ==appspawn==21855==AddressSanitizer: WARNING: unexpected format specifier in printf interceptor: %{ (reported once per process)
   =================================================================
   ==appspawn==21855==ERROR: AddressSanitizer: heap-use-after-free on address 0x005d688b7520 at pc 0x007b877dab18 bp 0x007e4d273ff0 sp 0x007e4d273fe8
   WRITE of size 1 at 0x005d688b7520 thread T0 (e.myapplication)
       #0 0x7b877dab14  (/data/storage/el1/bundle/libs/arm64/libentry.so+0xdab14) (BuildId: 2e4bb9e372cca4f8c8748dc4c7656a43eafb3547)
       #1 0x7a6ae5bd10  (/system/lib64/platformsdk/libuv.so+0x1bd10) (BuildId: 736f600fc1ccf9b9d3388de5ff19abd1)

   0x005d688b7520 is located 0 bytes inside of 50-byte region [0x005d688b7520,0x005d688b7552)
   freed by thread T0 (e.myapplication) here:
       #0 0x59e426c48c  (/system/lib64/libclang_rt.asan.so+0xec48c) (BuildId: f56f0195024955df4ca655d4a88c5c0cb1a29e1a)
       #1 0x7b877cfe94  (/data/storage/el1/bundle/libs/arm64/libentry.so+0xcfe94) (BuildId: 2e4bb9e372cca4f8c8748dc4c7656a43eafb3547)
       #2 0x7a69ef010c  (/system/lib64/platformsdk/libace_napi.z.so+0x7010c) (BuildId: 226dc0ffc65e2899a5e810b4acb58e65)

   previously allocated by thread T0 (e.myapplication) here:
       #0 0x59e426bb04  (/system/lib64/libclang_rt.asan.so+0xebb04) (BuildId: f56f0195024955df4ca655d4a88c5c0cb1a29e1a)
       #1 0x7b877cfd70  (/data/storage/el1/bundle/libs/arm64/libentry.so+0xcfd70) (BuildId: 2e4bb9e372cca4f8c8748dc4c7656a43eafb3547)
       #2 0x7a69ef010c  (/system/lib64/platformsdk/libace_napi.z.so+0x7010c) (BuildId: 226dc0ffc65e2899a5e810b4acb58e65)

   SUMMARY: AddressSanitizer: heap-use-after-free (/data/storage/el1/bundle/libs/arm64/libentry.so+0xdab14) (BuildId: 2e4bb9e372cca4f8c8748dc4c7656a43eafb3547) 
   Shadow bytes around the buggy address:
     0x001ba1e22c10: fd fd fd fd fa fa fa fa fd fd fd fd fd fd fd fd
     0x001ba1e22c20: fa fa fa fa fd fd fd fd fd fd fd fd fa fa fa fa
     0x001ba1e22c30: fd fd fd fd fd fd fd fd fa fa fa fa fd fd fd fd
     0x001ba1e22c40: fd fd fd fd fa fa fa fa fd fd fd fd fd fd fd fd
     0x001ba1e22c50: fa fa fa fa fd fd fd fd fd fd fd fd fa fa fa fa
   =>0x001ba1e22c60:[fd]fd fd fd fd fd fd fa fa fa fa fa fd fd fd fd
     0x001ba1e22c70: fd fd fd fd fa fa fa fa fd fd fd fd fd fd fd fd
     0x001ba1e22c80: fa fa fa fa fd fd fd fd fd fd fd fd fa fa fa fa
     0x001ba1e22c90: fd fd fd fd fd fd fd fd fa fa fa fa fd fd fd fd
     0x001ba1e22ca0: fd fd fd fd fa fa fa fa fd fd fd fd fd fd fd fd
     0x001ba1e22cb0: fa fa fa fa fd fd fd fd fd fd fd fd fa fa fa fa
   Shadow byte legend (one shadow byte represents 8 application bytes):
     Addressable:           00
     Partially addressable: 01 02 03 04 05 06 07 
     Heap left redzone:       fa
     Freed heap region:       fd
     Stack left redzone:      f1
     Stack mid redzone:       f2
     Stack right redzone:     f3
     Stack after return:      f5
     Stack use after scope:   f8
     Global redzone:          f9
     Global init order:       f6
     Poisoned by user:        f7
     Container overflow:      fc
     Array cookie:            ac
     Intra object redzone:    bb
     ASan internal:           fe
     Left alloca redzone:     ca
     Right alloca redzone:    cb
   ```

   证据1：日志中明确给出heap-use-after-free，可确认该问题属于堆内存释放后访问。WRITE of size 1表明线程T0对异常地址执行了1字节写操作，且内存分配、释放和异常访问均发生在线程T0。

   ```screen
   Reason:heap-use-after-free
   ==appspawn==21855==ERROR: AddressSanitizer: heap-use-after-free on address 0x005d688b7520 at pc 0x007b877dab18 bp 0x007e4d273ff0 sp 0x007e4d273fe8
   WRITE of size 1 at 0x005d688b7520 thread T0 (e.myapplication)
   ...
   0x005d688b7520 is located 0 bytes inside of 50-byte region [0x005d688b7520,0x005d688b7552)
   freed by thread T0 (e.myapplication) here:
   ...
   previously allocated by thread T0 (e.myapplication) here:
   ...
   ```
2. 分析报错栈、释放栈和分配栈，定位对应的业务代码。

   通过llvm-addr2line（参考：[C++堆栈解析流程](../harmonyos-guides/ide-exception-stack-parsing-principle.md#section1735713501344)中对于llvm-addr2line的使用）等解析工具，定位到具体业务代码行，如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cc/v3/TSlj05j5TOeFLfOq-AdeUg/zh-cn_image_0000002699732126.png "点击放大")

   1号位置对应报错栈，通过ptr[0] = 42写入堆内存；2号位置对应分配栈，通过new char[50]申请堆内存；3号位置提交异步任务；4号位置对应释放栈，通过delete[] buffer释放堆内存。
3. 还原内存对象生命周期，确认问题根因。

   程序首先通过new char[50]为buffer申请50字节堆内存，并将其地址保存到async->data中。随后通过uv\_async\_send()提交异步任务，但主流程未等待异步回调执行完成，继续执行delete[] buffer释放该内存。本案例中，异步回调在内存释放后才执行，从handle->data中获取已经失效的地址，并通过ptr[0] = 42继续写入，最终触发ASan的heap-use-after-free异常。
4. 结合ASan Shadow信息辅助确认。

   证据2：同上一个案例一样，Shadow Byte中的fd表示对应堆内存已释放。本案例中释放的内存大小为50字节，因此在Shadow内存中表现为连续多个fd标记，可进一步确认该问题属于堆内存释放后访问。

   ```screen
   Shadow bytes around the buggy address:
     0x001ba1e22c50: fa fa fa fa fd fd fd fd fd fd fd fd fa fa fa fa
   =>0x001ba1e22c60:[fd]fd fd fd fd fd fd fa fa fa fa fa fd fd fd fd
   ```

**问题结论与总结**

该问题的根本原因是：InjectHeapUseAfterFree()中为buffer申请堆内存并提交异步任务后，主流程提前释放了该内存。异步回调执行时仍通过handle->data访问已经释放的地址，由于异步任务与内存生命周期管理不当，最终发生堆内存释放后访问。

**修复建议**

此类问题常见修复方案如下：

1. 使用智能指针管理生命周期。

2. 实现一个delete析构器来保证指针的重置。

3. 访问前判断对象是否有效。

4. 多线程访问加锁或引用计数保护。

## GWP-ASan堆内存释放后访问

### 根因描述

堆内存释放后访问的本质是内存生命周期管理错误。堆内存已释放，但程序仍持有指向该内存的指针，并继续通过该指针进行读写。当应用[GWP-ASan使能](bpta-stability-gwpasan-detection.md#section2735718353)后，GWP-ASan会对部分堆内存分配进行采样，并将采样对象放入受保护的内存区域。当程序访问已经释放的采样对象时，GWP-ASan会报告Use After Free异常。

### 问题分析思路

此类问题的常见原因与[HWASan堆内存释放后访问](bpta-stability-memory-uaf-fault-mode.md#section6313643164617)一致，通常由内存生命周期管理不当导致，此处不再赘述。对于GWP-ASan，问题分析步骤如下：

1. 查看GWP-ASan故障日志，确认故障类型。重点关注是否包含关键字Use After Free，若存在则可确认是堆内存释放后访问。
2. 分析报错栈、释放栈和分配栈，通过llvm-addr2line（参考：[C++堆栈解析流程](../harmonyos-guides/ide-exception-stack-parsing-principle.md#section1735713501344)中对于llvm-addr2line的使用）等解析工具，定位到具体业务代码行。
3. 结合报错栈、释放栈和分配栈，还原内存对象生命周期，确认问题根因。

### 关键字

此类问题通常可通过Use After Free确认故障类型。重点关注报错栈和释放栈，结合代码还原内存对象生命周期。

### 案例分析

**案例一**：堆内存释放后直接访问

**问题现象**

应用运行过程中触发GWP-ASan检测，检测到堆内存释放后访问应用闪退。

**问题分析**

1. 查看日志内容，确认故障类型。

   证据1：日志中明确给出Use After Free，可确认该问题属于堆内存释放后访问。异常地址0x5afbce5000位于一块1024字节的内存区域起始位置，异常访问、内存释放和内存分配均发生在线程52565。

   ```screen
   Module name:xxx
   Version:1.0.0
   Pid:24914
   Uid:20020211
   Reason:GWP-ASAN
   *** GWP-ASan detected a memory error ***
   Use After Free at 0x5afbce5000 (0 bytes into a 1024-byte allocation at 0x5afbce5000) by thread 52565 here:
   #0 0x5c55449468 (/data/storage/el1/bundle/libs/arm64/libsample.so+0x9468) (BuildId: 827c80263a1368b40c38b440d4d6c5b50bf3e133)
   #1 0x5ad6ae83b0 (/system/lib64/platformsdk/libace_napi.z.so+0x683b0) (BuildId: efc6ef6c37febf0b0a555a447a57f397)
   #2 0x5af239e9e8 (/system/lib64/module/arkcompiler/stub.an+0xe949e8)
   #3 0x5af198fda8 (/system/lib64/module/arkcompiler/stub.an+0x485da8)
   0x5afbce5000 was deallocated by thread 52565 here:
   #0 0x5a4b18e984 (/lib/ld-musl-aarch64.so.1+0x156984) (BuildId: 91116d590983090e9c440b80f23c4b2b)
   #1 0x5a4b186cb0 (/lib/ld-musl-aarch64.so.1+0x14ecb0) (BuildId: 91116d590983090e9c440b80f23c4b2b)
   #2 0x5c5544944c (/data/storage/el1/bundle/libs/arm64/libsample.so+0x944c) (BuildId: 827c80263a1368b40c38b440d4d6c5b50bf3e133)
   #3 0x5ad6ae83b0 (/system/lib64/platformsdk/libace_napi.z.so+0x683b0) (BuildId: efc6ef6c37febf0b0a555a447a57f397)
   #4 0x5af239e9e8 (/system/lib64/module/arkcompiler/stub.an+0xe949e8)
   #5 0x5af198fda8 (/system/lib64/module/arkcompiler/stub.an+0x485da8)
   0x5afbce5000 was allocated by thread 52565 here:
   #0 0x5a4b18e984 (/lib/ld-musl-aarch64.so.1+0x156984) (BuildId: 91116d590983090e9c440b80f23c4b2b)
   #1 0x5a4b186980 (/lib/ld-musl-aarch64.so.1+0x14e980) (BuildId: 91116d590983090e9c440b80f23c4b2b)
   #2 0x5a4b1a9668 (/lib/ld-musl-aarch64.so.1+0x171668) (BuildId: 91116d590983090e9c440b80f23c4b2b)
   #3 0x5a4b2333c8 (/lib/ld-musl-aarch64.so.1+0x1fb3c8) (BuildId: 91116d590983090e9c440b80f23c4b2b)
   #4 0x5c554493e8 (/data/storage/el1/bundle/libs/arm64/libsample.so+0x93e8) (BuildId: 827c80263a1368b40c38b440d4d6c5b50bf3e133)
   #5 0x5ad6ae83b0 (/system/lib64/platformsdk/libace_napi.z.so+0x683b0) (BuildId: efc6ef6c37febf0b0a555a447a57f397)
   #6 0x5af239e9e8 (/system/lib64/module/arkcompiler/stub.an+0xe949e8)
   #7 0x5af198fda8 (/system/lib64/module/arkcompiler/stub.an+0x485da8)
   * End GWP-ASan report *
   ```
2. 分析报错栈、释放栈和分配栈，定位对应的业务代码。

   通过llvm-addr2line（参考：[C++堆栈解析流程](../harmonyos-guides/ide-exception-stack-parsing-principle.md#section1735713501344)中对于llvm-addr2line的使用）等解析工具，定位到具体业务代码行，如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/_-bcGm8PTaSSQveKXBcQQA/zh-cn_image_0000002729491383.png "点击放大")

   1号位置对应分配栈，通过malloc(1024)申请1024字节堆内存；2号位置对应释放栈，通过free(ptr)释放该内存；3号位置对应报错栈，通过ptr[0] = 1再次访问已经释放的内存。
3. 还原内存对象生命周期，确认问题根因。

   根据解析出的栈可以确认，初始化ptr时malloc了一个1024字节的内存并交由ptr指针管理，随后调用free释放了该内存。但是，在内存释放后，业务代码又通过ptr指针访问了该已释放的内存空间，从而触发了GWP-ASan的Use After Free异常。

**问题结论与总结**

该问题的根本原因是：函数GwpAsanTestUseAfterFree()中，ptr指向的堆内存释放后，程序仍通过ptr访问该内存。由于内存生命周期管理不当，最终发生堆内存释放后访问。

**案例二**：异步回调中访问已经释放的堆内存对象

**问题现象**

应用运行过程中触发GWP-ASan检测，检测到堆内存释放后访问应用闪退。

**问题分析**

1. 查看日志内容，确认故障类型。

   证据1：日志中明确给出Use After Free，可确认该问题属于堆内存释放后访问。日志显示异常地址0x5ab7f93fc0位于一块50字节的堆内存区域起始位置，内存分配、释放和异常访问均发生在线程34817。

   ```screen
   Module name:com.example.myapplication
   Version:1.0.0
   Pid:34817
   Uid:20020212
   Reason:GWP-ASAN
   *** GWP-ASan detected a memory error ***
   Use After Free at 0x5ab7f93fc0 (0 bytes into a 50-byte allocation at 0x5ab7f93fc0) by thread 34817 here:
    #0 0x5aba3e39bc  (/data/storage/el1/bundle/libs/arm64/libentry.so+0xa39bc) (BuildId: 106e8994db1f366b03c66ab2356cc206aea70c15)
    #1 0x5a974dbd10  (/system/lib64/platformsdk/libuv.so+0x1bd10) (BuildId: 736f600fc1ccf9b9d3388de5ff19abd1)
    #2 0x5a974f1d70  (/system/lib64/platformsdk/libuv.so+0x31d70) (BuildId: 736f600fc1ccf9b9d3388de5ff19abd1)
    #3 0x5a974dce68  (/system/lib64/platformsdk/libuv.so+0x1ce68) (BuildId: 736f600fc1ccf9b9d3388de5ff19abd1)
    #4 0x5a962779e4  (/system/lib64/platformsdk/libruntime.z.so+0x779e4) (BuildId: 6503ae1fa1ed696b6edbe90490f3e1d1)
   0x5ab7f93fc0 was deallocated by thread 34817 here:
    #0 0x5a0945b1c4  (/lib/ld-musl-aarch64.so.1+0x1571c4) (BuildId: 6cb4f500aa5397373710021216afb05c)
    #1 0x5a094534f0  (/lib/ld-musl-aarch64.so.1+0x14f4f0) (BuildId: 6cb4f500aa5397373710021216afb05c)
    #2 0x5aba3e0238  (/data/storage/el1/bundle/libs/arm64/libentry.so+0xa0238) (BuildId: 106e8994db1f366b03c66ab2356cc206aea70c15)
    #3 0x5a90ff010c  (/system/lib64/platformsdk/libace_napi.z.so+0x7010c) (BuildId: 226dc0ffc65e2899a5e810b4acb58e65)
    #4 0x5aaf68c1e8  (/system/lib64/module/arkcompiler/stub.an+0xe8b1e8)
   0x5ab7f93fc0 was allocated by thread 34817 here:
    #0 0x5a0945b1c4  (/lib/ld-musl-aarch64.so.1+0x1571c4) (BuildId: 6cb4f500aa5397373710021216afb05c)
    #1 0x5a094531c0  (/lib/ld-musl-aarch64.so.1+0x14f1c0) (BuildId: 6cb4f500aa5397373710021216afb05c)
    #2 0x5a094765c0  (/lib/ld-musl-aarch64.so.1+0x1725c0) (BuildId: 6cb4f500aa5397373710021216afb05c)
    #3 0x5a0950102c  (/lib/ld-musl-aarch64.so.1+0x1fd02c) (BuildId: 6cb4f500aa5397373710021216afb05c)
    #4 0x5aba272648  (/data/storage/el1/bundle/libs/arm64/libc++_shared.so+0xb2648) (BuildId: d2aeda5d2b106eca7953ec5f8909f164a1df0abb)
    #5 0x5aba3e016c  (/data/storage/el1/bundle/libs/arm64/libentry.so+0xa016c) (BuildId: 106e8994db1f366b03c66ab2356cc206aea70c15)
    #6 0x5a90ff010c  (/system/lib64/platformsdk/libace_napi.z.so+0x7010c) (BuildId: 226dc0ffc65e2899a5e810b4acb58e65)
    #7 0x5aaf68c1e8  (/system/lib64/module/arkcompiler/stub.an+0xe8b1e8)
   *** End GWP-ASan report ***
   ```
2. 分析报错栈、释放栈和分配栈，定位对应的业务代码。

   通过llvm-addr2line（参考：[C++堆栈解析流程](../harmonyos-guides/ide-exception-stack-parsing-principle.md#section1735713501344)中对于llvm-addr2line的使用）等解析工具，定位到具体业务代码行，如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/77/v3/dKjWNDXRQnal6vj-S6P62Q/zh-cn_image_0000002699892010.png "点击放大")

   1号位置通过new char[UAF\_ALLOC\_SIZE]申请50字节堆内存，2号位置提交异步任务，3号位置通过delete[]释放堆内存，4号位置对应报错栈，在异步回调中通过ctx->freed\_ptrs[i][0] = 42再次访问已经释放的内存。
3. 分析报错栈、释放栈、分配栈，还原内存对象生命周期，确认问题根因。

   程序首先为ctx->freed\_ptrs[i]申请50字节堆内存，并将相关上下文保存到async->data中。随后通过uv\_async\_send()提交异步任务，但主流程未等待异步回调执行完成，继续通过delete[] ctx->freed\_ptrs[i]释放这些内存。本案例中，异步回调在内存释放后才执行，随后通过ctx->freed\_ptrs[i][0] = 42继续访问已经释放的内存，最终触发GWP-ASan的Use After Free异常。

**问题结论与总结**

该问题的根本原因是：InjectHeapUseAfterFree()提交异步任务后提前释放了ctx->freed\_ptrs指向的堆内存，但异步回调执行时仍继续访问这些已释放的内存。由于异步任务执行周期与堆内存生命周期管理不当，最终发生堆内存释放后访问。

**修复建议**

此类问题常见修复方案如下：

1. 使用智能指针管理生命周期。

2. 实现一个delete析构器来保证指针的重置。

3. 访问前判断对象是否有效。

4. 多线程访问加锁或引用计数保护。

## HWASan局部变量在代码块返回后被访问

### 根因描述

局部变量在代码块返回后被访问，属于内存释放后访问的一种细分场景。此类问题本质上是：程序在代码块内定义一个局部变量，将其地址保存在代码块外的对象中，在退出该代码块后，对保存的地址进行解引用，导致非法访问。当应用[开启HWASan](../harmonyos-guides/ide-hwasan.md#section38898177587)检测能力后，运行时会对指针和内存标签进行校验。一旦检测到程序通过失效指针访问生命周期已经结束的栈对象，HWASan会报告stack tag-mismatch异常。

### 问题分析思路

此类问题通常有以下几种可能：

1. 将代码块内对象的地址赋值给函数内地址对象，在代码块返回后，对保存的地址解引用。

2. 将代码块内对象的地址赋值给全局地址对象，在代码块返回后，对保存的地址解引用。

3. 将代码块内对象的地址赋值给堆中的地址对象，在代码块返回后，对保存的地址解引用。

**说明** 

当前集成的Clang版本为15.0，默认未开启检测局部变量在代码块返回后被访问类型异常。

本章节案例需要在应用的CMakeLists.txt中增加定义-mllvm -hwasan-use-after-scope，参考：

set(CMAKE\_CXX\_FLAGS "${CMAKE\_CXX\_FLAGS} -g -fno-omit-frame-pointer -mllvm -hwasan-use-after-scope")

set(CMAKE\_C\_FLAGS "${CMAKE\_C\_FLAGS} -g -fno-omit-frame-pointer -mllvm -hwasan-use-after-scope")

问题分析步骤如下：

1. 查看HWASan故障日志，确认故障类型。重点关注是否包含关键字stack tag-mismatch，若存在则可确认属于局部变量在代码块返回后被访问。
2. 分析报错栈，确认触发异常位置，并通过llvm-addr2line（参考：[C++堆栈解析流程](../harmonyos-guides/ide-exception-stack-parsing-principle.md#section1735713501344)中对于llvm-addr2line的使用）等解析工具，定位到具体代码行。
3. 分析分配栈，确认异常访问对象，并通过llvm-addr2line（参考：[C++堆栈解析流程](../harmonyos-guides/ide-exception-stack-parsing-principle.md#section1735713501344)中对于llvm-addr2line的使用）等解析工具，定位到被异常访问对象的定义函数。
4. 结合触发异常位置和异常访问对象，分析控制流路径。

### 关键字

此类问题通常可通过stack tag-mismatch确认故障类型。优先分析业务侧调用栈帧代码。

### 案例分析

**案例一**：局部栈地址逃逸至函数作用域指针

**问题现象**

应用运行过程中触发HWASan检测，应用闪退并生成HWASan故障日志。

**问题分析**

1. 查看日志内容，确认故障类型。

   证据1：根据字段Reason:stack tag-mismatch和字段ERROR: HWAddressSanitizer: tag-mismatch，可以确认是局部变量在代码块/函数返回后被访问。

   ```screen
   Module name:com.example.dfx_test
   Version:1.0.1
   Pid:16130
   Uid:20020216
   Reason:stack tag-mismatch
   ==appspawn==16130==ERROR: HWAddressSanitizer: tag-mismatch on address 0x007f8600d250 at pc 0x005abe7302a0
   READ of size 4 at 0x007f8600d250 tags: 8b/00 (ptr/mem) in thread 16130
       #0 0x5abe7302a0  (/data/storage/el1/bundle/libs/arm64/libentry.so+0x2f02a0) (BuildId: ba730004c176bffdb10c8e510527cb70c544f362)
       #1 0x5a983a7c90  (/system/lib64/platformsdk/libace_napi.z.so+0x67c90) (BuildId: 76bc1ed675edcc5f429a976d6c9b955d)
    
   Cause: stack tag-mismatch
   Address 0x007f8600d250 is located in stack of thread 16130
   Thread: T0 0x005b00002000 stack: [0x007f8581b000,0x007f8601a000) sz: 8384512 tls: [0x0059eabc8370,0x0059eabc8a6b) rb:(1698890/10230000) records(1698890/o:0) tid: 16130
   Previously allocated frames:
     record_addr:0x5a95cbc458 record:0xd3f005abe7301d0  (/data/storage/el1/bundle/libs/arm64/libentry.so+0x2f01d0) (BuildId: ba730004c176bffdb10c8e510527cb70c544f362)
     record_addr:0x5a95cbc450 record:0x151b005abe53c340  (/data/storage/el1/bundle/libs/arm64/libentry.so+0xfc340) (BuildId: ba730004c176bffdb10c8e510527cb70c544f362)
   ```
2. 分析报错栈，定位到具体业务代码行。

   通过llvm-addr2line工具（参考：[C++堆栈解析流程](../harmonyos-guides/ide-exception-stack-parsing-principle.md#section1735713501344)中对于llvm-addr2line的使用）、DevEco Studio自带的堆栈跟踪分析等类似工具，完成调用栈#0的符号解析，定位到具体业务代码行如下：

   ```screen
   ==appspawn==16130==ERROR: HWAddressSanitizer: tag-mismatch on address 0x007f8600d250 at pc 0x005abe7302a0
   READ of size 4 at 0x007f8600d250 tags: 8b/00 (ptr/mem) in thread 16130
       #0 TriggerStackUseAfterScope(napi_env__*, napi_callback_info__*) at (G:/2D-DFXDemo-master/2D-DFXDemo-master/dfx_test/entry/src/main/cpp/common/xsan/XsanTest.cpp:163)
       #1 0x5a983a7c90  (/system/lib64/platformsdk/libace_napi.z.so+0x67c90) (BuildId: 76bc1ed675edcc5f429a976d6c9b955d)
   ```

   解析结果表明，XsanTest.cpp:163行代码触发访问异常。
3. 分析分配栈，确认异常访问对象。

   在分析HWASan栈变量异常访问时，可结合Previously allocated frames中的开栈历史定位异常地址所属的函数栈帧。关键日志如下：

   ```screen
   Cause: stack tag-mismatch
   Address 0x007f8600d250 is located in stack of thread 16130
   Thread: T0 0x005b00002000 stack: [0x007f8581b000,0x007f8601a000) sz: 8384512 tls: [0x0059eabc8370,0x0059eabc8a6b) rb:(1698890/10230000) records(1698890/o:0) tid: 16130
   Previously allocated frames:
     record_addr:0x5a95cbc458 record:0x0d3f005abe7301d0  (TriggerStackUseAfterScope(napi_env__*, napi_callback_info__*) at (G:/2D-DFXDemo-master/2D-DFXDemo-master/dfx_test/entry/src/main/cpp/common/xsan/XsanTest.cpp:153))
     record_addr:0x5a95cbc450 record:0x151b005abe53c340  (Init(napi_env__*, napi_value__*) at (G:/2D-DFXDemo-master/2D-DFXDemo-master/dfx_test/entry/src/main/cpp/napi_init.cpp:8038))
   ```

   本案例中，首先截取报错地址0x007f8600d250的后5位，得到栈内相对偏移0x0d250；随后在Previously allocated frames列表中自上而下比较各record中的高5位栈指针偏移，找到第一个大于目标偏移的记录。本案例匹配到0x0d3f0，对应record:0x0d3f005abe7301d0。解析该record对应的函数符号后，定位到TriggerStackUseAfterScope()，说明异常的栈对象在该函数中定义。
4. 分析控制流路径，如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fa/v3/IGXn2W3iT0Spbm7p6gaL5g/zh-cn_image_0000002729611337.png "点击放大")

   1. 定义函数内局部指针ptr。
   2. 在代码块中，定义局部数组local。
   3. 在代码块中，将局部数组local的0号元素的地址赋值给指针对象ptr。
   4. 离开代码块后，local对象生命周期结束，ptr仍保存原地址。此时继续通过ptr解引用访问原local对象的内存，最终触发异常。

**问题结论与总结**

该问题的根本原因是：TriggerStackUseAfterScope()将代码块内局部数组local的地址保存到ptr中。在local离开作用域后，该变量的生命周期结束，但程序仍继续通过ptr访问原地址，最终触发局部变量在代码块返回后被访问异常。

**案例二**：局部栈地址逃逸至全局指针

**问题现象**

应用运行过程中触发HWASan检测，应用闪退并生成HWASan故障日志。

**问题分析**

1. 查看日志内容，确认故障类型。

   证据1：根据字段Reason:stack tag-mismatch和字段ERROR: HWAddressSanitizer: tag-mismatch，可以确认是局部变量在代码块/函数返回后被访问。

   ```screen
   Module name:com.example.myapplication
   Version:1.0.0
   Pid:17842
   Uid:20020212
   Reason:stack tag-mismatch
   ==appspawn==17842==ERROR: HWAddressSanitizer: tag-mismatch on address 0x007e91bf5c74 at pc 0x005ae14f67ec
   READ of size 4 at 0x007e91bf5c74 tags: 7c/00 (ptr/mem) in thread 17842
       #0 0x5ae14f67ec  (/data/storage/el1/bundle/libs/arm64/libentry.so+0xb67ec) (BuildId: 7227991c2d807faa9d3b6cc9fb12e36c33809a79)
       #1 0x5ae14f8448  (/data/storage/el1/bundle/libs/arm64/libentry.so+0xb8448) (BuildId: 7227991c2d807faa9d3b6cc9fb12e36c33809a79)
       #2 0x5ac617010c  (/system/lib64/platformsdk/libace_napi.z.so+0x7010c) (BuildId: 226dc0ffc65e2899a5e810b4acb58e65)

   Cause: stack tag-mismatch
   Address 0x007e91bf5c74 is located in stack of thread 17842
   Thread: T0 0x005b00002000 stack: [0x007e91404000,0x007e91c03000) sz: 8384512 tls: [0x005a37c2a8f0,0x005a37c2afeb) rb:(102300/102300/102300) records(1361309/o:0) tid: 17842
   Previously allocated frames:
     record_addr:0x5abd2f43e0 record:0xf5ca005ae14f6728  (/data/storage/el1/bundle/libs/arm64/libentry.so+0xb6728) (BuildId: 7227991c2d807faa9d3b6cc9fb12e36c33809a79)
     record_addr:0x5abd2f43d8 record:0x2c005ae14f6c18  (/data/storage/el1/bundle/libs/arm64/libentry.so+0xb6c18) (BuildId: 7227991c2d807faa9d3b6cc9fb12e36c33809a79)
     record_addr:0x5abd2f43d0 record:0xfdf3005ae14f6a98  (/data/storage/el1/bundle/libs/arm64/libentry.so+0xb6a98) (BuildId: 7227991c2d807faa9d3b6cc9fb12e36c33809a79)
   Searched 110585 records, find 0 with same addr 0x007e91bf5c74
   ```
2. 分析报错栈，定位到具体业务代码行。

   通过llvm-addr2line工具（参考：[C++堆栈解析流程](../harmonyos-guides/ide-exception-stack-parsing-principle.md#section1735713501344)中对于llvm-addr2line的使用）、DevEco Studio自带的堆栈跟踪分析等类似工具，完成调用栈#0的符号解析，定位到具体业务代码行：

   ```screen
   ==appspawn==17842==ERROR: HWAddressSanitizer: tag-mismatch on address 0x007e91bf5c74 at pc 0x005ae14f67ec
   READ of size 4 at 0x007e91bf5c74 tags: 7c/00 (ptr/mem) in thread 17842
       #0 stackUseAfterScope() at (C:/Users/Desktop/C/entry/src/main/cpp/napi_init.cpp:383)
       #1 InjectStackUseAfterScope(napi_env__*, napi_callback_info__*) at (C:/Users/Desktop/C/entry/src/main/cpp/napi_init.cpp:387)
       #2 0x5ac617010c  (/system/lib64/platformsdk/libace_napi.z.so+0x7010c) (BuildId: 226dc0ffc65e2899a5e810b4acb58e65)
   ```

   解析结果表明，napi\_init.cpp:383行代码触发异常。
3. 分析分配栈，确认异常访问对象。

   按照案例一中的开栈记录分析方法，本案例匹配到业务地址libentry.so+0xb6728。通过llvm-addr2line解析：

   ```screen
   llvm-addr2line -Cfpie libentry.so 0xb6728
   stackUseAfterScope() at .../entry/src/main/cpp/napi_init.cpp:378
   ```

   解析结果定位到napi\_init.cpp:378，对应stackUseAfterScope()函数的开栈位置，说明异常的栈对象在该函数中定义。
4. 分析控制流路径，如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5c/v3/s9GlK47nRMOMs6weMcgSbg/zh-cn_image_0000002699732128.png "点击放大")

   1. 定义全局指针gp。
   2. 在代码块中，定义局部数组x。
   3. 在代码块中，将局部数组1号元素的地址赋值给指针对象gp。
   4. 离开代码块后，x对象生命周期结束，但gp仍保存原地址。在代码块外继续通过gp访问原x对象的内存，最终触发异常。

**问题结论与总结**

该问题的根本原因是：stackUseAfterScope()将代码块内局部数组x的地址保存到全局指针gp中。在离开代码块后，x对象生命周期结束，但程序仍继续通过gp访问x，最终触发局部变量在代码块返回后被访问异常。

**案例三**：局部栈地址逃逸至堆内存指针

**问题现象**

应用运行过程中触发HWASan检测，应用闪退并生成HWASan故障日志。

**问题分析**

1. 查看日志内容，确认故障类型。

   证据1：根据字段Reason:stack tag-mismatch和字段ERROR: HWAddressSanitizer: tag-mismatch，可以确认是局部变量在代码块/函数返回后被访问。

   ```screen
   Module name:com.example.myapplication
   Version:1.0.0
   Pid:13787
   Uid:20020212
   Reason:stack tag-mismatch
   ==appspawn==13787==ERROR: HWAddressSanitizer: tag-mismatch on address 0x007e979e7c74 at pc 0x005a9a8f6804
   READ of size 4 at 0x007e979e7c74 tags: 65/00 (ptr/mem) in thread 13787
       #0 0x5a9a8f6804  (/data/storage/el1/bundle/libs/arm64/libentry.so+0xb6804) (BuildId: 8d87f2817f6214700df8eaa59edf0b36b4bd3bcf)
       #1 0x5a9a8f8460  (/data/storage/el1/bundle/libs/arm64/libentry.so+0xb8460) (BuildId: 8d87f2817f6214700df8eaa59edf0b36b4bd3bcf)
       #2 0x5a802b010c  (/system/lib64/platformsdk/libace_napi.z.so+0x7010c) (BuildId: 226dc0ffc65e2899a5e810b4acb58e65)

   Cause: stack tag-mismatch
   Address 0x007e979e7c74 is located in stack of thread 13787
   Thread: T0 0x005b00002000 stack: [0x007e971f6000,0x007e979f5000) sz: 8384512 tls: [0x0059f108f8f0,0x0059f108ffeb) rb:(102300/102300/102300) records(1385661/o:0) tid: 13787
   Previously allocated frames:
     record_addr:0x5a76579b28 record:0xe7ca005a9a8f6728  (/data/storage/el1/bundle/libs/arm64/libentry.so+0xb6728) (BuildId: 8d87f2817f6214700df8eaa59edf0b36b4bd3bcf)
     record_addr:0x5a76579b20 record:0xf18d005a9a8ff9cc  (/data/storage/el1/bundle/libs/arm64/libentry.so+0xbf9cc) (BuildId: 8d87f2817f6214700df8eaa59edf0b36b4bd3bcf)
   ```
2. 分析报错栈，定位到具体业务代码行。

   通过llvm-addr2line工具（参考：[C++堆栈解析流程](../harmonyos-guides/ide-exception-stack-parsing-principle.md#section1735713501344)中对于llvm-addr2line的使用）、DevEco Studio自带的堆栈跟踪分析等类似工具，完成调用栈#0的符号解析，定位到具体业务代码行：

   ```screen
   ==appspawn==13787==ERROR: HWAddressSanitizer: tag-mismatch on address 0x007e979e7c74 at pc 0x005a9a8f6804
   READ of size 4 at 0x007e979e7c74 tags: 65/00 (ptr/mem) in thread 13787
       #0 stackUseAfterScope() at (C:/Users/Desktop/C/entry/src/main/cpp/napi_init.cpp:384)
       #1 InjectStackUseAfterScope(napi_env__*, napi_callback_info__*) at (C:/Users/Desktop/C/entry/src/main/cpp/napi_init.cpp:389)
       #2 0x5a802b010c  (/system/lib64/platformsdk/libace_napi.z.so+0x7010c) (BuildId: 226dc0ffc65e2899a5e810b4acb58e65)
   ```

   解析结果表明，napi\_init.cpp:384行代码触发异常。
3. 分析分配栈，确认异常访问对象。

   按照案例一中的开栈记录分析方法，本案例匹配到业务地址libentry.so+0xb6728。通过llvm-addr2line解析：

   ```screen
   llvm-addr2line -Cfpie libentry.so 0xb6728
   stackUseAfterScope() at .../entry/src/main/cpp/napi_init.cpp:378
   ```

   解析结果定位到napi\_init.cpp:378，对应stackUseAfterScope()函数的开栈位置，说明异常的栈对象在该函数中定义。
4. 分析控制流路径，如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3/v3/RcUx04UsSTSILTm9hR-8TA/zh-cn_image_0000002729491385.png "点击放大")

   1. 定义指针heapP，并通过new int[100]申请堆内存。
   2. 在代码块中，定义局部数组x。
   3. 将局部数组x的偏移地址赋值给heapP，此时heapP转而指向栈对象x。
   4. 离开代码块后，x对象生命周期结束，但heapP仍保存原x对象的地址。在代码块外继续通过heapP访问该地址，最终触发异常。

**问题结论与总结**

该问题的根本原因是：stackUseAfterScope()将代码块内局部数组x的地址赋值给heapP。在离开代码块后，x对象生命周期结束，程序仍继续通过heapP访问x，最终触发局部变量在代码块返回后被访问异常。

**修复建议**

此类问题的修复原则是保证指针的使用范围不超过其指向对象的生命周期。建议避免将局部对象地址保存到作用域外继续使用；若后续流程仅需要对象中的数据，可在局部对象生命周期结束前将数据复制到生命周期更长的对象中；若后续仍需要通过地址访问对象，应调整对象的存储位置和生命周期，确保对象在整个访问期间始终有效。

## ASan局部变量在代码块返回后被访问

### 根因描述

局部变量在代码块返回后被访问，属于内存释放后访问的一种细分场景。此类问题本质上是：程序在代码块内定义一个局部变量，将其地址保存在代码块外的对象中，在退出该代码块后，对保存的地址进行解引用，导致非法访问。当应用[开启ASan](../harmonyos-guides/ide-asan.md#section111599216114)检测能力后，ASan会通过Shadow Memory记录栈内存的可访问状态。当局部对象生命周期结束后，ASan会将对应内存区域标记为不可访问状态。一旦程序继续访问该区域，ASan会报告stack-use-after-scope异常。

### 问题分析思路

此类问题的常见原因和[HWASan局部变量在代码块返回后被访问](bpta-stability-memory-uaf-fault-mode.md#section96190175307)一致，不再赘述。对于ASan，问题分析步骤如下：

1. 查看ASan故障日志，确认故障类型。重点关注是否包含关键字stack-use-after-scope，若存在则可确认属于局部变量在代码块返回后被访问。
2. 分析报错栈，确认触发异常位置，并通过llvm-addr2line（参考：[C++堆栈解析流程](../harmonyos-guides/ide-exception-stack-parsing-principle.md#section1735713501344)中对于llvm-addr2line的使用）等解析工具，定位到具体代码行。
3. 分析分配栈，确认异常访问对象，并通过llvm-addr2line（参考：[C++堆栈解析流程](../harmonyos-guides/ide-exception-stack-parsing-principle.md#section1735713501344)中对于llvm-addr2line的使用）等解析工具，定位到被异常访问对象的定义代码行。
4. 结合触发异常位置和异常访问对象，分析控制流路径。

### 关键字

此类问题通常可通过stack-use-after-scope确认故障类型。优先分析业务侧调用栈帧代码。

### 案例分析

**案例一**：局部栈地址逃逸至函数作用域指针

**问题现象**

应用运行过程中触发ASan检测，应用闪退并生成ASan故障日志。

**问题分析**

1. 查看日志内容，确认故障类型。

   证据1：根据字段Reason:stack-use-after-scope和ERROR: AddressSanitizer: stack-use-after-scope，可以确认该问题属于局部变量在代码块返回后被访问。

   ```screen
   Module name:com.example.dfx_test
   Version:1.0.1
   Pid:8891
   Uid:20020216
   Reason:stack-use-after-scope
   ==appspawn==8891==AddressSanitizer: WARNING: unexpected format specifier in printf interceptor: %{ (reported once per process)
   =================================================================
   ==appspawn==8891==ERROR: AddressSanitizer: stack-use-after-scope on address 0x007eb11c5140 at pc 0x007bb094730c bp 0x007eb11c5110 sp 0x007eb11c5108
   READ of size 4 at 0x007eb11c5140 thread T0 (xample.dfx_test)
   #0 0x7bb0947308  (/data/storage/el1/bundle/libs/arm64/libentry.so+0x3c7308) (BuildId: 1aedcc153af985e5f50c68ceb079a93278e4cff6)
   #1 0x7a89327c90  (/system/lib64/platformsdk/libace_napi.z.so+0x67c90) (BuildId: 76bc1ed675edcc5f429a976d6c9b955d)
   #2 0x7eb39029f4  (/system/lib64/module/arkcompiler/stub.an+0xe179f4)
   #3 0x7eb2f56900  (/system/lib64/module/arkcompiler/stub.an+0x46b900)

   Address 0x007eb11c5140 is located in stack of thread T0 (xample.dfx_test) at offset 32 in frame
   #0 0x7bb09470d4  (/data/storage/el1/bundle/libs/arm64/libentry.so+0x3c70d4) (BuildId: 1aedcc153af985e5f50c68ceb079a93278e4cff6)

   This frame has 2 object(s):
   [32, 432) 'local' (line 157) <== Memory access at offset 32 is inside this variable
   [496, 504) 'resultValue' (line 165)
   SUMMARY: AddressSanitizer: stack-use-after-scope (/data/storage/el1/bundle/libs/arm64/libentry.so+0x558a4) (BuildId: 0d123cf983620aabe17337ef99fa0f85e9107521)
   ```
2. 分析报错栈，确认触发异常位置。

   通过llvm-addr2line（参考：[C++堆栈解析流程](../harmonyos-guides/ide-exception-stack-parsing-principle.md#section1735713501344)中对于llvm-addr2line的使用）、DevEco Studio自带的堆栈跟踪分析等类似工具，完成调用栈#0的符号解析，定位到具体业务代码行：

   ```screen
   ==appspawn==8891==ERROR: AddressSanitizer: stack-use-after-scope on address 0x007eb11c5140 at pc 0x007bb094730c bp 0x007eb11c5110 sp 0x007eb11c5108
   READ of size 4 at 0x007eb11c5140 thread T0 (xample.dfx_test)
   #0 TriggerStackUseAfterScope(napi_env__*, napi_callback_info__*) at (G:/2D-DFXDemo-master/2D-DFXDemo-master/dfx_test/entry/src/main/cpp/common/xsan/XsanTest.cpp:162)
   #1 0x7a89327c90  (/system/lib64/platformsdk/libace_napi.z.so+0x67c90) (BuildId: 76bc1ed675edcc5f429a976d6c9b955d)
   #2 0x7eb39029f4  (/system/lib64/module/arkcompiler/stub.an+0xe179f4)
   #3 0x7eb2f56900  (/system/lib64/module/arkcompiler/stub.an+0x46b900)
   ```

   解析结果表明，XsanTest.cpp:162行代码触发异常访问。
3. 分析分配栈，确认异常访问对象。

   ```screen
   Address 0x007eb11c5140 is located in stack of thread T0 (xample.dfx_test) at offset 32 in frame
   #0 TriggerStackUseAfterScope(napi_env__*, napi_callback_info__*) at (G:/2D-DFXDemo-master/2D-DFXDemo-master/dfx_test/entry/src/main/cpp/common/xsan/XsanTest.cpp:152)

   This frame has 2 object(s):
   [32, 432) 'local' (line 157) <== Memory access at offset 32 is inside this variable
   [496, 504) 'resultValue' (line 165)
   ```

   日志显示异常地址位于当前函数栈帧偏移32的位置，该位置对应局部数组local，其定义位置为XsanTest.cpp:157。由此可以确认本次异常访问的对象为local。
4. 分析控制流路径，如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/15/v3/PNVtB4cwRKWYVQhas6-OHg/zh-cn_image_0000002699892012.png "点击放大")

   1. 定义函数内局部指针对象ptr。
   2. 在代码块中定义局部数组local。
   3. 在代码块中，将local的0号元素地址赋值给ptr。
   4. 离开代码块后，local生命周期结束，但ptr仍保存原地址。程序继续通过ptr访问原local对象的内存，最终触发异常。

**问题结论与总结**

TriggerStackUseAfterScope()将代码块内局部数组local的地址保存到函数内指针ptr中。在local生命周期结束后，程序仍继续通过ptr访问原地址，最终触发stack-use-after-scope异常。

**修复建议**

此类问题的修复原则是保证指针的使用范围不超过其指向对象的生命周期。避免将局部对象的地址保存到作用域外继续使用；若后续仅需要对象中的数据，可在局部对象生命周期结束前将数据复制到生命周期更长的对象中；若需要继续通过地址访问对象，应调整对象的存储位置和生命周期，确保对象在整个访问期间始终有效。

## HWASan局部变量在函数返回后被访问

### 根因描述

局部变量在函数返回后被访问，属于释放后访问的一种细分场景。此类问题本质上是：程序在函数内定义一个局部变量，将其地址保存在函数外的对象中，在退出该函数后，对保存的地址进行解引用，导致局部变量在函数返回后被访问。当应用[开启HWASan](../harmonyos-guides/ide-hwasan.md#section38898177587)检测能力后，运行时会对指针和内存标签进行校验。一旦检测到程序通过失效指针访问生命周期已经结束的局部栈对象，HWASan会报告stack tag-mismatch异常。

### 问题分析思路

此类问题通常有以下几种可能：

1. 将函数内对象的地址赋值给全局地址对象，在函数返回后，对保存的地址解引用。

2. 将函数内对象的地址赋值给堆中的地址对象，在函数返回后，对保存的地址解引用。

问题分析步骤如下：

1. 查看HWASan故障日志，确认故障类型。重点关注是否包含stack tag-mismatch，若存在则可确认属于局部变量在函数返回后被访问。
2. 分析报错栈，确认触发异常位置，并通过llvm-addr2line（参考：[C++堆栈解析流程](../harmonyos-guides/ide-exception-stack-parsing-principle.md#section1735713501344)中对于llvm-addr2line的使用）等解析工具，定位到具体代码行。
3. 分析分配栈，确认异常访问对象，并通过llvm-addr2line（参考：[C++堆栈解析流程](../harmonyos-guides/ide-exception-stack-parsing-principle.md#section1735713501344)中对于llvm-addr2line的使用）等解析工具，定位到被异常访问对象的定义函数。
4. 结合触发异常位置和异常访问对象，分析控制流路径。

### 关键字

此类问题通常可通过stack tag-mismatch确认故障类型。优先分析业务侧调用栈帧代码。

### 案例分析

**案例一**：局部变量地址逃逸至全局指针导致悬空访问

**问题现象**

应用运行过程中触发HWASan检测，应用闪退并生成HWASan故障日志。

**问题分析**

1. 查看日志内容，确认故障类型。

   证据1：根据字段Reason:stack tag-mismatch和字段ERROR: HWAddressSanitizer: tag-mismatch，可以确认是局部变量在代码块/函数返回后被访问。

   ```screen
   Module name:com.example.dfx_test
   Version:1.0.1
   Pid:9344
   Uid:20020216
   Reason:stack tag-mismatch
   ==appspawn==9344==ERROR: HWAddressSanitizer: tag-mismatch on address 0x007fa9b7e350 at pc 0x006439324550
   WRITE of size 1 at 0x007fa9b7e350 tags: 38/00 (ptr/mem) in thread 9344
   #0 0x6439324550  (/data/storage/el1/bundle/libs/arm64/libentry.so+0x2e4550) (BuildId: d6ebc1eaa4f97a70f8594308b76c3aa7daa9af72)
   #1 0x6317227c90  (/system/lib64/platformsdk/libace_napi.z.so+0x67c90) (BuildId: 76bc1ed675edcc5f429a976d6c9b955d)

   Cause: stack tag-mismatch
   Address 0x007fa9b7e350 is located in stack of thread 9344
   Thread: T0 0x005a00002000 stack: [0x007fa938c000,0x007fa9b8b000) sz: 8384512 tls: [0x0059670c4370,0x0059670c4a6b) rb:(1707495/10230000) records(1707495/o:0) tid: 9344
   Previously allocated frames:
   record_addr:0x59feb689c0 record:0x7e37006439324400  (/data/storage/el1/bundle/libs/arm64/libentry.so+0x2e4400) (BuildId: d6ebc1eaa4f97a70f8594308b76c3aa7daa9af72)
   record_addr:0x59feb689b8 record:0x7e3f0064393244c0  (/data/storage/el1/bundle/libs/arm64/libentry.so+0x2e44c0) (BuildId: d6ebc1eaa4f97a70f8594308b76c3aa7daa9af72)
   record_addr:0x59feb689b0 record:0x861b00643913bbac  (/data/storage/el1/bundle/libs/arm64/libentry.so+0xfbbac) (BuildId: d6ebc1eaa4f97a70f8594308b76c3aa7daa9af72)
   ```
2. 分析报错栈，确认触发异常位置。

   通过llvm-addr2line工具（参考：[C++堆栈解析流程](../harmonyos-guides/ide-exception-stack-parsing-principle.md#section1735713501344)中对于llvm-addr2line的使用）、DevEco Studio自带的堆栈跟踪分析等类似工具，完成调用栈#0的符号解析，定位到具体业务代码行：

   ```screen
   ==appspawn==9344==ERROR: HWAddressSanitizer: tag-mismatch on address 0x007fa9b7e350 at pc 0x006439324550
   WRITE of size 1 at 0x007fa9b7e350 tags: 38/00 (ptr/mem) in thread 9344
   #0 TriggerStackUseAfterReturn(napi_env__*, napi_callback_info__*) at (G:/2D-DFXDemo-master/2D-DFXDemo-master/dfx_test/entry/src/main/cpp/common/xsan/XsanTest.cpp:186)
   #1 0x6317227c90  (/system/lib64/platformsdk/libace_napi.z.so+0x67c90) (BuildId: 76bc1ed675edcc5f429a976d6c9b955d)
   ```

   解析结果表明，异常访问发生在TriggerStackUseAfterReturn()函数的XsanTest.cpp:186行。
3. 分析分配栈，确认异常访问对象。

   ```screen
   Cause: stack tag-mismatch
   Address 0x007fa9b7e350 is located in stack of thread 9344
   Thread: T0 0x005a00002000 stack: [0x007fa938c000,0x007fa9b8b000) sz: 8384512 tls: [0x0059670c4370,0x0059670c4a6b) rb:(1707495/10230000) records(1707495/o:0) tid: 9344
   Previously allocated frames:
   record_addr:0x59feb689c0 record:0x7e37006439324400  (LeafFuncOfTriggerStackUseAfterReturn() at (G:/2D-DFXDemo-master/2D-DFXDemo-master/dfx_test/entry/src/main/cpp/common/xsan/XsanTest.cpp:176))
   record_addr:0x59feb689b8 record:0x7e3f0064393244c0  (TriggerStackUseAfterReturn(napi_env__*, napi_callback_info__*) at (G:/2D-DFXDemo-master/2D-DFXDemo-master/dfx_test/entry/src/main/cpp/common/xsan/XsanTest.cpp:184))
   ```

   说明：踩写的内存地址0x007fa9b7e350，该栈对象在LeafFuncOfTriggerStackUseAfterReturn()中定义。
4. 分析控制流路径，如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/52/v3/A1Pr9DlCQPGgnvzzWX0iZw/zh-cn_image_0000002729611339.png "点击放大")

   1. TriggerStackUseAfterReturn()调用LeafFuncOfTriggerStackUseAfterReturn()。
   2. LeafFuncOfTriggerStackUseAfterReturn()在函数栈中定义局部变量local\_buffer。
   3. 将local\_buffer的地址保存到全局指针g\_ptr中。
   4. LeafFuncOfTriggerStackUseAfterReturn()返回后，local\_buffer生命周期结束，但g\_ptr仍保存原地址。TriggerStackUseAfterReturn()继续通过g\_ptr访问原local\_buffer所在的栈内存，最终触发异常。

**问题结论与总结**

该问题的根本原因是：LeafFuncOfTriggerStackUseAfterReturn()将局部变量local\_buffer的地址保存到全局指针g\_ptr中。函数返回后，local\_buffer生命周期已经结束，但程序仍继续通过g\_ptr访问原地址，最终触发局部变量在函数返回后被访问异常。

**案例二**：局部变量地址逃逸至堆内存指针导致悬空访问

**问题现象**

应用运行过程中触发HWASan检测，应用闪退并生成HWASan故障日志。

**问题分析**

1. 查看日志内容，确认故障类型。

   证据1：根据字段Reason:stack tag-mismatch和字段ERROR: HWAddressSanitizer: tag-mismatch，可以确认是局部变量在代码块/函数返回后被访问。

   ```screen
   Module name:com.example.myapplication
   Version:1.0.0
   Pid:58020
   Uid:20020212
   Reason:stack tag-mismatch
   ==appspawn==58020==ERROR: HWAddressSanitizer: tag-mismatch on address 0x007e82b6aaa4 at pc 0x00640b8b69b4
   READ of size 4 at 0x007e82b6aaa4 tags: 2f/00 (ptr/mem) in thread 58020
       #0 0x640b8b69b4  (/data/storage/el1/bundle/libs/arm64/libentry.so+0xb69b4) (BuildId: 0e5868d2ef93f14bc169442f3d39d4bb4dc7e3b8)
       #1 0x640b8b8618  (/data/storage/el1/bundle/libs/arm64/libentry.so+0xb8618) (BuildId: 0e5868d2ef93f14bc169442f3d39d4bb4dc7e3b8)
       #2 0x59f827010c  (/system/lib64/platformsdk/libace_napi.z.so+0x7010c) (BuildId: 226dc0ffc65e2899a5e810b4acb58e65)

   Cause: stack tag-mismatch
   Address 0x007e82b6aaa4 is located in stack of thread 58020
   Thread: T0 0x005a00002000 stack: [0x007e82379000,0x007e82b78000) sz: 8384512 tls: [0x005966ea98f0,0x005966ea9feb) rb:(102300/102300/102300) records(1330721/o:0) tid: 58020
   Previously allocated frames:
     record_addr:0x59ec538178 record:0x6ac400640b8b682c  (/data/storage/el1/bundle/libs/arm64/libentry.so+0xb682c) (BuildId: 0e5868d2ef93f14bc169442f3d39d4bb4dc7e3b8)
     record_addr:0x59ec538170 record:0x6aca00640b8b692c  (/data/storage/el1/bundle/libs/arm64/libentry.so+0xb692c) (BuildId: 0e5868d2ef93f14bc169442f3d39d4bb4dc7e3b8)
     record_addr:0x59ec538168 record:0x752c00640b8b6f20  (/data/storage/el1/bundle/libs/arm64/libentry.so+0xb6f20) (BuildId: 0e5868d2ef93f14bc169442f3d39d4bb4dc7e3b8)
     record_addr:0x59ec538160 record:0x72f300640b8b6da0  (/data/storage/el1/bundle/libs/arm64/libentry.so+0xb6da0) (BuildId: 0e5868d2ef93f14bc169442f3d39d4bb4dc7e3b8)
   Searched 109570 records, find 0 with same addr 0x007e82b6aaa4
   ```
2. 分析报错栈，定位到具体业务代码行。

   通过llvm-addr2line工具（参考：[C++堆栈解析流程](../harmonyos-guides/ide-exception-stack-parsing-principle.md#section1735713501344)中对于llvm-addr2line的使用）、DevEco Studio自带的堆栈跟踪分析等类似工具，完成调用栈#0的符号解析，定位到具体业务代码行：

   ```screen
   ==appspawn==58020==ERROR: HWAddressSanitizer: tag-mismatch on address 0x007e82b6aaa4 at pc 0x00640b8b69b4
   READ of size 4 at 0x007e82b6aaa4 tags: 2f/00 (ptr/mem) in thread 58020
       #0 StackUseAfterReturn() at (C:/Users/Desktop/C/entry/src/main/cpp/napi_init.cpp:356)
       #1 InjectStackUseAfterReturn(napi_env__*, napi_callback_info__*) at (C:/Users/Desktop/C/entry/src/main/cpp/napi_init.cpp:361)
       #2 0x59f827010c  (/system/lib64/platformsdk/libace_napi.z.so+0x7010c) (BuildId: 226dc0ffc65e2899a5e810b4acb58e65)
   ```

   解析结果表明，异常访问发生在StackUseAfterReturn()函数的napi\_init.cpp:356行。
3. 分析分配栈，确认异常访问对象。

   解析Previously allocated frames中的开栈记录，本案例匹配到业务地址libentry.so+0xb682c。通过llvm-addr2line解析：

   ```screen
   llvm-addr2line -Cfpie libentry.so 0xb682c
   FunctionThatEscapesLocalObject() at .../entry/src/main/cpp/napi_init.cpp:348
   ```

   解析结果定位到FunctionThatEscapesLocalObject()的开栈位置，说明异常的栈对象在该函数中定义。
4. 分析控制流路径，如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c6/v3/BZdNtICgRl2kJ_KtF1nxLQ/zh-cn_image_0000002699732130.png "点击放大")

   1. 在StackUseAfterReturn()中定义局部指针ptr，并通过new int申请堆内存，使ptr初始指向该堆对象。
   2. 调用FunctionThatEscapesLocalObject()并传入ptr的地址，在函数内定义局部数组local。
   3. 将local的1号元素地址赋值给ptr，此时ptr转而指向局部栈对象local。
   4. FunctionThatEscapesLocalObject()返回后，local生命周期结束，但ptr仍保存原地址。随后StackUseAfterReturn()继续通过\*ptr访问原local对象的内存，最终触发异常。

**问题结论与总结**

该问题的根本原因是：FunctionThatEscapesLocalObject()将函数内局部数组local的地址保存到调用方的指针ptr中。函数返回后，local生命周期已经结束，但程序仍继续通过ptr访问原地址，最终触发局部变量在函数返回后被访问异常。

**修复建议**

避免将函数内局部对象的地址保存到函数外，并在函数返回后继续使用。若后续流程仅需要对象中的数据，可在函数返回前将数据复制到生命周期更长的对象中；若确实需要在函数返回后继续通过地址访问该对象，可将对象存储在堆内存中，并明确管理其所有权和释放时机，确保对象生命周期覆盖整个访问过程。
