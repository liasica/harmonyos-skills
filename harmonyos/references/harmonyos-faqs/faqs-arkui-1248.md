---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1248
title: 页面上下滑动时，页面上的图片会闪跳
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 页面上下滑动时，页面上的图片会闪跳
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:15+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:1040ba0592e003c9bf98af68f9f3713c05b3d9af54d0821056ebd0de582356af
---

## 问题现象

图片在上下或左右滑动时，出现图片放大或缩小，又瞬间恢复原本大小的现象，视觉上内容闪烁。

## 背景知识

* [Image](../harmonyos-references/ts-basic-components-image.md)为图片组件，常用于在应用中显示图片。Image支持加载PixelMap、ResourceStr和DrawableDescriptor类型的数据源，支持png、jpg、jpeg、bmp、svg、webp、gif和heif类型的图片格式。
* [Scroll](../harmonyos-references/ts-container-scroll.md)是可滚动的容器组件，当子组件的布局尺寸超过父组件的尺寸时，内容可以滚动。
* [Swiper](../harmonyos-references/ts-container-swiper.md)是滑块视图容器，提供子组件滑动轮播显示的能力。

## 问题定位

1. 上下滑动页面时，排查日志发现，每次滚动高度都发生了改变。

   ```screen
   PDF_RENDER --> method=updateTex
   PDF_RENDER --> updateText: width=1271 height=891, srcX=0, setY=0
   PDF_RENDER --> method=updateTex
   PDF_RENDER --> updateText: width=1271,height=305,srcX=0,setY=1492
   PDF_RENDER --> method=updateTex
   PDF_RENDER --> updateText: width=1271,height=1505,srcX=0,setY=0
   ```
2. 使用DevEco Testing查看页面布局，是由多张图片组合而成的界面，结合日志可以发现每次往下滑动时，缩小上面图片的高度，放大下面图片的高度，否则反之。

## 分析结论

每次滑动图片时，高度/宽度会被刷新，导致出现闪烁现象。

## 修改建议

* 方案一：将图片整合为一张长图，使用Scroll使其可上下滚动。
* 方案二：使用Swiper轮播图左右滑动图片，而非上下滑动放大缩小图片。

  ```screen
  @Entry
  @Component
  struct NestedScroll {
    private swiperController: SwiperController = new SwiperController();

    build() {
      Column() {
        // 使用Scroll组件使长图可以滚动
        Scroll() {
          Column() {
            // 加载一张长图，请提供真实的长图
            Image($r("app.media.example"))
          }
        }.width('100%').height('100%').backgroundColor(0xDCDCDC).padding(20)

        Column({ space: 5 }) {
          // 可左右滑动的轮播图，请提供真实的图片
          Swiper(this.swiperController) {
            Image($r("app.media.example"))
            Image($r("app.media.example"))
            Image($r("app.media.example"))
            Image($r("app.media.example"))
          }
          .index(1)
          .autoPlay(true)
          .interval(4000)
          .loop(true)
          .duration(1000)
          .itemSpace(0)

        }.width('100%')
        .height('100%')
        .margin({ top: 5 })
      }
    }
  }
  ```
