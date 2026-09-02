---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-debugging-70
title: 应用开发过程中如何将测试包安装到测试机
breadcrumb: FAQ > DevEco Studio > 应用调试 > 应用开发过程中如何将测试包安装到测试机
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:57+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:cec6b620a05e911509707101a4f13cf3faae506fa57baa638c6c64c32433e830
---

## 问题现象

应用开发过程中，有哪几种方式可以将测试包安装到测试机？

## 解决方案

可以通过以下四种方式将测试包安装到测试机：

* 方式一：通过hdc命令安装到测试机。
  1. 下载[Command Line Tools](https://developer.huawei.com/consumer/cn/download/command-line-tools-for-hmos)。该命令行工具集合了HarmonyOS应用开发所用到的系列工具，包括代码检查codelinter、三方库的包管理Ohpm、命令行解析hstack、编译构建hvigorw。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9b/v3/gobg7eogQuiEoGFG-p1Kew/zh-cn_image_0000002628569322.png "点击放大")
  2. 配置环境变量：下载后的压缩包放到D盘，解压后获得文件夹D:\CommandLine-Tools-windows-x64-5.1.0.828SP1\Command-Line-Tools\SDK\default\OpenHarmony\toolchains，右击此电脑-属性-高级系统设置，把该路径添加到环境变量里，cmd窗口输入where hdc检查是否配置成功。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/88/v3/eTwr29x2Q--8BLu3n_tVVQ/zh-cn_image_0000002658928641.png "点击放大")

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/57/v3/wr0f89ViS7egxt-WulLamg/zh-cn_image_0000002628409416.png "点击放大")
  3. 使用hdc命令安装测试包：测试机进入手机系统设置菜单-关于手机，多次点击版本号启用开发者模式，然后进入系统设置菜单-系统-开发者选项，打开USB调试模式，并通过USB将手机连接到电脑，通过cmd使用命令hdc install <测试包路径>来安装hap包。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fc/v3/P0s-frtmQL2h8RRTLi6x6g/zh-cn_image_0000002658808685.png "点击放大")
* 方式二：通过IDE安装到测试机。
  1. 下载新版[DevEco Studio](https://developer.huawei.com/consumer/cn/download/deveco-studio)，并完成安装。安装过程中，新版本已经集成了Node.js、Ohpm和HarmonyOS SDK，因此不需要单独配置这些组件。
  2. 测试机开启开发者模式，采用[USB连接方式](../harmonyos-guides/ide-run-device.md#section171436512424)或者[使用无线调试连接方式](../harmonyos-guides/ide-run-device.md#section9315596477)。
  3. 在DevEco Studio中选择真机，Project Structure（项目结构）-Signing Configs（签名配置）-勾选Automatically generate signature(自动签名)-点击OK完成自动签名，点击“Run”或“Debug”按钮，DevEco Studio自动将hap文件安装到测试机上。具体请参考[使用本地真机运行应用](../harmonyos-guides/ide-run-device.md)。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6d/v3/stm9dREtSA-DREh2_lDvEg/zh-cn_image_0000002628569324.png "点击放大")

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d7/v3/wfgXy5lUSfewB7lkr3G46A/zh-cn_image_0000002658928647.png "点击放大") ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2c/v3/CXaI5cTLRRuK4ovKCfcmQg/zh-cn_image_0000002628409424.png "点击放大")
* 方式三：通过[DevEco Testing](https://developer.huawei.com/consumer/cn/download/deveco-testing)工具安装到测试机。

  测试机开启开发者模式，打开USB调试模式，并通过USB将手机连接到电脑，点击DevEco Testing工具左侧实用工具-设备投屏-开始投屏，点击安装应用，选择安装包路径，点击确定按钮进行安装，安装后可通过执行日志查看安装信息。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/33/v3/rudptH3USh2oHAAv-Uf-8w/zh-cn_image_0000002658808695.png "点击放大")

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ab/v3/W1LOraDQTvmZAT6GeTTjGA/zh-cn_image_0000002628569334.png "点击放大")

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a2/v3/e9aY9O9YQzeA7_SU1HY9Mg/zh-cn_image_0000002658928653.png "点击放大")
* **方式四**：通过[邀请测试和公开测试](../app/agc-help-harmonyos-testapp-0000001873653977.md)安装到测试机。

  通过AppGallery Connect，在应用正式版本发布之前，可以挑选特定的用户群组来测试HarmonyOS应用/元服务，或向AppGallery用户公开发布测试版本。
