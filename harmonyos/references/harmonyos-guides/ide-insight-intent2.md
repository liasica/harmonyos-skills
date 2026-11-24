---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-insight-intent2
title: 意图装饰器生成和小艺智能体创建
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 使用AI智能辅助编程（不推荐） > 意图装饰器生成和小艺智能体创建
category: harmonyos-guides
scraped_at: 2026-11-24T12:42:39+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:78588780e65a4066e5269dcfa53cc8d6cc2027810ed14adcf2a6aa7a23382730
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

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/LkV0pFMiT1OR3OoVF6Bk_w/zh-cn_image_0000002808766593.png?HW-CC-KV=V1&HW-CC-Date=20261124T044239Z&HW-CC-Expire=31536000000&HW-CC-Sign=74A106E907D828BF2A6FE1F83B239B5F6868A0BD0688A26A87A851074F4175E4 "点击放大")
2. 在class头部或内部位置，右键选择 **CodeGenie > Insight Intent > Link Insight Intent**。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bd/v3/XVddT8_aQeumBzYq1Is9Hg/zh-cn_image_0000002808886677.png?HW-CC-KV=V1&HW-CC-Date=20261124T044239Z&HW-CC-Expire=31536000000&HW-CC-Sign=C3453F507EF38ED454D5E75D066B0C98E3ABE8890EFDB447DEDDAA4B99A88FC5 "点击放大")
3. 意图装饰器自动添加至CodeGenie对话框中，可选择输入或不输入提示词，CodeGenie根据代码上下文分析输出结果。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/59/v3/_I2lC4V9ReqdYuRCLvqsoQ/zh-cn_image_0000002779567014.png?HW-CC-KV=V1&HW-CC-Date=20261124T044239Z&HW-CC-Expire=31536000000&HW-CC-Sign=F4ED8F213398102C000B5F17966B38998364E5AA4A499E6BE995A646169C8479 "点击放大")
4. 生成结果后，点击对话框中生成代码块右上方的**插入**按钮，在class上方插入生成的代码。开发者可基于结果微调，实现意图调用。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/ua_lebpnRrabun3I6PjCwA/zh-cn_image_0000002779407038.png?HW-CC-KV=V1&HW-CC-Date=20261124T044239Z&HW-CC-Expire=31536000000&HW-CC-Sign=01A775BAB88379FEFCCE6B736D3396AA363F77FCA4B6805B9AC043819F6E2C9A "点击放大")

### @InsightIntentPage装饰器

基于组件导航（Navigation）的子页面使用，@Component和struct需成对出现。

1. 在@Component头部\struct结构体内部\选中整个结构体区域，点击**右键 > CodeGenie > Insight Intent > Page Insight Intent**。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c6/v3/TusXR0mZRjuLy09tpsi-jw/zh-cn_image_0000002779567030.png?HW-CC-KV=V1&HW-CC-Date=20261124T044239Z&HW-CC-Expire=31536000000&HW-CC-Sign=A794487A8DE23A17ADD1AEACA364879C024BDFBCCA4B2FEEB311BDAE013D96A7 "点击放大")
2. 意图装饰器自动添加至CodeGenie对话框中，可选择输入或不输入提示词，CodeGenie根据代码上下文分析输出结果。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f7/v3/lfSjVq8eS2KMEbVNJWfkqg/zh-cn_image_0000002808766609.png?HW-CC-KV=V1&HW-CC-Date=20261124T044239Z&HW-CC-Expire=31536000000&HW-CC-Sign=D57434AB58A52443B28740DB50831208C64F51BAC238C247C12DD21B2AABB44F "点击放大")
3. 生成结果后，点击对话框中生成代码块右上方的**插入**按钮，在@Entry上方插入生成的代码。开发者可基于结果微调，实现意图调用。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/85/v3/yFaIO302QBWLiFITxweK0g/zh-cn_image_0000002779567020.png?HW-CC-KV=V1&HW-CC-Date=20261124T044239Z&HW-CC-Expire=31536000000&HW-CC-Sign=D380169C81471348FFD1BA58794D649EE168707FF0C395C5770E58E9E1AECD9B "点击放大")

### @InsightIntentFunction装饰器

1. 在类中静态方法区域，右键选择 **CodeGenie > Insight Intent > Function Insight Intent**。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a5/v3/XzKtERYVQOOd3wmVax3MRQ/zh-cn_image_0000002779567032.png?HW-CC-KV=V1&HW-CC-Date=20261124T044239Z&HW-CC-Expire=31536000000&HW-CC-Sign=D664257E134D6CE06D1D66AD837D42E49AE9FADC390D79820ADB584E2FE51DBF "点击放大")
2. 意图装饰器自动添加至CodeGenie对话框中，可选择输入或不输入提示词，CodeGenie根据代码上下文分析输出结果。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ef/v3/sZwck0qeQha-qYBKT9KmiQ/zh-cn_image_0000002779407040.png?HW-CC-KV=V1&HW-CC-Date=20261124T044239Z&HW-CC-Expire=31536000000&HW-CC-Sign=0F136640E7E9DD91BCE027A0D6DE068A47D7B4060F42B0D8A497E1268F48A9EF "点击放大")
3. 生成结果后，点击对话框中生成代码块右上方的**插入**按钮，在class上方插入@InsightIntentFunction，在class内部插入@InsightIntentFunctionMethod生成内容。开发者可基于结果微调，实现意图调用。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dd/v3/C2wtakB4RfeDkj7qA7p0NA/zh-cn_image_0000002808886683.png?HW-CC-KV=V1&HW-CC-Date=20261124T044239Z&HW-CC-Expire=31536000000&HW-CC-Sign=2F75E40D4FAD9D4AD5FEFBA0FA9A1E22243B5AAC9A582116E69E1FF4B1E35E82 "点击放大")

