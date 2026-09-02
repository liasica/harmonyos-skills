---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/displaysync-animation
title: 请求动画绘制帧率
breadcrumb: 指南 > 图形 > ArkGraphics 2D（方舟2D图形服务） > 使用可变帧率能力定制不同内容的绘制帧率 > 请求动画绘制帧率
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:20+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:f8faf74e8cdc05e769d91adc90d1babc3c4826fb348eb98f89c405cea097c74d
---

在应用开发中，[属性动画](../harmonyos-references/ts-animatorproperty.md)和[显式动画](../harmonyos-references/ts-explicit-animation.md)能够使用可选参数[ExpectedFrameRateRange](../harmonyos-references/ts-explicit-animation.md#expectedframeraterange11)，为不同的动画配置不同的期望绘制帧率。

## 请求属性动画的绘制帧率

定义文本组件的属性动画，请求绘制帧率为60，范例如下：

```typescript
Text('60')
  // ...
  .animation({
    duration: 1200,
    iterations: 10,
    // ...
    expectedFrameRateRange: {
      expected: 60,
      min: 0,
      max: 120,
    },
  })
```

## 请求显式动画的绘制帧率

定义按钮组件的显式动画，请求绘制帧率为30，范例如下：

```typescript
Button('Start')
  // ...
  .onClick(() => {
    // ...

    this.uiContext?.animateTo({
      duration: 1200,
      iterations: 10,
      // ...
      expectedFrameRateRange: {
        expected: 30,
        min: 0,
        max: 120,
      },
    }, () => {
      // ...
    })

    // ...
  })
```
