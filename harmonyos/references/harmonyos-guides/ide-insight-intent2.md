---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-insight-intent2
title: 意图装饰器生成和小艺智能体创建
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 使用AI智能辅助编程（不推荐） > 意图装饰器生成和小艺智能体创建
category: harmonyos-guides
scraped_at: 2026-11-28T10:34:48+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:dc4c98d6616367fc06d161dae20c11143cb0e8691a87f8ad7f357e56791b3ecd
---

通过装饰类或方法可以将应用的功能定义为"意图"，然后将应用功能以"意图"形式集成至系统入口。用户通过系统入口（如语音助手、智能推荐卡片）触发意图执行，即可便捷使用应用提供的功能。

从DevEco Studio 6.0.0 Beta2开始，CodeGenie新增通过装饰器开发意图的功能，支持生成五类意图装饰器。同时，DevEco Studio新增Application Agent入口，通过该入口可完成意图插件注册、智能体创建等，提升开发效率。

## 使用约束

* 使用API 20及以上版本。
* 仅支持使用团队账号登录时，添加意图插件。
* 应用在AGC已注册，具体可参考[创建HarmonyOS应用](../app/agc-help-create-app-0000002247955506.md#section1772711713288)。
* 生成意图装饰器时使用HarmonyOS Ask智能体。

## 意图装饰器分类

CodeGenie提供了几类意图装饰器，开发者可根据业务场景进行选择，具体请参考[意图装饰器定义](../harmonyos-references/js-apis-app-ability-insightintentdecorator.md)：

* @InsightIntentLink装饰器：在class头部或内部位置唤起意图装饰器，在class上方插入生成的代码。
* @InsightIntentPage装饰器：在@Component头部/struct结构体内部/选中整个结构体区域唤起意图装饰器，在@Entry上方插入生成的代码。
* @InsightIntentFunction装饰器：在类中静态方法区域唤起意图装饰器，在class上方插入@InsightIntentFunction，在class内部插入@InsightIntentFunctionMethod生成内容。
* @InsightIntentForm装饰器：在继承FormExtensionAbility的class头部或内部唤起意图装饰器，在class上方插入生成的代码。
* @InsightIntentEntry装饰器：在直接继承InsightIntentEntryExecutor的class头部或内部唤起意图装饰器，在class上方插入生成的代码。

### @InsightIntentLink装饰器

1. 打开module.json5文件，配置**abilities > skills > uris**字段。uri格式要求请参考[应用链接说明](app-uri-config.md)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b/v3/3URmDdywSLuYiYd6zbXDdA/zh-cn_image_0000002808766593.png?HW-CC-KV=V1&HW-CC-Date=20261128T023448Z&HW-CC-Expire=31536000000&HW-CC-Sign=3F878D007F59356F82906C41660B92F6826D4BA83F6B7FEF9617BA4188D03855 "点击放大")
2. 在class头部或内部位置，右键选择 **CodeGenie > Insight Intent > Link Insight Intent**。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ca/v3/C87Ud7-dSJ-SPKf63zOsgA/zh-cn_image_0000002808886677.png?HW-CC-KV=V1&HW-CC-Date=20261128T023448Z&HW-CC-Expire=31536000000&HW-CC-Sign=12AFF8D2978C82404ABCD9D510423E9436D8E49D2E709335E7AA1AA0BA5A283F "点击放大")
3. 意图装饰器自动添加至CodeGenie对话框中，可选择输入或不输入提示词，CodeGenie根据代码上下文分析输出结果。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c6/v3/HG19EXDtRrquTlYtDLbvnw/zh-cn_image_0000002779567014.png?HW-CC-KV=V1&HW-CC-Date=20261128T023448Z&HW-CC-Expire=31536000000&HW-CC-Sign=B11F87F15316C85C0C4B288C66ED5CB8B4A3EF8B376A850639D0008A0F06BDA5 "点击放大")
4. 生成结果后，点击对话框中生成代码块右上方的**插入**按钮，在class上方插入生成的代码。开发者可基于结果微调，实现意图调用。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/39/v3/154JWi0yRwOWS0HR_CcbDQ/zh-cn_image_0000002779407038.png?HW-CC-KV=V1&HW-CC-Date=20261128T023448Z&HW-CC-Expire=31536000000&HW-CC-Sign=639DE2ABC1F295734747DAC5C79256B2FC686DDFB713C3A3A493DA3009987853 "点击放大")

