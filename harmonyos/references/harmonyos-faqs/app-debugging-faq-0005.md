---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/app-debugging-faq-0005
title: 真机调试与测试包安装方法常见问题
breadcrumb: FAQ > DevEco Studio > 应用调试 > 常见问题 > 真机调试与测试包安装方法常见问题
category: harmonyos-faqs
scraped_at: 2026-10-23T07:14:49+08:00
doc_updated_at: 2026-10-22
content_hash: sha256:c4cdc6c5769feaaeef5e9cde0a72cedd731ff6c41f81ce84143c876fcc1b94e6
---

**Q：应用开发过程中，有哪几种方式可以将测试包安装到测试机？**

**A**：可以通过以下四种方式将测试包安装到测试机：

* 方式一：通过hdc命令安装到测试机。
  1. 下载[Command Line Tools](https://developer.huawei.com/consumer/cn/download/command-line-tools-for-hmos)。该命令行工具集合了HarmonyOS应用开发所用到的系列工具，包括代码检查codelinter、三方库的包管理Ohpm、命令行解析hstack、编译构建hvigorw。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/85/v3/qFYErO8tQKCb7AewaAojLg/zh-cn_image_0000002765752034.png "点击放大")
  2. 配置环境变量：下载后的压缩包放到D盘，解压后获得文件夹D:\CommandLine-Tools-windows-x64-5.1.0.828SP1\Command-Line-Tools\SDK\default\OpenHarmony\toolchains，右击此电脑-属性-高级系统设置，把该路径添加到环境变量里，cmd窗口输入where hdc检查是否配置成功。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/be/v3/W1LWVtbOT9S7mbRhn3sUTg/zh-cn_image_0000002765592114.png "点击放大")![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ca/v3/SAQQGRuaRhS5kSykN9gxjA/zh-cn_image_0000002765592116.png "点击放大")
  3. 使用hdc命令安装测试包：测试机进入手机系统设置菜单-关于手机，多次点击版本号启用开发者模式，然后进入系统设置菜单-系统-开发者选项，打开USB调试模式，并通过USB将手机连接到电脑，通过cmd使用命令hdc install <测试包路径>来安装hap包。![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ed/v3/_Jxit5ZKQfSrGsCwp4r8pQ/zh-cn_image_0000002795030821.png "点击放大")

* 方式二：通过IDE安装到测试机。
  1. 下载新版[DevEco Studio](https://developer.huawei.com/consumer/cn/download/deveco-studio)，并完成安装。安装过程中，新版本已经集成了Node.js、Ohpm和HarmonyOS SDK，因此不需要单独配置这些组件。
  2. 测试机开启开发者模式，采用[USB连接方式](../harmonyos-guides/ide-run-device.md#section171436512424)或者[使用无线调试连接方式](../harmonyos-guides/ide-run-device.md#section9315596477)。
  3. 在DevEco Studio中选择真机，Project Structure（项目结构）-Signing Configs（签名配置）-勾选Automatically generate signature(自动签名)-点击OK完成自动签名，点击“Run”或“Debug”按钮，DevEco Studio自动将hap文件安装到测试机上。具体请参考[使用本地真机运行应用](../harmonyos-guides/ide-run-device.md)。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5f/v3/lTHaXgzSSdWWoj7GO04BFQ/zh-cn_image_0000002765752352.png "点击放大")

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/35/v3/vhqDWJAVRQq62zyBIA45mg/zh-cn_image_0000002795150911.png "点击放大")![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/2B9lz-wRSXiggUOTYCajEw/zh-cn_image_0000002795150915.png "点击放大")

* 方式三：通过[DevEco Testing](https://developer.huawei.com/consumer/cn/download/deveco-testing)工具安装到测试机。

  测试机开启开发者模式，打开USB调试模式，并通过USB将手机连接到电脑，点击DevEco Testing工具左侧实用工具-设备投屏-开始投屏，点击安装应用，选择安装包路径，点击确定按钮进行安装，安装后可通过执行日志查看安装信息。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/38/v3/2EjhEPtBQJKyl7VNwUAwqA/zh-cn_image_0000002765753226.png "点击放大")

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/etiotd6LScqH0zdhT83uUw/zh-cn_image_0000002765753228.png "点击放大")

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a0/v3/4kN4H_H5QQeC_tQiJjtyrA/zh-cn_image_0000002795151789.png "点击放大")
* 方式四：通过[邀请测试和公开测试](../app/agc-help-harmonyos-testapp-0000001873653977.md)安装到测试机。

  通过HarmonyOS 开发者中心，在应用正式版本发布之前，可以挑选特定的用户群组来测试HarmonyOS应用/元服务，或向AppGallery用户公开发布测试版本。

**Q：开发者在开发Wearable和Lite Wearable设备应用时需要进行调试和调测，具体怎么做？**

**A**：Wearable和Lite Wearable设备调试方法如下：

Wearable设备调试：

前提条件：需要登录华为开发者账号才有无线调试选项。

1. 将Wearable设备和PC连接到同一WLAN网络。

   在设置>系统>开发者选项中，打开"无线调试"或"通过WLAN调试"（Wearable设备）开关，并获取设备端的IP地址和端口号。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d4/v3/D8Yzc2cXS0SiNrn3G0wNhg/zh-cn_image_0000002795155791.png "点击放大")
