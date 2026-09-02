---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1512
title: Swiper如何实现惯性滚动效果
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > Swiper如何实现惯性滚动效果
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:11+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:32cf0570387ee6fbb627baabdd795040aec9d899a3d987ea5037df0e375d7d1a
---

## 问题现象

Swiper组件在滑动时只能一次滚动一页，在需要一次滑动多个页面的场景下效率较低，Swiper组件如何实现惯性滚动效果，提高滑动效率？

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/18/v3/FirrMhCdSSKQurRC15Xcaw/zh-cn_image_0000002658845805.png "点击放大")

## 背景知识

* [parallelGesture](../harmonyos-guides/arkts-gesture-events-binding.md#parallelgesture并行手势绑定方法)：parallelGesture是并行的手势绑定方法，在父子组件上绑定可以同时响应的相同手势。
* [changeIndex](../harmonyos-references/ts-container-swiper.md#changeindex15)：Swiper翻页至指定页面。

## 解决方案

方案逻辑：向后翻动几页；如果抬手时速度小于设置的值，则保持原来每次翻一页的效果。通过以上逻辑实现快速滑动Swiper时，可以惯性向后翻几页。

```ts
.parallelGesture( // 同步手势
  PanGesture()
    .onActionEnd(e => {
      // 手势结束，获取当前的速度
      let velocityX = e.velocityX || 0;
      if (velocityX > 2000) {
        this.swiperController.changeIndex(this.currentIndex - 2, SwiperAnimationMode.FAST_ANIMATION);
      } else if (velocityX < -2000) {
        this.swiperController.changeIndex(this.currentIndex + 2, SwiperAnimationMode.FAST_ANIMATION);
      }
    })
)
```

完整示例参考如下：

```ts
@Entry
@Component
struct Swiper1 {
  private swiperController: SwiperController = new SwiperController();
  private data: string[] = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11'];
  private currentIndex: number = 0;

  build() {
    Column({ space: 5 }) {
      Swiper(this.swiperController) {
        ForEach(this.data, (item: string) => {
          Text(item.toString())
            .width('90%')
            .height(160)
            .backgroundColor(0xf1f3f5)
            .textAlign(TextAlign.Center)
            .fontSize(30)
            .borderRadius(12)
        }, (index: number) => index.toString())
      }
      .cachedCount(2)
      .index($$this.currentIndex)
      .loop(false)
      .indicator(false)
      .duration(500)
      .itemSpace(5)
      .curve(Curve.Friction)
      .prevMargin(35, true)
      .nextMargin(35, true)
      .parallelGesture( // 同步手势
        PanGesture()
          .onActionEnd(e => {
            // 手势结束，获取当前的速度
            let velocityX = e.velocityX || 0;
            if (velocityX > 2000) {
              this.swiperController.changeIndex(this.currentIndex - 2, SwiperAnimationMode.FAST_ANIMATION);
            } else if (velocityX < -2000) {
              this.swiperController.changeIndex(this.currentIndex + 2, SwiperAnimationMode.FAST_ANIMATION);
            }
          })
      )
    }.width('100%')
    .margin({ top: 5 })
  }
}
```

## 常见FAQ

Q：如何实现自定义组件滑动时的惯性效果？

A：与解决方案同理，使用PanGesture手势即可实现惯性滑动效果，具体可以参考示例[如何通过PanGesture手势或者SwipeGesture手势实现自定义组件的惯性滚动效果](faqs-arkui-33.md)。
