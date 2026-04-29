---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-segmentbutton
title: SegmentButton
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 系统预置UI组件库 > SegmentButton
category: harmonyos-references
scraped_at: 2026-04-29T13:53:02+08:00
doc_updated_at: 2026-04-28
content_hash: sha256:fd179913120848986034ba5c525d06b7753c7721d27a93a2709c58d1198a8a1c
---

分段按钮组件包含页签类分段按钮、胶囊类单选分段按钮和胶囊类多选分段按钮。

说明

该组件从API version 11开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { SegmentButton, SegmentButtonOptions, SegmentButtonItemOptionsArray } from '@kit.ArkUI';
```

## 子组件

PhonePC/2in1TabletTVWearable

无

## 属性

PhonePC/2in1TabletTVWearable

不支持[通用属性](ts-component-general-attributes.md)。

## 事件

PhonePC/2in1TabletTVWearable

不支持[通用事件](ts-component-general-events.md)。

## SegmentButton

PhonePC/2in1TabletTVWearable

SegmentButton({ options: SegmentButtonOptions, selectedIndexes: number[], onItemClicked: Callback<number>, maxFontScale: number | Resource })

**装饰器类型：**@Component

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

说明

* 分段按钮不支持[通用属性](ts-component-general-attributes.md)。分段按钮使用当前区域可使用的最大宽度作为组件宽度，并且根据按钮个数平均分配每个按钮宽度；分段按钮高度根据按钮内容（文本及图片）自动适应，其最小高度为28vp。
* @Prop装饰的属性为可选参数，仅当与@Require装饰器联合使用时，才必须在构造时传入对应参数。

| 名称 | 类型 | 必填 | 装饰器类型 | 说明 |
| --- | --- | --- | --- | --- |
| options | [SegmentButtonOptions](ohos-arkui-advanced-segmentbutton.md#segmentbuttonoptions) | 是 | @ObjectLink | 分段按钮选项。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| selectedIndexes | number[] | 是 | @Link | 分段按钮的选中项编号，第一项的编号为0，之后顺序增加。  **说明：**  selectedIndexes使用[@Link装饰器：父子双向同步](../harmonyos-guides/arkts-link.md)，仅支持有效的按钮编号（第一个按钮编号为0，之后按顺序累加），如没有选中项可传入空数组[]。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| onItemClicked13+ | Callback<number> | 否 | - | 当分段按钮选项被点击时，触发的回调函数接收被点击的选项下标作为参数。若不传入此参数，则点击时不触发回调。  **元服务API：** 从API version 13开始，该接口支持在元服务中使用。 |
| maxFontScale14+ | number | [Resource](ts-types.md#resource) | 否 | @Prop | 分段按钮选项文字的最大字体放大倍数。  取值范围：[1, 2]  当设置的值小于1时，按值为1处理，设置的值大于2时，按值为2处理。  **元服务API：** 从API version 14开始，该接口支持在元服务中使用。 |

## SegmentButtonOptions

PhonePC/2in1TabletTVWearable

说明

不支持设置字体类型。

分段按钮选项类用于提供初始数据和自定义属性。

**装饰器类型：** @Observed

### 属性

PhonePC/2in1TabletTVWearable

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| type | "tab" |"capsule" | 否 | 否 | 分段按钮组件的类型。  **说明：**  "tab"：页签类分段按钮，适用于页面或内容区域的切换场景。  "capsule"：胶囊类分段按钮，适用于单选或多选的选择场景。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| multiply | boolean | 否 | 否 | 分段按钮组件是否可以多选。  true: 可多选；false: 不可多选。页签类分段按钮只支持单选，设置multiply为true不生效。  值为undefined时，分段按钮不支持多选。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| buttons | [SegmentButtonItemOptionsArray](ohos-arkui-advanced-segmentbutton.md#segmentbuttonitemoptionsarray) | 否 | 否 | 分段按钮组件的按钮信息，包括图标和文本信息。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| fontColor | [ResourceColor](ts-types.md#resourcecolor) | 否 | 否 | 分段按钮组件的按钮未选中态的文本颜色。  值为undefined时，颜色为$r('sys.color.ohos\_id\_color\_text\_secondary')。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| selectedFontColor | [ResourceColor](ts-types.md#resourcecolor) | 否 | 否 | 分段按钮组件的按钮选中态的文本颜色。  值为undefined时，type为"tab"时，颜色为$r('sys.color.ohos\_id\_color\_text\_primary')。  type为"capsule"时，颜色为$r('sys.color.ohos\_id\_color\_foreground\_contrary')。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| fontSize | [DimensionNoPercentage](ohos-arkui-advanced-segmentbutton.md#dimensionnopercentage) | 否 | 否 | 分段按钮组件的按钮未选中态的字体大小，不支持百分比设置。  值为undefined时，字体大小为$r('sys.float.ohos\_id\_text\_size\_body2')。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| selectedFontSize | [DimensionNoPercentage](ohos-arkui-advanced-segmentbutton.md#dimensionnopercentage) | 否 | 否 | 分段按钮组件的按钮选中态的字体大小，不支持百分比设置。  值为undefined时，字体大小为$r('sys.float.ohos\_id\_text\_size\_body2')。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| fontWeight | [FontWeight](ts-appendix-enums.md#fontweight) | 否 | 否 | 分段按钮组件的按钮未选中态的字体粗细。  值为undefined时，字体粗细为FontWeight.Regular。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| selectedFontWeight | [FontWeight](ts-appendix-enums.md#fontweight) | 否 | 否 | 分段按钮组件的按钮选中态的字体粗细。  值为undefined时，字体粗细为FontWeight.Medium。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| backgroundColor | [ResourceColor](ts-types.md#resourcecolor) | 否 | 否 | 分段按钮组件的背景板颜色。  值为undefined时，背景板颜色为$r('sys.color.ohos\_id\_color\_button\_normal')。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| selectedBackgroundColor | [ResourceColor](ts-types.md#resourcecolor) | 否 | 否 | 分段按钮组件的按钮选中态背景板颜色。  值为undefined时，type为"tab"时，背景板颜色为$r('sys.color.segment\_button\_checked\_foreground\_color')。  type为"capsule"时，背景板颜色为$r('sys.color.ohos\_id\_color\_emphasize')。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| imageSize | [SizeOptions](ts-types.md#sizeoptions) | 否 | 否 | 分段按钮组件的图片尺寸。  值为undefined时，图片尺寸为{ width: 24, height: 24 }。  单位：vp  **说明：**  imageSize属性对仅图标按钮和图标+文本按钮生效，对仅文字按钮无效果。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| buttonPadding | [Padding](ts-types.md#padding) | [Dimension](ts-types.md#dimension10) | 否 | 否 | 分段按钮组件的按钮内边距。  值为undefined时，仅图标按钮和仅文字按钮内边距：{ top: 4, right: 8, bottom: 4, left: 8 }  图标+文本按钮内边距：{ top: 6, right: 8, bottom: 6, left: 8 }  单位：vp  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| textPadding | [Padding](ts-types.md#padding) | [Dimension](ts-types.md#dimension10) | 否 | 否 | 分段按钮组件的文本内边距。  值为undefined时，文本内边距为0。  单位：vp  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| localizedButtonPadding12+ | [LocalizedPadding](ts-types.md#localizedpadding12) | 否 | 是 | 分段按钮组件的按钮内边距。  默认值：  仅图标按钮和仅文字按钮默认值：{ top: LengthMetrics.vp(4), end: LengthMetrics.vp(8), bottom: LengthMetrics.vp(4), start: LengthMetrics.vp(8) }  图标+文本按钮默认值：{ top: LengthMetrics.vp(6), end: LengthMetrics.vp(8), bottom: LengthMetrics.vp(6), start: LengthMetrics.vp(8) }  值为undefined时，按默认值处理。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| localizedTextPadding12+ | [LocalizedPadding](ts-types.md#localizedpadding12) | 否 | 是 | 文本内边距。  默认值：0  值为undefined时，按默认值处理。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| direction12+ | [Direction](ts-appendix-enums.md#direction) | 否 | 是 | 分段按钮组件的布局方向。  默认值：Direction.Auto  值为undefined时，按默认值处理。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| backgroundBlurStyle | [BlurStyle](ts-universal-attributes-background.md#blurstyle9) | 否 | 否 | 分段按钮组件的背景模糊材质。  值为undefined时，背景模糊材质为BlurStyle.NONE。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| borderRadiusMode20+ | [BorderRadiusMode](ohos-arkui-advanced-segmentbutton.md#borderradiusmode20) | 否 | 是 | 边框圆角模式，用于控制圆角计算方式。  默认值：BorderRadiusMode.DEFAULT  值为undefined时，按默认值处理。  **元服务API：** 从API version 20开始，该接口支持在元服务中使用。 |
| backgroundBorderRadius20+ | [LengthMetrics](js-apis-arkui-graphics.md#lengthmetrics12) | 否 | 是 | 分段按钮整体容器的边框圆角半径。  **说明：**  此属性仅在borderRadiusMode为BorderRadiusMode.CUSTOM时生效。  对于胶囊类多选按钮(type为"capsule"且multiply为true)，此属性不生效，需要用itemBorderRadius配置圆角。  圆角大小受组件尺寸限制，最大值为组件宽或高的一半，不支持百分比设置。  默认值：$r('sys.float.segmentbutton\_container\_shape')  值为undefined时，按默认值处理。  **元服务API：** 从API version 20开始，该接口支持在元服务中使用。 |
| itemBorderRadius20+ | [LengthMetrics](js-apis-arkui-graphics.md#lengthmetrics12) | 否 | 是 | 分段按钮中按钮项的边框圆角半径。  **说明：**  此属性仅在borderRadiusMode为BorderRadiusMode.CUSTOM时生效。  对于胶囊类多选按钮(type为"capsule"且multiply为true)，只能控制两端的选项圆角。  圆角大小受组件尺寸限制，最大值为组件宽或高的一半，不支持百分比设置。  默认值：$r('sys.float.segmentbutton\_selected\_background\_shape')  值为undefined时，按默认值处理。  **元服务API：** 从API version 20开始，该接口支持在元服务中使用。 |

### constructor

PhonePC/2in1TabletTVWearable

constructor(options: TabSegmentButtonOptions | CapsuleSegmentButtonOptions)

构造函数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

**参数**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [TabSegmentButtonOptions](ohos-arkui-advanced-segmentbutton.md#tabsegmentbuttonoptions) | [CapsuleSegmentButtonOptions](ohos-arkui-advanced-segmentbutton.md#capsulesegmentbuttonoptions) | 是 | 页签类或者胶囊类分段按钮信息。 |

### tab

PhonePC/2in1TabletTVWearable

static tab(options: TabSegmentButtonConstructionOptions): SegmentButtonOptions

创建SegmentButtonOptions类，用于定义页签。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

**参数**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [TabSegmentButtonConstructionOptions](ohos-arkui-advanced-segmentbutton.md#tabsegmentbuttonconstructionoptions) | 是 | 页签类分段按钮信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [SegmentButtonOptions](ohos-arkui-advanced-segmentbutton.md#segmentbuttonoptions) | 分段按钮选项。 |

### capsule

PhonePC/2in1TabletTVWearable

static capsule(options: CapsuleSegmentButtonConstructionOptions): SegmentButtonOptions

创建胶囊类的SegmentButtonOptions。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

**参数**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [CapsuleSegmentButtonConstructionOptions](ohos-arkui-advanced-segmentbutton.md#capsulesegmentbuttonconstructionoptions) | 是 | 胶囊类分段按钮信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [SegmentButtonOptions](ohos-arkui-advanced-segmentbutton.md#segmentbuttonoptions) | 分段按钮选项。 |

## DimensionNoPercentage

PhonePC/2in1TabletTVWearable

type DimensionNoPercentage = PX | VP | FP | LPX | Resource

不支持百分比类型的长度联合类型。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

| 类型 | 说明 |
| --- | --- |
| [PX](ts-types.md#px10) | 长度类型，用于描述以px为单位的长度。 |
| [VP](ts-types.md#vp10) | 长度类型，用于描述以vp为单位的长度。 |
| [FP](ts-types.md#fp10) | 长度类型，用于描述以fp为单位的长度。 |
| [LPX](ts-types.md#lpx10) | 长度类型，用于描述以lpx为单位的长度。 |
| [Resource](ts-types.md#resource) | 资源引用类型，用于设置组件属性的值。 |

## CommonSegmentButtonOptions

PhonePC/2in1TabletTVWearable

定义分段按钮组件的可自定义的属性。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| fontColor | [ResourceColor](ts-types.md#resourcecolor) | 否 | 是 | 按钮未选中态的文本颜色。  默认值：$r('sys.color.ohos\_id\_color\_text\_secondary')  值为undefined时，按默认值处理。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| selectedFontColor | [ResourceColor](ts-types.md#resourcecolor) | 否 | 是 | 按钮选中态的文本颜色。  默认值：  type为"tab"时，默认值为$r('sys.color.ohos\_id\_color\_text\_primary')。  type为"capsule"时，默认值为$r('sys.color.ohos\_id\_color\_foreground\_contrary')。  值为undefined时，按默认值处理。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| fontSize | [DimensionNoPercentage](ohos-arkui-advanced-segmentbutton.md#dimensionnopercentage) | 否 | 是 | 按钮未选中态的字体大小（不支持百分比设置）。  默认值：$r('sys.float.ohos\_id\_text\_size\_body2')  值为undefined时，按默认值处理。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| selectedFontSize | [DimensionNoPercentage](ohos-arkui-advanced-segmentbutton.md#dimensionnopercentage) | 否 | 是 | 按钮选中态的字体大小（不支持百分比设置）。  默认值：$r('sys.float.ohos\_id\_text\_size\_body2')  值为undefined时，按默认值处理。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| fontWeight | [FontWeight](ts-appendix-enums.md#fontweight) | 否 | 是 | 按钮未选中态的字体粗细。  默认值：FontWeight.Regular  值为undefined时，按默认值处理。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| selectedFontWeight | [FontWeight](ts-appendix-enums.md#fontweight) | 否 | 是 | 按钮选中态的字体粗细。  默认值：FontWeight.Medium  值为undefined时，按默认值处理。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| backgroundColor | [ResourceColor](ts-types.md#resourcecolor) | 否 | 是 | 背景板颜色。  默认值：$r('sys.color.ohos\_id\_color\_button\_normal')  值为undefined时，按默认值处理。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| selectedBackgroundColor | [ResourceColor](ts-types.md#resourcecolor) | 否 | 是 | 按钮选中态的背景板颜色。  默认值：  type为"tab"时，默认值为$r('sys.color.segment\_button\_checked\_foreground\_color')。  type为"capsule"时，默认值为$r('sys.color.ohos\_id\_color\_emphasize')。  值为undefined时，按默认值处理。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| imageSize | [SizeOptions](ts-types.md#sizeoptions) | 否 | 是 | 图片尺寸。  默认值：{ width: 24, height: 24 }  单位：vp  值为undefined时，按默认值处理。  **说明：**  imageSize属性仅对图标按钮和图标+文本按钮生效，对纯文本按钮无效果。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| buttonPadding | [Padding](ts-types.md#padding) | [Dimension](ts-types.md#dimension10) | 否 | 是 | 按钮内边距。  默认值：  仅图标按钮和仅文字按钮默认值：{ top: 4, right: 8, bottom: 4, left: 8 }  图标+文本按钮默认值：{ top: 6, right: 8, bottom: 6, left: 8 }  单位：vp  值为undefined时，按默认值处理。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| textPadding | [Padding](ts-types.md#padding) | [Dimension](ts-types.md#dimension10) | 否 | 是 | 文本内边距。  默认值：0  单位：vp  值为undefined时，按默认值处理。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| localizedButtonPadding12+ | [LocalizedPadding](ts-types.md#localizedpadding12) | 否 | 是 | 按钮内边距。  默认值：  仅图标按钮和仅文字按钮默认值：{ top: LengthMetrics.vp(4), end: LengthMetrics.vp(8), bottom: LengthMetrics.vp(4), start: LengthMetrics.vp(8) }  图标+文本按钮默认值：{ top: LengthMetrics.vp(6), end: LengthMetrics.vp(8), bottom: LengthMetrics.vp(6), start: LengthMetrics.vp(8) }  值为undefined时，按默认值处理。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| localizedTextPadding12+ | [LocalizedPadding](ts-types.md#localizedpadding12) | 否 | 是 | 文本内边距。  默认值：0  单位：vp  值为undefined时，按默认值处理。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| direction12+ | [Direction](ts-appendix-enums.md#direction) | 否 | 是 | 布局方向。  默认值：Direction.Auto  值为undefined时，按默认值处理。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| backgroundBlurStyle | [BlurStyle](ts-universal-attributes-background.md#blurstyle9) | 否 | 是 | 背景模糊材质。  默认值：BlurStyle.NONE  值为undefined时，按默认值处理。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| borderRadiusMode20+ | [BorderRadiusMode](ohos-arkui-advanced-segmentbutton.md#borderradiusmode20) | 否 | 是 | 边框圆角模式，用于控制圆角计算方式。  默认值：BorderRadiusMode.DEFAULT  值为undefined时，按默认值处理。  **元服务API：** 从API version 20开始，该接口支持在元服务中使用。 |
| backgroundBorderRadius20+ | [LengthMetrics](js-apis-arkui-graphics.md#lengthmetrics12) | 否 | 是 | 分段按钮整体容器的边框圆角半径。  **说明：**  此属性仅在borderRadiusMode为BorderRadiusMode.CUSTOM时生效。  对于胶囊类多选按钮(type为"capsule"且multiply为true)，此属性不生效，需要用itemBorderRadius配置圆角。  圆角大小受组件尺寸限制，最大值为组件宽或高的一半，不支持百分比设置。  默认值：$r('sys.float.segmentbutton\_container\_shape')  值为undefined时，按默认值处理。  **元服务API：** 从API version 20开始，该接口支持在元服务中使用。 |
| itemBorderRadius20+ | [LengthMetrics](js-apis-arkui-graphics.md#lengthmetrics12) | 否 | 是 | 分段按钮中按钮项的边框圆角半径。  **说明：**  此属性仅在borderRadiusMode为BorderRadiusMode.CUSTOM时生效。  对于胶囊类多选按钮(type为"capsule"且multiply为true)，只能控制两端的选项圆角。  圆角大小受组件尺寸限制，最大值为组件宽或高的一半，不支持百分比设置。  默认值：$r('sys.float.segmentbutton\_selected\_background\_shape')  值为undefined时，按默认值处理。  **元服务API：** 从API version 20开始，该接口支持在元服务中使用。 |

## BorderRadiusMode20+

PhonePC/2in1TabletTVWearable

边框圆角模式枚举，用于控制分段按钮的圆角计算方式。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

| 名称 | 值 | 说明 |
| --- | --- | --- |
| DEFAULT | 0 | 默认模式，框架自动计算边框圆角。 |
| CUSTOM | 1 | 自定义模式，开发者设置边框圆角。 |

## TabSegmentButtonConstructionOptions

PhonePC/2in1TabletTVWearable

构建页签类的SegmentButtonOptions对象。

继承[CommonSegmentButtonOptions](ohos-arkui-advanced-segmentbutton.md#commonsegmentbuttonoptions)。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| buttons | [ItemRestriction](ohos-arkui-advanced-segmentbutton.md#itemrestriction)<[SegmentButtonTextItem](ohos-arkui-advanced-segmentbutton.md#segmentbuttontextitem)> | 否 | 否 | 按钮信息。 |

## CapsuleSegmentButtonConstructionOptions

PhonePC/2in1TabletTVWearable

用于构建胶囊类的SegmentButtonOptions对象。

继承[CommonSegmentButtonOptions](ohos-arkui-advanced-segmentbutton.md#commonsegmentbuttonoptions)。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| buttons | [SegmentButtonItemTuple](ohos-arkui-advanced-segmentbutton.md#segmentbuttonitemtuple) | 否 | 否 | 按钮信息。 |
| multiply | boolean | 否 | 是 | 是否可以多选。  默认值：false  值为undefined时，按默认值处理。  true表示可以多选，false表示不可以多选。 |

## ItemRestriction

PhonePC/2in1TabletTVWearable

type ItemRestriction<T> = [T, T, T?, T?, T?]

保存按钮信息的元组类型。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

| 类型 | 说明 |
| --- | --- |
| [T, T, T?, T?, T?] | 表示包含2~5个相同类型元素的元组。 |

说明

分段按钮组件仅支持2到5个按钮。

## SegmentButtonItemTuple

PhonePC/2in1TabletTVWearable

type SegmentButtonItemTuple = ItemRestriction<SegmentButtonTextItem> | ItemRestriction<SegmentButtonIconItem> | ItemRestriction<SegmentButtonIconTextItem>

用于保存按钮信息的元组的联合类型。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

| 类型 | 说明 |
| --- | --- |
| [ItemRestriction](ohos-arkui-advanced-segmentbutton.md#itemrestriction)<[SegmentButtonTextItem](ohos-arkui-advanced-segmentbutton.md#segmentbuttontextitem)> | 仅文本按钮信息的元组。 |
| [ItemRestriction](ohos-arkui-advanced-segmentbutton.md#itemrestriction)<[SegmentButtonIconItem](ohos-arkui-advanced-segmentbutton.md#segmentbuttoniconitem)> | 仅图标按钮信息的元组。 |
| [ItemRestriction](ohos-arkui-advanced-segmentbutton.md#itemrestriction)<[SegmentButtonIconTextItem](ohos-arkui-advanced-segmentbutton.md#segmentbuttonicontextitem)> | 图标+文本按钮信息的元组。 |

## SegmentButtonItemArray

PhonePC/2in1TabletTVWearable

type SegmentButtonItemArray = Array<SegmentButtonTextItem> | Array<SegmentButtonIconItem> | Array<SegmentButtonIconTextItem>

用于保存按钮信息的数组的联合类型。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

| 类型 | 说明 |
| --- | --- |
| Array<[SegmentButtonTextItem](ohos-arkui-advanced-segmentbutton.md#segmentbuttontextitem)> | 仅文本按钮信息的数组。 |
| Array<[SegmentButtonIconItem](ohos-arkui-advanced-segmentbutton.md#segmentbuttoniconitem)> | 仅图标按钮信息的数组。 |
| Array<[SegmentButtonIconTextItem](ohos-arkui-advanced-segmentbutton.md#segmentbuttonicontextitem)> | 图标+文本按钮信息的数组。 |

## SegmentButtonItemOptionsArray

PhonePC/2in1TabletTVWearable

用于保存按钮信息的数组。

**装饰器类型：** @Observed

说明

SegmentButtonItemOptionsArray仅支持保存2到5个按钮信息元素。

### constructor

PhonePC/2in1TabletTVWearable

constructor(elements: SegmentButtonItemTuple)

构造函数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| elements | [SegmentButtonItemTuple](ohos-arkui-advanced-segmentbutton.md#segmentbuttonitemtuple) | 是 | 按钮信息。 |

### push

PhonePC/2in1TabletTVWearable

push(...items: SegmentButtonItemArray): number

在数组末尾添加新的元素，返回添加元素后数组的长度。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| items | [SegmentButtonItemArray](ohos-arkui-advanced-segmentbutton.md#segmentbuttonitemarray) | 否 | 被添加的按钮信息数组。  默认值：0个被添加的按钮信息数组。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 添加元素后数组的长度。 |

说明

分段按钮组件数组仅支持保存2到5个按钮信息，若超过分段按钮组件数量个数的限制，添加按钮信息元素失败。

### pop

PhonePC/2in1TabletTVWearable

pop(): SegmentButtonItemOptions | undefined

移除数组末尾最后一个元素，返回被移除的元素。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [SegmentButtonItemOptions](ohos-arkui-advanced-segmentbutton.md#segmentbuttonitemoptions) | undefined | 被移除的元素。 |

说明

分段按钮组件数组仅支持保存2到5个按钮信息，若移除后按钮组件数量不在个数限制范围内，移除按钮信息元素失败。

### shift

PhonePC/2in1TabletTVWearable

shift(): SegmentButtonItemOptions | undefined

移除数组开头第一个元素，返回被移除的元素。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [SegmentButtonItemOptions](ohos-arkui-advanced-segmentbutton.md#segmentbuttonitemoptions) | undefined | 被移除的元素。 |

说明

分段按钮组件数组仅支持保存2到5个按钮信息，若移除后按钮组件数量不在个数限制范围内，移除按钮信息元素失败。

### unshift

PhonePC/2in1TabletTVWearable

unshift(...items: SegmentButtonItemArray): number

在数组开头添加一个新的元素，返回添加元素后数组的长度。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| items | [SegmentButtonItemArray](ohos-arkui-advanced-segmentbutton.md#segmentbuttonitemarray) | 否 | 添加的按钮信息数组。  默认值：0个被添加的按钮信息数组。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 添加元素后数组的长度。 |

说明

分段按钮组件数组仅支持保存2到5个按钮信息，若超过分段按钮组件数量个数的限制，添加按钮信息元素失败。

### splice

PhonePC/2in1TabletTVWearable

splice(start: number, deleteCount: number, ...items: SegmentButtonItemOptions[]): SegmentButtonItemOptions[]

在数组中，删除从start位置开始的deleteCount数量的元素，并插入items中的元素，返回一个包含了被删除的元素的数组。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| start | number | 是 | 删除元素的起始位置。 |
| deleteCount | number | 是 | 删除元素的数量。 |
| items | [SegmentButtonItemOptions](ohos-arkui-advanced-segmentbutton.md#segmentbuttonitemoptions)[] | 否 | 从start开始要加入到数组中的元素。  默认值：不指定任何元素，将从数组中删除元素。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [SegmentButtonItemOptions](ohos-arkui-advanced-segmentbutton.md#segmentbuttonitemoptions)[] | 返回包含了被删除的元素的数组。 |

说明

分段按钮组件数组仅保存2到5个按钮信息，若超过分段按钮组件数量个数的限制，不再删除和替换按钮信息元素。

### create

PhonePC/2in1TabletTVWearable

static create(elements: SegmentButtonItemTuple): SegmentButtonItemOptionsArray

创建一个SegmentButtonItemOptionsArray对象。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| elements | [SegmentButtonItemTuple](ohos-arkui-advanced-segmentbutton.md#segmentbuttonitemtuple) | 是 | 按钮信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [SegmentButtonItemOptionsArray](ohos-arkui-advanced-segmentbutton.md#segmentbuttonitemoptionsarray) | 返回创建的SegmentButtonItemOptionsArray对象。 |

## TabSegmentButtonOptions

PhonePC/2in1TabletTVWearable

页签类分段按钮选项。继承自[TabSegmentButtonConstructionOptions](ohos-arkui-advanced-segmentbutton.md#tabsegmentbuttonconstructionoptions)。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| type | "tab" | 否 | 否 | 类型为页签类分段按钮。 |

## CapsuleSegmentButtonOptions

PhonePC/2in1TabletTVWearable

胶囊类分段按钮选项。继承自[CapsuleSegmentButtonConstructionOptions](ohos-arkui-advanced-segmentbutton.md#capsulesegmentbuttonconstructionoptions)。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| type | "capsule" | 否 | 否 | 类型为胶囊类分段按钮。 |

## SegmentButtonTextItem

PhonePC/2in1TabletTVWearable

文本按钮信息。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| text | [ResourceStr](ts-types.md#resourcestr) | 否 | 否 | 按钮文本。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| accessibilityLevel13+ | string | 否 | 是 | 无障碍重要性，控制当前组件是否可被无障碍辅助服务识别。  支持的值为:  "auto"：当前组件可被无障碍辅助服务所识别。  "yes"：当前组件可被无障碍辅助服务所识别。  "no"：当前组件不可被无障碍辅助服务所识别。  "no-hide-descendants"：当前组件及其所有子组件不可被无障碍辅助服务所识别。  默认值："auto"  值为undefined时，按默认值处理。  **元服务API：** 从API version 13开始，该接口支持在元服务中使用。 |
| accessibilityDescription13+ | [ResourceStr](ts-types.md#resourcestr) | 否 | 是 | 无障碍说明，为用户解释组件操作，设置详细解释文本，帮助用户理解操作后果。若组件有文本和无障碍说明，选中时先播报文本，再播报无障碍说明。  默认值：空字符串。  值为undefined时，按默认值处理。  **元服务API：** 从API version 13开始，该接口支持在元服务中使用。 |

## SegmentButtonIconItem

PhonePC/2in1TabletTVWearable

图标按钮信息。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| icon | [ResourceStr](ts-types.md#resourcestr) | 否 | 否 | 未选中态的按钮图标。  值为undefined时，不显示图标。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| iconAccessibilityText13+ | [ResourceStr](ts-types.md#resourcestr) | 否 | 是 | 未选中态按钮图标的无障碍文本。  默认值：空字符串。  值为undefined时，按默认值处理。  **元服务API：** 从API version 13开始，该接口支持在元服务中使用。 |
| selectedIcon | [ResourceStr](ts-types.md#resourcestr) | 否 | 否 | 选中态的按钮图标。  值为undefined时，不显示图标。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| selectedIconAccessibilityText13+ | [ResourceStr](ts-types.md#resourcestr) | 否 | 是 | 选中态按钮图标的无障碍文本。  默认值：空字符串。  值为undefined时，按默认值处理。  **元服务API：** 从API version 13开始，该接口支持在元服务中使用。 |
| accessibilityLevel13+ | string | 否 | 是 | 无障碍重要性，用于控制当前组件是否可被无障碍辅助服务所识别。  支持的值为:  "auto"：当前组件可被无障碍辅助服务所识别。  "yes"：当前组件可被无障碍辅助服务所识别。  "no"：当前组件不可被无障碍辅助服务所识别。  "no-hide-descendants"：当前组件及其所有子组件不可被无障碍辅助服务所识别。  默认值："auto"  值为undefined时，按默认值处理。  **元服务API：** 从API version 13开始，该接口支持在元服务中使用。 |
| accessibilityDescription13+ | [ResourceStr](ts-types.md#resourcestr) | 否 | 是 | 无障碍说明，用于为用户进一步说明当前组件，开发人员可为组件的该属性设置相对较详细的解释文本，帮助用户理解将要执行的操作。如帮助用户理解将要执行的操作可能导致什么后果，尤其是当这些后果无法从组件本身属性与无障碍文本中了解到时。若组件既拥有文本属性又拥有无障碍说明属性，则组件被选中时，先播报组件的文本属性，再播报无障碍说明属性的内容。  默认值：空字符串。  值为undefined时，按默认值处理。  **元服务API：** 从API version 13开始，该接口支持在元服务中使用。 |

说明

未选中态的图标icon和选中态的图标selectedIcon都需设置，单独设置无效。

## SegmentButtonIconTextItem

PhonePC/2in1TabletTVWearable

图标与文本按钮信息。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| icon | [ResourceStr](ts-types.md#resourcestr) | 否 | 否 | 未选中态的按钮图标。  值为undefined时，不显示图标。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| iconAccessibilityText13+ | [ResourceStr](ts-types.md#resourcestr) | 否 | 是 | 未选中态按钮图标的无障碍文本。  默认值：空字符串。  值为undefined时，按默认值处理。  **元服务API：** 从API version 13开始，该接口支持在元服务中使用。 |
| selectedIcon | [ResourceStr](ts-types.md#resourcestr) | 否 | 否 | 选中态的按钮图标。  值为undefined时，不显示图标。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| selectedIconAccessibilityText13+ | [ResourceStr](ts-types.md#resourcestr) | 否 | 是 | 选中态按钮图标的无障碍文本。  默认值：空字符串。  值为undefined时，按默认值处理。  **元服务API：** 从API version 13开始，该接口支持在元服务中使用。 |
| text | [ResourceStr](ts-types.md#resourcestr) | 否 | 否 | 按钮文本。  值为undefined时，不显示文本内容。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| accessibilityLevel13+ | string | 否 | 是 | 无障碍重要性，用于控制当前组件是否可被无障碍辅助服务所识别。  支持的值为:  "auto"：当前组件可被无障碍辅助服务所识别。  "yes"：当前组件可被无障碍辅助服务所识别。  "no"：当前组件不可被无障碍辅助服务所识别。  "no-hide-descendants"：当前组件及其所有子组件不可被无障碍辅助服务所识别。  默认值："auto"  值为undefined时，按默认值处理。  **元服务API：** 从API version 13开始，该接口支持在元服务中使用。 |
| accessibilityDescription13+ | [ResourceStr](ts-types.md#resourcestr) | 否 | 是 | 无障碍说明，用于为用户进一步说明当前组件，开发人员可为组件的该属性设置相对较详细的解释文本，帮助用户理解将要执行的操作。如帮助用户理解将要执行的操作可能导致什么后果，尤其是当这些后果无法从组件本身属性与无障碍文本中了解到时。若组件既拥有文本属性又拥有无障碍说明属性，则组件被选中时，先播报组件的文本属性，再播报无障碍说明属性的内容。  默认值：空字符串。  值为undefined时，按默认值处理。  **元服务API：** 从API version 13开始，该接口支持在元服务中使用。 |

说明

未选中态的图标icon和选中态的图标selectedIcon都需设置，单独设置无效。

## SegmentButtonItemOptions

PhonePC/2in1TabletTVWearable

分段按钮中的按钮选项。

**装饰器类型：** @Observed

### 属性

PhonePC/2in1TabletTVWearable

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| icon | [ResourceStr](ts-types.md#resourcestr) | 否 | 是 | 未选中态的按钮图标。  默认值：不显示未选中态的按钮图标。  值为undefined时，按默认值处理。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| iconAccessibilityText13+ | [ResourceStr](ts-types.md#resourcestr) | 否 | 是 | 未选中态按钮图标的无障碍文本。  默认值：空字符串。  值为undefined时，按默认值处理。  **元服务API：** 从API version 13开始，该接口支持在元服务中使用。 |
| selectedIcon | [ResourceStr](ts-types.md#resourcestr) | 否 | 是 | 选中态的按钮图标。  默认值：不显示选中态按钮图标。  值为undefined时，按默认值处理。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| selectedIconAccessibilityText13+ | [ResourceStr](ts-types.md#resourcestr) | 否 | 是 | 选中态按钮图标的无障碍文本。  默认值：空字符串。  值为undefined时，按默认值处理。  **元服务API：** 从API version 13开始，该接口支持在元服务中使用。 |
| text | [ResourceStr](ts-types.md#resourcestr) | 否 | 是 | 按钮文本。  默认值：空字符串。  值为undefined时，按默认值处理。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| accessibilityLevel13+ | string | 否 | 是 | 无障碍重要性，用于控制当前组件是否可被无障碍辅助服务所识别。  支持的值为:  "auto"：当前组件可被无障碍辅助服务所识别。  "yes"：当前组件可被无障碍辅助服务所识别。  "no"：当前组件不可被无障碍辅助服务所识别。  "no-hide-descendants"：当前组件及其所有子组件不可被无障碍辅助服务所识别。  默认值："auto"  值为undefined时，按默认值处理。  **元服务API：** 从API version 13开始，该接口支持在元服务中使用。 |
| accessibilityDescription13+ | [ResourceStr](ts-types.md#resourcestr) | 否 | 是 | 无障碍说明，用于为用户进一步说明当前组件，开发人员可为组件的该属性设置相对较详细的解释文本，帮助用户理解将要执行的操作。如帮助用户理解将要执行的操作可能导致什么后果，尤其是当这些后果无法从组件本身属性与无障碍文本中了解到时。若组件既拥有文本属性又拥有无障碍说明属性，则组件被选中时，先播报组件的文本属性，再播报无障碍说明属性的内容。  默认值：空字符串。  值为undefined时，按默认值处理。  **元服务API：** 从API version 13开始，该接口支持在元服务中使用。 |

### constructor

PhonePC/2in1TabletTVWearable

constructor(options: SegmentButtonItemOptionsConstructorOptions)

构造函数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [SegmentButtonItemOptionsConstructorOptions](ohos-arkui-advanced-segmentbutton.md#segmentbuttonitemoptionsconstructoroptions) | 是 | 单个分段按钮的配置选项，包含图标、文本、无障碍属性等配置信息。 |

## SegmentButtonItemOptionsConstructorOptions

PhonePC/2in1TabletTVWearable

构造参数用于SegmentButtonItemOptions。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| icon | [ResourceStr](ts-types.md#resourcestr) | 否 | 是 | 未选中态的按钮图标。  默认值：不显示未选中态的按钮图标。  值为undefined时，按默认值处理。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| iconAccessibilityText13+ | [ResourceStr](ts-types.md#resourcestr) | 否 | 是 | 未选中态按钮图标的无障碍文本。  默认值：空字符串。  值为undefined时，按默认值处理。  **元服务API：** 从API version 13开始，该接口支持在元服务中使用。 |
| selectedIcon | [ResourceStr](ts-types.md#resourcestr) | 否 | 是 | 选中态的按钮图标。  默认值：不显示选中态的按钮图标。  值为undefined时，按默认值处理。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| selectedIconAccessibilityText13+ | [ResourceStr](ts-types.md#resourcestr) | 否 | 是 | 选中态按钮图标的无障碍文本。  默认值：空字符串。  值为undefined时，按默认值处理。  **元服务API：** 从API version 13开始，该接口支持在元服务中使用。 |
| text | [ResourceStr](ts-types.md#resourcestr) | 否 | 是 | 按钮文本。  默认值：空字符串。  值为undefined时，按默认值处理。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| accessibilityLevel13+ | string | 否 | 是 | 无障碍重要性，用于控制当前组件是否可被无障碍辅助服务所识别。  支持的值为:  "auto"：当前组件可被无障碍辅助服务所识别。  "yes"：当前组件可被无障碍辅助服务所识别。  "no"：当前组件不可被无障碍辅助服务所识别。  "no-hide-descendants"：当前组件及其所有子组件不可被无障碍辅助服务所识别。  默认值："auto"  值为undefined时，按默认值处理。  **元服务API：** 从API version 13开始，该接口支持在元服务中使用。 |
| accessibilityDescription13+ | [ResourceStr](ts-types.md#resourcestr) | 否 | 是 | 无障碍说明，用于为用户进一步说明当前组件，开发人员可为组件的该属性设置相对较详细的解释文本，帮助用户理解将要执行的操作。如帮助用户理解将要执行的操作可能导致什么后果，尤其是当这些后果无法从组件本身属性与无障碍文本中了解到时。若组件既拥有文本属性又拥有无障碍说明属性，则组件被选中时，先播报组件的文本属性，再播报无障碍说明属性的内容。  默认值：空字符串。  值为undefined时，按默认值处理。  **元服务API：** 从API version 13开始，该接口支持在元服务中使用。 |

## 示例

PhonePC/2in1TabletTVWearable

### 示例1（设置分段按钮的类型）

通过配置SegmentButtonOptions的tab和capsule，创建两种不同类型的分段按钮。

```
1. import {
2. ItemRestriction,
3. SegmentButton,
4. SegmentButtonItemTuple,
5. SegmentButtonOptions,
6. SegmentButtonTextItem
7. } from '@kit.ArkUI';

