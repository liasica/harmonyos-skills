---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-743
title: 如何解决元素显隐时动画只执行一次的问题
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 如何解决元素显隐时动画只执行一次的问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:20+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:93419f92eb6321851f3fd994fa4ff01b42cd0e04948e1a2f4760802566c1e760
---

## 问题现象

元素在显示隐藏时使用animateTo显式动画来控制显示的元素实现360°旋转效果，元素只在第一次显示时执行动画，后续再点击元素显示时动画不再执行。

问题代码示例参考如下：

```ts
@ComponentV2
@Entry
struct Index {
  @Local rotateAngle: number = 0
  @Local isAnimating: boolean = false // 动画状态

  // 启动动画的方法
  startAnimation() {
    this.isAnimating = true
    this.getUIContext()?.animateTo({
      duration: 1000, // 动画持续时间，单位毫秒
      curve: Curve.Linear, // 线性动画，确保匀速
      iterations: -1, // 无限循环
      playMode: PlayMode.Normal, // 正常播放模式，避免交替
      expectedFrameRateRange: {
        min: 10,
        max: 120,
        expected: 60,
      }
    }, () => {
      if (this.isAnimating) {
        this.rotateAngle = 360 // 旋转角度从0到360
      }
    })
  }

  build() {
    Column() {
      if (!this.isAnimating) {
        Text('遮挡条')
          .width('100%')
          .height(40)
          .backgroundColor('#2b3d79')
      } else {
        Image($r('app.media.startIcon'))
          .width(20)
          .height(20)
          .syncLoad(true) // 同步加载避免闪烁
          .interpolation(ImageInterpolation.High) // 高质量渲染
          .rotate({
            x: 0,
            y: 0,
            z: 1,
            angle: this.rotateAngle
          })
          .onAppear(() => {
            this.startAnimation()
          })
      }
      Text(this.isAnimating ? '展示遮挡条' : '隐藏遮挡条')
        .width('100%')
        .height(40)
        .backgroundColor('#0092ff')
        .onClick(() => {
          this.isAnimating = !this.isAnimating
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

## 背景知识

* [组件内转场](../harmonyos-references/ts-transition-animation-component.md)：通过[transition属性](../harmonyos-references/ts-transition-animation-component.md#属性)配置转场参数，在组件插入和删除时显示过渡动效，以提升用户体验。
* [visibility](../harmonyos-references/ts-universal-attributes-visibility.md#visibility)属性：可以用来控制元素的显示与隐藏，并结合显式动画来实现元素的显示与隐藏效果。
* [onAppear](../harmonyos-references/ts-universal-events-show-hide.md#onappear)：组件挂载显示后触发此回调。

## 问题定位

观察代码发现Image图片只有在其onAppear时会执行一次startAnimation动画方法，后续点击下方的元素不会触发其onAppear方法，所以动画只执行了一次。

## 分析结论

onAppear方法只执行一次导致动画只执行了一次。

## 修改建议

针对onAppear方法只执行一次导致动画只执行了一次问题，有以下两种解决方案：

* **方案一**：通过visibility属性来控制元素的显示隐藏，这样Image每次显示时都会触发onAppear方法。

  ```ts
  @Entry
  @ComponentV2
  struct ShowAnimationDemo {
    @Local rotateAngle: number = 0;
    @Local isAnimating: boolean = false; // 动画状态

    // 启动动画的方法
    startAnimation() {
      this.getUIContext()?.animateTo({
        duration: 1000, // 动画持续时间，单位毫秒
        curve: Curve.Linear, // 线性动画，确保匀速
        iterations: -1, // 无限循环
        playMode: PlayMode.Normal, // 正常播放模式，避免交替
        expectedFrameRateRange: {
          min: 10,
          max: 120,
          expected: 60,
        }
      }, () => {
        this.rotateAngle = 360;
      });
    };

    build() {
      Column() {
        if (!this.isAnimating) {
          Text('遮挡条')
            .width('100%')
            .height(40)
            .backgroundColor('#2b3d79')
        }
        Image($r('app.media.startIcon'))
          .width(20)
          .height(20)
          .id('image1')
          .syncLoad(true)
          .interpolation(ImageInterpolation.High)
          .visibility(this.isAnimating ? Visibility.Visible : Visibility.None)
          .rotate({
            x: 0,
            y: 0,
            z: 1,
            angle: this.rotateAngle
          })
          .onAppear(() => {
            this.startAnimation();
          });
        Text(this.isAnimating ? '展示遮挡条' : '隐藏遮挡条')
          .width('100%')
          .height(40)
          .backgroundColor('#0092ff')
          .onClick(() => {
            this.isAnimating = !this.isAnimating;
          });
      }
      .width('100%')
      .height('100%')
    }
  }
  ```
* **方案二**：使用组件内转场通过transition属性配置转场参数，在组件插入和删除时显示过渡动效，主要用于容器组件中的子组件插入和删除时，提升用户体验。

  ```ts
  @Entry
  @ComponentV2
  struct ShowAnimationDemo2  {
    @Local rotateAngle: number = 0;
    @Local isAnimating: boolean = false; // 动画状态

    build() {
      Column() {
        if (!this.isAnimating) {
          Text('遮挡条')
            .width('100%')
            .height(40)
            .backgroundColor('#2b3d79')
        } else {
          Image($r('app.media.startIcon'))
            .width(20)
            .height(20)
            .margin({top:2})
            .id('image1')
            .syncLoad(true)
            .interpolation(ImageInterpolation.High)
            .transition( // 配置组件内转场参数
              TransitionEffect.rotate({ z: -1, angle: 360 })
                .animation({ duration: 1000, iterations: -1, curve: Curve.Linear })
            )
        }
        Text(this.isAnimating ? '展示遮挡条' : '隐藏遮挡条')
          .width('100%')
          .height(40)
          .backgroundColor('#0092ff')
          .onClick(() => {
            this.isAnimating = !this.isAnimating;
          });
      }
      .width('100%')
      .height('100%')
    }
  }
  ```
