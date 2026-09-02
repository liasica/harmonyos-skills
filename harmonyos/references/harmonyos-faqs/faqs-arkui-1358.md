---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1358
title: 如何保持Swiper中图片居中效果
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 如何保持Swiper中图片居中效果
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:21+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:795726124d255938bf603ed9e060629f4104986ae5544ccf7c6fac6d05303ece
---

## 问题现象

Swiper加载高度不同的图片，在滑动图片时，会出现图片下移的情况。

问题代码示例参考如下：

```ts
@Entry
@Component
struct Page1 {
  build() {
    Column() {
      Swiper() {
        Image($r('app.media.backgroundImage')) // 图片请自行选择尺寸不同的两张图片
          .width('100%')
          .height('100%')
          .interpolation(ImageInterpolation.High)
          .fitOriginalSize(true)
          .objectFit(ImageFit.Cover)
          .draggable(false)
          .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.TOP, SafeAreaEdge.BOTTOM]); // 沉浸式
        Image($r('app.media.backgroundImage'))
          .width('100%')
          .interpolation(ImageInterpolation.High)
          .fitOriginalSize(true)
          .objectFit(ImageFit.Cover)
          .draggable(false);
      }
      .indicator(false) // 去掉点的显示
      .clip(true)
      .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.TOP, SafeAreaEdge.BOTTOM]);
    }
    .justifyContent(FlexAlign.Center)
    .width('100%')
    .height('100%')
    .backgroundColor(Color.White);
  }
}
```

问题效果预览：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5f/v3/7JisDQAiRduN8NNVtoqXEg/zh-cn_image_0000002658961207.png "点击放大")

## 效果预览

可以看到图片一直处于居中，不会出现图片下移的情况。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1c/v3/CbKQkns2Tq6_zNPKDpEjHw/zh-cn_image_0000002658841259.gif "点击放大")

## 背景知识

要实现[Swiper](../harmonyos-references/ts-container-swiper.md)组件中的居中效果，首先确保Swiper组件的宽度和高度设置为适应屏幕或父容器。例如，可以设置width:'100%'和height:'100%'来填满父容器。然后使用父组件使用[justifyContent](../harmonyos-references/ts-container-column.md#justifycontent8)和[alignItems](../harmonyos-references/ts-container-column.md#alignitems)样式属性来设置在垂直和水平方向上的对齐格式，此时设置为FlexAlign.Center居中模式。

## 解决方案

上述问题代码中将整个Swiper放到Column中并居中，这样在切换尺寸的不同图片时会产生渲染问题，每次滑动Swiper组件都会重新渲染Image并居中，因此Image组件不适合在此直接多次使用，组件规格如此。

要想避免这个问题，可以通过将每一个Image用一个Column包裹，并用justifyContent在垂直方向居中来使图片一直处于居中。

```ts
@Entry
@Component
struct Page2 {
  build() {
    Column() {
      Swiper() {
        Column() {
          Image($r('app.media.backgroundImage')) // 图片请自行选择尺寸不同的两张图片
            .width('100%')
            .height('100%')
            .interpolation(ImageInterpolation.High)
            .fitOriginalSize(true)
            .objectFit(ImageFit.Cover)
            .draggable(false)
            .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.TOP, SafeAreaEdge.BOTTOM]); // 沉浸式
        }
        .justifyContent(FlexAlign.Center)
        .width('100%')
        .height('100%')
        .backgroundColor(Color.White);

        Column() {
          Image($r('app.media.backgroundImage'))
            .width('100%')
            .interpolation(ImageInterpolation.High)
            .fitOriginalSize(true)
            .objectFit(ImageFit.Cover)
            .draggable(false);
        }
        .justifyContent(FlexAlign.Center)
        .width('100%')
        .height('100%')
        .backgroundColor(Color.White);
      }
      .indicator(false) // 去掉点的显示
      .clip(true)
      .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.TOP, SafeAreaEdge.BOTTOM]);
    }
    .width('100%')
    .height('100%');
  }
}
```
