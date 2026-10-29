---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/push-message-analysis
title: （可选）测试消息分析
breadcrumb: 指南 > 应用服务 > Push Kit（推送服务） > 端云调试 > （可选）测试消息分析
category: harmonyos-guides
scraped_at: 2026-10-29T07:57:48+08:00
doc_updated_at: 2026-10-28
content_hash: sha256:ad27358379db0d5b09f546deff8e1a565ab7e638ab230d00201ef7c3c0b25a9f
---

## 场景介绍

测试消息分析是Push Kit提供的消息追踪能力，用于帮助开发者查询接入Push Kit过程中测试消息（即testMessage=true的消息）的发送情况。

应用服务端调用REST API推送消息时，返回业务响应码80000000，消息发送成功，但设备没有收到消息。

对此，Push Kit提供了测试消息分析功能，开发者只需输入推送请求唯一标识“requestId”和“token”，即可查询测试消息的历程以及消息简述。

**说明** 

针对非测试消息的场景，请登录[HarmonyOS 开发者中心](https://developer.huawei.com/consumer/cn/hdc-console/index.html#/home/)，选择“推送服务 > 更多 > 自助分析（Beta） ”页签进入自助分析功能页面进行查询。

## 约束与限制

* 本页面仅支持查询HarmonyOS Next/5.x及之后版本的测试消息（即testMessage=true的消息）。
* requestId有效期为三天，超过有效期将无法查询。
* 使用前请确保当前页面已选择正确的项目，token对应的应用属于所选项目。

## 操作步骤

1. 登录[HarmonyOS 开发者中心](https://developer.huawei.com/consumer/cn/hdc-console/index.html#/home/)网站，点击“应用管理”，在项目列表中找到您的项目，通过“推广运营 > 增长运营 > 推送服务 > 测试消息分析（Beta）”页签进入测试消息分析页面。
2. 消息追踪，输入调用REST API推送消息时返回的“requestId”和“token”，点击“查询”即可查看消息发送情况。

   **说明** 

   “requestId”是应用服务端调用REST API推送消息时返回的[消息响应参数](../harmonyos-references/push-scenariozed-api-response.md)。
3. 查询结果，点击“查询”后即可返回测试消息的发送情况，包含消息历程以及消息简述。

   消息历程各字段含义如下：

   * 时间：当前消息状态的时间，格式为“YYYY-MM-DD HH:mm:ss”。
   * 状态简述：消息当前所处状态的简要描述，如“测试消息发送过多，消息被频控”等。
   * 详细描述：对当前状态的进一步说明，包括失败原因和解决建议，用于帮助开发者排查定位和解决问题。

   消息简述各字段含义如下：

   * 发送时间：应用服务端调用REST API推送测试消息请求的时间。
   * 过期时间：测试消息的有效期截止时间，超过该时间消息将不再下发或展示。
   * 消息类型：测试消息的分类标识，用于区分不同的推送场景，例如Alert消息(pushType:0)。
   * 应用包名：使用的应用包名。

   仅当消息类型为通知消息或语音播报消息的时候，消息简述中存在这两个字段：

   * 发送category：开发者调用REST API发送通知消息或语音播报消息时，在请求体中传入的category参数值，用于标识消息的业务分类。
   * 实际下发category：消息下发时真正生效的category值。该值可能与发送时指定的category不同，参考[典型场景](push-message-analysis.md#典型场景)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5c/v3/qJ1B59kLQLm0gwWj9AvGtg/zh-cn_image_0000002803265331.png)

## 典型场景

若应用未开通推送场景化消息权益，或开通的权益类型与调用REST API时请求体中category字段值不一致，消息将会默认归为资讯营销类消息（category实际取值为MARKETING）。资讯营销类消息受频控限制，单个应用每日每设备推送数量上限为2条或5条。超出频控后，设备将无法收到消息。

因此，当您的请求体中需要使用某个category值时，请提前确认该category对应的权益已开通。如未开通，请前往申请对应[推送场景化消息权益](push-apply-right.md#申请通知消息自分类权益)。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0e/v3/yBUiYKR6QP2NDjQQKTY8Ew/zh-cn_image_0000002803225239.png)
