---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-dialogv2
title: DialogV2
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 系统预置UI组件库 > DialogV2
category: harmonyos-references
scraped_at: 2026-04-28T08:02:35+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:ed4d35ccebd24ccd680a88f45dc78447228962b7f9bfdd0716f41ebe7a09c43b
---

弹出框是一种模态窗口，通常用于在保持当前的上下文环境时，临时展示用户需关注的信息或待处理的操作，用户在模态弹出框内完成上述交互任务。模态弹出框需要用户进行交互才能够退出模态模式。

该组件基于[状态管理（V2）](../harmonyos-guides/arkts-state-management-overview.md#状态管理v2)实现，相较于[状态管理（V1）](../harmonyos-guides/arkts-state-management-overview.md#状态管理v1)，状态管理（V2）增强了对数据对象的深度观察与管理能力，不再局限于组件层级。借助状态管理（V2），开发者可以通过该组件更灵活地控制弹出框的数据和状态，实现更高效的用户界面刷新。

说明

* 该组件从API version 18开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。
* 该组件仅可在Stage模型下使用。
* 如果DialogV2设置[通用属性](ts-component-general-attributes.md)和[通用事件](ts-component-general-events.md)，编译工具链会额外生成节点\_\_Common\_\_，并将通用属性或通用事件挂载在\_\_Common\_\_上，而不是直接应用到DialogV2本身。这可能导致开发者设置的通用属性或通用事件不生效或不符合预期，因此，不建议DialogV2设置通用属性和通用事件。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { TipsDialogV2, SelectDialogV2, ConfirmDialogV2, AlertDialogV2, LoadingDialogV2, CustomContentDialogV2, PopoverDialogV2 } from '@kit.ArkUI';
```

## 子组件

PhonePC/2in1TabletTVWearable

无

## TipsDialogV2

PhonePC/2in1TabletTVWearable

TipsDialogV2({imageRes: ResourceStr | PixelMap, imageSize?: SizeOptions, imageBorderColor: ColorMetrics, imageBorderWidth: LengthMetrics, title?: ResourceStr, content?: ResourceStr, checkTips?: ResourceStr, checked?: boolean, onCheckedChange?: AdvancedDialogV2OnCheckedChange, primaryButton?: AdvancedDialogV2Button, secondaryButton?: AdvancedDialogV2Button})

提示弹出框，即为带图形确认弹出框，必要时可通过图形化方式展现确认弹出框。

**装饰器类型：**@ComponentV2

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 必填 | 装饰器类型 | 说明 |
| --- | --- | --- | --- | --- |
| imageRes | [ResourceStr](ts-types.md#resourcestr) | [PixelMap](arkts-apis-image-pixelmap.md) | 是 | @Param  @Require | 展示的图片。 |
| imageSize | [SizeOptions](ts-types.md#sizeoptions) | 否 | @Param | 自定义图片尺寸。  默认值：64\*64vp |
| imageBorderColor | [ColorMetrics](js-apis-arkui-graphics.md#colormetrics12) | 否 | @Param | 图片描边颜色。  默认值：Color.Black |
| imageBorderWidth | [LengthMetrics](js-apis-arkui-graphics.md#lengthmetrics12) | 否 | @Param | 图片描边宽度。  默认无描边效果。 |
| title | [ResourceStr](ts-types.md#resourcestr) | 否 | @Param | 提示弹出框标题。  默认不显示。  **说明：** 标题超过两行会显示“...”。 |
| content | [ResourceStr](ts-types.md#resourcestr) | 否 | @Param | 提示弹出框内容。  默认不显示。 |
| checkTips | [ResourceStr](ts-types.md#resourcestr) | 否 | @Param | 选择框的提示内容。  默认不显示。 |
| checked | boolean | 否 | @Param | checked为true时，表示选择框已选中。checked为false时，表示选择框未选中。  默认值：false |
| onCheckedChange | [AdvancedDialogV2OnCheckedChange](ohos-arkui-advanced-dialogv2.md#advanceddialogv2oncheckedchange) | 否 | @Param | 选择框的选中状态改变事件。  默认无事件。 |
| primaryButton | [AdvancedDialogV2Button](ohos-arkui-advanced-dialogv2.md#advanceddialogv2button) | 否 | @Param | 提示弹出框左侧按钮。  默认不显示。 |
| secondaryButton | [AdvancedDialogV2Button](ohos-arkui-advanced-dialogv2.md#advanceddialogv2button) | 否 | @Param | 提示弹出框右侧按钮。  默认不显示。 |

## AdvancedDialogV2OnCheckedChange

PhonePC/2in1TabletTVWearable

type AdvancedDialogV2OnCheckedChange = (checked: boolean) => void

选择框选中状态改变事件。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| checked | boolean | 是 | 表示选择框选中状态。  checked为true时，表示选择框已选中。checked为false时，表示选择框未选中。 |

## SelectDialogV2

PhonePC/2in1TabletTVWearable

SelectDialogV2({title: ResourceStr, content?: ResourceStr, selectedIndex?: number, confirm?: AdvancedDialogV2Button, radioContent: SheetInfo[]})

选择类弹出框，弹框中以列表或网格的形式提供可选的内容。

**装饰器类型：**@ComponentV2

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 必填 | 装饰器类型 | 说明 |
| --- | --- | --- | --- | --- |
| title | [ResourceStr](ts-types.md#resourcestr) | 是 | @Param  @Require | 选择弹出框标题。  **说明：** 标题超过两行会显示“...”。 |
| content | [ResourceStr](ts-types.md#resourcestr) | 否 | @Param | 选择弹出框内容。默认不显示。 |
| selectedIndex | number | 否 | @Param | 选择弹出框的选中项。  默认值：-1，没有选中项。若设置数值不在取值范围，按没有选中项处理。  取值范围：小于选择弹出框的子项内容列表长度。 |
| confirm | [AdvancedDialogV2Button](ohos-arkui-advanced-dialogv2.md#advanceddialogv2button) | 否 | @Param | 选择弹出框底部按钮。  默认不显示。 |
| radioContent | [SheetInfo](ts-methods-action-sheet.md#sheetinfo对象说明)[] | 是 | @Param  @Require | 选择弹出框的子项内容列表，每个选择项支持设置文本和选中的回调事件。 |

## ConfirmDialogV2

PhonePC/2in1TabletTVWearable

ConfirmDialogV2({title: ResourceStr, content?: ResourceStr, checkTips?: ResourceStr, checked?: boolean, onCheckedChange: AdvancedDialogV2OnCheckedChange, primaryButton?: AdvancedDialogV2Button, secondaryButton?: AdvancedDialogV2Button})

信息确认类弹出框，操作未正确执行（如网络错误、电池电量过低），或未正确操作时（如指纹录入），反馈的错误或提示信息。

**装饰器类型：**@ComponentV2

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 必填 | 装饰器类型 | 说明 |
| --- | --- | --- | --- | --- |
| title | [ResourceStr](ts-types.md#resourcestr) | 是 | @Param  @Require | 确认弹出框标题。  **说明：** 标题超过两行会显示“...”。 |
| content | [ResourceStr](ts-types.md#resourcestr) | 否 | @Param | 确认弹出框内容。  默认不显示。 |
| checkTips | [ResourceStr](ts-types.md#resourcestr) | 否 | @Param | checkbox的提示内容。  默认不显示。 |
| checked | boolean | 否 | @Param | checked为true时，表示checkbox已选中，为false时，表示未选中。  默认值：false |
| onCheckedChange | [AdvancedDialogV2OnCheckedChange](ohos-arkui-advanced-dialogv2.md#advanceddialogv2oncheckedchange) | 否 | @Param | checkbox的选中状态改变事件。  默认无事件。 |
| primaryButton | [AdvancedDialogV2Button](ohos-arkui-advanced-dialogv2.md#advanceddialogv2button) | 否 | @Param | 确认弹出框左侧按钮。  默认不显示。 |
| secondaryButton | [AdvancedDialogV2Button](ohos-arkui-advanced-dialogv2.md#advanceddialogv2button) | 否 | @Param | 确认弹出框右侧按钮。  默认不显示。 |

## AlertDialogV2

PhonePC/2in1TabletTVWearable

AlertDialogV2({primaryTitle?: ResourceStr, secondaryTitle?: ResourceStr, content: ResourceStr, primaryButton?: AdvancedDialogV2Button, secondaryButton?: AdvancedDialogV2Button})

操作确认类弹出框。当触发一个将产生严重后果的不可逆操作时，如删除、重置、取消编辑、停止等，会触发该类弹出框提示。

**装饰器类型：**@ComponentV2

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 必填 | 装饰器类型 | 说明 |
| --- | --- | --- | --- | --- |
| primaryTitle | [ResourceStr](ts-types.md#resourcestr) | 否 | @Param | 确认弹出框一级标题。  默认不显示。  **说明：** 标题超过两行会显示“...”。 |
| secondaryTitle | [ResourceStr](ts-types.md#resourcestr) | 否 | @Param | 确认弹出框二级标题。  默认不显示。  **说明：** 标题超过两行会显示“...”。 |
| content | [ResourceStr](ts-types.md#resourcestr) | 是 | @Param  @Require | 确认弹出框内容。 |
| primaryButton | [AdvancedDialogV2Button](ohos-arkui-advanced-dialogv2.md#advanceddialogv2button) | 否 | @Param | 确认弹出框左侧按钮。  默认不显示。 |
| secondaryButton | [AdvancedDialogV2Button](ohos-arkui-advanced-dialogv2.md#advanceddialogv2button) | 否 | @Param | 确认弹出框右侧按钮。  默认不显示。 |

## LoadingDialogV2

PhonePC/2in1TabletTVWearable

LoadingDialogV2({content?: ResourceStr})

进度加载类弹出框，操作正在执行时的提示信息。

**装饰器类型：**@ComponentV2

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 必填 | 装饰器类型 | 说明 |
| --- | --- | --- | --- | --- |
| content | [ResourceStr](ts-types.md#resourcestr) | 否 | @Param | 加载弹出框内容。  默认为空。  **说明：** 内容超过十行会显示“...”。 |

## CustomContentDialogV2

PhonePC/2in1TabletTVWearable

CustomContentDialogV2({contentBuilder: () => void, primaryTitle?: ResourceStr, secondaryTitle?: ResourceStr, contentAreaPadding?: LocalizedPadding, buttons?: AdvancedDialogV2Button[]})

自定义内容区弹出框，同时支持定义操作区按钮样式。

**装饰器类型：**@ComponentV2

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 必填 | 装饰器类型 | 说明 |
| --- | --- | --- | --- | --- |
| contentBuilder | [CustomBuilder](ts-types.md#custombuilder8) | 是 | @BuilderParam | 弹出框内容。 |
| primaryTitle | [ResourceStr](ts-types.md#resourcestr) | 否 | @Param | 弹出框标题。  默认不显示。  **说明：** 标题超过两行会显示“...”。 |
| secondaryTitle | [ResourceStr](ts-types.md#resourcestr) | 否 | @Param | 弹出框辅助文本。  默认不显示。  **说明：** 辅助文本超过两行会显示“...”。 |
| contentAreaPadding | [LocalizedPadding](ts-types.md#localizedpadding12) | 否 | @Param | 弹出框内容区内边距。  默认不显示。 |
| buttons | [AdvancedDialogV2Button](ohos-arkui-advanced-dialogv2.md#advanceddialogv2button)[] | 否 | @Param | 弹出框操作区按钮，最多支持4个按钮。  默认不显示。 |

## PopoverDialogV2OnVisibleChange

PhonePC/2in1TabletTVWearable

type PopoverDialogV2OnVisibleChange = (visible: boolean) => void

跟手弹出框显示状态改变事件。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| visible | boolean | 是 | 表示跟手弹出框显示状态。  值为true时跟手弹出框显示，为false时隐藏。 |

## PopoverDialogV2

PhonePC/2in1TabletTVWearable

PopoverDialogV2({visible: boolean, $visible: PopoverDialogV2OnVisibleChange, popover: PopoverDialogV2Options, targetBuilder: CustomBuilder})

跟手弹出框，基于目标组件位置弹出，上文中的TipsDialogV2、SelectDialogV2、ConfirmDialogV2、AlertDialogV2、LoadingDialogV2、CustomContentDialogV2都可作为弹出框内容。

**装饰器类型：**@ComponentV2

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 必填 | 装饰器类型 | 说明 |
| --- | --- | --- | --- | --- |
| visible | boolean | 是 | @Param  @Require | 跟手弹出框的显示状态。  值为true时跟手弹出框显示，为false时隐藏。 |
| $visible | [PopoverDialogV2OnVisibleChange](ohos-arkui-advanced-dialogv2.md#popoverdialogv2onvisiblechange) | 否 | @Event | 修改跟手弹出框的显示状态时触发的回调函数，建议在visible后使用!!语法设置双向同步。  默认无事件。 |
| popover | [PopoverDialogV2Options](ohos-arkui-advanced-dialogv2.md#popoverdialogv2options) | 是 | @Param  @Require | 配置跟手弹出框的参数。 |
| targetBuilder | [CustomBuilder](ts-types.md#custombuilder8) | 是 | @BuilderParam | 跟手弹出框基于的目标组件。 |

## PopoverDialogV2Options

PhonePC/2in1TabletTVWearable

跟手弹出框参数，用于设置弹出框内容、位置属性等。

继承自[CustomPopupOptions](ts-universal-attributes-popup.md#custompopupoptions8类型说明)。

说明

radius默认值为32vp。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## AdvancedDialogV2ButtonAction

PhonePC/2in1TabletTVWearable

type AdvancedDialogV2ButtonAction = () => void

弹出框操作区按钮的点击事件类型。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## AdvancedDialogV2Button

PhonePC/2in1TabletTVWearable

弹出框操作区按钮。

**装饰器类型：**@ObservedV2

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| content | [ResourceStr](ts-types.md#resourcestr) | 否 | 否 | 按钮的内容。  装饰器类型：@Trace |
| action | [AdvancedDialogV2ButtonAction](ohos-arkui-advanced-dialogv2.md#advanceddialogv2buttonaction) | 否 | 是 | 按钮的点击事件。  默认无事件。  装饰器类型：@Trace |
| background | [ColorMetrics](js-apis-arkui-graphics.md#colormetrics12) | 否 | 是 | 按钮的背景。  默认值跟随buttonStyle。  装饰器类型：@Trace |
| fontColor | [ColorMetrics](js-apis-arkui-graphics.md#colormetrics12) | 否 | 是 | 按钮的字体颜色。  默认值跟随buttonStyle。  装饰器类型：@Trace |
| buttonStyle | [ButtonStyleMode](ts-basic-components-button.md#buttonstylemode11枚举说明) | 否 | 是 | 按钮的样式。  默认值：2in1设备为ButtonStyleMode.NORMAL，其他设备为ButtonStyleMode.TEXTUAL。  装饰器类型：@Trace |
| role | [ButtonRole](ts-basic-components-button.md#buttonrole12枚举说明) | 否 | 是 | 按钮的角色。  默认值：ButtonRole.NORMAL  装饰器类型：@Trace |
| defaultFocus | boolean | 否 | 是 | 是否为默认焦点。  true：按钮是默认焦点。  false：按钮不是默认焦点。  默认值：false  装饰器类型：@Trace |
| enabled | boolean | 否 | 是 | 是否可用。  true：按钮可用。  false：按钮不可用。  默认值：true  装饰器类型：@Trace |

说明

buttonStyle和role优先级高于fontColor和background。如果buttonStyle和role设置的是默认值，那么fontColor和background可生效。

若同时给多个按钮设置defaultFocus，那么默认焦点为设置defaultFocus按钮显示顺序的第一个。

### constructor

PhonePC/2in1TabletTVWearable

constructor(options: AdvancedDialogV2ButtonOptions)

AdvancedDialogV2Button的构造函数。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [AdvancedDialogV2ButtonOptions](ohos-arkui-advanced-dialogv2.md#advanceddialogv2buttonoptions) | 是 | 按钮配置信息。 |

## AdvancedDialogV2ButtonOptions

PhonePC/2in1TabletTVWearable

用于初始化AdvancedDialogV2Button对象。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| content | [ResourceStr](ts-types.md#resourcestr) | 否 | 否 | 按钮的内容。 |
| action | [AdvancedDialogV2ButtonAction](ohos-arkui-advanced-dialogv2.md#advanceddialogv2buttonaction) | 否 | 是 | 按钮的点击事件。  默认无事件。 |
| background | [ColorMetrics](js-apis-arkui-graphics.md#colormetrics12) | 否 | 是 | 按钮的背景。  默认值跟随buttonStyle。 |
| fontColor | [ColorMetrics](js-apis-arkui-graphics.md#colormetrics12) | 否 | 是 | 按钮的字体颜色。  默认值跟随buttonStyle。 |
| buttonStyle | [ButtonStyleMode](ts-basic-components-button.md#buttonstylemode11枚举说明) | 否 | 是 | 按钮的样式。  默认值：2in1设备为ButtonStyleMode.NORMAL，其他设备为ButtonStyleMode.TEXTUAL。 |
| role | [ButtonRole](ts-basic-components-button.md#buttonrole12枚举说明) | 否 | 是 | 按钮的角色。  默认值：ButtonRole.NORMAL |
| defaultFocus | boolean | 否 | 是 | 是否为默认焦点。  true：按钮是默认焦点。  false：按钮不是默认焦点。  默认值：false |
| enabled | boolean | 否 | 是 | 是否可用。  true：按钮可用。  false：按钮不可用。  默认值：true |

## 示例

PhonePC/2in1TabletTVWearable

### 示例1（上图下文弹出框）

上图下文弹出框，包含imageRes、content等内容。

```
1. import { TipsDialogV2, AdvancedDialogV2Button, UIContext  } from '@kit.ArkUI';

3. @Entry
4. @ComponentV2
5. struct Index {
6. @Local checked: boolean = false;

8. @Builder
9. dialogBuilder(): void {
10. TipsDialogV2({
11. imageRes: $r('sys.media.ohos_ic_public_voice'),
12. content: '想要卸载这个APP嘛?',
13. title: 'TipsDialogV2',
14. checkTips: '不再提示',
15. checked: this.checked,
16. primaryButton: new AdvancedDialogV2Button({
17. content: '取消',
18. action: () => {
19. console.info('Callback when the first button is clicked');
20. },
21. }),
22. secondaryButton: new AdvancedDialogV2Button({
23. content: '删除',
24. role: ButtonRole.ERROR,
25. action: () => {
26. console.info('Callback when the second button is clicked');
27. }
28. }),
29. onCheckedChange: (checked: boolean) => {
30. console.info('Callback when the checkbox is clicked');
31. this.checked = checked;
32. }
33. })
34. }

36. build() {
37. Row() {
38. Stack() {
39. Column() {
40. Button("打开TipsDialogV2弹出框")
41. .width(96)
42. .height(40)
43. .onClick(() => {
44. let uiContext: UIContext = this.getUIContext();
45. uiContext.getPromptAction().openCustomDialog({
46. builder: () => {
47. this.dialogBuilder();
48. },
49. });
50. })
51. }.margin({ bottom: 300 })
52. }.align(Alignment.Bottom)
53. .width('100%').height('100%')
54. }
55. .backgroundImageSize({ width: '100%', height: '100%' })
56. .height('100%')
57. }
58. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1e/v3/f48ZAGG5RVuUZnb2FtphuA/zh-cn_image_0000002552960102.png?HW-CC-KV=V1&HW-CC-Date=20260428T000234Z&HW-CC-Expire=86400&HW-CC-Sign=8E36BAA84686375C9D8B190DCB74D26BA2327CF556069AE283908A058B21176E)

### 示例2（纯列表弹出框）

纯列表弹出框，包含selectedIndex、radioContent等内容。

```
1. import { SelectDialogV2, AdvancedDialogV2Button ,UIContext  } from '@kit.ArkUI';

3. @Entry
4. @ComponentV2
5. struct Index {
6. @Local radioIndex: number = 0;
7. @Builder
8. dialogBuilder(): void {
9. SelectDialogV2({
10. title: '文本标题',
11. selectedIndex: this.radioIndex,
12. confirm: new AdvancedDialogV2Button({
13. content: '取消',
14. action: () => {},
15. }),
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
36. })
37. }
38. build() {
39. Row() {
40. Stack() {
41. Column() {
42. Button("纯列表弹出框")
43. .width(96)
44. .height(40)
45. .onClick(() => {
46. let uiContext: UIContext = this.getUIContext();
47. uiContext.getPromptAction().openCustomDialog({
48. builder: () => {
49. this.dialogBuilder();
50. }
51. })
52. })
53. }.margin({ bottom: 300 })
54. }.align(Alignment.Bottom)
55. .width('100%').height('100%')
56. }
57. .backgroundImageSize({ width: '100%', height: '100%' })
58. .height('100%')
59. }
60. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/97/v3/uXJVIQYjT8aSRcmqiV1sbw/zh-cn_image_0000002583480069.png?HW-CC-KV=V1&HW-CC-Date=20260428T000234Z&HW-CC-Expire=86400&HW-CC-Sign=79053581511575A1A128905C16230765FB4BC6CAA99D8DF66595662340150562)

### 示例3（文本与勾选弹出框）

文本与勾选弹出框，包含content、checkTips等内容。

```
1. import { ConfirmDialogV2, AdvancedDialogV2Button, UIContext  } from '@kit.ArkUI';

3. @Entry
4. @ComponentV2
5. struct Index {
6. @Local checked: boolean = false;

8. @Builder
9. dialogBuilder(): void {
10. ConfirmDialogV2({
11. title: '文本标题',
12. content: '文本文本文本文本文本文本文本文本文本文本文本文本文本文本文本文本文本文本文本',
13. checked: this.checked,
14. checkTips: '禁止后不再提示',
15. primaryButton: new AdvancedDialogV2Button({
16. content: '禁止',
17. action: () => {
18. console.info('Callback when the primary button is clicked');
19. },
20. }),
21. secondaryButton: new AdvancedDialogV2Button({
22. content: '允许',
23. action: () => {
24. this.checked = false
25. console.info('Callback when the second button is clicked');
26. }
27. }),
28. onCheckedChange: (checked: boolean) => {
29. console.info('Callback when the checkbox is clicked');
30. this.checked = checked;
31. },
32. })
33. }

35. build() {
36. Row() {
37. Stack() {
38. Column() {
39. Button("打开ConfirmDialogV2弹出框")
40. .width(96)
41. .height(40)
42. .onClick(() => {
43. let uiContext: UIContext = this.getUIContext();
44. uiContext.getPromptAction().openCustomDialog({
45. builder: () => {
46. this.dialogBuilder();
47. },
48. alignment: DialogAlignment.Bottom
49. });
50. })
51. }.margin({ bottom: 300 })
52. }.align(Alignment.Bottom)
53. .width('100%').height('100%')
54. }
55. .backgroundImageSize({ width: '100%', height: '100%' })
56. .height('100%')
57. }
58. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/27/v3/Y7pkxjNbR9a3GPRgpTssZg/zh-cn_image_0000002552800420.png?HW-CC-KV=V1&HW-CC-Date=20260428T000234Z&HW-CC-Expire=86400&HW-CC-Sign=40CDA79F33F503D7E99ACAA2FDDB5784D24800A005C1CB06FE26CD87F5AFB434)

### 示例4（纯文本弹出框）

纯文本弹出框，包含primaryTitle、secondaryTitle、content等内容。

```
1. import { AlertDialogV2, AdvancedDialogV2Button, UIContext  } from '@kit.ArkUI';

3. @Entry
4. @ComponentV2
5. struct Index {
6. @Builder
7. dialogBuilder(): void {
8. AlertDialogV2({
9. primaryTitle: '弹框一级标题',
10. secondaryTitle: '弹框二级标题',
11. content: '文本文本文本文本文本',
12. primaryButton: new AdvancedDialogV2Button({
13. content: '取消',
14. action: () => {
15. console.info('Callback when the primary button is clicked');
16. },
17. }),
18. secondaryButton: new AdvancedDialogV2Button({
19. content: '确认',
20. role: ButtonRole.ERROR,
21. action: () => {
22. console.info('Callback when the second button is clicked');
23. }
24. }),
25. })
26. }

28. build() {
29. Row() {
30. Stack() {
31. Column() {
32. Button("打开AlertDialogV2弹出框")
33. .width(96)
34. .height(40)
35. .onClick(() => {
36. let uiContext: UIContext = this.getUIContext();
37. uiContext.getPromptAction().openCustomDialog({
38. builder: () => {
39. this.dialogBuilder();
40. }
41. });
42. })
43. }.margin({ bottom: 300 })
44. }.align(Alignment.Bottom)
45. .width('100%').height('100%')
46. }
47. .backgroundImageSize({ width: '100%', height: '100%' })
48. .height('100%')
49. }
50. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9/v3/1UfcINVHRu6qfJsVQSl61Q/zh-cn_image_0000002583440115.png?HW-CC-KV=V1&HW-CC-Date=20260428T000234Z&HW-CC-Expire=86400&HW-CC-Sign=935D98898C5CFE22CE32F720532C7B28B440CCA5915CA892D7E57CE3EED31484)

### 示例5（进度加载类弹出框）

进度加载类弹出框，包含content等内容。

```
1. import { LoadingDialogV2, UIContext  } from '@kit.ArkUI';

3. @Entry
4. @ComponentV2
5. struct Index {
6. @Builder
7. dialogBuilder(): void {
8. LoadingDialogV2({
9. content: '文本文本文本文本文本...',
10. })
11. }

13. build() {
14. Row() {
15. Stack() {
16. Column() {
17. Button("打开LoadingDialogV2弹出框")
18. .width(96)
19. .height(40)
20. .onClick(() => {
21. let uiContext: UIContext = this.getUIContext();
22. uiContext.getPromptAction().openCustomDialog({
23. builder: () => {
24. this.dialogBuilder();
25. }
26. });
27. })
28. }.margin({ bottom: 300 })
29. }.align(Alignment.Bottom)
30. .width('100%').height('100%')
31. }
32. .backgroundImageSize({ width: '100%', height: '100%' })
33. .height('100%')
34. }
35. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/Zywvu-EgS1yy4ez_8k_y8w/zh-cn_image_0000002552960070.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000234Z&HW-CC-Expire=86400&HW-CC-Sign=92F9580C271CFBBB7A2868D73B21DE970EFC8391236091CA95E3A514172E002F)

### 示例6（自定义主题风格弹出框）

自定义主题风格弹出框，包含content、theme等内容。

```
1. import { CustomColors, CustomTheme, LoadingDialogV2, UIContext  } from '@kit.ArkUI';

3. class CustomThemeImpl implements CustomTheme {
4. colors?: CustomColors;

6. constructor(colors: CustomColors) {
7. this.colors = colors;
8. }
9. }

11. class CustomThemeColors implements CustomColors {
12. fontPrimary = '#ffd0a300';
13. iconSecondary = '#ffd000cd';
14. }

16. @Entry
17. @ComponentV2
18. struct Index {
19. @Builder
20. dialogBuilder(): void {
21. WithTheme({ theme: new CustomThemeImpl(new CustomThemeColors()) }) {
22. LoadingDialogV2({
23. content: '文本文本文本文本文本...',
24. })
25. }
26. }

28. build() {
29. Row() {
30. Stack() {
31. Column() {
32. Button("打开LoadingDialogV2弹出框")
33. .width(96)
34. .height(40)
35. .onClick(() => {
36. let uiContext: UIContext = this.getUIContext();
37. uiContext.getPromptAction().openCustomDialog({
38. builder: () => {
39. this.dialogBuilder();
40. }
41. });
42. })
43. }.margin({ bottom: 300 })
44. }.align(Alignment.Bottom)
45. .width('100%').height('100%')
46. }
47. .backgroundImageSize({ width: '100%', height: '100%' })
48. .height('100%')
49. }
50. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/83/v3/hJp4R9b3Q2ebunZ0Cgfk2A/zh-cn_image_0000002583480103.png?HW-CC-KV=V1&HW-CC-Date=20260428T000234Z&HW-CC-Expire=86400&HW-CC-Sign=726C8D1905FD726AF7C88D0686791ACE8F95A83C64465EEC1199E89E963C64D4)

### 示例7（自定义内容弹出框）

支持自定义内容弹出框，包含contentBuilder、buttons等内容。

```
1. import { CustomContentDialogV2, AdvancedDialogV2Button, UIContext  } from '@kit.ArkUI';

3. @Entry
4. @ComponentV2
5. struct Index {
6. @Builder
7. dialogBuilder(): void {
8. CustomContentDialogV2({
9. primaryTitle: '标题',
10. secondaryTitle: '辅助文本',
11. contentBuilder: () => {
12. this.buildContent();
13. },
14. buttons: [
15. new AdvancedDialogV2Button({
16. content: '按钮1', buttonStyle: ButtonStyleMode.TEXTUAL,
17. action: () => {
18. console.info('Callback when the button is clicked');
19. }
20. }),
21. new AdvancedDialogV2Button({
22. content: '按钮2', buttonStyle: ButtonStyleMode.TEXTUAL, role: ButtonRole.ERROR,
23. })
24. ],
25. })
26. }

28. build() {
29. Column() {
30. Button("打开CustomContentDialogV2弹出框")
31. .onClick(() => {
32. let uiContext: UIContext = this.getUIContext();
33. uiContext.getPromptAction().openCustomDialog({
34. builder: () => {
35. this.dialogBuilder();
36. }
37. })
38. })
39. }
40. .width('100%')
41. .height('100%')
42. .justifyContent(FlexAlign.Center)
43. }

45. @Builder
46. buildContent(): void {
47. Column() {
48. Text('内容区')
49. }
50. }
51. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d2/v3/tzE-iZLEQgC22dgOFEQQEA/zh-cn_image_0000002552800454.png?HW-CC-KV=V1&HW-CC-Date=20260428T000234Z&HW-CC-Expire=86400&HW-CC-Sign=08313E81D36924FFB03BF5AB7BF770F0BA0515203BC7CCAD38F2A0894BBBD862)

### 示例8（跟手弹出框）

跟手弹出框（警告弹出框为例），包含visible、popover、targetBuilder等内容。

```
1. import { AlertDialogV2, PopoverDialogV2, PopoverDialogV2Options, AdvancedDialogV2Button} from '@kit.ArkUI';

3. @Entry
4. @ComponentV2
5. struct Index {
6. @Local isShow: boolean = false;
7. @Local popoverOptions: PopoverDialogV2Options = {
8. builder: () => {
9. this.dialogBuilder();
10. }
11. }

13. @Builder dialogBuilder() {
14. AlertDialogV2({
15. content: '跟手弹出框',
16. primaryButton: new AdvancedDialogV2Button({
17. content: '取消',
18. action: () => {
19. this.isShow = false;
20. },
21. }),
22. secondaryButton: new AdvancedDialogV2Button({
23. content: '确认',
24. action: () => {
25. this.isShow = false;
26. },
27. }),
28. });
29. }

31. @Builder buttonBuilder() {
32. Button('跟手弹出框目标组件').onClick(() => {
33. this.isShow = true;
34. });
35. }

37. build() {
38. Column() {
39. PopoverDialogV2({
40. visible: this.isShow!!,
41. popover: this.popoverOptions,
42. targetBuilder: () => {
43. this.buttonBuilder();
44. },
45. })
46. }
47. }
48. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e0/v3/nWQKNB8jRSe8hnb2DAuxjw/zh-cn_image_0000002583440149.png?HW-CC-KV=V1&HW-CC-Date=20260428T000234Z&HW-CC-Expire=86400&HW-CC-Sign=37325B5CC70B7AFA24314EE76027A901DFE40D33ABD8C87B77EA4F00CD2E9E30)
