---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-stability-fd-invalid-close-fault-mode
title: 文件句柄非法关闭故障模式说明
breadcrumb: 最佳实践 > 稳定性 > 稳定性分析 > 稳定性故障模式说明 > 地址越界故障模式说明 > 文件句柄非法关闭故障模式说明
category: best-practices
scraped_at: 2026-09-04T06:33:23+08:00
doc_updated_at: 2026-09-03
content_hash: sha256:438e31e4ac435b601020a151436ef51b71bf2479811840ea0416c142e6fc938d
---

## 根因描述

文件句柄（File Descriptor，简称fd）是操作系统分配给进程用于管理I/O资源的整数标识。在程序中，打开文件、创建套接字、建立管道等操作都会生成一个文件描述符。若出现重复关闭、混用文件描述符与FILE\*接口等错误操作，将导致文件句柄非法关闭问题。在多线程环境中，文件句柄非法关闭可能引发数据损坏、内存泄漏或文件句柄泄漏等安全隐患。

## 问题分析思路

文件句柄非法关闭问题通常由以下原因导致：

1. **double-close**：对同一个文件描述符执行了两次关闭操作，第二次关闭时系统可能已复用该fd，导致误关闭其他线程打开的文件。

问题分析步骤如下：

1. **确认故障类型：**根据LastFatalMessage的内容，判断具体的错误类型。常见的LastFatalMessage类型及其含义如下：

   | LastFatalMessage | 含义 | 常见原因 |
   | --- | --- | --- |
   | attempted to close file descriptor <fd>, expected to be unowned, actually owned by <owner> | fd被非法关闭 | 对已有属主的fd执行了原始close()，而非属主对应的关闭接口（如fclose()或fdsan\_close\_with\_tag()） |
   | attempted to close file descriptor <fd>, expected to be owned by <owner>, actually unowned | fd被关闭后仍尝试属主关闭 | fd已被关闭或属主tag已清除，再使用fdsan\_close\_with\_tag()关闭，属于use-after-close或double-close |
   | attempted to close file descriptor <fd>, expected to be owned by <owner1>, actually owned by <owner2> | fd属主不匹配 | fd的所有权已被其他对象接管，当前属主再尝试关闭 |
   | EBADF: close failed for fd <fd> with expected tag: <tag> | fclose()关闭无效fd | FILE\*对应的fd已被原始close()关闭，fclose()再尝试关闭时fd已无效 |
   | failed to exchange ownership of file descriptor: fd <fd>, was owned by <owner>, was expected to be unowned | exchange时fd已有属主 | 对已设置tag的fd调用fdsan\_exchange\_owner\_tag()设置新tag，期望fd无属主但实际已有属主 |
   | failed to exchange ownership of file descriptor: fd <fd> is unowned, was expected to be owned by <owner> | exchange时fd已无属主 | fd已被关闭后仍尝试以原属主tag调用fdsan\_exchange\_owner\_tag()，属于use-after-close |
   | failed to exchange ownership of file descriptor: fd <fd>, was owned by <owner1>, was expected to be owned by <owner2> | exchange时属主不匹配 | fd的所有权已被其他对象接管，再尝试以原属主tag调用fdsan\_exchange\_owner\_tag() |

   在多线程场景下，fdsan日志中的owner信息不一定对应fd最初的属主。例如线程A关闭fd后，系统可能立即将相同的fd编号分配给线程B，并绑定新的owner tag。此时线程A再次错误关闭该fd时，fdsan日志中显示的actual owner可能已经是线程B的owner tag。

   因此，不能仅根据日志中的owner信息直接判断责任方，还需要结合fd生命周期、调用栈以及其他模块对该fd的使用情况综合分析。
