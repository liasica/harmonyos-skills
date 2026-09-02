---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/intents-skill-all-rec-decorator-overview
title: 方案概述
breadcrumb: 指南 > AI > Intents Kit（意图框架服务） > 技能调用方案 > 接入方案 > 任务执行类场景方案（装饰器接入方式） > 方案概述
category: harmonyos-guides
scraped_at: 2026-09-02T15:00:14+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:7da71d48283f5e00e82da18347f8117b424dc907d27cf7c29a630c2568c8a9f0
---

从6.0.0(20)开始，支持通过装饰器开发意图，支持将现有功能通过装饰器快速集成至系统入口。开发者可自定义意图，通过添加装饰器方式实现意图快速接入，支持Link跳转、Page和函数等意图装饰器，方便开发者快速开放应用内功能。

**说明** 

自定义意图的触发语料要求必须包含所属应用/元服务的名称。以“XX商城”应用开发“打开购物车”的自定义意图为例，用户触发语料需包含“XX商城”，示例：打开XX商城的购物车。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/12/v3/xv0-f6fzQ0OZ-qVApl-fBg/zh-cn_image_0000002706675450.png)

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