### @InsightIntentPage装饰器

基于组件导航（Navigation）的子页面使用，@Component和struct需成对出现。

1. 在@Component头部\struct结构体内部\选中整个结构体区域，点击**右键 > CodeGenie > Insight Intent > Page Insight Intent**。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8b/v3/oJiGvPghSIOlXMQhHDLdCg/zh-cn_image_0000002779567030.png?HW-CC-KV=V1&HW-CC-Date=20261128T023448Z&HW-CC-Expire=31536000000&HW-CC-Sign=BB88F2809A1C57007A5365B2CD957A2BC7AEE836D2468305F6558CCBF8F3A4E9 "点击放大")
2. 意图装饰器自动添加至CodeGenie对话框中，可选择输入或不输入提示词，CodeGenie根据代码上下文分析输出结果。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3c/v3/g-HEXtV2Sau0PIBihy2dLA/zh-cn_image_0000002808766609.png?HW-CC-KV=V1&HW-CC-Date=20261128T023448Z&HW-CC-Expire=31536000000&HW-CC-Sign=95086B6650AE15998CFDBDB324ABB233DC43DDCDF7E1FEDB737B49541B6415BF "点击放大")
3. 生成结果后，点击对话框中生成代码块右上方的**插入**按钮，在@Entry上方插入生成的代码。开发者可基于结果微调，实现意图调用。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2/v3/u727FccASGigtc8R5CWnAA/zh-cn_image_0000002779567020.png?HW-CC-KV=V1&HW-CC-Date=20261128T023448Z&HW-CC-Expire=31536000000&HW-CC-Sign=0DB18F3997355CE95475440CBFB6E71BE7CBC093D791F5246D75405DE4FA0D6D "点击放大")

### @InsightIntentFunction装饰器

1. 在类中静态方法区域，右键选择 **CodeGenie > Insight Intent > Function Insight Intent**。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8f/v3/gou3EwkJR0i7UrfLkuOgPw/zh-cn_image_0000002779567032.png?HW-CC-KV=V1&HW-CC-Date=20261128T023448Z&HW-CC-Expire=31536000000&HW-CC-Sign=F350B5FB2540DCC14E95F9B7297D6AD57ED648CF5980462E40FFC714ABF07931 "点击放大")
2. 意图装饰器自动添加至CodeGenie对话框中，可选择输入或不输入提示词，CodeGenie根据代码上下文分析输出结果。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/24/v3/YOU62hwvSM2-Rn817j0xtg/zh-cn_image_0000002779407040.png?HW-CC-KV=V1&HW-CC-Date=20261128T023448Z&HW-CC-Expire=31536000000&HW-CC-Sign=BF84B889BEE1BC25D766DB956D158A38AA5F5EB38898769E151458614E854D25 "点击放大")
3. 生成结果后，点击对话框中生成代码块右上方的**插入**按钮，在class上方插入@InsightIntentFunction，在class内部插入@InsightIntentFunctionMethod生成内容。开发者可基于结果微调，实现意图调用。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e6/v3/Y8igZ_5TS36hvicMeuGpJg/zh-cn_image_0000002808886683.png?HW-CC-KV=V1&HW-CC-Date=20261128T023448Z&HW-CC-Expire=31536000000&HW-CC-Sign=6E693D2042045DE45CA9D6ECD4F774C80FAAC3878DA799A210659932E8FC721C "点击放大")

### @InsightIntentForm装饰器

