---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-32
title: 如何解决子组件全屏后margin不会生效的问题
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 如何解决子组件全屏后margin不会生效的问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:58+08:00
doc_updated_at: 2026-06-15
content_hash: sha256:24dc5b13bfa46464a7408a6dd30715f2eeaafe8ad014fb8ca86556a7840f2e80
---

父组件全屏显示，子组件默认撑满。设置左右margin值后，子组件可能会超出屏幕范围。可以使用`constraintSize`属性限制子组件的最大宽高。参考代码如下：

```typescript
@Entry
@Component
struct Index {
  @State message: string = 'Hello World';

  build() {
    Row() {
      Column() {
        Text(this.message)
          .fontSize(50)
          .fontWeight(FontWeight.Bold)
          .textAlign(TextAlign.Center)
          .width('100%')
          .constraintSize({ maxWidth: '100%' })
          .backgroundColor(Color.Blue)
          .margin({ left: 50, right: 50 })
      }
      .width('100%')
    }
    .height('100%')
  }
}
```

**参考链接**

[尺寸设置](../harmonyos-references/ts-universal-attributes-size.md)中的constraintSize
