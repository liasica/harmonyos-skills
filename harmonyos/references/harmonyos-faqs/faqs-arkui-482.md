---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-482
title: Text组件设置opacity后，文字颜色在整体透明度基础上叠加了一个透明，应该如何处理
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > Text组件设置opacity后，文字颜色在整体透明度基础上叠加了一个透明，应该如何处理
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:00+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:19cf2af34c5b6d02adab52430d628c8363412da7ff552d25c25af2cb4b91a5b2
---

通过给组件设置renderGroup(true)或者blendMode(BlendMode.SRC\_OVER, BlendApplyType.OFFSCREEN)来实现。

可以参考如下示例：

```typescript
@Entry
@Component
struct Index {
  build() {
    Row() {
      Column() {
        Text('你好')
          .width(200)
          .height(100)
          .fontColor(Color.White)
          .backgroundColor(Color.Blue)
          .fontSize(20)
          .textAlign(TextAlign.Center)
          .opacity(0.3)
          .margin(20)

        Text('你好')
          .width(200)
          .height(100)
          .fontColor(Color.White)
          .backgroundColor(Color.Blue)
          .fontSize(20)
          .textAlign(TextAlign.Center)
          .opacity(0.3)
          .renderGroup(true)
      }
      .width('100%')
    }
    .height('100%')
  }
}
```
