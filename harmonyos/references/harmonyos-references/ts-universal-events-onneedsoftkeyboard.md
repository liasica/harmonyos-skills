---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-events-onneedsoftkeyboard
title: 键盘判断事件
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 通用事件 > 交互响应事件 > 键盘判断事件
category: harmonyos-references
scraped_at: 2026-09-02T15:00:55+08:00
doc_updated_at: 2026-09-01
content_hash: sha256:4a78c58201b80f7ffc9fb7170ab23215c5d2a53767d9dbb7e9808111af8878e0
---

当组件获得焦点时，获焦组件触发该事件，用于在焦点切换时灵活控制软键盘的显示与隐藏。系统会根据该事件回调函数返回值，判断是否需要键盘。主要适用于键盘接续场景，帮助开发者避免键盘频繁收起和拉起，优化用户交互体验。

**说明** 

* 本模块首批接口从API version 24开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 本模块接口仅可在Stage模型下使用。

## onNeedSoftkeyboard

onNeedSoftkeyboard(onNeedSoftkeyboardCallback: OnNeedSoftkeyboardCallback | undefined): T

设置组件判断是否需要键盘时触发的回调。主要用于键盘接续场景。当组件获得焦点时，系统会调用该组件绑定的[OnNeedSoftkeyboardCallback](ts-universal-events-onneedsoftkeyboard.md#onneedsoftkeyboardcallback)回调函数，根据返回值判断是否需要键盘：如果返回值为true，则表示该组件需要键盘，键盘将不会收起；如果返回值为false，则表示该组件不需要键盘，键盘将收起。

对于不能获焦的组件，本接口不生效。

输入框组件使用该接口并将返回值设置为false时，点击输入框将不会拉起键盘。

Web组件使用该方法时，如果返回值为true，Web组件会判断组件中是否有可编辑节点，如果有可编辑节点才会保留键盘，如果返回值为false，无论是否有可编辑节点，键盘都不会保留。

XComponent组件使用该方法时，如果返回值为true且XComponent组件使用[OH\_ArkUI\_XComponent\_SetNeedSoftKeyboard()](capi-native-interface-xcomponent-h.md#oh_arkui_xcomponent_setneedsoftkeyboard)设置了需要键盘，才会保留键盘，如果返回值为false，无论组件如何设置，键盘都不会保留。

当返回值为true时，应用的自绘制输入框需要在获焦时主动调用[attach](js-apis-inputmethod.md#attach15)方法，建立输入法框架和输入法应用的通信，否则点击键盘会失去响应。说明：失焦时输入法框架和输入法应用的通信会断开，获焦时需要重新建立通信。

该接口只适用于对输入法应用接续的场景，对自定义键盘不生效。自定义键盘接续详见[setCustomKeyboardContinueFeature](arkts-apis-uicontext-uicontext.md#setcustomkeyboardcontinuefeature23)。

**元服务API：** 从API version 24开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| onNeedSoftkeyboardCallback | [OnNeedSoftkeyboardCallback](ts-universal-events-onneedsoftkeyboard.md#onneedsoftkeyboardcallback) | undefined | 是 | 事件触发时执行的回调，系统会根据回调的返回值决定是否需要键盘。  设置为undefined时，不会触发回调，输入框类组件行为等同返回true。其他组件行为等同返回false。前提条件：组件需可获焦，否则本接口不生效。当返回值为true时，自绘制输入框需在获焦时主动调用[attach](js-apis-inputmethod.md#attach15)方法建立输入法通信，否则点击键盘会失去响应。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## OnNeedSoftkeyboardCallback

type OnNeedSoftkeyboardCallback = () => boolean

当绑定该方法的组件判断是否需要键盘时，将触发此回调。前提条件：组件需可获焦，否则本接口不生效。

**元服务API：** 从API version 24开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 是否需要键盘。  若此回调的返回值为true，则表明该组件需要键盘；返回值为false，则表明该组件不需要键盘。 |

## 示例

### 示例1（设置键盘接续）

该示例通过[onNeedSoftkeyboard](ts-universal-events-onneedsoftkeyboard.md#onneedsoftkeyboard)接口，设置按钮需要键盘。在从输入框拉起键盘后，点击按钮使焦点切换到按钮，此时键盘将不会收起，再次点击输入框可继续输入。

从API version 24开始，新增[onNeedSoftkeyboard](ts-universal-events-onneedsoftkeyboard.md#onneedsoftkeyboard)接口。

```ts
@Entry
@Component
struct Index {
  build() {
    Column() {
      Button('切换焦点到Button')
        .onClick(() => {
          this.getUIContext().getFocusController().requestFocus('Button');
        })
        .key('Button')
        .fontSize(20)
        .width('80%')
        .margin('10')
        .onNeedSoftkeyboard((): boolean => {
          return true;
        })
      TextInput()
        .key('TextInput1')
    }
    .height('100%')
    .width('100%')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/kVMk6f0gQZaNycbYGD7Rxg/zh-cn_image_0000002706835604.gif)
