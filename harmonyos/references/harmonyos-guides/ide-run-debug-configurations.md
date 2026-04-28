---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-run-debug-configurations
title: 自定义运行/调试配置
breadcrumb: 指南 > 编写与调试应用 > 应用调试 > 自定义运行/调试配置
category: harmonyos-guides
scraped_at: 2026-04-28T07:56:45+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:5b86bfb817e65260e61f696c2f3db5f88f06ead9474615e03a72f7e3f7ce82ec
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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a6/v3/mUBN1LIiSEWwv1mRo-11pw/zh-cn_image_0000002530913390.png?HW-CC-KV=V1&HW-CC-Date=20260427T235644Z&HW-CC-Expire=86400&HW-CC-Sign=7BD40050A7AA9BD2ADD3487E604CF0BB6A182EF8E26BFC763B3B5EC2769027F6)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6a/v3/XvHBf9TPR-e7FOnVDJdgeA/zh-cn_image_0000002530913378.png?HW-CC-KV=V1&HW-CC-Date=20260427T235644Z&HW-CC-Expire=86400&HW-CC-Sign=C2B31E3D855BD5D5C5CBAEA6F0D53C25C514BE6868BAF29A1CA3DB21E16E78DA)

### 配置自定义调试参数

如果未进行自定义，将按默认配置安装和运行应用。如果开发者需要对应用安装、运行等流程增加参数配置，可在“Installation Options”和“Launch Options”下进行配置。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/80/v3/gevp-gfWQ3GO7nMGKSl3Tg/zh-cn_image_0000002530913374.png?HW-CC-KV=V1&HW-CC-Date=20260427T235644Z&HW-CC-Expire=86400&HW-CC-Sign=4A7C449BBFC5F815BBA95C22E0ABFBC33ACA80CB36E2B83FCEE14D77D1637141)

* Installation Options
  + DebugLine Support：勾选Enable DebugLine表示在build产物中系统组件增加debugline属性，用于开启[ArkUI Inspector源码跳转](ide-arkui-inspector.md#section1226015494335)功能。
  + Install Flags：输入bm install命令相关的选项，请参见[bm install 参数](bm-tool.md#安装命令install)。如可以设置“-w 360”，表示将超时等待时间设置为360秒。
* Launch Options
  + Launch：指定在安装应用后启动的Ability。

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b7/v3/OxDhp3gDQhufAqpdHGJLzw/zh-cn_image_0000002530753382.png?HW-CC-KV=V1&HW-CC-Date=20260427T235644Z&HW-CC-Expire=86400&HW-CC-Sign=E2E0068A42E6FC4A30694525D55902C636DE28D43812CD6F4B53E81A1F8D12C2)
    - Nothing：只安装不启动任何Ability。
    - Default Ability：默认的EntryAbility。
      * Stage模型：module.json5文件中配置了“skills”属性的第一个ability；若无配置“skills”属性的ability，则取“mainElement”指定的ability（该ability需存在于“abilities”数组内）；若“mainElement”未指定，则取“abilities”数组内的第一个ability。

        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a4/v3/kpkvmznNSAG3eScPyn27yQ/zh-cn_image_0000002530913382.png?HW-CC-KV=V1&HW-CC-Date=20260427T235644Z&HW-CC-Expire=86400&HW-CC-Sign=B4BDCFD7A8A9DD1961A7E7640404CB2F7ACABA750CD419442C6F5BE8432DB07F "点击放大")
      * FA模型：config.json文件中配置了“skills”属性的第一个ability；若无配置“skills”属性的ability，则取“mainAbility”指定的ability（该ability需存在于“abilities”数组内）；若“mainAbility”未指定，则取“abilities”数组内的第一个ability。
    - Specified Ability：工程中的UIAbility或ExtensionAbility。

      您可以在工程中添加UIAbility或ExtensionAbility，详细请查看[UIAbility开发指导](uiability.md)或[ExtensionAbility开发指导](extensionability-overview.md)。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/34/v3/Kh5NkcOcTD62jqSGxwtsJw/zh-cn_image_0000002530913376.png?HW-CC-KV=V1&HW-CC-Date=20260427T235644Z&HW-CC-Expire=86400&HW-CC-Sign=EF6C86C647AD3F17C7E1C5F4C494F486FFACA55CD85B41FD9987FEDF7451F4B2)
  + Launch Flags：输入aa start命令相关的选项，请参见[aa start 参数](aa-tool.md)。

