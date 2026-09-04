---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cppcrash-guidelines
title: Cpp Crash（进程崩溃）检测
breadcrumb: 指南 > 系统 > 调测调优 > Performance Analysis Kit（性能分析服务） > 故障检测 > 崩溃检测 > Cpp Crash（进程崩溃）检测
category: harmonyos-guides
scraped_at: 2026-09-05T06:14:38+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:eb600c32155ff070b821408141a6b1ca5d56e79e99cf55c871da63c48445f4c3
---

## 简介

进程发生崩溃后，系统首先感知到崩溃，然后抓取崩溃相关的信息，最后生成崩溃日志并上报崩溃事件，为开发者提供详细的维测日志以辅助故障定位。本文分为基本概念、实现原理、约束与限制、日志获取、日志规格五个小节介绍系统提供的CppCrash检测方法。开发者如果想进一步了解如何分析CppCrash问题，请参见[CppCrash类问题分析方法](../best-practices/bpta-stability-app-crash-cpp-way.md)。

## 基本概念

* **信号**

  信号是兼容POSIX的操作系统中进程间通讯的一种方式。
* **信号处理函数**

  定义了进程在接收到信号之后进行一系列处理操作的函数，信号处理函数明确需要处理的信号。
* **pc**

  全称Program Counter（程序计数器），存储当前程序正在执行指令的地址。
* **lr**

  全称Link Register（链接寄存器），存储子程序的返回地址。
* **sp**

  全称Stack Pointer（堆栈指针寄存器），存储当前函数栈帧的栈顶地址。
* **fp**

  全称Frame Pointer（栈帧指针寄存器），存储当前函数栈帧的栈底地址。
* **调用栈**

  记录每个线程从开始到执行当前现场（如崩溃现场）整个过程中函数调用顺序。
* **寄存器**

  CPU中高速存储单元用于存储计算机程序执行过程中所需的数据、指令地址或状态信息。本文中，寄存器信息是指崩溃时保存在高速存储单元中的数据、指令地址或状态信息。

## 实现原理

系统检测进程崩溃的流程如下：

1. 进程在运行时发生崩溃，会收到来自内核发送的崩溃信号，由进程在启动时注册的信号处理模块进行处理。
2. 进程接收到崩溃信号后，保存当前进程上下文，并fork出子进程执行ProcessDump二进制抓取崩溃信息。
3. ProcessDump进程将崩溃日志数据写入到临时目录下进行存储。
4. ProcessDump进程收集完崩溃日志后，上报给维测进程Hiview，并补充仅Hiview有权限获取的部分信息（如整机内存状态、应用页面切换轨迹），然后将崩溃日志存储到“/data/log/faultlog/faultlogger”目录下并生成故障事件。

### 系统处理的崩溃信号

系统的进程崩溃检测能力主要基于POSIX信号机制，目前支持对以下崩溃信号的处理：

| 信号值(signo) | 信号 | 解释 | 触发原因 |
| --- | --- | --- | --- |
| 4 | SIGILL | 非法指令 | 进程执行了非法、格式错误、未知或特权指令。 |
| 5 | SIGTRAP | 断点或陷阱异常 | 异常或trap指令发生。 |
| 6 | SIGABRT | 进程终止 | 进程异常终止，通常为进程自身调用标准函数库的abort()函数。 |
| 7 | SIGBUS | 非法内存访问 | 进程访问了未对齐或者不存在的物理地址。 |
| 8 | SIGFPE | 浮点异常 | 进程执行了错误的算术运算，如除数为0、浮点溢出、整数溢出等。 |
| 11 | SIGSEGV | 无效内存访问 | 进程访问了无效内存。 |
| 16 | SIGSTKFLT | 栈错误 | 处理器执行了错误的栈操作，如栈空时弹出、栈满时压入。  SIGSTKFLT信号不支持生成minidump。 |
| 31 | SIGSYS | 错误系统调用 | 系统调用时使用了错误或非法参数。 |

以上系统处理的崩溃信号，根据错误码（code）还有二级分类，二级分类如下：

### SIGILL崩溃类型

SIGILL是一个在Unix和类Unix操作系统中的信号，它表示非法指令异常。SIGILL信号通常由以下几种类型的问题场景引起：

| 错误码（code） | 信号字符串 | 解释 | 触发原因 |
| --- | --- | --- | --- |
| 1 | ILL\_ILLOPC | 非法操作码异常 | 发生在执行不被CPU支持的指令或者无效指令时。 |
| 2 | ILL\_ILLOPN | 非法操作数异常 | 发生在指令使用了不正确的操作数，或者是操作数的类型不正确时。 |
| 3 | ILL\_ILLADR | 非法地址异常 | 发生在程序尝试访问无效的内存地址时，或者是在尝试执行未对齐的内存访问时。 |
| 4 | ILL\_ILLTRP | 非法陷阱异常 | 发生在程序尝试执行一个非法的陷阱指令时，或者是在尝试执行一个未定义的操作时。 |
| 5 | ILL\_PRVOPC | 特权操作码异常 | 发生在普通用户尝试执行特权指令时。 |
| 6 | ILL\_PRVREG | 特权寄存器异常 | 发生在普通用户尝试访问特权寄存器时。 |
| 7 | ILL\_COPROC | 协处理器异常 | 发生在程序尝试使用未定义的协处理器指令时。 |
| 8 | ILL\_BADSTK | 无效的堆栈异常 | 发生在程序尝试在无效的堆栈地址上执行操作时，或者是在堆栈溢出时。 |
| 0xacac | ILL\_ILLPACCFI | 指针校验异常 | 发生在程序校验指针失败时。 |

### SIGTRAP崩溃类型

SIGTRAP信号通常用于调试和跟踪程序的执行。下面是SIGTRAP信号类别的问题场景介绍：

| 错误码（code） | 信号字符串 | 解释 | 触发原因 |
| --- | --- | --- | --- |
| 1 | TRAP\_BRKPT | 软件断点 | 由软件断点引起的，当程序执行到设置的断点时会触发该信号。软件断点通常用于调试程序，可以在程序的关键位置设置断点，以便在调试时暂停程序的执行并检查变量值等信息。 |
| 2 | TRAP\_TRACE | 单步调试 | 由单步执行引起的，当程序执行单个指令时会触发该信号。单步执行通常用于调试程序，可以逐步执行程序并检查每个指令的执行结果。 |
| 3 | TRAP\_BRANCH | 分支跟踪 | 由分支指令引起的，当程序执行分支指令时会触发该信号。分支指令通常用于控制程序的执行流程，例如if语句和循环语句等。 |
| 4 | TRAP\_HWBKPT | 硬件断点 | 由硬件断点引起的，当程序执行到设置的硬件断点时会触发该信号。硬件断点通常用于调试程序，可以在程序的关键位置设置断点，以便在调试时暂停程序的执行并检查变量值等信息。与软件断点不同的是，硬件断点是由CPU硬件实现的，因此可以在程序执行过程中实时检测断点是否被触发。 |

### SIGBUS崩溃类型

SIGBUS是一种由操作系统向进程发送的信号，通常表示内存访问错误。其中，不同的信号类别表示不同的错误场景：

| 错误码（code） | 信号字符串 | 解释 | 触发原因 |
| --- | --- | --- | --- |
| 1 | BUS\_ADRALN | 内存地址对齐错误 | 发生在尝试访问未对齐的内存地址时，例如尝试访问一个4字节整数的非偶数地址。 |
| 2 | BUS\_ADRERR | 非法内存地址错误 | 发生在尝试访问不属于进程地址空间的内存地址时，例如尝试访问一个空指针。 |
| 3 | BUS\_OBJERR | 对象访问错误 | 发生在尝试访问一个已经被删除或未初始化的对象时。 |
| 4 | BUS\_MCEERR\_AR | 需立即处理的硬件内存校验错误 | 发生在访问内存时检测到需要立即处理的硬件内存错误。 |
| 5 | BUS\_MCEERR\_AO | 可等待或延迟处理的硬件内存校验错误 | 发生在访问内存时检测到可等待或延迟处理的硬件内存错误。 |

### SIGFPE崩溃类型

SIGFPE是一个信号，它表示浮点异常或算术异常。下面是这些SIGFPE信号类别的问题场景：

| 错误码（code） | 信号字符串 | 解释 | 触发原因 |
| --- | --- | --- | --- |
| 1 | FPE\_INTDIV | 整数除法错误 | 表示整数除法中的除数为零的情况。当一个程序尝试进行整数除法，但除数为零时，会发出这个信号。 |
| 2 | FPE\_INTOVF | 整数溢出错误 | 表示整数溢出错误。当一个程序尝试进行整数运算，结果超出整数范围时，会发出这个信号。 |
| 3 | FPE\_FLTDIV | 浮点除法错误 | 表示浮点数除法中的除数为零的情况。当一个程序尝试进行浮点数除法，但除数为零时，会发出这个信号。 |
| 4 | FPE\_FLTOVF | 浮点上溢错误 | 表示浮点溢出错误。当一个程序尝试进行浮点数运算，结果超出浮点数上限范围时，会发出这个信号。 |
| 5 | FPE\_FLTUND | 浮点下溢错误 | 表示浮点下溢错误。当一个程序尝试进行浮点数运算，结果小于浮点数下限范围时，会发出这个信号。 |
| 6 | FPE\_FLTRES | 浮点结果未定义错误 | 表示浮点结果未定义错误。当一个程序尝试进行浮点数运算，结果未定义时，会发出这个信号。 |
| 7 | FPE\_FLTINV | 无效浮点操作错误 | 表示无效浮点操作错误。当一个程序尝试进行无效的浮点数运算时，会发出这个信号。 |
| 8 | FPE\_FLTSUB | 浮点运算结果越界错误 | 表示浮点运算结果越界错误。当一个程序尝试进行浮点数运算，浮点数结果越界，会发出这个信号。 |

### SIGSEGV崩溃类型

SIGSEGV是一种信号，它表示进程试图访问一个不属于它的内存地址，或者试图访问一个已被操作系统标记为不可访问的内存地址。SIGSEGV信号通常是由以下两种情况引起的：

| 错误码（code） | 信号字符串 | 解释 | 触发原因 |
| --- | --- | --- | --- |
| 1 | SEGV\_MAPERR | 不存在的内存地址 | 进程试图访问一个不存在的内存地址，或者试图访问一个没有映射到进程地址空间的内存地址。这种情况通常是由于程序中的指针错误或内存泄漏引起的。 |
| 2 | SEGV\_ACCERR | 不可访问的内存地址 | 进程试图访问一个已被操作系统标记为不可访问的内存地址，例如向只读内存写入数据或执行没有执行权限的内存。这种情况通常是由于程序中的缓冲区溢出或者试图修改只读内存等错误引起的。 |

