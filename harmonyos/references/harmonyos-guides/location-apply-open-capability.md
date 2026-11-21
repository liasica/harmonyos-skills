---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/location-apply-open-capability
title: 申请开放能力权限指导
breadcrumb: 指南 > 应用服务 > Location Kit（位置服务） > 开发准备 > 申请开放能力权限指导
category: harmonyos-guides
scraped_at: 2026-11-21T09:12:30+08:00
doc_updated_at: 2026-09-23
content_hash: sha256:3eefbf5e627c2b29c3fb7216e95d0e892ae6fcc997d52b200c6e3568506b3a92
---

## 开放能力申请准备

请先参考[应用开发准备](application-dev-overview.md)完成基本准备工作，再继续以下开放能力准备项。

### 室内高精度定位

为了更好的用户体验，系统侧对室内高精度定位服务功能做了权限保护处理，使用相关接口开发者需先提交“室内高精度定位”能力开关的申请，请在申请通过后，再使用该能力。

室内高精度定位仅支持商场、高铁站、机场和医院等场所，支持的建筑列表如下。

[支持室内定位建筑列表](https://openlocation-portal-drcn.partner.petalmaps.com/indoormap/index.html#/homePage)

在这些建筑中支持楼层识别，定位精度约10~20米左右。

未开通室内高精度定位服务时Location Kit仍然支持在室内场景进行网络定位获取定位结果。

1. 登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)，选择“开发与服务”。
2. 在项目列表选择项目，并在应用列表下选择需要申请室内高精度定位功能的应用。
3. 进入“项目设置 > 开放能力管理”页面，选择能力名称为定位服务（HarmonyOS NEXT），然后点击“室内高精度定位”对应的“申请”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d7/v3/Gvigb5t5TuK-SAX9TiRYIQ/zh-cn_image_0000002821838011.png?HW-CC-KV=V1&HW-CC-Date=20261121T011230Z&HW-CC-Expire=31536000000&HW-CC-Sign=1399F96CD31D9A19A74C90865D85A91FA53FF67221C0BF0AECF23CDB02013F4B)
4. 参考“申请原因”中的模板，提供申请必需的相关信息，包括应用介绍、使用场景、申请用途，然后点击“提交”按钮。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/JSXRGJleR06AagzhJa2nnA/zh-cn_image_0000002821758013.png?HW-CC-KV=V1&HW-CC-Date=20261121T011230Z&HW-CC-Expire=31536000000&HW-CC-Sign=4FE7DE62726E882E196253494812CAB06E54AD4745B7BBA121017525A7D46C08)

返回“开放能力管理”页面，原“申请”变为“申请中”，1~3个工作日内反馈申请结果，请留意互动中心的“服务开通申请”信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/21/v3/6QfZip8wSPaddDegrXHE0w/zh-cn_image_0000002793038076.png?HW-CC-KV=V1&HW-CC-Date=20261121T011230Z&HW-CC-Expire=31536000000&HW-CC-Sign=60EE3ABF3B48886CB02F1852425C72A40BD41D190FEAE88A941430FC19F06AF9)

申请通过后，互动中心会发送通知给您，同时“申请中”会变为置灰显示的“申请”，至此，应用已成功开启室内高精度定位开放能力。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3f/v3/vmJGSI5aS-aFnwBx5hyjzA/zh-cn_image_0000002792878106.png?HW-CC-KV=V1&HW-CC-Date=20261121T011230Z&HW-CC-Expire=31536000000&HW-CC-Sign=F96988F7A6AD5DC350FC539EA5994531E2B88D0A16B92A14C63E2BE6C2A73C6C)

### 位置语义

为了更好的用户体验，系统侧对位置语义服务功能做了权限保护处理，使用相关接口开发者需先提交“位置语义”能力开关的申请。

若您的鸿蒙应用需感知用户周围的位置语义（如店铺、地铁站等）信息，请在申请通过后，再使用该能力。

1. 登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)，选择“开发与服务”。
2. 在项目列表选择项目，并在应用列表下选择需要申请位置语义功能的应用。
3. 进入“项目设置 > 开放能力管理”页面，选择能力名称为定位服务（HarmonyOS NEXT），然后点击“位置语义”对应的“申请”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/49/v3/y6TQ9P25RU6EiHbVeVYXWw/zh-cn_image_0000002821838011.png?HW-CC-KV=V1&HW-CC-Date=20261121T011230Z&HW-CC-Expire=31536000000&HW-CC-Sign=8B7F98BED034EC8CBFA306976C969ECFBF3453CE07B3513243B3D4E57FBBBFD1)
4. 参考“申请原因”中的模板，提供申请必需的相关信息，包括应用介绍、使用场景、申请用途，然后点击“提交”按钮。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/52/v3/KNL-N7uvRBmPnKHPJ7-inQ/zh-cn_image_0000002821838013.png?HW-CC-KV=V1&HW-CC-Date=20261121T011230Z&HW-CC-Expire=31536000000&HW-CC-Sign=1656D0C6914FC92B2647739512E9882C29D5FF2113ABD6823DE19C332497BE4B)

   返回“开放能力管理”页面，原“申请”变为“申请中”，1~3个工作日内反馈申请结果，请留意互动中心的“服务开通申请”信息。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bf/v3/KxDQJeWsT2eLHVZJ9vCRHg/zh-cn_image_0000002821758015.png?HW-CC-KV=V1&HW-CC-Date=20261121T011230Z&HW-CC-Expire=31536000000&HW-CC-Sign=7620B8CD8448A6F1C88AFC7699C38BD1AE62DF5D45C5D9678DA02F23AB8C1F22)

   申请通过后，互动中心会发送通知给您，同时“申请中”会变为置灰显示的“申请”，至此，应用已成功开启位置语义开放能力。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c7/v3/MjQXBDHuT6iHrkOrXzSSRg/zh-cn_image_0000002793038078.png?HW-CC-KV=V1&HW-CC-Date=20261121T011230Z&HW-CC-Expire=31536000000&HW-CC-Sign=394E95CCC3B1BB447D5F999232A1506A3395B421DE3022AEE0A84370E51568D2)

