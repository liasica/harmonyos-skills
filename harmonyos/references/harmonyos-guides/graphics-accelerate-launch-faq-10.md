---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/graphics-accelerate-launch-faq-10
title: 游戏接入秒级启动后无法热更应该如何处理？
breadcrumb: 指南 > 图形 > Graphics Accelerate Kit（图形加速服务） > Graphics Accelerate Kit常见问题 > 游戏启动加速服务 > 游戏接入秒级启动后无法热更应该如何处理？
category: harmonyos-guides
scraped_at: 2026-04-28T07:47:50+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:47ebba634269ad0b19f376210b5591b033ddbd130be57521b32d426ddfae98a0
---

**问题原因**：秒级启动是基于游戏上次退出的状态下进行的镜像恢复，因此往往会跳过游戏引擎启动过程中的一些场景，例如游戏资源加载和游戏资源更新环节。

**解决方案**：可类比游戏长时间挂后台，再切回前台场景。

1. 若游戏存在游戏内热更检测逻辑，可在游戏中特定事件或定期检测远端热更资源更新，若存在更新则弹出模态窗口提示用户有热更资源，强制玩家退出。
2. 秒级启动会创建新的[UIAbility](uiability.md)，其生命周期也会全量执行，开发者可在[onCreate](../harmonyos-references/js-apis-app-ability-uiability.md#oncreate)或者其它生命周期阶段执行资源更新检测逻辑，当检测到存在热更新资源时，可主动取消秒级启动流程。玩家当次退出后，系统不再制作内存镜像，游戏下一次启动将以冷启动方式运行，从而执行完整的资源更新流程。
