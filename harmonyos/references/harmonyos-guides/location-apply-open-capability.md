---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/location-apply-open-capability
title: 申请开放能力权限指导
breadcrumb: 指南 > 应用服务 > Location Kit（位置服务） > 开发准备 > 申请开放能力权限指导
category: harmonyos-guides
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-09-23
content_hash: sha256:f6c339fc555dd2bc07e8397d32ae9a506ff38895e7cf706806b856cc6e29ba73
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

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b2/v3/1aFdPd-STCmYxnfnJ6txfg/zh-cn_image_0000002786360390.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=F2D01845619E6DAA6017D149E457E2AE6B6574C5414F717A6AB281C76B539D0A)
4. 参考“申请原因”中的模板，提供申请必需的相关信息，包括应用介绍、使用场景、申请用途，然后点击“提交”按钮。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c8/v3/YwswhxtLQ1eFqoMyprk6qw/zh-cn_image_0000002815559811.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=7C3EAAD9D89921D4C6CCB689F3E08DC2DE310A382C97828AF892EAAD1455D7AF)

返回“开放能力管理”页面，原“申请”变为“申请中”，1~3个工作日内反馈申请结果，请留意互动中心的“服务开通申请”信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1c/v3/EUyd3CFeRRqaVWK21P9VYw/zh-cn_image_0000002815399895.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=A3DEEBD6528E47A1F47D41D2044702340AFAB686EC56714742979F13AF28F803)

申请通过后，互动中心会发送通知给您，同时“申请中”会变为置灰显示的“申请”，至此，应用已成功开启室内高精度定位开放能力。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3c/v3/zAceDzzgRLC4Z8ISJHTG5A/zh-cn_image_0000002786520320.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=D5875837D13B1E2700491DE777742108347CB2FAC6C05CEC5D0C8078F6F8E384)

### 位置语义

为了更好的用户体验，系统侧对位置语义服务功能做了权限保护处理，使用相关接口开发者需先提交“位置语义”能力开关的申请。

若您的鸿蒙应用需感知用户周围的位置语义（如店铺、地铁站等）信息，请在申请通过后，再使用该能力。

1. 登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)，选择“开发与服务”。
2. 在项目列表选择项目，并在应用列表下选择需要申请位置语义功能的应用。
3. 进入“项目设置 > 开放能力管理”页面，选择能力名称为定位服务（HarmonyOS NEXT），然后点击“位置语义”对应的“申请”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/83/v3/fR4DiiXSRL2Q07d_GXN-6w/zh-cn_image_0000002786360390.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=F69F00E3E73B8786C3071D0A39908A65396D34E4A2783E0AB58C5BF7C5A5F3F0)
4. 参考“申请原因”中的模板，提供申请必需的相关信息，包括应用介绍、使用场景、申请用途，然后点击“提交”按钮。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5f/v3/zgI-LbRzRteRLdycLJB7uA/zh-cn_image_0000002786360392.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=00703C6B855EB08D829DA1361006D4A30E5B11A18BA58285148F9247BF5FE10B)

   返回“开放能力管理”页面，原“申请”变为“申请中”，1~3个工作日内反馈申请结果，请留意互动中心的“服务开通申请”信息。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ed/v3/wqTtR0KjSKuFPB1TRI19ng/zh-cn_image_0000002815559813.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=4AF52D39FE2B07C43ACC4792BA30832A11FA88371D9E74C683036B9E50E215E8)

   申请通过后，互动中心会发送通知给您，同时“申请中”会变为置灰显示的“申请”，至此，应用已成功开启位置语义开放能力。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/VfZA5SHMTvyDuKkycgnK9Q/zh-cn_image_0000002815399897.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=50641B916A78DA88F15DB5F8D79E44734678EDB82BE8D16F11C32A0F813C5A4B)

### 围栏后台唤醒

基于安全考虑，系统侧对围栏后台唤醒功能做了权限保护处理，使用相关接口开发者需先提交“围栏后台唤醒”能力开关的申请。

