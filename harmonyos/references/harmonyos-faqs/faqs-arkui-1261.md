---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1261
title: Swiper如何显示指定index页面
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > Swiper如何显示指定index页面
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:08+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:397f919e69fc5180758d9e694aea050c69ece11c46ad47a4804756741a998f58
---

## 问题现象

使用Swiper组件，期望初始化显示时即加载最后一个位置的内容，应该如何实现？

## 背景知识

* Swiper组件是ArkUI中常用的轮播图组件，对于Swiper组件，提供了index属性，可以设置Swiper显示时的默认索引值，如果未设置，默认显示第0个位置的内容。
* index的属性介绍可参考：[Swiper的index属性](../harmonyos-references/ts-container-swiper.md#index)，该属性支持$$双向绑定变量。

## 解决方案

通过$$将index属性与@State装饰的变量双向绑定。

* 手指滑动Swiper切换页面，index变化会同步至@State变量，可实现获取当前显示页面下标的效果。
* 通过修改@State变量可以改变Swiper显示的页面，可实现显示指定index页面的效果。

示例代码如下：将@State变量showIndex与Swiper的index双向绑定。

```ts
@Entry
@Component
struct SwiperIndexDemo {
  private swiperNumber: number[] = [0, 1, 2, 3, 4, 5, 6, 7];
  @State showIndex: number = this.swiperNumber.length - 1;
  private swiperController: SwiperController = new SwiperController();

  build() {
    Column({ space: 16 }) {
      Swiper(this.swiperController) {
        ForEach(this.swiperNumber, (item: number) => {
          Text(item.toString())
            .width(250)
            .height(250)
            .backgroundColor(Color.Gray)
            .textAlign(TextAlign.Center)
            .fontSize(30);
        });
      }.index($$this.showIndex); // 与showIndex变量双向绑定
      Text(`当前showIndex: ${this.showIndex}`);
      Button(`showIndex+1`)
        .onClick(() => {
          this.showIndex = (this.showIndex + 1) % this.swiperNumber.length;
        });
    }.width('100%').margin({ top: 5 });
  }
}
```

效果如下：Swiper初始化显示最后一页内容，滑动Swiper会改变showIndex，改变showIndex也能滑动Swiper。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6c/v3/h4yahob2QX6dSTJFu3a3hg/zh-cn_image_0000002628756008.png "点击放大")

## 常见FAQ

Q：Swiper的index方法显示指定位置无滑动动画，期望和手动滑动动画一致。

A：可以使用SwiperController的[changeIndex](../harmonyos-references/ts-container-swiper.md#changeindex15)方法来指定显示位置，通过入参可以指定切换的动画效果。

Q：ArcSwiper没有changeIndex方法，如何跳转到指定页面？

A：可以通过设置[index](../harmonyos-references/ts-container-arcswiper.md#index)属性跳转到指定页面。
