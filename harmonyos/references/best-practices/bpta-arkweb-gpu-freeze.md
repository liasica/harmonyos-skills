---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-arkweb-gpu-freeze
title: ArkWeb GPU进程卡死故障模式说明
breadcrumb: 最佳实践 > 稳定性 > 稳定性分析 > 稳定性故障模式说明 > 应用冻屏故障模式说明 > ArkWeb GPU进程卡死故障模式说明
category: best-practices
scraped_at: 2026-09-02T15:03:23+08:00
doc_updated_at: 2026-08-26
content_hash: sha256:2b95619d6fe189e162855a7afc5857c599b0498f3ee63b9c7540d3301f4d21af
---

## 概述

本文旨在指导HarmonyOS应用开发者如何定位主线程阻塞在ArkWeb堆栈类型的应用冻屏（AppFreeze）问题。在这类问题中，GPU相关业务的堆栈较为普遍，造成这类问题的原因一般为I/O阻塞和等锁，本文将就这两个原因提供一些分析指导。

关于应用冻屏（AppFreeze）问题的检测原理和日志说明可先阅读[AppFreeze（应用冻屏）检测](../harmonyos-guides/appfreeze-guidelines.md)。

## I/O阻塞

### 根因描述

主线程ArkWeb内核因被耗时I/O操作阻塞，导致应用卡死，从而触发抓取AppFreeze日志操作。

### 问题分析思路

UI进程阻塞在WaitForGetOffsetInRange函数，该函数用于从UI进程向GPU进程发送mojo通信，I/O阻塞或GPU任务执行过慢，响应不及时，导致系统卡死。此类问题发生时，说明mojo通信对端有异常，可能存在耗时操作，需要查看I/O线程等堆栈进一步确认问题根因。

1. 参考[栈顶在方舟运行时的应用冻屏问题定位实践](bpta-stability-app-freeze-ark-runtime.md)，分析AppFreeze日志，3S和6S的堆栈一致，且栈帧如下：

   ```screen
   Tid:xxx, Name:xxx
   #00 pc xxx /system/lib/ld-musl-aarch64.so.1(__timedwait_cp+xx)
   #01 pc xxx /system/lib/ld-musl-aarch64.so.1(__pthread_cond_timedwait+xx)
   ...
   #xx pc xxx /data/.../libarkweb_engine.so
   gpu::CommandBufferProxyImpl::WaitForGetOffsetInRange(...)
   ```
2. 搜索线程名Chrome\_IOThread，分析该线程对应的堆栈。

### 关键字

3S和6S的堆栈一致，且其栈帧中包含关键字WaitForGetOffsetInRange；此外，Chrome\_IOThread线程作为I/O线程，也需要关注。

### 案例分析

**问题现象**

应用Web页面卡死，6秒后应用闪退。

**问题分析**

分析AppFreeze日志，3S和6S的堆栈一致，堆栈如下：

