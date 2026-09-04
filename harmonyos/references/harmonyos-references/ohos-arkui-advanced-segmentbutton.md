---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-segmentbutton
title: SegmentButton
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 系统预置UI组件库 > SegmentButton
category: harmonyos-references
scraped_at: 2026-09-05T06:17:31+08:00
doc_updated_at: 2026-09-01
content_hash: sha256:07e076e54582bb45b8f10a1f8f5a58963d41e906af91f13834e6f3d5f10e67da
---

分段按钮组件包含页签类分段按钮和胶囊类分段按钮。页签类分段按钮适用于页面或内容区域的切换场景；胶囊类分段按钮适用于单选或多选的选择场景，包含胶囊类单选分段按钮和胶囊类多选分段按钮。该组件支持自定义文本颜色、字体大小、字体粗细、背景色、图片尺寸、内边距、背景模糊材质等外观属性，支持仅文本、仅图标和图标+文本三种按钮样式，并提供无障碍朗读、布局方向镜像、自定义圆角、属性动画等能力，适用于需要快速构建符合设计规范的分段选择界面的场景。

**说明** 

* 该组件从API version 11开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。
* 本模块接口仅可在Stage模型下使用。

## 导入模块

```ts
import { SegmentButton, SegmentButtonOptions, SegmentButtonItemOptionsArray } from '@kit.ArkUI';
```

## 子组件

无

## 属性

不支持[通用属性](ts-component-general-attributes.md)。

## 事件

不支持[通用事件](ts-component-general-events.md)。

## SegmentButton

SegmentButton({ options: SegmentButtonOptions, selectedIndexes: number[], onItemClicked?: Callback<number>, maxFontScale: number | Resource, enableStateAnimation: boolean })

**装饰器类型：**@Component

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

**说明** 

* 分段按钮不支持[通用属性](ts-component-general-attributes.md)。分段按钮使用当前区域可使用的最大宽度作为组件宽度，并且根据按钮个数平均分配每个按钮宽度；分段按钮高度根据按钮内容（文本及图片）自动适应，其最小高度为28vp。
* @Prop装饰的属性为可选参数，仅当与@Require装饰器联合使用时，才必须在构造时传入对应参数。

