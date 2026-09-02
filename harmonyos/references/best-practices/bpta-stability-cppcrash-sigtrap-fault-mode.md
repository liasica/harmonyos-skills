---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-stability-cppcrash-sigtrap-fault-mode
title: SIGTRAP断点或陷阱异常故障模式说明
breadcrumb: 最佳实践 > 稳定性 > 稳定性分析 > 稳定性故障模式说明 > CppCrash故障模式说明 > SIGTRAP断点或陷阱异常故障模式说明
category: best-practices
scraped_at: 2026-09-02T15:03:23+08:00
doc_updated_at: 2026-09-02
content_hash: sha256:72ec20bb3bba86cd2c4e6dbce73c84766c9a403a37e132a0b1c6eeab6a630411
---

## TRAP\_BRKPT软件断点

### 根因描述

TRAP\_BRKPT是SIGTRAP信号的一种类型，通常由软件断点指令触发。在正常调试场景下这是预期行为；但在非调试环境中触发时往往预示着更深层次的系统或代码问题。

### 问题分析思路

此类问题，通常情况下，会有如下几种可能：

1. 模块内使用断言机制触发断言失败。

2. 模块检测机制使用BRKPT信号检测异常，常见有jemalloc的Double Free和CFI后向检测机制。

备注：CFI检测拦截也会使用此指令，如遇栈帧符号信息包含.cfi内容，按照CFI问题排查分析，CFI检查机制触发信号场景对照表：

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| 信号 | si\_code | 触发场景和机制 | 典型架构/实现 | 底层指令/异常 | 关键特征 |
| SIGTRAP | TRAP\_BRKPT | 软件CFI校验失败 | ARM64(LLVM -fsanitize=cfi配置) | brk #0 | 编译器插入，内核按照断点信号处理 |
| SIGILL | ILL\_ILLOPC | 软件CFI校验失败 | x86\_64/ARM64(udf配置) | ud2/udf #0 | CPU视为非法操作码 |
| SIGILL | ILL\_ILLPACCFI | 硬件CFI后向校验失败 | ARM64 v8.3+ | RETAA/RETAB | 高版本内核专门扩展的si\_code |
| SIGSEGV | SEGV\_CPERR | 硬件前向保护违规 | ARM64(BTI)/x86(CET) | BLR/BR 目标无标记/show stack不匹配 | 触发#CP异常 |

问题分析的步骤如下：