```screen
Tid:59546, Name:xxx
#00 pc 00000000001b9438 /system/lib/ld-musl-aarch64.so.1
#01 pc 00000000001bb58c /system/lib/ld-musl-aarch64.so.1
#02 pc 0000000004f9b1cc /data/storage/el1/bundle/arkwebcore/libs/arm64/libarkweb_engine.so
base::ConditionVariable::Wait() at /devcloud/ws/s0XHz/workspace/j_BPK0KULN/HwHarmonyEngine/src/out/musl_64\../../base/synchronization\condition_variable_posix.cc:79 (discriminator 2)
#03 pc 0000000004fbed40 /data/storage/el1/bundle/arkwebcore/libs/arm64/libarkweb_engine.so
base::WaitableEvent::TimedWaitImpl(base::TimeDelta) at /devcloud/ws/s0XHz/workspace/j_BPK0KULN/HwHarmonyEngine/src/out/musl_64\../../base/synchronization\waitable_event_posix.cc:193 (discriminator 2)
#04 pc 0000000004f4f754 /data/storage/el1/bundle/arkwebcore/libs/arm64/libarkweb_engine.so
base::WaitableEvent::TimedWait(base::TimeDelta) at /devcloud/ws/suJWu/workspace/j_HLS1VBOR/src/out/musl_64\../../base/synchronization\waitable_event.cc:39
#05 pc 0000000004f4f6e4 /data/storage/el1/bundle/arkwebcore/libs/arm64/libarkweb_engine.so
base::WaitableEvent::Wait() at /devcloud/ws/suJWu/workspace/j_HLS1VBOR/src/out/musl_64\../../base/synchronization\waitable_event.cc:23 (discriminator 2)
#06 pc 0000000005205390 /data/storage/el1/bundle/arkwebcore/libs/arm64/libarkweb_engine.so
mojo::(anonymous namespace)::ThreadSafeInterfaceEndpointClientProxy::SendMessageWithResponder(mojo::Message&, std::__h::unique_ptr<mojo::MessageReceiver, std::__h::default_delete<mojo::MessageReceiver> >) (.64c5c9a486ae75b6fffaf6ed09e7ff33) at /devcloud/ws/sSt7w/workspace/j_YFEIN8EW/HwHarmonyEngine/src/out/musl_64\../../mojo/public/cpp/bindings/lib\interface_endpoint_client.cc:431 (discriminator 2)
#07 pc 000000000520d680 /data/storage/el1/bundle/arkwebcore/libs/arm64/libarkweb_engine.so
mojo::internal::ThreadSafeForwarderBase::AcceptWithResponder(mojo::Message*, std::__h::unique_ptr<mojo::MessageReceiver, std::__h::default_delete<mojo::MessageReceiver> >) at /devcloud/ws/syGBE/workspace/j_PCKU3CLG/src/out/musl_64\../../mojo/public/cpp/bindings/lib\thread_safe_forwarder_base.cc:32 (discriminator 4)
#08 pc 0000000005213040 /data/storage/el1/bundle/arkwebcore/libs/arm64/libarkweb_engine.so
mojo::internal::SendMojoMessage(mojo::MessageReceiverWithResponder&, mojo::Message&, std::__h::unique_ptr<mojo::MessageReceiver, std::__h::default_delete<mojo::MessageReceiver> >) at /devcloud/ws/s0XHz/workspace/j_BPK0KULN/HwHarmonyEngine/src/out/musl_64\../../mojo/public/cpp/bindings/lib\send_message_helper.cc:42 (discriminator 2)
#09 pc 0000000002f7ffe4 /data/storage/el1/bundle/arkwebcore/libs/arm64/libarkweb_engine.so
gpu::mojom::GpuChannelProxy::WaitForGetOffsetInRange(int, unsigned int, int, int, gpu::CommandBuffer::State*) at /devcloud/ws/sSt7w/workspace/j_YFEIN8EW/HwHarmonyEngine/src/out/musl_64\gen/gpu/ipc/common\gpu_channel.mojom.cc:3251 (discriminator 2)
#10 pc 0000000003073c10 /data/storage/el1/bundle/arkwebcore/libs/arm64/libarkweb_engine.so
gpu::CommandBufferProxyImpl::WaitForGetOffsetInRange(unsigned int, int, int) at /devcloud/ws/sSt7w/workspace/j_YFEIN8EW/HwHarmonyEngine/src/out/musl_64\../../gpu/ipc/client\command_buffer_proxy_impl.cc:317 (discriminator 4)
```

分析上述堆栈，发现卡在WaitForGetOffsetInRange函数，表明此时可能有I/O阻塞的情况，需要全局查找线程Chrome\_IOThread。此时发现#19帧为Web提供的网络拦截接口，且最上层的#02栈是业务libxxx.so。分析可知，业务侧对Web进行网络拦截时，执行了超过6秒的逻辑，导致阻塞I/O线程超过6秒，此时UI线程转发mojo消息无法成功导致的卡死。

```screen
Tid:59729, Name:Chrome_IOThread
#00 pc 00000000001b9438 /system/lib/ld-musl-aarch64.so.1
#01 pc 00000000001bf5b4 /system/lib/ld-musl-aarch64.so.1
#02 pc 0000000000010a58 /data/storage/el1/bundle/libs/arm64/libxxx.so
#03 pc 0000000000019848 /data/storage/el1/bundle/libs/arm64/libxxx.so
...
#19 pc 0000000004e75bd8 /data/storage/el1/bundle/arkwebcore/libs/arm64/libarkweb_engine.so
OHOS::NWeb::NWebSchemeHandlerFactory::Create(scoped_refptr<CefBrowser>, scoped_refptr<CefFrame>, CefStringBase<CefStringTraitsUTF16> const&, scoped_refptr<CefRequest>) at /devcloud/ws/s9dho/workspace/j_Y9KURQTS/HwHarmonyEngine/src/out/musl_64\../../ohos_nweb/src/cef_delegate\nweb_scheme_handler_factory.cc:150
#20 pc 00000000027f8824 /data/storage/el1/bundle/arkwebcore/libs/arm64/libarkweb_engine.so
net_service::(anonymous namespace)::InterceptedRequestHandlerWrapper::GetOhosResourceHandlerResult(int, network::ResourceRequest*, scoped_refptr<CefResourceHandler>, base::OnceCallback<void (std::__h::unique_ptr<net_service::ResourceResponse, std::__h::default_delete<net_service::ResourceResponse> >)>) at /devcloud/ws/s9dho/workspace/j_Y9KURQTS/HwHarmonyEngine/src/out/musl_64\../../cef/libcef/browser/net_service\resource_request_handler_wrapper.cc:974 (discriminator 2)
 (inlined by) net_service::(anonymous namespace)::InterceptedRequestHandlerWrapper::GetOhosResourceHandlerResultInIO(int, network::ResourceRequest*, base::OnceCallback<void (std::__h::unique_ptr<net_service::ResourceResponse, std::__h::default_delete<net_service::ResourceResponse> >)>, scoped_refptr<CefResourceHandler>) (.df3920d6276824318412197eb3d7bb61) at /devcloud/ws/s9dho/workspace/j_Y9KURQTS/HwHarmonyEngine/src/out/musl_64\../../cef/libcef/browser/net_service\resource_request_handler_wrapper.cc:1073 (discriminator 4)
```

