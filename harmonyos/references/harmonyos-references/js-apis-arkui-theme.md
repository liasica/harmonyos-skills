---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkui-theme
title: "@ohos.arkui.theme(主题换肤)"
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS API > UI界面 > @ohos.arkui.theme(主题换肤)
category: harmonyos-references
scraped_at: 2026-09-02T15:00:49+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:1ab089c83eca33a155f50a3204e3695a6954ecc6922bf3149e0e609b8de5cfef
---

支持自定义主题风格，实现App组件风格跟随Theme切换。

**说明** 

* 本模块首批接口从API version 12开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 本模块接口仅可在Stage模型下使用。

## 导入模块

```ts
import { Theme, ThemeControl, CustomColors, Colors, CustomTheme, CustomDarkColors } from '@kit.ArkUI';
```

## Theme

当前生效的主题风格对象，可从[onWillApplyTheme](ts-custom-component-lifecycle.md#onwillapplytheme12)中获取。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| colors | [Colors](js-apis-arkui-theme.md#colors) | 否 | 否 | 主题颜色资源。 |

## Colors

主题颜色资源。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**说明** 

颜色对应的组件可参考[文本色与图标色](../design-guides/color-0000001776857164.md#section137153164914)。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| brand | [ResourceColor](ts-types.md#resourcecolor) | 否 | 否 | 品牌色。当使用[ResourceColor](ts-types.md#resourcecolor)中非[Resource](ts-types.md#resource)类型设置该颜色时，backgroundEmphasize、compBackgroundEmphasize、compEmphasizeSecondary、compEmphasizeTertiary、interactiveFocus、interactiveSelect的缺省值会随映射关系发生变化，具体参考对应颜色属性说明。  **影响组件：** [TextInput](ts-basic-components-textinput.md)、[Search](ts-basic-components-search.md)。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| primary | [ResourceColor](ts-types.md#resourcecolor) | 否 | 是 | 主色。默认值undefined，代表不生效primary主题色。从API版本26.0.0开始，当使用[ResourceColor](ts-types.md#resourcecolor)中非[Resource](ts-types.md#resource)类型设置该颜色时，fontPrimary、fontSecondary、fontTertiary、fontFourth、iconPrimary、iconSecondary、iconTertiary、iconFourth的缺省值会随映射关系发生变化，具体参考对应颜色属性说明。  **影响组件：** 暂无组件使用。  **起始版本：** 26.0.0  **元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。 |
| onPrimary | [ResourceColor](ts-types.md#resourcecolor) | 否 | 是 | 主色反转颜色。默认值undefined，代表不生效onPrimary主题色。从API版本26.0.0开始，当使用[ResourceColor](ts-types.md#resourcecolor)中非[Resource](ts-types.md#resource)类型设置该颜色时，fontOnPrimary、fontOnSecondary、fontOnTertiary、fontOnFourth、iconOnPrimary、iconOnSecondary、iconOnTertiary、iconOnFourth的缺省值会随映射关系发生变化，具体参考对应颜色属性说明。  **影响组件：** 暂无组件使用。  **起始版本：** 26.0.0  **元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。 |
| container | [ResourceColor](ts-types.md#resourcecolor) | 否 | 是 | 容器色。默认值undefined，代表不生效container主题色。从API版本26.0.0开始，当使用[ResourceColor](ts-types.md#resourcecolor)中非[Resource](ts-types.md#resource)类型设置该颜色时，compBackgroundSecondary、compBackgroundTertiary、compDivider、interactiveHover、interactivePressed、interactiveClick的缺省值会随映射关系发生变化，具体参考对应颜色属性说明。  **影响组件：** 暂无组件使用。  **起始版本：** 26.0.0  **元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。 |
| warning | [ResourceColor](ts-types.md#resourcecolor) | 否 | 否 | 一级警示色。  **影响组件：** [TipsDialog](ohos-arkui-advanced-dialog.md#tipsdialog)、[AlertDialog](ohos-arkui-advanced-dialog.md#alertdialog)、[CustomContentDialog](ohos-arkui-advanced-dialog.md#customcontentdialog12)、  [Badge](ts-container-badge.md)、[Button](ts-basic-components-button.md)。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| alert | [ResourceColor](ts-types.md#resourcecolor) | 否 | 否 | 二级提示色。  **影响组件：** 暂无组件使用。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| confirm | [ResourceColor](ts-types.md#resourcecolor) | 否 | 否 | 确认色。  **影响组件：** 暂无组件使用。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| fontPrimary | [ResourceColor](ts-types.md#resourcecolor) | 否 | 否 | 一级文本字体颜色。  **说明：** 从API版本26.0.0开始，当作为[CustomColors](js-apis-arkui-theme.md#customcolors)的属性被使用时，若设置了primary，fontPrimary在浅色模式和深色模式下的缺省值均为primary的颜色值叠加90%透明度。  **影响组件：** [EditableTitleBar](ohos-arkui-advanced-editabletitlebar.md)、[LoadingDialog](ohos-arkui-advanced-dialog.md#loadingdialog)、[TipsDialog](ohos-arkui-advanced-dialog.md#tipsdialog)、  [ConfirmDialog](ohos-arkui-advanced-dialog.md#confirmdialog)、[AlertDialog](ohos-arkui-advanced-dialog.md#alertdialog)、[SelectDialog](ohos-arkui-advanced-dialog.md#selectdialog)、  [CustomContentDialog](ohos-arkui-advanced-dialog.md#customcontentdialog12)、[Swiper](ts-container-swiper.md)、[Text](ts-basic-components-text.md)、  [SubHeader](ohos-arkui-advanced-subheader.md)、[ProgressButton](ohos-arkui-advanced-progressbutton.md)、[AlphabetIndexer](ts-container-alphabet-indexer.md)、  [Popup](ohos-arkui-advanced-popup.md)、[Select](ts-basic-components-select.md)、[Chip](ohos-arkui-advanced-chip.md)、  [ToolBar](ohos-arkui-advanced-toolbar.md)、[Menu](ts-basic-components-menu.md)、[TextInput](ts-basic-components-textinput.md)、  [Search](ts-basic-components-search.md)、[TimePicker](ts-basic-components-timepicker.md)、[DatePicker](ts-basic-components-datepicker.md)、  [TextPicker](ts-basic-components-textpicker.md)、[ComposeListItem](ohos-arkui-advanced-composelistitem.md)、[TreeView](ohos-arkui-advanced-treeview.md)。从API版本26.0.0开始，新增[CalendarPicker](ts-basic-components-calendarpicker.md)、[UIPickerComponent](ts-container-ui-picker-component.md)、[RichEditor](ts-basic-components-richeditor.md)、[MenuItem](ts-basic-components-menuitem.md)、[MenuItemGroup](ts-basic-components-menuitemgroup.md)、[Counter](ts-container-counter.md)。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| fontSecondary | [ResourceColor](ts-types.md#resourcecolor) | 否 | 否 | 二级文本字体颜色。  **说明：** 从API版本26.0.0开始，当作为[CustomColors](js-apis-arkui-theme.md#customcolors)的属性被使用时，若设置了primary，fontSecondary在浅色模式和深色模式下的缺省值均为primary的颜色值叠加60%透明度。  **影响组件：** [EditableTitleBar](ohos-arkui-advanced-editabletitlebar.md)、[AlertDialog](ohos-arkui-advanced-dialog.md#alertdialog)、[CustomContentDialog](ohos-arkui-advanced-dialog.md#customcontentdialog12)、  [SubHeader](ohos-arkui-advanced-subheader.md)、[AlphabetIndexer](ts-container-alphabet-indexer.md)、[Popup](ohos-arkui-advanced-popup.md)、  [TextInput](ts-basic-components-textinput.md)、[Search](ts-basic-components-search.md)、[ComposeListItem](ohos-arkui-advanced-composelistitem.md)、  [TreeView](ohos-arkui-advanced-treeview.md)、[TextClock](ts-basic-components-textclock.md)。从API版本26.0.0开始，新增[MenuItem](ts-basic-components-menuitem.md)、[MenuItemGroup](ts-basic-components-menuitemgroup.md)。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| fontTertiary | [ResourceColor](ts-types.md#resourcecolor) | 否 | 否 | 三级文本字体颜色。  **说明：** 从API版本26.0.0开始，当作为[CustomColors](js-apis-arkui-theme.md#customcolors)的属性被使用时，若设置了primary，fontTertiary在浅色模式和深色模式下的缺省值均为primary的颜色值叠加40%透明度。  **影响组件：** [ComposeListItem](ohos-arkui-advanced-composelistitem.md)。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| fontFourth | [ResourceColor](ts-types.md#resourcecolor) | 否 | 否 | 四级文本字体颜色。  **说明：** 从API版本26.0.0开始，当作为[CustomColors](js-apis-arkui-theme.md#customcolors)的属性被使用时，若设置了primary，fontFourth在浅色模式和深色模式下的缺省值均为primary的颜色值叠加20%透明度。  **影响组件：** 暂无组件使用。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| fontEmphasize | [ResourceColor](ts-types.md#resourcecolor) | 否 | 否 | 高亮字体颜色。  **影响组件：** [TipsDialog](ohos-arkui-advanced-dialog.md#tipsdialog)、[ConfirmDialog](ohos-arkui-advanced-dialog.md#confirmdialog)、[AlertDialog](ohos-arkui-advanced-dialog.md#alertdialog)、  [SelectDialog](ohos-arkui-advanced-dialog.md#selectdialog)、[CustomContentDialog](ohos-arkui-advanced-dialog.md#customcontentdialog12)、[SubHeader](ohos-arkui-advanced-subheader.md)、  [AlphabetIndexer](ts-container-alphabet-indexer.md)、[Popup](ohos-arkui-advanced-popup.md)、[Button](ts-basic-components-button.md)、  [Select](ts-basic-components-select.md)、[ToolBar](ohos-arkui-advanced-toolbar.md)、[Search](ts-basic-components-search.md)、  [TimePicker](ts-basic-components-timepicker.md)、[DatePicker](ts-basic-components-datepicker.md)、[TextPicker](ts-basic-components-textpicker.md)。从API版本26.0.0开始，新增[RichEditor](ts-basic-components-richeditor.md)。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| fontOnPrimary | [ResourceColor](ts-types.md#resourcecolor) | 否 | 否 | 一级文本反转颜色，用于彩色背景。  **说明：** 从API版本26.0.0开始，当作为[CustomColors](js-apis-arkui-theme.md#customcolors)的属性被使用时，若设置了onPrimary，fontOnPrimary在浅色模式和深色模式下的缺省值均为onPrimary的颜色值叠加100%透明度。  **影响组件：** [Badge](ts-container-badge.md)、[Button](ts-basic-components-button.md)、[Chip](ohos-arkui-advanced-chip.md)。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| fontOnSecondary | [ResourceColor](ts-types.md#resourcecolor) | 否 | 否 | 二级文本反转颜色，用于彩色背景。  **说明：** 从API版本26.0.0开始，当作为[CustomColors](js-apis-arkui-theme.md#customcolors)的属性被使用时，若设置了onPrimary，fontOnSecondary在浅色模式和深色模式下的缺省值均为onPrimary的颜色值叠加60%透明度。  **影响组件：** 暂无组件使用。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| fontOnTertiary | [ResourceColor](ts-types.md#resourcecolor) | 否 | 否 | 三级文本反转颜色，用于彩色背景。  **说明：** 从API版本26.0.0开始，当作为[CustomColors](js-apis-arkui-theme.md#customcolors)的属性被使用时，若设置了onPrimary，fontOnTertiary在浅色模式和深色模式下的缺省值均为onPrimary的颜色值叠加40%透明度。  **影响组件：** 暂无组件使用。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| fontOnFourth | [ResourceColor](ts-types.md#resourcecolor) | 否 | 否 | 四级文本反转颜色，用于彩色背景。  **说明：** 从API版本26.0.0开始，当作为[CustomColors](js-apis-arkui-theme.md#customcolors)的属性被使用时，若设置了onPrimary，fontOnFourth在浅色模式和深色模式下的缺省值均为onPrimary的颜色值叠加20%透明度。  **影响组件：** 暂无组件使用。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| iconPrimary | [ResourceColor](ts-types.md#resourcecolor) | 否 | 否 | 一级图标颜色。  **说明：** 从API版本26.0.0开始，当作为[CustomColors](js-apis-arkui-theme.md#customcolors)的属性被使用时，若设置了primary，iconPrimary在浅色模式和深色模式下的缺省值均为primary的颜色值叠加90%透明度。  **影响组件：** [EditableTitleBar](ohos-arkui-advanced-editabletitlebar.md)、[Swiper](ts-container-swiper.md)、[ToolBar](ohos-arkui-advanced-toolbar.md)、  [TreeView](ohos-arkui-advanced-treeview.md)。从API版本26.0.0开始，新增[MenuItem](ts-basic-components-menuitem.md)。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| iconSecondary | [ResourceColor](ts-types.md#resourcecolor) | 否 | 否 | 二级图标颜色。  **说明：** 从API版本26.0.0开始，当作为[CustomColors](js-apis-arkui-theme.md#customcolors)的属性被使用时，若设置了primary，iconSecondary在浅色模式和深色模式下的缺省值均为primary的颜色值叠加60%透明度。  **影响组件：** [LoadingDialog](ohos-arkui-advanced-dialog.md#loadingdialog)、[SubHeader](ohos-arkui-advanced-subheader.md)、  [Popup](ohos-arkui-advanced-popup.md)、[Chip](ohos-arkui-advanced-chip.md)、[Search](ts-basic-components-search.md)、  [TreeView](ohos-arkui-advanced-treeview.md)。从API版本26.0.0开始，新增[LoadingProgress](ts-basic-components-loadingprogress.md)。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| iconTertiary | [ResourceColor](ts-types.md#resourcecolor) | 否 | 否 | 三级图标颜色。  **说明：** 从API版本26.0.0开始，当作为[CustomColors](js-apis-arkui-theme.md#customcolors)的属性被使用时，若设置了primary，iconTertiary在浅色模式和深色模式下的缺省值均为primary的颜色值叠加40%透明度。  **影响组件：** [SubHeader](ohos-arkui-advanced-subheader.md)。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| iconFourth | [ResourceColor](ts-types.md#resourcecolor) | 否 | 否 | 四级图标颜色。  **说明：** 从API版本26.0.0开始，当作为[CustomColors](js-apis-arkui-theme.md#customcolors)的属性被使用时，若设置了primary，iconFourth在浅色模式和深色模式下的缺省值均为primary的颜色值叠加20%透明度。  **影响组件：** [Checkbox](ts-basic-components-checkbox.md)、[CheckboxGroup](ts-basic-components-checkboxgroup.md)、[Radio](ts-basic-components-radio.md)。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| iconEmphasize | [ResourceColor](ts-types.md#resourcecolor) | 否 | 否 | 高亮图标颜色。  **影响组件：** [ToolBar](ohos-arkui-advanced-toolbar.md)。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| iconSubEmphasize | [ResourceColor](ts-types.md#resourcecolor) | 否 | 否 | 高亮辅助图标颜色。  **影响组件：** 暂无组件使用。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| iconOnPrimary | [ResourceColor](ts-types.md#resourcecolor) | 否 | 否 | 一级图标反转颜色，用于彩色背景。  **说明：** 从API版本26.0.0开始，当作为[CustomColors](js-apis-arkui-theme.md#customcolors)的属性被使用时，若设置了onPrimary，iconOnPrimary在浅色模式和深色模式下的缺省值均为onPrimary的颜色值叠加100%透明度。  **影响组件：** [Checkbox](ts-basic-components-checkbox.md)、[CheckboxGroup](ts-basic-components-checkboxgroup.md)、[Radio](ts-basic-components-radio.md)。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| iconOnSecondary | [ResourceColor](ts-types.md#resourcecolor) | 否 | 否 | 二级图标反转颜色，用于彩色背景。  **说明：** 从API版本26.0.0开始，当作为[CustomColors](js-apis-arkui-theme.md#customcolors)的属性被使用时，若设置了onPrimary，iconOnSecondary在浅色模式和深色模式下的缺省值均为onPrimary的颜色值叠加60%透明度。  **影响组件：** [Chip](ohos-arkui-advanced-chip.md)。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| iconOnTertiary | [ResourceColor](ts-types.md#resourcecolor) | 否 | 否 | 三级图标反转颜色，用于彩色背景。  **说明：** 从API版本26.0.0开始，当作为[CustomColors](js-apis-arkui-theme.md#customcolors)的属性被使用时，若设置了onPrimary，iconOnTertiary在浅色模式和深色模式下的缺省值均为onPrimary的颜色值叠加40%透明度。  **影响组件：** 暂无组件使用。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| iconOnFourth | [ResourceColor](ts-types.md#resourcecolor) | 否 | 否 | 四级图标反转颜色，用于彩色背景。  **说明：** 从API版本26.0.0开始，当作为[CustomColors](js-apis-arkui-theme.md#customcolors)的属性被使用时，若设置了onPrimary，iconOnFourth在浅色模式和深色模式下的缺省值均为onPrimary的颜色值叠加20%透明度。  **影响组件：** [ProgressButton](ohos-arkui-advanced-progressbutton.md)。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| backgroundPrimary | [ResourceColor](ts-types.md#resourcecolor) | 否 | 否 | 一级背景颜色（实色，不透明）。  **影响组件：** [TextInput](ts-basic-components-textinput.md)、[QRCode](ts-basic-components-qrcode.md)。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| backgroundSecondary | [ResourceColor](ts-types.md#resourcecolor) | 否 | 否 | 二级背景颜色（实色，不透明）。  **影响组件：** 暂无组件使用。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| backgroundTertiary | [ResourceColor](ts-types.md#resourcecolor) | 否 | 否 | 三级背景颜色（实色，不透明）。  **影响组件：** 暂无组件使用。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| backgroundFourth | [ResourceColor](ts-types.md#resourcecolor) | 否 | 否 | 四级背景颜色（实色，不透明）。  **影响组件：** 暂无组件使用。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| backgroundEmphasize | [ResourceColor](ts-types.md#resourcecolor) | 否 | 否 | 高亮背景颜色（实色，不透明）。  **说明：** 当作为[CustomColors](js-apis-arkui-theme.md#customcolors)的属性被使用时，若设置了brand，backgroundEmphasize在浅色模式和深色模式下的缺省值均为brand的颜色值叠加100%透明度。  **影响组件：** [Progress](ts-basic-components-progress.md)、[Button](ts-basic-components-button.md)、[Slider](ts-basic-components-slider.md)。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| compForegroundPrimary | [ResourceColor](ts-types.md#resourcecolor) | 否 | 否 | 前背景。  **影响组件：** [QRCode](ts-basic-components-qrcode.md)。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| compBackgroundPrimary | [ResourceColor](ts-types.md#resourcecolor) | 否 | 否 | 白色背景。  **影响组件：** 暂无组件使用。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| compBackgroundPrimaryTran | [ResourceColor](ts-types.md#resourcecolor) | 否 | 否 | 白色透明背景。  **影响组件：** 暂无组件使用。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| compBackgroundPrimaryContrary | [ResourceColor](ts-types.md#resourcecolor) | 否 | 否 | 常亮背景。  **影响组件：** [Toggle](ts-basic-components-toggle.md)、[Slider](ts-basic-components-slider.md)。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| compBackgroundGray | [ResourceColor](ts-types.md#resourcecolor) | 否 | 否 | 灰色背景。  **影响组件：** 暂无组件使用。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| compBackgroundSecondary | [ResourceColor](ts-types.md#resourcecolor) | 否 | 否 | 二级背景。  **说明：** 从API版本26.0.0开始，当作为[CustomColors](js-apis-arkui-theme.md#customcolors)的属性被使用时，若设置了container，compBackgroundSecondary在浅色模式和深色模式下的缺省值均为container的颜色值叠加10%透明度。  **影响组件：** [Swiper](ts-container-swiper.md)、[Slider](ts-basic-components-slider.md)。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| compBackgroundTertiary | [ResourceColor](ts-types.md#resourcecolor) | 否 | 否 | 三级背景。  **说明：** 从API版本26.0.0开始，当作为[CustomColors](js-apis-arkui-theme.md#customcolors)的属性被使用时，若设置了container，compBackgroundTertiary在浅色模式下的缺省值为container的颜色值叠加5%透明度，在深色模式下的缺省值为container的颜色值叠加10%透明度。  **影响组件：** [EditableTitleBar](ohos-arkui-advanced-editabletitlebar.md)、[Progress](ts-basic-components-progress.md)、[AlphabetIndexer](ts-container-alphabet-indexer.md)、  [Button](ts-basic-components-button.md)、[Select](ts-basic-components-select.md)、[Toggle](ts-basic-components-toggle.md)、  [Chip](ohos-arkui-advanced-chip.md)、[TextInput](ts-basic-components-textinput.md)、[Search](ts-basic-components-search.md)。从API版本26.0.0开始，新增[UIPickerComponent](ts-container-ui-picker-component.md)、[TextPicker](ts-basic-components-textpicker.md)。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| compBackgroundEmphasize | [ResourceColor](ts-types.md#resourcecolor) | 否 | 否 | 高亮背景。  **说明：** 从API版本26.0.0开始，当作为[CustomColors](js-apis-arkui-theme.md#customcolors)的属性被使用时，若设置了brand，compBackgroundEmphasize在浅色模式和深色模式下的缺省值均为brand的颜色值叠加100%透明度。  **影响组件：** [Swiper](ts-container-swiper.md)、[Toggle](ts-basic-components-toggle.md)、[Chip](ohos-arkui-advanced-chip.md)、  [Checkbox](ts-basic-components-checkbox.md)、[CheckboxGroup](ts-basic-components-checkboxgroup.md)、[Radio](ts-basic-components-radio.md)。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| compBackgroundNeutral | [ResourceColor](ts-types.md#resourcecolor) | 否 | 否 | 黑色中性高亮背景颜色。  **影响组件：** [PatternLock](ts-basic-components-patternlock.md)。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| compEmphasizeSecondary | [ResourceColor](ts-types.md#resourcecolor) | 否 | 否 | 20%高亮背景颜色。  **说明：** 当作为[CustomColors](js-apis-arkui-theme.md#customcolors)的属性被使用时，若设置了brand，compEmphasizeSecondary在浅色模式和深色模式下的缺省值均为brand的颜色值叠加20%透明度。  **影响组件：** [Progress](ts-basic-components-progress.md)、[ProgressButton](ohos-arkui-advanced-progressbutton.md)、[AlphabetIndexer](ts-container-alphabet-indexer.md)、  [Select](ts-basic-components-select.md)、[Toggle](ts-basic-components-toggle.md)。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| compEmphasizeTertiary | [ResourceColor](ts-types.md#resourcecolor) | 否 | 否 | 10%高亮背景颜色。  **说明：** 当作为[CustomColors](js-apis-arkui-theme.md#customcolors)的属性被使用时，若设置了brand，compEmphasizeTertiary在浅色模式和深色模式下的缺省值均为brand的颜色值叠加10%透明度。  **影响组件：** 暂无组件使用。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| compDivider | [ResourceColor](ts-types.md#resourcecolor) | 否 | 否 | 通用分割线颜色。  **说明：** 从API版本26.0.0开始，当作为[CustomColors](js-apis-arkui-theme.md#customcolors)的属性被使用时，若设置了container，compDivider在浅色模式和深色模式下的缺省值均为container的颜色值叠加20%透明度。  **影响组件：** [SelectDialog](ohos-arkui-advanced-dialog.md#selectdialog)、[PatternLock](ts-basic-components-patternlock.md)、[Divider](ts-basic-components-divider.md)。从API版本26.0.0开始，新增[UIPickerComponent](ts-container-ui-picker-component.md)、[TextPicker](ts-basic-components-textpicker.md)、[MenuItem](ts-basic-components-menuitem.md)、[MenuItemGroup](ts-basic-components-menuitemgroup.md)、[Select](ts-basic-components-select.md)。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| compCommonContrary | [ResourceColor](ts-types.md#resourcecolor) | 否 | 否 | 通用反转颜色。  **影响组件：** 暂无组件使用。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| compBackgroundFocus | [ResourceColor](ts-types.md#resourcecolor) | 否 | 否 | 获焦态背景颜色。  **影响组件：** 暂无组件使用。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| compFocusedPrimary | [ResourceColor](ts-types.md#resourcecolor) | 否 | 否 | 获焦态一级反转颜色。  **影响组件：** 暂无组件使用。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| compFocusedSecondary | [ResourceColor](ts-types.md#resourcecolor) | 否 | 否 | 获焦态二级反转颜色。  **影响组件：** 暂无组件使用。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| compFocusedTertiary | [ResourceColor](ts-types.md#resourcecolor) | 否 | 否 | 获焦态三级反转颜色。  **影响组件：** [Scroll](ts-container-scroll.md)。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| interactiveHover | [ResourceColor](ts-types.md#resourcecolor) | 否 | 否 | 通用悬停交互式颜色。  **说明：** 从API版本26.0.0开始，当作为[CustomColors](js-apis-arkui-theme.md#customcolors)的属性被使用时，若设置了container，interactiveHover在浅色模式下的缺省值为container的颜色值叠加5%透明度，在深色模式下的缺省值为container的颜色值叠加10%透明度。  **影响组件：** [EditableTitleBar](ohos-arkui-advanced-editabletitlebar.md)、[Chip](ohos-arkui-advanced-chip.md)、[TreeView](ohos-arkui-advanced-treeview.md)。从API版本26.0.0开始，新增[RichEditor](ts-basic-components-richeditor.md)、[MenuItem](ts-basic-components-menuitem.md)、[Select](ts-basic-components-select.md)。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| interactivePressed | [ResourceColor](ts-types.md#resourcecolor) | 否 | 否 | 通用按压交互式颜色。  **说明：** 从API版本26.0.0开始，当作为[CustomColors](js-apis-arkui-theme.md#customcolors)的属性被使用时，若设置了container，interactivePressed在浅色模式下的缺省值为container的颜色值叠加10%透明度，在深色模式下的缺省值为container的颜色值叠加15%透明度。  **影响组件：** [EditableTitleBar](ohos-arkui-advanced-editabletitlebar.md)、[Chip](ohos-arkui-advanced-chip.md)、[TreeView](ohos-arkui-advanced-treeview.md)。从API版本26.0.0开始，新增[RichEditor](ts-basic-components-richeditor.md)。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| interactiveFocus | [ResourceColor](ts-types.md#resourcecolor) | 否 | 否 | 通用获焦交互式颜色。  **说明：** 当作为[CustomColors](js-apis-arkui-theme.md#customcolors)的属性被使用时，若设置了brand，interactiveFocus在浅色模式和深色模式下的缺省值均为brand的颜色值叠加100%透明度。  **影响组件：** [EditableTitleBar](ohos-arkui-advanced-editabletitlebar.md)、[Chip](ohos-arkui-advanced-chip.md)、[TreeView](ohos-arkui-advanced-treeview.md)。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| interactiveActive | [ResourceColor](ts-types.md#resourcecolor) | 否 | 否 | 通用激活交互式颜色。  **影响组件：** [TreeView](ohos-arkui-advanced-treeview.md)。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| interactiveSelect | [ResourceColor](ts-types.md#resourcecolor) | 否 | 否 | 通用选择交互式颜色。  **说明：** 当作为[CustomColors](js-apis-arkui-theme.md#customcolors)的属性被使用时，若设置了brand，interactiveSelect在浅色模式和深色模式下的缺省值均为brand的颜色值叠加20%透明度。  **影响组件：** [TreeView](ohos-arkui-advanced-treeview.md)。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| interactiveClick | [ResourceColor](ts-types.md#resourcecolor) | 否 | 否 | 通用点击交互式颜色。  **说明：** 从API版本26.0.0开始，当作为[CustomColors](js-apis-arkui-theme.md#customcolors)的属性被使用时，若设置了container，interactiveClick在浅色模式下的缺省值为container的颜色值叠加10%透明度，在深色模式下的缺省值为container的颜色值叠加15%透明度。  **影响组件：** 从API版本26.0.0开始，新增[MenuItem](ts-basic-components-menuitem.md)、[Select](ts-basic-components-select.md)。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |

## CustomTheme

自定义主题风格对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| colors | [CustomColors](js-apis-arkui-theme.md#customcolors) | 否 | 是 | 自定义浅色主题颜色资源。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| darkColors20+ | [CustomDarkColors](js-apis-arkui-theme.md#customdarkcolors20) | 否 | 是 | 自定义深色主题颜色资源。  **说明**：如果未设置darkColors，颜色值将与浅色模式下的colors配置相同，并且不会随着颜色模式的变化而变化，除非该颜色是通过dark目录下的资源进行设置的。  **元服务API：** 从API version 20开始，该接口支持在元服务中使用。 |

## CustomColors

type CustomColors = Partial<Colors>

自定义主题颜色资源类型。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 说明 |
| --- | --- |
| Partial<[Colors](js-apis-arkui-theme.md#colors)> | 自定义主题颜色资源类型。 |

## CustomDarkColors20+

type CustomDarkColors = Partial<Colors>

自定义深色主题颜色资源类型。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 说明 |
| --- | --- |
| Partial<[Colors](js-apis-arkui-theme.md#colors)> | 自定义深色主题颜色资源类型。 |

## ThemeControl

ThemeControl将自定义Theme应用于App组件内，实现App组件风格跟随Theme切换。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

### setDefaultTheme

setDefaultTheme(theme: CustomTheme): void

将用户自定义Theme设置应用级默认主题，以实现应用风格跟随Theme切换。若在页面中使用此接口设置应用级默认主题，需确保该接口在页面build前执行。若在UIAbility中使用此接口设置应用级默认主题，需确保该接口在onWindowStageCreate阶段里windowStage.[loadContent](arkts-apis-window-windowstage.md#loadcontent9)接口调用完成的回调函数中执行。详细代码可参考[设置应用内组件自定义主题色](../harmonyos-guides/theme_skinning.md#设置应用内组件自定义主题色)。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| theme | [CustomTheme](js-apis-arkui-theme.md#customtheme) | 是 | 表示设置的自定义主题风格。 |

## 示例

### 示例1（使用setDefaultTheme）

该示例主要演示[ThemeControl](js-apis-arkui-theme.md#themecontrol).[setDefaultTheme](js-apis-arkui-theme.md#setdefaulttheme)的使用。

```ts
import { CustomTheme, CustomColors, ThemeControl } from '@kit.ArkUI';
// 自定义主题颜色
class BlueColors implements CustomColors {
  fontPrimary = "#FF707070";
  backgroundPrimary = "#FF2787D9";
  brand = "#FFEEAAFF"; // 品牌色
}

class PageCustomTheme implements CustomTheme {
  colors?: CustomColors;

  constructor(colors: CustomColors) {
    this.colors = colors;
  }
}
// 创建实例
const BlueColorsTheme = new PageCustomTheme(new BlueColors());
// 在页面build之前执行ThemeControl.setDefaultTheme，设置App默认样式风格为BlueColorsTheme。
ThemeControl.setDefaultTheme(BlueColorsTheme);

@Entry
@Component
struct Index {

  build() {
    Row() {
      Column() {
        // 文本颜色应用fontPrimary
        Text('这是一段文本')
          .fontSize(30)
          .fontWeight(FontWeight.Bold)
          .margin('5%')
        // 二维码背景色应用backgroundPrimary
        QRCode('Hello')
          .width(100)
          .height(100)
        // 输入框光标颜色应用brand
        TextInput({placeholder: 'input your word...'})
          .width('80%')
          .height(40)
          .margin(20)
      }
      .width('100%')
    }
    .height('100%')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d1/v3/4-RsoT-2Q6GfkuUkwsqMpA/zh-cn_image_0000002736434667.png)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/aa/v3/obGOI3-uSAKt6jV76eDRMA/zh-cn_image_0000002706835520.png)

### 示例2（设置组件主题色）

该示例主要演示使用[Colors](js-apis-arkui-theme.md#colors)中的brand、primary、onPrimary和container设置组件主题色。

从API版本26.0.0开始，Colors新增primary、onPrimary和container属性。

```ts
import { CustomColors } from '@kit.ArkUI';

class AppColors implements CustomColors {
  brand?: ResourceColor;
  primary?: ResourceColor;
  onPrimary?: ResourceColor;
  container?: ResourceColor;

  constructor(brand?: ResourceColor, primary?: ResourceColor, onPrimary?: ResourceColor, container?: ResourceColor) {
    this.brand = brand;
    this.primary = primary;
    this.onPrimary = onPrimary;
    this.container = container;
  }
}

@Entry({ routeName: "text" })
@Component
struct TextPage {
  @State appColors: AppColors = new AppColors(
    "#ff0000", "#0000ff", "#00ff00", "#ff00ff"
  );
  controller: TextClockController = new TextClockController();
  @State accumulateTime: number = 0;

  build() {
    WithTheme({
      theme: {
        colors: this.appColors
      }
    }) {
      Column({ space: 15 }) {
        Text('11:00:00')
          .fontWeight(FontWeight.Bold)
          .fontSize(30)

        TextClock({ timeZoneOffset: -8, controller: this.controller })
          .format('aa hh:mm:ss')
          .onDateChange((value: number) => {
            this.accumulateTime = value;
          })
          .margin(20)
          .fontSize(30)
          .fontWeight(FontWeight.Bold)
      }
      .width('100%')
      .margin({ top: 30 })
      .padding(16)
    }
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e/v3/9JYDrFkjQFSwcpx7AM8wbQ/zh-cn_image_0000002736314625.png)
