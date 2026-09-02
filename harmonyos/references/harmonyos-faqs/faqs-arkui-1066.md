---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1066
title: 如何解决Canvas节点重新渲染后CanvasRenderingContext2D参数的属性会重置的问题
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 如何解决Canvas节点重新渲染后CanvasRenderingContext2D参数的属性会重置的问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:27+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:95711dd69b8a380c336c618151162ec9d956095ed2c35f71be7694621360bc57
---

## 问题现象

使用animator给Canvas实现动画效果，onReady中设置画笔颜色为蓝色，大小为'bold 18vp sans-serif'。Canvas宽度改变后CanvasRenderingContext2D画笔的粗细和颜色发生重置效果。

问题效果如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5d/v3/a3O3BCIdQhuhxHXDbi50dg/zh-cn_image_0000002658806483.png "点击放大")

点击变更时，蓝色的大“测试”闪烁成黑色的小“测试”。疑似CanvasRenderingContext2D发生重置。

问题代码如下：

```ts
import { AnimatorOptions, AnimatorResult } from '@kit.ArkUI'

@Entry
@Component
struct Index {
  private settings: RenderingContextSettings = new RenderingContextSettings(true)
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)
  private animatorResult: AnimatorResult = this.createAnimator()
  @State widthDp: number = 150

  aboutToAppear(): void {
    this.animatorResult.onFrame = (progress) => {
      this.context.clearRect(0, 0, 1000, 1000)
      this.context.fillText('测试', 30, 30)
      this.widthDp = 150 + (progress * 10)
    }
  }

  build() {
    Column() {
      // 需求:点击变更按钮的时候,Canvas绘制的内容不会闪动
      Button('变更').onClick(() => {
        this.animatorResult.play()
      })
      Canvas(this.context)
        .width(this.widthDp)
        .height(100)
        .onReady(() => {
          this.context.fillStyle = '#5291FF'
          this.context.font = 'bold 18vp sans-serif'
        })
    }
    .justifyContent(FlexAlign.Center)
    .alignItems(HorizontalAlign.Center)
    .height('100%')
    .width('100%')
  }

  private createAnimator() {
    this.settings.antialias = true
    // 创建动画的初始参数
    let options: AnimatorOptions = {
      duration: 1000,
      easing: 'friction',
      delay: 0,
      fill: 'forwards',
      direction: 'normal',
      iterations: 1,
      begin: 0, // 动画onFrame插值首帧值
      end: 18, // 动画onFrame插值尾帧值
    };
    return this.getUIContext().createAnimator(options)
  }
}
```

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c3/v3/SOTf3AAjSzGl9jM63jl2vQ/zh-cn_image_0000002628567126.png "点击放大")

## 背景知识

* [Canvas](../harmonyos-references/ts-components-canvas-canvas.md)是画布组件，组件本身只相当于一个画布，其参数[CanvasRenderingContext2D](../harmonyos-references/ts-canvasrenderingcontext2d.md)相当于画笔，[onReady](../harmonyos-references/ts-components-canvas-canvas.md#onready)是Canvas相关资源准备完毕后触发的回调，通常在此回调中使用CanvasRenderingContext2D进行赋值和绘制操作。
* [@ohos.animator (动画)](../harmonyos-references/js-apis-animator.md)每帧触发一次[AnimatorResult](../harmonyos-references/js-apis-animator.md#animatorresult)的onFrame回调。

## 问题定位

1. 查看代码中动画实现部分：自定义组件在生命周期aboutToAppear中创建了帧动画，每一帧动画执行时，系统会调用onFrame回调函数修改Canvas宽度。
2. 查阅Canvas官网文档可知：Canvas组件发生大小变化时会触发onReady回调，而问题代码中onReady回调中重置了画笔CanvasRenderingContext2D的样式。

## 分析结论

动画过程中每一帧都会重新渲染，所以每一帧会触发onFrame回调，也都会触发onReady回调，在onReady中设置CanvasRenderingContext2D的值完成之前就已经执行了onFrame中绘制“测试”的操作，体现为一个小的黑色“测试”。

## 修改建议

为防止Canvas刷新导致CanvasRenderingContext2D参数被重置，不要在onReady中进行参数设置，而是仅在onFrame中执行画布的清除，画笔参数的设置，绘制文字的全部过程。

同时改变this.context.font的赋值，使其根据progress的变化增长。使动画变为一个“测试”逐渐变大的动画。

```ts
import { AnimatorOptions, AnimatorResult } from '@kit.ArkUI';

@Entry
@Component
struct FrameAnimator {
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  private animatorResult: AnimatorResult = this.createAnimator();
  @State widthDp: number = 150;

  aboutToAppear(): void {
    this.animatorResult.onFrame = (progress) => {
      this.widthDp = 150 + (progress * 10);
      this.context.clearRect(0, 0, 1000, 1000);
      this.context.fillStyle = '#5291FF';
      this.context.font = `bold ${progress}vp sans-serif`;
      this.context.fillText('测试', 30, 30);
    };
  }

  build() {
    Column() {
      // 需求:点击变更按钮的时候,Canvas绘制的内容不会闪动
      Button('变更').onClick(() => {
        this.animatorResult.play();
      });
      Canvas(this.context)
        .width(this.widthDp)
        .height(100)
        .onReady(() => {
        });
    }
    .justifyContent(FlexAlign.Center)
    .alignItems(HorizontalAlign.Center)
    .height('100%')
    .width('100%');
  }

  private createAnimator() {
    this.settings.antialias = true;
    // 创建动画的初始参数
    let options: AnimatorOptions = {
      duration: 1000,
      easing: 'friction',
      delay: 0,
      fill: 'forwards',
      direction: 'normal',
      iterations: 1,
      begin: 0, // 动画onFrame插值首帧值
      end: 18, // 动画onFrame插值尾帧值
    };
    return this.getUIContext().createAnimator(options);
  }
}
```
