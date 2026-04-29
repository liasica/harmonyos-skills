---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/start-intent-panel
title: 拉起指定类型的应用概述
breadcrumb: 指南 > 应用框架 > Ability Kit（程序框架服务） > Stage模型开发指导 > 应用间跳转 > 拉起指定类型的应用 > 拉起指定类型的应用概述
category: harmonyos-guides
scraped_at: 2026-04-29T13:25:51+08:00
doc_updated_at: 2026-03-27
content_hash: sha256:de23142729120e67d331f47a0a55811de74a24acc43ee13d0cbb93f6d919e067
---

本章节主要介绍拉起方应用如何通过指定应用类型、而非某个具体的应用，来实现应用跳转。通常有以下几种方式：

* [通过startAbilityByType接口拉起垂类应用选择框](start-intent-panel.md#通过startabilitybytype接口拉起垂类应用选择框)：调用startAbilityByType接口拉起对应的垂类应用选择框（目前支持拉起导航、金融、邮件、航班、快递类应用）。选择框中将展示已接入的垂类应用，由用户选择打开指定的目标应用。
* [通过mailto方式跳转电子邮件应用](start-intent-panel.md#通过mailto方式跳转电子邮件应用)：通过mailto电子邮件协议，可以创建指向电子邮件地址的超链接，方便用户通过网页或应用中的超链接直接跳转电子邮件应用。
* [通过startAbility接口打开文件](start-intent-panel.md#通过startability接口打开文件)：开发者可以通过调用startAbility接口，由系统从已安装的应用中寻找符合要求的应用，打开特定类型的文件。

## 通过startAbilityByType接口拉起垂类应用选择框

### 实现机制

开发者可通过特定的业务类型如导航、金融、邮件等，调用startAbilityByType接口拉起对应的垂类应用选择框。

* 如果当前设备已安装应用中存在匹配的应用，选择框中将展示已接入的垂类应用，由用户选择打开指定应用以实现相应的意图。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4/v3/f5ythv5AR9a7P9hmH7sfnA/zh-cn_image_0000002589243801.png?HW-CC-KV=V1&HW-CC-Date=20260429T052550Z&HW-CC-Expire=86400&HW-CC-Sign=E98AC42EF4E2C226C24C7AC5650DF6367E73F420E8BD72E52768ECC367F6CE65)
* 如果当前设备已安装应用中没有匹配的应用，系统将自动弹窗提示用户没有相关应用（下图以导航类应用匹配失败为例）。无需开发者适配。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b/v3/6bVusHyHTpyfg7tIylWShg/zh-cn_image_0000002558763996.png?HW-CC-KV=V1&HW-CC-Date=20260429T052550Z&HW-CC-Expire=86400&HW-CC-Sign=B2305AB475482E1F798C324D47F645F41C558C5A9C3DC776BCA5277114DC5CB2)

这种方式可以为调用方提供统一的安全、可信的目标方应用，同时降低调用方的接入成本。

### 匹配规则

[UIAbilityContext.startAbilityByType](../harmonyos-references/js-apis-inner-application-uiabilitycontext.md#startabilitybytype11)和[UIExtensionContentSession.startAbilityByType](../harmonyos-references/js-apis-app-ability-uiextensioncontentsession.md#startabilitybytype11)接口支持基于业务类型拉起垂类应用选择框。调用方通过指定业务类型即可拉起对应的垂类应用选择框。选择框上将展示已接入的垂类应用。

系统会根据调用方在startAbilityByType接口传入的type与wantParams.sceneType取值，按照如下映射关系，匹配到在module.json5配置文件中声明了对应[linkFeature](module-configuration-file.md#skills标签)的目标应用。

| 支持的功能 | 调用方（startAbilityByType接口入参） | 目标方（配置文件linkFeature取值） |
| --- | --- | --- |
| 路线规划功能 | - type：navigation  - wantParams.sceneType：1 | RoutePlan |
| 导航功能 | - type：navigation  - wantParams.sceneType：2 | Navigation |
| 位置搜索功能 | - type：navigation  - wantParams.sceneType：3 | PlaceSearch |
| 转账汇款功能 | - type：finance  - wantParams.sceneType：1 | Transfer |
| 信用卡还款功能 | - type：finance  - wantParams.sceneType：2 | CreditCardRepayment |
| 撰写邮件功能 | - type：mail  - wantParams.sceneType：1 | ComposeMail |
| 按航班号查询航班功能 | - type：flight  - wantParams.sceneType：1 | QueryByFlightNo |
| 按起降地查询航班功能 | - type：flight  - wantParams.sceneType：2 | QueryByLocation |
| 快递查询功能 | - type：express  - wantParams.sceneType：1 | QueryExpress |

## 通过mailto方式跳转电子邮件应用

通过mailto电子邮件协议，可以创建指向电子邮件地址的超链接，方便用户通过网页或应用中的超链接直接跳转电子邮件应用。详见[拉起邮件类应用（mailto方式）](start-email-apps-by-mailto.md)。

## 通过startAbility接口打开文件

开发者可以通过调用startAbility接口，由系统从已安装的应用中寻找符合要求的应用，打开特定类型的文件。详见[拉起文件处理类应用](file-processing-apps-startup.md)。
