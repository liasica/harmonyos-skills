---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-512
title: 页面滚动到某个距离后禁止继续向下滚动
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 页面滚动到某个距离后禁止继续向下滚动
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:00+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:cb08daf0acaaabbf1c41d6378c83a09d49bf7470b5230c19ea21ac9b27305cac
---

## 问题现象

如何实现当页面滚动到某一个距离时，不能再继续向下滚动。

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e2/v3/s0z5MqTZSpe76Nu3issGjg/zh-cn_image_0000002628548520.png "点击放大")

## 背景知识

* [Scroll](../harmonyos-references/ts-container-scroll.md)是一种可滚动的容器组件，当子组件的布局尺寸超过父组件的尺寸时，内容可以滚动。
* [onDidScroll](../harmonyos-references/ts-container-scroll.md#ondidscroll12)方法在Scroll滚动时触发，可用于在滑动过程中获取Scroll组件的偏移量yOffset。
* [scrollTo](../harmonyos-references/ts-container-scroll.md#scrollto)方法可用于让Scroll组件滑动到指定位置。

## 解决方案

1. 为Scroll组件添加onDidScroll方法，该方法在页面滚动过程中实时通过currentOffset获取Scroll的偏移量yOffset。

   ```ts
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
           .margin({ top: 10 });
       }, (item: string) => item);
     }
     .width('100%');
   }
   .scrollable(ScrollDirection.Vertical)
   // Scroll滚动时触发该回调
   .onDidScroll(() => {
     this.yOffset = this.scroller.currentOffset().yOffset;
     if (this.yOffset >= 1000) {
       this.scroller.scrollTo({ xOffset: 0, yOffset: 1000, animation: true });
     }
   })
   ```
2. 当yOffset大于等于1000vp时，使用scrollTo方法使页面滑动到指定位置，即可实现页面无法继续向下滑动的效果。

   ```ts
   if (this.yOffset >= 1000) {
     this.scroller.scrollTo({ xOffset: 0, yOffset: 1000, animation: true });
   }
   ```

完整代码如下所示：

```ts
@Entry
@Component
struct ScrollDemo {
  @State yOffset: number = 0;
  scroller: Scroller = new Scroller();
  private arr: number[] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20];

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
              .margin({ top: 10 });
          }, (item: string) => item);
        }
        .width('100%');
      }
      .scrollable(ScrollDirection.Vertical)
      // Scroll滚动时触发该回调
      .onDidScroll(() => {
        this.yOffset = this.scroller.currentOffset().yOffset;
        if (this.yOffset >= 1000) {
          this.scroller.scrollTo({ xOffset: 0, yOffset: 1000, animation: true });
        }
      })
      .scrollBar(BarState.On)
      .scrollBarColor(Color.Gray)
      .scrollBarWidth(2)
      .friction(0.6)
      .edgeEffect(this.yOffset <= 0 ? EdgeEffect.Spring : EdgeEffect.None);
    }
    .width('100%')
    .height('100%')
    .backgroundColor(0xDCDCDC);
  }
}
```
