---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-316
title: 如何实现Scroll、List单边回弹效果
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 如何实现Scroll、List单边回弹效果
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:59+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:9c35f5d0db21b4f82ee8958e47cf7c53e718ca9b23727faf6b1f64e5de376ae0
---

1. [Scroll组件](../harmonyos-references/ts-container-scroll.md)：在onDidScroll里获取currentOffset().yOffset来控制单边回弹效果；

2. [List组件](../harmonyos-references/ts-container-list.md)：在onDidScroll里获取currentOffset().yOffset来控制，还可以通过onScrollIndex实现单边回弹效果。

参考代码如下：

```ts
// Single side rebound effect of Scroll component
@Entry
@Component
struct ScrollSideRebound {
  @State yOffset: number = 0;
  scroller: Scroller = new Scroller();
  private arr: number[] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];

  build() {
    Stack({ alignContent: Alignment.TopStart }) {
      Scroll(this.scroller) {
        Column() {
          ForEach(this.arr, (item: number) => {
            Text(item.toString())
              .width('90%')
              .height(150)
              .backgroundColor(0xFFFFFF)
              .borderRadius(15)
              .fontSize(16)
              .textAlign(TextAlign.Center)
              .margin({ top: 10 })
          }, (item: string) => item)
        }
        .width('100%')
      }
      .scrollable(ScrollDirection.Vertical) // Rolling direction vertically
      .scrollBar(BarState.On) // Scroll bar permanent display
      .scrollBarColor(Color.Gray) // Scroll bar color
      .scrollBarWidth(2) // Scroll bar width
      .friction(0.6)
      .edgeEffect(this.yOffset <= 0 ? EdgeEffect.Spring : EdgeEffect.None) // Rebound after rolling to the edge
      .onDidScroll(() => {
        this.yOffset = this.scroller.currentOffset().yOffset;
      })
    }
    .width('100%')
    .height('100%')
    .backgroundColor(0xDCDCDC)
  }
}
```

```ts
// Single side rebound effect of List component
@Entry
@Component
struct ListSideRebound {
  @State isTop: boolean = true;
  private arr: number[] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];

  build() {
    Column() {
      List({ space: 20, initialIndex: 0 }) {
        ForEach(this.arr, (item: number) => {
          ListItem() {
            Text('' + item)
              .width('100%')
              .height(100)
              .fontSize(16)
              .textAlign(TextAlign.Center)
              .borderRadius(10)
              .backgroundColor(0xFFFFFF)
          }
        }, (item: string) => item)
      }
      .listDirection(Axis.Vertical) // Arrangement direction
      .scrollBar(BarState.Off)
      .friction(0.6)
      .edgeEffect(this.isTop ? EdgeEffect.Spring : EdgeEffect.None) // Enable the flex effect only on the top boundary
      .onScrollIndex((firstIndex: number) => {
        if (this.arr.length === 0 || firstIndex === 0) {
          this.isTop = true;
        } else {
          this.isTop = false;
        }
      })
      .width('90%')
    }
    .width('100%')
    .height('100%')
    .backgroundColor(0xDCDCDC)
    .padding({ top: 5 })
  }
}
```