9. @Entry
10. @Component
11. struct Index {
12. // 页签类分段按钮数组。
13. @State tabOptions: SegmentButtonOptions = SegmentButtonOptions.tab({
14. buttons: [{ text: '页签按钮1' }, { text: '页签按钮2' }, {
15. text: '页签按钮3'
16. }] as ItemRestriction<SegmentButtonTextItem>,
17. // 配置CommonSegmentButtonOptions，实现背景模糊样式。
18. backgroundBlurStyle: BlurStyle.BACKGROUND_THICK
19. });
20. // 胶囊类分段按钮数组。
21. @State singleSelectCapsuleOptions: SegmentButtonOptions = SegmentButtonOptions.capsule({
22. buttons: [{ text: '单选按钮1' }, { text: '单选按钮2' }, { text: '单选按钮3' }] as SegmentButtonItemTuple,
23. multiply: false,
24. // 配置CommonSegmentButtonOptions，实现背景模糊样式。
25. backgroundBlurStyle: BlurStyle.BACKGROUND_THICK
26. });
27. // 可多选胶囊类分段按钮数组。
28. @State multiplySelectCapsuleOptions: SegmentButtonOptions = SegmentButtonOptions.capsule({
29. buttons: [{ text: '多选按钮1' }, { text: '多选按钮2' }, { text: '多选按钮3' }] as SegmentButtonItemTuple,
30. multiply: true
31. });
32. // 胶囊类分段按钮带选中非选中图标数组。
33. @State iconCapsuleOptions: SegmentButtonOptions = SegmentButtonOptions.capsule({
34. buttons: [
35. { icon: $r('sys.media.ohos_ic_public_email'), selectedIcon: $r('sys.media.ohos_ic_public_clock') },
36. { icon: $r('sys.media.ohos_ic_public_email'), selectedIcon: $r('sys.media.ohos_ic_public_clock') },
37. { icon: $r('sys.media.ohos_ic_public_email'), selectedIcon: $r('sys.media.ohos_ic_public_clock') },
38. { icon: $r('sys.media.ohos_ic_public_email'), selectedIcon: $r('sys.media.ohos_ic_public_clock') }
39. ] as SegmentButtonItemTuple,
40. multiply: false,
41. // 配置CommonSegmentButtonOptions，实现背景模糊样式。
42. backgroundBlurStyle: BlurStyle.BACKGROUND_THICK
43. });
44. // 可多选胶囊类分段按钮带选中非选中图标数组。
45. @State iconTextCapsuleOptions: SegmentButtonOptions = SegmentButtonOptions.capsule({
46. buttons: [
47. { text: '图标1', icon: $r('sys.media.ohos_ic_public_email'), selectedIcon: $r('sys.media.ohos_ic_public_clock') },
48. { text: '图标2', icon: $r('sys.media.ohos_ic_public_email'), selectedIcon: $r('sys.media.ohos_ic_public_clock') },
49. { text: '图标3', icon: $r('sys.media.ohos_ic_public_email'), selectedIcon: $r('sys.media.ohos_ic_public_clock') },
50. { text: '图标4', icon: $r('sys.media.ohos_ic_public_email'), selectedIcon: $r('sys.media.ohos_ic_public_clock') },
51. { text: '图标5', icon: $r('sys.media.ohos_ic_public_email'), selectedIcon: $r('sys.media.ohos_ic_public_clock') }
52. ] as SegmentButtonItemTuple,
53. multiply: true
54. });
55. @State tabSelectedIndexes: number[] = [1];
56. @State singleSelectCapsuleSelectedIndexes: number[] = [0];
57. @State multiplySelectCapsuleSelectedIndexes: number[] = [0, 1];
58. @State singleSelectIconCapsuleSelectedIndexes: number[] = [3];
59. @State multiplySelectIconTextCapsuleSelectedIndexes: number[] = [1, 2];

61. build() {
62. Row() {
63. Column() {
64. Column({ space: 25 }) {
65. SegmentButton({
66. options: this.tabOptions,
67. selectedIndexes: $tabSelectedIndexes
68. })
69. SegmentButton({
70. options: this.singleSelectCapsuleOptions,
71. selectedIndexes: $singleSelectCapsuleSelectedIndexes
72. })
73. SegmentButton({
74. options: this.multiplySelectCapsuleOptions,
75. selectedIndexes: $multiplySelectCapsuleSelectedIndexes
76. })
77. SegmentButton({
78. options: this.iconCapsuleOptions,
79. selectedIndexes: $singleSelectIconCapsuleSelectedIndexes
80. })
81. SegmentButton({
82. options: this.iconTextCapsuleOptions,
83. selectedIndexes: $multiplySelectIconTextCapsuleSelectedIndexes
84. })
85. }.width('90%')
86. }.width('100%')
87. }.height('100%')
88. }
89. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/55/v3/cPH-8l7dSRKcKyfSqIKrVg/zh-cn_image_0000002558606988.png?HW-CC-KV=V1&HW-CC-Date=20260429T055301Z&HW-CC-Expire=86400&HW-CC-Sign=95EC0FCBDE10316608B81005A70318742B6F9E3769132D8DED01594896364141)

