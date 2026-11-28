---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-run-debug-configurations
title: 自定义运行/调试配置
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 应用调试 > 自定义运行/调试配置
category: harmonyos-guides
scraped_at: 2026-11-28T10:34:55+08:00
doc_updated_at: 2026-10-10
content_hash: sha256:5e912949045a028e8000f30f80d24b1cf5608f2e20e0f2e59c160ea20ed225be
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

点击编辑器上方![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a4/v3/E8QiqPC5RhevlBq0a_0ngw/zh-cn_image_0000002820681195.png?HW-CC-KV=V1&HW-CC-Date=20261128T023455Z&HW-CC-Expire=31536000000&HW-CC-Sign=7F33BBCDDEFACEE67CD26202FE64861B359C85B557649E2CDB4A11C4F8EAA9FC "点击放大")按钮，在菜单中点击**Application**并选择相应模块，点击右侧![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/54/v3/nve7S_0RTXmqLr1IITIr5g/zh-cn_image_0000002820721199.png?HW-CC-KV=V1&HW-CC-Date=20261128T023455Z&HW-CC-Expire=31536000000&HW-CC-Sign=D7BE7FBD2A955C5F4434956E1587AD201CFA71CB6CD86FB345BFB414DA115422 "点击放大")按钮打开配置界面。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c8/v3/hFLT2QaCT968JLOxtjkC0Q/zh-cn_image_0000002820721195.png?HW-CC-KV=V1&HW-CC-Date=20261128T023455Z&HW-CC-Expire=31536000000&HW-CC-Sign=54B06CA8B63466863F4FAEB5E5712A701A4344717D3853D21E6AD09AB7979552)

在配置界面中点击**调试器**选项并设置**调试类型**。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ef/v3/5xEUAVG7TsKCI2zYUCHXGA/zh-cn_image_0000002820721191.png?HW-CC-KV=V1&HW-CC-Date=20261128T023455Z&HW-CC-Expire=31536000000&HW-CC-Sign=E97756068EC6E6C0F99BBA847C568FE34555324DE7DCA2CFF471C858D412F22F)

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

点击编辑器上方![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/PxujyRs7SDeCODl7tzkcnA/zh-cn_image_0000002820681193.png?HW-CC-KV=V1&HW-CC-Date=20261128T023455Z&HW-CC-Expire=31536000000&HW-CC-Sign=2F5274BA46F01C2E024DE01B5300605C1332D5BA5A76BD42D802AE0C87B81A02 "点击放大")按钮，在菜单中点击**Application**并选择相应模块，点击右侧![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/50/v3/LPuFu945ReyvxOTGyOCe-Q/zh-cn_image_0000002792001234.png?HW-CC-KV=V1&HW-CC-Date=20261128T023455Z&HW-CC-Expire=31536000000&HW-CC-Sign=A97D8E226238DC8C447E0A4BD2A4348DE0AF86E90EF18EED41DCF603EA121D30 "点击放大")按钮打开配置界面。在配置界面**通用**中设置指定模块的HAP安装方式，勾选**保留应用数据**，则表示采用覆盖安装方式，保留应用/元服务缓存数据。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f3/v3/VQ-KLsErSKiG-xaxEx07cw/zh-cn_image_0000002791841256.png?HW-CC-KV=V1&HW-CC-Date=20261128T023455Z&HW-CC-Expire=31536000000&HW-CC-Sign=A7E4F2797EA5C465E823DD6E4423CB69847B545C1D4A0C65032D6628E2298A05)

### 配置自定义调试参数

如果未进行自定义，将按默认配置安装和运行应用。如果开发者需要对应用安装、运行等流程增加参数配置，可在**安装参数**和**启动参数**下进行配置。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/73/v3/IDehv3EZS7S2yTD1nVwB2w/zh-cn_image_0000002792001230.png?HW-CC-KV=V1&HW-CC-Date=20261128T023455Z&HW-CC-Expire=31536000000&HW-CC-Sign=F7ED4DD9D0B81C71696E410C0B33233672D89C289B298D1A4CCBE5B7F5371695)

