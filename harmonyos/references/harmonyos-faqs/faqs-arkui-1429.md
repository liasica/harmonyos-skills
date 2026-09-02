---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1429
title: 如何实现双层Swiper组件嵌套联动
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 如何实现双层Swiper组件嵌套联动
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:10+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:d33f3244d0a267b4c80b84a9c352789142db384860b35db098d303287ed10da2
---

## 问题现象

Swiper组件嵌套Swiper，当子组件滑动到首页或尾页边界时，如何实现子组件索引不变，父组件滑动到上一个或下一个页签。

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9e/v3/xkzTUvZRTdad9KZ2wAgFoA/zh-cn_image_0000002628763650.png "点击放大")

## 背景知识

* [Swiper：](../harmonyos-references/ts-container-swiper.md)滑块视图容器，提供子组件滑动轮播显示的能力。
* [onGestureRecognizerJudgeBegin：](../harmonyos-references/ts-gesture-blocking-enhancement.md#ongesturerecognizerjudgebegin13)自定义手势识别器判定回调。通过记录子组件Swiper的索引值，判断当滑动达到子组件Swiper的边界处时，触发回调返回屏蔽使父组件Swiper产生滑动手势。
* [PanGesture](../harmonyos-references/ts-basic-gestures-pangesture.md)：滑动手势事件，当滑动的最小距离达到设定的最小值时触发滑动手势事件。

## 解决方案

* **方案一**：通过获取Swiper子组件进行手势滑动时的velocityX（当前手势的x轴方向速度）和索引值，判断当滑动达到子组件Swiper的边界处时，触发回调返回屏蔽使父组件Swiper产生滑动手势。

  ```ts
  @Entry
  @Component
  struct NestedSwiperExample {
    private swiperController: SwiperController = new SwiperController();
    // 外层Swiper的数据
    private outerSwiperData: string[] = ['Page 1', 'Page 2', 'Page 3'];
    // 内层Swiper的数据
    private innerSwiperData: string[] = ['Image 1', 'Image 2', 'Image 3'];
    // 外层Swiper的索引
    @State outerIndex: number = 0;
    // 内层Swiper的索引
    @State innerIndex: number = 0;

    build() {
      Swiper(this.swiperController) {
        ForEach(this.outerSwiperData, (outerItem: string) => {
          Column() {
            Text(outerItem)
              .fontSize(24)
              .margin({ top: 20, bottom: 20 });

            Swiper() {
              ForEach(this.innerSwiperData, (innerItem: string) => {
                Column() {
                  Text(innerItem)
                    .fontSize(18);
                }
                .width('100%')
                .height(200)
                .backgroundColor('#e0e0e0')
                .margin({ bottom: 10 })
              });
            }
            .width('100%')
            .height(200)
            .autoPlay(false)
            .loop(true)
            .index(this.innerIndex)
            .onAnimationStart((index: number, targetIndex: number) => {
              console.info('index', index);
              this.innerIndex = targetIndex;
            })
            .onGestureRecognizerJudgeBegin((event: BaseGestureEvent, current: GestureRecognizer,
              others: Array<GestureRecognizer>): GestureJudgeResult => { // 在识别器即将要成功时，根据当前组件状态，设置识别器使能状态
              console.info('others', others);
              console.info('ets onGestureRecognizerJudgeBegin child');
              if (current) {
                let target = current.getEventTargetInfo();
                if (target && current.isBuiltIn() && current.getType() === GestureControl.GestureType.PAN_GESTURE) {
                  console.info('ets onGestureRecognizerJudgeBegin child PAN_GESTURE');
                  let panEvent = event as PanGestureEvent;
                  if (panEvent && panEvent.velocityX < 0 && this.innerIndex === 2) { // 内层Swiper滑动到尾页
                    this.innerIndex = 0;
                    console.info('ets onGestureRecognizerJudgeBegin child reject end');
                    return GestureJudgeResult.REJECT;
                  }
                  if (panEvent && panEvent.velocityX > 0 && this.innerIndex === 0) { // 内层Swiper滑动到首页
                    console.info('ets onGestureRecognizerJudgeBegin child reject begin');
                    this.innerIndex = 0;
                    return GestureJudgeResult.REJECT;
                  }
                }
              }
              return GestureJudgeResult.CONTINUE;
            }, true)
          }
          .width('100%')
          .height('100%');
        });
      }
      .width('100%')
      .height('100%')
      .autoPlay(false)
      .loop(false)
      .index(this.outerIndex)
      .onAnimationStart((index: number, targetIndex: number, event: TabsAnimationEvent) => {
        console.info('index', index);
        console.info('event', event);
        this.outerIndex = targetIndex;
      })
    }
  }
  ```
* **方案二**：通过PanGesture手势获取滑动的速度和索引值，判断当滑动达到子组件Swiper的边界处时，调用父组件showNext()和showPrevious()方法，来控制父组件滑动到上一个和下一个页签。示例代码如下：

  ```screen
  @Entry
  @Component
  struct SwiperExample {
    private swiperController: SwiperController = new SwiperController();
    // 外层Swiper的数据
    private outerSwiperData: string[] = ['Page 1', 'Page 2', 'Page 3'];
    // 内层Swiper的数据
    private innerSwiperData: string[] = ['Image 1', 'Image 2', 'Image 3'];
    // 外层Swiper的索引
    @State outerIndex: number = 0;
    // 内层Swiper的索引
    @State innerIndex: number = 0;

    build() {
      Swiper(this.swiperController) {
        ForEach(this.outerSwiperData, (outerItem: string) => {
          Column() {
            Text(outerItem)
              .fontSize(24)
              .margin({ top: 20, bottom: 20 });

            Swiper() {
              ForEach(this.innerSwiperData, (innerItem: string) => {
                Column() {
                  Text(innerItem)
                    .fontSize(18);
                }
                .width('100%')
                .height(200)
                .backgroundColor('#e0e0e0')
                .margin({ bottom: 10 });
              });
            }
            .width('100%')
            .height(200)
            .autoPlay(false)
            .loop(false)
            .index(this.innerIndex)
            .onAnimationStart((index: number, targetIndex: number) => {
              console.info('index', index);
              this.innerIndex = targetIndex;
            })
            .parallelGesture(
              PanGesture()
                .onActionEnd((e) => {
                  let velocityX = e.velocityX || 0; // 手势结束，获取当前的速度
                  if (velocityX < 0 && this.innerIndex === 2) {
                    this.innerIndex = 0;
                    this.swiperController.showNext(); // x轴方向速度小于0时，向左移动
                  }
                  if (velocityX > 0 && this.innerIndex === 0) {
                    this.innerIndex = 0;
                    this.swiperController.showPrevious(); // x轴方向速度大于0时，向右移动
                  }
                })
            )
          }
          .width('100%')
          .height('100%');
        });
      }
      .width('100%')
      .height('100%')
      .autoPlay(false)
      .loop(false)
      .index(this.outerIndex)
      .onAnimationStart((index: number, targetIndex: number, event: TabsAnimationEvent) => {
        this.outerIndex = targetIndex;
        console.info('index', index);
        console.info('event', event);
      })
    }
  }
  ```