### 示例2（设置分段按钮样式）

通过配置CommonSegmentButtonOptions，实现自定义分段按钮的文本以及背板样式。

```
1. import {
2. ItemRestriction,
3. SegmentButton,
4. SegmentButtonItemTuple,
5. SegmentButtonOptions,
6. SegmentButtonTextItem
7. } from '@kit.ArkUI';

9. @Entry
10. @Component
11. struct Index {
12. @State tabOptions: SegmentButtonOptions = SegmentButtonOptions.tab({
13. buttons: [{ text: '页签按钮1' }, { text: '页签按钮2' }, {
14. text: '页签按钮3'
15. }] as ItemRestriction<SegmentButtonTextItem>,
16. backgroundColor: 'rgb(213,213,213)',
17. selectedBackgroundColor: 'rgb(112,112,112)', // 配置CommonSegmentButtonOptions，实现选中背景色
18. textPadding: {
19. top: 10,
20. right: 10,
21. bottom: 10,
22. left: 10
23. }, // 配置CommonSegmentButtonOptions，实现文字内边距
24. });
25. @State singleSelectCapsuleOptions: SegmentButtonOptions = SegmentButtonOptions.capsule({
26. buttons: [{ text: '单选按钮1' }, { text: '单选按钮2' }, { text: '单选按钮3' }] as SegmentButtonItemTuple,
27. multiply: false,
28. fontColor: 'rgb(0,74,175)', // 配置CommonSegmentButtonOptions，实现文字颜色
29. selectedFontColor: 'rgb(247,247,247)', // 配置CommonSegmentButtonOptions，实现选中文字颜色
30. backgroundBlurStyle: BlurStyle.BACKGROUND_THICK // 配置CommonSegmentButtonOptions，实现背景模糊样式
31. });
32. @State multiplySelectCapsuleOptions: SegmentButtonOptions = SegmentButtonOptions.capsule({
33. buttons: [{ text: '多选按钮1' }, { text: '多选按钮2' }, { text: '多选按钮3' }] as SegmentButtonItemTuple,
34. multiply: true,
35. fontSize: 18,
36. selectedFontSize: 18,
37. fontWeight: FontWeight.Bolder, // 配置CommonSegmentButtonOptions，实现文字粗细
38. selectedFontWeight: FontWeight.Lighter, // 配置CommonSegmentButtonOptions，实现选中文字粗细
39. });
40. @State iconCapsuleOptions: SegmentButtonOptions = SegmentButtonOptions.capsule({
41. buttons: [
42. { icon: $r('sys.media.ohos_ic_public_email'), selectedIcon: $r('sys.media.ohos_ic_public_clock') },
43. { icon: $r('sys.media.ohos_ic_public_email'), selectedIcon: $r('sys.media.ohos_ic_public_clock') },
44. { icon: $r('sys.media.ohos_ic_public_email'), selectedIcon: $r('sys.media.ohos_ic_public_clock') },
45. { icon: $r('sys.media.ohos_ic_public_email'), selectedIcon: $r('sys.media.ohos_ic_public_clock') }
46. ] as SegmentButtonItemTuple,
47. multiply: false,
48. imageSize: { width: 40, height: 40 },
49. buttonPadding: {
50. top: 6,
51. right: 10,
52. bottom: 6,
53. left: 10
54. },
55. backgroundBlurStyle: BlurStyle.BACKGROUND_THICK
56. });
57. @State iconTextCapsuleOptions: SegmentButtonOptions = SegmentButtonOptions.capsule({
58. buttons: [
59. { text: '图标1', icon: $r('sys.media.ohos_ic_public_email'), selectedIcon: $r('sys.media.ohos_ic_public_clock') },
60. { text: '图标2', icon: $r('sys.media.ohos_ic_public_email'), selectedIcon: $r('sys.media.ohos_ic_public_clock') },
61. { text: '图标3', icon: $r('sys.media.ohos_ic_public_email'), selectedIcon: $r('sys.media.ohos_ic_public_clock') },
62. { text: '图标4', icon: $r('sys.media.ohos_ic_public_email'), selectedIcon: $r('sys.media.ohos_ic_public_clock') },
63. { text: '图标5', icon: $r('sys.media.ohos_ic_public_email'), selectedIcon: $r('sys.media.ohos_ic_public_clock') }
64. ] as SegmentButtonItemTuple,
65. multiply: true,
66. imageSize: { width: 10, height: 10 },
67. });
68. @State tabSelectedIndexes: number[] = [0];
69. @State singleSelectCapsuleSelectedIndexes: number[] = [0];
70. @State multiplySelectCapsuleSelectedIndexes: number[] = [0, 1];
71. @State singleSelectIconCapsuleSelectedIndexes: number[] = [3];
72. @State multiplySelectIconTextCapsuleSelectedIndexes: number[] = [1, 2];

74. build() {
75. Row() {
76. Column() {
77. Column({ space: 20 }) {
78. SegmentButton({ options: this.tabOptions, selectedIndexes: $tabSelectedIndexes })
79. SegmentButton({
80. options: this.singleSelectCapsuleOptions,
81. selectedIndexes: $singleSelectCapsuleSelectedIndexes
82. })
83. SegmentButton({
84. options: this.multiplySelectCapsuleOptions,
85. selectedIndexes: $multiplySelectCapsuleSelectedIndexes
86. })
87. SegmentButton({
88. options: this.iconCapsuleOptions,
89. selectedIndexes: $singleSelectIconCapsuleSelectedIndexes
90. })
91. SegmentButton({
92. options: this.iconTextCapsuleOptions,
93. selectedIndexes: $multiplySelectIconTextCapsuleSelectedIndexes
94. })
95. }.width('90%')
96. }.width('100%')
97. }.height('100%')
98. }
99. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d3/v3/PNt6tA0CTf6mdibyXn2QxQ/zh-cn_image_0000002589326515.png?HW-CC-KV=V1&HW-CC-Date=20260429T055301Z&HW-CC-Expire=86400&HW-CC-Sign=3068D9984E3DC50AD502EA0F383D3D59D5A4FD46D99F1DF7E4BE0DF568EB917F)

### 示例3（分段按钮数组处理）

该示例通过pop、shift、unshift等函数实现分段按钮数组的添加、移除等操作。

```
1. import {
2. SegmentButton,
3. SegmentButtonOptions,
4. SegmentButtonItemOptionsArray,
5. SegmentButtonItemTuple,
6. SegmentButtonItemOptions
7. } from '@kit.ArkUI';

