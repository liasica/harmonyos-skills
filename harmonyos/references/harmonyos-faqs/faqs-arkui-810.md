---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-810
title: 手势拖拽时和Swiper组件滑动发生冲突如何解决
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 手势拖拽时和Swiper组件滑动发生冲突如何解决
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:04+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:1115e99b6ddc68ab1df007d590a0c94dc3845309384fcb8ac5fe6f3a3b9befba
---

## 问题现象

当Swiper组件与子组件发生手势冲突，或者Swiper组件的滑动与嵌套了Swiper的外部组件的gesture手势冲突时，如何解决？

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/36/v3/VloEHRzcShiQJ2spexrtGg/zh-cn_image_0000002628557800.gif "点击放大")

## 背景知识

* [Swiper](../harmonyos-references/ts-container-swiper.md)组件是滑块视图容器，提供子组件滑动轮播显示的能力。
* [TapGesture](../harmonyos-references/ts-basic-gestures-tapgesture.md)手势支持单击、双击和多次点击事件的识别。

## 解决方案

Swiper嵌套的页面包含[Canvas](../harmonyos-references/ts-components-canvas-canvas.md)时，使Canvas不响应左右滑动事件，不会触发Swiper切换显示。可以通过以下步骤实现：

1. 通过[priorityGesture](../harmonyos-references/ts-gesture-settings.md#prioritygesture)给画布绑定优先识别手势，使得画布组件Canvas优先于其他组件响应滑动事件。
2. 通过[触摸测试控制](../harmonyos-references/ts-universal-attributes-hit-test-behavior.md)来处理滑动冲突，确保在滑动Swiper时，Canvas组件不会被滑动。
3. 在主组件Index中，创建Swiper组件，同时在Swiper中调用自定义组件CanvasExample，使得画布在Swiper的页面中可见。

```ts
@Component
struct CanvasExampleOne {
  // 用来配置CanvasRenderingContext2D对象的参数，包括是否开启抗锯齿，true表明开启抗锯齿。
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  // 用来创建CanvasRenderingContext2D对象，通过在canvas中调用CanvasRenderingContext2D对象来绘制。
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);

  build() {
    Column() {
      Text('Canvas');
      // 在canvas中调用CanvasRenderingContext2D对象。
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffffffff')
        .onReady(() => {
          // 可以在这里绘制内容。
          this.context.strokeRect(50, 50, 200, 150);
        })
        .priorityGesture(GestureGroup(GestureMode.Exclusive,
          SwipeGesture()
            .onAction(() => {
              console.info(`Canvas响应，swiper不响应`);
            })
        ))
        .hitTestBehavior(HitTestMode.Block)
        .width('80%')
        .height('50%');
    }
    .width('100%')
    .height('100%')
    .backgroundColor('#ffbfffff');
  }
}

@Entry
@Component
struct GestureDragAndSwiper {
  private swiperController: SwiperController = new SwiperController();

  build() {
    Swiper(this.swiperController) {
      Text('0')
        .width('100%')
        .height('100%')
        .backgroundColor('#ff96b1ff')
        .textAlign(TextAlign.Center)
        .fontSize(30);
      Text('1')
        .width('100%')
        .height('100%')
        .backgroundColor('#ffffdcc6')
        .textAlign(TextAlign.Center)
        .fontSize(30);
      Text('2')
        .width('100%')
        .height('100%')
        .backgroundColor('#ffc9ffd9')
        .textAlign(TextAlign.Center)
        .fontSize(30);
      CanvasExampleOne();
    }.loop(false);
  }
}
```

## 常见FAQ

Q：场景二中除了使用优先识别手势priorityGesture，还有其他替代方案吗？

A：可以使用自定义手势判定方法[onGestureJudgeBegin](../harmonyos-references/ts-gesture-customize-judge.md#ongesturejudgebegin)，实现对[手势的自定义判定](../harmonyos-references/ts-gesture-customize-judge.md#示例1自定义手势判定)。
