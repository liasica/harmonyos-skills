---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1517
title: 如何解决在单次拖动内无法同时实现Scroll组件滚动和Slider进度条变化的问题
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 如何解决在单次拖动内无法同时实现Scroll组件滚动和Slider进度条变化的问题
category: harmonyos-faqs
scraped_at: 2026-09-02T15:03:48+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:643ae984bd36ce176dd2eb880d38ceb3477abd46bcb1e35522723caa4bae0d07
---

## 问题现象

横向的进度条嵌套在Scroll组件中，当触摸进度条时，手指不抬起进行拖动操作，若拖动操作起始为上下，那么后续的拖动只会影响Scroll的滚动。相反，若拖动操作起始为左右，那么后续拖动只会影响Slider进度条的变化，无法影响Scroll滚动。如何实现在单次拖动内Scroll组件和Slider进度条同时响应拖动操作？

问题代码如下：

```ts
@Entry
@Component
struct Index {
  dataArr: number[] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 171, 172, 173, 174];
  @State eventType: string = ''
  @State sliderNum: number[] = []
  @State offsetX: number = 0
  @State offsetY: number = 0
  scroller: Scroller = new Scroller()

  aboutToAppear(): void {
    // 初始化进度条进度参数
    for (let i = 0; i < this.dataArr.length; i++) {
      this.sliderNum[i] = 0
    }
  }

  build() {
    Scroll() {
      WaterFlow({ scroller: this.scroller }) {
        ForEach(this.dataArr, (item: number, index: number) => {
          FlowItem() {
            Column() {
              Slider({
                value: this.sliderNum[index],
                min: 0,
                max: 100,
                style: SliderStyle.OutSet
              })
                .enabled(true) // 取消进度条交互，防止消费拖拽事件
            }
          }
          .height(100)
        })
      }
      .columnsTemplate('1fr 1fr')
      .columnsGap(10)
      .rowsGap(5)
      .backgroundColor(0xFAEEE0)
      .width('100%')
      .height('100%')
    }
    .height('100%')
    .width('100%')
  }
}
```

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6e/v3/bCrO7kQmRTe2vfu5h_PIFw/zh-cn_image_0000002628766438.png "点击放大")

## 背景知识

在嵌套滚动模式下，[nestedScroll](../harmonyos-references/ts-container-scroll.md#nestedscroll10)属性支持在单方向拖动事件的透传，实现与父组件的滚动联动。而滑动组件[Slider](../harmonyos-references/ts-basic-components-slider.md)不支持nestedScroll，因此需要介入拖动手势[PanGesture](../harmonyos-references/ts-basic-gestures-pangesture.md)。

## 解决方案

使用拖动手势PanGesture可以根据手指在每个方向上的移动距离来做控制。后续仅需解决手势绑定在哪个组件上，以及如何使用手势内部参数。

1. 手势绑定的组件：

   只有当手指在Slider上拖动时，才会涉及到影响两个方向的不同组件，因此，将手势绑定在Slider上。这样方便判断拖动的是具体哪一个Slider，而且也不影响其他组件的点击拖动，降低耦合度，以及系统性能消耗。
2. 内部实现手势参数：

   通过[scrollBy](../harmonyos-references/ts-container-scroll.md#scrollby9)影响外部滑动组件。

   通过[SliderOptions](../harmonyos-references/ts-basic-components-slider.md#slideroptions对象说明)对象中的value影响内部进度条组件。

即在进度条上绑定拖动手势，此时需要将Slider通过额外的容器进行包裹，手势绑定在容器上。而Slider本身使用enabled或者hitTestBehavior.None属性取消掉本身对于手势的消费。手势需额外绑定的原因为当组件消费手势，组件额外绑定的手势将不生效，因此需要将手势透传到父组件进行处理，通过定位思路中的内部手势参数即可获得对应的调控接口，实现代码如下：

```ts
@Entry
@Component
struct ScrollSlider {
  dataArr: number[] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 171, 172, 173, 174];
  @State sliderNum: number[] = [];
  @State offsetX: number = 0;
  @State offsetY: number = 0;
  scroller: Scroller = new Scroller();

  aboutToAppear(): void {
    // 初始化进度条进度参数
    for (let i = 0; i < this.dataArr.length; i++) {
      this.sliderNum[i] = 0;
    }
  }

  build() {
    Scroll() {
      WaterFlow({ scroller: this.scroller }) {
        ForEach(this.dataArr, (index: number) => {
          FlowItem() {
            Column() {
              Slider({
                value: this.sliderNum[index],
                min: 0,
                max: 70,
                style: SliderStyle.OutSet
              })
                .margin(16)
                .enabled(false); // 取消进度条交互，防止消费拖拽事件
            }
            .hitTestBehavior(HitTestMode.Block)
            .gesture(
              PanGesture()
                .onActionStart(() => {
                  this.offsetX = 0;
                  this.offsetY = 0;
                })
                .onActionUpdate((event: GestureEvent) => { // 拖动为实时拖动，因此每次拖动的参数需要用当前拖动距离与上次拖动距离做减法
                  if (event) {
                    if (event.offsetY !== 0) {
                      this.scroller.scrollBy(0, -this.getUIContext().px2vp(event.offsetY - this.offsetY));
                      this.offsetY = event.offsetY;
                    }
                    if (event.offsetX !== 0) {
                      this.sliderNum[index] += this.getUIContext().px2vp(event.offsetX - this.offsetX);
                      this.offsetX = event.offsetX;
                    }
                  }
                })
            );
          }.height(100);
        });
      }
      .columnsTemplate('1fr 1fr')
      .columnsGap(10)
      .rowsGap(5)
      .backgroundColor(0xFAEEE0)
      .width('100%')
      .height('100%');
    }
    .height('100%')
    .width('100%');
  }
}
```

**说明** 

1. 手势不要绑定在Scroll组件上，会增加对控制哪一个进度条的判断的问题。
2. 拖动为实时拖动，因此每次拖动的参数需要用当前拖动距离与上次拖动距离做减法。
3. 建议将拖动距离进行单位转换。

## 总结

对于非触摸的交互事件，在第一次被组件消费掉之后就不会再继续往下透传，因此若想单次拖动影响多个组件，需使用手势接口，识别手势后再影响组件。
