---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-tablet-19
title: 平板竖屏场景，底部组件位置错乱
breadcrumb: FAQ > 多设备场景 > 平板 > 常见问题 > 平板竖屏场景，底部组件位置错乱
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:48+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:7d7d3eac8b05b1dbbf32cb3c3bf27c539f53814afeccffa330f001d0a2e3203a
---

## 问题现象

平板竖屏场景，切换到异常页面时底部组件位置突变，且覆盖了其他组件。

## 背景知识

* [Stack](../harmonyos-references/ts-container-stack.md)：堆叠容器，子组件按照顺序依次入栈，后一个子组件覆盖前一个子组件。
* [position](../harmonyos-references/ts-universal-attributes-location.md#position)：绝对定位，确定子组件相对父组件内容区的位置。当父容器为Row/Column/Flex时，设置position的子组件不占位。

## 问题定位

1. 若使用position给组件设置了绝对定位，在平板为竖屏时由于屏幕位置改变导致定位错误出现组件位置错乱的现象。检查异常页面是否使用了绝对定位。

   ```ts
   Row() {
     Text('2 position(30, 10)')
       .size({ width: '60%', height: '30' })
       .backgroundColor(0xbbb2cb)
       .border({ width: 1 })
       .fontSize(16)
       .align(Alignment.Start)
       .position({ x: 30, y: 10 })
     Text('4 position(50%, 70%)')
       .size({ width: '50%', height: '50' })
       .backgroundColor(0xbbb2cb)
       .border({ width: 1 })
       .fontSize(16)
       .position({ x: '50%', y: '70%' })
   }
   .width('90%')
   .height(100)
   .border({ width: 1, style: BorderStyle.Dashed })
   ```
2. 若使用Stack布局会导致组件覆盖。Stack层叠布局会优先显示最上层的组件，检查异常页面是否是Stack布局。

   ```ts
   Stack({ alignContent: Alignment.TopStart }) {
     Scroll() {
       Column() {
         // ...
       }
     }
     .zIndex(0)

     Button('结算').onClick((event: ClickEvent) => {
       // ...
     })
     .zIndex(1)
   }
   .margin({ top: 25 })
   .border({ width: 1, style: BorderStyle.Dashed })
   ```

## 分析结论

Stack布局导致组件覆盖，position绝对定位导致组件位置错乱。

## 修改建议

不同屏幕尺寸下绝对定位的适配性差，建议优先使用[Flex](../harmonyos-references/ts-universal-attributes-flex-layout.md)等响应式布局替代。以购物页面为例，简单的购物页面一般为Scroll包含的商品列表和底部结算按钮，可以将这两个组件放在同一图层，并给Scroll设置一个百分比高度，这样按钮组件默认会在Scroll底部显示，避免使用绝对定位。

```ts
@Entry
@Component
struct ShoppingPage {
  numArr: number[] = [];

  aboutToAppear(): void {
    for (let i = 0; i < 100; i++) {
      this.numArr.push(i);
    }
  }

  build() {
    Column() {
      Scroll() {
        Column({ space: 5 }) {
          ForEach(this.numArr, (item: number) => {
            Text(item.toString())
              .fontColor(Color.Black)
              .fontSize(20)
              .width('95%')
              .height('20%')
              .textAlign(TextAlign.Center)
              .backgroundColor('#f1f3f5');
          });
        }
        .width('100%')
        .justifyContent(FlexAlign.Center);
      }
      .expandSafeArea([SafeAreaType.SYSTEM])
      .height('90%')
      .scrollBar(BarState.Off)
      .scrollable(ScrollDirection.Vertical);

      Row({ space: 10 }) {
        Row({ space: 10 }) {
          Column() {

          }
          .width('30%')
          .height('100%')
          .backgroundColor('#f1f3f5');

          Column({ space: 5 }) {
            Row() {

            }
            .width('60%')
            .height('40%')
            .backgroundColor('#f1f3f5');

            Row() {

            }
            .width('60%')
            .height('40%')
            .backgroundColor('#f1f3f5');
          }
          .justifyContent(FlexAlign.Center);
        }
        .layoutWeight(1);

        Text('结算')
          .backgroundColor('#0A59F7')
          .fontColor(Color.White)
          .textAlign(TextAlign.Center)
          .width(100)
          .height(50)
          .borderRadius(25)
          .margin(10)
          .onClick(() => {
            // ...
          });
      }
      .width('95%')
      .layoutWeight(1)
      .margin({ top: 5 })
      .alignItems(VerticalAlign.Center)
      .justifyContent(FlexAlign.SpaceBetween);
    };
  }
}
```
