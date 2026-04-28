---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/overview-510
title: 版本概览
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.1.0(18) > 版本概览
category: harmonyos-releases
scraped_at: 2026-04-28T07:35:00+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:5d86f7f8f8dd94362e71a329e82b2b1e46b439f86e545951468106e0bd82bfdd
---

HarmonyOS 5.1.0(18)在HarmonyOS 5.0.5(17)的基础上，进一步增强ArkUI组件能力，提供更多组件调用细节；应用进程、数据等关键信息在保证安全的前提下，进一步提升获取和使用的灵活性。

同时，HarmonyOS 5.1.0(18)首次支持智能穿戴设备的开发，ArkUI针对穿戴设备的圆形表盘同步新增一系列组件能力。

更多详情可参见[OS平台新增和增强特性](os-new-feature-510.md)和[DevEco Studio新增和增强特性](deveco-studio-new-features-510-release.md)。

## 版本信息

说明

使用正确的配套关系进行应用开发可以获得更流畅的开发体验。

请在阅读版本更新和变更内容前，务必确认版本的配套关系是否与当前您所使用的开发套件是一致的。

### 5.1.0(18) Release开发者套件配套信息

| **软件包** | **发布类型** | **版本号** | **发布时间** |
| --- | --- | --- | --- |
| API版本 | Release | 5.1.0(18)  *\***注意**：设备系统支持的API能力范围请以**API版本****为准。* | 2025/06/11 |
| DevEco Studio | Release | DevEco Studio 5.1.0 Release (5.1.0.849)  （Patch版本） | 2025/08/14 |
| DevEco Studio 5.1.0 Release (5.1.0.840)  （Patch版本） | 2025/07/04 |
| DevEco Studio 5.1.0 Release (5.1.0.828SP1)  （Patch版本） | 2025/06/23 |
| DevEco Studio 5.1.0 Release (5.1.0.828) | 2025/06/11 |
| SDK | Release | HarmonyOS 5.1.0 Release SDK  基于OpenHarmony SDK Ohos\_sdk\_public 5.1.0.110(API 18 Release) | 2025/06/11 |

说明

* 该版本仅面向HUAWEI Watch 5系列智能穿戴设备和HUAWEI Pura 80系列手机、以及部分通过开发者渠道定向获得推送的Mate 60系列手机提供，因此使用其他设备的开发者可能暂时无法体验5.1.0(18)的新增能力。
* **API版本**请在设备的“设置”中点击设备名称，进入“**关于本机**”进行查询。

* DevEco Studio版本请从DevEco Studio界面菜单选择“Help > About DevEco Studio”进行查询。请[点击此处](https://developer.huawei.com/consumer/cn/deveco-studio/)获取最新的DevEco Studio软件版本。
* SDK内置在DevEco Studio，安装DevEco Studio时自动安装配套版本SDK。具体版本请从DevEco Studio界面菜单选择“Help > About HarmonyOS SDK”进行查询。

## 应用工程版本信息配置建议

应用工程中应当正确配置应用运行所依赖的SDK版本信息，以确保[应用在不同系统版本的设备上运行时的兼容性](app-compatibility.md)。

使用该版本开发的应用，其build-profile.json5配置项中关于版本的配置项建议如下：

| **build-profile.json5配置项** | **已开发应用** | | **新启动开发应用** |
| --- | --- | --- | --- |
| **配置建议** | **配置示例** |
| compileSdkVersion | 无需显性配置，编译时默认使用配套的SDK版本，即默认为：  “compileSdkVersion”: “5.1.0(18)” | NA | 推荐使用[5.0.5(17) Release](overview-505-release.md)进行新应用的开发。 |
| compatibleSdkVersion | 建议与工程升级前的compatibleSdkVersion保持一致 | 和升级前保持一致，如：  “compatibleSdkVersion”: “5.0.0(12)” |
| targetSdkVersion | 推荐您适配新版本的最新变更，然后配置为：“targetSdkVersion”: “5.1.0(18)”。  如果您期望延迟适配变更，可配置targetSdkVersion与工程升级前的targetSdkVersion一致。 | 1、应用适配变更，变更适配完成后配置为：  “targetSdkVersion”: “5.1.0(18)”    2、应用暂不适配变更，需配置为工程升级前的值，如：  “targetSdkVersion”: “5.0.0(12)” |
