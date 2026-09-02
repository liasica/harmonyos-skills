---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-8
title: 如何给UI组件设置不同情况下的属性
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 如何给UI组件设置不同情况下的属性
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:58+08:00
doc_updated_at: 2026-06-15
content_hash: sha256:a0ba1354cf1caad736ef2015367ba2488b1675b8101c4132a9e9d1a09ed56ebc
---

使用if/else条件渲染设置组件属性值。具体可参考示例代码：

```typescript
@Entry
@Component
struct TestHeightPage {
  @State message: string = 'Hello World';
  @State myHeight1: number = 30;
  @State myHeight2: number = 60;
  @State flag: boolean = false

  build() {
    Column() {
      Text(this.message)
        .fontSize(20)
        .fontWeight(FontWeight.Bold)
        .width('100%')
        .height(this.flag ? this.myHeight1 : this.myHeight2)
        .backgroundColor(Color.Orange)

      Button('Modify Text attribute height').onClick(() => {
        this.flag = !this.flag;
      }).margin({ top: 12 })
    }
    .height('100%')
  }
}
```

**参考链接**

[if/else：条件渲染](../harmonyos-guides/arkts-rendering-control-ifelse.md)
