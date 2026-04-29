---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-run-debug-configurations
title: 自定义运行/调试配置
breadcrumb: 指南 > 编写与调试应用 > 应用调试 > 自定义运行/调试配置
category: harmonyos-guides
scraped_at: 2026-04-29T13:46:40+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:2aaf5118f25cc920ed1a3f3513b90777e8ed3e197998f018bdee2e00d91d377c
---

## 配置应用可调试

应用是否支持调试，根据app.json5的debug字段和build-profile.json5的debuggable字段综合判断，app.json5的优先级高于build-profile.json5。

1. 在app.json5中配置debug字段：
   * true：应用支持调试。
   * false：应用不支持调试。
2. 如果没有配置debug字段，则根据build-profile.json5的debuggable字段判断应用是否支持调试。
   * true：应用支持调试。当[编译模式](ide-hvigor-compilation-options-customizing-guide.md#section192461528194916)不是release时，debuggable的缺省值是true，即支持调试。
   * false：应用不支持调试。当编译模式为release时，debuggable的缺省值是false，即不支持调试。

## 设置调试代码类型

点击**Run > Edit Configurations > Debugger**，选择相应模块，设置Debug type即可。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/13/v3/R4x8E-qrSoCw4aWWYSdQsw/zh-cn_image_0000002530913390.png?HW-CC-KV=V1&HW-CC-Date=20260429T054638Z&HW-CC-Expire=86400&HW-CC-Sign=117D352AB4834E38C648E58A73DCFDF4CF220C48859B0EF3F3415C8F7BCDDE04)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/db/v3/pKgN6a6xS1qhwUGroWkFfQ/zh-cn_image_0000002530913378.png?HW-CC-KV=V1&HW-CC-Date=20260429T054638Z&HW-CC-Expire=86400&HW-CC-Sign=46103978CBE19C90D77FD495563A96A20B20DF7E715A1501ED1B3227876D5D98)

### 配置自定义调试参数

如果未进行自定义，将按默认配置安装和运行应用。如果开发者需要对应用安装、运行等流程增加参数配置，可在“Installation Options”和“Launch Options”下进行配置。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1f/v3/Y0KwMLZ-SlyFZrbmSJs4hQ/zh-cn_image_0000002530913374.png?HW-CC-KV=V1&HW-CC-Date=20260429T054638Z&HW-CC-Expire=86400&HW-CC-Sign=5EECBD103C0079027A41BA6482AE0702F64B9F01ABB02632BD43584156B72223)

* Installation Options
  + DebugLine Support：勾选Enable DebugLine表示在build产物中系统组件增加debugline属性，用于开启[ArkUI Inspector源码跳转](ide-arkui-inspector.md#section1226015494335)功能。
  + Install Flags：输入bm install命令相关的选项，请参见[bm install 参数](bm-tool.md#安装命令install)。如可以设置“-w 360”，表示将超时等待时间设置为360秒。
* Launch Options
  + Launch：指定在安装应用后启动的Ability。

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ca/v3/6rvtQ5eyRayeCIbisRH97w/zh-cn_image_0000002530753382.png?HW-CC-KV=V1&HW-CC-Date=20260429T054638Z&HW-CC-Expire=86400&HW-CC-Sign=EFF66557D61FCD5014F67A15FC89CA1016F0FE42BF274A64D3C2CE9CE248380E)
    - Nothing：只安装不启动任何Ability。
    - Default Ability：默认的EntryAbility。
      * Stage模型：module.json5文件中配置了“skills”属性的第一个ability；若无配置“skills”属性的ability，则取“mainElement”指定的ability（该ability需存在于“abilities”数组内）；若“mainElement”未指定，则取“abilities”数组内的第一个ability。

        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0c/v3/_VRd5QrxS8-vCvqJeqwgVA/zh-cn_image_0000002530913382.png?HW-CC-KV=V1&HW-CC-Date=20260429T054638Z&HW-CC-Expire=86400&HW-CC-Sign=211F2DFFA18510DA68DF92EBF537133F35B8E73203071DE8CD0536F769ECA694 "点击放大")
      * FA模型：config.json文件中配置了“skills”属性的第一个ability；若无配置“skills”属性的ability，则取“mainAbility”指定的ability（该ability需存在于“abilities”数组内）；若“mainAbility”未指定，则取“abilities”数组内的第一个ability。
    - Specified Ability：工程中的UIAbility或ExtensionAbility。

      您可以在工程中添加UIAbility或ExtensionAbility，详细请查看[UIAbility开发指导](uiability.md)或[ExtensionAbility开发指导](extensionability-overview.md)。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ce/v3/ntCqaJ0aTeGGaQpPmzKXrw/zh-cn_image_0000002530913376.png?HW-CC-KV=V1&HW-CC-Date=20260429T054638Z&HW-CC-Expire=86400&HW-CC-Sign=C4ACD440ACE9A1FDCFC94E46BA739E2F5E64D1D7D6650976F18D5520D61ADC70)
  + Launch Flags：输入aa start命令相关的选项，请参见[aa start 参数](aa-tool.md)。

