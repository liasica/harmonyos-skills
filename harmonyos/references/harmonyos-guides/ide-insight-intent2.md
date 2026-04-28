---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-insight-intent2
title: 意图装饰器生成和小艺智能体创建
breadcrumb: 指南 > 使用AI智能辅助编程 > 意图装饰器生成和小艺智能体创建
category: harmonyos-guides
scraped_at: 2026-04-28T07:55:17+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:25dafdc61115e0bec977dfc3e301f19f20951bd3ae3e00081a20f7d9cc0e4ca3
---

通过装饰类或方法可以将应用的功能定义为"意图"，然后将应用功能以"意图"形式集成至系统入口。用户通过系统入口（如语音助手、智能推荐卡片）触发意图执行，即可便捷使用应用提供的功能。

从DevEco Studio 6.0.0 Beta2开始，CodeGenie新增通过装饰器开发意图的功能，支持生成五类意图装饰器。同时，DevEco Studio新增Application Agent入口，通过该入口可完成意图插件注册、智能体创建等，提升开发效率。

## 使用约束

* 使用API 20及以上版本。
* 仅支持使用团队账号登录时，添加意图插件。个人加入目标团队方式具体可参考[添加成员](../app/agc-help-manageaccount-0000002306610129.md#section151241455193313)。
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

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f0/v3/OGWVJD0uT9qB5Yaz10mBTg/zh-cn_image_0000002530913144.png?HW-CC-KV=V1&HW-CC-Date=20260427T235515Z&HW-CC-Expire=86400&HW-CC-Sign=6E3F116DCE8962DE84A0FAD725143876837FA1F74297855DEE1237A0EB9815A1 "点击放大")
2. 在class头部或内部位置，右键选择 **CodeGenie > Insight Intent > Link Insight Intent**。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/69/v3/Ho5FkNiBTYugqhiEouMFuA/zh-cn_image_0000002561753097.png?HW-CC-KV=V1&HW-CC-Date=20260427T235515Z&HW-CC-Expire=86400&HW-CC-Sign=8A6631B713522DA6C51EE1AFE5A78C3FE12FAB922E2FBACE8BC5735F47DFAF39)
3. 意图装饰器自动添加至CodeGenie对话框中，可选择输入或不输入提示词，CodeGenie根据代码上下文分析输出结果。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/23/v3/RcN0es5MSkyQuy0Gne0D3g/zh-cn_image_0000002561753095.png?HW-CC-KV=V1&HW-CC-Date=20260427T235515Z&HW-CC-Expire=86400&HW-CC-Sign=222B0828492E16B40DA301A8323A07677EF5AC7700CFD31C99469704F47FA74E)
4. 生成结果后，点击对话框中生成代码块右上方的**插入**按钮，在class上方插入生成的代码。开发者可基于结果微调，实现意图调用。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/33/v3/Hg8nT6shRFymht3nBKU-pg/zh-cn_image_0000002530913156.png?HW-CC-KV=V1&HW-CC-Date=20260427T235515Z&HW-CC-Expire=86400&HW-CC-Sign=FB55A778F3C5739292CAE6DDD0BB7C9CED47715FA15DD839F7B97BF5AA6659F6)

### @InsightIntentPage装饰器

基于组件导航（Navigation）的子页面使用，@Component和struct需成对出现。

1. 在@Component头部\struct结构体内部\选中整个结构体区域，点击**右键 > CodeGenie > Insight Intent > Page Insight Intent**。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ac/v3/sqswq9WPTy-i9FcJ209K-Q/zh-cn_image_0000002561753099.png?HW-CC-KV=V1&HW-CC-Date=20260427T235515Z&HW-CC-Expire=86400&HW-CC-Sign=BD6EA6F7444C62970244A19346CCBA864224980CE676296106A0EF2E212E159B)
2. 意图装饰器自动添加至CodeGenie对话框中，可选择输入或不输入提示词，CodeGenie根据代码上下文分析输出结果。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b4/v3/UY901sbTR9q-9tIYR6WOfA/zh-cn_image_0000002561833081.png?HW-CC-KV=V1&HW-CC-Date=20260427T235515Z&HW-CC-Expire=86400&HW-CC-Sign=175361F959A3794CB1EECF3DB34533F0E9F628F354653AEE0EAA5D0CA10AC3B7)
3. 生成结果后，点击对话框中生成代码块右上方的**插入**按钮，在@Entry上方插入生成的代码。开发者可基于结果微调，实现意图调用。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/27/v3/Qn_EMiKZTvyQqRGQoZ7gxQ/zh-cn_image_0000002530753160.png?HW-CC-KV=V1&HW-CC-Date=20260427T235515Z&HW-CC-Expire=86400&HW-CC-Sign=763F2EB9F175A1A0CE3AD8A87A7A7CC11437CE723337BB7CE5C8CB6F86A8EEB0)

### @InsightIntentFunction装饰器

1. 在类中静态方法区域，右键选择 **CodeGenie > Insight Intent > Function Insight Intent**。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b1/v3/TYj5stg_SiaYtso9gCrU5g/zh-cn_image_0000002530753166.png?HW-CC-KV=V1&HW-CC-Date=20260427T235515Z&HW-CC-Expire=86400&HW-CC-Sign=7A8879ECD3C8DA12D8AB844589D876775C67547F120F053026CD9FF505A64219)
2. 意图装饰器自动添加至CodeGenie对话框中，可选择输入或不输入提示词，CodeGenie根据代码上下文分析输出结果。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/96/v3/8qXYHkOAQiKl02VtETgRCw/zh-cn_image_0000002561833085.png?HW-CC-KV=V1&HW-CC-Date=20260427T235515Z&HW-CC-Expire=86400&HW-CC-Sign=CCB17AEE6E441690A0D1DC2EBE120F64F949377EFE365727A1F4CDDF4B45F072)
3. 生成结果后，点击对话框中生成代码块右上方的**插入**按钮，在class上方插入@InsightIntentFunction，在class内部插入@InsightIntentFunctionMethod生成内容。开发者可基于结果微调，实现意图调用。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/NUBLgr_3RBi6POtGDK2YjA/zh-cn_image_0000002561833083.png?HW-CC-KV=V1&HW-CC-Date=20260427T235515Z&HW-CC-Expire=86400&HW-CC-Sign=0495CE42ACA66915E771830625327DCBAF04638A07306F82E48EC274CFA54F1E)

