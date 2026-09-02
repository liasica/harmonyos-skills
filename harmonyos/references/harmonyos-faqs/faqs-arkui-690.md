---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-690
title: Swiper组件禁止手动滑动
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > Swiper组件禁止手动滑动
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:02+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:8396a2b86ac636dae59bb50406e262f6af0cbcb2ae3864b46134f08863fe5018
---

## 问题现象

如何能禁止如下图Swiper组件的手动滑动？

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/07/v3/zwsz1Lx5TNCGPS-gwRYw0g/zh-cn_image_0000002628394854.png "点击放大")

## 背景知识

* [disableSwipe](../harmonyos-references/ts-container-swiper.md#disableswipe8)：设置禁用组件滑动切换功能。
* [enabled](../harmonyos-references/ts-universal-attributes-enable.md#enabled)：设置组件是否可交互。当未设置enabled时，组件默认可交互。
* [showNext](../harmonyos-references/ts-container-swiper.md#shownext)：翻至下一页。
* [showPrevious](../harmonyos-references/ts-container-swiper.md#showprevious)：翻至上一页。

## 解决方案

* 方案一：禁止手动滑动，但保留导航点功能。

  通过设置Swiper组件的disableSwipe属性为true实现禁止手动滑动功能。

  代码示例如下：

  ```screen
  @Entry
  @Component
  struct DisableSwiperOne {
    private swiperController: SwiperController = new SwiperController();

    build() {
      Swiper(this.swiperController) {
        ForEach(['1', '2', '3'], (item: string) => {
          Text(`Item${item}`)
            .width('100%')
            .height(250)
            .backgroundColor('#F1F3F5')
            .textAlign(TextAlign.Center)
            .fontSize(30)
        })
      }
      .indicator(true)
      .disableSwipe(true) // 设置禁止手势滑动，点击导航点依旧可以滑动
      .displayCount(1)
      .padding(16)
    }
  }
  ```

  效果图如下：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c6/v3/FlsQiHzkRRCC9Bi7H--3Wg/zh-cn_image_0000002658914073.png "点击放大")
* 方案二：禁止手动滑动和导航点切换。

  通过设置enabled属性为false，使Swiper组件不可交互，不响应事件。此时Swiper组件可以通过[SwiperController](../harmonyos-references/ts-container-swiper.md#swipercontroller)的showNext和showPrevious方法进行翻页。

  代码示例如下：

  ```screen
  @Entry
  @Component
  struct DisableSwiperTwo {
    private swiperController: SwiperController = new SwiperController();
    @State canSwiper: boolean = true; // 设置组件是否可交互

    build() {
      Column() {
        Swiper(this.swiperController) {
          ForEach(['1', '2', '3'], (item: string) => {
            Text(`Item${item}`)
              .width('100%')
              .height(250)
              .backgroundColor('#F1F3F5')
              .textAlign(TextAlign.Center)
              .fontSize(30)
          })
        }
        .indicator(true)
        .enabled(this.canSwiper)
        .displayCount(1)
        .padding(16)

        Column({ space: 12 }) {
          Button('showNext')
            .onClick(() => {
              this.swiperController.showNext();
            })
          Button('showPrevious')
            .onClick(() => {
              this.swiperController.showPrevious();
            })
          Button('canSwiper')
            .onClick(() => {
              this.canSwiper = !this.canSwiper;
            })
        }.margin(5)
      }
    }
  }
  ```

  效果图如下：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/88/v3/GzoOxk12RBqyrjCrtaDkYg/zh-cn_image_0000002658794121.png "点击放大")
