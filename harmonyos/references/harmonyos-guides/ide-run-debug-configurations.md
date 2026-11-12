---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-run-debug-configurations
title: 自定义运行/调试配置
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 应用调试 > 自定义运行/调试配置
category: harmonyos-guides
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:fc310013d98a82d8e306b94545d94a605d08ac8f8ada543c6cca626f6a6d7507
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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/50/v3/bod7vOWhRgCAUBb2yLwyPQ/zh-cn_image_0000002808886759.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=5A17F65FA521F3B43BE4ACE00D013EE0D2D7AAD735957B807F4C31F4C5BCF12B)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/09/v3/V8V1zrDKRqKc7J0-90vU7g/zh-cn_image_0000002779407140.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=300F36748DCBB62D70D2345E1CAD83F9B9A832F167EAAA76059A7C4C2E65A017)

### 配置自定义调试参数

如果未进行自定义，将按默认配置安装和运行应用。如果开发者需要对应用安装、运行等流程增加参数配置，可在“Installation Options”和“Launch Options”下进行配置。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7a/v3/NT2QpMKkRfuf1KSWtfDgQQ/zh-cn_image_0000002808766677.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=7E397B229358B925D4A5CEF3504F43E59D62507F8BA5BD3F1C466651CAF08258)

* Installation Options
  + DebugLine Support：勾选Enable DebugLine表示在构建产物中系统组件增加debugline属性，用于开启[ArkUI Inspector源码跳转](ide-arkui-inspector.md#section1226015494335)功能。
  + Install Flags：输入bm install命令相关的选项，请参见[bm install 参数](bm-tool.md#安装命令install)。如可以设置“-w 360”，表示将超时等待时间设置为360秒。
* Launch Options
  + Launch：指定在安装应用后启动的Ability。

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/57/v3/gA6cLcZJSymZ2viysApFig/zh-cn_image_0000002808766693.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=4F9AB50F870F3BD9CBF2303A8238FE3392E83461D57FACCCD3BFAE418F9B0D51)
    - Nothing：只安装不启动任何Ability。
    - Default Ability：默认的EntryAbility。
      * Stage模型：module.json5文件中配置了“skills”属性的第一个ability；若无配置“skills”属性的ability，则取“mainElement”指定的ability（该ability需存在于“abilities”数组内）；若“mainElement”未指定，则取“abilities”数组内的第一个ability。

        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4b/v3/j4qcWeX3ScCdRhZY-qC8ZA/zh-cn_image_0000002779567108.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=A3455A1105E6EF21CEA434FF3A4A8AE8A96FD2EC8EF29610170C11C9D1062343 "点击放大")
      * FA模型：config.json文件中配置了“skills”属性的第一个ability；若无配置“skills”属性的ability，则取“mainAbility”指定的ability（该ability需存在于“abilities”数组内）；若“mainAbility”未指定，则取“abilities”数组内的第一个ability。
    - Specified Ability：工程中的UIAbility或ExtensionAbility。

      您可以在工程中添加UIAbility或ExtensionAbility，详细请查看[UIAbility开发指导](uiability.md)或[ExtensionAbility开发指导](extensionability-overview.md)。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d5/v3/6LDS8JJNSp-zWQ-fm7R1mA/zh-cn_image_0000002779407132.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=2BF91C01727EBF520096AD3C837D75E7E3C8B8E75D82F5700C5800DC12223197)
  + Launch Flags：输入aa start命令相关的选项，请参见[aa start 参数](aa-tool.md)。

### 配置环境变量

如果开发者需要配置和管理应用开发环境，以及控制应用程序的行为，可在**Environment Variables**下配置环境变量。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fe/v3/sNODw_UZQiWBlJCxpTWirg/zh-cn_image_0000002779407126.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=58B1BA50D64EAC8555DAA33FE219C67A44CFBE01D1B1266415F90E4CF6E02DC6)

点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/61/v3/2fqsFF92Tqm0ngpcALmBqw/zh-cn_image_0000002779567114.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=3FE3D362B39FE004DD13C078E631494E918AA210F5BF3E09AE4FA9C8FC2489D5)按钮，新增一行配置项。当前支持以下配置项：

* ASAN\_OPTIONS：在运行时配置ASan的行为，包括设置检测级别、输出格式、内存错误报告的详细程度等，具体可配置的value请参见[配置参数](../best-practices/bpta-stability-asan-detection.md#section1496994494018)。若开发者未配置log\_exe\_name、abort\_on\_error，DevEco Studio将自动填充。ASAN\_OPTIONS是应用级别的，只在entry和feature模块中配置生效，HAR/HSP模块配置不生效。

**说明** 

当配置Environment Variables后，“Keep Application Data”覆盖安装不生效。

环境变量配置完成后，需确保环境变量已勾选，勾选后点击**Apply**才可生效。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/73/v3/nYooiurVTbqnig-qljRmug/zh-cn_image_0000002808886777.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=3D3E855284303745E20FE5A2947ED2810921CD0C6862929E36E3A7896D6E0D54)

## 自动映射WebView调试链接

