---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/upgrade-adaptation
title: 应用升级适配指导——向26.0.0升级
breadcrumb: 版本说明 > 应用升级适配与兼容性 > 应用升级适配指导——向26.0.0升级
category: harmonyos-releases
scraped_at: 2026-09-02T14:59:07+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:ab459fb38e1f0cb51a8f71ccc98b77ef0ca0bda74642b5463be01bafac60fe08
---

## 应用升级适配简介

HarmonyOS 7.0将陆续面向全网HarmonyOS NEXT设备发布，其配套的API版本为26.0.0，推荐开发者将所使用的开发套件升级至26.0.0配套版本，并将应用在此版本上完成升级适配，保证终端用户在HarmonyOS 7.0版本上获得良好的应用使用体验。

HarmonyOS版本在快速迭代更新的过程中，新增了大量的API，少量API会被废弃或者发生行为变更。为确保兼容性，在应用升级前需要参考API变更文档评估废弃API以及API行为变更对应用的影响。此外，我们提供了API隔离机制（通过targetSdkVersion进行隔离）以及API变更工具来帮助开发者升级应用。完成应用在开发套件的升级适配后，需要在新老设备上进行兼容性测试，以确保应用的正确运行，验证完成后，将最新应用发布到应用市场。

迁移阶段包含以下几个阶段：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4c/v3/5mjdp3y1TCKnka6OK2Losg/zh-cn_image_0000002699792890.png "点击放大")

**说明** 

本升级指导适用于目标API版本为26.0.0的升级。如需升级至其他版本，也可以参考此流程。

如在升级过程中遇到问题，请参考[获取支持与帮助](support.md)章节反馈您的问题。

## 开发工具链升级

### 升级DevEco Studio

1. 获取并安装HarmonyOS最新开发套件版本配套的DevEco Studio。

   已安装历史版本DevEco Studio的开发者可从软件界面检查升级，或者在[官网下载中心](https://developer.huawei.com/consumer/cn/download/)重新下载最新版本DevEco Studio并重新安装。
2. 安装后请阅读DevEco Studio的[变更说明](ide-changelogs-2600.md)，查看软件变更是否涉及适配操作。

   如果涉及跨越多个版本，应依次阅读各版本DevEco Studio的变更说明。
3. 从6.0.0(20)起，HarmonyOS开发套件配套的DevEco Studio已预置对应版本的HarmonyOS SDK，再次编译应用时将会使用该SDK进行编译。

### 升级命令行工具

命令行工具中同样预置了配套版本的HarmonyOS SDK，DevEco Studio升级后，请同步升级相同版本的命令行工具，确保使用命令行工具在流水线编译出的应用包与DevEco Studio编译的应用包使用了相同的SDK工具链。

可在[官网下载中心](https://developer.huawei.com/consumer/cn/download/)的Command Line Tools部分获取与DevEco Studio同版本的命令行工具。

## 评估API版本变化的影响并适配

DevEco Studio升级版本后，如果应用工程中未显式配置[targetSdkVersion](../harmonyos-guides/ide-hvigor-build-profile-app.md#section45865492619)，则该字段会同步升级为DevEco Studio配套的SDK版本。同时，编译应用默认使用的[compileSdkVersion](../harmonyos-guides/ide-hvigor-build-profile-app.md#section45865492619)也将会同步升级为相同版本，如果希望应用兼容更低版本的SDK，可通过compatibleSdkVersion配置兼容的最低SDK版本。此时需要注意针对以下两种API使用情况进行评估和适配：

* 应用升级时使用了新版本的API，在部分尚未升级的设备上并不支持，需进行兼容性判断，以便应用能够在满足SDK兼容性条件的设备上均可正常运行。详情请阅读[应用开发中的兼容性场景开发指导](app-compatibility-scenarios.md)。除了HarmonyOS的API外，也需要关注应用集成的三方库（har包）和“集成态hsp”的兼容性影响。
* 应用所使用的API发生了行为变更，在升级后需要对变更进行评估，确认是否对应用的兼容性产生了影响。部分API的行为变更可能会通过targetSdkVersion字段进行API版本隔离，以便提供前向兼容手段，详情请阅读[应用兼容性说明](app-compatibility.md)。

  对于具体的API行为变更对应用带来的影响，开发者可通过以下两种手段来识别，并参考变更说明文档进行适配。

### 通过DevEco Studio的API变更助手检测

开发者可以通过DevEco Studio的API变更助手查看当前工程中使用到的ArkTS API/C API是否存在行为变更，并根据工具提供的适配指导链接完成工程代码适配修改。步骤如下：

1. 在DevEco Studio菜单栏点击“**Tools > API Change Assistant**”打开API变更助手，此时编辑区下方的API Change Assistant页签中，支持按模块查看API变更情况。选择需要对比的SDK版本号范围，点击**Start Scan**开始扫描。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/db/v3/B6512WfXRXKdo-SuaV7S-Q/zh-cn_image_0000002732068043.png)
2. 扫描完成将展示当前工程中使用的API是否在选择比较的SDK版本之间发生行为变更。点击Code Location中的代码地址，跳转到相应的代码编写位置；如需更多指导，可点击Guidance link中的链接，跳转至版本说明文档中查看详情。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f3/v3/ZXtEHNxUSNeEMniPpnvfWg/zh-cn_image_0000002733344967.png "点击放大")
3. 点击**Export**，选择API变更的存放位置后导出变更数据；点击**Scan Again**可重新进行扫描。通过右侧Setting按钮，可以设置在扫描API时，可使用的最大堆内存的大小，默认值为3072MB，当工程代码量较大导致扫描缓慢时，可以适当调大该参数。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/11/v3/5V-MsAQTQ6mbuzGFWRDW4g/zh-cn_image_0000002729392225.png "点击放大")

### 查看官网发布的全量变更

如果需要了解HarmonyOS在历次版本迭代中产生的所有变更清单，可参见[HarmonyOS行为变更汇总](../harmonyos-roadmap/changelogs-overview-pre.md)。

## 在新老版本设备上进行应用的兼容性验证

应用基于新的SDK进行编译后，需要将应用安装到新老版本的设备上进行全量测试验证，覆盖所有的功能点来发现可能存在的不兼容问题。

目前[AppGallery Connect提供的云调试](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html#/redirectToService?menuId=9249519184596051206&type=project)功能支持多种设备和多个API版本，如果缺少足够的真机设备进行多API版本的兼容性验证，可通过云调试功能进行测试。

## 发布最新编译的应用到应用市场

完成编译和兼容性验证后，将应用发布到应用市场。

详情参见[发布应用](../harmonyos-guides/ide-publish-app.md)。