1. **确认类型：**查看CppCrash日志中的Reason字段，确认信号为SIGTRAP(TRAP\_BRKPT)。
2. **分析崩溃堆栈：**反编译首帧地址的汇编指令是否为BRK指令（arm64架构为BRK指令，arm32为BKPT指令，x86为INT3指令）。
3. **定位代码位置：**参考[C++堆栈解析流程](../harmonyos-guides/ide-exception-stack-parsing-principle.md#section1735713501344)使用llvm-addr2line工具定位行号，结合代码走读分析，何处触发BRK指令。
4. **确认BRK原因：** 分析使用断言或者采用BRKPT触发信号的模块机制。

### 关键字

关注CppCrash故障日志中是否有如下关键字。

* SIGTRAP
* TRAP\_BRKPT

### 案例分析

**案例一：构造触发BRKPT故障**

**问题现象**

应用崩溃退出。

**问题分析**

1. 查看崩溃文件内容。

   **说明** 

   DevEco Studio成功连接手机时，可打开日志窗口找到FaultLog选项，点击即可查看崩溃日志。

   证据1: 确认信号为SIGTRAP(TRAP\_BRKPT)。

   ```screen
   Pid:40974
   Uid:20020206
   Process name:com.huawei.cppcrashanalysis
   App running unique id:6954091671400091859
   Process life time:24s
   Process Memory(kB): 80670(Rss)
   Device Memory(kB): Total 11699072, Free 574140, Available 5592064
   Reason:Signal:SIGTRAP(TRAP_BRKPT)@0x0000005a2e7a86e8
   Fault thread info:
   Tid:40974, Name:ppcrashanalysis
   #00 pc 00000000000286e8 /data/storage/el1/bundle/libs/arm64/libentry.so(TriggerBrkInstruction(napi_env__*, napi_callback_info__*)+12)(4687a4d714038f89c2e644d7b764097814597256)
   #01 pc 000000000005dad0 /system/lib64/platformsdk/libace_napi.z.so(panda::JSValueRef ArkNativeFunctionCallBack<true>(panda::JsiRuntimeCallInfo*)+236)(5ffe53d5891bfb79f68f6847054f0899)
   #02 pc 0000000000e871e8 /system/lib64/module/arkcompiler/stub.an(RTStub_PushCallArgsAndDispatchNative+40)
   #03 pc 00000000005976cc /system/lib64/module/arkcompiler/stub.an(BCStub_HandleCallthis0withnameImm8Id16V8StwCopy+400)
   ```
2. 反编译查看汇编指令。

   证据2：反汇编确认为BRK指令。

   ```screen
   .text:00000000000286E4                 BL              .puts
   .text:00000000000286E8                 BRK             #0
   .text:00000000000286EC                 ADRP            X0, #unk_4078A@PAGE
   ```
3. 参考[C++堆栈解析流程](../harmonyos-guides/ide-exception-stack-parsing-principle.md#section1735713501344)使用llvm-addr2line工具定位行号。

   证据3：找到对应的代码位置。

   ```screen
   ./clang/ohos/linux-x86_64/llvm/bin/llvm-addr2line -Cife ../libentry.so 286e8
   ```

   对应代码：

   ```cpp
   napi_value TriggerBrkInstruction(napi_env env, napi_callback_info info)
   {
   #if defined(__aarch64__)
       __asm__ __volatile__(".word 0xD4200000\n" ::: "memory");  // AArch64 brk #0
   #elif defined(__x86_64__) || defined(__i386__)
       __asm__ __volatile__(".byte 0xcc" ::: "memory");           // x86 int3
   #endif
       return {};
   }
   ```
4. 分析代码确认触发BRK原因。

   证据4：此处为直接调用内联汇编触发的BRK指令。

**问题结论与总结**

主动触发BRK指令构造的故障。

**修复建议**

清理删除BRK汇编指令代码。

**案例二：触发Double Free故障**

**问题现象**

应用崩溃退出。

**问题分析**

1. 查看崩溃文件内容。

   **说明** 

   DevEco Studio成功连接手机时，可打开日志窗口找到FaultLog选项，点击即可查看崩溃日志。

   证据1: 确认信号为SIGTRAP(TRAP\_BRKPT)。

   ```screen
   Pid:41223
   Uid:20020206
   Process name:com.huawei.cppcrashanalysis
   App running unique id:1183172198104424633
   Process life time:52s
   Process Memory(kB): 97828(Rss)
   Device Memory(kB): Total 11699072, Free 640984, Available 5668864
   Reason:Signal:SIGTRAP(TRAP_BRKPT)@0x00000059fbb88908 
   LastFatalMessage:This is an unexpected memory usage behavior.may double free
   Fault thread info:
   Tid:41223, Name:ppcrashanalysis
   #00 pc 00000000000b9908 /system/lib/ld-musl-aarch64.so.1(cache_bin_dalloc_safety_checks+108)(f9a4c305648402bdc0bcb0933fea9780)
   #01 pc 00000000000c6160 /system/lib/ld-musl-aarch64.so.1(je_free+408)(f9a4c305648402bdc0bcb0933fea9780)
   #02 pc 000000000002874c /data/storage/el1/bundle/libs/arm64/libentry.so(TriggerDoubleFreeTrap(napi_env__*, napi_callback_info__*)+84)(4687a4d714038f89c2e644d7b764097814597256)
   #03 pc 000000000005dad0 /system/lib64/platformsdk/libace_napi.z.so(panda::JSValueRef ArkNativeFunctionCallBack<true>(panda::JsiRuntimeCallInfo*)+236)(5ffe53d5891bfb79f68f6847054f0899)
   #04 pc 0000000000e871e8 /system/lib64/module/arkcompiler/stub.an(RTStub_PushCallArgsAndDispatchNative+40)
   #05 pc 00000000005976cc /system/lib64/module/arkcompiler/stub.an(BCStub_HandleCallthis0withnameImm8Id16V8StwCopy+400)
   ```
2. 反编译查看汇编指令。

   证据2：反汇编确认为BRK指令。

   ```screen
   .text:00000000000B9908 loc_B9908                               ; CODE XREF: cache_bin_dalloc_safety_checks+94↓j
   .text:00000000000B9908                                         ; cache_bin_dalloc_safety_checks+A0↓j
   .text:00000000000B9908                 BRK             #1
   .text:00000000000B9908
   ```
3. 参考[C++堆栈解析流程](../harmonyos-guides/ide-exception-stack-parsing-principle.md#section1735713501344)使用llvm-addr2line工具确认代码位置。

   证据3：找到对应的代码位置。

   ```screen
   ./clang/ohos/linux-x86_64/llvm/bin/llvm-addr2line -Cife ../libc.so b9908
   crash_brk
   cache_bin_dalloc_safety_checks
   ```
4. 继续向下推导调用栈代码位置，分析代码确认触发BRK原因。

   证据4：此处为jemalloc的Double Free检测机制。找到代码Double Free的位置。

   ```screen
   #00 pc 00000000000b9908 /system/lib/ld-musl-aarch64.so.1(cache_bin_dalloc_safety_checks+108)(f9a4c305648402bdc0bcb0933fea9780)
   #01 pc 00000000000c6160 /system/lib/ld-musl-aarch64.so.1(je_free+408)(f9a4c305648402bdc0bcb0933fea9780)
   #02 pc 000000000002874c /data/storage/el1/bundle/libs/arm64/libentry.so(TriggerDoubleFreeTrap(napi_env__*, napi_callback_info__*)+84)(4687a4d714038f89c2e644d7b764097814597256)
   ```

   查看02帧函数代码逻辑，分析其触发Double Free的逻辑。

   ```cpp
   napi_value TriggerDoubleFreeTrap(napi_env env, napi_callback_info info)
   {
       mallopt(M_OHOS_CONFIG, M_TCACHE_PERFORMANCE_MODE);
       mallopt(M_OHOS_CONFIG, M_ENABLE_OPT_TCACHE);
       mallopt(M_SET_THREAD_CACHE, M_THREAD_CACHE_ENABLE);
       char* test = (char*)malloc(128);
       free(test);
       free(test);
       return {};
   }
   ```

**问题结论与总结**

LastFatalMessage字段信息中已标明存在内存重复释放问题，后续修复内存重复释放代码。

**修复建议**

释放指针赋值为nullptr，增加重复释放校验, 删除重复释放。

### 常见易错代码预防建议

1. 清理调试代码，常见有\_\_asm\_\_()类的BRK指令，或者\_\_builtin\_trap()函数。
2. 严格管理断言assert()使用，尽量避免在release模式下开启。
3. 代码静态分析，检查内存申请和释放行为，避免重复释放内存逻辑。
4. 开启CFI配置编译，检查函数的跳转以及间接调用等是否符合CFI安全要求。
