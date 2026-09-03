---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-stability-memory-invalid-free-fault-mode
title: 内存释放地址异常故障模式说明
breadcrumb: 最佳实践 > 稳定性 > 稳定性分析 > 稳定性故障模式说明 > 地址越界故障模式说明 > 内存释放地址异常故障模式说明
category: best-practices
scraped_at: 2026-09-04T06:33:23+08:00
doc_updated_at: 2026-08-26
content_hash: sha256:645d1401ab1531d61c6d77bed8a46d42a7455f41b5346efd1de158806dc4a94d
---

内存释放要求传入有效的堆内存对象起始地址，若传入偏移后的地址、未初始化指针、野指针或非堆内存地址，将导致非法释放。此类问题可能直接在释放接口中触发崩溃，也可能破坏堆内存管理结构，随后在其他模块的内存分配或释放过程中暴露，导致故障现场难以追溯。开启检测能力后，可在非法释放时检测异常并记录现场调用栈。

本文结合HWASan（Hardware-assisted AddressSanitizer）、ASan（AddressSanitizer）典型案例，介绍内存释放地址异常问题的日志特征与定位方法，具体包括：

* [ASan堆内存释放地址非法](bpta-stability-memory-invalid-free-fault-mode.md#section14741252144517)
* [GWP-ASan堆内存释放地址非法](bpta-stability-memory-invalid-free-fault-mode.md#section11832112555220)

## ASan堆内存释放地址非法

### 根因描述

堆内存释放地址非法是指在释放堆内存时传入了非法堆内存块地址。问题本质是：程序在调用free()、delete、delete[]等释放函数时，传入了未初始化的指针（非0）或野指针，或重复释放已申请的内存块，导致释放失败。当应用[开启ASan](../harmonyos-guides/ide-asan.md#section111599216114)检测能力后，运行时会根据分配器的元数据检查待释放地址是否为有效分配块的起始地址，以及该内存块是否已被释放。一旦检测异常，将触发bad-free异常并退出。

### 问题分析思路

此类问题，通常有几种可能：

1. 传入野指针，导致释放失败。
2. 传入未初始化指针，导致释放失败。
3. 传入已释放内存地址，导致释放失败（也可能报Double Free）。

问题分析步骤如下：

1. 查看ASan日志中的报错关键字段，确认故障类型，关注是否为bad-free。
2. 分析报错栈，确认触发异常位置，并通过llvm-addr2line（参考：[C++堆栈解析流程](../harmonyos-guides/ide-exception-stack-parsing-principle.md#section1735713501344)中对于llvm-addr2line的使用）等解析工具，定位到具体代码行。
3. 分析分配栈，确认非法地址所在的已分配内存对象，并通过llvm-addr2line（参考：[C++堆栈解析流程](../harmonyos-guides/ide-exception-stack-parsing-principle.md#section1735713501344)中对于llvm-addr2line的使用）等解析工具，定位到被异常访问对象的定义函数。
4. 结合触发异常位置和被异常访问对象，分析堆内存释放地址非法的控制流路径。

### 关键字

此类问题日志关键词为：bad-free。确认故障类型后，应重点分析非法释放栈、内存分配栈，以及非法释放地址相对于已分配内存对象起始地址的偏移关系。

### 案例分析

**案例一：**指针偏移导致堆内存非法释放

**问题现象**

触发业务代码时，应用闪退，并生成ASan故障日志。

**问题分析**

1. 查看日志内容，确认故障类型。

   证据1：根据字段Reason:bad-free和字段ERROR: AddressSanitizer: attempting free on address which was not malloc，确认是堆内存释放地址非法错误。

   ```screen
   module name:xxx
   Version:1.0.1
   Pid:37322
   Uid:20020216
   Reason:bad-free
   ==appspawn==37322==AddressSanitizer: WARNING: unexpected format specifier in printf interceptor: %{ (reported once per process)
   =================================================================
   ==appspawn==37322==ERROR: AddressSanitizer: attempting free on address which was not malloc()-ed: 0x00260102d044 in thread T0 (xample.dfx_test)
       #0 0x690d8df164  (/system/lib64/libclang_rt.asan.so+0xdf164) (BuildId: e535b144d2e5a0b26e777a78001e130175ae94be)
       #1 0x6abe7480cc  (/data/storage/el1/bundle/libs/arm64/libentry.so+0x3c80cc) (BuildId: 4df2aaa9582493fb12c1d514bd77091a7113d24f)
       #2 0x6992be7c90  (/system/lib64/platformsdk/libace_napi.z.so+0x67c90) (BuildId: 76bc1ed675edcc5f429a976d6c9b955d)

   0x00260102d044 is located 4 bytes inside of 100-byte region [0x00260102d040,0x00260102d0a4)
   allocated by thread T0 (xample.dfx_test) here:
       #0 0x690d8df2b8  (/system/lib64/libclang_rt.asan.so+0xdf2b8) (BuildId: e535b144d2e5a0b26e777a78001e130175ae94be)
       #1 0x6abe7480bc  (/data/storage/el1/bundle/libs/arm64/libentry.so+0x3c80bc) (BuildId: 4df2aaa9582493fb12c1d514bd77091a7113d24f)
       #2 0x6992be7c90  (/system/lib64/platformsdk/libace_napi.z.so+0x67c90) (BuildId: 76bc1ed675edcc5f429a976d6c9b955d)
       #3 0x7fbfa429f4  (/system/lib64/module/arkcompiler/stub.an+0xe179f4)
       #4 0x7fbf096900  (/system/lib64/module/arkcompiler/stub.an+0x46b900)

   SUMMARY: AddressSanitizer: bad-free (/system/lib64/libclang_rt.asan.so+0xdb870) (BuildId: e535b144d2e5a0b26e777a78001e130175ae94be)
   ```
2. 分析报错栈，确认触发异常位置。

   证据2：

   ```screen
   ==appspawn==37322==ERROR: AddressSanitizer: attempting free on address which was not malloc()-ed: 0x00260102d044 in thread T0 (xample.dfx_test)
       #0 0x690d8df164  (/system/lib64/libclang_rt.asan.so+0xdf164) (BuildId: e535b144d2e5a0b26e777a78001e130175ae94be)
       #1 TriggerInvalidFree(napi_env__*, napi_callback_info__*) at (xxx/entry/src/main/cpp/common/xsan/XsanTest.cpp:236)
       #2 0x6992be7c90  (/system/lib64/platformsdk/libace_napi.z.so+0x67c90) (BuildId: 76bc1ed675edcc5f429a976d6c9b955d)
   ```

   通过llvm-addr2line工具（参考：[C++堆栈解析流程](../harmonyos-guides/ide-exception-stack-parsing-principle.md#section1735713501344)中对于llvm-addr2line的使用）或者DevEco Studio自带的堆栈跟踪分析等工具，完成调用栈#1的符号解析，定位到具体业务代码行。如下图所示，XsanTest.cpp第236行代码触发异常，结合代码确认为执行free((int \*)ptr + 1)时触发的异常。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b1/v3/KA4YPIUdQ6War-3O2LlcPg/zh-cn_image_0000002693605640.png)
3. 分析分配栈，确认非法地址所在已分配内存对象。

   证据3：日志显示，待释放地址0x00260102d044位于一个100字节的已分配内存对象[0x00260102d040, 0x00260102d0a4)内部，相对于对象起始地址向右偏移4字节。

   ```screen
   0x00260102d044 is located 4 bytes inside of 100-byte region [0x00260102d040,0x00260102d0a4)
   allocated by thread T0 (xample.dfx_test) here:
       #0 0x690d8df2b8  (/system/lib64/libclang_rt.asan.so+0xdf2b8) (BuildId: e535b144d2e5a0b26e777a78001e130175ae94be)
       #1 TriggerInvalidFree(napi_env__*, napi_callback_info__*) at (G:/2D-DFXDemo-master/2D-DFXDemo-master/dfx_test/entry/src/main/cpp/common/xsan/XsanTest.cpp:235)
       #2 0x6992be7c90  (/system/lib64/platformsdk/libace_napi.z.so+0x67c90) (BuildId: 76bc1ed675edcc5f429a976d6c9b955d)
       #3 0x7fbfa429f4  (/system/lib64/module/arkcompiler/stub.an+0xe179f4)
       #4 0x7fbf096900  (/system/lib64/module/arkcompiler/stub.an+0x46b900)
   ```

   通过llvm-addr2line工具（参考：[C++堆栈解析流程](../harmonyos-guides/ide-exception-stack-parsing-principle.md#section1735713501344)中对于llvm-addr2line的使用）或者DevEco Studio自带的堆栈跟踪分析等工具，完成调用栈#1的符号解析，定位到具体业务代码行。解析结果如下图所示，可以确认该内存的申请位置位于代码第235行。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/41/v3/9tQ3pZ2zSmmZq-hdFgvFOQ/zh-cn_image_0000002723285071.png)
4. 分析堆内存释放地址非法的控制流路径，如下图所示：
   1. 在函数内定义局部指针对象ptr，并申请100字节内存，并将地址赋值给ptr。
   2. 释放ptr+1指向的非法地址，导致ASan分配器检测到异常。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c/v3/dLFyIwVYQ4KQE17j0aLhlw/zh-cn_image_0000002693765526.png "点击放大")

**问题结论与总结**

根本原因：在函数TriggerInvalidFree()中，free()释放了指针运算偏移后的地址，而非malloc()返回的原始地址。

**修复建议**

修复此类问题时需注意：

谁申请，谁释放，释放的必须是malloc返回的原始地址，偏移运算后的地址不可直接释放。

## GWP-ASan堆内存释放地址非法

### 根因描述

GWP-ASan是一种用于检测堆内存错误的轻量级检测机制。堆内存释放地址非法（Invalid Free）本质上是：程序调用free()、delete、delete[]等释放函数时，传入的地址并非有效的堆内存起始地址。当应用[GWP-ASan使能](bpta-stability-gwpasan-detection.md#section2735718353)后，运行时会对堆内存分配进行采样，将采样对象放入受保护的内存池，并记录对象的起始地址、大小、分配栈和释放栈。当释放地址落在采样对象边界之外，或不是该对象的有效起始地址时，GWP-ASan会生成Invalid (Wild) Free异常日志。

### 问题分析思路

此类问题通常有以下几种可能：

1. 传入野指针导致释放失败。
2. 传入未初始化指针导致释放失败。
3. 传入已释放内存地址导致释放失败（也可能报Double Free）。

问题分析步骤如下：

1. 查看GWP-ASan故障日志，确认故障类型，是否包含关键字Invalid (Wild) Free，若存在则可确认为堆内存释放地址非法问题。
2. 确认非法地址释放位置：xx byte to the left/right of a xx-byte allocation at xxx分别对应非法地址释放位置位于内存地址左侧和右侧两种情况。
3. 确认两个关键调用栈：内存分配栈、内存释放栈，分别通过llvm-addr2line工具（参考：[C++堆栈解析流程](../harmonyos-guides/ide-exception-stack-parsing-principle.md#section1735713501344)中对于llvm-addr2line的使用），定位到具体业务代码行。
4. 还原指针生命周期，确认问题根因。

### 关键字

此类问题确认是堆内存释放地址非法问题后，确认非法地址释放栈（Invalid (Wild) Free at）、分配栈（was allocated），分析业务侧调用栈代码。

### 案例分析

**案例一****：**指针偏移导致堆内存非法释放

**问题现象**

触发业务代码时，应用会生成GWP-ASan故障日志，故障日志显示为Invalid (Wild) Free。

**问题分析**

1. 查看日志内容，确认故障类型。

   证据1：日志中明确打印Invalid (Wild) Free，确认此问题为堆内存释放地址非法。

   ```screen
   Module name:xxx
   Version:1.0.0
   Pid:24914
   Uid:20020211
   Reason:GWP-ASAN
   *** GWP-ASan detected a memory error ***
   Invalid (Wild) Free at 0x5bb1c18fef (1 byte to the left of a 16-byte allocation at 0x5bb1c18ff0) by thread 39823 here:
    #0 0x5b01d4e57c  (/lib/ld-musl-aarch64.so.1+0x14f57c) (BuildId: 0a18abca27f391c78e76aa767de106a3)
    #1 0x5bb59cbb4c  (/data/storage/el1/bundle/libs/arm64/libentry.so+0xbb4c) (BuildId: c9afeef4cf1ebf1e492c5886301054bc0f959cfe)
    #2 0x5b8e730a20  (/system/lib64/platformsdk/libace_napi.z.so+0x70a20) (BuildId: c902a8d91b50f7a25686415edf933520)
    #3 0x5ba828d1e8  (/system/lib64/module/arkcompiler/stub.an+0xe8c1e8)
    #4 0x5ba787edac  (/system/lib64/module/arkcompiler/stub.an+0x47ddac)
   0x5bb1c18fef was allocated by thread 39823 here:
    #0 0x5b01d56308  (/lib/ld-musl-aarch64.so.1+0x157308) (BuildId: 0a18abca27f391c78e76aa767de106a3)
    #1 0x5b01d4e304  (/lib/ld-musl-aarch64.so.1+0x14f304) (BuildId: 0a18abca27f391c78e76aa767de106a3)
    #2 0x5b01d717ec  (/lib/ld-musl-aarch64.so.1+0x1727ec) (BuildId: 0a18abca27f391c78e76aa767de106a3)
    #3 0x5b01dfc4a0  (/lib/ld-musl-aarch64.so.1+0x1fd4a0) (BuildId: 0a18abca27f391c78e76aa767de106a3)
    #4 0x5bb59cbb28  (/data/storage/el1/bundle/libs/arm64/libentry.so+0xbb28) (BuildId: c9afeef4cf1ebf1e492c5886301054bc0f959cfe)
    #5 0x5b8e730a20  (/system/lib64/platformsdk/libace_napi.z.so+0x70a20) (BuildId: c902a8d91b50f7a25686415edf933520)
    #6 0x5ba828d1e8  (/system/lib64/module/arkcompiler/stub.an+0xe8c1e8)
    #7 0x5ba787edac  (/system/lib64/module/arkcompiler/stub.an+0x47ddac)
   Reason:GWP-ASAN
   *** End GWP-ASan report ***
   ```
2. 确认非法地址释放位置。

   证据2：

   ```screen
   Invalid (Wild) Free at 0x5bb1c18fef (1 byte to the left of a 16-byte allocation at 0x5bb1c18ff0) by thread 39823 here:
   ```

   1 byte to the left of表示非法释放地址为内存起始地址0x5bb1c18ff0左侧1字节，即0x5bb1c18fef；若为right则表示内存地址向右偏移1字节处的地址。
3. 确认非法地址释放栈（Invalid (Wild) Free at）和分配栈（was allocated），解析对应代码。

   证据3：

   ```screen
   Invalid (Wild) Free at 0x5bb1c18fef (1 byte to the left of a 16-byte allocation at 0x5bb1c18ff0) by thread 39823 here:
    #0 0x5b01d4e57c  (/lib/ld-musl-aarch64.so.1+0x14f57c) (BuildId: 0a18abca27f391c78e76aa767de106a3)
    #1 0x5bb59cbb4c  (/data/storage/el1/bundle/libs/arm64/libentry.so+0xbb4c) (BuildId: c9afeef4cf1ebf1e492c5886301054bc0f959cfe)
    #2 0x5b8e730a20  (/system/lib64/platformsdk/libace_napi.z.so+0x70a20) (BuildId: c902a8d91b50f7a25686415edf933520)
    #3 0x5ba828d1e8  (/system/lib64/module/arkcompiler/stub.an+0xe8c1e8)
    #4 0x5ba787edac  (/system/lib64/module/arkcompiler/stub.an+0x47ddac)
   ```

   通过llvm-addr2line工具（参考：[C++堆栈解析流程](../harmonyos-guides/ide-exception-stack-parsing-principle.md#section1735713501344)中对于llvm-addr2line的使用）解析栈得出。如下图所示，1号位置为内存分配栈顶，2号位置为非法地址释放栈顶。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b1/v3/EVFWjc63QRSF3HOUGeAYSg/zh-cn_image_0000002723404997.png "点击放大")
4. 还原内存对象生命周期，确认问题根因。

   解析代码后确定，p申请了一块16字节的内存，起始地址为0x5bb1c18ff0，但释放的是p起始地址左侧偏移1字节的非法地址，即0x5bb1c18fef，并非返回的原始地址。

**问题结论与总结**

根本原因：在函数InvalidFreeLeft()中，free()传入了偏移后的非法地址，而非malloc()返回的原始地址，最终导致释放地址非法。

**修复建议**

修复此类问题时需注意：

1. 谁申请，谁释放，释放原始地址。
2. 移动指针使用cursor，所有权指针owner不可移动。