### 配置环境变量

如果开发者需要配置和管理应用开发环境，以及控制应用程序的行为，可在**Environment Variables**下配置环境变量。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d9/v3/quCDKuDJQKCtd5YhzE1Emg/zh-cn_image_0000002561833303.png?HW-CC-KV=V1&HW-CC-Date=20260427T235644Z&HW-CC-Expire=86400&HW-CC-Sign=AF3495C91F395289880D0C3EFFC709629DBFCF509DF2B04AFB457653CC1F35FC)

点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/48/v3/7xCaC2oYSBy6r0Ud0gCtbQ/zh-cn_image_0000002561833309.png?HW-CC-KV=V1&HW-CC-Date=20260427T235644Z&HW-CC-Expire=86400&HW-CC-Sign=21AEC8E09DA2C6D0C9C9D5A6F4F1E4AFB62EF9411C2E98EAACF5EDB0C0F4E2E2)按钮，新增一行配置项。当前支持以下配置项：

* ASAN\_OPTIONS：在运行时配置ASan的行为，包括设置检测级别、输出格式、内存错误报告的详细程度等，具体可配置的value请参见[配置参数](../best-practices/bpta-stability-asan-detection.md#section1496994494018)。若开发者未配置log\_exe\_name、abort\_on\_error，DevEco Studio将自动填充。ASAN\_OPTIONS是应用级别的，只在entry和feature模块中配置生效，HAR/HSP模块配置不生效。

说明

当配置Environment Variables后，“Keep Application Data”覆盖安装不生效。

环境变量配置完成后，需确保环境变量已勾选，勾选后点击**Apply**才可生效。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/38/v3/NVpcbfsJTlejqE4umihr7A/zh-cn_image_0000002561753325.png?HW-CC-KV=V1&HW-CC-Date=20260427T235644Z&HW-CC-Expire=86400&HW-CC-Sign=3D7B873B304E1913A0C616EB86C05C97B6B0DA515D4336C25DF3E5D898B4B005)

## 自动映射WebView调试链接

当应用中含有需要调试的WebView组件页面时，可以通过浏览器的DevTools工具进行页面调试，具体可参考[使用DevTools工具调试前端页面](web-debugging-with-devtools.md)。调试WebView组件需要执行转发端口等繁琐的命令行操作，因此可以在DevEco Studio中勾选**Auto WebView Debug**，该操作会在应用启动后两分钟内自动监听可调试的WebView进程并完成端口转发。

该功能从DevEco Studio 5.0.5 Release版本开始支持。

设置方法如下：

单击**Run** **>** **Edit Configurations**，在**General**中，勾选**Auto WebView Debug**。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/85/v3/21D7YB9xR-mYO3di_wRplQ/zh-cn_image_0000002561753313.png?HW-CC-KV=V1&HW-CC-Date=20260427T235644Z&HW-CC-Expire=86400&HW-CC-Sign=028D90341C48CFEBFA73A9E577550CC9821AF2CF511845BBC1508750808AFFA3)

开启后，当检测到设备上有可调试的WebView组件进程时，会在Run面板中打印转发成功的端口，通过浏览器的DevTools工具连接该端口即可进行WebView调试。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/4qRIq79rS0e8OhZ4qT5BvQ/zh-cn_image_0000002561753337.png?HW-CC-KV=V1&HW-CC-Date=20260427T235644Z&HW-CC-Expire=86400&HW-CC-Sign=A6B515F6C795F9F2D9100C7BA5AB85413019BC3F85472B6C7ACC1C59BC63ADCC)

## 多模块调试

### 安装多个模块

如果一个工程中同一个设备存在多个模块（如存在entry和feature模块），且存在模块间的调用时，在调试阶段需要同时安装多个模块的Hap包到设备中。此时，需要在**Deploy Multi Hap****/Hsp**中选择多个模块，启动调试时，DevEco Studio会将所有的模块都安装到设备上。

设置方法如下：

单击**Run > Edit Configurations**，在**Deploy Multi Hap****/Hsp**中，勾选**Deploy Multi Hap/Hsp Packages**，选择多个模块。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d2/v3/7qdzFjYHSAupB9GFAhF0xw/zh-cn_image_0000002561833295.png?HW-CC-KV=V1&HW-CC-Date=20260427T235644Z&HW-CC-Expire=86400&HW-CC-Sign=C7E7DF1DFA1C55C08DAACDBDDF7C8CE33B05A8C7C52E42E6DB6FB71D5A6BF50E)

