---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-run-debug-configurations
title: 自定义运行/调试配置
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 应用调试 > 自定义运行/调试配置
category: harmonyos-guides
scraped_at: 2026-11-14T08:49:16+08:00
doc_updated_at: 2026-10-10
content_hash: sha256:fae2e7732e652781bbc857dccf7a5a23260555cdc396704651fe415526a7ab93
---

## 配置应用可调试

应用是否支持调试，根据app.json5的debug字段和build-profile.json5的debuggable字段综合判断，app.json5的优先级高于build-profile.json5。

1. 在app.json5中配置debug字段：
   * true：应用支持调试。
   * false：应用不支持调试。
2. 如果没有配置debug字段，则根据build-profile.json5的debuggable字段判断应用是否支持调试。
   * true：应用支持调试。当[构建模式](ide-hmos-hvigor-compilation-options-customizing-guide.md#section192461528194916)不是release时，debuggable的缺省值是true，即支持调试。
   * false：应用不支持调试。当构建模式为release时，debuggable的缺省值是false，即不支持调试。

## 设置调试代码类型

点击编辑器上方![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/66/v3/vrKMQw_TSWuJcdhkT4Rt3A/zh-cn_image_0000002781471034.png?HW-CC-KV=V1&HW-CC-Date=20261114T004728Z&HW-CC-Expire=31536000000&HW-CC-Sign=98C196DC4A7A786F3E6AE9F6F0925791D8EF210E20E05016978797A92DAA48AB "点击放大")按钮，在菜单中点击**Application**并选择相应模块，点击右侧![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/37/v3/xgX4-OHBQCGdtycJGmo3VA/zh-cn_image_0000002781311098.png?HW-CC-KV=V1&HW-CC-Date=20261114T004728Z&HW-CC-Expire=31536000000&HW-CC-Sign=D13B2A1DD12670C107C042882980C13D22EDBAFBA23EEA97F0AA92D1090306B1 "点击放大")按钮打开配置界面。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/38/v3/WVB89DnURRGI-Hjt2F2gpQ/zh-cn_image_0000002810750703.png?HW-CC-KV=V1&HW-CC-Date=20261114T004728Z&HW-CC-Expire=31536000000&HW-CC-Sign=775A03DBF7B40C189B2AA89A7BD09422E639B4F6D1C09CA6A4E5C7A48050621E)

在配置界面中点击**调试器**选项并设置**调试类型**。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a2/v3/4SFTz0-fSoqyEBF1whFl4w/zh-cn_image_0000002810750697.png?HW-CC-KV=V1&HW-CC-Date=20261114T004728Z&HW-CC-Expire=31536000000&HW-CC-Sign=C4E38419D5A4C3DD61360EF37F7ECB690ADABD4C93EB76B7A6E4EAD1DD612A03)

工程调试类型默认为Detect Automatically，关于各调试类型的说明如下表所示：

**表1** 调试类型配置项

| 调试类型 | 调试代码 |
| --- | --- |
| **Detect Automatically** | 新建工程默认调试器选项。根据工程模块及其依赖的模块涉及的编程语言，自动启动对应的调试器。 |
| **ArkTS/JS** | * 调试ArkTS代码 * 调试JS代码 |
| **Native** | 仅调试C/C++代码 |
| **Dual(ArkTS/JS + Native)** | 调试C/C++工程的ArkTS/JS和C/C++代码 |

## 设置HAP安装方式

在调试阶段，HAP在设备上的安装方式有2种，可以根据实际需要进行设置。

* 安装方式一：先卸载应用/元服务后，再重新安装。该方式会清除设备上应用/元服务所有的缓存数据。

  DevEco Studio支持当代码无变化时，不进行推包安装。即根据模块有无变化来判断是否重新推送安装模块包，在运行调试时仅将有变化的模块及依赖它的模块重新推送安装至设备上。如entry依赖了HSP模块，当HSP模块有变化，运行调试时将同时推送安装HSP模块和entry模块。
* 安装方式二：采用覆盖安装方式，不卸载应用/元服务，该方式会保留应用/元服务的缓存数据。

设置方法如下：

点击编辑器上方![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8f/v3/K7KX2KVoRsaVB215b3FBtA/zh-cn_image_0000002810630555.png?HW-CC-KV=V1&HW-CC-Date=20261114T004728Z&HW-CC-Expire=31536000000&HW-CC-Sign=A61BE0613D4590B2E1308E8807614FE07E7027555A7531B0303D70197A406022 "点击放大")按钮，在菜单中点击**Application**并选择相应模块，点击右侧![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/JlcQPYgqQemIB062ptGLyQ/zh-cn_image_0000002781471044.png?HW-CC-KV=V1&HW-CC-Date=20261114T004728Z&HW-CC-Expire=31536000000&HW-CC-Sign=9660EC053B6A07042013EC908CD676A84920BBD471EB3AF8908A0BD4A7DB939A "点击放大")按钮打开配置界面。在配置界面**通用**中设置指定模块的HAP安装方式，勾选**保留应用数据**，则表示采用覆盖安装方式，保留应用/元服务缓存数据。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1/v3/rXrQ8u7LSBSIiRXm9eh5sA/zh-cn_image_0000002810630557.png?HW-CC-KV=V1&HW-CC-Date=20261114T004728Z&HW-CC-Expire=31536000000&HW-CC-Sign=C8109FB9F12768416968443B118845A134E7649BE32E6911DB6A766F850E41D7)