**问题总结**

遇到此类问题时，需要分析Chrome\_IOThread线程，查看该线程的调用栈来进一步分析。

**修复建议**

针对网络拦截的接口实现，建议参考用法：start后直接返回，在异步线程完成操作后再调用DidReceiveResponse()/DidReceiveData()返回数据。接口使用参考[拦截Web组件发起的网络请求](../harmonyos-guides/web-scheme-handler.md)。

## 等锁

### 根因描述

主线程ArkWeb内核由于受到其他业务持锁影响，mojo消息转发受阻塞，导致应用卡死，从而触发抓取AppFreeze日志操作。

### 问题分析思路

这类问题的3S和6S栈都报在ArkWeb的栈中，但此时往往ArkWeb是受害者，需要找到对应的持锁等待的线程，堆栈一般如下：

```screen
Tid:xxx, Name:xxx
#00 pc xxx /system/lib/ld-musl-aarch64.so.1(__timedwait_cp+xx)
#01 pc xxx /system/lib/ld-musl-aarch64.so.1(pthread_cond_timedwait+xx)
...
#xx pc xxx /data/storage/el1/bundle/arkwebcore/libs/arm64/libarkweb_engine.so(viz::mojom::PAC_FrameSinkManagerProxy::DestroyCompositorFrameSink(viz::PAC_FrameSinkId const&)+xx)
```

被阻塞线程堆栈一般如下：

```screen
Tid:xxx, Name:xxx
#00 pc xxx /system/lib/ld-musl-aarch64.so.1(__timedwait_cp+xx)
#01 pc xxx /system/lib/ld-musl-aarch64.so.1(pthread_cond_timedwait+xx)
#02 pc xxx /data/storage/el1/bundle/libs/arm64/libc++_shared.so(std::__n1::condition_variable::wait(std::__n1::unique_lock<std::__n1::mutex>&)+xx)
#03 pc xxx /data/storage/el1/bundle/libs/arm64/libc++_shared.so(std::__n1::__shared_mutex_base::lock_shared()+xx)
...
```

需要找到Chrome\_InProcGp、VizCompositorTh、CompositorGpuTh、Chrome\_IOThread等线程分析持锁情况，查看系统或业务堆栈，分析持锁是否不当。

### 关键字

被阻塞线程堆栈一般有mutex、lock等关键字；3S和6S的堆栈则无特殊关键字。

### 案例分析

**案例一**

**问题现象**

应用Web页面卡死，6秒后闪退。

**问题分析**

3S和6S的堆栈一致，堆栈如下：

```screen
Timestamp:2025-06-24 11:22:11:814
Tid:8360, Name:xxx
#00 pc 00000000001b67f8 /system/lib/ld-musl-aarch64.so.1(__timedwait_cp+192)(35064c759de623f1ea3ec0b012a28c3c)
#01 pc 00000000001b87fc /system/lib/ld-musl-aarch64.so.1(__pthread_cond_timedwait+188)(35064c759de623f1ea3ec0b012a28c3c)
#02 pc 0000000004f32180 /data/storage/el1/bundle/arkwebcore/libs/arm64/libarkweb_engine.so(b5f6591c9544815807de591f10430486a42ced64)
base::ConditionVariable::Wait() at /devcloud/ws/s0XHz/workspace/j_BPK0KULN/HwHarmonyEngine/src/out/musl_64\../../base/synchronization\condition_variable_posix.cc:79 (discriminator 2)
...
#13 pc 0000000003bfed38 /data/storage/el1/bundle/arkwebcore/libs/arm64/libarkweb_engine.so(b5f6591c9544815807de591f10430486a42ced64)
viz::mojom::FrameSinkManagerProxy::DestroyCompositorFrameSink(viz::FrameSinkId const&) at /devcloud/ws/s1qK3/workspace/j_SNQMFI5M/HwHarmonyEngine/src/out/musl_64\gen/services/viz/privileged/mojom/compositing\frame_sink_manager.mojom.cc:1387 (discriminator 2)
```