| 名称 | 类型 | 必填 | 装饰器类型 | 说明 |
| --- | --- | --- | --- | --- |
| options | [SegmentButtonOptions](ohos-arkui-advanced-segmentbutton.md#segmentbuttonoptions) | 是 | @ObjectLink | 分段按钮的配置选项，用于设置按钮的类型（页签类或胶囊类）、外观样式（颜色、字体、尺寸等）、按钮内容和选中状态等属性。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| selectedIndexes | number[] | 是 | @Link | 分段按钮的选中项编号，第一项的编号为0，之后顺序增加。  **说明：**  selectedIndexes使用[@Link装饰器：父子双向同步](../harmonyos-guides/arkts-link.md)，仅支持有效的按钮编号（第一个按钮编号为0，之后按顺序累加，最大编号为按钮数量减1），传入无效编号时该编号不生效。如没有选中项可传入空数组[]。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| onItemClicked13+ | Callback<number> | 否 | - | 当分段按钮选项被点击时，触发的回调函数接收被点击的选项下标作为参数。若不传入此参数，则点击时不触发回调。  **元服务API：** 从API version 13开始，该接口支持在元服务中使用。 |
| maxFontScale14+ | number | [Resource](ts-types.md#resource) | 否 | @Prop | 分段按钮选项文字的最大字体放大倍数，用于限制字体缩放上限。当需要控制字体放大倍数以适应特定UI布局或避免文字过大时传入此参数。  取值范围：[1, 2]  当设置的值小于1时，按值为1处理，设置的值大于2时，按值为2处理。  默认值：1  **元服务API：** 从API version 14开始，该接口支持在元服务中使用。 |
| enableStateAnimation24+ | boolean | 否 | @Prop | 设置当通过变量修改selectedIndexes值时，是否开启分段按钮的属性动画。  true表示开启分段按钮的属性动画；false表示不开启分段按钮的属性动画。  默认值：false  **元服务API：** 从API version 24开始，该接口支持在元服务中使用。  **模型约束：** 此接口仅可在Stage模型下使用。 |

## SegmentButtonOptions

**说明** 

不支持设置字体类型。

分段按钮选项类用于提供初始数据和自定义属性。

**装饰器类型：** @Observed

### 属性

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| type | "tab" | "capsule" | 否 | 否 | 分段按钮组件的类型。  **说明：**  "tab"：页签类分段按钮，适用于页面或内容区域的切换场景。  "capsule"：胶囊类分段按钮，适用于单选或多选的选择场景。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| multiply | boolean | 否 | 否 | 分段按钮组件是否可以多选。  true：可多选；false：不可多选。  页签类分段按钮（type为"tab"）时，multiply强制为false，设置true不生效。  默认值： false  值为undefined时，按默认值处理。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| buttons | [SegmentButtonItemOptionsArray](ohos-arkui-advanced-segmentbutton.md#segmentbuttonitemoptionsarray) | 否 | 否 | 分段按钮组件的按钮信息，包括图标和文本信息。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| fontColor | [ResourceColor](ts-types.md#resourcecolor) | 否 | 否 | 分段按钮组件的按钮未选中态的文本颜色。  值为undefined时，颜色为$r('sys.color.ohos\_id\_color\_text\_secondary')。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| selectedFontColor | [ResourceColor](ts-types.md#resourcecolor) | 否 | 否 | 分段按钮组件的按钮选中态的文本颜色。  值为undefined时，type为"tab"时，颜色为$r('sys.color.ohos\_id\_color\_text\_primary')。  type为"capsule"时，颜色为$r('sys.color.ohos\_id\_color\_foreground\_contrary')。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| fontSize | [DimensionNoPercentage](ohos-arkui-advanced-segmentbutton.md#dimensionnopercentage) | 否 | 否 | 分段按钮组件的按钮未选中态的字体大小，不支持百分比设置。  单位：fp  值为undefined时，字体大小为$r('sys.float.ohos\_id\_text\_size\_body2')。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| selectedFontSize | [DimensionNoPercentage](ohos-arkui-advanced-segmentbutton.md#dimensionnopercentage) | 否 | 否 | 分段按钮组件的按钮选中态的字体大小，不支持百分比设置。  单位：fp  值为undefined时，字体大小为$r('sys.float.ohos\_id\_text\_size\_body2')。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| fontWeight | [FontWeight](ts-appendix-enums.md#fontweight) | 否 | 否 | 分段按钮组件的按钮未选中态的字体粗细。  值为undefined时，字体粗细为FontWeight.Regular。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| selectedFontWeight | [FontWeight](ts-appendix-enums.md#fontweight) | 否 | 否 | 分段按钮组件的按钮选中态的字体粗细。  值为undefined时，字体粗细为FontWeight.Medium。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| backgroundColor | [ResourceColor](ts-types.md#resourcecolor) | 否 | 否 | 分段按钮组件的背景板颜色。  值为undefined时，背景板颜色为$r('sys.color.ohos\_id\_color\_button\_normal')。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| selectedBackgroundColor | [ResourceColor](ts-types.md#resourcecolor) | 否 | 否 | 分段按钮组件的按钮选中态背景板颜色。  值为undefined时，type为"tab"时，背景板颜色为$r('sys.color.segment\_button\_checked\_foreground\_color')。  type为"capsule"时，背景板颜色为$r('sys.color.ohos\_id\_color\_emphasize')。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| imageSize | [SizeOptions](ts-types.md#sizeoptions) | 否 | 否 | 分段按钮组件的图片尺寸。  值为undefined时，图片尺寸为{ width: 24, height: 24 }。  单位：vp  **说明：**  imageSize属性对仅图标按钮和图标+文本按钮生效，对纯文本按钮无效果。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| buttonPadding | [Padding](ts-types.md#padding) | [Dimension](ts-types.md#dimension10) | 否 | 否 | 分段按钮组件的按钮内边距。  值为undefined时，仅图标按钮和仅文字按钮内边距：{ top: 4, right: 8, bottom: 4, left: 8 }  图标+文本按钮内边距：{ top: 6, right: 8, bottom: 6, left: 8 }  单位：vp  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| textPadding | [Padding](ts-types.md#padding) | [Dimension](ts-types.md#dimension10) | 否 | 否 | 分段按钮组件的文本内边距。  值为undefined时，文本内边距为0。  单位：vp  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| localizedButtonPadding12+ | [LocalizedPadding](ts-types.md#localizedpadding12) | 否 | 是 | 分段按钮组件的按钮内边距，支持随布局方向（LTR/RTL）自适应。  默认值：  仅图标按钮和仅文字按钮默认值：{ top: LengthMetrics.vp(4), end: LengthMetrics.vp(8), bottom: LengthMetrics.vp(4), start: LengthMetrics.vp(8) }  图标+文本按钮默认值：{ top: LengthMetrics.vp(6), end: LengthMetrics.vp(8), bottom: LengthMetrics.vp(6), start: LengthMetrics.vp(8) }  值为undefined时，按默认值处理。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| localizedTextPadding12+ | [LocalizedPadding](ts-types.md#localizedpadding12) | 否 | 是 | 文本内边距，支持随布局方向（LTR/RTL）自适应。  默认值：0  单位：vp  值为undefined时，按默认值处理。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| direction12+ | [Direction](ts-appendix-enums.md#direction) | 否 | 是 | 分段按钮组件的布局方向。  默认值：Direction.Auto  值为undefined时，按默认值处理。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| backgroundBlurStyle | [BlurStyle](ts-universal-attributes-background.md#blurstyle9) | 否 | 否 | 分段按钮组件的背景模糊材质。  默认值：BlurStyle.NONE  值为undefined时，按默认值处理。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| borderRadiusMode20+ | [BorderRadiusMode](ohos-arkui-advanced-segmentbutton.md#borderradiusmode20) | 否 | 是 | 边框圆角模式，用于控制圆角计算方式。  默认值：BorderRadiusMode.DEFAULT  值为undefined时，按默认值处理。  **元服务API：** 从API version 20开始，该接口支持在元服务中使用。 |
| backgroundBorderRadius20+ | [LengthMetrics](js-apis-arkui-graphics.md#lengthmetrics12) | 否 | 是 | 分段按钮整体容器的边框圆角半径。  **说明：**  此属性仅在borderRadiusMode为BorderRadiusMode.CUSTOM时生效。  对于胶囊类多选分段按钮（type为"capsule"且multiply为true），此属性不生效，需要用itemBorderRadius配置圆角。  圆角大小受组件尺寸限制，最大值为组件宽或高的一半，不支持百分比设置。超出最大值时自动修正为最大值，使用百分比时按默认值处理。  默认值：$r('sys.float.segmentbutton\_container\_shape')  值为undefined时，按默认值处理。  **元服务API：** 从API version 20开始，该接口支持在元服务中使用。 |
| itemBorderRadius20+ | [LengthMetrics](js-apis-arkui-graphics.md#lengthmetrics12) | 否 | 是 | 分段按钮中按钮项的边框圆角半径。  **说明：**  此属性仅在borderRadiusMode为BorderRadiusMode.CUSTOM时生效。  对于胶囊类多选分段按钮（type为"capsule"且multiply为true），只能控制两端的选项圆角。  圆角大小受组件尺寸限制，最大值为组件宽或高的一半，不支持百分比设置。超出最大值时自动修正为最大值，使用百分比时按默认值处理。  默认值：$r('sys.float.segmentbutton\_selected\_background\_shape')  值为undefined时，按默认值处理。  **元服务API：** 从API version 20开始，该接口支持在元服务中使用。 |
| backgroundSystemMaterial | [uiMaterial.Material](arkts-apis-uimaterial.md#material) | 否 | 是 | 分段按钮组件的背景板的系统材质。需要将组件放置在Navigation或NavDestination的标题栏子树，或横向Tabs的底部TabBar子树中，材质效果才会生效。不同系统材质具有不同的属性，产生不同的效果。传入材质后，SegmentButton的动效发生改变。  对于胶囊类多选分段按钮（即type为"capsule"且multiply为true），该属性不生效。  默认值：无材质效果。  **起始版本：** 26.0.0  **元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。  **模型约束：** 此接口仅可在Stage模型下使用。 |

**说明** 

从API版本26.0.0开始，除胶囊类多选按钮（即type为"capsule"且multiply为true）外，backgroundSystemMaterial设置自动反色的系统材质时，fontColor和selectedFontColor使用支持反色的特殊系统资源，颜色自动适配到材质背景色的反色。

### constructor

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
| [SegmentButtonOptions](ohos-arkui-advanced-segmentbutton.md#segmentbuttonoptions) | 分段按钮选项，用于定义页签类分段按钮。 |

### capsule

static capsule(options: CapsuleSegmentButtonConstructionOptions): SegmentButtonOptions

创建胶囊类的SegmentButtonOptions，用于定义胶囊类分段按钮。

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
| [SegmentButtonOptions](ohos-arkui-advanced-segmentbutton.md#segmentbuttonoptions) | 分段按钮选项，用于定义胶囊类分段按钮。 |

## DimensionNoPercentage

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

定义分段按钮组件的可自定义的属性。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| fontColor | [ResourceColor](ts-types.md#resourcecolor) | 否 | 是 | 按钮未选中态的文本颜色。  默认值：$r('sys.color.ohos\_id\_color\_text\_secondary')  值为undefined时，按默认值处理。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| selectedFontColor | [ResourceColor](ts-types.md#resourcecolor) | 否 | 是 | 按钮选中态的文本颜色。  默认值：  type为"tab"时，默认值为$r('sys.color.ohos\_id\_color\_text\_primary')。  type为"capsule"时，默认值为$r('sys.color.ohos\_id\_color\_foreground\_contrary')。  值为undefined时，按默认值处理。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| fontSize | [DimensionNoPercentage](ohos-arkui-advanced-segmentbutton.md#dimensionnopercentage) | 否 | 是 | 按钮未选中态的字体大小（不支持百分比设置）。  默认值：$r('sys.float.ohos\_id\_text\_size\_body2')  单位：fp  值为undefined时，按默认值处理。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| selectedFontSize | [DimensionNoPercentage](ohos-arkui-advanced-segmentbutton.md#dimensionnopercentage) | 否 | 是 | 按钮选中态的字体大小（不支持百分比设置）。  默认值：$r('sys.float.ohos\_id\_text\_size\_body2')  单位：fp  值为undefined时，按默认值处理。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| fontWeight | [FontWeight](ts-appendix-enums.md#fontweight) | 否 | 是 | 按钮未选中态的字体粗细。  默认值：FontWeight.Regular  值为undefined时，按默认值处理。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| selectedFontWeight | [FontWeight](ts-appendix-enums.md#fontweight) | 否 | 是 | 按钮选中态的字体粗细。  默认值：FontWeight.Medium  值为undefined时，按默认值处理。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| backgroundColor | [ResourceColor](ts-types.md#resourcecolor) | 否 | 是 | 背景板颜色。  默认值：$r('sys.color.ohos\_id\_color\_button\_normal')  值为undefined时，按默认值处理。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| selectedBackgroundColor | [ResourceColor](ts-types.md#resourcecolor) | 否 | 是 | 按钮选中态的背景板颜色。  默认值：  type为"tab"时，默认值为$r('sys.color.segment\_button\_checked\_foreground\_color')。  type为"capsule"时，默认值为$r('sys.color.ohos\_id\_color\_emphasize')。  值为undefined时，按默认值处理。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| imageSize | [SizeOptions](ts-types.md#sizeoptions) | 否 | 是 | 图片尺寸。  默认值：{ width: 24, height: 24 }  单位：vp  值为undefined时，按默认值处理。  **说明：**  imageSize属性仅对图标按钮和图标+文本按钮生效，对纯文本按钮无效果。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| buttonPadding | [Padding](ts-types.md#padding) | [Dimension](ts-types.md#dimension10) | 否 | 是 | 按钮内边距。  默认值：  仅图标按钮和仅文字按钮默认值：{ top: 4, right: 8, bottom: 4, left: 8 }  图标+文本按钮默认值：{ top: 6, right: 8, bottom: 6, left: 8 }  单位：vp  值为undefined时，按默认值处理。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| textPadding | [Padding](ts-types.md#padding) | [Dimension](ts-types.md#dimension10) | 否 | 是 | 文本内边距。  默认值：0  单位：vp  值为undefined时，按默认值处理。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| localizedButtonPadding12+ | [LocalizedPadding](ts-types.md#localizedpadding12) | 否 | 是 | 按钮内边距，支持随布局方向（LTR/RTL）自适应。  默认值：  仅图标按钮和仅文字按钮默认值：{ top: LengthMetrics.vp(4), end: LengthMetrics.vp(8), bottom: LengthMetrics.vp(4), start: LengthMetrics.vp(8) }  图标+文本按钮默认值：{ top: LengthMetrics.vp(6), end: LengthMetrics.vp(8), bottom: LengthMetrics.vp(6), start: LengthMetrics.vp(8) }  值为undefined时，按默认值处理。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| localizedTextPadding12+ | [LocalizedPadding](ts-types.md#localizedpadding12) | 否 | 是 | 文本内边距，支持随布局方向（LTR/RTL）自适应。  默认值：0  单位：vp  值为undefined时，按默认值处理。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| direction12+ | [Direction](ts-appendix-enums.md#direction) | 否 | 是 | 布局方向。  默认值：Direction.Auto  值为undefined时，按默认值处理。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| backgroundBlurStyle | [BlurStyle](ts-universal-attributes-background.md#blurstyle9) | 否 | 是 | 背景模糊材质。  默认值：BlurStyle.NONE  值为undefined时，按默认值处理。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| borderRadiusMode20+ | [BorderRadiusMode](ohos-arkui-advanced-segmentbutton.md#borderradiusmode20) | 否 | 是 | 边框圆角模式，用于控制圆角计算方式。  默认值：BorderRadiusMode.DEFAULT  值为undefined时，按默认值处理。  **元服务API：** 从API version 20开始，该接口支持在元服务中使用。 |
| backgroundBorderRadius20+ | [LengthMetrics](js-apis-arkui-graphics.md#lengthmetrics12) | 否 | 是 | 分段按钮整体容器的边框圆角半径。  **说明：**  此属性仅在borderRadiusMode为BorderRadiusMode.CUSTOM时生效。  对于胶囊类多选分段按钮（type为"capsule"且multiply为true），此属性不生效，需要用itemBorderRadius配置圆角。  圆角大小受组件尺寸限制，最大值为组件宽或高的一半，不支持百分比设置。超出最大值时自动修正为最大值，使用百分比时按默认值处理。  默认值：$r('sys.float.segmentbutton\_container\_shape')  值为undefined时，按默认值处理。  **元服务API：** 从API version 20开始，该接口支持在元服务中使用。 |
| itemBorderRadius20+ | [LengthMetrics](js-apis-arkui-graphics.md#lengthmetrics12) | 否 | 是 | 分段按钮中按钮项的边框圆角半径。  **说明：**  此属性仅在borderRadiusMode为BorderRadiusMode.CUSTOM时生效。  对于胶囊类多选分段按钮（type为"capsule"且multiply为true），只能控制两端的选项圆角。  圆角大小受组件尺寸限制，最大值为组件宽或高的一半，不支持百分比设置。超出最大值时自动修正为最大值，使用百分比时按默认值处理。  默认值：$r('sys.float.segmentbutton\_selected\_background\_shape')  值为undefined时，按默认值处理。  **元服务API：** 从API version 20开始，该接口支持在元服务中使用。 |
| backgroundSystemMaterial | [uiMaterial.Material](arkts-apis-uimaterial.md#material) | 否 | 是 | 分段按钮组件的背景板的系统材质。需要将组件放置在Navigation或NavDestination的标题栏子树，或横向Tabs的底部TabBar子树中，材质效果才会生效。不同系统材质具有不同的属性，产生不同的效果。传入材质后，SegmentButton的动效发生改变。  对于胶囊类多选分段按钮（即type为"capsule"且multiply为true），该属性不生效。  默认值：无材质效果。  从API版本26.0.0开始，除胶囊类多选分段按钮（即type为"capsule"且multiply为true）外，backgroundSystemMaterial设置自动反色的系统材质时，fontColor和selectedFontColor使用支持反色的特殊系统资源，颜色自动适配到材质背景色的反色。  **起始版本：** 26.0.0  **元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。  **模型约束：** 此接口仅可在Stage模型下使用。 |

## BorderRadiusMode20+

边框圆角模式枚举，用于控制分段按钮的圆角计算方式。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

| 名称 | 值 | 说明 |
| --- | --- | --- |
| DEFAULT | 0 | 默认模式，框架自动计算边框圆角。 |
| CUSTOM | 1 | 自定义模式，开发者设置边框圆角。 |

## TabSegmentButtonConstructionOptions

构建页签类的SegmentButtonOptions对象。

继承[CommonSegmentButtonOptions](ohos-arkui-advanced-segmentbutton.md#commonsegmentbuttonoptions)。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| buttons | [ItemRestriction](ohos-arkui-advanced-segmentbutton.md#itemrestriction)<[SegmentButtonTextItem](ohos-arkui-advanced-segmentbutton.md#segmentbuttontextitem)> | 否 | 否 | 按钮信息。 |

## CapsuleSegmentButtonConstructionOptions

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

type ItemRestriction<T> = [T, T, T?, T?, T?]

保存按钮信息的元组类型。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

| 类型 | 说明 |
| --- | --- |
| [T, T, T?, T?, T?] | 表示包含2~5个相同类型元素的元组。 |

**说明** 

分段按钮组件仅支持2到5个按钮。

## SegmentButtonItemTuple

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

用于保存按钮信息的数组。

**装饰器类型：** @Observed

**说明** 

SegmentButtonItemOptionsArray仅支持保存2到5个按钮信息元素。

### constructor

constructor(elements: SegmentButtonItemTuple)

构造函数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| elements | [SegmentButtonItemTuple](ohos-arkui-advanced-segmentbutton.md#segmentbuttonitemtuple) | 是 | 用于初始化数组的按钮信息元组，包含2到5个按钮选项元素，每个元素定义一个按钮的图标、文本等属性。 |

**说明** 

SegmentButtonItemOptionsArray仅支持保存2到5个按钮信息元素。

### push

push(...items: SegmentButtonItemArray): number

在数组末尾添加新的元素，返回添加元素后数组的长度。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| items | [SegmentButtonItemArray](ohos-arkui-advanced-segmentbutton.md#segmentbuttonitemarray) | 否 | 被添加的按钮信息数组。  默认值：不传入任何按钮信息元素。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 添加元素后数组的长度。 |

**说明** 

分段按钮组件数组仅支持保存2到5个按钮信息。当传入的元素数量导致数组超过5个，操作不执行并返回当前数组的长度。

### pop

pop(): SegmentButtonItemOptions | undefined

移除数组末尾最后一个元素，返回被移除的元素。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [SegmentButtonItemOptions](ohos-arkui-advanced-segmentbutton.md#segmentbuttonitemoptions) | undefined | 被移除的元素。 |

**说明** 

分段按钮组件数组仅支持保存2到5个按钮信息。若移除后按钮数量少于2个，操作不执行并返回undefined，数组保持不变。

### shift

shift(): SegmentButtonItemOptions | undefined

移除数组开头第一个元素，返回被移除的元素。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [SegmentButtonItemOptions](ohos-arkui-advanced-segmentbutton.md#segmentbuttonitemoptions) | undefined | 被移除的元素。 |

**说明** 

分段按钮组件数组仅支持保存2到5个按钮信息。若移除后按钮数量少于2个，操作不执行并返回undefined，数组保持不变。

### unshift

unshift(...items: SegmentButtonItemArray): number

在数组开头添加新的元素，返回添加元素后数组的长度。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| items | [SegmentButtonItemArray](ohos-arkui-advanced-segmentbutton.md#segmentbuttonitemarray) | 否 | 添加的按钮信息数组。  默认值：不传入任何按钮信息元素。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 添加元素后数组的长度。 |

**说明** 

分段按钮组件数组仅支持保存2到5个按钮信息。当传入的元素数量导致数组超过5个，操作不执行并返回当前数组的长度。

### splice

splice(start: number, deleteCount: number, ...items: SegmentButtonItemOptions[]): SegmentButtonItemOptions[]

在数组中，删除从start位置开始的deleteCount数量的元素，并插入items中的元素，返回一个包含了被删除的元素的数组。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| start | number | 是 | 删除元素的起始位置，从0开始计数。 |
| deleteCount | number | 是 | 删除元素的数量，取值范围大于等于0。若deleteCount超过数组剩余长度，则删除从start位置开始的所有剩余元素。 |
| items | [SegmentButtonItemOptions](ohos-arkui-advanced-segmentbutton.md#segmentbuttonitemoptions)[] | 否 | 从start开始要加入到数组中的元素。  默认值：不指定任何元素，将从数组中删除元素。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [SegmentButtonItemOptions](ohos-arkui-advanced-segmentbutton.md#segmentbuttonitemoptions)[] | 返回包含了被删除的元素的数组。 |

**说明** 

分段按钮组件数组仅保存2到5个按钮信息。若操作结果会导致按钮数量少于2个或多于5个，操作将不执行并返回空数组。若删除操作导致数量少于2个，或添加操作导致数量超过5个，整个splice操作将不会生效，数组保持原状态。

### create

static create(elements: SegmentButtonItemTuple): SegmentButtonItemOptionsArray

创建一个SegmentButtonItemOptionsArray对象。与构造函数接受相同的参数，功能一致，可根据编码习惯选择使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| elements | [SegmentButtonItemTuple](ohos-arkui-advanced-segmentbutton.md#segmentbuttonitemtuple) | 是 | 用于初始化数组的按钮信息元组，包含2到5个按钮选项元素，每个元素定义一个按钮的图标、文本等属性。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [SegmentButtonItemOptionsArray](ohos-arkui-advanced-segmentbutton.md#segmentbuttonitemoptionsarray) | 返回创建的SegmentButtonItemOptionsArray对象，用于保存按钮信息的数组。 |

**说明** 

SegmentButtonItemOptionsArray仅支持保存2到5个按钮信息元素。

## TabSegmentButtonOptions

页签类分段按钮选项。继承自[TabSegmentButtonConstructionOptions](ohos-arkui-advanced-segmentbutton.md#tabsegmentbuttonconstructionoptions)。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| type | "tab" | 否 | 否 | 类型为页签类分段按钮。 |

## CapsuleSegmentButtonOptions

胶囊类分段按钮选项。继承自[CapsuleSegmentButtonConstructionOptions](ohos-arkui-advanced-segmentbutton.md#capsulesegmentbuttonconstructionoptions)。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| type | "capsule" | 否 | 否 | 类型为胶囊类分段按钮。 |

## SegmentButtonTextItem

文本按钮信息。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| text | [ResourceStr](ts-types.md#resourcestr) | 否 | 否 | 按钮文本。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| accessibilityLevel13+ | string | 否 | 是 | 无障碍重要性，控制当前组件是否可被无障碍辅助服务识别。  支持的值为：  "auto"：当前组件可被无障碍辅助服务所识别。  "yes"：当前组件可被无障碍辅助服务所识别。  "no"：当前组件不可被无障碍辅助服务所识别。  "no-hide-descendants"：当前组件及其所有子组件不可被无障碍辅助服务所识别。  默认值："auto"  值为undefined时，按默认值处理。  **元服务API：** 从API version 13开始，该接口支持在元服务中使用。 |
| accessibilityDescription13+ | [ResourceStr](ts-types.md#resourcestr) | 否 | 是 | 无障碍说明，用于为用户进一步说明当前组件，开发人员可为组件的该属性设置相对较详细的解释文本，帮助用户理解将要执行的操作。如帮助用户理解将要执行的操作可能导致什么后果，尤其是当这些后果无法从组件本身属性与无障碍文本中了解到时。若组件既拥有文本属性又拥有无障碍说明属性，则组件被选中时，先播报组件的文本属性，再播报无障碍说明属性的内容。  默认值：空字符串。  值为undefined时，按默认值处理。  **元服务API：** 从API version 13开始，该接口支持在元服务中使用。 |

## SegmentButtonIconItem

图标按钮信息。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| icon | [ResourceStr](ts-types.md#resourcestr) | 否 | 否 | 未选中态的按钮图标。  值为undefined时，不显示图标。  **说明：** icon和selectedIcon需同时设置，单独设置无效。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| iconAccessibilityText13+ | [ResourceStr](ts-types.md#resourcestr) | 否 | 是 | 未选中态按钮图标的无障碍文本。  默认值：空字符串。  值为undefined时，按默认值处理。  **元服务API：** 从API version 13开始，该接口支持在元服务中使用。 |
| selectedIcon | [ResourceStr](ts-types.md#resourcestr) | 否 | 否 | 选中态的按钮图标。  值为undefined时，不显示图标。  **说明：** icon和selectedIcon需同时设置，单独设置无效。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| selectedIconAccessibilityText13+ | [ResourceStr](ts-types.md#resourcestr) | 否 | 是 | 选中态按钮图标的无障碍文本。  默认值：空字符串。  值为undefined时，按默认值处理。  **元服务API：** 从API version 13开始，该接口支持在元服务中使用。 |
| accessibilityLevel13+ | string | 否 | 是 | 无障碍重要性，用于控制当前组件是否可被无障碍辅助服务所识别。  支持的值为：  "auto"：当前组件可被无障碍辅助服务所识别。  "yes"：当前组件可被无障碍辅助服务所识别。  "no"：当前组件不可被无障碍辅助服务所识别。  "no-hide-descendants"：当前组件及其所有子组件不可被无障碍辅助服务所识别。  默认值："auto"  值为undefined时，按默认值处理。  **元服务API：** 从API version 13开始，该接口支持在元服务中使用。 |
| accessibilityDescription13+ | [ResourceStr](ts-types.md#resourcestr) | 否 | 是 | 无障碍说明，用于为用户进一步说明当前组件，开发人员可为组件的该属性设置相对较详细的解释文本，帮助用户理解将要执行的操作。如帮助用户理解将要执行的操作可能导致什么后果，尤其是当这些后果无法从组件本身属性与无障碍文本中了解到时。若组件既拥有文本属性又拥有无障碍说明属性，则组件被选中时，先播报组件的文本属性，再播报无障碍说明属性的内容。  默认值：空字符串。  值为undefined时，按默认值处理。  **元服务API：** 从API version 13开始，该接口支持在元服务中使用。 |

**说明** 

未选中态的图标icon和选中态的图标selectedIcon都需设置，单独设置无效。

## SegmentButtonIconTextItem

图标与文本按钮信息。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| icon | [ResourceStr](ts-types.md#resourcestr) | 否 | 否 | 未选中态的按钮图标。  值为undefined时，不显示图标。  **说明：** icon和selectedIcon需同时设置，单独设置无效。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| iconAccessibilityText13+ | [ResourceStr](ts-types.md#resourcestr) | 否 | 是 | 未选中态按钮图标的无障碍文本。  默认值：空字符串。  值为undefined时，按默认值处理。  **元服务API：** 从API version 13开始，该接口支持在元服务中使用。 |
| selectedIcon | [ResourceStr](ts-types.md#resourcestr) | 否 | 否 | 选中态的按钮图标。  值为undefined时，不显示图标。  **说明：** icon和selectedIcon需同时设置，单独设置无效。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| selectedIconAccessibilityText13+ | [ResourceStr](ts-types.md#resourcestr) | 否 | 是 | 选中态按钮图标的无障碍文本。  默认值：空字符串。  值为undefined时，按默认值处理。  **元服务API：** 从API version 13开始，该接口支持在元服务中使用。 |
| text | [ResourceStr](ts-types.md#resourcestr) | 否 | 否 | 按钮文本。  值为undefined时，不显示文本内容。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| accessibilityLevel13+ | string | 否 | 是 | 无障碍重要性，用于控制当前组件是否可被无障碍辅助服务所识别。  支持的值为：  "auto"：当前组件可被无障碍辅助服务所识别。  "yes"：当前组件可被无障碍辅助服务所识别。  "no"：当前组件不可被无障碍辅助服务所识别。  "no-hide-descendants"：当前组件及其所有子组件不可被无障碍辅助服务所识别。  默认值："auto"  值为undefined时，按默认值处理。  **元服务API：** 从API version 13开始，该接口支持在元服务中使用。 |
| accessibilityDescription13+ | [ResourceStr](ts-types.md#resourcestr) | 否 | 是 | 无障碍说明，用于为用户进一步说明当前组件，开发人员可为组件的该属性设置相对较详细的解释文本，帮助用户理解将要执行的操作。如帮助用户理解将要执行的操作可能导致什么后果，尤其是当这些后果无法从组件本身属性与无障碍文本中了解到时。若组件既拥有文本属性又拥有无障碍说明属性，则组件被选中时，先播报组件的文本属性，再播报无障碍说明属性的内容。  默认值：空字符串。  值为undefined时，按默认值处理。  **元服务API：** 从API version 13开始，该接口支持在元服务中使用。 |

**说明** 

未选中态的图标icon和选中态的图标selectedIcon都需设置，单独设置无效。

## SegmentButtonItemOptions

分段按钮中的按钮选项。

**装饰器类型：** @Observed

### 属性

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| icon | [ResourceStr](ts-types.md#resourcestr) | 否 | 是 | 未选中态的按钮图标。  默认值：不显示未选中态的按钮图标。  值为undefined时，按默认值处理。  **说明：** icon和selectedIcon需同时设置，单独设置无效。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| iconAccessibilityText13+ | [ResourceStr](ts-types.md#resourcestr) | 否 | 是 | 未选中态按钮图标的无障碍文本。  默认值：空字符串。  值为undefined时，按默认值处理。  **元服务API：** 从API version 13开始，该接口支持在元服务中使用。 |
| selectedIcon | [ResourceStr](ts-types.md#resourcestr) | 否 | 是 | 选中态的按钮图标。  默认值：不显示选中态按钮图标。  值为undefined时，按默认值处理。  **说明：** icon和selectedIcon需同时设置，单独设置无效。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| selectedIconAccessibilityText13+ | [ResourceStr](ts-types.md#resourcestr) | 否 | 是 | 选中态按钮图标的无障碍文本。  默认值：空字符串。  值为undefined时，按默认值处理。  **元服务API：** 从API version 13开始，该接口支持在元服务中使用。 |
| text | [ResourceStr](ts-types.md#resourcestr) | 否 | 是 | 按钮文本。  默认值：空字符串。  值为undefined时，按默认值处理。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| accessibilityLevel13+ | string | 否 | 是 | 无障碍重要性，用于控制当前组件是否可被无障碍辅助服务所识别。  支持的值为：  "auto"：当前组件可被无障碍辅助服务所识别。  "yes"：当前组件可被无障碍辅助服务所识别。  "no"：当前组件不可被无障碍辅助服务所识别。  "no-hide-descendants"：当前组件及其所有子组件不可被无障碍辅助服务所识别。  默认值："auto"  值为undefined时，按默认值处理。  **元服务API：** 从API version 13开始，该接口支持在元服务中使用。 |
| accessibilityDescription13+ | [ResourceStr](ts-types.md#resourcestr) | 否 | 是 | 无障碍说明，用于为用户进一步说明当前组件，开发人员可为组件的该属性设置相对较详细的解释文本，帮助用户理解将要执行的操作。如帮助用户理解将要执行的操作可能导致什么后果，尤其是当这些后果无法从组件本身属性与无障碍文本中了解到时。若组件既拥有文本属性又拥有无障碍说明属性，则组件被选中时，先播报组件的文本属性，再播报无障碍说明属性的内容。  默认值：空字符串。  值为undefined时，按默认值处理。  **元服务API：** 从API version 13开始，该接口支持在元服务中使用。 |

**说明** 

未选中态的图标icon和选中态的图标selectedIcon都需设置，单独设置无效。

### constructor

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

构造参数用于SegmentButtonItemOptions。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| icon | [ResourceStr](ts-types.md#resourcestr) | 否 | 是 | 未选中态的按钮图标。  默认值：不显示未选中态的按钮图标。  值为undefined时，按默认值处理。  **说明：** icon和selectedIcon需同时设置，单独设置无效。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| iconAccessibilityText13+ | [ResourceStr](ts-types.md#resourcestr) | 否 | 是 | 未选中态按钮图标的无障碍文本。  默认值：空字符串。  值为undefined时，按默认值处理。  **元服务API：** 从API version 13开始，该接口支持在元服务中使用。 |
| selectedIcon | [ResourceStr](ts-types.md#resourcestr) | 否 | 是 | 选中态的按钮图标。  默认值：不显示选中态的按钮图标。  值为undefined时，按默认值处理。  **说明：** icon和selectedIcon需同时设置，单独设置无效。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| selectedIconAccessibilityText13+ | [ResourceStr](ts-types.md#resourcestr) | 否 | 是 | 选中态按钮图标的无障碍文本。  默认值：空字符串。  值为undefined时，按默认值处理。  **元服务API：** 从API version 13开始，该接口支持在元服务中使用。 |
| text | [ResourceStr](ts-types.md#resourcestr) | 否 | 是 | 按钮文本。  默认值：空字符串。  值为undefined时，按默认值处理。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| accessibilityLevel13+ | string | 否 | 是 | 无障碍重要性，用于控制当前组件是否可被无障碍辅助服务所识别。  支持的值为：  "auto"：当前组件可被无障碍辅助服务所识别。  "yes"：当前组件可被无障碍辅助服务所识别。  "no"：当前组件不可被无障碍辅助服务所识别。  "no-hide-descendants"：当前组件及其所有子组件不可被无障碍辅助服务所识别。  默认值："auto"  值为undefined时，按默认值处理。  **元服务API：** 从API version 13开始，该接口支持在元服务中使用。 |
| accessibilityDescription13+ | [ResourceStr](ts-types.md#resourcestr) | 否 | 是 | 无障碍说明，用于为用户进一步说明当前组件，开发人员可为组件的该属性设置相对较详细的解释文本，帮助用户理解将要执行的操作。如帮助用户理解将要执行的操作可能导致什么后果，尤其是当这些后果无法从组件本身属性与无障碍文本中了解到时。若组件既拥有文本属性又拥有无障碍说明属性，则组件被选中时，先播报组件的文本属性，再播报无障碍说明属性的内容。  默认值：空字符串。  值为undefined时，按默认值处理。  **元服务API：** 从API version 13开始，该接口支持在元服务中使用。 |

**说明** 

未选中态的图标icon和选中态的图标selectedIcon都需设置，单独设置无效。

## 示例

### 示例1（设置分段按钮的类型）

通过配置SegmentButtonOptions的tab和capsule，创建两种不同类型的分段按钮。

```ts
import {
  ItemRestriction,
  SegmentButton,
  SegmentButtonItemTuple,
  SegmentButtonOptions,
  SegmentButtonTextItem
} from '@kit.ArkUI';

@Entry
@Component
struct Index {
  // 页签类分段按钮数组。
  @State tabOptions: SegmentButtonOptions = SegmentButtonOptions.tab({
    buttons: [{ text: '页签按钮1' }, { text: '页签按钮2' }, {
      text: '页签按钮3'
    }] as ItemRestriction<SegmentButtonTextItem>,
    // 配置CommonSegmentButtonOptions，实现背景模糊样式。
    backgroundBlurStyle: BlurStyle.BACKGROUND_THICK
  });
  // 胶囊类分段按钮数组。
  @State singleSelectCapsuleOptions: SegmentButtonOptions = SegmentButtonOptions.capsule({
    buttons: [{ text: '单选按钮1' }, { text: '单选按钮2' }, { text: '单选按钮3' }] as SegmentButtonItemTuple,
    multiply: false,
    // 配置CommonSegmentButtonOptions，实现背景模糊样式。
    backgroundBlurStyle: BlurStyle.BACKGROUND_THICK
  });
  // 可多选胶囊类分段按钮数组。
  @State multiplySelectCapsuleOptions: SegmentButtonOptions = SegmentButtonOptions.capsule({
    buttons: [{ text: '多选按钮1' }, { text: '多选按钮2' }, { text: '多选按钮3' }] as SegmentButtonItemTuple,
    multiply: true
  });
  // 胶囊类分段按钮带选中非选中图标数组。
  @State iconCapsuleOptions: SegmentButtonOptions = SegmentButtonOptions.capsule({
    buttons: [
      { icon: $r('sys.media.ohos_ic_public_email'), selectedIcon: $r('sys.media.ohos_ic_public_clock') },
      { icon: $r('sys.media.ohos_ic_public_email'), selectedIcon: $r('sys.media.ohos_ic_public_clock') },
      { icon: $r('sys.media.ohos_ic_public_email'), selectedIcon: $r('sys.media.ohos_ic_public_clock') },
      { icon: $r('sys.media.ohos_ic_public_email'), selectedIcon: $r('sys.media.ohos_ic_public_clock') }
    ] as SegmentButtonItemTuple,
    multiply: false,
    // 配置CommonSegmentButtonOptions，实现背景模糊样式。
    backgroundBlurStyle: BlurStyle.BACKGROUND_THICK
  });
  // 可多选胶囊类分段按钮带选中非选中图标数组。
  @State iconTextCapsuleOptions: SegmentButtonOptions = SegmentButtonOptions.capsule({
    buttons: [
      { text: '图标1', icon: $r('sys.media.ohos_ic_public_email'), selectedIcon: $r('sys.media.ohos_ic_public_clock') },
      { text: '图标2', icon: $r('sys.media.ohos_ic_public_email'), selectedIcon: $r('sys.media.ohos_ic_public_clock') },
      { text: '图标3', icon: $r('sys.media.ohos_ic_public_email'), selectedIcon: $r('sys.media.ohos_ic_public_clock') },
      { text: '图标4', icon: $r('sys.media.ohos_ic_public_email'), selectedIcon: $r('sys.media.ohos_ic_public_clock') },
      { text: '图标5', icon: $r('sys.media.ohos_ic_public_email'), selectedIcon: $r('sys.media.ohos_ic_public_clock') }
    ] as SegmentButtonItemTuple,
    multiply: true
  });
  @State tabSelectedIndexes: number[] = [1];
  @State singleSelectCapsuleSelectedIndexes: number[] = [0];
  @State multiplySelectCapsuleSelectedIndexes: number[] = [0, 1];
  @State singleSelectIconCapsuleSelectedIndexes: number[] = [3];
  @State multiplySelectIconTextCapsuleSelectedIndexes: number[] = [1, 2];

  build() {
    Row() {
      Column() {
        Column({ space: 25 }) {
          SegmentButton({
            options: this.tabOptions,
            selectedIndexes: $tabSelectedIndexes
          })
          SegmentButton({
            options: this.singleSelectCapsuleOptions,
            selectedIndexes: $singleSelectCapsuleSelectedIndexes
          })
          SegmentButton({
            options: this.multiplySelectCapsuleOptions,
            selectedIndexes: $multiplySelectCapsuleSelectedIndexes
          })
          SegmentButton({
            options: this.iconCapsuleOptions,
            selectedIndexes: $singleSelectIconCapsuleSelectedIndexes
          })
          SegmentButton({
            options: this.iconTextCapsuleOptions,
            selectedIndexes: $multiplySelectIconTextCapsuleSelectedIndexes
          })
        }.width('90%')
      }.width('100%')
    }.height('100%')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cb/v3/mTDNtu5qRRON0PomljvP_g/zh-cn_image_0000002712406536.png)

### 示例2（设置分段按钮样式）

通过配置CommonSegmentButtonOptions，实现自定义分段按钮的文本以及背景板样式。

```ts
import {
  ItemRestriction,
  SegmentButton,
  SegmentButtonItemTuple,
  SegmentButtonOptions,
  SegmentButtonTextItem
} from '@kit.ArkUI';

@Entry
@Component
struct Index {
  @State tabOptions: SegmentButtonOptions = SegmentButtonOptions.tab({
    buttons: [{ text: '页签按钮1' }, { text: '页签按钮2' }, {
      text: '页签按钮3'
    }] as ItemRestriction<SegmentButtonTextItem>,
    backgroundColor: 'rgb(213,213,213)',
    selectedBackgroundColor: 'rgb(112,112,112)', // 配置CommonSegmentButtonOptions，实现选中背景色
    textPadding: {
      top: 10,
      right: 10,
      bottom: 10,
      left: 10
    }, // 配置CommonSegmentButtonOptions，实现文字内边距
  });
  @State singleSelectCapsuleOptions: SegmentButtonOptions = SegmentButtonOptions.capsule({
    buttons: [{ text: '单选按钮1' }, { text: '单选按钮2' }, { text: '单选按钮3' }] as SegmentButtonItemTuple,
    multiply: false,
    fontColor: 'rgb(0,74,175)', // 配置CommonSegmentButtonOptions，实现文字颜色
    selectedFontColor: 'rgb(247,247,247)', // 配置CommonSegmentButtonOptions，实现选中文字颜色
    backgroundBlurStyle: BlurStyle.BACKGROUND_THICK // 配置CommonSegmentButtonOptions，实现背景模糊样式
  });
  @State multiplySelectCapsuleOptions: SegmentButtonOptions = SegmentButtonOptions.capsule({
    buttons: [{ text: '多选按钮1' }, { text: '多选按钮2' }, { text: '多选按钮3' }] as SegmentButtonItemTuple,
    multiply: true,
    fontSize: 18,
    selectedFontSize: 18,
    fontWeight: FontWeight.Bolder, // 配置CommonSegmentButtonOptions，实现文字粗细
    selectedFontWeight: FontWeight.Lighter, // 配置CommonSegmentButtonOptions，实现选中文字粗细
  });
  @State iconCapsuleOptions: SegmentButtonOptions = SegmentButtonOptions.capsule({
    buttons: [
      { icon: $r('sys.media.ohos_ic_public_email'), selectedIcon: $r('sys.media.ohos_ic_public_clock') },
      { icon: $r('sys.media.ohos_ic_public_email'), selectedIcon: $r('sys.media.ohos_ic_public_clock') },
      { icon: $r('sys.media.ohos_ic_public_email'), selectedIcon: $r('sys.media.ohos_ic_public_clock') },
      { icon: $r('sys.media.ohos_ic_public_email'), selectedIcon: $r('sys.media.ohos_ic_public_clock') }
    ] as SegmentButtonItemTuple,
    multiply: false,
    imageSize: { width: 40, height: 40 },
    buttonPadding: {
      top: 6,
      right: 10,
      bottom: 6,
      left: 10
    },
    backgroundBlurStyle: BlurStyle.BACKGROUND_THICK
  });
  @State iconTextCapsuleOptions: SegmentButtonOptions = SegmentButtonOptions.capsule({
    buttons: [
      { text: '图标1', icon: $r('sys.media.ohos_ic_public_email'), selectedIcon: $r('sys.media.ohos_ic_public_clock') },
      { text: '图标2', icon: $r('sys.media.ohos_ic_public_email'), selectedIcon: $r('sys.media.ohos_ic_public_clock') },
      { text: '图标3', icon: $r('sys.media.ohos_ic_public_email'), selectedIcon: $r('sys.media.ohos_ic_public_clock') },
      { text: '图标4', icon: $r('sys.media.ohos_ic_public_email'), selectedIcon: $r('sys.media.ohos_ic_public_clock') },
      { text: '图标5', icon: $r('sys.media.ohos_ic_public_email'), selectedIcon: $r('sys.media.ohos_ic_public_clock') }
    ] as SegmentButtonItemTuple,
    multiply: true,
    imageSize: { width: 10, height: 10 },
  });
  @State tabSelectedIndexes: number[] = [0];
  @State singleSelectCapsuleSelectedIndexes: number[] = [0];
  @State multiplySelectCapsuleSelectedIndexes: number[] = [0, 1];
  @State singleSelectIconCapsuleSelectedIndexes: number[] = [3];
  @State multiplySelectIconTextCapsuleSelectedIndexes: number[] = [1, 2];

  build() {
    Row() {
      Column() {
        Column({ space: 20 }) {
          SegmentButton({ options: this.tabOptions, selectedIndexes: $tabSelectedIndexes })
          SegmentButton({
            options: this.singleSelectCapsuleOptions,
            selectedIndexes: $singleSelectCapsuleSelectedIndexes
          })
          SegmentButton({
            options: this.multiplySelectCapsuleOptions,
            selectedIndexes: $multiplySelectCapsuleSelectedIndexes
          })
          SegmentButton({
            options: this.iconCapsuleOptions,
            selectedIndexes: $singleSelectIconCapsuleSelectedIndexes
          })
          SegmentButton({
            options: this.iconTextCapsuleOptions,
            selectedIndexes: $multiplySelectIconTextCapsuleSelectedIndexes
          })
        }.width('90%')
      }.width('100%')
    }.height('100%')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/wvzFEgkQQUOCbADseVYPqQ/zh-cn_image_0000002742125485.png)

### 示例3（分段按钮数组处理）

该示例通过pop、shift、unshift等函数实现分段按钮数组的添加、移除等操作。

```ts
import {
  SegmentButton,
  SegmentButtonOptions,
  SegmentButtonItemOptionsArray,
  SegmentButtonItemTuple,
  SegmentButtonItemOptions
} from '@kit.ArkUI';

@Entry
@Component
struct Index {
  // 胶囊类分段按钮数组。
  @State singleSelectCapsuleOptions: SegmentButtonOptions = SegmentButtonOptions.capsule({
    buttons: [{ text: '1' }, { text: '2' }, { text: '3' },
      { text: '4' }, { text: '5' }] as SegmentButtonItemTuple,
    multiply: false,
    // 配置CommonSegmentButtonOptions，实现背景模糊样式。
    backgroundBlurStyle: BlurStyle.BACKGROUND_THICK
  });
  @State capsuleSelectedIndexes: number[] = [0];

  build() {
    Row() {
      Column() {
        Column({ space: 10 }) {
          SegmentButton({
            options: this.singleSelectCapsuleOptions,
            selectedIndexes: $capsuleSelectedIndexes
          })
          // 点击“删除第一个按钮”，第一个按钮会删除。
          Button('删除第一个按钮')
            .onClick(() => {
              this.singleSelectCapsuleOptions.buttons.shift()
            })
          // 点击“删除最后一个按钮”，最后一个按钮会删除。
          Button('删除最后一个按钮')
            .onClick(() => {
              this.singleSelectCapsuleOptions.buttons.pop()
            })
          // 点击“末尾增加一个按钮push”，在按钮末尾会增加一个按钮。
          Button('末尾增加一个按钮push')
            .onClick(() => {
              this.singleSelectCapsuleOptions.buttons.push({ text: 'push' })
            })
          // 点击“开头增加一个按钮unshift”，在按钮开头会增加一个按钮。
          Button('开头增加一个按钮unshift')
            .onClick(() => {
              this.singleSelectCapsuleOptions.buttons.unshift(({ text: 'unshift' }))
            })
          // 点击“将按钮2、3替换为splice1、splice2”，按钮2、3会被替换成splice1、splice2。
          Button('将按钮2、3替换为splice1、splice2')
            .onClick(() => {
              this.singleSelectCapsuleOptions.buttons.splice(1, 2, new SegmentButtonItemOptions({
                text: 'splice1'
              }), new SegmentButtonItemOptions({ text: 'splice2' }))
            })
          // 点击“更改所有按钮文字”，按钮会由1、2、3、4、5替换成a、b、c、d、e。
          Button('更改所有按钮文字')
            .onClick(() => {
              this.singleSelectCapsuleOptions.buttons =
                SegmentButtonItemOptionsArray.create([{ text: 'a' }, { text: 'b' },
                  { text: 'c' }, { text: 'd' }, { text: 'e' }])
            })
        }.width('90%')
      }.width('100%')
    }.height('100%')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/zTgF28zOTqC47s7Xx9dgSQ/zh-cn_image_0000002712246578.gif)

### 示例4（设置镜像效果）

该示例通过配置direction属性设置分段按钮的布局方向，实现镜像效果。

```ts
import { LengthMetrics, SegmentButton, SegmentButtonOptions } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  // 页签类分段按钮数组。
  @State tabOptions: SegmentButtonOptions = SegmentButtonOptions.tab({
    buttons: [{ text: '页签按钮1' }, { text: '页签按钮2' }, {
      text: '页签按钮3'
    }],
    direction: Direction.Rtl, // 设置分段按钮的布局方向。
    backgroundColor: Color.Green, // 设置分段按钮的背景板颜色。
    selectedBackgroundColor: Color.Orange, // 设置分段按钮组件的按钮选中态背景板颜色。
    // 设置文本内边距。
    localizedTextPadding: {
      end: LengthMetrics.vp(10),
      start: LengthMetrics.vp(10)
    },
  });
  // 胶囊类分段按钮数组。
  @State singleSelectCapsuleOptions: SegmentButtonOptions = SegmentButtonOptions.capsule({
    buttons: [{ text: '单选按钮1' }, { text: '单选按钮2' }, { text: '单选按钮3' }],
    multiply: false, // 设置分段按钮组件是否可以多选。
    direction: Direction.Rtl, // 设置分段按钮的布局方向。
    fontColor: Color.Black, // 设置分段按钮组件的按钮未选中态的文本颜色。
    selectedFontColor: Color.Yellow, // 设置分段按钮组件的按钮选中态的文本颜色。
    backgroundBlurStyle: BlurStyle.BACKGROUND_THICK // 设置分段按钮组件的背景模糊材质。
  });
  // 胶囊类分段按钮数组。
  @State multiplySelectCapsuleOptions: SegmentButtonOptions = SegmentButtonOptions.capsule({
    buttons: [{ text: '多选按钮1' }, { text: '多选按钮2' }, { text: '多选按钮3' }],
    multiply: true, // 设置分段按钮组件是否可以多选。
    direction: Direction.Rtl, // 设置分段按钮的布局方向。
    fontSize: 18, // 设置分段按钮组件的按钮未选中态的字体大小。
    selectedFontSize: 18, // 设置分段按钮组件的按钮选中态的字体大小。
    fontWeight: FontWeight.Bolder, // 设置分段按钮组件的按钮未选中态的字体粗细。
    selectedFontWeight: FontWeight.Lighter, // 设置分段按钮组件的按钮选中态的字体粗细。
  });
  // 胶囊类分段按钮数组。
  @State iconCapsuleOptions: SegmentButtonOptions = SegmentButtonOptions.capsule({
    buttons: [
      { icon: $r('sys.media.ohos_ic_public_email'), selectedIcon: $r('sys.media.ohos_ic_public_clock') },
      { icon: $r('sys.media.ohos_ic_public_email'), selectedIcon: $r('sys.media.ohos_ic_public_clock') },
      { icon: $r('sys.media.ohos_ic_public_email'), selectedIcon: $r('sys.media.ohos_ic_public_clock') },
      { icon: $r('sys.media.ohos_ic_public_email'), selectedIcon: $r('sys.media.ohos_ic_public_clock') },
      { icon: $r('sys.media.ohos_ic_public_email'), selectedIcon: $r('sys.media.ohos_ic_public_clock') }
    ],
    multiply: false, // 设置分段按钮组件是否可以多选。
    direction: Direction.Rtl, // 设置分段按钮的布局方向。
    imageSize: { width: 40, height: 40 }, // 设置分段按钮组件的图片尺寸。
    // 设置分段按钮组件的按钮内边距，支持随布局方向（LTR/RTL）自适应。
    localizedButtonPadding: {
      end: LengthMetrics.vp(10),
      start: LengthMetrics.vp(10)
    },
    backgroundBlurStyle: BlurStyle.BACKGROUND_THICK // 设置分段按钮组件的背景模糊材质。
  });
  @State iconTextCapsuleOptions: SegmentButtonOptions = SegmentButtonOptions.capsule({
    buttons: [
      { text: '图标1', icon: $r('sys.media.ohos_ic_public_email'), selectedIcon: $r('sys.media.ohos_ic_public_clock') },
      { text: '图标2', icon: $r('sys.media.ohos_ic_public_email'), selectedIcon: $r('sys.media.ohos_ic_public_clock') },
      { text: '图标3', icon: $r('sys.media.ohos_ic_public_email'), selectedIcon: $r('sys.media.ohos_ic_public_clock') },
      { text: '图标4', icon: $r('sys.media.ohos_ic_public_email'), selectedIcon: $r('sys.media.ohos_ic_public_clock') },
      { text: '图标5', icon: $r('sys.media.ohos_ic_public_email'), selectedIcon: $r('sys.media.ohos_ic_public_clock') }
    ],
    multiply: true, // 设置分段按钮组件是否可以多选。
    direction: Direction.Rtl, // 设置分段按钮的布局方向。
    imageSize: { width: 10, height: 10 }, // 设置分段按钮组件的图片尺寸。
  });
  @State tabSelectedIndexes: number[] = [0];
  @State singleSelectCapsuleSelectedIndexes: number[] = [0];
  @State multiplySelectCapsuleSelectedIndexes: number[] = [0, 1];
  @State singleSelectIconCapsuleSelectedIndexes: number[] = [3];
  @State multiplySelectIconTextCapsuleSelectedIndexes: number[] = [1, 2];

  build() {
    Row() {
      Column() {
        Column({ space: 20 }) {
          SegmentButton({ options: this.tabOptions, selectedIndexes: $tabSelectedIndexes })
          SegmentButton({
            options: this.singleSelectCapsuleOptions,
            selectedIndexes: $singleSelectCapsuleSelectedIndexes
          })
          SegmentButton({
            options: this.multiplySelectCapsuleOptions,
            selectedIndexes: $multiplySelectCapsuleSelectedIndexes
          })
          SegmentButton({
            options: this.iconCapsuleOptions,
            selectedIndexes: $singleSelectIconCapsuleSelectedIndexes
          })
          SegmentButton({
            options: this.iconTextCapsuleOptions,
            selectedIndexes: $multiplySelectIconTextCapsuleSelectedIndexes
          })
        }.width('90%')
      }.width('100%')
    }.height('100%')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2c/v3/lbx6mkA7T7yTvZE4oqIovA/zh-cn_image_0000002742005529.png)

### 示例5（设置无障碍朗读）

通过配置accessibilityLevel和selectedIconAccessibilityText等属性，实现了分段按钮的无障碍朗读功能。

```ts
import {
  ItemRestriction,
  SegmentButton,
  SegmentButtonItemTuple,
  SegmentButtonOptions,
  SegmentButtonTextItem,
  SegmentButtonItemOptions
} from '@kit.ArkUI';

@Entry
@Component
struct Index {
  @State tabOptions: SegmentButtonOptions = SegmentButtonOptions.tab({
    buttons: [{ text: '页签按钮1', accessibilityLevel: 'yes', accessibilityDescription: '页签按钮1 新手提醒' },
      { text: '页签按钮2', accessibilityLevel: 'yes', accessibilityDescription: '页签按钮2 新手提醒' },
      {
        text: '页签按钮3', accessibilityLevel: 'yes', accessibilityDescription: '页签按钮3 新手提醒'
      }] as ItemRestriction<SegmentButtonTextItem>,
    backgroundBlurStyle: BlurStyle.BACKGROUND_THICK
  });
  @State iconCapsuleOptions: SegmentButtonOptions = SegmentButtonOptions.capsule({
    buttons: [
      {
        icon: $r('sys.media.ohos_ic_public_email'),
        iconAccessibilityText: '未选中图标无障碍文本', // 未选中态按钮图标的无障碍文本。
        selectedIcon: $r('sys.media.ohos_ic_public_clock'),
        selectedIconAccessibilityText: '选中图标无障碍文本', // 选中态按钮图标的无障碍文本。
        accessibilityLevel: 'yes', // 无障碍重要性，控制当前组件是否可被无障碍辅助服务识别。
        accessibilityDescription: 'SegmentButtonIconItem 新手提醒' // 无障碍说明。
      },
      {
        icon: $r('sys.media.ohos_ic_public_email'),
        iconAccessibilityText: '未选中图标无障碍文本', // 未选中态按钮图标的无障碍文本。
        selectedIcon: $r('sys.media.ohos_ic_public_clock'),
        selectedIconAccessibilityText: '选中图标无障碍文本', // 选中态按钮图标的无障碍文本。
        accessibilityLevel: 'yes', // 无障碍重要性，控制当前组件是否可被无障碍辅助服务识别。
        accessibilityDescription: 'SegmentButtonIconItem 新手提醒' // 无障碍说明。
      },
      {
        icon: $r('sys.media.ohos_ic_public_email'),
        iconAccessibilityText: '未选中图标无障碍文本', // 未选中态按钮图标的无障碍文本。
        selectedIcon: $r('sys.media.ohos_ic_public_clock'),
        selectedIconAccessibilityText: '选中图标无障碍文本', // 选中态按钮图标的无障碍文本。
        accessibilityLevel: 'yes', // 无障碍重要性，控制当前组件是否可被无障碍辅助服务识别。
        accessibilityDescription: 'SegmentButtonIconItem 新手提醒' // 无障碍说明。
      },
      {
        icon: $r('sys.media.ohos_ic_public_email'),
        iconAccessibilityText: '未选中图标无障碍文本', // 未选中态按钮图标的无障碍文本。
        selectedIcon: $r('sys.media.ohos_ic_public_clock'),
        selectedIconAccessibilityText: '选中图标无障碍文本', // 选中态按钮图标的无障碍文本。
        accessibilityLevel: 'yes', // 无障碍重要性，控制当前组件是否可被无障碍辅助服务识别。
        accessibilityDescription: 'SegmentButtonIconItem 新手提醒' // 无障碍说明。
      }
    ] as SegmentButtonItemTuple,
    multiply: false,
    backgroundBlurStyle: BlurStyle.BACKGROUND_THICK
  });
  @State iconTextCapsuleOptions: SegmentButtonOptions = SegmentButtonOptions.capsule({
    buttons: [
      {
        text: '图标1',
        icon: $r('sys.media.ohos_ic_public_email'),
        iconAccessibilityText: '未选中图标无障碍文本', // 未选中态按钮图标的无障碍文本。
        selectedIcon: $r('sys.media.ohos_ic_public_clock'),
        selectedIconAccessibilityText: '选中图标无障碍文本', // 选中态按钮图标的无障碍文本。
        accessibilityLevel: 'yes', // 无障碍重要性，控制当前组件是否可被无障碍辅助服务识别。
        accessibilityDescription: 'SegmentButtonIconTextItem 新手提醒' // 无障碍说明。
      },
      {
        text: '图标2',
        icon: $r('sys.media.ohos_ic_public_email'),
        iconAccessibilityText: '未选中图标无障碍文本', // 未选中态按钮图标的无障碍文本。
        selectedIcon: $r('sys.media.ohos_ic_public_clock'),
        selectedIconAccessibilityText: '选中图标无障碍文本', // 选中态按钮图标的无障碍文本。
        accessibilityLevel: 'yes', // 无障碍重要性，控制当前组件是否可被无障碍辅助服务识别。
        accessibilityDescription: 'SegmentButtonIconTextItem 新手提醒' // 无障碍说明。
      },
      {
        text: '图标3',
        icon: $r('sys.media.ohos_ic_public_email'),
        iconAccessibilityText: '未选中图标无障碍文本', // 未选中态按钮图标的无障碍文本。
        selectedIcon: $r('sys.media.ohos_ic_public_clock'),
        selectedIconAccessibilityText: '选中图标无障碍文本', // 选中态按钮图标的无障碍文本。
        accessibilityLevel: 'yes', // 无障碍重要性，控制当前组件是否可被无障碍辅助服务识别。
        accessibilityDescription: 'SegmentButtonIconTextItem 新手提醒' // 无障碍说明。
      },
      {
        text: '图标4',
        icon: $r('sys.media.ohos_ic_public_email'),
        iconAccessibilityText: '未选中图标无障碍文本', // 未选中态按钮图标的无障碍文本。
        selectedIcon: $r('sys.media.ohos_ic_public_clock'),
        selectedIconAccessibilityText: '选中图标无障碍文本', // 选中态按钮图标的无障碍文本。
        accessibilityLevel: 'yes', // 无障碍重要性，控制当前组件是否可被无障碍辅助服务识别。
        accessibilityDescription: 'SegmentButtonIconTextItem 新手提醒' // 无障碍说明。
      }
    ] as SegmentButtonItemTuple,
    multiply: true
  });
  @State tabSelectedIndexes: number[] = [1];
  @State singleSelectIconCapsuleSelectedIndexes: number[] = [3];
  @State multiplySelectIconTextCapsuleSelectedIndexes: number[] = [1, 2];

  build() {
    Row() {
      Column() {
        Column({ space: 25 }) {
          SegmentButton({
            options: this.tabOptions,
            selectedIndexes: $tabSelectedIndexes
          })
          SegmentButton({
            options: this.iconCapsuleOptions,
            selectedIndexes: $singleSelectIconCapsuleSelectedIndexes
          })
          SegmentButton({
            options: this.iconTextCapsuleOptions,
            selectedIndexes: $multiplySelectIconTextCapsuleSelectedIndexes
          })
          Button('将按钮2、3替换为splice1、splice2')
            .onClick(() => {
              this.iconTextCapsuleOptions.buttons.splice(1, 2, new SegmentButtonItemOptions({
                text: 'splice1', accessibilityLevel: 'yes', accessibilityDescription: 'SegmentButtonItemOptions 新手提醒'
              }), new SegmentButtonItemOptions({
                text: 'splice2',
                icon: $r('sys.media.ohos_ic_public_email'),
                iconAccessibilityText: '未选中图标无障碍文本', // 未选中态按钮图标的无障碍文本。
                selectedIcon: $r('sys.media.ohos_ic_public_clock'),
                selectedIconAccessibilityText: '选中图标无障碍文本', // 选中态按钮图标的无障碍文本。
                accessibilityLevel: 'yes', // 无障碍重要性，控制当前组件是否可被无障碍辅助服务识别。
                accessibilityDescription: 'SegmentButtonIconTextItem 新手提醒' // 无障碍说明。
              }))
            })
        }.width('90%')
      }.width('100%')
    }.height('100%')
  }
}
```

### 示例6（设置自定义圆角）

该示例演示了如何为分段按钮组件设置自定义的边框圆角半径。

```ts
import {
  BorderRadiusMode,
  ItemRestriction,
  LengthMetrics,
  SegmentButton,
  SegmentButtonOptions,
  SegmentButtonTextItem
} from '@kit.ArkUI';

@Entry
@Component
struct Index {
  @State tabOptions: SegmentButtonOptions = SegmentButtonOptions.tab({
    buttons: [{ text: '页签按钮1' }, { text: '页签按钮2' }, {
      text: '页签按钮3'
    }] as ItemRestriction<SegmentButtonTextItem>,
    backgroundBlurStyle: BlurStyle.BACKGROUND_THICK,
    borderRadiusMode: BorderRadiusMode.CUSTOM, // 设置自定义的边框圆角半径
    backgroundBorderRadius: LengthMetrics.vp(8),
    itemBorderRadius: LengthMetrics.vp(6)
  });
  @State tabSelectedIndexes: number[] = [1];

  build() {
    Row() {
      Column() {
        Column({ space: 25 }) {
          SegmentButton({
            options: this.tabOptions,
            selectedIndexes: $tabSelectedIndexes,
          })
        }.width('90%')
      }.width('100%')
    }.height('100%')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b1/v3/Qq_RZjk8Sj2V2zmasLD3_A/zh-cn_image_0000002712406540.png)

### 示例7（开启SegmentButton的属性动画）

本示例展示了SegmentButton开启属性动画，即enableStateAnimation设置为true后，修改选中项编号selectedIndexes值会触发按钮切换动画。并且选中项编号相同的两个SegmentButton组件，是否开启属性动画，也会呈现不同的切换动画。

从API version 24开始，[SegmentButton](ohos-arkui-advanced-segmentbutton.md#segmentbutton-1)新增enableStateAnimation属性。

```ts
import { SegmentButton, SegmentButtonItemTuple, SegmentButtonOptions } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  @State singleSelectTextCapsuleOptions: SegmentButtonOptions = SegmentButtonOptions.capsule({
    buttons: [
      { text: '单选按钮1' }, { text: '单选按钮2' }, { text: '单选按钮3' }
    ] as SegmentButtonItemTuple,
    multiply: false
  });

  @State textCapsuleSingleSelected: number[] = [0]; // 单选按钮的选中索引值，默认选中第一个。

  enableStateAnimation: boolean[] = [false, true];
  @State enableStateAnimationIndex: number = 0;
  @State currentSelectedIndex: number = 0; // 切换选中项的索引计数器。

  build() {
    Row() {
      Column() {
        Column({ space: 25 }) {
          // 动画仅在手动点击切换选中项时生效，非点击类操作修改选中项均无动画。
          SegmentButton({
            options: this.singleSelectTextCapsuleOptions,
            selectedIndexes: this.textCapsuleSingleSelected // 未开启属性动画。
          })

          Text('enableStateAnimation: ' + this.enableStateAnimation[this.enableStateAnimationIndex])
            .fontSize(18)
            .fontWeight(FontWeight.Bold)

          Row({ space: 10 }) {
            Button('false')
              .onClick(() => {
                this.enableStateAnimationIndex = 0;
              })

            Button('true')
              .onClick(() => {
                this.enableStateAnimationIndex = 1;
              })
          }
          .width('100%')
          .justifyContent(FlexAlign.Center)
          .margin({ bottom: 10 })

          // enableStateAnimation为true时，切换选中项会触发按钮切换动画。enableStateAnimation为false时，动画仅在手动点击切换选中项时生效，非点击类操作修改选中项均无动画。
          SegmentButton({
            options: this.singleSelectTextCapsuleOptions,
            selectedIndexes: this.textCapsuleSingleSelected,
            enableStateAnimation: this.enableStateAnimation[this.enableStateAnimationIndex] // 开启属性动画。
          })

          Button('change selectedIndexes')
            .onClick(() => {
              // 对选中项的索引值进行自增操作，若超出最大索引则重置为0。
              this.currentSelectedIndex = this.currentSelectedIndex < 2 ? this.currentSelectedIndex + 1 : 0;
              this.textCapsuleSingleSelected = [this.currentSelectedIndex];
            })
        }.width('90%')
      }.width('100%')
    }.height('100%')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/db/v3/nirW_GRtRRKYH9JUt8Cvwg/zh-cn_image_0000002742125489.gif)

### 示例8（设置背景板材质）

以下示例通过backgroundSystemMaterial属性，为分段按钮设置了透明的背景板材质、开启自动反色和交互形变效果，并自定义反馈光感的颜色。

从API版本26.0.0开始，[SegmentButtonOptions](ohos-arkui-advanced-segmentbutton.md#segmentbuttonoptions)和[CommonSegmentButtonOptions](ohos-arkui-advanced-segmentbutton.md#commonsegmentbuttonoptions)中新增backgroundSystemMaterial属性。

```ts
import {
  ItemRestriction,
  SegmentButton,
  SegmentButtonOptions,
  SegmentButtonTextItem,
  uiMaterial
} from '@kit.ArkUI';

@Entry
@Component
struct Index {
  @State tabOptions: SegmentButtonOptions = SegmentButtonOptions.tab({
    buttons: [{ text: '页签按钮1' }, { text: '页签按钮2' }, {
      text: '页签按钮3'
    }] as ItemRestriction<SegmentButtonTextItem>,
    backgroundColor: Color.Transparent,
    // 将fontColor设置为特殊系统资源值，启用自动反色能力。
    fontColor: $r('sys.color.font_primary'),
    // 设置为系统材质样式为ULTRA_THIN，并开启自动反色和交互形变效果、自定义反馈光感的颜色。
    backgroundSystemMaterial: new uiMaterial.ImmersiveMaterial({
      style: uiMaterial.ImmersiveStyle.ULTRA_THIN,
      colorInvert: true,
      interactive: true,
      lightEffect: { color: undefined }
    })
  });
  @State tabSelectedIndexes: number[] = [0];

  @Builder
  NavigationTitle() {
    Column({ space: 20 }) {
      SegmentButton({
        options: this.tabOptions,
        selectedIndexes: $tabSelectedIndexes
      })
    }
    .width('100%')
    .height('20%')
    .padding(20)
    .linearGradient({
      angle: 90, // 渐变角度，90度是从左到右。
      colors: [
        ['#FF9A9E', 0.0], // 起始颜色及位置（0.0表示起点）。
        ['#FECFEF', 0.1], // 中间颜色及位置。
        ['#3B324C', 1.0] // 结束颜色及位置（1.0表示终点）。
      ]
    })
  }

  build() {
    Column() {
      Navigation() {
        // 页面内容
      }
      .title({ builder: this.NavigationTitle, height: '100%' })
    }.width('100%').height('100%')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a9/v3/6nX1R_hwRsC9YEuvSOCKCw/zh-cn_image_0000002712246582.gif)

### 示例9（监听SegmentButtonOptions内属性的变化）

[SegmentButtonOptions](ohos-arkui-advanced-segmentbutton.md#segmentbuttonoptions)使用了@Observed装饰器，SegmentButton组件通过@ObjectLink接收该对象。对于SegmentButtonOptions的一层基本类型属性（如fontColor、backgroundColor等），@Observed与@ObjectLink的联动机制已能观测到属性变化并触发UI刷新，无需额外处理。但对于SegmentButtonOptions中对象类型属性（如imageSize、buttonPadding等）的内部属性（如imageSize的width、height），属于更深层的嵌套属性，@State仅能观测到一层赋值变化，无法感知这类深层属性的修改，导致修改对象类型属性的内部属性时UI不会自动刷新。使用[makeObserved](js-apis-statemanagement.md#makeobserved)接口对对象类型属性（如imageSize）进行包裹，可以为该对象的内部属性补充深度观察能力，使得修改内部属性（如width、height）时，框架能够监听到变化并触发UI刷新。makeObserved接口的详细说明请参考[makeObserved接口：将非观察数据变为可观察数据](../harmonyos-guides/arkts-new-makeobserved.md)。

以下示例对比了两种场景：点击“修改fontColor颜色”按钮修改iconTextCapsuleOptions的fontColor属性（一层基本类型属性，已通过@Observed与@ObjectLink支持观测），UI自动刷新；点击“修改图标大小”按钮修改iconTextCapsuleOptions.imageSize的width和height属性（imageSize对象的内部属性，需通过UIUtils.makeObserved包裹imageSize才能观测），UI同样自动刷新。

```ts
import {
  SegmentButton,
  SegmentButtonOptions,
  SegmentButtonItemTuple,
  UIUtils
} from '@kit.ArkUI';

@Entry
@Component
struct Index {
  @State iconTextCapsuleOptions: SegmentButtonOptions = SegmentButtonOptions.capsule({
    buttons: [
      { text: '图标1', icon: $r('sys.media.ohos_ic_public_email'), selectedIcon: $r('sys.media.ohos_ic_public_clock') },
      { text: '图标2', icon: $r('sys.media.ohos_ic_public_email'), selectedIcon: $r('sys.media.ohos_ic_public_clock') },
      { text: '图标3', icon: $r('sys.media.ohos_ic_public_email'), selectedIcon: $r('sys.media.ohos_ic_public_clock') },
      { text: '图标4', icon: $r('sys.media.ohos_ic_public_email'), selectedIcon: $r('sys.media.ohos_ic_public_clock') },
      { text: '图标5', icon: $r('sys.media.ohos_ic_public_email'), selectedIcon: $r('sys.media.ohos_ic_public_clock') }
    ] as SegmentButtonItemTuple,
    multiply: false,
    // 使用UIUtils.makeObserved包裹imageSize，使内部属性width和height可被观测。
    imageSize: UIUtils.makeObserved({ width: 30, height: 30 })
  });
  @State selectedIndexes: number[] = [0];
  @State currentFontColor: ResourceColor = Color.Blue;

  build() {
    Column({ space: 20 }) {
      SegmentButton({
        options: this.iconTextCapsuleOptions,
        selectedIndexes: $selectedIndexes
      })
      // 一层基本类型属性，已通过@Observed与@ObjectLink支持this.iconTextCapsuleOptions.fontColor的观测，UI自动刷新。
      Button('修改fontColor颜色')
        .onClick(() => {
          if (this.currentFontColor === Color.Blue) {
            this.currentFontColor = Color.Red;
          } else {
            this.currentFontColor = Color.Blue;
          }
          this.iconTextCapsuleOptions.fontColor = this.currentFontColor;
        })
      // 修改imageSize的内部属性，由于makeObserved包裹，UI会自动刷新。
      Button('修改图标大小')
        .onClick(() => {
          this.iconTextCapsuleOptions.imageSize.width = 10;
          this.iconTextCapsuleOptions.imageSize.height = 10;
        })
    }
    .width('100%')
    .height('50%')
    .padding({ top: 20 })
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d5/v3/D5P45K6YSUWW7wyjJyLRhg/zh-cn_image_0000002742005531.gif)
