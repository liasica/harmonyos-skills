---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-run-debug-configurations
title: 自定义运行/调试配置
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 应用调试 > 自定义运行/调试配置
category: harmonyos-guides
scraped_at: 2026-11-14T08:48:59+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:0272142c5754b5fd0b8b7d5914d83895e2415cfcbdb96dfe91da11d690c7d3e5
---

## 配置应用可调试

应用是否支持调试，根据app.json5的debug字段和build-profile.json5的debuggable字段综合判断，app.json5的优先级高于build-profile.json5。

1. 在app.json5中配置debug字段：
   * true：应用支持调试。
   * false：应用不支持调试。
2. 如果没有配置debug字段，则根据build-profile.json5的debuggable字段判断应用是否支持调试。
   * true：应用支持调试。当[构建模式](ide-hvigor-compilation-options-customizing-guide.md#section192461528194916)不是release时，debuggable的缺省值是true，即支持调试。
   * false：应用不支持调试。当构建模式为release时，debuggable的缺省值是false，即不支持调试。

## 设置调试代码类型

点击**Run > Edit Configurations > Debugger**，选择相应模块，设置Debug type即可。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1f/v3/Hd5tIrrqRha6W7pUMoNkjw/zh-cn_image_0000002808886759.png?HW-CC-KV=V1&HW-CC-Date=20261114T004712Z&HW-CC-Expire=31536000000&HW-CC-Sign=9A7992A46FE3943F1EB837F8E3CD2974333D155EB71AE1C1A927EDA98AFEAE42)

工程调试类型默认为**Detect Automatically**，关于各调试类型的说明如下表所示：

**表1** 调试类型配置项

| 调试类型 | 调试代码 |
| --- | --- |
| **Detect Automatically** | 新建工程默认调试器选项。根据工程模块及其依赖的模块涉及的编程语言，自动启动对应的调试器。 |
| **ArkTS/JS** | * 调试ArkTS代码 * 调试JS代码 |
| **Native** | 仅调试C/C++代码 |
| **Dual(ArkTS/JS + Native)** | 调试C/C++工程的ArkTS/JS和C/C++代码 |

## 设置HAP安装方式

在调试阶段，HAP在设备上的安装方式有2种，可以根据实际需要进行设置。

* 安装方式一：先卸载应用/元服务后，再重新安装，该方式会清除设备上应用/元服务所有的缓存数据。

  从DevEco Studio 4.1 Canary2版本开始，支持当代码无变化时，不进行推包安装。即根据模块有无变化来判断是否重新推送安装模块包，在运行调试时仅将有变化的模块及依赖它的模块重新推送安装至设备上。如entry依赖了HSP模块，当HSP模块有变化，运行调试时将同时推送安装HSP模块和entry模块。
* 安装方式二：采用覆盖安装方式，不卸载应用/元服务，该方式会保留应用/元服务的缓存数据。

设置方法如下：

单击**Run > Edit Configurations**，设置指定模块的HAP安装方式，勾选**Keep Application Data**，则表示采用覆盖安装方式，保留应用/元服务缓存数据。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5c/v3/HBupkZHeRVGyvqhrKSqvtg/zh-cn_image_0000002779407140.png?HW-CC-KV=V1&HW-CC-Date=20261114T004712Z&HW-CC-Expire=31536000000&HW-CC-Sign=AA2B44087D6EC535158F998147AF60054720937D95F110529AA0F9F5F36E05C4)

### 配置自定义调试参数

如果未进行自定义，将按默认配置安装和运行应用。如果开发者需要对应用安装、运行等流程增加参数配置，可在“Installation Options”和“Launch Options”下进行配置。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/66/v3/iJ4ySG93QmqVHfMRA0sWLg/zh-cn_image_0000002808766677.png?HW-CC-KV=V1&HW-CC-Date=20261114T004712Z&HW-CC-Expire=31536000000&HW-CC-Sign=DA9DDC6FBCB9B8514A3918C193DE859B53F4726336BFA889126A8C6FAA99A25C)

