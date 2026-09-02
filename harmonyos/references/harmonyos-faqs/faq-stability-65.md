---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faq-stability-65
title: 应用闪退-Native运行时崩溃（CppCrash）信号与定位指导
breadcrumb: FAQ > 应用质量 > 技术质量 > 稳定性 > 应用闪退-Native运行时崩溃（CppCrash）信号与定位指导
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:50+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:f1c89bb339d764e6023eb0fd6eaf98eaf5f1ac434a7d2c382a3deb2fab9e3590
---

## 问题现象

应用在使用过程中出现闪退，系统日志或FaultLog中生成以cppcrash命名的故障日志文件。

## 背景知识

* CppCrash进程崩溃检测基于操作系统信号机制，目前支持的崩溃信号参考[Cpp Crash（进程崩溃）检测](../harmonyos-guides/cppcrash-guidelines.md)。
* CppCrash日志规格说明可以参考[日志规格](../harmonyos-guides/cppcrash-guidelines.md#日志规格)。

| 崩溃信号 | 崩溃错误码 | 故障根因 | 关键字段 | 解决方案 |
| --- | --- | --- | --- | --- |
| SIGABRT | SI\_TKILL | 断言检查失败 | LastFatalMessage:Assertion failed | 检查代码运行时的断言条件，修复业务逻辑异常。 |
| SIGABRT | SI\_TKILL | 未处理抛出的异常 | terminating due to uncaught exception of type | 在抛出异常的位置使用try-catch捕获并处理异常。 |
| SIGABRT | SI\_TKILL | 调用napi\_fatal\_error引发致命错误 | LastFatalMessage:[(xxx)(napi\_fatal\_error)] FATAL ERROR | 排查napi\_fatal\_error的调用逻辑是否符合预期。 |
| SIGSEGV | SEGV\_MAPERR | 空指针解引用 | probably caused by NULL pointer dereference | 排查代码中的指针变量，是否存在使用未初始化、赋值为空或已释放的指针。 |
| SIGSEGV | SEGV\_ACCERR | 访问越栈内存上界 | probably caused by stack-buffer-overflow | 排查递归调用时未设置递归终止条件导致栈内存耗尽；局部变量占用过多栈内存导致栈内存耗尽；在信号栈中使用超过系统限制的栈内存。 |

## 问题定位

进程在Native层发生崩溃后，系统会抓取崩溃相关的信息，在faultlogger目录下生成cppcrash-应用包名-应用UID-发生时间.log崩溃日志并上报崩溃事件，以供开发者分析定位。CppCrash日志规格说明可以参考[日志规格](../harmonyos-guides/cppcrash-guidelines.md#日志规格)。

**步骤一：获取cppcrash-应用包名-应用UID-发生时间.log故障日志。**

* 开发态：DevEco Studio会自动收集到日志工具栏的FaultLog下，该工具有高亮关键信息、跳转到对应的代码行、以及结构化日志等方便开发者分析的功能，详情可见使用文档[FaultLog](../harmonyos-guides/ide-fault-log.md)。
* 运维态：
  + 直接导出故障日志目录：必须先打开开发者模式，再执行命令hdc file recv /data/log/faultlog/faultlogger/ [本地目录]。
  + 使用HiAppEvent故障订阅接口：可记录应用运行过程中的故障，为应用开发者提供的事件打点机制，详见[HiAppEvent介绍](../harmonyos-guides/hiappevent-intro.md)和[崩溃事件介绍](../harmonyos-guides/hiappevent-watcher-crash-events.md)。

**步骤二：分析故障原因Reason和崩溃堆栈Stack。**

**Reason字段规格如下：**

一般规格包含崩溃类型Signal、崩溃地址和信号发送方信息，Signal信号的含义可见[基本概念](../harmonyos-guides/cppcrash-guidelines.md#基本概念)和[实现原理](../harmonyos-guides/cppcrash-guidelines.md#实现原理)。

```txt
Reason:Signal:SIGABRT(SI_TKILL)@0x01317bc900000a02 from:2562:20020169
字段解释如下：
Reason:Signal:信号值(tkill()函数信号)@崩溃地址 from:发送信号的Pid:发送信号的Uid
```

**堆栈日志规格如下：**

崩溃堆栈搜索关键字Fault thread info。

堆栈日志打印上限为256个栈帧，超出部分不打印。

```txt
Fault thread info:
#00 pc 00000000001b0958 /system/lib/ld-musl-aarch64.so.1(raise+216)(52299a28d60f0bb4073bd788bc023a3a)
#<序号> pc <pc在段内的偏移> <pc属于的段名称(函数名+函数内偏移的字节数)(BuildID)>

pc：程序计数器（Program Counter）的缩写，作用是储存当前程序正在执行指令的地址。
BuildID：是用于标识二进制文件的唯一标识符。
```

**问题场景如下：**

1. 场景一：断言检查失败。
   * 关键字：LastFatalMessage:Assertion failed。
   * 定位：调试代码，检查断言条件中变量的值是否符合预期。
2. 场景二：未处理抛出的异常。
   * 关键字：terminating due to uncaught exception of type。
   * 定位：定位抛出异常的代码行，检查抛出异常的业务逻辑是否符合预期。
3. 场景三：调用napi\_fatal\_error引发致命错误。
   * 关键字：LastFatalMessage:[(xxx)(napi\_fatal\_error)] FATAL ERROR
   * 定位：排查napi\_fatal\_error的调用逻辑是否符合预期。
4. 场景四：空指针解引用。
   * 关键字：probably caused by NULL pointer dereference
   * 定位：排查代码中的指针变量，是否存在使用未初始化、赋值为空或已释放的指针。
5. 场景五：访问越栈内存上界。
   * 关键字：current thread stack low address = 0x0000005b479ef000, probably caused by stack-buffer-overflow
   * 定位：排查代码逻辑是否存在以下三种栈溢出场景。
     + 递归调用时未设置递归终止条件导致栈内存耗尽。
     + 局部变量占用过多栈内存导致栈内存耗尽。
     + 在信号栈中使用超过系统限制的栈内存。

**步骤三：结合业务代码分析根因。**

* 堆栈定位代码行：
  + 开发态环境下，DevEco Studio生成的CppCrash调用栈支持直接跳转到代码行，详情可见使用文档[跳转至引起错误的代码行](../harmonyos-guides/ide-fault-log.md#section26629489166)。
  + 运维态的日志，可以使用hstack工具将Release应用混淆的调用栈还原为源码对应调用栈。详情可见[堆栈解析工具（hstack）](../harmonyos-guides/ide-command-line-hstack.md)。
  + 可能存在部分未能解析跳转到对应行号的栈帧，可以使用llvm-addr2line工具将函数地址解析成文件名或行号，详情参考[C++堆栈解析流程](../harmonyos-guides/ide-exception-stack-parsing-principle.md#section1735713501344)。
* 代码调试：
  + 开发态：DevEco Studio提供了丰富的调试能力，支持跨语言和三方库调试，详情可见[Native代码调试](../harmonyos-guides/ide-debug-native.md)。
  + 运维态：建议使用HiAppEvent[事件订阅](../harmonyos-guides/hiappevent.md)和hilog[日志打印](../harmonyos-guides/hilog-dev.md)，再次发生CppCrash时，打印关键信息。

**步骤四：异常崩溃场景排查地址越界(可选)。**

如果多次崩溃产生了随机的崩溃调用栈，或堆栈指向的代码不应该发生此崩溃信号，则可能发生了地址越界，此时的崩溃栈已非第一现场，需要使用HWASan等内存检测工具，调试压测抓取第一现场的堆栈，详情参考[地址越界类问题分析方法](../best-practices/bpta-stability-address-illegal-way.md)。

## 分析结论

* 断言检查失败：断言条件为false时，进程会直接终止。
* 未处理抛出的异常：未处理抛出的异常导致应用闪退。
* 调用napi\_fatal\_error引发致命错误：进程主动调用napi\_fatal\_error引发致命错误导致应用闪退。
* 空指针解引用：空指针解引用，访问到空内存地址导致崩溃。
* 访问越栈内存上界：进程栈内存溢出导致应用闪退。

## 修改建议

* 业务逻辑异常：使用[堆栈解析工具（hstack）](../harmonyos-guides/ide-command-line-hstack.md)解析崩溃栈后结合具体代码进行分析。
* 内存异常：[使用HWASan检测内存错误](../best-practices/bpta-stability-hwasan-detection.md)，获取运行时的内存栈信息，分析并修复引起内存错误的代码。
* 多线程异常：启用[方舟运行时检测](../best-practices/bpta-stability-ark-runtime-detection.md)，获取多线程安全问题产生的日志信息，跳转至对应代码分析并修复。
