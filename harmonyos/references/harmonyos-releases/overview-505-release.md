---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/overview-505-release
title: 版本概览
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.0.5(17) > 版本概览
category: harmonyos-releases
scraped_at: 2026-04-28T07:35:17+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:ee6f1930168d4ff3b7d3a8219e8f0d32f90f38ac7012717f38f2551663874ef0
---

HarmonyOS 5.0.5(17)在此前发布的HarmonyOS 5.0.4(16)的基础上，进一步丰富了ArkUI的组件能力，完善了应用在窗口化场景下的管理能力。

更多详细信息请参见[OS平台新增和增强特性](os-new-feature-505.md)和[DevEco Studio新增和增强特性](deveco-studio-new-features.md)。

## 版本信息

使用正确的配套关系进行应用开发可以获得更流畅的开发体验。

请在阅读版本更新和变更内容前，务必确认版本的配套关系是否与当前您所使用的开发套件是一致的。

### 5.0.5(17) Release开发者套件配套信息

| **软件包** | **发布类型** | **版本号** | Build Version | **发布时间** |
| --- | --- | --- | --- | --- |
| API版本 | Release | HarmonyOS 5.0.5 Release | 5.0.5(17)  *\***注意**：设备系统支持的API能力范围请以**API版本****为准。* | 2025/05/14 |
| DevEco Studio | Release | DevEco Studio 5.0.5 Release | 5.0.13.240（patch版本） | 2025/09/20 |
| 5.0.13.230（patch版本） | 2025/08/19 |
| 5.0.13.220（patch版本） | 2025/07/28 |
| 5.0.13.210（patch版本） | 2025/06/20 |
| 5.0.13.200 | 2025/05/14 |
| SDK | Release | HarmonyOS 5.0.5 Release SDK | 基于OpenHarmony SDK Ohos\_sdk\_public 5.0.5.165(API 17 Release) | 2025/05/14 |

说明

* **API版本**请在设备的“设置”中点击设备名称，进入“**关于本机**”进行查询。

  当前系统版本配套的设备包括：Mate 60、Mate 60 Pro、Mate X5、MatePad Pro 13.2英寸、MatePad Pro 11英寸 2024款等。请升级至配套的版本进行应用开发。

  不排除其他型号的设备通过其他途径升级至上述系统软件（ROM）版本，但设备所支持的开放能力请以“**关于本机**”页面显示的“**API版本**”为准。

* DevEco Studio版本请从DevEco Studio界面菜单选择“Help > About DevEco Studio”进行查询。请[点击此处](https://developer.huawei.com/consumer/cn/deveco-studio/)获取最新的DevEco Studio软件版本。
* SDK内置在DevEco Studio，安装DevEco Studio时自动安装配套版本SDK。具体版本请从DevEco Studio界面菜单选择“Help > About HarmonyOS SDK”进行查询。

## 历史Beta版本

### 5.0.5(17) Beta1

| **软件包** | **发布类型** | **版本号** | Build Version | **发布时间** |
| --- | --- | --- | --- | --- |
| API版本 | Beta | HarmonyOS 5.0.5 Beta1 | 5.0.5(17) Beta1  *\***注意**：设备系统支持的API能力范围请以**API版本****为准。* | 2025/04/24 |
| DevEco Studio | Beta | DevEco Studio 5.0.5 Beta1 | 5.0.13.100 | 2025/04/24 |
| SDK | Beta | HarmonyOS 5.0.5 Beta1 SDK | 基于OpenHarmony SDK Ohos\_sdk\_public 5.0.5.160(API 17 Beta1) | 2025/04/24 |

## 应用工程版本信息配置建议

应用工程中应当正确配置应用运行所依赖的SDK版本信息，以确保[应用在不同系统版本的设备上运行时的兼容性](app-compatibility.md)。

使用该版本开发的应用，其build-profile.json5配置项中关于版本的配置项建议如下：

| **build-profile.json5配置项** | **已开发应用** | | **新启动开发应用** | |
| --- | --- | --- | --- | --- |
| **配置建议** | **配置示例** | **配置建议** | **配置示例** |
| compileSdkVersion | 无需显性配置，编译时默认使用配套的SDK版本，即默认为：  “compileSdkVersion”: “5.0.5(17)” | NA | 无需显性配置，编译时默认使用配套的SDK版本，即默认为：  “compileSdkVersion”: “5.0.5(17)” | NA |
| compatibleSdkVersion | 建议与工程升级前的compatibleSdkVersion保持一致 | 和升级前保持一致，如：  “compatibleSdkVersion”: “5.0.0(12)” | 默认和compileSdkVersion的值保持一致，开发者在创建工程时可根据实际情况选择 | “compatibleSdkVersion”: “5.0.5(17)” |
| targetSdkVersion | 推荐您适配新版本的最新变更，然后配置为：“targetSdkVersion”: “5.0.5(17)”。  如果您期望延迟适配变更，可配置targetSdkVersion与工程升级前的targetSdkVersion一致。 | 1、应用适配变更，变更适配完成后配置为：  “targetSdkVersion”: “5.0.5(17)”    2、应用暂不适配变更，需配置为工程升级前的值，如：  “targetSdkVersion”: “5.0.0(12)” | 默认值和compileSdkVersion保持一致，开发者可根据实际情况进行配置 | “targetSdkVersion”: “5.0.5(17)” |
