---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/location-apply-open-capability
title: 申请开放能力权限指导
breadcrumb: 指南 > 应用服务 > Location Kit（位置服务） > 开发准备 > 申请开放能力权限指导
category: harmonyos-guides
scraped_at: 2026-11-14T08:48:23+08:00
doc_updated_at: 2026-09-23
content_hash: sha256:980d16b0953b623a01c6fee7db9fc3ce31276d0cb1611fe14b477001e26e78aa
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

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/62/v3/q64jmb5aTCaDYD4WQIllsA/zh-cn_image_0000002817427485.png?HW-CC-KV=V1&HW-CC-Date=20261114T004639Z&HW-CC-Expire=31536000000&HW-CC-Sign=4F61FCBC83EAB29A50A9C1368C54139189B0EEEA424E9CE88E2DB88C8A9036D8)
4. 参考“申请原因”中的模板，提供申请必需的相关信息，包括应用介绍、使用场景、申请用途，然后点击“提交”按钮。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8/v3/DiRaG5X9QqGp3ZCVHBCXtg/zh-cn_image_0000002788468066.png?HW-CC-KV=V1&HW-CC-Date=20261114T004639Z&HW-CC-Expire=31536000000&HW-CC-Sign=EBCC8CF0B1D920D04B6581762C0408CF9D578413D53571A5C0F509A04A504D3A)

返回“开放能力管理”页面，原“申请”变为“申请中”，1~3个工作日内反馈申请结果，请留意互动中心的“服务开通申请”信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/19/v3/j6iAOQuGTRiGlAhrH6DEZQ/zh-cn_image_0000002817507555.png?HW-CC-KV=V1&HW-CC-Date=20261114T004639Z&HW-CC-Expire=31536000000&HW-CC-Sign=33DB1B05879E566DB809217809AEAE2C287B3D2DC6F9DF315C52CD42377C09BC)

申请通过后，互动中心会发送通知给您，同时“申请中”会变为置灰显示的“申请”，至此，应用已成功开启室内高精度定位开放能力。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ce/v3/MLLm_WnmQ5eASX2_SwhYAQ/zh-cn_image_0000002788308124.png?HW-CC-KV=V1&HW-CC-Date=20261114T004639Z&HW-CC-Expire=31536000000&HW-CC-Sign=739AA0D7C82FA659244781583006BAAE4EFBEAADB5CE49A57BD705A0D8519B8F)

### 位置语义

为了更好的用户体验，系统侧对位置语义服务功能做了权限保护处理，使用相关接口开发者需先提交“位置语义”能力开关的申请。

若您的鸿蒙应用需感知用户周围的位置语义（如店铺、地铁站等）信息，请在申请通过后，再使用该能力。

1. 登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)，选择“开发与服务”。
2. 在项目列表选择项目，并在应用列表下选择需要申请位置语义功能的应用。
3. 进入“项目设置 > 开放能力管理”页面，选择能力名称为定位服务（HarmonyOS NEXT），然后点击“位置语义”对应的“申请”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f1/v3/zYslhzReT7qjG_GKRTRWrg/zh-cn_image_0000002817427485.png?HW-CC-KV=V1&HW-CC-Date=20261114T004639Z&HW-CC-Expire=31536000000&HW-CC-Sign=BCEFAAFA985F2F78EFFD488D1F8CAA997374A6C928B686EC5C1EC61AA3A590D1)
4. 参考“申请原因”中的模板，提供申请必需的相关信息，包括应用介绍、使用场景、申请用途，然后点击“提交”按钮。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f6/v3/90PVwcV1TqKvv8rIWaQPIQ/zh-cn_image_0000002817427487.png?HW-CC-KV=V1&HW-CC-Date=20261114T004639Z&HW-CC-Expire=31536000000&HW-CC-Sign=A90D0EACEB4BEFDEB3F23FCF7BFD6B2D6C00FCAC441ADA1FB6A79BC16FB42C6E)

   返回“开放能力管理”页面，原“申请”变为“申请中”，1~3个工作日内反馈申请结果，请留意互动中心的“服务开通申请”信息。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/DJDA9zgnTzm4xHd9P6Gs4g/zh-cn_image_0000002788468068.png?HW-CC-KV=V1&HW-CC-Date=20261114T004639Z&HW-CC-Expire=31536000000&HW-CC-Sign=B63516350C1FCC30DF83E1AF4CA17242C2730BE006B1B3C737E5722F6AD5D0A4)

   申请通过后，互动中心会发送通知给您，同时“申请中”会变为置灰显示的“申请”，至此，应用已成功开启位置语义开放能力。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/D7C0vYrRSh-zn-gLQlFfcA/zh-cn_image_0000002817507557.png?HW-CC-KV=V1&HW-CC-Date=20261114T004639Z&HW-CC-Expire=31536000000&HW-CC-Sign=3644275B99ADDDC1B9537703338C9569BAAE1F8F2595721440072B9F86B61878)

### 围栏后台唤醒

基于安全考虑，系统侧对围栏后台唤醒功能做了权限保护处理，使用相关接口开发者需先提交“围栏后台唤醒”能力开关的申请。

