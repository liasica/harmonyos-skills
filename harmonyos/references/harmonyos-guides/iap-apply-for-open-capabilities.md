---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/iap-apply-for-open-capabilities
title: （可选）申请嵌入式收银台开放能力权限
breadcrumb: 指南 > 应用服务 > IAP Kit（应用内支付服务） > 开发准备 > 基本准备工作 > （可选）申请嵌入式收银台开放能力权限
category: harmonyos-guides
scraped_at: 2026-11-21T09:12:28+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:0f171a3dcc0d428e3ab6ec5c49f8f21fcd59b63494434dc1a2796846965d09a7
---

如果需要接入[CashierComponent(iap嵌入式收银台组件)](../harmonyos-references/iap-cashier-component.md)，则需要申请对应权限。

## 开放能力申请准备

请先参考[应用开发准备](application-dev-overview.md)完成基本准备工作，再继续以下开放能力准备项。

### 嵌入式收银台

为了提升用户体验，系统对嵌入式收银台服务进行了权限保护。开发者在调用相关接口前，需要先提交“嵌入式收银台”能力开关的申请。只有在申请通过后，才能使用该功能。

1. 登录[HarmonyOS 开发者中心](https://developer.huawei.com/consumer/cn/hdc-console)，选择“开发者管理”。
2. 选择“ID、证书和Profile > APP ID”，在“选择应用”下拉框中选择需要申请嵌入式收银台功能的应用。
3. 进入“开放能力管理”页签，点击“开放能力申请”，找到“应用内购买服务”，点击“嵌入式收银台”对应的“申请”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/91/v3/WDG56fwiQeaC2Tn-soVscg/zh-cn_image_0000002793038004.png?HW-CC-KV=V1&HW-CC-Date=20261121T011227Z&HW-CC-Expire=31536000000&HW-CC-Sign=A4C70D41EF526ABAAA1E9EB4B015EAF26EA8576F147E5F4A8B2D65E057122465)
4. 参考“申请原因”中的模板，提供申请必需的相关信息，包括应用介绍、使用场景，然后点击“提交”按钮。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6d/v3/K7wAGOXORMeUGwk_iT5LjQ/zh-cn_image_0000002792878034.png?HW-CC-KV=V1&HW-CC-Date=20261121T011227Z&HW-CC-Expire=31536000000&HW-CC-Sign=7406F8B9D76474F544DDD40D51B0C789213287938B025446C2516014104C443A)

   返回“开放能力管理”页面，原“申请”变为“申请中”，5个工作日内反馈申请结果，请留意互动中心的“服务开通申请”信息。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/10/v3/pt-ViMrMRdmp0ro7E6wF2w/zh-cn_image_0000002821837941.png?HW-CC-KV=V1&HW-CC-Date=20261121T011227Z&HW-CC-Expire=31536000000&HW-CC-Sign=36C3259DC48354935CE1E731809615E50F0FC08905B49D9EC41DC0FA46313694)

   申请通过后，互动中心会发送通知给开发者，同时“申请中”会变为置灰显示的“申请”，至此，应用已成功开启嵌入式收银台开放能力。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c0/v3/nGzkb4mNRZiP3B311pwDFA/zh-cn_image_0000002821757943.png?HW-CC-KV=V1&HW-CC-Date=20261121T011227Z&HW-CC-Expire=31536000000&HW-CC-Sign=CA97E8697C29B091694D01C0B1595775558FDB0309535254F259FFAB8279A638)
