---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1315
title: 实现一个左右抖动的动画效果
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 实现一个左右抖动的动画效果
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:27+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:09951cd91365cc6a59c40b58534134a24897b31159ca37ebeeba469bfe226441
---

## 问题现象

如何实现一个全局可以使用的左右抖动的动画效果？

## 背景知识

* [关键帧动画 (keyframeAnimateTo)](../harmonyos-references/ts-keyframeanimateto.md)：在[UIContext](../harmonyos-references/arkts-apis-uicontext-uicontext.md)中提供keyframeAnimateTo接口来指定若干个关键帧状态，实现分段的动画。
* [@BuilderParam装饰器](../harmonyos-guides/arkts-builderparam.md)：@BuilderParam用于装饰指向@Builder方法的变量，开发者可以在初始化自定义组件时，使用不同的方式（如参数修改、尾随闭包、借用箭头函数等）对@BuilderParam装饰的自定义构建函数进行传参赋值。在自定义组件内部，通过调用@BuilderParam为组件增加特定功能。

## 解决方案

1. 创建抖动容器组件：使用keyframeAnimateTo关键帧动画通过控制translateX属性，让动画对象在X轴进行平移，实现左右抖动效果。
2. 设置全局状态：AppStorage.setOrCreate<number>('shakeCount', 0);，便于全局调用该状态。
3. 将需要设置抖动的页面添加抖动容器组件作为根组件，通过按钮点击事件调用AppStorage.set<number>('shakeCount', count + 1)改变shakeCount的值，触发页面抖动效果。

示例参考如下：

```ts
@Entry
@Component
struct ShakeExamplePage {
  build() {
    Column() {
      ShakeContainer() {
        // 原页面内容（如Column/Stack等）
        Column() {
          Text('页面内容').fontSize(20)
          Button('点击').onClick(() => {
            let count = AppStorage.get<number>('shakeCount');
            if (count !== undefined) {
              AppStorage.set<number>('shakeCount', count + 1);
            }
          })
        }
      }
    }
  }
}

const CONFIGURATION: Record<string, number> = {
  'VIBRATION_TIME': 600,
  'ANIMATION_TIME': 100,
  'MARGIN_VERTICAL': 16,
  'FLEX_SHRINK': 1,
  'POPUP_POSITION_X': 8,
  'POPUP_POSITION_Y': 1,
  'MARK_POSITION_X': 4,
  'MARK_POSITION_Y': 9,
  'POSITION_ZERO': 0,
  'POSITION_MINUS_FIVE': -5,
  'OPACITY_VALUE': 0.8,
  'PLAYBACK_COUNT': 2,
  'TRANSLATE_OFFSET_X': 5,
};

@Component
export struct ShakeContainer {
  @Builder
  customBuilder() {
  }

  @BuilderParam content: () => void = this.customBuilder; // 接收页面内容
  @Watch('startAnimation') @StorageLink('shakeCount') shakeCount: number = 0;
  uiContext: UIContext | undefined = undefined;
  @State translateX: number = 0; // 初始化提示文本的偏移量
  private lastTrigger: number = 0;

  aboutToAppear() {
    this.uiContext = this.getUIContext?.();
    if (this.shakeCount > this.lastTrigger) {
      this.lastTrigger = this.shakeCount;
      this.startAnimation(); // 触发动画
    }
  }

  // 触发提示文本抖动动画效果
  startAnimation() {
    if (!this.uiContext) {
      return;
    }
    this.translateX = CONFIGURATION.POSITION_MINUS_FIVE;
    // 通过keyframeAnimateTo关键帧动画指定状态变化过渡动效
    this.uiContext.keyframeAnimateTo({ iterations: CONFIGURATION.PLAYBACK_COUNT }, [
      {
        // 第一段动画时长为100ms，translateX属性从-5到5
        duration: CONFIGURATION.ANIMATION_TIME,
        event: () => {
          this.translateX = CONFIGURATION.TRANSLATE_OFFSET_X;
        }
      },
      {
        // 第二段动画时长为100ms，translateX属性从5到0
        duration: CONFIGURATION.ANIMATION_TIME,
        event: () => {
          this.translateX = CONFIGURATION.POSITION_ZERO;
        }
      }
    ]);
  }

  build() {
    Column() {
      this.content(); // 包裹实际页面内容
    }
    .width('100%')
    .height('100%')
    .backgroundColor(Color.Green)
    .margin({ top: 5 })
    .position({
      x: this.translateX,
      y: CONFIGURATION.POSITION_ZERO
    })
  }
}
```
