---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/location-apply-open-capability
title: 申请开放能力权限指导
breadcrumb: 指南 > 应用服务 > Location Kit（位置服务） > 开发准备 > 申请开放能力权限指导
category: harmonyos-guides
scraped_at: 2026-04-28T07:49:40+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:1111f21196336d0181c3204852ae32ff74c9a0ba48835eba9a55725ea9c5522a
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

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a4/v3/jHU4dZ_yShSQYbDaqqTRww/zh-cn_image_0000002583478987.png?HW-CC-KV=V1&HW-CC-Date=20260427T234939Z&HW-CC-Expire=86400&HW-CC-Sign=1EFB99473ADCC40094289D9DC217289DC10F86904ECE1B12A984D5CB3E6CF3A9)
4. 参考“申请原因”中的模板，提供申请必需的相关信息，包括应用介绍、使用场景、申请用途，然后点击“提交”按钮。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7b/v3/lZQXBw-FRUGuI6vm-d-7OQ/zh-cn_image_0000002552799338.png?HW-CC-KV=V1&HW-CC-Date=20260427T234939Z&HW-CC-Expire=86400&HW-CC-Sign=4B3BF975D7520F2F7ED8C95232EC08CFD2402B57F1168C0094BCE64C28A94406)

返回“开放能力管理”页面，原“申请”变为“申请中”，1~3个工作日内反馈申请结果，请留意互动中心的“服务开通申请”信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a3/v3/yARztH6-QjKLoMSlQp_ZJg/zh-cn_image_0000002583439033.png?HW-CC-KV=V1&HW-CC-Date=20260427T234939Z&HW-CC-Expire=86400&HW-CC-Sign=5727F7E0FDDAA14D569BA15A206CA9BD6921A1D2660D3E93584D68972994FF84)

申请通过后，互动中心会发送通知给您，同时“申请中”会变为置灰显示的“申请”，至此，应用已成功开启室内高精度定位开放能力。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/77/v3/aAbPISHUQu29b1cENj085g/zh-cn_image_0000002552958988.png?HW-CC-KV=V1&HW-CC-Date=20260427T234939Z&HW-CC-Expire=86400&HW-CC-Sign=D8E9AECEA458B7C8B27290E6748E749A952BF3E5B138CE92DBAC38B31FF96D21)

### 位置语义

为了更好的用户体验，系统侧对位置语义服务功能做了权限保护处理，使用相关接口开发者需先提交“位置语义”能力开关的申请。

若您的鸿蒙应用需感知用户周围的位置语义（如店铺、地铁站等）信息，请在申请通过后，再使用该能力。

1. 登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)，选择“开发与服务”。
2. 在项目列表选择项目，并在应用列表下选择需要申请位置语义功能的应用。
3. 进入“项目设置 > 开放能力管理”页面，选择能力名称为定位服务（HarmonyOS NEXT），然后点击“位置语义”对应的“申请”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/86/v3/xnmNqo12QwS257yHfmKhkA/zh-cn_image_0000002583478989.png?HW-CC-KV=V1&HW-CC-Date=20260427T234939Z&HW-CC-Expire=86400&HW-CC-Sign=0F0FB9C245AA35C8D976052F249AD02AB8CAF595CE8F2A8E6386F6290F82F107)
4. 参考“申请原因”中的模板，提供申请必需的相关信息，包括应用介绍、使用场景、申请用途，然后点击“提交”按钮。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/75/v3/ecwt7pc8SDidXluceaJMRQ/zh-cn_image_0000002552799340.png?HW-CC-KV=V1&HW-CC-Date=20260427T234939Z&HW-CC-Expire=86400&HW-CC-Sign=4ABDE6AC3FE5CCF20A642E5515F3C54CAC951EBB2B635F67C19D92B0803AA713)

   返回“开放能力管理”页面，原“申请”变为“申请中”，1~3个工作日内反馈申请结果，请留意互动中心的“服务开通申请”信息。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d3/v3/NXc4btaUSxC9gznBf1DZHw/zh-cn_image_0000002583439035.png?HW-CC-KV=V1&HW-CC-Date=20260427T234939Z&HW-CC-Expire=86400&HW-CC-Sign=986D4745A0BC623B125DF271C0E214077116AEF074F67AE2D3956CA85A9C6969)

   申请通过后，互动中心会发送通知给您，同时“申请中”会变为置灰显示的“申请”，至此，应用已成功开启位置语义开放能力。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/28/v3/1FlD_bfhTcq4IXPFPqbQXg/zh-cn_image_0000002552958990.png?HW-CC-KV=V1&HW-CC-Date=20260427T234939Z&HW-CC-Expire=86400&HW-CC-Sign=43A8A53AE31D101AD1148810C1711756CDEB445D996BCC25242C824FADD868C4)

### Beacon围栏后台唤醒

基于安全考虑，系统侧对Beacon围栏后台唤醒功能做了权限保护处理，使用相关接口开发者需先提交“Beacon围栏后台唤醒”能力开关的申请。

