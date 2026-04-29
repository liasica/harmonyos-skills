---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/location-apply-open-capability
title: 申请开放能力权限指导
breadcrumb: 指南 > 应用服务 > Location Kit（位置服务） > 开发准备 > 申请开放能力权限指导
category: harmonyos-guides
scraped_at: 2026-04-29T13:38:57+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:4eb3f759c7a65c31a5ef8e85c9fbd81ecf6ddf15d3dd4c37bc9c5bdada2d8780
---

## 开放能力申请准备

请先参考[应用开发准备](application-dev-overview.md)完成基本准备工作，再继续以下开放能力准备项。

### 室内高精度定位

为了更好的用户体验，系统侧对室内高精度定位服务功能做了权限保护处理，使用相关接口开发者需先提交“室内高精度定位”能力开关的申请，请在申请通过后，再使用该能力。

室内高精度定位仅支持商场、高铁站、机场和医院等场所，支持的建筑列表如下。

[支持室内定位建筑列表](https://openlocation-portal-drcn.partner.petalmaps.com/indoormap/index.html#/homePage)

在这些建筑中支持楼层识别，定位精度约10~20米左右。

未开通室内高精度定位服务时locationKit仍然支持在室内场景进行网络定位获取定位结果。

1. 登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)，选择“开发与服务”。
2. 在项目列表选择项目，并在应用列表下选择需要申请室内高精度定位功能的应用。
3. 进入“项目设置 > 开放能力管理”页面，选择能力名称为定位服务（HarmonyOS NEXT），然后点击“室内高精度定位”对应的“申请”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/63/v3/ZzTJNHm7RHWQIIVjyHmHVQ/zh-cn_image_0000002558605830.png?HW-CC-KV=V1&HW-CC-Date=20260429T053856Z&HW-CC-Expire=86400&HW-CC-Sign=05D42D808914F0B8BE523EF230850809874FD6E8DB53D6518C2F8DE9C62D589B)
4. 参考“申请原因”中的模板，提供申请必需的相关信息，包括应用介绍、使用场景、申请用途，然后点击“提交”按钮。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4a/v3/HS8NN6DxSTiwP-GJ_sXP_Q/zh-cn_image_0000002589325359.png?HW-CC-KV=V1&HW-CC-Date=20260429T053856Z&HW-CC-Expire=86400&HW-CC-Sign=4DB8363754296C5601CD905470904E4802B4D2C4A4B80ED3A758E5CC6436322B)

返回“开放能力管理”页面，原“申请”变为“申请中”，1~3个工作日内反馈申请结果，请留意互动中心的“服务开通申请”信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2a/v3/A1yQrrAESbOlr29jt-jetA/zh-cn_image_0000002589245295.png?HW-CC-KV=V1&HW-CC-Date=20260429T053856Z&HW-CC-Expire=86400&HW-CC-Sign=D5CA2939585D9051EC99FC0BB660A9F94CE9023A0C9F1E311D522BD98A427904)

申请通过后，互动中心会发送通知给您，同时“申请中”会变为置灰显示的“申请”，至此，应用已成功开启室内高精度定位开放能力。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f4/v3/opO0MwnzQfOMUmmSVjJNdw/zh-cn_image_0000002558765488.png?HW-CC-KV=V1&HW-CC-Date=20260429T053856Z&HW-CC-Expire=86400&HW-CC-Sign=FBAC6C9ECAB5B3200505F32E94316532D266525110F82AF51CF714D3065ABC6F)

### 位置语义

为了更好的用户体验，系统侧对位置语义服务功能做了权限保护处理，使用相关接口开发者需先提交“位置语义”能力开关的申请。

若您的鸿蒙应用需感知用户周围的位置语义（如店铺、地铁站等）信息，请在申请通过后，再使用该能力。

1. 登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)，选择“开发与服务”。
2. 在项目列表选择项目，并在应用列表下选择需要申请位置语义功能的应用。
3. 进入“项目设置 > 开放能力管理”页面，选择能力名称为定位服务（HarmonyOS NEXT），然后点击“位置语义”对应的“申请”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/aa/v3/aoQO-eavS_uBXBZtA23G8g/zh-cn_image_0000002558605834.png?HW-CC-KV=V1&HW-CC-Date=20260429T053856Z&HW-CC-Expire=86400&HW-CC-Sign=D0C2247F35905B352F989960CD077F028C3D69D8F88FF5FE7A52D052D0EA58C9)
4. 参考“申请原因”中的模板，提供申请必需的相关信息，包括应用介绍、使用场景、申请用途，然后点击“提交”按钮。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d7/v3/juqifpo7QUKviRKMRPHlQw/zh-cn_image_0000002589325361.png?HW-CC-KV=V1&HW-CC-Date=20260429T053856Z&HW-CC-Expire=86400&HW-CC-Sign=8483DBD92102DA3F3B9B1AF6B58CE6581CD760E66AF28E94F0F164AAC4714E85)

   返回“开放能力管理”页面，原“申请”变为“申请中”，1~3个工作日内反馈申请结果，请留意互动中心的“服务开通申请”信息。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dd/v3/XiU35GjDQauphQjA-_Pxjg/zh-cn_image_0000002589245297.png?HW-CC-KV=V1&HW-CC-Date=20260429T053856Z&HW-CC-Expire=86400&HW-CC-Sign=FC6D97AD6D0A9C08EA728DEB4EF91AFF1FE680EA3252DE277F0B8F8C72AA07E8)

   申请通过后，互动中心会发送通知给您，同时“申请中”会变为置灰显示的“申请”，至此，应用已成功开启位置语义开放能力。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/13/v3/pQbQ6zwiSlGW2394zU_WBw/zh-cn_image_0000002558765490.png?HW-CC-KV=V1&HW-CC-Date=20260429T053856Z&HW-CC-Expire=86400&HW-CC-Sign=633ED5064C6369A967FEAF6F337515C47F1AC9937405D2B8FA1E7124B5BEBE06)