### 配置环境变量

如果开发者需要配置和管理应用开发环境，以及控制应用程序的行为，可在**Environment Variables**下配置环境变量。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0c/v3/GEcaHfZlQVOObHHELviMgQ/zh-cn_image_0000002561833303.png?HW-CC-KV=V1&HW-CC-Date=20260429T054638Z&HW-CC-Expire=86400&HW-CC-Sign=56B74309A73E83246BFD556E4F82B112389F26427670AFF1B5189A30A61BFD85)

点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/07/v3/G-Z5SNuoTZW9-YadHG-Cbg/zh-cn_image_0000002561833309.png?HW-CC-KV=V1&HW-CC-Date=20260429T054638Z&HW-CC-Expire=86400&HW-CC-Sign=50AB4E928A3E1BDCE877493D604236ABAD61152F9E0281D9B8BECBA81A6D5B79)按钮，新增一行配置项。当前支持以下配置项：

* ASAN\_OPTIONS：在运行时配置ASan的行为，包括设置检测级别、输出格式、内存错误报告的详细程度等，具体可配置的value请参见[配置参数](../best-practices/bpta-stability-asan-detection.md#section1496994494018)。若开发者未配置log\_exe\_name、abort\_on\_error，DevEco Studio将自动填充。ASAN\_OPTIONS是应用级别的，只在entry和feature模块中配置生效，HAR/HSP模块配置不生效。

说明

当配置Environment Variables后，“Keep Application Data”覆盖安装不生效。

环境变量配置完成后，需确保环境变量已勾选，勾选后点击**Apply**才可生效。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/74/v3/LFkX-MAHQPyeBQPPYIz4_A/zh-cn_image_0000002561753325.png?HW-CC-KV=V1&HW-CC-Date=20260429T054638Z&HW-CC-Expire=86400&HW-CC-Sign=9BD665F5AC11F226858D43606F53126C5F31524EC51F20001C8A8B83B2D5E329)

## 自动映射WebView调试链接

当应用中含有需要调试的WebView组件页面时，可以通过浏览器的DevTools工具进行页面调试，具体可参考[使用DevTools工具调试前端页面](web-debugging-with-devtools.md)。调试WebView组件需要执行转发端口等繁琐的命令行操作，因此可以在DevEco Studio中勾选**Auto WebView Debug**，该操作会在应用启动后两分钟内自动监听可调试的WebView进程并完成端口转发。

该功能从DevEco Studio 5.0.5 Release版本开始支持。

设置方法如下：

单击**Run** **>** **Edit Configurations**，在**General**中，勾选**Auto WebView Debug**。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/98/v3/zQo681-_Tj2OdCi2h-NcMg/zh-cn_image_0000002561753313.png?HW-CC-KV=V1&HW-CC-Date=20260429T054638Z&HW-CC-Expire=86400&HW-CC-Sign=A2F3D86DCAED98915D5783B409E4BF71B0B498147A5676B17CB85B7815EC8253)

开启后，当检测到设备上有可调试的WebView组件进程时，会在Run面板中打印转发成功的端口，通过浏览器的DevTools工具连接该端口即可进行WebView调试。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a7/v3/oYeYWoIGROeoGzR3XqVEwg/zh-cn_image_0000002561753337.png?HW-CC-KV=V1&HW-CC-Date=20260429T054638Z&HW-CC-Expire=86400&HW-CC-Sign=B19DC5543E94B28B79CCF992BAC43A99BBD142F57CE88381AD6087BAD5F96704)

## 多模块调试

### 安装多个模块

如果一个工程中同一个设备存在多个模块（如存在entry和feature模块），且存在模块间的调用时，在调试阶段需要同时安装多个模块的Hap包到设备中。此时，需要在**Deploy Multi Hap****/Hsp**中选择多个模块，启动调试时，DevEco Studio会将所有的模块都安装到设备上。

设置方法如下：

