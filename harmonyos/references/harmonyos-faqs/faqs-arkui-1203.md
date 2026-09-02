---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1203
title: 移动进场动画的常见场景
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 移动进场动画的常见场景
category: harmonyos-faqs
scraped_at: 2026-09-02T15:04:05+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:0b2860b741e07b44a6268698c68e991caf6c3b75f1d0ce274d69e62564b9be5d
---

## 问题现象

开发者在实现进场动画时，可能会遇到以下几种典型场景：

场景一：如何实现多张图片组成动画组，并实现其向右循环移动的效果？

场景二：如何实现直播间欢迎词的进场动画，使其从左至右移动并逐渐淡出？

场景三：组件当前绑定了一个转场动画transitionEffect，能否在运行时动态切换为另一种转场动画？

## 背景知识

* [帧动画（ohos.animator）](../harmonyos-guides/arkts-animator.md)：帧动画具备逐帧回调的特性，便于开发者在每一帧中处理需调整的属性。
* [animateTo](../harmonyos-references/arkts-apis-uicontext-uicontext.md#animateto)：提供animateTo接口，用于为闭包代码中的状态变化添加过渡动画效果。
* [markAnchor](../harmonyos-references/ts-universal-attributes-location.md#markanchor)：设置元素在位置定位时的锚点，支持attributeModifier动态设置属性方法。
* [transition](../harmonyos-references/ts-transition-animation-component.md)：组件内转场主要通过transition属性配置转场参数，在组件插入和删除时显示过渡动效，主要用于容器组件中的子组件插入和删除时，提升用户体验。

## 解决方案

### 场景一：如何实现多张图片组成动画组，并实现其向右循环移动的效果

1. 使用Repeat组件对图片进行循环渲染，构建统一的排列结构，以便集中控制布局与动画。
2. 借助Animator逐步更新offsetX属性，以此驱动图片产生横向位移的动画效果。
3. 将offsetX的变化值绑定至translate属性，最终呈现多图片向右循环移动的视觉效果。

```ts
import { AnimatorResult } from '@kit.ArkUI';

@Entry
@ComponentV2
export struct MovingAnimationDemo {
  // 循环播放图片资源
  @Local playAnimation: Resource[][] = [
    [
      $r('app.media.startIcon'), // 此处仅为示例，请开发者自行替换为可用图片
      $r('app.media.startIcon'),
      $r('app.media.startIcon'),
      $r('app.media.startIcon')
    ],
    [
      $r('app.media.startIcon'),
      $r('app.media.startIcon'),
      $r('app.media.startIcon'),
      $r('app.media.startIcon')
    ],
    [
      $r('app.media.startIcon'),
      $r('app.media.startIcon'),
      $r('app.media.startIcon'),
      $r('app.media.startIcon')
    ]
  ];
  backAnimator?: AnimatorResult;
  // 动画偏移量
  @Local offsetX: number = -120;
  @Local isPlaying: boolean = false;

  @Monitor('isPlaying')
  onChangeIsPlaying(monitor: IMonitor) {
    monitor.dirty.forEach((path: string) => {
      if (path === 'isPlaying') {
        if (this.isPlaying) {
          this.backAnimator?.play();
        } else {
          this.backAnimator?.pause();
        }
      }
    });
  }

  aboutToAppear() {
    this.backAnimator = this.getUIContext().createAnimator({
      duration: 5000,
      easing: 'liner',
      delay: 0,
      fill: 'both',
      direction: 'normal',
      iterations: -1,
      begin: 0,
      end: 120
    });
    // 在5s内，逐步改变offsetX的值
    this.backAnimator.onFrame = (value: number) => {
      this.offsetX = -120 + value;
    };
  }

  build() {
    Column({ space: 15 }) {
      Text('实现向右循环移动动画效果');
      Row() {
        Row({ space: 5 }) {
          Repeat(this.playAnimation).each(ri => {
            Row({ space: 5 }) {
              Repeat(ri.item).each(ri2 => {
                Image(ri2.item)
                  .height(25)
                  .width(25);
              });
            };
          });
        }
        .translate({ x: this.offsetX })
        .layoutWeight(1);
      }
      .backgroundColor(Color.Gray)
      .width(160)
      .clip(true);

      Button(this.isPlaying ? '暂停' : '播放')
        .width(60)
        .height(40)
        .onClick(() => {
          this.isPlaying = !this.isPlaying;
        });
    }
    .width('100%');
  }
}
```

### 场景二：如何实现直播间欢迎词的进场动画，使其从左至右移动并逐渐淡出

1. 定义变量op以管理欢迎词的显示状态。监听按钮的点击事件，触发animateTo动画，实现欢迎词的入场效果。
2. 利用onFinish回调函数，在入场动画结束后调用animateTo方法，执行隐藏动画，从而实现欢迎词的自动消失效果。

```ts
@Entry
@Component
struct LiveBroadcastDemo {
  message: string = 'xxx进入了直播间';
  @State markX: number | string = '100%';
  @State op: number = 1; // 显示状态

  build() {
    Column() {
      Button('点击进入直播间')
        .margin({ top: 60 })
        .onClick(() => {
          this.getUIContext().animateTo({
            delay: 0,
            duration: 500,
            onFinish: () => {
              this.getUIContext().animateTo({
                delay: 3000,
                duration: 800
              }, () => {
                this.op = 0;
              });
            }
          }, () => {
            this.markX = 0;
          });
        });
      if (this.op !== 0) {
        Text(this.message)
          .fontSize(30)
          .fontWeight(FontWeight.Bold)
          .backgroundColor(Color.Pink)
          .borderRadius(3)
          .markAnchor({ x: this.markX })
          .position({ x: 0 })
          .opacity(this.op);
      }
    }
    .width('100%')
    .height('100%');
  }
}
```

### 场景三：组件当前绑定了一个转场动画transitionEffect，能否在运行时动态切换为另一种转场动画

1. 自定义两种不同的transitionEffect转场效果。
2. 声明并初始化transitionEffect实例，通过transition接口将其应用到目标组件。
3. 在组件的动态添加或移除过程中，通过animation接口配置动画参数，从而为组件应用不同的转场动画效果。

```ts
import { curves } from '@kit.ArkUI';

@Entry
@Component
struct TransitionEffectDemo {
  @State isPresent: boolean = false;
  // 创建transitionEffect
  private effect1: TransitionEffect =
    // 创建默认透明度转场效果，并指定了springMotion(0.6, 0.8)曲线
    TransitionEffect.OPACITY.animation({
      curve: curves.springMotion(0.6, 0.8)
    })
      .combine(TransitionEffect.scale({
        x: 0,
        y: 0
      }))// 添加旋转转场效果，这里的动画参数会跟随上面带animation的TransitionEffect，也就是springMotion(0.6, 0.8)
      .combine(TransitionEffect.rotate({ angle: -90 }))// 添加平移转场效果，这里的动画参数使用指定的springMotion()
      .combine(TransitionEffect.translate({ y: 150 })
        .animation({ curve: curves.springMotion() }))// 添加move转场效果，这里的动画参数会跟随上面的TransitionEffect，也就是springMotion()
      .combine(TransitionEffect.move(TransitionEdge.START));
  private effect2: TransitionEffect =
    TransitionEffect.OPACITY.animation({
      curve: curves.springMotion(0.6, 0.8)
    })
      .combine(TransitionEffect.scale({
        x: 0,
        y: 0
      }))
      .combine(TransitionEffect.rotate({ angle: 90 }))
      .combine(TransitionEffect.translate({ y: 150 })
        .animation({ curve: curves.springMotion() }))
      .combine(TransitionEffect.move(TransitionEdge.END));
  effect: TransitionEffect | null = null;

  build() {
    Stack() {
      if (this.isPresent) {
        Column() {
          Text('ArkUI')
            .fontWeight(FontWeight.Bold)
            .fontSize(20)
            .fontColor(Color.White);
        }
        .justifyContent(FlexAlign.Center)
        .width(150)
        .height(150)
        .borderRadius(10)
        .backgroundColor(0xf56c6c)
        // 将转场效果通过transition接口设置到组件
        .transition(this.effect);
      }
      Column()
        .width(155)
        .height(155)
        .border({
          width: 5,
          radius: 10,
          color: Color.Black
        });
      // 触发转场
      Column({ space: 10 }) {
        Button('从左侧入场')
          .onClick(() => {
            this.effect = this.effect1;
            this.isPresent = !this.isPresent;
          });
        Button('从右侧入场')
          .onClick(() => {
            this.effect = this.effect2;
            this.isPresent = !this.isPresent;
          });
      }
      .margin({ top: 320 });
    }
    .width('100%')
    .height('60%');
  }
}
```
