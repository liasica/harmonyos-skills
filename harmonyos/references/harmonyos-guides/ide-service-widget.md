---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-service-widget
title: 创建服务卡片
breadcrumb: 指南 > 开发环境搭建 > 工程创建 > 模块管理 > 创建服务卡片
category: harmonyos-guides
scraped_at: 2026-04-28T07:54:57+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:0f5cef0a00be176f1c2f96b160869fb511d712adbb54e4e341aa728c1fbc2ff5
---

## 概述

[服务卡片（简称“卡片”）](formkit-overview.md)可将元服务/应用的重要信息以卡片的形式展示在桌面，用户可通过快捷手势使用卡片，通过轻量交互行为实现服务直达、减少层级跳转的目的。

卡片类型分静态卡片和动态卡片两种。静态卡片内存占用较小，有助于实现整机内存优化，可实现静态信息展示、刷新和点击跳转；动态卡片支持自定义交互、动效、滑动等功能，功能丰富但内存占用较大。

从编译产物角度，卡片包产物分为共包和独立包两种类型，详情请参考[创建ArkTS卡片](arkts-ui-widget-creation.md)。

| 创建方式 | 卡片类型 |
| --- | --- |
| 共包 | 静态卡片（Static Widget） |
| 动态卡片（Dynamic Widget） |
| 独立包 | 独立静态卡片（Static Widget(Standalone)） |
| 独立动态卡片（Dynamic Widget(Standalone)） |

创建卡片后可选择不同卡片模板以满足业务需求，具体卡片模板和详细描述如下。

| 模板名称 | 支持的设备 | 支持的开发语言 | 模板描述 |
| --- | --- | --- | --- |
| Hello World | Phone、Tablet、2in1、Wearable、Car、TV | ArkTS、JS | HelloWorld卡片，用于高效直观地构建UI。当前Hello World卡片模板支持使用6\*4尺寸。 |
| Image With Information（图文卡片模板） | Phone、Tablet、2in1、Wearable、Car | ArkTS、JS | 图文卡片模板主要在于展现图片和一定数量文本的搭配，在这种布局下，图片和文本属于同等重要的信息。在不同尺寸下，图片大小和文本数量会发生一定变化，用于凸显关键信息。 |
| Immersive Information（沉浸图文卡片模板） | Phone、Tablet、2in1、Wearable、Car | ArkTS、JS | 沉浸式卡片的装饰性较强，能够较好的提升卡片品质感并起到装饰桌面的作用，合理的去布局信息与背景图片之间的空间比例，可以提升用户的个性化使用体验。 |
| List | Phone、Tablet、2in1、Car | ArkTS | 提供基本的列表功能。当前仅动态卡片支持在API 11及以上工程创建List卡片模板。 |
| Control Button | Phone、Tablet、2in1、Car | ArkTS | 操控类型的卡片，展示文本信息与按钮操作，点击按钮响应事件。当前仅静态卡片支持API 11及以上工程创建Control Button卡片模板。 |
| Control Search | Phone、Tablet、2in1、Car | ArkTS | 操控类型的卡片，适用于搜索场景。当前仅静态卡片支持API 11及以上工程创建Control Search卡片模板。 |

## 使用约束

* 卡片不支持调试。
* 仅应用的Hello World、Image With Information、Immersive Information的动态卡片和独立动态卡片支持JS语言，元服务不支持JS语言。
* 从DevEco Studio 5.0.4 Release开始，支持在API 16及以上工程创建Wearable设备可用的卡片。
* 从DevEco Studio 6.0.0 Beta3开始，支持在API 20及以上工程创建Car设备可用的卡片。
* 从DevEco Studio 6.0.0 Beta3开始，支持Phone设备创建独立静态/动态卡片。
* DevEco Studio 5.1.1 Release（Build Version:5.1.1.850）版本、DevEco Studio 6.0.0 Release（Build Version:6.0.0.868）及以上版本，支持工程创建TV设备可用的卡片。
* 一个工程模块内，仅支持创建共包类型卡片或独立包类型卡片。
* 每个模块最多可以配置16张卡片。

