---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-137
title: List组件如何设置两端的渐变效果
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > List组件如何设置两端的渐变效果
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:58+08:00
doc_updated_at: 2026-06-15
content_hash: sha256:a99cf8adaf458017416a71f9c36bf345e4b0daa28dfb95722e87b37c1fa95dd5
---

List组件本身不支持直接设置两端渐变效果，但可通过Stack布局结合LinearGradient对象实现效果。参考代码如下：

```typescript
@Entry
@Component
struct ListExample {
  @State arr: number[] = [1, 2, 3, 4, 5, 6, 7, 8, 9]
  private scroller: Scroller = new Scroller()

  build() {
    Stack() {
      List({ space: 10 }) {
        ForEach(this.arr, (item: string) => {
          ListItem() {
            Text("Hello World")
              .width(100)
              .height(64)
              .fontColor(Color.White)
              .backgroundColor(Color.Black)
              .textAlign(TextAlign.Center)
          }
        }, (item: string) => item)
      }
      .listDirection(Axis.Horizontal)
      .scrollBar(BarState.Off)
      .padding({ top: 20, bottom: 20 })
      .width("80%")
      .height("100%")

      Stack() {

      }
      .linearGradient({
        angle: 90,
        colors: [[0x000000, 0.0], ['rgba(0,0,0,0)', 0.1], ['rgba(0,0,0,0)', 0.9], [0x000000, 1.0]]
      })
      .width("80%")
      .height("100%")
      .hitTestBehavior(HitTestMode.None)
    }.height(100).width('100%').backgroundColor(Color.Black)
  }
}
```

**参考链接**

[颜色渐变](../harmonyos-references/ts-universal-attributes-gradient-color.md)
