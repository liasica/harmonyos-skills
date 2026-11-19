---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/location-apply-open-capability
title: 申请开放能力权限指导
breadcrumb: 指南 > 应用服务 > Location Kit（位置服务） > 开发准备 > 申请开放能力权限指导
category: harmonyos-guides
scraped_at: 2026-11-19T09:49:04+08:00
doc_updated_at: 2026-09-23
content_hash: sha256:f697c3902426bfbc9c6fed77f65fc77c5f34031f043d65d1986476c283cd64ba
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

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4c/v3/QDHVBXOmQZKuVuOV0gM8UQ/zh-cn_image_0000002791726424.png?HW-CC-KV=V1&HW-CC-Date=20261119T014904Z&HW-CC-Expire=31536000000&HW-CC-Sign=0CF2CC8FFB03449C2DD4DC9F9A13E4B5D77537E7A3CBF59F0144B376FDF23AB4)
4. 参考“申请原因”中的模板，提供申请必需的相关信息，包括应用介绍、使用场景、申请用途，然后点击“提交”按钮。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/27/v3/nFnRZafjQYyyVva-KZjxXg/zh-cn_image_0000002791566452.png?HW-CC-KV=V1&HW-CC-Date=20261119T014904Z&HW-CC-Expire=31536000000&HW-CC-Sign=7A5A55ED5119AC39D6B1C864405DDE488325FF109725BB82126A39F3E7E707E0)

返回“开放能力管理”页面，原“申请”变为“申请中”，1~3个工作日内反馈申请结果，请留意互动中心的“服务开通申请”信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2b/v3/2fpCaGWKQhysAxJZ0ked9Q/zh-cn_image_0000002820526405.png?HW-CC-KV=V1&HW-CC-Date=20261119T014904Z&HW-CC-Expire=31536000000&HW-CC-Sign=F12DB8FC10988CDBBCBAE4492ABCED1BDCE46E19825033A57BE5A1BC3592F15E)

申请通过后，互动中心会发送通知给您，同时“申请中”会变为置灰显示的“申请”，至此，应用已成功开启室内高精度定位开放能力。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4b/v3/q-1FAnkXQSC9GKjsGCpvhA/zh-cn_image_0000002820406405.png?HW-CC-KV=V1&HW-CC-Date=20261119T014904Z&HW-CC-Expire=31536000000&HW-CC-Sign=0A129E31FFF27EDB56D9D82535F52EA7B9FAE49AA46CD3F76A1424B54D4AF961)

### 位置语义

为了更好的用户体验，系统侧对位置语义服务功能做了权限保护处理，使用相关接口开发者需先提交“位置语义”能力开关的申请。

若您的鸿蒙应用需感知用户周围的位置语义（如店铺、地铁站等）信息，请在申请通过后，再使用该能力。

1. 登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)，选择“开发与服务”。
2. 在项目列表选择项目，并在应用列表下选择需要申请位置语义功能的应用。
3. 进入“项目设置 > 开放能力管理”页面，选择能力名称为定位服务（HarmonyOS NEXT），然后点击“位置语义”对应的“申请”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/30/v3/2JFcKZTbT3yJHzWARjJpcw/zh-cn_image_0000002791726424.png?HW-CC-KV=V1&HW-CC-Date=20261119T014904Z&HW-CC-Expire=31536000000&HW-CC-Sign=7CDE3F8424CD406497009B1D9F846C6A89C73CFBCB5610FC44437666994A5C6C)
4. 参考“申请原因”中的模板，提供申请必需的相关信息，包括应用介绍、使用场景、申请用途，然后点击“提交”按钮。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/41/v3/MWogUFEaQ-OwweoRMLKPhA/zh-cn_image_0000002791726426.png?HW-CC-KV=V1&HW-CC-Date=20261119T014904Z&HW-CC-Expire=31536000000&HW-CC-Sign=F29DA4E4F518657539D66D58553DAF3FA6AB31D7252334CBF8E07AC26C74B314)

   返回“开放能力管理”页面，原“申请”变为“申请中”，1~3个工作日内反馈申请结果，请留意互动中心的“服务开通申请”信息。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/k-ucw1rlT8apQpCWVJKHDA/zh-cn_image_0000002791566454.png?HW-CC-KV=V1&HW-CC-Date=20261119T014904Z&HW-CC-Expire=31536000000&HW-CC-Sign=813604D95015C579E2F9CC823DC69AA151B0F03AB950C91BA36428B3C258BC06)

   申请通过后，互动中心会发送通知给您，同时“申请中”会变为置灰显示的“申请”，至此，应用已成功开启位置语义开放能力。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d8/v3/NP9s6qvyRpyHlKNfDk5rkA/zh-cn_image_0000002820526407.png?HW-CC-KV=V1&HW-CC-Date=20261119T014904Z&HW-CC-Expire=31536000000&HW-CC-Sign=6570E579A9E84917C399A9D1A9AFE23B64D8A3BF8352107F16B3BDC4171C82D9)

### 围栏后台唤醒

基于安全考虑，系统侧对围栏后台唤醒功能做了权限保护处理，使用相关接口开发者需先提交“围栏后台唤醒”能力开关的申请。

