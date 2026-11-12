---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-subheaderv2
title: SubHeaderV2
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 系统预置UI组件库 > SubHeaderV2
category: harmonyos-references
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:c4635b9dd84b6e08845e84d81bbae7db20923137e6e803c39acb749def935268
---

子标题，用于列表项或内容项顶部，将该列表或内容划分为一个区块，子标题名称用来概括该区块内容。

该组件基于[状态管理（V2）](../harmonyos-guides/arkts-state-management-overview.md#状态管理v2)实现，相较于[状态管理（V1）](../harmonyos-guides/arkts-state-management-overview.md#状态管理v1)，状态管理（V2）增强了对数据对象的深度观察与管理能力，不再局限于组件层级。借助状态管理（V2），开发者可以通过该组件更灵活地控制子标题的数据和状态，实现更高效的用户界面刷新。

**说明** 

* 该组件从API version 18开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。
* 该组件仅可在Stage模型下使用。
* 如果SubHeaderV2设置[通用属性](ts-component-general-attributes.md)和[通用事件](ts-component-general-events.md)，编译工具链会额外生成节点\_\_Common\_\_，并将通用属性或通用事件挂载在\_\_Common\_\_上，而不是直接应用到SubHeaderV2本身。这可能导致开发者设置的通用属性或通用事件不生效或不符合预期，因此，不建议SubHeaderV2设置通用属性和通用事件。

## 导入模块

```ts
import { SubHeaderV2 } from '@kit.ArkUI';
```

## 子组件

无

## SubHeaderV2

SubHeaderV2({ icon?: SubHeaderV2IconType, endIcon?: SubHeaderV2IconType, title?: SubHeaderV2Title, select?: SubHeaderV2Select, operationType?: SubHeaderV2OperationType, operationItems?: SubHeaderV2OperationItem[], titleBuilder?: SubHeaderV2TitleBuilder })

子标题，用于列表项顶部，将该组列表划分为一个区块，子标题名称用来概括该区块内容。也可以用于内容项顶部，子标题名称用来概括该区块内容。

**装饰器类型：** @ComponentV2

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

| 名称 | 类型 | 必填 | 装饰器类型 | 说明 |
| --- | --- | --- | --- | --- |
| icon | [SubHeaderV2IconType](ohos-arkui-advanced-subheaderv2.md#subheaderv2icontype) | 否 | @Param | 图标设置项，用于为子标题添加图标标识。  默认值：undefined  当title使用secondaryTitle属性时，设置icon属性才会生效。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| endIcon | [SubHeaderV2IconType](ohos-arkui-advanced-subheaderv2.md#subheaderv2icontype) | 否 | @Param | 子标题尾部图标设置项，用于为子标题添加尾部图标标识。  当title使用primaryTitle或secondaryTitle属性时，设置endIcon属性才会生效。  默认值：undefined，表示不显示标题尾部图标。  **起始版本：** 26.0.1  **元服务API：** 从API版本26.0.1开始，该接口支持在元服务中使用。  **模型约束：** 此接口仅可在Stage模型下使用。 |
| title | [SubHeaderV2Title](ohos-arkui-advanced-subheaderv2.md#subheaderv2title) | 否 | @Param | 标题设置项。  默认值：undefined  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| select | [SubHeaderV2Select](ohos-arkui-advanced-subheaderv2.md#subheaderv2select) | 否 | @Param | 下拉选择器的配置项，包含下拉选项内容、选中状态及回调事件。  默认值：undefined  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| operationType | [SubHeaderV2OperationType](ohos-arkui-advanced-subheaderv2.md#subheaderv2operationtype) | 否 | @Param | 操作区元素样式，用于定义子标题尾部操作按钮的显示形式。  默认值：SubHeaderV2OperationType.BUTTON  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| operationItems | [SubHeaderV2OperationItem](ohos-arkui-advanced-subheaderv2.md#subheaderv2operationitem)[] | 否 | @Param | 操作区的设置项，用于配置子标题尾部的操作按钮。  默认值：undefined  当operationType为ICON\_GROUP时，数组最多包含三个元素。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| titleBuilder | [SubHeaderV2TitleBuilder](ohos-arkui-advanced-subheaderv2.md#subheaderv2titlebuilder) | 否 | @BuilderParam | 自定义标题区内容。当设置此参数时，title参数将不生效。  默认值：() => void  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |

## SubHeaderV2IconType

type SubHeaderV2IconType = ResourceStr | SymbolGlyphModifier

图标内容的联合类型。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

| 类型 | 说明 |
| --- | --- |
| [ResourceStr](ts-types.md#resourcestr) | 资源类型，用于定义普通图标。 |
| [SymbolGlyphModifier](ts-universal-attributes-attribute-symbolglyphmodifier.md#symbolglyphmodifier) | Symbol类型，用于定义Symbol图标。 |

## SubHeaderV2Title

标题设置项。

**装饰器类型：** @ObservedV2

### 属性

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| primaryTitle | [ResourceStr](ts-types.md#resourcestr) | 否 | 是 | 标题内容。  当[SubHeaderV2](ohos-arkui-advanced-subheaderv2.md#subheaderv2-1)中同时使用primaryTitle、secondaryTitle、icon属性时，设置primaryTitle属性不生效。  默认值：undefined  装饰器类型：@Trace  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| secondaryTitle | [ResourceStr](ts-types.md#resourcestr) | 否 | 是 | 副标题内容。  默认值：undefined  装饰器类型：@Trace  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| primaryTitleModifier | [TextModifier](ts-universal-attributes-attribute-modifier.md#自定义modifier) | 否 | 是 | 设置标题文本属性，如设置标题颜色、字体大小、字重等。  默认值：undefined  装饰器类型：@Trace  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| secondaryTitleModifier | [TextModifier](ts-universal-attributes-attribute-modifier.md#自定义modifier) | 否 | 是 | 设置副标题文本属性，如设置副标题颜色、字体大小、字重等。  默认值：undefined  装饰器类型：@Trace  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| titleAccessibilityText23+ | [ResourceStr](ts-types.md#resourcestr) | 否 | 是 | 设置标题自定义朗读内容。  默认值：undefined  值为undefined时，默认朗读组件显示的标题内容。  装饰器类型：@Trace  **元服务API：** 从API version 23开始，该接口支持在元服务中使用。 |
| id24+ | string | 否 | 是 | 标题id。需要为标题设置id的时候设置此参数，缺省时不设置此参数。  默认值：undefined，表示不设置标题id。  装饰器类型：@Trace  **元服务API：** 从API version 24开始，该接口支持在元服务中使用。 |

### constructor

constructor(options: SubHeaderV2TitleOptions)

标题内容信息SubHeaderV2Title构造函数。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [SubHeaderV2TitleOptions](ohos-arkui-advanced-subheaderv2.md#subheaderv2titleoptions) | 是 | 标题内容信息。 |

## SubHeaderV2TitleOptions

用于构建SubHeaderV2Title对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| primaryTitle | [ResourceStr](ts-types.md#resourcestr) | 否 | 是 | 标题内容。  默认值：undefined  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| secondaryTitle | [ResourceStr](ts-types.md#resourcestr) | 否 | 是 | 副标题内容。  默认值：undefined  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| primaryTitleModifier | [TextModifier](ts-universal-attributes-attribute-modifier.md#自定义modifier) | 否 | 是 | 设置标题文本属性，如设置主标题颜色、字体大小、字重等。  默认值：undefined  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| secondaryTitleModifier | [TextModifier](ts-universal-attributes-attribute-modifier.md#自定义modifier) | 否 | 是 | 设置副标题文本属性，如设置副标题颜色、字体大小、字重等。  默认值：undefined  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| titleAccessibilityText23+ | [ResourceStr](ts-types.md#resourcestr) | 否 | 是 | 设置标题自定义朗读内容。  默认值：undefined  值为undefined时，默认朗读组件显示的标题内容。  **元服务API：** 从API version 23开始，该接口支持在元服务中使用。 |
| id24+ | string | 否 | 是 | 标题id。需要为标题设置id的时候设置此参数，缺省时不设置此参数。  默认值：undefined，表示不设置标题id。  **元服务API：** 从API version 24开始，该接口支持在元服务中使用。 |

## SubHeaderV2Select

select内容以及事件。

**装饰器类型：** @ObservedV2

### 属性

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| options | [SelectOption](ts-basic-components-select.md#selectoption对象说明)[] | 否 | 否 | 下拉选项内容。  装饰器类型：@Trace  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| selectedIndex | number | 否 | 是 | 设置下拉菜单初始选项的索引。  第一项的索引为0。  当不设置selected属性时，  默认选择值为-1，菜单项不选中。  装饰器类型：@Trace  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| selectedContent | [ResourceStr](ts-types.md#resourcestr) | 否 | 是 | 设置下拉按钮本身的文本内容。默认值：'' 。从API version 20开始，支持Resource类型。  装饰器类型：@Trace  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| onSelect | [SubHeaderV2SelectOnSelect](ohos-arkui-advanced-subheaderv2.md#subheaderv2selectonselect) | 否 | 是 | 下拉菜单选中某一项的回调。  默认值：undefined  装饰器类型：@Trace  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| defaultFocus | boolean | 否 | 是 | 下拉按钮是否为默认焦点。  true：下拉按钮是默认焦点。  false：下拉按钮不是默认焦点。  默认值：false  装饰器类型：@Trace  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| id24+ | string | 否 | 是 | 下拉按钮id。需要为下拉按钮设置id的时候设置此参数，缺省时不设置此参数。  默认值：undefined，表示不设置下拉按钮id。  装饰器类型：@Trace  **元服务API：** 从API version 24开始，该接口支持在元服务中使用。 |

### constructor

constructor(options: SubHeaderV2SelectOptions)

select内容以及事件构造函数。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [SubHeaderV2SelectOptions](ohos-arkui-advanced-subheaderv2.md#subheaderv2selectoptions) | 是 | 下拉选项信息。 |

## SubHeaderV2SelectOptions

用于构建SubHeaderV2Select对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| options | [SelectOption](ts-basic-components-select.md#selectoption对象说明)[] | 否 | 否 | 下拉选项内容。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| selectedIndex | number | 否 | 是 | 设置下拉菜单初始选项的索引。  第一项的索引为0。  当不设置selected属性时，  默认选择值为-1，菜单项不选中。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| selectedContent | [ResourceStr](ts-types.md#resourcestr) | 否 | 是 | 设置下拉按钮本身的文本内容。默认值：''。从API version 20开始，支持Resource类型。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| onSelect | [SubHeaderV2SelectOnSelect](ohos-arkui-advanced-subheaderv2.md#subheaderv2selectonselect) | 否 | 是 | 下拉菜单选中某一项的回调。  默认值：undefined  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| defaultFocus | boolean | 否 | 是 | 下拉按钮是否为默认焦点。  true：下拉按钮是默认焦点。  false：下拉按钮不是默认焦点。  默认值：false  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| id24+ | string | 否 | 是 | 下拉按钮id。需要为下拉按钮设置id的时候设置此参数，缺省时不设置此参数。  默认值：undefined，表示不设置下拉按钮id。  **元服务API：** 从API version 24开始，该接口支持在元服务中使用。 |

## SubHeaderV2SelectOnSelect

type SubHeaderV2SelectOnSelect = (selectedIndex: number, selectedContent?: string) => void

下拉菜单选中某一项的回调类型。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| selectedIndex | number | 是 | 表示选中的下拉菜单项的索引值。 |
| selectedContent | string | 否 | 表示选中的下拉菜单项的内容值。 |

## SubHeaderV2OperationType

操作区元素样式。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

| 名称 | 值 | 说明 |
| --- | --- | --- |
| TEXT\_ARROW | 0 | 文本按钮（带右箭头）。 |
| BUTTON | 1 | 文本按钮（不带右箭头）。 |
| ICON\_GROUP | 2 | 图标按钮（最多支持配置三张图标）。 |
| LOADING | 3 | 加载动画。 |

## SubHeaderV2OperationItemType

type SubHeaderV2OperationItemType = ResourceStr | SymbolGlyphModifier

操作区元素内容的联合类型。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

| 类型 | 说明 |
| --- | --- |
| [ResourceStr](ts-types.md#resourcestr) | 字符串类型用于定义文本显示或普通图标；资源类型，用于定义普通图标。 |
| [SymbolGlyphModifier](ts-universal-attributes-attribute-symbolglyphmodifier.md#symbolglyphmodifier) | Symbol类型，用于定义Symbol图标。 |

## SubHeaderV2OperationItem

操作区的设置项。

**装饰器类型：** @ObservedV2

### 属性

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| content | [SubHeaderV2OperationItemType](ohos-arkui-advanced-subheaderv2.md#subheaderv2operationitemtype) | 否 | 否 | 操作区元素内容。  装饰器类型：@Trace  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| action | [SubHeaderV2OperationItemAction](ohos-arkui-advanced-subheaderv2.md#subheaderv2operationitemaction) | 否 | 是 | 操作区事件回调。默认值：() => void。  装饰器类型：@Trace  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| accessibilityText | [ResourceStr](ts-types.md#resourcestr) | 否 | 是 | 子标题尾部操作项无障碍描述。  默认值：undefined  装饰器类型：@Trace  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| accessibilityLevel | string | 否 | 是 | 子标题尾部操作项无障碍重要性。  支持的值为：  "auto"：当前子标题尾部操作项由无障碍分组服务和ArkUI进行综合判断是否可被无障碍辅助服务所识别。  "yes"：当前子标题尾部操作项可被无障碍辅助服务所识别。  "no"：当前子标题尾部操作项不可被无障碍辅助服务所识别。  "no-hide-descendants"：当前子标题尾部操作项及其所有子组件不可被无障碍辅助服务所识别。  默认值：“yes”。  装饰器类型：@Trace  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| accessibilityDescription | [ResourceStr](ts-types.md#resourcestr) | 否 | 是 | 子标题尾部操作项无障碍说明，用于为用户进一步说明当前组件。  默认值：“单指双击即可执行”。  装饰器类型：@Trace  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| defaultFocus | boolean | 否 | 是 | 子标题尾部操作项是否为默认焦点。  true：子标题尾部操作项是默认焦点。  false：子标题尾部操作项不是默认焦点。  默认值：false  装饰器类型：@Trace  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| id24+ | string | 否 | 是 | 子标题尾部操作项id。需要为子标题尾部操作项设置id的时候设置此参数，缺省时不设置此参数。  默认值：undefined，表示不设置子标题尾部操作项id。  装饰器类型：@Trace  **元服务API：** 从API version 24开始，该接口支持在元服务中使用。 |

### constructor

constructor(options: SubHeaderV2OperationItemOptions)

操作项SubHeaderV2OperationItem的构造函数。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [SubHeaderV2OperationItemOptions](ohos-arkui-advanced-subheaderv2.md#subheaderv2operationitemoptions) | 是 | 操作项配置信息。用于构建SubHeaderV2OperationItem对象。 |

## SubHeaderV2OperationItemAction

type SubHeaderV2OperationItemAction = () => void

操作区的设置项的回调事件类型。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

## SubHeaderV2OperationItemOptions

用于构建SubHeaderV2OperationItem对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| content | [SubHeaderV2OperationItemType](ohos-arkui-advanced-subheaderv2.md#subheaderv2operationitemtype) | 否 | 否 | 操作项显示的内容。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| action | [SubHeaderV2OperationItemAction](ohos-arkui-advanced-subheaderv2.md#subheaderv2operationitemaction) | 否 | 是 | 选项操作事件回调，点击操作项时触发，用于执行自定义操作。默认值：() => void。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| accessibilityText | [ResourceStr](ts-types.md#resourcestr) | 否 | 是 | 子标题尾部操作项无障碍描述。  默认值：undefined  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| accessibilityLevel | string | 否 | 是 | 子标题尾部操作项无障碍重要性。  支持的值为：  "auto"：当前子标题尾部操作项由无障碍分组服务和ArkUI进行综合判断是否可被无障碍辅助服务所识别。  "yes"：当前子标题尾部操作项可被无障碍辅助服务所识别。  "no"：当前子标题尾部操作项不可被无障碍辅助服务所识别。  "no-hide-descendants"：当前子标题尾部操作项及其所有子组件不可被无障碍辅助服务所识别。  默认值：“yes”。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| accessibilityDescription | [ResourceStr](ts-types.md#resourcestr) | 否 | 是 | 子标题尾部操作项无障碍说明，用于为用户进一步说明当前组件。  默认值：“单指双击即可执行”。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| defaultFocus | boolean | 否 | 是 | 子标题尾部操作项是否为默认焦点。  true：子标题尾部操作项是默认焦点。  false：子标题尾部操作项不是默认焦点。  默认值：false  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| id24+ | string | 否 | 是 | 子标题尾部操作项id。需要为子标题尾部操作项设置id的时候设置此参数，缺省时不设置此参数。  默认值：undefined，表示不设置子标题尾部操作项id。  **元服务API：** 从API version 24开始，该接口支持在元服务中使用。 |

## SubHeaderV2TitleBuilder

type SubHeaderV2TitleBuilder= () => void

自定义标题区内容的回调事件类型。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

## 事件

不支持[通用事件](ts-component-general-events.md)。

## 示例

### 示例1（效率型子标题）

该示例主要演示子标题左侧为icon、secondaryTitle，右侧operationType为按钮类型。

```ts
import {
  SubHeaderV2OperationType,
  SubHeaderV2,
  SubHeaderV2Title,
  SubHeaderV2OperationItem,
  Prompt,
  TextModifier
} from '@kit.ArkUI';

@Entry
@ComponentV2
struct SubHeaderExample {
  @Local selectText: string = "TTTTT"
  @Local selectIndex: number = 2
  @Local flag: boolean = true;
  @Local index: number = 1;
  @Local primaryTitle: ResourceStr = '一级标题';
  @Local secondaryTitle: ResourceStr = '二级标题';
  @Local subHeaderIcon: Resource = $r('sys.media.ohos_ic_public_email');
  @Local title: SubHeaderV2Title = new SubHeaderV2Title({ primaryTitle: '一级标题' });
  @Local primaryModifier: TextModifier = new TextModifier().fontColor(Color.Red);
  @Local secondaryModifier: TextModifier = new TextModifier().fontColor(Color.Red);
  @Local subHeaderOperationType: SubHeaderV2OperationType = SubHeaderV2OperationType.BUTTON;
  @Local operationItems: SubHeaderV2OperationItem[] = [];

  aboutToAppear(): void {
    this.title = new SubHeaderV2Title({
      primaryTitle: this.primaryTitle,
      secondaryTitle: this.secondaryTitle,
    });
    this.operationItems = [new SubHeaderV2OperationItem({
      content: '操作',
      action: () => {
        Prompt.showToast({ message: 'demo2' })
      }
    })]
  }

  build() {
    Column() {
      Column() {
        SubHeaderV2({
          icon: this.subHeaderIcon,
          title: this.title,
          operationType: this.subHeaderOperationType,
          operationItems: this.operationItems
        });
      }
    }
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a6/v3/v7AwMUwHSMiihB1lkWrmaA/zh-cn_image_0000002815401189.png?HW-CC-KV=V1&HW-CC-Date=20261112T233240Z&HW-CC-Expire=31536000000&HW-CC-Sign=5807AF5FE994E39BD7574D763662A296B4C3177C9BF135D92F16ECB4CC8457A8)

### 示例2（双行文本内容型子标题）

该示例主要演示子标题左侧为primaryTitle、secondaryTitle，右侧operationType类型为TEXT\_ARROW。

```ts
import {
  SubHeaderV2OperationType,
  SubHeaderV2,
  SubHeaderV2Title,
  SubHeaderV2OperationItem,
  Prompt,
  TextModifier
} from '@kit.ArkUI';

@Entry
@ComponentV2
struct SubHeaderExample {
  @Local title: SubHeaderV2Title = new SubHeaderV2Title({ primaryTitle: '一级标题', secondaryTitle: '二级标题' });
  @Local primaryModifier: TextModifier = new TextModifier().fontColor(Color.Red);
  @Local secondaryModifier: TextModifier = new TextModifier().fontColor(Color.Red);
  @Local subHeaderOperationType: SubHeaderV2OperationType = SubHeaderV2OperationType.TEXT_ARROW;
  @Local operationItems: SubHeaderV2OperationItem[] = [];

  aboutToAppear(): void {
    this.title = new SubHeaderV2Title({
      primaryTitle: '一级标题',
      secondaryTitle: '二级标题'
    });
    this.operationItems = [new SubHeaderV2OperationItem({
      content: '更多',
      action: () => {
        Prompt.showToast({ message: 'demo2' })
      }
    })]
  }

  build() {
    Column() {
      Column() {
        SubHeaderV2({
          title: this.title,
          operationType: this.subHeaderOperationType,
          operationItems: this.operationItems
        });
      }
    }
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/38/v3/bVlfsbDVTT20Hzf9uhce6g/zh-cn_image_0000002786521614.png?HW-CC-KV=V1&HW-CC-Date=20261112T233240Z&HW-CC-Expire=31536000000&HW-CC-Sign=C71B640261F582F6823E9E8EEE5058F69AE883768DC28DEBBD99A916252106BE)

### 示例3（spinner型内容型子标题）

该示例主要演示子标题左侧为select，右侧operationType类型为ICON\_GROUP。

```ts
import {
  SubHeaderV2,
  SubHeaderV2OperationType,
  SubHeaderV2OperationItem,
  SubHeaderV2Title,
  SubHeaderV2Select,
  Prompt
} from '@kit.ArkUI';

@Entry
@ComponentV2
struct SubHeaderExample {
  @Local selectedValue: string = 'aaa';
  @Local selectedIndex: number = 0;
  @Local title: SubHeaderV2Title = new SubHeaderV2Title({ primaryTitle: '一级标题', secondaryTitle: '二级标题' });
  @Local operationItems: SubHeaderV2OperationItem[] = [];
  @Local select: SubHeaderV2Select =
    new SubHeaderV2Select({ options: [{ value: 'aaa' }, { value: 'bbb' }, { value: 'ccc' }] });

  aboutToAppear(): void {

    this.title = new SubHeaderV2Title({
      primaryTitle: '一级标题',
      secondaryTitle: '二级标题'
    });

    this.selectedValue = 'selectDemo';
    this.select = new SubHeaderV2Select({
      options: [{ value: 'aaa' }, { value: 'bbb' }, { value: 'ccc' }],
      selectedContent: this.selectedValue,
      selectedIndex: this.selectedIndex,
      onSelect: (index: number, value?: string) => {
        Prompt.showToast({ message: 'selectDemo' })
      }
    })

    this.operationItems = [
      new SubHeaderV2OperationItem({
        content: $r('sys.media.ohos_ic_public_email'),
        action: () => {
          Prompt.showToast({ message: 'demo' })
        }
      }),
      new SubHeaderV2OperationItem({
        content: $r('sys.media.ohos_ic_public_email'),
        action: () => {
          Prompt.showToast({ message: 'demo' })
        }
      }),
      new SubHeaderV2OperationItem({
        content: $r('sys.media.ohos_ic_public_email'),
        action: () => {
          Prompt.showToast({ message: 'demo' })
        }
      })]
  }

  build() {
    Column() {
      Column() {
        SubHeaderV2({
          select: this.select,
          operationType: SubHeaderV2OperationType.ICON_GROUP,
          operationItems: this.operationItems
        })
      }
    }
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/32/v3/heyt4FGMS3mwHHDhfBPZYg/zh-cn_image_0000002786361686.png?HW-CC-KV=V1&HW-CC-Date=20261112T233240Z&HW-CC-Expire=31536000000&HW-CC-Sign=863CF9CE1F6336F706D630BFDE24CBA9EB74E1291FBD07F1821A0D15C80D2714)

### 示例4（设置左侧symbol图标）

该示例主要演示子标题左侧icon设置symbol图标。

```ts
import {
  SubHeaderV2,
  SubHeaderV2OperationType,
  SubHeaderV2OperationItem,
  SubHeaderV2Title,
  Prompt,
  SymbolGlyphModifier
} from '@kit.ArkUI';

@Entry
@ComponentV2
struct SubHeaderExample {
  @Local icon: SymbolGlyphModifier = new SymbolGlyphModifier($r('sys.symbol.ohos_wifi'));

  aboutToAppear(): void {
    this.icon = new SymbolGlyphModifier($r('sys.symbol.ohos_wifi')).fontSize(24);
    this.icon.effectStrategy(SymbolEffectStrategy.HIERARCHICAL)
  }

  build() {
    Column() {
      SubHeaderV2({
        icon: this.icon,
        title: new SubHeaderV2Title({ secondaryTitle: '标题' }),
        operationType: SubHeaderV2OperationType.BUTTON,
        operationItems: [new SubHeaderV2OperationItem({
          content: '操作',
          action: () => {
            Prompt.showToast({ message: 'demo' })
          }
        })]
      })
    }
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9a/v3/YievpQukTWGk9dtRQYV4UA/zh-cn_image_0000002815561107.gif?HW-CC-KV=V1&HW-CC-Date=20261112T233240Z&HW-CC-Expire=31536000000&HW-CC-Sign=A27B63E2407764ADB6FB1C634D263CAF1AC37B6D1830B2A44880D4DA665452CA)

### 示例5（设置右侧symbol图标）

该示例主要演示子标题operationType设置为OperationType.ICON\_GROUP，operationItem的value设置为symbol图标。

```ts
import {
  SubHeaderV2,
  SubHeaderV2OperationType,
  SubHeaderV2OperationItem,
  SubHeaderV2Title,
  SubHeaderV2Select,
  Prompt,
  SymbolGlyphModifier
} from '@kit.ArkUI';

@Entry
@ComponentV2
struct SubHeaderExample {
  @Local icon: SymbolGlyphModifier = new SymbolGlyphModifier($r('sys.symbol.ohos_wifi'));
  @Local selectedValue: string = 'aaa';
  @Local selectedIndex: number = 2;
  @Local title: SubHeaderV2Title = new SubHeaderV2Title({ primaryTitle: '一级标题', secondaryTitle: '二级标题' });
  @Local operationItem: SubHeaderV2OperationItem[] = [];
  @Local select: SubHeaderV2Select =
    new SubHeaderV2Select({ options: [{ value: 'aaa' }, { value: 'bbb' }, { value: 'ccc' }] });

  aboutToAppear(): void {
    this.icon = new SymbolGlyphModifier($r('sys.symbol.ohos_wifi'));
    this.icon.effectStrategy(SymbolEffectStrategy.HIERARCHICAL);

    this.selectedValue = 'selectDemo';
    this.selectedIndex = 2;
    this.title = new SubHeaderV2Title({
      primaryTitle: '一级标题',
      secondaryTitle: '二级标题'
    });
    this.select = new SubHeaderV2Select({
      options: [{ value: 'aaa' }, { value: 'bbb' }, { value: 'ccc' }],
      selectedContent: this.selectedValue,
      selectedIndex: this.selectedIndex,
      onSelect: (index: number, value?: string) => {
        Prompt.showToast({ message: 'demo' })
      }
    })

    this.operationItem = [
      new SubHeaderV2OperationItem({
        content: new SymbolGlyphModifier($r('sys.symbol.ohos_lungs')).fontWeight(FontWeight.Lighter),
        action: () => {
          Prompt.showToast({ message: 'demo1' })
        }
      }),
      new SubHeaderV2OperationItem({
        content: new SymbolGlyphModifier($r('sys.symbol.ohos_lungs'))
          .renderingStrategy(SymbolRenderingStrategy.MULTIPLE_COLOR)
          .fontColor([Color.Blue, Color.Grey, Color.Green])
      ,
        action: () => {
          Prompt.showToast({ message: 'demo2' })
        }
      }),
      new SubHeaderV2OperationItem({
        content: new SymbolGlyphModifier($r('sys.symbol.ohos_lungs'))
          .renderingStrategy(SymbolRenderingStrategy.MULTIPLE_OPACITY)
          .fontColor([Color.Blue, Color.Grey, Color.Green])
      ,
        action: () => {
          Prompt.showToast({ message: 'demo3' })
        }
      })]
  }

  build() {
    Column() {
      SubHeaderV2({
        select: this.select,
        operationType: SubHeaderV2OperationType.ICON_GROUP,
        operationItems: this.operationItem
      })
    }
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7d/v3/tUY7mC_wQBSFvFHulQnU4w/zh-cn_image_0000002815401191.png?HW-CC-KV=V1&HW-CC-Date=20261112T233240Z&HW-CC-Expire=31536000000&HW-CC-Sign=F0F9C4A39D2995650A5F1447760794362B932A9008CE31FF0EA6D1BEEFC7C6E5)

### 示例6（自定义标题内容）

该示例主要演示SubHeaderV2设置titleBuilder自定义标题内容的效果。

```ts
import {
  SubHeaderV2,
  SubHeaderV2OperationType,
  SubHeaderV2OperationItem,
  SubHeaderV2Title,
  Prompt
} from '@kit.ArkUI';

@Entry
@ComponentV2
struct SubHeaderExample {
  @Local title: SubHeaderV2Title = new SubHeaderV2Title({ primaryTitle: '一级标题' });
  @Local operationItem: SubHeaderV2OperationItem[] = [];

  aboutToAppear(): void {
    this.title = new SubHeaderV2Title({
      primaryTitle: '一级标题',
      secondaryTitle: '二级标题'
    });
    this.operationItem = [new SubHeaderV2OperationItem({
      content: '更多信息',
      action: () => {
        Prompt.showToast({ message: 'demo' })
      }
    })]
  }

  @Builder
  TitleBuilder(): void {
    Text('自定义标题')
      .fontSize(24)
      .fontColor(Color.Blue)
      .fontWeight(FontWeight.Bold)
  }

  build() {
    Column() {
      SubHeaderV2({
        titleBuilder: () => {
          this.TitleBuilder();
        },
        title: this.title,

        operationType: SubHeaderV2OperationType.TEXT_ARROW,
        operationItems: this.operationItem
      })
    }
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/19/v3/GwMWrrWCQRSe5dzDyC2phg/zh-cn_image_0000002786521616.png?HW-CC-KV=V1&HW-CC-Date=20261112T233240Z&HW-CC-Expire=31536000000&HW-CC-Sign=A9404B8C75FEDDF9B1C45E4195AFA391FF85EC192EB0248A1DDAB221EB2248F6)

### 示例7（自定义标题样式）

该示例主要演示SubHeaderV2设置标题和副标题字体样式。

```ts
import {
  SubHeaderV2,
  SubHeaderV2OperationType,
  SubHeaderV2OperationItem,
  SubHeaderV2Title,
  Prompt,
  TextModifier
} from '@kit.ArkUI';

@Entry
@ComponentV2
struct SubHeaderExample {
  @Local primaryModifier: TextModifier = new TextModifier().fontColor(Color.Blue);
  @Local secondaryModifier: TextModifier = new TextModifier().fontColor(Color.Blue);
  @Local title: SubHeaderV2Title = new SubHeaderV2Title({ primaryTitle: '一级标题' });
  @Local operationItems4: SubHeaderV2OperationItem[] = [];

  aboutToAppear(): void {
    this.title = new SubHeaderV2Title({
      primaryTitle: '一级标题',
      primaryTitleModifier: this.primaryModifier,
      secondaryTitle: '二级标题',
      secondaryTitleModifier: this.secondaryModifier
    });
    this.operationItems4 = [new SubHeaderV2OperationItem({
      content: '更多信息',
      action: () => {
        Prompt.showToast({ message: 'demo' })
      }
    })]
  }

  build() {
    Column() {
      SubHeaderV2({
        title: this.title,
        operationType: SubHeaderV2OperationType.TEXT_ARROW,
        operationItems: this.operationItems4
      })
    }
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7/v3/-BINOSquSPyFViidqgYxYQ/zh-cn_image_0000002786361690.png?HW-CC-KV=V1&HW-CC-Date=20261112T233240Z&HW-CC-Expire=31536000000&HW-CC-Sign=56061F77B9E5968A6EEF25DC15B2EE5634FA31DEF383FD57806669CECC1B803B)

### 示例8（右侧按钮自定义播报）

该示例通过设置SubHeaderV2的右侧按钮属性accessibilityText、accessibilityDescription、accessibilityLevel自定义屏幕朗读播报文本。

```ts
import {
  SubHeaderV2OperationType,
  SubHeaderV2,
  SubHeaderV2Title,
  SubHeaderV2OperationItem,
  SubHeaderV2IconType,
  SubHeaderV2Select,
  Prompt
} from '@kit.ArkUI';

@Entry
@ComponentV2
struct SubHeaderExample {
  @Local index: number = 1;
  @Local primaryTitle: ResourceStr = '一级标题';
  @Local secondaryTitle: ResourceStr = '二级标题';
  @Local subHeaderIcon: SubHeaderV2IconType | undefined = $r('sys.media.ohos_ic_public_email');
  @Local title: SubHeaderV2Title = new SubHeaderV2Title({ primaryTitle: '一级标题' });
  @Local title2: SubHeaderV2Title = new SubHeaderV2Title({ primaryTitle: '一级标题', secondaryTitle: '二级标题' });
  @Local subHeaderOperationType: SubHeaderV2OperationType = SubHeaderV2OperationType.BUTTON;
  @Local subHeaderOperationType2: SubHeaderV2OperationType = SubHeaderV2OperationType.TEXT_ARROW;
  @Local subHeaderOperationType3: SubHeaderV2OperationType = SubHeaderV2OperationType.ICON_GROUP;
  @Local operationItems: SubHeaderV2OperationItem[] = [];
  @Local selectedValue: string | undefined = 'selectDemo';
  @Local selectedIndex: number = 0;
  @Local select: SubHeaderV2Select =
    new SubHeaderV2Select({ options: [{ value: 'aaa' }, { value: 'bbb' }, { value: 'ccc' }] });

  aboutToAppear(): void {
    this.select = new SubHeaderV2Select({ options: [] });
    this.title = new SubHeaderV2Title({
      primaryTitle: this.primaryTitle,
      secondaryTitle: this.secondaryTitle,
    });
    this.operationItems = [new SubHeaderV2OperationItem({
      content: '操作',
      action: () => {
        Prompt.showToast({ message: 'demo2' })
      }
    })]
  }

  build() {
    Column() {
      Column() {
        SubHeaderV2({
          icon: this.subHeaderIcon,
          title: this.title,
          select: this.select,
          operationType: this.subHeaderOperationType,
          operationItems: this.operationItems
        });
        Divider().color('grey').width('100%').height('2vp')
        SubHeaderV2({
          title: this.title2,
          select: this.select,
          operationType: this.subHeaderOperationType2,
          operationItems: this.operationItems
        });
        Divider().color('grey').width('100%').height('2vp')
        SubHeaderV2({
          select: new SubHeaderV2Select({
            options: [{ value: 'aaa' }, { value: 'bbb' }, { value: 'ccc' }],
            selectedIndex: this.selectedIndex,
            selectedContent: this.selectedValue,
            onSelect: (index: number, value?: string) => {
              this.selectedIndex = index;
              this.selectedValue = value;
              Prompt.showToast({ message: this.selectedValue })
            }
          }),
          operationType: this.subHeaderOperationType3,
          operationItems: [new SubHeaderV2OperationItem({
            content: $r('sys.media.ohos_ic_public_email'),
            accessibilityText: '图标1',
            accessibilityLevel: 'yes',
          }), new SubHeaderV2OperationItem({
            content: $r('sys.media.ohos_ic_public_email'),
            accessibilityText: '图标2',
            accessibilityLevel: 'no',
          }), new SubHeaderV2OperationItem({
            content: $r('sys.media.ohos_ic_public_email'),
            accessibilityText: '图标3',
            accessibilityDescription: '点击操作图标3',
          })]
        });
      }
      Divider().color('grey').width('100%').height('2vp')
    }
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/04/v3/BCVyxBoIRUucz05YawVG-w/zh-cn_image_0000002815561109.png?HW-CC-KV=V1&HW-CC-Date=20261112T233240Z&HW-CC-Expire=31536000000&HW-CC-Sign=32F7A357EE772C7F4291A8072A8FDCD55B16F358CFE8AB42350B7534C1701332)

### 示例9（右侧按钮设置默认获焦）

在获焦状态下，该示例通过设置SubHeaderV2的右侧按钮属性defaultFocus使其默认获焦。

从API version 18开始，在[SubHeaderV2OperationItem](ohos-arkui-advanced-subheaderv2.md#subheaderv2operationitemoptions)中新增defaultFocus接口。

```ts
import {
  SubHeaderV2OperationType,
  SubHeaderV2,
  SubHeaderV2Title,
  SubHeaderV2OperationItem,
  Prompt,
  TextModifier
} from '@kit.ArkUI';

@Entry
@ComponentV2
struct SubHeaderExample {
  @Local selectText: string = "TTTTT"
  @Local selectIndex: number = 2
  @Local flag: boolean = true;
  @Local index: number = 1;
  @Local primaryTitle: ResourceStr = '一级标题';
  @Local secondaryTitle: ResourceStr = '二级标题';
  @Local subHeaderIcon: Resource = $r('sys.media.ohos_ic_public_email');
  @Local title: SubHeaderV2Title = new SubHeaderV2Title({ primaryTitle: '一级标题' });
  @Local primaryModifier: TextModifier = new TextModifier().fontColor(Color.Red);
  @Local secondaryModifier: TextModifier = new TextModifier().fontColor(Color.Red);
  @Local subHeaderOperationType: SubHeaderV2OperationType = SubHeaderV2OperationType.BUTTON;
  @Local operationItems: SubHeaderV2OperationItem[] = [];

  aboutToAppear(): void {
    this.title = new SubHeaderV2Title({
      secondaryTitle: this.secondaryTitle,
    });
    this.operationItems = [new SubHeaderV2OperationItem({
      content: '操作',
      defaultFocus: true,
      action: () => {
        Prompt.showToast({ message: 'demo2' })
      }
    })]
  }

  build() {
    Column() {
      Column() {
        SubHeaderV2({
          icon: this.subHeaderIcon,
          title: this.title,
          operationType: this.subHeaderOperationType,
          operationItems: this.operationItems
        });
      }
    }
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/25/v3/O8E8B9HIRv6mwrf2hG-bLg/zh-cn_image_0000002815401193.png?HW-CC-KV=V1&HW-CC-Date=20261112T233240Z&HW-CC-Expire=31536000000&HW-CC-Sign=695D8ECCF66F57FB58FAF7DD98CC6CB62030BFE5DB8DA44540BBD544EBD17DEC)

### 示例10（设置子标题尾部图标）

该示例主要演示子标题设置endIcon尾部图标，包括普通图片资源和Symbol图标两种形式。

从API版本26.0.1开始，[SubHeaderV2](ohos-arkui-advanced-subheaderv2.md#subheaderv2-1)新增endIcon属性。

```ts
import {
  SubHeaderV2,
  SubHeaderV2Title,
  SubHeaderV2IconType,
  SymbolGlyphModifier
} from '@kit.ArkUI';

@Entry
@ComponentV2
struct SubHeaderExample {
  @Local title: SubHeaderV2Title = new SubHeaderV2Title({ secondaryTitle: '二级标题' });
  // $r('app.media.startIcon')需要替换为开发者所需的图像资源文件。
  @Local endIcon: SubHeaderV2IconType = $r('app.media.startIcon');
  @Local endIconSymbol: SymbolGlyphModifier = new SymbolGlyphModifier($r('sys.symbol.ohos_lungs'));

  aboutToAppear(): void {
    this.title = new SubHeaderV2Title({
      secondaryTitle: '二级标题'
    });
    this.endIconSymbol = new SymbolGlyphModifier($r('sys.symbol.ohos_lungs'))
      .renderingStrategy(SymbolRenderingStrategy.MULTIPLE_COLOR)
      .fontColor([Color.Blue, Color.Grey, Color.Green]);
  }

  build() {
    Column() {
      // 图标+二级标题+尾部图标（Image）
      SubHeaderV2({
        icon: $r('sys.media.ohos_ic_public_email'),
        endIcon: this.endIcon,
        title: this.title
      })
      // 图标+二级标题+尾部图标（Symbol）
      SubHeaderV2({
        icon: $r('sys.media.ohos_ic_public_email'),
        endIcon: this.endIconSymbol,
        title: this.title
      })
    }
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d9/v3/fSk23uyyRAe33DqaM70yEw/zh-cn_image_0000002815561111.png?HW-CC-KV=V1&HW-CC-Date=20261112T233240Z&HW-CC-Expire=31536000000&HW-CC-Sign=D09DDC7A5F8E0DA1315AAD589B2B97816FD30CBC9EA5906E5435649EED1FCC02)
