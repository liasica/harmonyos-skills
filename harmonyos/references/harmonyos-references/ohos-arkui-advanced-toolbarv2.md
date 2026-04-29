---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-toolbarv2
title: ToolBarV2
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 系统预置UI组件库 > ToolBarV2
category: harmonyos-references
scraped_at: 2026-04-29T13:53:06+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:8daf9abc0678d8589f29dff19be4290503b250e069cd60e205f513b701abf9ca
---

工具栏用于展示针对当前界面内容的操作选项，在界面底部显示。底部最多显示5个入口，超过则收纳入“更多”子项中，在最右侧显示。

该组件基于[状态管理（V2）](../harmonyos-guides/arkts-state-management-overview.md#状态管理v2)实现，相较于[状态管理（V1）](../harmonyos-guides/arkts-state-management-overview.md#状态管理v1)，状态管理（V2）增强了对数据对象的深度观察与管理能力，不再局限于组件层级。借助状态管理（V2），开发者可以通过该组件更灵活地控制工具栏的数据和状态，实现更高效的用户界面刷新。

说明

* 该组件从API version 18开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。
* 该组件仅可在Stage模型下使用。
* 如果ToolBarV2设置[通用属性](ts-component-general-attributes.md)和[通用事件](ts-component-general-events.md)，编译工具链会额外生成节点\_\_Common\_\_，并将通用属性或通用事件挂载在\_\_Common\_\_上，而不是直接应用到ToolBarV2本身。这可能导致开发者设置的通用属性或通用事件不生效或不符合预期，因此，不建议ToolBarV2设置通用属性和通用事件。
* 系统切换深浅色模式，工具栏背景色不支持自动切换。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { ToolBarV2 } from '@kit.ArkUI';
```

## 子组件

PhonePC/2in1TabletTVWearable

无

## ToolBarV2

PhonePC/2in1TabletTVWearable

ToolBarV2({toolBarList: ToolBarV2Item[], activatedIndex?: number, dividerModifier: DividerModifier, toolBarModifier: ToolBarV2Modifier})

工具栏。

**装饰器类型：**@ComponentV2

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

| 名称 | 类型 | 必填 | 装饰器类型 | 说明 |
| --- | --- | --- | --- | --- |
| toolBarList | [ToolBarV2Item](ohos-arkui-advanced-toolbarv2.md#toolbarv2item)[] | 是 | @Param  @Require | 工具栏列表。 |
| activatedIndex | number | 否 | @Param | 激活态的子项。  默认值：-1，即无工具栏子项为激活态。  取值范围：[-1,4]。 |
| dividerModifier | [DividerModifier](ts-universal-attributes-attribute-modifier.md#自定义modifier) | 否 | @Param | 工具栏头部分割线属性，可设置分割线高度、颜色等。  默认不生效。 |
| toolBarModifier | [ToolBarV2Modifier](ohos-arkui-advanced-toolbarv2.md#toolbarv2modifier) | 否 | @Param | 工具栏属性，可设置工具栏高度、背景色、内边距（仅在工具栏子项数量小于5时生效）、是否显示按压态。  默认不生效。 |

## ToolBarV2Item

PhonePC/2in1TabletTVWearable

定义工具栏子项。

**装饰器类型：**@ObservedV2

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

### 属性

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| content | [ToolBarV2ItemText](ohos-arkui-advanced-toolbarv2.md#toolbarv2itemtext) | 否 | 否 | 工具栏子项的文本。  装饰器类型：@Trace |
| action | [ToolBarV2ItemAction](ohos-arkui-advanced-toolbarv2.md#toolbarv2itemaction) | 否 | 是 | 工具栏子项点击事件。  默认无点击事件。  装饰器类型：@Trace |
| icon | [ToolBarV2ItemIconType](ohos-arkui-advanced-toolbarv2.md#toolbarv2itemicontype) | 否 | 是 | 工具栏子项的图标。  默认不显示图标。  装饰器类型：@Trace |
| state | [ToolBarV2ItemState](ohos-arkui-advanced-toolbarv2.md#toolbarv2itemstate) | 否 | 是 | 工具栏子项的状态。  默认为ToolBarV2ItemState.ENABLE。  装饰器类型：@Trace |
| accessibilityText | [ResourceStr](ts-types.md#resourcestr) | 否 | 是 | 工具栏子项的无障碍文本属性。当组件不包含文本属性时，屏幕朗读选中此组件时不播报，使用者无法清楚地知道当前选中了什么组件。为了解决此场景，开发人员可为不包含文字信息的组件设置无障碍文本，当屏幕朗读选中此组件时播报无障碍文本的内容，帮助屏幕朗读的使用者清楚地知道自己选中了什么组件。  默认值为当前项content属性内容。  装饰器类型：@Trace |
| accessibilityDescription | [ResourceStr](ts-types.md#resourcestr) | 否 | 是 | 工具栏子项的无障碍描述。此描述用于向用户详细解释当前组件，开发人员应为组件的这一属性提供较为详尽的文本说明，以协助用户理解即将执行的操作及其可能产生的后果。特别是当这些后果无法仅从组件的属性和无障碍文本中直接获知时。如果组件同时具备文本属性和无障碍说明属性，当组件被选中时，系统将首先播报组件的文本属性，随后播报无障碍说明属性的内容。  默认值：“单指双击即可执行”。  装饰器类型：@Trace |
| accessibilityLevel | string | 否 | 是 | 工具栏子项无障碍重要性。用于控制当前项是否可被无障碍辅助服务所识别。  支持的值为：  "auto"：当前组件会转换"yes"。  "yes"：当前组件可被无障碍辅助服务所识别。  "no"：当前组件不可被无障碍辅助服务所识别。  "no-hide-descendants"：当前组件及其所有子组件不可被无障碍辅助服务所识别。  默认值："auto"  装饰器类型：@Trace |

### constructor

PhonePC/2in1TabletTVWearable

constructor(options: ToolBarV2ItemOptions)

ToolBarV2Item的构造函数。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [ToolBarV2ItemOptions](ohos-arkui-advanced-toolbarv2.md#toolbarv2itemoptions) | 是 | 工具栏子项信息。 |

## ToolBarV2ItemOptions

PhonePC/2in1TabletTVWearable

用于构建ToolBarV2Item对象。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| content | [ToolBarV2ItemText](ohos-arkui-advanced-toolbarv2.md#toolbarv2itemtext) | 否 | 否 | 工具栏子项的文本。 |
| action | [ToolBarV2ItemAction](ohos-arkui-advanced-toolbarv2.md#toolbarv2itemaction) | 否 | 是 | 工具栏子项点击事件。  默认无点击事件。 |
| icon | [ToolBarV2ItemIconType](ohos-arkui-advanced-toolbarv2.md#toolbarv2itemicontype) | 否 | 是 | 工具栏子项的图标。  默认不显示图标。 |
| state | [ToolBarV2ItemState](ohos-arkui-advanced-toolbarv2.md#toolbarv2itemstate) | 否 | 是 | 工具栏子项的状态。  默认为ToolBarV2ItemState.ENABLE。 |
| accessibilityText | [ResourceStr](ts-types.md#resourcestr) | 否 | 是 | 工具栏子项的无障碍文本属性。当组件不包含文本属性时，屏幕朗读选中此组件时不播报，使用者无法清楚地知道当前选中了什么组件。为了解决此场景，开发人员可为不包含文字信息的组件设置无障碍文本，当屏幕朗读选中此组件时播报无障碍文本的内容，帮助屏幕朗读的使用者清楚地知道自己选中了什么组件。  默认值为当前项content属性内容。 |
| accessibilityDescription | [ResourceStr](ts-types.md#resourcestr) | 否 | 是 | 工具栏子项的无障碍描述。此描述用于向用户详细解释当前组件，开发人员应为组件的这一属性提供较为详尽的文本说明，以协助用户理解即将执行的操作及其可能产生的后果。特别是当这些后果无法仅从组件的属性和无障碍文本中直接获知时。如果组件同时具备文本属性和无障碍说明属性，当组件被选中时，系统将首先播报组件的文本属性，随后播报无障碍说明属性的内容。  默认值为“单指双击即可执行”。 |
| accessibilityLevel | string | 否 | 是 | 工具栏子项无障碍重要性。用于控制当前项是否可被无障碍辅助服务所识别。  支持的值为：  "auto"：当前组件会转换"yes"。  "yes"：当前组件可被无障碍辅助服务所识别。  "no"：当前组件不可被无障碍辅助服务所识别。  "no-hide-descendants"：当前组件及其所有子组件不可被无障碍辅助服务所识别。  默认值："auto" |

## ToolBarV2ItemAction

PhonePC/2in1TabletTVWearable

type ToolBarV2ItemAction = (index: number) => void

工具栏子项点击事件回调类型。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | number | 是 | 工具栏子项点击事件的回调。  -index: 表示触发事件的工具栏子项索引。 |

## ToolBarV2ItemText

PhonePC/2in1TabletTVWearable

定义工具栏子项的文本。

**装饰器类型：**@ObservedV2

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

### 属性

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| text | [ResourceStr](ts-types.md#resourcestr) | 否 | 否 | 工具栏子项的文本。  装饰器类型：@Trace |
| color | [ColorMetrics](js-apis-arkui-graphics.md#colormetrics12) | 否 | 是 | 工具栏子项的文本的颜色。  默认值：$r('sys.color.font\_primary')  装饰器类型：@Trace |
| activatedColor | [ColorMetrics](js-apis-arkui-graphics.md#colormetrics12) | 否 | 是 | 工具栏子项在激活态下文本的颜色。  默认值：$r('sys.color.font\_emphasize')  装饰器类型：@Trace |

### constructor

PhonePC/2in1TabletTVWearable

constructor(options: ToolBarV2ItemTextOptions)

ToolBarV2ItemText的构造函数。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [ToolBarV2ItemTextOptions](ohos-arkui-advanced-toolbarv2.md#toolbarv2itemtextoptions) | 是 | 工具栏子项文本信息。 |

## ToolBarV2ItemTextOptions

PhonePC/2in1TabletTVWearable

用于构建ToolBarV2ItemText对象。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| text | [ResourceStr](ts-types.md#resourcestr) | 否 | 否 | 工具栏子项的文本。 |
| color | [ColorMetrics](js-apis-arkui-graphics.md#colormetrics12) | 否 | 是 | 工具栏子项的文本的颜色。  默认值：$r('sys.color.font\_primary') |
| activatedColor | [ColorMetrics](js-apis-arkui-graphics.md#colormetrics12) | 否 | 是 | 工具栏子项在激活态下文本的颜色。  默认值：$r('sys.color.font\_emphasize') |

## ToolBarV2ItemImage

PhonePC/2in1TabletTVWearable

定义工具栏子项的普通图标。

**装饰器类型：**@ObservedV2

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

### 属性

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| src | [ResourceStr](ts-types.md#resourcestr) | 否 | 否 | 工具栏子项的图标。  装饰器类型：@Trace |
| color | [ColorMetrics](js-apis-arkui-graphics.md#colormetrics12) | 否 | 是 | 工具栏子项的图标的颜色。  默认值：$r('sys.color.icon\_primary')  装饰器类型：@Trace |
| activatedColor | [ColorMetrics](js-apis-arkui-graphics.md#colormetrics12) | 否 | 是 | 工具栏子项在激活态下图标的颜色。  默认值：$r('sys.color.icon\_emphasize')  装饰器类型：@Trace |

### constructor

PhonePC/2in1TabletTVWearable

constructor(options: ToolBarV2ItemImageOptions)

ToolBarV2ItemImage的构造函数。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [ToolBarV2ItemImageOptions](ohos-arkui-advanced-toolbarv2.md#toolbarv2itemimageoptions) | 是 | 工具栏子项图标信息。 |

## ToolBarV2ItemImageOptions

PhonePC/2in1TabletTVWearable

用于构建ToolBarV2ItemImage对象。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| src | [ResourceStr](ts-types.md#resourcestr) | 否 | 否 | 工具栏子项的图标。 |
| color | [ColorMetrics](js-apis-arkui-graphics.md#colormetrics12) | 否 | 是 | 工具栏子项的图标的颜色。  默认值：$r('sys.color.icon\_primary') |
| activatedColor | [ColorMetrics](js-apis-arkui-graphics.md#colormetrics12) | 否 | 是 | 工具栏子项在激活态下图标的颜色。  默认值：$r('sys.color.icon\_emphasize') |

## ToolBarV2ItemIconType

PhonePC/2in1TabletTVWearable

type ToolBarV2ItemIconType = ToolBarV2ItemImage | ToolBarV2SymbolGlyph

工具栏子项图标内容的联合类型。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

| 类型 | 说明 |
| --- | --- |
| [ToolBarV2ItemImage](ohos-arkui-advanced-toolbarv2.md#toolbarv2itemimage) | 用于定义普通图标。 |
| [ToolBarV2SymbolGlyph](ohos-arkui-advanced-toolbarv2.md#toolbarv2symbolglyph) | 用于定义Symbol图标。 |

## ToolBarV2Modifier

PhonePC/2in1TabletTVWearable

ToolBarV2Modifier提供设置工具栏高度(height)、背景色(backgroundColor)、左右内边距（padding，仅在item小于5个时生效）、是否显示按压态（stateEffect）的方法。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

### backgroundColor

PhonePC/2in1TabletTVWearable

backgroundColor(backgroundColor: ColorMetrics): ToolBarV2Modifier

自定义绘制工具栏背景色的接口，若重载该方法则可进行工具栏背景色的自定义绘制。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| backgroundColor | [ColorMetrics](js-apis-arkui-graphics.md#colormetrics12) | 是 | 工具栏背景色。  默认背景色为$r('sys.color.ohos\_id\_color\_toolbar\_bg')。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ToolBarV2Modifier](ohos-arkui-advanced-toolbarv2.md#toolbarv2modifier) | 设置backgroundColor后的ToolBarV2Modifier对象。 |

### padding

PhonePC/2in1TabletTVWearable

padding(padding: LengthMetrics): ToolBarV2Modifier

自定义绘制工具栏左右内边距的接口，若重载该方法则可进行工具栏左右内边距的自定义绘制。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| padding | [LengthMetrics](js-apis-arkui-graphics.md#lengthmetrics12) | 是 | 工具栏左右内边距，仅在子项数量小于5个时生效。  当子项数量少于5个时，工具栏默认左右内边距为24vp；当子项数量达到或超过5个时，工具栏默认左右内边距为0。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ToolBarV2Modifier](ohos-arkui-advanced-toolbarv2.md#toolbarv2modifier) | 设置padding后的ToolBarV2Modifier对象。 |

### height

PhonePC/2in1TabletTVWearable

height(height: LengthMetrics): ToolBarV2Modifier

自定义绘制工具栏高度的接口，若重载该方法则可进行工具栏高度的自定义绘制，此高度不包含分割线高度。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| height | [LengthMetrics](js-apis-arkui-graphics.md#lengthmetrics12) | 是 | 工具栏高度。  工具栏高度默认为56vp（不包含分割线）。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ToolBarV2Modifier](ohos-arkui-advanced-toolbarv2.md#toolbarv2modifier) | 设置height后的ToolBarV2Modifier对象。 |

### stateEffect

PhonePC/2in1TabletTVWearable

stateEffect(stateEffect: boolean): ToolBarV2Modifier

设置是否显示按压态效果的接口。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| stateEffect | boolean | 是 | 工具栏是否显示按压态效果。  true为显示按压态效果，false为移除按压态效果。默认为true。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ToolBarV2Modifier](ohos-arkui-advanced-toolbarv2.md#toolbarv2modifier) | 设置stateEffect后的ToolBarV2Modifier对象。 |

## ToolBarV2ItemState

PhonePC/2in1TabletTVWearable

工具栏子项状态枚举。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

| 名称 | 值 | 说明 |
| --- | --- | --- |
| ENABLE | 1 | 工具栏子项为正常可点击状态。 |
| DISABLE | 2 | 工具栏子项为不可点击状态。 |
| ACTIVATE | 3 | 工具栏子项为激活状态，可点击。 |

## ToolBarV2SymbolGlyph

PhonePC/2in1TabletTVWearable

ToolBarV2SymbolGlyph定义Symbol图标的属性。

**装饰器类型**：@ObservedV2

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

### 属性

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| normal | [SymbolGlyphModifier](universal-attributes-attribute-symbolglyphmodifier.md#symbolglyphmodifier) | 否 | 否 | 工具栏symbol图标普通态样式。  装饰器类型：@Trace |
| activated | [SymbolGlyphModifier](universal-attributes-attribute-symbolglyphmodifier.md#symbolglyphmodifier) | 否 | 是 | 工具栏symbol图标激活态样式。  默认值：fontColor：$r('sys.color.icon\_emphasize')，fontSize：24vp。  装饰器类型：@Trace |

### constructor

PhonePC/2in1TabletTVWearable

constructor(options: ToolBarV2SymbolGlyphOptions)

ToolBarV2SymbolGlyph的构造函数。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [ToolBarV2SymbolGlyphOptions](ohos-arkui-advanced-toolbarv2.md#toolbarv2symbolglyphoptions) | 是 | Symbol图标信息。 |

## ToolBarV2SymbolGlyphOptions

PhonePC/2in1TabletTVWearable

ToolBarV2SymbolGlyphOptions定义图标的属性。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| normal | [SymbolGlyphModifier](universal-attributes-attribute-symbolglyphmodifier.md#symbolglyphmodifier) | 否 | 否 | 工具栏symbol图标普通态样式。 |
| activated | [SymbolGlyphModifier](universal-attributes-attribute-symbolglyphmodifier.md#symbolglyphmodifier) | 否 | 是 | 工具栏symbol图标激活态样式。  默认值：fontColor：$r('sys.color.icon\_emphasize')，fontSize：24vp。 |

## 示例

PhonePC/2in1TabletTVWearable

### 示例1（工具栏不同状态的默认效果）

该示例展示了工具栏子项state属性分别设置ENABLE、DISABLE、ACTIVATE状态的不同显示效果。

```
1. import { ToolBarV2ItemImage, ToolBarV2ItemState, ToolBarV2ItemText, ToolBarV2Item, ToolBarV2 } from '@kit.ArkUI';

3. @Entry
4. @ComponentV2
5. struct Index {
6. @Local toolbarList: ToolBarV2Item[] = []

8. aboutToAppear() {
9. this.toolbarList.push(new ToolBarV2Item({
10. content: new ToolBarV2ItemText(
11. {
12. text: '剪贴我是超超超超超超超超超长样式'
13. }
14. ),
15. icon: new ToolBarV2ItemImage({
16. src: $r('sys.media.ohos_ic_public_share')
17. }),
18. action: () => {
19. },
20. }))
21. this.toolbarList.push(
22. new ToolBarV2Item({
23. content: new ToolBarV2ItemText(
24. {
25. text: '拷贝'
26. }
27. ),
28. icon: new ToolBarV2ItemImage({
29. src: $r('sys.media.ohos_ic_public_copy')
30. }),
31. action: () => {
32. },
33. state: ToolBarV2ItemState.DISABLE
34. })
35. )
36. this.toolbarList.push(
37. new ToolBarV2Item({
38. content: new ToolBarV2ItemText(
39. {
40. text: '粘贴'
41. }
42. ),
43. icon: new ToolBarV2ItemImage({
44. src: $r('sys.media.ohos_ic_public_paste')
45. }),
46. action: () => {
47. },
48. state: ToolBarV2ItemState.ACTIVATE
49. })
50. )
51. this.toolbarList.push(
52. new ToolBarV2Item({
53. content: new ToolBarV2ItemText(
54. {
55. text: '全选'
56. }
57. ),
58. icon: new ToolBarV2ItemImage({
59. src: $r('sys.media.ohos_ic_public_select_all')
60. }),
61. action: () => {
62. },
63. })
64. )
65. this.toolbarList.push(
66. new ToolBarV2Item({
67. content: new ToolBarV2ItemText(
68. {
69. text: '分享'
70. }
71. ),
72. icon: new ToolBarV2ItemImage({
73. src: $r('sys.media.ohos_ic_public_share')
74. }),
75. action: () => {
76. },
77. })
78. )
79. this.toolbarList.push(
80. new ToolBarV2Item({
81. content: new ToolBarV2ItemText(
82. {
83. text: '分享'
84. }
85. ),
86. icon: new ToolBarV2ItemImage({
87. src: $r('sys.media.ohos_ic_public_share')
88. }),
89. action: () => {
90. },
91. })
92. )
93. }

95. build() {
96. Row() {
97. Stack() {
98. Column() {
99. ToolBarV2({
100. activatedIndex: 2,
101. toolBarList: this.toolbarList,
102. })
103. }
104. }.align(Alignment.Bottom)
105. .width('100%').height('100%')
106. }
107. }
108. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3b/v3/AmwegHXOTb2vy_OmCTcGSQ/zh-cn_image_0000002558766664.png?HW-CC-KV=V1&HW-CC-Date=20260429T055305Z&HW-CC-Expire=86400&HW-CC-Sign=C4AD5DAE460BC1F1992BE829C70AD75329E3AAF09D9721E87A62589C1A56B8D3)

### 示例2（设置工具栏自定义样式）

该示例通过设置属性ToolBarV2Modifier自定义工具栏高度、背景色、按压效果等样式。

```
1. import {
2. SymbolGlyphModifier,
3. DividerModifier,
4. LengthMetrics,
5. ColorMetrics,
6. ToolBarV2Item,
7. ToolBarV2Modifier,
8. ToolBarV2ItemText,
9. ToolBarV2ItemImage,
10. ToolBarV2,
11. ToolBarV2ItemState,
12. ToolBarV2SymbolGlyph
13. } from '@kit.ArkUI';

15. @Entry
16. @ComponentV2
17. struct Index {
18. @Local toolbarList: ToolBarV2Item[] = [];
19. private toolBarModifier: ToolBarV2Modifier =
20. new ToolBarV2Modifier().height(LengthMetrics.vp(52))
21. .backgroundColor(ColorMetrics.resourceColor(Color.Transparent))
22. .stateEffect(false);
23. @Local dividerModifier: DividerModifier = new DividerModifier().height(0);

25. aboutToAppear() {
26. this.toolbarList.push(
27. new ToolBarV2Item({
28. content: new ToolBarV2ItemText({
29. text: 'Long long long long long long long long text',
30. activatedColor: ColorMetrics.resourceColor($r('sys.color.font_primary'))
31. }),
32. icon: new ToolBarV2SymbolGlyph({
33. normal: new SymbolGlyphModifier($r('sys.symbol.ohos_star')).fontColor([Color.Green]),
34. activated: new SymbolGlyphModifier($r('sys.symbol.ohos_star')).fontColor([Color.Red]),
35. }),
36. action: () => {
37. },
38. state: ToolBarV2ItemState.ACTIVATE,
39. })
40. )
41. this.toolbarList.push(
42. new ToolBarV2Item({
43. content: new ToolBarV2ItemText({
44. text: 'Copy',
45. activatedColor: ColorMetrics.resourceColor('#ffec5d5d')
46. }),
47. icon: new ToolBarV2ItemImage({
48. src: $r('sys.media.ohos_ic_public_copy'),
49. color: ColorMetrics.resourceColor('#ff18cb53'),
50. activatedColor: ColorMetrics.resourceColor('#ffec5d5d'),
51. }),
52. action: () => {
53. },
54. state: ToolBarV2ItemState.DISABLE,
55. }))
56. this.toolbarList.push(
57. new ToolBarV2Item({
58. content: new ToolBarV2ItemText({
59. text: 'Paste',
60. color: ColorMetrics.resourceColor('#ff18cb53')
61. }),
62. icon: new ToolBarV2ItemImage({
63. src: $r('sys.media.ohos_ic_public_paste'),
64. }),
65. action: () => {
66. },
67. state: ToolBarV2ItemState.ACTIVATE,
68. })
69. )
70. this.toolbarList.push(
71. new ToolBarV2Item({
72. content: new ToolBarV2ItemText({
73. text: 'All',
74. }),
75. icon: new ToolBarV2ItemImage({
76. src: $r('sys.media.ohos_ic_public_select_all'),
77. }),
78. action: () => {
79. },
80. state: ToolBarV2ItemState.ACTIVATE,
81. }))
82. this.toolbarList.push(
83. new ToolBarV2Item({
84. content: new ToolBarV2ItemText({
85. text: '分享',
86. }),
87. icon: new ToolBarV2ItemImage({
88. src: $r('sys.media.ohos_ic_public_share'),
89. }),
90. action: () => {
91. },
92. }))
93. this.toolbarList.push(
94. new ToolBarV2Item({
95. content: new ToolBarV2ItemText({
96. text: '分享',
97. }),
98. icon: new ToolBarV2ItemImage({
99. src: $r('sys.media.ohos_ic_public_share'),
100. }),
101. action: () => {
102. },
103. })
104. )
105. }

107. build() {
108. Row() {
109. Stack() {
110. Column() {
111. ToolBarV2({
112. toolBarModifier: this.toolBarModifier,
113. dividerModifier: this.dividerModifier,
114. activatedIndex: 0,
115. toolBarList: this.toolbarList,
116. })
117. .height(52)
118. }
119. }.align(Alignment.Bottom)
120. .width('100%').height('100%')
121. }
122. }
123. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/21/v3/q72mqTEeQc-KpYDyH2Jksw/zh-cn_image_0000002558607004.png?HW-CC-KV=V1&HW-CC-Date=20260429T055305Z&HW-CC-Expire=86400&HW-CC-Sign=388AEB7E0556C1E4F100077366F67D096FEAED0CF590A0086945CFB0ECA7E376)

### 示例3（设置工具栏自定义播报）

该示例通过设置工具栏子项属性accessibilityText、accessibilityDescription、accessibilityLevel自定义屏幕朗读播报文本。

```
1. import {
2. DividerModifier,
3. LengthMetrics,
4. ColorMetrics,
5. ToolBarV2Item,
6. ToolBarV2Modifier,
7. ToolBarV2ItemText,
8. ToolBarV2ItemImage,
9. ToolBarV2,
10. ToolBarV2ItemState,
11. } from '@kit.ArkUI';

13. @Entry
14. @ComponentV2
15. struct Index {
16. @Local toolbarList: ToolBarV2Item[] = [];
17. private toolBarModifier: ToolBarV2Modifier =
18. new ToolBarV2Modifier().height(LengthMetrics.vp(52))
19. .backgroundColor(ColorMetrics.resourceColor(Color.Transparent))
20. .stateEffect(false);
21. @Local dividerModifier: DividerModifier = new DividerModifier().height(0);

23. aboutToAppear() {
24. this.toolbarList.push(
25. new ToolBarV2Item({
26. content: new ToolBarV2ItemText({
27. text: '剪贴我是超超超超超超超超超长样式',
28. }),
29. icon: new ToolBarV2ItemImage({
30. src: $r('sys.media.ohos_ic_public_share')
31. }),
32. action: () => {
33. },
34. accessibilityText: '剪贴', // 该项屏幕朗读播报文本为‘剪贴’
35. accessibilityDescription: '单指双击即可剪贴', // 该项屏幕朗读播报描述为'单指双击即可剪贴'
36. accessibilityLevel: 'yes'  // 该项可被无障碍屏幕朗读聚焦
37. })
38. )
39. this.toolbarList.push(
40. new ToolBarV2Item({
41. content: new ToolBarV2ItemText({
42. text: '拷贝',
43. }),
44. icon: new ToolBarV2ItemImage({
45. src: $r('sys.media.ohos_ic_public_copy'),
46. }),
47. action: () => {
48. },
49. state: ToolBarV2ItemState.DISABLE,
50. accessibilityLevel: 'no'  // 该项将无法被无障碍屏幕朗读聚焦
51. }))
52. this.toolbarList.push(
53. new ToolBarV2Item({
54. content: new ToolBarV2ItemText({
55. text: '粘贴',
56. }),
57. icon: new ToolBarV2ItemImage({
58. src: $r('sys.media.ohos_ic_public_paste'),
59. }),
60. action: () => {
61. },
62. state: ToolBarV2ItemState.ACTIVATE,
63. })
64. )
65. this.toolbarList.push(
66. new ToolBarV2Item({
67. content: new ToolBarV2ItemText({
68. text: '全选',
69. }),
70. icon: new ToolBarV2ItemImage({
71. src: $r('sys.media.ohos_ic_public_select_all'),
72. }),
73. action: () => {
74. },
75. }))
76. this.toolbarList.push(
77. new ToolBarV2Item({
78. content: new ToolBarV2ItemText({
79. text: '分享',
80. }),
81. icon: new ToolBarV2ItemImage({
82. src: $r('sys.media.ohos_ic_public_share'),
83. }),
84. action: () => {
85. },
86. }))
87. this.toolbarList.push(
88. new ToolBarV2Item({
89. content: new ToolBarV2ItemText({
90. text: '分享',
91. }),
92. icon: new ToolBarV2ItemImage({
93. src: $r('sys.media.ohos_ic_public_share'),
94. }),
95. action: () => {
96. },
97. })
98. )
99. }

101. build() {
102. Row() {
103. Stack() {
104. Column() {
105. ToolBarV2({
106. toolBarModifier: this.toolBarModifier,
107. dividerModifier: this.dividerModifier,
108. activatedIndex: 0,
109. toolBarList: this.toolbarList,
110. })
111. .height(52)
112. }
113. }.align(Alignment.Bottom)
114. .width('100%').height('100%')
115. }
116. }
117. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dc/v3/4M7pmZ7qSU6kvn_S5XO1vQ/zh-cn_image_0000002558766664.png?HW-CC-KV=V1&HW-CC-Date=20260429T055305Z&HW-CC-Expire=86400&HW-CC-Sign=EF0CBEFB0ADE3C6DF951AE85EDB577A90E8ED7AD6D01F1F4F5208CA85AF24342)
