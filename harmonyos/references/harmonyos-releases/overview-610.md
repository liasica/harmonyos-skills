---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/overview-610
title: 版本概览
breadcrumb: 版本说明 > HarmonyOS 6.1.0(23) > 版本概览
category: harmonyos-releases
scraped_at: 2026-04-28T07:33:18+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:4be942e33106e7917528f50784d1e4eae71cb5efdbac025ce928d20bb52f241c
---

6.1.0(23)在6.0.2(22)的基础上，开发能力得到进一步增强：ArkUI新增自定义键盘切换接续、跑马灯间距配置、滚动组件模拟拖拽等能力；Ability Kit支持Native软件包独立签名及启动时间戳获取；ArkWeb新增模拟点击检测、首屏渲染时间统计、Cookies管理能力；Camera Kit支持HDR动态照片拍摄；Audio Kit新增变声效果和系统音效管理；Media Kit支持批量提取视频缩略图及HDR转SDR；Network Kit增强HTTP请求配置和DNS转码能力；Connectivity Kit的BLE支持自定义广播名称；UI Design Kit新增底部页签悬浮样式和沉浸式材质效果的设置；新增AR Engine人脸识别与骨骼跟踪、3D空间重建会话管理、营销组件等能力，等等。更多详情可参见[OS平台新增和增强特性](os-new-feature-610.md)。

DevEco Studio能力进一步增强：支持开发API 23工程；支持一键启动模拟器，运行调试应用；Hvigor支持可视化查看和执行任务；CodeGenie支持工程问答，支持添加和管理提示词库；API变更助手扫描结果支持快速智能问答；ArkUI Inspector支持查看窗口交互事件，帮助开发者定位窗口失焦、获焦、重绘等问题，等等。更多详情可参见[DevEco Studio新增和增强特性](deveco-studio-new-features-610.md)。

## 版本信息

说明

使用正确的配套关系进行应用开发可以获得更流畅的开发体验。

请在阅读版本更新和变更内容前，务必确认版本的配套关系是否与当前您所使用的开发套件是一致的。

### 6.1.0(23)开发者套件配套信息

| **软件包** | **发布类型** | **版本号** | **发布时间** |
| --- | --- | --- | --- |
| API版本 | Release | 6.1.0(23)  *\***注意**：设备系统支持的API能力范围请以**API版本****为准。* | 2026/04/20 |
| DevEco Studio | Release | DevEco Studio 6.1.0 Release（6.1.0.830） | 2026/04/20 |
| SDK | Release | 基于OpenHarmony SDK Ohos\_sdk\_public 6.1.0.105 (API 23 Release) | 2026/04/20 |

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
| compileSdkVersion | 无需显性配置，编译时默认使用配套的SDK版本，即默认为：  “compileSdkVersion”: “6.1.0(23)” | NA | 推荐使用[6.0.0(20)](overview-600.md)进行新应用的开发。 |
| compatibleSdkVersion | 建议与工程升级前的compatibleSdkVersion保持一致。 | 和升级前保持一致，如：  “compatibleSdkVersion”: “6.0.0(20)” |
| targetSdkVersion | 推荐您适配新版本的最新变更，然后配置为：“targetSdkVersion”: “6.1.0(23)”。  如果您期望延迟适配变更，可配置targetSdkVersion与工程升级前的targetSdkVersion一致。 | 1、应用适配变更，变更适配完成后配置为：  “targetSdkVersion”: “6.1.0(23)”  2、应用暂不适配变更，需配置为工程升级前的值，如：  “targetSdkVersion”: “6.0.0(20)” |

## 历史版本

### 6.1.0(23) Release配套信息

说明

该版本为受限发布的版本，未面向全网公开发布。

| **软件包** | **发布类型** | **版本号** | **发布时间** |
| --- | --- | --- | --- |
| ROM | Release | 6.0.0.328 (SP36) | 2026/03/20 |
| DevEco Studio | Release | DevEco Studio 6.1.0 Release（6.1.0.818） | 2026/03/20 |
| SDK | Release | 基于OpenHarmony SDK Ohos\_sdk\_public 6.1.0.105 (API 23 Release) | 2026/03/20 |

### 6.1.0(23) Beta2配套信息

说明

该版本为受限发布的版本，未面向全网公开发布。

| **软件包** | **发布类型** | **版本号** | **发布时间** |
| --- | --- | --- | --- |
| ROM | Beta | 6.0.0.328 (SP22) | 2026/03/09 |
| DevEco Studio | Beta | DevEco Studio 6.1.0 Beta2（6.1.0.816） | 2026/03/09 |
| SDK | Beta | 基于OpenHarmony SDK Ohos\_sdk\_public 6.1.0.31 (API 23 Beta2) | 2026/03/09 |

### 6.1.0(23) Beta1配套信息

说明

该版本为受限发布的版本，未面向全网公开发布。

| **软件包** | **发布类型** | **版本号** | **发布时间** |
| --- | --- | --- | --- |
| ROM | Beta | 6.0.0.328 | 2026/02/06 |
| DevEco Studio | Beta | DevEco Studio 6.1.0 Beta1（6.1.0.609） | 2026/02/06 |
| SDK | Beta | 基于OpenHarmony SDK Ohos\_sdk\_public 6.1.0.28 (API 23 Beta1) | 2026/02/06 |