### 信号产生原因分类

除了以上根据信号值维度分类，还可以根据信号产生的原因维度分类。所有信号值都可以按照信号产生的原因分类，当前已有信号产生原因分类的code值如下：

| 错误码（code） | 信号字符串 | 解释 | 触发原因 |
| --- | --- | --- | --- |
| 0 | SI\_USER | 用户空间信号 | 由用户空间的进程发送给进程的，通常是通过kill()系统调用发送的。例如，当用户在终端中按下Ctrl+C时，会发送一个SIGINT信号给前台进程组中的所有进程。 |
| 0x80 | SI\_KERNEL | 内核信号 | 由内核发送给进程的，通常是由内核检测到某些错误或异常情况时发出的。例如，当进程访问无效的内存地址或者执行非法指令时，内核会发送一个SIGSEGV信号给进程。 |
| -1 | SI\_QUEUE | sigqueue()函数信号 | 由sigqueue()系统调用发送的，可以携带一个附加的整数值和一个指针。通常用于进程间高级通信，例如传递数据或者通知进程某个事件已经发生。 |
| -2 | SI\_TIMER | 定时器信号 | 由定时器发送的，通常用于定时任务或者周期性任务的执行。例如，当一个定时器到期时，内核会向进程发送一个SIGALRM信号。 |
| -3 | SI\_MESGQ | 消息队列信号 | 由消息队列发送的，通常用于进程间通信。例如，当一个进程向一个消息队列发送消息时，内核会向接收进程发送一个MESGQ信号。 |
| -4 | SI\_ASYNCIO | 异步I/O信号 | 由异步I/O操作发送的，通常用于非阻塞I/O操作。例如，当一个文件描述符上的I/O操作完成时，内核会向进程发送一个ASYNCIO信号。 |
| -5 | SI\_SIGIO | 同步I/O信号 | 由同步I/O操作发送的，通常用于阻塞I/O操作。例如，当一个文件描述符上的I/O操作完成时，内核会向进程发送一个SIGIO信号。 |
| -6 | SI\_TKILL | tkill()函数信号 | 由tkill()系统调用发送的，与kill()系统调用类似，但是可以指定发送信号的线程ID。通常用于多线程程序中，向指定线程发送信号。 |

## 约束与限制

