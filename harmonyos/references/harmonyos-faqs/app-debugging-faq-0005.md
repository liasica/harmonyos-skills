---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/app-debugging-faq-0005
title: 真机调试与测试包安装方法常见问题
breadcrumb: FAQ > DevEco Studio > 应用调试 > 常见问题 > 真机调试与测试包安装方法常见问题
category: harmonyos-faqs
scraped_at: 2026-10-28T07:48:59+08:00
doc_updated_at: 2026-10-22
content_hash: sha256:31760f38dfd5e6b2458149d86e3b138ec8791e7ccacea194a5cbb128ea3dd9ea
---

**Q：应用开发过程中，有哪几种方式可以将测试包安装到测试机？**

**A**：可以通过以下四种方式将测试包安装到测试机：

* 方式一：通过hdc命令安装到测试机。
  1. 下载[Command Line Tools](https://developer.huawei.com/consumer/cn/download/command-line-tools-for-hmos)。该命令行工具集合了HarmonyOS应用开发所用到的系列工具，包括代码检查codelinter、三方库的包管理Ohpm、命令行解析hstack、编译构建hvigorw。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ea/v3/biRKT-YeSUCX3tzoIei7Iw/zh-cn_image_0000002765752034.png "点击放大")
  2. 配置环境变量：下载后的压缩包放到D盘，解压后获得文件夹D:\CommandLine-Tools-windows-x64-5.1.0.828SP1\Command-Line-Tools\SDK\default\OpenHarmony\toolchains，右击此电脑-属性-高级系统设置，把该路径添加到环境变量里，cmd窗口输入where hdc检查是否配置成功。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/32/v3/r_4ZeWm6Qwe7-O4kycgNeg/zh-cn_image_0000002765592114.png "点击放大")![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/90/v3/YvPJodpvT5yDfYbJS6gWCg/zh-cn_image_0000002765592116.png "点击放大")
  3. 使用hdc命令安装测试包：测试机进入手机系统设置菜单-关于手机，多次点击版本号启用开发者模式，然后进入系统设置菜单-系统-开发者选项，打开USB调试模式，并通过USB将手机连接到电脑，通过cmd使用命令hdc install <测试包路径>来安装hap包。![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/24/v3/WB6pAEArRE2Zv-hGlXbnvw/zh-cn_image_0000002795030821.png "点击放大")

* 方式二：通过IDE安装到测试机。
  1. 下载新版[DevEco Studio](https://developer.huawei.com/consumer/cn/download/deveco-studio)，并完成安装。安装过程中，新版本已经集成了Node.js、Ohpm和HarmonyOS SDK，因此不需要单独配置这些组件。
  2. 测试机开启开发者模式，采用[USB连接方式](../harmonyos-guides/ide-run-device.md#section171436512424)或者[使用无线调试连接方式](../harmonyos-guides/ide-run-device.md#section9315596477)。
  3. 在DevEco Studio中选择真机，Project Structure（项目结构）-Signing Configs（签名配置）-勾选Automatically generate signature(自动签名)-点击OK完成自动签名，点击“Run”或“Debug”按钮，DevEco Studio自动将hap文件安装到测试机上。具体请参考[使用本地真机运行应用](../harmonyos-guides/ide-run-device.md)。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0b/v3/2dDEjDbpRVulTYM9QaRxiw/zh-cn_image_0000002765752352.png "点击放大")

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a6/v3/N92tdPdDT0aUebEvqmqS6g/zh-cn_image_0000002795150911.png "点击放大")![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/83/v3/TnQjCJyyQiGHeWa4lhgQ2w/zh-cn_image_0000002795150915.png "点击放大")

* 方式三：通过[DevEco Testing](https://developer.huawei.com/consumer/cn/download/deveco-testing)工具安装到测试机。

  测试机开启开发者模式，打开USB调试模式，并通过USB将手机连接到电脑，点击DevEco Testing工具左侧实用工具-设备投屏-开始投屏，点击安装应用，选择安装包路径，点击确定按钮进行安装，安装后可通过执行日志查看安装信息。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d9/v3/GPWIiNy_QoO_ECs9RTSYXQ/zh-cn_image_0000002765753226.png "点击放大")

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f/v3/f2Tq5c-3RXOvx6XbtvVRrQ/zh-cn_image_0000002765753228.png "点击放大")

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/75/v3/FPtAKCc4TEKLsYVf7cAF5Q/zh-cn_image_0000002795151789.png "点击放大")
* 方式四：通过[邀请测试和公开测试](../app/agc-help-harmonyos-testapp-0000001873653977.md)安装到测试机。

  通过HarmonyOS 开发者中心，在应用正式版本发布之前，可以挑选特定的用户群组来测试HarmonyOS应用/元服务，或向AppGallery用户公开发布测试版本。

**Q：开发者在开发Wearable和Lite Wearable设备应用时需要进行调试和调测，具体怎么做？**

**A**：Wearable和Lite Wearable设备调试方法如下：

Wearable设备调试：

前提条件：需要登录华为开发者账号才有无线调试选项。

1. 将Wearable设备和PC连接到同一WLAN网络。

   在设置>系统>开发者选项中，打开"无线调试"或"通过WLAN调试"（Wearable设备）开关，并获取设备端的IP地址和端口号。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/2RjFhS8wSSSZtRQ_YQMe9Q/zh-cn_image_0000002795155791.png "点击放大")
