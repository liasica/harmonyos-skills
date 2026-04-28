---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-promptaction
title: @ohos.promptAction (弹窗)
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS API > UI界面 > @ohos.promptAction (弹窗)
category: harmonyos-references
scraped_at: 2026-04-28T08:00:33+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:7722c6f281fe6cabb6d07d71d1b7d473bbbc876b8694679bc492f590768cda82
---

创建并显示即时反馈、对话框和操作菜单。

说明

* 本模块首批接口从API version 9开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 本模块不支持在[UIAbility](js-apis-app-ability-uiability.md)的文件声明处使用，即不能在UIAbility的生命周期中调用，需要在创建组件实例后使用。
* 本模块功能依赖UI的执行上下文，不可在[UI上下文不明确](../harmonyos-guides/arkts-global-interface.md#ui上下文不明确)的地方使用，参见[UIContext](arkts-apis-uicontext-uicontext.md)说明。建议使用UIContext中的弹窗方法。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { promptAction } from '@kit.ArkUI';
```

## promptAction.openToast18+

PhonePC/2in1TabletTVWearable

openToast(options: ShowToastOptions): Promise<number>

显示即时反馈并通过Promise返回其id。

说明

* 不支持在输入法类型窗口中使用子窗（showMode设置为TOP\_MOST或者SYSTEM\_TOP\_MOST）的openToast，详情见输入法框架的约束与限制说明[createPanel](js-apis-inputmethodengine.md#createpanel10-1)。
* 直接使用openToast可能导致[UI上下文不明确](../harmonyos-guides/arkts-global-interface.md#ui上下文不明确)的问题，建议使用UIContext中的getPromptAction方法获取到PromptAction对象，再通过该对象调用[openToast](arkts-apis-uicontext-promptaction.md#opentoast18)实现。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [ShowToastOptions](js-apis-promptaction.md#showtoastoptions) | 是 | Toast选项。 |

**返回值**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | 返回即时反馈的id，可供closeToast使用。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[接口调用异常错误码](errorcode-internal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |
| 100001 | Internal error. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { PromptAction, UIContext } from '@kit.ArkUI';

4. @Entry
5. @Component
6. struct toastExample {
7. @State toastId: number = 0;
8. uiContext: UIContext = this.getUIContext();
9. promptAction: PromptAction = this.uiContext.getPromptAction();

11. build() {
12. Column() {
13. Button('Open Toast')
14. .height(100)
15. .type(ButtonType.Capsule)
16. .onClick(() => {
17. this.promptAction.openToast({
18. message: 'Toast Message',
19. duration: 10000,
20. }).then((toastId: number) => {
21. this.toastId = toastId;
22. })
23. .catch((error: BusinessError) => {
24. console.error(`openToast error code is ${error.code}, message is ${error.message}`);
25. })
26. })
27. Blank().height(50)
28. Button('Close Toast')
29. .height(100)
30. .type(ButtonType.Capsule)
31. .onClick(() => {
32. try {
33. this.promptAction.closeToast(this.toastId);
34. } catch (error) {
35. let message = (error as BusinessError).message;
36. let code = (error as BusinessError).code;
37. console.error(`CloseToast error code is ${code}, message is ${message}`);
38. }
39. })
40. }.height('100%').width('100%').justifyContent(FlexAlign.Center)
41. }
42. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4e/v3/wyNmCS4RS8a-y6Z00BNVvw/zh-cn_image_0000002552799774.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000030Z&HW-CC-Expire=86400&HW-CC-Sign=1B861971270F9656825EC2B45FBA53199817908F23CB187B227773C44341B899)

## promptAction.closeToast18+

PhonePC/2in1TabletTVWearable

closeToast(toastId: number): void

关闭即时反馈。

说明

直接使用closeToast可能导致[UI上下文不明确](../harmonyos-guides/arkts-global-interface.md#ui上下文不明确)的问题，建议使用UIContext中的getPromptAction方法获取到PromptAction对象，再通过该对象调用[closeToast](arkts-apis-uicontext-promptaction.md#closetoast18)实现。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| toastId | number | 是 | openToast返回的id。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)、[弹窗错误码](errorcode-promptaction.md)和[接口调用异常错误码](errorcode-internal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |
| 100001 | Internal error. |
| 103401 | Cannot find the toast. |

**示例：**

示例请看[promptAction.openToast18](js-apis-promptaction.md#promptactionopentoast18)的示例。

## ShowToastOptions

PhonePC/2in1TabletTVWearable

Toast的选项。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| message | string | [Resource](ts-types.md#resource) | 否 | 否 | 显示的文本信息。  **说明：**  默认字体为'Harmony Sans'，不支持设置其他字体。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| duration | number | 否 | 是 | 设置Toast弹出的持续时间。  默认值：1500ms  取值范围：[1500, 10000]  若小于1500ms则取默认值，若大于10000ms则取上限值10000ms。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| bottom | string | number | 否 | 是 | 设置Toast底部边框距离导航条的高度，软键盘拉起时，如果bottom值过小，Toast要被软键盘遮挡时，会自动避让至距离软键盘80vp处。  默认值：80vp  **说明：**  当底部没有导航条时，bottom为设置弹窗底部边框距离窗口底部的高度。  设置对齐方式alignment后，bottom不生效。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| alignment12+ | [Alignment](ts-appendix-enums.md#alignment) | 否 | 是 | 对齐方式。  默认值：undefined，当未设置alignment且存在导航条或软键盘时，Toast会自动根据导航条或软键盘位置进行调整，可参考bottom的说明。  **说明：**  不同alignment下，Toast位置对齐效果，如下图所示。    Toast的文本显示默认自左向右，不支持其他对齐方式。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| offset12+ | [Offset](ts-types.md#offset) | 否 | 是 | 在对齐方式上的偏移。  默认值：{ dx: 0, dy: 0 }，默认没有偏移。  **说明：**  仅支持设置px类型的数值。如需设置其他类型的数值，应将其他类型转换为px类型后传入。例如，若需设置vp，应将其转换为px后传入。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| showMode11+ | [ToastShowMode](js-apis-promptaction.md#toastshowmode11) | 否 | 是 | 设置Toast层级。  默认值：ToastShowMode.DEFAULT，默认显示在应用内。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| backgroundColor12+ | [ResourceColor](ts-types.md#resourcecolor) | 否 | 是 | Toast的背板颜色。  默认值：Color.Transparent  **说明：**  backgroundColor会与模糊属性backgroundBlurStyle叠加产生效果，如果不符合预期，可将backgroundBlurStyle设置为BlurStyle.NONE，即可取消模糊。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| textColor12+ | [ResourceColor](ts-types.md#resourcecolor) | 否 | 是 | Toast的文本颜色。  默认值：Color.Black  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| backgroundBlurStyle12+ | [BlurStyle](ts-universal-attributes-background.md#blurstyle9) | 否 | 是 | Toast的背板模糊材质。  默认值：BlurStyle.COMPONENT\_ULTRA\_THICK  **说明：**  设置为BlurStyle.NONE即可关闭背景虚化。当设置了backgroundBlurStyle为非NONE值时，则不要设置backgroundColor，否则颜色显示将不符合预期效果。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| shadow12+ | [ShadowOptions](ts-universal-attributes-image-effect.md#shadowoptions对象说明) | [ShadowStyle](ts-universal-attributes-image-effect.md#shadowstyle10枚举说明) | 否 | 是 | Toast的背板阴影。  默认值：ShadowStyle.OUTER\_DEFAULT\_MD  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| enableHoverMode14+ | boolean | 否 | 是 | 是否响应悬停态，值为true时，响应悬停态。  默认值：false，默认不响应。  **元服务API：** 从API version 14开始，该接口支持在元服务中使用。 |
| hoverModeArea14+ | [HoverModeAreaType](ts-universal-attributes-sheet-transition.md#hovermodeareatype14) | 否 | 是 | 响应悬停态时，弹窗的显示区域。  默认值：HoverModeAreaType.BOTTOM\_SCREEN，默认显示在下半屏。  **元服务API：** 从API version 14开始，该接口支持在元服务中使用。 |

## ToastShowMode11+

PhonePC/2in1TabletTVWearable

设置Toast的显示模式，默认显示在应用内，支持显示在子窗。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| DEFAULT | 0 | Toast显示在应用内。 |
| TOP\_MOST | 1 | Toast显示在子窗。 |

## ShowDialogOptions

PhonePC/2in1TabletTVWearable

对话框的选项。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| title | string | [Resource](ts-types.md#resource) | 否 | 是 | 标题文本。  默认值：undefined，取值为undefined默认不显示标题。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| message | string | [Resource](ts-types.md#resource) | 否 | 是 | 内容文本。  默认值：undefined，取值为undefined默认不显示内容。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| buttons | Array<[Button](js-apis-promptaction.md#button)> | 否 | 是 | 对话框中按钮的数组，结构为：{text:'button', color: '#666666'}，支持大于1个按钮。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| alignment10+ | [DialogAlignment](ts-methods-alert-dialog-box.md#dialogalignment枚举说明) | 否 | 是 | 对话框在竖直方向上的对齐方式。  默认值：DialogAlignment.Default  **说明：**  若在UIExtension中设置showInSubWindow为true, 弹窗将基于UIExtension的宿主窗口对齐。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| offset10+ | [Offset](ts-types.md#offset) | 否 | 是 | 对话框相对alignment所在位置的偏移量。  默认值：{ dx: 0 , dy: 0 }  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| maskRect10+ | [Rectangle](ts-methods-alert-dialog-box.md#rectangle8类型说明) | 否 | 是 | 对话框遮蔽层区域，在遮蔽层区域内的事件不透传，在遮蔽层区域外的事件透传。  默认值：{ x: 0, y: 0, width: '100%', height: '100%' }  **说明：**  showInSubWindow为true时，maskRect不生效。  maskRect在设置[Rectangle](ts-methods-alert-dialog-box.md#rectangle8类型说明)中的部分属性后，若未设置其余的属性，则其余属性的默认值为0。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| showInSubWindow11+ | boolean | 否 | 是 | 某对话框需要显示在主窗口之外时，是否在子窗口显示此对话框。值为true表示在子窗口显示对话框。  默认值：false，对话框显示在应用内，而非独立子窗口。  **说明：** showInSubWindow为true的对话框无法触发显示另一个showInSubWindow为true的对话框。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| isModal11+ | boolean | 否 | 是 | 对话框是否为模态窗口。值为true表示为模态窗口且有蒙层，不可与对话框周围其他控件进行交互，即蒙层区域无法事件透传。值为false表示为非模态窗口且无蒙层，可以与对话框周围其他控件进行交互。  默认值：true  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| backgroundColor12+ | [ResourceColor](ts-types.md#resourcecolor) | 否 | 是 | 对话框背板颜色。  默认值：Color.Transparent  **说明：**  backgroundColor会与模糊属性backgroundBlurStyle叠加产生效果，如果不符合预期，可将backgroundBlurStyle设置为BlurStyle.NONE，即可取消模糊。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| backgroundBlurStyle12+ | [BlurStyle](ts-universal-attributes-background.md#blurstyle9) | 否 | 是 | 对话框背板模糊材质。  默认值：BlurStyle.COMPONENT\_ULTRA\_THICK  **说明：**  设置为BlurStyle.NONE即可关闭背景虚化。当设置了backgroundBlurStyle为非NONE值时，则不要设置backgroundColor，否则颜色显示将不符合预期效果。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| backgroundBlurStyleOptions19+ | [BackgroundBlurStyleOptions](ts-universal-attributes-background.md#backgroundblurstyleoptions10对象说明) | 否 | 是 | 背景模糊效果。默认值请参考BackgroundBlurStyleOptions类型说明。  **元服务API：** 从API version 19开始，该接口支持在元服务中使用。 |
| backgroundEffect19+ | [BackgroundEffectOptions](ts-universal-attributes-background.md#backgroundeffectoptions11) | 否 | 是 | 背景效果参数。默认值请参考BackgroundEffectOptions类型说明。  **元服务API：** 从API version 19开始，该接口支持在元服务中使用。 |
| shadow12+ | [ShadowOptions](ts-universal-attributes-image-effect.md#shadowoptions对象说明) | [ShadowStyle](ts-universal-attributes-image-effect.md#shadowstyle10枚举说明) | 否 | 是 | 设置对话框背板的阴影。  当设备为2in1时，默认场景下获焦阴影值为ShadowStyle.OUTER\_FLOATING\_MD，失焦为ShadowStyle.OUTER\_FLOATING\_SM。其他设备默认无阴影。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| enableHoverMode14+ | boolean | 否 | 是 | 是否响应悬停态，值为true时，响应悬停态。  默认值：false，默认不响应。  **说明：**  PC/2in1设备弹窗默认显示在上半屏，在enableHoverMode设置为true时，可以通过设置hoverModeArea参数显示在下半屏。其他设备弹窗在enableHoverMode设置为true时默认显示在下半屏，可以通过设置hoverModeArea参数显示在上半屏。  **元服务API：** 从API version 14开始，该接口支持在元服务中使用。 |
| hoverModeArea14+ | [HoverModeAreaType](ts-universal-attributes-sheet-transition.md#hovermodeareatype14) | 否 | 是 | 设置悬停态下对话框的默认展示区域。  默认值：HoverModeAreaType.BOTTOM\_SCREEN  **元服务API：** 从API version 14开始，该接口支持在元服务中使用。 |
| onWillAppear19+ | Callback<void> | 否 | 是 | 对话框显示动效前的事件回调。  **说明：**  1.正常时序依次为：onWillAppear>>onDidAppear>>onWillDisappear>>onDidDisappear。  2.在onWillAppear内设置改变对话框显示效果的回调事件，二次弹出生效。  **元服务API：** 从API version 19开始，该接口支持在元服务中使用。 |
| onDidAppear19+ | Callback<void> | 否 | 是 | 对话框弹出后的事件回调。  **说明：**  1.正常时序依次为：onWillAppear>>onDidAppear>>onWillDisappear>>onDidDisappear。  2.在onDidAppear内设置改变弹窗显示效果的回调事件，二次弹出生效。  3.快速点击弹出，关闭对话框时，onWillDisappear在onDidAppear前生效。  4.对话框入场动效未完成时彻底关闭对话框，动效打断，onDidAppear不会触发。  **元服务API：** 从API version 19开始，该接口支持在元服务中使用。 |
| onWillDisappear19+ | Callback<void> | 否 | 是 | 对话框退出动效前的事件回调。  **说明：**  1.正常时序依次为：onWillAppear>>onDidAppear>>onWillDisappear>>onDidDisappear。  **元服务API：** 从API version 19开始，该接口支持在元服务中使用。 |
| onDidDisappear19+ | Callback<void> | 否 | 是 | 对话框消失后的事件回调。  **说明：**  1.正常时序依次为：onWillAppear>>onDidAppear>>onWillDisappear>>onDidDisappear。  **元服务API：** 从API version 19开始，该接口支持在元服务中使用。 |
| levelMode15+ | [LevelMode](js-apis-promptaction.md#levelmode15枚举说明) | 否 | 是 | 设置对话框显示层级。  **说明：**  - 默认值：LevelMode.OVERLAY  - 当且仅当showInSubWindow属性设置为false时生效。  **元服务API：** 从API version 15开始，该接口支持在元服务中使用。 |
| levelUniqueId15+ | number | 否 | 是 | 设置页面级对话框需要显示的层级下的[节点UniqueID](js-apis-arkui-framenode.md#getuniqueid12)。  取值范围：大于等于0的数字。  **说明：**  - 当且仅当levelMode属性设置为LevelMode.EMBEDDED时生效。  **元服务API：** 从API version 15开始，该接口支持在元服务中使用。 |
| immersiveMode15+ | [ImmersiveMode](js-apis-promptaction.md#immersivemode15枚举说明) | 否 | 是 | 设置页面内对话框蒙层效果。  **说明：**  - 默认值：ImmersiveMode.DEFAULT  - 当且仅当levelMode属性设置为LevelMode.EMBEDDED时生效。  **元服务API：** 从API version 15开始，该接口支持在元服务中使用。 |
| levelOrder18+ | [LevelOrder](js-apis-promptaction.md#levelorder18) | 否 | 是 | 设置对话框显示的顺序。  **说明：**  - 默认值：LevelOrder.clamp(0)  - 不支持动态刷新顺序。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |

## ShowDialogSuccessResponse

PhonePC/2in1TabletTVWearable

对话框的响应结果。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| index | number | 否 | 否 | 选中按钮在buttons数组中的索引，从0开始。 |

## ActionMenuOptions

PhonePC/2in1TabletTVWearable

操作菜单的选项。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| title | string | [Resource](ts-types.md#resource) | 否 | 是 | 标题文本。  默认值：undefined，取值为undefined默认不显示标题。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| buttons | [[Button](js-apis-promptaction.md#button),[Button](js-apis-promptaction.md#button)?,[Button](js-apis-promptaction.md#button)?,[Button](js-apis-promptaction.md#button)?,[Button](js-apis-promptaction.md#button)?,[Button](js-apis-promptaction.md#button)?] | 否 | 否 | 菜单中菜单项按钮的数组，结构为：{text:'button', color: '#666666'}，支持1-6个按钮。按钮数量大于6个时，仅显示前6个按钮，之后的按钮不显示。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| showInSubWindow11+ | boolean | 否 | 是 | 某操作菜单需要显示在主窗口之外时，是否在子窗口显示此菜单。值为true表示在子窗口显示菜单。  默认值：false，在子窗口不显示菜单。  **说明：**  - showInSubWindow为true的菜单无法触发显示另一个showInSubWindow为true的菜单。  - 若在UIExtension中设置showInSubWindow为true, 菜单将基于UIExtension的宿主窗口对齐。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| isModal11+ | boolean | 否 | 是 | 菜单是否为模态窗口。值为true表示为模态窗口且有蒙层，不可与菜单周围其他控件进行交互，即蒙层区域无法事件透传。值为false表示为非模态窗口且无蒙层，可以与菜单周围其他控件进行交互。  默认值：true  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| levelMode15+ | [LevelMode](js-apis-promptaction.md#levelmode15枚举说明) | 否 | 是 | 设置菜单显示层级。  **说明：**  - 默认值：LevelMode.OVERLAY  - 当且仅当showInSubWindow属性设置为false时生效。  **元服务API：** 从API version 15开始，该接口支持在元服务中使用。 |
| levelUniqueId15+ | number | 否 | 是 | 设置页面级菜单需要显示的层级下的[节点UniqueID](js-apis-arkui-framenode.md#getuniqueid12)。  取值范围：大于等于0的数字。  **说明：**  - 当且仅当levelMode属性设置为LevelMode.EMBEDDED时生效。  **元服务API：** 从API version 15开始，该接口支持在元服务中使用。 |
| immersiveMode15+ | [ImmersiveMode](js-apis-promptaction.md#immersivemode15枚举说明) | 否 | 是 | 设置页面内菜单蒙层效果。  **说明：**  - 默认值：ImmersiveMode.DEFAULT  - 当且仅当levelMode属性设置为LevelMode.EMBEDDED时生效。  **元服务API：** 从API version 15开始，该接口支持在元服务中使用。 |
| onWillAppear20+ | Callback<void> | 否 | 是 | 菜单显示动效前的事件回调。  **说明：**  1.正常时序依次为：onWillAppear>>onDidAppear>>onWillDisappear>>onDidDisappear。  **元服务API：** 从API version 20开始，该接口支持在元服务中使用。 |
| onDidAppear20+ | Callback<void> | 否 | 是 | 菜单弹出后的事件回调。  **说明：**  1.正常时序依次为：onWillAppear>>onDidAppear>>onWillDisappear>>onDidDisappear。  2.快速点击弹出，关闭菜单时，onWillDisappear在onDidAppear前生效。  **元服务API：** 从API version 20开始，该接口支持在元服务中使用。 |
| onWillDisappear20+ | Callback<void> | 否 | 是 | 菜单退出动效前的事件回调。  **说明：**  1.正常时序依次为：onWillAppear>>onDidAppear>>onWillDisappear>>onDidDisappear。  **元服务API：** 从API version 20开始，该接口支持在元服务中使用。 |
| onDidDisappear20+ | Callback<void> | 否 | 是 | 菜单消失后的事件回调。  **说明：**  1.正常时序依次为：onWillAppear>>onDidAppear>>onWillDisappear>>onDidDisappear。  **元服务API：** 从API version 20开始，该接口支持在元服务中使用。 |

## ActionMenuSuccessResponse

PhonePC/2in1TabletTVWearable

操作菜单的响应结果。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| index | number | 否 | 否 | 选中按钮在buttons数组中的索引，从0开始。 |

## CommonState20+枚举说明

PhonePC/2in1TabletTVWearable

自定义弹窗的状态。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| UNINITIALIZED | 0 | 未初始化，控制器未与dialog绑定时。 |
| INITIALIZED | 1 | 已初始化，控制器与dialog绑定后。 |
| APPEARING | 2 | 显示中，dialog显示动画过程中。 |
| APPEARED | 3 | 已显示，dialog显示动画结束。 |
| DISAPPEARING | 4 | 消失中，dialog消失动画过程中。 |
| DISAPPEARED | 5 | 已消失，dialog消失动画结束后。 |

## DialogController18+

PhonePC/2in1TabletTVWearable

自定义弹窗控制器，继承自[CommonController](js-apis-promptaction.md#commoncontroller18)。

DialogController可作为UIContext弹出自定义弹窗的成员变量，具体用法可看[openCustomDialogWithController](arkts-apis-uicontext-promptaction.md#opencustomdialogwithcontroller18)和[presentCustomDialog](arkts-apis-uicontext-promptaction.md#presentcustomdialog18)示例。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## CommonController18+

PhonePC/2in1TabletTVWearable

公共控制器，可以控制promptAction相关组件。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

### constructor18+

PhonePC/2in1TabletTVWearable

constructor()

控制器的构造函数。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

### close18+

PhonePC/2in1TabletTVWearable

close(): void

关闭显示的自定义弹窗，若已关闭，则不生效。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

### getState20+

PhonePC/2in1TabletTVWearable

getState(): CommonState

获取自定义弹窗的状态。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [CommonState](js-apis-promptaction.md#commonstate20枚举说明) | 返回对应的弹窗状态。 |

## LevelOrder18+

PhonePC/2in1TabletTVWearable

弹窗层级，可以控制弹窗显示的顺序。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

### clamp18+

PhonePC/2in1TabletTVWearable

static clamp(order: number): LevelOrder

创建指定顺序的弹窗层级。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| order | number | 是 | 弹窗显示顺序。取值范围为[-100000.0, 100000.0]，如果值小于-100000.0则设置为-100000.0，如果值大于100000.0则设置为100000.0。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [LevelOrder](js-apis-promptaction.md#levelorder18) | 返回当前对象实例。 |

### getOrder18+

PhonePC/2in1TabletTVWearable

getOrder(): number

获取弹窗显示顺序。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 返回显示顺序数值。 |

## DialogOptions18+

PhonePC/2in1TabletTVWearable

自定义弹窗的内容，继承自[BaseDialogOptions](js-apis-promptaction.md#basedialogoptions11)。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| backgroundColor | [ResourceColor](ts-types.md#resourcecolor) | 否 | 是 | 设置弹窗背板颜色。  默认值：Color.Transparent  **说明：**  backgroundColor会与模糊属性backgroundBlurStyle叠加产生效果，如果不符合预期，可将backgroundBlurStyle设置为BlurStyle.NONE，即可取消模糊。 |
| cornerRadius | [DialogOptionsCornerRadius](js-apis-promptaction.md#dialogoptionscornerradius18) | 否 | 是 | 设置弹窗背板的圆角半径。  可分别设置4个圆角的半径。  默认值：{ topLeft: '32vp', topRight: '32vp', bottomLeft: '32vp', bottomRight: '32vp' }  圆角大小受组件尺寸限制，最大值为组件宽或高的一半，若值为负，则按照默认值处理。  百分比参数方式：以父元素弹窗宽和高的百分比来设置弹窗的圆角。 |
| borderWidth | [DialogOptionsBorderWidth](js-apis-promptaction.md#dialogoptionsborderwidth18) | 否 | 是 | 设置弹窗背板的边框宽度。  可分别设置4个边框宽度。  默认值：0  单位：vp  百分比参数方式：以父元素弹窗宽的百分比来设置弹窗的边框宽度。  当弹窗左边框和右边框大于弹窗宽度，弹窗上边框和下边框大于弹窗高度，显示可能不符合预期。 |
| borderColor | [DialogOptionsBorderColor](js-apis-promptaction.md#dialogoptionsbordercolor18) | 否 | 是 | 设置弹窗背板的边框颜色。  默认值：Color.Black  如果使用borderColor属性，需要和borderWidth属性一起使用。 |
| borderStyle | [DialogOptionsBorderStyle](js-apis-promptaction.md#dialogoptionsborderstyle18) | 否 | 是 | 设置弹窗背板的边框样式。  默认值：BorderStyle.Solid。  如果使用borderStyle属性，需要和borderWidth属性一起使用。 |
| width | [Dimension](ts-types.md#dimension10) | 否 | 是 | 设置弹窗背板的宽度。  **说明：**  - 默认最大值：400vp  - 百分比参数方式：弹窗参考宽度基于所在窗口宽度调整。 |
| height | [Dimension](ts-types.md#dimension10) | 否 | 是 | 设置弹窗背板的高度。  **说明：**  - 默认最大值：0.9 \*（窗口高度 - 安全区域）。  - 百分比参数方式：弹窗参考高度为（窗口高度 - 安全区域），在此基础上调小或调大。 |
| shadow | [DialogOptionsShadow](js-apis-promptaction.md#dialogoptionsshadow18) | 否 | 是 | 设置弹窗背板的阴影。  当设备为2in1时，默认场景下获焦阴影值为ShadowStyle.OUTER\_FLOATING\_MD，失焦为ShadowStyle.OUTER\_FLOATING\_SM。其他设备默认无阴影。 |
| backgroundBlurStyle | [BlurStyle](ts-universal-attributes-background.md#blurstyle9) | 否 | 是 | 弹窗背板模糊材质。  默认值：BlurStyle.COMPONENT\_ULTRA\_THICK  **说明：**  设置为BlurStyle.NONE即可关闭背景虚化。当设置了backgroundBlurStyle为非NONE值时，则不要设置backgroundColor，否则颜色显示将不符合预期效果。 |

## DialogOptionsCornerRadius18+

PhonePC/2in1TabletTVWearable

type DialogOptionsCornerRadius = Dimension | BorderRadiuses

表示弹窗背板的圆角半径允许的数据字段类型。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 说明 |
| --- | --- |
| [Dimension](ts-types.md#dimension10) | 表示值类型为长度类型，用于描述尺寸单位。 |
| [BorderRadiuses](ts-types.md#borderradiuses9) | 表示值类型为圆角类型，用于描述组件边框圆角半径。 |

## DialogOptionsBorderWidth18+

PhonePC/2in1TabletTVWearable

type DialogOptionsBorderWidth = Dimension | EdgeWidths

表示弹窗背板的边框宽度允许的数据字段类型。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 说明 |
| --- | --- |
| [Dimension](ts-types.md#dimension10) | 表示值类型为长度类型，用于描述尺寸单位。 |
| [EdgeWidths](ts-types.md#edgewidths9) | 表示值类型为边框宽度类型，用于描述组件边框不同方向的宽度。 |

## DialogOptionsBorderColor18+

PhonePC/2in1TabletTVWearable

type DialogOptionsBorderColor = ResourceColor | EdgeColors

表示弹窗背板的边框颜色允许的数据字段类型。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 说明 |
| --- | --- |
| [ResourceColor](ts-types.md#resourcecolor) | 表示值类型为颜色类型，用于描述资源颜色类型。 |
| [EdgeColors](ts-types.md#edgecolors9) | 表示值类型为边框颜色，用于描述组件边框四条边的颜色。 |

## DialogOptionsBorderStyle18+

PhonePC/2in1TabletTVWearable

type DialogOptionsBorderStyle = BorderStyle | EdgeStyles

表示弹窗背板的边框样式允许的数据字段类型。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 说明 |
| --- | --- |
| [BorderStyle](ts-appendix-enums.md#borderstyle) | 表示值类型为边框类型，用于描述组件边框的类型。 |
| [EdgeStyles](ts-types.md#edgestyles9) | 表示值类型为边框样式，用于描述组件边框四条边的样式。 |

## DialogOptionsShadow18+

PhonePC/2in1TabletTVWearable

type DialogOptionsShadow = ShadowOptions | ShadowStyle

表示弹窗背板的阴影允许的数据字段类型。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 说明 |
| --- | --- |
| [ShadowOptions](ts-universal-attributes-image-effect.md#shadowoptions对象说明) | 表示值类型为阴影属性集合，用于设置阴影的模糊半径、阴影的颜色、X轴和Y轴的偏移量。 |
| [ShadowStyle](ts-universal-attributes-image-effect.md#shadowstyle10枚举说明) | 表示值类型为阴影类型，用于描述阴影的类型。 |

## CustomDialogOptions11+

PhonePC/2in1TabletTVWearable

自定义弹窗的内容，继承自[BaseDialogOptions](js-apis-promptaction.md#basedialogoptions11)。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| builder | [CustomBuilder](ts-types.md#custombuilder8) | 否 | 否 | 设置自定义弹窗的内容。  **说明：**  builder需要赋值为箭头函数，格式如下：() => { this.XXX() }，其中XXX是内部builder名。  全局builder需要在组件内部创建，并在内部builder中调用。  builder根节点宽高百分比相对弹窗容器大小。  builder非根节点宽高百分比相对父节点大小。 |
| backgroundColor 12+ | [ResourceColor](ts-types.md#resourcecolor) | 否 | 是 | 设置弹窗背板颜色。  默认值：Color.Transparent  **说明：**  当设置了backgroundColor为非透明色时，backgroundBlurStyle需要设置为BlurStyle.NONE，否则颜色显示将不符合预期效果。 |
| cornerRadius12+ | [Dimension](ts-types.md#dimension10) | [BorderRadiuses](ts-types.md#borderradiuses9) | 否 | 是 | 设置背板的圆角半径。  可分别设置4个圆角的半径。  默认值：{ topLeft: '32vp', topRight: '32vp', bottomLeft: '32vp', bottomRight: '32vp' }  圆角大小受组件尺寸限制，最大值为组件宽或高的一半，若值为负，则按照默认值处理。  百分比参数方式：以父元素弹窗宽和高的百分比来设置弹窗的圆角。 |
| borderWidth12+ | [Dimension](ts-types.md#dimension10) | [EdgeWidths](ts-types.md#edgewidths9) | 否 | 是 | 设置弹窗背板的边框宽度。  可分别设置4个边框宽度。  默认值：0  单位：vp  百分比参数方式：以父元素弹窗宽的百分比来设置弹窗的边框宽度。  当弹窗左边框和右边框大于弹窗宽度，弹窗上边框和下边框大于弹窗高度，显示可能不符合预期。 |
| borderColor12+ | [ResourceColor](ts-types.md#resourcecolor) | [EdgeColors](ts-types.md#edgecolors9) | 否 | 是 | 设置弹窗背板的边框颜色。  默认值：Color.Black  如果使用borderColor属性，需要和borderWidth属性一起使用。 |
| borderStyle12+ | [BorderStyle](ts-appendix-enums.md#borderstyle) | [EdgeStyles](ts-types.md#edgestyles9) | 否 | 是 | 设置弹窗背板的边框样式。  默认值：BorderStyle.Solid  如果使用borderStyle属性，需要和borderWidth属性一起使用。 |
| width12+ | [Dimension](ts-types.md#dimension10) | 否 | 是 | 设置弹窗背板的宽度。  **说明：**  - 弹窗宽度默认最大值：400vp  - 百分比参数方式：弹窗参考宽度基于所在窗口的宽度的基础上调整。 |
| height12+ | [Dimension](ts-types.md#dimension10) | 否 | 是 | 设置弹窗背板的高度。  **说明：**  - 弹窗高度默认最大值：0.9 \*（窗口高度 - 安全区域）。  - 百分比参数方式：弹窗参考高度为（窗口高度 - 安全区域），在此基础上调小或调大。 |
| shadow12+ | [ShadowOptions](ts-universal-attributes-image-effect.md#shadowoptions对象说明) | [ShadowStyle](ts-universal-attributes-image-effect.md#shadowstyle10枚举说明) | 否 | 是 | 设置弹窗背板的阴影。  当设备为2in1时，默认场景下获焦阴影值为ShadowStyle.OUTER\_FLOATING\_MD，失焦为ShadowStyle.OUTER\_FLOATING\_SM。其他设备默认无阴影。 |
| backgroundBlurStyle12+ | [BlurStyle](ts-universal-attributes-background.md#blurstyle9) | 否 | 是 | 弹窗背板模糊材质。  默认值：BlurStyle.COMPONENT\_ULTRA\_THICK  **说明：**  设置为BlurStyle.NONE即可关闭背景虚化。当设置了backgroundBlurStyle为非NONE值时，则不要设置backgroundColor，否则颜色显示将不符合预期效果。 |

## BaseDialogOptions11+

PhonePC/2in1TabletTVWearable

弹窗的选项。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| maskRect | [Rectangle](ts-methods-alert-dialog-box.md#rectangle8类型说明) | 否 | 是 | 弹窗遮蔽层区域。  默认值：{ x: 0, y: 0, width: '100%', height: '100%' }  **说明：**  showInSubWindow为true时，maskRect不生效。  maskRect在设置[Rectangle](ts-methods-alert-dialog-box.md#rectangle8类型说明)中的部分属性后，若未设置其余的属性，则其余属性的默认值为0。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| alignment | [DialogAlignment](ts-methods-alert-dialog-box.md#dialogalignment枚举说明) | 否 | 是 | 弹窗在竖直方向上的对齐方式。  默认值：DialogAlignment.Default  **说明：**  若在UIExtension中设置showInSubWindow为true, 弹窗将基于UIExtension的宿主窗口对齐。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| offset | [Offset](ts-types.md#offset) | 否 | 是 | 弹窗相对alignment所在位置的偏移量。  默认值：{ dx: 0 , dy: 0 }  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| isModal | boolean | 否 | 是 | 弹窗是否为模态窗口。值为true表示为模态窗口且有蒙层，不可与弹窗周围其他控件进行交互，即蒙层区域无法事件透传。值为false表示为非模态窗口且无蒙层，可以与弹窗周围其他控件进行交互。  默认值：true  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| showInSubWindow | boolean | 否 | 是 | 某弹窗需要显示在主窗口之外时，是否在子窗口显示此弹窗。值为true表示在子窗口显示弹窗。  默认值：false，弹窗显示在应用内，而非独立子窗口。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| onWillDismiss12+ | Callback<[DismissDialogAction](js-apis-promptaction.md#dismissdialogaction12)> | 否 | 是 | 交互式关闭回调函数。  **说明：**  1.当用户执行点击遮障层关闭、侧滑（左滑/右滑）、三键back、键盘ESC关闭交互操作时，如果注册该回调函数，则不会立刻关闭弹窗。在回调函数中可以通过reason得到阻拦关闭弹窗的操作类型，从而根据原因选择是否能关闭弹窗。当前组件返回的reason中，暂不支持CLOSE\_BUTTON的枚举值。  2.在onWillDismiss回调中，不能再做onWillDismiss拦截。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| autoCancel12+ | boolean | 否 | 是 | 点击遮障层时，是否关闭弹窗，true表示关闭弹窗。false表示不关闭弹窗。  默认值：true  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| maskColor12+ | [ResourceColor](ts-types.md#resourcecolor) | 否 | 是 | 自定义蒙层颜色。  默认值: 0x33000000  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| transition12+ | [TransitionEffect](ts-transition-animation-component.md#transitioneffect10对象说明) | 否 | 是 | 设置弹窗显示和退出的过渡效果。  **说明：**  1.如果不设置，则使用默认的显示/退出动效。  2.显示动效中按back键，打断显示动效，执行退出动效，动画效果为显示动效与退出动效的曲线叠加后的效果。  3.退出动效中按back键，不会打断退出动效，退出动效继续执行，继续按back键退出应用。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| dialogTransition19+ | [TransitionEffect](ts-transition-animation-component.md#transitioneffect10对象说明) | 否 | 是 | 设置弹窗内容显示的过渡效果。默认无动效。  **元服务API：** 从API version 19开始，该接口支持在元服务中使用。 |
| maskTransition19+ | [TransitionEffect](ts-transition-animation-component.md#transitioneffect10对象说明) | 否 | 是 | 设置蒙层显示的过渡效果。默认无动效。  **元服务API：** 从API version 19开始，该接口支持在元服务中使用。 |
| onDidAppear12+ | () => void | 否 | 是 | 弹窗弹出后的事件回调。  **说明：**  1.正常时序依次为：onWillAppear>>onDidAppear>>(onDateAccept/onCancel/onDateChange)>>onWillDisappear>>onDidDisappear。  2.在onDidAppear内设置改变弹窗显示效果的回调事件，二次弹出生效。  3.快速点击弹出，消失弹窗时，存在onWillDisappear在onDidAppear前生效。  4. 当弹窗入场动效未完成时关闭弹窗，该回调不会触发。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| onDidDisappear12+ | () => void | 否 | 是 | 弹窗消失后的事件回调。  **说明：**  正常时序依次为：onWillAppear>>onDidAppear>>(onDateAccept/onCancel/onDateChange)>>onWillDisappear>>onDidDisappear。  当弹窗退场动画未完成时（例如：同时触发弹窗关闭和页面切换），该回调不会触发。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| onWillAppear12+ | () => void | 否 | 是 | 弹窗显示动效前的事件回调。  **说明：**  1.正常时序依次为：onWillAppear>>onDidAppear>>(onDateAccept/onCancel/onDateChange)>>onWillDisappear>>onDidDisappear。  2.在onWillAppear内设置改变弹窗显示效果的回调事件，二次弹出生效。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| onWillDisappear12+ | () => void | 否 | 是 | 弹窗退出动效前的事件回调。  **说明：**  1.正常时序依次为：onWillAppear>>onDidAppear>>(onDateAccept/onCancel/onDateChange)>>onWillDisappear>>onDidDisappear。  2.快速点击弹出，消失弹窗时，存在onWillDisappear在onDidAppear前生效。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| keyboardAvoidMode12+ | [KeyboardAvoidMode](ts-universal-attributes-popup.md#keyboardavoidmode12枚举说明) | 否 | 是 | 用于设置弹窗是否在拉起软键盘时进行自动避让。  默认值：KeyboardAvoidMode.DEFAULT  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| enableHoverMode14+ | boolean | 否 | 是 | 是否响应悬停态，值为true时，响应悬停态。  默认值：false，默认不响应。  **说明：**  PC/2in1设备弹窗默认显示在上半屏，在enableHoverMode设置为true。可以通过设置hoverModeArea参数显示在下半屏。其他设备弹窗在enableHoverMode设置为true时默认显示在下半屏，可以通过设置hoverModeArea参数显示在上半屏。  **元服务API：** 从API version 14开始，该接口支持在元服务中使用。 |
| hoverModeArea14+ | [HoverModeAreaType](ts-universal-attributes-sheet-transition.md#hovermodeareatype14) | 否 | 是 | 悬停态下弹窗默认展示区域。  默认值：HoverModeAreaType.BOTTOM\_SCREEN  **元服务API：** 从API version 14开始，该接口支持在元服务中使用。 |
| backgroundBlurStyleOptions19+ | [BackgroundBlurStyleOptions](ts-universal-attributes-background.md#backgroundblurstyleoptions10对象说明) | 否 | 是 | 背景模糊效果。默认值请参考BackgroundBlurStyleOptions类型说明。  **元服务API：** 从API version 19开始，该接口支持在元服务中使用。 |
| backgroundEffect19+ | [BackgroundEffectOptions](ts-universal-attributes-background.md#backgroundeffectoptions11) | 否 | 是 | 背景效果参数。默认值请参考BackgroundEffectOptions类型说明。  **元服务API：** 从API version 19开始，该接口支持在元服务中使用。 |
| keyboardAvoidDistance15+ | [LengthMetrics](js-apis-arkui-graphics.md#lengthmetrics12) | 否 | 是 | 弹窗避让键盘后，和键盘之间距离。  **说明：**  - 默认值：16vp  - 默认单位：vp  - 当且仅当keyboardAvoidMode属性设置为DEFAULT时生效。  **元服务API：** 从API version 15开始，该接口支持在元服务中使用。 |
| levelMode15+ | [LevelMode](js-apis-promptaction.md#levelmode15枚举说明) | 否 | 是 | 设置弹窗显示层级。  **说明：**  - 默认值：LevelMode.OVERLAY  - 当且仅当showInSubWindow属性设置为false时生效。  **元服务API：** 从API version 15开始，该接口支持在元服务中使用。 |
| levelUniqueId15+ | number | 否 | 是 | 设置页面级弹窗需要显示的层级下的[节点UniqueID](js-apis-arkui-framenode.md#getuniqueid12)。  取值范围：大于等于0的数字。  **说明：**  - 当且仅当levelMode属性设置为LevelMode.EMBEDDED时生效。  **元服务API：** 从API version 15开始，该接口支持在元服务中使用。 |
| immersiveMode15+ | [ImmersiveMode](js-apis-promptaction.md#immersivemode15枚举说明) | 否 | 是 | 设置页面内弹窗蒙层效果。  **说明：**  - 默认值：ImmersiveMode.DEFAULT  - 当且仅当levelMode属性设置为LevelMode.EMBEDDED时生效。  **元服务API：** 从API version 15开始，该接口支持在元服务中使用。 |
| levelOrder18+ | [LevelOrder](js-apis-promptaction.md#levelorder18) | 否 | 是 | 设置弹窗显示的顺序。  **说明：**  - 默认值：LevelOrder.clamp(0)  - 不支持动态刷新顺序。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| focusable19+ | boolean | 否 | 是 | 设置弹窗是否获取焦点。值为true表示获取焦点，值为false表示不获取焦点。  默认值：true  **说明：**  只有弹出覆盖在当前窗口之上的弹窗才可以获取焦点。  **元服务API：** 从API version 19开始，该接口支持在元服务中使用。 |

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

## LevelMode15+枚举说明

PhonePC/2in1TabletTVWearable

弹窗显示层级模式。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| OVERLAY | 0 | 弹窗层级为应用窗口根节点，应用内路由导航切换弹窗不隐藏。 |
| EMBEDDED | 1 | 弹窗节点为页面内路由/导航下的节点，随路由导航切换，弹窗随页面隐藏。  **说明：**  1. 目前只支持挂载在Page或者[NavDestination](ts-basic-components-navdestination.md)节点上，优先挂载在Page节点下，只支持在这两种页面内顶层显示。  2. 该模式下新起的页面可以覆盖在弹窗上，页面返回后该弹窗依旧存在，弹窗内容不会丢失。  3. 该模式下需确保目标页面节点如Page节点已挂载上树，再拉起弹窗，否则弹窗将无法挂载到对应的页面节点内。 |

## ImmersiveMode15+枚举说明

PhonePC/2in1TabletTVWearable

页面内弹窗蒙层显示区域模式。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| DEFAULT | 0 | 弹窗蒙层遵循父节点布局约束进行显示。 |
| EXTEND | 1 | 弹窗蒙层可扩展至覆盖状态栏和导航条。 |

## Button

PhonePC/2in1TabletTVWearable

菜单中的菜单项按钮。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| text | string | [Resource](ts-types.md#resource) | 否 | 否 | 按钮文本内容。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| color | string | [Resource](ts-types.md#resource) | 否 | 否 | 按钮文本颜色。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| primary12+ | boolean | 否 | 是 | 在弹窗获焦且未进行tab键走焦时，按钮是否默认响应Enter键。多个Button时，只允许一个Button的该字段配置为true，否则所有Button均不响应。多重弹窗可自动获焦连续响应。值为true表示按钮默认响应Enter键，值为false时，按钮不默认响应Enter键。  默认值：false  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |

## 示例

PhonePC/2in1TabletTVWearable

从API version 20开始，该示例实现了在promptAction.DialogController中调用getState获取弹窗当前状态。

```
1. // xxx.ets
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { ComponentContent, promptAction } from '@kit.ArkUI';

5. @Component
6. struct CustomDialogExample {
7. build() {
8. Column() {
9. Text('Hello')
10. .fontSize(50)
11. .fontWeight(FontWeight.Bold)
12. .margin({ bottom: 36 })
13. Button('点我关闭弹窗')
14. .onClick(() => {
15. if (this.getDialogController()) {
16. this.getDialogController().close();
17. }
18. })
19. Button('点我获取状态')
20. .onClick(() => {
21. if (this.getDialogController()) {
22. let state: promptAction.CommonState = this.getDialogController().getState();
23. switch (state) {
24. case promptAction.CommonState.UNINITIALIZED: {
25. console.info('The dialog state is uninitialized.');
26. break;
27. }
28. case promptAction.CommonState.INITIALIZED: {
29. console.info('The dialog state is initialized.');
30. break;
31. }
32. case promptAction.CommonState.APPEARING: {
33. console.info('The dialog state is appearing.');
34. break;
35. }
36. case promptAction.CommonState.APPEARED: {
37. console.info('The dialog state is appeared.');
38. break;
39. }
40. case promptAction.CommonState.DISAPPEARING: {
41. console.info('The dialog state is disappearing.');
42. break;
43. }
44. case promptAction.CommonState.DISAPPEARED: {
45. console.info('The dialog state is disappeared.');
46. break;
47. }
48. default: {
49. console.info('The dialog state is unknown.');
50. break;
51. }
52. }
53. }
54. })

56. }.backgroundColor('#FFF0F0F0')
57. }
58. }

60. @Builder
61. function buildText() {
62. CustomDialogExample()
63. }

65. @Entry
66. @Component
67. struct Index {

69. private dialogController: promptAction.DialogController = new promptAction.DialogController()

71. build() {
72. Row() {
73. Column() {
74. Button("click me")
75. .onClick(() => {
76. let uiContext = this.getUIContext();
77. let promptAction = uiContext.getPromptAction();
78. let contentNode = new ComponentContent(uiContext, wrapBuilder(buildText),
79. );

81. promptAction.openCustomDialogWithController(contentNode, this.dialogController, {

83. transition: TransitionEffect.OPACITY.animation({
84. duration: 3000
85. })
86. }).then(() => {
87. console.info('succeeded')
88. }).catch((error: BusinessError) => {
89. console.error(`OpenCustomDialogWithController args error code is ${error.code}, message is ${error.message}`);
90. })
91. })
92. }
93. .width('100%')
94. .height('100%')
95. }
96. .height('100%')
97. }
98. }
```

## promptAction.showToast(deprecated)

PhonePC/2in1TabletTVWearable

showToast(options: ShowToastOptions): void

创建并显示即时反馈。

说明

* 从API version 9开始支持，从API version 18开始废弃，建议使用[showToast](arkts-apis-uicontext-promptaction.md#showtoast)替代。showToast需先通过[UIContext](arkts-apis-uicontext-uicontext.md)中的[getPromptAction](arkts-apis-uicontext-uicontext.md#getpromptaction)方法获取[PromptAction](arkts-apis-uicontext-promptaction.md)对象，然后通过该对象进行调用。且直接使用showToast可能导致[UI上下文不明确](../harmonyos-guides/arkts-global-interface.md#ui上下文不明确)的问题。
* 从API version 10开始，可以通过使用[UIContext](arkts-apis-uicontext-uicontext.md)中的[getPromptAction](arkts-apis-uicontext-uicontext.md#getpromptaction)方法获取当前UI上下文关联的[PromptAction](arkts-apis-uicontext-promptaction.md)对象。
* Toast样式单一，不支持内容的自定义，具体支持能力请参考[ShowToastOptions](js-apis-promptaction.md#showtoastoptions)提供的接口。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [ShowToastOptions](js-apis-promptaction.md#showtoastoptions) | 是 | Toast选项。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[接口调用异常错误码](errorcode-internal.md)。

说明

当返回100001错误码时，可能出现了UI上下文不明确的问题，对此可以使用UIContext中的接口进行替换，详细说明可参考[使用UI上下文接口操作界面](../harmonyos-guides/arkts-global-interface.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |
| 100001 | Internal error. |

**示例：**

```
1. import { promptAction } from '@kit.ArkUI';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. @Entry
5. @Component
6. struct toastExample {
7. build() {
8. Column() {
9. Button('Show toast').fontSize(20)
10. .onClick(() => {
11. try {
12. promptAction.showToast({
13. message: 'Hello World',
14. duration: 2000
15. });
16. } catch (error) {
17. let message = (error as BusinessError).message;
18. let code = (error as BusinessError).code;
19. console.error(`showToast args error code is ${code}, message is ${message}`);
20. };
21. })
22. }.height('100%').width('100%').justifyContent(FlexAlign.Center)
23. }
24. }
```

API version 11及之前Toast样式。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c6/v3/uTPklDVLROChwQc6uwZSMA/zh-cn_image_0000002552959424.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000030Z&HW-CC-Expire=86400&HW-CC-Sign=333D242545969EBE1A548DE7C572612683EB0CB10FC78156C5A0CF0C07B08FC1)

API version 12及之后Toast样式。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/pOxWbdt7THib_8LLywnGyw/zh-cn_image_0000002583479425.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000030Z&HW-CC-Expire=86400&HW-CC-Sign=A28546C376FE6116D8E3E6A0DB5191D35469C0FA81DDA6949ECFEE9D88C7941A)

## promptAction.showDialog(deprecated)

PhonePC/2in1TabletTVWearable

showDialog(options: ShowDialogOptions): Promise<ShowDialogSuccessResponse>

创建并显示对话框，对话框通过Promise返回结果。

说明

* 从API version 9开始支持，从API version 18开始废弃，建议使用[showDialog](arkts-apis-uicontext-promptaction.md#showdialog-1)替代。showDialog需先通过[UIContext](arkts-apis-uicontext-uicontext.md)中的[getPromptAction](arkts-apis-uicontext-uicontext.md#getpromptaction)方法获取[PromptAction](arkts-apis-uicontext-promptaction.md)对象，然后通过该对象进行调用。且直接使用showDialog可能导致[UI上下文不明确](../harmonyos-guides/arkts-global-interface.md#ui上下文不明确)的问题。
* 从API version 10开始，可以通过使用[UIContext](arkts-apis-uicontext-uicontext.md)中的[getPromptAction](arkts-apis-uicontext-uicontext.md#getpromptaction)方法获取当前UI上下文关联的[PromptAction](arkts-apis-uicontext-promptaction.md)对象。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [ShowDialogOptions](js-apis-promptaction.md#showdialogoptions) | 是 | 对话框选项。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[ShowDialogSuccessResponse](js-apis-promptaction.md#showdialogsuccessresponse)> | Promise对象，返回对话框的响应结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[接口调用异常错误码](errorcode-internal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |
| 100001 | Internal error. |

**示例：**

```
1. import { promptAction } from '@kit.ArkUI';

3. promptAction.showDialog({
4. title: 'Title Info',
5. message: 'Message Info',
6. buttons: [
7. {
8. text: 'button1',
9. color: '#000000'
10. },
11. {
12. text: 'button2',
13. color: '#000000'
14. }
15. ],
16. })
17. .then(data => {
18. console.info('showDialog success, click button: ' + data.index);
19. })
20. .catch((err: Error) => {
21. console.info('showDialog error: ' + err);
22. })
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/56/v3/gkUWOyKAT5OLqhx8uhL96Q/zh-cn_image_0000002552799776.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000030Z&HW-CC-Expire=86400&HW-CC-Sign=350ADCD638801830380771359F5F3AFF45971AC05FB9E86DC957CB8E9B351FA5)

