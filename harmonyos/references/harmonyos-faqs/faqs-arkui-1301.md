---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1301
title: 滑动组件的偏移量如何获取
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 滑动组件的偏移量如何获取
category: harmonyos-faqs
scraped_at: 2026-09-02T15:03:46+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:f40b152f52a2168e6a09ea3ef21ded83c72fb0edc2d2ee2627c67d0467edfe42
---

## 问题现象

如何监听指定的滑动组件的滑动行为并获取偏移量？

## 背景知识

[onDidScroll](../harmonyos-references/ts-container-scrollable-common.md#ondidscroll12)是滑动组件的通用接口，滑动时触发，回调信息[OnScrollCallback](../harmonyos-references/ts-container-scrollable-common.md#onscrollcallback12)包含当前帧滑动的偏移量和当前滑动状态。其中偏移量[currentOffset](../harmonyos-references/ts-container-scroll.md#currentoffset)需要依靠滑动控制器获取。

## 解决方案

以List嵌套WaterFlow为例，观察如何通过onDidScroll获取滑动组件的偏移量。

```screen
@Entry
@Component
struct ListComponentPage {
  private arr: number[] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];
  private arr2: number[] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 14, 14, 14, 14];
  private scroller: ListScroller = new ListScroller();
  private scroller2: Scroller = new Scroller();

  build() {
    Column() {
      List({ space: 10, scroller: this.scroller }) {
        ForEach(this.arr, (item: number) => {
          ListItem() {
            Column() {
              Text(`ListItem${item.toString()}`)
                .backgroundColor('#5291FF')
                .borderRadius(16)
                .height(30)
                .width('90%')
                .textAlign(TextAlign.Center);
            }.width('100%').justifyContent(FlexAlign.Center);
          };
        });
        ListItem() {
          WaterFlow({ scroller: this.scroller2 }) {
            ForEach(this.arr2, (item: number) => {
              FlowItem() {
                Column() {
                  Text(`FlowItem${item.toString()}`)
                    .backgroundColor('#61CFBE')
                    .borderRadius(16)
                    .height(30)
                    .width('90%')
                    .textAlign(TextAlign.Center);
                  Blank().height(10);
                }.width('100%').justifyContent(FlexAlign.Center);
              };
            });
          }
          // 示例高度，目的是设置一个小于WaterFlow总高度的值，使WaterFlow具备滑动行为
          .height(200)
          .onDidScroll((scrollOffset: number, scrollState: ScrollState) => {
            console.info(`当前WaterFlow帧滑动偏移量：${scrollOffset}`);
            console.info(`当前WaterFlow滑动状态：${scrollState}`);
            console.info(`当前WaterFlow的滑动偏移量：xOffset：${this.scroller.currentOffset().xOffset}  yOffset：
            ${this.scroller2.currentOffset().yOffset}`);

          });
        };

        ForEach(this.arr, (item: number) => {
          ListItem() {
            Column() {
              Text(`ListItem${item.toString()}`)
                .backgroundColor('#5291FF')
                .borderRadius(16)
                .height(30)
                .width('90%')
                .textAlign(TextAlign.Center);
            }.width('100%').justifyContent(FlexAlign.Center);
          };
        });
      }
      // 滑动时触发
      .onDidScroll((scrollOffset: number, scrollState: ScrollState) => {
        console.info(`当前List帧滑动偏移量：${scrollOffset}`);
        console.info(`当前List滑动状态：${scrollState}`);
        console.info(`当前List的滑动偏移量：xOffset：${this.scroller.currentOffset().xOffset}  yOffset：
        ${this.scroller.currentOffset().yOffset}`);
      });
    }
    .height('100%');
  }
}
```

**说明** 

如果内层的WaterFlow不再设置高度，只需滑动外层List便能看到WaterFlow全部项时，WaterFlow的onDidScroll回调不会触发，即在此场景下无法监听内层滑动组件的滑动行为，如果只需监听内层的滑动组件是否在滑动，可以给内层的滑动组件设置.edgeEffect(EdgeEffect.None, { alwaysEnabled: true })即可触发其对应的onDidScroll回调。

但此时scrollOffset，scrollState，currentOffset的返回值均为0，这是因为滑动组件虽然添加了滑动逻辑，但并没有产生真正的滑动行为。

## 总结

利用onDidScroll获取偏移量，可以监听指定的滑动组件是否在滑动，滑动方向是哪边。由于onDidScroll是给具体的滑动组件设置的属性，并依靠Scroller控制器获取返回值，同时触发时机是开始滑动的第一帧。因此该滑动组件与其他滑动组件平级或者嵌套时，都能精确地进行监听。

## 常见FAQ

Q：onDidScroll中会回调滑动状态[ScrollState](../harmonyos-references/ts-container-list.md#scrollstate枚举说明)，能否根据ScrollState.Idle来判断滚动是否完全停止。

A：不推荐使用onDidScroll的ScrollState去判断滚动停止状态，推荐使用[onScrollStop](../harmonyos-references/ts-container-list.md#onscrollstop)进行判断。
