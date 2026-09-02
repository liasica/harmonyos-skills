---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1008
title: 如何在图片旋转变换时加上动画效果
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 如何在图片旋转变换时加上动画效果
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:25+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:410b96555d82670a3238bad24ae167c5a8361a3f1b56ece1b48069405caaa093
---

## 问题现象

图片A通过旋转变换得到图片B，在旋转过程中如何加上动画效果？

## 背景知识

* [rotate](../harmonyos-references/ts-universal-attributes-transformation.md#rotate)：可以设置组件旋转。
* [帧动画（ohos.animator）](../harmonyos-guides/arkts-animator.md)：帧动画使开发者能够在应用的每一帧设置属性值，从而实现组件属性值变化的自然过渡，营造出动画效果。

## 解决方案

给图片加上rotate属性，点击按钮实现帧动画的播放，在onFrame方法中实现旋转角度的更新，在动画结束后替换图片资源并且归零旋转角度，步骤如下：

1. 定义帧动画：

   ```ts
   aboutToAppear(): void {
     this.result = this.getUIContext().createAnimator(this.options);
     this.result.onFrame = (value: number) => {
       this.angle = -value * 30;
     };
     this.result.onFinish = () => {
       // 这里图片资源需要修改为开发者自定义的资源
       this.imageSource = $r('app.media.img2');
       this.angle = 0;
     };
   }
   ```
2. 给图片加上rotate属性：

   ```ts
   Image(this.imageSource)
     .width(200)
     .height(200)
     .margin({ top: 50 })
     .objectFit(ImageFit.Cover)
     .rotate({
       x: 0,
       y: 0,
       z: 1,
       angle: this.angle,
       centerX: '50%',
       centerY: '50%',
       centerZ: 0,
       perspective: 0
     });
   ```

完整示例参考如下：

```ts
import { AnimatorOptions, AnimatorResult } from '@kit.ArkUI';

@Entry
@Component
struct ImageRotateAnimator {
  @State angle: number = 0;
  // 这里图片资源需要修改为开发者自定义的资源
  @State imageSource: string | Resource = $r('app.media.img1');
  result: AnimatorResult | undefined = undefined;
  private options: AnimatorOptions = {
    duration: 1200,
    easing: 'friction',
    delay: 0,
    fill: 'forwards',
    direction: 'normal',
    iterations: 1,
    begin: 0,
    end: 1
  };

  aboutToAppear(): void {
    this.result = this.getUIContext().createAnimator(this.options);
    this.result.onFrame = (value: number) => {
      this.angle = -value * 30;
    };
    this.result.onFinish = () => {
      // 这里图片资源需要修改为开发者自定义的资源
      this.imageSource = $r('app.media.img2');
      this.angle = 0;
    };
  }

  build() {
    Column() {
      Column() {
        Image(this.imageSource)
          .width(200)
          .height(200)
          .margin({ top: 50 })
          .objectFit(ImageFit.Cover)
          .rotate({
            x: 0,
            y: 0,
            z: 1,
            angle: this.angle,
            centerX: '50%',
            centerY: '50%',
            centerZ: 0,
            perspective: 0
          });
      }
      .borderColor(Color.Blue)
      .borderWidth(2)
      .width(300)
      .height(300);

      Button('Click rotate')
        .onClick(() => {
          this.result?.play();
        });
    }.width('100%').height('100%');
  }
}
```