若您的鸿蒙应用在后台状态下需要接收用户进出围栏的事件通知，请在申请通过后，再使用该能力。

1. 登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)，选择“开发与服务”。
2. 在项目列表选择项目，并在应用列表下选择需要申请围栏后台唤醒功能的应用。
3. 进入“项目设置 > 开放能力管理”页面，选择能力名称为定位服务（HarmonyOS NEXT），然后点击“围栏后台唤醒”对应的“申请”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a7/v3/knPCRHYLSBiq_nowvCL5mQ/zh-cn_image_0000002817427485.png?HW-CC-KV=V1&HW-CC-Date=20261114T004639Z&HW-CC-Expire=31536000000&HW-CC-Sign=D2150880859EAFBBCA93375F93303197E604D86EBC778EA6D2849FCCDE037F9A)
4. 参考“申请原因”中的模板，提供申请必需的相关信息，包括应用介绍、使用场景、申请用途，然后点击“提交”按钮。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/r5SN2hzlRq-sGFGAqkdnlQ/zh-cn_image_0000002788308126.png?HW-CC-KV=V1&HW-CC-Date=20261114T004639Z&HW-CC-Expire=31536000000&HW-CC-Sign=2130C7BEB9EA3F70A49407E180A8B48D944175710D6AC41CA3B0D6D7A39C7078)

   返回“开放能力管理”页面，原“申请”变为“申请中”，1~3个工作日内反馈申请结果，请留意互动中心的“服务开通申请”信息。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/12/v3/nm8a3yXARbytm8jRMya_tg/zh-cn_image_0000002817427489.png?HW-CC-KV=V1&HW-CC-Date=20261114T004639Z&HW-CC-Expire=31536000000&HW-CC-Sign=647749FD1727D83F3BDBB1A0A0F923EA3C2154308ABA00E24B56F88E8BD4E19D)

   申请通过后，互动中心会发送通知给您，同时“申请中”会变为置灰显示的“申请”，至此，应用已成功开启围栏后台唤醒开放能力。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0f/v3/1hK7XZtRSvaT_b5YpKnYxA/zh-cn_image_0000002788468070.png?HW-CC-KV=V1&HW-CC-Date=20261114T004639Z&HW-CC-Expire=31536000000&HW-CC-Sign=5D7C531A3D4B86916D09A03EF40017E77A22083E2942003D2A578C0150DD96DE)

### 获取蓝牙扫描信息

基于安全考虑，系统侧对获取蓝牙扫描信息功能做了权限保护处理，使用相关接口开发者需先提交“获取蓝牙扫描信息”能力开关的申请。

若您的鸿蒙应用需获取用户周围的蓝牙扫描信息，请在申请通过后，再使用该能力。

1. 登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)，选择“开发与服务”。
2. 在项目列表选择项目，并在应用列表下选择需要申请获取蓝牙扫描信息功能的应用。
3. 进入“项目设置 > 开放能力管理”页面，选择能力名称为定位服务（HarmonyOS NEXT），然后点击“获取蓝牙扫描信息”对应的“申请”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/31/v3/8qgDOwW3QpqXb0A5KlmAmg/zh-cn_image_0000002817427485.png?HW-CC-KV=V1&HW-CC-Date=20261114T004639Z&HW-CC-Expire=31536000000&HW-CC-Sign=EA73E920EF4A4546C4B157694D44796B4C57E2FB795A615AB1E3294E4457D2D7)
4. 参考“申请原因”中的模板，提供申请必需的相关信息，包括应用介绍、使用场景、申请用途，然后点击“提交”按钮。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/59/v3/A_5x5dMrQ86hpuGZAWg6cQ/zh-cn_image_0000002817507559.png?HW-CC-KV=V1&HW-CC-Date=20261114T004639Z&HW-CC-Expire=31536000000&HW-CC-Sign=9CD6F42CEA52C91D2701F592AA08676C75C867FCD9653E6491F8E111E79893AB)

   返回“开放能力管理”页面，原“申请”变为“申请中”，1~3个工作日内反馈申请结果，请留意互动中心的“服务开通申请”信息。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f8/v3/P0y6MRCYT06DbQ6Je_-FQQ/zh-cn_image_0000002788308128.png?HW-CC-KV=V1&HW-CC-Date=20261114T004639Z&HW-CC-Expire=31536000000&HW-CC-Sign=766AD088A41393D77432AECAF94E8148A5A529703F598D6706E6316EC34CDA14)

   申请通过后，互动中心会发送通知给您，同时“申请中”会变为置灰显示的“申请”，至此，应用已成功开启获取蓝牙扫描信息开放能力。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/86/v3/tbCq90PkTH6izIXmz90Vow/zh-cn_image_0000002817427491.png?HW-CC-KV=V1&HW-CC-Date=20261114T004639Z&HW-CC-Expire=31536000000&HW-CC-Sign=38C42E8DFD86EB5343759D5A3096413408F32E0DBC5B7F465A5831CF1BF9F40C)
