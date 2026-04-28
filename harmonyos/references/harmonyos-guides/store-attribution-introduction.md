---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/store-attribution-introduction
title: 开发概述
breadcrumb: 指南 > 应用服务 > AppGallery Kit（应用市场服务） > 应用归因服务 > 开发概述
category: harmonyos-guides
scraped_at: 2026-04-28T07:48:18+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:02e1180ea543554e49d19ac77380ebfb95854e4c9dda547b1c66b7112a558245
---

应用归因服务是华为提供的不依赖用户标识符的端侧归因能力。

当用户完成应用安装或在已安装应用内完成转化时，应用归因服务通过匹配用户在转化前的行为数据，分析用户的来源渠道以及转化的原因，并将归因结果回传给分发平台、开发者、归因监测平台。开发者可以通过归因结果数据分析投放效果、评估渠道质量，进而优化投放策略，分发平台可以评估渠道商业价值，优化营销效果。

## 业务流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ae/v3/mDYKdpHtRgqwKSu9kE4whQ/zh-cn_image_0000002552799132.jpg?HW-CC-KV=V1&HW-CC-Date=20260427T234817Z&HW-CC-Expire=86400&HW-CC-Sign=CBD593CF68A265263E448B6393224FA03BF2825A312DAAC8862760EA1F7C904E)

业务流程中各任务描述如下：

| 序号 | 任务 | 详情 |
| --- | --- | --- |
| 1 | [注册归因角色](store-attribution-register.md#注册归因角色) | 应用生态伙伴通过应用归因服务云侧注册归因角色并完成其信息的配置，包括：名称、回传地址（用于接收归因结果回传的URL）、公钥。注册成功后平台生成归因角色ID。应用生态伙伴指：开发者、分发平台、归因监测平台。 |
| 2 | [登记归因来源](store-attribution-developmentguide.md#登记归因来源) | 媒体App、分发平台通过调用[registerSource](../harmonyos-references/store-attributionmanager.md#attributionmanagerregistersource)接口登记归因来源（曝光/点击）。 |
| 3 | [登记归因转化](store-attribution-developmentguide.md#登记归因转化) | 开发者App、归因监测平台通过调用[registerTrigger](../harmonyos-references/store-attributionmanager.md#attributionmanagerregistertrigger)接口登记归因转化事件。 |
| 4 | [归因结果回传](store-attribution-receive.md) | 应用归因服务将归因结果通过回传地址回传至应用生态伙伴。 |
| 5 | [接入调试](store-attribution-test.md) | 应用归因服务提供接入调试功能，开发者通过调用调试接口验证接入的准确性及归因结果回传等基础能力。 |

## 约束与限制

* 应用需要在应用市场上架。
* 接入应用归因服务的所有开发者应严格遵循法律法规、已签署的协议条款和开发者文档的要求处理用户的个人信息。
* 禁止通过应用归因服务上报、透传个人信息。
* 应用归因服务接入调试功能接口当前支持ARM版本、X86版本的模拟器。
* 应用归因服务支持Phone、Tablet设备。并且从6.1.0(23)版本开始，新增支持PC/2in1、TV设备。
