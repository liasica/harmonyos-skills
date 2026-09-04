---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-counter
title: Counter
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 信息展示 > Counter
category: harmonyos-references
scraped_at: 2026-09-05T06:17:20+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:6128cd30231f7b98ef6a1a8061a6be484e2fa79c46d9b8b7ba15e96dc1e106dc
---

计数器组件，提供增加或减少的计数操作。适用于商品数量选择、参数调整等需要频繁修改数值的场景，帮助用户快速直观地调整数值。

**说明** 

* 该组件从API version 7开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。
* 该组件从API版本26.0.0开始支持[WithTheme](ts-container-with-theme.md)。

## 子组件

可以包含子组件。

## 接口

Counter()

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 属性

除支持[通用属性](ts-component-general-attributes.md)外，还支持以下属性。

### enableInc10+

enableInc(value: boolean)

设置“增加”按钮的禁用或使能。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean | 是 | “增加”按钮禁用或使能。  默认值：true，true表示使能“增加”按钮，false表示禁用“增加”按钮。 |

### enableDec10+

enableDec(value: boolean)

设置“减少”按钮的禁用或使能。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean | 是 | “减少”按钮禁用或使能。  默认值：true，true表示使能“减少”按钮，false表示禁用“减少”按钮。 |

## 事件

除支持[通用事件](ts-component-general-events.md)外，还支持以下事件：

### onInc

onInc(event: VoidCallback)

监听数值增加事件。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | [VoidCallback](ts-types.md#voidcallback12) | 是 | Counter 数值增加的回调函数。 |

### onDec

onDec(event: VoidCallback)

监听数值减少事件。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | [VoidCallback](ts-types.md#voidcallback12) | 是 | Counter 数值减少的回调函数。 |

## 示例

该示例展示了Counter组件的基本使用方法。点击+、-按钮可以修改计数器的数值。

```ts
// xxx.ets
@Entry
@Component
struct CounterExample {
  @State counterValue1: number = 0;
  @State counterValue2: number = 0;

  build() {
    Column({ space: 50 }) {
      Counter() {
        Text(this.counterValue1.toString())
      }
      .onInc(() => {
        this.counterValue1++;
      })
      .onDec(() => {
        this.counterValue1--;
      })

      Counter() {
        Text(this.counterValue2.toString())
      }
      .onInc(() => {
        this.counterValue2++;
      })
      .onDec(() => {
        this.counterValue2--;
      })
      .enableInc(true)
      .enableDec(false)
    }
    .width('100%')
    .height('100%')
    .justifyContent(FlexAlign.Center)
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/17/v3/3HkinyFvRRO4OPRVWvURNQ/zh-cn_image_0000002712246330.gif)
