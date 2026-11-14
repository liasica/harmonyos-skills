---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/iap-apply-for-open-capabilities
title: （可选）申请嵌入式收银台开放能力权限
breadcrumb: 指南 > 应用服务 > IAP Kit（应用内支付服务） > 开发准备 > 基本准备工作 > （可选）申请嵌入式收银台开放能力权限
category: harmonyos-guides
scraped_at: 2026-11-14T08:48:21+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:2f8799c5f02ee88de46339890c23079e47a9d567ca71e8613dc00afc3bb4ffd2
---

如果需要接入[CashierComponent(iap嵌入式收银台组件)](../harmonyos-references/iap-cashier-component.md)，则需要申请对应权限。

## 开放能力申请准备

请先参考[应用开发准备](application-dev-overview.md)完成基本准备工作，再继续以下开放能力准备项。

### 嵌入式收银台

为了提升用户体验，系统对嵌入式收银台服务进行了权限保护。开发者在调用相关接口前，需要先提交“嵌入式收银台”能力开关的申请。只有在申请通过后，才能使用该功能。

1. 登录[HarmonyOS 开发者中心](https://developer.huawei.com/consumer/cn/hdc-console)，选择“开发者管理”。
2. 选择“ID、证书和Profile > APP ID”，在“选择应用”下拉框中选择需要申请嵌入式收银台功能的应用。
3. 进入“开放能力管理”页签，点击“开放能力申请”，找到“应用内购买服务”，点击“嵌入式收银台”对应的“申请”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fe/v3/Dvu6z7-3RgaHkyZyqvf3dQ/zh-cn_image_0000002817507483.png?HW-CC-KV=V1&HW-CC-Date=20261114T004821Z&HW-CC-Expire=31536000000&HW-CC-Sign=4A335F6A655EFF93A5D5F97C134C2BEAE7C1E8A97320BB520E7094E23A652400)
4. 参考“申请原因”中的模板，提供申请必需的相关信息，包括应用介绍、使用场景，然后点击“提交”按钮。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ac/v3/9mtS7szxQVypvfmPM56QtA/zh-cn_image_0000002788308052.png?HW-CC-KV=V1&HW-CC-Date=20261114T004821Z&HW-CC-Expire=31536000000&HW-CC-Sign=8C41FD025EF69E18842178FAD042E3657710D0734E6F94FC3C7D55630B382CA5)

   返回“开放能力管理”页面，原“申请”变为“申请中”，5个工作日内反馈申请结果，请留意互动中心的“服务开通申请”信息。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3e/v3/R0rNAGVGRQG4b6CT7YGp0A/zh-cn_image_0000002817427415.png?HW-CC-KV=V1&HW-CC-Date=20261114T004821Z&HW-CC-Expire=31536000000&HW-CC-Sign=72EAEE205757435EC1BAC1ED3253D40197D7529D5E21C7F03DBFFC0197FF1108)

   申请通过后，互动中心会发送通知给开发者，同时“申请中”会变为置灰显示的“申请”，至此，应用已成功开启嵌入式收银台开放能力。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/93/v3/quRVKBabSLiJYMoeyKf3AQ/zh-cn_image_0000002788467996.png?HW-CC-KV=V1&HW-CC-Date=20261114T004821Z&HW-CC-Expire=31536000000&HW-CC-Sign=64B80233A3218196B6D7080B41EC52F4A8B7D315758ED3A53C79B711B0D75F0C)
