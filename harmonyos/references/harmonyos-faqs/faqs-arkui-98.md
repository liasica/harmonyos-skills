---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-98
title: 如何设置组件不同状态下的样式
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 如何设置组件不同状态下的样式
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:27+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:a50761652e47d014afd930a2d3b60e5139c8f33c3f58df0476c91e6ce32942c4
---

使用多态样式，在组件的StateStyles接口中，定义组件不同状态下的样式。参考代码如下：

```typescript
@Component
struct PolymorphicStyle {
  @Styles
  pressedStyles() {
    .backgroundColor('#ED6F21')
    .borderRadius(10)
    .borderStyle(BorderStyle.Dashed)
    .borderWidth(2)
    .borderColor('#33000000')
    .width(120)
    .height(30)
    .opacity(1)
  }

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center }) {
      Text('pressed')
        .backgroundColor('#0A59F7')
        .borderRadius(20)
        .borderStyle(BorderStyle.Dotted)
        .borderWidth(2)
        .borderColor(Color.Red)
        .width(100)
        .height(25)
        .opacity(1)
        .fontSize(14)
        .fontColor(Color.White)
        .stateStyles({
          pressed: this.pressedStyles
        })
        .margin({ bottom: 20 })
        .textAlign(TextAlign.Center)
    }
    .width(350)
    .height(300)
  }
}
```

**参考链接**

[多态样式](../harmonyos-references/ts-universal-attributes-polymorphic-style.md)