* **安装参数**
  + **启用源码行跳转**：勾选**启用源码行跳转**表示在构建产物中系统组件增加debugline属性，用于开启[ArkUI 界面检查器源码跳转功能](ide-hmos-arkui-inspector.md#section44774145517)。
  + **安装标志**：输入bm install命令相关的选项，请参见[bm install 参数](bm-tool.md#安装命令install)。如设置"-w 360"，表示将超时等待时间设置为360秒。
* **启动参数**
  + **启动**：指定在安装应用后启动的Ability。

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/82/v3/G_4yC0FqSZCqiXnxfMs7mA/zh-cn_image_0000002791841260.png?HW-CC-KV=V1&HW-CC-Date=20261128T023455Z&HW-CC-Expire=31536000000&HW-CC-Sign=A497A0B16E21D303665988AFFF6A23EA0CCA26EEDBED4DE044DCCA43608EB2CA)

    - **空**：只安装不启动任何Ability。
    - **默认 Ability**：默认的EntryAbility，即module.json5文件中配置了“skills”属性的第一个ability；若无配置“skills”属性的ability，则取“mainElement”指定的ability（该ability需存在于“abilities”数组内）；若“mainElement”未指定，则取“abilities”数组内的第一个ability。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/84/v3/qjA_roV1RDG_OT3F3_aTSg/zh-cn_image_0000002792001236.png?HW-CC-KV=V1&HW-CC-Date=20261128T023455Z&HW-CC-Expire=31536000000&HW-CC-Sign=74653FBBDEE8FA453340A77D7AD1B9A48DD67B4A3B77237AB0567CB2DAF28C38 "点击放大")
    - **指定 Ability**：工程中的UIAbility或ExtensionAbility。

      可以在工程中添加UIAbility或ExtensionAbility，详细请参阅[UIAbility开发指导](uiability.md)或[ExtensionAbility开发指导](extensionability-overview.md)。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d6/v3/fSdDPmySScSXiXjP0tFpMg/zh-cn_image_0000002820681189.png?HW-CC-KV=V1&HW-CC-Date=20261128T023455Z&HW-CC-Expire=31536000000&HW-CC-Sign=0D1F66B4C0DDE667FA1DB65580AAD90692EA6B64ECA7AB2B10A02E4F6C25695E)
  + **启动标志**：输入aa start命令相关的选项，请参见[aa start 参数](aa-tool.md)。

### 配置环境变量

如果开发者需要配置和管理应用开发环境，以及控制应用程序的行为，可配置环境变量。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/41/v3/nZQbhyF0R2-SukabbVekew/zh-cn_image_0000002820721201.png?HW-CC-KV=V1&HW-CC-Date=20261128T023455Z&HW-CC-Expire=31536000000&HW-CC-Sign=CF6AEE2DD2390525D214BE412D8574422EE8640002B574727777365A9B9F6359)

点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c8/v3/msireUfeRXeKSyC0aQqGbg/zh-cn_image_0000002820681197.png?HW-CC-KV=V1&HW-CC-Date=20261128T023455Z&HW-CC-Expire=31536000000&HW-CC-Sign=1B3A8F0F2B2AF4F97700D99B331226675331ACF1963BF8A1C19406FCAB083C2A)按钮，新增一行配置项。当前支持以下配置项：

