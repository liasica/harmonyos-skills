---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/location-apply-open-capability
title: 申请开放能力权限指导
breadcrumb: 指南 > 应用服务 > Location Kit（位置服务） > 开发准备 > 申请开放能力权限指导
category: harmonyos-guides
scraped_at: 2026-09-21T06:18:40+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:ab63a2b6ed0754886039df9eb3d50f5d234046451aadb974e44be33bcf0576bf
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

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/89/v3/43lEfCazTEy2mY-1us86LQ/zh-cn_image_0000002762994813.png)
4. 参考“申请原因”中的模板，提供申请必需的相关信息，包括应用介绍、使用场景、申请用途，然后点击“提交”按钮。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/16/v3/hh9-HA9WTnmCHMFrvlyeYA/zh-cn_image_0000002762834925.png)

返回“开放能力管理”页面，原“申请”变为“申请中”，1~3个工作日内反馈申请结果，请留意互动中心的“服务开通申请”信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a5/v3/TZ72eNXiQOuoQzK7v66ZHA/zh-cn_image_0000002733275410.png)

申请通过后，互动中心会发送通知给您，同时“申请中”会变为置灰显示的“申请”，至此，应用已成功开启室内高精度定位开放能力。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/44/v3/3AEOuD6KQQ22l_SXYQ6HkQ/zh-cn_image_0000002733435292.png)

### 位置语义

为了更好的用户体验，系统侧对位置语义服务功能做了权限保护处理，使用相关接口开发者需先提交“位置语义”能力开关的申请。

若您的鸿蒙应用需感知用户周围的位置语义（如店铺、地铁站等）信息，请在申请通过后，再使用该能力。

1. 登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)，选择“开发与服务”。
2. 在项目列表选择项目，并在应用列表下选择需要申请位置语义功能的应用。
3. 进入“项目设置 > 开放能力管理”页面，选择能力名称为定位服务（HarmonyOS NEXT），然后点击“位置语义”对应的“申请”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0d/v3/bVtCmSorTeGH-j09Kn4zqQ/zh-cn_image_0000002762994813.png)
4. 参考“申请原因”中的模板，提供申请必需的相关信息，包括应用介绍、使用场景、申请用途，然后点击“提交”按钮。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cf/v3/fe4noR44RXuDf-zQ21Hxfw/zh-cn_image_0000002762994815.png)

   返回“开放能力管理”页面，原“申请”变为“申请中”，1~3个工作日内反馈申请结果，请留意互动中心的“服务开通申请”信息。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/82/v3/tw3mQxL0QwuNu3c5rqZStg/zh-cn_image_0000002762834927.png)

   申请通过后，互动中心会发送通知给您，同时“申请中”会变为置灰显示的“申请”，至此，应用已成功开启位置语义开放能力。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e7/v3/dpTc7UWvQ2mKPha75cgZpQ/zh-cn_image_0000002733275412.png)

### 围栏后台唤醒

基于安全考虑，系统侧对围栏后台唤醒功能做了权限保护处理，使用相关接口开发者需先提交“围栏后台唤醒”能力开关的申请。

若您的鸿蒙应用在后台状态下需要接收用户进出围栏的事件通知，请在申请通过后，再使用该能力。

1. 登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)，选择“开发与服务”。
2. 在项目列表选择项目，并在应用列表下选择需要申请围栏后台唤醒功能的应用。
3. 进入“项目设置 > 开放能力管理”页面，选择能力名称为定位服务（HarmonyOS NEXT），然后点击“围栏后台唤醒”对应的“申请”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ed/v3/_5CDTFssQBy32HRyWT-inQ/zh-cn_image_0000002762994813.png)
4. 参考“申请原因”中的模板，提供申请必需的相关信息，包括应用介绍、使用场景、申请用途，然后点击“提交”按钮。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a2/v3/MLrqoCadRxiVb9t-zBpA0A/zh-cn_image_0000002733435294.png)

   返回“开放能力管理”页面，原“申请”变为“申请中”，1~3个工作日内反馈申请结果，请留意互动中心的“服务开通申请”信息。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/bYvttnB6Ram0FAgMN9VX8A/zh-cn_image_0000002762994817.png)

   申请通过后，互动中心会发送通知给您，同时“申请中”会变为置灰显示的“申请”，至此，应用已成功开启Beacon围栏后台唤醒开放能力。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8f/v3/tCOEB3Q5T8m0wvlwdklZXg/zh-cn_image_0000002762834929.png)

### 获取蓝牙扫描信息

基于安全考虑，系统侧对获取蓝牙扫描信息功能做了权限保护处理，使用相关接口开发者需先提交“获取蓝牙扫描信息”能力开关的申请。

若您的鸿蒙应用需获取用户周围的蓝牙扫描信息，请在申请通过后，再使用该能力。

1. 登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)，选择“开发与服务”。
2. 在项目列表选择项目，并在应用列表下选择需要申请获取蓝牙扫描信息功能的应用。
3. 进入“项目设置 > 开放能力管理”页面，选择能力名称为定位服务（HarmonyOS NEXT），然后点击“获取蓝牙扫描信息”对应的“申请”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/13/v3/y_sWSRLpSVGXmc4fo8Ej5Q/zh-cn_image_0000002762994813.png)
4. 参考“申请原因”中的模板，提供申请必需的相关信息，包括应用介绍、使用场景、申请用途，然后点击“提交”按钮。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e5/v3/iwQgS2YYT2mWIO2FKt5gBg/zh-cn_image_0000002733275414.png)

   返回“开放能力管理”页面，原“申请”变为“申请中”，1~3个工作日内反馈申请结果，请留意互动中心的“服务开通申请”信息。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6d/v3/C0BrHzWIRhCfm8iXrUDvmQ/zh-cn_image_0000002733435296.png)

   申请通过后，互动中心会发送通知给您，同时“申请中”会变为置灰显示的“申请”，至此，应用已成功开启获取蓝牙扫描信息开放能力。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/Sg-Hy2WoSVigv188P1465w/zh-cn_image_0000002762994819.png)
