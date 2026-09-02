---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-function-flow-runtime-1
title: 下载任务切换到后台下载中断
breadcrumb: FAQ > 应用框架开发 > NDK开发 > 任务并发调度（Function Flow Runtime） > 下载任务切换到后台下载中断
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:58+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:67f83394425a086fae9e82bc592368e2437299d1a42684cf2e61b5b969a90fe2
---

## 问题现象

下载任务正常启动，但是应用切换到后台后下载中断。

## 背景知识

[FFRT](../harmonyos-references/capi-ffrt.md)：用于调度执行开发者基于Function Flow编程模型开发的应用，FFRT日志能够显示资源分配和线程的错误信息。

## 问题定位

根据HiLog日志，进行问题定位。

1. 搜索关键字FOREGROUND、BACKGROUND，如果出现了类似日志且附近有“应用包名”的日志，则说明该应用此时进入了前台或后台，即故障发生点：

   ```shell
   I C01406/render_service/OHOS::RS: RSSurfaceRenderNodeDrawable::OnDraw name:BackgroundBlurView2, the number of total processedNodes: 2
   W C03301/'应用包名'/LIBUV: loop:394697872256, flag:complete, active reqs:100
   I C015B0/'应用包名'/NETSTACK: [http_exec.cpp:298] CURL_TRACE: type = 7, data = STATE: INIT => CONNECT handle f000
   I C01406/render_service/skia: RSHardwareThread::CommitAndReleaseLayers task execute, SurfaceName: [RCDBottomSurfaceNode7030861463553, RCDTopSurfaceNode7030861463553, DisplayNode]
   I C015B0/’应用包名’/NETSTACK: [http_exec.cpp:298] CURL_TRACE: type = 7, data = STATE: CONNECT => CONNECTING handle f000
   I C015B0/’应用包名’/NETSTACK: [http_exec.cpp:298] CURL_TRACE: type = 7, data = STATE: CONNECTING => PROTOCONNECT handle f000
   I C015B0/’应用包名’/NETSTACK: [http_exec.cpp:298] CURL_TRACE: type = 7, data = STATE: PROTOCONNECT => DO handle f000
   W C01719/hiview/ffrt: 73810:DevFFTSSchedClose:116 close ffts sched device fd:4
   I C015B0/’应用包名’/NETSTACK: [http_exec.cpp:298] CURL_TRACE: type = 7, data = STATE: DO => DID handle f000
   W C01719/useriam/ffrt: 24152:FFRTQosApplyForOther:244 tid 59557, Operation not permitted, ret:-1, eno:1
   I C015B0/’应用包名’/NETSTACK: [http_exec.cpp:298] CURL_TRACE: type = 7, data = STATE: DID => PERFORMING handle f000
   E C01719/hiview/ffrt: 73811:DevFFTSOpen:73 open ffts device error, fd= -1, errno=12.
   ```
2. 在故障位置附近发现报错信息为：

   ```shell
    W C01719/hiview/ffrt: 73810:DevFFTSSchedClose:116 close ffts sched device fd:4 code:1001
    W C01719/useriam/ffrt: 24152:FFRTQosApplyForOther:244 tid 59557, Operation not permitted, ret:-1, eno:1
    E C01719/hiview/ffrt: 73811:DevFFTSOpen:73 open ffts device error, fd= -1, errno=12.
   ```

   日志显示：

   * 尝试关闭FFRT设备时失败（fd:4）。
   * FFRTQosApplyForOther报错“Operation not permitted”。
   * DevFFTSOpen失败，返回errno=12（ENOMEM，内存不足）。
3. 且故障点附近日志显示LiveEventBus频繁调用，多个下载任务同时进行。

   ```screen
   -------> LiveEventBusCore get <------
   [LiveEventBus]    postValue:[object Object] observer:[object Object] owner:3
   -------> LiveEventBusCore get <------
   [LiveEventBus]    message received: [object Object]
   -------> LiveEventBusCore get <------
   [LiveEventBus]    postValue:[object Object] observer:[object Object] owner:3
   -------> LiveEventBusCore get <------
   [LiveEventBus]    message received: [object Object]
   -------> LiveEventBusCore get <------
   [LiveEventBus]    postValue:[object Object] observer:[object Object] owner:3
   -------> LiveEventBusCore get <------
   [LiveEventBus]    message received: [object Object]
   -------> LiveEventBusCore get <------
   [LiveEventBus]    postValue:[object Object] observer:[object Object] owner:3
   ```

## 分析结论

应用未考虑高负载下的处理逻辑进行优化，高并发下载导致手机内存耗尽，下载线程崩溃暂停。

## 修改建议

对高并发下的下载场景进行优化，使用TaskPool提供的多任务优先级调度机制，根据业务需求合理设置优先级。参考[应用并发设计](../best-practices/bpta-app-concurrency-design.md)。