### 配置自定义调试参数

如果未进行自定义，将按默认配置安装和运行应用。如果开发者需要对应用安装、运行等流程增加参数配置，可在**安装参数**和**启动参数**下进行配置。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/79/v3/RBsrM2KOT66pSZHqRkpRWQ/zh-cn_image_0000002781311100.png?HW-CC-KV=V1&HW-CC-Date=20261114T004728Z&HW-CC-Expire=31536000000&HW-CC-Sign=53AB7728EC98E8718FBC7FBF8FFB4C457335176244D18E467D4E03F9CF9162B4)

* **安装参数**
  + **启用源码行跳转**：勾选**启用源码行跳转**表示在构建产物中系统组件增加debugline属性，用于开启[ArkUI 界面检查器源码跳转功能](ide-hmos-arkui-inspector.md#section44774145517)。
  + **安装标志**：输入bm install命令相关的选项，请参见[bm install 参数](bm-tool.md#安装命令install)。如设置"-w 360"，表示将超时等待时间设置为360秒。
* **启动参数**
  + **启动**：指定在安装应用后启动的Ability。

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0c/v3/CuL8OYdOR5i8ukDyoAwCYw/zh-cn_image_0000002810630563.png?HW-CC-KV=V1&HW-CC-Date=20261114T004728Z&HW-CC-Expire=31536000000&HW-CC-Sign=175663ECF4260351B0EE1C6D00A3EE975E37E0B128B825180438535C2AD9E6B3)

    - **空**：只安装不启动任何Ability。
    - **默认 Ability**：默认的EntryAbility，即module.json5文件中配置了“skills”属性的第一个ability；若无配置“skills”属性的ability，则取“mainElement”指定的ability（该ability需存在于“abilities”数组内）；若“mainElement”未指定，则取“abilities”数组内的第一个ability。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1e/v3/MZXtCcLYTPeQW68SkDo72w/zh-cn_image_0000002810630585.png?HW-CC-KV=V1&HW-CC-Date=20261114T004728Z&HW-CC-Expire=31536000000&HW-CC-Sign=BBC93DD4A85A8C2C76557A254B821E6CABE83B31D8C1564907FEFE5A92D17B96 "点击放大")
    - **指定 Ability**：工程中的UIAbility或ExtensionAbility。

      可以在工程中添加UIAbility或ExtensionAbility，详细请参阅[UIAbility开发指导](uiability.md)或[ExtensionAbility开发指导](extensionability-overview.md)。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/55/v3/e63qmux3TxiEMY9jwXJNfg/zh-cn_image_0000002781471008.png?HW-CC-KV=V1&HW-CC-Date=20261114T004728Z&HW-CC-Expire=31536000000&HW-CC-Sign=027CDE9FD13F0404F96FE9F00F2A4F4CA7209F9218710A8E7FF41FE6E7FE8195)
  + **启动标志**：输入aa start命令相关的选项，请参见[aa start 参数](aa-tool.md)。

### 配置环境变量

如果开发者需要配置和管理应用开发环境，以及控制应用程序的行为，可配置环境变量。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/80/v3/YKgE91k4TIGkaoQtvGThgg/zh-cn_image_0000002810630587.png?HW-CC-KV=V1&HW-CC-Date=20261114T004728Z&HW-CC-Expire=31536000000&HW-CC-Sign=7DEDBE893EE91DA298D2861006A1852DA7B3B754466FE0D3FB5E5F4193BDE1AD)

点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3f/v3/zslOIrNGTN-XBvTJ_JIX_w/zh-cn_image_0000002781471036.png?HW-CC-KV=V1&HW-CC-Date=20261114T004728Z&HW-CC-Expire=31536000000&HW-CC-Sign=1779AF8C64DA737542B9CF5AD6AC7B0539CD3044190D8C508E0583CFBF30646E)按钮，新增一行配置项。当前支持以下配置项：

