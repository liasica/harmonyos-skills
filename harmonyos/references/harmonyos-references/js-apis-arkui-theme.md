---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkui-theme
title: @ohos.arkui.theme(主题换肤)
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS API > UI界面 > @ohos.arkui.theme(主题换肤)
category: harmonyos-references
scraped_at: 2026-04-28T08:00:19+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:45c1e968f1fe851145e2c1a5537ee172dd63f6ab5b3f92253410d6aa5b4dca42
---

支持自定义主题风格，实现App组件风格跟随Theme切换。

说明

本模块首批接口从API version 12开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { Theme, ThemeControl, CustomColors, Colors, CustomTheme, CustomDarkColors } from '@kit.ArkUI';
```

## Theme

PhonePC/2in1TabletTVWearable

当前生效的主题风格对象，可从[onWillApplyTheme](ts-custom-component-lifecycle.md#onwillapplytheme12)中获取。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| colors | [Colors](js-apis-arkui-theme.md#colors) | 否 | 否 | 主题颜色资源。 |

## Colors

PhonePC/2in1TabletTVWearable

主题颜色资源。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

说明

颜色对应的组件可参考[文本色与图标色](../design-guides/color-0000001776857164.md#section137153164914)。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| brand | [ResourceColor](ts-types.md#resourcecolor) | 否 | 否 | 品牌色。  **影响组件：** [TextInput](ts-basic-components-textinput.md)、[Search](ts-basic-components-search.md) |
| warning | [ResourceColor](ts-types.md#resourcecolor) | 否 | 否 | 一级警示色。  **影响组件：** [TipsDialog](ohos-arkui-advanced-dialog.md#tipsdialog)、[AlertDialog](ohos-arkui-advanced-dialog.md#alertdialog)、[CustomContentDialog](ohos-arkui-advanced-dialog.md#customcontentdialog12)、  [Badge](ts-container-badge.md)、[Button](ts-basic-components-button.md) |
| alert | [ResourceColor](ts-types.md#resourcecolor) | 否 | 否 | 二级提示色。  **影响组件：** 暂无组件使用。 |
| confirm | [ResourceColor](ts-types.md#resourcecolor) | 否 | 否 | 确认色。  **影响组件：** 暂无组件使用。 |
| fontPrimary | [ResourceColor](ts-types.md#resourcecolor) | 否 | 否 | 一级文本字体颜色。  **影响组件：** [EditableTitleBar](ohos-arkui-advanced-editabletitlebar.md)、[LoadingDialog](ohos-arkui-advanced-dialog.md#loadingdialog)、[TipsDialog](ohos-arkui-advanced-dialog.md#tipsdialog)、  [ConfirmDialog](ohos-arkui-advanced-dialog.md#confirmdialog)、[AlertDialog](ohos-arkui-advanced-dialog.md#alertdialog)、[SelectDialog](ohos-arkui-advanced-dialog.md#selectdialog)、  [CustomContentDialog](ohos-arkui-advanced-dialog.md#customcontentdialog12)、[Swiper](ts-container-swiper.md)、[Text](ts-basic-components-text.md)、  [SubHeader](ohos-arkui-advanced-subheader.md)、[ProgressButton](ohos-arkui-advanced-progressbutton.md)、[AlphabetIndexer](ts-container-alphabet-indexer.md)、  [Popup](ohos-arkui-advanced-popup.md)、[Select](ts-basic-components-select.md)、[Chip](ohos-arkui-advanced-chip.md)、  [ToolBar](ohos-arkui-advanced-toolbar.md)、[Menu](ts-basic-components-menu.md)、[TextInput](ts-basic-components-textinput.md)、  [Search](ts-basic-components-search.md)、[Counter](ts-container-counter.md)、[TimePicker](ts-basic-components-timepicker.md)、[DatePicker](ts-basic-components-datepicker.md)、  [TextPicker](ts-basic-components-textpicker.md)、[ComposeListItem](ohos-arkui-advanced-composelistitem.md)、[TreeView](ohos-arkui-advanced-treeview.md) |
| fontSecondary | [ResourceColor](ts-types.md#resourcecolor) | 否 | 否 | 二级文本字体颜色。  **影响组件：** [EditableTitleBar](ohos-arkui-advanced-editabletitlebar.md)、[AlertDialog](ohos-arkui-advanced-dialog.md#alertdialog)、[CustomContentDialog](ohos-arkui-advanced-dialog.md#customcontentdialog12)、  [SubHeader](ohos-arkui-advanced-subheader.md)、[AlphabetIndexer](ts-container-alphabet-indexer.md)、[Popup](ohos-arkui-advanced-popup.md)、  [TextInput](ts-basic-components-textinput.md)、[Search](ts-basic-components-search.md)、[ComposeListItem](ohos-arkui-advanced-composelistitem.md)、  [TreeView](ohos-arkui-advanced-treeview.md) |
| fontTertiary | [ResourceColor](ts-types.md#resourcecolor) | 否 | 否 | 三级文本字体颜色。  **影响组件：** [ComposeListItem](ohos-arkui-advanced-composelistitem.md) |
| fontFourth | [ResourceColor](ts-types.md#resourcecolor) | 否 | 否 | 四级文本字体颜色。  **影响组件：** 暂无组件使用。 |
| fontEmphasize | [ResourceColor](ts-types.md#resourcecolor) | 否 | 否 | 高亮字体颜色。  **影响组件：** [TipsDialog](ohos-arkui-advanced-dialog.md#tipsdialog)、[ConfirmDialog](ohos-arkui-advanced-dialog.md#confirmdialog)、[AlertDialog](ohos-arkui-advanced-dialog.md#alertdialog)、  [SelectDialog](ohos-arkui-advanced-dialog.md#selectdialog)、[CustomContentDialog](ohos-arkui-advanced-dialog.md#customcontentdialog12)、[SubHeader](ohos-arkui-advanced-subheader.md)、  [AlphabetIndexer](ts-container-alphabet-indexer.md)、[Popup](ohos-arkui-advanced-popup.md)、[Button](ts-basic-components-button.md)、  [Select](ts-basic-components-select.md)、[ToolBar](ohos-arkui-advanced-toolbar.md)、[Search](ts-basic-components-search.md)、  [TimePicker](ts-basic-components-timepicker.md)、[DatePicker](ts-basic-components-datepicker.md)、[TextPicker](ts-basic-components-textpicker.md) |
| fontOnPrimary | [ResourceColor](ts-types.md#resourcecolor) | 否 | 否 | 一级文本反转颜色，用于彩色背景。  **影响组件：** [Badge](ts-container-badge.md)、[Button](ts-basic-components-button.md)、[Chip](ohos-arkui-advanced-chip.md) |
| fontOnSecondary | [ResourceColor](ts-types.md#resourcecolor) | 否 | 否 | 二级文本反转颜色，用于彩色背景。  **影响组件：** 暂无组件使用。 |
| fontOnTertiary | [ResourceColor](ts-types.md#resourcecolor) | 否 | 否 | 三级文本反转颜色，用于彩色背景。  **影响组件：** 暂无组件使用。 |
| fontOnFourth | [ResourceColor](ts-types.md#resourcecolor) | 否 | 否 | 四级文本反转颜色，用于彩色背景。  **影响组件：** 暂无组件使用。 |
| iconPrimary | [ResourceColor](ts-types.md#resourcecolor) | 否 | 否 | 一级图标颜色。  **影响组件：** [EditableTitleBar](ohos-arkui-advanced-editabletitlebar.md)、[Swiper](ts-container-swiper.md)、[ToolBar](ohos-arkui-advanced-toolbar.md)、  [TreeView](ohos-arkui-advanced-treeview.md) |
| iconSecondary | [ResourceColor](ts-types.md#resourcecolor) | 否 | 否 | 二级图标颜色。  **影响组件：** [LoadingDialog](ohos-arkui-advanced-dialog.md#loadingdialog)、[SubHeader](ohos-arkui-advanced-subheader.md)、[LoadingProgress](ts-basic-components-loadingprogress.md)、  [Popup](ohos-arkui-advanced-popup.md)、[Chip](ohos-arkui-advanced-chip.md)、[Search](ts-basic-components-search.md)、  [TreeView](ohos-arkui-advanced-treeview.md) |
| iconTertiary | [ResourceColor](ts-types.md#resourcecolor) | 否 | 否 | 三级图标颜色。  **影响组件：** [SubHeader](ohos-arkui-advanced-subheader.md) |
| iconFourth | [ResourceColor](ts-types.md#resourcecolor) | 否 | 否 | 四级图标颜色。  **影响组件：** [Checkbox](ts-basic-components-checkbox.md)、[CheckboxGroup](ts-basic-components-checkboxgroup.md)、[Radio](ts-basic-components-radio.md) |
| iconEmphasize | [ResourceColor](ts-types.md#resourcecolor) | 否 | 否 | 高亮图标颜色。  **影响组件：** [ToolBar](ohos-arkui-advanced-toolbar.md) |
| iconSubEmphasize | [ResourceColor](ts-types.md#resourcecolor) | 否 | 否 | 高亮辅助图标颜色。  **影响组件：** 暂无组件使用。 |
| iconOnPrimary | [ResourceColor](ts-types.md#resourcecolor) | 否 | 否 | 一级图标反转颜色，用于彩色背景。  **影响组件：** [Checkbox](ts-basic-components-checkbox.md)、[CheckboxGroup](ts-basic-components-checkboxgroup.md)、[Radio](ts-basic-components-radio.md) |
| iconOnSecondary | [ResourceColor](ts-types.md#resourcecolor) | 否 | 否 | 二级图标反转颜色，用于彩色背景。  **影响组件：** [Chip](ohos-arkui-advanced-chip.md) |
| iconOnTertiary | [ResourceColor](ts-types.md#resourcecolor) | 否 | 否 | 三级图标反转颜色，用于彩色背景。  **影响组件：** 暂无组件使用。 |
| iconOnFourth | [ResourceColor](ts-types.md#resourcecolor) | 否 | 否 | 四级图标反转颜色，用于彩色背景。  **影响组件：** [ProgressButton](ohos-arkui-advanced-progressbutton.md) |
| backgroundPrimary | [ResourceColor](ts-types.md#resourcecolor) | 否 | 否 | 一级背景颜色（实色，不透明）。  **影响组件：** [TextInput](ts-basic-components-textinput.md)、[QRCode](ts-basic-components-qrcode.md) |
| backgroundSecondary | [ResourceColor](ts-types.md#resourcecolor) | 否 | 否 | 二级背景颜色（实色，不透明）。  **影响组件：** 暂无组件使用。 |
| backgroundTertiary | [ResourceColor](ts-types.md#resourcecolor) | 否 | 否 | 三级背景颜色（实色，不透明）。  **影响组件：** 暂无组件使用。 |
| backgroundFourth | [ResourceColor](ts-types.md#resourcecolor) | 否 | 否 | 四级背景颜色（实色，不透明）。  **影响组件：** 暂无组件使用。 |
| backgroundEmphasize | [ResourceColor](ts-types.md#resourcecolor) | 否 | 否 | 高亮背景颜色（实色，不透明）。  **影响组件：** [Progress](ts-basic-components-progress.md)、[Button](ts-basic-components-button.md)、[Slider](ts-basic-components-slider.md) |
| compForegroundPrimary | [ResourceColor](ts-types.md#resourcecolor) | 否 | 否 | 前背景。  **影响组件：** [QRCode](ts-basic-components-qrcode.md) |
| compBackgroundPrimary | [ResourceColor](ts-types.md#resourcecolor) | 否 | 否 | 白色背景。  **影响组件：** 暂无组件使用。 |
| compBackgroundPrimaryTran | [ResourceColor](ts-types.md#resourcecolor) | 否 | 否 | 白色透明背景。  **影响组件：** 暂无组件使用。 |
| compBackgroundPrimaryContrary | [ResourceColor](ts-types.md#resourcecolor) | 否 | 否 | 常亮背景。  **影响组件：** [Toggle](ts-basic-components-toggle.md)、[Slider](ts-basic-components-slider.md) |
| compBackgroundGray | [ResourceColor](ts-types.md#resourcecolor) | 否 | 否 | 灰色背景。  **影响组件：** 暂无组件使用。 |
| compBackgroundSecondary | [ResourceColor](ts-types.md#resourcecolor) | 否 | 否 | 二级背景。  **影响组件：** [Swiper](ts-container-swiper.md)、[Slider](ts-basic-components-slider.md) |
| compBackgroundTertiary | [ResourceColor](ts-types.md#resourcecolor) | 否 | 否 | 三级背景。  **影响组件：** [EditableTitleBar](ohos-arkui-advanced-editabletitlebar.md)、[Progress](ts-basic-components-progress.md)、[AlphabetIndexer](ts-container-alphabet-indexer.md)、  [Button](ts-basic-components-button.md)、[Select](ts-basic-components-select.md)、[Toggle](ts-basic-components-toggle.md)、  [Chip](ohos-arkui-advanced-chip.md)、[TextInput](ts-basic-components-textinput.md)、[Search](ts-basic-components-search.md) |
| compBackgroundEmphasize | [ResourceColor](ts-types.md#resourcecolor) | 否 | 否 | 高亮背景。  **影响组件：** [Swiper](ts-container-swiper.md)、[Toggle](ts-basic-components-toggle.md)、[Chip](ohos-arkui-advanced-chip.md)、  [Checkbox](ts-basic-components-checkbox.md)、[CheckboxGroup](ts-basic-components-checkboxgroup.md)、[Radio](ts-basic-components-radio.md) |
| compBackgroundNeutral | [ResourceColor](ts-types.md#resourcecolor) | 否 | 否 | 黑色中性高亮背景颜色。  **影响组件：** [PatternLock](ts-basic-components-patternlock.md) |
| compEmphasizeSecondary | [ResourceColor](ts-types.md#resourcecolor) | 否 | 否 | 20%高亮背景颜色。  **影响组件：** [Progress](ts-basic-components-progress.md)、[ProgressButton](ohos-arkui-advanced-progressbutton.md)、[AlphabetIndexer](ts-container-alphabet-indexer.md)、  [Select](ts-basic-components-select.md)、[Toggle](ts-basic-components-toggle.md) |
| compEmphasizeTertiary | [ResourceColor](ts-types.md#resourcecolor) | 否 | 否 | 10%高亮背景颜色。  **影响组件：** 暂无组件使用。 |
| compDivider | [ResourceColor](ts-types.md#resourcecolor) | 否 | 否 | 通用分割线颜色。  **影响组件：** [SelectDialog](ohos-arkui-advanced-dialog.md#selectdialog)、[PatternLock](ts-basic-components-patternlock.md)、[Divider](ts-basic-components-divider.md) |
| compCommonContrary | [ResourceColor](ts-types.md#resourcecolor) | 否 | 否 | 通用反转颜色。  **影响组件：** 暂无组件使用。 |
| compBackgroundFocus | [ResourceColor](ts-types.md#resourcecolor) | 否 | 否 | 获焦态背景颜色。  **影响组件：** 暂无组件使用。 |
| compFocusedPrimary | [ResourceColor](ts-types.md#resourcecolor) | 否 | 否 | 获焦态一级反转颜色。  **影响组件：** 暂无组件使用。 |
| compFocusedSecondary | [ResourceColor](ts-types.md#resourcecolor) | 否 | 否 | 获焦态二级反转颜色。  **影响组件：** 暂无组件使用。 |
| compFocusedTertiary | [ResourceColor](ts-types.md#resourcecolor) | 否 | 否 | 获焦态三级反转颜色。  **影响组件：** [Scroll](ts-container-scroll.md) |
| interactiveHover | [ResourceColor](ts-types.md#resourcecolor) | 否 | 否 | 通用悬停交互式颜色。  **影响组件：** [EditableTitleBar](ohos-arkui-advanced-editabletitlebar.md)、[Chip](ohos-arkui-advanced-chip.md)、[TreeView](ohos-arkui-advanced-treeview.md) |
| interactivePressed | [ResourceColor](ts-types.md#resourcecolor) | 否 | 否 | 通用按压交互式颜色。  **影响组件：** [EditableTitleBar](ohos-arkui-advanced-editabletitlebar.md)、[Chip](ohos-arkui-advanced-chip.md)、[TreeView](ohos-arkui-advanced-treeview.md) |
| interactiveFocus | [ResourceColor](ts-types.md#resourcecolor) | 否 | 否 | 通用获焦交互式颜色。  **影响组件：** [EditableTitleBar](ohos-arkui-advanced-editabletitlebar.md)、[Chip](ohos-arkui-advanced-chip.md)、[TreeView](ohos-arkui-advanced-treeview.md) |
| interactiveActive | [ResourceColor](ts-types.md#resourcecolor) | 否 | 否 | 通用激活交互式颜色。  **影响组件：** [TreeView](ohos-arkui-advanced-treeview.md) |
| interactiveSelect | [ResourceColor](ts-types.md#resourcecolor) | 否 | 否 | 通用选择交互式颜色。  **影响组件：** [TreeView](ohos-arkui-advanced-treeview.md) |
| interactiveClick | [ResourceColor](ts-types.md#resourcecolor) | 否 | 否 | 通用点击交互式颜色。  **影响组件：** 暂无组件使用。 |

## CustomTheme

PhonePC/2in1TabletTVWearable

自定义主题风格对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| colors | [CustomColors](js-apis-arkui-theme.md#customcolors) | 否 | 是 | 自定义浅色主题颜色资源。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| darkColors20+ | [CustomDarkColors](js-apis-arkui-theme.md#customdarkcolors20) | 否 | 是 | 自定义深色主题颜色资源。  **说明**：如果未设置darkColors，颜色值将与浅色模式下的colors配置相同，并且不会随着颜色模式的变化而变化，除非该颜色是通过dark目录下的资源进行设置的。  **元服务API：** 从API version 20开始，该接口支持在元服务中使用。 |

## CustomColors

PhonePC/2in1TabletTVWearable

type CustomColors = Partial<Colors>

自定义主题颜色资源类型。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 说明 |
| --- | --- |
| Partial<[Colors](js-apis-arkui-theme.md#colors)> | 自定义主题颜色资源类型。 |

## CustomDarkColors20+

PhonePC/2in1TabletTVWearable

type CustomDarkColors = Partial<Colors>

自定义深色主题颜色资源类型。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 说明 |
| --- | --- |
| Partial<[Colors](js-apis-arkui-theme.md#colors)> | 自定义深色主题颜色资源类型。 |

## ThemeControl

PhonePC/2in1TabletTVWearable

ThemeControl将自定义Theme应用于App组件内，实现App组件风格跟随Theme切换。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

### setDefaultTheme

PhonePC/2in1TabletTVWearable

setDefaultTheme(theme: [CustomTheme](js-apis-arkui-theme.md#customtheme)): void

将用户自定义Theme设置应用级默认主题，以实现应用风格跟随Theme切换。若在页面中使用此接口设置应用级默认主题，需确保该接口在页面build前执行。若在UIAbility中使用此接口设置应用级默认主题，需确保该接口在onWindowStageCreate阶段里windowStage.[loadContent](arkts-apis-window-windowstage.md#loadcontent9)接口调用完成的回调函数中执行。详细代码可参考[设置应用内组件自定义主题色](../harmonyos-guides/theme_skinning.md#设置应用内组件自定义主题色)。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| theme | [CustomTheme](js-apis-arkui-theme.md#customtheme) | 是 | 表示设置的自定义主题风格。 |

**示例**

```
1. import { CustomTheme, CustomColors, ThemeControl } from '@kit.ArkUI';
2. // 自定义主题颜色
3. class BlueColors implements CustomColors {
4. fontPrimary = "#FF707070";
5. backgroundPrimary = "#FF2787D9";
6. brand = "#FFEEAAFF"; // 品牌色
7. }

