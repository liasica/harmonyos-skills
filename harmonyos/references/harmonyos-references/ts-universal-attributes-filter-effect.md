---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-filter-effect
title: 视效设置
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 通用属性 > 视效与模糊 > 视效设置
category: harmonyos-references
scraped_at: 2026-04-28T08:01:08+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:9bbf7f649cc8a0f5c63e9f51de87934be61199b1516e84bfb915e9a8e713f77c
---

本模块提供接口设置组件视觉效果，包括滤镜效果（如：模糊，像素扩展等）和非滤镜效果（如：点光源等）。

说明

从API version 12开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

## visualEffect

PhonePC/2in1TabletTVWearable

visualEffect(effect: VisualEffect): T

设置非滤镜视觉效果。

说明

从API version 20开始，该接口支持在[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)中调用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| effect | [VisualEffect](ts-universal-attributes-filter-effect.md#visualeffect-1) | 是 | 非滤镜视觉效果。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## backgroundFilter

PhonePC/2in1TabletTVWearable

backgroundFilter(filter: Filter): T

设置背景滤镜视觉效果。

说明

从API version 20开始，该接口支持在[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)中调用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| filter | [Filter](ts-universal-attributes-filter-effect.md#filter) | 是 | 背景滤镜视觉效果。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## foregroundFilter

PhonePC/2in1TabletTVWearable

foregroundFilter(filter: Filter): T

设置前景滤镜（内容）视觉效果。

说明

从API version 20开始，该接口支持在[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)中调用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| filter | [Filter](ts-universal-attributes-filter-effect.md#filter) | 是 | 前景滤镜（内容）视觉效果。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## compositingFilter

PhonePC/2in1TabletTVWearable

compositingFilter(filter: Filter): T

设置合成滤镜视觉效果。

说明

从API version 20开始，该接口支持在[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)中调用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| filter | [Filter](ts-universal-attributes-filter-effect.md#filter) | 是 | 合成滤镜视觉效果。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## materialFilter23+

PhonePC/2in1TabletTVWearable

materialFilter(filter: Filter | undefined): T

设置系统材质滤镜效果，系统材质滤镜的绘制早于[backgroundFilter](ts-universal-attributes-filter-effect.md#backgroundfilter)绘制，即位于backgroundFilter的更底层。

说明

该接口支持在[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)中调用。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| filter | [Filter](ts-universal-attributes-filter-effect.md#filter) | undefined | 是 | 系统材质滤镜视觉效果。设置为undefined时恢复为无系统材质滤镜效果。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## Filter

PhonePC/2in1TabletTVWearable

type Filter = Filter

导入Filter类型对象。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 说明 |
| --- | --- |
| [Filter](js-apis-uieffect.md#filter) | 用于将相应的效果添加到指定的组件上。 |

## VisualEffect

PhonePC/2in1TabletTVWearable

type VisualEffect = VisualEffect

导入VisualEffect类型对象。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 说明 |
| --- | --- |
| [VisualEffect](js-apis-uieffect.md#visualeffect) | 用于将相应的效果添加到指定的组件上。 |

## 示例

PhonePC/2in1TabletTVWearable

该示例主要演示前景滤镜、背景滤镜和合成滤镜的模糊效果。

```
1. // xxx.ets
2. import { uiEffect } from '@kit.ArkGraphics2D';

4. @Entry
5. @Component
6. struct FilterEffectExample {
7. @State filterTest1: uiEffect.Filter = uiEffect.createFilter().blur(10);
8. @State filterTest2: uiEffect.Filter = uiEffect.createFilter().blur(10);
9. @State filterTest3: uiEffect.Filter = uiEffect.createFilter().blur(10);

11. build() {
12. Column({ space: 15 }) {

14. Text('foregroundFilter').fontSize(20).width('75%').fontColor('#DCDCDC')
15. Text('前景滤镜')
16. .width(100)
17. .height(100)
18. .backgroundColor('#ADD8E6')
19. // $r("app.media.app_icon")需替换为开发者所需的资源文件
20. .backgroundImage($r("app.media.app_icon"))
21. .backgroundImageSize({ width: 80, height: 80 })
22. .foregroundFilter(this.filterTest1) // 通过 foregroundFilter 设置模糊效果

24. Text('backgroundFilter').fontSize(20).width('75%').fontColor('#DCDCDC')
25. Text('背景滤镜')
26. .width(100)
27. .height(100)
28. .backgroundColor('#ADD8E6')
29. // $r("app.media.app_icon")需替换为开发者所需的资源文件
30. .backgroundImage($r("app.media.app_icon"))
31. .backgroundImageSize({ width: 80, height: 80 })
32. .backgroundFilter(this.filterTest2) // 通过 backgroundFilter 设置模糊效果

34. Text('compositingFilter').fontSize(20).width('75%').fontColor('#DCDCDC')
35. Text('合成滤镜')
36. .width(100)
37. .height(100)
38. .backgroundColor('#ADD8E6')
39. // $r("app.media.app_icon")需替换为开发者所需的资源文件
40. .backgroundImage($r("app.media.app_icon"))
41. .backgroundImageSize({ width: 80, height: 80 })
42. .compositingFilter(this.filterTest3) // 通过 compositingFilter 设置模糊效果
43. }
44. .height('100%')
45. .width('100%')
46. }
47. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ae/v3/nIgce0RaQ_O-HnesPtfaSQ/zh-cn_image_0000002552799874.jpg?HW-CC-KV=V1&HW-CC-Date=20260428T000107Z&HW-CC-Expire=86400&HW-CC-Sign=50AC138DC5AA8E4F88DFB1751E65D6AD0E524DB1BE66162E8972FB8F7EF03240)