根据栈顶分析，阻塞发生在mojo的接口中，分析调用栈发现是viz业务DestroyCompositorFrameSink触发的等待，因此优先检查Chrome\_InProcGp线程堆栈是否存在阻塞。此时发现阻塞在EglWrapper调用中，#02帧显示正在等待recursive\_mutex。

```screen
Tid:8599, Name:Chrome_InProcGp
#00 pc 00000000001b67f8 /system/lib/ld-musl-aarch64.so.1(__timedwait_cp+192)(35064c759de623f1ea3ec0b012a28c3c)
#01 pc 00000000001bc810 /system/lib/ld-musl-aarch64.so.1(__pthread_mutex_timedlock_inner+592)(35064c759de623f1ea3ec0b012a28c3c)
#02 pc 00000000000c4014 /system/lib64/libc++.so(std::__h::recursive_mutex::lock()+8)(a2d45389edece3475c17a1d7fc9a76ec2b697825)
#03 pc 000000000003a788 /system/lib64/libEGL.so(OHOS::EglWrapperDisplay::MakeCurrent(void*, void*, void*)+44)(12088e3ba5a7595b85687e148a8d8bd2)
#04 pc 000000000002ee60 /system/lib64/libEGL.so(eglMakeCurrent+288)(12088e3ba5a7595b85687e148a8d8bd2)
#05 pc 0000000005c87530 /data/storage/el1/bundle/arkwebcore/libs/arm64/libarkweb_engine.so(b5f6591c9544815807de591f10430486a42ced64)
gl::GLContextEGL::MakeCurrentImpl(gl::GLSurface*) at /devcloud/ws/sSt7w/workspace/j_YFEIN8EW/HwHarmonyEngine/src/out/musl_64\../../ui/gl\gl_context_egl.cc:486 (discriminator 6)
#06 pc 00000000062500dc /data/storage/el1/bundle/arkwebcore/libs/arm64/libarkweb_engine.so(b5f6591c9544815807de591f10430486a42ced64)
gpu::SharedContextState::MakeCurrent(gl::GLSurface*, bool) at /devcloud/ws/sSt7w/workspace/j_YFEIN8EW/HwHarmonyEngine/src/out/musl_64\../../gpu/command_buffer/service\shared_context_state.cc:596 (discriminator 2)
#07 pc 000000000622d278 /data/storage/el1/bundle/arkwebcore/libs/arm64/libarkweb_engine.so(b5f6591c9544815807de591f10430486a42ced64)
gpu::raster::GrCacheController::PurgeGrCache(unsigned long) at /devcloud/ws/sSt7w/workspace/j_YFEIN8EW/HwHarmonyEngine/src/out/musl_64\../../gpu/command_buffer/service\gr_cache_controller.cc:62
#08 pc 00000000030cd728 /data/storage/el1/bundle/arkwebcore/libs/arm64/libarkweb_engine.so(b5f6591c9544815807de591f10430486a42ced64)
base::RepeatingCallback<void ()>::Run() && at /devcloud/ws/sP0jU/workspace/j_HLCVDUC4/HwHarmonyEngine/src/out/musl_64\../../base/functional\callback.h:152 (discriminator 4)
```

因单进程中仅允许一个线程持有EGL锁，故搜索EglWrapperDisplay，查看其他线程调用。

