---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/iap-apply-for-open-capabilities
title: （可选）申请嵌入式收银台开放能力权限
breadcrumb: 指南 > 应用服务 > IAP Kit（应用内支付服务） > 开发准备 > 基本准备工作 > （可选）申请嵌入式收银台开放能力权限
category: harmonyos-guides
scraped_at: 2026-10-22T07:05:49+08:00
doc_updated_at: 2026-09-09
content_hash: sha256:0f53e40773d62bf45b891c38d8fbb0e686a50bde5a18e234d372a846796f7a12
---

如果需要接入[CashierComponent(iap嵌入式收银台组件)](../harmonyos-references/iap-cashier-component.md)，则需要申请对应权限。

## 开放能力申请准备

请先参考[应用开发准备](application-dev-overview.md)完成基本准备工作，再继续以下开放能力准备项。

### 嵌入式收银台

为了提升用户体验，系统对嵌入式收银台服务进行了权限保护。开发者在调用相关接口前，需要先提交“嵌入式收银台”能力开关的申请。只有在申请通过后，才能使用该功能。

1. 登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)，选择“开发与服务”。
2. 在项目列表选择项目，并在应用列表下选择需要申请嵌入式收银台功能的应用。
3. 进入“项目设置 > 开放能力管理”页面，选择能力名称为应用内购买服务（HarmonyOS NEXT），然后点击“嵌入式收银台”对应的“申请”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/61/v3/1xa2GZ-PRqmF9QKkm8CkGw/zh-cn_image_0000002768021418.png)
4. 参考“申请原因”中的模板，提供申请必需的相关信息，包括应用介绍、使用场景，然后点击“提交”按钮。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f6/v3/SJF5lInrSV2HiwOiQhQuNA/zh-cn_image_0000002797301367.png)

   返回“开放能力管理”页面，原“申请”变为“申请中”，1~5个工作日内反馈申请结果，请留意互动中心的“服务开通申请”信息。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d8/v3/x65bOZtORROHzA2XI82IvQ/zh-cn_image_0000002767861436.png)

   申请通过后，互动中心会发送通知给开发者，同时“申请中”会变为置灰显示的“申请”，至此，应用已成功开启嵌入式收银台开放能力。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f8/v3/HeGIv8z5RsCxGF-zIHGUJw/zh-cn_image_0000002797181399.png)
