---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-dialog
title: 弹出框 (Dialog)
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 弹窗 > 弹出框 (Dialog)
category: harmonyos-references
scraped_at: 2026-04-28T08:02:23+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:faf51400736a080792df10f6339ed6e6ff29ff719e9c652062b7f733717b6f75
---

弹出框是一种模态窗口，用于临时展示用户需关注的信息或待处理的操作，同时保持当前上下文环境。用户必须完成交互才能退出该模式。

说明

* 该组件从API version 10开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。
* 该组件仅可在Stage模型下使用。
* 如果Dialog设置[通用属性](ts-component-general-attributes.md)和[通用事件](ts-component-general-events.md)，编译工具链会额外生成节点\_\_Common\_\_，并将通用属性或通用事件挂载在\_\_Common\_\_上，而不是直接应用到Dialog本身。这可能导致开发者设置的通用属性或通用事件不生效或不符合预期，因此，不建议Dialog设置通用属性和通用事件。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { TipsDialog, SelectDialog, ConfirmDialog, AlertDialog, LoadingDialog, CustomContentDialog } from '@kit.ArkUI';
```

## 子组件

PhonePC/2in1TabletTVWearable

无

## TipsDialog

PhonePC/2in1TabletTVWearable

TipsDialog({controller: CustomDialogController, imageRes: ResourceStr | PixelMap, imageSize?: SizeOptions, title?: ResourceStr, content?: ResourceStr, checkTips?: ResourceStr, isChecked?: boolean, checkAction?: (isChecked: boolean) => void, onCheckedChange?: Callback<boolean>, primaryButton?: ButtonOptions, secondaryButton?: ButtonOptions, theme?: Theme | CustomTheme, themeColorMode?: ThemeColorMode})

提示弹出框，即为带图形确认弹出框，必要时可通过图形化方式展现确认弹出框。

**装饰器类型：**@CustomDialog

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 必填 | 装饰器类型 | 说明 |
| --- | --- | --- | --- | --- |
| controller | [CustomDialogController](ts-methods-custom-dialog-box.md#customdialogcontroller) | 是 | - | 提示弹出框控制器。  **说明：** 未使用@Require装饰，构造时不强制校验参数。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| imageRes | [ResourceStr12+](ts-types.md#resourcestr) | [PixelMap12+](arkts-apis-image-pixelmap.md) | 是 | - | 展示的图片。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| imageSize | [SizeOptions](ts-types.md#sizeoptions) | 否 | - | 自定义图片尺寸。  默认值：64\*64vp  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| title | [ResourceStr](ts-types.md#resourcestr) | 否 | - | 提示弹出框标题。  默认不设置或设置为undefined，弹出框标题不显示。  **说明：** 标题超过两行会显示“...”。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| content | [ResourceStr](ts-types.md#resourcestr) | 否 | - | 提示弹出框内容。  默认不设置或设置为undefined，弹出框内容不显示。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| checkTips | [ResourceStr](ts-types.md#resourcestr) | 否 | - | checkbox的提示内容。  默认不设置或设置为undefined，提示内容不显示。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| isChecked | boolean | 否 | @Prop | value为true时，表示checkbox已选中，value为false时，表示未选中。  默认值：false  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| checkAction12+ | (isChecked: boolean) => void | 否 | - | checkbox的选中状态改变事件。isChecked为true时，表示checkbox已选中，isChecked为false时，表示checkbox未选中。现推荐使用onCheckedChange12+。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| onCheckedChange12+ | [Callback](ts-types.md#callback12)<boolean> | 否 | - | checkbox的选中状态改变事件回调。回调参数类型为boolean，true表示checkbox已选中，false表示checkbox未选中。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| primaryButton | [ButtonOptions](ohos-arkui-advanced-dialog.md#buttonoptions) | 否 | - | 提示弹出框左侧按钮。  默认不设置或设置为undefined，左侧按钮不显示。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| secondaryButton | [ButtonOptions](ohos-arkui-advanced-dialog.md#buttonoptions) | 否 | - | 提示弹出框右侧按钮。  默认不设置或设置为undefined，右侧按钮不显示。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| theme12+ | [Theme](js-apis-arkui-theme.md#theme) | [CustomTheme](js-apis-arkui-theme.md#customtheme) | 否 | - | 主题信息，可以是CustomTheme或从onWillApplyTheme中获取的Theme实例。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| themeColorMode12+ | [ThemeColorMode](ts-universal-attributes-foreground-blur-style.md#themecolormode枚举说明) | 否 | - | 自定义弹出框深浅色模式。  默认值：ThemeColorMode.SYSTEM  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |

## SelectDialog

PhonePC/2in1TabletTVWearable

SelectDialog({controller: CustomDialogController, title: ResourceStr, content?: ResourceStr, selectedIndex?: number, confirm?: ButtonOptions, radioContent: Array<SheetInfo>, theme?: Theme | CustomTheme, themeColorMode?: ThemeColorMode})

选择类弹出框，弹框中以列表或网格的形式提供可选的内容。

**装饰器类型：**@CustomDialog

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| controller | [CustomDialogController](ts-methods-custom-dialog-box.md#customdialogcontroller) | 是 | 选择弹出框控制器。  **说明：** 未使用@Require装饰，构造时不强制校验参数。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| title | [ResourceStr](ts-types.md#resourcestr) | 是 | 选择弹出框标题。  **说明：** 标题超过两行会显示“...”。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| content | [ResourceStr](ts-types.md#resourcestr) | 否 | 选择弹出框内容。  默认不设置或设置为undefined，弹出框内容不显示。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| selectedIndex | number | 否 | 选择弹出框的选中项。  取值范围：大于等于-1的整数。  默认值：-1，没有选中项。若设置数值小于-1，按没有选中项处理。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| confirm | [ButtonOptions](ohos-arkui-advanced-dialog.md#buttonoptions) | 否 | 选择弹出框底部按钮。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| radioContent | Array<[SheetInfo](ts-methods-action-sheet.md#sheetinfo对象说明)> | 是 | 选择弹出框的子项内容列表，每个选择项支持设置文本和选中的回调事件。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| theme12+ | [Theme](js-apis-arkui-theme.md#theme) | [CustomTheme](js-apis-arkui-theme.md#customtheme) | 否 | 主题信息，可以是CustomTheme或从onWillApplyTheme中获取的Theme实例。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| themeColorMode12+ | [ThemeColorMode](ts-universal-attributes-foreground-blur-style.md#themecolormode枚举说明) | 否 | 自定义弹出框深浅色模式。  默认值：ThemeColorMode.SYSTEM  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |

## ConfirmDialog

PhonePC/2in1TabletTVWearable

ConfirmDialog({controller: CustomDialogController, title: ResourceStr, content?: ResourceStr, checkTips?: ResourceStr, isChecked?: boolean, primaryButton?: ButtonOptions, secondaryButton?: ButtonOptions, theme?: Theme | CustomTheme, themeColorMode?: ThemeColorMode})

信息确认类弹出框，操作未正确执行（如网络错误、电池电量过低），或未正确操作时（如指纹录入），反馈的错误或提示信息。

**装饰器类型：**@CustomDialog

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 必填 | 装饰器类型 | 说明 |
| --- | --- | --- | --- | --- |
| controller | [CustomDialogController](ts-methods-custom-dialog-box.md#customdialogcontroller) | 是 | - | 确认弹出框控制器。  **说明：** 未使用@Require装饰，构造时不强制校验参数。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| title | [ResourceStr](ts-types.md#resourcestr) | 是 | - | 确认弹出框标题。  **说明：** 标题超过两行会显示“...”。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| content | [ResourceStr](ts-types.md#resourcestr) | 否 | - | 确认弹出框内容。  默认不设置或设置为undefined，确认弹出框内容不显示。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| checkTips | [ResourceStr](ts-types.md#resourcestr) | 否 | - | checkbox的提示内容。  默认不设置或设置为undefined，checkbox的提示内容不显示。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| isChecked | boolean | 否 | @Prop | value为true时，表示checkbox已选中，value为false时，表示未选中。  默认值：false  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| onCheckedChange12+ | [Callback](ts-types.md#callback12)<boolean> | 否 | - | checkbox的选中状态改变事件回调。回调参数类型为boolean，true表示checkbox已选中，false表示checkbox未选中。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| primaryButton | [ButtonOptions](ohos-arkui-advanced-dialog.md#buttonoptions) | 否 | - | 确认弹出框左侧按钮。  默认不设置或设置为undefined，确认弹出框左侧按钮不显示。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| secondaryButton | [ButtonOptions](ohos-arkui-advanced-dialog.md#buttonoptions) | 否 | - | 确认弹出框右侧按钮。  默认不设置或设置为undefined，确认弹出框右侧按钮不显示。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| theme12+ | [Theme](js-apis-arkui-theme.md#theme) | [CustomTheme](js-apis-arkui-theme.md#customtheme) | 否 | - | 主题信息，可以是CustomTheme或从onWillApplyTheme中获取的Theme实例。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| themeColorMode12+ | [ThemeColorMode](ts-universal-attributes-foreground-blur-style.md#themecolormode枚举说明) | 否 | - | 自定义弹出框深浅色模式。  默认值：ThemeColorMode.SYSTEM  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |

## AlertDialog

PhonePC/2in1TabletTVWearable

AlertDialog({controller: CustomDialogController, primaryTitle?: ResourceStr, secondaryTitle?: ResourceStr, content: ResourceStr, primaryButton?: ButtonOptions, secondaryButton?: ButtonOptions, theme?: Theme | CustomTheme, themeColorMode?: ThemeColorMode})

操作确认类弹出框，触发一个将产生严重后果的不可逆操作时，如删除、重置、取消编辑、停止等。

**装饰器类型：**@CustomDialog

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| controller | [CustomDialogController](ts-methods-custom-dialog-box.md#customdialogcontroller) | 是 | 确认弹出框控制器。  **说明：** 未使用@Require装饰，构造时不强制校验参数。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| primaryTitle12+ | [ResourceStr](ts-types.md#resourcestr) | 否 | 确认弹出框一级标题。  默认不设置或设置为undefined，确认弹出框一级标题不显示。  **说明：** 标题超过两行会显示“...”。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| secondaryTitle12+ | [ResourceStr](ts-types.md#resourcestr) | 否 | 确认弹出框二级标题。  默认不设置或设置为undefined，确认弹出框二级标题不显示。  **说明：** 标题超过两行会显示“...”。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| content | [ResourceStr](ts-types.md#resourcestr) | 是 | 确认弹出框内容。  默认不设置或设置为undefined，确认弹出框内容不显示。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| primaryButton | [ButtonOptions](ohos-arkui-advanced-dialog.md#buttonoptions) | 否 | 确认弹出框左侧按钮。  默认不设置或设置为undefined，确认弹出框左侧按钮不显示。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| secondaryButton | [ButtonOptions](ohos-arkui-advanced-dialog.md#buttonoptions) | 否 | 确认弹出框右侧按钮。  默认不设置或设置为undefined，确认弹出框右侧按钮不显示。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| theme12+ | [Theme](js-apis-arkui-theme.md#theme) | [CustomTheme](js-apis-arkui-theme.md#customtheme) | 否 | 主题信息，可以是CustomTheme或从onWillApplyTheme中获取的Theme实例。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| themeColorMode12+ | [ThemeColorMode](ts-universal-attributes-foreground-blur-style.md#themecolormode枚举说明) | 否 | 自定义弹出框深浅色模式。  默认值：ThemeColorMode.SYSTEM  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |

## LoadingDialog

PhonePC/2in1TabletTVWearable

LoadingDialog({Controller: CustomDialogController, content?: ResourceStr, theme?: Theme | CustomTheme, themeColorMode?: ThemeColorMode})

进度加载类弹出框，用于显示操作执行中的提示信息。

**装饰器类型：**@CustomDialog

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| Controller | [CustomDialogController](ts-methods-custom-dialog-box.md#customdialogcontroller) | 是 | 加载弹出框控制器。  **说明：** 未使用@Require装饰，构造时不强制校验参数。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| content | [ResourceStr](ts-types.md#resourcestr) | 否 | 加载弹出框内容。  默认不设置或设置为undefined，加载弹出框内容不显示。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| theme12+ | [Theme](js-apis-arkui-theme.md#theme) | [CustomTheme](js-apis-arkui-theme.md#customtheme) | 否 | 主题信息，可以是CustomTheme或从onWillApplyTheme中获取的Theme实例。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| themeColorMode12+ | [ThemeColorMode](ts-universal-attributes-foreground-blur-style.md#themecolormode枚举说明) | 否 | 自定义弹出框深浅色模式。  默认值：ThemeColorMode.SYSTEM  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |

## CustomContentDialog12+

PhonePC/2in1TabletTVWearable

CustomContentDialog({controller: CustomDialogController, contentBuilder: () => void, primaryTitle?: ResourceStr, secondaryTitle?: ResourceStr, contentAreaPadding?: Padding, buttons?: ButtonOptions[], theme?: Theme | CustomTheme, themeColorMode?: ThemeColorMode})

自定义内容区弹出框，同时支持定义操作区按钮样式。

**装饰器类型：**@CustomDialog

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 必填 | 装饰器类型 | 说明 |
| --- | --- | --- | --- | --- |
| controller | [CustomDialogController](ts-methods-custom-dialog-box.md#customdialogcontroller) | 是 | - | 弹出框控制器。  **说明：** 未使用@Require装饰，构造时不强制校验参数。 |
| contentBuilder | () => void | 是 | @BuilderParam | 弹出框内容。 |
| primaryTitle | [ResourceStr](ts-types.md#resourcestr) | 否 | - | 弹出框标题。  默认不设置或设置为undefined，弹出框标题不显示。  **说明：** 标题超过两行会显示“...”。 |
| secondaryTitle | [ResourceStr](ts-types.md#resourcestr) | 否 | - | 弹出框辅助文本。  默认不设置或设置为undefined，弹出框辅助文本不显示。  **说明：** 辅助文本超过两行会显示“...”。 |
| localizedContentAreaPadding | [LocalizedPadding](ts-types.md#localizedpadding12) | 否 | - | 弹出框内容区内边距。 |
| contentAreaPadding | [Padding](ts-types.md#padding) | 否 | - | 弹出框内容区内边距。设置了localizedContentAreaPadding属性时该属性不生效。 |
| buttons | [ButtonOptions](ohos-arkui-advanced-dialog.md#buttonoptions)[] | 否 | - | 弹出框操作区按钮，最多支持4个按钮。 |
| theme | [Theme](js-apis-arkui-theme.md#theme) | [CustomTheme](js-apis-arkui-theme.md#customtheme) | 否 | - | 主题信息，可以是CustomTheme或从onWillApplyTheme中获取的Theme实例。 |
| themeColorMode | [ThemeColorMode](ts-universal-attributes-foreground-blur-style.md#themecolormode枚举说明) | 否 | - | 自定义弹出框深浅色模式。  默认值：ThemeColorMode.SYSTEM |

说明

当弹框高度不足时，触发全局滚动的规格为contentBuilder被压缩，压缩至小于100vp时启动全局滚动。

CustomContentDialog内容区的滚动需由开发者自定义，内容区自定义滚动必须配合属性nestedScroll，nestedScroll({ scrollForward: NestedScrollMode.PARALLEL, scrollBackward: NestedScrollMode.PARALLEL })

## PopoverDialog14+

PhonePC/2in1TabletTVWearable

PopoverDialog({visible: boolean, popover: PopoverOptions, targetBuilder: Callback<void>})

跟手弹出框，基于目标组件位置弹出，上文中的TipsDialog、SelectDialog、ConfirmDialog、AlertDialog、LoadingDialog、CustomContentDialog都可作为弹出框内容。

**装饰器类型：**@Component

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 必填 | 装饰器类型 | 说明 |
| --- | --- | --- | --- | --- |
| visible | boolean | 是 | @Link | 跟手弹出框显示状态。value为true时，表示显示弹出框，value为false时，表示隐藏弹出框。  默认值为false，隐藏弹出框。 |
| popover | [PopoverOptions](ohos-arkui-advanced-dialog.md#popoveroptions14) | 是 | @Prop  @Require | 配置跟手弹出框的参数。 |
| targetBuilder | [Callback](ts-types.md#callback12)<void> | 是 | @Require  @BuilderParam | 跟手弹出框基于的目标组件。 |

## ButtonOptions

PhonePC/2in1TabletTVWearable

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

说明

buttonStyle和role优先级高于fontColor和background。当buttonStyle和role设置的是默认值时，fontColor和background生效。

若同时给多个按钮设置defaultFocus，则默认焦点为设置defaultFocus按钮中显示顺序的第一个按钮。

## PopoverOptions14+

PhonePC/2in1TabletTVWearable

跟手弹出框参数，用于设置弹出框内容、位置属性等。

继承自[CustomPopupOptions](ts-universal-attributes-popup.md#custompopupoptions8类型说明)。

说明

radius默认值为32vp。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 事件

PhonePC/2in1TabletTVWearable

不支持[通用事件](ts-component-general-events.md)。

## 示例

PhonePC/2in1TabletTVWearable

### 示例1（上图下文弹出框）

上图下文弹出框，包含imageRes、content等内容。

```
1. import { TipsDialog } from '@kit.ArkUI';

