---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/graphics-accelerate-launch-faq-5
title: "日志中频繁打印BusinessError: The Worker instance is not running, maybe worker is terminated when PostMessage错误信息，应该如何排查"
breadcrumb: "指南 > 图形 > Graphics Accelerate Kit（图形加速服务） > Graphics Accelerate Kit常见问题 > 游戏启动加速服务 > 日志中频繁打印BusinessError: The Worker instance is not running, maybe worker is terminated when PostMessage错误信息，应该如何排查"
category: harmonyos-guides
scraped_at: 2026-11-19T09:48:48+08:00
doc_updated_at: 2026-05-08
content_hash: sha256:2b22cf51ace99d0e34a2e274c95c7c5142b7058e5e06b079235ed162c52ea95d
---

该错误通常是由于Worker线程崩溃或被终止导致。

开发者可在日志中进一步查找worker.onerror相关日志，确认Worker线程崩溃时的具体异常信息。

```typescript
TuanjieMainWorker Error TypeError: undefined is not callable entry|entry|1.0.0|src/main/ets/workers/TuanjieMainWorkerHandler.ts
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1c/v3/lIqSOLZ7TbaTclNr7HXncQ/zh-cn_image_0000002820526133.png?HW-CC-KV=V1&HW-CC-Date=20261119T014755Z&HW-CC-Expire=31536000000&HW-CC-Sign=03A2B332291B61BB8EDF12195C970AA6E90CFD63BA2D1C0BC56372761A2B832B)

根据worker.onerror日志排查，确认是否同时存在以下情况：

* 在onDestroy生命周期中销毁三方SDK。
* 三方SDK被销毁后，仍继续向Worker线程发送消息。
* Worker线程在处理消息过程中仍继续调用已销毁的三方SDK，且未进行异常处理。

在秒级启动场景下，如果用户重新启动游戏后又上滑移除游戏App，游戏进程不会主动销毁Worker线程和团结引擎。当上述三种情况同时发生时，可能导致Worker线程崩溃，并在日志中频繁打印如下错误信息：

```typescript
BusinessError: The Worker instance is not running, maybe worker is terminated when PostMessage
```