9. @Entry
10. @Component
11. struct Index {
12. // 胶囊类分段按钮数组。
13. @State singleSelectCapsuleOptions: SegmentButtonOptions = SegmentButtonOptions.capsule({
14. buttons: [{ text: '1' }, { text: '2' }, { text: '3' },
15. { text: '4' }, { text: '5' }] as SegmentButtonItemTuple,
16. multiply: false,
17. // 配置CommonSegmentButtonOptions，实现背景模糊样式。
18. backgroundBlurStyle: BlurStyle.BACKGROUND_THICK
19. });
20. @State capsuleSelectedIndexes: number[] = [0];

22. build() {
23. Row() {
24. Column() {
25. Column({ space: 10 }) {
26. SegmentButton({
27. options: this.singleSelectCapsuleOptions,
28. selectedIndexes: $capsuleSelectedIndexes
29. })
30. // 点击’删除第一个按钮‘，第一个按钮会删除。
31. Button('删除第一个按钮')
32. .onClick(() => {
33. this.singleSelectCapsuleOptions.buttons.shift()
34. })
35. // 点击’删除最后一个按钮‘，最后一个按钮会删除。
36. Button('删除最后一个按钮')
37. .onClick(() => {
38. this.singleSelectCapsuleOptions.buttons.pop()
39. })
40. // 点击’末尾增加一个按钮push‘，在按钮末尾会增加一个按钮。
41. Button('末尾增加一个按钮push')
42. .onClick(() => {
43. this.singleSelectCapsuleOptions.buttons.push({ text: 'push' })
44. })
45. // 点击’开头增加一个按钮unshift‘，在按钮开头会增加一个按钮。
46. Button('开头增加一个按钮unshift')
47. .onClick(() => {
48. this.singleSelectCapsuleOptions.buttons.unshift(({ text: 'unshift' }))
49. })
50. // 点击’将按钮2、3替换为splice1、splice2‘，按钮2、3会被替换成splice1、splice2。
51. Button('将按钮2、3替换为splice1、splice2')
52. .onClick(() => {
53. this.singleSelectCapsuleOptions.buttons.splice(1, 2, new SegmentButtonItemOptions({
54. text: 'splice1'
55. }), new SegmentButtonItemOptions({ text: 'splice2' }))
56. })
57. // 点击’更改所有按钮文字‘，按钮会由1、2、3、4、5替换成a、b、c、d、e。
58. Button('更改所有按钮文字')
59. .onClick(() => {
60. this.singleSelectCapsuleOptions.buttons =
61. SegmentButtonItemOptionsArray.create([{ text: 'a' }, { text: 'b' },
62. { text: 'c' }, { text: 'd' }, { text: 'e' }])
63. })
64. }.width('90%')
65. }.width('100%')
66. }.height('100%')
67. }
68. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/44/v3/-EnJ7AQYQC-OrP1xBUOYiQ/zh-cn_image_0000002589246457.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055301Z&HW-CC-Expire=86400&HW-CC-Sign=A40F4A5C8E341F816E905B4E4BFEC38AB12F51C5A861ACB5050707F230A233A5)

