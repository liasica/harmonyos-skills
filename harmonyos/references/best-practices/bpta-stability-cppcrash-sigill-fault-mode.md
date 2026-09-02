---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-stability-cppcrash-sigill-fault-mode
title: SIGILL非法指令故障模式说明
breadcrumb: 最佳实践 > 稳定性 > 稳定性分析 > 稳定性故障模式说明 > CppCrash故障模式说明 > SIGILL非法指令故障模式说明
category: best-practices
scraped_at: 2026-09-02T15:03:23+08:00
doc_updated_at: 2026-08-26
content_hash: sha256:6c9ac92e1fa6101d34b249f96ab3524638f245245e14b640130139443a211f5e
---

## ILL\_ILLOPC非法操作码异常

### 根因描述

ILL\_ILLOPC是一种非法操作码异常，属于SIGILL信号类型。当CPU尝试执行一个无效或未定义的机器指令时，会触发此异常。

### 问题分析思路

此类问题，通常情况下会有如下几种可能：

**1. 执行了无效指令：例如ud2指令**

示例：无效调试指令。

```cpp
napi_value TriggerUD2Instruction(napi_env env, napi_callback_info info)
{
#if defined(__x86_64__) || defined(__i386__)
    __asm__ __volatile__(".byte 0x0f, 0x0b");  // x86 ud2
#elif defined(__aarch64__)
    __asm__ __volatile__("udf #0");
#endif
    return {};
}
```

备注：CFI检测拦截也会使用此指令，如遇栈帧符号信息包含.cfi内容，按照CFI问题排查分析，CFI检查机制触发信号场景对照表：

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| 信号 | si\_code | 触发场景和机制 | 典型架构/实现 | 底层指令/异常 | 关键特征 |
| SIGTRAP | TRAP\_BRKPT | 软件CFI校验失败 | ARM64(LLVM -fsanitize=cfi配置) | brk #0 | 编译器插入，内核按照断点信号处理 |
| SIGILL | ILL\_ILLOPC | 软件CFI校验失败 | x86\_64/ARM64(udf配置) | ud2/udf #0 | CPU视为非法操作码 |
| SIGILL | ILL\_ILLPACCFI | 硬件CFI后向校验失败 | ARM64 v8.3+ | RETAA/RETAB | 高版本内核专门扩展的si\_code |
| SIGSEGV | SEGV\_CPERR | 硬件前向保护违规 | ARM64(BTI)/x86(CET) | BLR/BR目标无标记/show stack不匹配 | 触发#CP异常 |

**2. 内联汇编嵌入未分配编码或不支持指令**

示例：嵌入汇编未分配编码指令。

```cpp
napi_value TriggerUndefinedInstruction(napi_env env, napi_callback_info info)
{
#if defined(__aarch64__)
    __asm__ __volatile__(".inst 0x00000000");   // AArch64 UDF #0
#elif defined(__x86_64__) || defined(__i386__)
    __asm__ __volatile__(".word 0x0b0f");
#endif
    return {};
}
```

备注：存在部分旧款CPU硬件不支持第三方图形库使用FP16指令（半精度浮点数）。

问题分析的步骤如下：

1. **确****认类型：**查看CppCrash故障日志中的Reason字段，确认信号为SIGILL(ILL\_ILLOPC)。
2. **分析PC地址值：**关注崩溃地址（PC值）是否在代码段地址范围。
3. **地址是否4字节对齐：**关注PC对应地址是否4字节对齐。
4. **指令有效性排查：**是否为当前CPU架构支持指令，是否为有效指令。

### 关键字

关注CppCrash故障日志中是否有如下关键字。

* SIGILL
* ILL\_ILLOPC

### 案例分析

**案例一：无效指令触发故障**

**问题现象**

应用异常崩溃退出，生成CppCrash故障文件。

**问题分析**

