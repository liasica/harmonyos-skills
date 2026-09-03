---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-stability-sanitizer-overview-fault-mode
title: 地址越界故障模式概述
breadcrumb: 最佳实践 > 稳定性 > 稳定性分析 > 稳定性故障模式说明 > 地址越界故障模式说明 > 地址越界故障模式概述
category: best-practices
scraped_at: 2026-09-04T06:33:23+08:00
doc_updated_at: 2026-09-03
content_hash: sha256:5536b9d35d99b1043afdf854f874baa6f9ecc5670f5b72c765153985b6b379ae
---

## 概述

在应用运行过程中，内存边界计算错误、对象生命周期管理不当、资源所有权混乱、多线程并发冲突等问题，均会引发严重隐患。程序可能因此访问无效地址、破坏内存数据或错误使用系统资源。此类问题通常具有偶现性强、复现条件复杂、故障非第一现场等特点。情况严重时，可能造成数据异常、功能失效甚至应用闪退。

本文档旨在系统梳理常见故障场景、日志特征、分析步骤和修复方法，帮助开发者根据故障日志快速识别问题类型、定位异常代码。本文涵盖HWASan（Hardware-assisted AddressSanitizer）、ASan（AddressSanitizer）、GWP-ASan（GWP-ASan Will Provide Allocation SANity）、TSan（ThreadSanitizer）、UBSan（Undefined Behavior Sanitizer）和fdsan（file descriptor sanitizer）等故障检测能力，并重点介绍以下七类故障模式：

* [内存越界访问故障模式说明](bpta-stability-memory-overflow-fault-mode.md)：堆、栈内存对象均具有明确的有效地址范围。索引计算错误可能导致程序读写对象边界之外的地址，引发内存越界访问，造成数据异常或应用崩溃。开启HWASan、ASan或GWP-ASan检测能力后，可在越界访问时记录异常地址、访问大小和现场调用栈等信息。本文结合HWASan、ASan和GWP-ASan典型案例，介绍此类问题的日志特征与定位方法。
* [内存释放后访问故障模式说明](bpta-stability-memory-uaf-fault-mode.md)：堆内存释放后或栈变量生命周期结束后，原有指针将失效，若程序继续通过失效指针读写内存，将导致内存释放后访问。此类问题可能表现为读取错误数据，导致业务异常；也可能破坏其他有效内存，使应用后续在其他位置崩溃，问题难以定位。开启HWASan、ASan或GWP-ASan检测能力后，可在访问失效内存时检测异常，并记录异常访问、内存分配和释放等调用栈。本文结合HWASan、ASan和GWP-ASan典型案例，介绍此类问题的日志特征与定位方法。
* [内存重复释放故障模式说明](bpta-stability-memory-double-free-fault-mode.md)：释放同一块内存后，若程序再次通过原指针或其他别名指针释放该内存，将导致堆内存重复释放。此类问题可能破坏堆内存管理结构，造成应用立即崩溃或后续在其他程序位置随机异常，故障现场难以追溯。开启HWASan、ASan或GWP-ASan检测能力后，可在重复释放发生时检测异常，并记录内存分配、首次释放和重复释放等调用栈。本文结合HWASan、ASan和GWP-ASan典型案例，介绍此类问题的日志特征与定位方法。

* [内存释放地址异常故障模式说明](bpta-stability-memory-invalid-free-fault-mode.md)：内存释放要求传入有效的堆内存对象起始地址，若传入的是偏移后的地址、未初始化指针、野指针或非堆内存地址等，将导致非法释放。此类问题可能直接在释放接口中触发崩溃，也可能破坏堆内存管理结构，随后在其他模块的内存分配或释放过程中暴露该问题，导致故障现场难以追溯。开启ASan或GWP-ASan检测能力后，可在非法释放时检测异常并记录现场调用栈。本文结合ASan和GWP-ASan典型案例，介绍此类问题的日志特征与定位方法。
* [文件句柄非法关闭故障模式说明](bpta-stability-fd-invalid-close-fault-mode.md)：错误对象关闭文件句柄、重复关闭文件句柄，或混用文件描述符与FILE\*接口，都会引发文件句柄非法关闭。此类问题可能触发文件读写失败、误关其他资源或应用崩溃。开启fdsan检测能力后，系统可校验文件描述符的实际所有者与预期所有者，并记录相关信息。本文结合句柄重复释放等典型案例，介绍此类问题的日志特征与定位方法。
* [未定义异常访问故障模式说明](bpta-stability-undefined-behavior-fault-mode.md)：程序在运行过程中若违反C/C++语言规范，例如除零运算、使用未对齐地址、数值转换溢出等，可能触发未定义行为。此类问题的执行结果不可预测，可能导致数据异常、功能异常或应用崩溃。开启UBSan检测能力后，可在运行阶段检测相关未定义行为，并记录异常类型、代码位置等信息。本文结合典型案例，介绍此类问题的日志特征与定位方法。
* [数据竞争异常访问故障模式说明](bpta-stability-data-race-fault-mode.md)：多个线程未正确同步并发访问共享内存，或错误使用线程同步和信号处理机制时，可能引发数据竞争及并发访问异常。此类问题可能造成数据错误或应用崩溃，且受线程执行时序影响，难以稳定复现。开启TSan检测能力后，可记录冲突访问线程及其调用栈。本文结合多线程读写冲突、并发释放后使用、信号处理异常和非法解锁等案例，介绍此类问题的日志特征与定位方法。

