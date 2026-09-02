---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1229
title: 如何实现从底部弹出自定义弹窗并根据手势下拉关闭
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 如何实现从底部弹出自定义弹窗并根据手势下拉关闭
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:07+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:e086217d9927c62505181519fa4296d74c8d057e0e3c80f6acd11c96ee48d21d
---

## 问题现象

如何实现一个从底部弹出的自定义弹窗，并支持通过手势下拉来关闭该弹窗？

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bf/v3/ohZzGh7LQgmsCGxguwf5Wg/zh-cn_image_0000002628594046.gif "点击放大")

## 背景知识

* [弹窗](../harmonyos-guides/arkts-dialog-overview.md)一般指打开应用时自动弹出或者用户行为操作时弹出的UI界面，用于短时间内展示用户需关注的信息或待处理的操作。
* [自定义弹窗 (CustomDialog)](../harmonyos-references/ts-methods-custom-dialog-box.md)可用于广告、中奖、警告、软件更新等与用户交互响应操作。开发者可以通过[CustomDialogController](../harmonyos-references/ts-methods-custom-dialog-box.md#customdialogcontroller)类显示自定义弹出框。
* [触摸事件](../harmonyos-references/ts-universal-events-touch.md)由手指在组件上按下、滑动或抬起时触发。[onTouch](../harmonyos-references/ts-universal-events-touch.md#ontouch)是手指触摸动作触发的回调，可以获取触摸类型[TouchType](../harmonyos-references/ts-appendix-enums.md#touchtype)（按下、滑动、抬起等），以及触点信息[TouchObject](../harmonyos-references/ts-universal-events-touch.md#touchobject)（类型、坐标、时间等）。
* [transition](../harmonyos-references/ts-transition-animation-component.md#transition)可用于设置组件插入显示和删除隐藏的过渡效果。

## 解决方案

可以通过onTouch监听触摸事件，判断用户是否进行了下拉动作，然后使用transition实现弹窗的入场和出场动画，最后为了保证动画完整播放，关闭操作延迟执行。

```screen
let anmDuration: number = 300;

// 弹窗交互
@CustomDialog
struct CustomDialogExampleOne {
  controller?: CustomDialogController;
  @State showFlag: Visibility = Visibility.Visible;
  touchDown: number = 0;
  touchUp: number = 0;

  build() {
    Column() {
      Row() {
        Text('自定义动画的弹窗');
      }
      .borderRadius(16)
      .backgroundColor('#fff')
      .padding(24)
      .width('100%')
      .justifyContent(FlexAlign.Center);
    }
    .justifyContent(FlexAlign.Center)
    .width('100%')
    .height('100%')
    .padding({ left: 16, right: 16 })
    .onTouch((event?: TouchEvent) => {
      if (event) {
        if (event.type === TouchType.Down) {
          this.touchDown = event.touches[0].y;
        }
        if (event.type === TouchType.Up) {
          this.touchUp = event.touches[0].y;
        }
        if (this.touchUp - this.touchDown > 0) {
          this.cancel();
        }
      }
    })
    .visibility(this.showFlag)
    // 定义进场出场转场动画效果
    .transition(
      TransitionEffect.OPACITY
        .animation({ duration: anmDuration })
        .combine(TransitionEffect.translate({ y: 500 }))
    );
  }

  // 延迟关闭弹窗，让自定义的出场动画显示
  cancel() {
    this.showFlag = Visibility.Hidden;
    setTimeout(() => {
      this.controller?.close();
    }, anmDuration);
  }
}

@Entry
@Component
struct CustomDialogUser {
  dialogController: CustomDialogController = new CustomDialogController({
    builder: CustomDialogExampleOne(),
    customStyle: true
  });

  build() {
    Column() {
      Button('click me')
        .onClick(() => {
          this.dialogController.open();
        })
        .margin({ top: 10 });
    }
    .width('100%')
    .height('100%');
  }
}
```

## 常见FAQ

Q：自定义组件添加[TransitionEffect](../harmonyos-references/ts-transition-animation-component.md#transitioneffect10对象说明).OPACITY进场出场动画，组件显示的颜色是否和透明度有关系？

A：为组件添加透明度转场效果，出现时透明度从0到1，消失时透明度从1到0，当完全透明的时候，显示的是组件自身的背景色。