当应用中含有需要调试的WebView组件页面时，可以通过浏览器的DevTools工具进行页面调试，具体可参考[使用DevTools工具调试前端页面](web-debugging-with-devtools.md)。调试WebView组件需要执行转发端口等繁琐的命令行操作，因此可以在DevEco Studio中勾选**Auto WebView Debug**，该操作会在应用启动后两分钟内自动监听可调试的WebView进程并完成端口转发。

该功能从DevEco Studio 5.0.5 Release版本开始支持。

设置方法如下：

单击**Run** **>** **Edit Configurations**，在**General**中，勾选**Auto WebView Debug**。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a3/v3/nQZjbUdpQ4ysmRcrZ_ZAcw/zh-cn_image_0000002779567120.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=B8650E6B3916D31C0B88E99B39A0FAFAF5D93CD38BD193B739DE7733264B2957)

开启后，当检测到设备上有可调试的WebView组件进程时，会在Run面板中打印转发成功的端口，通过浏览器的DevTools工具连接该端口即可进行WebView调试。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/65/v3/_skY__V3RhmjPgzFzkb22A/zh-cn_image_0000002808766681.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=7BB75AC5E761229E695C626E1A5C960662A1F7917C0D5E8EB27227612C079E48)

## 多模块调试

### 安装多个模块

如果一个工程中同一个设备存在多个模块（如存在entry和feature模块），且存在模块间的调用时，在调试阶段需要同时安装多个模块的Hap包到设备中。此时，需要在**Deploy Multi Hap****/Hsp**中选择多个模块，启动调试时，DevEco Studio会将所有的模块都安装到设备上。

设置方法如下：

单击**Run > Edit Configurations**，在**Deploy Multi Hap****/Hsp**中，勾选**Deploy Multi Hap/Hsp Packages**，选择多个模块。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1b/v3/8Mx7z_THQIKf0n_-oL-WIQ/zh-cn_image_0000002779407138.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=3DED9FA021E86023015C3568AB1FD02779FA40A0DB51FF15730F6AE78C0D1D00)

### 自动安装依赖

如果一个工程中entry/feature/HSP模块直接依赖其他HAR/HSP模块（如entry模块依赖HSP模块）及间接依赖其他模块（如entry模块依赖HAR模块，HAR又依赖HSP模块），在调试阶段需要同时安装模块包及其所有依赖模块的包到设备中，此时，可以设置**Auto Dependencies**，启动调试时会自动将所有依赖的模块都安装到设备上。

设置方法如下：

单击**Run > Edit Configurations**，在**General**中，勾选**Auto Dependencies。**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/Neu1eCVpQzasymlQvu_q0A/zh-cn_image_0000002779407118.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=CF188B00D1DE1DC2922ADC721B90A8099DCBC71912B68B98E2119CBE135D91D5)

在Before launch窗格中，您可以点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1b/v3/v3Zuj46VR66nCGyGjkq6bg/zh-cn_image_0000002808886763.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=D369E48B3BE77F032DBAB85203382F02626795076B9FA713C55F60561855DD8D)添加应用启动前的任务。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8a/v3/5UXk4TkHTe2wYkrig9zc1Q/zh-cn_image_0000002808766683.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=AAB44D4E4E53D1A54F877542A640FB1F728FBD136CCC191A12532A0D5960B338)

也可以点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fb/v3/coEjTovrTeGv_JwAPumSNA/zh-cn_image_0000002808886761.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=0C2386E56971E229A4CC05CEC15DDD3E79AB232771842042F4A4FB409E4211CF)移除任务。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/24/v3/-AE-FJFkSEqQL8GNH-U3JA/zh-cn_image_0000002808766679.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=F4135E254FAFEE7022E7F78F7FFFAD0B7653A70C9E3FA2B4130BC9B9654B9871)

在勾选**Auto Dependencies**后，可以同时勾选**Deploy Multi Hap/Hsp Packages**，从而达到推送所有包的效果。

## 多设备运行

从DevEco Studio 6.0.2 Beta1版本开始，支持同时在多个设备上运行应用，包括真机和已启动的模拟器。

1. 在设备选择框中，点击**Select Multiple Devices**，弹出多设备选择框。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/38/v3/rCOEdAuTS5Wu7oQr-AlAnA/zh-cn_image_0000002808766687.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=1904E5D2CF45F3F87AC3B0F2C77E118A031AF48FE29FA7AB32D06B5D2E3D4A91)
2. 选择需要推包运行的设备。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/47/v3/HvA0QwvUSFq6Jm9-dyAJ9Q/zh-cn_image_0000002808886771.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=DDC0A7B8FB24A37490E17C2565950AAA9B8A608BBBBA0BADC34E98D07080815B)
3. 设备栏会出现Multiple Devices(N)，表示选中N个设备，点击运行按钮即可同时在选中设备上运行应用。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1b/v3/7Z9yvqksQRu1zWt1r1Hyyg/zh-cn_image_0000002808886765.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=AE839288319EF894F0734D2DB1218969C17F785D0FA58449455C852FEE575971)
