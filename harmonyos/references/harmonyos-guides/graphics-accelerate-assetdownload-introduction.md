---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/graphics-accelerate-assetdownload-introduction
title: 业务概述
breadcrumb: 指南 > 图形 > Graphics Accelerate Kit（图形加速服务） > 游戏资源加速服务 > 资源包后台下载 > 业务概述
category: harmonyos-guides
scraped_at: 2026-04-28T07:47:40+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:c2b33543d08ac21a6e89e6de88ec307f0ad78ea86454543191cd0c04732c6e4c
---

从5.1.0(18)版本开始，新增资源包后台下载。

资源包后台下载是将资源文件（例如关卡包、3D角色模型、纹理等）静默下载到用户设备中，减少游戏启动后等待资源包下载的时间，解决游戏启动慢的问题，为用户提供即开即玩的游戏体验。

## 主要功能

### 系统后台下载资源包

* 场景一

  用户在应用市场安装游戏后、或在应用市场更新游戏后，在游戏未启动状态下，若检测到该游戏有资源包需要更新，将自动触发资源包下载。用户下拉通知栏，实时查看资源包下载进度。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9a/v3/TxOWkSocT4Kobeo384tCUQ/zh-cn_image_0000002583478715.gif?HW-CC-KV=V1&HW-CC-Date=20260427T234727Z&HW-CC-Expire=86400&HW-CC-Sign=FA325D8D1328C317ACAFEAF736F18ABE23BA92B2D15A2CD93CFD3F4C5D8730DE "点击放大")
* 场景二

  待用户设备满足闲时条件时，在游戏未启动状态下，若检测到上次更新资源包未完成，或该游戏有新的资源包需要更新，将自动触发资源包下载。用户下拉通知栏，实时查看资源包下载进度。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1a/v3/EXrOezkNQMKJgEipOlF3iQ/zh-cn_image_0000002552799066.gif?HW-CC-KV=V1&HW-CC-Date=20260427T234727Z&HW-CC-Expire=86400&HW-CC-Sign=FF2AD0A14DE5B12A65CAF636BC13BC07DABA37FAA50E941E7CFAFF19AF88A1A4 "点击放大")

### 系统后台切应用前台接续下载资源包

用户在应用市场安装游戏后、或在应用市场更新游戏后，在游戏未启动状态下，若检测到该游戏有资源包需要更新，将自动触发资源包下载。用户下拉通知栏，实时查看资源包下载进度。在下载过程中点击游戏App，游戏接管未完成的下载任务。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b/v3/QHJrhe82SUaL92m6VsqbOg/zh-cn_image_0000002583438761.gif?HW-CC-KV=V1&HW-CC-Date=20260427T234727Z&HW-CC-Expire=86400&HW-CC-Sign=73108CA3520E06905FE6E41406DE5DB3D3E19EDBA86D0BB8488C49E6F3618F9E "点击放大")

### 应用前台下载资源包

用户点击游戏App，若检测到上次更新资源包未完成，或该游戏有新的资源包需要更新，游戏将接续执行未完成的下载任务或提交新的下载任务。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/neJU45-pRliuUvQFdYOePA/zh-cn_image_0000002552958716.gif?HW-CC-KV=V1&HW-CC-Date=20260427T234727Z&HW-CC-Expire=86400&HW-CC-Sign=48F37B5321ECE3F60F50973401781DD775819E45079AA5F0180FC4D115781AF2 "点击放大")

### 应用前台切应用后台下载资源包

说明

需要与[dataTransfer类型的长时任务](continuous-task.md)协同使用。

应用前台下载资源包的过程中，将游戏切至后台，资源包下载任务不中断。用户下拉通知栏，实时查看资源包下载进度。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/12/v3/5D9sdmpEQKmR101jpRVXAQ/zh-cn_image_0000002583478717.gif?HW-CC-KV=V1&HW-CC-Date=20260427T234727Z&HW-CC-Expire=86400&HW-CC-Sign=909B6677868FEF8C79E7564CC4093D9714B5C9B865AA04886B592C90F5F87CE8 "点击放大")

## 实现流程

| 序号 | 步骤 | 说明 |
| --- | --- | --- |
| 1 | [开发准备](graphics-accelerate-assetdownload-prepare.md) | 开发者需提前做好相关准备工作。 |
| 2 | 开发资源包后台下载功能：  - [系统后台下载资源包](graphics-accelerate-assetdownload-back-system.md)  - [应用前台下载资源包](graphics-accelerate-assetdownload-fore.md)  - [系统后台切应用前台接续下载资源包](graphics-accelerate-assetdownload-back-fore.md) | 开发者可以在游戏工程中接入资源包系统后台下载、应用前台下载、系统后台切应用前台接续下载功能。 |
| 3 | 发布资源包下载任务：  1. [进入申请页面](graphics-accelerate-assetdownload-release.md#进入申请页面)  2. [创建下载任务](graphics-accelerate-assetdownload-release.md#创建下载任务)  3. [提交下载任务](graphics-accelerate-assetdownload-release.md#提交下载任务)  4. [测试下载功能](graphics-accelerate-assetdownload-release.md#测试下载功能)  5. [发布下载任务](graphics-accelerate-assetdownload-release.md#发布下载任务) | 开发者需前往AppGallery Connect创建并发布下载资源包任务。建议开发者在正式发布资源包下载任务前，先在本地测试是否可以成功下载资源包。 |
| 4 | [查看资源包分发数据](graphics-accelerate-assetdownload-data.md) | 资源包下载任务正式发布后，开发者可以前往AppGallery Connect查看资源包分发情况。 |

## 基本概念

| 概念 | 说明 |
| --- | --- |
| CDN | 内容分发网络（Content Delivery Network），是一种通过网络中分布资源服务器，用以提高网站访问速度的技术。当前资源包后台下载功能支持游戏在AppGallery Connect配置华为CDN或三方CDN的资源包下载配置项。 |
| 资源加速ExtensionAbility | [ExtensionAbility](../harmonyos-references/js-apis-app-ability-extensionability.md)组件是基于特定场景（例如服务卡片、输入法）提供的应用组件，以便满足更多的使用场景。[资源加速ExtensionAbility](../harmonyos-references/graphics-accelerate-extensionability.md)是为资源包后台下载框架，为资源包后台下载提供关键的生命周期函数。在后台下载任务成功/失败/结束后支持调用相应的回调函数。 |
| 系统后台下载 | 游戏应用进程未加载时，系统能力自动开启资源包下载任务。 |