* 不建议进程自己注册信号处理函数，进程崩溃后可能会延迟退出，当处理时间超过5s可能会导致进程无响应问题上报。
* “/data/log/faultlog/faultlogger”目录下同一进程/应用最多保存10份cppcrash日志，日志数量超限时会从最早生成该进程/应用的cppcrash日志开始删除直至数量不超限。建议开发者在开发调试阶段及时查看cppcrash日志，避免因cppcrash日志被删除而无法获取崩溃信息。
* 上述崩溃信号和35、38、42信号已经被系统注册信号处理函数，建议应用不要对这些信号注册信号处理函数，如果应用注册了可能会造成系统检测能力失效。
* 异步线程栈跟踪维测功能默认仅在ARM 64位系统中开启。对于**API version 22**之前版本，**三方和系统应用**通过[libuv](../harmonyos-references/libuv.md)和[ffrt](../harmonyos-references/capi-ffrt.md)提交异步任务仅debug版本默认开启。对于**API version 22**及之后版本，**三方应用**通过libuv提交异步任务debug和release版本均默认开启，**三方和系统应用**通过ffrt提交异步任务仅debug版本默认开启。崩溃日志规格请参见[异步线程栈跟踪故障场景日志规格](cppcrash-guidelines.md#异步线程栈跟踪故障场景日志规格)。

## 日志获取

进程崩溃日志是故障日志中的一种，可通过以下方式获取：

**方式一：通过DevEco Studio获取日志**

DevEco Studio会收集设备“/data/log/faultlog/faultlogger/”路径下的进程崩溃故障日志到FaultLog下，根据进程名和故障类型分类显示。获取日志的方法参见：[DevEco Studio使用指南-FaultLog](ide-fault-log.md)。

**方式二：通过HiAppEvent接口订阅**

HiAppEvent给开发者提供了故障订阅接口，详见[HiAppEvent介绍](hiappevent-intro.md)。参考[订阅崩溃事件（ArkTS）](hiappevent-watcher-crash-events-arkts.md)或[订阅崩溃事件（C/C++）](hiappevent-watcher-crash-events-ndk.md)完成崩溃事件订阅，并通过事件的[external\_log](hiappevent-watcher-crash-events.md#事件字段说明)字段读取故障日志文件内容。

**方式三：通过hdc获取日志，需打开开发者选项**

在开发者选项打开的情况下，开发者可以通过“hdc file recv /data/log/faultlog/faultlogger D:\”命令导出故障日志到本地，故障日志文件名格式为：cppcrash-进程名-进程UID-毫秒级时间.log。

## 日志规格

故障日志的字段信息表如下：

| 字段 | 描述 | 起始API版本 | 是否必选项 | 非必选说明 |
| --- | --- | --- | --- | --- |
| Device info | 设备信息 | 8 | 是 | - |
| Build info | 版本信息 | 8 | 是 | - |
| DeviceDebuggable | 设备的系统版本是否可调试 | 23 | 是 | - |
| Fingerprint | 故障特征，聚类同类问题的哈希值，哈希值相同即判定为同一故障原因。 | 8 | 是 | - |
| Enabled app log configs | 使能的配置参数列表 | 20 | 否 | 仅用户配置时打印，详见[应用通过HiAppEvent设置崩溃日志配置参数场景日志规格](cppcrash-guidelines.md#应用通过hiappevent设置崩溃日志配置参数场景日志规格)。 |
| Module name | 模块名 | 8 | 是 | - |
| ReleaseType | 应用的版本类型 | 23 | 否 | 仅在应用进程提供，release表示应用为[release版本应用](ide-hvigor-compilation-options-customizing-guide.md#section192461528194916)，debug表示应用为[debug版本应用](ide-hvigor-compilation-options-customizing-guide.md#section192461528194916)。 |
| CpuAbi | 二进制接口类型 | 23 | 否 | 仅在应用进程提供。 |
| Version | 应用版本号（点分格式） | 8 | 否 | 仅在应用进程提供。 |
| VersionCode | 应用版本号（整数格式） | 8 | 否 | 仅在应用进程提供。 |
| IsSystemApp | 应用是否为系统应用 | 23 | 否 | 仅在应用进程提供。 |
| PreInstalled | 是否预置应用 | 8 | 否 | 仅在应用进程提供。 |
| Foreground | 前后台状态 | 8 | 否 | 仅在应用进程提供。 |
| Page switch history | 页面切换轨迹 | 20 | 否 | 如果维测服务进程出现故障或未缓存切换轨迹，则不包含此字段，详见[实现原理](cppcrash-guidelines.md#实现原理)。 |
| Timestamp | 故障发生时间戳 | 8 | 是 | - |
| Pid | 进程号 | 8 | 是 | - |
| Uid | 用户ID | 8 | 是 | - |
| HiTraceId | HiTraceChain唯一跟踪标识 | 20 | 否 | 仅故障线程开启HiTraceChain功能时提供，详见[HiTraceChain介绍](hitracechain-intro.md)。 |
| Process name | 故障进程名 | 8 | 是 | - |
| App running unique id | 应用运行时唯一关联的ID | 26.0.0 | 是 | - |
| Process life time | 故障进程存活时间 | 8 | 是 | - |
| Process Memory(kB) | 故障进程内存占用 | 20 | 是 | - |
| Device Memory(kB) | 整机内存信息 | 20 | 否 | 依赖维测服务进程，若发生故障时维测服务进程停止或设备重启则无此字段，详见[实现原理](cppcrash-guidelines.md#实现原理)。 |
| Log source | 用于标识采集日志的方式，目前有以下几种方式：  **processdump：** 由用户态生成  **pdump：** 用户态生成cppcrash日志失败时由内核补偿生成  **liteprocessdump：** render/cpu等低权限进程崩溃时由用户态生成  不同方式下生成日志规格会有差异，详见[不同采集方式下日志规格差异](cppcrash-guidelines.md#不同采集方式下日志规格差异)。 | 26.0.0 | 是 | - |
| Reason | 故障原因 | 8 | 是 | - |
| LastFatalMessage | Fatal消息 | 8 | 否 | 以下几种情况共用此字段：  解析到不可靠的栈帧地址时输出的提示信息。  因ABORT信号崩溃退出时保存最后一条FATAL级Hilog日志。  系统内部的维测信息。  应用通过[OH\_HiDebug\_SetCrashObj](hidebug-guidelines.md#添加维测信息到崩溃日志中)设置的字符串信息。  从API版本26.0.0开始，应用若开启[模块加载链路调试开关](arkts-module-debug.md)，则此字段包含模块加载链路。 |
| Fault thread info | 故障线程信息 | 8 | 是 | - |
| SubmitterStacktrace | 提交者线程栈 | 12 | 否 | 异步线程栈跟踪维测功能默认仅在ARM 64位系统中开启。  对于**API version 22**之前版本，**三方和系统应用**通过libuv和ffrt提交异步任务仅debug版本默认开启。  对于**API version 22**及之后版本，**三方应用**通过libuv提交异步任务debug和release版本均默认开启；**三方和系统应用**通过ffrt提交异步任务仅debug版本默认开启。 |
| Registers | 故障现场寄存器 | 8 | 是 | - |
| Other thread info | 其他线程信息 | 8 | 是 | - |
| Memory near registers | 故障现场寄存器附近内存值 | 8 | 是 | - |
| FaultStack | 故障线程栈内存信息 | 8 | 是 | - |
| Maps | 故障时进程的内存空间 | 8 | 是 | - |
| OpenFiles | 故障时进程持有的文件句柄信息 | 12 | 是 | - |
| HiLog | 故障之前打印的流水日志，最多1000行 | 8 | 是 | - |
| [truncated] | 故障日志截断标志 | 20 | 否 | 配置故障日志截断大小并发生截断时。 |
| MergeLog | 三方应用拼接日志标识 | 24 | 否 | 配置三方应用日志标识，用于拼接应用日志。 |

**说明** 

从**API version 20**开始，故障现场寄存器中新增状态寄存器pstate和esr。

不同的故障场景中日志规格略有不同，分以下七个场景的日志规格，示例如下：

* [一般故障场景日志规格](cppcrash-guidelines.md#一般故障场景日志规格)
* [空指针解引用故障场景日志规格](cppcrash-guidelines.md#空指针解引用故障场景日志规格)
* [栈溢出故障场景日志规格](cppcrash-guidelines.md#栈溢出故障场景日志规格)
* [栈覆盖故障场景日志规格](cppcrash-guidelines.md#栈覆盖故障场景日志规格)
* [异步线程栈跟踪故障场景日志规格](cppcrash-guidelines.md#异步线程栈跟踪故障场景日志规格)
* [应用通过HiAppEvent设置崩溃日志配置参数场景日志规格](cppcrash-guidelines.md#应用通过hiappevent设置崩溃日志配置参数场景日志规格)
* [有页面切换轨迹的故障场景日志规格](cppcrash-guidelines.md#有页面切换轨迹的故障场景日志规格)

**说明** 

以下崩溃日志示例中"<-"右边的文字不是日志内容，是用来解释日志格式的说明文字。

### 一般故障场景日志规格

本节主要介绍崩溃日志的一般日志规格，其余节介绍特殊场景下日志规格，以下是一份DevEco Studio归档在FaultLog的进程崩溃日志的核心内容。

```text
Generated by HiviewDFX@HarmonyOS
================================================================
Device info:HarmonyOS 3.2   <- 设备信息
Build info:HarmonyOS 5.1.0.101 <- 版本信息
DeviceDebuggable:No <- 设备的系统版本是否可调试
Fingerprint:67bc4e29d8af56b6c0cbda154095949e83f3f1d6afe05bfc06c6cbb9f5591bb0 <- 标识故障特征
Module name:com.example.myapplication <- 模块名
ReleaseType:debug <- 应用的版本类型
CpuAbi:arm64-v8a <- 二进制接口类型
Version:1.0.0 <- 应用版本号(点分格式)
VersionCode:1000000 <- 应用版本号(整数格式)
IsSystemApp:No <- 应用是否为系统应用
PreInstalled:No <- 是否预制应用
Foreground:Yes <- 前后台状态
Page switch history: <- 页面切换轨迹
  11:43:21.840 :enters foreground
  11:43:17.317 :leaves foreground
  11:42:46.780 :enters foreground
Timestamp:2026-01-21 11:43:35.140 <- 故障发生时间戳
Pid:11941 <- 进程号
Uid:20020205 <- 用户ID
HiTraceId:a92ab1c7eae68fa <- HiTraceChain唯一跟踪标识(非必选，故障线程无HiTraceId不打印)
Process name:com.example.myapplication <- 故障进程名
Process life time:50s <- 故障进程存活时间
Process Memory(kB): 185430(Rss) <- 故障进程内存占用
Device Memory(kB): Total 11688288, Free 2427804, Available 5592064 <- 整机内存状态（非必选）
Log source:processdump <- 用于标识采集日志的方式，processdump表示由用户态生成
Reason:Signal:SIGSEGV(SI_USER)@0x000000000000303e from:12350:0 <- 故障原因，详见信号值说明
Fault thread info:           <- 故障线程信息
Tid:11941, Name:.hiappeventtest  <- 故障线程号，线程名
#00 pc 00000000001843f0 /system/lib/ld-musl-aarch64.so.1(epoll_wait+80)(6c643df40fcfff22745e25b37e2ca85b) <- 调用栈，调用顺序#06->#05->...->#00，最终在#00的函数中发生崩溃
#01 pc 0000000000021b74 /system/lib64/chipset-sdk-sp/libeventhandler.z.so(OHOS::AppExecFwk::EpollIoWaiter::WaitFor(std::__h::unique_lock<std::__h::mutex>&, long, bool)+232)(ed7ae4e867a4ab26cb8c67afc737116c)
#02 pc 00000000000273f8 /system/lib64/chipset-sdk-sp/libeventhandler.z.so(OHOS::AppExecFwk::EventQueue::WaitUntilLocked(std::__h::chrono::time_point<std::__h::chrono::steady_clock, std::__h::chrono::duration<long long, std::__h::ratio<1l, 1000000000l>>> const&, std::__h::unique_lock<std::__h::mutex>&, bool)+112)(ed7ae4e867a4ab26cb8c67afc737116c)
#03 pc 000000000002c358 /system/lib64/chipset-sdk-sp/libeventhandler.z.so(OHOS::AppExecFwk::EventQueueBase::GetEvent()+168)(ed7ae4e867a4ab26cb8c67afc737116c)
#04 pc 000000000001b148 /system/lib64/chipset-sdk-sp/libeventhandler.z.so(OHOS::AppExecFwk::(anonymous namespace)::EventRunnerImpl::Run()+808)(ed7ae4e867a4ab26cb8c67afc737116c)
#05 pc 000000000001fa04 /system/lib64/chipset-sdk-sp/libeventhandler.z.so(OHOS::AppExecFwk::EventRunner::Run()+356)(ed7ae4e867a4ab26cb8c67afc737116c)
#06 pc 00000000000f3a4c /system/lib64/platformsdk/libappkit_native.z.so(OHOS::AppExecFwk::MainThread::Start()+240)(e30f6c7f026034c7d6fa1692a05d3d69)
Registers:  <- 故障现场寄存器
x0:fffffffffffffffc x1:0000007e5420ad60 x2:0000000000000008 x3:000000007fffffff
x4:0000000000000000 x5:0000000000000008 x6:575f45524f464542 x7:474e49544941575f
x8:0000000000000016 x9:0000000000000008 x10:0000007e5420ad60 x11:e18b0e5877a00005
x12:000000003b9ac9ff x13:007070632e72656e x14:2f72656c646e6168 x15:8f94b1d6208ca9b4
x16:0000005afeafe7d0 x17:0000005afb7f83a0 x18:000000000000000d x19:0000005b1b4dde10
x20:0000005b0c5fcf20 x21:0000005b1b4ddda0 x22:7fffffafde60b8cc x23:0000005b1b4ddda0
x24:0000007e5420af40 x25:0000000000000000 x26:0000000000000000 x27:00000055a511d354
x28:0000005b1a937bc8 x29:0000007e5420ad20
lr:0000005afeae1b78 sp:0000007e5420ad20 pc:0000005afb7f83f0
pstate:0000000020001000 esr:0000000000000000          <-  状态寄存器值（arm32架构为cpsr，aarch64架构为pstate和esr）
Other thread info:      <- 其他线程信息
Tid:12006, Name:OS_IPC_0_120064 <- 线程号，线程名
#00 pc 00000000001a4524 /system/lib/ld-musl-aarch64.so.1(ioctl+200)(6c643df40fcfff22745e25b37e2ca85b)
#01 pc 0000000000012044 /system/lib64/platformsdk/libipc_common.z.so(OHOS::BinderConnector::WriteBinder(unsigned long, void*)+120)(036a4c254e8f85b2af1c2a4f4d540e45)
#02 pc 0000000000070ae8 /system/lib64/platformsdk/libipc_single.z.so(OHOS::BinderInvoker::TransactWithDriver(bool)+284)(f9c345696cb6cee8d986e176f59f003d)
#03 pc 0000000000070ed8 /system/lib64/platformsdk/libipc_single.z.so(OHOS::BinderInvoker::StartWorkLoop()+100)(f9c345696cb6cee8d986e176f59f003d)
Memory near registers:  <-  故障现场寄存器的地址（地址必须在有效内存中）附近内存值，括号表示寄存器里的地址是在哪一段内存中
x1([stack]):         <- 故障现场r1寄存器的地址附近内存值
    0000007e5420ad50 0000000000000000
    0000007e5420ad58 0000005afeaec828
    0000007e5420ad60 0000000000000000
    0000007e5420ad68 0000000000000000
    ...
x10([stack]):
    0000007e5420ad50 0000000000000000
    0000007e5420ad58 0000005afeaec828
    0000007e5420ad60 0000000000000000
    0000007e5420ad68 0000000000000000
    0000007e5420ad70 0000000000000000
    ...
fp([stack]):
    0000007e5420ad10 7fffffafde60b8cc
    0000007e5420ad18 0000005b1b4ddda0
    0000007e5420ad20 0000007e5420ae70
    0000007e5420ad28 0000005afeae1b78
    ...
sp([stack]):
    0000007e5420ad10 7fffffafde60b8cc
    0000007e5420ad18 0000005b1b4ddda0
    0000007e5420ad20 0000007e5420ae70
    0000007e5420ad28 0000005afeae1b78
    ...
lr(/system/lib64/chipset-sdk-sp/libeventhandler.z.so):
    0000005afeae1a80 2a1f03e0940067e8
    0000005afeae1a88 b00000ef17ffff7c
    0000005afeae1a90 ca1d01eff945a5ef
    0000005afeae1a98 d503237fca1e01ef
    ...
pc(/system/lib/ld-musl-aarch64.so.1):
    0000005afb7f82f8 f9000bf3a9be7bfd
    0000005afb7f8300 f0001bc8910003fd
    0000005afb7f8308 aa0103eaaa0403e5
    0000005afb7f8310 93407c4993407c01
    ...
FaultStack: <- 崩溃线程的栈地址空间
    0000007e5420ac20 0000007e00000072
    0000007e5420ac28 73615474736f5010
    0000007e5420ac30 0000007e5420006b
    0000007e5420ac38 ffffff80fffffff8
    ...
sp0:0000007e5420ad20 0000007e5420ae70 <- #00层栈帧顶部位置
    0000007e5420ad28 0000005afeae1b78
    ...
sp1:0000007e5420ad40 0000007e5420aed0
    0000007e5420ad48 815c005afeaec858
    ...
sp2:0000007e5420aee0 0000007e5420af50
    0000007e5420aee8 7835005afeaec35c
    ...
sp3:0000007e5420af20 00000050219e3694
    0000007e5420af28 0000000000000000
    ...

Maps: <- 故障时进程的内存空间
55a511d000-55a5128000 r--p 00000000 /system/bin/appspawn
55a5128000-55a513b000 r-xp 0000a000 /system/bin/appspawn
55a513b000-55a513c000 r--p 0001c000 /system/bin/appspawn
55a513c000-55a513e000 rw-p 0001c000 /system/bin/appspawn
...
5b0c3cf000-5b0c64f000 rw-p 00000000 [anon:native_heap:jemalloc]
5b19605000-5b1d505000 rw-p 00000000 [anon:native_heap:jemalloc]
5b20100000-5b20107000 r--p 00000000 /system/lib64/platformsdk/libhdc_register.z.so
5b20107000-5b20110000 r-xp 00006000 /system/lib64/platformsdk/libhdc_register.z.so
5b20110000-5b20112000 r--p 0000e000 /system/lib64/platformsdk/libhdc_register.z.so
5b20112000-5b20113000 rw-p 0000f000 /system/lib64/platformsdk/libhdc_register.z.so
7e53a0d000-7e5420c000 rw-p 00000000 [stack]
7e55b92000-7e55b93000 rw-p 00000000 [anon:libark_tooling.so.bss]
OpenFiles: <- 故障时进程持有文件句柄信息
0->/dev/null native object of unknown type 0
1->/dev/null native object of unknown type 0
2->/dev/null native object of unknown type 0
3->socket:[2671] native object of unknown type 218115328
6->socket:[2793] native object of unknown type 0
36->/dev/urandom native object of unknown type 0

HiLog: <- 故障之前进程打印的流水日志
01-21 11:43:35.140 11941 11941 I C02D11/DfxSignalHandler: DFX_SigchainHandler :: signo(11), si_code(0), pid(11941), tid(11941).
01-21 11:43:35.140 11941 11941 I C02D11/DfxSignalHandler: DFX_SigchainHandler :: signo(11), pid(11941), processName(com.example.hiappeventtest), threadName(.hiappeventtest).

MergeLog: <- 应用提供的拼接日志
Last Modified: 2026-03-18 10:10:10 <- 应用提供的拼接日志的最后修改时间戳
app crash log. <- 应用生成用于拼接的日志
```

**HiTraceId说明**

HiTraceId：HiTraceChain提供的唯一跟踪标识，参考[HiTraceChain介绍](hitracechain-intro.md)。

**调用栈帧内容说明**

以三层调用栈为例，详细解释调用栈帧内容：

```text
#00 pc 000e8400 /system/lib/ld-musl-arm.so.1(raise+176)(a40044d0acb68107cfc4adb5049c0725)
#01 pc 00006e95 /data/crasher_cpp(DfxCrasher::RaiseSegmentFaultException()+92)(d6cead5be17c9bb7eee2a9b4df4b7626)
#02 pc 00008909 /data/crasher_cpp(DfxCrasher::ParseAndDoCrash(char const*) const+612)(d6cead5be17c9bb7eee2a9b4df4b7626)
```

| 序号 | pc在文件内的偏移字节数 | pc属于内存段的文件名 | 函数名 | 函数内偏移的字节数 | BuildID |
| --- | --- | --- | --- | --- | --- |
| #00 | 000e8400 | /system/lib/ld-musl-arm.so.1 | raise | 176 | a40044d0acb68107cfc4adb5049c0725 |
| #01 | 00006e95 | /data/crasher\_cpp | DfxCrasher::RaiseSegmentFaultException() | 92 | d6cead5be17c9bb7eee2a9b4df4b7626 |
| #02 | 00008909 | /data/crasher\_cpp | DfxCrasher::ParseAndDoCrash(char const\*) const | 612 | d6cead5be17c9bb7eee2a9b4df4b7626 |

**说明** 

* 文件名也有可能是匿名内存映射，比如[heap]、[stack]等。
* 日志没有打印函数名可能是由于以下两种原因：

  1. 二进制文件中没有保存该函数名信息。
  2. 二进制文件中保存的函数名长度超过256字节。
* 函数名是通过解析二进制符号表和[MiniDebugInfo](https://sourceware.org/gdb/current/onlinedocs/gdb.html/MiniDebugInfo.html)得来，**可能会随版本函数名变更、编译优化等原因而改变**。
* 如果没打印BuildID，可以通过readelf -n xxx.so确认二进制是否有BuildID。如果没有则尝试在编译选项里增加编译参数--enable-linker-build-id，同时注意编译选项中不要加编译参数--build-id=none。

**JS混合栈帧内容说明**

ARM 64位系统支持抓取CPP和JS之间跨语言的调用栈，因此如果在函数调用链上有JS代码，崩溃日志还会打印如下格式的JS代码调用栈：

```text
#00 at onPageShow (entry|har1|1.0.0|src/main/ets/pages/Index.ts:7:13)
```

详细说明[JS异常代码调用栈格式规范](jscrash-guidelines.md#异常代码调用栈格式)。

### 空指针解引用故障场景日志规格

空指针解引用通常有以下两个常见的场景：

1.形如SIGSEGV(SEGV\_MAPERR)@0x00000000或cppcrash日志的Register中打印的r0，r1等传参寄存器的值为0，应首先考虑调用时是否传入了空指针。

2.形如SIGSEGV(SEGV\_MAPERR)@0x0000000c（小于一个内存页大小）或cppcrash日志Register中打印的r1等传参寄存器的值为一个很小的值时应考虑调用入参的结构体成员是否包含空指针。

该场景会在日志中打印出提示信息，表明故障很有可能是因为空指针解引用导致。以下是一份DevEco Studio归档在FaultLog的进程崩溃日志的核心内容。

```text
Generated by HiviewDFX@HarmonyOS
================================================================
Device info:HarmonyOS 3.2   <- 设备信息
Build info:HarmonyOS 5.1.0.101 <- 版本信息
DeviceDebuggable:No <- 设备的系统版本是否可调试
Fingerprint:125680eed3692695a944851a4e6e61500e9633c49224b68e02c0d6789a7e8c2a <- 标识故障特征
Module name:crasher_cpp            <- 模块名
Timestamp:2026-01-21 14:29:01.652  <- 故障发生时间戳
Pid:46314   <- 进程号
Uid:0         <- 用户ID
HiTraceId:a92ab1722d9f297  <-HiTraceChain唯一跟踪标识(非必选，故障线程无HiTraceId不打印)
Process name:./crasher_cpp         <- 故障进程名
Process life time:1s               <- 故障进程存活时间
Process Memory(kB): 8286(Rss)     <- 故障进程内存占用
Device Memory(kB): Total 11688288, Free 2590168, Available 6153216 <- 整机内存状态（非必选）
Log source:processdump <- 用于标识采集日志的方式，processdump表示由用户态生成
Reason:Signal:SIGSEGV(SEGV_MAPERR)@0x0000000000000004  probably caused by NULL pointer dereference   <- 故障原因和空指针提示
Fault thread info:
Tid:46314, Name:crasher_cpp         <- 故障线程号，线程名
#00 pc 000000000001092c /data/crasher_cpp(TestNullPointerDereferenceCrash0()+48)(16bde6cdd3f8bb6d20de4e68c210ee7c)
#01 pc 000000000000bd50 /data/crasher_cpp(DfxCrasher::ParseAndDoCrash(char const*) const+616)(16bde6cdd3f8bb6d20de4e68c210ee7c)
#02 pc 000000000000c530 /data/crasher_cpp(main+1160)(16bde6cdd3f8bb6d20de4e68c210ee7c)
#03 pc 00000000000af9b0 /system/lib/ld-musl-aarch64.so.1(libc_start_main_stage2+80)(6c643df40fcfff22745e25b37e2ca85b)
Registers:   <- 故障现场寄存器
x0:0000005704762398 x1:0000007e60d9d8ac x2:0000000000000001 x3:0000005b2efaa268
x4:00000057047620c1 x5:0000005b2f288ea9 x6:6e696f506c6c754e x7:6665726544726574
x8:0000000000000004 x9:13a5bcd2d1efb552 x10:0000005b2efaa290 x11:503a3a65636e6572
x12:626d654d746e6972 x13:3a65756c61567265 x14:000000000000000c x15:0000000000000000
x16:0000005704773120 x17:0000005b2ef6cb94 x18:0000000000000000 x19:0000007e60d9d940
x20:0000007e60d9d9a8 x21:0000007e60d9d909 x22:0000005704771c68 x23:000000570476fba8
x24:000000570476fc40 x25:0000000000000d20 x26:0000000000000001 x27:0000005b2efa6000
x28:0000005b2efaa838 x29:0000007e60d9d8f0
lr:000000570476d920 sp:0000007e60d9d8f0 pc:000000570476d92c
pstate:0000000060001000 esr:0000000092000005          <-  状态寄存器值（arm32架构为cpsr，aarch64架构为pstate和esr）
...
```

### 栈溢出故障场景日志规格

以下三种场景可能出现栈溢出：

* 递归调用时未设置递归终止条件导致栈内存耗尽。
* 局部变量占用过多栈内存导致栈内存耗尽。
* 在信号栈中使用超过系统限制的栈内存。

以递归调用时未设置递归终止条件导致栈内存耗尽为例，示例代码如下：

```
static void *DoStackOverflow(void * inputArg) __attribute__((optnone))
{
    int b[10] = {1};
    if (b[0] == 0) {
        return static_cast<void*>(b + 9); // 9: last element of array
    }
    DoStackOverflow(inputArg); // 多次递归调用，导致栈内存耗尽后在栈的范围外进行内存的读写，产生崩溃。
    return static_cast<void*>(b + 9); // 9: last element of array
}
```

该场景会在日志中打印出提示信息，表明故障很有可能是由于栈溢出导致。以下是一份DevEco Studio归档在FaultLog的进程崩溃日志的核心内容。

```text
Generated by HiviewDFX@HarmonyOS
================================================================
Device info:HarmonyOS 3.2   <- 设备信息
Build info:HarmonyOS 5.1.0.101 <- 版本信息
DeviceDebuggable:No <- 设备的系统版本是否可调试
Fingerprint:efeb9bc182c8eedd0cb5672809fcc02a2ceb65050589c1512ce30cd62469ed03  <- 标识故障特征
Module name:crasher_cpp                <- 模块名
Timestamp:2026-01-21 14:32:29.539      <- 故障发生时间戳
Pid:47049                            <- 进程号
Uid:0                                  <- 用户ID
HiTraceId:a92ab1c7eae68fa  <- HiTraceChain唯一跟踪标识(非必选，故障线程无HiTraceId不打印)
Process name:./crasher_cpp             <- 故障进程名
Process life time:2s                  <- 故障进程存活时间
Process Memory(kB): 8306(Rss)     <- 故障进程内存占用
Device Memory(kB): Total 11688288, Free 2595812, Available 6161408 <- 整机内存状态（非必选）
Log source:processdump <- 用于标识采集日志的方式，processdump表示由用户态生成
Reason:Signal:SIGSEGV(SEGV_ACCERR)@0x0000005b517d3fd0  current thread stack low address = 0x0000005b517d4000, probably caused by stack-buffer-overflow    <- 故障原因和栈溢出提示
Fault thread info:
Tid:47050, Name:crasher_cpp
#00 pc 000000000000a11c /data/crasher_cpp(DoStackOverflow(void*)+36)(16bde6cdd3f8bb6d20de4e68c210ee7c)
#01 pc 000000000000a15c /data/crasher_cpp(DoStackOverflow(void*)+100)(16bde6cdd3f8bb6d20de4e68c210ee7c)
#02 pc 000000000000a15c /data/crasher_cpp(DoStackOverflow(void*)+100)(16bde6cdd3f8bb6d20de4e68c210ee7c)
#03 pc 000000000000a15c /data/crasher_cpp(DoStackOverflow(void*)+100)(16bde6cdd3f8bb6d20de4e68c210ee7c)
#04 pc 000000000000a15c /data/crasher_cpp(DoStackOverflow(void*)+100)(16bde6cdd3f8bb6d20de4e68c210ee7c)
#05 pc 000000000000a15c /data/crasher_cpp(DoStackOverflow(void*)+100)(16bde6cdd3f8bb6d20de4e68c210ee7c)
...
```

### 栈覆盖故障场景日志规格

栈覆盖故障场景是指业务代码运行时改写了原本保存函数调用信息的栈内存，导致无法成功回溯调用栈。系统在回栈失败后尽可能提供开发者信息以分析问题，该场景会在日志中打印信息提示从#xx开始尝试从线程栈内存里解析不可靠的调用栈。之所以说不可靠的调用栈，是因为调用栈可能不是一个完整的函数调用链路，从#xx层往下的调用栈是不可靠的，意味着从#xx层开始相邻两层栈之间可能不存在调用关系，需要开发者结合业务代码分析其中的调用链路，比如下例中正确的调用关系是#05->#04->#03->#01。以下是一份DevEco Studio归档在FaultLog的进程崩溃日志的核心内容。

```text
Generated by HiviewDFX@HarmonyOS
================================================================
Device info:HarmonyOS 3.2   <- 设备信息
Build info:HarmonyOS 5.1.0.101 <- 版本信息
DeviceDebuggable:No <- 设备的系统版本是否可调试
Fingerprint:494b19375266bbefaa667b860e9404317deae24200320b2b8afbe2781476167c    <- 标识故障特征
Module name:crasher_cpp                   <- 模块名
Timestamp:2026-01-21 14:42:02.675  <- 故障发生时间戳
Pid:49315                                 <- 进程号
Uid:0                                     <- 用户ID
HiTraceId:a92ab1753aa4af0  <- HiTraceChain唯一跟踪标识(非必选，故障线程无HiTraceId不打印)
Process name:./crasher_cpp                <- 故障进程名
Process life time:1s                      <- 故障进程存活时间
Process Memory(kB): 8245(Rss)            <- 故障进程内存占用
Device Memory(kB): Total 11688288, Free 2570076, Available 6149120 <- 整机内存状态（非必选）
Log source:processdump <- 用于标识采集日志的方式，processdump表示由用户态生成
Reason:Signal:SIGILL(ILL_ILLOPN)@000000000000000000      <- 故障原因
LastFatalMessage:Failed to unwind stack, try to get unreliable call stack from #01 by reparsing thread stack. <- #00和#01一般认为是可信的，从#02开始尝试从线程栈内存里解析不可靠的调用栈
Fault thread info:
Tid:49315, Name:crasher_cpp               <- 故障线程号，线程名
#00 pc 00000000000096b0 /data/crasher_cpp(RecursiveHelperFunction(int, int, int)+160)(16bde6cdd3f8bb6d20de4e68c210ee7c)
#01 pc 0000000000009650 /data/crasher_cpp(RecursiveHelperFunction(int, int, int)+64)(16bde6cdd3f8bb6d20de4e68c210ee7c)
#02 pc 000000000000968c /data/crasher_cpp(RecursiveHelperFunction(int, int, int)+124)(16bde6cdd3f8bb6d20de4e68c210ee7c)
#03 pc 000000000000968c /data/crasher_cpp(RecursiveHelperFunction(int, int, int)+124)(16bde6cdd3f8bb6d20de4e68c210ee7c)
#04 pc 000000000000968c /data/crasher_cpp(RecursiveHelperFunction(int, int, int)+124)(16bde6cdd3f8bb6d20de4e68c210ee7c)
#05 pc 000000000000968c /data/crasher_cpp(RecursiveHelperFunction(int, int, int)+124)(16bde6cdd3f8bb6d20de4e68c210ee7c)
...
Registers:
x0:0000000000000000 x1:0000000000000000 x2:0000000000000000 x3:0000007f7264b180
x4:0000007f7264b200 x5:0000000000000004 x6:3162343632376637 x7:3030316234363237
x8:0000000000000100 x9:0000000000000000 x10:0000000000000078 x11:0000000000000000
x12:0000007f7264ada8 x13:00000059ece0863d x14:0000000000000001 x15:0000000000000000
x16:00000059ee950538 x17:00000059ecf2b880 x18:0000000000000000 x19:0000000000000000
x20:0000000000000000 x21:0000007f7264b909 x22:00000056855f8b18 x23:00000056855f6ba8
x24:00000056855f6c40 x25:0000000000000e70 x26:0000000000000001 x27:00000059ecfea000
x28:00000059ecfee838 x29:0000000000000000
lr:0000000000000000 sp:0000007f7264b120 pc:00000056855ed6b0
pstate:0000000060001000 esr:0000000000000000
...
```

### 异步线程栈跟踪故障场景日志规格

当异步线程发生崩溃后，把提交该异步任务的线程栈也打印出来，帮助定位由于异步任务提交者造成的崩溃问题。崩溃线程的调用栈和其提交线程的调用栈通过SubmitterStacktrace字符串分隔。

**异步线程栈生成原理**

原理示意图如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/36/v3/yG1CeRomTr20DL2hYNWb0A/zh-cn_image_0000002742123581.png)

1. 提交线程搜集自身的调用栈信息，保存至进程特定区域内存的异步栈表中。
2. 记录保存后，异步栈表返回唯一标识stackId。
3. 提交线程提交异步任务，并传递标识stackId。
4. 执行线程在执行任务前保存stackId至线程局部存储区中。
5. 执行线程开始执行异步任务。
6. 执行线程在执行异步任务过程中发生崩溃，产生崩溃信号。
7. 信号处理函数通过GetStackId函数获取保存在线程局部存储区中的stackId。
8. 信号处理函数将stackId传递给回栈进程processdump。
9. processdump跨进程读取异步栈表，根据stackId值查询获取提交线程的调用栈信息，填充至故障日志对应的SubmitterStacktrace字段。

以下是一份DevEco Studio归档在FaultLog的进程崩溃日志的核心内容。

**注意** 

异步线程栈跟踪维测功能默认仅在ARM 64位系统中开启。

对于**API version 22**之前版本，**三方和系统应用**通过libuv和ffrt提交异步任务仅debug版本默认开启。

对于**API version 22**及之后版本，**三方应用**通过libuv提交异步任务debug和release版本均默认开启，**三方和系统应用**通过ffrt提交异步任务仅debug版本默认开启。

```text
Generated by HiviewDFX@HarmonyOS
================================================================
Device info:HarmonyOS 3.2   <- 设备信息
Build info:HarmonyOS 5.1.0.101 <- 版本信息
DeviceDebuggable:No <- 设备的系统版本是否可调试
Fingerprint:8bc3343f50024204e258b8dce86f41f8fcc50c4d25d56b24e71fe26c0a23e321  <- 标识故障特征
Module name:com.example.uv001      <- 模块名
ReleaseType:release <- 应用的版本类型
CpuAbi:armeabi-v7a <- 二进制接口类型
Version:1.0.0 <- 应用版本号(点分格式)
VersionCode:1000000 <- 应用版本号(整数格式)
IsSystemApp:No <- 应用是否为系统应用
PreInstalled:No <- 是否预制应用
Foreground:Yes <- 前后台状态
Page switch history: <- 页面切换轨迹
10:09:06.006 :enters foreground
Timestamp:2026-01-08 11:25:46.000  <- 故障发生时间戳
Pid:28421                                   <- 进程号
Uid:20020214                                <- 用户ID
HiTraceId:a92ab1c7eae68fa  <- HiTraceChain唯一跟踪标识(非必选，故障线程无HiTraceId不打印)
Process name:com.example.uv001              <- 故障进程名
Process life time:42s                        <- 故障进程存活时间
Process Memory(kB): 151736(Rss)            <- 故障进程内存占用
Device Memory(kB): Total 11712088, Free 2500232, Available 5275648 <- 整机内存状态（非必选）
Log source:processdump <- 用于标识采集日志的方式，processdump表示由用户态生成
Reason:Signal:SIGABRT(SI_TKILL)@0x01317bf600006f05  from:28421:20020214  <- 故障原因
Fault thread info:
Tid:29192, Name:OS_FFRT_2_0                 <- 故障线程号，线程名
#00 pc 00000000001bfa74 /system/lib/ld-musl-aarch64.so.1(raise+216)(2f1b32d70ef466b15265fd08a0eca91e)  <- 调用栈
#01 pc 0000000000001ff8 /data/storage/el1/bundle/libs/arm64/libentry.so(7869adbb6ed8ae9fed544fa0eb2883f9a22d3bc5)
#02 pc 0000000000013694 /system/lib64/platformsdk/libuv.so(uv__queue_work+60)(f78cf9546cece23d7b088a751ff98497)
#03 pc 0000000000093224 /system/lib64/ndk/libffrt.so(ffrt::UVTask::Execute()+744)(4f907cee9caa17cf5d72826c09f13f10)
#04 pc 000000000008e784 /system/lib64/ndk/libffrt.so(ffrt::ExecuteTask(ffrt::TaskBase*)+248)(4f907cee9caa17cf5d72826c09f13f10)
#05 pc 000000000002ed3c /system/lib64/ndk/libffrt.so(ffrt::CPUWorker::RunTask(ffrt::TaskBase*,ffrt::CPUWorker*)+84)(4f907cee9caa17cf5d72826c09f13f10)
#06 pc 00000000000c87b0 /system/lib64/ndk/libffrt.so(4f907cee9caa17cf5d72826c09f13f10)
#07 pc 00000000001dfbf0 /system/lib/ld-musl-aarch64.so.1(start+240)(2f1b32d70ef466b15265fd08a0eca91e)
========SubmitterStacktrace========       <- 任务异常时打印任务提交者调用栈
#00 pc 0000000000013590 /system/lib64/platformsdk/libuv.so(uv_queue_work+304)(f78cf9546cece23d7b088a751ff98497)
#01 pc 0000000000001f74 /data/storage/el1/bundle/libs/arm64/libentry.so(7869adbb6ed8ae9fed544fa0eb2883f9a22d3bc5)
#02 pc 000000000006a258 /system/lib64/platformsdk/libace_napi.z.so(panda::JSValueRefArkNativeFunctionCallBack<true>(panda::JsiRuntimeCallInfo*)+296)(23225c16f1721ec4629f9788305fc487)
#03 pc 0000000000e7f46c /system/lib64/module/arkcompiler/stub.an(RTStub_PushCallArgsAndDispatchNative+44)
#04 pc 00000000004854c0 /system/lib64/module/arkcompiler/stub.an(BCStub_HandleCallthis2Imm8V8V8V8StwCopy+440)
#05 at func_main_0 (entry|entry|1.0.0|src/main/ets/pages/Index.ts:72:10)
#06 pc 0000000000366444 /system/lib64/platformsdk/libark_jsruntime.so(panda::ecmascript::EcmaInterpreter::Execute(panda::ecmascript::EcmaRuntimeCallInfo*)+800)(6e93189f3a9e33adb9455beb7c675df6)
#07 pc 0000000000803fcc /system/lib64/platformsdk/libark_jsruntime.so(6e93189f3a9e33adb9455beb7c675df6)
#08 pc 0000000000804da4 /system/lib64/platformsdk/libark_jsruntime.so(panda::ecmascript::EcmaVM::InvokeEcmaEntrypoint(panda::ecmascript::JSPandaFile const*,std::__h::basic_string<char,std::__h::char_traits<char>,panda::ecmascript::CAddressAllocator<char>> const&,panda::ecmascript::ExecuteTypes const&)+776)(6e93189f3a9e33adb9455beb7c675df6)
#09 pc 000000000049d0f4 /system/lib64/platformsdk/libark_jsruntime.so(6e93189f3a9e33adb9455beb7c675df6)
#10 pc 000000000039735c /system/lib64/platformsdk/libark_jsruntime.so(panda::ecmascript::SourceTextModule::ModuleExecution(panda::ecmascript::JSThread*,panda::ecmascript::JSHandle<panda::ecmascript::SourceTextModule> const&,void const*,unsigned long, panda::ecmascript::ExecuteTypes const&)+1108)(6e93189f3a9e33adb9455beb7c675df6)
#11 pc 00000000003db718 /system/lib64/platformsdk/libark_jsruntime.so(6e93189f3a9e33adb9455beb7c675df6)
#12 pc 00000000003dacc0 /system/lib64/platformsdk/libark_jsruntime.so(panda::ecmascript::SourceTextModule::Evaluate(panda::ecmascript::JSThread*,panda::ecmascript::JSHandle<panda::ecmascript::SourceTextModule> const&,void const*,unsigned long,panda::ecmascript::ExecuteTypes const&)+736)(6e93189f3a9e33adb9455beb7c675df6)
#13 pc 00000000005ac534 /system/lib64/platformsdk/libark_jsruntime.so(6e93189f3a9e33adb9455beb7c675df6)
#14 pc 00000000005abbec /system/lib64/platformsdk/libark_jsruntime.so(6e93189f3a9e33adb9455beb7c675df6)
#15 pc 0000000000644acc /system/lib64/platformsdk/libark_jsruntime.so(6e93189f3a9e33adb9455beb7c675df6)
...
```

### 应用通过HiAppEvent设置崩溃日志配置参数场景日志规格

系统提供了通用的崩溃日志生成功能，但部分应用有自定义日志内容的需求。因此从**API version 20**开始，可通过设置[setEventConfig](hiappevent-watcher-crash-events.md#seteventconfig接口说明)接口配置自定义日志内容。

以下是一份DevEco Studio归档在FaultLog的系统崩溃日志的核心内容：

```text
...
Build info:HarmonyOS 5.0.0.23
...
Enabled app log configs:    <- 使能的配置参数列表，只打印不是默认值的配置参数
Extend pc lr printing:true  <- extend_pc_lr_printing参数设置为true
Log cut off size:102400B    <- 崩溃日志大小截断到100KB（仅通过HiAppEvent接口订阅获取的崩溃日志生效）
Simplify maps printing:true <- simplify_vma_printing参数设置为true
Timestamp:2026-01-08 11:25:46.000
...
Registers: <- 故障现场寄存器
x0:fffffffffffffffc x1:0000007e5420ad60 x2:0000000000000008 x3:000000007fffffff
x4:0000000000000000 x5:0000000000000008 x6:575f45524f464542 x7:474e49544941575f
x8:0000000000000016 x9:0000000000000008 x10:0000007e5420ad60 x11:e18b0e5877a00005
x12:000000003b9ac9ff x13:007070632e72656e x14:2f72656c646e6168 x15:8f94b1d6208ca9b4
x16:0000005afeafe7d0 x17:0000005afb7f83a0 x18:000000000000000d x19:0000005b1b4d4d50
x20:0000005b0c5fcf20 x21:0000005b1b4d4ce0 x22:7fffa71517841b1d x23:0000005b1b4d4ce0
x24:0000007e5420af40 x25:0000000000000000 x26:0000000000000000 x27:00000055a511d354
x28:0000005b1a937bc8 x29:0000007e5420ad20
lr:0000005afeae1b78 sp:0000007e5420ad20 pc:0000005afb7f83f0
pstate:0000000020001000 esr:0000000000000000
Memory near registers:
...
lr(/system/lib64/chipset-sdk-sp/libeventhandler.z.so): <- lr寄存器地址附近的内存值
    0000005afeae1a80 2a1f03e0940067e8 <- extend_pc_lr_printing设置为true时，向前打印内存值到此
    ...
    0000005afeae1b68 910083e19a89b103 <- extend_pc_lr_printing设置为false时，向前打印内存值到此
    0000005afeae1b70 9400680b52800102
    0000005afeae1b78 885ffe682a0003f7 <- lr寄存器地址（0000005afeae1b78）的内存值（885ffe682a0003f7）
    ...
    0000005afeae1c60 52801002d10243a1 <- extend_pc_lr_printing设置为false时，向后打印内存值到此
    0000005afeae1c68 ad3c83a0ad3b83a0
    0000005afeae1c70 ad3e83a0ad3d83a0
    0000005afeae1c78 94006799b9400000 <- extend_pc_lr_printing设置为true时，向后打印内存值到此
pc(/system/lib/ld-musl-aarch64.so.1): <- pc寄存器地址附近的内存值
    0000005afb7f82f8 f9000bf3a9be7bfd <- extend_pc_lr_printing设置为true时，向前打印内存值到此
    ...
    0000005afb7f83e0 aa1f03e4aa0403e3 <- extend_pc_lr_printing设置为false时，向前打印内存值到此
    0000005afb7f83e8 d400000152800105
    0000005afb7f83f0 eb00811fb25453e8 <- pc寄存器地址（0000005afb7f83f0）的内存值（eb00811fb25453e8）
    ...
    0000005afb7f84d8 aa0903e152800260 <- extend_pc_lr_printing设置为false时，向后打印内存值到此
    0000005afb7f84e0 d63f0100f9439508
    0000005afb7f84e8 a9be7bfd17ffffe6
    0000005afb7f84f0 910003fdf9000bf3 <- extend_pc_lr_printing设置为true时，向后打印内存值到此
...
Maps:       <- simplify_vma_printing设置为true，打印Maps数量减少，只保留崩溃日志中出现的地址所属的Maps
55a511d000-55a5128000 r--p 00000000 /system/bin/appspawn
55a5128000-55a513b000 r-xp 0000a000 /system/bin/appspawn
55a513b000-55a513c000 r--p 0001c000 /system/bin/appspawn
55a513c000-55a513e000 rw-p 0001c000 /system/bin/appspawn
... <- 继续打印崩溃日志中出现的地址所属的Maps，此处省略不展示
OpenFiles:
...
[truncated]  <- 日志截断的标志符，如果有打印说明日志被截断了
```

### 有页面切换轨迹的故障场景日志规格

针对包含页面切换的应用，自API version 20起，维测进程会记录应用切换历史。应用发生故障后，生成的故障文件将包含页面切换历史轨迹。

故障日志文件最多记录最新的10条历史轨迹。

```text
...
Foreground:Yes
Page switch history:
  14:08:30:327 /ets/pages/Index:JsError
  14:08:28:986 /ets/pages/Index
  14:08:07:606 :leaves foreground
  14:08:06:246 /ets/pages/Index:AppFreeze
  14:08:01:955 :enters foreground
Timestamp:2025-08-20 14:08:30:327
Pid:10208
Uid:0
...
```

单条记录的格式如下：

```text
  14:08:30:327 /ets/pages/Index:JsError
       ^             ^            ^
    切换时间      页面URL       页面名
```

**注意** 

仅在通过Navigation跳转到子页面时才会有页面名，页面名在[系统路由表](arkts-navigation-cross-package.md#系统路由表)中定义。

当应用发生前后台切换时，对应的页面URL为空，但是会将enters foreground、leaves foreground作为特殊的页面名进行填充。

enters foreground：应用进入前台运行。

leaves foreground：应用在后台运行。

## CppCrash聚类

### 聚类简介

应用程序在不同版本或同一版本的不同时间产生的Cpp Crash可能为同一原因，但在Cpp crash故障日志中生成的大部分信息会随版本、时间等因素变化，无法快速确定是否为重复问题；

Cpp Crash故障信息包含系统侧和应用侧的调用栈，不利于应用开发者快速排查应用侧的问题。

因此，为避免重复分析多份故障信息，提高应用故障问题的分析效率，需要对Cpp Crash故障信息进行聚类；

同时，聚类也能帮助开发者对不同原因问题进行分类统计。

### 聚类信息范围

Cpp Crash故障日志信息中的故障线程信息表示业务线程发生故障时代码调用信息，相同的故障线程调用栈信息必然表示相同的故障原因。

因此，将故障线程信息作为聚类范围是最为准确的，开发者可根据业务聚类的需求调整增加其他故障日志的信息。

故障线程信息在Cpp Crash故障日志中从“Fault thread info:”开始，到“Registers:”结束，示例如下：

```text
...
Fault thread info:
Tid:10208, Name:crasher_cpp
#00 pc 000e8400 /system/lib/ld-musl-arm.so.1(raise+176)(a40044d0acb68107cfc4adb5049c0725)
#01 pc 00008cdc /data/storage/el1bundle/libs/arm64/libsample.so(8b74cdc906ea6b2eba95d891bc91c72a)
#02 pc 0005ae00 /system/lib/platformsdk/libace_napi.z.so(panda::JSValueRef ArkNativeFunctionCallBack<true>(panda::JsiRuntimeCallInfo*)+272)(bc1c64aabbe5c7d4db2282a6137443e1)
#03 pc 00de3efc /system/lib/module/arkcompiler/stub.an(RTStub_PushCallArgsAndDispatchNative+44)
#04 pc 00448dd4 /system/lib/module/arkcompiler/stub.an(BCStub_HandleCallthis0Imm8V8StwCopy+372)
#05 at triggerCrash (sample|sample|1.0.0|src/main/ets/pages/CppCrash.ts:49:25)
#06 at onPageShow (sample|sample|1.0.0|src/main/ets/pages/Index.ts:381:36)
#07 pc 001e5c8c /system/lib/platformsdk/libark_jsruntime.so(ce0b05d90b9fae02e7abf8e9f1e5a0f3)
...
Registers:
...
```

### 提取聚类信息

故障线程信息，除线程名和线程号外，主要为调用栈信息，可以通过正则匹配筛选堆栈内容。

由于系统或应用的版本不同，调用栈中会存在一些易变的信息（如行号、字节偏移、BuildID），因此需要对信息做提取和过滤操作。

建议对每一帧栈帧，执行以下操作：

**Native栈帧标准化：**

| 原始栈帧内容 | 标准化后栈帧内容 |
| --- | --- |
| #02 pc 0005ae00 /system/lib/platformsdk/libace\_napi.z.so(panda::JSValueRef ArkNativeFunctionCallBack<true>(panda::JsiRuntimeCallInfo\*)+272)(bc1c64aabbe5c7d4db2282a6137443e1) | /system/lib/platformsdk/libace\_napi.z.so(panda::JSValueRef ArkNativeFunctionCallBack<true>(panda::JsiRuntimeCallInfo\*)+272) |

按以下步骤处理：

a. 去除行号；

b. 去除PC偏移和BuildID；

c. 保留文件路径（如 /system/lib/platformsdk/libace\_napi.z.so）；

d. 保留函数完整签名（如 panda::JSValueRef ArkNativeFunctionCallBack<true>(panda::JsiRuntimeCallInfo\*)+272)，括号内的内容，含类名、函数名、参数，包括 const、参数类型等）。

若Native栈帧存在仅有二进制文件名而没有函数名时，可选择保留PC的偏移值与文件路径：

| 原始栈帧内容 | 标准化后栈帧内容 |
| --- | --- |
| #01 pc 00008cdc /data/storage/el1bundle/libs/arm64/libsample.so(8b74cdc906ea6b2eba95d891bc91c72a) | 00008cdc /data/storage/el1bundle/libs/arm64/libsample.so |

**JS栈帧标准化：**

| 原始栈帧内容 | 标准化后栈帧内容 |
| --- | --- |
| #06 at onPageShow (sample|sample|1.0.0|src/main/ets/pages/Index.ts:381:36) | onPageShow (sample|sample|1.0.0|src/main/ets/pages/Index.ts:381:36) |

按以下步骤处理：

a. 去除行号；

b. 保留函数名（如 onPageShow）；

c. 保留文件路径、代码行号和列号（如 src/main/ets/pages/Index.ts:381:36）；

d. 保留模块名、依赖模块名、版本号信息（如sample|sample|1.0.0|）。

### 提取聚类特征

经过标准化的栈帧可能仍然存在栈帧较多，不利于聚类后存储以及查询的情况，因此开发者需要根据业务情况制定聚类特征提取方法，将栈帧信息进一步简化为聚类特征。

以下为推荐的聚类特征提取方法：

**1. 过滤基础库与异常栈帧**

即栈帧包含如下字段之一：

```text
libc.so
libc++.so
ld-musl-aarch64.so
libc_fdleak_debug.so
unknown
watchdog
kthread
rdr_system_error
libart.so
__switch_to
dump_backtrace
show_stack
dump_stack
panic
libace_napi.z.so
libarkjs_runtime.z.so
```

**2. 过滤系统栈帧，筛选业务栈帧**

系统库栈帧以“/system/lib”或“/system/lib64”为起始字符，系统栈帧格式示例：

```text
/system/lib/platformsdk/libace_napi.z.so(panda::JSValueRef ArkNativeFunctionCallBack\<true\>(panda::JsiRuntimeCallInfo*)+272)
```

业务栈帧以“at”为起始字符，或包含“/data”、“/data/storage”子串。业务栈帧格式示例：

JS栈帧默认为业务栈帧：

```text
at onPageShow (sample|sample|1.0.0|src/main/ets/pages/Index.ts:381:36)
```

应用的Native栈帧：

```text
00008cdc /data/storage/el1bundle/libs/arm64/libsample.so
```

**3. 筛选部分关键栈帧**

按照栈帧的顺序提取少量信息作为聚类特征，例如仅保留第一帧、第二帧和最后一帧信息作为特征信息。

开发者可根据业务需求制定相应的筛选条件，保证特征信息在同一故障问题上一致即可。

### 生成聚类特征

最终生成的聚类特征是一个包含少量标准化栈帧的业务调用栈序列。

| 原始故障线程栈 | 最终聚类特征（调用顺序从上到下） |
| --- | --- |
| #00 pc 000e8400 /system/lib/ld-musl-arm.so.1  (raise+176)(a40044d0acb68107cfc4adb5049c0725)  #01 pc 00008cdc /data/storage/el1bundle/libs/arm64/libsample.so  (8b74cdc906ea6b2eba95d891bc91c72a)  #02 pc 0005ae00 /system/lib/platformsdk/libace\_napi.z.so  (panda::JSValueRef ArkNativeFunctionCallBack<true>(panda::JsiRuntimeCallInfo\*)+272)(bc1c64aabbe5c7d4db2282a6137443e1)  #03 pc 00de3efc /system/lib/module/arkcompiler/stub.an(RTStub\_PushCallArgsAndDispatchNative+44)  #04 pc 00448dd4 /system/lib/module/arkcompiler/stub.an(BCStub\_HandleCallthis0Imm8V8StwCopy+372)  #05 at triggerCrash (sample|sample|1.0.0|src/main/ets/pages/CppCrash.ts:49:25)  #06 at onPageShow (sample|sample|1.0.0|src/main/ets/pages/Index.ts:381:36)  #07 pc 001e5c8c /system/lib/platformsdk/libark\_jsruntime.so(ce0b05d90b9fae02e7abf8e9f1e5a0f3) | 00008cdc /data/storage/el1bundle/libs/arm64/libsample.so  triggerCrash (sample|sample|1.0.0|src/main/ets/pages/CppCrash.ts:49:25)  onPageShow (sample|sample|1.0.0|src/main/ets/pages/Index.ts:381:36) |

开发者通过比对多份故障日志提取出的聚类特征，对Cpp Crash故障问题进行分类统计。

也可以参考当前故障日志中的Fingerprint字段，对聚类特征内容进行哈希运算生成故障特征标识值，再根据故障特征标识值对Cpp Crash故障问题进行分类统计。

## 不同采集方式下日志规格差异

| 字段 | 描述 | processdump | pdump | liteprocessdump |
| --- | --- | --- | --- | --- |
| Device info | 设备信息 | 有 | 有 | 有 |
| Build info | 版本信息 | 有 | 有 | 有 |
| DeviceDebuggable | 设备的系统版本是否可调试 | 有 | 有 | 有 |
| Fingerprint | 故障特征，聚类同类问题的哈希值，哈希值相同即判定为同一故障原因。 | 有 | 有 | 有 |
| Enabled app log configs | 使能的配置参数列表 | 有 | 无 | 无 |
| Module name | 模块名 | 有 | 有 | 有 |
| ReleaseType | 应用的版本类型 | 有 | 有 | 有 |
| CpuAbi | 二进制接口类型 | 有 | 有 | 有 |
| Version | 应用版本号(点分格式) | 有 | 有 | 有 |
| VersionCode | 应用版本号(整数格式) | 有 | 有 | 有 |
| IsSystemApp | 应用是否为系统应用 | 有 | 有 | 有 |
| PreInstalled | 是否预置应用 | 有 | 有 | 有 |
| Foreground | 前后台状态 | 有 | 有 | 有 |
| Page switch history | 页面切换轨迹 | 有 | 有 | 有 |
| Timestamp | 故障发生时间戳 | 有 | 有 | 有 |
| Pid | 进程号 | 有 | 有 | 有 |
| Uid | 用户ID | 有 | 有 | 有 |
| HiTraceId | HiTraceChain唯一跟踪标识 | 有 | 无 | 无 |
| Process name | 故障进程名 | 有 | 有 | 有 |
| App running unique id | 应用运行时唯一关联的ID | 有 | 无 | 有 |
| Process life time | 故障进程存活时间 | 有 | 有 | 有 |
| Process Memory(kB) | 故障进程内存占用 | 有 | 有 | 有 |
| Device Memory(kB) | 整机内存状态 | 有 | 有 | 有 |
| Log source | 用于标识采集日志的方式 | 有 | 有 | 有 |
| Reason | 故障原因 | 有 | 有 | 有 |
| LastFatalMessage | Fatal消息 | 有 | 无 | 无 |
| Fault thread info | 故障线程信息 | 有 | 有 | 有 |
| SubmitterStacktrace | 提交者线程栈 | 有 | 无 | 无 |
| Registers | 故障现场寄存器 | 有 | 有 | 有 |
| ExtraCrashInfo | 额外的内存信息 | 有 | 无 | 无 |
| Other thread info | 其他线程信息 | 有 | 有 | 有 |
| Memory near registers | 故障现场寄存器附近内存值 | 有 | 有 | 有 |
| FaultStack | 故障线程栈内存信息 | 有 | 有 | 有 |
| Maps | 故障时进程的内存空间 | 有 | 有 | 有 |
| OpenFiles | 故障时进程持有的文件句柄信息 | 有 | 无 | 有 |
| HiLog | 故障之前打印的流水日志，最多1000行 | 有 | 有 | 有 |
| [truncated] | 故障日志截断标志 | 有 | 有 | 有 |
| MergeLog | 三方应用拼接日志标识 | 有 | 无 | 无 |

## 常见问题

### 故障日志中调用栈出现中断

在HarmonyOS系统中，调用栈获取依赖回栈表（记录调用栈信息的表）和frame pointer（栈帧指针）两种机制，需要保证以下两个编译选项开启：

* **-funwind-tables**

  该选项指示编译器在二进制中生成回栈表，用于异常处理和调用栈回溯。
* **-fno-omit-frame-pointer**

  该选项指示编译器将栈帧指针存储在一个寄存器中，用于异常处理和调用栈回溯。

**编译选项开启方法**

以Cmake为例，在CMakeList.txt中添加set(CMAKE\_CXX\_FLAGS "${CMAKE\_CXX\_FLAGS} -fno-omit-frame-pointer -funwind-tables")。

### 应用发生SIGPIPE异常退出

从**API version 24**开始，当应用发生SIGPIPE异常退出时，可开启SIGPIPE信号打印调用栈功能，重启应用后，开发者复现问题场景，可以抓取调用栈信息并输出到HILOG。

**注意** 

此功能只能在[debug版本应用](performance-analysis-kit-terminology.md#debug版本应用)开启。

SIGPIPE异常退出时关键日志如下所示：

```text
应用包名 with pid xxxx exit with signal:13
```

* **SIGPIPE信号说明**

  | 信号值(signo) | 信号 | 解释 | 触发原因 |
  | --- | --- | --- | --- |
  | 13 | SIGPIPE | 非法操作管道或套接字 | - 管道（pipe）或命名管道（FIFO）：写端向管道写入，但读端已经关闭。  - 套接字（socket）：客户端断开连接后，服务端仍尝试往已关闭的连接写数据。 |
* **打开SIGPIPE调试开关**

  在“DevEco Studio”终端中运行命令：hdc shell param set hilog.signal.stack.on SIGPIPE，完成之后需要重新打开应用。设备重启后会失效。
* **验证是否成功开启**

  在HILOG中使用关键字C02D11过滤日志，根据筛选日志能够获取异常发生所在行相应信息，则表示调用栈功能成功开启。

  以通过testSIGPIPE()函数来实现SIGPIPE的异常场景为例：

  ```
  #include <unistd.h>
  #include <signal.h>

  int testSIGPIPE()
  {
      sigset_t set, oldset;
      // 初始化信号集，加入要临时解除阻塞的信号
      sigemptyset(&set);
      sigaddset(&set, SIGPIPE);
      // 先保存当前的信号屏蔽集
      if (sigprocmask(SIG_SETMASK, NULL, &oldset) != 0) {
          return -1;
      }
      // 临时解除阻塞
      if (sigprocmask(SIG_UNBLOCK, &set, NULL) != 0) {
          return -1;
      }
      // 创建pipe后，先关闭读端pipe，然后写端继续写，构建SIGPIPE的异常场景
      int pipe[2]{-1};
      if (pipe2(pipe, 0) != 0) {
          return -1;
      }
      close(pipe[0]);
      int src = 1;
      write(pipe[1], reinterpret_cast<const void*>(&src), sizeof(int));
      close(pipe[1]);
    
      // 最后恢复原来的屏蔽集
      if (sigprocmask(SIG_SETMASK, &oldset, NULL) != 0) {
          return -1;
      }
      return 0;
  }
  ```

  过滤日志信息，根据调用栈信息，成功定位到异常发生在testSIGPIPE()函数中，表示功能开启成功。

  ```text
  ...
  03-06 13:55:25.876   20440-20440   C02D11/process...fxFaultLogger  pid-20440             I     Timestamp:2026-03-06 13:55:25.382
  03-06 13:55:25.876   20440-20440   C02D11/process...fxFaultLogger  pid-20440             I     Pid:19787
  03-06 13:55:25.876   20440-20440   C02D11/process...fxFaultLogger  pid-20440             I     Uid:20020208
  03-06 13:55:25.876   20440-20440   C02D11/process...fxFaultLogger  pid-20440             I     Process name:com.example.myapplication
  03-06 13:55:25.876   20440-20440   C02D11/process...fxFaultLogger  pid-20440             I     Process life time:12s
  03-06 13:55:25.876   20440-20440   C02D11/process...fxFaultLogger  pid-20440             I     Process Memory(kB): 172773(Rss)
  03-06 13:55:25.876   20440-20440   C02D11/process...fxFaultLogger  pid-20440             I     Reason:Signal:SIGPIPE(SI_USER)from:19787:20020208
  03-06 13:55:25.876   20440-20440   C02D11/process...fxFaultLogger  pid-20440             I     Fault thread info:
  03-06 13:55:25.876   20440-20440   C02D11/process...fxFaultLogger  pid-20440             I     Tid:19787, Name:e.myapplication
  03-06 13:55:25.876   20440-20440   C02D11/process...fxFaultLogger  pid-20440             I     #00 pc 00000000001e8150 /system/lib/ld-musl-aarch64.so.1(write+68)(90776dcdb3f38042fc78b97d93138bde)
  03-06 13:55:25.876   20440-20440   C02D11/process...fxFaultLogger  pid-20440             I     #01 pc 0000000000001cf8 /data/storage/el1/bundle/libs/arm64/libentry.so(testSIGPIPE()+228)(d6af99a8111f4c2761800cb1432bea140f5176e4)
  03-06 13:55:25.876   20440-20440   C02D11/process...fxFaultLogger  pid-20440             I     #02 pc 0000000000001e34 /data/storage/el1/bundle/libs/arm64/libentry.so(d6af99a8111f4c2761800cb1432bea140f5176e4)
  ...
  ```

### 内存问题引发的Crash故障

**问题现象**

Crash日志如包含以下两种信息：

1. 故障信息中包含LastFatalMessage: This is an unexpected memory usage behavior。
2. 故障信息中未包含上述LastFatalMessage信息，但故障线程的调用栈栈顶为jemalloc调用ld-musl-aarch64.so.1(crash\_brk+0)。

**可能原因**

以上两种日志信息表示发生了内存访问异常的问题，从而导致触发Crash，这种Crash的内存问题原因主要有两类：

1. Double Free：内存释放成功后，在释放内存写入特殊标记（6b），再次释放该内存时会检测到这些标记，导致触发Crash。
2. UAF(Use After Free)： 内存释放成功后再次读取或写入，由于内存释放后写入特殊标记(6b)，再次读取或写入会触发Crash，这种Crash日志中可以查找到6b字样。

总之，内存问题触发的Crash日志可查找对应内存是否存在特殊标记（6b），来判断该内存地址是否已被jemalloc释放过。

**解决措施**

当发现故障日志信息中，有以上现象时，可根据故障信息中内存内容来查找特殊标记（6b），找到对应的内存地址，结合代码分析定位并修复Double Free或UAF问题。

以下为一个Double Free案例，代码片段如下：

```
// ...
// 开启jemalloc cache, 确保触发内存标记写入
mallopt(M_OHOS_CONFIG, M_TCACHE_PERFORMANCE_MODE);
mallopt(M_OHOS_CONFIG, M_ENABLE_OPT_TCACHE);
mallopt(M_SET_THREAD_CACHE, M_THREAD_CACHE_ENABLE);
char* test = (char*)malloc(4096);
// 这里日志输出test地址值，方便查找crash日志中内存内容
std::cout << "test addr: " << std::hex << test << std::endl;
free(test);
free(test); // Double Free
// ...
```

查看对应生成的Crash日志：

```text
Generated by HiviewDFX@HarmonyOS
================================================================
Device info:HUAWEI Mate 70
Build info:CLS-AL00 6.1.0.263(C00E1R4P3DEVDUlog)
DeviceDebuggable:Yes
Fingerprint:27af54212714ee9cc5026e020716783795c2ae8434730476532415be04f0277d
Module name:test_processdump
Timestamp:2026-01-14 19:52:53.207
Pid:43588
Uid:0
Process name:./test_processdump
Process life time:1s
Process Memory(kB): 18497(Rss)
Device Memory(kB): Total 11688320, Free 704432, Available 6171648
Log source:processdump <- 用于标识采集日志的方式，processdump表示由用户态生成
Reason:Signal:SIGTRAP(TRAP_BRKPT)@0x0000005a6cabe068
LastFatalMessage:This is an unexpected memory usage behavior.may double free   ----> 发生了内存问题触发的Crash。
Fault thread info:
Tid:43588, Name:test_processdum
#00 pc 00000000000b3068 /system/lib/ld-musl-aarch64.so.1(cache_bin_dalloc_safety_checks+108)(f4bc554163a467382fbc9026ef320fb7)
#01 pc 00000000000bfd38 /system/lib/ld-musl-aarch64.so.1(je_free+408)(f4bc554163a467382fbc9026ef320fb7)
#02 pc 00000000000515c8 /data/test/test_processdump((anonymous namespace)::ProcessDumpTest_DfxProcessTest008_Test::TestBody()+260)(bcace1bb3be03ebd7b59c921eb0c9f42)
#03 pc 00000000000ca924 /data/test/test_processdump(testing::internal::UnitTestImpl::RunAllTests()+6676)(bcace1bb3be03ebd7b59c921eb0c9f42)
#04 pc 00000000000c8d44 /data/test/test_processdump(testing::UnitTest::Run()+120)(bcace1bb3be03ebd7b59c921eb0c9f42)
#05 pc 00000000000b11bc /data/test/test_processdump(main+100)(bcace1bb3be03ebd7b59c921eb0c9f42)
#06 pc 00000000000afe58 /system/lib/ld-musl-aarch64.so.1(libc_start_main_stage2+80)(f4bc554163a467382fbc9026ef320fb7)
Registers:
x0:0000000000000000 x1:0000000000000000 x2:0000005a6cc1f1e0 x3:0000007f43f875a0
x4:0000005a6cefdbf0 x5:0000007f43f87580 x6:0000007f43f87580 x7:3030306361326436
x8:0000000000000000 x9:0000005a6f452fc4 x10:0000000000000000 x11:0000005a6f452f68
x12:000000000000001f x13:0000007f43f875c8 x14:0000000000000000 x15:0000000000000000
x16:0000005a6f451a38 x17:0000005a6cbfa3cc x18:0000000000000000 x19:0000005a6d2ac000
x20:0000005a6cabdc50 x21:0000005a6d2a21d8 x22:0000005a6ce2a000 x23:0000005a6d2a2228
x24:0000005a6f447778 x25:0000005a6d29ab00 x26:20c49ba5e353f7cf x27:0000000000000005
x28:0000000000000001 x29:0000007f43f87610
lr:0000005a6cabe094 sp:0000007f43f87610 pc:0000005a6cabe068
pstate:0000000040001000 esr:00000000f2000001
...
x19([anon:native_heap:jemalloc]):
    0000005a6d2abff0 0000000000000000
    0000005a6d2abff8 0000000000000000
    0000005a6d2ac000 6b6b195687b5f541   ---->  内存地址位置的内容为6b6b195687b5f541,表明该地址已被释放过。
    0000005a6d2ac008 0000000000000000
    0000005a6d2ac010 0000000000000000
    0000005a6d2ac018 0000000000000000
    0000005a6d2ac020 0000000000000000
    0000005a6d2ac028 0000000000000000
    0000005a6d2ac030 0000000000000000
    0000005a6d2ac038 0000000000000000
    0000005a6d2ac040 0000000000000000
    0000005a6d2ac048 0000000000000000
    0000005a6d2ac050 0000000000000000
    0000005a6d2ac058 0000000000000000
    0000005a6d2ac060 0000000000000000
    0000005a6d2ac068 0000000000000000
    0000005a6d2ac070 0000000000000000
    0000005a6d2ac078 0000000000000000
    0000005a6d2ac080 0000000000000000
```

内存地址5a6d2ac000被填填充了6b开头的字节内容，表明该地址为已被释放。查看程序运行时日志打印：

```text
test addr: 5a6d2ac000
```

test指针的内存地址是5a6d2ac000，表明test指针发生了Double Free，找到对应代码修复指针重复释放问题。
