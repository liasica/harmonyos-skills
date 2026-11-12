---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-run-debug-configurations
title: 自定义运行/调试配置
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 应用调试 > 自定义运行/调试配置
category: harmonyos-guides
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-10-10
content_hash: sha256:e9eb834c005159ea50fa03ee6c37e32d247655ca6a4ff7622380f364ca33800b
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

点击编辑器上方![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/jNfBch1BT9a6NVj_gZ9IMQ/zh-cn_image_0000002781471034.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=8F6ACA271F6A22D011A775944B0CB58BE7F26E076E4C1959C1484CF10E737978 "点击放大")按钮，在菜单中点击**Application**并选择相应模块，点击右侧![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/20/v3/uuF68BzAQzu2BYr5ffvYkg/zh-cn_image_0000002781311098.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=B8A00694ADC945BF08AFF72DAC5A5B5A0F19E71029E29E47064B3A1576477DDD "点击放大")按钮打开配置界面。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9d/v3/RjA5Wy-2TsCUglVtdVsN8A/zh-cn_image_0000002810750703.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=9B9AAA46F0755ABA877BCE5C72E44D8C469D9F4E312199054D1E81C863C75330)

在配置界面中点击**调试器**选项并设置**调试类型**。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9c/v3/80NhvErxRO-TaZqqIIhPWg/zh-cn_image_0000002810750697.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=12DE78C28F743EC6B333E9F0C8E4A50FD0374995B886546329F3C596CB8B7676)

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

点击编辑器上方![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f6/v3/lSYCeXdFRP6FTwURLqUcbQ/zh-cn_image_0000002810630555.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=5DBDF2DDD6A70B760E783AF8CC7AB2CB77E4194CC573F948974ACBCBEF0BBE91 "点击放大")按钮，在菜单中点击**Application**并选择相应模块，点击右侧![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/iRb0J770SrCoZYjydosbfA/zh-cn_image_0000002781471044.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=93C8D872AF67C964441003E788DFD3B16EF86CF05C7D3FFE24744B5243030853 "点击放大")按钮打开配置界面。在配置界面**通用**中设置指定模块的HAP安装方式，勾选**保留应用数据**，则表示采用覆盖安装方式，保留应用/元服务缓存数据。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6f/v3/mL92KdymQwCSnaeQGMXpzQ/zh-cn_image_0000002810630557.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=474B2EC56D2C0944538F4B15237B0A855EF1DD471FF50A346FB4F6460F76A289)

### 配置自定义调试参数

如果未进行自定义，将按默认配置安装和运行应用。如果开发者需要对应用安装、运行等流程增加参数配置，可在**安装参数**和**启动参数**下进行配置。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f9/v3/KnOTKnusTGi3BQSQomJBGw/zh-cn_image_0000002781311100.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=ABB35BA62574184CE73C9559CCC1E24F52E183B702A4E00EF50360C68991EBE9)

* **安装参数**
  + **启用源码行跳转**：勾选**启用源码行跳转**表示在构建产物中系统组件增加debugline属性，用于开启[ArkUI 界面检查器源码跳转功能](ide-hmos-arkui-inspector.md#section44774145517)。
  + **安装标志**：输入bm install命令相关的选项，请参见[bm install 参数](bm-tool.md#安装命令install)。如设置"-w 360"，表示将超时等待时间设置为360秒。
* **启动参数**
  + **启动**：指定在安装应用后启动的Ability。

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ff/v3/1VefCsZiS7mSstO6P-PHDw/zh-cn_image_0000002810630563.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=949360EEC976D550FC17E293BFD2B61A18A8719964B71EAF27391185223C7021)

    - **空**：只安装不启动任何Ability。
    - **默认 Ability**：默认的EntryAbility，即module.json5文件中配置了“skills”属性的第一个ability；若无配置“skills”属性的ability，则取“mainElement”指定的ability（该ability需存在于“abilities”数组内）；若“mainElement”未指定，则取“abilities”数组内的第一个ability。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/32/v3/mEfFPbTtQrmoT2HfW7am4Q/zh-cn_image_0000002810630585.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=FE230FC3416474624809A8F2966BAC9D091E1EF5F2F11E71B563088AE39FC5FE "点击放大")
    - **指定 Ability**：工程中的UIAbility或ExtensionAbility。

      可以在工程中添加UIAbility或ExtensionAbility，详细请参阅[UIAbility开发指导](uiability.md)或[ExtensionAbility开发指导](extensionability-overview.md)。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d0/v3/K38BntiATy6-YPER93DK8w/zh-cn_image_0000002781471008.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=95794FD70EA45293B46C21217F3818F72469086A46E4C61B03C3747337A848CC)
  + **启动标志**：输入aa start命令相关的选项，请参见[aa start 参数](aa-tool.md)。

