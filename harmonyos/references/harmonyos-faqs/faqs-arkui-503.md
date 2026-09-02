---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-503
title: 如何控制Swiper组件只能向一个方向滑动
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 如何控制Swiper组件只能向一个方向滑动
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:00+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:0dc2729f67e19359ccf0258d0ae1b81b2701ce84124d92af50b4ecf28228b266
---

## 问题现象

在使用Swiper组件时，需要控制Swiper组件只往一个方向滑动，例如：

期望只能向右滑动，实际在使用onGestureRecognizerJudgeBegin拦截滑动手势时，先向右滑动不松手，再快速向左滑动Swiper组件会向左滑动并翻页与预期不符。具体现象如下图：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d0/v3/wpneRZIqSGCcLfRD4HTklQ/zh-cn_image_0000002628388618.png "点击放大")

问题代码如下：

```ts
@Entry
@Component
struct Index {
  @State list: string[] = ['1', '2', '3'];
  private swiperController: SwiperController = new SwiperController();

  build() {
    Column() {
      Swiper(this.swiperController) {
        ForEach(this.list, (item: string, index: number) => {
          Text(item.toString())
            .width('90%')
            .height(160)
            .backgroundColor('#F1F3F5')
            .textAlign(TextAlign.Center)
            .fontSize(30)
            .borderRadius(8);
        }, (item: string) => item);
      }
      .loop(true)
      .itemSpace(5)
      .prevMargin(35)
      .nextMargin(35)
      .onGestureRecognizerJudgeBegin((event: BaseGestureEvent, current: GestureRecognizer,
        recognizers: Array<GestureRecognizer>) => {
        // 判断手势识别器的类型
        if (current.getType() === GestureControl.GestureType.PAN_GESTURE) {
          let pan: PanGestureEvent = event as PanGestureEvent;
          // 获取手势事件偏移量X
          if (pan.offsetX < 0) {
            current.setEnabled(true);
            return GestureJudgeResult.CONTINUE;
          } else {
            current.setEnabled(false);
            // 判定手势结果为失败
            return GestureJudgeResult.REJECT;
          }
        }
        return GestureJudgeResult.CONTINUE;
      })
      .prevMargin(100)
      .height(400);
    }
    .width('100%')
    .height('100%');
  }
}
```

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/98/v3/ntikjJMnSK-9LfXQkKF3lw/zh-cn_image_0000002628548518.png "点击放大")

## 背景知识

* [Swiper](../harmonyos-references/ts-container-swiper.md)：滑块视图容器，提供子组件滑动轮播显示的能力；
* [onGestureRecognizerJudgeBegin](../harmonyos-references/ts-gesture-blocking-enhancement.md#ongesturerecognizerjudgebegin13)：自定义手势识别器判定回调，可以获取Swiper组件进行手势滑动时的offsetX从而判断是向右滑动还是向左滑动，再通过返回[GestureJudgeResult](../harmonyos-references/ts-gesture-common.md#gesturejudgeresult11)手势判定结果，实现控制Swiper组件单一方向滑动的需求。

## 解决方案

使用onGestureRecognizerJudgeBegin回调时，按住Swiper组件先向一个方向滑动，不松手再快速向另一个方向滑动时，Swiper组件会向另一个方向滑动并翻页，排查后发现在不松手滑动时Swiper组件不会逐帧触发onGestureRecognizerJudgeBegin回调，因此无法逐帧拦截滑动手势。

可以将[disableSwipe](../harmonyos-references/ts-container-swiper.md#disableswipe8)设置为true，禁止组件滑动切换功能，并且通过PanGesture手势获取滑动的速度，从而判断是调用showNext()还是showPrevious()方法，从而控制Swiper组件只能往一个方向滑动。代码示例如下：

```ts
@Entry
@Component
struct SwiperLimitTest {
  @State list: string[] = ['1', '2', '3'];
  private swiperController: SwiperController = new SwiperController();

  build() {
    Column() {
      Swiper(this.swiperController) {
        ForEach(this.list, (item: string) => {
          Text(item.toString())
            .width('90%')
            .height(160)
            .backgroundColor('#F1F3F5')
            .textAlign(TextAlign.Center)
            .fontSize(30)
            .borderRadius(8)
            .parallelGesture(
              PanGesture().onActionEnd(e => {
                // 手势结束，获取当前的速度
                let velocityX = e.velocityX || 0;
                if (velocityX < 0) {
                  // x轴方向速度小于0时，向左移动
                  this.swiperController.showNext();
                }
              })
            )
        }, (item: string) => item);
      }
      .disableSwipe(true)
      .loop(true)
      .itemSpace(5)
      .prevMargin(35)
      .nextMargin(35)
      .prevMargin(100)
      .height(400);
    }
    .width('100%')
    .height('100%');
  }
}
```