* ASAN\_OPTIONS：在运行时配置ASan的行为，包括设置检测级别、输出格式、内存错误报告的详细程度等，具体可配置的value请参见[配置参数](../best-practices/bpta-stability-asan-detection.md#section1496994494018)。若开发者未配置log\_exe\_name、abort\_on\_error，DevEco Studio将自动填充。ASAN\_OPTIONS是应用级别的，只在entry和feature模块中配置生效，HAR/HSP模块配置不生效。

**说明** 

当配置环境变量后，**保留应用数据**覆盖安装不生效。

环境变量配置完成后，需确保环境变量已勾选。

## 多模块调试

### 安装多个模块

如果一个工程中同一个设备存在多个模块（如存在entry和feature模块），且存在模块间的调用时，在调试阶段需要同时安装多个模块的Hap包到设备中。此时，需要在**多包推送**中选择多个模块，启动调试时，DevEco Studio会将所有的模块都安装到设备上。

设置方法如下：

点击编辑器上方![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/aa/v3/XioSv9owSl21pWkFZzcDRA/zh-cn_image_0000002820681199.png?HW-CC-KV=V1&HW-CC-Date=20261128T023455Z&HW-CC-Expire=31536000000&HW-CC-Sign=CCA78C1E5DA23BB26E4794000FBC012F5125E25C12A803D3E882859C339FD4A0 "点击放大")按钮，在菜单中点击**Application**并选择相应模块，点击右侧![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a6/v3/8CzM5jGaRfuUiMLxRQYZRg/zh-cn_image_0000002820721205.png?HW-CC-KV=V1&HW-CC-Date=20261128T023455Z&HW-CC-Expire=31536000000&HW-CC-Sign=84BE97F0FCFF6F39F897592CF4979C0FFCD8589CC132F8D19B63B3B58EC4DC6B "点击放大")按钮打开配置界面。在配置界面**通用**中，勾选**多包推送**，选择多个模块。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b3/v3/ML8E9OZjQeW3p0cwYi-gTg/zh-cn_image_0000002791841250.png?HW-CC-KV=V1&HW-CC-Date=20261128T023455Z&HW-CC-Expire=31536000000&HW-CC-Sign=412CB62C3EC4F16C6CB367DEF16FC8570629A41A5FD60C3F81EDD8853DD02658)

### 自动安装依赖

如果一个工程中entry/feature/HSP模块直接依赖其他HAR/HSP模块（如entry模块依赖HSP模块）及间接依赖其他模块（如entry模块依赖HAR模块，HAR又依赖HSP模块），在调试阶段需要同时安装模块包及其所有依赖模块的包到设备中，此时，可以设置**自动依赖**，启动调试时会自动将所有依赖的模块都安装到设备上。

设置方法如下：

点击编辑器上方![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/68/v3/CF82e3DxRPGUPVUnqXSbiQ/zh-cn_image_0000002820721207.png?HW-CC-KV=V1&HW-CC-Date=20261128T023455Z&HW-CC-Expire=31536000000&HW-CC-Sign=332F664859095EF90EA1CF705CC85029F969AEA46ABD271585349EEF94FC17D9 "点击放大")按钮，在菜单中点击**Application**并选择相应模块，点击右侧![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/JrSip5STS-ukuOyELDNYFg/zh-cn_image_0000002791841258.png?HW-CC-KV=V1&HW-CC-Date=20261128T023455Z&HW-CC-Expire=31536000000&HW-CC-Sign=D02073E83E3CF592EB61955ED3ECC8FA5FECD1F6D49A236FB33C7899BB8E9D0D "点击放大")按钮打开配置界面。在配置界面**通用**中，勾选**自动依赖。**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b/v3/tBcej0l4Sy-aIuN10W71tw/zh-cn_image_0000002791841262.png?HW-CC-KV=V1&HW-CC-Date=20261128T023455Z&HW-CC-Expire=31536000000&HW-CC-Sign=36BE779BCD27213873162D208718E4AC3D4F12BC76D0BE4873D24FB1BBDD9E7B)

在**前置任务**中，可以点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b4/v3/GiSqJnlCQTq93gJhd1tvdQ/zh-cn_image_0000002792001232.png?HW-CC-KV=V1&HW-CC-Date=20261128T023455Z&HW-CC-Expire=31536000000&HW-CC-Sign=15F20E400CAD4C777BE98DB0A260883629042E6FA773FBBB347D5BC2EEDCD63D "点击放大")添加应用启动前的任务，也可以点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/O0l8xLT_TsmoLcNiSNDQ6Q/zh-cn_image_0000002792001238.png?HW-CC-KV=V1&HW-CC-Date=20261128T023455Z&HW-CC-Expire=31536000000&HW-CC-Sign=E1A459649447F8E9D417DD80F9396662DB464615854D2C0AC2A44B6F7446F9FB "点击放大")移除任务。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/47/v3/pwmb2pjjQi-mpcuhLCAXVw/zh-cn_image_0000002791841264.png?HW-CC-KV=V1&HW-CC-Date=20261128T023455Z&HW-CC-Expire=31536000000&HW-CC-Sign=BBD0AF64ECE1C3B32846E4BFFB94FB841A1E4E5F0B94AA42F8F41F0FB4C18F81 "点击放大")

在勾选**自动依赖**后，可以同时勾选**多包推送**，从而达到推送所有包的效果。
