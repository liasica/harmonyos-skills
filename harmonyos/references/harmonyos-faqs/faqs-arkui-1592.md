---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1592
title: 如何解决显式动画过程中点击事件无法触发的问题
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 如何解决显式动画过程中点击事件无法触发的问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:25+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:4c3cb3daf21e05f6236530cc9b35d0bb702f8a51eb8564d41c445e8a8013296e
---

## 问题现象

当组件在动画执行过程中，对组件当前显示位置进行点击操作，无法触发onClick事件，唯有当动画结束、组件停止在最终位置后，该组件的点击操作才可正常响应。如何在动画执行过程中使组件能正确响应onClick事件？

```ts
@Entry
@Component
struct Problem {
  @State title: string = '点击更新时间参数：';
  @State x: number = 0;

  startAnimation() {
    this.getUIContext().animateTo({ duration: 5000, playMode: PlayMode.Normal }, () => {
      this.x = 100;
    });
  }

  build() {
    Stack() {
      Text(this.title)
        .fontSize(18)
        .position({ x: this.x, y: 40 })
        .animation({
          duration: 5000,
          curve: Curve.Linear,
          playMode: PlayMode.Normal
        })
        .onClick(() => {
          this.title = '点击更新时间参数：' + new Date().getTime();
        })
        .onAppear(() => {
          this.startAnimation();
        });
    }
    .height(100)
    .width('100%');
  }
}
```

## 背景知识

* [@ohos.animator(动画)](../harmonyos-references/js-apis-animator.md)：提供组件动画效果，包括定义动画、启动动画和以相反的顺序播放动画等。
* [显式动画(animateTo)](../harmonyos-references/ts-explicit-animation.md)：提供全局animateTo显式动画接口来指定由于闭包代码导致的状态变化插入过渡动效。

## 解决方案

1. 由于显式动画的特性，目标对象在动画执行期间所处的位置仅在动画结束时被识别和记录。当用户在动画播放过程中尝试点击该对象时，点击事件无法被正确识别和响应。
2. 为了解决这一问题，可以采用帧动画的方式来实现，帧动画通过逐帧定义对象的状态，系统会在每一帧更新对象的位置和状态，并据此响应用户交互事件。完整示例代码参考如下：

   ```ts
   import { AnimatorResult } from '@kit.ArkUI';

   @Entry
   @Component
   struct SolutionOne {
     @State title: string = '点击更新时间参数：';
     @State x: number = 0;
     private backAnimator: AnimatorResult = this.getUIContext().createAnimator({
       duration: 5000,
       easing: 'ease',
       delay: 0,
       fill: 'forwards',
       direction: 'normal',
       iterations: -1,
       begin: 0,
       end: 100
     });

     build() {
       Stack() {
         Text(this.title)
           .fontSize(18)
           .position({ x: this.x, y: 40 })
           .onClick(() => {
             this.title = '点击更新时间参数：' + new Date().getTime();
           })
           .onAppear(() => {
             this.backAnimator.play();
             this.backAnimator.onFrame = (value: number) => {
               this.x = value;
             };
           });
       }
       .height(100)
       .width('100%');
     }
   }
   ```
