---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-211
title: Grid如何实现拖拽功能
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > Grid如何实现拖拽功能
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:59+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:ec3a6d42b92a1e7384be169ab335ae8d8a34b577b1fec9b5af974355fc1ed4b0
---

1. 通过editMode(true)属性设置Grid进入编辑模式，该模式下可拖拽内部GridItem。
2. 在onItemDragStart回调中设置拖拽过程中显示的图片。
3. 在onItemDrop中获取拖拽起始位置和拖拽插入位置，并在onItemDrop中完成交换数组位置动作。

可以参考如下示例代码：

```ts
@Component
export struct GridExample {
  @State numbers: string[] = [];
  scroller: Scroller = new Scroller();

  // Drag and drop process style
  @Builder
  pixelMapBuilder(text: string) {
    Column() {
      Text(text)
        .fontSize(16)
        .backgroundColor(0xF9CF93)
        .width(80)
        .height(80)
        .textAlign(TextAlign.Center)
    }
  }

  aboutToAppear() {
    for (let i = 1; i <= 15; i++) {
      this.numbers.push(i + '');
    }
  }

  // Swap array positions
  changeIndex(index1: number, index2: number) {
    let temp: string;
    temp = this.numbers[index1];
    this.numbers[index1] = this.numbers[index2];
    this.numbers[index2] = temp;
  }

  build() {
    Column({ space: 5 }) {
      Grid(this.scroller) {
        ForEach(this.numbers, (day: string) => {
          GridItem() {
            this.pixelMapBuilder(day)
          }
        })
      }
      .columnsTemplate('1fr 1fr 1fr')
      .columnsGap(10)
      .rowsGap(10)
      .width('90%')
      .backgroundColor(0xFAEEE0)
      .height(500)
      .editMode(true) // Set whether the Grid enters editing mode. When entering editing mode, you can drag and drop the GridItem inside the Grid component
      .onItemDragStart((event: ItemDragInfo, itemIndex: number) => { // 第一次拖拽此事件绑定的组件时，触发回调。
        // Set the image displayed during the drag and drop process
        return this.pixelMapBuilder(this.numbers[itemIndex]);
      })
      .onItemDrop((event: ItemDragInfo, itemIndex: number, insertIndex: number, isSuccess: boolean) => {
        // The component bound to this event can be used as a drag and drop release target. When the drag behavior stops within the scope of this component, a callback is triggered.
        // When isSuccess=false, it indicates that the drop is located outside the grid; When insertIndex>length, it indicates that an event of adding new elements has occurred
        if (!isSuccess || insertIndex >= this.numbers.length) {
          return;
        }
        this.changeIndex(itemIndex, insertIndex);
      })
    }
    .width('100%')
    .margin({ top: 5 })
  }
}
```

**参考链接**

[Grid](../harmonyos-references/ts-container-grid.md)