### 自动安装依赖

如果一个工程中entry/feature/HSP模块直接依赖其他HAR/HSP模块（如entry模块依赖HSP模块）及间接依赖其他模块（如entry模块依赖HAR模块，HAR又依赖HSP模块）时，在调试阶段需要同时安装模块包及其所有依赖模块的包到设备中。此时，可以设置**Auto Dependencies**，启动调试时会自动将所有依赖的模块都安装到设备上。

设置方法如下：

单击**Run > Edit Configurations**，在**General**中，勾选**Auto Dependencies。**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/HNeX6e_3Q5-L86glmh-kSw/zh-cn_image_0000002561753333.png?HW-CC-KV=V1&HW-CC-Date=20260427T235644Z&HW-CC-Expire=86400&HW-CC-Sign=6BF511D85E3FC17D79BD2E1E0FC347770EE1F79C8FE45556DEC6D2743302FE39)

在Before launch窗格中，您可以点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/31/v3/Tod02AxISJmrj4jnESix4w/zh-cn_image_0000002530913388.png?HW-CC-KV=V1&HW-CC-Date=20260427T235644Z&HW-CC-Expire=86400&HW-CC-Sign=482BF2E338744C4B6E44E02966B41A87E6ECE69595A81D16945BF31F0FEC4A86)添加应用启动前的任务。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e6/v3/veW8L9BxTZCtB4QFZSsBjw/zh-cn_image_0000002561753327.png?HW-CC-KV=V1&HW-CC-Date=20260427T235644Z&HW-CC-Expire=86400&HW-CC-Sign=35ADAB6D9CD047B5A8BF3CD2D617CAEE15134DE57B481A9D44791CBAF11009C3)

也可以点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a6/v3/h9n2VQorS5asp9dvzsgBWg/zh-cn_image_0000002561753331.png?HW-CC-KV=V1&HW-CC-Date=20260427T235644Z&HW-CC-Expire=86400&HW-CC-Sign=34597FE027A0AD4F057B9997D0B0B9E5DD79F358D07656D71D1B4DA72D594BCC)移除任务。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/37/v3/jgPK7r6eR2ai6IWrJr19rA/zh-cn_image_0000002530753378.png?HW-CC-KV=V1&HW-CC-Date=20260427T235644Z&HW-CC-Expire=86400&HW-CC-Sign=DD9FD0B113E03415E088DD894DBCD843B571B86FCB6986C1EE5EB943827CC99F)

在勾选**Auto Dependencies**后，可以同时勾选**Deploy Multi Hap/Hsp Packages**，从而达到推送所有包的效果。

## 多设备运行

从DevEco Studio 6.0.2 Beta1版本开始，支持同时在多个设备上运行应用，包括真机和已启动的模拟器。

1. 在设备选择框中，点击**Select Multiple Devices**，弹出多设备选择框。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d4/v3/BpsMkOYLQuq6aY76jOjYFg/zh-cn_image_0000002530753380.png?HW-CC-KV=V1&HW-CC-Date=20260427T235644Z&HW-CC-Expire=86400&HW-CC-Sign=A37C8ABE3514AF4A251B44CDF4EBF70771419860A66E5E7EBFBDA5339BC60261)
2. 选择需要推包运行的设备。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/db/v3/lgTW5fWxRQiCG5e3h_9yRQ/zh-cn_image_0000002530753394.png?HW-CC-KV=V1&HW-CC-Date=20260427T235644Z&HW-CC-Expire=86400&HW-CC-Sign=0AA49214868401490E9AA2C567B1DF647C423B2C9E97D725C45D6F6DC7105ED6)
3. 设备栏会出现Multiple Devices(N)，表示选中N个设备，点击运行按钮即可同时在选中设备上运行应用。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d6/v3/Ya050xnFSra93h0srd_3MA/zh-cn_image_0000002561833307.png?HW-CC-KV=V1&HW-CC-Date=20260427T235644Z&HW-CC-Expire=86400&HW-CC-Sign=52BF412E4DE46273C3C19A89AEECBE6C23F9A3ED190CFA47D9AB78E18D040D90)