若您的鸿蒙应用在后台状态下需要接收用户进出围栏的事件通知，请在申请通过后，再使用该能力。

1. 登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)，选择“开发与服务”。
2. 在项目列表选择项目，并在应用列表下选择需要申请围栏后台唤醒功能的应用。
3. 进入“项目设置 > 开放能力管理”页面，选择能力名称为定位服务（HarmonyOS NEXT），然后点击“围栏后台唤醒”对应的“申请”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/83/v3/bevaFepIRt-_rC1se8ILgg/zh-cn_image_0000002791726424.png?HW-CC-KV=V1&HW-CC-Date=20261119T014904Z&HW-CC-Expire=31536000000&HW-CC-Sign=F9B371D2D397B778FB7128E526A4AECBEE4949BACB9A21EB668D77E8F541893A)
4. 参考“申请原因”中的模板，提供申请必需的相关信息，包括应用介绍、使用场景、申请用途，然后点击“提交”按钮。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/74/v3/BJqyKC8DTvGG7BMAj4XgkQ/zh-cn_image_0000002820406407.png?HW-CC-KV=V1&HW-CC-Date=20261119T014904Z&HW-CC-Expire=31536000000&HW-CC-Sign=874E517600D59A9BF4E3D9FC680F10560AA4A0512C1851A7B126A87C3A2C848D)

   返回“开放能力管理”页面，原“申请”变为“申请中”，1~3个工作日内反馈申请结果，请留意互动中心的“服务开通申请”信息。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f5/v3/4jU6bNIrTl6XwV3Uy-3oyw/zh-cn_image_0000002791726428.png?HW-CC-KV=V1&HW-CC-Date=20261119T014904Z&HW-CC-Expire=31536000000&HW-CC-Sign=B8E3780C81F4A91EA0045B756094B6198B1AD98F67B161E3C981B0DA3F7F1823)

   申请通过后，互动中心会发送通知给您，同时“申请中”会变为置灰显示的“申请”，至此，应用已成功开启围栏后台唤醒开放能力。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/41/v3/u-YZVJKZQHaow9GmbquilA/zh-cn_image_0000002791566456.png?HW-CC-KV=V1&HW-CC-Date=20261119T014904Z&HW-CC-Expire=31536000000&HW-CC-Sign=98D06DAD9C95E3A4BA1C1504ABEBF0942136A9CBB12D2B3126872377C729FA5E)

### 获取蓝牙扫描信息

基于安全考虑，系统侧对获取蓝牙扫描信息功能做了权限保护处理，使用相关接口开发者需先提交“获取蓝牙扫描信息”能力开关的申请。

若您的鸿蒙应用需获取用户周围的蓝牙扫描信息，请在申请通过后，再使用该能力。

1. 登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)，选择“开发与服务”。
2. 在项目列表选择项目，并在应用列表下选择需要申请获取蓝牙扫描信息功能的应用。
3. 进入“项目设置 > 开放能力管理”页面，选择能力名称为定位服务（HarmonyOS NEXT），然后点击“获取蓝牙扫描信息”对应的“申请”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ce/v3/ug8DtJadTP-DYSnxoUDn1A/zh-cn_image_0000002791726424.png?HW-CC-KV=V1&HW-CC-Date=20261119T014904Z&HW-CC-Expire=31536000000&HW-CC-Sign=2DF985B28B3840ACA9F10D1FE99F7ABCA1669A7544B9218CE88D0792EEF86EE4)
4. 参考“申请原因”中的模板，提供申请必需的相关信息，包括应用介绍、使用场景、申请用途，然后点击“提交”按钮。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f6/v3/bze3KxAVTw-YUt4u78UyWQ/zh-cn_image_0000002820526409.png?HW-CC-KV=V1&HW-CC-Date=20261119T014904Z&HW-CC-Expire=31536000000&HW-CC-Sign=8CC2CA5A25EF0D48E050A300DF9901D31C6E4A0EB933433CC2E19C2E793E6BD3)

   返回“开放能力管理”页面，原“申请”变为“申请中”，1~3个工作日内反馈申请结果，请留意互动中心的“服务开通申请”信息。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f3/v3/8njUD2PYQBOWddjfXA4eUA/zh-cn_image_0000002820406409.png?HW-CC-KV=V1&HW-CC-Date=20261119T014904Z&HW-CC-Expire=31536000000&HW-CC-Sign=A7FD9AD8EE6241CF11409D9DA6677A11FEAEE1567A6F984DC750179E4EC15E9D)

   申请通过后，互动中心会发送通知给您，同时“申请中”会变为置灰显示的“申请”，至此，应用已成功开启获取蓝牙扫描信息开放能力。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/16/v3/hKVEu5r1SNidybuxC5XjHg/zh-cn_image_0000002791726430.png?HW-CC-KV=V1&HW-CC-Date=20261119T014904Z&HW-CC-Expire=31536000000&HW-CC-Sign=0E3093E0959EF3AD242FBF3C6BC9A21098B6BEEC04C18AA2D3735214AC3AAB69)
