---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/multi-picture-app
title: 多设备图片美化界面
breadcrumb: 最佳实践 > 一次开发，多端部署 > 多设备界面开发 > 多设备界面开发案例 > 多设备图片美化界面
category: best-practices
scraped_at: 2026-04-29T14:12:35+08:00
doc_updated_at: 2026-03-26
content_hash: sha256:bde4d5c1b23bf7ab88ca6830258ccd8ca98edbcdfbe783ab27de5e7477fa9283
---

## 概述

本文从目前流行的垂类市场中，选择图片美化应用作为典型案例详细介绍“一多”在实际开发中的应用。一多图片美化应用包含相册，大图预览，图片编辑功能。

本文的重点内容包括：

* [根据宽度自适应相册列数](multi-picture-app.md#section12641735489)
* [双指缩放控制图片缩放](multi-picture-app.md#section255214446101)

当前系统的产品形态包括手机、折叠屏、平板三种。本文从UX设计、架构设计和页面开发三个角度，提供符合“一多”设计原则的参考样例，介绍“一多”图片美化应用在开发过程中的最佳实践。

* [UX设计](multi-picture-app.md#section206991621369)章节介绍图片美化应用的交互逻辑，类似的设计要点可以直接应用于其他项目。
* [架构设计](multi-picture-app.md#section171321517134515)章节介绍一多项目的三层架构，开发者可以去相关文章或章节了解。
* [页面开发](multi-picture-app.md#section12641735489)章节主要介绍图片美化三个页面的布局设计及如何实现。

说明

阅读本文前，开发者需熟悉[ArkUI（方舟UI框架）](../harmonyos-guides/arkui.md)和页面开发的“一多”能力（参考[一次开发，多端部署概览](bpta-multi-device-overview.md)）。下文将详细介绍它们在“一多”开发实践中如何使用。

## UX设计

本示例中的图片美化应用包含相册、大图预览、图片编辑页面。详细的UX设计可以参考[拍摄美化类设计](../design-guides/responsive-design-examples3-0000001746498074.md)。

## 架构设计

HarmonyOS的分层架构主要包括三个层次：产品定制层、基础特性层和公共能力层，为开发者构建了一个清晰、高效、可扩展的设计架构。更多详情请参考[分层架构设计](bpta-layered-architecture-design.md)。

## 页面开发

本章介绍图片美化应用中如何使用“一多”布局能力，完成页面层级的代码编写和多端适配，同时介绍图片美化应用中的[交互开发](multi-picture-app.md#section255214446101)。

### 布局能力

本节介绍每个页面区域的具体布局能力，帮助开发者从零开始进行图片美化应用的开发。

**相册**

相册页显示所有图片。通过观察相册页在折叠屏上的UX设计图，可以进行如下设计：

* 相册页的两个基础区域及其实现方案如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/af/v3/Uwdey7ciT1yDjXi46hF-Yg/zh-cn_image_0000002194009916.png?HW-CC-KV=V1&HW-CC-Date=20260429T061224Z&HW-CC-Expire=86400&HW-CC-Sign=18ED910C46D5662BAD67150E62EF5E8F2E947F0093AE1C0420D767484BCC5A3E "点击放大")

相册页的2个基础区域介绍及实现方案如下表所示：

| 区域编号 | 简介 | 实现方案 |
| --- | --- | --- |
| 1 | 顶部返回 | 使用[自适应布局](bpta-multi-device-adaptive-layout.md)实现左侧返回图标、文字以及右侧图标。 |
| 2 | 相册列表 | 使用[网格布局](bpta-multi-device-page-layout.md#section1373617413916)实现相册列表。 |

示意图如下：

| 示意图 | sm | md | lg |
| --- | --- | --- | --- |
| 效果图 |  |  |  |

当组件区域宽度变化时，可以通过[onAreaChange()](../harmonyos-references/ts-universal-component-area-change-event.md#onareachange) 获取组件的相关信息，并调整相册列数。

```
1. Flex({ direction: FlexDirection.Column }) {
2. // ...
3. .onAreaChange((oldValue: Area, newValue: Area) => {
4. this.gridColumn = this.getGridColumn(newValue.width);
5. })
6. // ...
7. }
```

[AlbumView.ets](https://gitcode.com/harmonyos_codelabs/MultiPictureBeautification/blob/master/features/albumView/src/main/ets/views/AlbumView.ets#L162-L192)

```
1. // Change the number of Grid columns based on the width of the Grid component.
2. getGridColumn(value: Length): number {
3. return Math.floor(2 * ((parseInt(JSON.stringify(value)) / 360) - 1) + 4);
4. }
```

[AlbumView.ets](https://gitcode.com/harmonyos_codelabs/MultiPictureBeautification/blob/master/features/albumView/src/main/ets/views/AlbumView.ets#L50-L53)

**大图预览**

大图预览显示一张图片。观察大图预览页在折叠屏上的用户体验设计图，可以进行以下设计：

* 将大图预览页划分为4个区域，效果图如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ed/v3/904E5PH6R0GfJVTDQf7iuQ/zh-cn_image_0000002194009904.png?HW-CC-KV=V1&HW-CC-Date=20260429T061224Z&HW-CC-Expire=86400&HW-CC-Sign=90D0E8BFCDD9FF385193FD5F635B3BA5D8C9096EC4F35D4E47FA9CEC6C5D6950 "点击放大")

大图预览页的4个基础区域及其实现方案如下表所示：

| 区域编号 | 简介 | 实现方案 |
| --- | --- | --- |
| 1 | 顶部返回 | 使用[自适应布局](bpta-multi-device-adaptive-layout.md)实现左侧返回图标、文字以及右侧图标。 |
| 2 | 图片展示 | 使用[Image](../harmonyos-references/ts-basic-components-image.md)组件展示图片。 |
| 3 | 相册滚动展示 | 使用[List](../harmonyos-references/ts-container-list.md)实现相册滚动展示。 |
| 4 | 图片操作 | 使用[自适应布局](bpta-multi-device-adaptive-layout.md)实现图标自适应摆放。 |

示意图如下：

| 示意图 | sm | md | lg |
| --- | --- | --- | --- |
| 效果图 |  |  |  |

**图片编辑**

在折叠屏中，可以切换图片区域和编辑操作区域的位置。观察折叠屏上的图片编辑页UX设计图，可以这样设计：

* 图片编辑页划分为3个区域，效果图如下：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4e/v3/2ST3LhuNSJ65Na987PMgcA/zh-cn_image_0000002502028274.png?HW-CC-KV=V1&HW-CC-Date=20260429T061224Z&HW-CC-Expire=86400&HW-CC-Sign=6507930003704321A8AE823E620A8601BC53465D0919EF21203B2BD7DD1AADBE "点击放大")

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7e/v3/isOak9SyQEWXzXP34YzOsQ/zh-cn_image_0000002501868592.png?HW-CC-KV=V1&HW-CC-Date=20260429T061224Z&HW-CC-Expire=86400&HW-CC-Sign=8287DC227CC6220D46137A7F47C7A9C414242BBD5DCBB7548FE166A6382885D0 "点击放大")

* 区域2与区域3使用[Flex](../harmonyos-references/ts-container-flex.md)组件实现左右摆放与上下摆放的切换

图片编辑的3个基础区域及其实现方案如下表所示：

| 区域编号 | 简介 | 实现方案 |
| --- | --- | --- |
| 1 | 顶部返回 | 使用[自适应布局](bpta-multi-device-adaptive-layout.md)实现左侧返回图标、文字以及右侧图标。 |
| 2 | 图片展示 | 使用[Image](../harmonyos-references/ts-basic-components-image.md)组件展示图片。 |
| 3 | 编辑操作栏 | 使用[Flex](../harmonyos-references/ts-container-flex.md)组件实现编辑操作栏的自适应摆放。 |

示意图如下：

| 示意图 | sm | md | lg |
| --- | --- | --- | --- |
| 效果图 |  |  |  |

### 交互开发

针对不同类型的智能设备，交互方式包括触摸屏、鼠标、触控板等。单独适配各种交互方式会增加开发工作量并产生大量重复代码。为了解决这一问题，我们统一了各种交互方式的API，实现了[多设备交互](bpta-multi-interaction.md)。常见的交互方式有触屏事件、键鼠事件、焦点事件。图片美化涉及的交互主要为图片的缩放。

**双指缩放**

在触控屏和触控板上，使用双指捏合或张开可实现缩放功能。本文有两处提到双指缩放操作：

* 相册页，双指缩放控制相册中图片列数变更。可以参考[多设备长视频界面](multi-video-app.md#zh-cn_topic_0000001744653537_section3198710114717)。
* 大图预览页，双指缩放控制图片的宽高变更。

  双指缩放使用[PinchGesture()](../harmonyos-references/ts-basic-gestures-pinchgesture.md) API实现， 当触发双指缩放时，可以实时获取缩放比例参数，传入[scale()](../harmonyos-references/ts-universal-attributes-transformation.md#scale) API（控制组件缩放的API）即可调整图片的比例。

  ```
  1. Row() {
  2. Column() {
  3. Image($r('app.media.photo'))
  4. .autoResize(true)
  5. }
  6. }
  7. // ...
  8. .scale({ x: this.scaleValue, y: this.scaleValue, z: 1 })
  9. .gesture(PinchGesture({ fingers: 2 })
  10. .onActionUpdate((event: GestureEvent | undefined) => {
  11. if (event) {
  12. this.scaleValue = this.pinchValue * event.scale;
  13. }
  14. })
  15. .onActionEnd(() => {
  16. this.pinchValue = this.scaleValue;
  17. }))
  ```

  [CenterPart.ets](https://gitcode.com/harmonyos_codelabs/MultiPictureBeautification/blob/master/features/pictureView/src/main/ets/view/CenterPart.ets#L29-L48)

## 示例代码

* [多设备图片美化界面](https://gitcode.com/harmonyos_codelabs/MultiPictureBeautification)