## promptAction.showDialog(deprecated)

PhonePC/2in1TabletTVWearable

showDialog(options: ShowDialogOptions, callback: AsyncCallback<ShowDialogSuccessResponse>):void

创建并显示对话框，对话框响应结果使用callback异步回调返回。

说明

* 从API version 9开始支持，从API version 18开始废弃，建议使用[showDialog](arkts-apis-uicontext-promptaction.md#showdialog)替代。showDialog需先通过[UIContext](arkts-apis-uicontext-uicontext.md)中的[getPromptAction](arkts-apis-uicontext-uicontext.md#getpromptaction)方法获取[PromptAction](arkts-apis-uicontext-promptaction.md)对象，然后通过该对象进行调用。且直接使用showDialog可能导致[UI上下文不明确](../harmonyos-guides/arkts-global-interface.md#ui上下文不明确)的问题。
* 从API version 10开始，可以通过使用[UIContext](arkts-apis-uicontext-uicontext.md)中的[getPromptAction](arkts-apis-uicontext-uicontext.md#getpromptaction)方法获取当前UI上下文关联的[PromptAction](arkts-apis-uicontext-promptaction.md)对象。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [ShowDialogOptions](js-apis-promptaction.md#showdialogoptions) | 是 | 页面显示对话框信息描述。 |
| callback | AsyncCallback<[ShowDialogSuccessResponse](js-apis-promptaction.md#showdialogsuccessresponse)> | 是 | 回调函数。弹出对话框成功，err为undefined，data为获取到的对话框响应结果，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[接口调用异常错误码](errorcode-internal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |
| 100001 | Internal error. |

**示例：**

```
1. import { promptAction } from '@kit.ArkUI';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. try {
5. promptAction.showDialog({
6. title: 'showDialog Title Info',
7. message: 'Message Info',
8. buttons: [
9. {
10. text: 'button1',
11. color: '#000000'
12. },
13. {
14. text: 'button2',
15. color: '#000000'
16. }
17. ]
18. }, (err, data) => {
19. if (err) {
20. console.info('showDialog err: ' + err);
21. return;
22. }
23. console.info('showDialog success callback, click button: ' + data.index);
24. });
25. } catch (error) {
26. let message = (error as BusinessError).message;
27. let code = (error as BusinessError).code;
28. console.error(`showDialog args error code is ${code}, message is ${message}`);
29. };
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/35/v3/-rdLD9pATqygqR3Kja8BTQ/zh-cn_image_0000002583439471.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000030Z&HW-CC-Expire=86400&HW-CC-Sign=76488894AD01AB35F02CC0A1795B5A71279DC4E2586A5F165036EB4C31D6486F)

当弹窗的showInSubWindow属性为true时，弹窗可显示在窗口外。

```
1. import { promptAction } from '@kit.ArkUI';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. try {
5. promptAction.showDialog({
6. title: 'showDialog Title Info',
7. message: 'Message Info',
8. isModal: true,
9. showInSubWindow: true,
10. buttons: [
11. {
12. text: 'button1',
13. color: '#000000'
14. },
15. {
16. text: 'button2',
17. color: '#000000'
18. }
19. ]
20. }, (err, data) => {
21. if (err) {
22. console.info('showDialog err: ' + err);
23. return;
24. }
25. console.info('showDialog success callback, click button: ' + data.index);
26. });
27. } catch (error) {
28. let message = (error as BusinessError).message;
29. let code = (error as BusinessError).code;
30. console.error(`showDialog args error code is ${code}, message is ${message}`);
31. };
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8f/v3/QGA1dfvvQam1UZq_TB6lKg/zh-cn_image_0000002552959426.jpg?HW-CC-KV=V1&HW-CC-Date=20260428T000030Z&HW-CC-Expire=86400&HW-CC-Sign=1F385F975E374B8C419A6755B5912CCC37415E135C78064BA8469D4174F5331E)

从API version 19开始，该示例通过调用[ShowDialogOptions](js-apis-promptaction.md#showdialogoptions)中的onDidAppear、onDidDisappear、onWillAppear和onWillDisappear属性展示了弹窗生命周期的相关接口的使用方法。

```
1. // xxx.ets
2. import { BusinessError } from '@kit.BasicServicesKit';

4. @Entry
5. @Component
6. struct DialogExample {
7. @State log: string = 'Log information:';
8. build() {
9. Column() {
10. Button('showDialog')
11. .onClick(() => {
12. this.showCustomDialog();
13. })
14. Text(this.log).fontSize(30).margin({ top: 200 })
15. }.width('100%').margin({ top: 5 })
16. }

18. showCustomDialog() {
19. try {
20. this.getUIContext().getPromptAction().showDialog({
21. title: '操作确认',
22. message: '您确定要执行此操作吗？',
23. alignment: DialogAlignment.Bottom,
24. buttons: [
25. {
26. text: '取消',
27. color: '#999999'
28. },
29. {
30. text: '确定',
31. color: '#007DFF'
32. }
33. ],
34. onDidAppear: () => {
35. this.log += '# onDidAppear';
36. console.info("showDialog,is onDidAppear!");
37. },
38. onDidDisappear: () => {
39. this.log += '# onDidDisappear';
40. console.info("showDialog,is onDidDisappear!");
41. },
42. onWillAppear: () => {
43. this.log = 'Log information:#onWillAppear';
44. console.info("showDialog,is onWillAppear!");
45. },
46. onWillDisappear: () => {
47. this.log += '# onWillDisappear';
48. console.info("showDialog,is onWillDisappear!");
49. },
50. })
51. } catch (error) {
52. let err: BusinessError = error as BusinessError;
53. console.error(`捕获到异常: ${err.code}, ${err.message}`);
54. }
55. }
56. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/46/v3/NAUjxDj_RBis6NTTGmRW7w/zh-cn_image_0000002583479427.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000030Z&HW-CC-Expire=86400&HW-CC-Sign=CD55C37E720BCB187C9CCDEBFDB28EE658EFD4E24410288F4F8D844EBEE2B9C0)

## promptAction.showActionMenu(deprecated)

PhonePC/2in1TabletTVWearable

showActionMenu(options: ActionMenuOptions, callback: AsyncCallback<ActionMenuSuccessResponse>):void

创建并显示操作菜单，菜单响应结果使用callback异步回调返回。

说明

* 从API version 9开始支持，从API version 18开始废弃，建议使用[showActionMenu](arkts-apis-uicontext-promptaction.md#showactionmenu11)替代。showActionMenu需先通过[UIContext](arkts-apis-uicontext-uicontext.md)中的[getPromptAction](arkts-apis-uicontext-uicontext.md#getpromptaction)方法获取[PromptAction](arkts-apis-uicontext-promptaction.md)对象，然后通过该对象进行调用。且直接使用showActionMenu可能导致[UI上下文不明确](../harmonyos-guides/arkts-global-interface.md#ui上下文不明确)的问题。
* 从API version 11开始，可以通过使用[UIContext](arkts-apis-uicontext-uicontext.md)中的[getPromptAction](arkts-apis-uicontext-uicontext.md#getpromptaction)方法获取当前UI上下文关联的[PromptAction](arkts-apis-uicontext-promptaction.md)对象。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [ActionMenuOptions](js-apis-promptaction.md#actionmenuoptions) | 是 | 操作菜单选项。 |
| callback | AsyncCallback<[ActionMenuSuccessResponse](js-apis-promptaction.md#actionmenusuccessresponse)> | 是 | 回调函数。弹出操作菜单成功，err为undefined，data为获取到的操作菜单响应结果，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[接口调用异常错误码](errorcode-internal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |
| 100001 | Internal error. |

**示例：1**

```
1. import { promptAction } from '@kit.ArkUI';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. try {
5. promptAction.showActionMenu({
6. title: 'Title Info',
7. buttons: [
8. {
9. text: 'item1',
10. color: '#666666'
11. },
12. {
13. text: 'item2',
14. color: '#000000'
15. },
16. ]
17. }, (err, data) => {
18. if (err) {
19. console.info('showActionMenu err: ' + err);
20. return;
21. }
22. console.info('showActionMenu success callback, click button: ' + data.index);
23. })
24. } catch (error) {
25. let message = (error as BusinessError).message
26. let code = (error as BusinessError).code
27. console.error(`showActionMenu args error code is ${code}, message is ${message}`);
28. };
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bb/v3/UHNLTzboTiGMp_XLaDiZ2w/zh-cn_image_0000002552799778.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000030Z&HW-CC-Expire=86400&HW-CC-Sign=6518225A8B5D6002AA05DB98E5BE6F15CF9785A7A42B3CAF234EAE58F9C238B4)

**示例：2**

从API version 19开始，该示例通过调用[ActionMenuOptions](js-apis-promptaction.md#actionmenuoptions)中的onDidAppear、onDidDisappear、onWillAppear和onWillDisappear属性展示了操作菜单生命周期相关接口的使用方法。

```
1. import { promptAction } from '@kit.ArkUI';

3. @Entry
4. @Component
5. struct Index {
6. @State isShown: boolean = false
7. @State textColor: Color = Color.Black
8. @State blueColor: Color = Color.Blue

10. @State onWillAppear: boolean = false
11. @State onDidAppear: boolean = false
12. @State onWillDisappear: boolean = false
13. @State onDidDisappear: boolean = false
14. build() {
15. Column({ space: 50 }) {
16. Text('onWillAppear').fontColor(this.onWillAppear ? this.blueColor : this.textColor)
17. Text('onDidAppear').fontColor(this.onDidAppear ? this.blueColor : this.textColor)
18. Text('onWillDisappear').fontColor(this.onWillDisappear ? this.blueColor : this.textColor)
19. Text('onDidDisappear').fontColor(this.onDidDisappear ? this.blueColor : this.textColor)
20. Button('click')
21. .width(200)
22. .height(100)
23. .margin(100)
24. .fontColor(this.textColor)
25. .onClick(() => {
26. promptAction.showActionMenu({
27. title: 'showActionMenu Title Info',
28. buttons: [
29. {
30. text: 'item1',
31. color: '#666666'
32. },
33. {
34. text: 'item2',
35. color: '#000000'
36. },
37. ],
38. onWillAppear:() => {
39. console.info("promptAction menu cycle life onWillAppear");
40. this.onWillAppear = true;
41. },
42. onDidAppear:() => {
43. console.info("promptAction menu cycle life onDidAppear");
44. this.onDidAppear = true;
45. },
46. onWillDisappear:() => {
47. this.isShown = false;
48. console.info("promptAction menu cycle life onWillDisappear");
49. this.onWillDisappear = true;
50. },
51. onDidDisappear:() => {
52. console.info("promptAction menu cycle life onDidDisappear");
53. this.onDidDisappear = true;
54. }
55. })
56. .then(data => {
57. console.info('showActionMenu success, click button: ' + data.index);
58. })
59. .catch((err: Error) => {
60. console.info('showActionMenu error: ' + err);
61. })
62. })
63. }
64. .width('100%')
65. }
66. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1b/v3/U0XumdoLR66xPiKnBhHg_g/zh-cn_image_0000002583439473.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000030Z&HW-CC-Expire=86400&HW-CC-Sign=5518F3F480517050B9DAD3E4574F29A6CCEECEBF19FB93560F53A1ADF15A1CC7)

## promptAction.showActionMenu(deprecated)

PhonePC/2in1TabletTVWearable

showActionMenu(options: ActionMenuOptions): Promise<ActionMenuSuccessResponse>

创建并显示操作菜单，菜单响应后通过Promise返回结果。

说明

* 从API version 9开始支持，从API version 18开始废弃，建议使用[showActionMenu](arkts-apis-uicontext-promptaction.md#showactionmenu)替代。showActionMenu需先通过[UIContext](arkts-apis-uicontext-uicontext.md)中的[getPromptAction](arkts-apis-uicontext-uicontext.md#getpromptaction)方法获取[PromptAction](arkts-apis-uicontext-promptaction.md)对象，然后通过该对象进行调用。且直接使用showActionMenu可能导致[UI上下文不明确](../harmonyos-guides/arkts-global-interface.md#ui上下文不明确)的问题。
* 从API version 10开始，可以通过使用[UIContext](arkts-apis-uicontext-uicontext.md)中的[getPromptAction](arkts-apis-uicontext-uicontext.md#getpromptaction)方法获取当前UI上下文关联的[PromptAction](arkts-apis-uicontext-promptaction.md)对象。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [ActionMenuOptions](js-apis-promptaction.md#actionmenuoptions) | 是 | Promise对象，返回菜单的响应结果。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[ActionMenuSuccessResponse](js-apis-promptaction.md#actionmenusuccessresponse)> | Promise对象，返回菜单的响应结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[接口调用异常错误码](errorcode-internal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |
| 100001 | Internal error. |

**示例：**

```
1. import { promptAction } from '@kit.ArkUI';

3. promptAction.showActionMenu({
4. title: 'showActionMenu Title Info',
5. buttons: [
6. {
7. text: 'item1',
8. color: '#666666'
9. },
10. {
11. text: 'item2',
12. color: '#000000'
13. },
14. ]
15. })
16. .then(data => {
17. console.info('showActionMenu success, click button: ' + data.index);
18. })
19. .catch((err: Error) => {
20. console.info('showActionMenu error: ' + err);
21. })
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d8/v3/U6b4dMWcS9Okyee_HJJsdA/zh-cn_image_0000002552959428.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000030Z&HW-CC-Expire=86400&HW-CC-Sign=8A76EC6BE9DBB98C12D6685A08D0886690FBAE3DDF6843FE200CB8A34DE7947B)

## promptAction.openCustomDialog(deprecated)

PhonePC/2in1TabletTVWearable

openCustomDialog(options: CustomDialogOptions): Promise<number>

打开自定义弹窗。通过Promise返回结果。

弹窗宽度在设备竖屏时默认为 所在窗口宽度 - 左右margin（16vp，设备为2in1时为40vp），最大默认宽度为400vp。

说明

* 从API version 11开始支持，从API version 18开始废弃，建议使用[openCustomDialog](arkts-apis-uicontext-promptaction.md#opencustomdialog12-1)替代。openCustomDialog需先通过[UIContext](arkts-apis-uicontext-uicontext.md)中的[getPromptAction](arkts-apis-uicontext-uicontext.md#getpromptaction)方法获取[PromptAction](arkts-apis-uicontext-promptaction.md)对象，然后通过该对象进行调用。且直接使用openCustomDialog可能导致[UI上下文不明确](../harmonyos-guides/arkts-global-interface.md#ui上下文不明确)的问题。
* 从API version 12开始，可以通过使用[UIContext](arkts-apis-uicontext-uicontext.md)中的[getPromptAction](arkts-apis-uicontext-uicontext.md#getpromptaction)方法获取当前UI上下文关联的[PromptAction](arkts-apis-uicontext-promptaction.md)对象。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [CustomDialogOptions](js-apis-promptaction.md#customdialogoptions11) | 是 | 自定义弹窗的内容。  **说明：** 如果BaseDialogOptions中的[isModal](js-apis-promptaction.md#basedialogoptions11)与[showInSubWindow](js-apis-promptaction.md#basedialogoptions11)同时设置为true，则只生效showInSubWindow = true，此时为非模态弹出框且不会显示蒙层，并在子窗口中显示。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | 返回供closeCustomDialog使用的对话框id。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[接口调用异常错误码](errorcode-internal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |
| 100001 | Internal error. |

**示例：**

```
1. import { promptAction } from '@kit.ArkUI';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. @Entry
5. @Component
6. struct Index {
7. private customDialogComponentId: number = 0;

9. @Builder
10. customDialogComponent() {
11. Column() {
12. Text('弹窗').fontSize(30)
13. Row({ space: 50 }) {
14. Button("确认").onClick(() => {
15. try {
16. promptAction.closeCustomDialog(this.customDialogComponentId)
17. } catch (error) {
18. let message = (error as BusinessError).message;
19. let code = (error as BusinessError).code;
20. console.error(`closeCustomDialog error code is ${code}, message is ${message}`);
21. }
22. })
23. Button("取消").onClick(() => {
24. try {
25. promptAction.closeCustomDialog(this.customDialogComponentId)
26. } catch (error) {
27. let message = (error as BusinessError).message;
28. let code = (error as BusinessError).code;
29. console.error(`closeCustomDialog error code is ${code}, message is ${message}`);
30. }
31. })
32. }
33. }.height(200).padding(5).justifyContent(FlexAlign.SpaceBetween)
34. }

36. build() {
37. Row() {
38. Column({ space: 20 }) {
39. Text('组件内弹窗')
40. .fontSize(30)
41. .onClick(() => {
42. promptAction.openCustomDialog({
43. builder: () => {
44. this.customDialogComponent()
45. },
46. onWillDismiss: (dismissDialogAction: DismissDialogAction) => {
47. console.info('reason' + JSON.stringify(dismissDialogAction.reason));
48. console.info('dialog onWillDismiss');
49. if (dismissDialogAction.reason == DismissReason.PRESS_BACK) {
50. dismissDialogAction.dismiss();
51. }
52. if (dismissDialogAction.reason == DismissReason.TOUCH_OUTSIDE) {
53. dismissDialogAction.dismiss();
54. }
55. }
56. }).then((dialogId: number) => {
57. this.customDialogComponentId = dialogId;
58. })
59. .catch((error: BusinessError) => {
60. console.error(`openCustomDialog error code is ${error.code}, message is ${error.message}`);
61. })
62. })
63. }
64. .width('100%')
65. }
66. .height('100%')
67. }
68. }
```

该示例定义了弹窗样式，如宽度、高度、背景色、阴影等。

说明

直接使用openCustomDialog可能导致实例不明确的问题，建议使用[UIContext](arkts-apis-uicontext-uicontext.md)中的[getPromptAction](arkts-apis-uicontext-uicontext.md#getpromptaction)获取[PromptAction](arkts-apis-uicontext-promptaction.md)对象，再通过此对象调用替代方法[openCustomDialog](arkts-apis-uicontext-promptaction.md#opencustomdialog12-1)。

```
1. import { LevelMode, ImmersiveMode } from '@kit.ArkUI';

3. let customDialogId: number = 0;

5. @Builder
6. function customDialogBuilder(uiContext: UIContext) {
7. Column() {
8. Text('Custom dialog Message').fontSize(10)
9. Row() {
10. Button("确认").onClick(() => {
11. uiContext.getPromptAction().closeCustomDialog(customDialogId);
12. })
13. Blank().width(50)
14. Button("取消").onClick(() => {
15. uiContext.getPromptAction().closeCustomDialog(customDialogId);
16. })
17. }
18. }
19. }

21. @Entry
22. @Component
23. struct Index {
24. @State message: string = 'Hello World';
25. private uiContext: UIContext = this.getUIContext();

27. @Builder
28. customDialogComponent() {
29. customDialogBuilder(this.uiContext)
30. }

32. build() {
33. Row() {
34. Column() {
35. Text(this.message).id("test_text")
36. .fontSize(50)
37. .fontWeight(FontWeight.Bold)
38. .onClick(() => {
39. const node: FrameNode | null = this.uiContext.getFrameNodeById("test_text") || null;
40. this.uiContext.getPromptAction().openCustomDialog({
41. builder: () => {
42. this.customDialogComponent()
43. },
44. keyboardAvoidMode: KeyboardAvoidMode.NONE,
45. showInSubWindow: false,
46. offset: { dx: 5, dy: 5 },
47. backgroundColor: 0xd9ffffff,
48. cornerRadius: 20,
49. width: '80%',
50. height: 200,
51. borderWidth: 1,
52. borderStyle: BorderStyle.Dashed, // 使用borderStyle属性，需要和borderWidth属性一起使用
53. borderColor: Color.Blue, // 使用borderColor属性，需要和borderWidth属性一起使用
54. shadow: ({
55. radius: 20,
56. color: Color.Grey,
57. offsetX: 50,
58. offsetY: 0
59. }),
60. levelMode: LevelMode.EMBEDDED,
61. levelUniqueId: node?.getUniqueId(),
62. immersiveMode: ImmersiveMode.DEFAULT,
63. }).then((dialogId: number) => {
64. customDialogId = dialogId;
65. })
66. })
67. }
68. .width('100%')
69. }
70. .height('100%')
71. }
72. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7f/v3/V4Su13pqT3mlQRmDxzS_yQ/zh-cn_image_0000002583479429.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000030Z&HW-CC-Expire=86400&HW-CC-Sign=4AD760052480D8DCB6528312D14241DB0BDF1168E229B6ED876D62BA4D31DFAA)

该示例实现了一个页面内的弹窗。

说明

直接使用openCustomDialog可能导致实例不明确的问题，建议使用[UIContext](arkts-apis-uicontext-uicontext.md)中的[getPromptAction](arkts-apis-uicontext-uicontext.md#getpromptaction)获取[PromptAction](arkts-apis-uicontext-promptaction.md)对象，再通过此对象调用替代方法[openCustomDialog](arkts-apis-uicontext-promptaction.md#opencustomdialog12-1)。

```
1. // Index.ets
2. import { LevelMode, ImmersiveMode } from '@kit.ArkUI';

4. let customDialogId: number = 0;

6. @Builder
7. function customDialogBuilder(uiContext: UIContext) {
8. Column() {
9. Text('Custom dialog Message').fontSize(10).height(100)
10. Row() {
11. Button("Next").onClick(() => {
12. uiContext.getRouter().pushUrl({ url: 'pages/Next' });
13. })
14. Blank().width(50)
15. Button("Close").onClick(() => {
16. uiContext.getPromptAction().closeCustomDialog(customDialogId);
17. })
18. }
19. }.padding(20)
20. }

22. @Entry
23. @Component
24. struct Index {
25. @State message: string = 'Hello World';
26. private uiContext: UIContext = this.getUIContext();

28. @Builder
29. customDialogComponent() {
30. customDialogBuilder(this.uiContext)
31. }

33. build() {
34. Row() {
35. Column() {
36. Text(this.message).id("test_text")
37. .fontSize(50)
38. .fontWeight(FontWeight.Bold)
39. .onClick(() => {
40. const node: FrameNode | null = this.uiContext.getFrameNodeById("test_text") || null;
41. this.uiContext.getPromptAction().openCustomDialog({
42. builder: () => {
43. this.customDialogComponent()
44. },
45. levelMode: LevelMode.EMBEDDED,
46. levelUniqueId: node?.getUniqueId(),
47. immersiveMode: ImmersiveMode.DEFAULT,
48. }).then((dialogId: number) => {
49. customDialogId = dialogId;
50. })
51. })
52. }
53. .width('100%')
54. }
55. .height('100%')
56. }
57. }
```

```
1. // Next.ets
2. @Entry
3. @Component
4. struct Next {
5. @State message: string = 'Back';

7. build() {
8. Row() {
9. Column() {
10. Button(this.message)
11. .onClick(() => {
12. this.getUIContext().getRouter().back();
13. })
14. }
15. .width('100%')
16. }
17. .height('100%')
18. }
19. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/91/v3/VE12xxP1TyyxVAD14X_VxA/zh-cn_image_0000002552799780.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000030Z&HW-CC-Expire=86400&HW-CC-Sign=83DAF3D16E4526676DDC257EECB47366095336DD957B7F5779B90E8C30DD10E7)

## promptAction.closeCustomDialog(deprecated)

PhonePC/2in1TabletTVWearable

closeCustomDialog(dialogId: number): void

关闭自定义弹窗。

说明

* 从API version 11开始支持，从API version 18开始废弃，建议使用[closeCustomDialog](arkts-apis-uicontext-promptaction.md#closecustomdialog12-1)替代。closeCustomDialog需先通过[UIContext](arkts-apis-uicontext-uicontext.md)中的[getPromptAction](arkts-apis-uicontext-uicontext.md#getpromptaction)方法获取[PromptAction](arkts-apis-uicontext-promptaction.md)对象，然后通过该对象进行调用。且直接使用closeCustomDialog可能导致[UI上下文不明确](../harmonyos-guides/arkts-global-interface.md#ui上下文不明确)的问题。
* 从API version 12开始，可以通过使用[UIContext](arkts-apis-uicontext-uicontext.md)中的[getPromptAction](arkts-apis-uicontext-uicontext.md#getpromptaction)方法获取当前UI上下文关联的[PromptAction](arkts-apis-uicontext-promptaction.md)对象。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| dialogId | number | 是 | openCustomDialog返回的对话框id。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[接口调用异常错误码](errorcode-internal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |
| 100001 | Internal error. |

**示例：**

示例请看[promptAction.openCustomDialog](js-apis-promptaction.md#promptactionopencustomdialogdeprecated)的示例。
