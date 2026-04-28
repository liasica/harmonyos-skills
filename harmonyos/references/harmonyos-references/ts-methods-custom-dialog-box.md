---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-methods-custom-dialog-box
title: 自定义弹窗 (CustomDialog)
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 弹窗 > 自定义弹窗 (CustomDialog)
category: harmonyos-references
scraped_at: 2026-04-28T08:02:21+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:922e6748901eece7f6e1c95c0801533b90c21d301eab870ddd1d261004d0a02f
---

通过CustomDialogController类显示自定义弹窗。使用弹窗组件时，优先考虑自定义弹窗，便于弹窗样式与内容的自定义。

说明

从API version 7开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

## CustomDialogController

PhonePC/2in1TabletTVWearable

自定义弹窗的控制器。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

### 导入对象

```
1. dialogController : CustomDialogController | null = new CustomDialogController(CustomDialogControllerOptions)
```

说明

* CustomDialogController仅在作为@CustomDialog和@Component struct成员变量，且在@Component struct内部定义时赋值才有效，具体用法可参考下方示例。
* 若尝试在CustomDialog中传入多个其他的Controller，以实现在CustomDialog中打开另一个或另一些CustomDialog，那么此处需要将指向自己的controller放在所有controller的后面。详细用法可参考[示例1弹出嵌套弹窗](ts-methods-custom-dialog-box.md#示例1弹出嵌套弹窗)。

### constructor

PhonePC/2in1TabletTVWearable

constructor(value: CustomDialogControllerOptions)

自定义弹窗的构造器。

说明

自定义弹窗的所有参数，不支持动态刷新，但可以通过设置customStyle为true，并在自定义组件上设置[背景色](ts-universal-attributes-background.md#backgroundcolor)、[背景模糊](ts-universal-attributes-background.md#backgroundblurstyle9)、[宽高](ts-universal-attributes-size.md)等属性，通过属性绑定的状态变量来实现动态刷新的效果。

在CustomDialogController作为全局变量以实现全局自定义弹窗的场景下，若对controller重新赋值，则无法通过其关闭之前的弹窗。建议在重新赋值前先关闭弹窗。

在自定义弹窗内拉起另一个自定义弹窗时，不建议直接关闭拉起方。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [CustomDialogControllerOptions](ts-methods-custom-dialog-box.md#customdialogcontrolleroptions对象说明) | 是 | 配置自定义弹窗的参数。 |

### open

PhonePC/2in1TabletTVWearable

open()

显示自定义弹窗内容，允许多次使用，但如果弹框为SubWindow模式，则该弹框不允许再弹出SubWindow弹框。

说明

不支持在输入法类型窗口中使用子窗（showInSubwindow为true）的CustomDialog，详情见输入法框架的约束与限制说明[createPanel](js-apis-inputmethodengine.md#createpanel10-1)。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

### close

PhonePC/2in1TabletTVWearable

close()

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

关闭显示的自定义弹窗，若已关闭，则不生效。

### getState20+

PhonePC/2in1TabletTVWearable

getState(): PromptActionCommonState

获取自定义弹窗的状态。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [PromptActionCommonState](ts-methods-custom-dialog-box.md#promptactioncommonstate20) | 返回对应的弹窗状态。 |

## PromptActionCommonState20+

PhonePC/2in1TabletTVWearable

type PromptActionCommonState = promptAction.CommonState

自定义弹窗的状态。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 说明 |
| --- | --- |
| [promptAction.CommonState](js-apis-promptaction.md#commonstate20枚举说明) | 返回对应的弹窗状态。 |

## CustomDialogControllerOptions对象说明

PhonePC/2in1TabletTVWearable

自定义弹窗的样式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| builder | [CustomDialog](../harmonyos-guides/arkts-common-components-custom-dialog.md) | 否 | 否 | 自定义弹窗内容构造器。  **说明：**  若builder构造器使用回调函数作为入参，请注意使用this绑定问题，如builder: custombuilder({ callback: ()=> {...}})。  若在builder中监听数据变化可以使用@Link或@Consume，而其他方式如@Prop、@ObjectLink不适用此场景。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| cancel | () => void | 否 | 是 | 返回、ESC键和点击遮障层弹窗退出时的回调。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| autoCancel | boolean | 否 | 是 | 是否允许点击遮障层退出，true表示关闭弹窗。false表示不关闭弹窗。  默认值：true  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| alignment | [DialogAlignment](ts-methods-alert-dialog-box.md#dialogalignment枚举说明) | 否 | 是 | 弹窗在竖直方向上的对齐方式。  默认值：DialogAlignment.Default  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| offset | [Offset](ts-types.md#offset) | 否 | 是 | 弹窗相对alignment所在位置的偏移量。  默认值：{ dx: 0, dy: 0 }  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| customStyle | boolean | 否 | 是 | 弹窗容器样式是否自定义。值为true表示弹窗容器样式不能自定义，值为false表示弹窗容器样式能自定义。  默认值：false  设置为false时：  1. 默认圆角为32vp。  2. 未设置弹窗宽度高度：弹窗容器的宽度根据栅格系统自适应。高度自适应自定义的内容节点。  3. 设置弹窗宽度高度：弹窗容器的宽度不超过默认样式下的最大宽度（自定义节点设置100%的宽度），弹窗容器的高度不超过默认样式下的最大高度（自定义节点设置100%的高度）。  4. 受安全区域的影响，弹窗显示区域将排除安全区域。例如在PC/2in1设备上避让屏幕边缘以及窗口标题栏。  设置为true时：  1. 圆角为0，弹窗背景色为透明色。  2. 不支持设置弹窗宽度、高度、边框宽度、边框样式、边框颜色以及阴影宽度。  3. 弹窗显示区域为屏幕。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| gridCount8+ | number | 否 | 是 | 弹窗宽度占[栅格宽度](../harmonyos-guides/arkts-layout-development-grid-layout.md)的个数。  默认为按照窗口大小自适应，异常值按默认值处理，最大栅格数为系统最大栅格数。  取值范围：大于等于0的整数。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| maskColor10+ | [ResourceColor](ts-types.md#resourcecolor) | 否 | 是 | 自定义蒙层颜色。  默认值：0x33000000  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| maskRect10+ | [Rectangle](ts-methods-alert-dialog-box.md#rectangle8类型说明) | 否 | 是 | 弹窗遮蔽层区域，在遮蔽层区域内的事件不透传，在遮蔽层区域外的事件透传。  默认值：{ x: 0, y: 0, width: '100%', height: '100%' }  **说明：**  showInSubWindow为true时，maskRect不生效。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| openAnimation10+ | [AnimateParam](ts-explicit-animation.md#animateparam对象说明) | 否 | 是 | 自定义设置弹窗弹出的动画效果相关参数。  **说明**：  tempo默认值为1，当设置小于等于0的值时按默认值处理。  iterations默认值为1，默认播放一次，设置为其他数值时按默认值处理。  playMode控制动画播放模式，默认值为PlayMode.Normal，设置为其他数值时按照默认值处理。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| closeAnimation10+ | [AnimateParam](ts-explicit-animation.md#animateparam对象说明) | 否 | 是 | 自定义设置弹窗关闭的动画效果相关参数。  **说明**：  tempo默认值为1，当设置小于等于0的值时按默认值处理。  iterations默认值为1，默认播放一次，设置为其他数值时按默认值处理。  playMode控制动画播放模式，默认值为PlayMode.Normal，设置为其他数值时按照默认值处理。  页面转场切换时，建议使用默认关闭动效。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| showInSubWindow10+ | boolean | 否 | 是 | 某弹框需要显示在主窗口之外时，是否在子窗口显示此弹窗。值为true表示在子窗口显示弹窗。  默认值：false，弹窗显示在应用内，而非独立子窗口。  **说明**：showInSubWindow为true的弹窗无法触发显示另一个showInSubWindow为true的弹窗。不建议在showInSubWindow为true的弹窗中使用CalendarPicker、CalendarPickerDialog、DatePickerDialog、TextPickerDialog、TimePickerDialog、Toast组件，弹窗会影响上述组件行为。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| backgroundColor10+ | [ResourceColor](ts-types.md#resourcecolor) | 否 | 是 | 设置弹窗背板填充。  默认值：Color.Transparent  **说明：** 如果同时设置了内容构造器的背景色，则backgroundColor会被内容构造器的背景色覆盖。  backgroundColor会与模糊属性backgroundBlurStyle叠加产生效果，如果不符合预期，可将backgroundBlurStyle设置为BlurStyle.NONE，即可取消模糊。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| cornerRadius10+ | [Dimension](ts-types.md#dimension10) | [BorderRadiuses](ts-types.md#borderradiuses9) | 否 | 是 | 设置背板的圆角半径。  可分别设置4个圆角的半径。  默认值：{ topLeft: '32vp', topRight: '32vp', bottomLeft: '32vp', bottomRight: '32vp' }  **说明**：自定义弹窗默认的背板圆角半径为32vp，如果需要使用cornerRadius属性，请和[borderRadius](ts-universal-attributes-border.md#borderradius)属性一起使用。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| isModal11+ | boolean | 否 | 是 | 弹窗是否为模态窗口。值为true表示为模态窗口且有蒙层，不可与弹窗周围其他控件进行交互，即蒙层区域无法事件透传。值为false表示为非模态窗口且无蒙层，可以与弹窗周围其他控件进行交互。  默认值：true  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| onWillDismiss12+ | Callback<[DismissDialogAction](ts-methods-custom-dialog-box.md#dismissdialogaction12)> | 否 | 是 | 交互式关闭回调函数。  **说明：**  1.当用户执行点击遮障层关闭、侧滑（左滑/右滑）、三键back、键盘ESC关闭交互操作时，如果注册该回调函数，则不会立刻关闭弹窗。在回调函数中可以通过reason得到阻拦关闭弹窗的操作类型，从而根据原因选择是否能关闭弹窗。当前组件返回的reason中，暂不支持CLOSE\_BUTTON的枚举值。  2.在onWillDismiss回调中，不能再做onWillDismiss拦截。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| borderWidth12+ | [Dimension](ts-types.md#dimension10) | [EdgeWidths](ts-types.md#edgewidths9) | 否 | 是 | 设置弹窗背板的边框宽度。  可分别设置4个边框宽度。  默认值：0。  百分比参数方式：以父元素弹窗宽的百分比来设置弹窗的边框宽度。  当弹窗左边框和右边框大于弹窗宽度，弹窗上边框和下边框大于弹窗高度，显示可能不符合预期。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| borderColor12+ | [ResourceColor](ts-types.md#resourcecolor) | [EdgeColors](ts-types.md#edgecolors9) | 否 | 是 | 设置弹窗背板的边框颜色。  默认值：Color.Black  如果使用borderColor属性，需要和borderWidth属性一起使用。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| borderStyle12+ | [BorderStyle](ts-appendix-enums.md#borderstyle) | [EdgeStyles](ts-types.md#edgestyles9) | 否 | 是 | 设置弹窗背板的边框样式。  默认值：BorderStyle.Solid  如果使用borderStyle属性，需要和borderWidth属性一起使用。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| width12+ | [Dimension](ts-types.md#dimension10) | 否 | 是 | 设置弹窗背板的宽度。  **说明：**  - 弹窗宽度默认最大值：400vp。  - 百分比参数方式：弹窗参考宽度为所在窗口的宽度，在此基础上调小或调大。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| height12+ | [Dimension](ts-types.md#dimension10) | 否 | 是 | 设置弹窗背板的高度。  **说明：**  - 弹窗高度默认最大值：0.9 \*（窗口高度 - 安全区域）。  - 百分比参数方式：弹窗参考高度为（窗口高度 - 安全区域），在此基础上调小或调大。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| shadow12+ | [ShadowOptions](ts-universal-attributes-image-effect.md#shadowoptions对象说明) | [ShadowStyle](ts-universal-attributes-image-effect.md#shadowstyle10枚举说明) | 否 | 是 | 设置弹窗背板的阴影。  当设备为2in1时，默认场景下获焦阴影值为ShadowStyle.OUTER\_FLOATING\_MD，失焦为ShadowStyle.OUTER\_FLOATING\_SM。其他设备默认无阴影。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| backgroundBlurStyle12+ | [BlurStyle](ts-universal-attributes-background.md#blurstyle9) | 否 | 是 | 弹窗背板模糊材质。  默认值：BlurStyle.COMPONENT\_ULTRA\_THICK  **说明：**  设置为BlurStyle.NONE即可关闭背景虚化。当设置了backgroundBlurStyle为非NONE值时，则不要设置backgroundColor，否则颜色显示将不符合预期效果。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| backgroundBlurStyleOptions19+ | [BackgroundBlurStyleOptions](ts-universal-attributes-background.md#backgroundblurstyleoptions10对象说明) | 否 | 是 | 背景模糊效果。默认值请参考BackgroundBlurStyleOptions类型说明。  **元服务API：** 从API version 19开始，该接口支持在元服务中使用。 |
| backgroundEffect19+ | [BackgroundEffectOptions](ts-universal-attributes-background.md#backgroundeffectoptions11) | 否 | 是 | 背景效果参数。默认值请参考BackgroundEffectOptions类型说明。  **元服务API：** 从API version 19开始，该接口支持在元服务中使用。 |
| keyboardAvoidMode12+ | [KeyboardAvoidMode](ts-universal-attributes-popup.md#keyboardavoidmode12枚举说明) | 否 | 是 | 用于设置弹窗是否在拉起软键盘时进行自动避让。  默认值：KeyboardAvoidMode.DEFAULT  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| enableHoverMode14+ | boolean | 否 | 是 | 是否响应悬停态，值为true时，响应悬停态。  默认值：false，默认不响应。  **说明：**  PC/2in1设备弹窗默认显示在上半屏，在enableHoverMode设置为true时，可以通过设置hoverModeArea参数显示在下半屏。其他设备弹窗在enableHoverMode设置为true时默认显示在下半屏，可以通过设置hoverModeArea参数显示在上半屏。  **元服务API：** 从API version 14开始，该接口支持在元服务中使用。 |
| hoverModeArea14+ | [HoverModeAreaType](ts-universal-attributes-sheet-transition.md#hovermodeareatype14) | 否 | 是 | 悬停态下弹窗默认展示区域。  默认值：HoverModeAreaType.BOTTOM\_SCREEN。  **元服务API：** 从API version 14开始，该接口支持在元服务中使用。 |
| onWillAppear19+ | Callback<void> | 否 | 是 | 弹窗显示动效前的事件回调。  **说明：**  1.正常时序依次为：onWillAppear>>onDidAppear>>onWillDisappear>>onDidDisappear。  2.在onWillAppear内设置改变弹窗显示效果的回调事件，二次弹出生效。  **元服务API：** 从API version 19开始，该接口支持在元服务中使用。 |
| onDidAppear19+ | Callback<void> | 否 | 是 | 弹窗弹出后的事件回调。  **说明：**  1.正常时序依次为：onWillAppear>>onDidAppear>>onWillDisappear>>onDidDisappear。  2.在onDidAppear内设置改变弹窗显示效果的回调事件，二次弹出生效。  3.快速点击弹出，关闭弹窗时，onWillDisappear在onDidAppear前生效。  4.弹窗入场动效未完成时彻底关闭弹窗，动效打断，onDidAppear不会触发。  **元服务API：** 从API version 19开始，该接口支持在元服务中使用。 |
| onWillDisappear19+ | Callback<void> | 否 | 是 | 弹窗退出动效前的事件回调。  **说明：**  1.正常时序依次为：onWillAppear>>onDidAppear>>onWillDisappear>>onDidDisappear。  **元服务API：** 从API version 19开始，该接口支持在元服务中使用。 |
| onDidDisappear19+ | Callback<void> | 否 | 是 | 弹窗消失后的事件回调。  **说明：**  1.正常时序依次为：onWillAppear>>onDidAppear>>onWillDisappear>>onDidDisappear。  **元服务API：** 从API version 19开始，该接口支持在元服务中使用。 |
| keyboardAvoidDistance15+ | [LengthMetrics](js-apis-arkui-graphics.md#lengthmetrics12) | 否 | 是 | 弹窗避让键盘后，和键盘之间的距离。  **说明：**  - 默认值：16vp。  - 默认单位：vp。  - 当且仅当keyboardAvoidMode属性设置为DEFAULT时生效。  **元服务API：** 从API version 15开始，该接口支持在元服务中使用。 |
| levelMode15+ | [LevelMode](js-apis-promptaction.md#levelmode15枚举说明) | 否 | 是 | 设置弹窗显示层级。  **说明：**  - 默认值：LevelMode.OVERLAY。  - 当且仅当showInSubWindow属性设置为false时生效。  **元服务API：** 从API version 15开始，该接口支持在元服务中使用。 |
| levelUniqueId15+ | number | 否 | 是 | 设置页面级弹窗需要显示的层级下的[节点UniqueID](js-apis-arkui-framenode.md#getuniqueid12)。  取值范围：大于等于0的数字。  **说明：**  - 当且仅当levelMode属性设置为LevelMode.EMBEDDED时生效。  **元服务API：** 从API version 15开始，该接口支持在元服务中使用。 |
| immersiveMode15+ | [ImmersiveMode](js-apis-promptaction.md#immersivemode15枚举说明) | 否 | 是 | 设置页面内弹窗蒙层效果。  **说明：**  - 默认值：ImmersiveMode.DEFAULT  - 当且仅当levelMode属性设置为LevelMode.EMBEDDED时生效。  **元服务API：** 从API version 15开始，该接口支持在元服务中使用。 |
| levelOrder18+ | [LevelOrder](js-apis-promptaction.md#levelorder18) | 否 | 是 | 设置弹窗显示的顺序。  **说明：**  - 默认值：LevelOrder.clamp(0)  - 不支持动态刷新顺序。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| focusable19+ | boolean | 否 | 是 | 设置弹窗是否获取焦点。值为true表示获取焦点，值为false表示不获取焦点。  默认值：true  **说明：**  只有弹出覆盖在当前窗口之上的弹窗才可以获取焦点。  **元服务API：** 从API version 19开始，该接口支持在元服务中使用。 |

说明

* 按下返回键和ESC键时会让弹窗退出。
* 弹窗在避让软键盘时到达极限高度之后会压缩高度。

  需要注意：高度压缩生效在外层容器上，如果容器根节点中的子组件设置了较大的固定高度，由于容器默认不裁剪，依然可能存在超出屏幕显示的情况。
* 自定义弹窗仅适用于简单提示场景，不能替代页面使用。弹窗避让软键盘时，与软键盘之间存在16vp的安全间距。
* 为了达成良好的视觉体验，弹窗的显示和关闭存在默认动画，动画时长不同设备间可能存在差异。

  需要注意：在动画播放过程中，页面不响应触摸、滑动、点击操作。关闭默认弹窗动画效果可设置openAnimation和closeAnimation的duration为0。
* 当前，ArkUI弹出框默认为非页面级弹出框，在页面路由跳转时，如果开发者未调用close方法将其关闭，弹出框将不会自动关闭。若需实现在跳转页面时覆盖弹出框的场景，可以使用[组件导航子页面显示类型的弹窗类型](../harmonyos-guides/arkts-navigation-navdestination.md#页面显示类型)或者[页面级弹出框](../harmonyos-guides/arkts-embedded-dialog.md)。

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

## 示例

PhonePC/2in1TabletTVWearable

### 示例1（弹出嵌套弹窗）

该示例实现了在CustomDialog中打开另一个或另一些CustomDialog。

```
1. // xxx.ets
2. @CustomDialog
3. struct CustomDialogExampleTwo {
4. controllerTwo?: CustomDialogController;
5. build() {
6. Column() {
7. Text('我是第二个弹窗')
8. .fontSize(30)
9. .height(100)
10. Button('点我关闭第二个弹窗')
11. .onClick(() => {
12. if (this.controllerTwo != undefined) {
13. this.controllerTwo.close();
14. }
15. })
16. .margin(20)
17. }
18. }
19. }
20. @CustomDialog
21. @Component
22. struct CustomDialogExample {
23. @Link textValue: string;
24. @Link inputValue: string;
25. dialogControllerTwo: CustomDialogController | null = new CustomDialogController({
26. builder: CustomDialogExampleTwo(),
27. alignment: DialogAlignment.Bottom,
28. onWillDismiss:(dismissDialogAction: DismissDialogAction)=> {
29. console.info(`reason= ${dismissDialogAction.reason}`);
30. console.info('dialog onWillDismiss');
31. if (dismissDialogAction.reason == DismissReason.PRESS_BACK) {
32. dismissDialogAction.dismiss();
33. }
34. if (dismissDialogAction.reason == DismissReason.TOUCH_OUTSIDE) {
35. dismissDialogAction.dismiss();
36. }
37. },
38. offset: { dx: 0, dy: -25 } })
39. controller?: CustomDialogController;
40. // 若尝试在CustomDialog中传入多个其他的Controller，以实现在CustomDialog中打开另一个或另一些CustomDialog，那么此处需要将指向自己的controller放在所有controller的后面
41. cancel: () => void = () => {
42. }
43. confirm: () => void = () => {
44. }

46. build() {
47. Column() {
48. Text('Change text').fontSize(20).margin({ top: 10, bottom: 10 })
49. TextInput({ placeholder: '', text: this.textValue }).height(60).width('90%')
50. .onChange((value: string) => {
51. this.textValue = value;
52. })
53. Text('Whether to change a text?').fontSize(16).margin({ bottom: 10 })
54. Flex({ justifyContent: FlexAlign.SpaceAround }) {
55. Button('cancel')
56. .onClick(() => {
57. if (this.controller != undefined) {
58. this.controller.close();
59. this.cancel();
60. }
61. }).backgroundColor(0xffffff).fontColor(Color.Black)
62. Button('confirm')
63. .onClick(() => {
64. if (this.controller != undefined) {
65. this.inputValue = this.textValue;
66. this.controller.close();
67. this.confirm();
68. }
69. }).backgroundColor(0xffffff).fontColor(Color.Red)
70. }.margin({ bottom: 10 })

72. Button('点我打开第二个弹窗')
73. .onClick(() => {
74. if (this.dialogControllerTwo != null) {
75. this.dialogControllerTwo.open();
76. }
77. })
78. .margin(20)
79. }.borderRadius(10)
80. // 如果需要使用border属性或cornerRadius属性，请和borderRadius属性一起使用。
81. }
82. }
83. @Entry
84. @Component
85. struct CustomDialogUser {
86. @State textValue: string = ''
87. @State inputValue: string = 'click me'
88. dialogController: CustomDialogController | null = new CustomDialogController({
89. builder: CustomDialogExample({
90. cancel: ()=> { this.onCancel(); },
91. confirm: ()=> { this.onAccept(); },
92. textValue: this.textValue,
93. inputValue: this.inputValue
94. }),
95. cancel: this.exitApp,
96. autoCancel: true,
97. onWillDismiss:(dismissDialogAction: DismissDialogAction)=> {
98. console.info(`reason= ${dismissDialogAction.reason}`);
99. console.info('dialog onWillDismiss');
100. if (dismissDialogAction.reason == DismissReason.PRESS_BACK) {
101. dismissDialogAction.dismiss();
102. }
103. if (dismissDialogAction.reason == DismissReason.TOUCH_OUTSIDE) {
104. dismissDialogAction.dismiss();
105. }
106. },
107. alignment: DialogAlignment.Bottom,
108. offset: { dx: 0, dy: -20 },
109. gridCount: 4,
110. customStyle: false,
111. cornerRadius: 10,
112. })

114. // 在自定义组件即将析构销毁时将dialogController置空
115. aboutToDisappear() {
116. this.dialogController = null; // 将dialogController置空
117. }

119. onCancel() {
120. console.info('Callback when the first button is clicked');
121. }

123. onAccept() {
124. console.info('Callback when the second button is clicked');
125. }

127. exitApp() {
128. console.info('Click the callback in the blank area');
129. }
130. build() {
131. Column() {
132. Button(this.inputValue)
133. .onClick(() => {
134. if (this.dialogController != null) {
135. this.dialogController.open();
136. }
137. }).backgroundColor(0x317aff)
138. }.width('100%').margin({ top: 5 })
139. }
140. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d7/v3/btaXGB7OSeW-2Ife1zkrtA/zh-cn_image_0000002552960042.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000220Z&HW-CC-Expire=86400&HW-CC-Sign=FC5A7BED6BA1A921FB15558A483474758589835E236306F1E82AA102470C4964)

### 示例2（可在主窗外弹出的弹窗）

在2in1设备上设置[showInSubWindow](ts-methods-custom-dialog-box.md#customdialogcontrolleroptions对象说明)为true时，可以弹出在主窗外显示的弹窗。

```
1. // xxx.ets
2. @CustomDialog
3. struct CustomDialogExample {
4. controller?: CustomDialogController;
5. cancel: () => void = () => {
6. }
7. confirm: () => void = () => {
8. }
9. build() {
10. Column() {
11. Text('可展示在主窗口外的弹窗')
12. .fontSize(30)
13. .height(100)
14. Button('点我关闭弹窗')
15. .onClick(() => {
16. if (this.controller != undefined) {
17. this.controller.close();
18. }
19. })
20. .margin(20)
21. }
22. }
23. }
24. @Entry
25. @Component
26. struct CustomDialogUser {
27. dialogController: CustomDialogController | null = new CustomDialogController({
28. builder: CustomDialogExample({
29. cancel: ()=> { this.onCancel(); },
30. confirm: ()=> { this.onAccept(); }
31. }),
32. cancel: this.existApp,
33. autoCancel: true,
34. onWillDismiss:(dismissDialogAction: DismissDialogAction)=> {
35. console.info(`reason= ${dismissDialogAction.reason}`);
36. console.info('dialog onWillDismiss');
37. if (dismissDialogAction.reason == DismissReason.PRESS_BACK) {
38. dismissDialogAction.dismiss();
39. }
40. if (dismissDialogAction.reason == DismissReason.TOUCH_OUTSIDE) {
41. dismissDialogAction.dismiss();
42. }
43. },
44. alignment: DialogAlignment.Center,
45. offset: { dx: 0, dy: -20 },
46. gridCount: 4,
47. showInSubWindow: true,
48. isModal: true,
49. customStyle: false,
50. cornerRadius: 10,
51. focusable: true
52. })
53. // 在自定义组件即将析构销毁时将dialogController置空
54. aboutToDisappear() {
55. this.dialogController = null; // 将dialogController置空
56. }

58. onCancel() {
59. console.info('Callback when the first button is clicked');
60. }

62. onAccept() {
63. console.info('Callback when the second button is clicked');
64. }

66. existApp() {
67. console.info('Click the callback in the blank area');
68. }

70. build() {
71. Column() {
72. Button('click me')
73. .onClick(() => {
74. if (this.dialogController != null) {
75. this.dialogController.open();
76. }
77. }).backgroundColor(0x317aff)
78. }.width('100%').margin({ top: 5 })
79. }
80. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b8/v3/MDay8zJRRJKW_V0znMnLtQ/zh-cn_image_0000002583480043.jpg?HW-CC-KV=V1&HW-CC-Date=20260428T000220Z&HW-CC-Expire=86400&HW-CC-Sign=AFB3607EA5FA2734BB98478F5FC00DD9A43D246D4DEDD920D5F8DABC804D653A)

### 示例3（设置弹窗的样式）

该示例定义了CustomDialog的样式，包括宽度、高度、背景色、阴影等。

```
1. // xxx.ets
2. @CustomDialog
3. struct CustomDialogExample {
4. controller?: CustomDialogController;
5. cancel: () => void = () => {
6. }
7. confirm: () => void = () => {
8. }
9. build() {
10. Column() {
11. Text('这是自定义弹窗')
12. .fontSize(30)
13. .height(100)
14. Button('点我关闭弹窗')
15. .onClick(() => {
16. if (this.controller != undefined) {
17. this.controller.close();
18. }
19. })
20. .margin(20)
21. }
22. }
23. }
24. @Entry
25. @Component
26. struct CustomDialogUser {
27. dialogController: CustomDialogController | null = new CustomDialogController({
28. builder: CustomDialogExample({
29. cancel: ()=> { this.onCancel(); },
30. confirm: ()=> { this.onAccept(); }
31. }),
32. cancel: this.existApp,
33. autoCancel: true,
34. onWillDismiss:(dismissDialogAction: DismissDialogAction)=> {
35. console.info(`reason= ${dismissDialogAction.reason}`);
36. console.info('dialog onWillDismiss')
37. if (dismissDialogAction.reason == DismissReason.PRESS_BACK) {
38. dismissDialogAction.dismiss();
39. }
40. if (dismissDialogAction.reason == DismissReason.TOUCH_OUTSIDE) {
41. dismissDialogAction.dismiss();
42. }
43. },
44. alignment: DialogAlignment.Center,
45. offset: { dx: 0, dy: -20 },
46. customStyle: false,
47. cornerRadius: 20,
48. width: 300,
49. height: 200,
50. borderWidth: 1,
51. borderStyle: BorderStyle.Dashed,// 使用borderStyle属性，需要和borderWidth属性一起使用
52. borderColor: Color.Blue,// 使用borderColor属性，需要和borderWidth属性一起使用
53. backgroundColor: Color.White,
54. shadow: ({ radius: 20, color: Color.Grey, offsetX: 50, offsetY: 0}),
55. })
56. // 在自定义组件即将析构销毁时将dialogController置空
57. aboutToDisappear() {
58. this.dialogController = null; // 将dialogController置空
59. }

61. onCancel() {
62. console.info('Callback when the first button is clicked');
63. }

65. onAccept() {
66. console.info('Callback when the second button is clicked');
67. }

69. existApp() {
70. console.info('Click the callback in the blank area');
71. }

73. build() {
74. Column() {
75. Button('click me')
76. .onClick(() => {
77. if (this.dialogController != null) {
78. this.dialogController.open();
79. }
80. }).backgroundColor(0x317aff)
81. }.width('100%').margin({ top: 5 })
82. }
83. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8a/v3/fXMY2xpMQBCAsL0FtEXRGg/zh-cn_image_0000002552800394.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000220Z&HW-CC-Expire=86400&HW-CC-Sign=A40EE384BA2C857024B1715DE8FF1A86EA0E8E50A238875D92A6740026A0AE13)

### 示例4（悬停态弹窗）

该示例展示了在折叠屏悬停态下设置dialog布局区域的效果。

```
1. @CustomDialog
2. @Component
3. struct CustomDialogExample {
4. @Link textValue: string;
5. @Link inputValue: string;
6. controller?: CustomDialogController;

8. build() {
9. Column() {
10. Text('Change text').fontSize(20).margin({ top: 10, bottom: 10 })
11. TextInput({ placeholder: '', text: this.textValue }).height(60).width('90%')
12. .onChange((value: string) => {
13. this.textValue = value;
14. })
15. Text('Whether to change a text?').fontSize(16).margin({ bottom: 10 })
16. Flex({ justifyContent: FlexAlign.SpaceAround }) {
17. Button('cancel')
18. .onClick(() => {
19. if (this.controller != undefined) {
20. this.controller.close();
21. }
22. }).backgroundColor(0xffffff).fontColor(Color.Black)
23. Button('confirm')
24. .onClick(() => {
25. if (this.controller != undefined) {
26. this.inputValue = this.textValue;
27. this.controller.close();
28. }
29. }).backgroundColor(0xffffff).fontColor(Color.Red)
30. }.margin({ bottom: 10 })
31. }.borderRadius(10)
32. // 如果需要使用border属性或cornerRadius属性，请和borderRadius属性一起使用。
33. }
34. }
35. @Entry
36. @Component
37. struct CustomDialogUser {
38. @State textValue: string = '';
39. @State inputValue: string = 'click me';
40. dialogController: CustomDialogController | null = new CustomDialogController({
41. builder: CustomDialogExample({
42. textValue: this.textValue,
43. inputValue: this.inputValue
44. }),
45. cancel: this.exitApp,
46. autoCancel: true,
47. onWillDismiss: (dismissDialogAction: DismissDialogAction)=> {
48. console.info(`reason= ${dismissDialogAction.reason}`);
49. console.info('dialog onWillDismiss');
50. if (dismissDialogAction.reason == DismissReason.PRESS_BACK) {
51. dismissDialogAction.dismiss();
52. }
53. if (dismissDialogAction.reason == DismissReason.TOUCH_OUTSIDE) {
54. dismissDialogAction.dismiss();
55. }
56. },
57. alignment: DialogAlignment.Bottom,
58. offset: { dx: 0, dy: -20 },
59. gridCount: 4,
60. customStyle: false,
61. cornerRadius: 10,
62. enableHoverMode: true,
63. hoverModeArea: HoverModeAreaType.TOP_SCREEN
64. })

66. // 在自定义组件即将析构销毁时将dialogController置空
67. aboutToDisappear() {
68. this.dialogController = null; // 将dialogController置空
69. }

71. exitApp() {
72. console.info('Click the callback in the blank area');
73. }

75. build() {
76. Column() {
77. Button(this.inputValue)
78. .onClick(() => {
79. if (this.dialogController != null) {
80. this.dialogController.open();
81. }
82. }).backgroundColor(0x317aff)
83. }.width('100%').margin({ top: 5 })
84. }
85. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e2/v3/zXfAqa-sRqyWLNejEfA0Hg/zh-cn_image_0000002583440089.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000220Z&HW-CC-Expire=86400&HW-CC-Sign=7A3E3398FBD608F862C2A599EC2148AD16EB9CED4CD75EFE3F39856525F86B0B)

### 示例5（获取弹窗的状态）

该示例实现了在[CustomDialogController](ts-methods-custom-dialog-box.md#customdialogcontroller)中调用[getState](ts-methods-custom-dialog-box.md#getstate20)获取弹窗当前状态。

从API version 20开始，在CustomDialogController中新增了getState接口。

```
1. // xxx.ets
2. @CustomDialog
3. struct CustomDialogExample {
4. controller?: CustomDialogController

6. build() {
7. Column() {
8. Button("点我查询弹窗状态:通过自定义组件自带controller")
9. .onClick(() => {
10. if (this.getDialogController() != undefined) {
11. console.info('state:' + this.getDialogController().getState())
12. } else {
13. console.info('state: no exist')
14. }
15. }).margin(20)
16. Button('点我查询弹窗状态:通过CustomDialogController ')
17. .onClick(() => {
18. console.info('state:' + this.controller?.getState())
19. }).margin(20)
20. Button('点我关闭弹窗')
21. .onClick(() => {
22. if (this.getDialogController() != undefined) {
23. this.getDialogController().close()
24. }
25. }).margin(20)

27. }
28. }
29. }

31. @Entry
32. @Component
33. struct CustomDialogUser {
34. @State bg: ResourceColor = Color.Green
35. dialogController: CustomDialogController | null = new CustomDialogController({
36. builder: CustomDialogExample({
37. }),
38. autoCancel: false
39. })

41. build() {
42. Column() {
43. Button('click me')
44. .onClick(() => {
45. if (this.dialogController != null) {
46. this.dialogController.open()
47. }
48. }).backgroundColor(0x317aff)
49. }.width('100%').margin({ top: 5 })
50. .backgroundColor(this.bg)
51. }
52. }
```

### 示例6（使用@Link和@Consume监听数据变化）

该示例使用[@Link](../harmonyos-guides/arkts-link.md)和[@Consume](../harmonyos-guides/arkts-provide-and-consume.md)实现页面与弹窗内数据的双向绑定。

```
1. @CustomDialog
2. @Component
3. struct CustomDialogExample {
4. @Link textValue: string;
5. @Consume inputValue: string;
6. controller?: CustomDialogController;

8. cancel: () => void = () => {
9. }
10. confirm: () => void = () => {
11. }

13. build() {
14. Column() {
15. Text('Change text').fontSize(20).margin({ top: 10, bottom: 10 })
16. TextInput({ placeholder: '', text: this.textValue }).height(60).width('90%')
17. .onChange((value: string) => {
18. this.textValue = value;
19. })
20. Text('Whether to change a text?').fontSize(16).margin({ bottom: 10 })
21. Flex({ justifyContent: FlexAlign.SpaceAround }) {
22. Button('cancel')
23. .onClick(() => {
24. if (this.controller != undefined) {
25. this.controller.close();
26. this.cancel();
27. }
28. }).backgroundColor(0xffffff).fontColor(Color.Black)
29. Button('confirm')
30. .onClick(() => {
31. if (this.controller != undefined) {
32. this.inputValue = this.textValue;
33. this.controller.close();
34. this.confirm();
35. }
36. }).backgroundColor(0xffffff).fontColor(Color.Red)
37. }.margin({ bottom: 10 })
38. }.borderRadius(10)
39. }
40. }
41. @Entry
42. @Component
43. struct CustomDialogUser {
44. @State textValue: string = ''
45. @Provide inputValue: string = 'click me'
46. dialogController: CustomDialogController | null = new CustomDialogController({
47. builder: CustomDialogExample({
48. cancel: ()=> { this.onCancel(); },
49. confirm: ()=> { this.onAccept(); },
50. textValue: this.textValue
51. }),
52. cancel: this.exitApp,
53. autoCancel: true,
54. onWillDismiss:(dismissDialogAction: DismissDialogAction)=> {
55. if (dismissDialogAction.reason == DismissReason.PRESS_BACK) {
56. dismissDialogAction.dismiss();
57. }
58. if (dismissDialogAction.reason == DismissReason.TOUCH_OUTSIDE) {
59. dismissDialogAction.dismiss();
60. }
61. },
62. alignment: DialogAlignment.Center,
63. offset: { dx: 0, dy: -20 },
64. gridCount: 4,
65. customStyle: false,
66. cornerRadius: 10,
67. })

69. // 在自定义组件即将析构销毁时将dialogController置空
70. aboutToDisappear() {
71. this.dialogController = null; // 将dialogController置空
72. }

74. onCancel() {
75. console.info('Callback when the first button is clicked');
76. }

78. onAccept() {
79. console.info('Callback when the second button is clicked');
80. }

82. exitApp() {
83. console.info('Click the callback in the blank area');
84. }
85. build() {
86. Column() {
87. Button(this.inputValue)
88. .onClick(() => {
89. if (this.dialogController != null) {
90. this.dialogController.open();
91. }
92. }).backgroundColor(0x317aff)
93. }.width('100%').margin({ top: 5 })
94. }
95. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f0/v3/UTS8LHeZShS3pOzTtXVqcQ/zh-cn_image_0000002552960044.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000220Z&HW-CC-Expire=86400&HW-CC-Sign=16FF9C69A433D37412FF5B5097010E50908EE7A406741EEE20806400E2814E1E)

### 示例7（自定义带loading的弹窗）

该示例使用[maskColor](ts-methods-custom-dialog-box.md#customdialogcontrolleroptions对象说明)，[maskRect](ts-methods-custom-dialog-box.md#customdialogcontrolleroptions对象说明)和[LoadingProgress](ts-basic-components-loadingprogress.md)，实现带loading的弹窗，并展示不在maskRect区域的事件透传效果。

```
1. import { window } from '@kit.ArkUI';

3. @CustomDialog
4. @Component
5. struct LoadingDialogExample {
6. controller?: CustomDialogController;
7. cancel: () => void = () => {
8. }
9. confirm: () => void = () => {
10. }

12. build() {
13. Column() {
14. LoadingProgress().color(Color.Blue).layoutWeight(1)
15. }.borderRadius(10).width(100).height(100)
16. }
17. }

19. @Entry
20. @Component
21. struct CustomDialogUser {
22. @State number: number = 0;
23. dialogController: CustomDialogController | null = null;

25. // 在自定义组件即将析构销毁时将dialogController置空
26. aboutToDisappear() {
27. this.dialogController = null; // 将dialogController置空
28. }

30. onCancel() {
31. console.info('Callback when the first button is clicked');
32. }

34. onAccept() {
35. console.info('Callback when the second button is clicked');
36. }

38. exitApp() {
39. console.info('Click the callback in the blank area');
40. }

42. build() {
43. Column() {
44. Button("click " + this.number).onClick(() => {
45. this.number++;
46. })
47. Button("show loading dialog").onClick(() => {
48. // 获取窗口对象
49. let windowClass = window.getLastWindow(this.getUIContext().getHostContext());
50. windowClass.then(window => {
51. // 获取窗口信息，设置maskRect
52. let properties = window.getWindowProperties();
53. let maskRect = {
54. x: this.getUIContext().px2vp(properties.windowRect.left + 150),
55. y: this.getUIContext().px2vp(properties.windowRect.top + 350),
56. width: this.getUIContext().px2vp(properties.windowRect.width - 300),
57. height: this.getUIContext().px2vp(properties.windowRect.height - 700)
58. } as Rectangle
59. if (this.dialogController == null) {
60. this.dialogController = new CustomDialogController({
61. builder: LoadingDialogExample({
62. cancel: () => {
63. this.onCancel();
64. },
65. confirm: () => {
66. this.onAccept();
67. },
68. }),
69. cancel: this.exitApp,
70. maskRect: maskRect,
71. autoCancel: false,
72. maskColor: "#33AA0000",
73. showInSubWindow: false,
74. backgroundBlurStyle: BlurStyle.NONE,
75. onWillDismiss: (dismissDialogAction: DismissDialogAction) => {
76. if (dismissDialogAction.reason == DismissReason.PRESS_BACK) {
77. dismissDialogAction.dismiss();
78. }
79. if (dismissDialogAction.reason == DismissReason.TOUCH_OUTSIDE) {
80. dismissDialogAction.dismiss();
81. }
82. },
83. alignment: DialogAlignment.Center,
84. customStyle: false,
85. cornerRadius: 10,
86. openAnimation: { duration: 0, tempo: 0 },
87. closeAnimation: { duration: 0, tempo: 0 }
88. })
89. }
90. this.dialogController.close();
91. this.dialogController.open();
92. })
93. }).backgroundColor(0x317aff)
94. }.width('100%').margin({ top: 5 })
95. }
96. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/db/v3/Qsb-KwszSLaas05R2AKFig/zh-cn_image_0000002583480045.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000220Z&HW-CC-Expire=86400&HW-CC-Sign=CE799955181D2CC1E2A7C89C5E66EB624BBA2A99769849448CA5FCFD0B4668D7)

### 示例8（不使用keyboardAvoidDistance调整弹窗与软键盘的间距）

该示例通过监听键盘变化，调整布局[margin](ts-universal-attributes-size.md#margin)的[bottom](ts-types.md#margin)，实现与使用[keyboardAvoidDistance](ts-methods-custom-dialog-box.md#customdialogcontrolleroptions对象说明)调整弹窗与软键盘的间距一样的效果。

从API version 15开始，在CustomDialogControllerOptions中新增了keyboardAvoidDistance属性。

```
1. import { window } from '@kit.ArkUI';

3. @CustomDialog
4. @Component
5. struct CustomDialogExample {
6. @Link textValue: string;
7. @Link inputValue: string;
8. @Link isKeyboardShow: boolean
9. @Link navigationBarHeight: number
10. controller?: CustomDialogController;
11. cancel: () => void = () => {
12. }
13. confirm: () => void = () => {
14. }

16. build() {
17. Column() {
18. Text('Change text').fontSize(20).margin({ top: 10, bottom: 10 })
19. TextInput({ placeholder: '', text: this.textValue }).height(60).width('90%')
20. .onChange((value: string) => {
21. this.textValue = value;
22. })
23. Text('Whether to change a text?').fontSize(16).margin({ bottom: 10 })
24. Flex({ justifyContent: FlexAlign.SpaceAround }) {
25. Button('cancel')
26. .onClick(() => {
27. if (this.controller != undefined) {
28. this.controller.close();
29. this.cancel();
30. }
31. }).backgroundColor(0xffffff).fontColor(Color.Black)
32. Button('confirm')
33. .onClick(() => {
34. if (this.controller != undefined) {
35. this.inputValue = this.textValue;
36. this.controller.close();
37. this.confirm();
38. }
39. }).backgroundColor(0xffffff).fontColor(Color.Red)
40. }.margin({ bottom: 10 })
41. }.borderRadius(10)
42. .margin({
43. // 通过键盘显隐调整间距（键盘与弹窗间距为16vp）
44. bottom: this.isKeyboardShow ? -16 : this.navigationBarHeight
45. }).backgroundColor(Color.White)
46. }
47. }

49. @Entry
50. @Component
51. struct CustomDialogUser {
52. @State textValue: string = ''
53. @State inputValue: string = 'click me'
54. @State isKeyboardShow: boolean = false
55. @State navigationBarHeight: number = 0
56. windowClass: window.Window | null = null
57. dialogController: CustomDialogController | null = new CustomDialogController({
58. builder: CustomDialogExample({
59. cancel: () => {
60. this.onCancel();
61. },
62. confirm: () => {
63. this.onAccept();
64. },
65. textValue: this.textValue,
66. inputValue: this.inputValue,
67. isKeyboardShow: this.isKeyboardShow,
68. navigationBarHeight: this.navigationBarHeight
69. }),
70. cancel: this.exitApp,
71. autoCancel: true,
72. onWillDismiss: (dismissDialogAction: DismissDialogAction) => {
73. if (dismissDialogAction.reason == DismissReason.PRESS_BACK) {
74. dismissDialogAction.dismiss();
75. }
76. if (dismissDialogAction.reason == DismissReason.TOUCH_OUTSIDE) {
77. dismissDialogAction.dismiss();
78. }
79. },
80. alignment: DialogAlignment.Bottom,
81. customStyle: true,
82. cornerRadius: 10,
83. })

85. aboutToAppear(): void {
86. let windowClass = window.getLastWindow(this.getUIContext().getHostContext());
87. windowClass.then(win => {
88. this.windowClass = win;
89. // 获取底部导航栏高度
90. let navigationArea = this.windowClass?.getWindowAvoidArea(window.AvoidAreaType.TYPE_NAVIGATION_INDICATOR);
91. this.navigationBarHeight = navigationArea.bottomRect.height;
92. this.windowClass?.on('avoidAreaChange', (data) => {
93. if (data.type == window.AvoidAreaType.TYPE_KEYBOARD) {
94. this.isKeyboardShow = data.area.bottomRect.height > 0;
95. }
96. })
97. });
98. }

100. // 在自定义组件即将析构销毁时将dialogController置空
101. aboutToDisappear() {
102. this.dialogController = null; // 将dialogController置空
103. this.windowClass?.off('avoidAreaChange')
104. }

106. onCancel() {
107. console.info('Callback when the first button is clicked');
108. }

110. onAccept() {
111. console.info('Callback when the second button is clicked');
112. }

114. exitApp() {
115. console.info('Click the callback in the blank area');
116. }

118. build() {
119. Column() {
120. Button(this.inputValue)
121. .onClick(() => {
122. if (this.dialogController != null) {
123. this.dialogController.open();
124. }
125. }).backgroundColor(0x317aff)
126. }.width('100%').margin({ top: 5 })
127. }
128. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f/v3/t9HpkisTR9CczFeMLBN8ow/zh-cn_image_0000002552800396.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000220Z&HW-CC-Expire=86400&HW-CC-Sign=4E2E50F06C344A4EF241A2CDF1FB51E5359CF45758C178D853A0FE1E0D2BED6A)

### 示例9（弹窗生命周期）

该示例为弹窗配置生命周期回调。

从API version 19开始，在[CustomDialogControllerOptions](ts-methods-custom-dialog-box.md#customdialogcontrolleroptions对象说明)中新增了onDidAppear、onDidDisappear、onWillAppear和onWillDisappear属性。

```
1. // xxx.ets
2. @CustomDialog
3. struct CustomDialogExample1 {
4. controller?: CustomDialogController
5. cancel: () => void = () => {
6. }
7. confirm: () => void = () => {
8. }
9. build() {
10. Column() {
11. Text('允许访问相机？')
12. .fontSize(30)
13. .height(100)
14. Button('点我关闭弹窗')
15. .onClick(() => {
16. if (this.controller != undefined) {
17. this.controller.close();
18. }
19. })
20. .margin(20)
21. }
22. }
23. }

25. @Entry
26. @Component
27. struct Example3 {
28. @State log: string = 'Log information:';
29. dialogController: CustomDialogController | null = new CustomDialogController({
30. builder: CustomDialogExample1({
31. cancel: ()=> { this.onCancel(); },
32. confirm: ()=> { this.onAccept(); }
33. }),
34. cancel: this.existApp,
35. autoCancel: true,
36. alignment: DialogAlignment.Bottom,
37. onWillDismiss:(dismissDialogAction: DismissDialogAction)=> {
38. console.info(`reason= ${dismissDialogAction.reason}`);
39. console.info('dialog onWillDismiss');
40. if (dismissDialogAction.reason == DismissReason.PRESS_BACK) {
41. dismissDialogAction.dismiss();
42. }
43. if (dismissDialogAction.reason == DismissReason.TOUCH_OUTSIDE) {
44. dismissDialogAction.dismiss();
45. }
46. },
47. onDidAppear: () => {
48. this.log += '# onDidAppear';
49. console.info('CustomDialog,is onDidAppear!');
50. },
51. onDidDisappear: () => {
52. this.log += '# onDidDisappear';
53. console.info('CustomDialog,is onDidDisappear!');
54. },
55. onWillAppear: () => {
56. this.log = 'Log information:onWillAppear';
57. console.info('CustomDialog,is onWillAppear!');
58. },
59. onWillDisappear: () => {
60. this.log += '# onWillDisappear';
61. console.info('CustomDialog,is onWillDisappear!');
62. },
63. offset: { dx: 0, dy: -20 },
64. customStyle: false,
65. })
66. onCancel() {
67. console.info('CustomDialog Callback when the first button is clicked');
68. }

70. onAccept() {
71. console.info('CustomDialog Callback when the second button is clicked');
72. }

74. existApp() {
75. console.info('CustomDialog Click the callback in the blank area');
76. }
77. build() {
78. Column({ space: 5 }) {
79. Button('CustomDialog')
80. .onClick(() => {
81. this.dialogController?.open();
82. })
83. Text(this.log).fontSize(30).margin({ top: 200 })
84. }.width('100%').margin({ top: 5 })
85. }
86. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/_MV-G1CKTcm-hbSkTxx5Ow/zh-cn_image_0000002583440091.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000220Z&HW-CC-Expire=86400&HW-CC-Sign=A724B609A3A718B1775450F3BBF7C035DFF76A9C9F9775A64A06CE376B33B821)

### 示例10（不同customStyle下的弹窗示例）

该示例是在对齐方式为[DialogAlignment.Bottom](ts-methods-custom-dialog-box.md#customdialogcontrolleroptions对象说明)时，展示[customStyle](ts-methods-custom-dialog-box.md#customdialogcontrolleroptions对象说明)不同值下，弹窗内容与安全区域的效果。

```
1. @CustomDialog
2. @Component
3. struct CustomStyleDialogExample {
4. controller?: CustomDialogController;
5. cancel: () => void = () => {
6. }
7. confirm: () => void = () => {
8. }

10. build() {
11. Column().borderRadius(10).width(110).height(110).backgroundColor("#2787d9")
12. }
13. }

15. @Entry
16. @Component
17. struct CustomDialogUser {
18. @State customStyle: boolean = false;
19. dialogController: CustomDialogController | null = null;

21. // 在自定义组件即将析构销毁时将dialogController置空
22. aboutToDisappear() {
23. this.dialogController = null; // 将dialogController置空
24. }

26. onCancel() {
27. console.info('Callback when the first button is clicked');
28. }

30. onAccept() {
31. console.info('Callback when the second button is clicked');
32. }

34. exitApp() {
35. console.info('Click the callback in the blank area');
36. }

38. build() {
39. Column() {
40. Button('change  customStyle:' + this.customStyle).onClick(() => {
41. this.customStyle = !this.customStyle;
42. })
43. Button('show dialog').onClick(() => {
44. if (this.dialogController != null) {
45. this.dialogController.close();
46. }
47. this.dialogController = new CustomDialogController({
48. builder: CustomStyleDialogExample({
49. cancel: () => {
50. this.onCancel();
51. },
52. confirm: () => {
53. this.onAccept();
54. },
55. }),
56. cancel: this.exitApp,
57. autoCancel: true,
58. showInSubWindow: false,
59. onWillDismiss: (dismissDialogAction: DismissDialogAction) => {
60. if (dismissDialogAction.reason == DismissReason.PRESS_BACK) {
61. dismissDialogAction.dismiss();
62. }
63. if (dismissDialogAction.reason == DismissReason.TOUCH_OUTSIDE) {
64. dismissDialogAction.dismiss();
65. }
66. },
67. alignment: DialogAlignment.Bottom,
68. customStyle: this.customStyle,
69. cornerRadius: 10,
70. openAnimation: { duration: 0, tempo: 0 },
71. closeAnimation: { duration: 0, tempo: 0 }
72. })
73. this.dialogController.open();
74. }).margin({ top: 5 })
75. }.width('100%').margin({ top: 5 })
76. }
77. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/63/v3/AAofjLiLSWeAgb5zZk5Q-g/zh-cn_image_0000002552960046.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000220Z&HW-CC-Expire=86400&HW-CC-Sign=0280A8033D2B2CA46585C1F322804CF8C532E8609EB02A1A9B04B15D945711A7)

### 示例11（自定义背景模糊效果参数）

该示例通过配置[backgroundBlurStyleOptions](ts-methods-custom-dialog-box.md#customdialogcontrolleroptions对象说明)，实现自定义背景模糊效果。

从API version 19开始，在[CustomDialogControllerOptions](ts-methods-custom-dialog-box.md#customdialogcontrolleroptions对象说明)中新增了backgroundBlurStyleOptions属性。

```
1. @CustomDialog
2. struct CustomDialogExample {
3. controller?: CustomDialogController;

5. build() {
6. Column() {
7. Text('这是自定义弹窗')
8. .fontSize(30)
9. .height(100)
10. Button('点我关闭弹窗')
11. .onClick(() => {
12. if (this.controller != undefined) {
13. this.controller.close();
14. }
15. })
16. .margin(20)
17. }
18. }
19. }

21. @Entry
22. @Component
23. struct CustomDialogUser {
24. dialogController: CustomDialogController | null = new CustomDialogController({
25. builder: CustomDialogExample(),
26. backgroundColor: undefined,
27. backgroundBlurStyle: BlurStyle.Thin,
28. backgroundBlurStyleOptions: {
29. colorMode: ThemeColorMode.LIGHT,
30. adaptiveColor: AdaptiveColor.AVERAGE,
31. scale: 1,
32. blurOptions: { grayscale: [20, 20] },
33. },
34. })

36. build() {
37. Stack({ alignContent: Alignment.Top }) {
38. // $r('app.media.bg')需要替换为开发者所需的图像资源文件。
39. Image($r('app.media.bg'))
40. Column() {
41. Button('CustomDialog')
42. .margin(20)
43. .onClick(() => {
44. if (this.dialogController != null) {
45. this.dialogController.open();
46. }
47. })
48. }.width('100%')
49. }
50. }
51. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6e/v3/WfNN56enTYq0E-AVka0reA/zh-cn_image_0000002583480047.png?HW-CC-KV=V1&HW-CC-Date=20260428T000220Z&HW-CC-Expire=86400&HW-CC-Sign=A702FB5A5EB9E091DFCF0419A8F1E3D2AC199467B4AE26C7ADE0A8944AC4888B)

### 示例12（自定义背景效果参数）

该示例通过配置[backgroundEffect](ts-methods-custom-dialog-box.md#customdialogcontrolleroptions对象说明)，实现自定义背景效果。

从API version 19开始，在[CustomDialogControllerOptions](ts-methods-custom-dialog-box.md#customdialogcontrolleroptions对象说明)中新增了backgroundEffect属性。

```
1. @CustomDialog
2. struct CustomDialogExample {
3. controller?: CustomDialogController;

5. build() {
6. Column() {
7. Text('这是自定义弹窗')
8. .fontSize(30)
9. .height(100)
10. Button('点我关闭弹窗')
11. .onClick(() => {
12. if (this.controller != undefined) {
13. this.controller.close();
14. }
15. })
16. .margin(20)
17. }
18. }
19. }

21. @Entry
22. @Component
23. struct CustomDialogUser {
24. dialogController: CustomDialogController | null = new CustomDialogController({
25. builder: CustomDialogExample(),
26. backgroundColor: undefined,
27. backgroundBlurStyle: BlurStyle.Thin,
28. backgroundEffect: {
29. radius: 60,
30. saturation: 0,
31. brightness: 1,
32. color: Color.White,
33. blurOptions: { grayscale: [20, 20] }
34. },
35. })

37. build() {
38. Stack({ alignContent: Alignment.Top }) {
39. // $r('app.media.bg')需要替换为开发者所需的图像资源文件。
40. Image($r('app.media.bg'))
41. Column() {
42. Button('CustomDialog')
43. .margin(20)
44. .onClick(() => {
45. if (this.dialogController != null) {
46. this.dialogController.open();
47. }
48. })
49. }.width('100%')
50. }
51. }
52. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a6/v3/CbfAfGXrQz6c6zqUClN9rQ/zh-cn_image_0000002552800398.png?HW-CC-KV=V1&HW-CC-Date=20260428T000220Z&HW-CC-Expire=86400&HW-CC-Sign=38D82B9DBB303866CE043B190EE066B0F48B32219D64565343073B19BBA12954)

### 示例13（自定义弹窗动态刷新宽度）

该示例通过状态变量同步自定义组件的宽度，实现自定义弹窗宽度动态切换。

```
1. @CustomDialog
2. struct CustomDialogExample {
3. controller?: CustomDialogController;
4. @Link currentWidth: number;

6. build() {
7. Column() {
8. Text('这是自定义弹窗')
9. .fontSize(30)
10. .height(100)
11. Button('点我关闭弹窗')
12. .onClick(() => {
13. if (this.controller != undefined) {
14. this.controller.close();
15. }
16. })
17. .margin(20)
18. }
19. .borderRadius(32)
20. .backgroundColor(Color.White)
21. .shadow(ShadowStyle.OUTER_DEFAULT_SM)
22. .width(this.currentWidth + "%")
23. }
24. }

26. @Entry
27. @Component
28. struct CustomDialogUser {
29. @State currentWidth: number = 0
30. dialogController: CustomDialogController | null = new CustomDialogController({
31. builder: CustomDialogExample({ currentWidth: this.currentWidth }),
32. customStyle: true,
33. isModal: false,
34. })

36. build() {
37. Column() {

39. Row() {
40. Text("宽度设置：")
41. .height(50)
42. Slider({ min: 60, max: 100, step: 5 })
43. .showTips(true, this.currentWidth + '%')
44. .onChange((value: number, mode: SliderChangeMode) => {
45. this.currentWidth = value;
46. }).width(200)
47. }

49. Button('CustomDialog')
50. .margin(20)
51. .onClick(() => {
52. if (this.dialogController != null) {
53. this.dialogController.open();
54. }
55. })
56. }.width('100%')
57. }
58. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/84/v3/vEaY-Y5GTkan4Io0RxpUWQ/zh-cn_image_0000002583440093.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000220Z&HW-CC-Expire=86400&HW-CC-Sign=BEE6B4ED526B1F8471AAA15BA9AF879E1ECE1207328D1D384642B2607B1343E5)
