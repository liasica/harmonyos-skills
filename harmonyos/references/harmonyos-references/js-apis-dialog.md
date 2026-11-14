---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-dialog
title: "@ohos.arkui.dialog (弹出框)"
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS API > UI界面 > @ohos.arkui.dialog (弹出框)
category: harmonyos-references
scraped_at: 2026-11-14T08:49:54+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:c031ffa8d0f45bfdcacf15a9c994004f5969813f486fe5784e9c6fbc027f613c
---

为满足应用中灵活配置与管理弹出框的需求，本模块提供统一的Dialog类型声明能力，包括弹出框选项、按钮配置、工作表项以及弹出框控制器、对齐方式、状态等枚举。具体接口调用请使用UIContext中的[DialogPresenter](arkts-apis-uicontext-dialogpresenter.md)对象。

**说明** 

弹出框的弹出、更新与关闭请通过UIContext中的[getDialogPresenter()](arkts-apis-uicontext-uicontext.md#getdialogpresenter)方法获取到[DialogPresenter](arkts-apis-uicontext-dialogpresenter.md)对象后调用。

**起始版本：** 26.0.1

## 导入模块

```ts
import { dialog } from '@kit.ArkUI';
```

## DialogTextStyleOptions

在Dialog中定义文本样式属性，可作为消息内容的文字样式。

**起始版本：** 26.0.1

**元服务API：** 从API版本26.0.1开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| wordBreak | [WordBreak](ts-appendix-enums.md#wordbreak11) | 否 | 是 | 设置分词类型。  默认值：WordBreak.BREAK\_ALL |

## DialogButton

固定样式弹出框的按钮配置。

**起始版本：** 26.0.1

**元服务API：** 从API版本26.0.1开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| value | [ResourceStr](ts-types.md#resourcestr) | 否 | 否 | 按钮的文本内容。 |
| fontColor | [ResourceColor](ts-types.md#resourcecolor) | 否 | 是 | 按钮文字颜色。  默认值：跟随系统主题。 |
| backgroundColor | [ResourceColor](ts-types.md#resourcecolor) | 否 | 是 | 按钮背景色。  默认值：跟随系统主题。 |
| enabled | boolean | 否 | 是 | 点击按钮时是否响应。值为true表示响应，值为false表示不响应。  默认值：true |
| primary | boolean | 否 | 是 | 定义按钮是否默认响应回车/空格键。值为true表示默认响应，值为false表示不默认响应。  默认值：false |
| style | [DialogButtonStyle](ts-appendix-enums.md#dialogbuttonstyle10) | 否 | 是 | 按钮的样式。  默认值：DialogButtonStyle.DEFAULT |
| action | [VoidCallback](ts-types.md#voidcallback12) | 否 | 否 | 点击按钮时执行的回调。 |

## DialogSheet

弹出框列表配置项，用于ActionSheet样式的弹出框。

**起始版本：** 26.0.1

**元服务API：** 从API版本26.0.1开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| title | [ResourceStr](ts-types.md#resourcestr) | 否 | 否 | 标题内容。 |
| icon | [ResourceStr](ts-types.md#resourcestr) | 否 | 是 | 图标内容。  默认值：空 |
| action | [VoidCallback](ts-types.md#voidcallback12) | 否 | 否 | 单击选项时执行的回调。 |

## DialogBaseOptions

所有弹出框共享的基本选项，定义弹出框的背景、边框、对齐、蒙层、避让等通用属性。[DialogStyleOptions](js-apis-dialog.md#dialogstyleoptions)与[DialogCustomOptions](js-apis-dialog.md#dialogcustomoptions)均继承自本接口。

**起始版本：** 26.0.1

**元服务API：** 从API版本26.0.1开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| controller | [DialogBaseController](js-apis-dialog.md#dialogbasecontroller) | 否 | 是 | Dialog控制器。 |
| width | [Dimension](ts-types.md#dimension10) | 否 | 是 | 弹出框的宽度。  默认值：根据内容自适应。 |
| height | [Dimension](ts-types.md#dimension10) | 否 | 是 | 弹出框的高度。  默认值：根据内容自适应。 |
| backgroundColor | [ResourceColor](ts-types.md#resourcecolor) | 否 | 是 | 弹出框的背景颜色。  默认值：Color.Transparent  **说明：** 当backgroundColor设置为非透明色时，backgroundBlurStyle必须设置为BlurStyle.NONE。 |
| backgroundBlurStyle | [BlurStyle](ts-universal-attributes-background.md#blurstyle9) | 否 | 是 | 弹出框的背景模糊样式。  默认值：BlurStyle.COMPONENT\_ULTRA\_THICK  **说明：** 设置为BlurStyle.NONE即可关闭背景模糊。当设置了backgroundBlurStyle为非NONE值时，则不要设置backgroundColor，否则颜色显示将不符合预期效果。当设置系统材质systemMaterial时，backgroundBlurStyle不生效。 |
| backgroundBlurStyleOptions | [BackgroundBlurStyleOptions](ts-universal-attributes-background.md#backgroundblurstyleoptions10对象说明) | 否 | 是 | 带选项的背景模糊样式。默认值与BackgroundBlurStyleOptions类型说明中的默认值一致。 |
| backgroundEffect | [BackgroundEffectOptions](ts-universal-attributes-background.md#backgroundeffectoptions11) | 否 | 是 | 带选项的背景效果。默认值与BackgroundEffectOptions类型说明中的默认值一致。 |
| borderRadius | [Dimension](ts-types.md#dimension10) | [BorderRadiuses](ts-types.md#borderradiuses9) | [LocalizedBorderRadiuses](ts-types.md#localizedborderradiuses12) | 否 | 是 | 背景的边框圆角半径。  默认值：{ topLeft: '32vp', topRight: '32vp', bottomLeft: '32vp', bottomRight: '32vp' } |
| borderWidth | [Dimension](ts-types.md#dimension10) | [EdgeWidths](ts-types.md#edgewidths9) | [LocalizedEdgeWidths](ts-types.md#localizededgewidths12) | 否 | 是 | 弹出框边框宽度。  默认值：0 |
| borderColor | [ResourceColor](ts-types.md#resourcecolor) | [EdgeColors](ts-types.md#edgecolors9) | [LocalizedEdgeColors](ts-types.md#localizededgecolors12) | 否 | 是 | 弹出框的边框颜色。  默认值：Color.Black |
| borderStyle | [BorderStyle](ts-appendix-enums.md#borderstyle) | [EdgeStyles](ts-types.md#edgestyles9) | 否 | 是 | 弹出框边框样式。  默认值：BorderStyle.Solid |
| shadow | [ShadowOptions](ts-universal-attributes-image-effect.md#shadowoptions对象说明) | [ShadowStyle](ts-universal-attributes-image-effect.md#shadowstyle10枚举说明) | 否 | 是 | 弹出框的阴影。  当设备为PC/2in1时，默认场景下获焦阴影值为ShadowStyle.OUTER\_FLOATING\_MD，失焦为ShadowStyle.OUTER\_FLOATING\_SM。其他设备默认无阴影。 |
| alignment | [DialogBaseAlignment](js-apis-dialog.md#dialogbasealignment) | 否 | 是 | 弹出框的对齐模式。  默认值：DialogBaseAlignment.DEFAULT |
| offset | [Offset](ts-types.md#offset) | 否 | 是 | 弹出框相对于对齐位置的偏移。  默认值：{ dx: 0, dy: 0 } |
| maskRect | [Rectangle](ts-methods-alert-dialog-box.md#rectangle8类型说明) | 否 | 是 | 弹出框的蒙层区域。  默认值：{ x: 0, y: 0, width: '100%', height: '100%' } |
| maskColor | [ResourceColor](ts-types.md#resourcecolor) | 否 | 是 | 弹出框的蒙层颜色。  默认值：跟随系统主题的默认蒙层颜色。 |
| isModal | boolean | 否 | 是 | 弹出框是否为模态。值为true表示为模态且有蒙层，值为false表示为非模态且无蒙层。  默认值：true |
| showInSubWindow | boolean | 否 | 是 | 是否在子窗口中显示。值为true表示在子窗口中显示，值为false表示在应用内显示。  默认值：false  **说明：** isModal为true和showInSubWindow为true不能同时使用。 |
| displayModeInSubWindow | [DialogDisplayMode](ts-appendix-enums.md#dialogdisplaymode) | 否 | 是 | 定义在子窗口中显示时的弹出框显示模式。  默认值：DialogDisplayMode.SCREEN\_BASED |
| autoCancel | boolean | 否 | 是 | 是否允许通过触摸蒙层或按返回键退出。值为true表示允许退出，值为false表示不允许退出。  默认值：true |
| focusable | boolean | 否 | 是 | 弹出框是否可以获得焦点。值为true表示可以获得焦点，值为false表示不可以获得焦点。  默认值：true |
| dialogTransition | [TransitionEffect](ts-transition-animation-component.md#transitioneffect10对象说明) | 否 | 是 | 用于打开/关闭弹出框内容区域的弹出框过渡动效参数。  默认值：系统默认过渡动效。 |
| maskTransition | [TransitionEffect](ts-transition-animation-component.md#transitioneffect10对象说明) | 否 | 是 | 用于打开/关闭遮罩的蒙层过渡动效参数。  默认值：系统默认蒙层过渡动效。 |
| keyboardAvoidMode | [KeyboardAvoidMode](ts-universal-attributes-popup.md#keyboardavoidmode12枚举说明) | 否 | 是 | 键盘避让模式。  默认值：KeyboardAvoidMode.DEFAULT |
| keyboardAvoidDistance | [LengthMetrics](js-apis-arkui-graphics.md#lengthmetrics12) | 否 | 是 | 弹出框与系统键盘之间的距离。  默认值：系统默认避让距离。 |
| onWillAppear | [VoidCallback](ts-types.md#voidcallback12) | 否 | 是 | 弹出框打开动画开始前的回调函数。 |
| onDidAppear | [VoidCallback](ts-types.md#voidcallback12) | 否 | 是 | 弹出框出现时的回调函数。 |
| onWillDisappear | [VoidCallback](ts-types.md#voidcallback12) | 否 | 是 | 弹出框关闭动画开始前的回调函数。 |
| onDidDisappear | [VoidCallback](ts-types.md#voidcallback12) | 否 | 是 | 弹出框消失时的回调函数。 |
| onWillDismiss | Callback<[DialogDismissal](js-apis-dialog.md#dialogdismissal)> | 否 | 是 | 弹出框交互关闭的回调。  **说明：** 如果注册了此回调，则用户点击蒙层或返回按钮后弹出框不会立即关闭，回调中的reason参数用于判断是否可以关闭弹出框。 |
| enableHoverMode | boolean | 否 | 是 | 是否启用悬停模式。值为true表示启用，值为false表示不启用。  默认值：false |
| hoverModeArea | [HoverModeAreaType](ts-universal-attributes-sheet-transition.md#hovermodeareatype14) | 否 | 是 | 悬停模式下弹出框的显示区域。  默认值：HoverModeAreaType.BOTTOM\_SCREEN |
| levelMode | [LevelMode](js-apis-promptaction.md#levelmode15) | 否 | 是 | 弹出框的显示级别。  默认值：LevelMode.OVERLAY |
| levelUniqueId | number | 否 | 是 | 页面级弹出框显示层下节点的唯一标识。  取值范围：大于等于0的整数。  **说明：** 该参数仅在levelMode为LevelMode.EMBEDDED时生效。 |
| immersiveMode | [ImmersiveMode](js-apis-promptaction.md#immersivemode15) | 否 | 是 | 页面级弹出框蒙层效果。  默认值：ImmersiveMode.DEFAULT  **说明：** 该参数仅在levelMode为LevelMode.EMBEDDED时生效。 |
| levelOrder | [LevelOrder](js-apis-promptaction.md#levelorder18) | 否 | 是 | 弹出框的显示顺序。  默认值：LevelOrder.clamp(0)返回的值。 |
| systemMaterial | [SystemUiMaterial](ts-universal-attributes-image-effect.md#systemuimaterial) | 否 | 是 | 为弹出框设置系统材质，不同的材质有不同的效果，会影响背景色、边框、阴影和弹出框的其他视觉属性。  **说明：**  - 默认值：[ImmersiveOptions](arkts-apis-uimaterial.md#immersiveoptions)的style为ImmersiveStyle.ULTRA\_THICK的[ImmersiveMaterial](arkts-apis-uimaterial.md#immersivematerial)对象。设置undefined时与默认值保持一致。  - 该参数影响背景色[backgroundColor](ts-universal-attributes-background.md#backgroundcolor)、背景模糊[backgroundBlurStyle](ts-universal-attributes-background.md#backgroundblurstyle9)、背景效果[backgroundEffect](ts-universal-attributes-background.md#backgroundeffect11)、边框颜色[borderColor](ts-universal-attributes-border.md#bordercolor)、边框宽度[borderWidth](ts-universal-attributes-border.md#borderwidth)、阴影[shadow](ts-universal-attributes-image-effect.md#shadow)，当设置系统材质时，上述属性不生效。 |

## DialogMessage

弹出框的消息内容与文字样式，继承自[DialogTextStyleOptions](js-apis-dialog.md#dialogtextstyleoptions)。

**起始版本：** 26.0.1

**元服务API：** 从API版本26.0.1开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| content | [ResourceStr](ts-types.md#resourcestr) | 否 | 否 | 弹出框消息内容。 |

## DialogStyleOptions

固定样式弹出框的选项，继承自[DialogBaseOptions](js-apis-dialog.md#dialogbaseoptions)。具体用法可参考DialogPresenter的[present](arkts-apis-uicontext-dialogpresenter.md#present)接口示例。

**起始版本：** 26.0.1

**元服务API：** 从API版本26.0.1开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| title | [ResourceStr](ts-types.md#resourcestr) | 否 | 是 | 弹出框标题。  默认值：未设置时不显示标题。 |
| subtitle | [ResourceStr](ts-types.md#resourcestr) | 否 | 是 | 弹出框的副标题。  默认值：未设置时不显示副标题。 |
| message | [DialogMessage](js-apis-dialog.md#dialogmessage) | 否 | 是 | 弹出框的消息内容和文字样式。  默认值：未设置时不显示消息内容。 |
| buttons | Array<[DialogButton](js-apis-dialog.md#dialogbutton)> | 否 | 是 | 弹出框中的按钮数组。提供时，弹出框显示为带有按钮的警报样式弹出框；与sheets一起使用时，按钮显示在工作表项列表下方。  默认值：未设置时不显示按钮。 |
| buttonDirection | [DialogButtonOrientation](js-apis-dialog.md#dialogbuttonorientation) | 否 | 是 | 按钮的排列方式。  默认值：DialogButtonOrientation.AUTO |
| sheets | Array<[DialogSheet](js-apis-dialog.md#dialogsheet)> | 否 | 是 | action-sheet样式的工作表项数组。提供时，弹出框将显示供用户选择的工作表项。  默认值：未设置时不显示工作表项。 |
| gridCount | number | 否 | 是 | 弹出框中工作表项的网格列数，用于控制工作表项在网格中的分栏显示布局。  默认值：4  取值范围：大于0的整数。 |

## DialogCustomOptions

自定义样式弹出框的选项，继承自[DialogBaseOptions](js-apis-dialog.md#dialogbaseoptions)。

弹出框的内容由[DialogPresenter.present](arkts-apis-uicontext-dialogpresenter.md#present)方法的第一个参数提供，不在此选项对象中。具体用法可参考DialogPresenter的[present](arkts-apis-uicontext-dialogpresenter.md#present)接口示例。

**起始版本：** 26.0.1

**元服务API：** 从API版本26.0.1开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| customStyle | boolean | 否 | 是 | 是否开启自定义样式。值为true表示开启自定义样式，值为false表示不开启。  默认值：false |

## DialogBaseController

用于控制弹出框的类，可通过[DialogBaseOptions](js-apis-dialog.md#dialogbaseoptions)中的controller属性与弹出框绑定。具体用法可参考DialogPresenter的[present](arkts-apis-uicontext-dialogpresenter.md#present)接口示例。

### constructor

constructor()

控制器的构造函数。

**起始版本：** 26.0.1

**元服务API：** 从API版本26.0.1开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

### close

close(): void

关闭相应的弹出框。

**起始版本：** 26.0.1

**元服务API：** 从API版本26.0.1开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

### getState

getState(): DialogState

获取弹出框的状态。

**起始版本：** 26.0.1

**元服务API：** 从API版本26.0.1开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [DialogState](js-apis-dialog.md#dialogstate) | 返回弹出框状态。 |

**示例：**

该示例通过DialogBaseController与弹出框绑定，展示了弹出弹出框，并通过控制器关闭以及获取弹出框状态的功能。

```ts
import { DialogBaseController, DialogPresenter, DialogState } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  private ctx: UIContext = this.getUIContext();
  private dialogPresenter: DialogPresenter = this.ctx.getDialogPresenter();
  private controller: DialogBaseController = new DialogBaseController();
  @State dialogState: DialogState = DialogState.UNINITIALIZED;

  @Builder
  customDialogComponent() {
    Column() {
      Text('Dialog').fontSize(20)
      Column({ space: 10 }) {
        Button('Close dialog via controller').onClick(() => {
          try {
            this.controller.close();
          } catch (error) {
            let message = (error as BusinessError).message;
            let code = (error as BusinessError).code;
            console.error(`Failed to close dialog. Code: ${code}, message: ${message}`);
          }
        })
        Button('Get dialog state')
          .onClick(() => {
            this.dialogState = this.controller.getState();
            console.info('dialog state: ' + this.dialogState);
          })
      }
    }.height(150).padding(20).justifyContent(FlexAlign.SpaceBetween)
  }

  build() {
    Column({ space: 50 }) {
      Text(`Dialog state: ${this.dialogState}`)
      Button('Present dialog')
        .onClick(() => {
          this.dialogPresenter.present(() => { this.customDialogComponent() },
          {
            controller: this.controller,
          })
            .catch((error: BusinessError) => {
              console.error(`Failed to present dialog. Code: ${error.code}, message: ${error.message}`);
            })
        })
      Button('Get dialog state')
        .onClick(() => {
          this.dialogState = this.controller.getState();
          console.info('dialog state: ' + this.dialogState);
        })
    }.width('100%').height('100%').justifyContent(FlexAlign.Start)
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ab/v3/fNsqKYlUSDmB_G92agPzjA/zh-cn_image_0000002817508029.gif?HW-CC-KV=V1&HW-CC-Date=20261114T004952Z&HW-CC-Expire=31536000000&HW-CC-Sign=007B192544C00592999FEBC5E928072831966C00AD49DB2220262493E5D73602)

## DialogResult

对话的响应结果。

**起始版本：** 26.0.1

**元服务API：** 从API版本26.0.1开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| dialogId | number | 否 | 否 | 弹出框的ID。  取值范围：大于等于0的整数。 |

## DialogDismissal

提供关闭弹出框操作的信息与关闭接口。

**起始版本：** 26.0.1

**元服务API：** 从API版本26.0.1开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| dismiss | [VoidCallback](ts-types.md#voidcallback12) | 否 | 否 | 关闭弹出框的回调。只有当需要退出弹出框时，才会调用此接口。 |
| reason | [DismissReason](ts-universal-attributes-popup.md#dismissreason12枚举说明) | 否 | 否 | 触发弹出框关闭操作的原因类型。 |

## DialogBaseAlignment

弹出框的对齐方式。

**起始版本：** 26.0.1

**元服务API：** 从API版本26.0.1开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| TOP | 0 | 垂直顶部对齐。 |
| CENTER | 1 | 垂直居中对齐。 |
| BOTTOM | 2 | 垂直底部对齐。 |
| DEFAULT | 3 | 默认对齐方式。 |
| TOP\_START | 4 | 左上角对齐。 |
| TOP\_END | 5 | 右上角对齐。 |
| CENTER\_START | 6 | 左居中对齐。 |
| CENTER\_END | 7 | 右居中对齐。 |
| BOTTOM\_START | 8 | 左下角对齐。 |
| BOTTOM\_END | 9 | 右下角对齐。 |

## DialogButtonOrientation

弹出框中按钮的排列方式。

**起始版本：** 26.0.1

**元服务API：** 从API版本26.0.1开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| AUTO | 0 | 两个或两个以下的按钮水平排列，两个以上的按钮垂直排列。 |
| HORIZONTAL | 1 | 按钮水平排列。 |
| VERTICAL | 2 | 按钮垂直排列。 |

## DialogState

Dialog状态的枚举。

**起始版本：** 26.0.1

**元服务API：** 从API版本26.0.1开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| UNINITIALIZED | 0 | 表示未初始化。 |
| INITIALIZED | 1 | 表示已初始化。 |
| APPEARING | 2 | 表示正在出现。 |
| APPEARED | 3 | 表示已出现。 |
| DISAPPEARING | 4 | 表示正在消失。 |
| DISAPPEARED | 5 | 表示已消失。 |
