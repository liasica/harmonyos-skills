---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-136
title: Grid组件的scrollBar是否支持自定义
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > Grid组件的scrollBar是否支持自定义
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:58+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:32e2a1d8e6e70bc31a5a4ae1f95c99b8811d7fef4352f00cefdb8aaa80ecbe44
---

Grid组件的默认滑动条scrollBar不支持自定义样式。

可以通过隐藏默认滑动条并绑定ScrollBar组件来满足该场景。参考代码如下：

```ts
@Entry
@Component
struct Index {
  private scroller: Scroller = new Scroller()
  private arr: number[] = [];

  build() {
    Column() {
      Stack({ alignContent: Alignment.End }) {
        Grid(this.scroller) {
          ForEach(this.arr, (item: number) => {
            GridItem() {
              Text(item.toString())
                .width(100)
                .height(50)
                .backgroundColor('#3366CC')
                .borderRadius(15)
                .fontSize(16)
                .textAlign(TextAlign.Center)
            }
          })
        }
        .width('100%')
        .columnsTemplate("1fr 1fr 1fr")
        .columnsGap(5)
        .rowsGap(5)
        // Hide native scrollBar
        .scrollBar(BarState.Off)

        ScrollBar({ scroller: this.scroller, direction: ScrollBarDirection.Vertical, state: BarState.Auto }) {
          Text("A")
            .width(20)
            .height(50)
            .borderRadius(10)
            .backgroundColor('#C0C0C0')
        }
        .width(20)
        .backgroundColor('#ededed')
      }
    }
  }

  aboutToAppear() {
    for (let i = 0; i < 100; i++) {
      this.arr.push(i)
    }
  }
}
```

**参考链接**

[Grid](../harmonyos-references/ts-container-grid.md)，[ScrollBar](../harmonyos-references/ts-basic-components-scrollbar.md)
