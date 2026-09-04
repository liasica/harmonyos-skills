---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-component-size-change-event
title: 组件尺寸变化事件
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 通用事件 > 组件变化事件 > 组件尺寸变化事件
category: harmonyos-references
scraped_at: 2026-09-05T06:17:02+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:798c2e0eac643ebec0ae59d012ca14d842d63fb134e6f34040938962915da604
---

该事件指组件显示的尺寸发生变化时触发的事件，可用于监听组件因布局变化导致的尺寸更新，获取变化前后的宽高信息，适用于需要根据组件实际绘制尺寸处理后续逻辑的场景。

**说明** 

* 从API version 12开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 本模块接口仅可在Stage模型下使用。
* 该事件返回的宽高是组件绘制出来的宽高，可能与组件设置的宽高不同。

## onSizeChange

onSizeChange(event: SizeChangeCallback): T

组件尺寸变化时触发该回调。仅会响应由布局变化所导致的组件尺寸发生变化时的回调。

**说明** 

1. 该接口在布局发生变化时触发，由于计算精度的关系，其返回值可能与真实物理尺寸存在差异。
2. onSizeChange是布局过程中触发的同步回调，直接在其中更改状态变量存在被纳入动画闭包的风险。具体而言，动画会对比动画前的布局与动画闭包后的布局，若onSizeChange的回调在动画前的布局中同步触发，那么onSizeChange回调中所做的变更将与动画闭包中的变更一同纳入动画过程。为了避免此类问题，可在onSizeChange中使用延迟时间为0ms的[setTimeout](js-apis-timer.md#settimeout)或[postFrameCallback](arkts-apis-uicontext-uicontext.md#postframecallback12)，将UI处理逻辑延后至异步执行。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | [SizeChangeCallback](ts-universal-component-size-change-event.md#sizechangecallback) | 是 | 组件尺寸变化时触发的回调函数，用于获取目标元素变化前后的尺寸。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## SizeChangeCallback

type SizeChangeCallback = (oldValue: SizeOptions, newValue: SizeOptions) => void

组件尺寸变化时的回调类型。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| oldValue | [SizeOptions](ts-types.md#sizeoptions) | 是 | 目标元素变化之前的宽高。 |
| newValue | [SizeOptions](ts-types.md#sizeoptions) | 是 | 目标元素变化之后的宽高。 |

## 示例

该示例通过Text组件设置组件尺寸变化事件，当Text尺寸变化时可以触发onSizeChange事件，获取oldValue和newValue参数。

```ts
// xxx.ets
@Entry
@Component
struct AreaExample {
  @State value: string = 'Text'
  @State sizeValue: string = ''

  build() {
    Column() {
      Text(this.value)
        .backgroundColor(Color.Green)
        .margin(30)
        .fontSize(20)
        .onClick(() => {
          this.value = this.value + 'Text';
        })
        .onSizeChange((oldValue: SizeOptions, newValue: SizeOptions) => {
          console.info(`Ace: on size change, oldValue is ${JSON.stringify(oldValue)} newValue is ${JSON.stringify(newValue)}`);
          this.sizeValue = JSON.stringify(newValue);
        })
      Text('new area is: \n' + this.sizeValue).margin({ right: 30, left: 30 })
    }
    .width('100%').height('100%').margin({ top: 30 })
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dc/v3/eYKJYpGJQBiuqh0sSIu0zA/zh-cn_image_0000002742124763.gif)