若您的鸿蒙应用在后台状态下需要接收用户进出围栏的事件通知，请在申请通过后，再使用该能力。

1. 登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)，选择“开发与服务”。
2. 在项目列表选择项目，并在应用列表下选择需要申请Beacon围栏后台唤醒功能的应用。
3. 进入“项目设置 > 开放能力管理”页面，选择能力名称为定位服务（HarmonyOS NEXT），然后点击“Beacon围栏后台唤醒”对应的“申请”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a8/v3/s5eDe6wATpm1Kc0ExcSZZg/zh-cn_image_0000002583478991.png?HW-CC-KV=V1&HW-CC-Date=20260427T234939Z&HW-CC-Expire=86400&HW-CC-Sign=7E382B6F509DE256B047724DB44D653F38263D207E01821957B85F06AD8DC42D)
4. 参考“申请原因”中的模板，提供申请必需的相关信息，包括应用介绍、使用场景、申请用途，然后点击“提交”按钮。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/97/v3/2sx4hANMRQmalJG3KxbLIw/zh-cn_image_0000002552799342.png?HW-CC-KV=V1&HW-CC-Date=20260427T234939Z&HW-CC-Expire=86400&HW-CC-Sign=5FC93C40911E2C7C2A9A8C7AC10F9B1E8767A4FF86BAC4361C50ACC08BA4B621)

   返回“开放能力管理”页面，原“申请”变为“申请中”，1~3个工作日内反馈申请结果，请留意互动中心的“服务开通申请”信息。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3e/v3/ktQy7GXgScCICEA3KmfVOA/zh-cn_image_0000002583439037.png?HW-CC-KV=V1&HW-CC-Date=20260427T234939Z&HW-CC-Expire=86400&HW-CC-Sign=B0F6AA666D6ED1F33A2045FB2CC56D3667372837384B78B7A4546ABEE14BFCD1)

   申请通过后，互动中心会发送通知给您，同时“申请中”会变为置灰显示的“申请”，至此，应用已成功开启Beacon围栏后台唤醒开放能力。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/62/v3/ju-k48pJRka_r4yddpEtuQ/zh-cn_image_0000002552958992.png?HW-CC-KV=V1&HW-CC-Date=20260427T234939Z&HW-CC-Expire=86400&HW-CC-Sign=F489893FC278A7CDC960AE1530ED9D33FDE1BD0DCC3135B1A4D316E7BCB72C4B)

### 获取蓝牙扫描信息

基于安全考虑，系统侧对获取蓝牙扫描信息功能做了权限保护处理，使用相关接口开发者需先提交“获取蓝牙扫描信息”能力开关的申请。

若您的鸿蒙应用需获取用户周围的蓝牙扫描信息，请在申请通过后，再使用该能力。

1. 登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)，选择“开发与服务”。
2. 在项目列表选择项目，并在应用列表下选择需要申请获取蓝牙扫描信息功能的应用。
3. 进入“项目设置 > 开放能力管理”页面，选择能力名称为定位服务（HarmonyOS NEXT），然后点击“获取蓝牙扫描信息”对应的“申请”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/67/v3/SeUOhnx1QeiTQp93bBACoQ/zh-cn_image_0000002583478993.png?HW-CC-KV=V1&HW-CC-Date=20260427T234939Z&HW-CC-Expire=86400&HW-CC-Sign=F872EAA993055837C31748466345EEE6B9458DF4FF6D9AFA6A26929F780AD524)
4. 参考“申请原因”中的模板，提供申请必需的相关信息，包括应用介绍、使用场景、申请用途，然后点击“提交”按钮。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d6/v3/PFwO5SCXRKiUz4FvJX5_CQ/zh-cn_image_0000002552799344.png?HW-CC-KV=V1&HW-CC-Date=20260427T234939Z&HW-CC-Expire=86400&HW-CC-Sign=02D4CD3AF6BB6FE5D7D769769B5652EC2ECD22E71D658F7C4861C248093C2007)

   返回“开放能力管理”页面，原“申请”变为“申请中”，1~3个工作日内反馈申请结果，请留意互动中心的“服务开通申请”信息。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e4/v3/bPsJUaivQ_mJEJIg8b3qQA/zh-cn_image_0000002583439039.png?HW-CC-KV=V1&HW-CC-Date=20260427T234939Z&HW-CC-Expire=86400&HW-CC-Sign=5B45FC64F4AA4E8B8C2C458926077694F2ED216D42BDB324835D02B29F582EC7)

   申请通过后，互动中心会发送通知给您，同时“申请中”会变为置灰显示的“申请”，至此，应用已成功开启获取蓝牙扫描信息开放能力。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/75/v3/t-vYmxYrRFKwj6J_9zbgCQ/zh-cn_image_0000002552958994.png?HW-CC-KV=V1&HW-CC-Date=20260427T234939Z&HW-CC-Expire=86400&HW-CC-Sign=BEEB3E2E9626BB5A42AD83008EB9C57B70208472FBA2DC96969E47B97BB089E7)