1. 基于FormExtensionAbility使用，在继承FormExtensionAbility的class头部或内部，右键选择**CodeGenie > Insight Intent > Form Insight Intent**。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a0/v3/M0t1h3SqT1e8EHWj0IjZIQ/zh-cn_image_0000002808766605.png?HW-CC-KV=V1&HW-CC-Date=20261128T023448Z&HW-CC-Expire=31536000000&HW-CC-Sign=023B01BD2A725F17788B2B8383B22455481E5FF6F3F23EFB129576852CF63E6D "点击放大")
2. 意图装饰器自动添加至CodeGenie对话框中，可选择输入或不输入提示词，CodeGenie根据代码上下文分析输出结果。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/61/v3/H0NQm817T6SgAy4PUTGH6Q/zh-cn_image_0000002779567026.png?HW-CC-KV=V1&HW-CC-Date=20261128T023448Z&HW-CC-Expire=31536000000&HW-CC-Sign=D85087024197006CB739613FC4BA7EEE9112D0209E22994AF6618ED3389081A2 "点击放大")
3. 生成结果后，点击对话框中生成代码块右上方的**插入**按钮，在class上方插入生成的代码，开发者可基于结果微调，实现意图调用。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5d/v3/y8RDwd3TSEiciabAzvJ7oA/zh-cn_image_0000002779407044.png?HW-CC-KV=V1&HW-CC-Date=20261128T023448Z&HW-CC-Expire=31536000000&HW-CC-Sign=9E055053AF41F341FD4F870B7DBAFCDCD7A781E84997D83C1922D0146297B927 "点击放大")

### @InsightIntentEntry装饰器

1. 基于InsightIntentEntryExecutor使用，在直接继承InsightIntentEntryExecutor的class头部或内部，右键选择**CodeGenie > Insight Intent > Entry Insight Intent**。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5d/v3/5ze8u9NSSdKOQuxtnzPsIA/zh-cn_image_0000002779567034.png?HW-CC-KV=V1&HW-CC-Date=20261128T023448Z&HW-CC-Expire=31536000000&HW-CC-Sign=1289707A925F7B8F3A1C77401C882B1FD939BF54A0777AF7C251816E39CD28DC "点击放大")
2. 意图装饰器自动添加至CodeGenie对话框中，可选择输入或不输入提示词，CodeGenie根据代码上下文分析输出结果。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d3/v3/HMjDcMNjQMawQF6-vt7bPw/zh-cn_image_0000002808766613.png?HW-CC-KV=V1&HW-CC-Date=20261128T023448Z&HW-CC-Expire=31536000000&HW-CC-Sign=CBD9EB43A630248E2EA0B5F4796AA119FEC4A5DC5912C113299AC9F702C545BA "点击放大")
3. 生成结果后，点击对话框中生成代码块右上方的**插入**按钮，在class上方插入生成的代码，开发者可基于结果微调，实现意图调用。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/19/v3/tPzoMoKtTIWBpU6KtiTOdw/zh-cn_image_0000002779567024.png?HW-CC-KV=V1&HW-CC-Date=20261128T023448Z&HW-CC-Expire=31536000000&HW-CC-Sign=A3D7FA6102513EDD0995E39DAFFE084107F7BF32498B9220201CC307557A8415 "点击放大")

## 生成意图插件和创建小艺智能体

1. 点击DevEco Studio右上角![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a7/v3/wnDq6G1cRYCwFNckf7xFKA/zh-cn_image_0000002808886673.png?HW-CC-KV=V1&HW-CC-Date=20261128T023448Z&HW-CC-Expire=31536000000&HW-CC-Sign=6BC911A5423134166D21B04B113423310DFFF2DB9C66EBC224751ECF30497EAD)图标登录个人账号，再切换至个人所在的团队账号。

   **说明** 

   * 个人账号需要完成实名认证。
   * 如下企业开发者账号为某团队账号名称，仅供参考。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/41/v3/818pqSzJTs-w1d1844HTRA/zh-cn_image_0000002808766591.png?HW-CC-KV=V1&HW-CC-Date=20261128T023448Z&HW-CC-Expire=31536000000&HW-CC-Sign=14B58C17A4C0FEF6CB6107B794A07C104E5108A46C3DDD491E2040A396BE7A9D)
2. 在意图注解代码块内部任意位置，右键选择**CodeGenie > Add Intent Plugin**，生成的意图注解插件将注册到小艺智能平台中。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a6/v3/uAruIY3MRY2JuG2Or9AMEQ/zh-cn_image_0000002808886689.png?HW-CC-KV=V1&HW-CC-Date=20261128T023448Z&HW-CC-Expire=31536000000&HW-CC-Sign=5BADCF783645B265591EF1D949FA6B5E91C820ADB703F3F0AC3B4337B09ACBF4 "点击放大")
3. 在DevEco Studio菜单栏点击**View > Tool Windows > Application Agent** ，打开内嵌的小艺智能平台新建智能体和添加插件。
