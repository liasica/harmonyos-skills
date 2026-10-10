---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-service-widget
title: 创建服务卡片
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 开发环境搭建 > 工程创建 > 模块管理 > 创建服务卡片
category: harmonyos-guides
scraped_at: 2026-10-11T07:23:16+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:cbf0e9679c9a3574819d504c780bf07703ba2b978a07109cd31b1556c5740523
---

## 概述

服务卡片可将应用的重要信息以卡片的形式展示在桌面，用户可通过快捷手势使用卡片，通过轻量交互行为实现服务直达、减少层级跳转的目的。

当前提供如下卡片模板：

| 模板名称 | 支持的设备 | 支持的开发语言 | 模板描述 |
| --- | --- | --- | --- |
| Hello World | Phone、Tablet、2in1 | ArkTS | HelloWorld卡片，用于高效直观地构建UI。当前Hello World卡片模板支持使用6\*4尺寸。 |
| Image With Information（图文卡片模板） | Phone、Tablet、2in1 | ArkTS | 图文卡片模板主要在于展现图片和一定数量文本的搭配，在这种布局下，图片和文本属于同等重要的信息。在不同尺寸下，图片大小和文本数量会发生一定变化，用于凸显关键信息。 |
| Immersive Information（沉浸图文卡片模板） | Phone、Tablet、2in1 | ArkTS | 沉浸式卡片的装饰性较强，能够较好的提升卡片品质感并起到装饰桌面的作用，合理的去布局信息与背景图片之间的空间比例，可以提升用户的个性化使用体验。 |

## 使用约束

* 每个module最多可以配置16张服务卡片。
* 卡片不支持调试。

## 创建服务卡片

1. [创建一个工程](ide-hmos-create-new-project.md)后，选择模块（如entry模块）下的任意文件，单击**右键 > 新建 > Service Widget，**选择创建动/静态服务卡片。

   **Dynamic** **Widget**：动态服务卡片。**form\_config.json**文件中**isDynamic**参数配置为"true"。动态卡片支持自定义交互、动效、滑动等功能，功能丰富但内存占用较大。

   **Static** **Widget**：静态服务卡片。**form\_config.json**文件中**isDynamic**参数配置为"false"。静态卡片内存占用较小，有助实现整机内存优化，可实现静态信息展示、刷新和点击跳转。
2. 选择卡片模板，单击**确认**。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1e/v3/9H1CiNmvTaqFK0k92XMQ7g/zh-cn_image_0000002750169520.png "点击放大")
3. 在界面中配置卡片的基本信息，包括：
   * **服务卡片名**：卡片的名称，在同一个应用中，卡片名称不能重复，且只能包含大小写字母、数字和下划线。
   * **显示名**：卡片预览面板上显示的卡片名称。
   * **描述**：卡片的描述信息。
   * **开发语言：**界面开发语言，可选择创建ArkTS卡片。
   * **支持规格**：选择卡片的规格。部分卡片支持同时设置多种规格。
   * **默认规格**：在下拉框中可选择默认的卡片。
   * **Ability名称：**选择一个挂靠服务卡片的Form Ability，或者创建一个新的Form Ability。
   * **模块名：**卡片所属的模块。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/d57tEEmpSbyW-e-L__RXzA/zh-cn_image_0000002779608543.png "点击放大")
4. 单击**确认**完成卡片的创建。创建完成后，工具会自动创建出服务卡片的布局文件，并在form\_config.json文件中写入服务卡片的属性字段，关于各字段的说明请参考[配置文件说明](arkts-ui-widget-configuration.md)。
5. 卡片创建完成后，请根据开发指导，完成服务卡片的开发，详情请参考[服务卡片开发指南](arkts-ui-widget.md)。