```screen
Tid:10052, Name:xxx
#00 pc 00000000001b67f8 /system/lib/ld-musl-aarch64.so.1(__timedwait_cp+192)(35064c759de623f1ea3ec0b012a28c3c)
#01 pc 00000000001b87fc /system/lib/ld-musl-aarch64.so.1(__pthread_cond_timedwait+188)(35064c759de623f1ea3ec0b012a28c3c)
#02 pc 00000000000c11c0 /system/lib64/libc++.so(std::__h::condition_variable::__do_timed_wait(std::__h::unique_lock<std::__h::mutex>&, std::__h::chrono::time_point<std::__h::chrono::system_clock, std::__h::chrono::duration<long long, std::__h::ratio<1l, 1000000000l>>>)+108)(a2d45389edece3475c17a1d7fc9a76ec2b697825)
#03 pc 0000000000056d10 /system/lib64/chipset-pub-sdk/libsurface.z.so(38ecd06f7a8774e8edf4b5cc278015ea)
#04 pc 0000000000048b98 /system/lib64/chipset-pub-sdk/libsurface.z.so(OHOS::BufferQueue::RequestBufferLocked(OHOS::BufferRequestConfig const&, OHOS::sptr<OHOS::BufferExtraData>&, OHOS::IBufferProducer::RequestBufferReturnValue&, std::__h::unique_lock<std::__h::mutex>&)+840)(38ecd06f7a8774e8edf4b5cc278015ea)
#05 pc 0000000000049b1c /system/lib64/chipset-pub-sdk/libsurface.z.so(OHOS::BufferQueue::RequestBuffer(OHOS::BufferRequestConfig const&, OHOS::sptr<OHOS::BufferExtraData>&, OHOS::IBufferProducer::RequestBufferReturnValue&)+272)(38ecd06f7a8774e8edf4b5cc278015ea)
#06 pc 0000000000073a1c /system/lib64/chipset-pub-sdk/libsurface.z.so(OHOS::ProducerSurface::RequestBuffer(OHOS::sptr<OHOS::SurfaceBuffer>&, OHOS::sptr<OHOS::SyncFence>&, OHOS::BufferRequestConfig&)+204)(38ecd06f7a8774e8edf4b5cc278015ea)
#07 pc 000000000006d170 /system/lib64/chipset-pub-sdk/libsurface.z.so(OH_NativeWindow_NativeWindowRequestBuffer+404)(38ecd06f7a8774e8edf4b5cc278015ea)
#08 pc 0000000000416cf8 /vendor/lib64/chipsetsdk/libhvgr_v200.so
#09 pc 000000000037c314 /vendor/lib64/chipsetsdk/libhvgr_v200.so
#10 pc 000000000037d138 /vendor/lib64/chipsetsdk/libhvgr_v200.so
#11 pc 000000000037ce80 /vendor/lib64/chipsetsdk/libhvgr_v200.so(eglSwapBuffers+44)
#12 pc 000000000003bcd8 /system/lib64/libEGL.so(OHOS::EglWrapperDisplay::SwapBuffers(void*)+100)(12088e3ba5a7595b85687e148a8d8bd2)
#13 pc 000000000002f2d0 /system/lib64/libEGL.so(eglSwapBuffers+264)(12088e3ba5a7595b85687e148a8d8bd2)
#14 pc 00000000001f6370 /data/storage/el1/bundle/libs/arm64/libxxx.so(...)
#15 pc 00000000001f50bc /data/storage/el1/bundle/libs/arm64/libxxx.so(...)
#16 pc 000000000022c1d8 /data/storage/el1/bundle/libs/arm64/libxxx.so(...)
#17 pc 0000000000229ed4 /data/storage/el1/bundle/libs/arm64/libxxx.so(...)
```

此时发现10052线程调用EGL函数卡住，对应业务需进一步分析，可通过调用栈排查具体业务so的持锁情况。

**排查建议**

业务优先解堆栈，根据业务的堆栈代码，排查是否有持EGL锁的业务，查看EGL锁使用是否规范。

**案例二**

**问题现象**

应用Web页面卡死，6秒后闪退。

**问题分析**

3S和6S的堆栈如下：