* Installation Options
  + DebugLine Support：勾选Enable DebugLine表示在构建产物中系统组件增加debugline属性，用于开启[ArkUI Inspector源码跳转](ide-arkui-inspector.md#section1226015494335)功能。
  + Install Flags：输入bm install命令相关的选项，请参见[bm install 参数](bm-tool.md#安装命令install)。如可以设置“-w 360”，表示将超时等待时间设置为360秒。
* Launch Options
  + Launch：指定在安装应用后启动的Ability。

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/34/v3/_Rdcp3TCTgitK8R4ElknxQ/zh-cn_image_0000002808766693.png?HW-CC-KV=V1&HW-CC-Date=20261114T004712Z&HW-CC-Expire=31536000000&HW-CC-Sign=9AF8759F040EB6078FA3D5B6E1E23B68AD4072FA2652F376B23B1AE775291DC2)
    - Nothing：只安装不启动任何Ability。
    - Default Ability：默认的EntryAbility。
      * Stage模型：module.json5文件中配置了“skills”属性的第一个ability；若无配置“skills”属性的ability，则取“mainElement”指定的ability（该ability需存在于“abilities”数组内）；若“mainElement”未指定，则取“abilities”数组内的第一个ability。

        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/JtrAbcAlT1uf2vxlrbaBbg/zh-cn_image_0000002779567108.png?HW-CC-KV=V1&HW-CC-Date=20261114T004712Z&HW-CC-Expire=31536000000&HW-CC-Sign=768DF8B6E635EC82AD2B49527F248797E12ADF0833A082877B6AFC62A1CE44AA "点击放大")
      * FA模型：config.json文件中配置了“skills”属性的第一个ability；若无配置“skills”属性的ability，则取“mainAbility”指定的ability（该ability需存在于“abilities”数组内）；若“mainAbility”未指定，则取“abilities”数组内的第一个ability。
    - Specified Ability：工程中的UIAbility或ExtensionAbility。

      您可以在工程中添加UIAbility或ExtensionAbility，详细请查看[UIAbility开发指导](uiability.md)或[ExtensionAbility开发指导](extensionability-overview.md)。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4c/v3/e8X_iyb0R9SI3PV-COEEpg/zh-cn_image_0000002779407132.png?HW-CC-KV=V1&HW-CC-Date=20261114T004712Z&HW-CC-Expire=31536000000&HW-CC-Sign=3BC6DFEA60AE91607C0E3DB68E3107D0E9DF145D27561102245AB8A949F01025)
  + Launch Flags：输入aa start命令相关的选项，请参见[aa start 参数](aa-tool.md)。

### 配置环境变量

如果开发者需要配置和管理应用开发环境，以及控制应用程序的行为，可在**Environment Variables**下配置环境变量。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/oF_ookNXSKC8SFbXWh2bqA/zh-cn_image_0000002779407126.png?HW-CC-KV=V1&HW-CC-Date=20261114T004712Z&HW-CC-Expire=31536000000&HW-CC-Sign=A7BDC4F732A44B57C1DE408835E9203F1F23DE34BB148FCB542BFA6DA75787D2)

点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/bAbkaJF_TlyGm8bu1hMznA/zh-cn_image_0000002779567114.png?HW-CC-KV=V1&HW-CC-Date=20261114T004712Z&HW-CC-Expire=31536000000&HW-CC-Sign=E04C06EA0ED69F241133CA21CE90EDE4312C4CEBE9C768AE62E6230EF86DA05C)按钮，新增一行配置项。当前支持以下配置项：

* ASAN\_OPTIONS：在运行时配置ASan的行为，包括设置检测级别、输出格式、内存错误报告的详细程度等，具体可配置的value请参见[配置参数](../best-practices/bpta-stability-asan-detection.md#section1496994494018)。若开发者未配置log\_exe\_name、abort\_on\_error，DevEco Studio将自动填充。ASAN\_OPTIONS是应用级别的，只在entry和feature模块中配置生效，HAR/HSP模块配置不生效。

**说明** 

当配置Environment Variables后，“Keep Application Data”覆盖安装不生效。

环境变量配置完成后，需确保环境变量已勾选，勾选后点击**Apply**才可生效。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d8/v3/HkXzWkojRqC4BTlvycbPqQ/zh-cn_image_0000002808886777.png?HW-CC-KV=V1&HW-CC-Date=20261114T004712Z&HW-CC-Expire=31536000000&HW-CC-Sign=1C620BC1F47EA91171302B4695BFED7E6AC0844699995A465772217D129AAFDB)

## 自动映射WebView调试链接

当应用中含有需要调试的WebView组件页面时，可以通过浏览器的DevTools工具进行页面调试，具体可参考[使用DevTools工具调试前端页面](web-debugging-with-devtools.md)。调试WebView组件需要执行转发端口等繁琐的命令行操作，因此可以在DevEco Studio中勾选**Auto WebView Debug**，该操作会在应用启动后两分钟内自动监听可调试的WebView进程并完成端口转发。

该功能从DevEco Studio 5.0.5 Release版本开始支持。

设置方法如下：

单击**Run** **>** **Edit Configurations**，在**General**中，勾选**Auto WebView Debug**。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7a/v3/zZteU6fTSf2PGKOcj2xI9Q/zh-cn_image_0000002779567120.png?HW-CC-KV=V1&HW-CC-Date=20261114T004712Z&HW-CC-Expire=31536000000&HW-CC-Sign=832C8560130D68FCB807D76FC65A3811BBBA1EDF0DA0377AAC6AFCFBBC282188)

开启后，当检测到设备上有可调试的WebView组件进程时，会在Run面板中打印转发成功的端口，通过浏览器的DevTools工具连接该端口即可进行WebView调试。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2/v3/pDqPE0hiQS2I1DCMkR9k-A/zh-cn_image_0000002808766681.png?HW-CC-KV=V1&HW-CC-Date=20261114T004712Z&HW-CC-Expire=31536000000&HW-CC-Sign=2FC96C5E1E1B9FD564483FD43F5F701333541C638066EF100A3C1BF6150EE565)