2. **代码分析**：通过llvm-addr2line工具（参考：[C++堆栈解析流程](../harmonyos-guides/ide-exception-stack-parsing-principle.md#section1735713501344)中对于llvm-addr2line的使用），结合调用栈文件和地址偏移，定位到具体业务代码行。根据代码上下文，分析其中存在的逻辑问题，找到异常使用或者释放fd的原因，必要时沿栈帧多分析几层。
3. **更多日志**：结合崩溃日志文件中的其他信息还原故障现场。同时参考hilog（HarmonyOS 日志系统，用于采集系统及应用运行日志）和kmsg（kernel message，内核消息日志，用于记录内核侧运行信息）等日志，进行综合定位。

## 关键字

关注CppCrash或者fdsan故障日志中是否有如下关键字：

* DEBUG SIGNAL(FDSAN)
* LastFatalMessage
* SIGABRT

## 案例分析

以下案例均未额外设置 fdsan\_error\_level，使用默认的FDSAN\_ERROR\_LEVEL\_WARN\_ALWAYS模式。该模式仅生成fdsan告警日志，不会触发应用崩溃。

如需在检测到异常时触发崩溃，可参考[fdsan使用指导](../harmonyos-guides/fdsan.md)，通过fdsan\_set\_error\_level()接口将fdsan\_error\_level设置为FDSAN\_ERROR\_LEVEL\_FATAL。

### 案例：句柄被double-close

**问题现象**

业务代码调用后，DevEco Studio告警并生成fdsan故障日志。

**问题分析**

1. 查看崩溃文件内容。

   证据1：进程异常使用句柄触发了fdsan检测生成故障日志。EBADF: close failed for fd 68 with expected tag: 0x01000059e724e2e8表示fclose()关闭了无效fd。

   ```screen
   Reason:Signal:DEBUG SIGNAL(FDSAN)
   LastFatalMessage:EBADF: close failed for fd 68 with expected tag: 0x01000059e724e2e8
   ```

   说明1：LastFatalMessage是fdsan故障检测时的最后一条fatal级别日志，对于fdsan类问题其一般能提供fd异常使用的原因类别，对定位该类问题有很大帮助。
2. 分析崩溃栈。ld-musl-aarch64.so.1中的栈帧，为触发fdsan的常见流程，可以跳过该部分到业务栈帧。

   证据2：#00-#01帧展示了fdsan主动检测部分的堆栈信息，表明fdsan检测到了句柄使用异常。触发的函数来源于#07帧的anonymous entry，位于xsan\_fileHandleCloseillegally.ets文件的39行，该函数调用到libentry.so内，执行了fclose()命令后触发了fdsan异常扫描，生成故障日志。

   ```screen
   Fault thread info:
   Tid:56492, Name:xample.dfx_test
   #00 pc 00000000001817d8 /system/lib/ld-musl-aarch64.so.1(fdsan_error+740)(7cf8b7b4510e12a63e6a3a479a770ae4)
   #01 pc 0000000000181ad8 /system/lib/ld-musl-aarch64.so.1(fdsan_close_with_tag+616)(7cf8b7b4510e12a63e6a3a479a770ae4)
   #02 pc 00000000001dbe2c /system/lib/ld-musl-aarch64.so.1(fclose+68)(7cf8b7b4510e12a63e6a3a479a770ae4)
   #03 pc 000000000008af3c /data/storage/el1/bundle/libs/arm64/libentry.so(5f8efa0006d1a4ae66229f5411364d2eecdedc1f)
   #04 pc 0000000000062674 /system/lib64/platformsdk/libace_napi.z.so(panda::JSValueRef ArkNativeFunctionCallBack<true>(panda::JsiRuntimeCallInfo*)+236)(790355d8b83b7c804589de4d345e30e5)
   #05 pc 0000000000e86b98 /system/lib64/module/arkcompiler/stub.an(RTStub_PushCallArgsAndDispatchNative+40)
   #06 pc 0000000000d29818 /system/lib64/module/arkcompiler/stub.an(BCStub_HandleCallthis0Imm8V8StwCopy+396)
   #07 at anonymous entry (entry/src/main/ets/pages/page_second/page_third_xsan/xsan_fileHandleCloseillegally.ets:39:30)
   ```

   说明2：通常认为标准库、系统库较为稳定，因此优先分析异常调用栈中业务部分的栈。
3. 获取问题版本对应的带符号的so，通过llvm-addr2line工具（参考：[C++堆栈解析流程](../harmonyos-guides/ide-exception-stack-parsing-principle.md#section1735713501344)中对于llvm-addr2line的使用）定位行号并找到执行上下文。

   通常用法为"llvm-addr2line -Cfie libentry.so 000000000008af3c"，即可定位到代码行号，so为带符号版本。

   证据3：从上往下跳过C库和fdsan检测的调用栈，找到触发fdsan扫描的栈。

   说明3：由于fd被double-close触发fdsan检测，代码如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a5/v3/g9b0IrIPRleglKLWJjlciA/zh-cn_image_0000002729491387.png)

**问题结论与总结**

句柄被double-close触发fdsan故障。

**修复建议**

1. 明确责任主体：谁申请，谁释放。
2. 规范句柄释放流程：同一执行路径下不能重复close()同一个文件句柄。释放后应及时更新句柄状态，避免后续误操作。
