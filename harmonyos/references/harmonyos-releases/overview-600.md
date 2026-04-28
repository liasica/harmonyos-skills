---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/overview-600
title: 版本概览
breadcrumb: 版本说明 > HarmonyOS 6.0.0(20) > 版本概览
category: harmonyos-releases
scraped_at: 2026-04-28T07:34:04+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:67b14dc1c8ed030660b85cbf3ea3fdc7ee8c0d8916aa7046b6bb024705227cf4
---

HarmonyOS开发者版本6.0.0(20) Release于2025年9月25日正式发布。

6.0.0(20)在5.1.1(19)的基础上，进一步增强ArkUI组件能力，新增多个系统组件并优化多个组件调用细节等；ArkWeb的Chromium内核升级至132版本，ArkWeb能力增强；新增端侧问答模型，支持端侧的智能问答，新增智慧化数据检索C API，支持向量化、知识检索和知识问答的能力；地图能力新增矢量图层、流场图层、海量点图层、热力图层，支持通过自定义组件生成marker图标等等，更多详情可参见[OS平台新增和增强特性](os-new-feature-600.md)。

DevEco Studio新增AI智能辅助编程，进一步提升编译构建效率和优化内存占用，ArkUI Inspector新增支持按照组件粒度3D展开应用，方便查看组件之间的嵌套、遮挡关系，智慧调优能力新增支持对Allocation内存分配问题和Snapshot内存堆快照问题进行分析，更多详情可参见[DevEco Studio新增和增强特性](deveco-studio-new-features-600.md)。

## 版本信息

说明

使用正确的配套关系进行应用开发可以获得更流畅的开发体验。

请在阅读版本更新和变更内容前，务必确认版本的配套关系是否与当前您所使用的开发套件是一致的。

### 6.0.0(20) Release开发者套件配套信息

| **软件包** | **发布类型** | **版本号** | **发布时间** |
| --- | --- | --- | --- |
| API版本 | Release | 6.0.0(20)  *\***注意**：设备系统支持的API能力范围请以**API版本****为准。* | 2025/09/25 |
| DevEco Studio | Release | DevEco Studio 6.0.0 Release（6.0.0.878）  （Patch版本） | 2025/12/24 |
| DevEco Studio 6.0.0 Release (6.0.0.868)  （Patch版本） | 2025/10/23 |
| DevEco Studio 6.0.0 Release (6.0.0.858) | 2025/09/25 |
| SDK | Release | HarmonyOS 6.0.0 Release SDK  基于OpenHarmony SDK Ohos\_sdk\_public 6.0.0.47 (API 20 Release) | 2025/09/25 |

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
| compileSdkVersion | 无需显性配置，编译时默认使用配套的SDK版本，即默认为：  “compileSdkVersion”: “6.0.0(20)” | NA | 推荐使用[6.0.0(20)](overview-600.md)进行新应用的开发。 |
| compatibleSdkVersion | 建议与工程升级前的compatibleSdkVersion保持一致 | 和升级前保持一致，如：  “compatibleSdkVersion”: “5.0.5(17)” |
| targetSdkVersion | 推荐您适配新版本的最新变更，然后配置为：“targetSdkVersion”: “6.0.0(20)”。  如果您期望延迟适配变更，可配置targetSdkVersion与工程升级前的targetSdkVersion一致。 | 1、应用适配变更，变更适配完成后配置为：  “targetSdkVersion”: “6.0.0(20)”  2、应用暂不适配变更，需配置为工程升级前的值，如：  “targetSdkVersion”: “5.0.5(17)” |

## 历史Beta版本

### 6.0.0(20) Beta5

| **软件包** | **发布类型** | **版本号** | **发布时间** |
| --- | --- | --- | --- |
| API版本 | Beta | 6.0.0(20) Beta5  *\***注意**：设备系统支持的API能力范围请以**API版本****为准。* | 2025/09/15 |
| DevEco Studio | Beta | DevEco Studio 6.0.0 Beta5 (6.0.0.848) | 2025/09/15 |
| SDK | Beta | HarmonyOS 6.0.0 Beta5 SDK  基于OpenHarmony SDK Ohos\_sdk\_public 6.0.0.47 (API 20 Beta5) | 2025/09/15 |

### 6.0.0(20) Beta3

| **软件包** | **发布类型** | **版本号** | **发布时间** |
| --- | --- | --- | --- |
| API版本 | Beta | 6.0.0(20) Beta3  *\***注意**：设备系统支持的API能力范围请以**API版本****为准。* | 2025/08/20 |
| DevEco Studio | Beta | DevEco Studio 6.0.0 Beta3 (6.0.0.828) | 2025/08/20 |
| SDK | Beta | HarmonyOS 6.0.0 Beta3 SDK  基于OpenHarmony SDK Ohos\_sdk\_public 6.0.0.45(API 20 Beta3) | 2025/08/20 |

### 6.0.0(20) Beta2

| **软件包** | **发布类型** | **版本号** | **发布时间** |
| --- | --- | --- | --- |
| API版本 | Beta | 6.0.0(20) Beta2  *\***注意**：设备系统支持的API能力范围请以**API版本****为准。* | 2025/07/23 |
| DevEco Studio | Beta | DevEco Studio 6.0.0 Beta2 (6.0.0.456) | 2025/07/23 |
| SDK | Beta | HarmonyOS 6.0.0 Beta2 SDK  基于OpenHarmony SDK Ohos\_sdk\_public 6.0.0.39(API 20 Beta2) | 2025/07/23 |

### 6.0.0(20) Beta1

| **软件包** | **发布类型** | **版本号** | **发布时间** |
| --- | --- | --- | --- |
| API版本 | Beta | 6.0.0(20) Beta1  *\***注意**：设备系统支持的API能力范围请以**API版本****为准。* | 2025/06/20 |
| DevEco Studio | Beta | DevEco Studio 6.0.0 Beta1 (6.0.0.418SP) | 2025/06/25 |
| DevEco Studio 6.0.0 Beta1 (6.0.0.418) | 2025/06/20 |
| SDK | Beta | HarmonyOS 6.0.0 Beta1 SDK  基于OpenHarmony SDK Ohos\_sdk\_public 6.0.0.35(API 20 Beta1) | 2025/06/20 |
