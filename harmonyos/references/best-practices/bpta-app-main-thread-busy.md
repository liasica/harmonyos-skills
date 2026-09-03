---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-app-main-thread-busy
title: 应用主线程繁忙故障模式说明
breadcrumb: 最佳实践 > 稳定性 > 稳定性分析 > 稳定性故障模式说明 > 应用冻屏故障模式说明 > 应用主线程繁忙故障模式说明
category: best-practices
scraped_at: 2026-09-04T06:33:24+08:00
doc_updated_at: 2026-07-22
content_hash: sha256:2e8b67b3958edb6fe28ccefe058c0c782db3956fdaa09ca88f34748b42ae5c2a
---

## 概述

本文旨在指导HarmonyOS应用开发者如何定位主线程繁忙类型的应用冻屏（AppFreeze）问题。通过分析应用冻屏故障日志中的主线程堆栈，将主线程繁忙类型的应用冻屏问题分为以下故障根因：

* [频繁等锁](bpta-app-main-thread-busy.md#section15741142111511)
* [频繁调用Binder接口](bpta-app-main-thread-busy.md#section1249193810202)
* [频繁执行I/O操作](bpta-app-main-thread-busy.md#section711018112112)
* [频繁执行UI操作](bpta-app-main-thread-busy.md#section6164181919215)
* [频繁执行特定业务](bpta-app-main-thread-busy.md#section5769184718215)
* [执行耗时操作](bpta-app-main-thread-busy.md#section9745134227)

**说明** 

开发者可通过阅读[AppFreeze（应用冻屏）检测](../harmonyos-guides/appfreeze-guidelines.md)了解关于应用冻屏（AppFreeze）问题的检测原理和日志说明。

## 确认问题类型

对于一个应用冻屏（AppFreeze）问题，可通过AppFreeze日志和其增强日志确认是否为主线程繁忙类型：

* 通过AppFreeze日志确认

对比告警和卡死两次事件的主线程堆栈是否一致。两次事件包括：THREAD\_BLOCK\_3S和THREAD\_BLOCK\_6S、THREAD\_BLOCK\_3S和APP\_INPUT\_BLOCK、LIFECYCLE\_HALF\_TIMEOUT和LIFECYCLE\_TIMEOUT。若堆栈不一致，则表明是主线程繁忙类型。

* 通过AppFreeze日志和增强日志确认

对比AppFreeze日志中的主线程堆栈以及增强日志中的主线程采样栈是否一致，不一致则表明是主线程繁忙类型。

## 根因分类

### 频繁等锁

**根因描述**

应用主线程连续多次等锁，累计耗时长造成主线程繁忙。

**问题分析思路**

1. 对增强日志中主线程采样栈按照阻塞类别下的根因进行分析聚类；
2. 占比最高的根因是等锁；
3. 从等锁的主线程采样栈中获取应用侧业务。

**关键字**

关注增强日志主线程采样栈栈顶共享库和符号是否匹配如下关键字。

共享库：

ld-musl-aarch64.so.1

符号：

* \_\_timedwait\_cp
* pthread\_join

**案例分析**

**案例：子线程循环竞争锁资源导致主线程繁忙**

**问题现象**

当用户触发业务代码调用后，应用进入无响应状态，一段时间后应用退出，并生成冻屏日志文件。

**问题分析**

1. 查看AppFreeze中THREAD\_BLOCK\_3S和THREAD\_BLOCK\_6S两部分的主线程堆栈，确认不一致。

   证据1：主线程堆栈关键栈帧

   THREAD\_BLOCK\_3S部分

   ```screen
   Tid:58244, Name:pfreezeanalysis
   state=R, utime=597, stime=24, priority=-54, nice=-10, clk=100
   #00 pc 00000000000018a4 [shmm](__kernel_gettimeofday+68)
   #01 pc 00000000001fdfac /system/lib/ld-musl-aarch64.so.1(gettimeofday+52)(0fd6c257b7c8566c76aa08c474be61aa)
   #02 pc 0000000000240024 /system/lib64/platformsdk/libark_jsruntime.so(panda::ecmascript::JSDate::Now()+40)(a0191e40080d8d657554ee4036a515b0)
   #03 pc 0000000000e8b488 /system/lib64/module/arkcompiler/stub.an(RTStub_PushCallArgsAndDispatchNative+40)
   #04 pc 000000000047dd94 /system/lib64/module/arkcompiler/stub.an(BCStub_HandleCallthis0Imm8V8StwCopy+396)
   #05 at triggerFrequentLockWait entry (entry/src/main/ets/pages/page_second/page_third_appfreeze/appfreeze_threadblock.ets:103:15)
   ```

   THREAD\_BLOCK\_6S部分

   ```screen
   Tid:58244, Name:pfreezeanalysis
   state=S, utime=741, stime=24, priority=-54, nice=-10, clk=100
   #00 pc 00000000001f6bf8 /system/lib/ld-musl-aarch64.so.1(pthread_join+132)(0fd6c257b7c8566c76aa08c474be61aa)
   #01 pc 00000000000d3d34 /data/storage/el1/bundle/libs/arm64/libc++_shared.so(std::__n1::thread::join()+28)(d6ecfba39e9497d96d44a304084a03488c99ebb0)
   #02 pc 00000000000be8fc /data/storage/el1/bundle/libs/arm64/libentry.so(WaitThread(napi_env__*, napi_callback_info__*)+400)(6264c42063cc3206ff41b971f2f20e61257fba21)
   #03 pc 000000000005f6b8 /system/lib64/platformsdk/libace_napi.z.so(panda::JSValueRef ArkNativeFunctionCallBack<true>(panda::JsiRuntimeCallInfo*)+240)(cbac5c2cdec75704b84a9ddba0333eb9)
   #04 pc 0000000000e8b488 /system/lib64/module/arkcompiler/stub.an(RTStub_PushCallArgsAndDispatchNative+40)
   #05 pc 000000000047dd94 /system/lib64/module/arkcompiler/stub.an(BCStub_HandleCallthis0Imm8V8StwCopy+396)
   #06 at triggerFrequentLockWait entry (entry/src/main/ets/pages/page_second/page_third_appfreeze/appfreeze_threadblock.ets:110:12)
   ```

   两次主线程堆栈不一致，表明主线程没有阻塞，是处于繁忙状态。需要通过增强日志查看更多时间点的主线程堆栈切片来确认繁忙的原因。
2. 查看增强日志中的主线程采样栈。

   证据2：主线程采样栈出现次数最多的关键栈帧

   ```screen
   #00 pc 00000000001f6bf4 /system/lib/ld-musl-aarch64.so.1(pthread_join+128)(0fd6c257b7c8566c76aa08c474be61aa)
   #01 pc 00000000000d3d34 /data/storage/el1/bundle/libs/arm64/libc++_shared.so(std::__n1::thread::join()+28)(d6ecfba39e9497d96d44a304084a03488c99ebb0)
   #02 pc 00000000000be8fc /data/storage/el1/bundle/libs/arm64/libentry.so(WaitThread(napi_env__*, napi_callback_info__*)+400)(6264c42063cc3206ff41b971f2f20e61257fba21)
   #03 pc 000000000005f6b8 /system/lib64/platformsdk/libace_napi.z.so(panda::JSValueRef ArkNativeFunctionCallBack<true>(panda::JsiRuntimeCallInfo*)+240)(cbac5c2cdec75704b84a9ddba0333eb9)
   #04 pc 0000000000e8b488 /system/lib64/module/arkcompiler/stub.an(RTStub_PushCallArgsAndDispatchNative+40)
   #05 pc 000000000047dd94 /system/lib64/module/arkcompiler/stub.an(BCStub_HandleCallthis0Imm8V8StwCopy+396)
   #06 at triggerFrequentLockWait (entry|entry|1.0.0|src/main/ets/pages/page_second/page_third_appfreeze/appfreeze_threadblock.ts:97:14)
   ```

   采样栈聚合后根因主要为等锁。#02栈帧表明业务方是libentry.so(WaitThread)，结合代码继续分析等锁原因。
3. 开发调试场景下可直接在DevEco Studio中单击libentry.so所在的栈帧跳转到对应代码行；运维场景下使用[llvm-addr2line](bpta-stability-app-crash-cpp-way.md#li186453444512)解析找到对应代码行。

   证据3：故障栈帧所在的代码

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/28/v3/AwxqcxqFRcCGlSYemYu5VQ/zh-cn_image_0000002673735603.png "点击放大")

   代码中创建了多个子线程，并且子线程中循环竞争锁资源，导致主线程繁忙。

**预防建议**

缩小锁粒度，使用无锁数据结构。

### 频繁调用Binder接口

**根因描述**

应用主线程业务连续多次向系统服务或其他进程发起Binder接口调用，累计耗时长造成主线程繁忙。

**问题分析思路**

1. 对增强日志中主线程采样栈按照阻塞类别下的根因进行分析聚类；
2. 占比最高的根因是同步Binder接口调用阻塞；
3. 从Binder接口调用阻塞的主线程采样栈中获取应用侧业务。

**关键字**

关注增强日志主线程采样栈共享库和符号是否匹配如下关键字。

共享库：

libipc\_common.z.so

符号：

WriteBinder

**案例分析**

**案例：循环调用系统音频服务接口导致主线程繁忙**

**问题现象**

当用户触发业务代码调用后，应用进入无响应状态，一段时间后应用退出，并生成冻屏日志文件。

**问题分析**

1. 查看AppFreeze中THREAD\_BLOCK\_3S和THREAD\_BLOCK\_6S两部分的主线程堆栈，确认不一致。

   证据1：主线程堆栈关键栈帧

   THREAD\_BLOCK\_3S部分

   ```screen
   Tid:11480, Name:pfreezeanalysis
   state=S, utime=507, stime=48, priority=-54, nice=-10, clk=100
   #00 pc 000000000001c51c /system/lib64/libhilog_inner.so(OHOS::HiviewDFX::GetGlobalLevel() (.cfi)+92)(6354f07a703d8f245d82889f0cf8c14d)
   #01 pc 00000000000185f0 /system/lib64/libhilog_inner.so(OHOS::HiviewDFX::HiLogPrintDictArgs(HilogMsg&, unsigned int, char const*, FmtId const*, char const*, std::__va_list) (.cfi)+416)(6354f07a703d8f245d82889f0cf8c14d)
   #02 pc 0000000000003658 /system/lib64/platformsdk/libhilog.so(HiLogPrintDictNew.cfi+156)(e4cc09aac1ffa99c34fa89a22026469f)
   #03 pc 000000000012dd74 /system/lib64/platformsdk/libappexecfwk_core.z.so(OHOS::AppExecFwk::BundleMgrProxy::GetBundleNameForUid(int, std::__h::basic_string<char, std::__h::char_traits<char>, std::__h::allocator<char>>&)+752)(80db8096f4ef7d86a16204925176d700)
   #04 pc 00000000000848ac /system/lib64/platformsdk/libaudio_common.z.so(OHOS::AudioStandard::AppBundleManager::GetBundleNameFromUid(int) (.cfi)+600)(3d96f3d82968d2646a0b1ebdd75aa0b5)
   #05 pc 000000000003b698 /system/lib64/platformsdk/libaudio_policy_manager.z.so(OHOS::AudioStandard::AudioSystemClientPolicyManager::GetAudioScene() const+72)(1c4bbc1b1972c3dc93180d60180cacc3)
   #06 pc 00000000000fc598 /system/lib64/module/multimedia/libaudio.z.so(OHOS::AudioStandard::NapiAudioManager::GetAudioSceneSync(napi_env__*, napi_callback_info__*) (.cfi)+160)(afd152a27fc802f4dc979e8a5d253f7d)
   #07 pc 000000000004f9b0 /system/lib64/platformsdk/libace_napi.z.so(panda::JSValueRef ArkNativeFunctionCallBack<true>(panda::JsiRuntimeCallInfo*)+288)(2bd324bcfae36fa9497b62ed308cf824)
   #08 pc 0000000000e949e8 /system/lib64/module/arkcompiler/stub.an(RTStub_PushCallArgsAndDispatchNative+40)
   #09 pc 00000000005a4658 /system/lib64/module/arkcompiler/stub.an(BCStub_HandleCallthis0withnameImm8Id16V8StwCopy+400)
   #10 at triggerFrequentBinderCalls (entry|entry|1.0.0|src/main/ets/pages/page_second/page_third_appfreeze/appfreeze_threadblock.ts:65:47)
   ```

   THREAD\_BLOCK\_6S部分

   ```screen
   Tid:11480, Name:pfreezeanalysis
   state=S, utime=570, stime=127, priority=-54, nice=-10, clk=100
   #00 pc 000000000019c674 /system/lib/ld-musl-aarch64.so.1(ioctl+184)(58b5bc0b32f5d8462c0e616fbc5ee53a)
   #01 pc 00000000000102e8 /system/lib64/platformsdk/libipc_common.z.so(OHOS::BinderConnector::WriteBinder(unsigned long, void*)+108)(79d15a46e94dbb151b338b9b4d955e09)
   #02 pc 00000000000779e0 /system/lib64/platformsdk/libipc_single.z.so(OHOS::BinderInvoker::TransactWithDriver(bool)+284)(fd75264c3da5d3ad49399e757c1fcd72)
   #03 pc 00000000000762ec /system/lib64/platformsdk/libipc_single.z.so(OHOS::BinderInvoker::WaitForCompletion(OHOS::MessageParcel*)+124)(fd75264c3da5d3ad49399e757c1fcd72)
   #04 pc 000000000007587c /system/lib64/platformsdk/libipc_single.z.so(OHOS::BinderInvoker::SendRequest(int, unsigned int, OHOS::MessageParcel&, OHOS::MessageParcel&, OHOS::MessageOption&)+612)(fd75264c3da5d3ad49399e757c1fcd72)
   #05 pc 000000000004cae4 /system/lib64/platformsdk/libipc_single.z.so(OHOS::IPCObjectProxy::SendRequestInner(bool, unsigned int, OHOS::MessageParcel&, OHOS::MessageParcel&, OHOS::MessageOption&)+148)(fd75264c3da5d3ad49399e757c1fcd72)
   #06 pc 000000000004d4a0 /system/lib64/platformsdk/libipc_single.z.so(OHOS::IPCObjectProxy::SendRequest(unsigned int, OHOS::MessageParcel&, OHOS::MessageParcel&, OHOS::MessageOption&)+216)(fd75264c3da5d3ad49399e757c1fcd72)
   #07 pc 00000000000b8cc0 /system/lib64/libaudio_framework_interface.z.so(OHOS::AudioStandard::AudioPolicyProxy::GetAudioScene(int&)+320)(541767ac76398d730304e9d891eb9543)
   #08 pc 000000000003b67c /system/lib64/platformsdk/libaudio_policy_manager.z.so(OHOS::AudioStandard::AudioSystemClientPolicyManager::GetAudioScene() const+44)(1c4bbc1b1972c3dc93180d60180cacc3)
   #09 pc 00000000000fc598 /system/lib64/module/multimedia/libaudio.z.so(OHOS::AudioStandard::NapiAudioManager::GetAudioSceneSync(napi_env__*, napi_callback_info__*) (.cfi)+160)(afd152a27fc802f4dc979e8a5d253f7d)
   #10 pc 000000000004f9b0 /system/lib64/platformsdk/libace_napi.z.so(panda::JSValueRef ArkNativeFunctionCallBack<true>(panda::JsiRuntimeCallInfo*)+288)(2bd324bcfae36fa9497b62ed308cf824)
   #11 pc 0000000000e949e8 /system/lib64/module/arkcompiler/stub.an(RTStub_PushCallArgsAndDispatchNative+40)
   #12 pc 00000000005a4658 /system/lib64/module/arkcompiler/stub.an(BCStub_HandleCallthis0withnameImm8Id16V8StwCopy+400)
   #13 at triggerFrequentBinderCalls (entry|entry|1.0.0|src/main/ets/pages/page_second/page_third_appfreeze/appfreeze_threadblock.ts:65:47)
   ```

   两次主线程堆栈不一致，表明主线程没有阻塞，是处于繁忙状态。需要通过增强日志查看更多时间点的主线程堆栈切片来确认繁忙的原因。
2. 查看增强日志中的主线程采样栈。

   证据2：主线程采样栈出现次数最多的关键栈帧

   ```screen
   #00 pc 000000000019c674 /system/lib/ld-musl-aarch64.so.1(ioctl+184)(58b5bc0b32f5d8462c0e616fbc5ee53a)
   #01 pc 00000000000102e8 /system/lib64/platformsdk/libipc_common.z.so(OHOS::BinderConnector::WriteBinder(unsigned long, void*)+108)(79d15a46e94dbb151b338b9b4d955e09)
   #02 pc 00000000000779e0 /system/lib64/platformsdk/libipc_single.z.so(OHOS::BinderInvoker::TransactWithDriver(bool)+284)(fd75264c3da5d3ad49399e757c1fcd72)
   #03 pc 00000000000762ec /system/lib64/platformsdk/libipc_single.z.so(OHOS::BinderInvoker::WaitForCompletion(OHOS::MessageParcel*)+124)(fd75264c3da5d3ad49399e757c1fcd72)
   #04 pc 000000000007587c /system/lib64/platformsdk/libipc_single.z.so(OHOS::BinderInvoker::SendRequest(int, unsigned int, OHOS::MessageParcel&, OHOS::MessageParcel&, OHOS::MessageOption&)+612)(fd75264c3da5d3ad49399e757c1fcd72)
   #05 pc 000000000004cae4 /system/lib64/platformsdk/libipc_single.z.so(OHOS::IPCObjectProxy::SendRequestInner(bool, unsigned int, OHOS::MessageParcel&, OHOS::MessageParcel&, OHOS::MessageOption&)+148)(fd75264c3da5d3ad49399e757c1fcd72)
   #06 pc 000000000004d4a0 /system/lib64/platformsdk/libipc_single.z.so(OHOS::IPCObjectProxy::SendRequest(unsigned int, OHOS::MessageParcel&, OHOS::MessageParcel&, OHOS::MessageOption&)+216)(fd75264c3da5d3ad49399e757c1fcd72)
   #07 pc 0000000000158dec /system/lib64/platformsdk/libappexecfwk_core.z.so(OHOS::AppExecFwk::BundleMgrProxy::SendTransactCmd(OHOS::AppExecFwk::BundleMgrInterfaceCode, OHOS::MessageParcel&, OHOS::MessageParcel&)+168)(80db8096f4ef7d86a16204925176d700)
   #08 pc 000000000012dc04 /system/lib64/platformsdk/libappexecfwk_core.z.so(OHOS::AppExecFwk::BundleMgrProxy::GetBundleNameForUid(int, std::__h::basic_string<char, std::__h::char_traits<char>, std::__h::allocator<char>>&)+384)(80db8096f4ef7d86a16204925176d700)
   #09 pc 00000000000848ac /system/lib64/platformsdk/libaudio_common.z.so(3d96f3d82968d2646a0b1ebdd75aa0b5)
   #10 pc 000000000003b698 /system/lib64/platformsdk/libaudio_policy_manager.z.so(OHOS::AudioStandard::AudioSystemClientPolicyManager::GetAudioScene() const+72)(1c4bbc1b1972c3dc93180d60180cacc3)
   #11 pc 00000000000fc598 /system/lib64/module/multimedia/libaudio.z.so(afd152a27fc802f4dc979e8a5d253f7d)
   #12 pc 000000000004f9b0 /system/lib64/platformsdk/libace_napi.z.so(panda::JSValueRef ArkNativeFunctionCallBack<true>(panda::JsiRuntimeCallInfo*)+288)(2bd324bcfae36fa9497b62ed308cf824)
   #13 pc 0000000000e949e8 /system/lib64/module/arkcompiler/stub.an(RTStub_PushCallArgsAndDispatchNative+40)
   #14 pc 00000000005a4658 /system/lib64/module/arkcompiler/stub.an(BCStub_HandleCallthis0withnameImm8Id16V8StwCopy+400)
   #15 at triggerFrequentBinderCalls (entry|entry|1.0.0|src/main/ets/pages/page_second/page_third_appfreeze/appfreeze_threadblock.ts:65:47)
   ```

   堆栈表明主线程耗时最多的业务是调用Binder接口。#15栈帧表明应用侧业务是triggerFrequentBinderCalls，结合代码进一步分析。
3. 查看triggerFrequentBinderCalls的代码。

   证据3：故障栈帧所在的代码

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/10/v3/xNGFnDnyTnOIBZdaEcDmWA/zh-cn_image_0000002643575820.png "点击放大")

   业务中循环调用系统音频服务接口导致主线程繁忙。

**预防建议**

优化Binder调用频率，考虑批量处理或缓存结果。

### 频繁执行I/O操作

**根因描述**

应用主线程业务连续多次进行同步I/O操作，累计耗时长造成主线程繁忙。

**问题分析思路**

1. 对增强日志中主线程采样栈按照阻塞类别下的根因进行分析聚类；
2. 占比最高的根因是进行阻塞I/O操作；
3. 从进行阻塞I/O操作的主线程采样栈中获取应用侧业务。

**关键字**

关注增强日志主线程采样栈栈顶共享库和符号是否匹配如下关键字。

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

**案例：频繁写入文件导致主线程繁忙**

**问题现象**

当用户触发业务代码调用后，应用进入无响应状态，一段时间后应用退出，并生成冻屏日志文件。

**问题分析**

1. 查看AppFreeze中THREAD\_BLOCK\_3S和THREAD\_BLOCK\_6S两部分的主线程堆栈，确认不一致。

   证据1：主线程堆栈关键栈帧

   THREAD\_BLOCK\_3S部分

   ```screen
   Tid:45449, Name:pfreezeanalysis
   state=R, utime=419, stime=23, priority=-54, nice=-10, clk=100
   #00 pc 0000000000623aec /system/lib64/platformsdk/libark_jsruntime.so(panda::ecmascript::JSThread::Iterate(panda::ecmascript::RootVisitor&, panda::ecmascript::GlobalVisitType)+524)(528445894c7c84ccb26a5e5f1d8f925b)
   #01 pc 00000000006d4c84 /system/lib64/platformsdk/libark_jsruntime.so(panda::ecmascript::Marker::MarkRoots(panda::ecmascript::RootVisitor&, panda::ecmascript::GlobalVisitType)+128)(528445894c7c84ccb26a5e5f1d8f925b)
   #02 pc 0000000000668380 /system/lib64/platformsdk/libark_jsruntime.so(panda::ecmascript::ConcurrentMarker::InitializeMarking()+280)(528445894c7c84ccb26a5e5f1d8f925b)
   #03 pc 0000000000667ef8 /system/lib64/platformsdk/libark_jsruntime.so(panda::ecmascript::ConcurrentMarker::Mark()+1840)(528445894c7c84ccb26a5e5f1d8f925b)
   #04 pc 000000000068c1fc /system/lib64/platformsdk/libark_jsruntime.so(panda::ecmascript::Heap::TryTriggerConcurrentMarking(panda::ecmascript::MarkReason)+1020)(528445894c7c84ccb26a5e5f1d8f925b)
   #05 pc 000000000069657c /system/lib64/platformsdk/libark_jsruntime.so(panda::ecmascript::LinearSpace::Allocate(unsigned long, bool)+176)(528445894c7c84ccb26a5e5f1d8f925b)
   #06 pc 000000000080b078 /system/lib64/platformsdk/libark_jsruntime.so(panda::ecmascript::ObjectFactory::NewTaggedArray(unsigned int, panda::ecmascript::JSTaggedValue)+800)(528445894c7c84ccb26a5e5f1d8f925b)
   #07 pc 00000000005019d0 /system/lib64/platformsdk/libark_jsruntime.so(panda::ecmascript::RuntimeStubs::RuntimeGetCallSpreadArgs(panda::ecmascript::JSThread*, panda::ecmascript::JSHandle<panda::ecmascript::JSTaggedValue> const&)+92)(528445894c7c84ccb26a5e5f1d8f925b)
   #08 pc 00000000008f9ea4 /system/lib64/platformsdk/libark_jsruntime.so(panda::ecmascript::RuntimeStubs::CallSpread(unsigned long, unsigned int, unsigned long)+344)(528445894c7c84ccb26a5e5f1d8f925b)
   #09 pc 0000000000e92148 /system/lib64/module/arkcompiler/stub.an(RTStub_CallRuntime+40)
   #10 pc 000000000054b190 /system/lib64/module/arkcompiler/stub.an(BCStub_HandleApplyImm8V8V8StwCopy+72)
   #11 at anonymous (/usr1/hmos_for_system/src/increment/sourcecode/out/generic_generic_arm_64only/general_all_phone_standard_2d/obj/commonlibrary/ets_utils/js_api_module/buffer/js_buffer.js:253:1)
   #12 at triggerHighFrequentIO (entry|entry|1.0.0|src/main/ets/pages/page_second/page_third_appfreeze/appfreeze_threadblock.ts:21:17)
   ```

   THREAD\_BLOCK\_6S部分

   ```screen
   Tid:45449, Name:pfreezeanalysis
   state=R, utime=677, stime=57, priority=-54, nice=-10, clk=100
   #00 pc 00000000001f474c /system/lib/ld-musl-aarch64.so.1(write+64)(58b5bc0b32f5d8462c0e616fbc5ee53a)
   #01 pc 000000000001c408 /system/lib64/platformsdk/libuv.so(uv__fs_work+2564)(5c9b6391b25c71005320ce5b0e68e238)
   #02 pc 000000000001ec1c /system/lib64/platformsdk/libuv.so(uv_fs_write+300)(5c9b6391b25c71005320ce5b0e68e238)
   #03 pc 0000000000160e2c /system/lib64/module/file/libfs.z.so(OHOS::FileManagement::ModuleFileIO::PropNExporter::WriteSync(napi_env__*, napi_callback_info__*) (.cfi)+896)(e3a582b785def20ae95665a025945421)
   #04 pc 000000000004f9b0 /system/lib64/platformsdk/libace_napi.z.so(panda::JSValueRef ArkNativeFunctionCallBack<true>(panda::JsiRuntimeCallInfo*)+288)(2bd324bcfae36fa9497b62ed308cf824)
   #05 pc 0000000000e949e8 /system/lib64/module/arkcompiler/stub.an(RTStub_PushCallArgsAndDispatchNative+40)
   #06 pc 00000000005a4e24 /system/lib64/module/arkcompiler/stub.an(BCStub_HandleCallthis2withnameImm8Id16V8V8V8StwCopy+440)
   #07 at highFrequencyIO5 (entry|entry|1.0.0|src/main/ets/pages/page_second/page_third_appfreeze/appfreeze_threadblock.ts:47:8)
   #08 at triggerHighFrequentIO (entry|entry|1.0.0|src/main/ets/pages/page_second/page_third_appfreeze/appfreeze_threadblock.ts:25:9)
   ```

   两次主线程堆栈不一致，表明主线程没有阻塞，是处于繁忙状态。需要通过增强日志查看更多时间点的主线程堆栈切片来确认繁忙的原因。
2. 查看增强日志中的主线程采样栈。

   证据2：主线程采样栈出现次数最多的关键栈帧

   ```screen
   #00 pc 00000000001f474c /system/lib/ld-musl-aarch64.so.1(write+64)(58b5bc0b32f5d8462c0e616fbc5ee53a)
   #01 pc 000000000001c408 /system/lib64/platformsdk/libuv.so(uv__fs_work+2564)(5c9b6391b25c71005320ce5b0e68e238)
   #02 pc 000000000001ec1c /system/lib64/platformsdk/libuv.so(uv_fs_write+300)(5c9b6391b25c71005320ce5b0e68e238)
   #03 pc 0000000000160e2c /system/lib64/module/file/libfs.z.so(OHOS::FileManagement::ModuleFileIO::PropNExporter::WriteSync(napi_env__*, napi_callback_info__*) (.cfi)+896)(e3a582b785def20ae95665a025945421)
   #04 pc 000000000004f9b0 /system/lib64/platformsdk/libace_napi.z.so(panda::JSValueRef ArkNativeFunctionCallBack<true>(panda::JsiRuntimeCallInfo*)+288)(2bd324bcfae36fa9497b62ed308cf824)
   #05 pc 0000000000e949e8 /system/lib64/module/arkcompiler/stub.an(RTStub_PushCallArgsAndDispatchNative+40)
   #06 pc 00000000005a4e24 /system/lib64/module/arkcompiler/stub.an(BCStub_HandleCallthis2withnameImm8Id16V8V8V8StwCopy+440)
   #07 at highFrequencyIO5 (entry|entry|1.0.0|src/main/ets/pages/page_second/page_third_appfreeze/appfreeze_threadblock.ts:47:8)
   #08 at triggerHighFrequentIO (entry|entry|1.0.0|src/main/ets/pages/page_second/page_third_appfreeze/appfreeze_threadblock.ts:25:9)
   ```

   堆栈表明主线程耗时最多的业务是I/O操作。#08栈帧表明应用侧业务是triggerHighFrequentIO，结合代码进一步分析。
3. 查看triggerHighFrequentIO的代码。

   证据3：故障栈帧所在的代码

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/wlvLg8yJRZ6S1mdn58mYRA/zh-cn_image_0000002643415866.png "点击放大")

   业务中循环进行文件读写操作导致主线程繁忙。

**预防建议**

优化I/O读写策略，使用TaskPool或者Worker进行异步I/O操作。

### 频繁执行UI操作

**根因描述**

应用主线程UI渲染负载过重，累计耗时长造成主线程繁忙。

**问题分析思路**

1. 对增强日志中主线程采样栈进行分析聚类；
2. 主线程采样栈聚类后的根因中占比最高的是在进行UI组件操作；
3. 从进行UI组件操作的主线程采样栈中获取应用侧业务。

**关键字**

关注增强日志主线程采样栈共享库是否匹配如下关键字：

libace\_compatible.z.so

**案例分析**

**案例：频繁刷新文本组件导致主线程繁忙**

**问题现象**

当用户触发业务代码调用后，应用进入无响应状态，一段时间后应用退出，并生成冻屏日志文件。

**问题分析**

1. 查看AppFreeze中THREAD\_BLOCK\_3S和THREAD\_BLOCK\_6S两部分的主线程堆栈，确认不一致。

   证据1：主线程堆栈关键栈帧

   THREAD\_BLOCK\_3S部分

   ```screen
   Tid:62838, Name:pfreezeanalysis
   state=R, utime=802, stime=42, priority=-54, nice=-10, clk=100
   #00 pc 00000000000df550 /system/lib/ld-musl-aarch64.so.1(arena_slab_reg_alloc_batch+316)(58b5bc0b32f5d8462c0e616fbc5ee53a)
   #01 pc 00000000000df018 /system/lib/ld-musl-aarch64.so.1(arena_cache_bin_fill_small+504)(58b5bc0b32f5d8462c0e616fbc5ee53a)
   #02 pc 00000000001042d4 /system/lib/ld-musl-aarch64.so.1(je_tcache_alloc_small_hard+268)(58b5bc0b32f5d8462c0e616fbc5ee53a)
   #03 pc 00000000000bab40 /system/lib/ld-musl-aarch64.so.1(malloc_default+4644)(58b5bc0b32f5d8462c0e616fbc5ee53a)
   #04 pc 00000000000bbf98 /system/lib/ld-musl-aarch64.so.1(je_malloc+676)(58b5bc0b32f5d8462c0e616fbc5ee53a)
   #05 pc 00000000000b0050 /system/lib64/chipset-sdk-sp/libc++.so(operator new(unsigned long)+24)(df2393506d17d97a741820dba41a227fe61b1f00)
   #06 pc 0000000001340f08 /system/lib64/platformsdk/libace_compatible.z.so(OHOS::Ace::RefPtr<OHOS::Ace::NG::TextEventHub> OHOS::Ace::Referenced::MakeRefPtr<OHOS::Ace::NG::TextEventHub>()+32)(37cb86795b559fcddf104355c179fdbc)
   #07 pc 00000000009d40a8 /system/lib64/platformsdk/libace_compatible.z.so(OHOS::Ace::NG::FrameNode::CreateEventHubInner()+740)(37cb86795b559fcddf104355c179fdbc)
   #08 pc 0000000000d86e48 /system/lib64/platformsdk/libace_compatible.z.so(OHOS::Ace::NG::TextModelNG::Create(std::__h::basic_string<char16_t, std::__h::char_traits<char16_t>, std::__h::allocator<char16_t>> const&)+928)(37cb86795b559fcddf104355c179fdbc)
   #09 pc 0000000000d8565c /system/lib64/platformsdk/libace_compatible.z.so(OHOS::Ace::Framework::JSText::Create(OHOS::Ace::Framework::JsiCallbackInfo const&)+564)(37cb86795b559fcddf104355c179fdbc)
   #10 pc 0000000003859888 /system/lib64/platformsdk/libace_compatible.z.so(OHOS::Ace::Framework::JsiClass<OHOS::Ace::Framework::JSText>::JSStaticMethodCallback(panda::JsiRuntimeCallInfo*)+216)(37cb86795b559fcddf104355c179fdbc)
   #11 pc 00000000007a0234 /system/lib64/platformsdk/libark_jsruntime.so(panda::Callback::RegisterCallback(panda::ecmascript::EcmaRuntimeCallInfo*)+336)(528445894c7c84ccb26a5e5f1d8f925b)
   #12 pc 0000000000e949e8 /system/lib64/module/arkcompiler/stub.an(RTStub_PushCallArgsAndDispatchNative+40)
   #13 pc 00000000005a4a2c /system/lib64/module/arkcompiler/stub.an(BCStub_HandleCallthis1withnameImm8Id16V8V8StwCopy+424)
   #14 at anonymous (entry|entry|1.0.0|src/main/ets/pages/page_second/page_third_appfreeze/appfreeze_threadblock.ts:272:26)
   ```

   THREAD\_BLOCK\_6S部分

   ```screen
   Tid:62838, Name:pfreezeanalysis
   state=R, utime=1024, stime=102, priority=-54, nice=-10, clk=100
   #00 pc 0000000000adee1c /system/lib64/platformsdk/libace_compatible.z.so(OHOS::Ace::NG::TextPattern::RecoverCopyOption()+212)(37cb86795b559fcddf104355c179fdbc)
   #01 pc 000000000285acd4 /system/lib64/platformsdk/libace_compatible.z.so(OHOS::Ace::NG::TextPattern::OnModifyDone()+1012)(37cb86795b559fcddf104355c179fdbc)
   #02 pc 0000000000aaafd4 /system/lib64/platformsdk/libace_compatible.z.so(OHOS::Ace::NG::FrameNode::MarkModifyDone()+224)(37cb86795b559fcddf104355c179fdbc)
   #03 pc 0000000001346ad8 /system/lib64/platformsdk/libace_compatible.z.so(OHOS::Ace::NG::IfElseModelNG::Pop()+1360)(37cb86795b559fcddf104355c179fdbc)
   #04 pc 000000000368d17c /system/lib64/platformsdk/libace_compatible.z.so(panda::Local<panda::JSValueRef> OHOS::Ace::Framework::JsiClass<OHOS::Ace::Framework::JSContainerBase>::StaticMethodCallback<void>(panda::JsiRuntimeCallInfo*)+1048)(37cb86795b559fcddf104355c179fdbc)
   #05 pc 00000000007a0234 /system/lib64/platformsdk/libark_jsruntime.so(panda::Callback::RegisterCallback(panda::ecmascript::EcmaRuntimeCallInfo*)+336)(528445894c7c84ccb26a5e5f1d8f925b)
   #06 pc 0000000000e949e8 /system/lib64/module/arkcompiler/stub.an(RTStub_PushCallArgsAndDispatchNative+40)
   #07 pc 00000000005a4658 /system/lib64/module/arkcompiler/stub.an(BCStub_HandleCallthis0withnameImm8Id16V8StwCopy+400)
   #08 at l199 (entry|entry|1.0.0|src/main/ets/pages/page_second/page_third_appfreeze/appfreeze_threadblock.ts:274:22)
   #09 at anonymous (/usr1/hmos_for_system/src/increment/sourcecode/out/generic_generic_arm_64only/general_all_phone_standard_2d/obj/foundation/arkui/ace_engine/frameworks/bridge/declarative_frontend/stateMgmt.js:6203:1)
   #10 pc 0000000000b726f4 /system/lib64/module/arkcompiler/stub.an(BuiltinStub_ArrayForEachStwCopy+788)
   #11 pc 0000000000486190 /system/lib64/module/arkcompiler/stub.an(BCStub_HandleCallthis1Imm8V8V8StwCopy+532)
   #12 at forEachUpdateFunction (/usr1/hmos_for_system/src/increment/sourcecode/out/generic_generic_arm_64only/general_all_phone_standard_2d/obj/foundation/arkui/ace_engine/frameworks/bridge/declarative_frontend/stateMgmt.js:6200:1)
   #13 at anonymous (entry|entry|1.0.0|src/main/ets/pages/page_second/page_third_appfreeze/appfreeze_threadblock.ts:276:18)
   ```

   两次主线程堆栈不一致，表明主线程没有阻塞，是处于繁忙状态。需要通过增强日志查看更多时间点的主线程堆栈切片来确认繁忙的原因。
2. 查看增强日志中的主线程采样栈。

   证据2：主线程采样栈出现次数最多的关键栈帧

   ```screen
   #00 pc 0000000000adee1c /system/lib64/platformsdk/libace_compatible.z.so(OHOS::Ace::NG::TextPattern::RecoverCopyOption()+212)(37cb86795b559fcddf104355c179fdbc)
   #01 pc 000000000285acd4 /system/lib64/platformsdk/libace_compatible.z.so(OHOS::Ace::NG::TextPattern::OnModifyDone()+1012)(37cb86795b559fcddf104355c179fdbc)
   #02 pc 0000000000aaafd4 /system/lib64/platformsdk/libace_compatible.z.so(OHOS::Ace::NG::FrameNode::MarkModifyDone()+224)(37cb86795b559fcddf104355c179fdbc)
   #03 pc 0000000001346ad8 /system/lib64/platformsdk/libace_compatible.z.so(OHOS::Ace::NG::IfElseModelNG::Pop()+1360)(37cb86795b559fcddf104355c179fdbc)
   #04 pc 000000000368d17c /system/lib64/platformsdk/libace_compatible.z.so(panda::Local<panda::JSValueRef> OHOS::Ace::Framework::JsiClass<OHOS::Ace::Framework::JSContainerBase>::StaticMethodCallback<void>(panda::JsiRuntimeCallInfo*)+1048)(37cb86795b559fcddf104355c179fdbc)
   #05 pc 00000000007a0234 /system/lib64/platformsdk/libark_jsruntime.so(panda::Callback::RegisterCallback(panda::ecmascript::EcmaRuntimeCallInfo*)+336)(528445894c7c84ccb26a5e5f1d8f925b)
   #06 pc 0000000000e949e8 /system/lib64/module/arkcompiler/stub.an(RTStub_PushCallArgsAndDispatchNative+40)
   #07 pc 00000000005a4658 /system/lib64/module/arkcompiler/stub.an(BCStub_HandleCallthis0withnameImm8Id16V8StwCopy+400)
   #08 at l199 (entry|entry|1.0.0|src/main/ets/pages/page_second/page_third_appfreeze/appfreeze_threadblock.ts:274:22)
   #09 at anonymous (/usr1/hmos_for_system/src/increment/sourcecode/out/generic_generic_arm_64only/general_all_phone_standard_2d/obj/foundation/arkui/ace_engine/frameworks/bridge/declarative_frontend/stateMgmt.js:6203:1)
   #10 pc 0000000000b726f4 /system/lib64/module/arkcompiler/stub.an(BuiltinStub_ArrayForEachStwCopy+788)
   #11 pc 0000000000486190 /system/lib64/module/arkcompiler/stub.an(BCStub_HandleCallthis1Imm8V8V8StwCopy+532)
   #12 at forEachUpdateFunction (/usr1/hmos_for_system/src/increment/sourcecode/out/generic_generic_arm_64only/general_all_phone_standard_2d/obj/foundation/arkui/ace_engine/frameworks/bridge/declarative_frontend/stateMgmt.js:6200:1)
   #13 at anonymous (entry|entry|1.0.0|src/main/ets/pages/page_second/page_third_appfreeze/appfreeze_threadblock.ts:276:18)
   ```

   堆栈表明主线程耗时最多的业务是刷新UI组件。结合代码进一步分析。
3. 查看UI操作业务代码。

   证据3：故障栈帧关联的代码

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/34/v3/Ep218iRfRpSWE8qVIbvnGA/zh-cn_image_0000002673575733.png "点击放大")

   业务中循环刷新Text组件导致主线程繁忙。

**预防建议**

简化UI渲染逻辑，减少过度绘制，使用虚拟化列表。

### 频繁执行特定业务

**根因描述**

应用主线程连续多次进行某项业务，累计耗时长造成主线程繁忙。

**问题分析思路**

1. 对增强日志中主线程采样栈进行分析聚类；
2. 从占比最高的主线程采样栈中获取应用侧业务。

**关键字**

关注增强日志主线程采样栈中的应用侧业务栈帧：

* at开头的栈帧，如下所示：

  ```screen
  #13 at triggerBinderInterfaceBlockSync (entry|entry|1.0.0|src/main/ets/pages/page_second/page_third_appfreeze/appfreeze_threadblock.ts:147:43)
  ```
* /data/storage目录下的共享库的栈帧，如下所示：

  ```screen
  #01 pc 000000000007a638 /data/storage/el1/bundle/libs/arm64/libentry.so(TriggerLongTimeOp(napi_env__*, napi_callback_info__*)+44)(f9377ecb68078186ec50cb9740a6a4c259058746)
  ```

**案例分析**

**案例：循环处理计算任务导致主线程繁忙**

**问题现象**

当用户触发业务代码调用后，应用进入无响应状态，一段时间后应用退出，并生成冻屏日志文件。

**问题分析**

1. 查看AppFreeze中THREAD\_BLOCK\_3S和THREAD\_BLOCK\_6S两部分的主线程堆栈，确认不一致。

   证据1：主线程堆栈关键栈帧

   THREAD\_BLOCK\_3S部分

   ```screen
   Tid:13354, Name:pfreezeanalysis
   state=R, utime=751, stime=23, priority=-54, nice=-10, clk=100
   #00 pc 00000000000b6e88 /system/lib/ld-musl-aarch64.so.1(sin+12)(0fd6c257b7c8566c76aa08c474be61aa)
   #01 pc 00000000001e4114 /data/storage/el1/bundle/libs/arm64/libentry.so(e57aefaa6cf62773d5dccf7a4e2f403def474600)
   #02 pc 00000000001e4678 /data/storage/el1/bundle/libs/arm64/libentry.so(TriggerBusinessBusySync(napi_env__*, napi_callback_info__*)+140)(e57aefaa6cf62773d5dccf7a4e2f403def474600)
   #03 pc 000000000005f6b8 /system/lib64/platformsdk/libace_napi.z.so(panda::JSValueRef ArkNativeFunctionCallBack<true>(panda::JsiRuntimeCallInfo*)+240)(cbac5c2cdec75704b84a9ddba0333eb9)
   #04 pc 0000000000e8b488 /system/lib64/module/arkcompiler/stub.an(RTStub_PushCallArgsAndDispatchNative+40)
   #05 pc 000000000047dd94 /system/lib64/module/arkcompiler/stub.an(BCStub_HandleCallthis0Imm8V8StwCopy+396)
   #06 at anonymous entry (entry/src/main/ets/pages/page_second/page_third_appfreeze/appfreeze_threadblock.ets:810:19)
   ```

   THREAD\_BLOCK\_6S部分

   ```screen
   Tid:13354, Name:pfreezeanalysis
   state=R, utime=942, stime=23, priority=-54, nice=-10, clk=100
   #00 pc 0000000000199a00 /system/lib/ld-musl-aarch64.so.1(__rem_pio2_large+0)(0fd6c257b7c8566c76aa08c474be61aa)
   #01 pc 0000000000199938 /system/lib/ld-musl-aarch64.so.1(__rem_pio2+788)(0fd6c257b7c8566c76aa08c474be61aa)
   #02 pc 00000000000b6f3c /system/lib/ld-musl-aarch64.so.1(sin+192)(0fd6c257b7c8566c76aa08c474be61aa)
   #03 pc 00000000001e4114 /data/storage/el1/bundle/libs/arm64/libentry.so(e57aefaa6cf62773d5dccf7a4e2f403def474600)
   #04 pc 00000000001e4678 /data/storage/el1/bundle/libs/arm64/libentry.so(TriggerBusinessBusySync(napi_env__*, napi_callback_info__*)+140)(e57aefaa6cf62773d5dccf7a4e2f403def474600)
   #05 pc 000000000005f6b8 /system/lib64/platformsdk/libace_napi.z.so(panda::JSValueRef ArkNativeFunctionCallBack<true>(panda::JsiRuntimeCallInfo*)+240)(cbac5c2cdec75704b84a9ddba0333eb9)
   #06 pc 0000000000e8b488 /system/lib64/module/arkcompiler/stub.an(RTStub_PushCallArgsAndDispatchNative+40)
   #07 pc 000000000047dd94 /system/lib64/module/arkcompiler/stub.an(BCStub_HandleCallthis0Imm8V8StwCopy+396)
   #08 at anonymous entry (entry/src/main/ets/pages/page_second/page_third_appfreeze/appfreeze_threadblock.ets:810:19)
   ```

   两次主线程堆栈不一致，表明主线程没有阻塞，是处于繁忙状态。需要通过增强日志查看更多时间点的主线程堆栈切片来确认繁忙的原因。
2. 查看增强日志中的主线程采样栈。

   证据2：主线程采样栈出现次数最多的关键栈帧

   ```screen
   #02 pc 00000000001e46c0 /data/storage/el1/bundle/libs/arm64/libentry.so(TriggerBusinessBusySync(napi_env__*, napi_callback_info__*)+212)(e57aefaa6cf62773d5dccf7a4e2f403def474600)
   #03 pc 000000000005f6b8 /system/lib64/platformsdk/libace_napi.z.so(panda::JSValueRef ArkNativeFunctionCallBack<true>(panda::JsiRuntimeCallInfo*)+240)(cbac5c2cdec75704b84a9ddba0333eb9)
   #04 pc 0000000000e8b488 /system/lib64/module/arkcompiler/stub.an(RTStub_PushCallArgsAndDispatchNative+40)
   #05 pc 000000000047dd94 /system/lib64/module/arkcompiler/stub.an(BCStub_HandleCallthis0Imm8V8StwCopy+396)
   #06 at anonymous (entry|entry|1.0.0|src/main/ets/pages/page_second/page_third_appfreeze/appfreeze_threadblock.ts:1730:25)
   ```

   堆栈表明主线程耗时最多的业务是libentry.so(TriggerBusinessBusySync)。结合代码进一步分析。
3. 开发调试场景下可直接在DevEco Studio中单击libentry.so所在的栈帧跳转到对应代码行；运维场景下使用[llvm-addr2line](bpta-stability-app-crash-cpp-way.md#li186453444512)解析找到对应代码行。

   证据3：故障栈帧所在的代码

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/73/v3/8_6z7hxVTr6hGnwPWeqChQ/zh-cn_image_0000002673735605.png "点击放大")

   业务中循环处理计算任务导致主线程繁忙。

**预防建议**

优化业务逻辑，减少主线程工作量，使用延迟加载。

### 执行耗时操作

**根因描述**

应用主线程连续多次进行耗时操作，累计耗时长造成主线程繁忙。

**问题分析思路**

1. 获取故障日志中告警部分和卡死部分的主线程堆栈中的应用侧业务信息；
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

**案例：循环处理多种耗时任务导致主线程繁忙**

**问题现象**

当用户触发业务代码调用后，应用进入无响应状态，一段时间后应用退出，并生成冻屏日志文件。

**问题分析**

1. 查看AppFreeze中THREAD\_BLOCK\_3S和THREAD\_BLOCK\_6S两部分的主线程堆栈，确认不一致。

   证据1：主线程堆栈关键栈帧

   THREAD\_BLOCK\_3S部分

   ```screen
   Tid:22780, Name:pfreezeanalysis
   state=R, utime=1239, stime=92, priority=-54, nice=-10, clk=100
   #00 pc 0000000000240030 /system/lib64/platformsdk/libark_jsruntime.so(panda::ecmascript::JSDate::Now()+52)(a0191e40080d8d657554ee4036a515b0)
   #01 pc 0000000000e8b488 /system/lib64/module/arkcompiler/stub.an(RTStub_PushCallArgsAndDispatchNative+40)
   #02 pc 000000000047dd94 /system/lib64/module/arkcompiler/stub.an(BCStub_HandleCallthis0Imm8V8StwCopy+396)
   #03 at delay entry (entry/src/main/ets/pages/page_second/page_third_appfreeze/appfreeze_threadblock.ets:997:14)
   #04 at businessOperationA3 entry (entry/src/main/ets/pages/page_second/page_third_appfreeze/appfreeze_threadblock.ets:989:3)
   #05 at businessOperationA entry (entry/src/main/ets/pages/page_second/page_third_appfreeze/appfreeze_threadblock.ets:951:9)
   #06 at triggerComplexOperations entry (entry/src/main/ets/pages/page_second/page_third_appfreeze/appfreeze_threadblock.ets:912:9)
   ```

   THREAD\_BLOCK\_6S部分

   ```screen
   Tid:22780, Name:pfreezeanalysis
   state=R, utime=1529, stime=92, priority=-54, nice=-10, clk=100
   #00 pc 0000000000497270 /system/lib64/module/arkcompiler/stub.an(BCStub_HandleLdobjbynameImm8Id16StwCopy+48)
   #01 at delay entry (entry/src/main/ets/pages/page_second/page_third_appfreeze/appfreeze_threadblock.ets:996:15)
   #02 at businessOperationB2 entry (entry/src/main/ets/pages/page_second/page_third_appfreeze/appfreeze_threadblock.ets:984:3)
   #03 at businessOperationB entry (entry/src/main/ets/pages/page_second/page_third_appfreeze/appfreeze_threadblock.ets:948:9)
   #04 at triggerComplexOperations entry (entry/src/main/ets/pages/page_second/page_third_appfreeze/appfreeze_threadblock.ets:912:9)
   ```

   两次主线程堆栈不一致，表明主线程没有阻塞，是处于繁忙状态。
2. 无增强日志，根据两次主线程堆栈提取热点业务函数为triggerComplexOperations。结合代码进一步分析。

   证据2：故障栈帧所在的代码

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c5/v3/jB9R_BsBT7SF7t_seLjSlw/zh-cn_image_0000002643575824.png "点击放大")

   业务中循环处理多个不同类型的耗时子任务导致主线程繁忙。

**预防建议**

将耗时操作移至子线程，使用异步任务处理。
