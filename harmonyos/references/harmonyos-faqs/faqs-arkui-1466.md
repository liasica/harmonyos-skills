---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1466
title: Swiper轮播组件单页如何显示非整数条的数据
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > Swiper轮播组件单页如何显示非整数条的数据
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:10+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:6f2d87c17fe9c8af293b9cd54eca5dbf6059f1d3deeaf3173b7c6f042602978b
---

## 问题现象

如何实现如下效果：

1. 显示轮播组件内的一条数据的完整页面，以及下一条数据约30%的前部分页面。
2. 最后一页显示最后一条数据的完整页面，以及上一条数据约30%的后部分页面。

## 背景知识

* [Swiper](../harmonyos-references/ts-container-swiper.md)：滑块视图容器，提供子组件滑动轮播显示的能力。
* [nextMargin](../harmonyos-references/ts-container-swiper.md#nextmargin10)：设置后边距，用于露出后一项的一小部分。
* [prevMargin](../harmonyos-references/ts-container-swiper.md#prevmargin10)：设置前边距，用于露出前一项的一小部分。

需要注意的是，Swiper不支持上下条按百分比显示的效果，能否支持都是要基于布局流程的，Swiper要根据子组件布局的结果来确定尺寸，目前对前后边距的使用早于自身尺寸确定，用百分比转换是不合理的。

## 解决方案

使用nextMargin设置固定的后边距，并且将nextMargin属性的ignoreBlank参数设置为true即可实现需求效果。

示例代码如下：

```ts
@Entry
@Component
struct SwiperExample {
  private swiperController: SwiperController = new SwiperController();

  build() {
    Column({ space: 5 }) {
      Swiper(this.swiperController) {
        Text('0')
          .width('100%')
          .height(250)
          .backgroundColor('#f1f3f5')
          .textAlign(TextAlign.Center)
          .fontSize(30)
          .borderRadius('8px')
          .margin('16px');
        Text('1')
          .width('100%')
          .height(250)
          .backgroundColor('#f1f3f5')
          .textAlign(TextAlign.Center)
          .fontSize(30)
          .borderRadius('8px')
          .margin('16px');
        Text('2')
          .width('100%')
          .height(250)
          .backgroundColor('#f1f3f5')
          .textAlign(TextAlign.Center)
          .fontSize(30)
          .borderRadius('8px')
          .margin('16px');
        Text('3')
          .width('100%')
          .height(250)
          .backgroundColor('#f1f3f5')
          .textAlign(TextAlign.Center)
          .fontSize(30)
          .borderRadius('8px')
          .margin('16px');
      }
      .indicator(true)
      .displayMode(SwiperDisplayMode.STRETCH)
      .nextMargin('90vp', true)
      .autoPlay(true)
      .loop(false);
    };
  }
}
```