3. @Entry
4. @Component
5. struct Index {
6. dialogControllerImage: CustomDialogController = new CustomDialogController({
7. builder: TipsDialog({
8. imageRes: $r('sys.media.ohos_ic_public_voice'),
9. content: '想要卸载这个APP嘛?',
10. primaryButton: {
11. value: '取消',
12. action: () => {
13. console.info('Callback when the first button is clicked')
14. },
15. },
16. secondaryButton: {
17. value: '删除',
18. role: ButtonRole.ERROR,
19. action: () => {
20. console.info('Callback when the second button is clicked')
21. }
22. },
23. onCheckedChange: () => {
24. console.info('Callback when the checkbox is clicked')
25. }
26. }),
27. })

29. build() {
30. Row() {
31. Stack() {
32. Column(){
33. Button("上图下文弹出框")
34. .width(96)
35. .height(40)
36. .onClick(() => {
37. this.dialogControllerImage.open()
38. })
39. }.margin({bottom: 300})
40. }.align(Alignment.Bottom)
41. .width('100%').height('100%')
42. }
43. .backgroundImageSize({ width: '100%', height: '100%' })
44. .height('100%')
45. }
46. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a6/v3/VTrlrv1URd-IVFfRpZIntA/zh-cn_image_0000002552960068.png?HW-CC-KV=V1&HW-CC-Date=20260428T000221Z&HW-CC-Expire=86400&HW-CC-Sign=55918482B36795EC15EDDF1BA5AADFAF7123AC28493AC354252E0EF3169A8413)

