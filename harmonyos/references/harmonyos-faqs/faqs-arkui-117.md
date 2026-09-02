---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-117
title: 文本组件是否支持分段设置字体样式
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 文本组件是否支持分段设置字体样式
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:58+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:089506e11c0dd1a1ffb2f467864aef769ae58ff98252221d377488cddc9334b6
---

单个组件只能设置一种字体样式，可以通过多个Span子组件实现一行文本展示不同样式。参考代码如下：

```ts
@Entry
@Component
struct TestDemoPage {
  @State message: string = "Hello World";

  build() {
    Row() {
      Column() {
        Text() {
          // Using the Span subcomponent to implement segmented style settings
          Span('test text: ')
            .fontSize(20)
            .fontWeight(FontWeight.Bolder)
            .fontColor(Color.Black)
          Span(this.message)
            .fontSize(15)
            .fontColor(Color.Red)
        }
      }
      .width('100%')
    }
    .height('100%')
  }
}
```

**参考链接**

[Text](../harmonyos-references/ts-basic-components-text.md)