```screen
Tid:50027, Name:xxx
#00 pc 00000000001b64c8 /system/lib/ld-musl-aarch64.so.1(__timedwait_cp+148)(16e71a67bfa83c977534a6b3e5f80cee)
#01 pc 00000000001b8518 /system/lib/ld-musl-aarch64.so.1(__pthread_cond_timedwait+168)(16e71a67bfa83c977534a6b3e5f80cee)
#02 pc 0000000005003aa0 /data/storage/el1/bundle/arkwebcore/libs/arm64/libarkweb_engine.so(base::ConditionVariable::Wait()+104)(c2910157af51b9971be1eddcf1d98f0a5dff4dd8)
#03 pc 0000000005027368 /data/storage/el1/bundle/arkwebcore/libs/arm64/libarkweb_engine.so(base::WaitableEvent::TimedWaitImpl(base::TimeDelta)+784)(c2910157af51b9971be1eddcf1d98f0a5dff4dd8)
#04 pc 0000000004fb8960 /data/storage/el1/bundle/arkwebcore/libs/arm64/libarkweb_engine.so(base::WaitableEvent::TimedWait(base::TimeDelta)+96)(c2910157af51b9971be1eddcf1d98f0a5dff4dd8)
#05 pc 0000000004fb88f0 /data/storage/el1/bundle/arkwebcore/libs/arm64/libarkweb_engine.so(base::WaitableEvent::Wait()+16)(c2910157af51b9971be1eddcf1d98f0a5dff4dd8)
#06 pc 000000000526e3d4 /data/storage/el1/bundle/arkwebcore/libs/arm64/libarkweb_engine.so(mojo::(anonymous namespace)::ThreadSafeInterfaceEndpointClientProxy::SendMessageWithResponder(mojo::Message&, std::__h::unique_ptr<mojo::MessageReceiver, std::__h::default_delete<mojo::MessageReceiver>>)+1336)(c2910157af51b9971be1eddcf1d98f0a5dff4dd8)
#07 pc 00000000052766c4 /data/storage/el1/bundle/arkwebcore/libs/arm64/libarkweb_engine.so(mojo::internal::ThreadSafeForwarderBase::AcceptWithResponder(mojo::Message*, std::__h::unique_ptr<mojo::MessageReceiver, std::__h::default_delete<mojo::MessageReceiver>>)+44)(c2910157af51b9971be1eddcf1d98f0a5dff4dd8)
#08 pc 000000000527c084 /data/storage/el1/bundle/arkwebcore/libs/arm64/libarkweb_engine.so(mojo::internal::SendMojoMessage(mojo::MessageReceiverWithResponder&, mojo::Message&, std::__h::unique_ptr<mojo::MessageReceiver, std::__h::default_delete<mojo::MessageReceiver>>)+144)(c2910157af51b9971be1eddcf1d98f0a5dff4dd8)
#09 pc 0000000002fb59a0 /data/storage/el1/bundle/arkwebcore/libs/arm64/libarkweb_engine.so(gpu::mojom::GpuChannelProxy::WaitForGetOffsetInRange(int, unsigned int, int, int, gpu::CommandBuffer::State*)+360)(c2910157af51b9971be1eddcf1d98f0a5dff4dd8)
#10 pc 00000000030b9ad4 /data/storage/el1/bundle/arkwebcore/libs/arm64/libarkweb_engine.so(gpu::CommandBufferProxyImpl::WaitForGetOffsetInRange(unsigned int, int, int)+612)(c2910157af51b9971be1eddcf1d98f0a5dff4dd8)
```

观察到有关键字WaitForGetOffsetInRange，在堆栈日志中全局搜索Chrome\_IOThread，找到该线程的堆栈。

```screen
Tid:50276, Name:Chrome_IOThread
#00 pc 00000000001b64c8 /system/lib/ld-musl-aarch64.so.1(__timedwait_cp+148)(16e71a67bfa83c977534a6b3e5f80cee)
#01 pc 00000000001b8518 /system/lib/ld-musl-aarch64.so.1(__pthread_cond_timedwait+168)(16e71a67bfa83c977534a6b3e5f80cee)
#02 pc 00000000000c439c /data/storage/el1/bundle/libs/arm64/libc++_shared.so(std::__n1::condition_variable::wait(std::__n1::unique_lock<std::__n1::mutex>&)+20)(1204f957e9c8ca1e5b2539b1755de7e26e4f8e8d)
#03 pc 00000000000ca004 /data/storage/el1/bundle/libs/arm64/libc++_shared.so(std::__n1::__shared_mutex_base::lock_shared()+84)(1204f957e9c8ca1e5b2539b1755de7e26e4f8e8d)
#04 pc 00000000000840cc /data/storage/el1/bundle/libs/arm64/libxxx.so(...)
#05 pc 0000000000089444 /data/storage/el1/bundle/libs/arm64/libxxx.so(...)
#06 pc 0000000000088908 /data/storage/el1/bundle/libs/arm64/libxxx.so(...)
#07 pc 000000000008d00c /data/storage/el1/bundle/libs/arm64/libxxx.so(...)
```

这类问题的根本原因在于Chromium原生逻辑：需要在UI线程上抛出同步任务到GPU相关线程，等待任务执行完成后返回，才能析构Web组件，保证生命周期。在这里mojo同步接口需通过Chrome\_IOThread线程转发消息，通过调用栈可以看到，由于业务so持锁未释放，阻塞了Chrome\_IOThread线程消息转发，导致UI线程阻塞。

**排查建议**

业务优先根据so解堆栈，根据堆栈代码排查业务持锁的问题，是否未释放锁。

