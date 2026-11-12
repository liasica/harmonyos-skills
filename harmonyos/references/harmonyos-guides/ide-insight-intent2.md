---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-insight-intent2
title: 意图装饰器生成和小艺智能体创建
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 使用AI智能辅助编程（不推荐） > 意图装饰器生成和小艺智能体创建
category: harmonyos-guides
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:6e0d520a17cc4315e285ddae20a0b10b4eaca7b4a2a49a51cdef9d5de70d2b52
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

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f3/v3/wJhfypNeStaCW581u0N2fA/zh-cn_image_0000002808766593.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=E736CD602E3215F0E7A67904462C3D6771AD2A89B6E6F3CCFE2125F2F26C5A05 "点击放大")
2. 在class头部或内部位置，右键选择 **CodeGenie > Insight Intent > Link Insight Intent**。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a2/v3/LC-58e4_TT2LG0s-iXUruw/zh-cn_image_0000002808886677.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=02542B02D5CD3B4D2183FC3E53AABC58FEC1A2BFABEDC675A0BC34F62D4C78FB "点击放大")
3. 意图装饰器自动添加至CodeGenie对话框中，可选择输入或不输入提示词，CodeGenie根据代码上下文分析输出结果。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/15/v3/4hoEuYLLSIaEjyrXOBon1w/zh-cn_image_0000002779567014.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=9DFBBB6121D8656B0410FF63453375316B100F8E53DCD789B2054669E866E2A4 "点击放大")
4. 生成结果后，点击对话框中生成代码块右上方的**插入**按钮，在class上方插入生成的代码。开发者可基于结果微调，实现意图调用。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/WNQGSoWOSFSEQYCiZ5N1IQ/zh-cn_image_0000002779407038.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=74B9EEF9BC8C727EB2CA0FD93F77EBCB8403B60D861C8B8D48D752669CDAA68B "点击放大")

### @InsightIntentPage装饰器

基于组件导航（Navigation）的子页面使用，@Component和struct需成对出现。

1. 在@Component头部\struct结构体内部\选中整个结构体区域，点击**右键 > CodeGenie > Insight Intent > Page Insight Intent**。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ac/v3/v2DXDV5MTWKl4Azmp-a5Jg/zh-cn_image_0000002779567030.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=14945020FC19E02B41250BF2D25335D3F34EF7A3984486B1DA81DB0C2457F9CD "点击放大")
2. 意图装饰器自动添加至CodeGenie对话框中，可选择输入或不输入提示词，CodeGenie根据代码上下文分析输出结果。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/99/v3/uPmPFtZMQ_y3Y2xwDkaZMg/zh-cn_image_0000002808766609.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=478D456ABAB2F0988933FF42813D52BADD43369946DE44C17BF205519214E13F "点击放大")
3. 生成结果后，点击对话框中生成代码块右上方的**插入**按钮，在@Entry上方插入生成的代码。开发者可基于结果微调，实现意图调用。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f6/v3/URsi5Xi9S0mMKq9-pTeGTg/zh-cn_image_0000002779567020.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=782EE4D8C9D0258567318442F729DE62FAED4450406639DCBBFE982F400D05B2 "点击放大")

### @InsightIntentFunction装饰器

1. 在类中静态方法区域，右键选择 **CodeGenie > Insight Intent > Function Insight Intent**。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/60/v3/0dYohHvhQ2qEnXfGlQM7Bw/zh-cn_image_0000002779567032.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=D66BFF09F621CE4290951DF2D9A222A8E063FB2307992689D165813CB8A6F295 "点击放大")
2. 意图装饰器自动添加至CodeGenie对话框中，可选择输入或不输入提示词，CodeGenie根据代码上下文分析输出结果。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/36/v3/I6ANOK7JTOqpaLKcRBX-vA/zh-cn_image_0000002779407040.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=7658D6DED8F8DCEEB32D2B066BEA88831C12F4412C089BC900325AD45A634B2C "点击放大")
3. 生成结果后，点击对话框中生成代码块右上方的**插入**按钮，在class上方插入@InsightIntentFunction，在class内部插入@InsightIntentFunctionMethod生成内容。开发者可基于结果微调，实现意图调用。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1c/v3/nfL3JysPShay9i0PHpK9Yw/zh-cn_image_0000002808886683.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=3FC973F367E7EC8D3C7E9071932B9EF5D9B949F5179057EB7A886475257BC4D2 "点击放大")

