---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/graphics-accelerate-launch-faq-3
title: 快速启动的游戏存在三方SDK功能异常，应该如何排查？
breadcrumb: 指南 > 图形 > Graphics Accelerate Kit（图形加速服务） > Graphics Accelerate Kit常见问题 > 游戏启动加速服务 > 快速启动的游戏存在三方SDK功能异常，应该如何排查？
category: harmonyos-guides
scraped_at: 2026-04-28T07:47:49+08:00
doc_updated_at: 2026-03-17
content_hash: sha256:184a4a1d8599f6a1e32f5f484d811c32baa528748e436db2ab86b79ff9a1741b
---

在秒级启动使能后，如果用户对游戏进行上滑移除操作，系统会对游戏进程进行深度冻结和内存换出。此时游戏进程、[ArkTS Runtime](arkts-runtime-overview.md)、[AbilityStage](../harmonyos-references/js-apis-app-ability-abilitystage.md)均不会被销毁，只有[UIAbility](uiability.md)会经历完整的创建到销毁生命周期。因此，由ArkTS定义的全局变量、静态变量、[AppStorage](arkts-appstorage.md)变量、globalThis变量以及单例对象等都不会被销毁或重置。

三方SDK的生命周期通常与进程生命周期保持一致。当进程未被销毁时，已创建的SDK实例会一直保留在内存中。如果在下一次秒级启动时再次执行SDK初始化逻辑，可能会因重复创建SDK实例而导致功能异常。因此，建议开发者在应用侧维护SDK初始化状态标识（例如全局状态变量或单例状态），用于记录SDK是否已经完成初始化。在应用启动或Ability创建时，先判断SDK是否已初始化，若未初始化则执行初始化；若已初始化则复用已有实例，避免重复创建。

通过这种方式，可以确保在秒级启动场景下SDK初始化逻辑只执行一次，从而避免因重复初始化导致的异常问题。
