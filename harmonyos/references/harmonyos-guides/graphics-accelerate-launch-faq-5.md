---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/graphics-accelerate-launch-faq-5
title: 日志中频繁打印BusinessError: The Worker instance is not running, maybe worker is terminated when PostMessage错误信息，应该如何排查？
breadcrumb: 指南 > 图形 > Graphics Accelerate Kit（图形加速服务） > Graphics Accelerate Kit常见问题 > 游戏启动加速服务 > 日志中频繁打印BusinessError: The Worker instance is not running, maybe worker is terminated when PostMessage错误信息，应该如何排查？
category: harmonyos-guides
scraped_at: 2026-04-29T13:36:40+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:ee13c62c05b81334ab356a7271259cfe7745db6955125313c1b01f2b2a7a1a5f
---

该错误通常是由于Worker线程崩溃或被终止导致。

开发者可在日志中进一步查找worker.onerror相关日志，确认Worker线程崩溃时的具体异常信息。

```
1. TuanjieMainWorker Error TypeError: undefined is not callable entry|entry|1.0.0|src/main/ets/workers/TuanjieMainWorkerHandler.ts
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ea/v3/IFqMbhNaRNKvPnLef-ACfw/zh-cn_image_0000002589325103.png?HW-CC-KV=V1&HW-CC-Date=20260429T053639Z&HW-CC-Expire=86400&HW-CC-Sign=4AA5B8E6C16CC9C26CABF5F07CE0E3CBDF8A3766FA9FBC0D9A573DA994C642C2)

根据worker.onerror日志排查，确认是否同时存在以下情况：

* 在onDestroy生命周期中销毁三方SDK。
* 三方SDK被销毁后，仍继续向Worker线程发送消息。
* Worker线程在处理消息过程中仍继续调用已销毁的三方SDK，且未进行异常处理。

在秒级启动场景下，如果用户重新启动游戏后又上滑移除游戏App，游戏进程不会主动销毁Worker线程和团结引擎。当上述三种情况同时发生时，可能导致Worker线程崩溃，并在日志中频繁打印如下错误信息：

```
1. BusinessError: The Worker instance is not running, maybe worker is terminated when PostMessage
```
