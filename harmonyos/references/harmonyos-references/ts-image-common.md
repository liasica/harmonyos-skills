---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-image-common
title: 图像类型定义
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 图片与视频 > 图像类型定义
category: harmonyos-references
scraped_at: 2026-04-28T08:01:56+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:447ee55d04d61e3dc57cf6056d303d1e664d3a40ffb24af3a685fd977a7bab31
---

说明

本模块首批接口从API version 7开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## PixelMap

PhonePC/2in1TabletTVWearable

type PixelMap = PixelMap

图像像素类，用于读取或写入图像数据以及获取图像信息。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

| 类型 | 说明 |
| --- | --- |
| [PixelMap](arkts-apis-image-pixelmap.md) | 图像像素类，用于读取或写入图像数据以及获取图像信息。 |

## ImageAnalyzerConfig12+

PhonePC/2in1TabletTVWearable

图像AI分析配置项。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| types | [ImageAnalyzerType[]](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-image-common#imageanalyzertype12) | 否 | 否 | 图像AI分析类型。 |

## ImageAnalyzerType12+

PhonePC/2in1TabletTVWearable

图像AI分析类型，未设置时默认开启主体识别和文字识别功能。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| SUBJECT | 0 | 主体识别功能。 |
| TEXT | 1 | 文字识别功能。 |
| OBJECT\_LOOKUP | 2 | 对象查找功能。 |

## ImageAIOptions12+

PhonePC/2in1TabletTVWearable

图像AI分析选项。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| types | [ImageAnalyzerType[]](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-image-common#imageanalyzertype12) | 否 | 是 | 图像AI分析类型。 |
| aiController | [ImageAnalyzerController](ts-image-common.md#imageanalyzercontroller12) | 否 | 是 | 图像AI分析控制器。 |

说明

该特性中的参数types优先级高于[ImageAnalyzerConfig](ts-image-common.md#imageanalyzerconfig12)中的参数types，两者同时设置时以该特性设置的值为准。

该特性依赖设备能力，且需要和对应组件的[enableAnalyzer](ts-basic-components-image.md#enableanalyzer11)接口（例如[Image组件](ts-basic-components-image.md)）搭配使用。

## ImageAnalyzerController12+

PhonePC/2in1TabletTVWearable

图像分析控制器。可以将此对象绑定至支持的组件，通过控制器来调用支持的方法。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

### constructor12+

PhonePC/2in1TabletTVWearable

constructor()

构造函数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

### getImageAnalyzerSupportTypes12+

PhonePC/2in1TabletTVWearable

getImageAnalyzerSupportTypes(): ImageAnalyzerType[]

获取对应组件支持的分析类型。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值:**

| 类型 | 说明 |
| --- | --- |
| [ImageAnalyzerType[]](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-image-common#imageanalyzertype12) | 对应组件支持的分析类型。 |

## ContentTransitionEffect21+对象说明

PhonePC/2in1TabletTVWearable

定义内容切换时的过渡效果。

### 属性

PhonePC/2in1TabletTVWearable

**元服务API：** 从 API version 21开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| IDENTITY | [ContentTransitionEffect](ts-image-common.md#contenttransitioneffect21对象说明) | 是 | 否 | 内容切换时无过渡动画效果。 |
| OPACITY | [ContentTransitionEffect](ts-image-common.md#contenttransitioneffect21对象说明) | 是 | 否 | 内容切换时采用淡入淡出过渡动画。 |
