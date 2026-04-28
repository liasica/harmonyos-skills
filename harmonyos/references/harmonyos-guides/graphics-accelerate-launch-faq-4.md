---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/graphics-accelerate-launch-faq-4
title: 游戏调用UnityEngine.Application.Quit侧滑退出时出现黑屏现象，应该如何避免？
breadcrumb: 指南 > 图形 > Graphics Accelerate Kit（图形加速服务） > Graphics Accelerate Kit常见问题 > 游戏启动加速服务 > 游戏调用UnityEngine.Application.Quit侧滑退出时出现黑屏现象，应该如何避免？
category: harmonyos-guides
scraped_at: 2026-04-28T07:47:49+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:574788f270c296451c84047c3b8570a42f45615fb021ea5710f8a9ce9b81903d
---

需根据“退出后是否希望继续使用**秒级启动**能力”选择不同的退出策略：

1. **希望下次启动仍支持秒级启动**

   在侧滑退出场景下，应调用[terminateSelf](../harmonyos-references/js-apis-inner-application-uiabilitycontext.md#terminateself)实现退出，确保进程状态可被系统正确保留，避免出现黑屏问题。
2. **不希望下次启动使用秒级启动**

   在侧滑退出场景下，应调用[killAllProcesses](../harmonyos-references/js-apis-inner-application-applicationcontext.md#applicationcontextkillallprocesses)实现强制退出，彻底清理进程，避免残留状态引发异常。