**案例三**

**问题现象**

应用Web页面卡死，6秒后闪退。

**问题分析**

3S和6S的堆栈一致，堆栈如下：

```screen
Tid:1558, Name:xxx
#00 pc 00000000001cc2fc /system/lib/ld-musl-aarch64.so.1(__timedwait_cp+156)(4dcf1315ac91d1611e703e23ab16e8c7)
#01 pc 00000000001ce3cc /system/lib/ld-musl-aarch64.so.1(pthread_cond_timedwait+172)(4dcf1315ac91d1611e703e23ab16e8c7)
#02 pc 00000000047dce28 /data/storage/el1/bundle/arkwebcore/libs/arm64/libarkweb_engine.so(base::PAC_ConditionVariable::Wait()+148)(36d1a5650b9ab413653e7fb36581fd2f0610b9aa)
#03 pc 0000000004818d08 /data/storage/el1/bundle/arkwebcore/libs/arm64/libarkweb_engine.so(base::PAC_WaitableEvent::TimedWaitImpl(base::PAC_TimeDelta)+544)(36d1a5650b9ab413653e7fb36581fd2f0610b9aa)
#04 pc 0000000004782970 /data/storage/el1/bundle/arkwebcore/libs/arm64/libarkweb_engine.so(base::PAC_WaitableEvent::TimedWait(base::PAC_TimeDelta)+160)(36d1a5650b9ab413653e7fb36581fd2f0610b9aa)
#05 pc 00000000047828c0 /data/storage/el1/bundle/arkwebcore/libs/arm64/libarkweb_engine.so(base::PAC_WaitableEvent::Wait()+16)(36d1a5650b9ab413653e7fb36581fd2f0610b9aa)
#06 pc 0000000004bfceec /data/storage/el1/bundle/arkwebcore/libs/arm64/libarkweb_engine.so(mojo::Wait(mojo::PAC_Handle, unsigned int, unsigned int, PAC_MojoHandleSignalsState*)+268)(36d1a5650b9ab413653e7fb36581fd2f0610b9aa)
#07 pc 00000000038c43c4 /data/storage/el1/bundle/arkwebcore/libs/arm64/libarkweb_engine.so(mojo::Wait(mojo::PAC_Handle, unsigned int, PAC_MojoHandleSignalsState*)+36)(36d1a5650b9ab413653e7fb36581fd2f0610b9aa)
#08 pc 0000000004be1274 /data/storage/el1/bundle/arkwebcore/libs/arm64/libarkweb_engine.so(mojo::PAC_Connector::WaitForIncomingMessage()+60)(36d1a5650b9ab413653e7fb36581fd2f0610b9aa)
#09 pc 0000000004beb3e0 /data/storage/el1/bundle/arkwebcore/libs/arm64/libarkweb_engine.so(mojo::internal::PAC_MultiplexRouter::PAC_InterfaceEndpoint::SyncWatchExclusive(unsigned long)+112)(36d1a5650b9ab413653e7fb36581fd2f0610b9aa)
#10 pc 0000000004be4f18 /data/storage/el1/bundle/arkwebcore/libs/arm64/libarkweb_engine.so(mojo::PAC_InterfaceEndpointClient::SendMessageWithResponder(mojo::PAC_Message*, bool, mojo::PAC_InterfaceEndpointClient::SyncSendMode, std::__Cr::unique_ptr<mojo::PAC_MessageReceiver, std::__Cr::default_delete<mojo::PAC_MessageReceiver>>)+628)(36d1a5650b9ab413653e7fb36581fd2f0610b9aa)
#11 pc 0000000004be5134 /data/storage/el1/bundle/arkwebcore/libs/arm64/libarkweb_engine.so(mojo::PAC_InterfaceEndpointClient::AcceptWithResponder(mojo::PAC_Message*, std::__Cr::unique_ptr<mojo::PAC_MessageReceiver, std::__Cr::default_delete<mojo::PAC_MessageReceiver>>)+32)(36d1a5650b9ab413653e7fb36581fd2f0610b9aa)
#12 pc 0000000004bf84b8 /data/storage/el1/bundle/arkwebcore/libs/arm64/libarkweb_engine.so(mojo::internal::SendMojoMessage(mojo::PAC_MessageReceiverWithResponder&, mojo::PAC_Message&, std::__Cr::unique_ptr<mojo::PAC_MessageReceiver, std::__Cr::default_delete<mojo::PAC_MessageReceiver>>)+108)(36d1a5650b9ab413653e7fb36581fd2f0610b9aa)
#13 pc 0000000001ed1b7c /data/storage/el1/bundle/arkwebcore/libs/arm64/libarkweb_engine.so(viz::mojom::PAC_FrameSinkManagerProxy::DestroyCompositorFrameSink(viz::PAC_FrameSinkId const&)+340)(36d1a5650b9ab413653e7fb36581fd2f0610b9aa)
```