## 故障检测机制

HarmonyOS提供HWASan、ASan、GWP-ASan、TSan、UBSan和fdsan等故障检测能力，覆盖了从开发、测试到运维的全生命周期。可用于检测内存访问异常、多线程数据竞争、未定义行为及文件描述符异常等问题。各故障检测能力如下表所示：

| 能力 | 概述 | 故障类型 | 使用场景 |
| --- | --- | --- | --- |
| **HWASan** | 利用ARM64 TBI（Top Byte Ignore）特性，基于编译插桩和内存标签机制，为指针和内存设置Tag，并在访问时校验二者是否匹配。 | 堆/栈内存越界、堆/栈内存释放后访问、堆内存重复释放、堆非法释放。 | 开发态 |
| **ASan** | 基于编译插桩和影子内存机制，在内存对象边界周围设置红区，并通过影子内存记录内存状态。在内存读写时，一旦访问红区或已释放内存，立即触发异常并生成故障日志。 | 堆/栈内存越界、堆/栈内存释放后访问、堆内存重复释放、堆非法释放。 | 开发态 |
| **GWP-ASan** | 通过概率采样拦截堆分配，将其放入受保护内存池，并记录其分配和释放信息。 | 堆内存越界、堆内存释放后访问、堆内存重复释放、堆非法释放。 | 运维态 |
| **TSan** | 基于编译插桩和运行时访问跟踪，记录多线程内存访问及同步关系，检测并发异常。 | 多线程数据竞争、锁错误检测、条件变量错误检测。 | 开发态 |
| **UBSan** | 在编译时插桩，在程序运行过程中检查违反C/C++语言规范的未定义行为。 | 整数溢出、未对齐访问、异常类型转换、除零错误。 | 开发态 |
| **fdsan** | 基于文件描述符所有权标记机制，在关闭文件描述符时校验关闭方与预期所有者是否匹配。 | 句柄重复关闭。 | 运维态 |

## 日志规格

HarmonyOS系统在检测到地址越界之后，会生成相应故障日志。日志通常包含进程基本信息、异常描述和调用栈，部分日志还会记录寄存器快照、内存映射等信息。开发者可根据不同检测能力的日志关键字段定位问题。

地址越界日志详情请参考：[日志规格](../harmonyos-guides/address-sanitizer-guidelines.md#日志规格)。

## 日志获取方式

HarmonyOS提供多条路径获取故障日志，包括开发态和运维态，开发者可根据当前所处的开发阶段选择对应方式。

地址越界日志获取方式详情请参考：[日志获取方式](../harmonyos-guides/address-sanitizer-guidelines.md#日志获取方式)。

## 地址越界事件

HarmonyOS通过HiAppEvent提供地址越界事件订阅能力。应用调用HiAppEvent的[addWatcher()](../harmonyos-references/js-apis-hiviewdfx-hiappevent.md#hiappeventaddwatcher)接口订阅地址越界事件。当系统检测到相关异常时，会生成对应的事件信息和故障日志，并通过HiAppEvent将事件回调给应用。开发者可根据事件中的故障类型、日志路径等信息获取故障日志并分析问题。

地址越界事件字段详情请参考：[事件字段说明](../harmonyos-guides/hiappevent-watcher-address-sanitizer-events.md#事件字段说明)。

事件订阅机制请参考：[事件订阅](../harmonyos-guides/hiappevent.md)。

订阅地址越界事件（ArkTS）请参考：[订阅地址越界事件（ArkTS）](../harmonyos-guides/hiappevent-watcher-address-sanitizer-events-arkts.md)。

订阅地址越界事件（C/C++）请参考：[订阅地址越界事件（C/C++）](../harmonyos-guides/hiappevent-watcher-address-sanitizer-events-ndk.md)。