2. 连接设备，有两种方式。

   2.1 在DevEco Studio菜单栏中，单击Tools > IP Connection，输入连接设备的IP地址和端口号，单击，连接正常后，设备状态为online。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ea/v3/ukAPMX71SiW8G7uLbxbTWQ/zh-cn_image_0000002765597306.png "点击放大")

   2.2 执行hdc命令，关于hdc工具的使用指导请参考[hdc](../harmonyos-guides/hdc.md)。

   hdc tconn设备IP地址:端口号。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cb/v3/f0Xn-isaQGWyXy-I71qcAA/zh-cn_image_0000002795036011.png)

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

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f7/v3/ESZ3u0TzTauHhP20b1ksug/zh-cn_image_0000002765757618.png "点击放大")
3. 在工程目录中的Build > outputs >hap中选择生成的HAP，通过手工拷贝的方式将HAP拷贝至手机中的"/sdcard/haps/"目录。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3d/v3/rZnvpCClQluKY-dvRFrxWw/zh-cn_image_0000002765597716.png)
4. 将Lite Wearable通过蓝牙与华为手机进行连接。

   4.1 进入运动健康APP，在设备页签中，单击添加设备按钮。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fb/v3/fEOUFKW2Toa4pjOYKZkLMA/zh-cn_image_0000002795036407.png "点击放大")

   4.2 进入手表列表中，选择对应的Lite Wearable型号。

   4.3 单击开始配对，按照界面指引完成Lite Wearable与华为手机之间的连接。
5. 打开应用调测助手APP，界面会显示已经与华为手机连接的Lite Wearable。
6. 单击应用调测助手APP界面中的应用管理按钮，选择需要安装的HarmonyOS安装包进行安装。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fb/v3/pQFATnNBQdeHOsBBRQAUMQ/zh-cn_image_0000002765757622.png "点击放大")
7. 安装完成后，单击Lite Wearable中的应用图标，运行HarmonyOS应用。

**Q：HarmonyOS NEXT系统上能否开发Lite Wearable类型的手表应用？**

**A**：Lite Wearable中运行应用/服务依赖HarmonyOS NEXT版本以前的手机上的运动健康和应用调测助手APP辅助进行，暂不支持在HarmonyOS NEXT系统上直接调试Lite Wearable设备。轻量级智能穿戴与智能穿戴在硬件能力和系统支持上不同，暂时无法仅开发一版实现通用。Wearable是当前更主流的方向，是HarmonyOS NEXT生态重点支持的穿戴设备类型。

**Q：通过应用调测助手向Lite Wearable设备安装HAP时提示"安装失败：40.配置文件格式错误"怎么办？**

**A**：该问题通常是由于工程级[build-profile.json5](../harmonyos-guides/ide-hvigor-build-profile-app.md)中[compatibleSdkVersion](../harmonyos-guides/ide-hvigor-build-profile-app.md#section45865492619)配置格式不正确导致。compatibleSdkVersion必须写成5.0.0(12)格式，不能写成其他字符串格式。若配置格式正确但仍报此错误，需检查工程的API版本是否超出目标设备实际支持的SDK版本范围，例如WATCH GT 3对应API 6，使用API 10创建工程会因版本不匹配导致安装失败，需将compatibleSdkVersion和targetSdkVersion调整为设备支持的API版本。

**Q：GT系列手表能否用于穿戴应用测试？**

**A**：可以。GT系列手表属于Lite Wearable（轻量级智能穿戴）设备，应按Lite Wearable方式进行测试，不支持Wearable（智能穿戴）直连方式。当前支持的GT系列手表型号及对应API版本如下：WATCH GT 2（API 5）、WATCH GT 2 Pro（API 6）、WATCH GT 3（API 6）、WATCH GT 4（API 10）、WATCH GT 5（API 12），开发时需按具体型号的API能力做兼容。创建工程时选择"[Lite] Empty Ability"模板，设备类型设为"Lite Wearable"。Lite Wearable设备仅支持JS开发，不支持ArkTS，应使用JS+CSS+HTML的类Web开发范式。GT真机不能直接连接DevEco Studio，需手动签名并在调试Profile中注册设备，将HAP拷贝至华为手机，通过运动健康完成配对，再用应用调测助手安装到手表。基础功能也可先用Lite Wearable预览器或仿真器验证。

**Q：Lite Wearable设备（如WATCH GT5）设置中没有USB/无线调试入口，无法执行hdc命令，是什么原因？**

**A**：Lite Wearable设备运行轻量系统，不支持独立Wi-Fi网络连接，手表本体不具备HDC调试能力，设置中没有USB/无线调试入口属于产品规格预期行为，并非入口被隐藏。只有运行标准HarmonyOS的智能穿戴（如WATCH 4/5系列）才支持"开发者选项>无线调试+hdc tconn"直连方案。Lite Wearable设备调试请参考【解决方案】中"Lite Wearable设备调试"章节，也可使用[仿真器](../harmonyos-guides/ide-run-simulator.md)完成功能开发与调试。
