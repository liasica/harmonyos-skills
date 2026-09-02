---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-334
title: List控件加载的数据如何判断是否超过一屏
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > List控件加载的数据如何判断是否超过一屏
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:59+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:fd3d545b204e9b58d98d7aa24376d3387f9b47041cfdadfd3c57722713bc5bca
---

1.通过行高计算。

```typescript
@Entry
@Component
struct AllListItemHeight {
  private itemHeightArr = [100, 150, 200, 130, 120, 110.130];
  private listHeight = 700;
  scroller = new ListScroller();

  build() {
    Column() {
      Button('Is it more than one screen')
        .height(50)
        .width('100%')
        .onClick(() => {
          let result = 0;
          for (let i = 0; i < this.itemHeightArr.length; i++) {
            result += this.itemHeightArr[i];
          }
          console.info(result > this.listHeight ? 'More than one screen' : 'Not exceeding one screen');
        })
      List({ scroller: this.scroller }) {
        ForEach(this.itemHeightArr, (_: number, index: number) => {
          ListItem() {
            Text(index.toString())
              .width('100%')
              .textAlign(TextAlign.Center)
          }
          .height(this.itemHeightArr[index])
          .align(Alignment.Center)
        }, (item: number) => JSON.stringify(item))
      }
      .height(this.listHeight)
      .width('100%')
    }
  }
}
```

2.通过getItemRect(index: number): RectResult获取子组件的大小位置，可以获取最后一个ListItem的位置大小信息进行计算。

```ts
@Entry
@Component
struct GetLastItem {
  private itemHeightArr = [100, 150, 200, 130, 120, 110.130];
  private listHeight = 700;
  // Scroll controller for obtaining the position information of list items
  scroller = new ListScroller();

  build() {
    Column() {
      Button('Is it more than one screen')
        .height(50)
        .width('100%')
        .onClick(() => {
          let result = this.scroller.getItemRect(this.itemHeightArr.length - 1);
          let flag = result.y + result.height > this.listHeight;
          console.info(flag ? 'More than one screen' : 'Not exceeding one screen')
        })
      List({ scroller: this.scroller }) {
        ForEach(this.itemHeightArr, (_: number, index: number) => {
          ListItem() {
            Text(index.toString())
              .width('100%')
              .textAlign(TextAlign.Center)
          }
          .height(this.itemHeightArr[index])
          .align(Alignment.Center)
        }, (item: number) => JSON.stringify(item))
      }
      .height(this.listHeight)
      .width('100%')
    }
  }
}
```

3.通过getItemRectInGroup(index: number, indexInGroup: number): RectResult，获取最后一个ListItemGroup中的最后一个ListItem的大小和相对于List的位置进行计算

```screen
@Entry
@Component
struct GetLastGroup {
  private groupItemHeightArr =
    [[30, 50, 60, 40, 90, 80.60],
      [50, 40, 50, 55, 77, 88.44],];
  private listHeight = 700;
  // Scroll controller for obtaining the position information of list items
  scroller = new ListScroller();

  build() {
    Column() {
      Button('Is it more than one screen')
        .height(50)
        .width('100%')
        .onClick(() => {
          let lastGroupIndex = this.groupItemHeightArr.length - 1;
          let lastItemIndex = this.groupItemHeightArr[lastGroupIndex].length - 1;
          let result = this.scroller.getItemRectInGroup(lastGroupIndex, lastItemIndex);
          let flag = result.y + result.height > this.listHeight;
          console.info(flag ? 'More than one screen' : 'Not exceeding one screen')
        })
      List({ scroller: this.scroller }) {
        ForEach(this.groupItemHeightArr, (itemHeight: number[], index: number) => {
          ListItemGroup() {
            ForEach(itemHeight, (height: number) => {
              ListItem() {
                Text(index.toString())
                  .width('100%')
                  .textAlign(TextAlign.Center)
              }
              .height(height)
              .align(Alignment.Center)
            }, (item: number, index: number) => JSON.stringify(item) + index)
          }
        }, (item: number[]) => JSON.stringify(item))
      }
      .height(this.listHeight)
      .width('100%')
    }
  }
}
```