9. class PageCustomTheme implements CustomTheme {
10. colors?: CustomColors;

12. constructor(colors: CustomColors) {
13. this.colors = colors;
14. }
15. }
16. // 创建实例
17. const BlueColorsTheme = new PageCustomTheme(new BlueColors());
18. // 在页面build之前执行ThemeControl.setDefaultTheme，设置App默认样式风格为BlueColorsTheme。
19. ThemeControl.setDefaultTheme(BlueColorsTheme);

21. @Entry
22. @Component
23. struct Index {

25. build() {
26. Row() {
27. Column() {
28. // 文本颜色应用fontPrimary
29. Text('这是一段文本')
30. .fontSize(30)
31. .fontWeight(FontWeight.Bold)
32. .margin('5%')
33. // 二维码背景色应用backgroundPrimary
34. QRCode('Hello')
35. .width(100)
36. .height(100)
37. // 输入框光标颜色应用brand
38. TextInput({placeholder: 'input your word...'})
39. .width('80%')
40. .height(40)
41. .margin(20)
42. }
43. .width('100%')
44. }
45. .height('100%')
46. }
47. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b/v3/Wrd4S6LyTwCrP68mOcg94Q/zh-cn_image_0000002583479405.png?HW-CC-KV=V1&HW-CC-Date=20260428T000018Z&HW-CC-Expire=86400&HW-CC-Sign=01C76362CCE4DDF47967CD8CD8DED069EE98303C7887348639B2AF6C16D4D07F)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/57/v3/eerkMjXxS_yg9sZ0UYR_Qw/zh-cn_image_0000002552799756.png?HW-CC-KV=V1&HW-CC-Date=20260428T000018Z&HW-CC-Expire=86400&HW-CC-Sign=CBD5D89BE3CDCFBA2C732A5D64BA3F199ECECE8ACCE2D54800284B46869A88FC)
