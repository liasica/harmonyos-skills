---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/overview-602
title: 版本概览
breadcrumb: 版本说明 > HarmonyOS 6.0.2(22) > 版本概览
category: harmonyos-releases
scraped_at: 2026-04-28T07:33:39+08:00
doc_updated_at: 2026-04-27
content_hash: sha256:e44279b3f3b7c8a68fde7703c19549f91c240362edd79e8e738e4c0ecd13db25
---

6.0.2(22)在6.0.1(21)的基础上，开发能力得到进一步增强：ArkUI增强了滚动组件相关能力，支持更多可配置和自定义的属性；Ability Kit增强了UIAbilityContext管理应用自身UIAbility的能力；ArkWeb增强了与终端用户交互的能力，提升Web页面的交互体验；Connectivity Kit的蓝牙模块增强了获取套接字链路信息的能力；Test Kit的UITest模块增强了模拟交互操作的能力；新增了FAST Kit（算法加速服务），提供高性能算法和数据结构等加速服务，等等。更多详情可参见[OS平台新增和增强特性](os-new-feature-602.md)。

DevEco Studio进一步增强AI智能辅助编程的能力和Code Linter静态检测能力，编译构建脚本（如hvigorfile.ts）支持代码联想、跳转等编辑能力，新增支持数据库可视化调试能力，等等。更多详情可参见[DevEco Studio新增和增强特性](deveco-studio-new-features-602.md)。

## 版本信息

说明

使用正确的配套关系进行应用开发可以获得更流畅的开发体验。

请在阅读版本更新和变更内容前，务必确认版本的配套关系是否与当前您所使用的开发套件是一致的。

### 6.0.2(22)开发者套件配套信息

| **软件包** | **发布类型** | **版本号** | **发布时间** |
| --- | --- | --- | --- |
| API版本 | Release | 6.0.2(22)  *\***注意**：设备系统支持的API能力范围请以**API版本****为准。* | 2026/01/21 |
| DevEco Studio | Release | DevEco Studio 6.0.2 Release（6.0.2.650）  （Patch版本） | 2026/03/30 |
| DevEco Studio 6.0.2 Release（6.0.2.642）  （Patch版本） | 2026/03/06 |
| DevEco Studio 6.0.2 Release（6.0.2.640） | 2026/01/21 |
| SDK | Release | HarmonyOS 6.0.2 Release SDK  基于OpenHarmony SDK Ohos\_sdk\_public 6.0.2.130 (API 22 Release) | 2026/01/21 |

说明

* 该版本需通过[开发者招募活动](https://developer.huawei.com/consumer/cn/activity/111766987539455127)进行申请，申请通过后可获得对应设备的ROM版本推送。
* **API版本**请在设备的“设置”中点击设备名称，进入“**关于本机**”进行查询。

* DevEco Studio版本请从DevEco Studio界面菜单选择“Help > About DevEco Studio”进行查询。
* SDK内置在DevEco Studio，安装DevEco Studio时自动安装配套版本SDK。具体版本请从DevEco Studio界面菜单选择“Help > About HarmonyOS SDK”进行查询。

## 应用工程版本信息配置建议

应用工程中应当正确配置应用运行所依赖的SDK版本信息，以确保[应用在不同系统版本的设备上运行时的兼容性](app-compatibility.md)。

使用该版本开发的应用，其build-profile.json5配置项中关于版本的配置项建议如下：

| **build-profile.json5配置项** | **已开发应用** | | **新启动开发应用** |
| --- | --- | --- | --- |
| **配置建议** | **配置示例** |
| compileSdkVersion | 无需显性配置，编译时默认使用配套的SDK版本，即默认为：  “compileSdkVersion”: “6.0.2(22)” | NA | 推荐使用[6.0.0(20)](overview-600.md)进行新应用的开发。 |
| compatibleSdkVersion | 建议与工程升级前的compatibleSdkVersion保持一致。 | 和升级前保持一致，如：  “compatibleSdkVersion”: “5.0.5(17)” |
| targetSdkVersion | 推荐您适配新版本的最新变更，然后配置为：“targetSdkVersion”: “6.0.2(22)”。  如果您期望延迟适配变更，可配置targetSdkVersion与工程升级前的targetSdkVersion一致。 | 1、应用适配变更，变更适配完成后配置为：  “targetSdkVersion”: “6.0.2(22)”  2、应用暂不适配变更，需配置为工程升级前的值，如：  “targetSdkVersion”: “5.0.5(17)” |

## 历史Beta版本

### 6.0.2(22) Beta1

| **软件包** | **发布类型** | **版本号** | **发布时间** |
| --- | --- | --- | --- |
| API版本 | Beta | 6.0.2(22) Beta1  *\***注意**：设备系统支持的API能力范围请以**API版本****为准。* | 2026/01/04 |
| DevEco Studio | Beta | DevEco Studio 6.0.2 Beta1（6.0.2.636） | 2026/01/04 |
| SDK | Beta | HarmonyOS 6.0.2 Beta1 SDK  基于OpenHarmony SDK Ohos\_sdk\_public 6.0.2.129 (API 22 Beta1) | 2026/01/04 |
