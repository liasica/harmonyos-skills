---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-run-debug-configurations
title: 自定义运行/调试配置
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 应用调试 > 自定义运行/调试配置
category: harmonyos-guides
scraped_at: 2026-10-09T08:15:33+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:2ef5fbbec6badd58c663cf2adb7d952712d4daf544105e258d063cd83e317520
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

点击编辑器上方![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/30/v3/5TOszrVNRlmPkDGS7Fgz8Q/zh-cn_image_0000002779082657.png "点击放大")按钮，在菜单中点击**Application**并选择相应模块，点击右侧![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/LXnynWcPRjO9uDx-IDiUZA/zh-cn_image_0000002749323722.png "点击放大")按钮打开配置界面。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fb/v3/3QOAq4pBSVyQmVz2nJMLbA/zh-cn_image_0000002779082667.png)

在配置界面中点击**调试器**选项并设置**调试类型**。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4a/v3/WE81ppUZQ5-RrAHuALyRLA/zh-cn_image_0000002778922809.png)

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

点击编辑器上方![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1a/v3/aMdolE3HTUSxMTz6GegvXw/zh-cn_image_0000002749323708.png "点击放大")按钮，在菜单中点击**Application**并选择相应模块，点击右侧![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4e/v3/jthzdT1DSn6Jw9NgWFh-vg/zh-cn_image_0000002749323730.png "点击放大")按钮打开配置界面。在配置界面**通用**中设置指定模块的HAP安装方式，勾选**保留应用数据**，则表示采用覆盖安装方式，保留应用/元服务缓存数据。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d3/v3/Y-SkgH1dS-yeb3xpEYd2_A/zh-cn_image_0000002778922797.png)

### 配置自定义调试参数

如果未进行自定义，将按默认配置安装和运行应用。如果开发者需要对应用安装、运行等流程增加参数配置，可在**安装参数**和**启动参数**下进行配置。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/12/v3/kCDatQomS0yaSb6RrE7xsQ/zh-cn_image_0000002778922811.png)

* **安装参数**
  + **启用源码行跳转**：勾选**启用源码行跳转**表示在构建产物中系统组件增加debugline属性，用于开启[ArkUI 界面检查器源码跳转功能](ide-hmos-arkui-inspector.md#section44774145517)。
  + **安装标志**：输入bm install命令相关的选项，请参见[bm install 参数](bm-tool.md#安装命令install)。如设置"-w 360"，表示将超时等待时间设置为360秒。
* **启动参数**
  + **启动**：指定在安装应用后启动的Ability。

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f5/v3/y205TbY_SeiQdb0lm9pTXw/zh-cn_image_0000002778922801.png)

    - **空**：只安装不启动任何Ability。
    - **默认 Ability**：默认的EntryAbility，即module.json5文件中配置了“skills”属性的第一个ability；若无配置“skills”属性的ability，则取“mainElement”指定的ability（该ability需存在于“abilities”数组内）；若“mainElement”未指定，则取“abilities”数组内的第一个ability。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d/v3/06pDjSvUTmSTLNFmRYHtlA/zh-cn_image_0000002749483590.png "点击放大")
    - **指定 Ability**：工程中的UIAbility或ExtensionAbility。

      可以在工程中添加UIAbility或ExtensionAbility，详细请参阅[UIAbility开发指导](uiability.md)或[ExtensionAbility开发指导](extensionability-overview.md)。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/34/v3/psy77fXpT2upLkRgs-2tTw/zh-cn_image_0000002749323714.png)
  + **启动标志**：输入aa start命令相关的选项，请参见[aa start 参数](aa-tool.md)。

### 配置环境变量

如果开发者需要配置和管理应用开发环境，以及控制应用程序的行为，可配置环境变量。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/88/v3/pvwyYdINRduD-jQXbj8bNg/zh-cn_image_0000002749483596.png)

点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/31/v3/0rPgy0T1RWSQOsnCYdPe9A/zh-cn_image_0000002749483600.png)按钮，新增一行配置项。当前支持以下配置项：

* ASAN\_OPTIONS：在运行时配置ASan的行为，包括设置检测级别、输出格式、内存错误报告的详细程度等，具体可配置的value请参见[配置参数](../best-practices/bpta-stability-asan-detection.md#section1496994494018)。若开发者未配置log\_exe\_name、abort\_on\_error，DevEco Studio将自动填充。ASAN\_OPTIONS是应用级别的，只在entry和feature模块中配置生效，HAR/HSP模块配置不生效。

**说明** 

当配置环境变量后，**保留应用数据**覆盖安装不生效。

环境变量配置完成后，需确保环境变量已勾选。

## 多模块调试

### 安装多个模块

如果一个工程中同一个设备存在多个模块（如存在entry和feature模块），且存在模块间的调用时，在调试阶段需要同时安装多个模块的Hap包到设备中。此时，需要在**多包推送**中选择多个模块，启动调试时，DevEco Studio会将所有的模块都安装到设备上。

设置方法如下：

点击编辑器上方![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/68/v3/MUMIwwSiQ5iHK3CAqZI2nA/zh-cn_image_0000002749483602.png "点击放大")按钮，在菜单中点击**Application**并选择相应模块，点击右侧![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cf/v3/SVLOhfWBRNG_43GUUz1_kw/zh-cn_image_0000002779082653.png "点击放大")按钮打开配置界面。在配置界面**通用**中，勾选**多包推送**，选择多个模块。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/D8sOWTodQbOsMhLzqFoqsA/zh-cn_image_0000002749323712.png)

### 自动安装依赖

如果一个工程中entry/feature/HSP模块直接依赖其他HAR/HSP模块（如entry模块依赖HSP模块）及间接依赖其他模块（如entry模块依赖HAR模块，HAR又依赖HSP模块），在调试阶段需要同时安装模块包及其所有依赖模块的包到设备中，此时，可以设置**自动依赖**，启动调试时会自动将所有依赖的模块都安装到设备上。

设置方法如下：

点击编辑器上方![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/RTsHGP6yQMWxn5SuZw1uVw/zh-cn_image_0000002778922813.png "点击放大")按钮，在菜单中点击**Application**并选择相应模块，点击右侧![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/21/v3/v_25t9aUQlCHUIdsEKrKGA/zh-cn_image_0000002749483588.png "点击放大")按钮打开配置界面。在配置界面**通用**中，勾选**自动依赖。**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1a/v3/HsqRIEE-QIW6Q4NSHw3S5Q/zh-cn_image_0000002779082645.png)

在**前置任务**中，可以点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d2/v3/M99yX8wzTjqKZfa4SlWZ9Q/zh-cn_image_0000002749323720.png "点击放大")添加应用启动前的任务，也可以点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/19/v3/VJOyB5z6Tv6dzYldZov0kA/zh-cn_image_0000002749483604.png "点击放大")移除任务。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/nPXdTN7_QCKJ8PcawR8wqA/zh-cn_image_0000002778922805.png "点击放大")

在勾选**自动依赖**后，可以同时勾选**多包推送**，从而达到推送所有包的效果。
