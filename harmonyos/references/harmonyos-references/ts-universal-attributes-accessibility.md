---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-accessibility
title: 无障碍属性
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 通用属性 > 无障碍属性
category: harmonyos-references
scraped_at: 2026-09-05T06:17:06+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:d7ebd4b05bb624a32f416f14dcfa406c5ebdac129b41de844689a0053cdfd2e4
---

设置组件的无障碍属性和事件，以充分利用无障碍功能。支持设置无障碍分组、无障碍文本、无障碍说明、无障碍重要性、无障碍虚拟子节点、无障碍组件类型、屏幕朗读焦点控制、状态播报、自定义无障碍操作等能力，适用于需要为视障用户提供屏幕朗读辅助、提升应用无障碍可达性的场景。

**说明** 

* 从API version 10 开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 本模块接口仅可在Stage模型下使用。

## accessibilityGroup

accessibilityGroup(value: boolean): T

设置是否启用无障碍分组。启用无障碍分组后，组件及其子组件作为一整个可选中组件，无障碍服务不再关注子组件内容。

若组件启用无障碍分组，当组件不包含通用文本属性，同时未设置无障碍文本[accessibilityText](ts-universal-attributes-accessibility.md#accessibilitytext)时，将默认拼接其子组件的通用文本属性作为组件的合并文本。若某一子组件没有通用文本属性，则忽略该子组件不进行拼接，此时合并文本不使用子组件的无障碍文本。

当子组件[accessibilityLevel](ts-universal-attributes-accessibility.md#accessibilitylevel)设置为"yes"时则不受accessibilityGroup约束，在满足屏幕朗读其他规则下，子组件可聚焦。

**说明** 

该接口不支持在[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)中调用。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean | 是 | 无障碍分组，设置为true时表示该组件及其所有子组件为一整个可以选中的组件，无障碍服务将不再关注其子组件内容，会合并子组件的文本与无障碍信息，并将其发送至无障碍服务；设置为false表示不启用无障碍分组。  默认值：false |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前对象。 |

## accessibilityGroup14+

accessibilityGroup(isGroup: boolean, accessibilityOptions: AccessibilityOptions): T

设置是否启用无障碍分组。启用无障碍分组后，组件及其子组件作为一整个可选中组件，无障碍服务不再关注子组件内容。

若组件启用无障碍分组，当组件不包含通用文本属性，同时未设置无障碍文本[accessibilityText](ts-universal-attributes-accessibility.md#accessibilitytext)时，将默认拼接其子组件的通用文本属性作为组件的合并文本。若某一子组件没有通用文本属性，则忽略该子组件不进行拼接，此时合并文本不使用子组件的无障碍文本。

当子组件[accessibilityLevel](ts-universal-attributes-accessibility.md#accessibilitylevel)设置为"yes"时则不受accessibilityGroup约束，在满足屏幕朗读其他规则下，子组件可聚焦。

通过[accessibilityPreferred](ts-types.md#accessibilityoptions14对象说明)启用优先拼接无障碍文本进行朗读后，将优先拼接其子组件的无障碍文本属性作为组件的合并文本。若某一子组件未设置无障碍文本，则继续拼接该子组件的通用文本属性，若该子组件没有通用文本属性，则忽略该子组件不进行拼接。

从API version 23开始，通过accessibilityOptions中的相关配置项（stateControllerRoleType或stateControllerId、actionControllerRoleType或actionControllerId），可以指定一个特定子组件，由该子组件的状态信息和点击事件来接管当前聚合组件的无障碍能力。

**说明** 

该接口不支持在[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)中调用。

**卡片能力：** 从API version 14开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isGroup | boolean | 是 | 无障碍分组，设置为true时表示该组件及其所有子组件为一整个可以选中的组件，无障碍服务将不再关注其子组件内容，会合并子组件的文本与无障碍信息，并将其发送至无障碍服务；设置为false表示不启用无障碍分组。  默认值：false |
| accessibilityOptions | [AccessibilityOptions](ts-types.md#accessibilityoptions14对象说明) | 是 | 无障碍分组的配置选项对象，包含以下属性：  - accessibilityPreferred：设置为true时，使应用优先拼接无障碍文本进行朗读；设置为false时，应用进行屏幕朗读时不会优先使用无障碍文本。  - stateControllerRoleType或stateControllerId：从API version 23开始支持，指定一个特定子组件，使用该子组件的状态信息作为当前聚合组件的无障碍状态。  - actionControllerRoleType或actionControllerId：从API version 23开始支持，指定一个特定子组件，使用该子组件的点击事件作为当前聚合组件的无障碍操作。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前对象。 |

## accessibilityText

accessibilityText(value: string): T

设置无障碍文本。当组件不包含文本属性时，开发人员可通过设置无障碍文本属性，使不包含文字信息的组件能够播报无障碍文本的内容；当组件同时包含文本属性时，在朗读场景优先播报无障碍文本。

**说明** 

该接口不支持在[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)中调用。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | string | 是 | 无障碍文本，当组件不包含文本属性时，屏幕朗读选中此组件时不播报，使用者无法清楚地知道当前选中了什么组件。为了解决此场景，开发人员可为不包含文字信息的组件设置无障碍文本，当屏幕朗读选中此组件时播报无障碍文本的内容，帮助屏幕朗读的使用者清楚地知道自己选中了什么组件。  默认值：“”  **说明：**  若组件既拥有文本属性，又拥有无障碍文本属性，则组件被选中时，仅播报无障碍文本内容。  若组件设置了无障碍分组属性为true，但是既没有无障碍文本属性，也没有文本属性，会对其子节点的组件进行文本拼接（深度优先）。  不对无障碍文本属性进行拼接，如需优先拼接无障碍文本，则需设置[accessibilityGroup](ts-universal-attributes-accessibility.md#accessibilitygroup14)的accessibilityPreferred。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前对象。 |

## accessibilityText12+

accessibilityText(text: Resource): T

设置无障碍文本，支持通过[Resource](ts-types.md#resource)引用资源文件。当组件不包含文本属性时，开发人员可通过设置无障碍文本属性，使不包含文字信息的组件能够播报无障碍文本的内容；当组件同时包含文本属性时，在朗读场景优先播报无障碍文本。

**说明** 

该接口不支持在[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)中调用。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| text | [Resource](ts-types.md#resource) | 是 | 无障碍文本引用资源，当组件不包含文本属性时，屏幕朗读选中此组件时不播报，使用者无法清楚地知道当前选中了什么组件。为了解决此场景，开发人员可为不包含文字信息的组件设置无障碍文本，当屏幕朗读选中此组件时播报无障碍文本的内容，帮助屏幕朗读的使用者清楚地知道自己选中了什么组件。  **说明：**  若组件既拥有文本属性，又拥有无障碍文本属性，则组件被选中时，仅播报无障碍文本内容。  若组件设置了无障碍分组属性为true，但是既没有无障碍文本属性，也没有文本属性，会对其子节点的组件进行文本拼接（深度优先）。  不对无障碍文本属性进行拼接，如需优先拼接无障碍文本，则需设置[accessibilityGroup](ts-universal-attributes-accessibility.md#accessibilitygroup14)的accessibilityPreferred。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前对象。 |

## accessibilityDescription

accessibilityDescription(value: string): T

设置无障碍说明。该属性用于为用户进一步说明当前组件，开发人员可为组件设置相对较详细的解释文本，帮助用户理解将要执行的操作。

**说明** 

该接口不支持在[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)中调用。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | string | 是 | 无障碍说明，用于为用户进一步说明当前组件，开发人员可为组件的该属性设置相对较详细的解释文本，帮助用户理解将要执行的操作。如帮助用户理解将要执行的操作可能导致什么后果，尤其是当这些后果无法从组件本身属性与无障碍文本中了解到时。若组件既拥有文本属性又拥有无障碍说明属性，则组件被选中时，先播报组件的文本属性，再播报无障碍说明属性的内容。  默认值：“” |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前对象。 |

## accessibilityDescription12+

accessibilityDescription(description: Resource): T

设置无障碍说明，支持通过[Resource](ts-types.md#resource)引用资源文件。该属性用于为用户进一步说明当前组件，开发人员可为组件设置相对较详细的解释文本，帮助用户理解将要执行的操作。

**说明** 

该接口不支持在[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)中调用。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| description | [Resource](ts-types.md#resource) | 是 | 无障碍说明引用资源，用于为用户进一步说明当前组件，开发人员可为组件的该属性设置相对较详细的解释文本，帮助用户理解将要执行的操作。如帮助用户理解将要执行的操作可能导致什么后果，尤其是当这些后果无法从组件本身属性与无障碍文本中了解到时。若组件既拥有文本属性又拥有无障碍说明属性，则组件被选中时，先播报组件的文本属性，再播报无障碍说明属性的内容。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前对象。 |

## accessibilityLevel

accessibilityLevel(value: string): T

设置无障碍重要性。该属性用于控制某个组件是否可被无障碍辅助服务所识别。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | string | 是 | 无障碍重要性，用于控制某个组件是否可被无障碍辅助服务所识别。  支持的值为：  "auto"：当前组件由无障碍辅助服务和ArkUI进行综合判断组件是否可被无障碍辅助服务所识别。  "yes"：当前组件可被无障碍辅助服务所识别。当父组件启用无障碍分组时，设置为"yes"的子组件不受分组约束，在满足屏幕朗读其他规则下仍可聚焦。  "no"：当前组件不可被无障碍辅助服务所识别。  "no-hide-descendants"：当前组件及其所有子组件不可被无障碍辅助服务所识别。  默认值："auto"  **说明：**  当accessibilityLevel设置成"auto"时，组件是否可被无障碍辅助服务所识别取决于以下多方面因素：  1. 组件是否可被识别由无障碍辅助服务内部判断，自行选择。  2. 若组件的父组件accessibilityGroup属性中isGroup设置为true，无障碍服务将不再关注其子组件内容，组件不可被无障碍辅助服务所识别。  3. 若组件的父组件accessibilityLevel属性设置为"no-hide-descendants"，组件不可被无障碍辅助服务所识别。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前对象。 |

## accessibilityVirtualNode11+

accessibilityVirtualNode(builder: CustomBuilder): T

设置无障碍虚拟子节点。对自绘制组件传入一个CustomBuilder，该CustomBuilder中的组件在后端仅做布局不做显示，辅助应用获取无障碍节点信息时会返回CustomBuilder中的节点信息。如使用画布组件[Canvas](ts-components-canvas-canvas.md)时，可以通过虚拟节点设置相应位置和大小匹配的占位组件，让无障碍服务识别到对应区域的自绘制信息。

**说明** 

该接口不支持在[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)中调用。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| builder | [CustomBuilder](ts-types.md#custombuilder8) | 是 | 无障碍虚拟子节点，使开发者可以对自绘制组件传入一个CustomBuilder，该CustomBuilder中的组件在后端仅做布局不做显示，辅助应用获取无障碍节点信息时会返回CustomBuilder中的节点信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前对象。 |

## accessibilityChecked13+

accessibilityChecked(isCheck: boolean): T

无障碍节点是否选中的状态维护，用于支持多选，表示组件是否被选中。此接口只影响屏幕朗读场景下的组件状态播报信息。

**说明** 

从API version 20开始，该接口支持在[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)中调用。

**卡片能力：** 从API version 13开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 13开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isCheck | boolean | 是 | 用于表示组件是否被选中。  支持的值为：  true：当前组件被选中。  false：当前组件未被选中。  undefined：由组件自行确定选中状态。  默认值：undefined  **说明：**  1. 使用该接口设置true或false后，会默认修改该组件的checkable属性为true。  2. accessibilityChecked属性代表组件是多选模式，而[accessibilitySelected](ts-universal-attributes-accessibility.md#accessibilityselected13)属性代表组件是单选模式。组件不能同时存在两种选择模式，会造成无障碍状态冲突，导致屏幕朗读等无障碍辅助应用无法正确识别选中状态。如使用当前接口设置组件为多选模式（设置为true、false），则需要保证未使用accessibilitySelected函数设置属性为true或者false，如果已设置，需使用accessibilitySelected函数设置accessibilitySelected属性为undefined模式。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前对象。 |

## accessibilitySelected13+

accessibilitySelected(isSelect: boolean): T

无障碍节点是否选中的状态维护，用于支持单选，表示组件是否被选中。此接口只影响屏幕朗读场景下的组件状态播报信息。

**说明** 

从API version 20开始，该接口支持在[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)中调用。

**卡片能力：** 从API version 13开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 13开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isSelect | boolean | 是 | 用于表示组件是否被选中。  支持的值为：  true：当前组件被选中。  false：当前组件未被选中。  undefined：由组件自行确定选中状态。  默认值：undefined  **说明：**  1. [accessibilityChecked](ts-universal-attributes-accessibility.md#accessibilitychecked13)属性代表组件是多选模式，而accessibilitySelected属性代表组件是单选模式。组件不能同时存在两种选择模式，会造成无障碍状态冲突，导致屏幕朗读等无障碍辅助应用无法正确识别选中状态。  如使用当前接口设置组件为单选模式（true、false），则需要保证未使用accessibilityChecked函数设置属性为true或者false；  如果已设置，需使用accessibilityChecked函数设置accessibilityChecked属性为undefined模式。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前对象。 |

## accessibilityRole18+

accessibilityRole(role: AccessibilityRoleType): T

设置无障碍组件类型，不同组件类型有对应的朗读方式，可以根据应用诉求，修改组件类型，用于控制无障碍模式下对组件的朗读方式和朗读内容。

**卡片能力：** 从API version 18开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| role | [AccessibilityRoleType](ts-universal-attributes-accessibility.md#accessibilityroletype18枚举说明) | 是 | 屏幕朗读播报的组件类型，如按钮、图表。具体类型可由开发者根据需要选择。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前对象。 |

## AccessibilityRoleType18+枚举说明

定义组件的屏幕朗读功能角色类型。

**卡片能力：** 从API version 18开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| ACTION\_SHEET | 0 | 列表弹窗。 |
| ALERT\_DIALOG | 1 | 显示警告弹窗组件。 |
| INDEXER\_COMPONENT | 2 | 索引器组件。 |
| BADGE\_COMPONENT | 3 | 信息标记组件。 |
| BLANK | 4 | 空白填充组件。 |
| BUTTON | 5 | 按钮。 |
| BACK\_BUTTON | 6 | 大图页返回按钮。 |
| SHEET\_DRAG\_BAR | 7 | 弹窗拖拽条。 |
| CALENDAR\_PICKER | 8 | 日历选择器组件。 |
| CALENDAR | 9 | 日历。 |
| CANVAS | 10 | 提供画布组件。 |
| CANVAS\_GRADIENT | 11 | 渐变对象。 |
| CANVAS\_PATTERN | 12 | 通过指定图像和重复方式创建图片填充的模板。 |
| CHECKBOX | 13 | 提供多选框组件。 |
| CHECKBOX\_GROUP | 14 | 多选框群组。 |
| CIRCLE | 15 | 用于绘制圆形的组件。 |
| COLUMN\_SPLIT | 16 | 将子组件纵向布局，并在每个子组件之间插入一根横向的分割线。 |
| COLUMN | 17 | 沿垂直方向布局的容器。 |
| CANVAS\_RENDERING\_CONTEXT\_2D | 18 | 用于在画布组件上绘制矩形、文本、图片等。 |
| CHART | 19 | 图表组件。 |
| COUNTER | 20 | 计数器组件。 |
| CONTAINER\_MODAL | 21 | 模态容器。 |
| DATA\_PANEL | 22 | 数据面板组件。 |
| DATE\_PICKER | 23 | 选择日期的滑动选择器组件。 |
| DIALOG | 24 | 弹出框。 |
| DIVIDER | 25 | 提供分隔器组件。 |
| DRAG\_BAR | 26 | 拖拽条。 |
| EFFECT\_COMPONENT | 27 | 特效合并容器组件。 |
| ELLIPSE | 28 | 椭圆绘制组件。 |
| FLEX | 29 | 以弹性方式布局子组件的容器组件。 |
| FLOW\_ITEM | 30 | 瀑布流组件的子组件。 |
| FORM\_COMPONENT | 31 | 提供卡片组件。 |
| FORM\_LINK | 32 | 静态卡片交互组件。 |
| GAUGE | 33 | 数据量规图表组件。 |
| GRID | 34 | 网格容器。 |
| GRID\_COL | 35 | 栅格子组件。 |
| GRID\_CONTAINER | 36 | 纵向排布栅格布局容器。 |
| GRID\_ITEM | 37 | 网格容器中单项内容容器。 |
| GRID\_ROW | 38 | 栅格容器组件。 |
| HYPERLINK | 39 | 超链接组件。 |
| IMAGE | 40 | 图片组件。 |
| IMAGE\_ANIMATOR | 41 | 提供帧动画组件。 |
| IMAGE\_BITMAP | 42 | 可在画布上绘制的位图图像对象。 |
| IMAGE\_DATA | 43 | 存储画布区域的像素数据。 |
| IMAGE\_SPAN | 44 | 用于显示行内图片。 |
| LABEL | 45 | 标签。 |
| LINE | 46 | 线型。 |
| LIST | 47 | 列表。 |
| LIST\_ITEM | 48 | 用来展示列表具体item。 |
| LIST\_ITEM\_GROUP | 49 | 用来展示列表item分组。 |
| LOADING\_PROGRESS | 50 | 用于显示加载动效的组件。 |
| MARQUEE | 51 | 跑马灯组件。 |
| MATRIX2D | 52 | 矩阵对象。 |
| MENU | 53 | 菜单。 |
| MENU\_ITEM | 54 | 菜单项。 |
| MENU\_ITEM\_GROUP | 55 | 菜单项分组。 |
| NAV\_DESTINATION | 56 | 显示Navigation的内容区。 |
| NAV\_ROUTER | 57 | 导航组件。 |
| NAVIGATION | 58 | 路由导航的根视图容器。 |
| NAVIGATION\_BAR | 59 | 导航栏。 |
| NAVIGATION\_MENU | 60 | 导航菜单。 |
| NAVIGATOR | 61 | 路由容器组件。 |
| OFFSCREEN\_CANVAS | 62 | 用于自定义绘制图形。 |
| OFFSCREEN\_CANVAS\_RENDERING\_CONTEXT2D | 63 | 2D绘制对象，用于在画布组件上绘制矩形、文本、图片等。 |
| OPTION | 64 | 具体项目。 |
| PANEL | 65 | 可滑动面板。 |
| PAPER\_PAGE | 66 | 页面。 |
| PATH | 67 | 路径绘制组件。 |
| PATH2D | 68 | 路径对象。 |
| PATTERN\_LOCK | 69 | 图案密码锁组件。 |
| PICKER | 70 | 选择器。 |
| PICKER\_VIEW | 71 | 选择器视图。 |
| PLUGIN\_COMPONENT | 72 | 新增插件组件。 |
| POLYGON | 73 | 多边形绘制组件。 |
| POLYLINE | 74 | 折线绘制组件。 |
| POPUP | 75 | 显示特定样式气泡。 |
| PROGRESS | 76 | 进度条组件。 |
| QRCODE | 77 | 二维码。 |
| RADIO | 78 | 单选框。 |
| RATING | 79 | 提供在给定范围内选择评分的组件。 |
| RECT | 80 | 矩形绘制组件。 |
| REFRESH | 81 | 下拉刷新容器组件。 |
| RELATIVE\_CONTAINER | 82 | 相对布局组件。 |
| REMOTE\_WINDOW | 83 | 远程控制窗口组件。 |
| RICH\_EDITOR | 84 | 支持图文混排和文本交互式编辑的组件。 |
| RICH\_TEXT | 85 | 富文本组件。 |
| ROLE\_PAGER | 86 | 分页。 |
| ROW | 87 | 沿水平方向布局容器。 |
| ROW\_SPLIT | 88 | 将子组件横向布局，并在每个子组件之间插入一根纵向的分割线。 |
| SCROLL | 89 | 可滚动的容器组件。 |
| SCROLL\_BAR | 90 | 滚动条。 |
| SEARCH | 91 | 搜索框组件。 |
| SEARCH\_FIELD | 92 | 搜索框。 |
| SELECT | 93 | 下拉选择菜单组件。 |
| SHAPE | 94 | 绘制组件的父组件。 |
| SIDEBAR\_CONTAINER | 95 | 提供侧边栏可以显示和隐藏的侧边栏容器。 |
| SLIDER | 96 | 滑动条组件。 |
| SPAN | 97 | 用于显示行内文本的组件。 |
| STACK | 98 | 堆叠容器。 |
| STEPPER | 99 | 步骤导航器组件。 |
| STEPPER\_ITEM | 100 | 用作Stepper组件的页面子组件。 |
| SWIPER | 101 | 滑块视图容器。 |
| SWIPER\_INDICATOR | 102 | 定义 Swiper 组件的导航指示器。 |
| SWITCH | 103 | 开关。 |
| SYMBOL\_GLYPH | 104 | 显示图标小符号的组件。 |
| TAB\_CONTENT | 105 | 仅在Tabs中使用，对应一个切换页签的内容视图。 |
| TAB\_BAR | 106 | 页签栏。 |
| TABS | 107 | 通过页签进行内容视图切换的容器组件。 |
| TEXT | 108 | 文本。 |
| TEXT\_CLOCK | 109 | 文本时钟组件。 |
| TEXT\_ENTRY | 110 | 文本输入。 |
| TEXT\_INPUT | 111 | 输入框组件。 |
| TEXT\_PICKER | 112 | 文本类滑动选择器组件。 |
| TEXT\_TIMER | 113 | 通过文本显示计时信息并控制其计时器状态的组件。 |
| TEXT\_AREA | 114 | 输入区域组件。 |
| TEXT\_FIELD | 115 | 文本框。 |
| TIME\_PICKER | 116 | 时间选择组件。 |
| TITLE\_BAR | 117 | 标题栏。 |
| TOGGLER | 118 | 状态组件。 |
| UI\_EXTENSION\_COMPONENT | 119 | 用户界面扩展组件。 |
| VIDEO | 120 | 用于播放视频文件并控制其播放状态的组件。 |
| WATER\_FLOW | 121 | 瀑布流容器。 |
| WEB | 122 | 加载网页组件。 |
| XCOMPONENT | 123 | 自定义渲染。 |
| ROLE\_NONE | 124 | 不设置特定的无障碍组件类型，组件按照自身默认类型进行屏幕朗读播报。 |

## accessibilityNextFocusId18+

accessibilityNextFocusId(nextId: string): T

指定屏幕朗读扫动走焦过程中组件的下一个焦点。

**卡片能力：** 从API version 18开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| nextId | string | 是 | 下一个被指定聚焦组件的[唯一标识id](ts-universal-attributes-component-id.md#id)。若唯一标识id无对应组件，则设置的accessibilityNextFocusId不存在，设置无效。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前对象。 |

## accessibilityNextFocusId

accessibilityNextFocusId(nextId: string, nextFocusParams: AccessibilityNextFocusParams | undefined): T

指定屏幕朗读扫动走焦过程中组件的下一个焦点，并支持配置详细参数。

通过[AccessibilityNextFocusParams](ts-types.md#accessibilitynextfocusparams)参数，可以配置是否在无障碍下一个焦点处理过程中查找后代节点中的焦点。

**起始版本：** 26.0.0

**卡片能力：** 从API版本26.0.0开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| nextId | string | 是 | 下一个被指定聚焦组件的[唯一标识id](ts-universal-attributes-component-id.md#id)。若唯一标识id无对应组件，则设置的accessibilityNextFocusId不存在，设置无效。 |
| nextFocusParams | [AccessibilityNextFocusParams](ts-types.md#accessibilitynextfocusparams) | undefined | 是 | 无障碍下一个焦点处理的详细参数，用于配置是否在后代节点中查找可聚焦节点。  取值为undefined时，不配置下一个焦点处理的详细参数，不在后代节点中查找焦点。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前对象。 |

## accessibilityDefaultFocus18+

accessibilityDefaultFocus(focus: boolean): T

为页面设置屏幕朗读初始焦点。屏幕朗读首次进入当前页面时，会将焦点定位到设置为true的组件，便于开发者引导用户优先关注页面核心内容。

**卡片能力：** 从API version 18开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| focus | boolean | 是 | 为页面设置屏幕朗读初始焦点。值为true则表示该组件为当前页默认首焦点，值为false则不设置该组件为默认首焦点。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前对象。 |

## accessibilityUseSamePage18+

accessibilityUseSamePage(pageMode: AccessibilitySamePageMode): T

设置当前组件和宿主应用为同page模式。

针对跨进程嵌入式显示的组件，例如[EmbeddedComponent](ts-container-embedded-component.md)，其子树场景中出现的跳焦问题，可通过设置accessibilityUseSamePage属性解决。因跨进程嵌入式显示的组件启动进程的页面变化事件与宿主页面变化事件发送时序不一致，可能导致焦点从当前组件移至另一组件，此现象称为“跳焦”。

**卡片能力：** 从API version 18开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| pageMode | [AccessibilitySamePageMode](ts-universal-attributes-accessibility.md#accessibilitysamepagemode18枚举说明) | 是 | 当前跨进程嵌入式显示的组件和宿主应用的同page模式。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前对象。 |

## AccessibilitySamePageMode18+枚举说明

当前跨进程嵌入式显示的组件和宿主应用的同page模式。

**卡片能力：** 从API version 18开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| SEMI\_SILENT | 0 | 跨进程嵌入式显示的组件所启动的进程中，首次加载页面时发送的page事件，以及该页面根节点发送的page事件，将被忽略。 |
| FULL\_SILENT | 1 | 跨进程嵌入式显示的组件将忽略所有的page事件。 |

## accessibilityScrollTriggerable18+

accessibilityScrollTriggerable(isTriggerable: boolean): T

设置无障碍节点是否支持屏幕朗读滚动操作。当屏幕朗读在扫动走焦时，若容器内当前页面无可聚焦的组件，会发起一次自动滚动操作。

**卡片能力：** 从API version 18开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isTriggerable | boolean | 是 | 用于表示组件是否支持该能力。  支持的值为：  true：屏幕朗读焦点切换而容器内当前页面无可聚焦的组件时，需要自动滚动操作。  false：屏幕朗读焦点切换而容器内当前页面无可聚焦的组件时，不需要自动滚动操作。  undefined：还原默认值。  默认值：true。  **说明：**  1. 该属性不影响原先无障碍节点属性[ElementAttributeValues](js-apis-inner-application-accessibilityextensioncontext.md#elementattributevalues)中的scrollable。  2. 组件在屏幕朗读下的滚动逻辑由屏幕朗读根据该属性和组件是否支持scroll来决定。  3. 该属性为通用属性，所有基础组件均可配置。建议配置的滚动组件类型，如[List](ts-container-list.md)、[Grid](ts-container-grid.md)、[Scroll](ts-container-scroll.md)、[WaterFlow](ts-container-waterflow.md)等。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前对象。 |

## accessibilityTextHint12+

accessibilityTextHint(value: string): T

设置组件的文本提示信息，仅在与车机交互的场景下供车机的无障碍服务监听并响应。

**说明** 

从API version 20开始，该接口支持在[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)中调用。该接口用于设置组件通用属性，通过该属性接口进行配置的文本内容仅会被车机的无障碍服务所监听并响应，因此该接口仅在与车机交互的场景下生效，用于和车机服务进行[地址推送联动](../harmonyos-guides/car-address-hop.md)。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | string | 是 | 组件的文本提示信息，仅在与车机交互的场景下供车机的无障碍服务监听并响应。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前对象。 |

## accessibilityFocusDrawLevel19+

accessibilityFocusDrawLevel(drawLevel: FocusDrawLevel): T

设置无障碍焦点绿框的绘制层级。

**说明** 

1. 在聚焦节点层级绘制获焦无障碍绿框，默认使用该层级绘制，由于组件的绘制顺序以及图形绘制顺序，绘制的绿框会被父组件或者[Z序控制](ts-universal-attributes-z-order.md)更高的兄弟组件遮挡裁切。
2. 在[Z序控制](ts-universal-attributes-z-order.md)顶层绘制绿框情况下，可以避免由于组件遮挡[overlay](ts-universal-attributes-overlay.md#overlay)、裁切[clip](ts-universal-attributes-sharp-clipping.md#clip12)导致无障碍绿框无法正常显示。但由于具备较高的绘制层级，如果在交互过程中需要遮挡当前获焦的组件，且不希望显示无障碍绿框，则不适合使用该配置。

**卡片能力：** 从API version 19开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| drawLevel | [FocusDrawLevel](ts-appendix-enums.md#focusdrawlevel19) | 是 | 无障碍焦点绿框的绘制层级，用于控制绿框的绘制位置。默认情况下在聚焦节点层级绘制（即绘制聚焦节点本身）。可选值及含义参见[FocusDrawLevel](ts-appendix-enums.md#focusdrawlevel19)枚举，包括在聚焦节点层级绘制和在Z序控制顶层绘制两种模式。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前对象。 |

## accessibilityStateDescription23+

accessibilityStateDescription(description: string | Resource | undefined): T

设置组件的状态播报文本，用于屏幕朗读场景下清晰说明组件当前的实时状态。屏幕朗读时会优先播报该状态文本。

**卡片能力：** 从API version 23开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| description | string | [Resource](ts-types.md#resource) | undefined | 是 | 需要播报组件当前状态的语音播报文本。  设置文本超过1000字符时，截取前1000字符进行播报。  undefined：播报文本默认为空。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前对象。 |

## accessibilityActionOptions23+

accessibilityActionOptions(option: AccessibilityActionOptions | undefined): T

设置组件无障碍操作的可选参数，用于限制或修改屏幕朗读等辅助应用发起的操作行为。

**卡片能力：** 从API version 23开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| option | [AccessibilityActionOptions](ts-types.md#accessibilityactionoptions23对象说明) | undefined | 是 | 无障碍操作的参数，用于限制或者修改无障碍操作下的滑动行为。  AccessibilityActionOptions中的scrollStep用于设置无障碍操作下的滑动步数。  取值为undefined时scrollStep按1处理。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前对象。 |

## accessibilityCustomActions

accessibilityCustomActions(actions: Array<AccessibilityCustomAction> | undefined): T

设置组件的自定义无障碍操作，支持开发者设置一个自定义actions的数组，用于给组件按操作名进行自定义操作的回调绑定。

**起始版本：** 26.0.0

**卡片能力：** 从API版本26.0.0开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| actions | Array<[AccessibilityCustomAction](ts-types.md#accessibilitycustomaction)> | undefined | 是 | 自定义无障碍操作数组，每个操作包含操作名称和回调，用于给组件按操作名进行自定义操作的回调绑定。  **说明：**  数组长度最大支持16个，超出部分将不生效。  取值为undefined时，不设置自定义操作。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前对象。 |

## 示例

### 示例1（设置无障碍文本和无障碍说明）

该示例主要演示accessibilityText无障碍文本和accessibilityDescription无障碍说明的播报内容。

```ts
// xxx.ets
@Entry
@Component
struct Index {
  @Builder
  customAccessibilityNode() {
    Column() {
      Text(`virtual node`)
    }
    .width(10)
    .height(10)
  }

  build() {
    Row() {
      Column() {
        Text('文本1')
          .fontSize(50)
          .fontWeight(FontWeight.Bold)
        Text("文本2")
          .fontSize(50)
          .fontWeight(FontWeight.Bold)
      }
      .width('100%')
      .accessibilityGroup(true)
      .accessibilityLevel("yes")
      .accessibilityText("分组") // 无障碍文本的内容，若组件既拥有文本属性又拥有无障碍文本属性，则组件被选中时，仅播报无障碍文本内容。
      .accessibilityDescription("Column组件可以被选中，播报的内容是“分组”")
      .accessibilityVirtualNode(this.customAccessibilityNode)
      .accessibilityChecked(true)
      .accessibilitySelected(undefined)
    }
    .height('100%')
  }
}
```

### 示例2（设置无障碍组）

该示例主要演示优先使用子组件的无障碍文本进行朗读。

```ts
// xxx.ets
@Entry
@Component
struct Index {
  build() {
    Column({ space: 10 }) {
      Text('123456')
        .focusable(true)
        .borderRadius(5)
        .accessibilityText("有accessibility有text优先读accessibility")
        .accessibilityLevel("yes")
      Button().accessibilityLevel("yes").accessibilityText("accessibility无text 读accessibility")
      Button("无accessibility有text 读text").accessibilityLevel("yes")
      Button()
      Button('btn123').accessibilityText('有accessibility有text btn123').accessibilityLevel('yes')
      Button('btn123').accessibilityLevel("yes")
    }
    .accessibilityGroup(true, { accessibilityPreferred: true })
    .borderWidth(5)
    .width('100%')
    .height('100%')
  }
}
```

### 示例3（设置首焦点和组件的下一个焦点）

该示例主要演示accessibilityDefaultFocus屏幕朗读当前页默认首焦点和accessibilityNextFocusId走焦过程中组件的下一个焦点。

```ts
// xxx.ets
@Entry
@Component
struct Index {
  build() {
    Column({ space: 20 }) {
      Text('Text Demo 1')
        .fontSize(50)
        .accessibilityLevel('yes')
        .accessibilityNextFocusId('text3')
      Text('Text Demo 2')
        .id('text2')
        .fontSize(50)
        .accessibilityLevel('yes')
        .accessibilityDefaultFocus(true)  // 设置该组件为屏幕朗读当前页默认首焦点
        .accessibilityNextFocusId('text4')
      Text('Text Demo 3')
        .id('text3')
        .fontSize(50)
        .accessibilityLevel('yes')
        .accessibilityNextFocusId('text2')
      Text('Text Demo 4')
        .id('text4')
        .fontSize(50)
        .accessibilityLevel('yes')
    }
    .height('100%')
    .width('100%')
  }
}
```

### 示例4（设置无障碍组件类型和文本提示信息）

该示例主要演示accessibilityRole无障碍组件类型和accessibilityTextHint供无障碍辅助应用查询的组件的文本提示信息。

```ts
// xxx.ets
@Entry
@Component
struct Index {
  @State isDownloading: boolean = false;
  @State hintStr: string = '点击开始下载';

  build() {
    Column({ space: 20 }) {
      Button(this.isDownloading ? '下载中' : '点击下载')
        .accessibilityLevel('yes')
        .accessibilityTextHint(this.hintStr)
        .onClick(() => {
          this.isDownloading = !this.isDownloading;
          this.hintStr = this.isDownloading ? '状态变为下载中' : '状态变为暂停下载';
        })
      TextInput({ placeholder: '请输入手机号码' })
        .accessibilityLevel('yes')
        .accessibilityTextHint('请输入11位手机号码')
        .width('80%')
      Text('按照按钮类型播报')
        .accessibilityLevel('yes')
        .accessibilityRole(AccessibilityRoleType.BUTTON)
        .accessibilityTextHint('屏幕朗读播报时，该组件将按照按钮类型进行播报')
        .fontSize(30)
    }
    .height('100%')
    .width('100%')
  }
}
```

### 示例5（设置无障碍屏幕朗读滚动和焦点绿框绘制）

该示例主要演示accessibilityScrollTriggerable设置无障碍节点是否支持屏幕朗读滚动、accessibilityFocusDrawLevel设置无障碍焦点绿框的绘制层级和accessibilityUseSamePage为跨进程嵌入式显示的组件（如[EmbeddedComponent](ts-container-embedded-component.md)）设置同page模式。

```ts
// xxx.ets
import { Want } from '@kit.AbilityKit';

@Entry
@Component
struct Index {
  @State message: string = 'Message: ';
  private want: Want = {
    // EmbeddedComponent提供方的bundleName，根据实际情况配置。
    bundleName: 'com.example.embeddeddemo',
    // EmbeddedComponent提供方的abilityName，根据实际情况配置。
    abilityName: 'ExampleEmbeddedAbility',
  }

  build() {
    Row() {
      List() {
        ListItem() {
          Column() {
            Text(this.message)
              .fontSize(18)
              .fontColor('#2D2D2D')
              .fontWeight(FontWeight.Medium)
            Column() {
              EmbeddedComponent(this.want, EmbeddedType.EMBEDDED_UI_EXTENSION)
                .onTerminated((info) => {
                  this.message = 'Termination: code = ' + info.code + ', want = ' + JSON.stringify(info.want);
                })
                .onError((error) => {
                  this.message = 'Error: code = ' + error.code;
                })
                .accessibilityUseSamePage(AccessibilitySamePageMode.FULL_SILENT)
                .width('90%')
                .height('50%')
                .backgroundColor('#F0F0F0')
                .borderRadius(8)
                .borderWidth(1)
                .borderColor('#D9D9D9')

              Stack() {
                Column() {
                  Text('文本1')
                    .fontSize(18)
                    .fontColor('#2D2D2D')
                    .fontWeight(FontWeight.Medium)
                  Text('文本1')
                    .fontSize(18)
                    .fontColor('#2D2D2D')
                    .fontWeight(FontWeight.Medium)
                    .accessibilityFocusDrawLevel(FocusDrawLevel.TOP)
                }
                .padding({ top: 8, bottom: 8 })

                Column() {
                  Text('文本2')
                    .fontSize(18)
                    .fontColor('#FFFFFF')
                    .fontWeight(FontWeight.Medium)
                  Text('文本2')
                    .fontSize(18)
                    .fontColor('#FFFFFF')
                    .fontWeight(FontWeight.Medium)
                }
                .backgroundColor('#4A90E2')
                .padding({
                  left: 12,
                  right: 12,
                  top: 10,
                  bottom: 10
                })
                .borderRadius(6)
              }
              .width('100%')
              .margin({ top: 10, bottom: 10 })
            }
            .width('100%')
            .height('100%')
            .margin({ top: 15 })
            .accessibilityText($r('app.string.app_name'))
            .accessibilityDescription($r('app.string.module_desc'))

            Column() {
              Text('文本4')
                .fontSize(18)
                .fontWeight(FontWeight.Medium)
            }
            .margin({ top: 15 })
          }
          .width('100%')
        }
      }
      .accessibilityScrollTriggerable(false)
      .width('100%')
    }
    .height('100%')
    .backgroundColor('#F7F9FC')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/99/v3/taan_b_7TUymNKUtZTAw4w/zh-cn_image_0000002712405912.png)

### 示例6（设置无障碍聚合功能下的子组件状态和操作接管功能）

该示例主要演示使用accessibilityGroup的可选参数stateControllerRoleType或者stateControllerId来选择一个特定子组件接管其无障碍状态信息，可选参数actionControllerRoleType或者actionControllerId来选择一个特定子组件接管其无障碍控制操作。

```ts
// xxx.ets
@Entry
@Component
struct Index {

  build() {
    Column({ space: 20 }) {
      Flex({ justifyContent: FlexAlign.SpaceEvenly, alignItems: ItemAlign.Center }) {
        Text('是否开启功能')
        Toggle({ type: ToggleType.Switch, isOn: false })
          .selectedColor('#007DFF')
          .switchPointColor('#FFFFFF')
          .onChange((isOn: boolean) => {
            console.info('Component status:' + isOn);
          })
      }
      .accessibilityGroup(true, {
        stateControllerRoleType: AccessibilityRoleType.TOGGLER,
        actionControllerRoleType: AccessibilityRoleType.TOGGLER
      })
      .width('80%')
      .border({ color: Color.Black, width: 2 })

      Flex({ justifyContent: FlexAlign.SpaceEvenly, alignItems: ItemAlign.Center }) {
        Text("是否开启功能")
        Toggle({ type: ToggleType.Switch, isOn: false })
          .selectedColor('#007DFF')
          .switchPointColor('#FFFFFF')
          .onChange((isOn: boolean) => {
            console.info('Component status:' + isOn);
          })
          .id("TestToggle")
      }
      .accessibilityGroup(true, {
        stateControllerId: "TestToggle",
        actionControllerId: "TestToggle"
      })
      .width('80%')
      .border({ color: Color.Black, width: 2 })

    }
    .height('100%')
    .width('100%')
  }
}
```

### 示例7（设置无障碍组件状态播报信息）

该示例主要通过[accessibilityStateDescription](ts-universal-attributes-accessibility.md#accessibilitystatedescription23)接口修改组件的状态播报。在开启无障碍功能后，组件发生聚焦或者点击后，屏幕朗读进行组件的状态信息播报。

从API version 23开始，新增accessibilityStateDescription接口。

```ts
// xxx.ets
@Entry
@Component
struct Index {
  @State isSelected: boolean = false;

  build() {
    Column({ space: 20 }) {
      Button(this.isSelected ? '已点赞' : '未点赞')
        .accessibilityLevel('yes')
        .onClick(() => {
          this.isSelected = !this.isSelected;
        })
        .accessibilityStateDescription(this.isSelected ? '已点赞' : '未点赞')
    }
    .height('100%')
    .width('100%')
  }
}
```

### 示例8（设置无障碍操作选项修改组件滚动步长）

本示例主要演示如何通过[accessibilityActionOptions](ts-types.md#accessibilityactionoptions23对象说明)中的scrollStep参数，自定义组件的滚动步长。以下将以slider组件在屏幕朗读场景下滑动距离变化为例进行说明。

从API version 23开始，新增AccessibilityActionOptions。

```ts
// xxx.ets
@Entry
@Component
struct Index {
  build() {
    Column({ space: 20 }) {
      Row() {
        Slider({
          min: 0,
          max: 100,
          style: SliderStyle.OutSet
        })
        // 调整屏幕朗读手势下slider滑动的步长
          .accessibilityActionOptions({ scrollStep: 10 })
      }
      .width('80%')
    }
    .height('100%')
    .width('100%')
  }
}
```

### 示例9（设置自定义无障碍操作）

本示例主要演示如何使用[accessibilityCustomActions](ts-universal-attributes-accessibility.md#accessibilitycustomactions)为组件设置自定义无障碍操作。开发者可以按操作名为组件进行自定义操作的回调绑定。

从API版本26.0.0开始，新增accessibilityCustomActions。

```ts
// xxx.ets
@Entry
@Component
struct Index {
  @State listData: Array<string> = ['列表项1', '列表项2', '列表项3', '列表项4'];

  build() {
    Column() {
      List({ space: 10 }) {
        ForEach(this.listData, (item: string, index: number) => {
          ListItem() {
            Row() {
              Text(item)
                .fontSize(16)
              Blank()
              Text('删除')
                .fontSize(14)
                .fontColor(Color.Red)
            }
            .width('100%')
            .padding(10)
            .onClick(() => {
              console.info('[TestTag] click success!')
            })
            .accessibilityLevel('yes')
            .accessibilityCustomActions([
              {
                name: 'deleteItem',
                onAction: () => {
                  this.listData.splice(index, 1);
                }
              }
            ])
          }
        }, (item: string) => item)
      }
      .width('100%')
      .height('100%')
    }
  }
}
```