### 围栏后台唤醒

基于安全考虑，系统侧对围栏后台唤醒功能做了权限保护处理，使用相关接口开发者需先提交“围栏后台唤醒”能力开关的申请。

若您的鸿蒙应用在后台状态下需要接收用户进出围栏的事件通知，请在申请通过后，再使用该能力。

1. 登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)，选择“开发与服务”。
2. 在项目列表选择项目，并在应用列表下选择需要申请围栏后台唤醒功能的应用。
3. 进入“项目设置 > 开放能力管理”页面，选择能力名称为定位服务（HarmonyOS NEXT），然后点击“围栏后台唤醒”对应的“申请”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3c/v3/Jls1h8jaTzig3MY7HobvsQ/zh-cn_image_0000002821838011.png?HW-CC-KV=V1&HW-CC-Date=20261121T011230Z&HW-CC-Expire=31536000000&HW-CC-Sign=E81D934BBD22A34A0131528478788C2BD52056AA7293D27AAA426F215DEFFB03)
4. 参考“申请原因”中的模板，提供申请必需的相关信息，包括应用介绍、使用场景、申请用途，然后点击“提交”按钮。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/40/v3/d_sr2H0TSxy2TFZsgbNdEw/zh-cn_image_0000002792878108.png?HW-CC-KV=V1&HW-CC-Date=20261121T011230Z&HW-CC-Expire=31536000000&HW-CC-Sign=8F50EFDC98F4D96295446F8BD3BB32E4F7104D88B53927AD3543BFBFB9B5338C)

   返回“开放能力管理”页面，原“申请”变为“申请中”，1~3个工作日内反馈申请结果，请留意互动中心的“服务开通申请”信息。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5f/v3/HmwfXXQtSMWqYzQLdcu2EA/zh-cn_image_0000002821838015.png?HW-CC-KV=V1&HW-CC-Date=20261121T011230Z&HW-CC-Expire=31536000000&HW-CC-Sign=67AB0073C432819418631EA1E06D40BB589E4BCD006FA70EFB569E8CB6D18518)

   申请通过后，互动中心会发送通知给您，同时“申请中”会变为置灰显示的“申请”，至此，应用已成功开启围栏后台唤醒开放能力。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/zvI4rC4RR9yBFwZgp8Gupw/zh-cn_image_0000002821758017.png?HW-CC-KV=V1&HW-CC-Date=20261121T011230Z&HW-CC-Expire=31536000000&HW-CC-Sign=3A72E6528C2011A41BBEFFB4231DBE7B7EC70FB350B2140B063129A03D0D6F68)

### 获取蓝牙扫描信息

基于安全考虑，系统侧对获取蓝牙扫描信息功能做了权限保护处理，使用相关接口开发者需先提交“获取蓝牙扫描信息”能力开关的申请。

若您的鸿蒙应用需获取用户周围的蓝牙扫描信息，请在申请通过后，再使用该能力。

1. 登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)，选择“开发与服务”。
2. 在项目列表选择项目，并在应用列表下选择需要申请获取蓝牙扫描信息功能的应用。
3. 进入“项目设置 > 开放能力管理”页面，选择能力名称为定位服务（HarmonyOS NEXT），然后点击“获取蓝牙扫描信息”对应的“申请”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b6/v3/f75TZqJATnSOP3Wqv-ZDcg/zh-cn_image_0000002821838011.png?HW-CC-KV=V1&HW-CC-Date=20261121T011230Z&HW-CC-Expire=31536000000&HW-CC-Sign=01E6B26C95394B2FAC82F03B10B09C1BBB287975CB8C0048E22917959AF09615)
4. 参考“申请原因”中的模板，提供申请必需的相关信息，包括应用介绍、使用场景、申请用途，然后点击“提交”按钮。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ce/v3/Xcltw80FQH-6-H_posfS0w/zh-cn_image_0000002793038080.png?HW-CC-KV=V1&HW-CC-Date=20261121T011230Z&HW-CC-Expire=31536000000&HW-CC-Sign=CC852CEEFEA63B92AF260BFB21C4F415EF97A64843A3A29ECBAD8514A6A2598E)

   返回“开放能力管理”页面，原“申请”变为“申请中”，1~3个工作日内反馈申请结果，请留意互动中心的“服务开通申请”信息。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a6/v3/_n9_WqqZS-u2hj1wNVR2pw/zh-cn_image_0000002792878110.png?HW-CC-KV=V1&HW-CC-Date=20261121T011230Z&HW-CC-Expire=31536000000&HW-CC-Sign=85D7CA9EA1E6373736580D074B332AAC2FCA5B86BC9E8B8E5803D58321B91E97)

   申请通过后，互动中心会发送通知给您，同时“申请中”会变为置灰显示的“申请”，至此，应用已成功开启获取蓝牙扫描信息开放能力。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e6/v3/-S3H_PK2R8CiSkPLoZeySg/zh-cn_image_0000002821838017.png?HW-CC-KV=V1&HW-CC-Date=20261121T011230Z&HW-CC-Expire=31536000000&HW-CC-Sign=F28676CC4EC62D2DE91316E60BE641D3B948D00875761838B80D18370447EAB1)