根据堆栈分析，找到VizCompositorTh线程，进一步看到阻塞在了IPC通信中，需要找到对端的线程号，因此全局搜索2178；

```screen
Tid:2178, Name:VizCompositorTh
#00 pc 000000000018a648 /system/lib/ld-musl-aarch64.so.1(ioctl+164)(4dcf1315ac91d1611e703e23ab16e8c7)
#01 pc 000000000000ecd0 /system/lib64/chipset-sdk-sp/libipc_common.z.so(OHOS::BinderConnector::WriteBinder(unsigned long, void*)+124)(1c998eec085cdb89fa5895a5080a0839)
#02 pc 0000000000072ee4 /system/lib64/chipset-sdk-sp/libipc_single.z.so(OHOS::BinderInvoker::TransactWithDriver(bool)+284)(64a17fcbe779a6da9fa26574ccce2f1e)
#03 pc 000000000007187c /system/lib64/chipset-sdk-sp/libipc_single.z.so(OHOS::BinderInvoker::WaitForCompletion(OHOS::MessageParcel*)+124)(64a17fcbe779a6da9fa26574ccce2f1e)
#04 pc 0000000000070cf0 /system/lib64/chipset-sdk-sp/libipc_single.z.so(OHOS::BinderInvoker::SendRequest(int, unsigned int, OHOS::MessageParcel&, OHOS::MessageParcel&, OHOS::MessageOption&)+620)(64a17fcbe779a6da9fa26574ccce2f1e)
#05 pc 0000000000049b3c /system/lib64/chipset-sdk-sp/libipc_single.z.so(OHOS::IPCObjectProxy::SendRequestInner(bool, unsigned int, OHOS::MessageParcel&, OHOS::MessageParcel&, OHOS::MessageOption&)+272)(64a17fcbe779a6da9fa26574ccce2f1e)
#06 pc 000000000004a588 /system/lib64/chipset-sdk-sp/libipc_single.z.so(OHOS::IPCObjectProxy::SendRequest(unsigned int, OHOS::MessageParcel&, OHOS::MessageParcel&, OHOS::MessageOption&)+216)(64a17fcbe779a6da9fa26574ccce2f1e)
```

找到线程2178的对端线程为2150，因此全局搜索2150；

```screen
BinderCatcher --
    1558:2178 to 1790:2150 code 5004 wait:15.672447500 s frz_state:3,  ns:-1:-1 to -1:-1, debug:1558:2178 to 1790:2150, active_code:0, active_thread=0, pending_async_proc=0
async   5921:6512 to 1558:0 code 13 wait:3.205905625 s frz_state:3,  ns:-1:-1 to -1:-1, debug:5921:6512 to 1558:0, active_code:2, active_thread=2037, pending_async_proc=5921
async   5921:6512 to 1558:0 code 2f wait:3.30637187 s frz_state:3,  ns:-1:-1 to -1:-1, debug:5921:6512 to 1558:0, active_code:2, active_thread=2037, pending_async_proc=5921
```

根据2150线程的堆栈，需要排查下面的业务so的持锁情况。

```screen
Tid:2150, Name:OS_IPC_0_2150
#00 pc 00000000001cc2fc /system/lib/ld-musl-aarch64.so.1(__timedwait_cp+156)(4dcf1315ac91d1611e703e23ab16e8c7)
#01 pc 00000000001ce3cc /system/lib/ld-musl-aarch64.so.1(pthread_cond_timedwait+172)(4dcf1315ac91d1611e703e23ab16e8c7)
#02 pc 00000000000c4984 /system/lib64/chipset-sdk-sp/libc++.so(std::__h::condition_variable::wait(std::__h::unique_lock<std::__h::mutex>&)+32)(4c257fafd66f57a4f1f873163a520100e191a256)
#03 pc 00000000000c55b0 /system/lib64/chipset-sdk-sp/libc++.so(std::__h::__assoc_sub_state::wait()+72)(4c257fafd66f57a4f1f873163a520100e191a256)
#04 pc 0000000000214a2c /system/lib64/libxxx.so(...)
#05 pc 0000000000496770 /system/lib64/libxxx.so(...)
```

**排查建议**

结合binder对端进程堆栈信息，排查对端阻塞原因。
