---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-methods-alert-dialog-box
title: 警告弹窗 (AlertDialog)
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 弹窗 > 警告弹窗 (AlertDialog)
category: harmonyos-references
scraped_at: 2026-04-28T08:02:21+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:624696705f09bfe5564ea7de2475dc529cdf6caf2821294aafbe75e9e587195e
---

显示警告弹窗组件，可设置文本内容与响应回调。

说明

从API version 7开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

本模块功能依赖UI的执行上下文，不可在[UI上下文不明确](../harmonyos-guides/arkts-global-interface.md#ui上下文不明确)的地方使用，参见[UIContext](arkts-apis-uicontext-uicontext.md)说明。

## AlertDialogParam对象说明

PhonePC/2in1TabletTVWearable

警告弹窗的样式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| title | [ResourceStr](ts-types.md#resourcestr) | 否 | 是 | 弹窗标题。  API version 20之前，弹窗标题的对齐方式为左对齐。  API version 20及之后，弹窗标题的对齐方式为居中对齐。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| subtitle10+ | [ResourceStr](ts-types.md#resourcestr) | 否 | 是 | 弹窗副标题。  API version 20之前，弹窗副标题的对齐方式为左对齐。  API version 20及之后，弹窗副标题的对齐方式为居中对齐。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| message | [ResourceStr](ts-types.md#resourcestr) | 否 | 否 | 弹窗内容。  API version 20之前，弹窗内容的对齐方式为左对齐。  API version 20及之后，弹窗内容的对齐方式为居中对齐。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| autoCancel | boolean | 否 | 是 | 点击遮障层时，是否关闭弹窗，true表示关闭弹窗。false表示不关闭弹窗。  默认值：true  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| cancel | [VoidCallback](ts-types.md#voidcallback12) | 否 | 是 | 点击遮障层关闭dialog时的回调。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| alignment | [DialogAlignment](ts-methods-alert-dialog-box.md#dialogalignment枚举说明) | 否 | 是 | 弹窗在竖直方向上的对齐方式。  默认值：DialogAlignment.Default  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。  **说明**：  若在UIExtension中设置showInSubWindow为true，弹窗将基于UIExtension的宿主窗口对齐。 |
| offset | [Offset](ts-types.md#offset) | 否 | 是 | 弹窗相对alignment所在位置的偏移量。  默认值：{ dx: 0 , dy: 0 }  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| gridCount | number | 否 | 是 | 弹窗容器宽度所占用栅格数。  默认值：4  取值范围：大于等于0的整数。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| maskRect10+ | [Rectangle](ts-methods-alert-dialog-box.md#rectangle8类型说明) | 否 | 是 | 弹窗遮蔽层区域，在遮蔽层区域内的事件不透传，在遮蔽层区域外的事件透传。  默认值：{ x: 0, y: 0, width: '100%', height: '100%' }  **说明：**  showInSubWindow为true时，maskRect不生效。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| showInSubWindow11+ | boolean | 否 | 是 | 某弹窗需要显示在主窗口之外时，是否在子窗口显示此弹窗。值为true表示在子窗口显示弹窗。  默认值：false，弹窗显示在应用内，而非独立子窗口。  **说明**：showInSubWindow为true的弹窗无法触发显示另一个showInSubWindow为true的弹窗。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| isModal11+ | boolean | 否 | 是 | 弹窗是否为模态窗口，模态窗口有蒙层，非模态窗口无蒙层。值为false时，弹窗为非模态窗口，无蒙层。  默认值：true，此时弹窗有蒙层。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| backgroundColor11+ | [ResourceColor](ts-types.md#resourcecolor) | 否 | 是 | 弹窗背板颜色。  默认值：Color.Transparent  **说明：**  backgroundColor会与模糊属性backgroundBlurStyle叠加产生效果，如果不符合预期，可将backgroundBlurStyle设置为BlurStyle.NONE，即可取消模糊。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| backgroundBlurStyle11+ | [BlurStyle](ts-universal-attributes-background.md#blurstyle9) | 否 | 是 | 弹窗背板模糊材质。  默认值：BlurStyle.COMPONENT\_ULTRA\_THICK  **说明：**  设置为BlurStyle.NONE即可关闭背景虚化。当设置了backgroundBlurStyle为非NONE值时，则不要设置backgroundColor，否则颜色显示将不符合预期效果。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| backgroundBlurStyleOptions19+ | [BackgroundBlurStyleOptions](ts-universal-attributes-background.md#backgroundblurstyleoptions10对象说明) | 否 | 是 | 背景模糊效果。默认值请参考BackgroundBlurStyleOptions类型说明。  **元服务API：** 从API version 19开始，该接口支持在元服务中使用。 |
| backgroundEffect19+ | [BackgroundEffectOptions](ts-universal-attributes-background.md#backgroundeffectoptions11) | 否 | 是 | 背景效果参数。默认值请参考BackgroundEffectOptions类型说明。  **元服务API：** 从API version 19开始，该接口支持在元服务中使用。 |
| onWillDismiss12+ | Callback<[DismissDialogAction](ts-methods-alert-dialog-box.md#dismissdialogaction12)> | 否 | 是 | 交互式关闭回调函数。  **说明：**  1.当用户执行点击遮障层关闭、侧滑（左滑/右滑）、三键back、键盘ESC关闭交互操作时，如果注册该回调函数，则不会立刻关闭弹窗。在回调函数中可以通过reason得到阻拦关闭弹窗的操作类型，从而根据原因选择是否能关闭弹窗。当前组件返回的reason中，暂不支持CLOSE\_BUTTON的枚举值。  2.在onWillDismiss回调中，不能再做onWillDismiss拦截。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| cornerRadius12+ | [Dimension](ts-types.md#dimension10) | [BorderRadiuses](ts-types.md#borderradiuses9) | [LocalizedBorderRadiuses](ts-types.md#localizedborderradiuses12) | 否 | 是 | 设置背板的圆角半径。  可分别设置4个圆角的半径。  默认值：{ topLeft: '32vp', topRight: '32vp', bottomLeft: '32vp', bottomRight: '32vp' }  圆角大小受组件尺寸限制，最大值为组件宽或高的一半，若值为负，则按照默认值处理。  百分比参数方式：以父元素弹窗宽和高的百分比来设置弹窗的圆角。  **说明：**  当cornerRadius属性类型为LocalizedBorderRadiuses时，支持随语言习惯改变布局顺序。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| transition12+ | [TransitionEffect](ts-transition-animation-component.md#transitioneffect10对象说明) | 否 | 是 | 设置弹窗显示和退出的过渡效果。  **说明：**  1.如果不设置，则使用默认的显示/退出动效。  2.显示动效中按back键，打断显示动效，执行退出动效，动画效果为显示动效与退出动效的曲线叠加后的效果。  3.退出动效中按back键，不会打断退出动效，退出动效继续执行，继续按back键退出应用。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| width12+ | [Dimension](ts-types.md#dimension10) | 否 | 是 | 设置弹窗背板的宽度。  **说明：**  - 弹窗宽度默认最大值：400vp。  - 百分比参数方式：弹窗参考宽度为所在窗口的宽度，在此基础上调小或调大。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| height12+ | [Dimension](ts-types.md#dimension10) | 否 | 是 | 设置弹窗背板的高度。  **说明：**  - 弹窗高度默认最大值：0.9 \*（窗口高度 - 安全区域）。  - 百分比参数方式：弹窗参考高度为（窗口高度 - 安全区域），在此基础上调小或调大。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| borderWidth12+ | [Dimension](ts-types.md#dimension10) | [EdgeWidths](ts-types.md#edgewidths9) | [LocalizedEdgeWidths](ts-types.md#localizededgewidths12) | 否 | 是 | 可分别设置4个边框宽度。  默认值：0  百分比参数方式：以父元素弹窗宽的百分比来设置弹窗的边框宽度。  当弹窗左边框和右边框大于弹窗宽度，弹窗上边框和下边框大于弹窗高度，显示可能不符合预期。  **说明：**  当borderWidth属性类型为LocalizedEdgeWidths时，支持随语言习惯改变布局顺序。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| borderColor12+ | [ResourceColor](ts-types.md#resourcecolor) | [EdgeColors](ts-types.md#edgecolors9) | [LocalizedEdgeColors](ts-types.md#localizededgecolors12) | 否 | 是 | 设置弹窗背板的边框颜色。  默认值：Color.Black  如果使用borderColor属性，需要和borderWidth属性一起使用。  **说明：**  当borderColor属性类型为LocalizedEdgeColors时，支持随语言习惯改变布局顺序。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| borderStyle12+ | [BorderStyle](ts-appendix-enums.md#borderstyle) | [EdgeStyles](ts-types.md#edgestyles9) | 否 | 是 | 设置弹窗背板的边框样式。  默认值：BorderStyle.Solid  如果使用borderStyle属性，需要和borderWidth属性一起使用。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| shadow12+ | [ShadowOptions](ts-universal-attributes-image-effect.md#shadowoptions对象说明) | [ShadowStyle](ts-universal-attributes-image-effect.md#shadowstyle10枚举说明) | 否 | 是 | 设置弹窗背板的阴影。  当设备为2in1时，默认场景下获焦阴影值为ShadowStyle.OUTER\_FLOATING\_MD，失焦为ShadowStyle.OUTER\_FLOATING\_SM。其他设备默认无阴影。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| textStyle12+ | [TextStyle](ts-methods-alert-dialog-box.md#textstyle12对象说明) | 否 | 是 | 设置弹窗message内容的文本样式。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| enableHoverMode14+ | boolean | 否 | 是 | 是否响应悬停态，值为true时，响应悬停态。  默认值：false，默认不响应。  **说明：**  PC/2in1设备弹窗默认显示在上半屏，在enableHoverMode设置为true时，可以通过设置hoverModeArea参数显示在下半屏。其他设备弹窗在enableHoverMode设置为true时默认显示在下半屏，可以通过设置hoverModeArea参数显示在上半屏。  **元服务API：** 从API version 14开始，该接口支持在元服务中使用。 |
| hoverModeArea14+ | [HoverModeAreaType](ts-universal-attributes-sheet-transition.md#hovermodeareatype14) | 否 | 是 | 悬停态下弹窗默认展示区域。  默认值：HoverModeAreaType.BOTTOM\_SCREEN。  **元服务API：** 从API version 14开始，该接口支持在元服务中使用。 |
| onWillAppear19+ | Callback<void> | 否 | 是 | 弹窗显示动效前的事件回调。  **说明：**  1.正常时序依次为：onWillAppear >> onDidAppear >> onWillDisappear >> onDidDisappear。  2.在onWillAppear内设置改变弹窗显示效果的回调事件，二次弹出生效。  **元服务API：** 从API version 19开始，该接口支持在元服务中使用。 |
| onDidAppear19+ | Callback<void> | 否 | 是 | 弹窗弹出后的事件回调。  **说明：**  1.正常时序依次为：onWillAppear >> onDidAppear >> onWillDisappear >> onDidDisappear。  2.在onDidAppear内设置改变弹窗显示效果的回调事件，二次弹出生效。  3.快速点击弹出，关闭弹窗时，onWillDisappear在onDidAppear前生效。  4.弹窗入场动效未完成时彻底关闭弹窗，动效打断，onDidAppear不会触发。  **元服务API：** 从API version 19开始，该接口支持在元服务中使用。 |
| onWillDisappear19+ | Callback<void> | 否 | 是 | 弹窗退出动效前的事件回调。  **说明：**  正常时序依次为：onWillAppear >> onDidAppear >> onWillDisappear >> onDidDisappear。  **元服务API：** 从API version 19开始，该接口支持在元服务中使用。 |
| onDidDisappear19+ | Callback<void> | 否 | 是 | 弹窗消失后的事件回调。  **说明：**  正常时序依次为：onWillAppear >> onDidAppear >> onWillDisappear >> onDidDisappear。  **元服务API：** 从API version 19开始，该接口支持在元服务中使用。 |
| levelMode15+ | [LevelMode](js-apis-promptaction.md#levelmode15枚举说明) | 否 | 是 | 设置弹窗显示层级。  **说明：**  - 默认值：LevelMode.OVERLAY。  - 当且仅当showInSubWindow属性设置为false时生效。  **元服务API：** 从API version 15开始，该接口支持在元服务中使用。 |
| levelUniqueId15+ | number | 否 | 是 | 设置页面级弹窗需要显示的层级下的[节点UniqueID](js-apis-arkui-framenode.md#getuniqueid12)。仅在levelMode属性设置为LevelMode.EMBEDDED时生效。  取值范围：大于等于0的数字。  **元服务API：** 从API version 15开始，该接口支持在元服务中使用。 |
| immersiveMode15+ | [ImmersiveMode](js-apis-promptaction.md#immersivemode15枚举说明) | 否 | 是 | 设置页面内弹窗蒙层效果。  **说明：**  - 默认值：ImmersiveMode.DEFAULT  - 当且仅当levelMode属性设置为LevelMode.EMBEDDED时生效。  **元服务API：** 从API version 15开始，该接口支持在元服务中使用。 |
| levelOrder18+ | [LevelOrder](ts-methods-alert-dialog-box.md#levelorder18) | 否 | 是 | 设置弹窗显示的顺序。  **说明：**  - 默认值：LevelOrder.clamp(0)  - 不支持动态刷新顺序。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |

## LevelOrder18+

PhonePC/2in1TabletTVWearable

type LevelOrder = LevelOrder

弹窗的显示顺序。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 说明 |
| --- | --- |
| [LevelOrder](js-apis-promptaction.md#levelorder18) | 设置弹窗的显示顺序。 |

## AlertDialogParamWithConfirm对象说明

PhonePC/2in1TabletTVWearable

继承自[AlertDialogParam](ts-methods-alert-dialog-box.md#alertdialogparam对象说明)。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| confirm | [AlertDialogButtonBaseOptions](ts-methods-alert-dialog-box.md#alertdialogbuttonbaseoptions18对象说明) | 否 | 是 | 确认Button的使能状态、默认焦点、按钮风格、文本内容、文本色、按钮背景色和点击回调。在弹窗获焦且未进行tab键走焦时，该按钮默认响应Enter键。多重弹窗情况下，可自动获焦并连续响应。默认响应Enter键能力在defaultFocus为true时不生效。 |

confirm参数优先级：fontColor、backgroundColor > style > defaultFocus

| backgroundColor | fontColor | style | defaultFocus | 效果 |
| --- | --- | --- | --- | --- |
| 绿底 | 红字 | - | - | 绿底红字 |
| 绿底 | - | DialogButtonStyle.HIGHLIGHT | - | 绿底白字 |
| 绿底 | - | DialogButtonStyle.DEFAULT | - | 绿底蓝字 |
| 绿底 | - | - | TRUE | 绿底白字 |
| 绿底 | - | - | FALSE/- | 绿底蓝字 |
| - | 红字 | DialogButtonStyle.HIGHLIGHT | - | 蓝底红字 |
| - | 红字 | DialogButtonStyle.DEFAULT | - | 白底红字 |
| - | 红字 | - | TRUE | 蓝底红字 |
| - | 红字 | - | FALSE/- | 白底红字 |
| - | - | DialogButtonStyle.HIGHLIGHT | - | 蓝底白字 |
| - | - | DialogButtonStyle.DEFAULT | - | 白底蓝字 |
| - | - | - | TRUE | 蓝底白字 |
| - | - | - | FALSE/- | 白底蓝字 |

## AlertDialogParamWithButtons对象说明

PhonePC/2in1TabletTVWearable

继承自[AlertDialogParam](ts-methods-alert-dialog-box.md#alertdialogparam对象说明)。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| primaryButton | [AlertDialogButtonBaseOptions](ts-methods-alert-dialog-box.md#alertdialogbuttonbaseoptions18对象说明) | 否 | 否 | 主要Button的使能状态、默认焦点、按钮风格、文本内容、文本色、按钮背景色和点击回调。在弹窗获焦且未进行tab键走焦时，该按钮默认响应Enter键，且多重弹窗可自动获焦连续响应。默认响应Enter键能力在defaultFocus为true时不生效。 具体使用方式请参考[示例7](ts-methods-alert-dialog-box.md#示例7自定义背景模糊效果参数) 。 |
| secondaryButton | [AlertDialogButtonBaseOptions](ts-methods-alert-dialog-box.md#alertdialogbuttonbaseoptions18对象说明) | 否 | 否 | 次要Button的使能状态、默认焦点、按钮风格、文本内容、文本色、按钮背景色和点击回调。 |

## AlertDialogParamWithOptions10+对象说明

PhonePC/2in1TabletTVWearable

继承自[AlertDialogParam](ts-methods-alert-dialog-box.md#alertdialogparam对象说明)。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| buttons | Array<[AlertDialogButtonOptions](ts-methods-alert-dialog-box.md#alertdialogbuttonoptions10对象说明)> | 否 | 否 | 弹窗容器中的多个按钮。 |
| buttonDirection | [DialogButtonDirection](ts-methods-alert-dialog-box.md#dialogbuttondirection10枚举说明) | 否 | 是 | 按钮排布方向默认为DialogButtonDirection.AUTO。建议3个以上按钮使用Auto模式（两个以上按钮会切换为纵向模式，通常能显示更多按钮）。非Auto模式下，3个以上按钮可能会显示不全，超出显示范围的按钮会被截断。 |

## AlertDialogButtonOptions10+对象说明

PhonePC/2in1TabletTVWearable

继承自[AlertDialogButtonBaseOptions](ts-methods-alert-dialog-box.md#alertdialogbuttonbaseoptions18对象说明)。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| primary12+ | boolean | 否 | 是 | 在弹窗获焦且未进行tab键走焦时，按钮是否默认响应Enter键。多个Button时，只允许一个Button的该字段配置为true，否则所有Button均不响应。多重弹窗可自动获焦连续响应。在defaultFocus为true时不生效。值为true表示按钮默认响应Enter键，值为false时，按钮不默认响应Enter键。  默认值：false  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |

## AlertDialogButtonBaseOptions18+对象说明

PhonePC/2in1TabletTVWearable

警告弹窗中按钮的样式。

说明

为规范匿名对象的定义，API 18版本修改了此处的元素定义。其中，保留了历史匿名对象的起始版本信息，会出现外层元素@since版本号高于内层元素版本号的情况，但这不影响接口的使用。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| enabled10+ | boolean | 否 | 是 | 点击Button是否响应，默认值true。  值为true时，Button可以响应。值为false时，Button不可以响应。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| defaultFocus10+ | boolean | 否 | 是 | 设置Button是否是默认焦点，默认值false。值为true表示Button为默认焦点，值为false表示Button不为默认焦点。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| style10+ | [DialogButtonStyle](ts-appendix-enums.md#dialogbuttonstyle10) | 否 | 是 | 设置Button的风格样式，默认值DialogButtonStyle.DEFAULT。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| value10+ | [ResourceStr](ts-types.md#resourcestr) | 否 | 否 | Button的文本内容，若值为null，则该按钮不显示。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| fontColor10+ | [ResourceColor](ts-types.md#resourcecolor) | 否 | 是 | Button的文本颜色。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| backgroundColor10+ | [ResourceColor](ts-types.md#resourcecolor) | 否 | 是 | Button背景颜色。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| action10+ | [VoidCallback](ts-types.md#voidcallback12) | 否 | 否 | Button选中时的回调。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |

## DialogButtonDirection10+枚举说明

PhonePC/2in1TabletTVWearable

警告弹窗中按钮的对齐方式。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| AUTO | 0 | 两个及以下按钮水平排布，两个以上为竖直排布。 |
| HORIZONTAL | 1 | 按钮水平布局。 |
| VERTICAL | 2 | 按钮竖直布局。 |

## DialogAlignment枚举说明

PhonePC/2in1TabletTVWearable

警告弹窗的对齐方式。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| Top | 0 | 垂直顶部对齐。 |
| Center | 1 | 垂直居中对齐。 |
| Bottom | 2 | 垂直底部对齐。 |
| Default | 3 | 默认对齐。 |
| TopStart8+ | 4 | 左上对齐。 |
| TopEnd8+ | 5 | 右上对齐。 |
| CenterStart8+ | 6 | 左中对齐。 |
| CenterEnd8+ | 7 | 右中对齐。 |
| BottomStart8+ | 8 | 左下对齐。 |
| BottomEnd8+ | 9 | 右下对齐。 |

## Rectangle8+类型说明

PhonePC/2in1TabletTVWearable

Rectangle是各种Dialog中maskRect参数的类型。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| x | [Length](ts-types.md#length) | 否 | 是 | 弹窗遮蔽层区域相对于窗口左上角的x轴坐标。  默认值：0vp |
| y | [Length](ts-types.md#length) | 否 | 是 | 弹窗遮蔽层区域相对于窗口左上角的y轴坐标。  默认值：0vp |
| width | [Length](ts-types.md#length) | 否 | 是 | 弹窗遮蔽层区域的宽度。  默认值：'100%' |
| height | [Length](ts-types.md#length) | 否 | 是 | 弹窗遮蔽层区域的高度。  默认值：'100%' |

说明

x和y可以设置正负值百分比。当x设置为'100%'时表示遮蔽层区域往右偏移窗口本身宽度大小，当x设置为'-100%'时表示遮蔽层区域往左偏移窗口本身宽度大小。当y设置为'100%'时表示遮蔽层区域往下偏移窗口本身高度大小，当y设置为'-100%'时表示遮蔽层区域往上偏移窗口本身高度大小。

width和height只能设置正值，支持百分比，如果设置为负值，那么该值将被重置为默认值。

百分比相对于窗口自身宽高进行计算。

## DismissDialogAction12+

PhonePC/2in1TabletTVWearable

Dialog关闭的信息。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

### 属性

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| dismiss | Callback<void> | 否 | 否 | Dialog关闭回调函数。开发者需要退出时调用，不需要退出时无需调用。 |
| reason | [DismissReason](ts-universal-attributes-popup.md#dismissreason12枚举说明) | 否 | 否 | Dialog无法关闭原因。根据开发者需要选择不同操作下，Dialog是否需要关闭。 |

## TextStyle12+对象说明

PhonePC/2in1TabletTVWearable

弹窗中message的截断方式。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| wordBreak | [WordBreak](ts-appendix-enums.md#wordbreak11) | 否 | 是 | 弹窗message内容的文本截断方式。  默认值：WordBreak.BREAK\_ALL |

## AlertDialog

PhonePC/2in1TabletTVWearable

### show(deprecated)

PhonePC/2in1TabletTVWearable

static show(value: AlertDialogParamWithConfirm | AlertDialogParamWithButtons | AlertDialogParamWithOptions)

定义警告弹窗并弹出。

说明

从API version 7开始支持，从API version 18开始废弃，建议使用[showAlertDialog](arkts-apis-uicontext-uicontext.md#showalertdialog)替代。showAlertDialog需先获取[UIContext](arkts-apis-uicontext-uicontext.md)实例后再进行调用。

从API version 10开始，可以通过使用[UIContext](arkts-apis-uicontext-uicontext.md)中的[showAlertDialog](arkts-apis-uicontext-uicontext.md#showalertdialog)来明确UI的执行上下文。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [AlertDialogParamWithConfirm](ts-methods-alert-dialog-box.md#alertdialogparamwithconfirm对象说明) | [AlertDialogParamWithButtons](ts-methods-alert-dialog-box.md#alertdialogparamwithbuttons对象说明) | [AlertDialogParamWithOptions](ts-methods-alert-dialog-box.md#alertdialogparamwithoptions10对象说明)10+ | 是 | 定义并显示AlertDialog组件。 |

## 示例

PhonePC/2in1TabletTVWearable

说明

直接使用AlertDialog可能导致[UI上下文不明确](../harmonyos-guides/arkts-global-interface.md#ui上下文不明确)的问题，建议使用getUIContext()获取[UIContext](arkts-apis-uicontext-uicontext.md)实例，并使用[showAlertDialog](arkts-apis-uicontext-uicontext.md#showalertdialog)调用绑定实例的AlertDialog.show()。

### 示例1（弹出多个按钮的弹窗）

该示例通过[AlertDialogParamWithConfirm](ts-methods-alert-dialog-box.md#alertdialogparamwithconfirm对象说明)、[AlertDialogParamWithButtons](ts-methods-alert-dialog-box.md#alertdialogparamwithbuttons对象说明)和[AlertDialogParamWithOptions](ts-methods-alert-dialog-box.md#alertdialogparamwithoptions10对象说明)实现了分别弹出一、二、三个按钮的弹窗。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct AlertDialogExample {
5. build() {
6. Column({ space: 5 }) {
7. Button('one button dialog')
8. .onClick(() => {
9. this.getUIContext().showAlertDialog(
10. {
11. title: 'title',
12. message: 'text',
13. autoCancel: true,
14. alignment: DialogAlignment.Bottom,
15. offset: { dx: 0, dy: -20 },
16. gridCount: 3,
17. confirm: {
18. value: 'button',
19. action: () => {
20. console.info('Button-clicking callback');
21. }
22. },
23. cancel: () => {
24. console.info('Closed callbacks');
25. },
26. onWillDismiss: (dismissDialogAction: DismissDialogAction) => {
27. console.info(`reason= ${dismissDialogAction.reason}`);
28. console.info('AlertDialog onWillDismiss');
29. if (dismissDialogAction.reason === DismissReason.PRESS_BACK) {
30. dismissDialogAction.dismiss();
31. }
32. if (dismissDialogAction.reason === DismissReason.TOUCH_OUTSIDE) {
33. dismissDialogAction.dismiss();
34. }
35. }
36. }
37. )
38. })
39. .backgroundColor(0x317aff)
40. Button('two button dialog')
41. .onClick(() => {
42. this.getUIContext().showAlertDialog(
43. {
44. title: 'title',
45. subtitle: 'subtitle',
46. message: 'text',
47. autoCancel: true,
48. alignment: DialogAlignment.Bottom,
49. gridCount: 4,
50. offset: { dx: 0, dy: -20 },
51. primaryButton: {
52. value: 'cancel',
53. action: () => {
54. console.info('Callback when the first button is clicked');
55. }
56. },
57. secondaryButton: {
58. enabled: true,
59. defaultFocus: true,
60. style: DialogButtonStyle.HIGHLIGHT,
61. value: 'ok',
62. action: () => {
63. console.info('Callback when the second button is clicked');
64. }
65. },
66. cancel: () => {
67. console.info('Closed callbacks');
68. },
69. onWillDismiss: (dismissDialogAction: DismissDialogAction) => {
70. console.info(`reason= ${dismissDialogAction.reason}`);
71. console.info('AlertDialog onWillDismiss');
72. if (dismissDialogAction.reason === DismissReason.PRESS_BACK) {
73. dismissDialogAction.dismiss();
74. }
75. if (dismissDialogAction.reason === DismissReason.TOUCH_OUTSIDE) {
76. dismissDialogAction.dismiss();
77. }
78. }
79. }
80. )
81. }).backgroundColor(0x317aff)
82. Button('three button dialog')
83. .onClick(() => {
84. this.getUIContext().showAlertDialog(
85. {
86. title: 'title',
87. subtitle: 'subtitle',
88. message: 'text',
89. autoCancel: true,
90. alignment: DialogAlignment.Bottom,
91. gridCount: 4,
92. offset: { dx: 0, dy: -20 },
93. buttonDirection: DialogButtonDirection.HORIZONTAL,
94. buttons: [
95. {
96. value: '按钮',
97. action: () => {
98. console.info('Callback when button1 is clicked');
99. }
100. },
101. {
102. value: '按钮',
103. action: () => {
104. console.info('Callback when button2 is clicked');
105. }
106. },
107. {
108. value: '按钮',
109. enabled: true,
110. defaultFocus: true,
111. style: DialogButtonStyle.HIGHLIGHT,
112. action: () => {
113. console.info('Callback when button3 is clicked');
114. }
115. },
116. ],
117. cancel: () => {
118. console.info('Closed callbacks');
119. },
120. onWillDismiss: (dismissDialogAction: DismissDialogAction) => {
121. console.info(`reason= ${dismissDialogAction.reason}`);
122. console.info('AlertDialog onWillDismiss');
123. if (dismissDialogAction.reason === DismissReason.PRESS_BACK) {
124. dismissDialogAction.dismiss();
125. }
126. if (dismissDialogAction.reason === DismissReason.TOUCH_OUTSIDE) {
127. dismissDialogAction.dismiss();
128. }
129. }
130. }
131. )
132. }).backgroundColor(0x317aff)
133. }.width('100%').margin({ top: 5 })
134. }
135. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/17/v3/DRYR7ayESmGsvQUYTIfe6w/zh-cn_image_0000002552960034.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000219Z&HW-CC-Expire=86400&HW-CC-Sign=7A34586FD28519FB7BB1B512D371563D861F32AC5FF5BB3B70C40F172C55AD74)

### 示例2（可在主窗外弹出的弹窗）

在2in1设备上设置[AlertDialogParam](ts-methods-alert-dialog-box.md#alertdialogparam对象说明)中showInSubWindow属性的值为true时，可以弹出在主窗外显示的弹窗。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct AlertDialogExample {
5. build() {
6. Column({ space: 5 }) {
7. Button('one button dialog')
8. .onClick(() => {
9. this.getUIContext().showAlertDialog(
10. {
11. title: 'title',
12. subtitle: 'subtitle',
13. message: 'text',
14. autoCancel: true,
15. alignment: DialogAlignment.Center,
16. gridCount: 4,
17. showInSubWindow: true,
18. isModal: true,
19. offset: { dx: 0, dy: -20 },
20. buttonDirection: DialogButtonDirection.HORIZONTAL,
21. buttons: [
22. {
23. value: '按钮',
24. action: () => {
25. console.info('Callback when button1 is clicked');
26. }
27. },
28. {
29. value: '按钮',
30. action: () => {
31. console.info('Callback when button2 is clicked');
32. }
33. },
34. {
35. value: '按钮',
36. enabled: true,
37. defaultFocus: true,
38. style: DialogButtonStyle.HIGHLIGHT,
39. action: () => {
40. console.info('Callback when button3 is clicked');
41. }
42. },
43. ],
44. cancel: () => {
45. console.info('Closed callbacks');
46. },
47. onWillDismiss: (dismissDialogAction: DismissDialogAction) => {
48. console.info(`reason= ${dismissDialogAction.reason}`);
49. console.info('AlertDialog onWillDismiss');
50. if (dismissDialogAction.reason === DismissReason.PRESS_BACK) {
51. dismissDialogAction.dismiss();
52. }
53. if (dismissDialogAction.reason === DismissReason.TOUCH_OUTSIDE) {
54. dismissDialogAction.dismiss();
55. }
56. }
57. })
58. })
59. }.width('100%').margin({ top: 5 })
60. }
61. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/41/v3/l-UueLTrS46Ku7GLiH39Ng/zh-cn_image_0000002583480035.jpg?HW-CC-KV=V1&HW-CC-Date=20260428T000219Z&HW-CC-Expire=86400&HW-CC-Sign=C3B8D905FF23805713331D2073B909813E6C0390A308FDB81A506BFE6268EC02)

### 示例3（设置弹窗的动画）

该示例通过配置[AlertDialogParam](ts-methods-alert-dialog-box.md#alertdialogparam对象说明)中的transition属性来实现弹窗的显示和消失动画。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct AlertDialogExample {
5. build() {
6. Column({ space: 5 }) {
7. Button('AlertDialog Set Duration')
8. .onClick(() => {
9. this.getUIContext().showAlertDialog(
10. {
11. title: 'AlertDialog 1',
12. message: 'Set Animation Duration open 3 second, close 100ms',
13. autoCancel: true,
14. alignment: DialogAlignment.Top,
15. offset: { dx: 0, dy: -20 },
16. gridCount: 3,
17. transition: TransitionEffect.asymmetric(TransitionEffect.OPACITY
18. .animation({ duration: 3000, curve: Curve.Sharp })
19. .combine(TransitionEffect.scale({ x: 1.5, y: 1.5 }).animation({ duration: 3000, curve: Curve.Sharp })),
20. TransitionEffect.OPACITY.animation({ duration: 100, curve: Curve.Smooth })
21. .combine(TransitionEffect.scale({ x: 0.5, y: 0.5 })
22. .animation({ duration: 100, curve: Curve.Smooth }))),
23. confirm: {
24. value: 'button',
25. action: () => {
26. console.info('Button-clicking callback');
27. }
28. },
29. cancel: () => {
30. console.info('Closed callbacks');
31. }
32. }
33. )
34. })
35. .backgroundColor(0x317aff).height('88px')
36. }.width('100%').margin({ top: 5 })
37. }
38. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/ayIc86UoRTiHaZ-G879MAQ/zh-cn_image_0000002552800386.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000219Z&HW-CC-Expire=86400&HW-CC-Sign=067C9CA01318E7F07AF866FB48888413A6C9610C71CA04AE1C48F8CC3786D85F)

### 示例4（设置弹窗的样式）

示例定义了AlertDialog的样式，包括宽度、高度、背景色、阴影等。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct AlertDialogExample {
5. build() {
6. Column({ space: 5 }) {
7. Button('one button dialog')
8. .onClick(() => {
9. this.getUIContext().showAlertDialog(
10. {
11. title: 'title',
12. message: 'text',
13. autoCancel: true,
14. alignment: DialogAlignment.Center,
15. offset: { dx: 0, dy: -20 },
16. gridCount: 3,
17. width: 300,
18. height: 200,
19. cornerRadius: 20,
20. borderWidth: 1,
21. borderStyle: BorderStyle.Dashed, // 使用borderStyle属性，需要和borderWidth属性一起使用
22. borderColor: Color.Blue, // 使用borderColor属性，需要和borderWidth属性一起使用
23. backgroundColor: Color.White,
24. shadow: ({
25. radius: 20,
26. color: Color.Grey,
27. offsetX: 50,
28. offsetY: 0
29. }),
30. textStyle: { wordBreak: WordBreak.BREAK_ALL },
31. confirm: {
32. value: 'button',
33. action: () => {
34. console.info('Button-clicking callback');
35. }
36. },
37. cancel: () => {
38. console.info('Closed callbacks');
39. },
40. onWillDismiss: (dismissDialogAction: DismissDialogAction) => {
41. console.info(`reason= ${dismissDialogAction.reason}`);
42. console.info('AlertDialog onWillDismiss');
43. if (dismissDialogAction.reason === DismissReason.PRESS_BACK) {
44. dismissDialogAction.dismiss();
45. }
46. if (dismissDialogAction.reason === DismissReason.TOUCH_OUTSIDE) {
47. dismissDialogAction.dismiss();
48. }
49. }
50. }
51. )
52. })
53. .backgroundColor(0x317aff)
54. }.width('100%').margin({ top: 5 })
55. }
56. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d5/v3/ICXywD34TXK1qX-uZHg7Bw/zh-cn_image_0000002583440081.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000219Z&HW-CC-Expire=86400&HW-CC-Sign=3C3F040449C217FBAFE39BBECC559082C20C1C886FFF00AB472877E3985F72B1)

### 示例5（悬停态弹窗）

该示例展示了在折叠屏悬停态下设置dialog布局区域的效果。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct AlertDialogExample {
5. build() {
6. Column({ space: 5 }) {
7. Button('one button dialog')
8. .onClick(() => {
9. this.getUIContext().showAlertDialog(
10. {
11. title: 'title',
12. message: 'text',
13. autoCancel: true,
14. alignment: DialogAlignment.Bottom,
15. gridCount: 3,
16. confirm: {
17. value: 'button',
18. action: () => {
19. console.info('Button-clicking callback');
20. }
21. },
22. cancel: () => {
23. console.info('Closed callbacks');
24. },
25. onWillDismiss: (dismissDialogAction: DismissDialogAction) => {
26. console.info(`reason= ${dismissDialogAction.reason}`);
27. console.info('AlertDialog onWillDismiss');
28. if (dismissDialogAction.reason === DismissReason.PRESS_BACK) {
29. dismissDialogAction.dismiss();
30. }
31. if (dismissDialogAction.reason === DismissReason.TOUCH_OUTSIDE) {
32. dismissDialogAction.dismiss();
33. }
34. },
35. enableHoverMode: true,
36. hoverModeArea: HoverModeAreaType.TOP_SCREEN
37. }
38. )
39. })
40. .backgroundColor(0x317aff)
41. }.width('100%').margin({ top: 5 })
42. }
43. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7d/v3/7o_oV95JSAWQyDwq4B4KvA/zh-cn_image_0000002552960036.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000219Z&HW-CC-Expire=86400&HW-CC-Sign=B1B8DE7C76FB859A06DF6BD6CAACC2B06D33353697032606C9E800E889E06924)

### 示例6（弹窗生命周期）

该示例展示了弹窗生命周期的相关接口的使用方法。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct Example2 {
5. @State log: string = 'Log information:';

7. build() {
8. Column({ space: 5 }) {
9. Button('AlertDialog')
10. .onClick(() => {
11. this.getUIContext().showAlertDialog({
12. title: 'AlertDialog',
13. message: 'message',
14. autoCancel: true,
15. alignment: DialogAlignment.Bottom,
16. offset: { dx: 0, dy: -20 },
17. confirm: {
18. value: 'button',
19. action: () => {
20. console.info('AlertDialog Button-clicking callback');
21. }
22. },
23. cancel: () => {
24. console.info('Closed callbacks');
25. },
26. onDidAppear: () => {
27. this.log += '# onDidAppear';
28. console.info('AlertDialog,is onDidAppear!');
29. },
30. onDidDisappear: () => {
31. this.log += '# onDidDisappear';
32. console.info('AlertDialog,is onDidDisappear!');
33. },
34. onWillAppear: () => {
35. this.log = 'Log information:onWillAppear';
36. console.info('AlertDialog,is onWillAppear!');
37. },
38. onWillDisappear: () => {
39. this.log += '# onWillDisappear';
40. console.info('AlertDialog,is onWillDisappear!');
41. }
42. })
43. })
44. Text(this.log).fontSize(30).margin({ top: 200 })
45. }.width('100%').margin({ top: 5 })
46. }
47. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e9/v3/kbC_c7UgRKCTEYTwVWtrWg/zh-cn_image_0000002583480037.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000219Z&HW-CC-Expire=86400&HW-CC-Sign=68DB30073791A44150A0CE096D21B620DF6C8DE95CDDE2D4C9A749555D7274C1)

### 示例7（自定义背景模糊效果参数）

该示例通过配置[AlertDialogParam](ts-methods-alert-dialog-box.md#alertdialogparam对象说明)中的backgroundBlurStyleOptions属性，实现了自定义背景模糊效果。

从API version 19开始，在AlertDialogParam中新增了backgroundBlurStyleOptions属性。

```
1. @Entry
2. @Component
3. struct AlertDialogExample {
4. build() {
5. Stack({ alignContent: Alignment.Top }) {
6. // $r('app.media.bg')需要替换为开发者所需的图像资源文件。
7. Image($r('app.media.bg'))
8. Column() {
9. Button("AlertDialog")
10. .margin(20)
11. .onClick(() => {
12. this.getUIContext().showAlertDialog({
13. title: 'AlertDialog Title',
14. message: 'AlertDialog Text',
15. primaryButton: {
16. value: '确定',
17. action: () => {
18. console.info('primaryButton');
19. }
20. },
21. secondaryButton: {
22. value: '取消',
23. action: () => {
24. console.info('secondaryButton');
25. }
26. },
27. backgroundColor: undefined,
28. backgroundBlurStyle: BlurStyle.Thin,
29. backgroundBlurStyleOptions: {
30. colorMode: ThemeColorMode.LIGHT,
31. adaptiveColor: AdaptiveColor.AVERAGE,
32. scale: 1,
33. blurOptions: { grayscale: [20, 20] },
34. },
35. });
36. })
37. }.width('100%')
38. }
39. }
40. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/53/v3/b70DD6uVT5W44iRYu9z9wQ/zh-cn_image_0000002552800388.png?HW-CC-KV=V1&HW-CC-Date=20260428T000219Z&HW-CC-Expire=86400&HW-CC-Sign=1C9AEB5D5F169AFC55B414F84F843587A0DF0A158931AC93AACC75B004FCCADD)

### 示例8（自定义背景效果参数）

该示例通过配置[AlertDialogParam](ts-methods-alert-dialog-box.md#alertdialogparam对象说明)中的backgroundEffect属性，实现自定义背景效果。

从API version 19开始，在AlertDialogParam中新增了backgroundEffect属性。

```
1. @Entry
2. @Component
3. struct AlertDialogExample {
4. build() {
5. Stack({ alignContent: Alignment.Top }) {
6. // $r('app.media.bg')需要替换为开发者所需的图像资源文件。
7. Image($r('app.media.bg'))
8. Column() {
9. Button("AlertDialog")
10. .margin(20)
11. .onClick(() => {
12. this.getUIContext().showAlertDialog({
13. title: 'AlertDialog Title',
14. message: 'AlertDialog Text',
15. primaryButton: {
16. value: '确定',
17. action: () => {
18. console.info('primaryButton');
19. }
20. },
21. secondaryButton: {
22. value: '取消',
23. action: () => {
24. console.info('secondaryButton');
25. }
26. },
27. backgroundColor: undefined,
28. backgroundBlurStyle: BlurStyle.Thin,
29. backgroundEffect: {
30. radius: 60,
31. saturation: 0,
32. brightness: 1,
33. color: Color.White,
34. blurOptions: { grayscale: [20, 20] }
35. },
36. });
37. })
38. }.width('100%')
39. }
40. }
41. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7f/v3/Aj5JvXvMSOi4arCHcn3Nbg/zh-cn_image_0000002583440083.png?HW-CC-KV=V1&HW-CC-Date=20260428T000219Z&HW-CC-Expire=86400&HW-CC-Sign=02AA7949E80C07D556960B5DA82AE52E5CD61CDC94F5CD00E2D547997787332A)
