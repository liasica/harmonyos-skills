---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-software-install
title: 下载与安装DevEco Studio
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 开发环境搭建 > 下载与安装DevEco Studio
category: harmonyos-guides
scraped_at: 2026-11-24T12:42:19+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:88d03f28b927fb116bba223c134ff29c01589656243e4e0d274c86d0a05046ed
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

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8b/v3/VA724_m0SMqdMGGbVhwfMA/zh-cn_image_0000002779406846.png?HW-CC-KV=V1&HW-CC-Date=20261124T044219Z&HW-CC-Expire=31536000000&HW-CC-Sign=5C410C4EDCAF4CF85FF527599BD9051A4F89987E5A9FCB2D0D5616B215B861B8)
2. 在如下安装选项界面勾选**DevEco Studio**后，单击**下一步**，直至安装完成。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a8/v3/NDLMFPvjQeWgMjAU6Q2w3Q/zh-cn_image_0000002779406844.png?HW-CC-KV=V1&HW-CC-Date=20261124T044219Z&HW-CC-Expire=31536000000&HW-CC-Sign=6736125F64AFE9A98B90BB594DC018AE175A0964A0EE3262187591E13B14AF75)
3. 单击**Finish**完成安装。安装完成后，如有需要请根据[配置代理](ide-environment-config.md)，检查和配置开发环境。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/chX8hqCUStyDDVvHpFAbhw/zh-cn_image_0000002808766407.png?HW-CC-KV=V1&HW-CC-Date=20261124T044219Z&HW-CC-Expire=31536000000&HW-CC-Sign=82A1188C2D6D7C80865FDD3CDA6DCA7EC92027E0914AE37FC00AAD9BBEE90B4E)

   **说明** 

   * DevEco Studio提供开箱即用的开发体验，将HarmonyOS SDK、Node.js、Hvigor、OHPM、模拟器平台等进行合一打包，简化DevEco Studio安装配置流程。
   * HarmonyOS SDK已嵌入DevEco Studio中，无需额外下载配置。HarmonyOS SDK可以在DevEco Studio安装位置下DevEco Studio\sdk目录中查看。如需进行OpenHarmony应用开发，可通过File > Settings > OpenHarmony SDK页签下载OpenHarmony SDK。
   * 首次运行DevEco Studio时，若出现**Import DevEco Studio Settings**弹窗，请选择**Do not import settings**后单击**OK**。

## macOS环境

### 运行环境要求

为保证DevEco Studio正常运行，建议电脑配置满足如下要求：

* 操作系统：macOS(X86) 11/12/13/14/15/26、 macOS(ARM) 12/13/14/15/26
* 内存：8GB及以上
* 硬盘：100GB及以上
* 分辨率：1280\*800像素及以上

### 安装DevEco Studio

1. 在安装界面中，将“**DevEco-Studio.app**”拖拽到“**Applications**”中，等待安装完成。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e8/v3/Pmf2D5N3SqCbRg78_OSrPw/zh-cn_image_0000002779566822.png?HW-CC-KV=V1&HW-CC-Date=20261124T044219Z&HW-CC-Expire=31536000000&HW-CC-Sign=0EE027EFD00F86A734226C1FBCBDC162BBEFD99F245F55C32BF202982B03DCD2 "点击放大")
2. 安装完成后，如有需要请根据[配置代理](ide-environment-config.md)，检查和配置开发环境。

   **说明** 

   * DevEco Studio提供开箱即用的开发体验，将HarmonyOS SDK、Node.js、Hvigor、OHPM、模拟器平台等进行合一打包，简化DevEco Studio安装配置流程。
   * HarmonyOS SDK已嵌入DevEco Studio中，无需额外下载配置。HarmonyOS SDK可以在DevEco Studio安装位置下DevEco Studio\sdk目录中查看。如需进行OpenHarmony应用开发，可通过DevEco Studio > Preferences/Settings **>** OpenHarmony SDK页签下载OpenHarmony SDK。

## 诊断开发环境

DevEco Studio提供开发环境诊断功能，帮助您检查开发环境是否完备。您可以在欢迎页面单击**Diagnose**进行诊断。如果您已经打开了工程开发界面，也可以在菜单栏单击**Help > Diagnostic Tools > Diagnose Development Environment**进行诊断。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a3/v3/faCGmns-TQqagchEHqjWzg/zh-cn_image_0000002779566826.png?HW-CC-KV=V1&HW-CC-Date=20261124T044219Z&HW-CC-Expire=31536000000&HW-CC-Sign=DFBE28E5F9B5D15AD5087669FB273EBBC5984C94C1E90D9407ECAA60F98DFDCC)

DevEco Studio开发环境诊断项包括电脑的配置、网络的连通情况、依赖的工具是否安装等。如果检测结果为未通过，请根据检查项的描述和修复建议进行处理。

## 启用中文化插件

该功能仅支持中国境内（香港特别行政区、澳门特别行政区、中国台湾除外）。

* 从DevEco Studio 6.0.0 Beta1版本开始，中文化插件默认启用。如需切换为中文显示效果，在菜单栏进入**File > Settings...**（macOS为**DevEco Studio > Preferences/Settings** ） **> Appearance & Behavior > System Settings** > **Language**，语言选择**Chinese**并点击**Apply**，在弹窗中点击**Restart**重启即可完成语言切换。若语言选择时未找到Chinese，请按照[之前版本操作](ide-software-install.md#li1956431816322)启用插件后，再选择。

  **说明** 

  从DevEco Studio 6.1.0 Beta1版本开始，语言选择时**Chinese**变更为**Chinese(Simplified)**简体中文。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/ZN5eluc6QtaX56WRcTwYjg/zh-cn_image_0000002808886483.png?HW-CC-KV=V1&HW-CC-Date=20261124T044219Z&HW-CC-Expire=31536000000&HW-CC-Sign=7DD55A39786538B2E6834EF5E75CDFA7DC012C47069FE46C5F53E11F12D73673)

* 若使用DevEco Studio 6.0.0 Beta1以下版本，请在菜单栏进入**File > Settings** （macOS为**DevEco Studio > Preferences****/Settings** ）**> Plugins**，选择**Installed**页签，在搜索框输入“Chinese”，搜索结果里将出现**Chinese(Simplified)**，在右侧单击**Enable**，点击**OK**，在弹窗中单击**Restart**，重启DevEco Studio后即可生效。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/79/v3/OKNJSS7aRA-e3ufeNxZLDw/zh-cn_image_0000002779566820.png?HW-CC-KV=V1&HW-CC-Date=20261124T044219Z&HW-CC-Expire=31536000000&HW-CC-Sign=860D9662EEAF88983BBA5151658A92A98415611C5A94FE30FE154636F4E1D9A5)
