---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-insight-intent2
title: 意图装饰器生成和小艺智能体创建
breadcrumb: 指南 > 使用AI智能辅助编程 > 意图装饰器生成和小艺智能体创建
category: harmonyos-guides
scraped_at: 2026-04-29T13:45:13+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:75f9848d087001cefee6acf1f6c18a3729dbec09f2fd1f5e83b17a6cea4dcb50
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

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/8cwcjq0BTj6ItLIfM3PX1w/zh-cn_image_0000002530913144.png?HW-CC-KV=V1&HW-CC-Date=20260429T054512Z&HW-CC-Expire=86400&HW-CC-Sign=F3201BD9AF6E9415D0D6EC1080AF5B8E9DE8C659110E72C78D4F8450257DE473 "点击放大")
2. 在class头部或内部位置，右键选择 **CodeGenie > Insight Intent > Link Insight Intent**。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cb/v3/tIJ5APJxSLuzLDY2ENb4-Q/zh-cn_image_0000002561753097.png?HW-CC-KV=V1&HW-CC-Date=20260429T054512Z&HW-CC-Expire=86400&HW-CC-Sign=135FB60310FB5F391F02D418EC86FB977104E8BEB29CC417BE7714453A9FAF2C)
3. 意图装饰器自动添加至CodeGenie对话框中，可选择输入或不输入提示词，CodeGenie根据代码上下文分析输出结果。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b2/v3/AOcyDWJKQ5iV9HkIrbWnRg/zh-cn_image_0000002561753095.png?HW-CC-KV=V1&HW-CC-Date=20260429T054512Z&HW-CC-Expire=86400&HW-CC-Sign=34589987604F1CFA3BB43B7A76C48DB916FADC29ECCD872B33DB369201ADC5B5)
4. 生成结果后，点击对话框中生成代码块右上方的**插入**按钮，在class上方插入生成的代码。开发者可基于结果微调，实现意图调用。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/df/v3/8jYH3-W7TciGWOe3wjI6Vg/zh-cn_image_0000002530913156.png?HW-CC-KV=V1&HW-CC-Date=20260429T054512Z&HW-CC-Expire=86400&HW-CC-Sign=BF74775E11C772DDE5501BE0F4957A31555BABCF57FE6DADFD9BF9E68D830A4B)

### @InsightIntentPage装饰器

基于组件导航（Navigation）的子页面使用，@Component和struct需成对出现。

1. 在@Component头部\struct结构体内部\选中整个结构体区域，点击**右键 > CodeGenie > Insight Intent > Page Insight Intent**。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f3/v3/aON8OS2kR1OGT6pATNKyEQ/zh-cn_image_0000002561753099.png?HW-CC-KV=V1&HW-CC-Date=20260429T054512Z&HW-CC-Expire=86400&HW-CC-Sign=B945B0BDD9CF5C3E68A49E8D0D16F66579EA3B6E16897593C224A21C38E2F7C1)
2. 意图装饰器自动添加至CodeGenie对话框中，可选择输入或不输入提示词，CodeGenie根据代码上下文分析输出结果。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/56/v3/qldqYNKMQUG7ozSGmOkMaA/zh-cn_image_0000002561833081.png?HW-CC-KV=V1&HW-CC-Date=20260429T054512Z&HW-CC-Expire=86400&HW-CC-Sign=66F052B3A1D530502DE70464F32A1B740560DDE862EE6006D9FAFD5AB846D460)
3. 生成结果后，点击对话框中生成代码块右上方的**插入**按钮，在@Entry上方插入生成的代码。开发者可基于结果微调，实现意图调用。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b1/v3/Pxfsp2TDRhKUng53KWHyKA/zh-cn_image_0000002530753160.png?HW-CC-KV=V1&HW-CC-Date=20260429T054512Z&HW-CC-Expire=86400&HW-CC-Sign=A91AF5A0AA502499ECDDE156B33217F02AD105DF1A67DF3357F3E98E4A7E0F79)

### @InsightIntentFunction装饰器

1. 在类中静态方法区域，右键选择 **CodeGenie > Insight Intent > Function Insight Intent**。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e9/v3/yx0PphEQTIudPumEHfgExA/zh-cn_image_0000002530753166.png?HW-CC-KV=V1&HW-CC-Date=20260429T054512Z&HW-CC-Expire=86400&HW-CC-Sign=2CF7AE986342857B786D3A7583873F95A0BAF5C0BD244F684B276944E535CCE8)
2. 意图装饰器自动添加至CodeGenie对话框中，可选择输入或不输入提示词，CodeGenie根据代码上下文分析输出结果。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a9/v3/pdUWXTGFRqiBqDduI5FytQ/zh-cn_image_0000002561833085.png?HW-CC-KV=V1&HW-CC-Date=20260429T054512Z&HW-CC-Expire=86400&HW-CC-Sign=B5F29887F71948F16C3F1A36D787F34B5BEF1ABED46C1A0EAC12BF9655410B5F)
3. 生成结果后，点击对话框中生成代码块右上方的**插入**按钮，在class上方插入@InsightIntentFunction，在class内部插入@InsightIntentFunctionMethod生成内容。开发者可基于结果微调，实现意图调用。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/77/v3/mojtrCn6TEGRk6mFjVmbPA/zh-cn_image_0000002561833083.png?HW-CC-KV=V1&HW-CC-Date=20260429T054512Z&HW-CC-Expire=86400&HW-CC-Sign=142EB7A2290BE618CB4C56AD68A56149EC2653D0661A7E4645DF31DED192C5BD)

