---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/graphics-accelerate-launch-faq-5
title: "日志中频繁打印BusinessError: The Worker instance is not running, maybe worker is terminated when PostMessage错误信息，应该如何排查"
breadcrumb: "指南 > 图形 > Graphics Accelerate Kit（图形加速服务） > Graphics Accelerate Kit常见问题 > 游戏启动加速服务 > 日志中频繁打印BusinessError: The Worker instance is not running, maybe worker is terminated when PostMessage错误信息，应该如何排查"
category: harmonyos-guides
scraped_at: 2026-09-21T06:18:26+08:00
doc_updated_at: 2026-05-08
content_hash: sha256:9c9d24e00264662b1c5501ee4342d20f91521b2066550cea2e374d3ddf0defae
---

该错误通常是由于Worker线程崩溃或被终止导致。

开发者可在日志中进一步查找worker.onerror相关日志，确认Worker线程崩溃时的具体异常信息。

```typescript
TuanjieMainWorker Error TypeError: undefined is not callable entry|entry|1.0.0|src/main/ets/workers/TuanjieMainWorkerHandler.ts
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cc/v3/rg2i4whgRcq_TRSfU24asw/zh-cn_image_0000002733435022.png)

根据worker.onerror日志排查，确认是否同时存在以下情况：

* 在onDestroy生命周期中销毁三方SDK。
* 三方SDK被销毁后，仍继续向Worker线程发送消息。
* Worker线程在处理消息过程中仍继续调用已销毁的三方SDK，且未进行异常处理。

在秒级启动场景下，如果用户重新启动游戏后又上滑移除游戏App，游戏进程不会主动销毁Worker线程和团结引擎。当上述三种情况同时发生时，可能导致Worker线程崩溃，并在日志中频繁打印如下错误信息：

```typescript
BusinessError: The Worker instance is not running, maybe worker is terminated when PostMessage
```