1. 查看崩溃文件内容。

   **说明** 

   DevEco Studio成功连接手机时，可打开日志窗口找到FaultLog选项，点击即可查看崩溃日志。

   证据1：信号类型为SIGILL(ILL\_ILLOPC)。

   ```screen
   Pid:40168
   Uid:20020206
   Process name:com.huawei.cppcrashanalysis
   App running unique id:1975637108740622813
   Process life time:9s
   Process Memory(kB): 113418(Rss)
   Device Memory(kB): Total 11699072, Free 283332, Available 5270528
   Reason:Signal:SIGILL(ILL_ILLOPC)@000000000000000000 
   Fault thread info:
   Tid:40168, Name:ppcrashanalysis
   #00 pc 00000000000286b0 /data/storage/el1/bundle/libs/arm64/libentry.so(TriggerUD2Instruction(napi_env__*, napi_callback_info__*)+12)(4687a4d714038f89c2e644d7b764097814597256)
   #01 pc 000000000005dad0 /system/lib64/platformsdk/libace_napi.z.so(panda::JSValueRef ArkNativeFunctionCallBack<true>(panda::JsiRuntimeCallInfo*)+236)(5ffe53d5891bfb79f68f6847054f0899)
   #02 pc 0000000000e871e8 /system/lib64/module/arkcompiler/stub.an(RTStub_PushCallArgsAndDispatchNative+40)
   #03 pc 00000000005976cc /system/lib64/module/arkcompiler/stub.an(BCStub_HandleCallthis0withnameImm8Id16V8StwCopy+400)
   ```
2. 确认PC地址是否在代码段地址范围。

   证据2：地址范围处于libentry.so的可执行代码段范围。

   ```screen
   Registers:
   x0:0000005a16258000 x1:0000007ea9ccb4c0 x2:0000005a0b69d9e4 x3:0001000000000000
   x4:0000000000000003 x5:0000007ea9ccb4d0 x6:000000000000000d x7:00000000ffffffff
   x8:0000000000000000 x9:0000000000000000 x10:0000000000010000 x11:000000251f8727f8
   x12:0000000000000008 x13:0000000000001b00 x14:00000000000001e9 x15:0000000000000018
   x16:0000005a0b6e3fb0 x17:0000005a07908c30 x18:00000000000001d3 x19:0000005a1ad9c000
   x20:0000005a16258000 x21:0000005a2e7e86a4 x22:0000007ea9ccb4c0 x23:0000000000000000
   x24:0000000000000136 x25:0000005a0b6e6be0 x26:0000007ea9ccb2b0 x27:00000059fbcee780
   x28:0000000000000000 x29:0000007ea9ccb440
   lr:0000005a0b69dad4 sp:0000007ea9ccb200 pc:0000005a2e7e86b0
   pstate:0000000080001000 esr:0000000000000000
   ... 
   maps：
   5a2e7c0000-5a2e7d7000 r--p 00000000 /data/storage/el1/bundle/libs/arm64/libentry.so
   5a2e7d7000-5a2e804000 r-xp 00016000 /data/storage/el1/bundle/libs/arm64/libentry.so
   5a2e804000-5a2e806000 r--p 00042000 /data/storage/el1/bundle/libs/arm64/libentry.so
   5a2e806000-5a2e807000 rw-p 00043000 /data/storage/el1/bundle/libs/arm64/libentry.so
   ```
3. 确认地址值是否4字节对齐。

   证据3：0000005a2e7e86b0是4字节对齐地址。