### @InsightIntentForm装饰器

1. 基于FormExtensionAbility使用，在继承FormExtensionAbility的class头部或内部，右键选择**CodeGenie > Insight Intent > Form Insight Intent**。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0a/v3/zVXM-uE3Tkq-2-RBNbW2qg/zh-cn_image_0000002561833069.png?HW-CC-KV=V1&HW-CC-Date=20260429T054512Z&HW-CC-Expire=86400&HW-CC-Sign=81C92D276A17D63B116D6A5DF54BEAC8D5E7D0755ED6AC7A66C146B26AD6A7B3)
2. 意图装饰器自动添加至CodeGenie对话框中，可选择输入或不输入提示词，CodeGenie根据代码上下文分析输出结果。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0a/v3/1SF2q9EURzayziPzqkRTRA/zh-cn_image_0000002561833067.png?HW-CC-KV=V1&HW-CC-Date=20260429T054512Z&HW-CC-Expire=86400&HW-CC-Sign=3335D231DEBD1ED4687E4968C0468073FB6166E16A7108BBA16CE24C6176676E)
3. 生成结果后，点击对话框中生成代码块右上方的**插入**按钮，在class上方插入生成的代码，开发者可基于结果微调，实现意图调用。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5c/v3/4EPj69diS3CyVId_TQ9f6Q/zh-cn_image_0000002561753107.png?HW-CC-KV=V1&HW-CC-Date=20260429T054512Z&HW-CC-Expire=86400&HW-CC-Sign=4CC41AF93B4D4099F1D73C9904E38708D51C5E82440F2F5D4C675BF00955A51A)

### @InsightIntentEntry装饰器

1. 基于InsightIntentEntryExecutor使用，在直接继承InsightIntentEntryExecutor的class头部或内部，右键选择**CodeGenie > Insight Intent > Entry Insight Intent**。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1b/v3/B1DSD8SHTqCRU9Wn-UUy6w/zh-cn_image_0000002530913148.png?HW-CC-KV=V1&HW-CC-Date=20260429T054512Z&HW-CC-Expire=86400&HW-CC-Sign=011AD959492ADBF90B76D608A98EAC8AE56D9A9236AD0E0A4F088467360B07F4)
2. 意图装饰器自动添加至CodeGenie对话框中，可选择输入或不输入提示词，CodeGenie根据代码上下文分析输出结果。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d5/v3/yiZ7aObQTIahn_SEo8sm8A/zh-cn_image_0000002561833075.png?HW-CC-KV=V1&HW-CC-Date=20260429T054512Z&HW-CC-Expire=86400&HW-CC-Sign=E7BB6CD9ABB079A022E1C18FE9A2DB6E95975217207E9732CA4120F5B48FC2C1)
3. 生成结果后，点击对话框中生成代码块右上方的**插入**按钮，在class上方插入生成的代码，开发者可基于结果微调，实现意图调用。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/66/v3/Fs4_afieR_2jwDGtPHbYrQ/zh-cn_image_0000002530753154.png?HW-CC-KV=V1&HW-CC-Date=20260429T054512Z&HW-CC-Expire=86400&HW-CC-Sign=7A8FF67F320D6D3D4A70CB4CAA2DB69540593F85DA9A1B4D1A9E91D15A2EC090)

## 生成意图插件和创建小艺智能体

1. 点击DevEco Studio右上角![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3a/v3/4I7rarm7Q3SNlwRWFnMOOg/zh-cn_image_0000002561753085.png?HW-CC-KV=V1&HW-CC-Date=20260429T054512Z&HW-CC-Expire=86400&HW-CC-Sign=E6EBC7058C821970C7F93C25E43986D6195619F8D7E153A46BF5AF2ADE3F8460)图标登录个人账号，再切换至个人所在的团队账号。

   说明

   * 个人账号需要完成实名认证，具体请参考[实名认证](../start/rna-0000001062530373.md)。
   * 如下企业开发者账号为某团队账号名称，仅供参考。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/WHWAsyRDRniyxwUktAgAMw/zh-cn_image_0000002530913162.png?HW-CC-KV=V1&HW-CC-Date=20260429T054512Z&HW-CC-Expire=86400&HW-CC-Sign=A24014B1C0DB3F6D830EBBE740DC517663894A69C5E8E2DEDAC94D90FDF1D9AF)
2. 在意图注解代码块内部任意位置，右键选择**CodeGenie > Add Intent Plugin**，生成的意图注解插件将注册到小艺智能平台中。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dc/v3/a0ZOw7PUQUesFVVpRS8qJg/zh-cn_image_0000002561833073.png?HW-CC-KV=V1&HW-CC-Date=20260429T054512Z&HW-CC-Expire=86400&HW-CC-Sign=ACDA98621DC31252940EA1096F1A26413D7E3440A909A09A8FF24BDDC34E8780)
3. 在DevEco Studio菜单栏点击**View > Tool Windows > Application Agent** ，打开内嵌的小艺智能平台新建智能体和添加插件。小艺智能平台更多具体操作可参考[鸿蒙智能体](../service/developer-guide-0000002469667881.md)。
