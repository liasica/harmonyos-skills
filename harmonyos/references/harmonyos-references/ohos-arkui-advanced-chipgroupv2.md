---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-chipgroupv2
title: ChipGroupV2
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 系统预置UI组件库 > ChipGroupV2
category: harmonyos-references
scraped_at: 2026-09-05T06:17:29+08:00
doc_updated_at: 2026-09-04
content_hash: sha256:130a181c16e6cf3fd394f66d691dcf56c991b9c1727fd9dd26e962bcb8909abb
---

ChipGroupV2组件提供操作块群组容器，支持单选或多选、自定义样式和间距、以及尾部自定义内容。该组件适用于文件或资源内容的分类、标签选择、筛选等场景，可帮助开发者快速构建美观且交互丰富的标签组界面。

该组件基于[状态管理（V2）](../harmonyos-guides/arkts-state-management-overview.md#状态管理v2)实现，相较于[状态管理（V1）](../harmonyos-guides/arkts-state-management-overview.md#状态管理v1)，状态管理（V2）增强了对数据对象的深度观察与管理能力，不再局限于组件层级。借助状态管理（V2），开发者可以更灵活地控制组件的数据和状态，实现更高效的用户界面刷新。

**说明** 

* 本模块接口仅可在Stage模型下使用。
* 如果ChipGroupV2设置[通用属性](ts-component-general-attributes.md)或[通用事件](ts-component-general-events.md)，编译工具链会额外生成节点\_\_Common\_\_，并将通用属性或通用事件挂载在\_\_Common\_\_上，而不是直接应用到ChipGroupV2本身。这可能导致开发者设置的通用属性或通用事件不生效或不符合预期，因此，不建议ChipGroupV2设置通用属性和通用事件。

**起始版本：** 26.0.0

## 导入模块

```ts
import { ChipV2Size, ChipGroupV2 } from '@kit.ArkUI';
```

## 子组件

无

## ChipGroupV2

ChipGroupV2({

items: ChipGroupV2Items,

$items?: Callback<ChipGroupV2Items>,

itemStyle?: ChipGroupV2ItemStyle,

selectedIndexes?: Array<number>,

$selectedIndexes?: Callback<Array<number>>,

multiple?: boolean,

chipGroupSpace?: ChipGroupV2Space,

chipGroupPadding?: ChipGroupV2Padding,

onChange?: Callback<Array<number>>,

suffix?: Callback<void>

})

**起始版本：** 26.0.0

**装饰器类型：** @ComponentV2

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

| 名称 | 类型 | 必填 | 装饰器类型 | 说明 |
| --- | --- | --- | --- | --- |
| items | [ChipGroupV2Items](ohos-arkui-advanced-chipgroupv2.md#chipgroupv2items) | 是 | @Require  @Param | 每个ChipV2的特定属性，参考[ChipGroupV2ItemConfig](ohos-arkui-advanced-chipgroupv2.md#chipgroupv2itemconfig)类型。  值为undefined或空数组时，ChipGroupV2不渲染内部的[ChipV2](ohos-arkui-advanced-chipv2.md)。 |
| $items | [Callback](ts-types.md#callback12)<[ChipGroupV2Items](ohos-arkui-advanced-chipgroupv2.md#chipgroupv2items)> | 否 | @Event | ChipV2项的双向绑定回调方法，当需要监听或修改ChipV2项列表时传入此回调。  默认值：undefined，不触发回调。 |
| itemStyle | [ChipGroupV2ItemStyle](ohos-arkui-advanced-chipgroupv2.md#chipgroupv2itemstyle) | 否 | @Param | ChipV2的style属性，如颜色、大小等，参考[ChipGroupV2ItemStyle](ohos-arkui-advanced-chipgroupv2.md#chipgroupv2itemstyle)类型。  默认值：  { size: ChipV2Size.NORMAL, backgroundColor: $r('sys.color.ohos\_id\_color\_button\_normal'), fontColor: $r('sys.color.ohos\_id\_color\_text\_primary'), selectedFontColor: $r('sys.color.ohos\_id\_color\_text\_primary\_contrary'), selectedBackgroundColor: $r('sys.color.ohos\_id\_color\_emphasize') }  值为undefined时，按默认值处理。  图标填充色（[fillColor](ohos-arkui-advanced-chipv2.md#chipv2imageiconconfig)和[activatedFillColor](ohos-arkui-advanced-chipv2.md#chipv2imageiconconfig)）的设置与对应的字体颜色保持一致：未选中状态下fillColor与[fontColor](ohos-arkui-advanced-chipgroupv2.md#chipgroupv2itemstyleconfig)保持一致，选中状态下activatedFillColor与[selectedFontColor](ohos-arkui-advanced-chipgroupv2.md#chipgroupv2itemstyleconfig)保持一致。如果需要设置不同的颜色，可以在传入items时使用[prefixSymbolIcon](ohos-arkui-advanced-chipgroupv2.md#chipgroupv2itemconfig)和[suffixSymbolIcon](ohos-arkui-advanced-chipgroupv2.md#chipgroupv2itemconfig)。 |
| selectedIndexes | Array<number> | 否 | @Param | 被选中ChipV2的索引。  取值范围：索引值必须为大于等于0且小于items数组长度的整数。传入不在取值范围内的索引时，该索引不生效。  默认值：[0]  值为undefined时，按默认值处理。  当multiple等于false时，如果没有传入selectedIndexes，默认是第一个ChipV2被选中，如果传入的selectedIndexes有多个元素时，默认第一个索引的ChipV2被选中。  当multiple等于true时，如果没有传入selectedIndexes，默认第一个ChipV2被选中；如果传入的selectedIndexes有多个元素时，所有对应索引的ChipV2均被选中。 |
| $selectedIndexes | [Callback](ts-types.md#callback12)<Array<number>> | 否 | @Event | 被选中ChipV2索引的双向绑定回调方法，当需要监听或修改选中的ChipV2索引时传入此回调。  默认值：undefined，不触发回调。 |
| multiple | boolean | 否 | @Param | 是否选中多个ChipV2。  true：支持多个ChipV2选中；false：仅支持单个ChipV2选中。  默认值：false  值为undefined时，按默认值处理。 |
| chipGroupSpace | [ChipGroupV2Space](ohos-arkui-advanced-chipgroupv2.md#chipgroupv2space) | 否 | @Param | 左右内边距及ChipV2之间间距。设置后可调整ChipGroupV2的左右内边距和ChipV2之间的间距，增大间距使布局更宽松，减小间距使布局更紧凑。参考[ChipGroupV2Space](ohos-arkui-advanced-chipgroupv2.md#chipgroupv2space)类型。  默认值：{ itemSpace: 8, startSpace: 16, endSpace: 16 }  单位：vp  值为undefined时，按默认值处理。 |
| chipGroupPadding | [ChipGroupV2Padding](ohos-arkui-advanced-chipgroupv2.md#chipgroupv2padding) | 否 | @Param | 设置ChipGroupV2的上下内边距，以控制整体高度。类型为[ChipGroupV2Padding](ohos-arkui-advanced-chipgroupv2.md#chipgroupv2padding)。  默认值：{ top: 14, bottom: 14 }  单位：vp  值为undefined时，按默认值处理。 |
| onChange | [Callback](ts-types.md#callback12)<Array<number>> | 否 | @Event | ChipV2状态改变时的回调方法，用于响应ChipV2选中状态变化。当需要监听ChipV2选中状态改变时传入此回调。  触发场景：用户点击ChipV2改变选中状态时触发，返回当前选中ChipV2的索引数组。  默认值：undefined，不触发事件。 |
| suffix | [Callback](ts-types.md#callback12)<void> | 否 | @BuilderParam | 支持开发者自定义builder，如需在组件最右侧显示自定义内容可配置suffix属性，使用属性suffix需引用[ChipGroupV2IconGroupSuffix](ohos-arkui-advanced-chipgroupv2.md#chipgroupv2icongroupsuffix)接口。  默认值：undefined，不在最右侧显示自定义内容。 |

### build

build(): void

build函数用于构造ChipGroupV2高级组件。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

## ChipGroupV2Item

ChipGroupV2Item定义了ChipGroupV2组件中的单个操作块项。

**起始版本：** 26.0.0

**装饰器类型：** @ObservedV2

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

### 属性

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| prefixIcon | [ChipV2PrefixImageIcon](ohos-arkui-advanced-chipv2.md#chipv2prefiximageicon) | 否 | 是 | 前缀图标属性，用于在ChipV2文本前显示Image图标。当需要在ChipV2左侧显示图标标识时设置此属性。  默认值：没有前缀Image图标。  值为undefined时，按默认值处理。  **装饰器类型：** @Trace |
| prefixSymbolIcon | [ChipV2PrefixSymbolIcon](ohos-arkui-advanced-chipv2.md#chipv2prefixsymbolicon) | 否 | 是 | 前缀Symbol图标属性，用于在ChipV2文本前显示Symbol图标。当需要在ChipV2左侧显示Symbol图标标识时设置此属性。  默认值：没有前缀Symbol图标。  值为undefined时，按默认值处理。  **装饰器类型：** @Trace |
| label | [ChipV2Label](ohos-arkui-advanced-chipv2.md#chipv2label) | 否 | 否 | ChipV2文本属性。  **装饰器类型：** @Trace |
| suffixIcon | [ChipV2SuffixImageIcon](ohos-arkui-advanced-chipv2.md#chipv2suffiximageicon) | 否 | 是 | 后缀图标属性，用于在ChipV2文本后显示Image图标。设置该属性时，allowClose属性将不生效。  默认值：不显示后缀Image图标。  值为undefined时，按默认值处理。  **装饰器类型：** @Trace |
| suffixSymbolIcon | [ChipV2SuffixSymbolIcon](ohos-arkui-advanced-chipv2.md#chipv2suffixsymbolicon) | 否 | 是 | 后缀Symbol图标属性，用于在ChipV2文本后显示Symbol图标。设置该属性时，allowClose属性将不生效。  默认值：不显示后缀Symbol图标。  值为undefined时，按默认值处理。  **装饰器类型：** @Trace |
| allowClose | boolean | 否 | 是 | 关闭图标是否显示。取值原则：true表示关闭图标显示，false表示关闭图标不显示。当传入suffixIcon或suffixSymbolIcon参数时，allowClose不生效；未传入suffixIcon和suffixSymbolIcon参数时，allowClose决定是否显示关闭图标。  默认值：false  值为undefined时，按默认值处理。  **装饰器类型：** @Trace |
| closeIcon | [ChipV2CloseConfig](ohos-arkui-advanced-chipv2.md#chipv2closeconfig) | 否 | 是 | 关闭图标的配置，包括无障碍属性配置。当需要自定义关闭图标的大小或无障碍属性时设置此属性。  默认值：  - fontSize默认值：size为ChipV2Size.SMALL时，默认值为$r('sys.float.chip\_small\_font\_size')；其他情况默认值为$r('sys.float.chip\_normal\_font\_size')。  - 无障碍默认值：无无障碍描述。  值为undefined时，按默认值处理。  **装饰器类型：** @Trace |
| accessibilityDescription | [ResourceStr](ts-types.md#resourcestr) | 否 | 是 | 无障碍描述。用于向用户详细解释组件，开发人员应为该属性提供详尽的文本说明，以协助用户理解操作及其可能结果，特别是当这些结果无法仅从组件的属性和无障碍文本中直接获知时。如果组件同时具备文本属性和无障碍说明属性，当组件被选中时，系统将首先播报组件的文本属性，随后播报无障碍说明属性的内容。  默认值：空字符串。  值为undefined时，按默认值处理。  **装饰器类型：** @Trace |
| accessibilityLevel | string | 否 | 是 | 无障碍重要性。用于控制组件是否可被无障碍辅助服务所识别。  支持的值为：  "auto"：当前组件会转换为"yes"。  "yes"：当前组件可被无障碍辅助服务所识别。  "no"：当前组件不可被无障碍辅助服务所识别。  "no-hide-descendants"：当前组件及其所有子组件不可被无障碍辅助服务所识别。  传入不在支持范围内的值时，按默认值处理。  默认值："auto"  值为undefined时，按默认值处理。  **装饰器类型：** @Trace |

**说明** 

1. 如果需要在显示后缀图标（suffixIcon或suffixSymbolIcon）的同时支持关闭功能，建议在suffixIcon或suffixSymbolIcon的点击事件中实现删除逻辑，或使用其他交互方式替代。

### constructor

constructor(config: ChipGroupV2ItemConfig)

ChipGroupV2Item的构造函数。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| config | [ChipGroupV2ItemConfig](ohos-arkui-advanced-chipgroupv2.md#chipgroupv2itemconfig) | 是 | ChipGroupV2项配置。 |

## ChipGroupV2ItemConfig

ChipGroupV2ItemConfig定义每个ChipV2的非通用属性配置。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| prefixIcon | [ChipV2PrefixImageIconConfig](ohos-arkui-advanced-chipv2.md#chipv2prefiximageiconconfig) | 否 | 是 | 前缀Image图标属性，用于在ChipV2文本前显示Image图标。当需要在ChipV2左侧显示图标标识时设置此属性。  默认值：没有前缀Image图标。  值为undefined时，按默认值处理。 |
| prefixSymbolIcon | [ChipV2PrefixSymbolIconConfig](ohos-arkui-advanced-chipv2.md#chipv2prefixsymboliconconfig) | 否 | 是 | 前缀Symbol图标属性，用于在ChipV2文本前显示Symbol图标。当需要在ChipV2左侧显示Symbol图标标识时设置此属性。  默认值：没有前缀Symbol图标。  值为undefined时，按默认值处理。 |
| label | [ChipV2LabelConfig](ohos-arkui-advanced-chipv2.md#chipv2labelconfig) | 否 | 否 | 文本属性。 |
| suffixIcon | [ChipV2SuffixImageIconConfig](ohos-arkui-advanced-chipv2.md#chipv2suffiximageiconconfig) | 否 | 是 | 后缀Image图标属性，用于在ChipV2文本后显示Image图标。设置该属性时，allowClose属性将不生效。  默认值：不显示后缀Image图标。  值为undefined时，按默认值处理。 |
| suffixSymbolIcon | [ChipV2SuffixSymbolIconConfig](ohos-arkui-advanced-chipv2.md#chipv2suffixsymboliconconfig) | 否 | 是 | 后缀Symbol图标属性，用于在ChipV2文本后显示Symbol图标。设置该属性时，allowClose属性将不生效。  默认值：不显示后缀Symbol图标。  值为undefined时，按默认值处理。 |
| allowClose | boolean | 否 | 是 | 关闭图标是否显示。取值原则：true表示关闭图标显示，false表示关闭图标不显示。  当传入suffixIcon或suffixSymbolIcon参数时，allowClose不生效；未传入suffixIcon和suffixSymbolIcon参数时，allowClose决定是否显示关闭图标。  默认值：false  值为undefined时，按默认值处理。 |
| closeIcon | [ChipV2CloseConfig](ohos-arkui-advanced-chipv2.md#chipv2closeconfig) | 否 | 是 | 关闭图标的配置，包括无障碍属性配置。当需要自定义关闭图标的大小或无障碍属性时设置此属性。  默认值：  - fontSize默认值：size为ChipV2Size.SMALL时，默认值为$r('sys.float.chip\_small\_font\_size')；其他情况默认值为$r('sys.float.chip\_normal\_font\_size')。  - 无障碍默认值：无无障碍描述。  值为undefined时，按默认值处理。 |
| accessibilityDescription | [ResourceStr](ts-types.md#resourcestr) | 否 | 是 | ChipGroupV2中ChipV2项的无障碍描述。此描述用于向用户详细解释ChipGroupV2中ChipV2项，开发人员应为ChipGroupV2中ChipV2项的属性提供较为详尽的文本说明，以协助用户理解即将执行的操作及其可能产生的结果，特别是当这些结果无法仅从ChipGroupV2中ChipV2项的属性和无障碍文本中直接获知时。如果ChipGroupV2中ChipV2项同时具备文本属性和无障碍说明属性，当ChipGroupV2中ChipV2项被选中时，系统将首先播报ChipGroupV2中ChipV2项的文本属性，随后播报无障碍说明属性的内容。  默认值：空字符串。  值为undefined时，按默认值处理。 |
| accessibilityLevel | string | 否 | 是 | ChipGroupV2中ChipV2项无障碍重要性。用于控制ChipGroupV2中ChipV2项是否可被无障碍辅助服务所识别。  支持的值为：  "auto"：ChipGroupV2中ChipV2项会转换为"yes"。  "yes"：ChipGroupV2中ChipV2项可被无障碍辅助服务所识别。  "no"：ChipGroupV2中ChipV2项不可被无障碍辅助服务所识别。  "no-hide-descendants"：ChipGroupV2中ChipV2项及其所有子组件不可被无障碍辅助服务所识别。  传入不在支持范围内的值时，按默认值处理。  默认值："auto"  值为undefined时，按默认值处理。 |

## ChipGroupV2Items

ChipGroupV2Items定义了ChipGroupV2项的数组类，继承自Array<[ChipGroupV2Item](ohos-arkui-advanced-chipgroupv2.md#chipgroupv2item)>。

**起始版本：** 26.0.0

**装饰器类型：** @ObservedV2

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

### constructor

constructor(items: ChipGroupV2ItemConfig[])

ChipGroupV2Items的构造函数。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| items | [ChipGroupV2ItemConfig](ohos-arkui-advanced-chipgroupv2.md#chipgroupv2itemconfig)[] | 是 | ChipGroupV2项配置数组。 |

## ChipGroupV2ItemStyle

ChipGroupV2ItemStyle定义了ChipV2的共通属性类。

**起始版本：** 26.0.0

**装饰器类型：** @ObservedV2

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

### 属性

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| size | [ChipV2Size](ohos-arkui-advanced-chipv2.md#chipv2size) | [SizeT](js-apis-arkui-graphics.md#sizett12)<[LengthMetrics](js-apis-arkui-graphics.md#lengthmetrics12)> | 否 | 是 | ChipV2尺寸。  默认值：ChipV2Size.NORMAL  值为undefined时，按默认值处理。  **装饰器类型：** @Trace |
| backgroundColor | [ColorMetrics](js-apis-arkui-graphics.md#colormetrics12) | 否 | 是 | ChipV2背景颜色。  默认值：$r('sys.color.ohos\_id\_color\_button\_normal')  值为undefined时，按默认值处理。  **装饰器类型：** @Trace |
| fontColor | [ColorMetrics](js-apis-arkui-graphics.md#colormetrics12) | 否 | 是 | ChipV2文字颜色。  默认值：$r('sys.color.ohos\_id\_color\_text\_primary')  值为undefined时，按默认值处理。  **装饰器类型：** @Trace |
| selectedFontColor | [ColorMetrics](js-apis-arkui-graphics.md#colormetrics12) | 否 | 是 | ChipV2选中时的文字颜色。设置后，当ChipV2被选中时，label文本会显示此颜色，替代未选中状态下的fontColor。  默认值：$r('sys.color.ohos\_id\_color\_text\_primary\_contrary')  值为undefined时，按默认值处理。  **装饰器类型：** @Trace |
| selectedBackgroundColor | [ColorMetrics](js-apis-arkui-graphics.md#colormetrics12) | 否 | 是 | ChipV2选中时的背景颜色。设置后，当ChipV2被选中时，背景会填充此颜色，替代未选中状态下的backgroundColor。  默认值：$r('sys.color.ohos\_id\_color\_emphasize')  值为undefined时，按默认值处理。  **装饰器类型：** @Trace |
| backgroundSystemMaterial | uiMaterial.[Material](arkts-apis-uimaterial.md#material) | 否 | 是 | 设置组件系统材质样式。需要将组件放置在Navigation或NavDestination的标题栏子树，或横向Tabs的底部TabBar子树中，材质效果才会生效。不同材质具有不同的效果，能够影响组件的背景色[backgroundColor](ts-universal-attributes-background.md#backgroundcolor)、边框颜色[borderColor](ts-universal-attributes-border.md#bordercolor)、边框宽度[borderWidth](ts-universal-attributes-border.md#borderwidth)、阴影[shadow](ts-universal-attributes-image-effect.md#shadow)效果、材质层滤镜效果[materialFilter](ts-universal-attributes-filter-effect.md#materialfilter23)。  默认值：undefined，不应用材质样式。  **装饰器类型：** @Trace |
| selectedBackgroundSystemMaterial | uiMaterial.[Material](arkts-apis-uimaterial.md#material) | 否 | 是 | 设置组件选中状态下的系统材质样式。需要将组件放置在Navigation或NavDestination的标题栏子树，或横向Tabs的底部TabBar子树中，材质效果才会生效。设置后，当ChipV2被选中时，应用此材质样式，替代未选中状态下的backgroundSystemMaterial。不同材质具有不同的效果，能够影响组件的背景色[backgroundColor](ts-universal-attributes-background.md#backgroundcolor)、边框颜色[borderColor](ts-universal-attributes-border.md#bordercolor)、边框宽度[borderWidth](ts-universal-attributes-border.md#borderwidth)、阴影[shadow](ts-universal-attributes-image-effect.md#shadow)效果、材质层滤镜效果[materialFilter](ts-universal-attributes-filter-effect.md#materialfilter23)。  默认值：undefined，不应用材质样式。  **装饰器类型：** @Trace |

### constructor

constructor(config: ChipGroupV2ItemStyleConfig)

ChipGroupV2ItemStyle的构造函数。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| config | [ChipGroupV2ItemStyleConfig](ohos-arkui-advanced-chipgroupv2.md#chipgroupv2itemstyleconfig) | 是 | ChipGroupV2项样式配置。 |

## ChipGroupV2ItemStyleConfig

ChipGroupV2ItemStyleConfig定义了ChipV2的共通属性配置。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| size | [ChipV2Size](ohos-arkui-advanced-chipv2.md#chipv2size) | [SizeT](js-apis-arkui-graphics.md#sizett12)<[LengthMetrics](js-apis-arkui-graphics.md#lengthmetrics12)> | 否 | 是 | ChipV2尺寸，使用时需要从ChipV2组件引入ChipV2Size类型。  默认值：ChipV2Size.NORMAL  值为undefined时，按默认值处理。 |
| backgroundColor | [ColorMetrics](js-apis-arkui-graphics.md#colormetrics12) | 否 | 是 | ChipV2背景颜色。  默认值：$r('sys.color.ohos\_id\_color\_button\_normal')  值为undefined时，按默认值处理。 |
| fontColor | [ColorMetrics](js-apis-arkui-graphics.md#colormetrics12) | 否 | 是 | ChipV2文字颜色。  默认值：$r('sys.color.ohos\_id\_color\_text\_primary')  值为undefined时，按默认值处理。 |
| selectedFontColor | [ColorMetrics](js-apis-arkui-graphics.md#colormetrics12) | 否 | 是 | ChipV2选中时的文字颜色。设置后，当ChipV2被选中时，label文本会显示此颜色，替代未选中状态下的fontColor。  默认值：$r('sys.color.ohos\_id\_color\_text\_primary\_contrary')  值为undefined时，按默认值处理。 |
| selectedBackgroundColor | [ColorMetrics](js-apis-arkui-graphics.md#colormetrics12) | 否 | 是 | ChipV2选中时的背景颜色。设置后，当ChipV2被选中时，背景会填充此颜色，替代未选中状态下的backgroundColor。  默认值：$r('sys.color.ohos\_id\_color\_emphasize')  值为undefined时，按默认值处理。 |
| backgroundSystemMaterial | uiMaterial.[Material](arkts-apis-uimaterial.md#material) | 否 | 是 | 设置组件系统材质样式。需要将组件放置在Navigation或NavDestination的标题栏子树，或横向Tabs的底部TabBar子树中，材质效果才会生效。不同材质具有不同的效果，能够影响组件的背景色[backgroundColor](ts-universal-attributes-background.md#backgroundcolor)、边框颜色[borderColor](ts-universal-attributes-border.md#bordercolor)、边框宽度[borderWidth](ts-universal-attributes-border.md#borderwidth)、阴影[shadow](ts-universal-attributes-image-effect.md#shadow)效果、材质层滤镜效果[materialFilter](ts-universal-attributes-filter-effect.md#materialfilter23)。  默认值：undefined，不应用材质样式。 |
| selectedBackgroundSystemMaterial | uiMaterial.[Material](arkts-apis-uimaterial.md#material) | 否 | 是 | 设置组件选中状态下的系统材质样式。需要将组件放置在Navigation或NavDestination的标题栏子树，或横向Tabs的底部TabBar子树中，材质效果才会生效。设置后，当ChipV2被选中时，应用此材质样式，替代未选中状态下的backgroundSystemMaterial。不同材质具有不同的效果，能够影响组件的背景色[backgroundColor](ts-universal-attributes-background.md#backgroundcolor)、边框颜色[borderColor](ts-universal-attributes-border.md#bordercolor)、边框宽度[borderWidth](ts-universal-attributes-border.md#borderwidth)、阴影[shadow](ts-universal-attributes-image-effect.md#shadow)效果、材质层滤镜效果[materialFilter](ts-universal-attributes-filter-effect.md#materialfilter23)。  默认值：undefined，不应用材质样式。 |

## ChipGroupV2Space

ChipGroupV2Space定义了ChipGroupV2左右内边距，以及ChipV2与ChipV2之间的间距。

**起始版本：** 26.0.0

**装饰器类型：** @ObservedV2

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

### 属性

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| itemSpace | string | number | 否 | 是 | ChipV2与ChipV2之间的间距（不支持百分比）。增大间距会使相邻ChipV2之间更分散，整体布局更宽松；减小间距会使ChipV2更紧凑。  取值范围：  - number类型：[0, +∞)，如0、8、16、24.5。  - string类型：单位为fp | vp | px | lpx且数值部分大于等于0的字符串，如"8vp"、"16fp"、"12px"、"10lpx"。  - 不支持：负数、百分比单位、无效字符串格式。  传入不在取值范围内或不支持格式的值时，按默认值处理。  默认值：8  单位：vp  值为undefined时，按默认值处理。  **装饰器类型：** @Trace |
| startSpace | [Length](ts-types.md#length) | 否 | 是 | 左侧内边距（不支持百分比）。  默认值：16  单位：vp  值为undefined时，按默认值处理。  **装饰器类型：** @Trace |
| endSpace | [Length](ts-types.md#length) | 否 | 是 | 右侧内边距（不支持百分比）。  默认值：16  单位：vp  值为undefined时，按默认值处理。  **装饰器类型：** @Trace |

### constructor

constructor(config: ChipGroupV2SpaceConfig)

ChipGroupV2Space的构造函数。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| config | [ChipGroupV2SpaceConfig](ohos-arkui-advanced-chipgroupv2.md#chipgroupv2spaceconfig) | 是 | ChipGroupV2间距配置。 |

## ChipGroupV2SpaceConfig

ChipGroupV2SpaceConfig定义了ChipGroupV2左右内边距，以及ChipV2与ChipV2之间的间距配置。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| itemSpace | string | number | 否 | 是 | ChipV2与ChipV2之间的间距（不支持百分比）。  取值范围：  - number类型：[0, +∞)，如0、8、16、24.5。  - string类型：单位为fp | vp | px | lpx且数值部分大于等于0的字符串，如"8vp"、"16fp"、"12px"、"10lpx"。  - 不支持：负数、百分比单位、无效字符串格式。  传入不在取值范围内或不支持格式的值时，按默认值处理。  默认值：8  单位：vp  值为undefined时，按默认值处理。 |
| startSpace | [Length](ts-types.md#length) | 否 | 是 | 左侧内边距（不支持百分比）。  默认值：16  单位：vp  值为undefined时，按默认值处理。 |
| endSpace | [Length](ts-types.md#length) | 否 | 是 | 右侧内边距（不支持百分比）。  默认值：16  单位：vp  值为undefined时，按默认值处理。 |

## ChipGroupV2Padding

ChipGroupV2Padding定义了ChipGroupV2的上下内边距，用于控制其整体高度。

**起始版本：** 26.0.0

**装饰器类型：** @ObservedV2

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

### 属性

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| top | [Length](ts-types.md#length) | 否 | 否 | ChipGroupV2的上方内边距（不支持百分比）。  默认值：14  单位：vp  值为undefined时，按默认值处理。  **装饰器类型：** @Trace |
| bottom | [Length](ts-types.md#length) | 否 | 否 | ChipGroupV2的下方内边距（不支持百分比）。  默认值：14  单位：vp  值为undefined时，按默认值处理。  **装饰器类型：** @Trace |

### constructor

constructor(config: ChipGroupV2PaddingConfig)

ChipGroupV2Padding的构造函数。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| config | [ChipGroupV2PaddingConfig](ohos-arkui-advanced-chipgroupv2.md#chipgroupv2paddingconfig) | 是 | ChipGroupV2内边距配置。 |

## ChipGroupV2PaddingConfig

ChipGroupV2PaddingConfig定义了ChipGroupV2的上下内边距配置，用于控制其整体高度。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| top | [Length](ts-types.md#length) | 否 | 否 | ChipGroupV2的上方内边距（不支持百分比）。  默认值：14  单位：vp  值为undefined时，按默认值处理。 |
| bottom | [Length](ts-types.md#length) | 否 | 否 | ChipGroupV2的下方内边距（不支持百分比）。  默认值：14  单位：vp  值为undefined时，按默认值处理。 |

## ChipGroupV2IconGroupSuffix

ChipGroupV2IconGroupSuffix用于在ChipGroupV2组件最右侧显示自定义内容，支持配置Image图标、Symbol图标或Symbol图标配置项，以及图标背景材质样式，适用于需要在标签组尾部添加额外操作入口的场景。

```typescript
ChipGroupV2IconGroupSuffix({
  items: Array<ChipGroupV2IconItemConfig | SymbolGlyphModifier | ChipGroupV2SymbolItemConfig>,
  iconBackgroundSystemMaterial?: uiMaterial.Material
})
```

**起始版本：** 26.0.0

**装饰器类型：** @ComponentV2

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

| 名称 | 类型 | 必填 | 装饰器类型 | 说明 |
| --- | --- | --- | --- | --- |
| items | Array<[ChipGroupV2IconItemConfig](ohos-arkui-advanced-chipgroupv2.md#chipgroupv2iconitemconfig) | [SymbolGlyphModifier](ts-universal-attributes-attribute-symbolglyphmodifier.md#symbolglyphmodifier) | [ChipGroupV2SymbolItemConfig](ohos-arkui-advanced-chipgroupv2.md#chipgroupv2symbolitemconfig)> | 是 | @Require  @Param | 尾部区域显示的自定义项数组，支持ChipGroupV2IconItemConfig（Image图标）、SymbolGlyphModifier（Symbol图标）或ChipGroupV2SymbolItemConfig（Symbol图标配置）类型。  传参SymbolGlyphModifier时，不支持使用symbolEffect修改动效类型和[effectStrategy](ts-basic-components-symbolglyph.md#effectstrategy)设置动效。 |
| iconBackgroundSystemMaterial | uiMaterial.[Material](arkts-apis-uimaterial.md#material) | 否 | @Param | 设置组件系统材质样式。需要将组件放置在Navigation或NavDestination的标题栏子树，或横向Tabs的底部TabBar子树中，材质效果才会生效。不同材质具有不同的效果，能够影响组件的背景色[backgroundColor](ts-universal-attributes-background.md#backgroundcolor)、边框颜色[borderColor](ts-universal-attributes-border.md#bordercolor)、边框宽度[borderWidth](ts-universal-attributes-border.md#borderwidth)、阴影[shadow](ts-universal-attributes-image-effect.md#shadow)效果、材质层滤镜效果[materialFilter](ts-universal-attributes-filter-effect.md#materialfilter23)。  默认值：undefined，不应用材质样式。 |

### build

build(): void

build函数用于构造ChipGroupV2IconGroupSuffix组件。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

## ChipGroupV2IconItemConfig

ChipGroupV2IconItemConfig定义了尾部图标项的配置，用于设置尾部图标的样式、交互和无障碍属性。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| icon | [ChipV2ImageIconConfig](ohos-arkui-advanced-chipv2.md#chipv2imageiconconfig) | 否 | 否 | 自定义尾部图标，设置后会在ChipGroupV2尾部区域显示指定的图标。  如果想动态修改图标尺寸，那么必须在引入[ChipGroupV2IconGroupSuffix](ohos-arkui-advanced-chipgroupv2.md#chipgroupv2icongroupsuffix)时，使用[SymbolGlyphModifier](ts-universal-attributes-attribute-symbolglyphmodifier.md#symbolglyphmodifier)类型，并通过该类型提供的方法设置图标尺寸属性，例如通过fontSize或size方法动态调整尺寸值。 |
| action | [Callback](ts-types.md#callback12)<void> | 否 | 否 | 自定义尾部图标的响应事件。 |
| accessibilityText | [ResourceStr](ts-types.md#resourcestr) | 否 | 是 | 尾部图标的无障碍文本属性。用于为用户进一步说明尾部图标，开发人员可为尾部图标的该属性设置相对较详细的解释文本，帮助用户理解将要执行的操作。例如，帮助用户理解将要执行的操作可能导致什么后果，尤其是当这些后果无法从尾部图标本身属性与无障碍文本中了解到时。若尾部图标既拥有文本属性又拥有无障碍说明属性，则尾部图标被选中时，先播报尾部图标的文本属性，再播报无障碍说明属性的内容。  默认值：空字符串。  值为undefined时，按默认值处理。 |
| accessibilityDescription | [ResourceStr](ts-types.md#resourcestr) | 否 | 是 | 尾部图标的无障碍描述。此描述用于向用户详细解释尾部图标，开发人员应为尾部图标的这一属性提供较为详尽的文本说明，以协助用户理解即将执行的操作及其可能产生的后果，特别是当这些后果无法仅从尾部图标的属性和无障碍文本中直接获知时。如果尾部图标同时具备文本属性和无障碍说明属性，当尾部图标被选中时，系统将首先播报尾部图标的文本属性，随后播报无障碍说明属性的内容。  默认值：空字符串。  值为undefined时，按默认值处理。 |
| accessibilityLevel | string | 否 | 是 | 尾部图标无障碍重要性。用于控制尾部图标是否可被无障碍辅助服务所识别。  支持的值为：  "auto"：尾部图标转换为"yes"。  "yes"：尾部图标可被无障碍辅助服务所识别。  "no"：尾部图标不可被无障碍辅助服务所识别。  "no-hide-descendants"：尾部图标及其所有子组件不可被无障碍辅助服务所识别。  传入不在支持范围内的值时，按默认值处理。  默认值："auto"  值为undefined时，按默认值处理。 |

## ChipGroupV2SymbolItemConfig

ChipGroupV2SymbolItemConfig定义了尾部Symbol图标的配置类型。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| symbol | [SymbolGlyphModifier](ts-universal-attributes-attribute-symbolglyphmodifier.md#symbolglyphmodifier) | 否 | 否 | 尾部图标的SymbolGlyphModifier配置对象，设置后会在ChipGroupV2尾部区域显示指定的Symbol图标，支持配置显示样式、渲染模式、颜色等属性。  **说明：** 传参SymbolGlyphModifier时，不支持使用symbolEffect修改动效类型和[effectStrategy](ts-basic-components-symbolglyph.md#effectstrategy)设置动效。 |
| action | [VoidCallback](ts-types.md#voidcallback12) | 否 | 否 | 尾部图标响应事件。 |
| accessibilityText | [ResourceStr](ts-types.md#resourcestr) | 否 | 是 | 尾部图标的无障碍文本属性。用于为用户进一步说明尾部图标，开发人员可为尾部图标的该属性设置相对较详细的解释文本，帮助用户理解将要执行的操作。例如，帮助用户理解将要执行的操作可能导致什么后果，尤其是当这些后果无法从尾部图标本身属性与无障碍文本中了解到时。若尾部图标既拥有文本属性又拥有无障碍说明属性，则尾部图标被选中时，先播报尾部图标的文本属性，再播报无障碍说明属性的内容。  默认值：空字符串。  值为undefined时，按默认值处理。 |
| accessibilityDescription | [ResourceStr](ts-types.md#resourcestr) | 否 | 是 | 尾部图标的无障碍描述。此描述用于向用户详细解释尾部图标，开发人员应为尾部图标的这一属性提供较为详尽的文本说明，以协助用户理解即将执行的操作及其可能产生的后果，特别是当这些后果无法仅从尾部图标的属性和无障碍文本中直接获知时。如果尾部图标同时具备文本属性和无障碍说明属性，当尾部图标被选中时，系统将首先播报尾部图标的文本属性，随后播报无障碍说明属性的内容。  默认值：空字符串。  值为undefined时，按默认值处理。 |
| accessibilityLevel | string | 否 | 是 | 尾部图标无障碍重要性。用于控制尾部图标是否可被无障碍辅助服务所识别。  支持的值为：  "auto"：尾部图标转换为"yes"。  "yes"：尾部图标可被无障碍辅助服务所识别。  "no"：尾部图标不可被无障碍辅助服务所识别。  "no-hide-descendants"：尾部图标及其所有子组件不可被无障碍辅助服务所识别。  传入不在支持范围内的值时，按默认值处理。  默认值："auto"  值为undefined时，按默认值处理。 |

## 示例

### 示例1（ChipGroupV2无最右侧自定义组件）

该示例通过不设置suffix参数，实现了[ChipGroupV2](ohos-arkui-advanced-chipgroupv2.md#chipgroupv2-1)没有最右侧自定义组件时的效果。

```ts
import { ChipV2Size, ChipGroupV2, ChipGroupV2Items, ChipGroupV2ItemStyle, ChipGroupV2Space, ChipGroupV2Padding, ColorMetrics } from '@kit.ArkUI';

@Entry
@ComponentV2
struct Index {
  @Local selectedIndex: Array<number> = [0];

  build() {
    Column() {
      ChipGroupV2({
        // items内每个对象设置的都是每个ChipV2的特定属性。
        items: new ChipGroupV2Items([
          {
            // $r('app.media.icon')需要替换为开发者所需的图像资源文件。
            prefixIcon: { src: $r('app.media.icon') },
            label: { text: '操作块1' },
            suffixIcon: { src: $r('sys.media.ohos_ic_public_cut') },
            allowClose: false
          },
          {
            prefixIcon: { src: $r('sys.media.ohos_ic_public_copy') },
            label: { text: '操作块2' },
            allowClose: true
          },
          {
            prefixIcon: { src: $r('sys.media.ohos_ic_public_clock') },
            label: { text: '操作块3' },
            allowClose: true
          },
          {
            prefixIcon: { src: $r('sys.media.ohos_ic_public_cast_stream') },
            label: { text: '操作块4' },
            allowClose: true
          },
          {
            prefixIcon: { src: $r('sys.media.ohos_ic_public_cast_mirror') },
            label: { text: '操作块5' },
            allowClose: true
          },
          {
            prefixIcon: { src: $r('sys.media.ohos_ic_public_cast_stream') },
            label: { text: '操作块6' },
            allowClose: true
          },
        ]),
        // 设置ChipV2的style属性。
        itemStyle: new ChipGroupV2ItemStyle({
          size: ChipV2Size.SMALL,
          backgroundColor: ColorMetrics.resourceColor($r('sys.color.ohos_id_color_button_normal')),
          fontColor: ColorMetrics.resourceColor($r('sys.color.ohos_id_color_text_primary')),
          selectedBackgroundColor: ColorMetrics.resourceColor($r('sys.color.ohos_id_color_emphasize')),
          selectedFontColor: ColorMetrics.resourceColor($r('sys.color.ohos_id_color_text_primary_contrary')),
        }),
        selectedIndexes: this.selectedIndex,
        multiple: false,
        chipGroupSpace: new ChipGroupV2Space({ itemSpace: 8, endSpace: 0 }),
        chipGroupPadding: new ChipGroupV2Padding({ top: 10, bottom: 10 }),
        onChange: (activatedChipsIndex: Array<number>) => {
          console.info('chips on clicked, activated index ' + activatedChipsIndex);
        },
      })
    }
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5b/v3/XxqdfBjwR3iw8-ykk41bHw/zh-cn_image_0000002742005465.png)

### 示例2（ChipGroupV2设置最右侧自定义组件）

该示例通过设置suffix参数，实现了[ChipGroupV2](ohos-arkui-advanced-chipgroupv2.md#chipgroupv2-1)最右侧的自定义组件效果。

从API版本26.0.0开始，ChipGroupV2新增suffix属性。

```ts
import { ChipV2Size, ChipGroupV2, ChipGroupV2Items, ChipGroupV2IconGroupSuffix, ChipGroupV2ItemStyle, ChipGroupV2Space, ChipGroupV2Padding, ColorMetrics, LengthMetrics } from '@kit.ArkUI';

@Entry
@ComponentV2
struct Index {
  @Local selectedIndex: Array<number> = [0, 1, 2, 3, 4, 5];
  @Local selectedState: boolean = true;

  @Builder
  ChipGroupSuffix(): void {
    // 开发者通过引用ChipGroupV2IconGroupSuffix，实现组件最右侧的自定义组件效果。
    ChipGroupV2IconGroupSuffix({
      items: [{
        icon: { src: $r('sys.media.ohos_ic_public_search_filled'), size: { width: LengthMetrics.fp(36), height: LengthMetrics.fp(36) } },
        action: () => {
          if (this.selectedState === false) {
            this.selectedIndex = [0, 1, 2, 3, 4, 5];
            this.selectedState = true;
          } else {
            this.selectedIndex = [];
            this.selectedState = false;
          }
        }
      }
      ]
    })
  }

  build() {
    Column() {
      ChipGroupV2({
        // items内每个对象设置的都是每个ChipV2的特定属性。
        items: new ChipGroupV2Items([
          {
            // $r('app.media.icon')需要替换为开发者所需的图像资源文件。
            prefixIcon: { src: $r('app.media.icon') },
            label: { text: '操作块1' },
            suffixIcon: { src: $r('sys.media.ohos_ic_public_cut') },
            allowClose: false
          },
          {
            prefixIcon: { src: $r('sys.media.ohos_ic_public_copy') },
            label: { text: '操作块2' },
            allowClose: true
          },
          {
            prefixIcon: { src: $r('sys.media.ohos_ic_public_clock') },
            label: { text: '操作块3' },
            allowClose: true
          },
          {
            prefixIcon: { src: $r('sys.media.ohos_ic_public_cast_stream') },
            label: { text: '操作块4' },
            allowClose: true
          },
          {
            prefixIcon: { src: $r('sys.media.ohos_ic_public_cast_mirror') },
            label: { text: '操作块5' },
            allowClose: true
          },
          {
            prefixIcon: { src: $r('sys.media.ohos_ic_public_cast_stream') },
            label: { text: '操作块6' },
            allowClose: true
          },
        ]),
        // 设置ChipV2的style属性。
        itemStyle: new ChipGroupV2ItemStyle({
          size: ChipV2Size.NORMAL,
          backgroundColor: ColorMetrics.resourceColor($r('sys.color.ohos_id_color_button_normal')),
          fontColor: ColorMetrics.resourceColor($r('sys.color.ohos_id_color_text_primary')),
          selectedBackgroundColor: ColorMetrics.resourceColor($r('sys.color.ohos_id_color_emphasize')),
          selectedFontColor: ColorMetrics.resourceColor($r('sys.color.ohos_id_color_text_primary_contrary')),
        }),
        selectedIndexes: this.selectedIndex,
        multiple: true,
        chipGroupSpace: new ChipGroupV2Space({ itemSpace: 8, endSpace: 0 }),
        chipGroupPadding: new ChipGroupV2Padding({ top: 10, bottom: 10 }),
        onChange: (activatedChipsIndex: Array<number>) => {
          console.info('chips on clicked, activated index ' + activatedChipsIndex);
        },
        // ChipGroupV2最右侧显示的自定义组件。
        suffix: this.ChipGroupSuffix
      })
    }
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fd/v3/vxvEdXQIReq_o1nWj2CLNQ/zh-cn_image_0000002712406476.png)

### 示例3（设置Symbol类型图标）

该示例通过[SymbolGlyphModifier](ts-universal-attributes-attribute-symbolglyphmodifier.md#symbolglyphmodifier)实现了[ChipGroupV2IconGroupSuffix](ohos-arkui-advanced-chipgroupv2.md#chipgroupv2icongroupsuffix)和[ChipGroupV2](ohos-arkui-advanced-chipgroupv2.md#chipgroupv2-1)设置Symbol类型图标。

从API版本26.0.0开始，新增ChipGroupV2IconGroupSuffix和ChipGroupV2。

```ts
import { ChipV2Size, ChipGroupV2, ChipGroupV2Items, ChipGroupV2IconGroupSuffix, SymbolGlyphModifier, ChipGroupV2ItemStyle, ChipGroupV2Space, ChipGroupV2Padding, ColorMetrics } from '@kit.ArkUI';

@Entry
@ComponentV2
struct Index {
  @Local selectedIndex: Array<number> = [0, 1, 2, 3, 4, 5];
  @Local selectedState: boolean = true;
  @Local prefixModifierNormal: SymbolGlyphModifier = new SymbolGlyphModifier($r('sys.symbol.ohos_star'));
  @Local prefixModifierActivated: SymbolGlyphModifier =
    new SymbolGlyphModifier($r('sys.symbol.ohos_star')).fontColor([Color.Red]);
  @Local suffixModifierNormal: SymbolGlyphModifier = new SymbolGlyphModifier($r('sys.symbol.ohos_wifi'));
  @Local suffixModifierActivated: SymbolGlyphModifier =
    new SymbolGlyphModifier($r('sys.symbol.ohos_wifi')).fontColor([Color.Red]);

  @Builder
  ChipGroupSuffix(): void {
    // 开发者通过引用ChipGroupV2IconGroupSuffix，实现组件最右侧的自定义组件效果。
    ChipGroupV2IconGroupSuffix({
      items: [
        new SymbolGlyphModifier($r('sys.symbol.magnifyingglass'))
          .onClick(() => {
            if (this.selectedState === false) {
              this.selectedIndex = [0, 1, 2, 3, 4, 5];
              this.selectedState = true;
            } else {
              this.selectedIndex = [];
              this.selectedState = false;
            }
          })
      ]
    })
  }

  build() {
    Column() {
      ChipGroupV2({
        // items内每个对象设置的都是每个ChipV2的特定属性。
        items: new ChipGroupV2Items([
          {
            prefixSymbolIcon: { normal: this.prefixModifierNormal, activated: this.prefixModifierActivated },
            label: { text: '操作块1' },
            suffixSymbolIcon: { normal: this.suffixModifierNormal, activated: this.suffixModifierActivated },
            allowClose: false,
          },
          {
            prefixSymbolIcon: { normal: this.prefixModifierNormal, activated: this.prefixModifierActivated },
            label: { text: '操作块2' },
            allowClose: true,
          },
          {
            prefixIcon: { src: $r('sys.media.ohos_ic_public_clock') },
            label: { text: '操作块3' },
            allowClose: true,
          },
          {
            prefixIcon: { src: $r('sys.media.ohos_ic_public_cast_stream') },
            label: { text: '操作块4' },
            allowClose: true,
          },
          {
            prefixIcon: { src: $r('sys.media.ohos_ic_public_cast_mirror') },
            label: { text: '操作块5' },
            allowClose: true,
          },
          {
            prefixIcon: { src: $r('sys.media.ohos_ic_public_cast_stream') },
            label: { text: '操作块6' },
            allowClose: true,
          },
        ]),
        // 设置ChipV2的style属性。
        itemStyle: new ChipGroupV2ItemStyle({
          size: ChipV2Size.NORMAL,
          backgroundColor: ColorMetrics.resourceColor($r('sys.color.ohos_id_color_button_normal')),
          fontColor: ColorMetrics.resourceColor($r('sys.color.ohos_id_color_text_primary')),
          selectedBackgroundColor: ColorMetrics.resourceColor($r('sys.color.ohos_id_color_emphasize')),
          selectedFontColor: ColorMetrics.resourceColor($r('sys.color.ohos_id_color_text_primary_contrary')),
        }),
        selectedIndexes: this.selectedIndex,
        multiple: true,
        chipGroupSpace: new ChipGroupV2Space({ itemSpace: 8, endSpace: 0 }),
        chipGroupPadding: new ChipGroupV2Padding({ top: 10, bottom: 10 }),
        onChange: (activatedChipsIndex: Array<number>) => {
          console.info('chips on clicked, activated index ' + activatedChipsIndex);
        },
        // ChipGroupV2最右侧显示的自定义组件。
        suffix: this.ChipGroupSuffix
      })
    }
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/46/v3/5G0NWyQvSeCiGMphpdoxeA/zh-cn_image_0000002742125425.png)

### 示例4（监听ChipGroupV2内对象类型属性的内部属性变化）

[ChipGroupV2Items](ohos-arkui-advanced-chipgroupv2.md#chipgroupv2items)、[ChipGroupV2Item](ohos-arkui-advanced-chipgroupv2.md#chipgroupv2item)、[ChipGroupV2ItemStyle](ohos-arkui-advanced-chipgroupv2.md#chipgroupv2itemstyle)等类使用了@ObservedV2装饰器，ChipGroupV2组件通过@Param接收各属性参数。对于@Trace装饰的基本类型属性（如ChipGroupV2Space的itemSpace等），@Param已能观测到属性变化并触发UI刷新，无需额外处理。但对于这些类中对象类型属性（如ChipGroupV2Item中prefixIcon的size）的内部属性，这些对象类型本身未被@ObservedV2装饰，其内部属性变化无法被@Param感知，导致修改内部属性时UI不会自动刷新。使用[makeObserved](js-apis-statemanagement.md#makeobserved)接口对对象类型属性进行包裹，可以为该对象的内部属性补充深度观察能力。makeObserved接口的详细说明请参考[makeObserved接口：将非观察数据变为可观察数据](../harmonyos-guides/arkts-new-makeobserved.md)。

以下示例对比了两种场景：点击“修改itemSpace间距”按钮修改chipGroupSpace的itemSpace属性（@Trace装饰的基本类型属性，已支持观测），UI自动刷新；点击“修改图标大小”按钮修改ChipGroupV2Item中prefixIcon的size内部属性（对象类型属性的内部属性，需通过UIUtils.makeObserved包裹size才能观测），UI同样自动刷新。

```ts
import {
  ChipGroupV2,
  ChipGroupV2Items,
  ChipGroupV2ItemStyle,
  ChipGroupV2Space,
  ChipGroupV2Padding,
  LengthMetrics,
  UIUtils
} from '@kit.ArkUI';

@Entry
@ComponentV2
struct Index {
  @Local items: ChipGroupV2Items = new ChipGroupV2Items([
    {
      // 使用UIUtils.makeObserved包裹size，使内部属性width和height可被观测。
      prefixIcon: {
        src: $r('sys.media.ohos_ic_public_clock'),
        size: UIUtils.makeObserved({ width: LengthMetrics.fp(16), height: LengthMetrics.fp(16) })
      },
      label: { text: '操作块1' }
    },
    {
      label: { text: '操作块2' }
    },
    {
      label: { text: '操作块3' }
    }
  ]);
  // ChipGroupV2Space的内部属性已被@Trace装饰，无需makeObserved。
  @Local chipGroupSpace: ChipGroupV2Space = new ChipGroupV2Space({ itemSpace: 8 });
  @Local chipGroupPadding: ChipGroupV2Padding = new ChipGroupV2Padding({ top: 10, bottom: 10 });
  @Local itemStyle: ChipGroupV2ItemStyle = new ChipGroupV2ItemStyle({});
  @Local selectedIndexes: number[] = [];
  @Local currentIconSize: number = 16;
  @Local currentItemSpace: number = 8;

  build() {
    Column({ space: 10 }) {
      ChipGroupV2({
        items: this.items,
        $items: (items: ChipGroupV2Items) => { this.items = items; },
        itemStyle: this.itemStyle,
        chipGroupSpace: this.chipGroupSpace,
        chipGroupPadding: this.chipGroupPadding,
        selectedIndexes: this.selectedIndexes,
        $selectedIndexes: (indexes: number[]) => { this.selectedIndexes = indexes; },
      })
      // 修改@Trace装饰的基本类型属性，UI自动刷新。
      Button('修改itemSpace间距')
        .onClick(() => {
          this.currentItemSpace = this.currentItemSpace === 8 ? 16 : 8;
          this.chipGroupSpace.itemSpace = this.currentItemSpace;
        })
      // 修改对象类型属性的内部属性，由于makeObserved包裹，UI同样自动刷新。
      Button('修改图标大小')
        .onClick(() => {
          if (this.items.length >= 1 && this.items[0] && this.items[0].prefixIcon && this.items[0].prefixIcon.size) {
            this.currentIconSize = this.currentIconSize === 16 ? 30 : 16;
            this.items[0].prefixIcon.size.width = LengthMetrics.fp(this.currentIconSize);
            this.items[0].prefixIcon.size.height = LengthMetrics.fp(this.currentIconSize);
          }
        })
    }
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/37/v3/8wQ4wQSnT5SD_tlCFx-quA/zh-cn_image_0000002712246518.gif)
