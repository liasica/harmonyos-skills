---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-dialog
title: 弹出框 (Dialog)
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 弹窗 > 弹出框 (Dialog)
category: harmonyos-references
scraped_at: 2026-09-02T15:01:07+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:fc5006435c0a83a2fb65f4a3e21dabf69f0ed75ec42e0d8096e2a274de921eec
---

弹出框是一种模态窗口，用于临时展示用户需关注的信息或待处理的操作，同时保持当前上下文环境。用户必须完成交互才能退出该模式。

**说明** 

* 该组件从API version 10开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。
* 该组件仅可在Stage模型下使用。
* 如果Dialog设置[通用属性](ts-component-general-attributes.md)和[通用事件](ts-component-general-events.md)，编译工具链会额外生成节点\_\_Common\_\_，并将通用属性或通用事件挂载在\_\_Common\_\_上，而不是直接应用到Dialog本身。这可能导致开发者设置的通用属性或通用事件不生效或不符合预期，因此，不建议Dialog设置通用属性和通用事件。

## 导入模块

```ts
import { TipsDialog, SelectDialog, ConfirmDialog, AlertDialog, LoadingDialog, CustomContentDialog } from '@kit.ArkUI';
```

## 子组件

无

## TipsDialog

TipsDialog({controller: CustomDialogController, imageRes: ResourceStr | PixelMap, imageSize?: SizeOptions, title?: ResourceStr, content?: ResourceStr, checkTips?: ResourceStr, isChecked?: boolean, checkAction?: (isChecked: boolean) => void, onCheckedChange?: Callback<boolean>, primaryButton?: ButtonOptions, secondaryButton?: ButtonOptions, theme?: Theme | CustomTheme, themeColorMode?: ThemeColorMode})

提示弹出框，用于提醒用户关注特定事项或进行确认操作。

