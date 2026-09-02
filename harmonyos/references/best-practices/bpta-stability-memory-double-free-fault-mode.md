---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-stability-memory-double-free-fault-mode
title: 内存重复释放故障模式说明
breadcrumb: 最佳实践 > 稳定性 > 稳定性分析 > 稳定性故障模式说明 > 地址越界故障模式说明 > 内存重复释放故障模式说明
category: best-practices
scraped_at: 2026-09-02T15:03:23+08:00
doc_updated_at: 2026-08-26
content_hash: sha256:32c52d7fad96071bacabf305ae21bb141a48592256608df6e7bde8d4802439f4
---

同一块堆内存被释放后，若程序再次通过原指针或其他别名指针释放该内存，将导致堆内存重复释放。此类问题可能破坏堆内存管理结构，造成应用立即崩溃或后续在无关位置随机异常，故障现场通常难以追溯。开启地址越界检测能力后，可在重复释放发生时检测异常，并记录内存分配、首次释放和重复释放等调用栈。

本文结合HWASan（Hardware-assisted AddressSanitizer）、ASan（AddressSanitizer）和GWP-ASan（GWP-ASan Will Provide Allocation SANity）典型案例，介绍堆内存重复释放问题的日志特征与定位方法，具体包括：

* [HWASan堆内存重复释放](bpta-stability-memory-double-free-fault-mode.md#section425111116116)
* [ASan堆内存重复释放](bpta-stability-memory-double-free-fault-mode.md#section2804201817410)
* [GWP-ASan堆内存重复释放](bpta-stability-memory-double-free-fault-mode.md#section795141682)

## HWASan堆内存重复释放

### 根因描述

堆内存重复释放，是HWASan use-after-free异常的一种细分模式。指的是同一块通过malloc()/new()/calloc()/realloc()等方式申请的堆内存，在已经释放后再次释放，从而产生堆内存重复释放问题。此类问题本质上是程序对同一块内存的所有权管理混乱。多个路径、多个对象或多个线程都认为自己有权释放该内存。当应用[开启HWASan](../harmonyos-guides/ide-hwasan.md#section38898177587)检测后，HWASan会在内存释放过程中对指针和内存标签进行校验，一旦检测到程序再次释放已经释放的内存对象，应用就会触发invalid-free异常进而退出。

### 问题分析思路

此类问题，通常情况下，会有如下几种可能：

1. 当前上下文释放内存块后，保存地址的指针变量未清空，在后续流程中又触发释放操作。
2. 共享场景下，内存地址在多个地方存储，当前上下文释放内存块后，未同步清空其它地方存储的指针，在其它上下文中重新触发释放操作。

问题分析步骤如下：

1. 查看HWASan日志中的报错关键字段，确认故障类型。重点关注是否为use-after-free且包含ERROR: HWAddressSanitizer: invalid-free。
2. 分析报错栈，确认触发异常位置，并通过llvm-addr2line（参考：[C++堆栈解析流程](../harmonyos-guides/ide-exception-stack-parsing-principle.md#section1735713501344)中对于llvm-addr2line的使用）等解析工具，定位到具体代码行。
3. 分析分配栈和首次释放栈，确认重复释放的内存对象，并通过llvm-addr2line（参考：[C++堆栈解析流程](../harmonyos-guides/ide-exception-stack-parsing-principle.md#section1735713501344)中对于llvm-addr2line的使用）等解析工具，定位到具体代码行。
4. 结合内存分配位置、首次释放位置和异常释放位置，分析堆内存重复释放的控制流路径。

### 关键字

此类问题日志关键词为：use-after-free和ERROR: HWAddressSanitizer: invalid-free。确认是堆内存重复释放后，优先分析业务侧调用栈帧代码。

### 案例分析

**案例一**：指针连续重复释放

**问题现象**

应用运行过程中触发HWASan检测，应用闪退并生成HWASan故障日志。

**问题分析**

1. 查看日志内容，确认故障类型。

   证据1：根据字段Reason:use-after-free和字段ERROR: HWAddressSanitizer: invalid-free，可以确认是堆内存重复释放错误。

   ```screen
   Device info:HUAWEI Pura 90 Pro
   Build info:MLN-AL00 6.1.0.120(SP8C00E120R3P1)
   Fingerprint:9bde5c83036ac7598576c9ebeca297ebd56e9899e7b143b88792579e4e5a5e16
   Timestamp:2026-05-13 21:40:11.951
   Module name:com.example.dfx_test
   Version:1.0.1
   Pid:23641
   Uid:20020216
   Reason:use-after-free
   ==appspawn==23641==ERROR: HWAddressSanitizer: invalid-free on address 0x000400822a80 at pc 0x0067893a3d28 on thread 23641
   tags: cd/94 (ptr/mem)
       #0 0x67893a3d28  (/system/lib64/libclang_rt.hwasan.so+0x23d28) (BuildId: 75d3a57a5341c45a993cce5a48e37c42a9c6157f)
       #1 0x685b024758  (/data/storage/el1/bundle/libs/arm64/libentry.so+0x2e4758) (BuildId: dfeb41cd84e19d2f6d0e1b2c4799953839391478)
       #2 0x68397e7c90  (/system/lib64/platformsdk/libace_napi.z.so+0x67c90) (BuildId: 76bc1ed675edcc5f429a976d6c9b955d)
       #3 0x6856ef29f4  (/system/lib64/module/arkcompiler/stub.an+0xe179f4)
       #4 0x6856546900  (/system/lib64/module/arkcompiler/stub.an+0x46b900)

   [0x000400822a80,0x000400822b00) is a small unallocated heap chunk; size: 128 offset: 0, Allocated By 23641

   Potential Cause: use-after-free
   0x000400822a80 (rb[0] tags:cd) is located 0 bytes inside of 100-byte region [0x000400822a80,0x000400822ae4)
   freed by thread 23641 here:
       #0 0x67893a3d28  (/system/lib64/libclang_rt.hwasan.so+0x23d28) (BuildId: 75d3a57a5341c45a993cce5a48e37c42a9c6157f)
       #1 0x685b024748  (/data/storage/el1/bundle/libs/arm64/libentry.so+0x2e4748) (BuildId: dfeb41cd84e19d2f6d0e1b2c4799953839391478)
       #2 0x68397e7c90  (/system/lib64/platformsdk/libace_napi.z.so+0x67c90) (BuildId: 76bc1ed675edcc5f429a976d6c9b955d)
       #3 0x6856ef29f4  (/system/lib64/module/arkcompiler/stub.an+0xe179f4)
       #4 0x6856546900  (/system/lib64/module/arkcompiler/stub.an+0x46b900)

   previously allocated by thread 23641 here:
       #0 0x67893a44ac  (/system/lib64/libclang_rt.hwasan.so+0x244ac) (BuildId: 75d3a57a5341c45a993cce5a48e37c42a9c6157f)
       #1 0x685b024708  (/data/storage/el1/bundle/libs/arm64/libentry.so+0x2e4708) (BuildId: dfeb41cd84e19d2f6d0e1b2c4799953839391478)
       #2 0x68397e7c90  (/system/lib64/platformsdk/libace_napi.z.so+0x67c90) (BuildId: 76bc1ed675edcc5f429a976d6c9b955d)
       #3 0x6856ef29f4  (/system/lib64/module/arkcompiler/stub.an+0xe179f4)
       #4 0x6856546900  (/system/lib64/module/arkcompiler/stub.an+0x46b900)
   ```
2. 分析报错栈，确认触发异常位置。

   证据2：

   ```screen
   ==appspawn==23641==ERROR: HWAddressSanitizer: invalid-free on address 0x000400822a80 at pc 0x0067893a3d28 on thread 23641
   tags: cd/94 (ptr/mem)
       #0 0x67893a3d28  (/system/lib64/libclang_rt.hwasan.so+0x23d28) (BuildId: 75d3a57a5341c45a993cce5a48e37c42a9c6157f)
       #1 (anonymous namespace)::DoubleFree() at (G:/2D-DFXDemo-master/2D-DFXDemo-master/dfx_test/entry/src/main/cpp/common/xsan/XsanTest.cpp:131)
       #2 0x68397e7c90  (/system/lib64/platformsdk/libace_napi.z.so+0x67c90) (BuildId: 76bc1ed675edcc5f429a976d6c9b955d)
       #3 0x6856ef29f4  (/system/lib64/module/arkcompiler/stub.an+0xe179f4)
       #4 0x6856546900  (/system/lib64/module/arkcompiler/stub.an+0x46b900)
   ```

   通过llvm-addr2line工具（参考：[C++堆栈解析流程](../harmonyos-guides/ide-exception-stack-parsing-principle.md#section1735713501344)中对于llvm-addr2line的使用）、DevEco Studio自带的堆栈跟踪分析等类似工具，对报错栈中的业务栈帧进行符号化，定位到具体源码位置。相关代码如下：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d5/v3/DP_6n8L1T9uvTCoQcKAPLA/zh-cn_image_0000002693765532.png)

   报错栈定位到XsanTest.cpp:131行。结合源码确认，程序调用free(ptr)时触发invalid-free异常。
3. 分析分配栈和首次释放栈，确认重复释放内存对象。

   证据3：

   ```screen
   Potential Cause: use-after-free
   0x000400822a80 (rb[0] tags:cd) is located 0 bytes inside of 100-byte region [0x000400822a80,0x000400822ae4)
   freed by thread 23641 here:
       #0 0x67893a3d28  (/system/lib64/libclang_rt.hwasan.so+0x23d28) (BuildId: 75d3a57a5341c45a993cce5a48e37c42a9c6157f)
       #1 (anonymous namespace)::DoubleFree() at (G:/2D-DFXDemo-master/2D-DFXDemo-master/dfx_test/entry/src/main/cpp/common/xsan/XsanTest.cpp:130)
       #2 0x68397e7c90  (/system/lib64/platformsdk/libace_napi.z.so+0x67c90) (BuildId: 76bc1ed675edcc5f429a976d6c9b955d)
       #3 0x6856ef29f4  (/system/lib64/module/arkcompiler/stub.an+0xe179f4)
       #4 0x6856546900  (/system/lib64/module/arkcompiler/stub.an+0x46b900)

   previously allocated by thread 23641 here:
       #0 0x67893a44ac  (/system/lib64/libclang_rt.hwasan.so+0x244ac) (BuildId: 75d3a57a5341c45a993cce5a48e37c42a9c6157f)
       #1 (anonymous namespace)::DoubleFree() at (G:/2D-DFXDemo-master/2D-DFXDemo-master/dfx_test/entry/src/main/cpp/common/xsan/XsanTest.cpp:128)
       #2 0x68397e7c90  (/system/lib64/platformsdk/libace_napi.z.so+0x67c90) (BuildId: 76bc1ed675edcc5f429a976d6c9b955d)
       #3 0x6856ef29f4  (/system/lib64/module/arkcompiler/stub.an+0xe179f4)
       #4 0x6856546900  (/system/lib64/module/arkcompiler/stub.an+0x46b900)
   ```

   通过llvm-addr2line工具（参考：[C++堆栈解析流程](../harmonyos-guides/ide-exception-stack-parsing-principle.md#section1735713501344)中对于llvm-addr2line的使用）、DevEco Studio自带的堆栈跟踪分析等类似工具，对分配栈和首次释放栈中的业务栈帧进行符号化，定位到对应的源码位置。相关代码如下：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/72/v3/eHigaKnzS1mc6SqMLZUQ3w/zh-cn_image_0000002723405003.png)

   日志显示，重复释放的内存地址0x000400822a80，在相同线程23641中DoubleFree（XsanTest.cpp:128）申请，在相同线程23641中DoubleFree（XsanTest.cpp:130）第一次释放。日志中的异常地址0x000400822a80正好等于100字节内存区域[0x000400822a80, 0x000400822ae4)的起始地址，located 0 bytes inside表示释放操作使用的是该内存对象的首地址，与源码中申请和释放的内存对象一致。
4. 分析控制流路径，如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/33/v3/HT562Du4QtquSy5GMvIZuQ/zh-cn_image_0000002693605648.png)
   1. 定义函数内局部指针对象ptr，并申请100字节内存，地址赋值给ptr。
   2. 第一次释放ptr，释放后ptr指针未置为nullptr。
   3. 第二次释放ptr，此时ptr所指向的内存块已释放，触发异常。

**问题结论与总结**

该问题是由于DoubleFree函数对同一块堆内存连续执行了两次释放操作。该内存在第一次调用free(ptr)后已经失效，后续代码又通过保存原地址的ptr再次执行释放，最终触发异常。

**修复建议**

应删除重复释放逻辑，确保每块堆内存只由明确的所有者释放一次。释放完成后，可将指针置为nullptr，降低后续代码继续使用原地址的风险。需要注意的是，指针置空只能起到防御作用，不能代替对重复释放流程的修正。

**案例二：**局部指针与全局指针所有权混乱导致重复释放

**问题现象**

应用运行过程中触发HWASan检测，应用闪退并生成HWASan故障日志。

**问题分析**

1. 查看日志内容，确认故障类型。

   证据1：根据字段Reason:use-after-free和字段ERROR: HWAddressSanitizer: invalid-free，可以确认是堆内存重复释放错误。

   ```screen
   Device info:HUAWEI Mate 60 Pro
   Build info:ALN-AL80 6.1.0.117(SP6C00E115R4P9)
   Fingerprint:ffee3be633ec610ed0fbc22f313c40ca7a615188736ae1e27193be3ad8c990af
   Timestamp:2026-07-11 17:26:59.849
   Module name:com.example.dfxdemov2
   Version:1.0.0
   Pid:12312
   Uid:20020196
   Reason:use-after-free
   ==appspawn==12312==ERROR: HWAddressSanitizer: invalid-free on address 0x0004007e0b80 at pc 0x0059a74639d0 on thread 12312
   tags: b5/c8 (ptr/mem)
       #0 0x59a74639d0  (/system/lib64/libclang_rt.hwasan.so+0x239d0) (BuildId: e25762f8b6428463640ec8eb41402ab47437da60)
       #1 0x5a53994750  (/data/storage/el1/bundle/libs/arm64/libsanitizer.so+0x14750) (BuildId: 3e4ca65f32da827dab5a8383d810cf82e341097f)
       #2 0x5a53994690  (/data/storage/el1/bundle/libs/arm64/libsanitizer.so+0x14690) (BuildId: 3e4ca65f32da827dab5a8383d810cf82e341097f)
       #3 0x5a5398afc4  (/data/storage/el1/bundle/libs/arm64/libsanitizer.so+0xafc4) (BuildId: 3e4ca65f32da827dab5a8383d810cf82e341097f)
       #4 0x5a364a67c0  (/system/lib64/platformsdk/libace_napi.z.so+0x667c0) (BuildId: 007d3dfdfbceca6f770655c180be87b0)
       #5 0x5a4e7bf37c  (/system/lib64/module/arkcompiler/stub.an+0xe1537c)
       #6 0x5a4de10904  (/system/lib64/module/arkcompiler/stub.an+0x466904)

   [0x0004007e0b80,0x0004007e0c00) is a small unallocated heap chunk; size: 128 offset: 0, Allocated By 12312

   Potential Cause: use-after-free
   0x0004007e0b80 (rb[0] tags:b5) is located 0 bytes inside of 100-byte region [0x0004007e0b80,0x0004007e0be4)
   freed by thread 12312 here:
       #0 0x59a74639d0  (/system/lib64/libclang_rt.hwasan.so+0x239d0) (BuildId: e25762f8b6428463640ec8eb41402ab47437da60)
       #1 0x5a53994678  (/data/storage/el1/bundle/libs/arm64/libsanitizer.so+0x14678) (BuildId: 3e4ca65f32da827dab5a8383d810cf82e341097f)
       #2 0x5a5398afc4  (/data/storage/el1/bundle/libs/arm64/libsanitizer.so+0xafc4) (BuildId: 3e4ca65f32da827dab5a8383d810cf82e341097f)
       #3 0x5a364a67c0  (/system/lib64/platformsdk/libace_napi.z.so+0x667c0) (BuildId: 007d3dfdfbceca6f770655c180be87b0)
       #4 0x5a4e7bf37c  (/system/lib64/module/arkcompiler/stub.an+0xe1537c)
       #5 0x5a4de10904  (/system/lib64/module/arkcompiler/stub.an+0x466904)

   previously allocated by thread 12312 here:
       #0 0x59a74640b8  (/system/lib64/libclang_rt.hwasan.so+0x240b8) (BuildId: e25762f8b6428463640ec8eb41402ab47437da60)
       #1 0x5a539945fc  (/data/storage/el1/bundle/libs/arm64/libsanitizer.so+0x145fc) (BuildId: 3e4ca65f32da827dab5a8383d810cf82e341097f)
       #2 0x5a5398afc4  (/data/storage/el1/bundle/libs/arm64/libsanitizer.so+0xafc4) (BuildId: 3e4ca65f32da827dab5a8383d810cf82e341097f)
       #3 0x5a364a67c0  (/system/lib64/platformsdk/libace_napi.z.so+0x667c0) (BuildId: 007d3dfdfbceca6f770655c180be87b0)
       #4 0x5a4e7bf37c  (/system/lib64/module/arkcompiler/stub.an+0xe1537c)
       #5 0x5a4de10904  (/system/lib64/module/arkcompiler/stub.an+0x466904)
   ```
2. 分析报错栈，确认触发异常位置。

   证据2：

   ```screen
   ==appspawn==12312==ERROR: HWAddressSanitizer: invalid-free on address 0x0004007e0b80 at pc 0x0059a74639d0 on thread 12312
   tags: b5/c8 (ptr/mem)
       #0 0x59a74639d0  (/system/lib64/libclang_rt.hwasan.so+0x239d0) (BuildId: e25762f8b6428463640ec8eb41402ab47437da60)
       #1 (anonymous namespace)::ClearSharedBuffer() at (C:/Users/DevEcoStudioProjects/DFXDemoV2/entry/src/main/cpp/sanitizer.cpp:202)
       #2 (anonymous namespace)::DoubleFreeShared() at (C:/Users/DevEcoStudioProjects/DFXDemoV2/entry/src/main/cpp/sanitizer.cpp:217)
       #3 (anonymous namespace)::TriggerHWAsanDoubleShared(napi_env__*, napi_callback_info__*) at (C:/Users/DevEcoStudioProjects/DFXDemoV2/entry/src/main/cpp/sanitizer.cpp:223)
   ```

   通过llvm-addr2line工具（参考：[C++堆栈解析流程](../harmonyos-guides/ide-exception-stack-parsing-principle.md#section1735713501344)中对于llvm-addr2line的使用）、DevEco Studio自带的堆栈跟踪分析等类似工具，对报错栈进行符号化，定位到对应的源码位置。相关代码如下：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7d/v3/BT3AgXVyRF6DJYMac-Ea9w/zh-cn_image_0000002723285081.png)

   结合源码分析，程序在执行free(g\_sharedPtr)时触发异常。此时g\_sharedPtr虽然不为nullptr，但其指向的堆内存已经在此前流程中被释放。
3. 分析分配栈和首次释放栈，确认重复释放内存对象。

   证据3：

   ```screen
   Potential Cause: use-after-free
   0x0004007e0b80 (rb[0] tags:b5) is located 0 bytes inside of 100-byte region [0x0004007e0b80,0x0004007e0be4)
   freed by thread 12312 here:
       #0 0x59a74639d0  (/system/lib64/libclang_rt.hwasan.so+0x239d0) (BuildId: e25762f8b6428463640ec8eb41402ab47437da60)
       #1 (anonymous namespace)::DoubleFreeShared() at (C:/Users/DevEcoStudioProjects/DFXDemoV2/entry/src/main/cpp/sanitizer.cpp:215)
       #2 (anonymous namespace)::TriggerHWAsanDoubleShared(napi_env__*, napi_callback_info__*) at (C:/Users/DevEcoStudioProjects/DFXDemoV2/entry/src/main/cpp/sanitizer.cpp:223)
       #3 0x5a364a67c0  (/system/lib64/platformsdk/libace_napi.z.so+0x667c0) (BuildId: 007d3dfdfbceca6f770655c180be87b0)
       #4 0x5a4e7bf37c  (/system/lib64/module/arkcompiler/stub.an+0xe1537c)
       #5 0x5a4de10904  (/system/lib64/module/arkcompiler/stub.an+0x466904)

   previously allocated by thread 12312 here:
       #0 0x59a74640b8  (/system/lib64/libclang_rt.hwasan.so+0x240b8) (BuildId: e25762f8b6428463640ec8eb41402ab47437da60)
       #1 (anonymous namespace)::DoubleFreeShared() at (C:/Users/DevEcoStudioProjects/DFXDemoV2/entry/src/main/cpp/sanitizer.cpp:210)
       #2 (anonymous namespace)::TriggerHWAsanDoubleShared(napi_env__*, napi_callback_info__*) at (C:/Users/DevEcoStudioProjects/DFXDemoV2/entry/src/main/cpp/sanitizer.cpp:223)
       #3 0x5a364a67c0  (/system/lib64/platformsdk/libace_napi.z.so+0x667c0) (BuildId: 007d3dfdfbceca6f770655c180be87b0)
       #4 0x5a4e7bf37c  (/system/lib64/module/arkcompiler/stub.an+0xe1537c)
       #5 0x5a4de10904  (/system/lib64/module/arkcompiler/stub.an+0x466904)
   ```

   通过llvm-addr2line工具（参考：[C++堆栈解析流程](../harmonyos-guides/ide-exception-stack-parsing-principle.md#section1735713501344)中对于llvm-addr2line的使用）、DevEco Studio自带的堆栈跟踪分析等类似工具，对分配栈和首次释放栈进行符号化，定位到对应的源码位置。相关代码如下：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/89/v3/UcNKZiYmRtyW_QgxhnSv8g/zh-cn_image_0000002693765534.png)

   日志显示，线程12312在sanitizer.cpp:210的DoubleFreeShared函数中申请了100字节内存，并将地址同时保存到局部指针ptr和全局指针g\_sharedPtr。代码在215行通过ptr首次释放内存，但未同步更新g\_sharedPtr，后续流程再次通过g\_sharedPtr释放同一块内存，最终触发重复释放异常。日志中的异常地址0x0004007e0b80正好等于100字节内存区域[0x0004007e0b80, 0x0004007e0be4)的起始地址，located 0 bytes inside表示释放操作使用的是该内存对象的首地址，与源码中申请和释放的内存对象一致。
4. 分析控制流路径，如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d3/v3/pAO5aa_qRZOnOM3yCksQNg/zh-cn_image_0000002723405037.png)
   1. 申请100字节堆内存，并将地址赋值给局部指针ptr。
   2. 将ptr保存的地址赋值给全局指针g\_sharedPtr，此时两个指针指向同一块内存。
   3. 通过free(ptr)首次释放该内存，g\_sharedPtr仍保存原地址。
   4. 调用ClearSharedBuffer()，再次通过free(g\_sharedPtr)释放同一块内存，触发重复释放异常。

**问题结论与总结**

该问题是由于同一块堆内存地址同时保存在局部指针ptr和全局指针g\_sharedPtr中。代码通过ptr释放内存后，后续清理流程仍通过g\_sharedPtr再次释放同一块内存，最终触发重复释放异常。问题的根本原因是共享内存的所有权和释放职责不明确，多个位置均执行了释放操作。

**修复建议**

1. 应明确内存的所有权和释放职责，由固定的对象、模块或流程负责释放，其他位置仅保存非拥有型指针，不得重复执行释放操作。
2. 对于确实需要由多个位置共同持有的内存，建议使用std::shared\_ptr等智能指针，通过引用计数机制统一管理内存生命周期，降低悬空指针和重复释放风险。

## ASan堆内存重复释放

### 根因描述

堆内存重复释放是一种堆内存错误，是指同一块通过malloc()/new()/calloc()/realloc()等方式申请的堆内存，在已经释放后再次被释放。此类问题本质上是程序对同一块内存的所有权管理混乱，导致多个路径、多个对象或多个线程认为自己有权释放该内存。当应用[开启ASan](../harmonyos-guides/ide-asan.md#section111599216114)检测后，ASan会记录堆内存的分配和释放状态。一旦检测到程序再次释放已经释放的内存，会报告double-free异常并导致应用退出。

### 问题分析思路

此类问题的常见原因与HWASan堆内存重复释放一致，通常包括当前上下文重复释放，以及共享场景下多个位置重复释放同一块内存。

问题分析步骤如下：

1. 查看ASan日志中的报错关键字段，确认故障类型，关注是否包含“ERROR: AddressSanitizer: attempting double-free ”。
2. 分析报错栈，确认触发异常位置，并通过llvm-addr2line（参考：[C++堆栈解析流程](../harmonyos-guides/ide-exception-stack-parsing-principle.md#section1735713501344)中对于llvm-addr2line的使用）等解析工具，定位到具体代码行。
3. 分析分配栈和首次释放栈，确认重复释放内存对象，并通过llvm-addr2line（参考：[C++堆栈解析流程](../harmonyos-guides/ide-exception-stack-parsing-principle.md#section1735713501344)中对于llvm-addr2line的使用）等解析工具，定位到具体代码行。
4. 结合内存分配位置、首次释放位置和异常释放位置，分析堆内存重复释放的控制流路径。

### 关键字

此类问题日志关键词为：ERROR: AddressSanitizer: attempting double-free。确认是堆内存重复释放后，优先分析业务侧调用栈帧代码。

### 案例分析

本案例与HWASan堆内存重复释放的基础案例采用相同业务场景，均为同一指针连续释放。此处重点说明ASan的日志结构和定位方法，重复的业务场景不再展开说明。

**案例一：**指针连续重复释放

**问题现象**

应用运行过程中触发ASan检测，应用闪退并生成ASan故障日志。

**问题分析**

1. 查看日志内容，确认故障类型。

   证据1：日志中明确给出ERROR: AddressSanitizer: attempting double-free，可确认问题为堆内存重复释放。

   ```screen
   Device info:HUAWEI Mate 60 Pro
   Build info:ALN-AL80 6.1.0.117(SP6C00E115R4P9)
   Fingerprint:4c9c51573fda8b7b4535ec66d0af36df6301ed65b03b7bdd210e34b2ce7eda21
   Timestamp:2026-07-13 12:13:42.076
   Module name:com.example.dfxdemov2
   Version:1.0.0
   Pid:32132
   Uid:20020196
   Reason:double-free
   ==appspawn==37068==ERROR: AddressSanitizer: attempting double-free on 0x0060dbf47d00 in thread T0 (ample.dfxdemov2):
       #0 0x5a5a7db870  (/system/lib64/libclang_rt.asan.so+0xdb870) (BuildId: f1131caa0ec57e4ec243cecbebedd1c7d6759f8d)
       #1 (anonymous namespace)::DoubleFree() at (C:/Users/DevEcoStudioProjects/DFXDemoV2/entry/src/main/cpp/sanitizer.cpp:185)
       #2 (anonymous namespace)::TriggerAsanDouble(napi_env__*, napi_callback_info__*) at (C:/Users/DevEcoStudioProjects/DFXDemoV2/entry/src/main/cpp/sanitizer.cpp:192)
       #3 0x7ae7fe67c0  (/system/lib64/platformsdk/libace_napi.z.so+0x667c0) (BuildId: 007d3dfdfbceca6f770655c180be87b0)

   0x0060dbf47d00 is located 0 bytes inside of 100-byte region [0x0060dbf47d00,0x0060dbf47d64)
   freed by thread T0 (ample.dfxdemov2) here:
       #0 0x5a5a7db870  (/system/lib64/libclang_rt.asan.so+0xdb870) (BuildId: f1131caa0ec57e4ec243cecbebedd1c7d6759f8d)
       #1 (anonymous namespace)::DoubleFree() at (C:/Users/DevEcoStudioProjects/DFXDemoV2/entry/src/main/cpp/sanitizer.cpp:184)
       #2 (anonymous namespace)::TriggerAsanDouble(napi_env__*, napi_callback_info__*) at (C:/Users/DevEcoStudioProjects/DFXDemoV2/entry/src/main/cpp/sanitizer.cpp:192)
       #3 0x7ae7fe67c0  (/system/lib64/platformsdk/libace_napi.z.so+0x667c0) (BuildId: 007d3dfdfbceca6f770655c180be87b0)
       #4 0x7e1f53b37c  (/system/lib64/module/arkcompiler/stub.an+0xe1537c)
       #5 0x7e1eb8c904  (/system/lib64/module/arkcompiler/stub.an+0x466904)

   previously allocated by thread T0 (ample.dfxdemov2) here:
       #0 0x5a5a7db9b8  (/system/lib64/libclang_rt.asan.so+0xdb9b8) (BuildId: f1131caa0ec57e4ec243cecbebedd1c7d6759f8d)
       #1 (anonymous namespace)::DoubleFree() at (C:/Users/DevEcoStudioProjects/DFXDemoV2/entry/src/main/cpp/sanitizer.cpp:182)
       #2 (anonymous namespace)::TriggerAsanDouble(napi_env__*, napi_callback_info__*) at (C:/Users/DevEcoStudioProjects/DFXDemoV2/entry/src/main/cpp/sanitizer.cpp:192)
       #3 0x7ae7fe67c0  (/system/lib64/platformsdk/libace_napi.z.so+0x667c0) (BuildId: 007d3dfdfbceca6f770655c180be87b0)
       #4 0x7e1f53b37c  (/system/lib64/module/arkcompiler/stub.an+0xe1537c)
       #5 0x7e1eb8c904  (/system/lib64/module/arkcompiler/stub.an+0x466904)

   SUMMARY: AddressSanitizer: double-free (/system/lib64/libclang_rt.asan.so+0xdb870) (BuildId: f1131caa0ec57e4ec243cecbebedd1c7d6759f8d)
   ```
2. 分析报错栈，确认触发异常位置。

   证据2：

   ```screen
   ==appspawn==37068==ERROR: AddressSanitizer: attempting double-free on 0x0060dbf47d00 in thread T0 (ample.dfxdemov2):
       #0 0x5a5a7db870  (/system/lib64/libclang_rt.asan.so+0xdb870) (BuildId: f1131caa0ec57e4ec243cecbebedd1c7d6759f8d)
       #1 (anonymous namespace)::DoubleFree() at (C:/Users/DevEcoStudioProjects/DFXDemoV2/entry/src/main/cpp/sanitizer.cpp:185)
       #2 (anonymous namespace)::TriggerAsanDouble(napi_env__*, napi_callback_info__*) at (C:/Users/DevEcoStudioProjects/DFXDemoV2/entry/src/main/cpp/sanitizer.cpp:192)
   ```

   通过llvm-addr2line（参考：[C++堆栈解析流程](../harmonyos-guides/ide-exception-stack-parsing-principle.md#section1735713501344)中对于llvm-addr2line的使用）、DevEco Studio自带的堆栈跟踪分析工具或其他类似工具，对报错栈中的业务栈帧进行符号化，定位到具体源码位置。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/29/v3/OQe7ZYwBQwKrbDkzvFXMOw/zh-cn_image_0000002693605716.png)

   报错栈定位到sanitizer.cpp:185。结合源码确认，程序在该行第二次调用free(ptr)时触发ASan double-free异常。
3. 分析分配栈和首次释放栈，确认重复释放的内存对象。

   证据3：

   ```screen
   0x0060dbf47d00 is located 0 bytes inside of 100-byte region [0x0060dbf47d00,0x0060dbf47d64)
   freed by thread T0 (ample.dfxdemov2) here:
       #0 0x5a5a7db870  (/system/lib64/libclang_rt.asan.so+0xdb870) (BuildId: f1131caa0ec57e4ec243cecbebedd1c7d6759f8d)
       #1 (anonymous namespace)::DoubleFree() at (C:/Users/DevEcoStudioProjects/DFXDemoV2/entry/src/main/cpp/sanitizer.cpp:184)
       #2 (anonymous namespace)::TriggerAsanDouble(napi_env__*, napi_callback_info__*) at (C:/Users/DevEcoStudioProjects/DFXDemoV2/entry/src/main/cpp/sanitizer.cpp:192)
       #3 0x7ae7fe67c0  (/system/lib64/platformsdk/libace_napi.z.so+0x667c0) (BuildId: 007d3dfdfbceca6f770655c180be87b0)
       #4 0x7e1f53b37c  (/system/lib64/module/arkcompiler/stub.an+0xe1537c)
       #5 0x7e1eb8c904  (/system/lib64/module/arkcompiler/stub.an+0x466904)

   previously allocated by thread T0 (ample.dfxdemov2) here:
       #0 0x5a5a7db9b8  (/system/lib64/libclang_rt.asan.so+0xdb9b8) (BuildId: f1131caa0ec57e4ec243cecbebedd1c7d6759f8d)
       #1 (anonymous namespace)::DoubleFree() at (C:/Users/DevEcoStudioProjects/DFXDemoV2/entry/src/main/cpp/sanitizer.cpp:182)
       #2 (anonymous namespace)::TriggerAsanDouble(napi_env__*, napi_callback_info__*) at (C:/Users/DevEcoStudioProjects/DFXDemoV2/entry/src/main/cpp/sanitizer.cpp:192)
       #3 0x7ae7fe67c0  (/system/lib64/platformsdk/libace_napi.z.so+0x667c0) (BuildId: 007d3dfdfbceca6f770655c180be87b0)
       #4 0x7e1f53b37c  (/system/lib64/module/arkcompiler/stub.an+0xe1537c)
       #5 0x7e1eb8c904  (/system/lib64/module/arkcompiler/stub.an+0x466904)
   ```

   通过llvm-addr2line（参考：[C++堆栈解析流程](../harmonyos-guides/ide-exception-stack-parsing-principle.md#section1735713501344)中对于llvm-addr2line的使用）等工具对分配栈和首次释放栈中的业务栈帧进行符号化，定位到对应的源码位置。相关代码如下：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b0/v3/lTNdiq4wSbOMvIke1yB6PA/zh-cn_image_0000002723285185.png)

   日志显示，地址为0x0060dbf47d00、大小为100字节的堆内存在sanitizer.cpp:182申请，并在sanitizer.cpp:184首次释放。随后代码在 sanitizer.cpp:185 再次通过同一指针释放该内存，最终触发重复释放异常。
4. 分析控制流路径，如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e8/v3/XY5TUIkbQCC-J9Jwl2J80A/zh-cn_image_0000002693765672.png)
   1. 定义函数内局部指针对象ptr，并申请100字节内存，地址赋值给ptr。
   2. 第一次释放ptr，释放后ptr指针未置为nullptr。
   3. 第二次释放ptr，此时ptr所指向的内存块已释放，触发异常。

**问题结论与总结**

该问题是由于DoubleFree函数对同一块堆内存连续执行了两次释放操作。该案例的业务根因与HWASan基础案例一致，区别在于ASan会直接报告attempting double-free，HWASan报告为invalid-free。

**修复建议**

应删除重复释放逻辑，确保每块堆内存只由明确的所有者释放一次。释放完成后，可将指针置为nullptr，降低后续代码继续使用原地址的风险。需要注意的是，指针置空只能起到防御作用，不能代替对重复释放流程的修正。

## GWP-ASan堆内存重复释放

### 根因描述

此类问题本质上是内存所有权或生命周期管理错误，导致同一执行路径、多个对象或多个线程重复释放同一块内存。当应用[GWP-ASan使能](bpta-stability-gwpasan-detection.md#section2735718353)后，运行时会对堆内存分配进行采样。当目标内存分配命中采样并进入受保护内存池后，GWP-ASan会记录该内存的分配和释放信息。一旦检测到程序再次释放已经释放的内存，会报告Double Free错误。需要注意的是，GWP-ASan只检测命中采样的堆内存对象，因此同一问题可能需要多次运行或压测才能检测到。

### 问题分析思路

此类问题的常见原因和HWASan、ASan堆内存重复释放一致，不再赘述。对于GWP-ASan，问题分析步骤如下：

1. 查看日志中的报错关键字段，确认故障类型。重点关注是否存在Double Free。
2. 分析报错栈，确认触发异常位置，并通过llvm-addr2line（参考：[C++堆栈解析流程](../harmonyos-guides/ide-exception-stack-parsing-principle.md#section1735713501344)中对于llvm-addr2line的使用）等解析工具，定位到具体代码行。
3. 分析分配栈和首次释放栈，确认重复释放的内存对象，并通过llvm-addr2line（参考：[C++堆栈解析流程](../harmonyos-guides/ide-exception-stack-parsing-principle.md#section1735713501344)中对于llvm-addr2line的使用）等解析工具，定位到具体代码行。
4. 结合内存分配位置、首次释放位置和异常释放位置，分析堆内存重复释放的控制流路径。

### 关键字

此类问题日志关键词为：Double Free。确认是堆内存重复释放后，优先分析业务侧调用栈帧代码。

### 案例分析

本案例与HWASan、ASan堆内存重复释放文档中的基础案例一致，均为同一指针在当前上下文中连续释放。此处重点说明GWP-ASan的日志结构和定位方法，重复的业务场景不再展开说明。

**案例一：**指针连续重复释放

**问题现象**

应用运行过程中触发GWP-ASan检测，应用闪退并生成GWP-ASan故障日志。

**问题分析**

1. 查看日志内容，确认故障类型。

   证据1：日志中明确给出Double Free at 0x5bfb35f000 (a 64-byte allocation) by thread 28195 here，可以确认问题为堆内存重复释放。异常涉及的内存地址为0x5bfb35f000，申请大小为64字节。

   ```screen
   *** GWP-ASan detected a memory error ***
   Double Free at 0x5bfb35f000 (a 64-byte allocation) by thread 28195 here:
    #0 0x5b4b83dda4  (/lib/ld-musl-aarch64.so.1+0x14bda4) (BuildId: 35422f66114500c7d794bf84b3fd302b)
    #1 (anonymous namespace)::DoubleFreeGWPASan() at (C:/Users/DevEcoStudioProjects/DFXDemoV2/entry/src/main/cpp/sanitizer.cpp:238)
    #2 (anonymous namespace)::TriggerGWPASanDouble(napi_env__*, napi_callback_info__*) at (C:/Users/DevEcoStudioProjects/DFXDemoV2/entry/src/main/cpp/sanitizer.cpp:244)
    #3 0x5bdafe67c0  (/system/lib64/platformsdk/libace_napi.z.so+0x667c0) (BuildId: 007d3dfdfbceca6f770655c180be87b0)
   0x5bfb35f000 was deallocated by thread 28195 here:
    #0 0x5b4b83e394  (/lib/ld-musl-aarch64.so.1+0x14c394) (BuildId: 35422f66114500c7d794bf84b3fd302b)
    #1 0x5b4b83dd6c  (/lib/ld-musl-aarch64.so.1+0x14bd6c) (BuildId: 35422f66114500c7d794bf84b3fd302b)
    #2 (anonymous namespace)::DoubleFreeGWPASan() at (C:/Users/DevEcoStudioProjects/DFXDemoV2/entry/src/main/cpp/sanitizer.cpp:237)
    #3 (anonymous namespace)::TriggerGWPASanDouble(napi_env__*, napi_callback_info__*) at (C:/Users/DevEcoStudioProjects/DFXDemoV2/entry/src/main/cpp/sanitizer.cpp:244)
    #4 0x5bdafe67c0  (/system/lib64/platformsdk/libace_napi.z.so+0x667c0) (BuildId: 007d3dfdfbceca6f770655c180be87b0)
   0x5bfb35f000 was allocated by thread 28195 here:
    #0 0x5b4b83e394  (/lib/ld-musl-aarch64.so.1+0x14c394) (BuildId: 35422f66114500c7d794bf84b3fd302b)
    #1 0x5b4b83dad0  (/lib/ld-musl-aarch64.so.1+0x14bad0) (BuildId: 35422f66114500c7d794bf84b3fd302b)
    #2 0x5b4b860168  (/lib/ld-musl-aarch64.so.1+0x16e168) (BuildId: 35422f66114500c7d794bf84b3fd302b)
    #3 0x5b4b8e8e88  (/lib/ld-musl-aarch64.so.1+0x1f6e88) (BuildId: 35422f66114500c7d794bf84b3fd302b)
    #4 (anonymous namespace)::DoubleFreeGWPASan() at (C:/Users/DevEcoStudioProjects/DFXDemoV2/entry/src/main/cpp/sanitizer.cpp:233)
    #5 (anonymous namespace)::TriggerGWPASanDouble(napi_env__*, napi_callback_info__*) at (C:/Users/DevEcoStudioProjects/DFXDemoV2/entry/src/main/cpp/sanitizer.cpp:244)
    #6 0x5bdafe67c0  (/system/lib64/platformsdk/libace_napi.z.so+0x667c0) (BuildId: 007d3dfdfbceca6f770655c180be87b0)
   *** End GWP-ASan report ***
   ```
2. 分析报错栈，确认触发异常位置。

   证据2：

   ```screen
   Double Free at 0x5bfb35f000 (a 64-byte allocation) by thread 28195 here:
    #0 0x5b4b83dda4  (/lib/ld-musl-aarch64.so.1+0x14bda4) (BuildId: 35422f66114500c7d794bf84b3fd302b)
    #1 (anonymous namespace)::DoubleFreeGWPASan() at (C:/Users/DevEcoStudioProjects/DFXDemoV2/entry/src/main/cpp/sanitizer.cpp:238)
   ```

   通过llvm-addr2line工具（参考：[C++堆栈解析流程](../harmonyos-guides/ide-exception-stack-parsing-principle.md#section1735713501344)中对于llvm-addr2line的使用）、DevEco Studio自带的堆栈跟踪分析等类似工具，对报错栈进行符号化，定位到对应的源码位置。相关代码如下：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ef/v3/6hWKeeJZT-usfyRatQuRAg/zh-cn_image_0000002723405179.png)

   结合源码确认，程序在该行第二次调用free(p)时触发GWP-ASan的Double Free错误。
3. 分析分配栈和首次释放栈，确认重复释放内存对象。

   证据3：

   ```screen
   0x5bfb35f000 was deallocated by thread 28195 here:
    #0 0x5b4b83e394  (/lib/ld-musl-aarch64.so.1+0x14c394) (BuildId: 35422f66114500c7d794bf84b3fd302b)
    #1 0x5b4b83dd6c  (/lib/ld-musl-aarch64.so.1+0x14bd6c) (BuildId: 35422f66114500c7d794bf84b3fd302b)
    #2 (anonymous namespace)::DoubleFreeGWPASan() at (C:/Users/DevEcoStudioProjects/DFXDemoV2/entry/src/main/cpp/sanitizer.cpp:237)
    #3 (anonymous namespace)::TriggerGWPASanDouble(napi_env__*, napi_callback_info__*) at (C:/Users/DevEcoStudioProjects/DFXDemoV2/entry/src/main/cpp/sanitizer.cpp:244)
    #4 0x5bdafe67c0  (/system/lib64/platformsdk/libace_napi.z.so+0x667c0) (BuildId: 007d3dfdfbceca6f770655c180be87b0)
   0x5bfb35f000 was allocated by thread 28195 here:
    #0 0x5b4b83e394  (/lib/ld-musl-aarch64.so.1+0x14c394) (BuildId: 35422f66114500c7d794bf84b3fd302b)
    #1 0x5b4b83dad0  (/lib/ld-musl-aarch64.so.1+0x14bad0) (BuildId: 35422f66114500c7d794bf84b3fd302b)
    #2 0x5b4b860168  (/lib/ld-musl-aarch64.so.1+0x16e168) (BuildId: 35422f66114500c7d794bf84b3fd302b)
    #3 0x5b4b8e8e88  (/lib/ld-musl-aarch64.so.1+0x1f6e88) (BuildId: 35422f66114500c7d794bf84b3fd302b)
    #4 (anonymous namespace)::DoubleFreeGWPASan() at (C:/Users/DevEcoStudioProjects/DFXDemoV2/entry/src/main/cpp/sanitizer.cpp:233)
   ```

   通过llvm-addr2line工具（参考：[C++堆栈解析流程](../harmonyos-guides/ide-exception-stack-parsing-principle.md#section1735713501344)中对于llvm-addr2line的使用）、DevEco Studio自带的堆栈跟踪分析等类似工具，对分配栈和首次释放栈进行符号化，定位到对应的源码位置。相关代码如下：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/99/v3/JaAzauvRQWGxugd9XdVyUA/zh-cn_image_0000002693605852.png)

   日志显示，线程28195在sanitizer.cpp:233申请了64字节堆内存，地址为0x5bfb35f000。该内存命中GWP-ASan采样后，在sanitizer.cpp:237首次释放，随后在sanitizer.cpp:238再次释放，最终触发重复释放错误。
4. 分析控制流路径，如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/7mq9iFj5TtqSzsZlR5n9vw/zh-cn_image_0000002723285319.png)
   1. 定义函数内局部指针对象ptr，并申请64字节内存，地址赋值给ptr。
   2. 第一次释放ptr，释放后ptr指针未置为nullptr。
   3. 第二次释放ptr，此时ptr所指向的内存块已释放，触发异常。

**问题结论与总结**

该问题是由于对同一块堆内存连续执行了两次释放操作导致的。该内存在第一次调用free(ptr)后已经失效，后续代码又通过保存原地址的ptr再次执行释放，最终触发异常。该案例的业务根因与HWASan、ASan基础案例一致，区别在于GWP-ASan采用采样检测机制，只有目标内存命中采样并进入受保护内存池后，才会记录并报告重复释放问题。

**修复建议**

应删除重复释放逻辑，确保每块堆内存只由明确的所有者释放一次。释放完成后，可将指针置为nullptr，降低后续代码继续使用原地址的风险。需要注意的是，指针置空只能起到防御作用，不能代替对重复释放流程的修正。