* ASAN\_OPTIONS：在运行时配置ASan的行为，包括设置检测级别、输出格式、内存错误报告的详细程度等，具体可配置的value请参见[配置参数](../best-practices/bpta-stability-asan-detection.md#section1496994494018)。若开发者未配置log\_exe\_name、abort\_on\_error，DevEco Studio将自动填充。ASAN\_OPTIONS是应用级别的，只在entry和feature模块中配置生效，HAR/HSP模块配置不生效。

**说明** 

当配置环境变量后，**保留应用数据**覆盖安装不生效。

环境变量配置完成后，需确保环境变量已勾选。

## 多模块调试

### 安装多个模块

如果一个工程中同一个设备存在多个模块（如存在entry和feature模块），且存在模块间的调用时，在调试阶段需要同时安装多个模块的Hap包到设备中。此时，需要在**多包推送**中选择多个模块，启动调试时，DevEco Studio会将所有的模块都安装到设备上。

设置方法如下：

点击编辑器上方![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3b/v3/ge_FUXd4SieRf2_quc4dcg/zh-cn_image_0000002781471038.png?HW-CC-KV=V1&HW-CC-Date=20261114T004728Z&HW-CC-Expire=31536000000&HW-CC-Sign=15D319445B665F400B09558D69501C5E9D6348B63F07DBE308EABC0485177543 "点击放大")按钮，在菜单中点击**Application**并选择相应模块，点击右侧![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/eb/v3/3U25CV1pRkyz6IQbe-pIlA/zh-cn_image_0000002781471026.png?HW-CC-KV=V1&HW-CC-Date=20261114T004728Z&HW-CC-Expire=31536000000&HW-CC-Sign=888B2B4359A3AFD64A41D0B7E95CB9E27B24CCBAC592967A072E685454FB68C2 "点击放大")按钮打开配置界面。在配置界面**通用**中，勾选**多包推送**，选择多个模块。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/51/v3/k0QVfRXsSA2qBpsDJm_Pww/zh-cn_image_0000002810750667.png?HW-CC-KV=V1&HW-CC-Date=20261114T004728Z&HW-CC-Expire=31536000000&HW-CC-Sign=9604407480B88F723EE1A6891E7C1093F73AF8492CB7E3D092830885C7D5A568)

### 自动安装依赖

如果一个工程中entry/feature/HSP模块直接依赖其他HAR/HSP模块（如entry模块依赖HSP模块）及间接依赖其他模块（如entry模块依赖HAR模块，HAR又依赖HSP模块），在调试阶段需要同时安装模块包及其所有依赖模块的包到设备中，此时，可以设置**自动依赖**，启动调试时会自动将所有依赖的模块都安装到设备上。

设置方法如下：

点击编辑器上方![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/21/v3/thGx4wndQz-A2BpEEOq5tg/zh-cn_image_0000002810630591.png?HW-CC-KV=V1&HW-CC-Date=20261114T004728Z&HW-CC-Expire=31536000000&HW-CC-Sign=1A762D1C59D3F7A5CC0716A13D1C18C9071FE1AB6768DDF4AAE7E65EF06B99F5 "点击放大")按钮，在菜单中点击**Application**并选择相应模块，点击右侧![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/72/v3/IPjf2rJWRd-iKMwy4ZRRmw/zh-cn_image_0000002781311072.png?HW-CC-KV=V1&HW-CC-Date=20261114T004728Z&HW-CC-Expire=31536000000&HW-CC-Sign=6E0A2D9EF8D9072C96064D731D06187EC7C112C63C92A821D9DAED1807A6F15A "点击放大")按钮打开配置界面。在配置界面**通用**中，勾选**自动依赖。**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3e/v3/IjMw9ypDR4KOx5txgT7eZw/zh-cn_image_0000002781471004.png?HW-CC-KV=V1&HW-CC-Date=20261114T004728Z&HW-CC-Expire=31536000000&HW-CC-Sign=1E9B7A5FF11C23F74461C9E238409F5A9BFEB5871DF310A94EC8B5A969846C0D)

在**前置任务**中，可以点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/46/v3/Bm15tu3qT6OYgFhk2Zixtg/zh-cn_image_0000002781311096.png?HW-CC-KV=V1&HW-CC-Date=20261114T004728Z&HW-CC-Expire=31536000000&HW-CC-Sign=1F20128EC0B2B1D22F2B5719D0A6C9F9D9A3262E211377D131F9A71DE6C2C5E6 "点击放大")添加应用启动前的任务，也可以点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/Y1pf1vBCTHGtMWMvgBOaXA/zh-cn_image_0000002810630593.png?HW-CC-KV=V1&HW-CC-Date=20261114T004728Z&HW-CC-Expire=31536000000&HW-CC-Sign=D9B3A2B87BBABAAD87FF71A79BE0B1B954D6EF8EDADDC4AA3033A74ECBCD0371 "点击放大")移除任务。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/95/v3/0f1m0Ju7RRu8n5e1vZBuGA/zh-cn_image_0000002810750695.png?HW-CC-KV=V1&HW-CC-Date=20261114T004728Z&HW-CC-Expire=31536000000&HW-CC-Sign=D93BDCC80583F4CE3EB529277964741D70149357161B045C8B17C1B90A7D5339 "点击放大")

在勾选**自动依赖**后，可以同时勾选**多包推送**，从而达到推送所有包的效果。
