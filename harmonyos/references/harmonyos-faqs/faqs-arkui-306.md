---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-306
title: 如何识别双击手势时忽视单击手势
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 如何识别双击手势时忽视单击手势
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:59+08:00
doc_updated_at: 2026-06-15
content_hash: sha256:2efe87f1625f7ee1acc0fc8f94b58d22589f67cd39ac89d6629401bafb068521
---

使用组合手势GestureGroup的互斥识别。双击事件应置于单击事件之前，互斥识别按排列顺序进行。如果单击事件在前，则只会识别单击事件。参考代码如下：

```typescript
@Entry
@Component
struct TapGestureExample {
  build() {
    Column() {
      Text('Click twice')
        .fontSize(28)
        .gesture(GestureGroup(GestureMode.Exclusive,
          TapGesture({ count: 2 })
            .onAction(() => {
              console.info('TapGesture 2');
            }),
          TapGesture({ count: 1 })
            .onAction(() => {
              console.info('TapGesture 1');
            })
        ))
    }
    .width('100%')
    .height('100%')
    .justifyContent(FlexAlign.Center)
    .alignSelf(ItemAlign.Center)
  }
}
```

**参考链接**

[互斥识别](../harmonyos-guides/arkts-gesture-events-combined-gestures.md#互斥识别)
