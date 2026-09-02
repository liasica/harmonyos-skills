---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-app-main-thread-block
title: 应用主线程阻塞故障模式说明
breadcrumb: 最佳实践 > 稳定性 > 稳定性分析 > 稳定性故障模式说明 > 应用冻屏故障模式说明 > 应用主线程阻塞故障模式说明
category: best-practices
scraped_at: 2026-09-02T15:03:23+08:00
doc_updated_at: 2026-07-22
content_hash: sha256:9f8abf0823f1ac67932471259e25647d249928b7a306843c12fe42a1c0622b76
---

## 概述

本文旨在指导HarmonyOS应用开发者如何定位主线程阻塞类型的应用冻屏（AppFreeze）问题。通过分析应用冻屏故障日志中的主线程堆栈，将主线程阻塞类型的应用冻屏问题分为以下故障根因：

* [等锁](bpta-app-main-thread-block.md#section138261239153915)
* [同步Binder接口调用阻塞](bpta-app-main-thread-block.md#section715018255107)
* [对端Binder线程满](bpta-app-main-thread-block.md#section46121838121717)
* [同步耗时I/O操作](bpta-app-main-thread-block.md#section128357941815)
* [触发长时间GC](bpta-app-main-thread-block.md#section192572721819)
* [触发长时间抓取内存快照](bpta-app-main-thread-block.md#section763875871819)
* [执行耗时操作](bpta-app-main-thread-block.md#section1137920772012)

**说明** 

开发者可通过阅读[AppFreeze（应用冻屏）检测](../harmonyos-guides/appfreeze-guidelines.md)了解关于应用冻屏（AppFreeze）问题的检测原理和日志说明。

## 确认问题类型

对于一个应用冻屏（AppFreeze）问题，可通过AppFreeze日志和其增强日志（采样栈）确认是否为主线程阻塞类型：

* 通过AppFreeze日志确认

对比告警和卡死两次事件的主线程堆栈是否一致。两次事件包括：THREAD\_BLOCK\_3S和THREAD\_BLOCK\_6S、THREAD\_BLOCK\_3S和APP\_INPUT\_BLOCK、LIFECYCLE\_HALF\_TIMEOUT和LIFECYCLE\_TIMEOUT。若堆栈一致，通常情况下表明是主线程阻塞类型，建议结合增强日志进行更准确的判定。

**说明** 

若AppFreeze日志中仅有APP\_INPUT\_BLOCK事件的单次主线程堆栈，则无法判定为主线程阻塞类型。

* 通过AppFreeze日志和增强日志确认

对比AppFreeze日志中的主线程堆栈以及增强日志中的主线程采样栈是否一致，一致则表明是主线程阻塞类型。

此外可以参考[堆栈信息](../harmonyos-guides/appfreeze-guidelines.md#堆栈信息)章节中线程状态的介绍来判断线程在冻屏发生过程中是否在运行。

## 根因分类

### 等锁

**根因描述**

应用的主线程业务等锁导致阻塞。

**问题分析思路**

1. 根据堆栈找到持锁的业务共享库，通过符号或者使用[llvm-addr2line](bpta-stability-app-crash-cpp-way.md#li186453444512)解析共享库定位到代码行，确认等待的锁资源，记为锁A；
2. 在故障应用的进程堆栈中搜索等待锁A的业务共享库，找到包含该业务共享库的线程的堆栈，然后结合代码找出其中持有锁A的线程堆栈；
3. 若持有锁A的线程堆栈的根因不是等锁，则按对应的根因继续分析；
4. 若持有锁A的线程堆栈的根因也是等锁，记为锁B，则按本章节分析思路重新分析。

   **说明** 

   若持有锁A的线程即主线程，或者持有锁A的线程等待的锁B被主线程或者其他等待锁A的线程持有，则该问题类型为死锁。

**关键字**

关注主线程堆栈栈顶共享库和符号是否匹配如下关键字。

共享库：

ld-musl-aarch64.so.1

符号：

* \_\_timedwait\_cp
* pthread\_join

**案例分析**

**案例一：子线程和主线程AB锁互锁导致主线程阻塞**

**问题现象**

当用户触发业务代码调用后，应用进入无响应状态，一段时间后应用退出，并生成冻屏日志文件。

**问题分析**

1. 查看AppFreeze中THREAD\_BLOCK\_3S和THREAD\_BLOCK\_6S两部分的主线程堆栈。确认一致后，分析堆栈内容。

   证据1：主线程堆栈关键栈帧

   ```screen
   Tid:18728, Name:pfreezeanalysis
   state=S, utime=55, stime=15, priority=-54, nice=-10, clk=100
   #00 pc 00000000001de3f0 /system/lib/ld-musl-aarch64.so.1(__timedwait_cp+156)(ede7850a729ebc7f50c03216608d9277)
   #01 pc 00000000001e4488 /system/lib/ld-musl-aarch64.so.1(__pthread_mutex_timedlock_inner+536)(ede7850a729ebc7f50c03216608d9277)
   #02 pc 000000000000a6c8 /data/storage/el1/bundle/libs/arm64/libentry.so(f5f54ab64da94326c537007dfa9fbf43b7db6ea1)
   #03 pc 000000000007010c /system/lib64/platformsdk/libace_napi.z.so(panda::JSValueRef ArkNativeFunctionCallBack<true>(panda::JsiRuntimeCallInfo*)+284)(c41c28aa2f0cdd937fc9063a8b806514)
   #04 pc 0000000000e8ad70 /system/lib64/module/arkcompiler/stub.an(RTStub_AsmInterpreterEntry+484)
   #05 pc 0000000000e8abc8 /system/lib64/module/arkcompiler/stub.an(RTStub_AsmInterpreterEntry+60)
   ```

   #02栈帧表明等锁的业务方是libentry.so，结合代码继续分析。
2. 开发调试场景下可直接在DevEco Studio中单击libentry.so所在的栈帧跳转到对应代码行；运维场景下使用[llvm-addr2line](bpta-stability-app-crash-cpp-way.md#li186453444512)解析找到对应代码行。

   证据2：故障栈帧所在的代码

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8e/v3/IRLfICe9TDuU8JpNk-y7tQ/zh-cn_image_0000002673575729.png "点击放大")

   代码行指向pthread\_mutex\_lock(&g\_deadlockMutexSecond)，即等待锁g\_deadlockMutexSecond。继续分析g\_deadlockMutexSecond的持锁情况。
3. 在代码中查找g\_deadlockMutexSecond，确认除TriggerDeadlockSync外，仅在DeadlockOtherThread中有使用。

   证据3：DeadlockOtherThread的实现代码

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/19/v3/gLfwLoQuQ4uflcNp_jBwXg/zh-cn_image_0000002673735601.png)

   DeadlockOtherThread是在主线程创建的子线程中调用的。子线程进入后先获取锁g\_deadlockMutexSecond，然后等待1s再获取锁g\_deadlockMutexFirst。创建子线程前主线程就已经获取g\_deadlockMutexFirst，创建子线程后主线程又去获取g\_deadlockMutexSecond。主线程和子线程发生死锁，主线程一直等锁阻塞。

**案例二：两个子线程死锁，主线程无法等到子线程结束导致阻塞**

**问题现象**

当用户触发业务代码调用后，应用进入无响应状态，一段时间后应用退出，并生成冻屏日志文件。

**问题分析**

1. 查看AppFreeze中THREAD\_BLOCK\_3S和THREAD\_BLOCK\_6S两部分的主线程堆栈。确认一致后，分析堆栈内容。

   证据1：主线程堆栈关键栈帧

   ```screen
   Tid:30591, Name:pfreezeanalysis
   state=S, utime=21, stime=14, priority=-54, nice=-10, clk=100
   #00 pc 00000000001e3578 /system/lib/ld-musl-aarch64.so.1(pthread_join+136)(ede7850a729ebc7f50c03216608d9277)
   #01 pc 000000000000aae0 /data/storage/el1/bundle/libs/arm64/libentry.so(f5f54ab64da94326c537007dfa9fbf43b7db6ea1)
   #02 pc 000000000007010c /system/lib64/platformsdk/libace_napi.z.so(panda::JSValueRef ArkNativeFunctionCallBack<true>(panda::JsiRuntimeCallInfo*)+284)(c41c28aa2f0cdd937fc9063a8b806514)
   #03 pc 0000000000e8ad70 /system/lib64/module/arkcompiler/stub.an(RTStub_AsmInterpreterEntry+484)
   #04 pc 0000000000e8abc8 /system/lib64/module/arkcompiler/stub.an(RTStub_AsmInterpreterEntry+60)
   ```

   #01栈帧表明等锁的业务方是libentry.so，结合代码继续分析。
2. 开发调试场景下可直接在DevEco Studio中单击libentry.so所在的栈帧跳转到对应代码行；运维场景下使用[llvm-addr2line](bpta-stability-app-crash-cpp-way.md#li186453444512)解析找到对应代码行。

   证据2：故障栈帧所在的代码

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ea/v3/Wq0PGuleSuGDTD3M3QEQ1g/zh-cn_image_0000002643575818.png "点击放大")

   代码行指向pthread\_join(t1, nullptr)，即等待子线程结束。继续分析子线程的实现。
3. 查看t1和t2两个子线程的实现代码。

   证据3：两个子线程的实现代码

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4f/v3/eQZK3X_LTISOqccw89cFBg/zh-cn_image_0000002643415864.png)

   线程A进入后先获取锁g\_deadlockMutexFirst，然后等待1ms再获取锁g\_deadlockMutexSecond。线程B则反过来，先获取锁g\_deadlockMutexSecond再等待1ms获取锁g\_deadlockMutexFirst。这样两个子线程进入后都获取到了对方想要获取的锁，从而造成死锁。两个子线程都无法结束，导致主线程等待阻塞。

**预防建议**

优化锁的使用策略，减少锁竞争，建议使用无锁数据结构。

### 同步Binder接口调用阻塞

**根因描述**

应用主线程业务向系统服务或其他进程发起调用同步Binder接口，对端长时间未返回，导致阻塞。

**问题分析思路**

1. 根据堆栈找到发起IPC的应用侧业务和服务接口；
2. 根据主线程ID在Binder信息中找到对端服务进程的进程号和IPC线程号；
3. 根据对端服务进程号找到对端服务进程堆栈，再找到对应的IPC线程堆栈；
4. 确认IPC线程阻塞的根因，再按对应根因的分析思路继续分析。

**关键字**

关注主线程堆栈共享库和符号是否匹配如下关键字。

共享库：

libipc\_common.z.so

符号：

WriteBinder

**案例分析**

**案例：系统音频服务未及时响应导致主线程阻塞**

**问题现象**

当用户触发业务代码调用后，应用进入无响应状态，一段时间后应用退出，并生成冻屏日志文件。

**问题分析**

1. 查看AppFreeze中THREAD\_BLOCK\_3S和THREAD\_BLOCK\_6S两部分的主线程堆栈。确认一致后，分析堆栈内容。

   证据1：主线程堆栈关键栈帧

   ```screen
   Tid:41777, Name:pfreezeanalysis
   state=S, utime=118, stime=49, priority=-14, nice=-10, clk=100
   #00 pc 0000000000197768 /system/lib/ld-musl-aarch64.so.1(ioctl+172)(8c2ca4e308a1de9ed1e6b4ccc14c7443)
   #01 pc 000000000000f0ac /system/lib64/platformsdk/libipc_common.z.so(OHOS::BinderConnector::WriteBinder(unsigned long, void*)+120)(21def93073c96c4161bfa61b948c2957)
   #02 pc 0000000000074934 /system/lib64/platformsdk/libipc_single.z.so(OHOS::BinderInvoker::TransactWithDriver(bool)+284)(5a12a4b7e05d71d18ea20b9f1e1aed8a)
   #03 pc 0000000000073154 /system/lib64/platformsdk/libipc_single.z.so(OHOS::BinderInvoker::WaitForCompletion(OHOS::MessageParcel*)+124)(5a12a4b7e05d71d18ea20b9f1e1aed8a)
   #04 pc 0000000000072624 /system/lib64/platformsdk/libipc_single.z.so(OHOS::BinderInvoker::SendRequest(int, unsigned int, OHOS::MessageParcel&, OHOS::MessageParcel&, OHOS::MessageOption&)+620)(5a12a4b7e05d71d18ea20b9f1e1aed8a)
   #05 pc 0000000000049d24 /system/lib64/platformsdk/libipc_single.z.so(OHOS::IPCObjectProxy::SendRequestInner(bool, unsigned int, OHOS::MessageParcel&, OHOS::MessageParcel&, OHOS::MessageOption&)+272)(5a12a4b7e05d71d18ea20b9f1e1aed8a)
   #06 pc 000000000004a73c /system/lib64/platformsdk/libipc_single.z.so(OHOS::IPCObjectProxy::SendRequest(unsigned int, OHOS::MessageParcel&, OHOS::MessageParcel&, OHOS::MessageOption&)+216)(5a12a4b7e05d71d18ea20b9f1e1aed8a)
   #07 pc 0000000000040dd4 /system/lib64/libaudio_policy_client_idl_interface.z.so(OHOS::AudioStandard::AudioPolicyProxy::GetAudioScene(int&)+320)(b95b8a9a8cca6ee70d60967fc1751cc5)
   #08 pc 000000000008cfec /system/lib64/platformsdk/libaudio_client.z.so(OHOS::AudioStandard::AudioSystemManager::GetAudioScene() const+44)(0e4839c7e3f20d5152f89c053c31d414)
   #09 pc 00000000000e0c44 /system/lib64/module/multimedia/libaudio.z.so(OHOS::AudioStandard::NapiAudioManager::GetAudioSceneSync(napi_env__*, napi_callback_info__*) (.cfi)+228)(3201d994d8d5f9e8fdf1c9aa5ed39509)
   #10 pc 0000000000067c90 /system/lib64/platformsdk/libace_napi.z.so(panda::JSValueRef ArkNativeFunctionCallBack<true>(panda::JsiRuntimeCallInfo*)+288)(76bc1ed675edcc5f429a976d6c9b955d)
   #11 pc 0000000000e179f4 /system/lib64/module/arkcompiler/stub.an(RTStub_PushCallArgsAndDispatchNative+40)
   #12 pc 000000000046b900 /system/lib64/module/arkcompiler/stub.an(BCStub_HandleCallthis0Imm8V8StwCopy+392)
   #13 at triggerBinderInterfaceBlockSync (entry|entry|1.0.0|src/main/ets/pages/page_second/page_third_appfreeze/appfreeze_threadblock.ts:147:43)
   ```

   堆栈的#13栈帧表明应用侧业务函数是triggerBinderInterfaceBlockSync，#09栈帧表明业务调用的接口是系统音频服务提供的GetAudioSceneSync。由于系统音频服务未及时响应返回，主线程阻塞在同步Binder通信上。由于对端进程是系统音频服务，不属于故障应用的业务，建议反馈给系统侧优化。若对端进程是故障应用的业务，可以按照下述步骤继续分析。
2. 查看日志中的BinderCatcher信息，根据to server\_pid:server\_tid确认对端进程的进程号和IPC线程号。

   证据2：BinderCatcher信息

   ```screen
   41777:41777 to 784:801 code 1b wait:6.446522656 s frz_state:1,  ns:-1:-1 to -1:-1, debug:41777:41777 to 784:801, active_code:0, active_thread=0, pending_async_proc=0
   ```

   BinderCatcher信息表明主线程等待对端进程响应的时间已超过6s，对端进程的进程号是784，IPC线程号是801。
3. 根据进程号找到对端进程信息，再根据IPC线程号找到IPC线程的堆栈。

   证据3：对端进程IPC线程的堆栈关键栈帧

   ```screen
   Tid:801, Name:OS_IPC_0_801
   state=S, utime=14, stime=9, priority=20, nice=0, clk=100
   #00 pc 0000000000197768 /system/lib/ld-musl-aarch64.so.1(ioctl+172)(8c2ca4e308a1de9ed1e6b4ccc14c7443)
   #01 pc 000000000000f0ac /system/lib64/platformsdk/libipc_common.z.so(OHOS::BinderConnector::WriteBinder(unsigned long, void*)+120)(21def93073c96c4161bfa61b948c2957)
   #02 pc 0000000000074934 /system/lib64/platformsdk/libipc_single.z.so(OHOS::BinderInvoker::TransactWithDriver(bool)+284)(5a12a4b7e05d71d18ea20b9f1e1aed8a)
   #03 pc 0000000000074d24 /system/lib64/platformsdk/libipc_single.z.so(OHOS::BinderInvoker::StartWorkLoop()+100)(5a12a4b7e05d71d18ea20b9f1e1aed8a)
   #04 pc 0000000000077958 /system/lib64/platformsdk/libipc_single.z.so(OHOS::BinderInvoker::JoinThread(bool)+80)(5a12a4b7e05d71d18ea20b9f1e1aed8a)
   #05 pc 000000000006c248 /system/lib64/platformsdk/libipc_single.z.so(OHOS::IPCWorkThread::ThreadHandler(void*)+1056)(5a12a4b7e05d71d18ea20b9f1e1aed8a)
   #06 pc 00000000001de740 /system/lib/ld-musl-aarch64.so.1(8c2ca4e308a1de9ed1e6b4ccc14c7443)
   #07 pc 00000000000b59ec /system/lib/ld-musl-aarch64.so.1(8c2ca4e308a1de9ed1e6b4ccc14c7443)
   ```

   IPC线程的堆栈表明服务未响应的根因也是同步Binder接口调用阻塞，则按本章节的分析思路继续分析。

**预防建议**

将同步Binder调用移至子线程，或使用异步接口。

### 对端Binder线程满

**根因描述**

应用主线程业务向系统服务或其他进程发起调用同步Binder接口，对端Binder线程耗尽，导致调用长时间未返回并处于阻塞状态。

**问题分析思路**

1. 根据堆栈找到发起IPC的应用侧业务和服务接口；
2. 根据主线程ID在Binder信息中找到对端服务进程的进程号和IPC线程号；
3. 根据对端服务进程号找到对端服务进程堆栈，再找到对应的IPC线程堆栈；
4. 按照故障模式根因的分析思路重新分析该IPC线程。

**关键字**

关注主线程堆栈共享库和符号是否匹配如下关键字。

共享库：

libipc\_common.z.so

符号：

WriteBinder

**案例分析**

**案例：系统音频服务Binder线程耗尽未及时响应导致主线程阻塞**

**问题现象**

当用户触发业务代码调用后，应用进入无响应状态，一段时间后应用退出，并生成冻屏日志文件。

**问题分析**

1. 查看AppFreeze中THREAD\_BLOCK\_3S和THREAD\_BLOCK\_6S两部分的主线程堆栈。确认一致后，分析堆栈内容。

   证据1：主线程堆栈关键栈帧

   ```screen
   Tid:17052, Name:pfreezeanalysis
   state=S, utime=203, stime=76, priority=-14, nice=-10, clk=100
   #00 pc 000000000019514c /system/lib/ld-musl-aarch64.so.1(ioctl+188)(9dcef83da65dee0250e2b6dbef45e66a)
   #01 pc 000000000000f030 /system/lib64/platformsdk/libipc_common.z.so(OHOS::BinderConnector::WriteBinder(unsigned long, void*)+120)(c3d820e943670c03802f3c6a6f6c02f7)
   #02 pc 0000000000071d64 /system/lib64/platformsdk/libipc_single.z.so(OHOS::BinderInvoker::TransactWithDriver(bool)+284)(725e65c2222991d0c1d55e2cf0cc2738)
   #03 pc 0000000000070764 /system/lib64/platformsdk/libipc_single.z.so(OHOS::BinderInvoker::WaitForCompletion(OHOS::MessageParcel*)+124)(725e65c2222991d0c1d55e2cf0cc2738)
   #04 pc 000000000006fc34 /system/lib64/platformsdk/libipc_single.z.so(OHOS::BinderInvoker::SendRequest(int, unsigned int, OHOS::MessageParcel&, OHOS::MessageParcel&, OHOS::MessageOption&)+620)(725e65c2222991d0c1d55e2cf0cc2738)
   #05 pc 0000000000048d14 /system/lib64/platformsdk/libipc_single.z.so(OHOS::IPCObjectProxy::SendRequestInner(bool, unsigned int, OHOS::MessageParcel&, OHOS::MessageParcel&, OHOS::MessageOption&)+272)(725e65c2222991d0c1d55e2cf0cc2738)
   #06 pc 000000000004972c /system/lib64/platformsdk/libipc_single.z.so(OHOS::IPCObjectProxy::SendRequest(unsigned int, OHOS::MessageParcel&, OHOS::MessageParcel&, OHOS::MessageOption&)+216)(725e65c2222991d0c1d55e2cf0cc2738)
   #07 pc 000000000003ee60 /system/lib64/libaudio_policy_client_idl_interface.z.so(OHOS::AudioStandard::AudioPolicyProxy::GetAudioScene(int&)+320)(16a5f13d157f85d0ce2574baf96e445a)
   #08 pc 00000000000896c8 /system/lib64/platformsdk/libaudio_client.z.so(OHOS::AudioStandard::AudioSystemManager::GetAudioScene() const+44)(fba17e35e3611dc6050105edd9d5bf7c)
   #09 pc 00000000000d3314 /system/lib64/module/multimedia/libaudio.z.so(OHOS::AudioStandard::NapiAudioManager::GetAudioSceneSync(napi_env__*, napi_callback_info__*) (.cfi)+228)(35129c60e8427727fa0ca4566d0f6524)
   #10 pc 0000000000066120 /system/lib64/platformsdk/libace_napi.z.so(panda::JSValueRef ArkNativeFunctionCallBack<true>(panda::JsiRuntimeCallInfo*)+288)(44ba8b408e7efd513bdc33ebeab8b671)
   #11 pc 0000000000e1537c /system/lib64/module/arkcompiler/stub.an(RTStub_PushCallArgsAndDispatchNative+40)
   #12 pc 0000000000466904 /system/lib64/module/arkcompiler/stub.an(BCStub_HandleCallthis0Imm8V8StwCopy+392)
   #13 at triggerBinderInterfaceBlockSync (entry|entry|1.0.0|src/main/ets/pages/page_second/page_third_appfreeze/appfreeze_threadblock.ts:216:43)
   ```

   堆栈的#13栈帧表明应用侧业务函数是triggerBinderInterfaceBlockSync，#09栈帧表明业务调用的接口是系统音频服务提供的GetAudioSceneSync。由于系统音频服务未及时响应返回，主线程阻塞在同步Binder通信上。由于对端进程是系统音频服务，不属于故障应用的业务，建议反馈给系统侧优化。若对端进程是故障应用的业务，可以按照下述步骤继续分析。
2. 查看日志中的BinderCatcher信息，根据to server\_pid:server\_tid确认对端进程的进程号和IPC线程号。

   证据2：BinderCatcher信息

   ```screen
   17052:17052 to 772:0 code 1b wait:6.74904063 s frz_state:1,  ns:-1:-1 to -1:-1, debug:17052:17052 to 772:0, active_code:0, active_thread=0, pending_async_proc=0
   ```

   BinderCatcher信息表明主线程等待对端进程响应的时间已超过6s，对端进程的进程号是772，IPC线程号是0，表明对端进程Binder线程耗尽，无法分配出IPC线程。
3. 根据进程号找到对端进程信息，找出对端进程所有的IPC线程的堆栈，相同堆栈聚合后确定到对应的根因，最后按对应根因的分析思路继续分析。

**预防建议**

1. 将同步Binder调用移至子线程，或使用异步接口。
2. 对端是故障应用的进程，建议增加Binder线程池大小，以及优化对端应用响应速度。

### 同步耗时I/O操作

**根因描述**

应用主线程在进行同步耗时I/O操作时被阻塞。

**问题分析思路**

1. 根据堆栈找到进行I/O操作的应用侧业务；
2. 若应用侧业务栈帧与栈顶之间存在系统侧业务，则可进一步识别出具体的I/O操作（如数据库读写）；
3. 分析hilog日志打印频率，若超过1000行每秒，建议优化日志。

**关键字**

关注主线程堆栈栈顶共享库和符号是否匹配如下关键字。

共享库：

ld-musl-aarch64.so.1

符号：

* \_\_stdio\_readx
* \_\_stdio\_write
* pread
* writev
* pread64
* pwrite64
* dlopen\_impl

**案例分析**

**案例：文件读取操作耗时导致主线程阻塞**

**问题现象**

当用户触发业务代码调用后，应用进入无响应状态，一段时间后应用退出，并生成冻屏日志文件。

**问题分析**

1. 查看AppFreeze中THREAD\_BLOCK\_3S和THREAD\_BLOCK\_6S两部分的主线程堆栈。确认一致后，分析堆栈内容。

   证据：主线程堆栈关键栈帧

   ```screen
   Tid:19502, Name:pfreezeanalysis
   state=R, utime=189, stime=635, priority=-14, nice=-10, clk=100
   #00 pc 00000000001ead94 /system/lib/ld-musl-aarch64.so.1(pread+76)(8c2ca4e308a1de9ed1e6b4ccc14c7443)
   #01 pc 00000000000121e0 /system/lib/libprocess.so(open+556)
   #02 pc 000000000001e108 /system/lib64/platformsdk/libuv.so(uv__fs_work.llvm.255697381303559595+204)(dd4ce8a088606e6444f0dceac8540868)
   #03 pc 0000000000020998 /system/lib64/platformsdk/libuv.so(uv_fs_open+176)(dd4ce8a088606e6444f0dceac8540868)
   #04 pc 0000000000109738 /system/lib64/module/file/libfs.z.so(OHOS::FileManagement::ModuleFileIO::OpenFileByPath(std::__h::basic_string<char, std::__h::char_traits<char>, std::__h::allocator<char>> const&, unsigned int)+148)(34d72fdf9d62dd4b9396c4c393f51d9f)
   #05 pc 0000000000107988 /system/lib64/module/file/libfs.z.so(OHOS::FileManagement::ModuleFileIO::Open::Sync(napi_env__*, napi_callback_info__*) (.cfi)+788)(34d72fdf9d62dd4b9396c4c393f51d9f)
   #06 pc 0000000000067c90 /system/lib64/platformsdk/libace_napi.z.so(panda::JSValueRef ArkNativeFunctionCallBack<true>(panda::JsiRuntimeCallInfo*)+288)(76bc1ed675edcc5f429a976d6c9b955d)
   #07 pc 0000000000e179f4 /system/lib64/module/arkcompiler/stub.an(RTStub_PushCallArgsAndDispatchNative+40)
   #08 pc 000000000046c00c /system/lib64/module/arkcompiler/stub.an(BCStub_HandleCallthis2Imm8V8V8V8StwCopy+432)
   #09 at write (entry|entry|1.0.0|src/main/ets/pages/page_second/page_third_appfreeze/appfreeze_threadblock_io.ts:182:31)
   #10 at anonymous (entry|entry|1.0.0|src/main/ets/pages/page_second/page_third_appfreeze/appfreeze_threadblock_io.ts:155:26)
   ```

   栈顶表明主线程阻塞在读取操作上，#09栈帧表明I/O操作的业务在write函数中。
2. 分析write函数中操作的具体文件及其大小，通常是文件过大导致主线程读写时阻塞。

**预防建议**

将耗时I/O操作移至子线程执行，避免主线程被阻塞。

### 触发长时间GC

**根因描述**

应用主线程业务触发长时间GC操作阻塞。

**问题分析思路**

1. 根据堆栈找到GC前的应用侧业务；
2. 结合代码分析业务中内存使用情况。

**关键字**

关注主线程堆栈共享库和符号是否匹配如下关键字。

共享库：

libark\_jsruntime.so

符号：

FullGC

**案例分析**

**案例：FullGC耗时导致主线程阻塞**

**问题现象**

当用户触发业务代码调用后，应用进入无响应状态，一段时间后应用退出，并生成冻屏日志文件。

**问题分析**

1. 查看AppFreeze中THREAD\_BLOCK\_3S和THREAD\_BLOCK\_6S两部分的主线程堆栈。确认一致后，分析堆栈内容。

   证据：主线程堆栈关键栈帧

   ```screen
   Tid:22887, Name:pfreezeanalysis
   state=R, utime=628, stime=55, priority=-14, nice=-10, clk=100
   #00 pc 0000000000015890 /system/lib/libprocess.so(trap_handler+1232)
   #01 pc 00000000001edecc /system/lib/ld-musl-aarch64.so.1(signal_chain_handler+864)(8c2ca4e308a1de9ed1e6b4ccc14c7443)
   #02 pc 0000000000001d30 [shmm]
   #03 pc 0000000000001480 [shmm](__kernel_rt_sigreturn+0)
   #04 pc 000000000020e9a8 /system/lib64/platformsdk/libark_jsruntime.so(panda::ecmascript::FullGCMarkRootVisitor::VisitRoot(panda::ecmascript::Root, panda::ecmascript::ObjectSlot)+548)(4025597d50430dc8ac5e5f0b44678df8)
   #05 pc 00000000008ec928 /system/lib64/platformsdk/libark_jsruntime.so(panda::ecmascript::FullGCMarkRootVisitor::VisitRangeRoot(panda::ecmascript::Root, panda::ecmascript::ObjectSlot, panda::ecmascript::ObjectSlot)+64)(4025597d50430dc8ac5e5f0b44678df8)
   #06 pc 0000000000459134 /system/lib64/platformsdk/libark_jsruntime.so(panda::ecmascript::EcmaVM::IterateSTWRoots(panda::ecmascript::RootVisitor&)+384)(4025597d50430dc8ac5e5f0b44678df8)
   #07 pc 0000000000458a6c /system/lib64/platformsdk/libark_jsruntime.so(panda::ecmascript::EcmaVM::Iterate(panda::ecmascript::RootVisitor&)+24)(4025597d50430dc8ac5e5f0b44678df8)
   #08 pc 00000000008ec000 /system/lib64/platformsdk/libark_jsruntime.so(panda::ecmascript::FullGC::Mark()+248)(4025597d50430dc8ac5e5f0b44678df8)
   #09 pc 00000000008eb750 /system/lib64/platformsdk/libark_jsruntime.so(panda::ecmascript::FullGC::RunPhases()+1660)(4025597d50430dc8ac5e5f0b44678df8)
   #10 pc 00000000001ef154 /system/lib64/platformsdk/libark_jsruntime.so(panda::ecmascript::Heap::CollectGarbageImpl(panda::ecmascript::TriggerGCType, panda::ecmascript::GCReason)+1212)(4025597d50430dc8ac5e5f0b44678df8)
   #11 pc 00000000003854b0 /system/lib64/platformsdk/libark_jsruntime.so(panda::ecmascript::Heap::CollectGarbage(panda::ecmascript::TriggerGCType, panda::ecmascript::GCReason)+136)(4025597d50430dc8ac5e5f0b44678df8)
   #12 pc 00000000003853b8 /system/lib64/platformsdk/libark_jsruntime.so(panda::ecmascript::Heap::CheckAndTriggerOldGC(unsigned long)+312)(4025597d50430dc8ac5e5f0b44678df8)
   #13 pc 00000000001eae98 /system/lib64/platformsdk/libark_jsruntime.so(panda::ecmascript::ObjectFactory::NewTaggedArray(unsigned int, panda::ecmascript::JSTaggedValue)+5012)(4025597d50430dc8ac5e5f0b44678df8)
   #14 pc 000000000026bc2c /system/lib64/platformsdk/libark_jsruntime.so(panda::ecmascript::JSObject::TryOptimizeAsFastElements(panda::ecmascript::JSThread const*, panda::ecmascript::JSHandle<panda::ecmascript::JSObject>)+168)(4025597d50430dc8ac5e5f0b44678df8)
   #15 pc 00000000004eeb9c /system/lib64/platformsdk/libark_jsruntime.so(panda::ecmascript::builtins::BuiltinsArray::Fill(panda::ecmascript::EcmaRuntimeCallInfo*)+1028)(4025597d50430dc8ac5e5f0b44678df8)
   #16 pc 0000000000e179f4 /system/lib64/module/arkcompiler/stub.an(RTStub_PushCallArgsAndDispatchNative+40)
   #17 pc 0000000000b25df8 /system/lib64/module/arkcompiler/stub.an(BuiltinStub_ArrayFillStwCopy+472)
   #18 pc 000000000046bce4 /system/lib64/module/arkcompiler/stub.an(BCStub_HandleCallthis1Imm8V8V8StwCopy+528)
   #19 at generateMemoryPressure (entry|entry|1.0.0|src/main/ets/pages/page_second/page_third_appfreeze/appfreeze_threadblock.ts:1865:56)
   ```

   关键字FullGC表明主线程阻塞在GC上，#19栈帧表明GC前的业务是generateMemoryPressure。
2. 分析generateMemoryPressure业务中的内存使用情况，通常是频繁创建大数组或复杂对象，导致内存压力升高后触发GC导致主线程阻塞。

**预防建议**

减少内存分配，优化数据结构，避免频繁GC。

### 触发长时间抓取内存快照

**根因描述**

应用主线程OOM触发长时间抓取内存快照导致阻塞。

**问题分析思路**

1. 查找本次应用冻屏问题对应的OOM日志；
2. 分析并解决OOM问题。

**关键字**

关注主线程堆栈共享库和符号是否匹配如下关键字。

共享库：

libark\_jsruntime.so

符号：

DumpHeapSnapshot

**案例分析**

**案例：OOM抓取内存快照耗时导致主线程阻塞**

**问题现象**

当用户触发业务代码调用后，应用进入无响应状态，一段时间后应用退出，并生成冻屏日志文件。

**问题分析**

1. 查看AppFreeze中THREAD\_BLOCK\_3S和THREAD\_BLOCK\_6S两部分的主线程堆栈。确认一致后，分析堆栈内容。

   证据：主线程堆栈关键栈帧

   ```screen
   Tid:12892, Name:pfreezeanalysis
   state=R, utime=648, stime=86, priority=-14, nice=-10, clk=100
   #00 pc 0000000000a45b30 /system/lib64/platformsdk/libark_jsruntime.so(4025597d50430dc8ac5e5f0b44678df8)
   #01 pc 0000000000a98880 /system/lib64/platformsdk/libark_jsruntime.so(panda::ecmascript::EntryIdMap::FindId(unsigned long)+48)(4025597d50430dc8ac5e5f0b44678df8)
   #02 pc 0000000000aaa860 /system/lib64/platformsdk/libark_jsruntime.so(panda::ecmascript::HeapSnapshot::GenerateNode(panda::ecmascript::JSTaggedValue, unsigned long, bool, bool, bool)+620)(4025597d50430dc8ac5e5f0b44678df8)
   #03 pc 0000000000aa2644 /system/lib64/platformsdk/libark_jsruntime.so(panda::ecmascript::HeapSnapshot::FillEdges(bool)+852)(4025597d50430dc8ac5e5f0b44678df8)
   #04 pc 0000000000aa2138 /system/lib64/platformsdk/libark_jsruntime.so(panda::ecmascript::HeapSnapshot::BuildUp(bool)+40)(4025597d50430dc8ac5e5f0b44678df8)
   #05 pc 0000000000a9aa30 /system/lib64/platformsdk/libark_jsruntime.so(panda::ecmascript::HeapProfiler::MakeHeapSnapshot(panda::ecmascript::HeapProfiler::SampleType, panda::ecmascript::DumpSnapShotOption const&, bool)+360)(4025597d50430dc8ac5e5f0b44678df8)
   #06 pc 0000000000a9a1c8 /system/lib64/platformsdk/libark_jsruntime.so(panda::ecmascript::HeapProfiler::DoDump(panda::ecmascript::Stream*, panda::ecmascript::Progress*, panda::ecmascript::DumpSnapShotOption const&)+100)(4025597d50430dc8ac5e5f0b44678df8)
   #07 pc 0000000000a9b630 /system/lib64/platformsdk/libark_jsruntime.so(panda::ecmascript::HeapProfiler::DumpHeapSnapshot(panda::ecmascript::Stream*, panda::ecmascript::DumpSnapShotOption const&, panda::ecmascript::Progress*, std::__h::function<void (unsigned char)>)+972)(4025597d50430dc8ac5e5f0b44678df8)
   #08 pc 0000000000a88120 /system/lib64/platformsdk/libark_jsruntime.so(panda::DFXJSNApi::DumpHeapSnapshot(panda::ecmascript::EcmaVM const*, panda::ecmascript::Stream*, panda::ecmascript::DumpSnapShotOption const&, panda::ecmascript::Progress*, std::__h::function<void (unsigned char)>)+136)(4025597d50430dc8ac5e5f0b44678df8)
   #09 pc 0000000000a87fec /system/lib64/platformsdk/libark_jsruntime.so(panda::DFXJSNApi::DumpHeapSnapshot(panda::ecmascript::EcmaVM const*, std::__h::basic_string<char, std::__h::char_traits<char>, std::__h::allocator<char>> const&, panda::ecmascript::DumpSnapShotOption const&, std::__h::function<void (unsigned char)> const&)+120)(4025597d50430dc8ac5e5f0b44678df8)
   #10 pc 000000000006d620 /system/lib64/platformsdk/libace_napi.z.so(ArkNativeEngine::DumpHeapSnapshot(std::__h::basic_string<char, std::__h::char_traits<char>, std::__h::allocator<char>> const&, bool, DumpFormat, bool, bool, bool, bool)+192)(76bc1ed675edcc5f429a976d6c9b955d)
   #11 pc 000000000000f4b4 /system/lib64/module/libhidebug.z.so(OHOS::HiviewDFX::DumpHeapSnapshot(std::__h::basic_string<char, std::__h::char_traits<char>, std::__h::allocator<char>> const&, napi_env__*, bool)+376)(91aaf2c7bd1d5fb2dfa77f48a3ffc31d)
   #12 pc 000000000000facc /system/lib64/module/libhidebug.z.so(OHOS::HiviewDFX::DumpJsHeapData(napi_env__*, napi_callback_info__*)+788)(91aaf2c7bd1d5fb2dfa77f48a3ffc31d)
   #13 pc 0000000000067c90 /system/lib64/platformsdk/libace_napi.z.so(panda::JSValueRef ArkNativeFunctionCallBack<true>(panda::JsiRuntimeCallInfo*)+288)(76bc1ed675edcc5f429a976d6c9b955d)
   #14 pc 0000000000e179f4 /system/lib64/module/arkcompiler/stub.an(RTStub_PushCallArgsAndDispatchNative+40)
   #15 pc 000000000046bc74 /system/lib64/module/arkcompiler/stub.an(BCStub_HandleCallthis1Imm8V8V8StwCopy+416)
   ```

   堆栈中DumpHeapSnapshot关键字表明应用正在生成堆快照，快照生成耗时导致主线程阻塞。
2. 此类应用冻屏问题是由于发生OOM问题后抓取内存快照耗时导致，需要分析对应的OOM问题。

**预防建议**

优化内存使用和管理，避免内存超限发生OOM。

### 执行耗时操作

**根因描述**

应用主线程执行耗时操作导致阻塞。

**问题分析思路**

1. 根据主线程堆栈找到应用侧的耗时业务；
2. 结合代码分析业务耗时原因。

**关键字**

关注主线程堆栈中的应用侧业务栈帧：

* at开头的栈帧，如下所示：

  ```screen
  #13 at triggerBinderInterfaceBlockSync (entry|entry|1.0.0|src/main/ets/pages/page_second/page_third_appfreeze/appfreeze_threadblock.ts:147:43)
  ```
* /data/storage目录下的共享库的栈帧，如下所示：

  ```screen
  #01 pc 000000000007a638 /data/storage/el1/bundle/libs/arm64/libentry.so(TriggerLongTimeOp(napi_env__*, napi_callback_info__*)+44)(f9377ecb68078186ec50cb9740a6a4c259058746)
  ```

**案例分析**

**案例：业务函数耗时导致主线程阻塞**

**问题现象**

当用户触发业务代码调用后，应用进入无响应状态，一段时间后应用退出，并生成冻屏日志文件。

**问题分析**

1. 查看AppFreeze中THREAD\_BLOCK\_3S和THREAD\_BLOCK\_6S两部分的主线程堆栈。确认一致后，分析堆栈内容。

   证据1：主线程堆栈关键栈帧

   ```screen
   Tid:23173, Name:pfreezeanalysis
   state=S, utime=61, stime=45, priority=-14, nice=-10, clk=100
   #00 pc 00000000001ebb00 /system/lib/ld-musl-aarch64.so.1(sleep+64)(8c2ca4e308a1de9ed1e6b4ccc14c7443)
   #01 pc 000000000007a638 /data/storage/el1/bundle/libs/arm64/libentry.so(TriggerLongTimeOp(napi_env__*, napi_callback_info__*)+44)(f9377ecb68078186ec50cb9740a6a4c259058746)
   #02 pc 0000000000067c90 /system/lib64/platformsdk/libace_napi.z.so(panda::JSValueRef ArkNativeFunctionCallBack<true>(panda::JsiRuntimeCallInfo*)+288)(76bc1ed675edcc5f429a976d6c9b955d)
   #03 pc 0000000000e179f4 /system/lib64/module/arkcompiler/stub.an(RTStub_PushCallArgsAndDispatchNative+40)
   #04 pc 000000000046b900 /system/lib64/module/arkcompiler/stub.an(BCStub_HandleCallthis0Imm8V8StwCopy+392)
   ```

   #01栈帧表明存在耗时操作的业务方是libentry.so(TriggerLongTimeOp)，结合代码继续分析。
2. 开发调试场景下可直接在DevEco Studio中单击libentry.so所在的栈帧跳转到对应代码行；运维场景下使用[llvm-addr2line](bpta-stability-app-crash-cpp-way.md#li186453444512)解析找到对应代码行。

   证据2：故障栈帧所在的代码

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f7/v3/ZUNEjIqkQiyNTs7FrSmlVg/zh-cn_image_0000002673575731.png "点击放大")

   TriggerLongTimeOp方法中的while循环耗时导致主线程阻塞。

**预防建议**

应用侧可以优化的方向：

1. 降低主线程负载，移动部分业务到异步线程；
2. 降低UI复杂度，使用懒加载方式加载UI，并在用户不可见后释放资源。

如果应用在后台，可能由于系统资源供给不足导致，可以忽略本次应用冻屏故障。
