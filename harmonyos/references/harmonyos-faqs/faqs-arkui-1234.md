---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1234
title: 监听Scroll滑动距离实现相关效果
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 监听Scroll滑动距离实现相关效果
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:07+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:1cfa20dea58a7f8e1da68672b5b91f038fd9577d85e46af2b444719fa35c2910
---

## 问题现象

如何在监听到Scroll向上滑动的距离后，根据滑动的距离动态改变其内部特定容器的背景颜色？

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/36/v3/mgMWFf1lTRq2P1C0M8W01w/zh-cn_image_0000002628594048.gif "点击放大")

## 背景知识

* [currentOffset](../harmonyos-references/ts-container-scroll.md#currentoffset)方法用于获取当前的滚动偏移量。滑动偏移量对象为xOffset、yOffset。
* [onScrollFrameBegin](../harmonyos-references/ts-container-scroll.md#onscrollframebegin9)该接口回调时，事件参数传入即将发生的滚动量，事件处理函数中可根据应用场景计算实际需要的滚动量并作为事件处理函数的返回值返回，Scroll将按照返回值的实际滚动量进行滚动。

## 解决方案

可以用this.scroller.currentOffset().yOffset作为滑动距离的标准，用onScrollFrameBegin回调进行监听，对滑动距离判断并进行色值变化。

```ts
@Entry
@Component
struct ScrollExample {
  scroller: Scroller = new Scroller();
  private arr: number[] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];
  @State bgColor: string = '#FFF';

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
              .backgroundColor(this.bgColor);
          }, (item: string) => item);
        }.width('100%');
      }
      .scrollable(ScrollDirection.Vertical) // 滚动方向纵向
      .scrollBar(BarState.On) // 滚动条常驻显示
      .scrollBarColor(Color.Gray) // 滚动条颜色
      .scrollBarWidth(10) // 滚动条宽度
      .friction(0.6)
      .edgeEffect(EdgeEffect.Spring)
      .onScrollFrameBegin((offset: number) => {
        if (this.scroller.currentOffset().yOffset > 0) {
          this.bgColor = '#FFF';
        }
        if (this.scroller.currentOffset().yOffset > 300) {
          this.bgColor = '#999';
        }
        if (this.scroller.currentOffset().yOffset > 600) {
          this.bgColor = '#333';
        }
        return { offsetRemain: offset };
      });
    }.width('100%').height('100%').backgroundColor(0xDCDCDC);
  }
}
```
