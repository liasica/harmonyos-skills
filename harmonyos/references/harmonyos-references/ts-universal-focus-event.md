---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-focus-event
title: 焦点事件
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 通用事件 > 交互响应事件 > 焦点事件
category: harmonyos-references
scraped_at: 2026-09-05T06:17:02+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:899ae4207713b03d12b15c577c7aab05323ac7b1e2312c93c583249a08ad4ad0
---

焦点事件指页面焦点在可获焦组件间移动时触发的事件，组件可使用焦点事件来处理相关逻辑。

**说明** 

* 本模块首批接口从API version 8开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 不支持嵌套滚动组件场景按键走焦。
* 存在默认交互逻辑的组件例如[Button](ts-basic-components-button.md)、[TextInput](ts-basic-components-textinput.md)等，默认即为可获焦，[Text](ts-basic-components-text.md)、[Image](ts-basic-components-image.md)等组件默认状态为不可获焦，不可获焦状态下，无法触发焦点事件，需要设置[focusable](ts-universal-attributes-focus.md#focusable)属性为true才可触发。
* 对于有获焦能力的容器组件，例如[Stack](ts-container-stack.md)、[Row](ts-container-row.md)等，若不存在可获焦子组件，该容器组件不可获焦。为其配置onClick或是单指单击的Tap手势，且不显式配置focusable属性，该组件会隐式地成为可获焦组件。
* 焦点开发及组件获焦能力参考[支持焦点处理](../harmonyos-guides/arkts-common-events-focus-event.md)。

## onFocus

onFocus(event: () => void): T

当前组件获取焦点时触发的回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | () => void | 是 | onFocus的回调函数，表示组件已获焦。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件，可用于链式调用。 |

## onBlur

onBlur(event:() => void): T

当前组件失去焦点时触发的回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | () => void | 是 | onBlur的回调函数，表示组件已失焦。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件，可用于链式调用。 |

## 示例

该示例展示了组件获焦和失焦的情况，按钮获焦和失焦时会改变按钮的颜色。

```ts
// xxx.ets
@Entry
@Component
struct FocusEventExample {
  @State oneButtonColor: string = '#0066FF'
  @State twoButtonColor: string = '#87CEFA'
  @State threeButtonColor: string = '#90EE90'

  build() {
    Column({ space: 20 }) {
      // 当焦点在三个按钮间移动，按钮获焦时颜色变化，失焦时变回原背景色
      Button('First Button')
        .backgroundColor(this.oneButtonColor)
        .width(260)
        .height(70)
        .fontColor(Color.Black)
        .onFocus(() => {
          this.oneButtonColor = '#FFFFFF';
        })
        .onBlur(() => {
          this.oneButtonColor = '#0066FF';
        })
      Button('Second Button')
        .backgroundColor(this.twoButtonColor)
        .width(260)
        .height(70)
        .fontColor(Color.Black)
        .onFocus(() => {
          this.twoButtonColor = '#FFFFFF';
        })
        .onBlur(() => {
          this.twoButtonColor = '#87CEFA';
        })
      Button('Third Button')
        .backgroundColor(this.threeButtonColor)
        .width(260)
        .height(70)
        .fontColor(Color.Black)
        .onFocus(() => {
          this.threeButtonColor = '#FFFFFF';
        })
        .onBlur(() => {
          this.threeButtonColor = '#90EE90';
        })
    }.width('100%').margin({ top: 20 })
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/41/v3/ZUPgmBuTQtmQjzjzDv2mPw/zh-cn_image_0000002712405808.png)