### 示例2（纯列表弹出框）

纯列表弹出框，包含selectedIndex、radioContent等内容。

```
1. import { SelectDialog } from '@kit.ArkUI';

3. @Entry
4. @Component
5. struct Index {
6. // 设置默认选中radio的index
7. radioIndex: number = 0;
8. dialogControllerList: CustomDialogController = new CustomDialogController({
9. builder: SelectDialog({
10. title: '文本标题',
11. selectedIndex: this.radioIndex,
12. confirm: {
13. value: '取消',
14. action: () => {},
15. },
16. radioContent: [
17. {
18. title: '文本文本文本文本文本',
19. action: () => {
20. this.radioIndex = 0
21. }
22. },
23. {
24. title: '文本文本文本文本',
25. action: () => {
26. this.radioIndex = 1
27. }
28. },
29. {
30. title: '文本文本文本文本',
31. action: () => {
32. this.radioIndex = 2
33. }
34. },
35. ]
36. }),
37. })

39. build() {
40. Row() {
41. Stack() {
42. Column() {
43. Button("纯列表弹出框")
44. .width(96)
45. .height(40)
46. .onClick(() => {
47. this.dialogControllerList.open()
48. })
49. }.margin({ bottom: 300 })
50. }
51. .align(Alignment.Bottom)
52. .width('100%')
53. .height('100%')
54. }
55. .backgroundImageSize({ width: '100%', height: '100%' })
56. .height('100%')
57. }
58. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/50/v3/_DfCeODmTOmeD2fHE07YvA/zh-cn_image_0000002583480069.png?HW-CC-KV=V1&HW-CC-Date=20260428T000221Z&HW-CC-Expire=86400&HW-CC-Sign=C85202BE5703FCBB430DCA3FC72E9216D6052395C660C8B81BCFDDAA1B66A2A3)

### 示例3（文本与勾选弹出框）

文本与勾选弹出框，包含content、checkTips等内容。

```
1. import { ConfirmDialog } from '@kit.ArkUI';

