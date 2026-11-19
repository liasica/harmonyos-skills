---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/iap-apply-for-open-capabilities
title: （可选）申请嵌入式收银台开放能力权限
breadcrumb: 指南 > 应用服务 > IAP Kit（应用内支付服务） > 开发准备 > 基本准备工作 > （可选）申请嵌入式收银台开放能力权限
category: harmonyos-guides
scraped_at: 2026-11-19T09:49:02+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:e4aa5774854f0da472e30a150b803896b27bf2200f7d39b1f90edf9a8555b377
---

如果需要接入[CashierComponent(iap嵌入式收银台组件)](../harmonyos-references/iap-cashier-component.md)，则需要申请对应权限。

## 开放能力申请准备

请先参考[应用开发准备](application-dev-overview.md)完成基本准备工作，再继续以下开放能力准备项。

### 嵌入式收银台

为了提升用户体验，系统对嵌入式收银台服务进行了权限保护。开发者在调用相关接口前，需要先提交“嵌入式收银台”能力开关的申请。只有在申请通过后，才能使用该功能。

1. 登录[HarmonyOS 开发者中心](https://developer.huawei.com/consumer/cn/hdc-console)，选择“开发者管理”。
2. 选择“ID、证书和Profile > APP ID”，在“选择应用”下拉框中选择需要申请嵌入式收银台功能的应用。
3. 进入“开放能力管理”页签，点击“开放能力申请”，找到“应用内购买服务”，点击“嵌入式收银台”对应的“申请”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a8/v3/39bNGdEKR0msHo7YoBuhqQ/zh-cn_image_0000002820526333.png?HW-CC-KV=V1&HW-CC-Date=20261119T014902Z&HW-CC-Expire=31536000000&HW-CC-Sign=86AA2B7A9D5745E66580CAAF56A36A433EDA8AA804D23EF2B44563344A366A20)
4. 参考“申请原因”中的模板，提供申请必需的相关信息，包括应用介绍、使用场景，然后点击“提交”按钮。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a3/v3/HlAPZ7hLQ_-cuVkyVjeHLQ/zh-cn_image_0000002820406333.png?HW-CC-KV=V1&HW-CC-Date=20261119T014902Z&HW-CC-Expire=31536000000&HW-CC-Sign=128167F2BEF29613E5AF6A98FA4B9D316DEE07C7C0AB0C406CDD0CB827952B81)

   返回“开放能力管理”页面，原“申请”变为“申请中”，5个工作日内反馈申请结果，请留意互动中心的“服务开通申请”信息。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0f/v3/xTRElsieQi6mTBfLzgrSeQ/zh-cn_image_0000002791726354.png?HW-CC-KV=V1&HW-CC-Date=20261119T014902Z&HW-CC-Expire=31536000000&HW-CC-Sign=00EC797848B2C674D7F36DD70E927ABD66A04D136E18C23F244433F3960E4D06)

   申请通过后，互动中心会发送通知给开发者，同时“申请中”会变为置灰显示的“申请”，至此，应用已成功开启嵌入式收银台开放能力。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b0/v3/iCnog_E0Qu-asJLAeCgA1g/zh-cn_image_0000002791566382.png?HW-CC-KV=V1&HW-CC-Date=20261119T014902Z&HW-CC-Expire=31536000000&HW-CC-Sign=AE05CC16A9CDF975DF554179CBDD94ECAEF11A10432294E80DD8B31566D4F4C3)