**装饰器类型：**@CustomDialog

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 必填 | 装饰器类型 | 说明 |
| --- | --- | --- | --- | --- |
| controller | [CustomDialogController](ts-methods-custom-dialog-box.md#customdialogcontroller) | 是 | - | 提示弹出框控制器，用于控制弹出框的显示和隐藏。  **说明：** 未使用@Require装饰，构造时不强制校验参数。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| imageRes | [ResourceStr](ts-types.md#resourcestr) | [PixelMap](arkts-apis-image-pixelmap.md) | 是 | - | 展示的图片。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| imageSize | [SizeOptions](ts-types.md#sizeoptions) | 否 | - | 自定义图片尺寸。  默认值：64\*64vp  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| title | [ResourceStr](ts-types.md#resourcestr) | 否 | - | 提示弹出框标题。  默认不设置或设置为undefined，弹出框标题不显示。  **说明：** 标题超过两行会显示“...”。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| content | [ResourceStr](ts-types.md#resourcestr) | 否 | - | 提示弹出框内容。  默认不设置或设置为undefined，弹出框内容不显示。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| checkTips | [ResourceStr](ts-types.md#resourcestr) | 否 | - | checkbox的提示内容。  默认不设置或设置为undefined，提示内容不显示。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| isChecked | boolean | 否 | @Prop | isChecked为true时，表示checkbox已选中，isChecked为false时，表示未选中。  默认值：false  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| checkAction12+ | (isChecked: boolean) => void | 否 | - | checkbox的选中状态改变事件。isChecked为true时，表示checkbox已选中，isChecked为false时，表示checkbox未选中。  **说明：** 推荐使用onCheckedChange12+。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| onCheckedChange12+ | [Callback](ts-types.md#callback12)<boolean> | 否 | - | checkbox的选中状态改变事件回调。回调参数类型为boolean，true表示checkbox已选中，false表示checkbox未选中。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| primaryButton | [ButtonOptions](ohos-arkui-advanced-dialog.md#buttonoptions) | 否 | - | 提示弹出框左侧按钮。  默认不设置或设置为undefined，左侧按钮不显示。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| secondaryButton | [ButtonOptions](ohos-arkui-advanced-dialog.md#buttonoptions) | 否 | - | 提示弹出框右侧按钮。  默认不设置或设置为undefined，右侧按钮不显示。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| theme12+ | [Theme](js-apis-arkui-theme.md#theme) | [CustomTheme](js-apis-arkui-theme.md#customtheme) | 否 | - | 主题信息，可以是CustomTheme或从onWillApplyTheme中获取的Theme实例。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| themeColorMode12+ | [ThemeColorMode](ts-universal-attributes-foreground-blur-style.md#themecolormode枚举说明) | 否 | - | 自定义弹出框深浅色模式。  默认值：ThemeColorMode.SYSTEM  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |

## SelectDialog

SelectDialog({controller: CustomDialogController, title: ResourceStr, content?: ResourceStr, selectedIndex?: number, confirm?: ButtonOptions, radioContent: Array<SheetInfo>, theme?: Theme | CustomTheme, themeColorMode?: ThemeColorMode})

选择类弹出框，弹框中以列表或网格的形式提供可选的内容。

**装饰器类型：**@CustomDialog

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| controller | [CustomDialogController](ts-methods-custom-dialog-box.md#customdialogcontroller) | 是 | 选择弹出框控制器，用于控制弹出框的显示和隐藏。  **说明：** 未使用@Require装饰，构造时不强制校验参数。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| title | [ResourceStr](ts-types.md#resourcestr) | 是 | 选择弹出框标题。  **说明：** 标题超过两行会显示“...”。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| content | [ResourceStr](ts-types.md#resourcestr) | 否 | 选择弹出框内容。  默认不设置或设置为undefined，弹出框内容不显示。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| selectedIndex | number | 否 | 选择弹出框的选中项。  取值范围：大于等于-1的整数。  默认值：-1，没有选中项。若设置数值小于-1，按没有选中项处理。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| confirm | [ButtonOptions](ohos-arkui-advanced-dialog.md#buttonoptions) | 否 | 选择弹出框底部按钮。  默认不设置或设置为undefined，底部按钮不显示。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| radioContent | Array<[SheetInfo](ts-methods-action-sheet.md#sheetinfo对象说明)> | 是 | 选择弹出框的子项内容列表，每个选择项支持设置文本和选中的回调事件。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| theme12+ | [Theme](js-apis-arkui-theme.md#theme) | [CustomTheme](js-apis-arkui-theme.md#customtheme) | 否 | 主题信息，可以是CustomTheme或从onWillApplyTheme中获取的Theme实例。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| themeColorMode12+ | [ThemeColorMode](ts-universal-attributes-foreground-blur-style.md#themecolormode枚举说明) | 否 | 自定义弹出框深浅色模式。  默认值：ThemeColorMode.SYSTEM  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |

## ConfirmDialog

ConfirmDialog({controller: CustomDialogController, title: ResourceStr, content?: ResourceStr, checkTips?: ResourceStr, isChecked?: boolean, onCheckedChange?: Callback<boolean>, primaryButton?: ButtonOptions, secondaryButton?: ButtonOptions, theme?: Theme | CustomTheme, themeColorMode?: ThemeColorMode})

信息确认类弹出框，用于在操作未正确执行（如网络错误、电池电量过低），或未正确操作时（如指纹录入）反馈错误或提示信息。

**装饰器类型：**@CustomDialog

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 必填 | 装饰器类型 | 说明 |
| --- | --- | --- | --- | --- |
| controller | [CustomDialogController](ts-methods-custom-dialog-box.md#customdialogcontroller) | 是 | - | 确认弹出框控制器，用于控制弹出框的显示和隐藏。  **说明：** 未使用@Require装饰，构造时不强制校验参数。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| title | [ResourceStr](ts-types.md#resourcestr) | 是 | - | 确认弹出框标题。  **说明：** 标题超过两行会显示“...”。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| content | [ResourceStr](ts-types.md#resourcestr) | 否 | - | 确认弹出框内容。  默认不设置或设置为undefined，确认弹出框内容不显示。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| checkTips | [ResourceStr](ts-types.md#resourcestr) | 否 | - | checkbox的提示内容。  默认不设置或设置为undefined，checkbox的提示内容不显示。  **说明：** 当提示内容不设置时，checkbox也会显示。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| isChecked | boolean | 否 | @Prop | isChecked为true时，表示checkbox已选中，isChecked为false时，表示未选中。  默认值：false  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| onCheckedChange12+ | [Callback](ts-types.md#callback12)<boolean> | 否 | - | checkbox的选中状态改变事件回调。回调参数类型为boolean，true表示checkbox已选中，false表示checkbox未选中。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| primaryButton | [ButtonOptions](ohos-arkui-advanced-dialog.md#buttonoptions) | 否 | - | 确认弹出框左侧按钮。  默认不设置或设置为undefined，确认弹出框左侧按钮不显示。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| secondaryButton | [ButtonOptions](ohos-arkui-advanced-dialog.md#buttonoptions) | 否 | - | 确认弹出框右侧按钮。  默认不设置或设置为undefined，确认弹出框右侧按钮不显示。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| theme12+ | [Theme](js-apis-arkui-theme.md#theme) | [CustomTheme](js-apis-arkui-theme.md#customtheme) | 否 | - | 主题信息，可以是CustomTheme或从onWillApplyTheme中获取的Theme实例。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| themeColorMode12+ | [ThemeColorMode](ts-universal-attributes-foreground-blur-style.md#themecolormode枚举说明) | 否 | - | 自定义弹出框深浅色模式。  默认值：ThemeColorMode.SYSTEM  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |

## AlertDialog

AlertDialog({controller: CustomDialogController, primaryTitle?: ResourceStr, secondaryTitle?: ResourceStr, content: ResourceStr, primaryButton?: ButtonOptions, secondaryButton?: ButtonOptions, theme?: Theme | CustomTheme, themeColorMode?: ThemeColorMode})

警告类弹出框，用于在触发一个将产生严重后果的不可逆操作（如删除、重置、取消编辑、停止等）时进行警告。

**装饰器类型：**@CustomDialog

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| controller | [CustomDialogController](ts-methods-custom-dialog-box.md#customdialogcontroller) | 是 | 警告弹出框控制器，用于控制弹出框的显示和隐藏。  **说明：** 未使用@Require装饰，构造时不强制校验参数。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| primaryTitle12+ | [ResourceStr](ts-types.md#resourcestr) | 否 | 警告弹出框一级标题。  默认不设置或设置为undefined，警告弹出框一级标题不显示。  **说明：** 标题超过两行会显示“...”。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| secondaryTitle12+ | [ResourceStr](ts-types.md#resourcestr) | 否 | 警告弹出框二级标题。  默认不设置或设置为undefined，警告弹出框二级标题不显示。  **说明：** 标题超过两行会显示“...”。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| content | [ResourceStr](ts-types.md#resourcestr) | 是 | 警告弹出框内容。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| primaryButton | [ButtonOptions](ohos-arkui-advanced-dialog.md#buttonoptions) | 否 | 警告弹出框左侧按钮。  默认不设置或设置为undefined，警告弹出框左侧按钮不显示。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| secondaryButton | [ButtonOptions](ohos-arkui-advanced-dialog.md#buttonoptions) | 否 | 警告弹出框右侧按钮。  默认不设置或设置为undefined，警告弹出框右侧按钮不显示。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| theme12+ | [Theme](js-apis-arkui-theme.md#theme) | [CustomTheme](js-apis-arkui-theme.md#customtheme) | 否 | 主题信息，可以是CustomTheme或从onWillApplyTheme中获取的Theme实例。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| themeColorMode12+ | [ThemeColorMode](ts-universal-attributes-foreground-blur-style.md#themecolormode枚举说明) | 否 | 自定义弹出框深浅色模式。  默认值：ThemeColorMode.SYSTEM  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |

## LoadingDialog

LoadingDialog({Controller: CustomDialogController, content?: ResourceStr, theme?: Theme | CustomTheme, themeColorMode?: ThemeColorMode})

进度加载类弹出框，用于显示操作执行中的提示信息。

**装饰器类型：**@CustomDialog

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| Controller | [CustomDialogController](ts-methods-custom-dialog-box.md#customdialogcontroller) | 是 | 加载弹出框控制器，用于控制弹出框的显示和隐藏。  **说明：** 未使用@Require装饰，构造时不强制校验参数。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| content | [ResourceStr](ts-types.md#resourcestr) | 否 | 加载弹出框内容。  默认不设置或设置为undefined，加载弹出框内容不显示。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| theme12+ | [Theme](js-apis-arkui-theme.md#theme) | [CustomTheme](js-apis-arkui-theme.md#customtheme) | 否 | 主题信息，可以是CustomTheme或从onWillApplyTheme中获取的Theme实例。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| themeColorMode12+ | [ThemeColorMode](ts-universal-attributes-foreground-blur-style.md#themecolormode枚举说明) | 否 | 自定义弹出框深浅色模式。  默认值：ThemeColorMode.SYSTEM  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |

## CustomContentDialog12+

CustomContentDialog({controller: CustomDialogController, contentBuilder: () => void, primaryTitle?: ResourceStr, secondaryTitle?: ResourceStr, localizedContentAreaPadding?: LocalizedPadding, contentAreaPadding?: Padding, buttons?: ButtonOptions[], theme?: Theme | CustomTheme, themeColorMode?: ThemeColorMode})

自定义内容区弹出框，同时支持定义操作区按钮样式。

**装饰器类型：**@CustomDialog

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 必填 | 装饰器类型 | 说明 |
| --- | --- | --- | --- | --- |
| controller | [CustomDialogController](ts-methods-custom-dialog-box.md#customdialogcontroller) | 是 | - | 弹出框控制器，用于控制弹出框的显示和隐藏。  **说明：** 未使用@Require装饰，构造时不强制校验参数。 |
| contentBuilder | () => void | 是 | @BuilderParam | 用于构建弹出框内容区域的组件构建函数。 |
| primaryTitle | [ResourceStr](ts-types.md#resourcestr) | 否 | - | 弹出框标题。  默认不设置或设置为undefined，弹出框标题不显示。  **说明：** 标题超过两行会显示“...”。 |
| secondaryTitle | [ResourceStr](ts-types.md#resourcestr) | 否 | - | 弹出框辅助文本。  默认不设置或设置为undefined，弹出框辅助文本不显示。  **说明：** 辅助文本超过两行会显示“...”。 |
| localizedContentAreaPadding | [LocalizedPadding](ts-types.md#localizedpadding12) | 否 | - | 弹出框内容区内边距，支持按语言方向自适应。设置了该属性时，contentAreaPadding不生效。 |
| contentAreaPadding | [Padding](ts-types.md#padding) | 否 | - | 弹出框内容区内边距。设置了localizedContentAreaPadding属性时该属性不生效。 |
| buttons | [ButtonOptions](ohos-arkui-advanced-dialog.md#buttonoptions)[] | 否 | - | 弹出框操作区按钮，最多支持4个按钮。 |
| theme | [Theme](js-apis-arkui-theme.md#theme) | [CustomTheme](js-apis-arkui-theme.md#customtheme) | 否 | - | 主题信息，可以是CustomTheme或从onWillApplyTheme中获取的Theme实例。 |
| themeColorMode | [ThemeColorMode](ts-universal-attributes-foreground-blur-style.md#themecolormode枚举说明) | 否 | - | 自定义弹出框深浅色模式。  默认值：ThemeColorMode.SYSTEM。 |

**说明** 

当弹框高度不足时，触发全局滚动的规格为contentBuilder被压缩，压缩至小于100vp时启动全局滚动。

CustomContentDialog内容区的滚动需由开发者自定义，内容区自定义滚动必须配合属性nestedScroll，nestedScroll({ scrollForward: NestedScrollMode.PARALLEL, scrollBackward: NestedScrollMode.PARALLEL })

## PopoverDialog14+

PopoverDialog({visible: boolean, popover: PopoverOptions, targetBuilder: Callback<void>})

跟手弹出框，基于目标组件位置弹出，上述的TipsDialog、SelectDialog、ConfirmDialog、AlertDialog、LoadingDialog、CustomContentDialog都可作为弹出框内容。

**装饰器类型：**@Component

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 必填 | 装饰器类型 | 说明 |
| --- | --- | --- | --- | --- |
| visible | boolean | 是 | @Link | 是否显示跟手弹出框。true表示显示弹出框，false表示隐藏弹出框。  默认值为false。 |
| popover | [PopoverOptions](ohos-arkui-advanced-dialog.md#popoveroptions14) | 是 | @Prop  @Require | 配置跟手弹出框的参数，包含弹出框内容、位置等属性，具体参见PopoverOptions类型说明。 |
| targetBuilder | [Callback](ts-types.md#callback12)<void> | 是 | @Require  @BuilderParam | 跟手弹出框基于的目标组件构建器函数，用于定义弹出框显示的参考位置组件。 |

## ButtonOptions

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| value | [ResourceStr](ts-types.md#resourcestr) | 否 | 否 | 按钮的内容。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| action | () => void | 否 | 是 | 按钮的点击事件。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| background | [ResourceColor](ts-types.md#resourcecolor) | 否 | 是 | 按钮的背景色。  默认值跟随buttonStyle。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| fontColor | [ResourceColor](ts-types.md#resourcecolor) | 否 | 是 | 按钮的字体颜色。  默认值跟随buttonStyle。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| buttonStyle12+ | [ButtonStyleMode](ts-basic-components-button.md#buttonstylemode11枚举说明) | 否 | 是 | 按钮的样式。  默认值：2in1设备为ButtonStyleMode.NORMAL，其他设备为ButtonStyleMode.TEXTUAL。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| role12+ | [ButtonRole](ts-basic-components-button.md#buttonrole12枚举说明) | 否 | 是 | 按钮的角色。  默认值：ButtonRole.NORMAL  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| defaultFocus18+ | boolean | 否 | 是 | 按钮是否设置默认焦点。  true：按钮是默认焦点。  false：按钮不是默认焦点。  默认值：false  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| textAlign24+ | [TextAlign](ts-appendix-enums.md#textalign) | 否 | 是 | 按钮文本的对齐方式。  默认值：TextAlign.Start  **元服务API：** 从API version 24开始，该接口支持在元服务中使用。 |

**说明** 

buttonStyle和role优先级高于fontColor和background。当buttonStyle和role设置的是默认值时，fontColor和background生效。

若同时给多个按钮设置defaultFocus，则默认焦点为设置defaultFocus按钮中显示顺序的第一个按钮。

## PopoverOptions14+

跟手弹出框参数，用于设置弹出框内容、位置属性等。

继承自[CustomPopupOptions](ts-universal-attributes-popup.md#custompopupoptions8类型说明)。

**说明** 

radius默认值为32vp。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 事件

不支持[通用事件](ts-component-general-events.md)。

## 示例

### 示例1（上图下文弹出框）

上图下文弹出框，包含imageRes、content等内容。

```ts
import { TipsDialog } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  dialogControllerImage: CustomDialogController = new CustomDialogController({
    builder: TipsDialog({
      imageRes: $r('sys.media.ohos_ic_public_voice'),
      content: '想要卸载这个APP嘛?',
      primaryButton: {
        value: '取消',
        action: () => {
          console.info('Callback when the first button is clicked');
        },
      },
      secondaryButton: {
        value: '删除',
        role: ButtonRole.ERROR,
        action: () => {
          console.info('Callback when the second button is clicked');
        }
      },
      onCheckedChange: () => {
        console.info('Callback when the checkbox is clicked');
      }
    }),
  })

  build() {
    Row() {
      Stack() {
        Column(){
          Button("上图下文弹出框")
            .width(96)
            .height(40)
            .onClick(() => {
              this.dialogControllerImage.open();
            })
        }.margin({bottom: 300})
      }.align(Alignment.Bottom)
      .width('100%').height('100%')
    }
    .backgroundImageSize({ width: '100%', height: '100%' })
    .height('100%')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/o25_TdfoRZKhjKqrIzmOmQ/zh-cn_image_0000002706836236.png)

### 示例2（纯列表弹出框）

纯列表弹出框，包含selectedIndex、radioContent等内容。

```ts
import { SelectDialog } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  // 设置默认选中radio的index
  radioIndex: number = 0;
  dialogControllerList: CustomDialogController = new CustomDialogController({
    builder: SelectDialog({
      title: '文本标题',
      selectedIndex: this.radioIndex,
      confirm: {
        value: '取消',
        action: () => {},
      },
      radioContent: [
        {
          title: '文本文本文本文本文本',
          action: () => {
            this.radioIndex = 0;
          }
        },
        {
          title: '文本文本文本文本',
          action: () => {
            this.radioIndex = 1;
          }
        },
        {
          title: '文本文本文本文本',
          action: () => {
            this.radioIndex = 2;
          }
        },
      ]
    }),
  })

  build() {
    Row() {
      Stack() {
        Column() {
          Button("纯列表弹出框")
            .width(96)
            .height(40)
            .onClick(() => {
              this.dialogControllerList.open();
            })
        }.margin({ bottom: 300 })
      }
      .align(Alignment.Bottom)
      .width('100%')
      .height('100%')
    }
    .backgroundImageSize({ width: '100%', height: '100%' })
    .height('100%')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/89/v3/kL902wSvQe-0Ia31hKfAYw/zh-cn_image_0000002736315341.png)

### 示例3（文本与勾选弹出框）

文本与勾选弹出框，包含content、checkTips等内容。

```ts
import { ConfirmDialog } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  isChecked: boolean = false;
  dialogControllerCheckBox: CustomDialogController = new CustomDialogController({
    builder: ConfirmDialog({
      title: '文本标题',
      content: '文本文本文本文本文本文本文本文本文本文本文本文本文本文本文本文本文本文本文本',
      // 勾选框选中状态
      isChecked: this.isChecked,
      // 勾选框说明文本
      checkTips: '禁止后不再提示',
      primaryButton: {
        value: '禁止',
        action: () => {},
      },
      secondaryButton: {
        value: '允许',
        action: () => {
          this.isChecked = false;
          console.info('Callback when the second button is clicked');
        }
      },
      onCheckedChange: () => {
        console.info('Callback when the checkbox is clicked');
      },
    }),
    autoCancel: true,
    alignment: DialogAlignment.Bottom
  })

  build() {
    Row() {
      Stack() {
        Column(){
          Button("文本+勾选弹出框")
            .width(96)
            .height(40)
            .onClick(() => {
              this.dialogControllerCheckBox.open();
            })
        }
        .margin({bottom: 300})
      }
      .align(Alignment.Bottom)
      .width('100%')
      .height('100%')
    }
    .backgroundImageSize({ width: '100%', height: '100%' })
    .height('100%')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8a/v3/DbBYIvKySreA7Y7M4wfANw/zh-cn_image_0000002706676302.png)

### 示例4（纯文本弹出框）

纯文本弹出框，包含primaryTitle、secondaryTitle、content等内容。

```ts
import { AlertDialog } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  dialogControllerConfirm: CustomDialogController = new CustomDialogController({
    builder: AlertDialog({
      primaryTitle: '弹框一级标题',
      secondaryTitle: '弹框二级标题',
      content: '文本文本文本文本文本',
      primaryButton: {
        value: '取消',
        action: () => {
        },
      },
      secondaryButton: {
        value: '确认',
        role: ButtonRole.ERROR,
        action: () => {
          console.info('Callback when the second button is clicked');
        }
      },
    }),
  })

  build() {
    Row() {
      Stack() {
        Column() {
          Button("纯文本弹出框")
            .width(96)
            .height(40)
            .onClick(() => {
              this.dialogControllerConfirm.open();
            })
        }
        .margin({ bottom: 300 })
      }
      .align(Alignment.Bottom)
      .width('100%')
      .height('100%')
    }
    .backgroundImageSize({ width: '100%', height: '100%' })
    .height('100%')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/15/v3/9DuC_UbfThOL9UU85cktFA/zh-cn_image_0000002736435389.png)

### 示例5（进度加载类弹出框）

进度加载类弹出框，包含content等内容。

```ts
import { LoadingDialog } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  dialogControllerProgress: CustomDialogController = new CustomDialogController({
    builder: LoadingDialog({
      content: '文本文本文本文本文本...',
    }),
  })

  build() {
    Row() {
      Stack() {
        Column() {
          Button("进度加载类弹出框")
            .width(96)
            .height(40)
            .onClick(() => {
              this.dialogControllerProgress.open();
            })
        }
        .margin({ bottom: 300 })
      }
      .align(Alignment.Bottom)
      .width('100%')
      .height('100%')
    }
    .backgroundImageSize({ width: '100%', height: '100%' })
    .height('100%')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c9/v3/yHBXn419RxOTo2lqhqqqwQ/zh-cn_image_0000002706836238.gif)

### 示例6（自定义主题风格弹出框）

自定义主题风格弹出框，包含content、theme等内容。

```ts
import { CustomColors, CustomTheme, LoadingDialog } from '@kit.ArkUI';

class CustomThemeImpl implements CustomTheme {
  colors?: CustomColors;

  constructor(colors: CustomColors) {
    this.colors = colors;
  }
}

// 自定义内容文字及loading组件主题颜色
class CustomThemeColors implements CustomColors {
  fontPrimary = '#ffd0a300';
  iconSecondary = '#ffd000cd';
}

@Entry
@Component
struct Index {
  @State customTheme: CustomTheme = new CustomThemeImpl(new CustomThemeColors());
  dialogController: CustomDialogController = new CustomDialogController({
    builder: LoadingDialog({
      content: 'text',
      theme: this.customTheme,
    })
  });

  build() {
    Row() {
      Stack() {
        Column() {
          Button("dialog")
            .width(96)
            .height(40)
            .onClick(() => {
              this.dialogController.open();
            })
        }
        .margin({ bottom: 300 })
      }
      .align(Alignment.Bottom)
      .width('100%')
      .height('100%')
    }
    .backgroundImageSize({ width: '100%', height: '100%' })
    .height('100%')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ec/v3/bL2fSw4HQsSaprBjx8ZXyw/zh-cn_image_0000002736315343.png)

### 示例7（自定义深浅色模式弹出框）

自定义深浅色模式弹出框，包含content、themeColorMode等内容。

```ts
import { LoadingDialog } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  dialogController: CustomDialogController = new CustomDialogController({
    builder: LoadingDialog({
      content: 'Text',
      themeColorMode: ThemeColorMode.DARK, // 设置弹出框深浅色模式为深色模式
    })
  });

  build() {
    Row() {
      Stack() {
        Column() {
          Button("Dialog")
            .width(96)
            .height(40)
            .onClick(() => {
              this.dialogController.open();
            })
        }
        .margin({ bottom: 300 })
      }
      .align(Alignment.Bottom)
      .width('100%')
      .height('100%')
    }
    .backgroundImageSize({ width: '100%', height: '100%' })
    .height('100%')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/y7P0-1IIRxa-iFKlV8-tUw/zh-cn_image_0000002706676304.png)

### 示例8（自定义内容弹出框）

支持自定义内容弹出框，包含contentBuilder、buttons等内容。

```ts
import { CustomContentDialog } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  dialogController: CustomDialogController = new CustomDialogController({
    builder: CustomContentDialog({
      primaryTitle: '标题',
      secondaryTitle: '辅助文本',
      contentBuilder: () => {
        this.buildContent();
      },
      buttons: [
        {
          value: '按钮1',
          buttonStyle: ButtonStyleMode.TEXTUAL,
          action: () => {
            console.info('Callback when the button is clicked');
          }
        },
        {
          value: '按钮2',
          buttonStyle: ButtonStyleMode.TEXTUAL,
          role: ButtonRole.ERROR
        }
      ],
    }),
  });

  build() {
    Column() {
      Button("支持自定义内容弹出框")
        .onClick(() => {
          this.dialogController.open();
        })
    }
    .width('100%')
    .height('100%')
    .justifyContent(FlexAlign.Center)
  }
  
  // 自定义弹出框的内容区
  @Builder
  buildContent(): void {
    Column() {
      Text('内容区')
    }
    .width('100%')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fc/v3/_u4Jm_dBRP2tmQsbBmVmVA/zh-cn_image_0000002736435391.png)

### 示例9（跟手弹出框）

从API version 14开始，该示例展示了设置跟手弹出框（警告弹出框为例），包含visible、popover、targetBuilder等内容。

```ts
import { AlertDialog, PopoverDialog, PopoverOptions } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  @State isShow: boolean = false;
  @State popoverOptions: PopoverOptions = {
    builder: () => {
      this.dialogBuilder();
    },
    width: 320,
  }
  
  // 跟手弹出框内容
  @Builder dialogBuilder() {
    AlertDialog({
      content: '跟手弹出框',
      primaryButton: {
        value: '取消',
        action: () => {
          this.isShow = false;
        },
      },
      secondaryButton: {
        value: '确认',
        action: () => {
          this.isShow = false;
        },
      },
    });
  }

  // 跟手弹出框绑定的builder
  @Builder buttonBuilder() {
    Button('跟手弹出框目标组件')
    .onClick(() => {
      this.isShow = true;
    });
  }

  build() {
    Column() {
      PopoverDialog({
        visible: this.isShow,
        popover: this.popoverOptions,
        targetBuilder: () => {
          this.buttonBuilder();
        },
      })
    }
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/86/v3/7C_2Iv5eTYuVzpaiOqFIFg/zh-cn_image_0000002706836240.png)

### 示例10（弹出框按钮设置默认获焦）

从API version 18开始，该示例展示了设置默认获焦按钮弹出框（以AlertDialog为例），包含defaultFocus等内容。

```ts
import { AlertDialog } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  dialogController: CustomDialogController = new CustomDialogController({
    builder: AlertDialog({
      primaryTitle: 'AlertDialog',
      secondaryTitle: '副标题',
      content: '第二个按钮设置为默认',
      primaryButton: {
        value: 'DEFAULT',
        action: () => {}
      },
      secondaryButton: {
        value: 'TRUE',
        defaultFocus: true, // 设置该按钮为默认获焦按钮。
        action: () => {}
      },
    })
  });

  build() {
    Row() {
      Stack() {
        Column() {
          Button("AlertDialog")
            .width(96)
            .height(40)
            .onClick(() => {
              this.dialogController.open();
            })
        }
        .margin({ bottom: 300 })
      }
      .align(Alignment.Bottom)
      .width('100%')
      .height('100%')
    }
    .backgroundImageSize({ width: '100%', height: '100%' })
    .height('100%')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f7/v3/6tse7KBnT1S3LTORYDoPtg/zh-cn_image_0000002736315345.png)