若您的鸿蒙应用在后台状态下需要接收用户进出围栏的事件通知，请在申请通过后，再使用该能力。

1. 登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)，选择“开发与服务”。
2. 在项目列表选择项目，并在应用列表下选择需要申请围栏后台唤醒功能的应用。
3. 进入“项目设置 > 开放能力管理”页面，选择能力名称为定位服务（HarmonyOS NEXT），然后点击“围栏后台唤醒”对应的“申请”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f1/v3/9du55p5GQ6arbkQiNFP4qw/zh-cn_image_0000002786360390.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=1623A4493F53C3D40EA9E500389CE5F28D74233EE0FED1AF40FE03D5539132BE)
4. 参考“申请原因”中的模板，提供申请必需的相关信息，包括应用介绍、使用场景、申请用途，然后点击“提交”按钮。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7/v3/PofuRpUSQ2SPG9tiNskqTA/zh-cn_image_0000002786520322.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=0AFDCE6B2C83AC766CCA3B378EF5208A3EED01BCAF559B68AAFDECFD725D3A6A)

   返回“开放能力管理”页面，原“申请”变为“申请中”，1~3个工作日内反馈申请结果，请留意互动中心的“服务开通申请”信息。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/86/v3/hdCaK-riSoKr-DRr1wQ2OA/zh-cn_image_0000002786360394.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=CC5E7AF66D5D6BB6549E9180B26D6154874460E9A9706A21EFFEBCC757AE5148)

   申请通过后，互动中心会发送通知给您，同时“申请中”会变为置灰显示的“申请”，至此，应用已成功开启围栏后台唤醒开放能力。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e9/v3/DgtTf6JOQAOJZPmp8Bkngg/zh-cn_image_0000002815559815.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=3097079B0B85C7BCF1DB9015E2AD61253A387B1E7375D70AB0E906B4AAA5A211)

### 获取蓝牙扫描信息

基于安全考虑，系统侧对获取蓝牙扫描信息功能做了权限保护处理，使用相关接口开发者需先提交“获取蓝牙扫描信息”能力开关的申请。

若您的鸿蒙应用需获取用户周围的蓝牙扫描信息，请在申请通过后，再使用该能力。

1. 登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)，选择“开发与服务”。
2. 在项目列表选择项目，并在应用列表下选择需要申请获取蓝牙扫描信息功能的应用。
3. 进入“项目设置 > 开放能力管理”页面，选择能力名称为定位服务（HarmonyOS NEXT），然后点击“获取蓝牙扫描信息”对应的“申请”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b4/v3/xvP94KjiSg--Nn94eknYjA/zh-cn_image_0000002786360390.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=BA3F85FE272C9405B167118E2B44DF605BC1BFF734C48F0D95A9CFA120DAFE8A)
4. 参考“申请原因”中的模板，提供申请必需的相关信息，包括应用介绍、使用场景、申请用途，然后点击“提交”按钮。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2f/v3/iF0Op9iqSn2hI4Tav4GSbQ/zh-cn_image_0000002815399899.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=56CD907B2D5E1231304AE77B08A46049A75EEE5BAAE8DEC9AA3E2A5144F33552)

   返回“开放能力管理”页面，原“申请”变为“申请中”，1~3个工作日内反馈申请结果，请留意互动中心的“服务开通申请”信息。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/gBtUVAwUTSefZP9wxOiulQ/zh-cn_image_0000002786520324.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=3363F18B0BEB837E653650E6E6CFE540C352940AE8B10022E24F2AD9A65E4358)

   申请通过后，互动中心会发送通知给您，同时“申请中”会变为置灰显示的“申请”，至此，应用已成功开启获取蓝牙扫描信息开放能力。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d5/v3/I7jr8qwXTFO9jKNmij1skQ/zh-cn_image_0000002786360396.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=3FF7BCDABC5D129ECCDBDF0DB3F0B63B3983C1F2305D2B31325B8F8CB53B54B6)