### @InsightIntentForm装饰器

1. 基于FormExtensionAbility使用，在继承FormExtensionAbility的class头部或内部，右键选择**CodeGenie > Insight Intent > Form Insight Intent**。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/50/v3/Y0c99_JMTQaNnEYNfAJ1uw/zh-cn_image_0000002808766605.png?HW-CC-KV=V1&HW-CC-Date=20261124T044239Z&HW-CC-Expire=31536000000&HW-CC-Sign=6D6B08DE02C968566D136868F485019C9C49BC59E9FA4ABA5AB00ECE4425FD47 "点击放大")
2. 意图装饰器自动添加至CodeGenie对话框中，可选择输入或不输入提示词，CodeGenie根据代码上下文分析输出结果。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c/v3/uqgeGSgmQ3qAUdUna4zRvQ/zh-cn_image_0000002779567026.png?HW-CC-KV=V1&HW-CC-Date=20261124T044239Z&HW-CC-Expire=31536000000&HW-CC-Sign=B57C8C064E0E364B15D88457ED88514E0B081C87125A666667B5243AEA354594 "点击放大")
3. 生成结果后，点击对话框中生成代码块右上方的**插入**按钮，在class上方插入生成的代码，开发者可基于结果微调，实现意图调用。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/36/v3/fiFl29sHT7K49R8VaY7Z4g/zh-cn_image_0000002779407044.png?HW-CC-KV=V1&HW-CC-Date=20261124T044239Z&HW-CC-Expire=31536000000&HW-CC-Sign=62390D228FF7AA3646CA8FD444632B713C0E72C4E0E984786A01C224E113F802 "点击放大")

### @InsightIntentEntry装饰器

1. 基于InsightIntentEntryExecutor使用，在直接继承InsightIntentEntryExecutor的class头部或内部，右键选择**CodeGenie > Insight Intent > Entry Insight Intent**。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8e/v3/Djj8TLUBRAyQ_GbKLB69-Q/zh-cn_image_0000002779567034.png?HW-CC-KV=V1&HW-CC-Date=20261124T044239Z&HW-CC-Expire=31536000000&HW-CC-Sign=0CB6992FB628079DB2FC2D8D9D0AF0C741E6FB0422D34B2C52AB191B060DC040 "点击放大")
2. 意图装饰器自动添加至CodeGenie对话框中，可选择输入或不输入提示词，CodeGenie根据代码上下文分析输出结果。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d4/v3/p0O1rdpZST-EnqOSKQ_Hpw/zh-cn_image_0000002808766613.png?HW-CC-KV=V1&HW-CC-Date=20261124T044239Z&HW-CC-Expire=31536000000&HW-CC-Sign=DC051C01BEF7CEAFDEEE2CBC112380ADAFFCD436EDAFC55DEDCBC8C33B2652B3 "点击放大")
3. 生成结果后，点击对话框中生成代码块右上方的**插入**按钮，在class上方插入生成的代码，开发者可基于结果微调，实现意图调用。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a/v3/Jye1Mp9aTMyeej9EhtCUwg/zh-cn_image_0000002779567024.png?HW-CC-KV=V1&HW-CC-Date=20261124T044239Z&HW-CC-Expire=31536000000&HW-CC-Sign=B21478BD8C660FB8034D19F69DB11E9B7D47F750500B216928B32364B8525D4F "点击放大")

## 生成意图插件和创建小艺智能体

1. 点击DevEco Studio右上角![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/11/v3/23p2MqzoS_2kydaW3fGUyg/zh-cn_image_0000002808886673.png?HW-CC-KV=V1&HW-CC-Date=20261124T044239Z&HW-CC-Expire=31536000000&HW-CC-Sign=424E31AAEBC782B2079979C27C660C453EC130483CCC2B75B33AA2BD8C91F6B9)图标登录个人账号，再切换至个人所在的团队账号。

   **说明** 

   * 个人账号需要完成实名认证。
   * 如下企业开发者账号为某团队账号名称，仅供参考。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f4/v3/EC8DXP1ZT1-JkOhOgbU_hg/zh-cn_image_0000002808766591.png?HW-CC-KV=V1&HW-CC-Date=20261124T044239Z&HW-CC-Expire=31536000000&HW-CC-Sign=F116010E02997ECB94C41C9973BBD9BA9136AAADD52DA59F36C462CCBF2E08EA)
2. 在意图注解代码块内部任意位置，右键选择**CodeGenie > Add Intent Plugin**，生成的意图注解插件将注册到小艺智能平台中。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b3/v3/dZbzuFHWTsONYML5P9bigA/zh-cn_image_0000002808886689.png?HW-CC-KV=V1&HW-CC-Date=20261124T044239Z&HW-CC-Expire=31536000000&HW-CC-Sign=FA7B396BCE743AFB85A5ABE00C0543E34A06FDC91541D9CF4692D9BEB8BE9944 "点击放大")
3. 在DevEco Studio菜单栏点击**View > Tool Windows > Application Agent** ，打开内嵌的小艺智能平台新建智能体和添加插件。