3. @Entry
4. @Component
5. struct Index {
6. isChecked: boolean = false;
7. dialogControllerCheckBox: CustomDialogController = new CustomDialogController({
8. builder: ConfirmDialog({
9. title: '文本标题',
10. content: '文本文本文本文本文本文本文本文本文本文本文本文本文本文本文本文本文本文本文本',
11. // 勾选框选中状态
12. isChecked: this.isChecked,
13. // 勾选框说明文本
14. checkTips: '禁止后不再提示',
15. primaryButton: {
16. value: '禁止',
17. action: () => {},
18. },
19. secondaryButton: {
20. value: '允许',
21. action: () => {
22. this.isChecked = false
23. console.info('Callback when the second button is clicked')
24. }
25. },
26. onCheckedChange: () => {
27. console.info('Callback when the checkbox is clicked')
28. },
29. }),
30. autoCancel: true,
31. alignment: DialogAlignment.Bottom
32. })

34. build() {
35. Row() {
36. Stack() {
37. Column(){
38. Button("文本+勾选弹出框")
39. .width(96)
40. .height(40)
41. .onClick(() => {
42. this.dialogControllerCheckBox.open()
43. })
44. }
45. .margin({bottom: 300})
46. }
47. .align(Alignment.Bottom)
48. .width('100%')
49. .height('100%')
50. }
51. .backgroundImageSize({ width: '100%', height: '100%' })
52. .height('100%')
53. }
54. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6e/v3/kIL6NoNVRP61zG5OENuMeA/zh-cn_image_0000002552800420.png?HW-CC-KV=V1&HW-CC-Date=20260428T000221Z&HW-CC-Expire=86400&HW-CC-Sign=94CB3A62215A6196A3267A308073AE386F95E09743F79CFE2946008D25E83BD2)

