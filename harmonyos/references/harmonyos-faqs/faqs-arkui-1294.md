---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1294
title: 控制动画播放与暂停
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 控制动画播放与暂停
category: harmonyos-faqs
scraped_at: 2026-09-02T15:04:00+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:9c5b94f952553743abe30e4057aafe2256962371a9b7ae356aa944f362aa2003
---

## 问题现象

如何实现播放中的动画暂停的功能？

## 背景知识

* [animateTo](../harmonyos-references/arkts-apis-uicontext-uicontext.md#animateto)：提供animateTo接口来指定由于闭包代码导致的状态变化插入过渡动效。用于普通的显式动画下发，适用于不需要立即执行的动画效果。它可以设置动画效果相关参数，但不会立即执行，而是在动画完成后执行闭包代码中的状态变化。
* [@ohos.animator（动画）](../harmonyos-references/js-apis-animator.md)：提供组件动画效果，包括定义动画、启动动画和以相反的顺序播放动画等。是组件级动画控制，通过play/pause等API手动控制动画生命周期，支持独立配置每个动画的参数，可精确控制暂停、反向播放等复杂动画效果。
* [setInterval](../harmonyos-references/js-apis-timer.md#setinterval)：重复调用一个函数，在每次调用之间具有固定的时间延迟。

## 解决方案

* 方案一：通过[lottie](https://gitcode.com/openharmony-tpc/lottieArkTS)动画三方库来实现动画播放暂停，详情参考：lottie[使用示例](https://gitcode.com/openharmony-tpc/lottieArkTS#使用示例)。
* 方案二：可以使用[@ohos.animator(动画)](../harmonyos-references/js-apis-animator.md)的[play](../harmonyos-references/js-apis-animator.md#play)，[pause](../harmonyos-references/js-apis-animator.md#pause)等相关方法来实现动画播放和暂停。具体代码见官网示例：[基于ArkTS扩展的声明式开发范式](../harmonyos-references/js-apis-animator.md#基于arkts扩展的声明式开发范式)。
* 方案三：API20提供了属性动画启停功能，详情请参考：[动画创建与取消示例](../harmonyos-references/js-apis-arkui-framenode.md#动画创建与取消示例)。
* 方案四：使用setInterval结合显式动画（animateTo）实现。
  1. 设置状态变量angle用于控制图像的旋转角度。
  2. 设置状态变量displaying用于控制动画的播放与暂停。
  3. 使用setInterval和clearInterval来控制动画的播放。当点击播放按钮时，执行animateTo动画，修改图片的旋转角度。设置定时器延迟间隔和动画时长相同，实现平滑过渡。点击停止播放按钮时，关闭定时器，保持当前的旋转角度。

  完整示例参考如下：

  ```ts
  @Entry
  @Component
  struct PageOne {
    @State angle: number = 0;
    @State displaying: boolean = false;
    timer: number | null = null;
    duration: number = 400;
    uiContext: UIContext | undefined = undefined;

    aboutToAppear() {
      this.uiContext = this.getUIContext();
    }

    build() {
      Stack() {
        Image($r('app.media.ship'))
          .width(200)
          .height(200)
          .borderRadius(100)
          .backgroundColor(Color.Blue)
          .rotate({ angle: this.angle });

        Text(this.displaying ? '❚❚' : '▶')
          .fontColor(Color.White)
          .fontSize(30)
          .onClick(() => {
            this.displaying = !this.displaying;
            if (this.displaying) {
              this.timer = setInterval(() => {
                this.uiContext?.animateTo({
                  duration: this.duration,
                  iterations: 1,
                  curve: Curve.Linear
                }, () => {
                  this.angle += 50;
                });
              }, this.duration);
            } else {
              clearInterval(this.timer);
            }
          });
      }
      .alignContent(Alignment.Center)
      .width('100%')
      .height('100%');
    }
  }
  ```

  **说明** 

  此方案点击暂停时动画不会立即停止，而会等当前的动画执行完毕，可能会存在体验问题。

  效果图如下：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0/v3/yTJ2ZIbxTNGs6GKtiso-Wg/zh-cn_image_0000002628757880.png "点击放大")
* 方案五：控制多个动画的播放和暂停。实现方法与方案三类似，区别在于当使用setInterval方法播放一个动画时，用clearInterval方法清除掉另外一个动画。

  具体代码如下：

  ```ts
  @Entry
  @Component
  struct PageTwo {
    @State angleOne: number = 0;
    @State angleTwo: number = 0;
    timerOne: number | null = null;
    timerTwo: number | null = null;
    duration: number = 400;
    uiContext: UIContext | undefined = undefined;

    aboutToAppear() {
      this.uiContext = this.getUIContext();
    }

    build() {
      Column({ space: 20 }) {
        Text('动画A：');
        Image($r('app.media.ship')) // 根据具体情况引用资源
          .width(200)
          .height(200)
          .borderRadius(100)
          .backgroundColor(Color.Blue)
          .rotate({ angle: this.angleOne });
        Text('动画B：');
        Image($r('app.media.ship')) // 根据具体情况引用资源
          .width(200)
          .height(200)
          .borderRadius(100)
          .backgroundColor(Color.Blue)
          .rotate({ angle: this.angleTwo });

        Button('播放A，暂停B')
          .fontColor(Color.White)
          .backgroundColor('0A59F7')
          .onClick(() => {
            clearInterval(this.timerOne);
            clearInterval(this.timerTwo);
            this.timerOne = setInterval(() => {
              this.uiContext?.animateTo({
                duration: this.duration,
                iterations: 1,
                curve: Curve.Linear
              }, () => {
                this.angleOne += 50;
              });
            }, this.duration);
          });

        Button('播放B，暂停A')
          .fontColor(Color.White)
          .backgroundColor('0A59F7')
          .onClick(() => {
            clearInterval(this.timerTwo);
            clearInterval(this.timerOne);
            this.timerTwo = setInterval(() => {
              this.uiContext?.animateTo({
                duration: this.duration,
                iterations: 1,
                curve: Curve.Linear
              }, () => {
                this.angleTwo += 50;
              });
            }, this.duration);
          });
      }
      .position({
        left: 90
      });
    }
  }
  ```

  具体演示如下：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d6/v3/U_8f2MgmQG689dN0d6Jahw/zh-cn_image_0000002658957197.png "点击放大")
* 方案六：在显式动画、关键帧动画中新增一个duration为0的动画，即可停止该状态变量所关联**属性的**之前的所有动画，并停止在最终设置的状态变量所对应的状态上。

  具体代码如下：

  ```ts
  @Entry
  @Component
  struct PageThree {
    @State angle: number = 0;
    @State displaying: boolean = false;
    timer: number | null = null;
    duration: number = 4000;
    uiContext: UIContext | undefined = undefined;

    aboutToAppear() {
      this.uiContext = this.getUIContext();
    }

    build() {
      Stack() {
        Image($r('app.media.ship'))
          .width(200)
          .height(200)
          .borderRadius(100)
          .backgroundColor(Color.Blue)
          .rotate({ angle: this.angle });

        Text(this.displaying ? '❚❚' : '▶')
          .fontColor(Color.White)
          .fontSize(30)
          .onClick(() => {
            this.displaying = !this.displaying;
            if (this.displaying) {
              this.uiContext?.animateTo({
                duration: this.duration,
                iterations: 1,
                curve: Curve.Linear,
              }, () => {
                this.angle += 360;
              });
            } else {
              // 启动一个duration为0的动画
              this.uiContext?.animateTo({
                duration: 0,
                iterations: 1,
                curve: Curve.Linear,
              }, () => {
                this.angle = 0;
              });
            }
          });
      }
      .alignContent(Alignment.Center)
      .width('100%')
      .height('100%');
    }
  }
  ```

## 常见FAQ

Q：能否在组件的aboutToAppear中调用animateTo动画？

A：不建议在aboutToAppear中调用动画，自定义组件内的build还未执行，内部组件还未创建，动画时机过早，动画属性没有初值无法对组件产生动画。

Q：为何有些场景动画设置的duration参数并不生效？

A：弹性动画曲线为物理曲线，animation、animateTo、pageTransition中的duration参数不生效，动画持续时间取决于interpolatingSpring动画曲线参数，具体可见[curves.interpolatingSpring](../harmonyos-references/js-apis-curve.md#curvesinterpolatingspring10)。

Q：animation属性生效，是否有特殊要求？

A：属性动画只对写在[animation](../harmonyos-references/ts-animatorproperty.md#animation)前面的属性生效，且对组件构造器的属性不生效。