## 多模块调试

### 安装多个模块

如果一个工程中同一个设备存在多个模块（如存在entry和feature模块），且存在模块间的调用时，在调试阶段需要同时安装多个模块的Hap包到设备中。此时，需要在**Deploy Multi Hap****/Hsp**中选择多个模块，启动调试时，DevEco Studio会将所有的模块都安装到设备上。

设置方法如下：

单击**Run > Edit Configurations**，在**Deploy Multi Hap****/Hsp**中，勾选**Deploy Multi Hap/Hsp Packages**，选择多个模块。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/70/v3/6Emek7n1SbqB7plCAMwG3A/zh-cn_image_0000002779407138.png?HW-CC-KV=V1&HW-CC-Date=20261114T004712Z&HW-CC-Expire=31536000000&HW-CC-Sign=8ECC0FB7FDE5B8963EC0C159FBDC0BED2ED2E215D83240425B477F1461E87A68)

### 自动安装依赖

如果一个工程中entry/feature/HSP模块直接依赖其他HAR/HSP模块（如entry模块依赖HSP模块）及间接依赖其他模块（如entry模块依赖HAR模块，HAR又依赖HSP模块），在调试阶段需要同时安装模块包及其所有依赖模块的包到设备中，此时，可以设置**Auto Dependencies**，启动调试时会自动将所有依赖的模块都安装到设备上。

设置方法如下：

单击**Run > Edit Configurations**，在**General**中，勾选**Auto Dependencies。**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/74/v3/R3lIr6DPQKaejuFOF2JMBg/zh-cn_image_0000002779407118.png?HW-CC-KV=V1&HW-CC-Date=20261114T004712Z&HW-CC-Expire=31536000000&HW-CC-Sign=422788E5C711FA3B6EE4BA68C13C4580EEDFF8C3C1506843C812CFA4941F59B0)

在Before launch窗格中，您可以点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8a/v3/RJc6CA5xSNKDcQzSLThp4g/zh-cn_image_0000002808886763.png?HW-CC-KV=V1&HW-CC-Date=20261114T004712Z&HW-CC-Expire=31536000000&HW-CC-Sign=3795062A78EEA56FE589A07205408EAE751809DF123D5A22D492752B0569F187)添加应用启动前的任务。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6d/v3/ihWC-VTnTp6KeYrWs4etBg/zh-cn_image_0000002808766683.png?HW-CC-KV=V1&HW-CC-Date=20261114T004712Z&HW-CC-Expire=31536000000&HW-CC-Sign=3AFB3CB8080F25ED90A474C193C5A19A5260A6414C9B6F5F6ADFEAD3E4B84809)

也可以点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3d/v3/5tLZcmxUTTeRpiUReEXGpg/zh-cn_image_0000002808886761.png?HW-CC-KV=V1&HW-CC-Date=20261114T004712Z&HW-CC-Expire=31536000000&HW-CC-Sign=D1547A6C599C33056062AECEE84219D57D929688F26DC734D4E1526A1A1C560D)移除任务。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/59/v3/FjEZdfZXT6SBReCF5b6aVw/zh-cn_image_0000002808766679.png?HW-CC-KV=V1&HW-CC-Date=20261114T004712Z&HW-CC-Expire=31536000000&HW-CC-Sign=C0D11D69D261423C94DF93452114921CE8DBDAEB9A75F5A7CB858653426CDC30)

在勾选**Auto Dependencies**后，可以同时勾选**Deploy Multi Hap/Hsp Packages**，从而达到推送所有包的效果。

## 多设备运行

从DevEco Studio 6.0.2 Beta1版本开始，支持同时在多个设备上运行应用，包括真机和已启动的模拟器。

1. 在设备选择框中，点击**Select Multiple Devices**，弹出多设备选择框。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/BDa-DZZFRZuMNdkIzuypxg/zh-cn_image_0000002808766687.png?HW-CC-KV=V1&HW-CC-Date=20261114T004712Z&HW-CC-Expire=31536000000&HW-CC-Sign=A5951BBC407414548432B60FB28773040282DB7D879819A9CD3EE02405D4C5DE)
2. 选择需要推包运行的设备。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/99/v3/W3evNx5JQjyruHz-w6FQVA/zh-cn_image_0000002808886771.png?HW-CC-KV=V1&HW-CC-Date=20261114T004712Z&HW-CC-Expire=31536000000&HW-CC-Sign=5E0FF627F41F8B2D295010578963AE3B03452CA3AF1981477FFF6D6224C75267)
3. 设备栏会出现Multiple Devices(N)，表示选中N个设备，点击运行按钮即可同时在选中设备上运行应用。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/70/v3/7Kh4hkHQQMOY_3GLesFKOA/zh-cn_image_0000002808886765.png?HW-CC-KV=V1&HW-CC-Date=20261114T004712Z&HW-CC-Expire=31536000000&HW-CC-Sign=36F6EA97E80838B23226274B431EA03D871C13F79EFD0D17EBE834FE007C3325)