### 示例4（纯文本弹出框）

纯文本弹出框，包含primaryTitle、secondaryTitle、content等内容。

```
1. import { AlertDialog } from '@kit.ArkUI';

3. @Entry
4. @Component
5. struct Index {
6. dialogControllerConfirm: CustomDialogController = new CustomDialogController({
7. builder: AlertDialog({
8. primaryTitle: '弹框一级标题',
9. secondaryTitle: '弹框二级标题',
10. content: '文本文本文本文本文本',
11. primaryButton: {
12. value: '取消',
13. action: () => {
14. },
15. },
16. secondaryButton: {
17. value: '确认',
18. role: ButtonRole.ERROR,
19. action: () => {
20. console.info('Callback when the second button is clicked')
21. }
22. },
23. }),
24. })

26. build() {
27. Row() {
28. Stack() {
29. Column() {
30. Button("纯文本弹出框")
31. .width(96)
32. .height(40)
33. .onClick(() => {
34. this.dialogControllerConfirm.open()
35. })
36. }
37. .margin({ bottom: 300 })
38. }
39. .align(Alignment.Bottom)
40. .width('100%')
41. .height('100%')
42. }
43. .backgroundImageSize({ width: '100%', height: '100%' })
44. .height('100%')
45. }
46. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7f/v3/i89DpQOaR-yNiF35sbCI3A/zh-cn_image_0000002583440115.png?HW-CC-KV=V1&HW-CC-Date=20260428T000221Z&HW-CC-Expire=86400&HW-CC-Sign=770A7C74D3F101F6CD1B16675A1B7F32486C5F0A61E01EAECBA3812457EEED8F)

### 示例5（进度加载类弹出框）

进度加载类弹出框，包含content等内容。

```
1. import { LoadingDialog } from '@kit.ArkUI';

