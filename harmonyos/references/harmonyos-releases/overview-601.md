---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/overview-601
title: 版本概览
breadcrumb: 版本说明 > HarmonyOS 6.0.1(21) > 版本概览
category: harmonyos-releases
scraped_at: 2026-04-28T07:33:51+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:e4dd7c95ddb8d133ad86c77a77f050881121b8f3fe640fb998610a1be41ce659
---

6.0.1(21)在6.0.0(20)的基础上，进一步增强ArkUI组件能力，新增一批属性样式的C API，增强了Image组件的SVG解析能力；Ability Kit增强了拉起应用的结果处理；ArkWeb增强了WebView相关能力；后台任务新增支持并行创建多个同样的长时任务；地图服务进一步丰富了可直接调用的场景，等等。更多详情可参见[OS平台新增和增强特性](os-new-feature-601.md)。

DevEco Studio进一步增强AI智能辅助编程的能力和Code Linter静态检测能力，工程级配置文件新增多个可选配置字段，等等。更多详情可参见[DevEco Studio新增和增强特性](deveco-studio-new-features-601.md)。

## 版本信息

说明

使用正确的配套关系进行应用开发可以获得更流畅的开发体验。

请在阅读版本更新和变更内容前，务必确认版本的配套关系是否与当前您所使用的开发套件是一致的。

### 6.0.1(21)开发者套件配套信息

| **软件包** | **发布类型** | **版本号** | **发布时间** |
| --- | --- | --- | --- |
| API版本 | Release | 6.0.1(21)  *\***注意**：设备系统支持的API能力范围请以**API版本****为准。* | 2025/11/20 |
| DevEco Studio | Release | DevEco Studio 6.0.1 Release (6.0.1.268)  （Patch版本） | 2026/02/13 |
| DevEco Studio 6.0.1 Release (6.0.1.260)  （Patch版本） | 2025/12/17 |
| DevEco Studio 6.0.1 Release (6.0.1.251)  （Patch版本） | 2025/11/24 |
| DevEco Studio 6.0.1 Release (6.0.1.249) | 2025/11/20 |
| SDK | Release | HarmonyOS 6.0.1 Release SDK  基于OpenHarmony SDK Ohos\_sdk\_public 6.0.1.112 (API 21 Release) | 2025/11/20 |

说明

* **API版本**请在设备的“设置”中点击设备名称，进入“**关于本机**”进行查询。

* DevEco Studio版本请从DevEco Studio界面菜单选择“Help > About DevEco Studio”进行查询。
* SDK内置在DevEco Studio，安装DevEco Studio时自动安装配套版本SDK。具体版本请从DevEco Studio界面菜单选择“Help > About HarmonyOS SDK”进行查询。

## 应用工程版本信息配置建议

应用工程中应当正确配置应用运行所依赖的SDK版本信息，以确保[应用在不同系统版本的设备上运行时的兼容性](app-compatibility.md)。

使用该版本开发的应用，其build-profile.json5配置项中关于版本的配置项建议如下：

| **build-profile.json5配置项** | **已开发应用** | | **新启动开发应用** |
| --- | --- | --- | --- |
| **配置建议** | **配置示例** |
| compileSdkVersion | 无需显性配置，编译时默认使用配套的SDK版本，即默认为：  “compileSdkVersion”: “6.0.1(21)” | NA | 推荐使用[6.0.0(20)](overview-600.md)进行新应用的开发。 |
| compatibleSdkVersion | 建议与工程升级前的compatibleSdkVersion保持一致 | 和升级前保持一致，如：  “compatibleSdkVersion”: “5.0.5(17)” |
| targetSdkVersion | 推荐您适配新版本的最新变更，然后配置为：“targetSdkVersion”: “6.0.1(21)”。  如果您期望延迟适配变更，可配置targetSdkVersion与工程升级前的targetSdkVersion一致。 | 1、应用适配变更，变更适配完成后配置为：  “targetSdkVersion”: “6.0.1(21)”  2、应用暂不适配变更，需配置为工程升级前的值，如：  “targetSdkVersion”: “5.0.5(17)” |

## 历史Beta版本

### 6.0.1(21) Beta1

| **软件包** | **发布类型** | **版本号** | **发布时间** |
| --- | --- | --- | --- |
| API版本 | Beta | 6.0.1(21) Beta1  *\***注意**：设备系统支持的API能力范围请以**API版本****为准。* | 2025/11/06 |
| DevEco Studio | Beta | DevEco Studio 6.0.1 Beta1 (6.0.1.246) | 2025/11/06 |
| SDK | Beta | HarmonyOS 6.0.1 Beta1 SDK  基于OpenHarmony SDK Ohos\_sdk\_public 6.0.1.111 (API 21 Beta1) | 2025/11/06 |
