---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-142
title: 半模态转场如何控制固定高度
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 半模态转场如何控制固定高度
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:58+08:00
doc_updated_at: 2026-06-15
content_hash: sha256:34e01cd337377df7298ffe6cbcc238c96a38d02985fab958d3e69e3e1505dcf1
---

通过设置bindSheet()的参数options对高度进行控制。参考代码如下：

```typescript
@Entry
@Component
struct SheetTransitionExample {
  @State isShow: boolean = false;
  @State sheetHeight: number = 300;

  @Builder
  myBuilder() {
    Column() {
      Button('change height')
        .margin(10)
        .fontSize(20)
        .onClick(() => {
          this.sheetHeight = 500;
        })

      Button('Set Illegal height')
        .margin(10)
        .fontSize(20)
        .onClick(() => {
          this.sheetHeight = 0;
        })
    }
    .width('100%')
    .height('100%')
  }

  build() {
    Column() {
      Button('transition modal 1')
        .onClick(() => {
          this.isShow = true;
        })
        .fontSize(20)
        .margin(10)
        .bindSheet(this.isShow, this.myBuilder(), { height: this.sheetHeight, backgroundColor: Color.Green })
    }
    .justifyContent(FlexAlign.Center)
    .width('100%')
    .height('100%')
  }
}
```

**参考链接**

[半模态转场](../harmonyos-references/ts-universal-attributes-sheet-transition.md)
