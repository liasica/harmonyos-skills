---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ability-startup-with-explicit-want
title: 使用显式Want启动应用组件
breadcrumb: 指南 > 应用框架 > Ability Kit（程序框架服务） > Stage模型开发指导 > Stage模型应用组件 > 信息传递载体Want > 使用显式Want启动应用组件
category: harmonyos-guides
scraped_at: 2026-04-28T07:37:45+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:1740b20415bec095c6b092f8b4140f67572b92e5a7ce4d8b2ac67caf2b67b59e
---

在应用使用场景中，当用户在应用内点击某个按钮时，经常需要拉起指定UIAbility组件来完成某些特定任务。在启动UIAbility时，指定了abilityName和bundleName参数，可以使用显式Want方式启动UIAbility。

针对应用的特定任务，用户需要通过点击应用内的按钮来启动指定的UIAbility组件。在启动UIAbility时，需要提供abilityName和bundleName参数，并使用显式Want方式来启动。关于如何使用显式Want方式启动应用内的UIAbility，请参见[启动应用内的UIAbility](uiability-intra-device-interaction.md)。
