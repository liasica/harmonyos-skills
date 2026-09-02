---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1470
title: 股票期权场景实现
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 股票期权场景实现
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:24+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:72cd7d5ca0144d5e6fc6773cf18bbd82b97e3eee1f714f4c341fe882f55b0f70
---

## 问题现象

在金融场景下，如何实现T型分布的交互，查看股票期权的涨跌？

## 背景知识

* [Scroll](../harmonyos-references/ts-container-scroll.md)是HarmonyOS提供的一种可滚动的容器组件，当子组件的布局尺寸超过父组件的尺寸时，内容可以滚动。
* [@Builder装饰器](../harmonyos-guides/arkts-builder.md)用于封装可复用的UI结构，通过提取重复的布局代码提高开发效率。该装饰器严格禁止在其内部定义状态变量或使用生命周期函数，必须通过参数传递的方式与调用方完成数据交互。

## 解决方案

通过设置三元表达式控制Scroller来实现不同区域的滚动，设置自定义boolean值，用[scrollTo](../harmonyos-references/ts-container-scroll.md#scrollto)去滑动到指定距离的不同方向，实现均匀的向两侧不同方向滚动。

1. 定义数据类Data，用于存储要展示的数据。

   ```ts
   class Data {
     itemOne: string;
     itemTwo: string;
     itemThree: string;
     itemFour: string;
     itemFive: string;
     itemSix: string;

     constructor(itemOne: string, itemTwo: string, itemThree: string, itemFour: string, itemFive: string,
       itemSix: string) {
       this.itemOne = itemOne;
       this.itemTwo = itemTwo;
       this.itemThree = itemThree;
       this.itemFour = itemFour;
       this.itemFive = itemFive;
       this.itemSix = itemSix;
     }
   }
   ```
2. 定义可复用的UI结构。

   ```ts
   @Builder
   listBuilder(isLeft: boolean) {

     Scroll(isLeft ? this.leftScroller : this.rightScroller) {
       Column() {
         ForEach(this.data, (item: Data) => {
           this.contentBuilder(item, isLeft);
         })
       }
     }
     .scrollable(ScrollDirection.Horizontal)
     .layoutWeight(1)
     .height('auto')
     .scrollBar(BarState.On)
     .onWillScroll((source) => {
       this.scrollSource = source;
     })
     // 当子组件的布局尺寸超过父组件的尺寸时，内容可以滚动
     .onDidScroll(() => {
       if (this.scrollSource !== ScrollSource.SCROLLER && this.scrollSource !== ScrollSource.SCROLLER_ANIMATION) {
         if (isLeft) {
           let leftOffset = this.leftScroller.currentOffset().xOffset;
           this.rightScroller.scrollTo({ xOffset: this.scrollLength - leftOffset, yOffset: 0 });
         } else {
           let rightOffset = this.rightScroller.currentOffset().xOffset;
           this.leftScroller.scrollTo({ xOffset: this.scrollLength - rightOffset, yOffset: 0 });
         }
       }
     })
     .onAppear(() => {
       if (!isLeft) {
         this.rightScroller.scrollEdge(Edge.End, { velocity: 10000000 });
         this.counter = setTimeout(() => {
           clearTimeout(this.counter);
           this.counter = -1;
           this.scrollLength = this.rightScroller.currentOffset().xOffset;
         }, 500);
       }
     })
     .onDisAppear(() => {
       if (this.counter > -1) {
         clearTimeout(this.counter);
         this.counter = -1;
       }
     })
   }
   ```
3. 当子组件的布局尺寸超过父组件的尺寸时，内容可以滚动。

   ```ts
   .onDidScroll(() => {
     if (this.scrollSource !== ScrollSource.SCROLLER && this.scrollSource !== ScrollSource.SCROLLER_ANIMATION) {
       if (isLeft) {
         let leftOffset = this.leftScroller.currentOffset().xOffset;
         this.rightScroller.scrollTo({ xOffset: this.scrollLength - leftOffset, yOffset: 0 });
       } else {
         let rightOffset = this.rightScroller.currentOffset().xOffset;
         this.leftScroller.scrollTo({ xOffset: this.scrollLength - rightOffset, yOffset: 0 });
       }
     }
   })
   ```

完整示例参考如下：

```ts
class Data {
  itemOne: string;
  itemTwo: string;
  itemThree: string;
  itemFour: string;
  itemFive: string;
  itemSix: string;

  constructor(itemOne: string, itemTwo: string, itemThree: string, itemFour: string, itemFive: string,
    itemSix: string) {
    this.itemOne = itemOne;
    this.itemTwo = itemTwo;
    this.itemThree = itemThree;
    this.itemFour = itemFour;
    this.itemFive = itemFive;
    this.itemSix = itemSix;
  }
}
@Entry
@Component
struct ListPage {
  @State data: Data[] = [];
  private scrollLength: number = 0;
  leftScroller: Scroller = new Scroller();
  rightScroller: Scroller = new Scroller();
  scrollSource: ScrollSource = ScrollSource.DRAG;
  private counter: number = -1;
  flag: boolean = true;

  aboutToAppear(): void {
    for (let i = 0; i < 100; i++) {
      this.data.push(new Data(`item1`, `item2`, `item3`, `item4`, `item5`, `item6`));
    }
  }

  // 定义可复用的UI结构
  @Builder
  listBuilder(isLeft: boolean) {

    Scroll(isLeft ? this.leftScroller : this.rightScroller) {
      Column() {
        ForEach(this.data, (item: Data) => {
          this.contentBuilder(item, isLeft);
        })
      }
    }
    .scrollable(ScrollDirection.Horizontal)
    .layoutWeight(1)
    .height('auto')
    .scrollBar(BarState.On)
    .onWillScroll((source) => {
      this.scrollSource = source;
    })
    // 当子组件的布局尺寸超过父组件的尺寸时，内容可以滚动
    .onDidScroll(() => {
      if (this.scrollSource !== ScrollSource.SCROLLER && this.scrollSource !== ScrollSource.SCROLLER_ANIMATION) {
        if (isLeft) {
          let leftOffset = this.leftScroller.currentOffset().xOffset;
          this.rightScroller.scrollTo({ xOffset: this.scrollLength - leftOffset, yOffset: 0 });
        } else {
          let rightOffset = this.rightScroller.currentOffset().xOffset;
          this.leftScroller.scrollTo({ xOffset: this.scrollLength - rightOffset, yOffset: 0 });
        }
      }
    })
    .onAppear(() => {
      if (!isLeft) {
        this.rightScroller.scrollEdge(Edge.End, { velocity: 10000000 });
        this.counter = setTimeout(() => {
          clearTimeout(this.counter);
          this.counter = -1;
          this.scrollLength = this.rightScroller.currentOffset().xOffset;
        }, 500);
      }
    })
    .onDisAppear(() => {
      if (this.counter > -1) {
        clearTimeout(this.counter);
        this.counter = -1;
      }
    })
  }

  @Builder
  contentBuilder(item: Data, isLeft: boolean) {
    Row() {
      ForEach(isLeft ? Reflect.ownKeys(item).reverse() : Reflect.ownKeys(item), (name: string) => {
        Text(Reflect.get(item, name))
          .width(80)
          .height(20)
          .textAlign(TextAlign.Center)
          .borderWidth(1)
      })
    }
  }

  build() {
    Column() {
      Scroll() {
        if (this.flag) {
          Row() {
            this.listBuilder(true);
            Column() {
              ForEach(this.data, (item: Data, index) => {
                Text(`第${index}项`)
                  .width(80)
                  .height(20)
                  .textAlign(TextAlign.Center)
                  .fontColor(Color.Orange)
                  .borderWidth(1)
              })
            }
            .width(80)

            this.listBuilder(false);
          }
          .width('100%')
        } else {
        }
      }
      .width('100%')
      .layoutWeight(1)
    }
  }
}
```

## 总结

通过设置三元表达式控制Scroller来实现不同区域的滚动，设置自定义boolean值，用currentOffset方法的xOffset获取不同方向的滚动距离，实现均匀地向两侧不同方向滚动的效果。
