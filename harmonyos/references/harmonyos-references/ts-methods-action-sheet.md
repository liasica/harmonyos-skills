---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-methods-action-sheet
title: 列表选择弹窗 (ActionSheet)
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 弹窗 > 列表选择弹窗 (ActionSheet)
category: harmonyos-references
scraped_at: 2026-04-29T13:52:44+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:de24000881e4ad152726a103964b5fac90a432e4a9241bbf29d3d8781bfe05d3
---

列表弹窗。

说明

从API version 8开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

本模块功能依赖UI的执行上下文，不可在[UI上下文不明确](../harmonyos-guides/arkts-global-interface.md#ui上下文不明确)的地方使用，参见[UIContext](arkts-apis-uicontext-uicontext.md)说明。

## ActionSheetOptions对象说明

PhonePC/2in1TabletTVWearable

列表选择弹窗的样式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| title | string | [Resource](ts-types.md#resource) | 否 | 否 | 弹窗标题。  当文本内容过长无法显示时，用省略号代替未显示的部分。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| subtitle10+ | [ResourceStr](ts-types.md#resourcestr) | 否 | 是 | 弹窗副标题。  当文本内容过长无法显示时，用省略号代替未显示的部分。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| message | string | [Resource](ts-types.md#resource) | 否 | 否 | 弹窗内容。  文本超长时会触发滚动条。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| autoCancel | boolean | 否 | 是 | 点击遮障层时，是否关闭弹窗。  默认值：true  值为true时，点击遮障层关闭弹窗，值为false时，点击遮障层不关闭弹窗。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| confirm | [ActionSheetButtonOptions](ts-methods-action-sheet.md#actionsheetbuttonoptions18对象说明) | 否 | 是 | 确认Button的使能状态、默认焦点、按钮风格、文本内容和点击回调。在弹窗获焦且未进行tab键走焦时，该按钮默认响应Enter键。多重弹窗情况下，可自动获焦并连续响应。默认响应Enter键能力在defaultFocus为true时不生效。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| cancel | [VoidCallback](ts-types.md#voidcallback12) | 否 | 是 | 点击遮障层关闭dialog时的回调。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| alignment | [DialogAlignment](ts-methods-alert-dialog-box.md#dialogalignment枚举说明) | 否 | 是 | 弹窗在竖直方向上的对齐方式。  默认值：DialogAlignment.Bottom  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。  **说明：**  若在UIExtension中设置showInSubWindow为true，弹窗将基于UIExtension的宿主窗口对齐。 |
| offset | [ActionSheetOffset](ts-methods-action-sheet.md#actionsheetoffset18对象说明) | 否 | 是 | 弹窗相对alignment所在位置的偏移量。  默认值：  1.alignment设置为Top、TopStart、TopEnd时默认值为{dx: 0,dy: "40vp"}  2.alignment设置为其他时默认值为{dx: 0,dy: "-40vp"}  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| sheets | Array<[SheetInfo](ts-methods-action-sheet.md#sheetinfo对象说明)> | 否 | 否 | 设置选项内容，每个选择项支持设置图片、文本和选中的回调。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| maskRect10+ | [Rectangle](ts-methods-alert-dialog-box.md#rectangle8类型说明) | 否 | 是 | 弹窗遮蔽层区域，在遮蔽层区域内的事件不透传，在遮蔽层区域外的事件透传。  默认值：{ x: 0, y: 0, width: '100%', height: '100%' }  **说明：**  showInSubWindow为true时，maskRect不生效。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| showInSubWindow11+ | boolean | 否 | 是 | 某弹窗需要显示在主窗口之外时，是否在子窗口显示此弹窗。值为true表示在子窗口显示弹窗。  默认值：false，弹窗显示在应用内，而非独立子窗口。  **说明：**  showInSubWindow为true的弹窗无法触发显示另一个showInSubWindow为true的弹窗。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| isModal11+ | boolean | 否 | 是 | 弹窗是否为模态窗口，模态窗口有蒙层，非模态窗口无蒙层。值为false时，弹窗为非模态窗口，无蒙层。  默认值：true，此时弹窗有蒙层。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| backgroundColor11+ | [ResourceColor](ts-types.md#resourcecolor) | 否 | 是 | 弹窗背板颜色。  默认值：Color.Transparent  **说明：**  backgroundColor会与模糊属性backgroundBlurStyle叠加产生效果，如果不符合预期，可将backgroundBlurStyle设置为BlurStyle.NONE，即可取消模糊。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| backgroundBlurStyle11+ | [BlurStyle](ts-universal-attributes-background.md#blurstyle9) | 否 | 是 | 弹窗背板模糊材质。  默认值：BlurStyle.COMPONENT\_ULTRA\_THICK  **说明：**  设置为BlurStyle.NONE即可关闭背景虚化。当设置了backgroundBlurStyle为非NONE值时，则不要设置backgroundColor，否则颜色显示将不符合预期效果。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| backgroundBlurStyleOptions19+ | [BackgroundBlurStyleOptions](ts-universal-attributes-background.md#backgroundblurstyleoptions10对象说明) | 否 | 是 | 背景模糊效果。默认值请参考BackgroundBlurStyleOptions类型说明。  **元服务API：** 从API version 19开始，该接口支持在元服务中使用。 |
| backgroundEffect19+ | [BackgroundEffectOptions](ts-universal-attributes-background.md#backgroundeffectoptions11) | 否 | 是 | 背景效果参数。默认值请参考BackgroundEffectOptions类型说明。  **元服务API：** 从API version 19开始，该接口支持在元服务中使用。 |
| onWillDismiss12+ | Callback<[DismissDialogAction](ts-methods-action-sheet.md#dismissdialogaction12)> | 否 | 是 | 交互式关闭回调函数。  **说明：**  1.当用户执行点击遮障层关闭、侧滑（左滑/右滑）、三键back、键盘ESC关闭交互操作时，如果注册该回调函数，则不会立刻关闭弹窗。在回调函数中可以通过reason得到阻拦关闭弹窗的操作类型，从而根据原因选择是否能关闭弹窗。当前组件返回的reason中，暂不支持CLOSE\_BUTTON的枚举值。  2.在onWillDismiss回调中，不能再做onWillDismiss拦截。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| cornerRadius12+ | [Dimension](ts-types.md#dimension10) | [BorderRadiuses](ts-types.md#borderradiuses9) | [LocalizedBorderRadiuses](ts-types.md#localizedborderradiuses12) | 否 | 是 | 设置背板的圆角半径。  可分别设置4个圆角的半径。  默认值：{ topLeft: '32vp', topRight: '32vp', bottomLeft: '32vp', bottomRight: '32vp' }  圆角大小受组件尺寸限制，最大值为组件宽或高的一半，若值为负，则按照默认值处理。  百分比参数方式：以父元素弹窗宽和高的百分比来设置弹窗的圆角。  **说明：**  当cornerRadius属性类型为LocalizedBorderRadiuses时，支持随语言习惯改变布局顺序。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| borderWidth12+ | [Dimension](ts-types.md#dimension10) | [EdgeWidths](ts-types.md#edgewidths9) | [LocalizedEdgeWidths](ts-types.md#localizededgewidths12) | 否 | 是 | 设置弹窗背板的边框宽度。  可分别设置4个边框宽度。  默认值：0  百分比参数方式：以父元素弹窗宽的百分比来设置弹窗的边框宽度。  当弹窗左边框和右边框大于弹窗宽度，弹窗上边框和下边框大于弹窗高度，显示可能不符合预期。  **说明：**  当borderWidth属性类型为LocalizedEdgeWidths时，支持随语言习惯改变布局顺序。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| borderColor12+ | [ResourceColor](ts-types.md#resourcecolor) | [EdgeColors](ts-types.md#edgecolors9) | [LocalizedEdgeColors](ts-types.md#localizededgecolors12) | 否 | 是 | 设置弹窗背板的边框颜色。  默认值：Color.Black  如果使用borderColor属性，需要和borderWidth属性一起使用。  **说明：**  当borderColor属性类型为LocalizedEdgeColors时，支持随语言习惯改变布局顺序。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| borderStyle12+ | [BorderStyle](ts-appendix-enums.md#borderstyle) | [EdgeStyles](ts-types.md#edgestyles9) | 否 | 是 | 设置弹窗背板的边框样式。  默认值：BorderStyle.Solid。  如果使用borderStyle属性，需要和borderWidth属性一起使用。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| width12+ | [Dimension](ts-types.md#dimension10) | 否 | 是 | 设置弹窗背板的宽度。  **说明：**  - 弹窗宽度默认最大值：400vp。  - 百分比参数方式：弹窗参考宽度为所在窗口的宽度，在此基础上调小或调大。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| height12+ | [Dimension](ts-types.md#dimension10) | 否 | 是 | 设置弹窗背板的高度。  **说明：**  - 弹窗高度默认最大值：0.9 \*（窗口高度 - 安全区域）。  - 百分比参数方式：弹窗参考高度为（窗口高度 - 安全区域），在此基础上调小或调大。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| shadow12+ | [ShadowOptions](ts-universal-attributes-image-effect.md#shadowoptions对象说明) | [ShadowStyle](ts-universal-attributes-image-effect.md#shadowstyle10枚举说明) | 否 | 是 | 设置弹窗背板的阴影。  当设备为2in1时，默认场景下获焦阴影值为ShadowStyle.OUTER\_FLOATING\_MD，失焦为ShadowStyle.OUTER\_FLOATING\_SM。其他设备默认无阴影。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| transition12+ | [TransitionEffect](ts-transition-animation-component.md#transitioneffect10对象说明) | 否 | 是 | 设置弹窗显示和退出的过渡效果。  **说明：**  1.如果不设置，则使用默认的显示/退出动效。  2.显示动效中按back键，打断显示动效，执行退出动效，动画效果为显示动效与退出动效的曲线叠加后的效果。  3.退出动效中按back键，不会打断退出动效，退出动效继续执行，继续按back键退出应用。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| enableHoverMode14+ | boolean | 否 | 是 | 是否响应悬停态，值为true表示响应悬停态。  默认值：false，默认不响应。  **说明：**  PC/2in1设备弹窗默认显示在上半屏，在enableHoverMode设置为true时，可以通过设置hoverModeArea参数显示在下半屏。其他设备弹窗在enableHoverMode设置为true时默认显示在下半屏，可以通过设置hoverModeArea参数显示在上半屏。  **元服务API：** 从API version 14开始，该接口支持在元服务中使用。 |
| hoverModeArea14+ | [HoverModeAreaType](ts-universal-attributes-sheet-transition.md#hovermodeareatype14) | 否 | 是 | 悬停态下弹窗默认展示区域。  默认值：HoverModeAreaType.BOTTOM\_SCREEN。  **元服务API：** 从API version 14开始，该接口支持在元服务中使用。 |
| onWillAppear19+ | Callback<void> | 否 | 是 | 弹窗显示动效前的事件回调。  **说明：**  1.正常时序依次为：onWillAppear >> onDidAppear >> onWillDisappear >> onDidDisappear。  2.在onWillAppear内设置改变弹窗显示效果的回调事件，二次弹出生效。  **元服务API：** 从API version 19开始，该接口支持在元服务中使用。 |
| onDidAppear19+ | Callback<void> | 否 | 是 | 弹窗弹出后的事件回调。  **说明：**  1.正常时序依次为：onWillAppear >> onDidAppear >> onWillDisappear >> onDidDisappear。  2.在onDidAppear内设置改变弹窗显示效果的回调事件，二次弹出生效。  3.快速点击弹出，关闭弹窗时，onWillDisappear在onDidAppear前生效。  4.弹窗入场动效未完成时彻底关闭弹窗，动效打断，onDidAppear不会触发。  **元服务API：** 从API version 19开始，该接口支持在元服务中使用。 |
| onWillDisappear19+ | Callback<void> | 否 | 是 | 弹窗退出动效前的事件回调。  **说明：**  正常时序依次为：onWillAppear >> onDidAppear >> onWillDisappear >> onDidDisappear。  **元服务API：** 从API version 19开始，该接口支持在元服务中使用。 |
| onDidDisappear19+ | Callback<void> | 否 | 是 | 弹窗消失后的事件回调。  **说明：**  正常时序依次为：onWillAppear >> onDidAppear >> onWillDisappear >> onDidDisappear。  **元服务API：** 从API version 19开始，该接口支持在元服务中使用。 |
| levelMode15+ | [LevelMode](ts-methods-action-sheet.md#levelmode15) | 否 | 是 | 设置弹窗显示层级。  **说明：**  - 默认值：LevelMode.OVERLAY  - 仅当showInSubWindow属性设置为false时生效。  **元服务API：** 从API version 15开始，该接口支持在元服务中使用。 |
| levelUniqueId15+ | number | 否 | 是 | 设置页面级弹窗需要显示的层级下的[节点UniqueID](js-apis-arkui-framenode.md#getuniqueid12)。  取值范围：大于等于0的数字。  **说明：**  - 当且仅当levelMode属性设置为LevelMode.EMBEDDED时生效。  **元服务API：** 从API version 15开始，该接口支持在元服务中使用。 |
| immersiveMode15+ | [ImmersiveMode](ts-methods-action-sheet.md#immersivemode15) | 否 | 是 | 设置页面内弹窗蒙层效果。  **说明：**  - 默认值：ImmersiveMode.DEFAULT  - 当且仅当levelMode属性设置为LevelMode.EMBEDDED时生效。  **元服务API：** 从API version 15开始，该接口支持在元服务中使用。 |
| levelOrder18+ | [LevelOrder](js-apis-promptaction.md#levelorder18) | 否 | 是 | 设置弹窗显示的顺序。  **说明：**  - 默认值：LevelOrder.clamp(0)  - 不支持动态刷新顺序。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |

## SheetInfo对象说明

PhonePC/2in1TabletTVWearable

弹窗中的选项内容，每一项支持设置文本、图标以及选中的回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| title | string | [Resource](ts-types.md#resource) | 否 | 否 | 选项的文本内容。  文本超长时会触发滚动条。 |
| icon | string | [Resource](ts-types.md#resource) | 否 | 是 | 选项的图标，默认无图标显示。  string格式可用于加载网络图片和本地图片，常用于加载网络图片。当使用相对路径引用本地图片时，例如Image("common/test.jpg")。 |
| action | [VoidCallback](ts-types.md#voidcallback12) | 否 | 否 | 选项选中的回调。 |

## LevelMode15+

PhonePC/2in1TabletTVWearable

type LevelMode = LevelMode

弹窗的显示层级。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 说明 |
| --- | --- |
| [LevelMode](js-apis-promptaction.md#levelmode15枚举说明) | 设置弹窗的显示层级。 |

## ImmersiveMode15+

PhonePC/2in1TabletTVWearable

type ImmersiveMode = ImmersiveMode

弹窗的蒙层效果。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 说明 |
| --- | --- |
| [ImmersiveMode](js-apis-promptaction.md#immersivemode15枚举说明) | 设置页面内弹窗的蒙层效果。 |

## DismissDialogAction12+

PhonePC/2in1TabletTVWearable

Dialog关闭的信息。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

### 属性

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| dismiss | Callback<void> | 否 | 否 | Dialog关闭回调函数。开发者需要退出时调用，不需要退出时无需调用。 |
| reason | [DismissReason](ts-universal-attributes-popup.md#dismissreason12枚举说明) | 否 | 否 | Dialog无法关闭原因。根据开发者需求选择不同操作下，Dialog是否关闭。 |

## ActionSheetButtonOptions18+对象说明

PhonePC/2in1TabletTVWearable

弹窗中按钮的样式。

说明

为规范匿名对象的定义，API 18版本修改了此处的元素定义。其中，保留了历史匿名对象的起始版本信息，会出现外层元素@since版本号高于内层元素版本号的情况，但这不影响接口的使用。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| enabled10+ | boolean | 否 | 是 | 点击Button是否响应，true表示Button可以响应，false表示Button不可以响应。  默认值：true  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| defaultFocus10+ | boolean | 否 | 是 | 设置Button是否是默认焦点，true表示Button是默认焦点，false表示Button不是默认焦点。  默认值：false  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| style10+ | [DialogButtonStyle](ts-appendix-enums.md#dialogbuttonstyle10) | 否 | 是 | 设置Button的风格样式。  默认值：DialogButtonStyle.DEFAULT  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| value8+ | string | [Resource](ts-types.md#resource) | 否 | 否 | Button文本内容。  当文本内容过长无法显示时，用省略号代替未显示的部分。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| action8+ | [VoidCallback](ts-types.md#voidcallback12) | 否 | 否 | Button选中时的回调。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |

## ActionSheetOffset18+对象说明

PhonePC/2in1TabletTVWearable

弹窗的对齐方式。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| dx | number | string | [Resource](ts-types.md#resource) | 否 | 否 | 弹出窗口相对于对齐位置dx的偏移量。  需要显式指定像素单位，如'10px'，也可设置百分比字符串，如'100%'。  **说明：**  不指定像素单位时，默认单位vp，如'10'，等同于10。 |
| dy | number | string | [Resource](ts-types.md#resource) | 否 | 否 | 弹出窗口相对于对齐位置dy的偏移量。  需要显式指定像素单位，如'10px'，也可设置百分比字符串，如'100%'。  **说明：**  不指定像素单位时，默认单位vp，如'10'，等同于10。 |

## ActionSheet

PhonePC/2in1TabletTVWearable

### show(deprecated)

PhonePC/2in1TabletTVWearable

static show(value: ActionSheetOptions)

定义列表弹窗并弹出。

说明

从API version 8开始支持，从API version 18开始废弃，建议使用[showActionSheet](arkts-apis-uicontext-uicontext.md#showactionsheet)替代。showActionSheet需先获取[UIContext](arkts-apis-uicontext-uicontext.md)实例后再进行调用。

从API version 10开始，可以通过使用[UIContext](arkts-apis-uicontext-uicontext.md)中的[showActionSheet](arkts-apis-uicontext-uicontext.md#showactionsheet)来明确UI的执行上下文。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ActionSheetOptions](ts-methods-action-sheet.md#actionsheetoptions对象说明) | 是 | 配置列表选择弹窗的参数。 |

## 示例

PhonePC/2in1TabletTVWearable

说明

直接使用ActionSheet可能导致实例不明确的问题，建议使用getUIContext()获取[UIContext](arkts-apis-uicontext-uicontext.md)实例，并使用[showActionSheet](arkts-apis-uicontext-uicontext.md#showactionsheet)调用绑定实例的ActionSheet.show()。

### 示例1（弹出列表选择弹窗）

该示例通过点击按钮弹出列表选择弹窗。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct ActionSheetExample {
5. build() {
6. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
7. Button('Click to Show ActionSheet')
8. .onClick(() => {
9. this.getUIContext().showActionSheet({
10. title: 'ActionSheet title',
11. subtitle: 'ActionSheet subtitle',
12. message: 'message',
13. autoCancel: true,
14. confirm: {
15. defaultFocus: true,
16. value: 'Confirm button',
17. action: () => {
18. console.info('Get ActionSheet handled');
19. }
20. },
21. cancel: () => {
22. console.info('ActionSheet canceled');
23. },
24. onWillDismiss: (dismissDialogAction: DismissDialogAction) => {
25. console.info(`reason= ${dismissDialogAction.reason}`);
26. console.info('ActionSheet onWillDismiss');
27. if (dismissDialogAction.reason === DismissReason.PRESS_BACK) {
28. dismissDialogAction.dismiss();
29. }
30. if (dismissDialogAction.reason === DismissReason.TOUCH_OUTSIDE) {
31. dismissDialogAction.dismiss();
32. }
33. },
34. alignment: DialogAlignment.Bottom,
35. offset: { dx: 0, dy: -10 },
36. sheets: [
37. {
38. title: 'apples',
39. action: () => {
40. console.info('apples');
41. }
42. },
43. {
44. title: 'bananas',
45. action: () => {
46. console.info('bananas');
47. }
48. },
49. {
50. title: 'pears',
51. action: () => {
52. console.info('pears');
53. }
54. }
55. ]
56. })
57. })
58. }.width('100%')
59. .height('100%')
60. }
61. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5b/v3/BeccOID6T8q7jCuqf1THcQ/zh-cn_image_0000002558766564.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055243Z&HW-CC-Expire=86400&HW-CC-Sign=BD96095663998E2D672733A27200699F2C6E4A4D75896B3D53A9678226B9A269)

### 示例2（可在主窗外弹出的弹窗）

在2in1设备上设置[showInSubWindow](ts-methods-action-sheet.md#actionsheetoptions对象说明)为true时，可以弹出在主窗外显示的弹窗。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct ActionSheetExample {
5. build() {
6. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
7. Button('Click to Show ActionSheet')
8. .onClick(() => {
9. this.getUIContext().showActionSheet({
10. title: 'ActionSheet title',
11. subtitle: 'ActionSheet subtitle',
12. message: 'message',
13. autoCancel: true,
14. showInSubWindow: true,
15. isModal: true,
16. confirm: {
17. defaultFocus: true,
18. value: 'Confirm button',
19. action: () => {
20. console.info('Get ActionSheet handled');
21. }
22. },
23. cancel: () => {
24. console.info('ActionSheet canceled');
25. },
26. onWillDismiss: (dismissDialogAction: DismissDialogAction) => {
27. console.info(`reason= ${dismissDialogAction.reason}`);
28. console.info('ActionSheet onWillDismiss');
29. if (dismissDialogAction.reason === DismissReason.PRESS_BACK) {
30. dismissDialogAction.dismiss();
31. }
32. if (dismissDialogAction.reason === DismissReason.TOUCH_OUTSIDE) {
33. dismissDialogAction.dismiss();
34. }
35. },
36. alignment: DialogAlignment.Center,
37. offset: { dx: 0, dy: -10 },
38. sheets: [
39. {
40. title: 'apples',
41. action: () => {
42. console.info('apples');
43. }
44. },
45. {
46. title: 'bananas',
47. action: () => {
48. console.info('bananas');
49. }
50. },
51. {
52. title: 'pears',
53. action: () => {
54. console.info('pears');
55. }
56. }
57. ]
58. })
59. })
60. }.width('100%')
61. .height('100%')
62. }
63. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/eb/v3/0tj5vzyCTZ-P1GhRxc1UAw/zh-cn_image_0000002558606904.jpg?HW-CC-KV=V1&HW-CC-Date=20260429T055243Z&HW-CC-Expire=86400&HW-CC-Sign=2A300F603D002AC67632E121F7DC3F2A0F5BCD1C353CB02CC851747D1E370349)

### 示例3（设置弹窗的动画）

该示例通过配置[transition](ts-methods-action-sheet.md#actionsheetoptions对象说明)实现弹窗的显示和消失动画。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct ActionSheetExample {
5. build() {
6. Column({ space: 5 }) {
7. Button('ActionSheet Set Duration')
8. .onClick(() => {
9. this.getUIContext().showActionSheet({
10. title: 'ActionSheet 1',
11. message: 'Set Animation Duration open 3 second, close 100 ms',
12. autoCancel: true,
13. alignment: DialogAlignment.Top,
14. transition: TransitionEffect.asymmetric(TransitionEffect.OPACITY
15. .animation({ duration: 3000, curve: Curve.Sharp })
16. .combine(TransitionEffect.scale({ x: 1.5, y: 1.5 }).animation({ duration: 3000, curve: Curve.Sharp })),
17. TransitionEffect.OPACITY.animation({ duration: 100, curve: Curve.Smooth })
18. .combine(TransitionEffect.scale({ x: 0.5, y: 0.5 }).animation({ duration: 100, curve: Curve.Smooth }))),
19. offset: { dx: 0, dy: -20 },
20. confirm: {
21. value: 'button',
22. action: () => {
23. console.info('Button-clicking callback');
24. }
25. },
26. cancel: () => {
27. console.info('Closed callbacks');
28. },
29. sheets: [
30. {
31. title: 'apples',
32. action: () => {
33. console.info('apples');
34. }
35. },
36. {
37. title: 'bananas',
38. action: () => {
39. console.info('bananas');
40. }
41. },
42. {
43. title: 'pears',
44. action: () => {
45. console.info('pears');
46. }
47. }
48. ]
49. })
50. }).backgroundColor(0x317aff).height("88px")
51. }.width('100%').margin({ top: 5 })
52. }
53. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d5/v3/nwJ6-B0vT4GktwgI67dOwg/zh-cn_image_0000002589326431.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055243Z&HW-CC-Expire=86400&HW-CC-Sign=6E5CD7368C32101F38D9A21A9927862BB1C90BE8398974784A8B1ABD8072D7DF)

### 示例4（设置弹窗的样式）

该示例定义了ActionSheet的样式，如宽度、高度、背景色、阴影等。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct ActionSheetExample {
5. build() {
6. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center }) {
7. Button('Click to Show ActionSheet')
8. .onClick(() => {
9. this.getUIContext().showActionSheet({
10. title: 'ActionSheet title',
11. subtitle: 'ActionSheet subtitle',
12. message: 'message',
13. autoCancel: true,
14. width: 300,
15. height: 350,
16. cornerRadius: 20,
17. borderWidth: 1,
18. borderStyle: BorderStyle.Solid, // 使用borderStyle属性，需要和borderWidth属性一起使用
19. borderColor: Color.Blue, // 使用borderColor属性，需要和borderWidth属性一起使用
20. backgroundColor: Color.White,
21. shadow: ({
22. radius: 20,
23. color: Color.Grey,
24. offsetX: 50,
25. offsetY: 0
26. }),
27. confirm: {
28. defaultFocus: true,
29. value: 'Confirm button',
30. action: () => {
31. console.info('Get ActionSheet handled');
32. }
33. },
34. cancel: () => {
35. console.info('ActionSheet canceled');
36. },
37. onWillDismiss: (dismissDialogAction: DismissDialogAction) => {
38. console.info(`reason= ${dismissDialogAction.reason}`);
39. console.info('ActionSheet onWillDismiss');
40. if (dismissDialogAction.reason === DismissReason.PRESS_BACK) {
41. dismissDialogAction.dismiss();
42. }
43. if (dismissDialogAction.reason === DismissReason.TOUCH_OUTSIDE) {
44. dismissDialogAction.dismiss();
45. }
46. },
47. alignment: DialogAlignment.Bottom,
48. offset: { dx: 0, dy: -10 },
49. sheets: [
50. {
51. title: 'apples',
52. action: () => {
53. console.info('apples');
54. }
55. },
56. {
57. title: 'bananas',
58. action: () => {
59. console.info('bananas');
60. }
61. },
62. {
63. title: 'pears',
64. action: () => {
65. console.info('pears');
66. }
67. }
68. ]
69. })
70. })
71. }.width('100%')
72. }
73. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ad/v3/gh7xb_saR62PjKjbJFQtQw/zh-cn_image_0000002589246373.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055243Z&HW-CC-Expire=86400&HW-CC-Sign=6F8B7F5003508E2CC196F4F33338CEDBCF2413706BEF8B18405AC9EEDE5BF1FD)

### 示例5（悬停态弹窗）

该示例展示了在折叠屏悬停态下设置dialog布局区域的效果。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct ActionSheetExample {
5. build() {
6. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
7. Button('Click to Show ActionSheet')
8. .onClick(() => {
9. this.getUIContext().showActionSheet({
10. title: 'ActionSheet title',
11. subtitle: 'ActionSheet subtitle',
12. message: 'message',
13. autoCancel: true,
14. confirm: {
15. defaultFocus: true,
16. value: 'Confirm button',
17. action: () => {
18. console.info('Get ActionSheet handled');
19. }
20. },
21. cancel: () => {
22. console.info('ActionSheet canceled');
23. },
24. onWillDismiss: (dismissDialogAction: DismissDialogAction) => {
25. console.info(`reason= ${dismissDialogAction.reason}`);
26. console.info('ActionSheet onWillDismiss');
27. if (dismissDialogAction.reason === DismissReason.PRESS_BACK) {
28. dismissDialogAction.dismiss();
29. }
30. if (dismissDialogAction.reason === DismissReason.TOUCH_OUTSIDE) {
31. dismissDialogAction.dismiss();
32. }
33. },
34. alignment: DialogAlignment.Bottom,
35. offset: { dx: 0, dy: -10 },
36. enableHoverMode: true,
37. hoverModeArea: HoverModeAreaType.TOP_SCREEN,
38. sheets: [
39. {
40. title: 'apples',
41. action: () => {
42. console.info('apples');
43. }
44. },
45. {
46. title: 'bananas',
47. action: () => {
48. console.info('bananas');
49. }
50. },
51. {
52. title: 'pears',
53. action: () => {
54. console.info('pears');
55. }
56. }
57. ]
58. })
59. })
60. }.width('100%')
61. .height('100%')
62. }
63. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e7/v3/RE4KEmjuSTeRX46z3noA8g/zh-cn_image_0000002558766566.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055243Z&HW-CC-Expire=86400&HW-CC-Sign=9C6C794968A2168F36617B4DFCCEB1BBF0FF9204CF16DCFA5F12346F61C7B0FC)

### 示例6（弹窗生命周期）

该示例为弹窗配置生命周期回调。

从API version 19开始，在[ActionSheetOptions](ts-methods-action-sheet.md#actionsheetoptions对象说明)中新增了onDidAppear、onDidDisappear、onWillAppear和onWillDisappear属性。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct Example1 {
5. @State log: string = 'Log information:';
6. flag: boolean = false;

8. build() {
9. Column({ space: 5 }) {
10. Button('ActionSheet')
11. .onClick(() => {
12. this.getUIContext().showActionSheet({
13. title: 'ActionSheet',
14. message: 'message',
15. autoCancel: true,
16. alignment: DialogAlignment.Bottom,
17. offset: { dx: 0, dy: -20 },
18. confirm: {
19. value: 'button',
20. action: () => {
21. console.info('ActionSheet Button-clicking callback');
22. }
23. },
24. cancel: () => {
25. console.info('ActionSheet Closed callbacks');
26. },
27. sheets: [
28. {
29. title: 'apples',
30. action: () => {
31. console.info('ActionSheet apples')
32. }
33. },
34. {
35. title: 'bananas',
36. action: () => {
37. console.info('ActionSheet bananas')
38. }
39. },
40. {
41. title: 'pears',
42. action: () => {
43. console.info('ActionSheet pears')
44. }
45. }
46. ],
47. onDidAppear: () => {
48. this.log += '# onDidAppear';
49. console.info('ActionSheet,is onDidAppear!');
50. },
51. onDidDisappear: () => {
52. this.log += '# onDidDisappear';
53. console.info('ActionSheet,is onDidDisappear!');
54. },
55. onWillAppear: () => {
56. this.log = 'Log information:onWillAppear';
57. console.info('ActionSheet,is onWillAppear!');
58. },
59. onWillDisappear: () => {
60. this.log += '# onWillDisappear';
61. console.info('ActionSheet,is onWillDisappear!');
62. }
63. })
64. })
65. Text(this.log).fontSize(30).margin({ top: 200 })
66. }.width('100%').margin({ top: 5 })
67. }
68. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f7/v3/PBfd704ORI2xlDgeGAox4Q/zh-cn_image_0000002558606906.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055243Z&HW-CC-Expire=86400&HW-CC-Sign=4F87416E1D9A9F1BE280FED69D29404E42489FFB0BC53E663681F3345F34FC75)

### 示例7（自定义背景模糊效果参数）

该示例通过配置[backgroundBlurStyleOptions](ts-methods-action-sheet.md#actionsheetoptions对象说明)，实现自定义背景模糊效果。

从API version 19开始，在[ActionSheetOptions](ts-methods-action-sheet.md#actionsheetoptions对象说明)中新增了backgroundBlurStyleOptions属性。

```
1. @Entry
2. @Component
3. struct ActionSheetExample {
4. build() {
5. Stack({ alignContent: Alignment.Top }) {
6. Image($r('app.media.bg'))
7. Column() {
8. Button("ActionSheet")
9. .margin(20)
10. .onClick(() => {
11. this.getUIContext().showActionSheet({
12. title: 'ActionSheet Title',
13. subtitle: 'ActionSheet Subtitle',
14. message: 'ActionSheet Text',
15. sheets: [
16. {
17. title: 'Apples',
18. action: () => {
19. console.info('apples');
20. }
21. },
22. {
23. title: 'Bananas',
24. action: () => {
25. console.info('bananas');
26. }
27. },
28. {
29. title: 'Pears',
30. action: () => {
31. console.info('pears');
32. }
33. }
34. ],
35. alignment: DialogAlignment.Center,
36. backgroundColor: undefined,
37. backgroundBlurStyle: BlurStyle.Thin,
38. backgroundBlurStyleOptions: {
39. colorMode: ThemeColorMode.LIGHT,
40. adaptiveColor: AdaptiveColor.AVERAGE,
41. scale: 1,
42. blurOptions: { grayscale: [20, 20] },
43. },
44. });
45. })
46. }.width('100%')
47. }
48. }
49. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/eb/v3/CnUsmHg5S32egO7wT7KAlQ/zh-cn_image_0000002589326433.png?HW-CC-KV=V1&HW-CC-Date=20260429T055243Z&HW-CC-Expire=86400&HW-CC-Sign=B00C14AFFB3B1EDA1080AFC24242EF592E0CB3F27E74EFEB6AAA208B3C864102)

### 示例8（自定义背景效果参数）

该示例通过配置[backgroundEffect](ts-methods-action-sheet.md#actionsheetoptions对象说明)，实现自定义背景效果。

从API version 19开始，在[ActionSheetOptions](ts-methods-action-sheet.md#actionsheetoptions对象说明)中新增了backgroundEffect属性。

```
1. @Entry
2. @Component
3. struct ActionSheetExample {
4. build() {
5. Stack({ alignContent: Alignment.Top }) {
6. Image($r('app.media.bg'))
7. Column() {
8. Button("ActionSheet")
9. .margin(20)
10. .onClick(() => {
11. this.getUIContext().showActionSheet({
12. title: 'ActionSheet Title',
13. subtitle: 'ActionSheet Subtitle',
14. message: 'ActionSheet Text',
15. sheets: [
16. {
17. title: 'Apples',
18. action: () => {
19. console.info('apples');
20. }
21. },
22. {
23. title: 'Bananas',
24. action: () => {
25. console.info('bananas');
26. }
27. },
28. {
29. title: 'Pears',
30. action: () => {
31. console.info('pears');
32. }
33. }
34. ],
35. alignment: DialogAlignment.Center,
36. backgroundColor: undefined,
37. backgroundBlurStyle: BlurStyle.Thin,
38. backgroundEffect: {
39. radius: 60,
40. saturation: 0,
41. brightness: 1,
42. color: Color.White,
43. blurOptions: { grayscale: [20, 20] }
44. },
45. });
46. })
47. }.width('100%')
48. }
49. }
50. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d2/v3/loBE6uUnQy-_7_uN8XcpEQ/zh-cn_image_0000002589246375.png?HW-CC-KV=V1&HW-CC-Date=20260429T055243Z&HW-CC-Expire=86400&HW-CC-Sign=2DE8A4C3FB7CCBCFF23ADBF3CB708869ECBCE3DF4C79E775CE0B8A5582362531)