### @InsightIntentForm装饰器

1. 基于FormExtensionAbility使用，在继承FormExtensionAbility的class头部或内部，右键选择**CodeGenie > Insight Intent > Form Insight Intent**。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/hxp5Y5GAREm7NwQs4AQ61Q/zh-cn_image_0000002561833069.png?HW-CC-KV=V1&HW-CC-Date=20260427T235515Z&HW-CC-Expire=86400&HW-CC-Sign=8E328D4344F296F5B958252067A905F2ED40CD2560FEA2E5C76782D60F5F31A3)
2. 意图装饰器自动添加至CodeGenie对话框中，可选择输入或不输入提示词，CodeGenie根据代码上下文分析输出结果。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0/v3/2ZXWh-9KSSWlLKoeuL7foA/zh-cn_image_0000002561833067.png?HW-CC-KV=V1&HW-CC-Date=20260427T235515Z&HW-CC-Expire=86400&HW-CC-Sign=9F54837EBD125B65AD35CD5242BACF57FC6FBDD370CA625343424894EC8E5BF0)
3. 生成结果后，点击对话框中生成代码块右上方的**插入**按钮，在class上方插入生成的代码，开发者可基于结果微调，实现意图调用。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/17/v3/rAScU2n3RyCKMlbAizRcjQ/zh-cn_image_0000002561753107.png?HW-CC-KV=V1&HW-CC-Date=20260427T235515Z&HW-CC-Expire=86400&HW-CC-Sign=B2FDB716D6766C34E683F0DB1467262390492DADE44D5F4F09E08076DA2052F3)

### @InsightIntentEntry装饰器

1. 基于InsightIntentEntryExecutor使用，在直接继承InsightIntentEntryExecutor的class头部或内部，右键选择**CodeGenie > Insight Intent > Entry Insight Intent**。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/84/v3/5EkXjcZHRF2rfkNiew73cA/zh-cn_image_0000002530913148.png?HW-CC-KV=V1&HW-CC-Date=20260427T235515Z&HW-CC-Expire=86400&HW-CC-Sign=3A401B1843C9E2BF012F44993E594FBA20DF564A65BA324DAEEBC9A0B7D476CD)
2. 意图装饰器自动添加至CodeGenie对话框中，可选择输入或不输入提示词，CodeGenie根据代码上下文分析输出结果。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7f/v3/9V9PBHTyTLKoM6uFNyDN2g/zh-cn_image_0000002561833075.png?HW-CC-KV=V1&HW-CC-Date=20260427T235515Z&HW-CC-Expire=86400&HW-CC-Sign=EE02930411EA1B92C699D7C1079F1AE6ACB5DC948AA53E77C401D4F66ECE2EED)
3. 生成结果后，点击对话框中生成代码块右上方的**插入**按钮，在class上方插入生成的代码，开发者可基于结果微调，实现意图调用。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d3/v3/3MU5-AK_SFKrJEaoCqhJsQ/zh-cn_image_0000002530753154.png?HW-CC-KV=V1&HW-CC-Date=20260427T235515Z&HW-CC-Expire=86400&HW-CC-Sign=F5C250A358B916508B93CF13147E570705006366838420D55F793DCCDB38C669)

## 生成意图插件和创建小艺智能体

1. 点击DevEco Studio右上角![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ec/v3/oaw2O-SITgiXOQjPFLP4Pg/zh-cn_image_0000002561753085.png?HW-CC-KV=V1&HW-CC-Date=20260427T235515Z&HW-CC-Expire=86400&HW-CC-Sign=3E4CABF36DAD2B9F4D4BD709C5ADAEFCFC23599F28B22539899F6E3498951B2E)图标登录个人账号，再切换至个人所在的团队账号。

   说明

   * 个人账号需要完成实名认证，具体请参考[实名认证](../start/rna-0000001062530373.md)。
   * 如下企业开发者账号为某团队账号名称，仅供参考。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/36/v3/4_KTFXBERjSaYvvFEfrnTQ/zh-cn_image_0000002530913162.png?HW-CC-KV=V1&HW-CC-Date=20260427T235515Z&HW-CC-Expire=86400&HW-CC-Sign=C0A01D0D055D216203ACE816F00E584760B5BB2B33978ACC753BE6B07DC0379A)
2. 在意图注解代码块内部任意位置，右键选择**CodeGenie > Add Intent Plugin**，生成的意图注解插件将注册到小艺智能平台中。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/CzlqnuJAQCKqeK6hIQpDbg/zh-cn_image_0000002561833073.png?HW-CC-KV=V1&HW-CC-Date=20260427T235515Z&HW-CC-Expire=86400&HW-CC-Sign=B759C0460BEDC47394846238A747B036977FAA2295CB8DDBFE548737253D4F0D)
3. 在DevEco Studio菜单栏点击**View > Tool Windows > Application Agent** ，打开内嵌的小艺智能平台新建智能体和添加插件。小艺智能平台更多具体操作可参考[鸿蒙智能体](../service/developer-guide-0000002469667881.md)。