4. 反编译libentry.so分析汇编代码指令有效性。

   证据4：对应指令DCD 0x3C00B0F，0F是双字节操作码，0B是扩展操作码，组合表示UD2(Undefined Operation)指令，属于无效指令。

   ```screen
   .text:0000000000092AEC      DCD 0x3C00B0F
   ```

   参考[C++堆栈解析流程](../harmonyos-guides/ide-exception-stack-parsing-principle.md#section1735713501344)使用llvm-addr2line工具定位到对应代码位置。

   ```cpp
   napi_value TriggerUD2Instruction(napi_env env, napi_callback_info info)
   {
   #if defined(__x86_64__) || defined(__i386__)
       __asm__ __volatile__(".byte 0x0f, 0x0b");  // x86 ud2
   #elif defined(__aarch64__)
       __asm__ __volatile__("udf #0");
   #endif
       return {};
   }
   ```

**问题结论与总结**

在执行的代码中插入了UD2无效指令，应用通过这种方式触发ILLOPC故障。

**修复建议**

清理无效汇编指令代码。

**案例二：未分配编码指令触发故障**

**问题现象**

构造非法指令故障，应用退出，生成CppCrash故障文件。

**问题分析**

1. 查看崩溃文件内容。

   **说明** 

   DevEco Studio成功连接手机时，可打开日志窗口找到FaultLog选项，点击即可查看崩溃日志。

   证据1：信号类型为SIGILL(ILL\_ILLOPC)。

   ```screen
   Pid:40645
   Uid:20020206
   Process name:com.huawei.cppcrashanalysis
   App running unique id:16554467495764280840
   Process life time:27s
   Process Memory(kB): 80236(Rss)
   Device Memory(kB): Total 11699072, Free 464960, Available 5491712
   Reason:Signal:SIGILL(ILL_ILLOPC)@000000000000000000 
   Fault thread info:
   Tid:40645, Name:ppcrashanalysis
   #00 pc 00000000000286cc /data/storage/el1/bundle/libs/arm64/libentry.so(TriggerUndefinedInstruction(napi_env__*, napi_callback_info__*)+12)(4687a4d714038f89c2e644d7b764097814597256)
   #01 pc 000000000005dad0 /system/lib64/platformsdk/libace_napi.z.so(panda::JSValueRef ArkNativeFunctionCallBack<true>(panda::JsiRuntimeCallInfo*)+236)(5ffe53d5891bfb79f68f6847054f0899)
   #02 pc 0000000000e871e8 /system/lib64/module/arkcompiler/stub.an(RTStub_PushCallArgsAndDispatchNative+40)
   #03 pc 00000000005976cc /system/lib64/module/arkcompiler/stub.an(BCStub_HandleCallthis0withnameImm8Id16V8StwCopy+400)
   ```
2. 确认PC地址是否在代码段地址范围。

   证据2：地址范围处于libentry.so的可执行代码段范围。

   ```screen
   Registers:
   x0:0000005a16258000 x1:0000007ea9ccb4c0 x2:0000005a0b69d9e4 x3:0001000000000000
   x4:0000000000000003 x5:0000007ea9ccb4d0 x6:000000000000000d x7:00000000ffffffff
   x8:0000000000000000 x9:0000000000000000 x10:0000000000010000 x11:000000251f872038
   x12:0000000000000008 x13:0000000000001b00 x14:00000000000001e9 x15:0000000000000018
   x16:0000005a0b6e3fb0 x17:0000005a07908c30 x18:00000000000001d3 x19:0000005a1ad9c000
   x20:0000005a16258000 x21:0000005a2e5686c0 x22:0000007ea9ccb4c0 x23:0000000000000000
   x24:0000000000000136 x25:0000005a0b6e6be0 x26:0000007ea9ccb2b0 x27:00000059fbcee780
   x28:0000000000000000 x29:0000007ea9ccb440
   lr:0000005a0b69dad4 sp:0000007ea9ccb200 pc:0000005a2e5686cc
   pstate:0000000080001000 esr:0000000000000000
   ...
   maps：
   5a2e540000-5a2e557000 r--p 00000000 /data/storage/el1/bundle/libs/arm64/libentry.so
   5a2e557000-5a2e584000 r-xp 00016000 /data/storage/el1/bundle/libs/arm64/libentry.so
   5a2e584000-5a2e586000 r--p 00042000 /data/storage/el1/bundle/libs/arm64/libentry.so
   5a2e586000-5a2e587000 rw-p 00043000 /data/storage/el1/bundle/libs/arm64/libentry.so
   ```
3. 确认地址值是否4字节对齐。

   证据3：0000005a2e5686cc是4字节对齐地址。
4. 反编译libentry.so分析汇编代码指令有效性。

   证据4：对应指令DCD 0，未分配编码的无效指令。

   ```screen
   .text:0000000000092AEC      DCD 0
   ```

   参考[C++堆栈解析流程](../harmonyos-guides/ide-exception-stack-parsing-principle.md#section1735713501344)使用llvm-addr2line工具找到对应代码位置。

   ```cpp
   napi_value TriggerUndefinedInstruction(napi_env env, napi_callback_info info)
   {
   #if defined(__aarch64__)
       __asm__ __volatile__(".inst 0x00000000");   // AArch64 UDF #0
   #elif defined(__x86_64__) || defined(__i386__)
       __asm__ __volatile__(".word 0x0b0f");
   #endif
       return {};
   }
   ```

**问题结论与总结**

在执行的代码中插入了未分配编码指令，示例代码通过这种方式触发ILLOPC故障。

**修复建议**

清理无效汇编指令代码。

### 常见易错代码预防建议

1. 开启编译选项CMAKE\_C\_FLAGS="-march=armv8-a"，锁定硬件架构与编译，拦截指令集架构不匹配问题。
2. 代码静态分析，禁用内联汇编，使用NDK API，避免嵌入无效指令。