3. @Entry
4. @Component
5. struct Index {
6. dialogControllerProgress: CustomDialogController = new CustomDialogController({
7. builder: LoadingDialog({
8. content: '文本文本文本文本文本...',
9. }),
10. })

12. build() {
13. Row() {
14. Stack() {
15. Column() {
16. Button("进度加载类弹出框")
17. .width(96)
18. .height(40)
19. .onClick(() => {
20. this.dialogControllerProgress.open()
21. })
22. }
23. .margin({ bottom: 300 })
24. }
25. .align(Alignment.Bottom)
26. .width('100%')
27. .height('100%')
28. }
29. .backgroundImageSize({ width: '100%', height: '100%' })
30. .height('100%')
31. }
32. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/73/v3/zYzVE7eWSv2xxHuHzKjRBQ/zh-cn_image_0000002552960070.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000221Z&HW-CC-Expire=86400&HW-CC-Sign=F5CF2009388482A3420739D5B8D7315635CD9407A1275000A54BC2085F6D408C)

### 示例6（自定义主题风格弹出框）

自定义主题风格弹出框，包含content、theme等内容。

```
1. import { CustomColors, CustomTheme, LoadingDialog } from '@kit.ArkUI';

3. class CustomThemeImpl implements CustomTheme {
4. colors?: CustomColors;

6. constructor(colors: CustomColors) {
7. this.colors = colors;
8. }
9. }

11. // 自定义内容文字及loading组件主题颜色
12. class CustomThemeColors implements CustomColors {
13. fontPrimary = '#ffd0a300';
14. iconSecondary = '#ffd000cd';
15. }

17. @Entry
18. @Component
19. struct Index {
20. @State customTheme: CustomTheme = new CustomThemeImpl(new CustomThemeColors());
21. dialogController: CustomDialogController = new CustomDialogController({
22. builder: LoadingDialog({
23. content: 'text',
24. theme: this.customTheme,
25. })
26. });

28. build() {
29. Row() {
30. Stack() {
31. Column() {
32. Button('dialog')
33. .width(96)
34. .height(40)
35. .onClick(() => {
36. this.dialogController.open();
37. })
38. }
39. .margin({ bottom: 300 })
40. }
41. .align(Alignment.Bottom)
42. .width('100%')
43. .height('100%')
44. }
45. .backgroundImageSize({ width: '100%', height: '100%' })
46. .height('100%')
47. }
48. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/27/v3/4LD-vRq4TDW64JsW0rUYyQ/zh-cn_image_0000002583480071.png?HW-CC-KV=V1&HW-CC-Date=20260428T000221Z&HW-CC-Expire=86400&HW-CC-Sign=210A154EE3ADA500AE3E9FCBA8CC286FCE20A65ED2C3D2DE0695246BA343EE69)

### 示例7（自定义深浅色模式弹出框）

自定义深浅色模式弹出框，包含content、themeColorMode等内容。

```
1. import { LoadingDialog } from '@kit.ArkUI';