### 示例4（设置镜像效果）

该示例通过配置direction属性设置分段按钮的布局方向，实现镜像效果。

```
1. import { LengthMetrics, SegmentButton, SegmentButtonOptions } from '@kit.ArkUI';

3. @Entry
4. @Component
5. struct Index {
6. // 页签类分段按钮数组。
7. @State tabOptions: SegmentButtonOptions = SegmentButtonOptions.tab({
8. buttons: [{ text: '页签按钮1' }, { text: '页签按钮2' }, {
9. text: '页签按钮3'
10. }],
11. direction: Direction.Rtl, // 设置分段按钮的布局方向。
12. backgroundColor: Color.Green, // 设置分段按钮的背景板颜色。
13. selectedBackgroundColor: Color.Orange, // 设置分段按钮组件的按钮选中态背景板颜色。
14. // 设置文本内边距。
15. localizedTextPadding: {
16. end: LengthMetrics.vp(10),
17. start: LengthMetrics.vp(10)
18. },
19. });
20. // 胶囊类分段按钮数组。
21. @State singleSelectCapsuleOptions: SegmentButtonOptions = SegmentButtonOptions.capsule({
22. buttons: [{ text: '单选按钮1' }, { text: '单选按钮2' }, { text: '单选按钮3' }],
23. multiply: false, // 设置分段按钮组件是否可以多选。
24. direction: Direction.Rtl, // 设置分段按钮的布局方向。
25. fontColor: Color.Black, // 设置分段按钮组件的按钮未选中态的文本颜色。
26. selectedFontColor: Color.Yellow, // 设置分段按钮组件的按钮选中态的文本颜色。
27. backgroundBlurStyle: BlurStyle.BACKGROUND_THICK // 设置分段按钮组件的背景模糊材质。
28. });
29. // 胶囊类分段按钮数组。
30. @State multiplySelectCapsuleOptions: SegmentButtonOptions = SegmentButtonOptions.capsule({
31. buttons: [{ text: '多选按钮1' }, { text: '多选按钮2' }, { text: '多选按钮3' }],
32. multiply: true, // 设置分段按钮组件是否可以多选。
33. direction: Direction.Rtl, // 设置分段按钮的布局方向。
34. fontSize: 18, // 设置分段按钮组件的按钮未选中态的字体大小。
35. selectedFontSize: 18, // 设置分段按钮组件的按钮选中态的字体大小。
36. fontWeight: FontWeight.Bolder, // 设置分段按钮组件的按钮未选中态的字体粗细。
37. selectedFontWeight: FontWeight.Lighter, // 设置分段按钮组件的按钮选中态的字体粗细。
38. });
39. // 胶囊类分段按钮数组。
40. @State iconCapsuleOptions: SegmentButtonOptions = SegmentButtonOptions.capsule({
41. buttons: [
42. { icon: $r('sys.media.ohos_ic_public_email'), selectedIcon: $r('sys.media.ohos_ic_public_clock') },
43. { icon: $r('sys.media.ohos_ic_public_email'), selectedIcon: $r('sys.media.ohos_ic_public_clock') },
44. { icon: $r('sys.media.ohos_ic_public_email'), selectedIcon: $r('sys.media.ohos_ic_public_clock') },
45. { icon: $r('sys.media.ohos_ic_public_email'), selectedIcon: $r('sys.media.ohos_ic_public_clock') },
46. { icon: $r('sys.media.ohos_ic_public_email'), selectedIcon: $r('sys.media.ohos_ic_public_clock') }
47. ],
48. multiply: false, // 设置分段按钮组件是否可以多选。
49. direction: Direction.Rtl, // 设置分段按钮的布局方向。
50. imageSize: { width: 40, height: 40 }, // 设置分段按钮组件的图片尺寸。
51. // 设置分段按钮组件的按钮内边距。
52. localizedButtonPadding: {
53. end: LengthMetrics.vp(10),
54. start: LengthMetrics.vp(10)
55. },
56. backgroundBlurStyle: BlurStyle.BACKGROUND_THICK // 设置分段按钮组件的背景模糊材质。
57. });
58. @State iconTextCapsuleOptions: SegmentButtonOptions = SegmentButtonOptions.capsule({
59. buttons: [
60. { text: '图标1', icon: $r('sys.media.ohos_ic_public_email'), selectedIcon: $r('sys.media.ohos_ic_public_clock') },
61. { text: '图标2', icon: $r('sys.media.ohos_ic_public_email'), selectedIcon: $r('sys.media.ohos_ic_public_clock') },
62. { text: '图标3', icon: $r('sys.media.ohos_ic_public_email'), selectedIcon: $r('sys.media.ohos_ic_public_clock') },
63. { text: '图标4', icon: $r('sys.media.ohos_ic_public_email'), selectedIcon: $r('sys.media.ohos_ic_public_clock') },
64. { text: '图标5', icon: $r('sys.media.ohos_ic_public_email'), selectedIcon: $r('sys.media.ohos_ic_public_clock') }
65. ],
66. multiply: true, // 设置分段按钮组件是否可以多选。
67. direction: Direction.Rtl, // 设置分段按钮的布局方向。
68. imageSize: { width: 10, height: 10 }, // 设置分段按钮组件的图片尺寸。
69. });
70. @State tabSelectedIndexes: number[] = [0];
71. @State singleSelectCapsuleSelectedIndexes: number[] = [0];
72. @State multiplySelectCapsuleSelectedIndexes: number[] = [0, 1];
73. @State singleSelectIconCapsuleSelectedIndexes: number[] = [3];
74. @State multiplySelectIconTextCapsuleSelectedIndexes: number[] = [1, 2];

76. build() {
77. Row() {
78. Column() {
79. Column({ space: 20 }) {
80. SegmentButton({ options: this.tabOptions, selectedIndexes: $tabSelectedIndexes })
81. SegmentButton({
82. options: this.singleSelectCapsuleOptions,
83. selectedIndexes: $singleSelectCapsuleSelectedIndexes
84. })
85. SegmentButton({
86. options: this.multiplySelectCapsuleOptions,
87. selectedIndexes: $multiplySelectCapsuleSelectedIndexes
88. })
89. SegmentButton({
90. options: this.iconCapsuleOptions,
91. selectedIndexes: $singleSelectIconCapsuleSelectedIndexes
92. })
93. SegmentButton({
94. options: this.iconTextCapsuleOptions,
95. selectedIndexes: $multiplySelectIconTextCapsuleSelectedIndexes
96. })
97. }.width('90%')
98. }.width('100%')
99. }.height('100%')
100. }
101. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/83/v3/kXrvnSiHT46cngbxSQyTxQ/zh-cn_image_0000002558766650.png?HW-CC-KV=V1&HW-CC-Date=20260429T055301Z&HW-CC-Expire=86400&HW-CC-Sign=E325CDC9E329E5443642E2DC8B5B33AAD3D7D3413DBD98144C4C0993CFC20CA5)

### 示例5（设置无障碍朗读）

通过配置accessibilityLevel和selectedIconAccessibilityText等属性，实现了分段按钮的无障碍朗读功能。

```
1. import {
2. ItemRestriction,
3. SegmentButton,
4. SegmentButtonItemTuple,
5. SegmentButtonOptions,
6. SegmentButtonTextItem,
7. SegmentButtonItemOptions
8. } from '@kit.ArkUI';

