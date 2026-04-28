---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/intents-skill-all-rec-decorator-overview
title: 方案概述
category: harmonyos-guides
scraped_at: 2026-04-28T07:53:39+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:8d492abb811157c2b831ee9e83ef63feeec8ac6e59b4a91d151e559925f0fbb9
---

从6.0.0(20)开始，支持通过装饰器开发意图，支持将现有功能通过装饰器快速集成至系统入口。开发者可自定义意图，通过添加装饰器方式实现意图快速接入，支持Link跳转、Page和函数等意图装饰器，方便开发者快速开放应用内功能。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0a/v3/IURFWL3PR-yXdGM8k61yTQ/zh-cn_image_0000002583439365.png?HW-CC-KV=V1&HW-CC-Date=20260427T235336Z&HW-CC-Expire=86400&HW-CC-Sign=3536577E350477C050AF918F9F382C61792A557416244BBA1155644B56AB3019)

开发者可根据想要暴露的应用功能，选择不同类型的装饰器进行意图声明：

* [基于Link的装饰器：@InsightIntentLink](intents-skill-all-rec-decorator-link.md)

  在开发者已实现的DeepLink，AppLink上添加装饰器，实现功能页面的拉起。

  约束：仅支持前台执行。
* [基于Page的装饰器：@InsightIntentPage](intents-skill-all-rec-decorator-page.md)

  在开发者已实现的Page上添加装饰器，实现功能页面的拉起。

  约束：仅支持前台执行，仅支持Navigation架构。
* [基于函数的装饰器：@InsightIntentFunction和@InsightIntentFunctionMethod](intents-skill-all-rec-decorator-function.md)

  在目标执行函数上添加@InsightIntentFunctionMethod装饰器，以及在目标执行函数所属Class上添加@InsightIntentFunction进行意图声明，实现目标函数的执行。

  约束：仅支持后台执行。