3. @Entry
4. @Component
5. struct Index {
6. dialogController: CustomDialogController = new CustomDialogController({
7. builder: LoadingDialog({
8. content: 'Text',
9. themeColorMode: ThemeColorMode.DARK, // 设置弹出框深浅色模式为深色模式
10. })
11. });

13. build() {
14. Row() {
15. Stack() {
16. Column() {
17. Button('Dialog')
18. .width(96)
19. .height(40)
20. .onClick(() => {
21. this.dialogController.open();
22. })
23. }
24. .margin({ bottom: 300 })
25. }
26. .align(Alignment.Bottom)
27. .width('100%')
28. .height('100%')
29. }
30. .backgroundImageSize({ width: '100%', height: '100%' })
31. .height('100%')
32. }
33. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5f/v3/NYYNIRkhSq-8pa6wBZDMzw/zh-cn_image_0000002552800422.png?HW-CC-KV=V1&HW-CC-Date=20260428T000221Z&HW-CC-Expire=86400&HW-CC-Sign=463A24D30BBCC46BC49159F2C7E8D01E92A60D1C94DCCD3377BE6EBFA5FD39CF)

### 示例8（自定义内容弹出框）

支持自定义内容弹出框，包含contentBuilder、buttons等内容。

```
1. import { CustomContentDialog } from '@kit.ArkUI';

3. @Entry
4. @Component
5. struct Index {
6. dialogController: CustomDialogController = new CustomDialogController({
7. builder: CustomContentDialog({
8. primaryTitle: '标题',
9. secondaryTitle: '辅助文本',
10. contentBuilder: () => {
11. this.buildContent();
12. },
13. buttons: [
14. {
15. value: '按钮1',
16. buttonStyle: ButtonStyleMode.TEXTUAL,
17. action: () => {
18. console.info('Callback when the button is clicked')
19. }
20. },
21. {
22. value: '按钮2',
23. buttonStyle: ButtonStyleMode.TEXTUAL,
24. role: ButtonRole.ERROR
25. }
26. ],
27. }),
28. });

30. build() {
31. Column() {
32. Button("支持自定义内容弹出框")
33. .onClick(() => {
34. this.dialogController.open()
35. })
36. }
37. .width('100%')
38. .height('100%')
39. .justifyContent(FlexAlign.Center)
40. }

42. // 自定义弹出框的内容区
43. @Builder
44. buildContent(): void {
45. Column() {
46. Text('内容区')
47. }
48. .width('100%')
49. }
50. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/48/v3/mjhbaa7tS1W6kMxPjpU-Hg/zh-cn_image_0000002583440117.png?HW-CC-KV=V1&HW-CC-Date=20260428T000221Z&HW-CC-Expire=86400&HW-CC-Sign=0B0626B31FB498B5D6755BF3A5D4E416323F8AAEB8EEEEB06A4DE1D3582C7FCE)

### 示例9（跟手弹出框）

从API version 14开始，该示例展示了设置跟手弹出框（警告弹出框为例），包含visible、popover、targetBuilder等内容。

```
1. import { AlertDialog, PopoverDialog, PopoverOptions } from '@kit.ArkUI';

