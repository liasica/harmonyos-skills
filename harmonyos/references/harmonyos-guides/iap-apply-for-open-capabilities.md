---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/iap-apply-for-open-capabilities
title: （可选）申请嵌入式收银台开放能力权限
breadcrumb: 指南 > 应用服务 > IAP Kit（应用内支付服务） > 开发准备 > 基本准备工作 > （可选）申请嵌入式收银台开放能力权限
category: harmonyos-guides
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:5203d507f628bdc5827d771f0c8075283bb923794a6571bfd48a3945654021f4
---

如果需要接入[CashierComponent(iap嵌入式收银台组件)](../harmonyos-references/iap-cashier-component.md)，则需要申请对应权限。

## 开放能力申请准备

请先参考[应用开发准备](application-dev-overview.md)完成基本准备工作，再继续以下开放能力准备项。

### 嵌入式收银台

为了提升用户体验，系统对嵌入式收银台服务进行了权限保护。开发者在调用相关接口前，需要先提交“嵌入式收银台”能力开关的申请。只有在申请通过后，才能使用该功能。

1. 登录[HarmonyOS 开发者中心](https://developer.huawei.com/consumer/cn/hdc-console)，选择“开发者管理”。
2. 选择“ID、证书和Profile > APP ID”，在“选择应用”下拉框中选择需要申请嵌入式收银台功能的应用。
3. 进入“开放能力管理”页签，点击“开放能力申请”，找到“应用内购买服务”，点击“嵌入式收银台”对应的“申请”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1c/v3/CzeKnembRWSw1wg4LNibeA/zh-cn_image_0000002815399823.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=A5F865EC5192E95C210BB44B07DC7E17F139A7A5123556B8CACEEAB2898A26E0)
4. 参考“申请原因”中的模板，提供申请必需的相关信息，包括应用介绍、使用场景，然后点击“提交”按钮。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/3pIQh0aeQVmTTkihr2U9Fg/zh-cn_image_0000002786520248.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=634D1A2B6F7A88F020AC9BAC7E5C042AE5F3DD94CD3DA063A3D0F0F7F26A5D96)

   返回“开放能力管理”页面，原“申请”变为“申请中”，5个工作日内反馈申请结果，请留意互动中心的“服务开通申请”信息。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c8/v3/gA_337QySVidBLxuk_d5Cg/zh-cn_image_0000002786360320.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=3A6D410E4960A30BA7C64D80B30475C676691B5A4077E47B07F436ECCF9AAE50)

   申请通过后，互动中心会发送通知给开发者，同时“申请中”会变为置灰显示的“申请”，至此，应用已成功开启嵌入式收银台开放能力。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e8/v3/E6kkk1TpQKyUuLLIoIkGLA/zh-cn_image_0000002815559741.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=13E336787F2ACBA8C0D5D1197FD4569096159AFBACDE88A902E8C1C01AF29D9D)