### Beacon围栏后台唤醒

基于安全考虑，系统侧对Beacon围栏后台唤醒功能做了权限保护处理，使用相关接口开发者需先提交“Beacon围栏后台唤醒”能力开关的申请。

若您的鸿蒙应用在后台状态下需要接收用户进出围栏的事件通知，请在申请通过后，再使用该能力。

1. 登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)，选择“开发与服务”。
2. 在项目列表选择项目，并在应用列表下选择需要申请Beacon围栏后台唤醒功能的应用。
3. 进入“项目设置 > 开放能力管理”页面，选择能力名称为定位服务（HarmonyOS NEXT），然后点击“Beacon围栏后台唤醒”对应的“申请”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/53/v3/znCSfsKaSG2vT2m04NIAFg/zh-cn_image_0000002558605836.png?HW-CC-KV=V1&HW-CC-Date=20260429T053856Z&HW-CC-Expire=86400&HW-CC-Sign=801BAA274EE5700D66CF50444836D58B78523E8ABB51B31E3C820FBE2B30D0A9)
4. 参考“申请原因”中的模板，提供申请必需的相关信息，包括应用介绍、使用场景、申请用途，然后点击“提交”按钮。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/WOtgLoKXSh6d-GlW6kJkrg/zh-cn_image_0000002589325363.png?HW-CC-KV=V1&HW-CC-Date=20260429T053856Z&HW-CC-Expire=86400&HW-CC-Sign=D29B3DC8561F9F7B5F82BC7FC2A92DC4D01E7F934282DF7F283EB72BD45A022D)

   返回“开放能力管理”页面，原“申请”变为“申请中”，1~3个工作日内反馈申请结果，请留意互动中心的“服务开通申请”信息。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/75/v3/v6pkqPHzTii3hPxBsv6TjA/zh-cn_image_0000002589245299.png?HW-CC-KV=V1&HW-CC-Date=20260429T053856Z&HW-CC-Expire=86400&HW-CC-Sign=FF6A3C4DF792E85E12707BFC0ADCC92037DECF2587B9DFFE2AD6430C8D65DD8A)

   申请通过后，互动中心会发送通知给您，同时“申请中”会变为置灰显示的“申请”，至此，应用已成功开启Beacon围栏后台唤醒开放能力。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ad/v3/YpLs0qD3RJuVQF1LGpzjJg/zh-cn_image_0000002558765492.png?HW-CC-KV=V1&HW-CC-Date=20260429T053856Z&HW-CC-Expire=86400&HW-CC-Sign=85C6E618CACE8A529342BA25AD66ECC69A0A5DF40301EE94746AD332AB38E211)

### 获取蓝牙扫描信息

基于安全考虑，系统侧对获取蓝牙扫描信息功能做了权限保护处理，使用相关接口开发者需先提交“获取蓝牙扫描信息”能力开关的申请。

若您的鸿蒙应用需获取用户周围的蓝牙扫描信息，请在申请通过后，再使用该能力。

1. 登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)，选择“开发与服务”。
2. 在项目列表选择项目，并在应用列表下选择需要申请获取蓝牙扫描信息功能的应用。
3. 进入“项目设置 > 开放能力管理”页面，选择能力名称为定位服务（HarmonyOS NEXT），然后点击“获取蓝牙扫描信息”对应的“申请”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/49/v3/0J2o2JLpTX2XhCo3tR6Gyw/zh-cn_image_0000002558605838.png?HW-CC-KV=V1&HW-CC-Date=20260429T053856Z&HW-CC-Expire=86400&HW-CC-Sign=B354970996EC436251DBAB7CF6397EE29BE49D98D374F11B00C7B727CCA9749A)
4. 参考“申请原因”中的模板，提供申请必需的相关信息，包括应用介绍、使用场景、申请用途，然后点击“提交”按钮。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/wyp4Los9TZSr1tuMw7SBzg/zh-cn_image_0000002589325365.png?HW-CC-KV=V1&HW-CC-Date=20260429T053856Z&HW-CC-Expire=86400&HW-CC-Sign=2037BEFC993C12E6A9495182C66B9ABC03D6DD452355F887CD4DB65F6DD77F96)

   返回“开放能力管理”页面，原“申请”变为“申请中”，1~3个工作日内反馈申请结果，请留意互动中心的“服务开通申请”信息。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f5/v3/RkauDgWCT_KD1TCRh4SUrg/zh-cn_image_0000002589245301.png?HW-CC-KV=V1&HW-CC-Date=20260429T053856Z&HW-CC-Expire=86400&HW-CC-Sign=79BA9ED16EB47A01F7C93C8A97EEBBFEED5F95ABD925231AA71AB6DAF28C38FB)

   申请通过后，互动中心会发送通知给您，同时“申请中”会变为置灰显示的“申请”，至此，应用已成功开启获取蓝牙扫描信息开放能力。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f2/v3/EtmsIvZXQAKgrslnR_67lA/zh-cn_image_0000002558765494.png?HW-CC-KV=V1&HW-CC-Date=20260429T053856Z&HW-CC-Expire=86400&HW-CC-Sign=FB1AF647301C10D59751306342675DC55BABE91593732B3B76F4E25C1EF1593B)