### 配置环境变量

如果开发者需要配置和管理应用开发环境，以及控制应用程序的行为，可配置环境变量。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/86/v3/VBdt9N8ISaGYTufJFnKS2A/zh-cn_image_0000002810630587.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=056C6CDDF75CFA94A1A3ACB1B3163E307E3AF943FBB3B2B906E1E96829FAB8C8)

点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/57/v3/ZnwKebZhR3K7797LmGqQKQ/zh-cn_image_0000002781471036.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=E68B89BE64FB20C61F8EBEB4B620D058DDDFE9997C7AEB30935CCEE8DAEEAD95)按钮，新增一行配置项。当前支持以下配置项：

* ASAN\_OPTIONS：在运行时配置ASan的行为，包括设置检测级别、输出格式、内存错误报告的详细程度等，具体可配置的value请参见[配置参数](../best-practices/bpta-stability-asan-detection.md#section1496994494018)。若开发者未配置log\_exe\_name、abort\_on\_error，DevEco Studio将自动填充。ASAN\_OPTIONS是应用级别的，只在entry和feature模块中配置生效，HAR/HSP模块配置不生效。

**说明** 

当配置环境变量后，**保留应用数据**覆盖安装不生效。

环境变量配置完成后，需确保环境变量已勾选。

## 多模块调试

### 安装多个模块

如果一个工程中同一个设备存在多个模块（如存在entry和feature模块），且存在模块间的调用时，在调试阶段需要同时安装多个模块的Hap包到设备中。此时，需要在**多包推送**中选择多个模块，启动调试时，DevEco Studio会将所有的模块都安装到设备上。

设置方法如下：

点击编辑器上方![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1b/v3/Ch1lsJi1SQW9VQCuN456yA/zh-cn_image_0000002781471038.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=1EB38DE4330DC8D8D3BF38E439ACA8843E9CA5197B9FAC42104F94F219AE71F1 "点击放大")按钮，在菜单中点击**Application**并选择相应模块，点击右侧![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/53/v3/iBRFcE46QfSBIz4e16hWYA/zh-cn_image_0000002781471026.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=355B3192A8CBCEDA17FC998E884BD182542EEFEA6E257206A31CE750675C5F9C "点击放大")按钮打开配置界面。在配置界面**通用**中，勾选**多包推送**，选择多个模块。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/75/v3/7nmp1bKRStmrdKStmlLTcQ/zh-cn_image_0000002810750667.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=62F6237E23699E63F2A2D1B20BF1EDAA49A5EF515CA8597EDF7E97CC51E2D0D1)

### 自动安装依赖

如果一个工程中entry/feature/HSP模块直接依赖其他HAR/HSP模块（如entry模块依赖HSP模块）及间接依赖其他模块（如entry模块依赖HAR模块，HAR又依赖HSP模块），在调试阶段需要同时安装模块包及其所有依赖模块的包到设备中，此时，可以设置**自动依赖**，启动调试时会自动将所有依赖的模块都安装到设备上。

设置方法如下：

点击编辑器上方![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5c/v3/ML1ijq2uR9K92l1IyqumSw/zh-cn_image_0000002810630591.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=BBEAFFC4B0D5A8B7D293CED899D4C6867195F53016B1FC8158E792B69497DE64 "点击放大")按钮，在菜单中点击**Application**并选择相应模块，点击右侧![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/K6RfNLecTguk6e8BBsIW3Q/zh-cn_image_0000002781311072.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=A8F644E512E07A2C889CD7400DD9B543841D05E0882F36A828A05C011256019D "点击放大")按钮打开配置界面。在配置界面**通用**中，勾选**自动依赖。**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/31/v3/wc0Vu_IyQHmw3iPFELmZ3w/zh-cn_image_0000002781471004.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=77365E50CF40D5C7AB91DD47C6EC2412FD76B361E3C208417BEEE4F9A378ECB1)

在**前置任务**中，可以点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ae/v3/hyawCVuNTgidsG4tfVn9CA/zh-cn_image_0000002781311096.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=A4B126A62EF4EF981E745E04CBB1BFBD558E4B598B9304C976189FCE26F5D8CD "点击放大")添加应用启动前的任务，也可以点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/16/v3/-XeKuoj3TVKxlzzM_0DdpQ/zh-cn_image_0000002810630593.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=650BF4880187BBDE2DCF5EE966D9A24438D215ECEA2D21F77305514EA080DF8A "点击放大")移除任务。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/84/v3/IQuGLKrgTiKW1zRrXjYVjg/zh-cn_image_0000002810750695.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=4D86AD7DEEBDF4B64526641F396D6FD6D62E580A0060F6C0B60690484CE91488 "点击放大")

在勾选**自动依赖**后，可以同时勾选**多包推送**，从而达到推送所有包的效果。
