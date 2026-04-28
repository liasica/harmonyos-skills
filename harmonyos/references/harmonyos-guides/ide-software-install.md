---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-software-install
title: 下载与安装DevEco Studio
breadcrumb: 指南 > 开发环境搭建 > 下载与安装DevEco Studio
category: harmonyos-guides
scraped_at: 2026-04-28T07:54:36+08:00
doc_updated_at: 2026-04-22
content_hash: sha256:81f943199d48fbbef639839212d2afed6d40779599fa67e772df7417cc1b021f
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

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ff/v3/zu4ZCWVjRxKKT_RxlV2_Ow/zh-cn_image_0000002561832793.png?HW-CC-KV=V1&HW-CC-Date=20260427T235434Z&HW-CC-Expire=86400&HW-CC-Sign=FC87980D8CC2D15561DFC8995A43FD999284C272ACC26DB5D97DA9B5A81090C3)
2. 在如下安装选项界面勾选**DevEco Studio**后，单击**下一步**，直至安装完成。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ce/v3/1A3mYFT3RxObR-tY-nH_JQ/zh-cn_image_0000002561752819.png?HW-CC-KV=V1&HW-CC-Date=20260427T235434Z&HW-CC-Expire=86400&HW-CC-Sign=14F7EAEC2A4CD363A876B1E7DC5D07FFC2DAA1C4759C7FF50AD5AF54385C7A9B)
3. 安装完成后，单击**Finish**完成安装。安装完成后，如有需要请根据[配置代理](ide-environment-config.md)，检查和配置开发环境。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e7/v3/QWAw0MF-RpStHanyO5mqMg/zh-cn_image_0000002561752813.png?HW-CC-KV=V1&HW-CC-Date=20260427T235434Z&HW-CC-Expire=86400&HW-CC-Sign=47534F5C0F012673F110119326FC64BF158C6C6B36FA23312773B91A588BC417)

   说明

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

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1f/v3/D-mmmKBaTFq9XALH2SZigQ/zh-cn_image_0000002530752870.png?HW-CC-KV=V1&HW-CC-Date=20260427T235434Z&HW-CC-Expire=86400&HW-CC-Sign=F5B2A447E7C65E938A3221885786B7339B745A34CC076BBB541D4E4899FB32CF "点击放大")
2. 安装完成后，如有需要请根据[配置代理](ide-environment-config.md)，检查和配置开发环境。

   说明

   * DevEco Studio提供开箱即用的开发体验，将HarmonyOS SDK、Node.js、Hvigor、OHPM、模拟器平台等进行合一打包，简化DevEco Studio安装配置流程。
   * HarmonyOS SDK已嵌入DevEco Studio中，无需额外下载配置。HarmonyOS SDK可以在DevEco Studio安装位置下DevEco Studio\sdk目录中查看。如需进行OpenHarmony应用开发，可通过DevEco Studio > Preferences/Settings **>** OpenHarmony SDK页签下载OpenHarmony SDK。

## 诊断开发环境

为了您开发应用/元服务的良好体验，DevEco Studio提供了开发环境诊断的功能，帮助您识别开发环境是否完备。您可以在欢迎页面单击**Diagnose**进行诊断。如果您已经打开了工程开发界面，也可以在菜单栏单击**Help > Diagnostic Tools > Diagnose Development Environment**进行诊断。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/17/v3/f2bp_JZSTNuuyQNKBCsOdQ/zh-cn_image_0000002561752817.png?HW-CC-KV=V1&HW-CC-Date=20260427T235434Z&HW-CC-Expire=86400&HW-CC-Sign=550FFE13ECC7FA00F749E20F387C248A2B3603537F322E074146786AEBE9348C)

DevEco Studio开发环境诊断项包括电脑的配置、网络的连通情况、依赖的工具是否安装等。如果检测结果为未通过，请根据检查项的描述和修复建议进行处理。

## 启用中文化插件

该功能仅支持中国境内（香港特别行政区、澳门特别行政区、中国台湾除外）。

* 从DevEco Studio 6.0.0 Beta1版本开始，中文化插件默认启用。如需切换为中文显示效果，在菜单栏进入**File > Settings...**（macOS为**DevEco Studio > Preferences/Settings** ） **> Appearance & Behavior > System Settings** > **Language**，语言选择**Chinese**并点击**Apply**，在弹窗中点击**Restart**重启即可完成语言切换。若语言选择时未找到Chinese，请按照[之前版本操作](ide-software-install.md#li1956431816322)启用插件后，再选择。

  说明

  从DevEco Studio 6.1.0 Beta1版本开始，语言选择时**Chinese**变更为**Chinese(Simplified)**简体中文。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/01/v3/PMpvWvHTTFS5c24MPBNaUg/zh-cn_image_0000002561832787.png?HW-CC-KV=V1&HW-CC-Date=20260427T235434Z&HW-CC-Expire=86400&HW-CC-Sign=2E30E12F84011A9DDF2C7B67E044CE3A5504C98F47151992A12B24FDA6316DF2)

* 若使用DevEco Studio 6.0.0 Beta1以下版本，请在菜单栏进入**File > Settings** （macOS为**DevEco Studio > Preferences** ）**> Plugins**，选择**Installed**页签，在搜索框输入“Chinese”，搜索结果里将出现**Chinese(Simplified)**，在右侧单击**Enable**，点击**OK**，在弹窗中单击**Restart**，重启DevEco Studio后即可生效。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3f/v3/Na-mJIZxTQuL_yY3b5FpMw/zh-cn_image_0000002530912864.png?HW-CC-KV=V1&HW-CC-Date=20260427T235434Z&HW-CC-Expire=86400&HW-CC-Sign=51CA765EBD5F810B84CFA2CF2FC2BE9237520DC44C16AC51F0D65C4B3382047C)
