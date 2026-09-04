---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-allow-force-dark
title: 禁用反色能力
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 通用属性 > 基础属性 > 禁用反色能力
category: harmonyos-references
scraped_at: 2026-09-05T06:17:02+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:23d41e10834c77435c3c0682627c6eb0ae2acfe1a31038bc2b65ae540de179fb
---

设置组件是否使用反色能力，反色能力是在深浅色切换时自动对颜色值进行反色或变换，开发者可以通过主动设置不启用反色算法，以保持在深浅色切换时的原有逻辑。

**说明** 

* 本模块首批接口从API version 21开始支持。后续版本的新增接口，采用上角标单独标记该接口的起始版本。
* 本模块接口仅可在Stage模型下使用。

## allowForceDark

allowForceDark(value: boolean): T

设置组件是否使用反色能力。

**说明** 

* 当组件主动设置不使用反色能力时，该组件及其所有子组件均不启用反色能力，不受父组件、祖先组件以及自身子组件的反色配置影响。
* 该接口仅在开启了反色能力的情况下生效，开启反色能力可参考[利用反色能力快速适配深色模式](../harmonyos-guides/ui-dark-light-color-adaptation.md#利用反色能力快速适配深色模式)。

**元服务API：** 从API version 21开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean | 是 | 组件是否使用反色能力。true：组件使用反色能力；false：组件不使用反色能力。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## 示例

```ts
// 组件添加allowForceDark(false)属性后，说明对当前组件不使用反色相关能力。
@Entry
@Component
struct ComponentPage {
  build() {
    Column() {
      Column() {
        Text("Hello World")
          .fontSize(20)
          .fontColor(Color.Blue)
          .onClick(() => {
            console.info(`Text is clicked`);
          })
      }
      .allowForceDark(false) // Column及其子组件Text不生效反色能力，不受父组件Column使用反色能力的影响。

      Row() {
        Button('BUTTON')
          .backgroundColor(Color.Grey)
          .allowForceDark(true)
          .onClick(() => {
            console.info(`Button is clicked`);
          })
      }
      .allowForceDark(false) // Row及其子组件Button不生效反色能力，不受父组件Column使用反色能力的影响。
    }
    .allowForceDark(true)
    .width('100%')
    .height('100%')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/98/v3/ptQ5EYdKTjW8EVrt7vph3g/zh-cn_image_0000002712245868.png)