2. 连接设备，有两种方式。

   2.1 在DevEco Studio菜单栏中，单击Tools > IP Connection，输入连接设备的IP地址和端口号，单击，连接正常后，设备状态为online。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/96/v3/rxny1l4LRAWvKlQZfJ67lA/zh-cn_image_0000002765597306.png "点击放大")

   2.2 执行hdc命令，关于hdc工具的使用指导请参考[hdc](../harmonyos-guides/hdc.md)。

   hdc tconn设备IP地址:端口号。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d1/v3/fyDJgCuUQca4ADc-lMQPgQ/zh-cn_image_0000002795036011.png)

   在菜单栏中，单击Run>Run'模块名称'或使用默认快捷键Shift+F10（macOS为Control+R）运行应用/元服务。
3. DevEco Studio启动HAP的编译构建和安装。安装成功后，设备会自动运行安装的HarmonyOS应用/元服务。

Lite wearable设备调试：

前提条件：

1. 运动健康app升级最新版本。
2. 从华为应用市场安装应用调测助手APP。
3. 提前对应用/服务进行[签名](../harmonyos-guides/ide-signing.md)。

具体步骤：

1. 使用USB连接线将手机和电脑进行连接，确保连接状态是正常的。
2. 手机与电脑使用USB连接时，在手机上选择传输文件连接方式。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/46/v3/MX73Rf-ETieOrmuwoC3doA/zh-cn_image_0000002765757618.png "点击放大")
3. 在工程目录中的Build > outputs >hap中选择生成的HAP，通过手工拷贝的方式将HAP拷贝至手机中的"/sdcard/haps/"目录。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/nvVc858oT5ad3Bk3734HHA/zh-cn_image_0000002765597716.png)
4. 将Lite Wearable通过蓝牙与华为手机进行连接。

   4.1 进入运动健康APP，在设备页签中，单击添加设备按钮。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/15/v3/Ku3eh9YlRjSoPj6Rt9thew/zh-cn_image_0000002795036407.png "点击放大")

   4.2 进入手表列表中，选择对应的Lite Wearable型号。

   4.3 单击开始配对，按照界面指引完成Lite Wearable与华为手机之间的连接。
5. 打开应用调测助手APP，界面会显示已经与华为手机连接的Lite Wearable。
6. 单击应用调测助手APP界面中的应用管理按钮，选择需要安装的HarmonyOS安装包进行安装。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e/v3/_gnUjfMrT9S3aC1syMZKaQ/zh-cn_image_0000002765757622.png "点击放大")
7. 安装完成后，单击Lite Wearable中的应用图标，运行HarmonyOS应用。

**Q：HarmonyOS NEXT系统上能否开发Lite Wearable类型的手表应用？**

**A**：Lite Wearable中运行应用/服务依赖HarmonyOS NEXT版本以前的手机上的运动健康和应用调测助手APP辅助进行，暂不支持在HarmonyOS NEXT系统上直接调试Lite Wearable设备。轻量级智能穿戴与智能穿戴在硬件能力和系统支持上不同，暂时无法仅开发一版实现通用。Wearable是当前更主流的方向，是HarmonyOS NEXT生态重点支持的穿戴设备类型。

**Q：通过应用调测助手向Lite Wearable设备安装HAP时提示"安装失败：40.配置文件格式错误"怎么办？**

**A**：该问题通常是由于工程级[build-profile.json5](../harmonyos-guides/ide-hvigor-build-profile-app.md)中[compatibleSdkVersion](../harmonyos-guides/ide-hvigor-build-profile-app.md#section45865492619)配置格式不正确导致。compatibleSdkVersion必须写成5.0.0(12)格式，不能写成其他字符串格式。若配置格式正确但仍报此错误，需检查工程的API版本是否超出目标设备实际支持的SDK版本范围，例如WATCH GT 3对应API 6，使用API 10创建工程会因版本不匹配导致安装失败，需将compatibleSdkVersion和targetSdkVersion调整为设备支持的API版本。

**Q：GT系列手表能否用于穿戴应用测试？**

**A**：可以。GT系列手表属于Lite Wearable（轻量级智能穿戴）设备，应按Lite Wearable方式进行测试，不支持Wearable（智能穿戴）直连方式。当前支持的GT系列手表型号及对应API版本如下：WATCH GT 2（API 5）、WATCH GT 2 Pro（API 6）、WATCH GT 3（API 6）、WATCH GT 4（API 10）、WATCH GT 5（API 12），开发时需按具体型号的API能力做兼容。创建工程时选择"[Lite] Empty Ability"模板，设备类型设为"Lite Wearable"。Lite Wearable设备仅支持JS开发，不支持ArkTS，应使用JS+CSS+HTML的类Web开发范式。GT真机不能直接连接DevEco Studio，需手动签名并在调试Profile中注册设备，将HAP拷贝至华为手机，通过运动健康完成配对，再用应用调测助手安装到手表。基础功能也可先用Lite Wearable预览器或仿真器验证。

**Q：Lite Wearable设备（如WATCH GT5）设置中没有USB/无线调试入口，无法执行hdc命令，是什么原因？**

**A**：Lite Wearable设备运行轻量系统，不支持独立Wi-Fi网络连接，手表本体不具备HDC调试能力，设置中没有USB/无线调试入口属于产品规格预期行为，并非入口被隐藏。只有运行标准HarmonyOS的智能穿戴（如WATCH 4/5系列）才支持"开发者选项>无线调试+hdc tconn"直连方案。Lite Wearable设备调试请参考【解决方案】中"Lite Wearable设备调试"章节，也可使用[仿真器](../harmonyos-guides/ide-run-simulator.md)完成功能开发与调试。