3. @Entry
4. @Component
5. struct Index {
6. @State isShow: boolean = false;
7. @State popoverOptions: PopoverOptions = {
8. builder: () => {
9. this.dialogBuilder();
10. },
11. width: 320,
12. }

14. // 跟手弹出框内容
15. @Builder dialogBuilder() {
16. AlertDialog({
17. content: '跟手弹出框',
18. primaryButton: {
19. value: '取消',
20. action: () => {
21. this.isShow = false;
22. },
23. },
24. secondaryButton: {
25. value: '确认',
26. action: () => {
27. this.isShow = false;
28. },
29. },
30. });
31. }

33. // 跟手弹出框绑定的builder
34. @Builder buttonBuilder() {
35. Button('跟手弹出框目标组件')
36. .onClick(() => {
37. this.isShow = true;
38. });
39. }

41. build() {
42. Column() {
43. PopoverDialog({
44. visible: this.isShow,
45. popover: this.popoverOptions,
46. targetBuilder: () => {
47. this.buttonBuilder();
48. },
49. })
50. }
51. }
52. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dc/v3/ctLmJV3vQ42zt8GGhPSDNA/zh-cn_image_0000002552960072.png?HW-CC-KV=V1&HW-CC-Date=20260428T000221Z&HW-CC-Expire=86400&HW-CC-Sign=2296B04107F594F842431B65BDB4B9ED58FE9E45D5DF1619DF3E3780249DC90E)

### 示例10（弹出框按钮设置默认获焦）

从API version 18开始，该示例展示了设置默认获焦按钮弹出框（以AlertDialog为例），包含defaultFocus等内容。

```
1. import { AlertDialog } from '@kit.ArkUI';

3. @Entry
4. @Component
5. struct Index {
6. dialogController: CustomDialogController = new CustomDialogController({
7. builder: AlertDialog({
8. primaryTitle: 'AlertDialog',
9. secondaryTitle: '副标题',
10. content: '第二个按钮设置为默认',
11. primaryButton: {
12. value: 'DEFAULT',
13. action: () => {}
14. },
15. secondaryButton: {
16. value: 'TRUE',
17. defaultFocus: true, // 设置该按钮为默认获焦按钮。
18. action: () => {}
19. },
20. })
21. });

23. build() {
24. Row() {
25. Stack() {
26. Column() {
27. Button("AlertDialog")
28. .width(96)
29. .height(40)
30. .onClick(() => {
31. this.dialogController.open()
32. })
33. }
34. .margin({ bottom: 300 })
35. }
36. .align(Alignment.Bottom)
37. .width('100%')
38. .height('100%')
39. }
40. .backgroundImageSize({ width: '100%', height: '100%' })
41. .height('100%')
42. }
43. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9d/v3/YC7oXbSAQjeA1MIxAFFB_A/zh-cn_image_0000002583480073.png?HW-CC-KV=V1&HW-CC-Date=20260428T000221Z&HW-CC-Expire=86400&HW-CC-Sign=3FAE847AF37E0713B5F2972C007F0BC466774A3EEFF325D4E8075FA6A0DCDA8C)