### @InsightIntentForm装饰器

1. 基于FormExtensionAbility使用，在继承FormExtensionAbility的class头部或内部，右键选择**CodeGenie > Insight Intent > Form Insight Intent**。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/90/v3/JVOH2QmoRW2nZ3T2aGGtXw/zh-cn_image_0000002808766605.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=14ED580DFCBD10202517C88ECFFDE146F3BED227091CBFE1EA67CA0E48A8A6F8 "点击放大")
2. 意图装饰器自动添加至CodeGenie对话框中，可选择输入或不输入提示词，CodeGenie根据代码上下文分析输出结果。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f6/v3/ErliIzLbStG1ybPZ29UVhg/zh-cn_image_0000002779567026.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=32A3CD783D191860A219794C455D331F2C3A457EDDE50311476987238D53C18F "点击放大")
3. 生成结果后，点击对话框中生成代码块右上方的**插入**按钮，在class上方插入生成的代码，开发者可基于结果微调，实现意图调用。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/67/v3/SQt2GzMiRF2vBSGdUW50ng/zh-cn_image_0000002779407044.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=FB073B4FFA894E0B2437CC07CF512F58CEA15EBF30FD9CFF9F318FD4ABE36816 "点击放大")

### @InsightIntentEntry装饰器

1. 基于InsightIntentEntryExecutor使用，在直接继承InsightIntentEntryExecutor的class头部或内部，右键选择**CodeGenie > Insight Intent > Entry Insight Intent**。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0f/v3/R1EPYKv4R_irYDpvsYk6DA/zh-cn_image_0000002779567034.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=85A07AD255B1E137095858265DBC3C19BB8F4126DB10091E1CAEC6663BEA372E "点击放大")
2. 意图装饰器自动添加至CodeGenie对话框中，可选择输入或不输入提示词，CodeGenie根据代码上下文分析输出结果。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a7/v3/8F_cBCO0Q8CY6YhIaLR8fg/zh-cn_image_0000002808766613.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=8B38077BC58A2AF3F2CC0932D1284E63EB555431B99378840B1FA9B789AD8A94 "点击放大")
3. 生成结果后，点击对话框中生成代码块右上方的**插入**按钮，在class上方插入生成的代码，开发者可基于结果微调，实现意图调用。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8/v3/8vaeTGZ-RRmATxFG3p5AIg/zh-cn_image_0000002779567024.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=3C48B1D327F667C9CFEB5039CEEEC67FDC1A7DDA109BAB01FC56A60F32D585AE "点击放大")

## 生成意图插件和创建小艺智能体

1. 点击DevEco Studio右上角![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4/v3/fTlQX0SZSPWrQffNWwPBFQ/zh-cn_image_0000002808886673.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=7242A93D13ED28CE1738847B14182F8493E0784CD46EBF292545059F4D60EDBE)图标登录个人账号，再切换至个人所在的团队账号。

   **说明** 

   * 个人账号需要完成实名认证。
   * 如下企业开发者账号为某团队账号名称，仅供参考。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7/v3/GGxRdm4MQsyTwwLT5a5u-g/zh-cn_image_0000002808766591.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=7BABE9B9C8FA34EF86E238C52F7A6EEF636EF9170146E59787AD42E9676A7EE5)
2. 在意图注解代码块内部任意位置，右键选择**CodeGenie > Add Intent Plugin**，生成的意图注解插件将注册到小艺智能平台中。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/32/v3/7wulAFe_QeaWpz4eCoo-4A/zh-cn_image_0000002808886689.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=1D7E126890FD5965BC6235D2DD062BEF51ACD7781241D08E1353AF2B7C27CFC5 "点击放大")
3. 在DevEco Studio菜单栏点击**View > Tool Windows > Application Agent** ，打开内嵌的小艺智能平台新建智能体和添加插件。
