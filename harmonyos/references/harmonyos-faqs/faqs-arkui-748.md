---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-748
title: 如何使用一个进度条同时显示两个进度
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 如何使用一个进度条同时显示两个进度
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:03+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:00012fc54d6fd47411e3aaf5efcd75e9959ff89525d89697339f9384b78d06ca
---

## 问题现象

视频进度条包含当前播放进度和视频缓冲进度，目前Slider组件只能设置一级进度，如何设置二级进度值用来显示播放缓冲进度？

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a3/v3/1pZuqkZQQ-2lyx8I2wHxTQ/zh-cn_image_0000002658914685.gif "点击放大")

## 背景知识

[Slider](../harmonyos-references/ts-basic-components-slider.md)组件用于快速调节设置值，如音量调节、亮度调节等应用场景，该组件仅支持接收一个进度值变化，而[Stack](../harmonyos-guides/arkts-layout-development-stack-layout.md)层叠布局提供了页面层叠能力，可以实现广告、卡片层叠等效果。

## 解决方案

使用Stack布局将两个Slider组件叠加在一起，实现一个进度条同时显示两个进度的效果。

```ts
@Entry
@Component
struct SliderExample {
  @State outSetValueOne: number = 0;
  @State outSetValueTwo: number = 0;
  @State intervalTimerOne: number = 1;
  @State intervalTimerTwo: number = 2;
  uiContext: UIContext | undefined = undefined;

  aboutToAppear(): void {
    this.uiContext = this.getUIContext();
    //  动画控制进度丝滑更新
    this.intervalTimerOne = setInterval(() => {
      this.uiContext?.animateTo({
        duration: 500,
        curve: Curve.Linear,
        playMode: PlayMode.Normal,
        onFinish: () => {
          console.info('play end');
        }
      }, () => {
        this.outSetValueOne += 5;
      });
    }, 500);
    this.intervalTimerTwo = setInterval(() => {
      this.uiContext?.animateTo({
        duration: 500,
        curve: Curve.Linear,
        playMode: PlayMode.Normal,
        onFinish: () => {
          console.info('play end');
        }
      }, () => {
        this.outSetValueTwo += 10;
      });
    }, 350);
  }

  build() {
    Column() {
      //  将Slider组件层叠一起
      Stack() {
        Row() {
          Slider({
            value: this.outSetValueTwo,
            min: 0,
            max: 100,
            style: SliderStyle.NONE
          })
            .showTips(true)
            .selectedColor('#bfbfbf')
            .trackColor(Color.Transparent)
            .trackThickness(12)
            .onChange((value: number) => {
              this.outSetValueTwo = value;
              if (this.outSetValueTwo === 100) {
                clearInterval(this.intervalTimerTwo);
              }
            })
        }
        .width('92%')

        Row() {
          Slider({
            value: this.outSetValueOne,
            min: 0,
            max: 100,
            style: SliderStyle.NONE
          })
            .showTips(true)
            .trackThickness(12)
            .onChange((value: number) => {
              this.outSetValueOne = value;
              if (this.outSetValueOne === 100) {
                clearInterval(this.intervalTimerOne);
              }
            })
        }
        .width('92%')
      }
    }
    .width('100%')
    .height('100%')
    .justifyContent(FlexAlign.Center)
  }
}
```