10. @Entry
11. @Component
12. struct Index {
13. @State tabOptions: SegmentButtonOptions = SegmentButtonOptions.tab({
14. buttons: [{ text: '页签按钮1', accessibilityLevel: 'yes', accessibilityDescription: '页签按钮1 新手提醒' },
15. { text: '页签按钮2', accessibilityLevel: 'yes', accessibilityDescription: '页签按钮2 新手提醒' },
16. {
17. text: '页签按钮3', accessibilityLevel: 'yes', accessibilityDescription: '页签按钮3 新手提醒'
18. }] as ItemRestriction<SegmentButtonTextItem>,
19. backgroundBlurStyle: BlurStyle.BACKGROUND_THICK
20. });
21. @State iconCapsuleOptions: SegmentButtonOptions = SegmentButtonOptions.capsule({
22. buttons: [
23. {
24. icon: $r('sys.media.ohos_ic_public_email'),
25. iconAccessibilityText: '未选中图标无障碍文本', // 未选中态按钮图标的无障碍文本。
26. selectedIcon: $r('sys.media.ohos_ic_public_clock'),
27. selectedIconAccessibilityText: '选中图标无障碍文本', // 选中态按钮图标的无障碍文本。
28. accessibilityLevel: 'yes', // 无障碍重要性，控制当前组件是否可被无障碍辅助服务识别。
29. accessibilityDescription: 'SegmentButtonIconItem 新手提醒' // 无障碍说明。
30. },
31. {
32. icon: $r('sys.media.ohos_ic_public_email'),
33. iconAccessibilityText: '未选中图标无障碍文本', // 未选中态按钮图标的无障碍文本。
34. selectedIcon: $r('sys.media.ohos_ic_public_clock'),
35. selectedIconAccessibilityText: '选中图标无障碍文本', // 选中态按钮图标的无障碍文本。
36. accessibilityLevel: 'yes', // 无障碍重要性，控制当前组件是否可被无障碍辅助服务识别。
37. accessibilityDescription: 'SegmentButtonIconItem 新手提醒' // 无障碍说明。
38. },
39. {
40. icon: $r('sys.media.ohos_ic_public_email'),
41. iconAccessibilityText: '未选中图标无障碍文本', // 未选中态按钮图标的无障碍文本。
42. selectedIcon: $r('sys.media.ohos_ic_public_clock'),
43. selectedIconAccessibilityText: '选中图标无障碍文本', // 选中态按钮图标的无障碍文本。
44. accessibilityLevel: 'yes', // 无障碍重要性，控制当前组件是否可被无障碍辅助服务识别。
45. accessibilityDescription: 'SegmentButtonIconItem 新手提醒' // 无障碍说明。
46. },
47. {
48. icon: $r('sys.media.ohos_ic_public_email'),
49. iconAccessibilityText: '未选中图标无障碍文本', // 未选中态按钮图标的无障碍文本。
50. selectedIcon: $r('sys.media.ohos_ic_public_clock'),
51. selectedIconAccessibilityText: '选中图标无障碍文本', // 选中态按钮图标的无障碍文本。
52. accessibilityLevel: 'yes', // 无障碍重要性，控制当前组件是否可被无障碍辅助服务识别。
53. accessibilityDescription: 'SegmentButtonIconItem 新手提醒' // 无障碍说明。
54. }
55. ] as SegmentButtonItemTuple,
56. multiply: false,
57. backgroundBlurStyle: BlurStyle.BACKGROUND_THICK
58. });
59. @State iconTextCapsuleOptions: SegmentButtonOptions = SegmentButtonOptions.capsule({
60. buttons: [
61. {
62. text: '图标1',
63. icon: $r('sys.media.ohos_ic_public_email'),
64. iconAccessibilityText: '未选中图标无障碍文本', // 未选中态按钮图标的无障碍文本。
65. selectedIcon: $r('sys.media.ohos_ic_public_clock'),
66. selectedIconAccessibilityText: '选中图标无障碍文本', // 选中态按钮图标的无障碍文本。
67. accessibilityLevel: 'yes', // 无障碍重要性，控制当前组件是否可被无障碍辅助服务识别。
68. accessibilityDescription: 'SegmentButtonIconTextItem 新手提醒' // 无障碍说明。
69. },
70. {
71. text: '图标1',
72. icon: $r('sys.media.ohos_ic_public_email'),
73. iconAccessibilityText: '未选中图标无障碍文本', // 未选中态按钮图标的无障碍文本。
74. selectedIcon: $r('sys.media.ohos_ic_public_clock'),
75. selectedIconAccessibilityText: '选中图标无障碍文本', // 选中态按钮图标的无障碍文本。
76. accessibilityLevel: 'yes', // 无障碍重要性，控制当前组件是否可被无障碍辅助服务识别。
77. accessibilityDescription: 'SegmentButtonIconTextItem 新手提醒' // 无障碍说明。
78. },
79. {
80. text: '图标1',
81. icon: $r('sys.media.ohos_ic_public_email'),
82. iconAccessibilityText: '未选中图标无障碍文本', // 未选中态按钮图标的无障碍文本。
83. selectedIcon: $r('sys.media.ohos_ic_public_clock'),
84. selectedIconAccessibilityText: '选中图标无障碍文本', // 选中态按钮图标的无障碍文本。
85. accessibilityLevel: 'yes', // 无障碍重要性，控制当前组件是否可被无障碍辅助服务识别。
86. accessibilityDescription: 'SegmentButtonIconTextItem 新手提醒' // 无障碍说明。
87. },
88. {
89. text: '图标1',
90. icon: $r('sys.media.ohos_ic_public_email'),
91. iconAccessibilityText: '未选中图标无障碍文本', // 未选中态按钮图标的无障碍文本。
92. selectedIcon: $r('sys.media.ohos_ic_public_clock'),
93. selectedIconAccessibilityText: '选中图标无障碍文本', // 选中态按钮图标的无障碍文本。
94. accessibilityLevel: 'yes', // 无障碍重要性，控制当前组件是否可被无障碍辅助服务识别。
95. accessibilityDescription: 'SegmentButtonIconTextItem 新手提醒' // 无障碍说明。
96. }
97. ] as SegmentButtonItemTuple,
98. multiply: true
99. });
100. @State tabSelectedIndexes: number[] = [1];
101. @State singleSelectIconCapsuleSelectedIndexes: number[] = [3];
102. @State multiplySelectIconTextCapsuleSelectedIndexes: number[] = [1, 2];

104. build() {
105. Row() {
106. Column() {
107. Column({ space: 25 }) {
108. SegmentButton({
109. options: this.tabOptions,
110. selectedIndexes: $tabSelectedIndexes
111. })
112. SegmentButton({
113. options: this.iconCapsuleOptions,
114. selectedIndexes: $singleSelectIconCapsuleSelectedIndexes
115. })
116. SegmentButton({
117. options: this.iconTextCapsuleOptions,
118. selectedIndexes: $multiplySelectIconTextCapsuleSelectedIndexes
119. })
120. Button('将按钮2、3替换为splice1、splice2')
121. .onClick(() => {
122. this.iconTextCapsuleOptions.buttons.splice(1, 2, new SegmentButtonItemOptions({
123. text: 'splice1', accessibilityLevel: 'yes', accessibilityDescription: 'SegmentButtonItemOptions 新手提醒'
124. }), new SegmentButtonItemOptions({
125. text: 'splice2',
126. icon: $r('sys.media.ohos_ic_public_email'),
127. iconAccessibilityText: '未选中图标无障碍文本', // 未选中态按钮图标的无障碍文本。
128. selectedIcon: $r('sys.media.ohos_ic_public_clock'),
129. selectedIconAccessibilityText: '选中图标无障碍文本', // 选中态按钮图标的无障碍文本。
130. accessibilityLevel: 'yes', // 无障碍重要性，控制当前组件是否可被无障碍辅助服务识别。
131. accessibilityDescription: 'SegmentButtonIconTextItem 新手提醒' // 无障碍说明。
132. }))
133. })
134. }.width('90%')
135. }.width('100%')
136. }.height('100%')
137. }
138. }
```

### 示例6（设置自定义圆角）

该示例演示了如何为分段按钮组件设置自定义的边框圆角半径。

```
1. import {
2. BorderRadiusMode,
3. ItemRestriction,
4. LengthMetrics,
5. SegmentButton,
6. SegmentButtonOptions,
7. SegmentButtonTextItem
8. } from '@kit.ArkUI';

