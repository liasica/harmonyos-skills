---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-software-install
title: 下载与安装DevEco Studio
breadcrumb: 指南 > 开发环境搭建 > 下载与安装DevEco Studio
category: harmonyos-guides
scraped_at: 2026-09-04T06:27:04+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:0ba66e4da06041c563f35af366a5666a6896e4bf666b1fc346f6713bde58b471
---

## 下载软件

请前往[下载中心](https://developer.huawei.com/consumer/cn/download/deveco-studio)，登录华为账号后下载DevEco Studio，并根据下载中心页面**工具完整性**指导进行完整性校验。

DevEco Studio支持Windows和macOS系统，下面将针对两种操作系统的软件安装方式分别进行介绍。

## Windows环境

### 运行环境要求

为保证DevEco Studio正常运行，建议电脑配置满足如下要求：

* 操作系统：Windows10 64位、Windows11 64位
* 内存：16GB及以上
* 硬盘：100GB及以上
* 分辨率：1280\*800像素及以上

### 安装DevEco Studio

1. 下载完成后，双击下载的“deveco-studio-xxxx.exe”，进入DevEco Studio安装向导。在如下界面选择安装路径，默认安装于C:\Program Files路径下，也可以单击**浏览（B）...**指定其他安装路径，然后单击**下一步**。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/61/v3/9q_ybDxNSjmtAR9i0UFZRQ/zh-cn_image_0000002731382039.png)
2. 在如下安装选项界面勾选**DevEco Studio**后，单击**下一步**，直至安装完成。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/98/v3/syP_o0Y8Qb-OYk4YHGI0NA/zh-cn_image_0000002701662816.png)
3. 单击**Finish**完成安装。安装完成后，如有需要请根据[配置代理](ide-environment-config.md)，检查和配置开发环境。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/14/v3/on9c5ylQRnSlbOcfQDtoHw/zh-cn_image_0000002701822736.png)

   **说明** 

   * DevEco Studio提供开箱即用的开发体验，将HarmonyOS SDK、Node.js、Hvigor、OHPM、模拟器平台等进行合一打包，简化DevEco Studio安装配置流程。
   * HarmonyOS SDK已嵌入DevEco Studio中，无需额外下载配置。HarmonyOS SDK可以在DevEco Studio安装位置下DevEco Studio\sdk目录中查看。如需进行OpenHarmony应用开发，可通过File > Settings > OpenHarmony SDK页签下载OpenHarmony SDK。
   * 首次运行DevEco Studio时，若出现**Import DevEco Studio Settings**弹窗，请选择**Do not import settings**后单击**OK**。

## macOS环境

### 运行环境要求

为保证DevEco Studio正常运行，建议电脑配置满足如下要求：

* 操作系统：macOS(X86) 11/12/13/14/15、 macOS(ARM) 12/13/14/15
* 内存：8GB及以上
* 硬盘：100GB及以上
* 分辨率：1280\*800像素及以上

### 安装DevEco Studio

1. 在安装界面中，将“**DevEco-Studio.app**”拖拽到“**Applications**”中，等待安装完成。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f4/v3/imHUCtcmQaaSjbURj_dU6A/zh-cn_image_0000002731542011.png "点击放大")
2. 安装完成后，如有需要请根据[配置代理](ide-environment-config.md)，检查和配置开发环境。

   **说明** 

   * DevEco Studio提供开箱即用的开发体验，将HarmonyOS SDK、Node.js、Hvigor、OHPM、模拟器平台等进行合一打包，简化DevEco Studio安装配置流程。
   * HarmonyOS SDK已嵌入DevEco Studio中，无需额外下载配置。HarmonyOS SDK可以在DevEco Studio安装位置下DevEco Studio\sdk目录中查看。如需进行OpenHarmony应用开发，可通过DevEco Studio > Preferences/Settings **>** OpenHarmony SDK页签下载OpenHarmony SDK。

## 诊断开发环境

DevEco Studio提供开发环境诊断功能，帮助您检查开发环境是否完备。您可以在欢迎页面单击**Diagnose**进行诊断。如果您已经打开了工程开发界面，也可以在菜单栏单击**Help > Diagnostic Tools > Diagnose Development Environment**进行诊断。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c3/v3/s0P4BjeAT5yyAbd-sCtJDQ/zh-cn_image_0000002731542013.png)

DevEco Studio开发环境诊断项包括电脑的配置、网络的连通情况、依赖的工具是否安装等。如果检测结果为未通过，请根据检查项的描述和修复建议进行处理。

## 启用中文化插件

该功能仅支持中国境内（香港特别行政区、澳门特别行政区、中国台湾除外）。

* 从DevEco Studio 6.0.0 Beta1版本开始，中文化插件默认启用。如需切换为中文显示效果，在菜单栏进入**File > Settings...**（macOS为**DevEco Studio > Preferences/Settings** ） **> Appearance & Behavior > System Settings** > **Language**，语言选择**Chinese**并点击**Apply**，在弹窗中点击**Restart**重启即可完成语言切换。若语言选择时未找到Chinese，请按照[之前版本操作](ide-software-install.md#li1956431816322)启用插件后，再选择。

  **说明** 

  从DevEco Studio 6.1.0 Beta1版本开始，语言选择时**Chinese**变更为**Chinese(Simplified)**简体中文。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c4/v3/tQshHjDvRMa870s3GwHQMg/zh-cn_image_0000002701822734.png)

* 若使用DevEco Studio 6.0.0 Beta1以下版本，请在菜单栏进入**File > Settings** （macOS为**DevEco Studio > Preferences****/Settings** ）**> Plugins**，选择**Installed**页签，在搜索框输入“Chinese”，搜索结果里将出现**Chinese(Simplified)**，在右侧单击**Enable**，点击**OK**，在弹窗中单击**Restart**，重启DevEco Studio后即可生效。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/BekHEIyXTl6nloWfg9wQ2w/zh-cn_image_0000002701662812.png)
