---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/overview-511-beta1
title: 版本概览
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.1.1(19) > 版本概览
category: harmonyos-releases
scraped_at: 2026-04-28T07:34:46+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:caef9fcd4352ed7a149bc71e433d7c80f9d154c65fbba48e6000421520acbc97
---

HarmonyOS 5.1.1(19)在HarmonyOS 5.1.0(18)的基础上，进一步增强ArkUI组件能力，提供更多组件调用细节，尤其是跟随手势相关的组件能力；进一步增强地图服务的能力，丰富开发者可使用的地图场景；进一步增强Hitrace的日志打点能力，等等。

更多详情可参见OS平台的[OS平台新增和增强特性](os-new-feature-511-beta1.md)和[DevEco Studio新增和增强特性](deveco-studio-new-features-511.md)。

## 版本信息

说明

使用正确的配套关系进行应用开发可以获得更流畅的开发体验。

请在阅读版本更新和变更内容前，务必确认版本的配套关系是否与当前您所使用的开发套件是一致的。

### 5.1.1(19) Release开发者套件配套信息

| **软件包** | **发布类型** | **版本号** | **发布时间** |
| --- | --- | --- | --- |
| API版本 | Release | 5.1.1(19)  *\***注意**：设备系统支持的API能力范围请以**API版本****为准。* | 2025/06/30 |
| DevEco Studio | Release | DevEco Studio 5.1.1 Release (5.1.1.850)  （Patch版本） | 2025/10/24 |
| DevEco Studio 5.1.1 Release (5.1.1.840)  （Patch版本） | 2025/09/05 |
| DevEco Studio 5.1.1 Release (5.1.1.830)  （Patch版本） | 2025/08/07 |
| DevEco Studio 5.1.1 Release (5.1.1.823)  （Patch版本） | 2025/07/16 |
| DevEco Studio 5.1.1 Release (5.1.1.820) | 2025/06/30 |
| SDK | Release | HarmonyOS 5.1.1 Release SDK  基于OpenHarmony SDK Ohos\_sdk\_public 5.1.1.212(API 19 Release) | 2025/10/24 |
| HarmonyOS 5.1.1 Release SDK  基于OpenHarmony SDK Ohos\_sdk\_public 5.1.1.202(API 19 Release) | 2025/06/30 |

说明

* 该版本仅面向部分通过开发者渠道定向获得推送的Mate 60系列手机提供，因此使用其他设备的开发者可能暂时无法体验5.1.1(19)的新增能力。
* **API版本**请在设备的“设置”中点击设备名称，进入“**关于本机**”进行查询。

* DevEco Studio版本请从DevEco Studio界面菜单选择“Help > About DevEco Studio”进行查询。请[点击此处](https://developer.huawei.com/consumer/cn/deveco-studio/)获取最新的DevEco Studio软件版本。
* SDK内置在DevEco Studio，安装DevEco Studio时自动安装配套版本SDK。具体版本请从DevEco Studio界面菜单选择“Help > About HarmonyOS SDK”进行查询。

## 历史Beta版本

### 5.1.1(19) Beta1

| **软件包** | **发布类型** | **版本号** | **发布时间** |
| --- | --- | --- | --- |
| API版本 | Beta | 5.1.1(19) Beta1  *\***注意**：设备系统支持的API能力范围请以**API版本****为准。* | 2025/06/12 |
| DevEco Studio | Beta | DevEco Studio 5.1.1 Beta1 (5.1.1.420) | 2025/06/12 |
| SDK | Beta | HarmonyOS 5.1.1 Beta1 SDK  基于OpenHarmony SDK Ohos\_sdk\_public 5.1.1.66(API 19 Beta1) | 2025/06/12 |

## 应用工程版本信息配置建议

应用工程中应当正确配置应用运行所依赖的SDK版本信息，以确保[应用在不同系统版本的设备上运行时的兼容性](app-compatibility.md)。

使用Beta状态的开发套件版本开发的应用无法上架应用市场，如有上架诉求，建议使用[5.0.5(17) Release](overview-505-release.md)进行新应用的开发。

使用该版本开发的应用，其build-profile.json5配置项中关于版本的配置项建议如下：

| **build-profile.json5配置项** | **已开发应用** | | **新启动开发应用** |
| --- | --- | --- | --- |
| **配置建议** | **配置示例** |
| compileSdkVersion | 无需显性配置，编译时默认使用配套的SDK版本，即默认为：  “compileSdkVersion”: “5.1.1(19)” | NA | 推荐使用[5.0.5(17) Release](overview-505-release.md)进行新应用的开发。 |
| compatibleSdkVersion | 建议与工程升级前的compatibleSdkVersion保持一致 | 和升级前保持一致，如：  “compatibleSdkVersion”: “5.0.0(12)” |
| targetSdkVersion | 推荐您适配新版本的最新变更，然后配置为：“targetSdkVersion”: “5.1.1(19)”。  如果您期望延迟适配变更，可配置targetSdkVersion与工程升级前的targetSdkVersion一致。 | 1、应用适配变更，变更适配完成后配置为：  “targetSdkVersion”: “5.1.1(19)”    2、应用暂不适配变更，需配置为工程升级前的值，如：  “targetSdkVersion”: “5.0.0(12)” |