10. @Entry
11. @Component
12. struct Index {
13. @State tabOptions: SegmentButtonOptions = SegmentButtonOptions.tab({
14. buttons: [{ text: '页签按钮1' }, { text: '页签按钮2' }, {
15. text: '页签按钮3'
16. }] as ItemRestriction<SegmentButtonTextItem>,
17. backgroundBlurStyle: BlurStyle.BACKGROUND_THICK,
18. borderRadiusMode: BorderRadiusMode.CUSTOM, // 设置自定义的边框圆角半径
19. backgroundBorderRadius: LengthMetrics.vp(8),
20. itemBorderRadius: LengthMetrics.vp(6)
21. });
22. @State tabSelectedIndexes: number[] = [1];

24. build() {
25. Row() {
26. Column() {
27. Column({ space: 25 }) {
28. SegmentButton({
29. options: this.tabOptions,
30. selectedIndexes: $tabSelectedIndexes,
31. })
32. }.width('90%')
33. }.width('100%')
34. }.height('100%')
35. }
36. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/90/v3/N_2TY8LARQmthc2KIq90wg/zh-cn_image_0000002558606990.png?HW-CC-KV=V1&HW-CC-Date=20260429T055301Z&HW-CC-Expire=86400&HW-CC-Sign=21C6C8B74D6FD0D06A0083E35A39C1E1FE7C072ED78116B203AFB8662C1DE64F)
