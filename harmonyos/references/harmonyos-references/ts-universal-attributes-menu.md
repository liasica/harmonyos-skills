---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-menu
title: 菜单控制
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 通用属性 > 弹窗控制 > 菜单控制
category: harmonyos-references
scraped_at: 2026-04-28T08:01:14+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:5dfbc5c01879c8682c6fc24bc70cad1dab3fd97fa4bb44382d02c821d1d66718
---

为组件绑定弹出式菜单，支持长按、点击或鼠标右键来触发菜单的弹出，菜单项以垂直列表形式显示。

说明

* 从API version 7开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。
* 不支持在CustomBuilder中使用bindMenu和bindContextMenu弹出多级菜单。对此，可以使用[Menu组件](ts-basic-components-menu.md)来实现多级菜单。
* 弹出菜单的文本内容不支持长按选中。
* 当窗口大小发生变化以及点击菜单内容区时，菜单自动隐藏。
* 如果绑定菜单的组件是可拖动节点且未指定bindContextMenu的preview，菜单弹出时会显示拖拽预览图，且菜单选项和预览图不会相互避让。开发者可根据使用场景设置preview或将目标节点设置为不可拖动。
* 从API version 12开始，菜单支持长按500ms弹出子菜单，支持按压态跟随手指移动。

  1. 仅支持使用[Menu组件](ts-basic-components-menu.md)且子组件包含[MenuItem](ts-basic-components-menuitem.md)或[MenuItemGroup](ts-basic-components-menuitemgroup.md)的场景。
  2. 仅支持[MenuPreviewMode](ts-universal-attributes-menu.md#menupreviewmode11)设置为NONE的菜单。
* 菜单最大宽度受设备所占栅格限制，即使设置宽度100%，也不会占满屏幕。
* 菜单绑定的组件对象销毁时，菜单消失。
* [bindContextMenu](ts-universal-attributes-menu.md#bindcontextmenu8)仅支持在子窗中显示，[bindMenu](ts-universal-attributes-menu.md#bindmenu)可以通过配置[MenuOptions](ts-universal-attributes-menu.md#menuoptions10)中的showInSubWindow属性设置是否在子窗中显示。

## bindMenu

PhonePC/2in1TabletTVWearable

bindMenu(content: Array<MenuElement> | CustomBuilder, options?: MenuOptions): T

给组件绑定菜单，点击后弹出菜单。弹出的菜单项支持图标+文本排列以及自定义组件两种功能。

说明

从API version 20开始，该接口仅当content的入参类型为Array<MenuElement>时支持在[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)中调用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| content | Array<[MenuElement](ts-universal-attributes-menu.md#menuelement)> | [CustomBuilder](ts-types.md#custombuilder8) | 是 | 配置菜单项图标和文本的数组，或者自定义组件。 |
| options | [MenuOptions](ts-universal-attributes-menu.md#menuoptions10) | 否 | 配置弹出菜单的参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## bindMenu11+

PhonePC/2in1TabletTVWearable

bindMenu(isShow: boolean, content: Array<MenuElement> | CustomBuilder, options?: MenuOptions): T

给组件绑定菜单，菜单的显隐通过控制绑定的isShow触发。弹出的菜单项支持图标+文本排列以及自定义组件两种功能。

说明

从API version 20开始，该接口仅当content的入参类型为Array<MenuElement>时支持在[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)中调用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isShow | boolean | 是 | 支持开发者通过状态变量控制显隐。菜单必须等待页面全部构建才能展示，因此不能在页面构建中设置为true，否则会导致显示位置及形状错误，该参数从API version 18开始支持[!!语法](../harmonyos-guides/arkts-new-binding.md#系统组件参数双向绑定)双向绑定变量。  true：弹出菜单；false：关闭菜单。  默认值：false |
| content | Array<[MenuElement](ts-universal-attributes-menu.md#menuelement)> | [CustomBuilder](ts-types.md#custombuilder8) | 是 | 配置菜单项图标和文本的数组，或者自定义组件。 |
| options | [MenuOptions](ts-universal-attributes-menu.md#menuoptions10) | 否 | 配置弹出菜单的参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## bindContextMenu8+

PhonePC/2in1TabletTVWearable

bindContextMenu(content: CustomBuilder, responseType: ResponseType, options?: ContextMenuOptions): T

给组件绑定菜单，控制菜单显隐的触发方式为长按或右键点击，弹出的菜单项需自定义。若需通过代码逻辑控制菜单显隐，请使用[bindContextMenu12+](ts-universal-attributes-menu.md#bindcontextmenu12)。

说明

* 不支持在输入法类型窗口中使用bindContextMenu(默认子窗实现)，详情见输入法框架的约束与限制说明[createPanel](js-apis-inputmethodengine.md#createpanel10-1)。
* 该接口不支持在[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)中调用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| content | [CustomBuilder](ts-types.md#custombuilder8) | 是 | 自定义菜单内容构造器。 |
| responseType | [ResponseType](ts-appendix-enums.md#responsetype8) | 是 | 菜单弹出条件，长按或者右键点击。不支持鼠标长按。 |
| options | [ContextMenuOptions](ts-universal-attributes-menu.md#contextmenuoptions10) | 否 | 配置弹出菜单的参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## bindContextMenu12+

PhonePC/2in1TabletTVWearable

bindContextMenu(isShown: boolean, content: CustomBuilder, options?: ContextMenuOptions): T

给组件绑定菜单，菜单的显隐通过控制绑定的isShown触发。

当isShown为true时，弹出菜单；为false时，隐藏菜单。菜单项支持自定义。

菜单弹出位置仅由placement设置决定，与点击位置无关。

说明

* 不支持在输入法类型窗口中使用bindContextMenu(默认子窗实现)，详情见输入法框架的约束与限制说明[createPanel](js-apis-inputmethodengine.md#createpanel10-1)。
* 该接口不支持在[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)中调用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isShown | boolean | 是 | 支持开发者通过状态变量控制显隐。菜单必须等待页面全部构建完成后才能展示，如果在页面构建前或构建中设置为true，可能导致显示位置及形状错误、无法正常弹出显示等问题。不支持长按触发拖拽。该参数从API version 18开始支持[!!语法](../harmonyos-guides/arkts-new-binding.md#系统组件参数双向绑定)双向绑定变量。  true：弹出菜单；false：关闭菜单。  默认值：false |
| content | [CustomBuilder](ts-types.md#custombuilder8) | 是 | 自定义菜单内容构造器。 |
| options | [ContextMenuOptions](ts-universal-attributes-menu.md#contextmenuoptions10) | 否 | 配置弹出菜单的参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## bindContextMenuWithResponse23+

PhonePC/2in1TabletTVWearable

bindContextMenuWithResponse(content: CustomBuilderT<ResponseType> | undefined, options?: ContextMenuOptions): T

给组件绑定菜单，控制菜单显隐的触发方式为长按或右键点击，弹出的菜单需自定义样式和内容。

说明

* 不支持在输入法类型窗口中使用bindContextMenuWithResponse（默认子窗实现），详情见输入法框架的约束与限制说明[createPanel](js-apis-inputmethodengine.md#createpanel10-1)。
* 该接口不支持在[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)中调用。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| content | [CustomBuilderT](ts-types.md#custombuildertt23)[<ResponseType>](ts-appendix-enums.md#responsetype8) | undefined | 是 | 自定义菜单内容构造器。入参为触发菜单的方式，开发者可据此实现差异化的内容。当传入undefined时，无菜单弹出。 |
| options | [ContextMenuOptions](ts-universal-attributes-menu.md#contextmenuoptions10) | 否 | 配置弹出菜单的参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## MenuElement

PhonePC/2in1TabletTVWearable

菜单项的图标、文本和交互信息。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| value | [ResourceStr](ts-types.md#resourcestr) | 否 | 否 | 菜单项文本。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| icon10+ | [ResourceStr](ts-types.md#resourcestr) | 否 | 是 | 菜单项图标。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| enabled11+ | boolean | 否 | 是 | 菜单条目是否可进行交互。  true：菜单条目可以进行交互；false：菜单条目不可以进行交互。  默认值：true  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| action | () => void | 否 | 否 | 点击菜单项的事件回调。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| symbolIcon12+ | [SymbolGlyphModifier](ts-universal-attributes-text-style.md#symbolglyphmodifier12) | 否 | 是 | 设置菜单项图标。通过Modifier配置菜单项图标，若同时配置symbolIcon和icon的情况下，icon图标不显示。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |

## MenuOptions10+

PhonePC/2in1TabletTVWearable

菜单项的信息，继承自[ContextMenuOptions](ts-universal-attributes-menu.md#contextmenuoptions10)。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| title | [ResourceStr](ts-types.md#resourcestr) | 否 | 是 | 菜单标题。  **说明：**  仅在content设置为Array<[MenuElement](ts-universal-attributes-menu.md#menuelement)> 时生效。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| showInSubWindow11+ | boolean | 否 | 是 | 是否在子窗口显示菜单。  true：在子窗口显示菜单；false：不在子窗显示菜单。  默认值：2in1设备上为true，其他设备为false。  **说明：**  仅对2in1设备生效。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |

## ContextMenuOptions10+

PhonePC/2in1TabletTVWearable

菜单项的信息。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| offset | [Position](ts-types.md#position) | 否 | 是 | 菜单弹出位置的偏移量，不会导致菜单显示超出屏幕范围。  默认值：{ x: 0, y: 0 }，不支持设置百分比。  **说明：**  菜单类型为相对父组件区域弹出时，自动根据菜单位置属性 (placement)将区域的宽或高计入偏移量中。  offset最终取值与placement设置值的关系参见表1：同时设置offset与placement时菜单的偏移位置。  未设置、异常值或者undefined时按默认{ x: 0, y: 0 }处理。若传入偏移量超出屏幕范围外，则会就近约束到屏幕范围内。  如果菜单调整了显示位置（与placement初始值主方向不一致），则偏移值 (offset) 失效。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| placement | [Placement](ts-appendix-enums.md#placement8) | 否 | 是 | 菜单组件优先显示的位置，当前位置显示不下时，会自动调整位置。  **说明：**  1. 作为[bindMenu](ts-universal-attributes-menu.md#bindmenu11)入参时，默认值为Placement.BottomLeft。  2. 作为[bindContextMenu8+](ts-universal-attributes-menu.md#bindcontextmenu8)或[bindContextMenuWithResponse23+](ts-universal-attributes-menu.md#bindcontextmenuwithresponse23)入参时，默认效果为菜单跟随点击位置弹出。  3. 作为[bindContextMenu12+](ts-universal-attributes-menu.md#bindcontextmenu12)入参时，默认值为Placement.BottomLeft。  4. placement值设置为undefined、null或缺省时，按默认值处理。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| enableArrow | boolean | 否 | 是 | 是否显示箭头。如果菜单的大小和位置不足以放置箭头时，不会显示箭头。  默认值：false，不显示箭头。  **说明：**  enableArrow为true时，placement未设置或者值为非法值，默认在目标物上方显示（此时菜单默认位置与接口的关系参见表3：enableArrow为true且placement未设置或者值为非法值的菜单默认位置），否则按照placement的位置优先显示。当前位置显示不下时，会自动调整位置，enableArrow为undefined时，不显示箭头。bindContextMenu从API version 10开始支持该属性；bindMenu从API version 12开始支持该属性。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| enableHoverMode18+ | boolean | 否 | 是 | 菜单组件是否响应悬停态（半折叠状态）变化，即在悬停态下是否触发避让折痕区域。  默认值：false，2in1设备默认为true。未设置或者值为非法值时，生效默认值。  **说明：**  1. 如果菜单的弹出位置在悬停态折痕区域，菜单组件不会响应悬停态。  2. 2in1设备从API version 20开始生效。  3. 2in1设备仅在窗口瀑布模式下生效。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| arrowOffset | [Length](ts-types.md#length) | 否 | 是 | 箭头在菜单处的偏移。偏移量必须合法且转换为具体数值时大于0才会生效，另外该值生效时不会导致箭头超出菜单四周的安全距离。  默认值：0  单位：vp  **说明：**  箭头距菜单四周的安全距离为菜单圆角大小与箭头宽度的一半之和。  根据配置的placement来计算是在水平还是垂直方向上偏移。  箭头在菜单水平方向时，偏移量为箭头至最左侧箭头安全距离处的距离。箭头在菜单垂直方向时，偏移量为箭头至最上侧箭头安全距离处的距离。  根据配置的placement的不同，箭头展示的默认位置不同：  在菜单不发生避让的情况下，箭头最终位置与placement设置值的关系参见表2：同时设置arrowOffset与placement时菜单箭头的默认位置。  bindContextMenu从API version 10开始支持该属性；bindMenu从API version 12开始支持该属性。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| preview11+ | [MenuPreviewMode](ts-universal-attributes-menu.md#menupreviewmode11) | [CustomBuilder](ts-types.md#custombuilder8) | 否 | 是 | 长按悬浮菜单或使用[bindContextMenu12+](ts-universal-attributes-menu.md#bindcontextmenu12)显示菜单的预览内容样式，可以为目标组件的截图，也可以为用户自定义的内容。  默认值：MenuPreviewMode.NONE，无预览内容。  **说明：**  - 不支持responseType为ResponseType.RightClick时触发，如果responseType为ResponseType.RightClick，则不会显示预览内容。  - 当未设置preview参数或preview参数设置为MenuPreviewMode.NONE时，enableArrow参数生效。  - 当preview参数设置为MenuPreviewMode.IMAGE或CustomBuilder时，enableArrow为true时也不显示箭头。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| previewAnimationOptions11+ | [ContextMenuAnimationOptions](ts-universal-attributes-menu.md#contextmenuanimationoptions11) | 否 | 是 | 控制长按预览的显示效果。  默认值：{ scale: [0.95, 1.1], transition: undefined, hoverScale: undefined }。  **说明：**  倍率设置参数小于等于0时，不生效。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| previewBorderRadius19+ | [BorderRadiusType](ts-universal-attributes-menu.md#borderradiustype19) | 否 | 是 | 设置预览图边框圆角半径。  默认值：16vp  **说明：**  当水平方向上两个圆角半径之和的最大值超过预览图的宽度，或者垂直方向上两个圆角半径之和的最大值超过预览图的高度时，应采用预览图所能允许的最大圆角半径值。  圆角设置越大，圆角动画变化越快。  **元服务API：** 从API version 19开始，该接口支持在元服务中使用。 |
| layoutRegionMargin13+ | [Margin](ts-types.md#margin) | 否 | 是 | 设置预览图与菜单布局时距上下左右边界的最小边距。  **说明：**  仅支持vp、px、fp、lpx、百分比。  当margin设置异常值或负值时，按默认值处理。  若preview为CustomBuilder，设置margin.left或margin.right时，预览图取消最大栅格的宽度限制。  注意应避免设置过大的margin导致布局区域变小，使得预览图和菜单无法正常布局。  当水平方向上margin之和超过布局最大宽度时，margin.left和margin.right均不生效，按默认值处理。  当垂直方向上margin之和超过布局最大高度时，margin.top和margin.bottom均不生效，按默认值处理。  边距默认值为左右边距16vp，上边距16vp, 下边距为4vp。  **元服务API：** 从API version 13开始，该接口支持在元服务中使用。 |
| previewScaleMode20+ | [PreviewScaleMode](ts-universal-attributes-menu.md#previewscalemode20枚举说明) | 否 | 是 | 预览图缩放方式。  默认值：PreviewScaleMode.AUTO  **说明：**  布局空间不足时，控制预览图的缩放方式。未设置或设置undefined按照PreviewScaleMode.AUTO处理。当设置成PreviewScaleMode.CONSTANT时，如果预览图过大，剩余的空间不足以放置菜单时，菜单将重叠显示在预览图之下。  预览图的最大宽高不会超过预览图最大可布局区域（窗口大小减去上下左右的安全边距）。  **元服务API：** 从API version 20开始，该接口支持在元服务中使用。 |
| availableLayoutArea20+ | [AvailableLayoutArea](ts-universal-attributes-menu.md#availablelayoutarea20枚举说明) | 否 | 是 | 设置预览图宽高的可布局区域，预览图的百分比依据此设置计算，最终可能因安全区限制而被压缩或裁剪。  **说明：**  未设置或设置为undefined时，百分比依据窗口大小计算。若设置为AvailableLayoutArea.SAFE\_AREA，预览图的可布局区域为窗口大小减去上下左右的安全边距。  **元服务API：** 从API version 20开始，该接口支持在元服务中使用。 |
| onAppear | () => void | 否 | 是 | 菜单弹出后的事件回调。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| onDisappear | () => void | 否 | 是 | 菜单消失后的事件回调。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| aboutToAppear11+ | () => void | 否 | 是 | 菜单显示动效前的事件回调。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| aboutToDisappear11+ | () => void | 否 | 是 | 菜单退出动效前的事件回调。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| backgroundColor11+ | [ResourceColor](ts-types.md#resourcecolor) | 否 | 是 | 菜单背板颜色。  默认值：Color.Transparent。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| backgroundBlurStyle11+ | [BlurStyle](ts-universal-attributes-background.md#blurstyle9) | 否 | 是 | 菜单背板模糊材质。  默认值：BlurStyle.COMPONENT\_ULTRA\_THICK。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| transition12+ | [TransitionEffect](ts-transition-animation-component.md#transitioneffect10对象说明) | 否 | 是 | 设置菜单显示和退出的过渡效果。  **说明：**  菜单退出动效过程中，进行横竖屏切换，菜单会避让。二级菜单不继承自定义动效。弹出过程可以点击二级菜单，退出动效执行过程不允许点击二级菜单。  详细描述见[TransitionEffect](ts-transition-animation-component.md#transitioneffect10对象说明)对象说明。  动效曲线使用弹簧曲线，在动效退出时，由于弹簧曲线的回弹震荡，菜单消失后有较长的拖尾，使得其他事件无法响应。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| borderRadius12+ | [Length](ts-types.md#length) | [BorderRadiuses](ts-types.md#borderradiuses9) | [LocalizedBorderRadiuses](ts-types.md#localizedborderradiuses12) | 否 | 是 | 设置菜单的边框圆角半径。  默认值：2in1设备上默认值8vp，其他设备上默认值20vp。  **说明：**  支持百分比。  当水平方向两个圆角半径之和的最大值超出菜单宽度或垂直方向两个圆角半径之和的最大值超出菜单高度时，采用菜单默认圆角半径值。  当设置Length类型且传参为异常值时，菜单圆角取默认值。  当设置BorderRadiuses或LocalizedBorderRadiuses类型且传参为异常值时，菜单默认没有圆角。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| backgroundBlurStyleOptions18+ | [BackgroundBlurStyleOptions](ts-universal-attributes-background.md#backgroundblurstyleoptions10对象说明) | 否 | 是 | 背景模糊效果。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| backgroundEffect18+ | [BackgroundEffectOptions](ts-universal-attributes-background.md#backgroundeffectoptions11) | 否 | 是 | 背景效果参数。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| hapticFeedbackMode18+ | [HapticFeedbackMode](ts-universal-attributes-menu.md#hapticfeedbackmode18) | 否 | 是 | 菜单弹出时振动效果。  默认值：HapticFeedbackMode.DISABLED，菜单弹出时不振动。  **说明：**  只有一级菜单可配置弹出时振动效果。  仅当用户启用系统触感反馈且在工程的[module.json5](../harmonyos-guides/module-configuration-file.md)中配置requestPermissions字段开启ohos.permission.VIBRATE振动权限时，方可生效。配置如下：    **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| outlineWidth20+ | [Dimension](ts-types.md#dimension10) | [EdgeOutlineWidths](ts-types.md#edgeoutlinewidths11对象说明) | 否 | 是 | 设置菜单边框外描边宽度。  默认值：0vp  **说明：**  不支持百分比，若需要外描边效果，outlineWidth为必填项。  **元服务API：** 从API version 20开始，该接口支持在元服务中使用。 |
| outlineColor20+ | [ResourceColor](ts-types.md#resourcecolor) | [EdgeColors](ts-types.md#edgecolors9) | 否 | 是 | 设置菜单边框外描边颜色。  **说明：**  默认值：'#19ffffff'  **元服务API：** 从API version 20开始，该接口支持在元服务中使用。 |
| mask20+ | boolean | [MenuMaskType](ts-universal-attributes-menu.md#menumasktype20类型说明) | 否 | 是 | 设置菜单是否有蒙层及蒙层样式。  true：有蒙层；false：没有蒙层；MenuMaskType：自定义蒙层的样式。  默认值：菜单有预览图时默认显示蒙层，否则不显示。  **说明：**  当设备配置不显示菜单蒙层时，该接口不生效。如当前在2in1设备上该接口不生效。  **元服务API：** 从API version 20开始，该接口支持在元服务中使用。 |
| modalMode20+ | [ModalMode](ts-universal-attributes-menu.md#modalmode20枚举说明) | 否 | 是 | 设置菜单的模态模式。  **说明：**  默认值：ModalMode.AUTO  **元服务API：** 从API version 20开始，该接口支持在元服务中使用。 |
| anchorPosition20+ | [Position](ts-types.md#position) | 否 | 是 | 通过设定水平与垂直偏移量，控制菜单相对于绑定组件左上角的弹出位置，与单独使用offset接口不同的是可以覆盖显示在绑定组件上。  默认值：{ x: undefined, y: undefined }，不支持设置百分比。  **说明：**  1. 当菜单处于预览状态时，设定的偏移量将无法生效。  2. 预设的placement对齐参数将不再生效。  3. 叠加offset参数的偏移量，最终确定菜单的精确弹出位置。  4. 当水平与垂直偏移量均设为负值时，菜单重置到Placement.BottomLeft进行显示。  5. 当水平或垂直偏移量存在undefined或null时，效果等同于不设置anchorPosition，此时预设的placement对齐参数可以生效。  **元服务API：** 从API version 20开始，该接口支持在元服务中使用。 |
| onWillAppear20+ | [Callback<void>](ts-types.md#callback12) | 否 | 是 | 菜单显示动效前的事件回调。  **说明：**  1. 正常时序依次为：aboutToAppear>>onWillAppear>>onAppear>>onDidAppear>>aboutToDisappear>>onWillDisappear>>onDisappear>>onDidDisappear。  2. aboutToAppear是初始化时触发调用，onWillAppear是在动画执行前触发调用，onWillAppear在aboutToAppear之后执行。  **元服务API：** 从API version 20开始，该接口支持在元服务中使用。 |
| onDidAppear20+ | [Callback<void>](ts-types.md#callback12) | 否 | 是 | 菜单弹出后的事件回调。  **说明：**  1. 正常时序依次为：aboutToAppear>>onWillAppear>>onAppear>>onDidAppear>>aboutToDisappear>>onWillDisappear>>onDisappear>>onDidDisappear。  2. 快速点击弹出，消失菜单时，存在onWillDisappear在onDidAppear前生效。  3. 当菜单入场动效未完成时关闭菜单，该回调不会触发。  4.onAppear和onDidAppear触发时机相同，onDidAppear在onAppear后生效。  **元服务API：** 从API version 20开始，该接口支持在元服务中使用。 |
| onWillDisappear20+ | [Callback<void>](ts-types.md#callback12) | 否 | 是 | 菜单退出动效前的事件回调。  **说明：**  1. 正常时序依次为：aboutToAppear>>onWillAppear>>onAppear>>onDidAppear>>aboutToDisappear>>onWillDisappear>>onDisappear>>onDidDisappear。  2. 快速点击弹出，消失菜单时，存在onWillDisappear在onDidAppear前生效。  3. aboutToDisappear和onWillDisappear触发时机相同，onWillDisappear在aboutToDisappear后生效。  **元服务API：** 从API version 20开始，该接口支持在元服务中使用。 |
| onDidDisappear20+ | [Callback<void>](ts-types.md#callback12) | 否 | 是 | 菜单消失后的事件回调。  **说明：**  1. 正常时序依次为：aboutToAppear>>onWillAppear>>onAppear>>onDidAppear>>aboutToDisappear>>onWillDisappear>>onDisappear>>onDidDisappear。  2. onDisappear和onDidDisappear触发时机相同，onDidDisappear在onDisappear后生效。  **元服务API：** 从API version 20开始，该接口支持在元服务中使用。 |
| keyboardAvoidMode23+ | [MenuKeyboardAvoidMode](ts-universal-attributes-menu.md#menukeyboardavoidmode23枚举说明) | 否 | 是 | 设置菜单是否避让软键盘。  **说明：**  未设置或设置为undefined时，按照MenuKeyboardAvoidMode.NONE处理。  **元服务API：** 从API version 23开始，该接口支持在元服务中使用。  **模型约束：** 此接口仅可在Stage模型下使用。 |
| minKeyboardAvoidDistance23+ | [LengthMetrics](js-apis-arkui-graphics.md#lengthmetrics12) | 否 | 是 | 设置菜单避让软键盘的最小距离。  **说明：**  未设置、设置为负数或undefined时，按照8vp处理。仅在keyboardAvoidMode设置为避让软键盘时生效。  **元服务API：** 从API version 23开始，该接口支持在元服务中使用。  **模型约束：** 此接口仅可在Stage模型下使用。 |

**表1：同时设置offset与placement时菜单的偏移位置**

| placement设置的值 | 菜单的偏移量说明 |
| --- | --- |
| Placement.TopLeft、Placement.Top、Placement.TopRight | offset的x为正数，菜单相对组件向右进行偏移，offset的y为正数，菜单相对组件向上进行偏移。 |
| Placement.BottomLeft、Placement.Bottom、Placement.BottomRight | offset的x为正数，菜单相对组件向左进行偏移，offset的y为正数，菜单相对组件向下进行偏移。 |
| Placement.RightTop、Placement.Right、Placement.RightBottom | offset的x为正数，菜单相对组件向右进行偏移，offset的y为正数，菜单相对组件向下进行偏移。 |

**表2：同时设置arrowOffset与placement时菜单箭头的默认位置**

| placement设置的值 | 菜单箭头的位置说明 |
| --- | --- |
| Placement.Top、Placement.Bottom | 箭头显示在水平方向且默认居中，且距离菜单左侧边缘距离为箭头安全距离。 |
| Placement.Left、Placement.Right | 箭头显示在垂直方向且默认居中，且距离菜单上侧距离为箭头安全距离。 |
| Placement.TopLeft、Placement.BottomLeft | 箭头默认显示在水平方向，且距离菜单左侧边缘距离为箭头安全距离。 |
| Placement.TopRight、Placement.BottomRight | 箭头默认显示在水平方向，且距离菜单右侧距离为箭头安全距离。 |
| Placement.LeftTop、Placement.RightTop | 箭头默认显示在垂直方向，且距离菜单上侧距离为箭头安全距离。 |
| Placement.LeftBottom、Placement.RightBottom | 箭头默认显示在垂直方向，且距离菜单下侧距离为箭头安全距离。 |

**表3：enableArrow为true且placement未设置或者值为非法值的菜单默认位置**

| 接口 | 菜单默认位置 |
| --- | --- |
| [bindMenu](ts-universal-attributes-menu.md#bindmenu) | Placement.BottomLeft |
| [bindMenu11+](ts-universal-attributes-menu.md#bindmenu11) | Placement.BottomLeft |
| [bindContextMenu8+](ts-universal-attributes-menu.md#bindcontextmenu8) | Placement.Top |
| [bindContextMenu12+](ts-universal-attributes-menu.md#bindcontextmenu12) | Placement.BottomLeft |
| [bindContextMenuWithResponse23+](ts-universal-attributes-menu.md#bindcontextmenuwithresponse23) | Placement.Top |

## MenuPreviewMode11+

PhonePC/2in1TabletTVWearable

菜单的预览样式。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| NONE | 0 | 不显示预览内容。 |
| IMAGE | 1 | 预览内容为触发长按悬浮菜单组件的截图。 |

## ContextMenuAnimationOptions11+

PhonePC/2in1TabletTVWearable

长按预览时显示的样式信息。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| scale | [AnimationRange](ts-universal-attributes-menu.md#animationrange11)<number> | 否 | 是 | 动画开始和结束时相对预览原图缩放比例。  默认值：[0.95, 1.1]  **说明：**  缩放比例需要根据实际开发场景设置，建议设置值为小于预览图宽度或布局的最大限制。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| transition12+ | [TransitionEffect](ts-transition-animation-component.md#transitioneffect10对象说明) | 否 | 是 | 设置菜单显示和退出的过渡效果。  **说明：**  在菜单退出动效过程中，横竖屏切换时，菜单会避让。二级菜单不继承自定义动效。弹出过程中可以点击二级菜单，但在退出动效执行过程中不允许点击二级菜单。  详细描述见[TransitionEffect](ts-transition-animation-component.md#transitioneffect10对象说明)对象说明。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| hoverScale12+ | [AnimationRange](ts-universal-attributes-menu.md#animationrange11)<number> | 否 | 是 | 在自定义预览图（preview为CustomBuilder类型）以及长按弹出（responseType指定为LongPress）菜单的场景下，hoverScale用于为绑定组件的截图浮起动画设置两个参数：相对于预览原图的起始与结束缩放比例。hoverScale设置后，浮起动画和预览图之间会有切换过渡动效。  **说明：**  倍率设置参数小于等于0时，不生效。  [bindContextMenu12+](ts-universal-attributes-menu.md#bindcontextmenu12)场景下，不生效。  设置transition接口时，不生效。  使用此接口且同时使用scale接口时，scale接口起始值不生效。  为保障最佳体验，最终预览图尺寸不建议小于原组件截图尺寸。当前预览动效宽高会受组件截图和自定义预览大小影响，请根据实际使用情况自行保障展示效果。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| hoverScaleInterruption20+ | boolean | 否 | 是 | 在自定义预览图（preview为CustomBuilder类型）以及长按弹出（responseType指定为LongPress）菜单的场景下，且hoverScaleInterruption为true时，在触发拖拽效果前抬起手是否允许取消预览菜单弹出。true表示允许取消预览菜单弹出，false表示不允许取消预览菜单弹出。  默认值：false  **说明：**  未设置hoverScale接口或设置了transition接口时，该参数不生效。长按时长不足以触发拖拽效果时抬起手，预览菜单hoverScale效果回退，预览菜单不弹出，并可触发原组件上绑定的click等手势事件。长按时长足以触发拖拽效果后抬起手，预览菜单正常弹出，并不再触发原组件上绑定的click等手势事件。  **元服务API：** 从API version 20开始，该接口支持在元服务中使用。 |

## AnimationRange11+

PhonePC/2in1TabletTVWearable

type AnimationRange<T>=[from: T, to: T]

动画开始和结束时相对预览原图缩放比例。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

| 类型 | 说明 |
| --- | --- |
| [from: T, to: T] | from表示动画开始时相对预览原图缩放比例，to表示动画结束时相对预览原图缩放比例。 |

## HapticFeedbackMode18+

PhonePC/2in1TabletTVWearable

菜单弹出时振动效果。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| DISABLED | 0 | 菜单弹出时不振动。 |
| ENABLED | 1 | 菜单弹出时振动。 |
| AUTO | 2 | 菜单振动效果跟随系统，当前为菜单有蒙层时振动。 |

## BorderRadiusType19+

PhonePC/2in1TabletTVWearable

type BorderRadiusType = [Length](ts-types.md#length) | [BorderRadiuses](ts-types.md#borderradiuses9) | [LocalizedBorderRadiuses](ts-types.md#localizedborderradiuses12)

圆角类型。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 说明 |
| --- | --- |
| [Length](ts-types.md#length) | 长度类型，用于描述尺寸单位。 |
| [BorderRadiuses](ts-types.md#borderradiuses9) | 圆角类型，用于描述组件边框圆角半径。 |
| [LocalizedBorderRadiuses](ts-types.md#localizedborderradiuses12) | 圆角类型，用于描述组件边框圆角半径。 |

## MenuMaskType20+类型说明

PhonePC/2in1TabletTVWearable

设置蒙层样式。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| color | [ResourceColor](ts-types.md#resourcecolor) | 否 | 是 | 设置蒙层颜色。  默认值：$r('sys.color.ohos\_id\_color\_mask\_thin') |
| backgroundBlurStyle | [BlurStyle](ts-universal-attributes-background.md#blurstyle9) | 否 | 是 | 设置蒙层模糊材质。  默认值：BlurStyle.BACKGROUND\_THIN |

## ModalMode20+枚举说明

PhonePC/2in1TabletTVWearable

子窗菜单的模态模式。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| AUTO | 0 | 自动模式，菜单组件在当前设备的默认行为。当前版本在所有设备上的效果等同于ModalMode.NONE。 |
| NONE | 1 | 除菜单自身区域外，其他区域均可传递事件，下层控件可响应事件。 |
| TARGET\_WINDOW | 2 | 菜单所在应用的窗口与菜单区域不可传递事件，其他区域可传递事件。 |

## PreviewScaleMode20+枚举说明

PhonePC/2in1TabletTVWearable

预览图的缩放方式。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| AUTO | 0 | 预览图根据[Placement](ts-appendix-enums.md#placement8)自动调整预览图宽高及缩放。 |
| CONSTANT | 1 | 预览图不缩放，大小保持不变。最终仍会受到安全区的限制而出现压缩、裁剪。 |
| MAINTAIN | 2 | 预览图缩放时保持宽高比。 |

## AvailableLayoutArea20+枚举说明

PhonePC/2in1TabletTVWearable

预览图宽高设置为百分比时的参考可布局区域大小。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| SAFE\_AREA | 0 | 参考可布局区域大小为窗口大小减去上下左右安全边距。 |

## MenuKeyboardAvoidMode23+枚举说明

PhonePC/2in1TabletTVWearable

菜单避让软键盘的模式。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**模型约束：** 此接口仅可在Stage模型下使用。

| 名称 | 值 | 说明 |
| --- | --- | --- |
| NONE | 0 | 菜单不避让软键盘。 |
| TRANSLATE\_AND\_RESIZE | 1 | 菜单避让软键盘。如果空间不足，会平移或重新调整菜单大小避让软键盘。 |

## 示例

PhonePC/2in1TabletTVWearable

### 示例1（弹出普通菜单）

该示例为bindMenu通过配置[MenuElement](ts-universal-attributes-menu.md#menuelement)弹出普通菜单。

```
1. @Entry
2. @Component
3. struct MenuExample {
4. build() {
5. Column() {
6. Text('click for Menu')
7. .bindMenu([
8. {
9. value: 'Menu1',
10. action: () => {
11. console.info('handle Menu1 select');
12. }
13. },
14. {
15. value: 'Menu2',
16. action: () => {
17. console.info('handle Menu2 select');
18. }
19. },
20. ])
21. }
22. .width('100%')
23. .margin({ top: 5 })
24. }
25. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/11mcZPFATiC4BxrpXw6zFA/zh-cn_image_0000002583479553.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000112Z&HW-CC-Expire=86400&HW-CC-Sign=5AD65744B95EBA9FDF9BB678F4185C977CDA5DD9A24DFE48461491CD4C498D0F)

### 示例2（弹出自定义菜单）

该示例为bindMenu通过配置CustomBuilder弹出自定义菜单。同时，从API version 18开始支持通过配置[ContextMenuOptions](ts-universal-attributes-menu.md#contextmenuoptions10)中的hapticFeedbackMode属性实现菜单弹出时的振动效果。

```
1. @Entry
2. @Component
3. struct MenuExample {
4. @State listData: number[] = [0, 0, 0];

6. @Builder MenuBuilder() {
7. Flex({ direction: FlexDirection.Column, justifyContent: FlexAlign.Center, alignItems: ItemAlign.Center }) {
8. ForEach(this.listData, (item:number, index) => {
9. Column() {
10. Row() {
11. // $r('app.media.icon')需要替换为开发者所需的图像资源文件。
12. Image($r("app.media.icon")).width(20).height(20).margin({ right: 5 })
13. Text(`Menu${index as number + 1}`).fontSize(20)
14. }
15. .width('100%')
16. .height(30)
17. .justifyContent(FlexAlign.Center)
18. .align(Alignment.Center)
19. .onClick(() => {
20. console.info(`Menu${index as number + 1} Clicked!`);
21. })

23. if (index != this.listData.length - 1) {
24. Divider().height(10).width('80%').color('#ccc')
25. }
26. }.padding(5).height(40)
27. })
28. }.width(100)
29. }

31. build() {
32. Column() {
33. Text('click for menu')
34. .fontSize(20)
35. .margin({ top: 20 })
36. .bindMenu(this.MenuBuilder, { hapticFeedbackMode: HapticFeedbackMode.ENABLED })
37. }
38. .height('100%')
39. .width('100%')
40. .backgroundColor('#f0f0f0')
41. }
42. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/20/v3/1c5ZXOcjR4udnFfN72UMpw/zh-cn_image_0000002552799904.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000112Z&HW-CC-Expire=86400&HW-CC-Sign=FA3ACCFC7D38A4331A7959124DC7D681FF024BA79D221284CC881A8650269A29)

### 示例3（长按弹出菜单）

该示例为bindContextMenu通过配置[responseType](ts-appendix-enums.md#responsetype8).LongPress弹出菜单。

```
1. @Entry
2. @Component
3. struct ContextMenuExample {
4. @Builder MenuBuilder() {
5. Flex({ direction: FlexDirection.Column, justifyContent: FlexAlign.Center, alignItems: ItemAlign.Center }) {
6. Text('Test menu item 1')
7. .fontSize(20)
8. .width(100)
9. .height(50)
10. .textAlign(TextAlign.Center)
11. Divider().height(10)
12. Text('Test menu item 2')
13. .fontSize(20)
14. .width(100)
15. .height(50)
16. .textAlign(TextAlign.Center)
17. }.width(100)
18. }

20. build() {
21. Column() {
22. Text('LongPress for menu')
23. }
24. .width('100%')
25. .margin({ top: 5 })
26. .bindContextMenu(this.MenuBuilder, ResponseType.LongPress)
27. }
28. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ae/v3/u4EUaiLTTouxwHdvw4t13g/zh-cn_image_0000002583439599.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000112Z&HW-CC-Expire=86400&HW-CC-Sign=493DFD63A0259384FF64869813166A60A380D064F27808AA48ED199CAC89F20A)

### 示例4（右键弹出指向型菜单）

该示例为bindContextMenu通过配置[responseType](ts-appendix-enums.md#responsetype8).RightClick和[ContextMenuOptions](ts-universal-attributes-menu.md#contextmenuoptions10)中的enableArrow属性弹出指向型菜单。同时，从API version 18开始支持通过配置[ContextMenuOptions](ts-universal-attributes-menu.md#contextmenuoptions10)中的hapticFeedbackMode属性实现菜单弹出时的振动效果。

```
1. @Entry
2. @Component
3. struct DirectiveMenuExample {
4. @Builder MenuBuilder() {
5. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
6. Text('Options')
7. Divider().strokeWidth(2).margin(5).color('#F0F0F0')
8. Text('Hide')
9. Divider().strokeWidth(2).margin(5).color('#F0F0F0')
10. Text('Exit')
11. }
12. .width(200)
13. }

15. build() {
16. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
17. Column() {
18. Text("DirectiveMenuExample")
19. .fontSize(20)
20. .width('100%')
21. .height("25%")
22. .backgroundColor('#F0F0F0')
23. .textAlign(TextAlign.Center)
24. .bindContextMenu(this.MenuBuilder, ResponseType.RightClick, {
25. enableArrow: true,
26. placement: Placement.Bottom,
27. hapticFeedbackMode: HapticFeedbackMode.ENABLED
28. })
29. }
30. }
31. .width('100%')
32. .height('100%')
33. }
34. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d9/v3/qnPtCTpiTuif4bIXUBD2og/zh-cn_image_0000002552959554.png?HW-CC-KV=V1&HW-CC-Date=20260428T000112Z&HW-CC-Expire=86400&HW-CC-Sign=BCEA0F9F42D9FD025990DFB79A46485E5A7C25336201B74F03FD2CC7ED2DD070)

### 示例5（长按弹出菜单的截图预览样式）

该示例为bindContextMenu通过配置[responseType](ts-appendix-enums.md#responsetype8).LongPress和[ContextMenuOptions](ts-universal-attributes-menu.md#contextmenuoptions10)中preview属性的[MenuPreviewMode](ts-universal-attributes-menu.md#menupreviewmode11)类型弹出菜单预览样式。

```
1. @Entry
2. @Component
3. struct Index {
4. // $r('app.media.icon')需要替换为开发者所需的图像资源文件。
5. private iconStr: ResourceStr = $r("app.media.icon");

7. @Builder
8. MyMenu() {
9. Menu() {
10. MenuItem({ startIcon: this.iconStr, content: "菜单选项" })
11. MenuItem({ startIcon: this.iconStr, content: "菜单选项" })
12. MenuItem({ startIcon: this.iconStr, content: "菜单选项" })
13. }
14. }

16. build() {
17. Column({ space: 50 }) {
18. Column() {
19. Column() {
20. Text('preview-image')
21. .width(200)
22. .height(100)
23. .textAlign(TextAlign.Center)
24. .margin(100)
25. .fontSize(30)
26. .bindContextMenu(this.MyMenu, ResponseType.LongPress,
27. { preview: MenuPreviewMode.IMAGE,
28. previewAnimationOptions: {scale: [0.8, 1.0]},
29. })
30. .backgroundColor("#ff3df2f5")
31. }
32. }.width('100%')
33. }
34. }
35. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/53/v3/qQRxa43FS0yt9iZHV8plTg/zh-cn_image_0000002583479555.png?HW-CC-KV=V1&HW-CC-Date=20260428T000112Z&HW-CC-Expire=86400&HW-CC-Sign=444244790C4E18418FCB679E0E4BEDE01FF07DCBF79DF59B07A8DAD44A16E64A)

### 示例6（长按弹出菜单的自定义预览样式）

该示例为bindContextMenu通过配置[responseType](ts-appendix-enums.md#responsetype8).LongPress和[ContextMenuOptions](ts-universal-attributes-menu.md#contextmenuoptions10)中preview属性的[CustomBuilder](ts-types.md#custombuilder8)类型弹出菜单自定义预览样式。

```
1. @Entry
2. @Component
3. struct Index {
4. // $r('app.media.icon')需要替换为开发者所需的图像资源文件。
5. private iconStr: ResourceStr = $r("app.media.icon");

7. @Builder
8. MyMenu() {
9. Menu() {
10. MenuItem({ startIcon: this.iconStr, content: "菜单选项" })
11. MenuItem({ startIcon: this.iconStr, content: "菜单选项" })
12. MenuItem({ startIcon: this.iconStr, content: "菜单选项" })
13. }
14. }

16. @Builder
17. MyPreview() {
18. Column() {
19. Image($r('app.media.icon'))
20. .width(200)
21. .height(200)
22. }
23. }

25. build() {
26. Column({ space: 50 }) {
27. Column() {
28. Column() {
29. Text('preview-builder')
30. .width(200)
31. .height(100)
32. .textAlign(TextAlign.Center)
33. .margin(100)
34. .fontSize(30)
35. .bindContextMenu(this.MyMenu, ResponseType.LongPress,
36. {
37. preview: this.MyPreview
38. })
39. }
40. }.width('100%')
41. }
42. }
43. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a5/v3/35V-9n5BSkGepzeZBw6ZeA/zh-cn_image_0000002552799906.png?HW-CC-KV=V1&HW-CC-Date=20260428T000112Z&HW-CC-Expire=86400&HW-CC-Sign=BE7DAE78EAE714AEEB4B53125618F5A0C32026319BA7BE569A6B7DB79187B385)

### 示例7（设置状态变量弹出菜单）

该示例为[bindContextMenu](ts-universal-attributes-menu.md#bindcontextmenu12)通过配置isShown弹出菜单预览样式。

```
1. @Entry
2. @Component
3. struct Index {
4. // $r('app.media.icon')需要替换为开发者所需的图像资源文件。
5. private iconStr: ResourceStr = $r("app.media.icon");
6. @State isShown: boolean = false;

8. @Builder
9. MyMenu() {
10. Menu() {
11. MenuItem({ startIcon: this.iconStr, content: "菜单选项" })
12. MenuItem({ startIcon: this.iconStr, content: "菜单选项" })
13. MenuItem({ startIcon: this.iconStr, content: "菜单选项" })
14. }
15. }

17. @Builder
18. MyPreview() {
19. Column() {
20. Image($r('app.media.icon'))
21. .width(200)
22. .height(200)
23. }
24. }

26. build() {
27. Column({ space: 50 }) {
28. Column() {
29. Column() {
30. Text('preview-builder')
31. .width(200)
32. .height(100)
33. .textAlign(TextAlign.Center)
34. .margin(100)
35. .fontSize(30)
36. .bindContextMenu(this.isShown, this.MyMenu,
37. {
38. preview: this.MyPreview,
39. aboutToDisappear: ()=>{
40. this.isShown = false;
41. }
42. })
43. Button('click')
44. .onClick(()=>{
45. this.isShown = true;
46. })
47. }
48. }.width('100%')
49. }
50. }
51. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7c/v3/ZpkWl8lMSZWwLZ0av7gxlA/zh-cn_image_0000002552799906.png?HW-CC-KV=V1&HW-CC-Date=20260428T000112Z&HW-CC-Expire=86400&HW-CC-Sign=5A8127B35E116A04E27FCD94FEA398C765656881756B707977295E0CF94E9841)

### 示例8（设置菜单和预览的动效）

该示例为bindContextMenu通过配置[ContextMenuOptions](ts-universal-attributes-menu.md#contextmenuoptions10)中的transition属性，实现自定义菜单以及菜单预览时的显示和退出动效。

```
1. @Entry
2. @Component
3. struct MenuExample {
4. @Builder
5. MenuBuilder() {
6. Flex({ direction: FlexDirection.Column, justifyContent: FlexAlign.Center, alignItems: ItemAlign.Center }) {
7. Text('Menu item 1')
8. .fontSize(12)
9. .width(200)
10. .height(30)
11. .textAlign(TextAlign.Center)
12. Divider().height(10)
13. Text('Menu item 2')
14. .fontSize(12)
15. .width(100)
16. .height(30)
17. .textAlign(TextAlign.Center)
18. }.width(100)
19. }

21. @Builder
22. MyPreview() {
23. Column() {
24. // $r('app.media.startIcon')需要替换为开发者所需的图像资源文件。
25. Image($r('app.media.startIcon'))
26. .width(50)
27. .height(50)
28. }
29. }

31. build() {
32. Column() {
33. Button('LongPress bindContextMenu')
34. .margin({ top: 15 })
35. .bindContextMenu(
36. this.MenuBuilder,
37. ResponseType.LongPress, {
38. transition: TransitionEffect.OPACITY.animation({ duration: 4000, curve: Curve.Ease }).combine(
39. TransitionEffect.rotate({ z: 1, angle: 180 })),
40. preview: this.MyPreview,
41. previewAnimationOptions: {
42. scale: [0.8, 1.0],
43. transition: TransitionEffect.OPACITY.animation({ duration: 4000, curve: Curve.Ease }).combine(
44. TransitionEffect.rotate({ z: 1, angle: 180 }))
45. }
46. })
47. }
48. .width('100%')
49. .margin({ top: 5 })
50. }
51. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e8/v3/J1jL7mSnRCyutBlu_Zx6fw/zh-cn_image_0000002583439601.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000112Z&HW-CC-Expire=86400&HW-CC-Sign=14C74BA07D677234EB66374740778F05C2BFF8C3C74974E46E8756B1DEC8A3CA)

### 示例9（设置symbol类型图标）

该示例为bindMenu通过配置[MenuElement](ts-universal-attributes-menu.md#menuelement)的symbolIcon弹出菜单。

```
1. import { SymbolGlyphModifier } from '@kit.ArkUI';
2. @Entry
3. @Component
4. struct MenuExample {
5. @State symbolIconModifier1: SymbolGlyphModifier = new SymbolGlyphModifier($r('sys.symbol.ohos_photo')).fontSize('24vp');
6. @State symbolIconModifier2: SymbolGlyphModifier = new SymbolGlyphModifier($r('sys.symbol.ohos_photo')).fontSize('24vp');
7. build() {
8. Column() {
9. Text('click for Menu')
10. }
11. .width('100%')
12. .margin({ top: 5 })
13. .bindMenu([
14. {
15. value: 'Menu1',
16. symbolIcon:this.symbolIconModifier1,
17. action: () => {
18. console.info('handle Menu1 select');
19. }
20. },
21. {
22. value: 'Menu2',
23. symbolIcon:this.symbolIconModifier2,
24. action: () => {
25. console.info('handle Menu2 select');
26. }
27. },
28. ])
29. }
30. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b5/v3/wCkzWYJ8QiWvs1Zv1nn07Q/zh-cn_image_0000002552959556.png?HW-CC-KV=V1&HW-CC-Date=20260428T000112Z&HW-CC-Expire=86400&HW-CC-Sign=2CEFC9611680855D620AFA43544EC3D064553FCFC9938D705460EDD75E358FD6)

### 示例10（设置一镜到底动效）

该示例为bindContextMenu通过配置[ContextMenuOptions](ts-universal-attributes-menu.md#contextmenuoptions10)中previewAnimationOptions属性的hoverScale，实现组件截图到自定义预览图的一镜到底过渡动效。

```
1. @Entry
2. @Component
3. struct Index {
4. // $r('app.media.xxx')需要替换为开发者所需的图像资源文件。
5. private iconStr: ResourceStr = $r("app.media.app_icon");

7. @Builder
8. MyMenu() {
9. Menu() {
10. MenuItem({ startIcon: this.iconStr, content: "菜单选项" })
11. MenuItem({ startIcon: this.iconStr, content: "菜单选项" })
12. MenuItem({ startIcon: this.iconStr, content: "菜单选项" })
13. }
14. }

16. @Builder
17. MyPreview() {
18. Column() {
19. Image($r('app.media.example'))
20. .width(200)
21. .height(200)
22. }
23. }

25. build() {
26. Column({ space: 50 }) {
27. Column() {
28. Column() {
29. Image($r('app.media.example'))
30. .width(100)
31. .height(100)
32. .margin(100)
33. .bindContextMenu(this.MyMenu, ResponseType.LongPress,
34. {
35. preview: this.MyPreview,
36. previewAnimationOptions: {
37. hoverScale: [1.0, 0.95]
38. }
39. })
40. }
41. }.width('100%')
42. }
43. }
44. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bc/v3/gkdFhMgZRZSRUNWQKZVAMw/zh-cn_image_0000002583479557.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000112Z&HW-CC-Expire=86400&HW-CC-Sign=54C33FC120CBFA2AE037EB6AE82F09703E0F81A0175508522C01D1643382F493)

### 示例11（自定义背景模糊效果参数）

该示例为bindMenu通过配置[ContextMenuOptions](ts-universal-attributes-menu.md#contextmenuoptions10)中的backgroundBlurStyleOptions属性，实现了自定义菜单背景模糊效果。

从API version 18开始，在ContextMenuOptions中新增了backgroundBlurStyleOptions属性。

```
1. @Entry
2. @Component
3. struct MenuExample {
4. build() {
5. Stack() {
6. // $r('app.media.bg')需要替换为开发者所需的图像资源文件。
7. Image($r('app.media.bg'))
8. Column() {
9. Text('click for Menu')
10. .bindMenu([
11. {
12. value: 'Menu1',
13. action: () => {
14. console.info('handle Menu1 select')
15. }
16. },
17. {
18. value: 'Menu2',
19. action: () => {
20. console.info('handle Menu2 select')
21. }
22. },
23. ],
24. {
25. backgroundBlurStyle: BlurStyle.BACKGROUND_THIN,
26. backgroundBlurStyleOptions: {
27. colorMode: ThemeColorMode.LIGHT,
28. blurOptions: { grayscale: [20, 20] },
29. policy: BlurStyleActivePolicy.ALWAYS_ACTIVE,
30. adaptiveColor: AdaptiveColor.AVERAGE,
31. scale: 1
32. },
33. }
34. )
35. }
36. .width('100%')
37. .margin({ top: 5 })
38. }
39. }
40. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/29/v3/gykvWE98T8ydwU0yAuvrNg/zh-cn_image_0000002552799908.png?HW-CC-KV=V1&HW-CC-Date=20260428T000112Z&HW-CC-Expire=86400&HW-CC-Sign=37B45894E802B85045FB2524180271A2A3327EC1CDC4173DB0BD21A61511CD08)

### 示例12（自定义背景效果参数）

该示例为bindMenu通过配置[ContextMenuOptions](ts-universal-attributes-menu.md#contextmenuoptions10)中的backgroundEffect属性，实现了自定义菜单背景效果。

从API version 18开始，在ContextMenuOptions中新增了backgroundEffect属性。

```
1. @Entry
2. @Component
3. struct MenuExample {
4. build() {
5. Stack() {
6. // $r('app.media.bg')需要替换为开发者所需的图像资源文件。
7. Image($r('app.media.bg'))
8. Column() {
9. Text('click for Menu')
10. .bindMenu([
11. {
12. value: 'Menu1',
13. action: () => {
14. console.info('handle Menu1 select');
15. }
16. },
17. {
18. value: 'Menu2',
19. action: () => {
20. console.info('handle Menu2 select');
21. }
22. },
23. ],
24. {
25. backgroundBlurStyle: BlurStyle.BACKGROUND_THIN,
26. backgroundEffect: {
27. radius: 60,
28. saturation: 10,
29. brightness: 1,
30. color: '#661A1A1A',
31. adaptiveColor: AdaptiveColor.AVERAGE,
32. blurOptions:{grayscale:[20,20]}
33. }
34. }
35. )
36. }
37. .width('100%')
38. .margin({ top: 5 })
39. }
40. }
41. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cc/v3/US9YzuHjTU6U2QAHs6txmQ/zh-cn_image_0000002583439603.png?HW-CC-KV=V1&HW-CC-Date=20260428T000112Z&HW-CC-Expire=86400&HW-CC-Sign=C14BC79C0E19E7A2A6DAA4CB43CEC70385B89BE42D8D75215132828CDBDCF972)

### 示例13（设置一镜到底动效支持抬手打断）

该示例通过为bindContextMenu配置[ContextMenuOptions](ts-universal-attributes-menu.md#contextmenuoptions10)中的previewAnimationOptions属性实现了一镜到底过渡动效的同时，再配置hoverScaleInterruption控制是否允许长按抬手取消菜单弹出。

从API version 20开始，在previewAnimationOptions的类型[ContextMenuAnimationOptions](ts-universal-attributes-menu.md#contextmenuanimationoptions11)中新增了hoverScaleInterruption属性。

```
1. @Entry
2. @Component
3. struct Index {
4. // $r('app.media.xxx')需要替换为开发者所需的图像资源文件。
5. private iconStr: ResourceStr = $r("app.media.app_icon");

7. @Builder
8. MyMenu() {
9. Menu() {
10. MenuItem({ startIcon: this.iconStr, content: "菜单选项" })
11. MenuItem({ startIcon: this.iconStr, content: "菜单选项" })
12. MenuItem({ startIcon: this.iconStr, content: "菜单选项" })
13. }
14. }

16. @Builder
17. MyPreview() {
18. Column() {
19. Image($r('app.media.example'))
20. .width(300)
21. .height(200)
22. }
23. }

25. build() {
26. Column({ space: 50 }) {
27. Column() {
28. Column() {
29. Image($r('app.media.example'))
30. .width(100)
31. .height(100)
32. .margin(100)
33. .bindContextMenu(this.MyMenu, ResponseType.LongPress,
34. {
35. preview: this.MyPreview,
36. previewAnimationOptions: {
37. hoverScale: [1.0, 0.8],
38. hoverScaleInterruption: true
39. }
40. })
41. .onClick(() => {
42. console.info('trigger onClick')
43. })
44. }
45. }.width('100%')
46. }
47. }
48. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8e/v3/fNe62N28SxKEanIm5YRkKQ/zh-cn_image_0000002552959558.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000112Z&HW-CC-Expire=86400&HW-CC-Sign=648DE18842743C20EEB483F272B45791049705A714B0E539A26F29682DC03DD0)

### 示例14（设置预览图边框圆角半径）

该示例通过bindContextMenu配置[responseType](ts-appendix-enums.md#responsetype8).LongPress来实现功能。同时，在[ContextMenuOptions](ts-universal-attributes-menu.md#contextmenuoptions10)中配置preview属性的[MenuPreviewMode](ts-universal-attributes-menu.md#menupreviewmode11)类型来设置菜单预览样式。最后，通过设置previewBorderRadius来实现预览图边框的圆角半径。

从API version 19开始，在[ContextMenuOptions](ts-universal-attributes-menu.md#contextmenuoptions10)中新增了previewBorderRadius属性。

```
1. @Entry
2. @Component
3. struct Index {
4. // $r('app.media.startIcon')需要替换为开发者所需的图像资源文件。
5. private iconStr: ResourceStr = $r("app.media.startIcon");

7. @Builder
8. MyMenu() {
9. Menu() {
10. MenuItem({ startIcon: this.iconStr, content: "菜单选项" })
11. MenuItem({ startIcon: this.iconStr, content: "菜单选项" })
12. MenuItem({ startIcon: this.iconStr, content: "菜单选项" })
13. }
14. }

16. build() {
17. Column({ space: 50 }) {
18. Column() {
19. Column() {
20. Text('preview-image')
21. .width(200)
22. .height(100)
23. .textAlign(TextAlign.Center)
24. .margin(100)
25. .fontSize(30)
26. .bindContextMenu(this.MyMenu, ResponseType.LongPress,
27. {
28. preview: MenuPreviewMode.IMAGE,
29. previewBorderRadius: 50
30. })
31. .backgroundColor("#ff7fcdff")
32. }
33. }.width('100%')
34. }
35. }
36. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ea/v3/vcxb9_tFTD-b-7_7zYZNPQ/zh-cn_image_0000002583479559.jpg?HW-CC-KV=V1&HW-CC-Date=20260428T000112Z&HW-CC-Expire=86400&HW-CC-Sign=377FCFA323CF6B08A7E44B7C04B8B9E1020DA131DAFF20D77CF4A33B900F80C0)

### 示例15（bindMenu配置生命周期回调）

该示例为bindMenu配置生命周期回调。

从API version 20开始，在[ContextMenuOptions](ts-universal-attributes-menu.md#contextmenuoptions10)中新增了onWillAppear、onDidAppear、onWillDisappear和onDidDisappear属性。

```
1. @Entry
2. @Component
3. struct Index {
4. // $r('app.media.startIcon')需要替换为开发者所需的图像资源文件。
5. private iconStr: ResourceStr = $r("app.media.startIcon");
6. @State isShown: boolean = false;
7. @State textColor: Color = Color.Black;
8. @State blueColor: Color = Color.Blue;
9. @State onWillAppear: boolean = false;
10. @State onDidAppear: boolean = false;
11. @State onWillDisappear: boolean = false;
12. @State onDidDisappear: boolean = false;

14. @Builder
15. MyMenu() {
16. Menu() {
17. MenuItem({ startIcon: this.iconStr, content: "菜单选项" })
18. MenuItem({ startIcon: this.iconStr, content: "菜单选项" })
19. MenuItem({ startIcon: this.iconStr, content: "菜单选项" })
20. }
21. }

23. build() {
24. Column() {
25. Column({ space: 30 }) {
26. Text('onWillAppear').fontColor(this.onWillAppear ? this.blueColor : this.textColor)
27. Text('onDidAppear').fontColor(this.onDidAppear ? this.blueColor : this.textColor)
28. Text('onWillDisappear').fontColor(this.onWillDisappear ? this.blueColor : this.textColor)
29. Text('onDidDisappear').fontColor(this.onDidDisappear ? this.blueColor : this.textColor)
30. Button('click')
31. .onClick(() => {
32. this.isShown = true;
33. })
34. .width(100)
35. .height(50)
36. Text('callback')
37. .width(200)
38. .height(100)
39. .textAlign(TextAlign.Center)
40. .fontSize(20)
41. .fontColor(this.textColor)
42. .bindMenu(this.isShown, this.MyMenu,
43. {
44. onWillAppear: () => {
45. console.info("menu cycle life onWillAppear");
46. this.onWillAppear = true;
47. },
48. onDidAppear: () => {
49. console.info("menu cycle life onDidAppear");
50. this.onDidAppear = true;
51. },
52. onWillDisappear: () => {
53. this.isShown = false;
54. console.info("menu cycle life onWillDisappear");
55. this.onWillDisappear = true;
56. },
57. onDidDisappear: () => {
58. console.info("menu cycle life onDidDisappear");
59. this.onDidDisappear = true;
60. }
61. })
62. }
63. }.width('100%')
64. }
65. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/88/v3/wQfGSHIDSoO6xqLQUZCjQA/zh-cn_image_0000002552799910.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000112Z&HW-CC-Expire=86400&HW-CC-Sign=7CC07226DE2B2AA03057A3E0E03C30215262E81F1DA431EAB6EF3B7E5DCE7FCC)

### 示例16（设置菜单蒙层）

该示例为bindMenu通过配置mask属性设置菜单蒙层。

从API version 20开始，在[ContextMenuOptions](ts-universal-attributes-menu.md#contextmenuoptions10)中新增了mask属性。

```
1. import { SymbolGlyphModifier } from '@kit.ArkUI';

3. @Entry
4. @Component
5. struct Index {
6. @State startIconModifier: SymbolGlyphModifier = new SymbolGlyphModifier($r('sys.symbol.ohos_star'))
7. @State isShow: boolean = false;

9. @Builder
10. MyMenu() {
11. Menu() {
12. MenuItem({
13. symbolStartIcon: this.startIconModifier,
14. content: "新建文件夹",
15. })
16. MenuItem({
17. symbolStartIcon: this.startIconModifier,
18. content: "排序方式",
19. })
20. MenuItem({
21. symbolStartIcon: this.startIconModifier,
22. content: "查看方式",
23. })
24. }
25. }

27. build() {
28. Button('bindMenu')
29. .position({ top: 80, left: 80 })
30. .onClick(() => {
31. this.isShow = !this.isShow;
32. })
33. .bindMenu(this.isShow, this.MyMenu, {
34. mask: { color: 'rgba(23,169,141,0.5)', backgroundBlurStyle: BlurStyle.Thin }
35. })
36. }
37. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/JZCfe_YUTt6oMhRmGL0kNw/zh-cn_image_0000002583439605.jpg?HW-CC-KV=V1&HW-CC-Date=20260428T000112Z&HW-CC-Expire=86400&HW-CC-Sign=63E0727B426C9310A4A38C65F3291E995D3682E9B980B0AA360E7787D37B2645)

### 示例17（bindMenu设置下拉菜单外描边样式）

该示例为bindMenu通过配置outlineWidth和outlineColor属性设置下拉菜单外描边样式。

从API version 20开始，在[ContextMenuOptions](ts-universal-attributes-menu.md#contextmenuoptions10)中新增了outlineWidth和outlineColor属性。

```
1. @Entry
2. @Component
3. struct Index {
4. @Builder
5. MyMenu() {
6. Menu() {
7. MenuItem({ content: "菜单选项" })
8. MenuItem({ content: "菜单选项" })
9. MenuItem({ content: "菜单选项" })
10. }.width(200)
11. }

13. build() {
14. Column({ space: 50 }) {
15. Column() {
16. Column() {
17. Text('click for Menu')
18. .width(200)
19. .height(100)
20. .textAlign(TextAlign.Center)
21. .margin(100)
22. .fontSize(30)
23. .bindMenu(this.MyMenu,
24. {
25. outlineWidth: '5vp',
26. outlineColor: Color.Blue
27. })
28. }
29. }
30. .width('100%')
31. .height('100%')
32. .backgroundColor('#F0F2F5')
33. }
34. }
35. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/35/v3/8iXStAWzTfqtZ4rkXT-0OA/zh-cn_image_0000002552959560.png?HW-CC-KV=V1&HW-CC-Date=20260428T000112Z&HW-CC-Expire=86400&HW-CC-Sign=AC8B821FE64F7EEA1C4054C61AB0194FC87F5324DA341E3573A22C6718E3D502)

### 示例18（bindMenu传入带参数的CustomBuilder）

该示例通过在bindMenu中传入带参数的CustomBuilder来配置菜单的具体属性。

```
1. @Entry
2. @Component
3. struct Index {
4. @State menuItemList: string[] = ['新建', '历史', '书签', '设置']

6. @Builder
7. MenuBuilder(itemList: string[]) {
8. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center }) {
9. ForEach(itemList, (item: string, index) => {
10. Row() {
11. Text(item)
12. .width('100%')
13. .height(32)
14. .fontWeight(400)
15. .fontSize(14)
16. .fontColor(Color.Black)
17. .textAlign(TextAlign.Center)
18. }
19. .onClick(() => {
20. console.info('handle' + item + 'Clicked!')
21. })
22. if (index != itemList.length - 1) {
23. Divider().height(10).width('80%').color('#ccc')
24. }
25. })
26. }
27. .width(100)
28. }

30. build() {
31. Column() {
32. Text('click for Menu')
33. .bindMenu(this.MenuBuilder(this.menuItemList))
34. }
35. .height('100%')
36. .width('100%')
37. .backgroundColor('#f0f0f0')
38. }
39. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/90/v3/oJEDnP01Ry6dewgEN62rag/zh-cn_image_0000002583479561.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000112Z&HW-CC-Expire=86400&HW-CC-Sign=FFEA5EC7DBDF0F1D29FAE276463C7AD7B6B340E060CD97BD83D61344CCC3C3B9)

### 示例19（根据触发方式弹出不同内容的菜单）

该示例通过在[bindContextMenuWithResponse](ts-universal-attributes-menu.md#bindcontextmenuwithresponse23)中传入CustomBuilderT<ResponseType>给目标组件绑定菜单，组件会在UI函数中返回弹出菜单的触发方式，开发者可根据返回的触发方式实现差异化显示。

从API version 23开始，新增了bindContextMenuWithResponse的接口。

```
1. @Entry
2. @Component
3. struct Index {
4. @State longPress: string = 'LONG_PRESS';
5. @State rightClick: string = 'RIGHT_CLICK';

7. @Builder
8. MenuBuilderWithParam(type: ResponseType) {
9. Flex({ direction: FlexDirection.Column, justifyContent: FlexAlign.Center, alignItems: ItemAlign.Center }) {
10. Text('Current ResponseType = ' + (type === 0 ? 'RIGHT_CLICK' : 'LONG_PRESS'))
11. Divider().height(10)
12. if (type === ResponseType.LongPress) {
13. Text('Item: ' + this.longPress)
14. .fontSize(20)
15. .width(200)
16. .height(20)
17. .textAlign(TextAlign.Center)
18. }
19. if (type === ResponseType.RightClick) {
20. Text('Item: ' + this.rightClick)
21. .fontSize(20)
22. .width(200)
23. .height(20)
24. .textAlign(TextAlign.Center)
25. }
26. }
27. }

29. build() {
30. Stack() {
31. Button('BindContextMenu长按和右键点击触发菜单')
32. .bindContextMenuWithResponse(this.MenuBuilderWithParam, {
33. enableArrow: true,
34. })
35. }
36. .height('100%')
37. .width('100%')
38. .backgroundColor('#f0f0f0')
39. }
40. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3d/v3/0D4p1qPORZWDuD27EbjZYQ/zh-cn_image_0000002552799912.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000112Z&HW-CC-Expire=86400&HW-CC-Sign=B279E3E26F5FEB710F2ECE49BCB9580627B57A8889C1DE78A39EAFBCAAB25D8E)

### 示例20（设置菜单避让软键盘）

该示例通过在bindMenu中配置keyboardAvoidMode设置菜单避让软键盘，通过minKeyboardAvoidDistance设置菜单避让软键盘的最小距离。

从API version 23开始，[ContextMenuOptions](ts-universal-attributes-menu.md#contextmenuoptions10)中新增keyboardAvoidMode、minKeyboardAvoidDistance属性。

```
1. import { inputMethod } from '@kit.IMEKit';
2. import { LengthMetrics } from '@kit.ArkUI';

4. @Entry
5. @Component
6. struct Index {
7. private inputController: inputMethod.InputMethodController = inputMethod.getController();

9. @Builder
10. MyMenu() {
11. Menu() {
12. MenuItem({ content: 'MenuItemContent' })
13. MenuItem({ content: 'MenuItemContent' })
14. MenuItem({ content: 'MenuItemContent' })
15. MenuItem({ content: 'MenuItemContent' })
16. MenuItem({ content: 'MenuItemContent' })
17. }
18. }

20. build() {
21. RelativeContainer() {
22. Button('Click Show Menu')
23. .alignRules({
24. center: { anchor: '__container__', align: VerticalAlign.Center },
25. middle: { anchor: '__container__', align: HorizontalAlign.Center },
26. })
27. .bindMenu(this.MyMenu, {
28. keyboardAvoidMode: MenuKeyboardAvoidMode.TRANSLATE_AND_RESIZE,
29. minKeyboardAvoidDistance: LengthMetrics.vp(20)
30. })
31. .onClick(() => {
32. setTimeout(() => {
33. this.attachAndListener()
34. }, 2000)
35. })
36. }
37. .height('100%')
38. .width('100%')

40. }

42. async attachAndListener() {
43. focusControl.requestFocus('Index')
44. try {
45. await this.inputController.attach(true, {
46. inputAttribute: {
47. textInputType: inputMethod.TextInputType.TEXT,
48. enterKeyType: inputMethod.EnterKeyType.SEARCH
49. }
50. })
51. } catch (err) {
52. console.error('Fail to attach')
53. }
54. }
55. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f4/v3/49WGClcsQwaHQGLXLGHL_w/zh-cn_image_0000002583439607.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000112Z&HW-CC-Expire=86400&HW-CC-Sign=EB12F97A6C05313D263922B468643C394202A3AC1828C5175BF36096C4817C7A)

### 示例21（设置菜单相对于绑定组件左上角的弹出位置）

该示例通过设置[ContextMenuOptions](ts-universal-attributes-menu.md#contextmenuoptions10)中的anchorPosition属性，实现了菜单相对于绑定组件左上角弹出的效果。

从API version 20开始，在ContextMenuOptions中新增了anchorPosition属性。

```
1. @Entry
2. @Component
3. struct Index {
4. // $r('app.media.startIcon')需要替换为开发者所需的图像资源文件。
5. private iconStr: ResourceStr = $r('app.media.startIcon');
6. @State isShown: boolean = false;

8. @Builder
9. MyMenu() {
10. Menu() {
11. MenuItem({ startIcon: this.iconStr, content: '菜单选项' })
12. MenuItem({ startIcon: this.iconStr, content: '菜单选项' })
13. MenuItem({ startIcon: this.iconStr, content: '菜单选项' })
14. }
15. }

17. @State menuAnchorPositionIndex: number = 0;
18. private menuAnchorPositionArray: Array<Position> = new Array<Position>(
19. { x: 0, y: 0 },
20. { x: 150, y: 0 },
21. { x: 0, y: 150 },
22. { x: 150, y: 150 },
23. );

25. build() {
26. Column({ space: 50 }) {
27. Column() {
28. Column() {
29. Text('Test Menu AnchorPosition')
30. .width(500)
31. .height(100)
32. .textAlign(TextAlign.Center)
33. .margin(100)
34. .fontSize(30)
35. .bindContextMenu(this.isShown, this.MyMenu,
36. {
37. anchorPosition: this.menuAnchorPositionArray[this.menuAnchorPositionIndex],
38. aboutToDisappear: () => {
39. this.isShown = false;
40. }
41. })
42. Button('click')
43. .margin(5)
44. .onClick(() => {
45. this.isShown = true;
46. })

48. Button('AnchorPosition change')
49. .margin(5)
50. .onClick(() => {
51. this.menuAnchorPositionIndex++;
52. if (this.menuAnchorPositionIndex >= this.menuAnchorPositionArray.length) {
53. this.menuAnchorPositionIndex = 0;
54. }
55. })
56. Text('Current x: ' + this.menuAnchorPositionArray[this.menuAnchorPositionIndex]?.x +
57. ' , y: ' + this.menuAnchorPositionArray[this.menuAnchorPositionIndex]?.y)
58. }
59. }.width('100%')
60. }
61. }
62. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c7/v3/mHZWkEAlSc253YmLi09nKA/zh-cn_image_0000002552959562.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000112Z&HW-CC-Expire=86400&HW-CC-Sign=A93BC0CAE7F5B294E5F9B0A1638188620BB73E5D448C3E7C2CC4B31658AE83DF)