单击**Run > Edit Configurations**，在**Deploy Multi Hap****/Hsp**中，勾选**Deploy Multi Hap/Hsp Packages**，选择多个模块。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/63/v3/q7x3mfMiQRmPeMNkbJbpsA/zh-cn_image_0000002561833295.png?HW-CC-KV=V1&HW-CC-Date=20260429T054638Z&HW-CC-Expire=86400&HW-CC-Sign=0C5320B67C4D8509FAAADF9FDF830A9793E82969DCC7CCD2FE0DF7142E1C4632)

### 自动安装依赖

如果一个工程中entry/feature/HSP模块直接依赖其他HAR/HSP模块（如entry模块依赖HSP模块）及间接依赖其他模块（如entry模块依赖HAR模块，HAR又依赖HSP模块）时，在调试阶段需要同时安装模块包及其所有依赖模块的包到设备中。此时，可以设置**Auto Dependencies**，启动调试时会自动将所有依赖的模块都安装到设备上。

设置方法如下：

单击**Run > Edit Configurations**，在**General**中，勾选**Auto Dependencies。**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/24/v3/FvhbehCiSf-SIaJ3xjDRJA/zh-cn_image_0000002561753333.png?HW-CC-KV=V1&HW-CC-Date=20260429T054638Z&HW-CC-Expire=86400&HW-CC-Sign=353A4D74F33660DC77BC84B0DFFDB81906549FEC3BAF2761184CF870715AA35B)

在Before launch窗格中，您可以点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/DcPHj1o-R5SojFJQwLxGWA/zh-cn_image_0000002530913388.png?HW-CC-KV=V1&HW-CC-Date=20260429T054638Z&HW-CC-Expire=86400&HW-CC-Sign=83F7D055CC4283CC45EAC632459654C8E7C66D33B12A8CD77CBF6011E1D90134)添加应用启动前的任务。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/61/v3/CVsYtuw2RZ2wX8jPg1IRag/zh-cn_image_0000002561753327.png?HW-CC-KV=V1&HW-CC-Date=20260429T054638Z&HW-CC-Expire=86400&HW-CC-Sign=C3715837192FD7EC5943B3C67A667C68C7CAA7EE5BBA7D3B503E89BF25BEFDBD)

也可以点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e5/v3/4aa5ZKzqSCKVEEVCu4RwaQ/zh-cn_image_0000002561753331.png?HW-CC-KV=V1&HW-CC-Date=20260429T054638Z&HW-CC-Expire=86400&HW-CC-Sign=9290C07EA5AC4ED0D0E3C8BD3C30183BFE94E0F4EDA710685E50C01159CAB48C)移除任务。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/47/v3/mMCUtGTKSE2_z35QzbbfVA/zh-cn_image_0000002530753378.png?HW-CC-KV=V1&HW-CC-Date=20260429T054638Z&HW-CC-Expire=86400&HW-CC-Sign=1207E6CB84B44EA735EA058B01923587D910570011AE6F2563296D53AD358DAB)

在勾选**Auto Dependencies**后，可以同时勾选**Deploy Multi Hap/Hsp Packages**，从而达到推送所有包的效果。

## 多设备运行

从DevEco Studio 6.0.2 Beta1版本开始，支持同时在多个设备上运行应用，包括真机和已启动的模拟器。

1. 在设备选择框中，点击**Select Multiple Devices**，弹出多设备选择框。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/66/v3/65CWm10iRna9zXfKDjPQYQ/zh-cn_image_0000002530753380.png?HW-CC-KV=V1&HW-CC-Date=20260429T054638Z&HW-CC-Expire=86400&HW-CC-Sign=B11CEABA681259A723E448F1F29D5D60EDA416433897772D2ED249353D7A62E4)
2. 选择需要推包运行的设备。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7a/v3/qCBR1D3BSqidkEEB8LfC2g/zh-cn_image_0000002530753394.png?HW-CC-KV=V1&HW-CC-Date=20260429T054638Z&HW-CC-Expire=86400&HW-CC-Sign=60B70BA5E0763618CC3EA9514B9B7521A71535C9AEB6D47165E48DA50350C71E)
3. 设备栏会出现Multiple Devices(N)，表示选中N个设备，点击运行按钮即可同时在选中设备上运行应用。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ae/v3/-jOR6gU5TVmpHgFOPfu-Uw/zh-cn_image_0000002561833307.png?HW-CC-KV=V1&HW-CC-Date=20260429T054638Z&HW-CC-Expire=86400&HW-CC-Sign=75D5C7CCC006BEF4056E62FFC419AF12254B20B6D8D698BA09A71D370D5FFD1F)