## 创建服务卡片

[创建一个工程](ide-create-new-project.md)后，可以通过如下方法进行创建卡片。

1. 创建卡片包括如下两种方式：
   * 选择模块（如entry模块）下的任意文件，单击菜单栏**File > New > Service Widget**，[按需选择卡片](ide-service-widget.md#section6353219163116)。
   * 选择模块（如entry模块）下的任意文件，单击**右键 > New > Service Widget**，[按需选择卡片](ide-service-widget.md#section6353219163116)。

   说明

   * API 11 Stage模型及以上，创建元服务工程或在元服务工程中创建模块时，不再默认创建卡片和EntryCard。
2. 在**Choose a Template for Your Service Widget**界面中，选择卡片模板，单击**Next**。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1/v3/CiHcjyJVSvamKD4lCO1lcA/zh-cn_image_0000002561832691.png?HW-CC-KV=V1&HW-CC-Date=20260427T235456Z&HW-CC-Expire=86400&HW-CC-Sign=3F933E31E01EAEDB202483046DEF56BBE0AD9E9D24CB83B3AD4BF1C8DF0142D1)
3. 在**Configure Your Service Widget**界面中，配置卡片的基本信息，包括：
   * **Service widget name**：卡片的名称，在同一个应用/元服务中，卡片名称不能重复，且只能包含大小写字母、数字和下划线。
   * **Display name**：卡片预览面板上显示的卡片名称。仅API 11 及以上Stage工程支持配置该字段。
   * **Description**：卡片的描述信息。
   * **Language：**界面开发语言，可选择创建ArkTS/JS卡片。
   * **Support dimension**：选择卡片的规格。部分卡片支持同时设置多种规格。首次创建卡片时，将默认生成一个EntryCard目录，用于存放卡片快照。
   * **Default dimension**：在下拉框中可选择默认的卡片。
   * **Ability name：**选择一个挂靠卡片的Form Ability，或者创建一个新的Form Ability。
   * **Module name：**卡片所属的模块。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b9/v3/V6obd83HTbGvpOouE7f7_w/zh-cn_image_0000002530752768.png?HW-CC-KV=V1&HW-CC-Date=20260427T235456Z&HW-CC-Expire=86400&HW-CC-Sign=0A921ECB3BF5B20F79E43C7915ACD0E0064C5BC6E55E979A45C3AF2C068E7750)
4. 单击**Finish**完成卡片的创建。创建完成后，工具会自动创建出卡片的布局文件，并在form\_config.json文件中写入服务卡片的属性字段，关于各字段的说明请参考[配置文件说明](arkts-ui-widget-configuration.md)。
5. 卡片创建完成后，请根据开发指导，完成卡片的开发，详情请参考[服务卡片开发指南](arkts-ui-widget.md)。

## 预览服务卡片

在开发卡片过程中，支持对卡片进行实时预览。卡片通过ArkTS文件进行布局设计，在开发过程中，可以对布局文件进行实时预览，只要在布局文件中保存了修改的源代码，在预览器中就可以实时查看布局效果。在Phone和Tablet卡片的预览效果中，每个尺寸的卡片提供3种场景的预览效果，分别为极窄（Minimum）、默认（Default）、极宽(Maximum)，开发者应确保三种尺寸的显示效果均正常，以便适应不同屏幕尺寸的设备。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e4/v3/64XfcWaiRkC5Q_MSWgCY0g/zh-cn_image_0000002530912762.png?HW-CC-KV=V1&HW-CC-Date=20260427T235456Z&HW-CC-Expire=86400&HW-CC-Sign=9F7D7ECDD87BB196F01A707547335936C9A7F77292386B7E6228CC19B89F1AAD)

关于预览器的使用详细说明请参考[界面预览](ide-previewer-01.md)。
