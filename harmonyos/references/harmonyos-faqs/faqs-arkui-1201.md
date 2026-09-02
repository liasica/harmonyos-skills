---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1201
title: 使用放大和缩小动画效果的场景
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 使用放大和缩小动画效果的场景
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:27+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:d5418ae94da00401ae6f4bf6dcabec1ad125b2d761e489aec8bc2463980c494b
---

## 问题现象

开发者在使用放大和缩小动画效果时，可能会遇到以下几种典型场景：

* 场景一：如何实现类似呼吸灯效果的动态缩放动画？
* 场景二：如何实现直播头像的缩放动画，并在头像周围叠加具有动态变化的缩放圆环？
* 场景三：如何实现点击组件时，触发动态的宽度拉伸与收缩动画效果？

## 背景知识

* [关键帧动画 (keyframeAnimateTo)](../harmonyos-references/ts-keyframeanimateto.md)：指定若干个关键帧状态，实现分段的动画。
* [显式动画 (animateTo)](../harmonyos-references/ts-explicit-animation.md)：提供全局animateTo显式动画接口来指定由于闭包代码导致的状态变化插入过渡动效。
* [属性动画 (animation)](../harmonyos-references/ts-animatorproperty.md)：组件的某些通用属性变化时，可以通过属性动画实现渐变过渡效果，提升用户体验。支持的属性包括width、height、backgroundColor、opacity、scale等。

## 解决方案

* 场景一：如何实现类似呼吸灯效果的动态缩放动画？
  1. 可通过关键帧动画，在特定时间段内动态修改组件的[scale](../harmonyos-references/ts-universal-attributes-transformation.md#scale)属性，实现有规律的缩放，从而呈现出类似呼吸灯的动画效果。
  2. 通过调整[brightness](../harmonyos-references/ts-universal-attributes-image-effect.md#brightness)属性，可以为组件添加高光效果，进一步增强其视觉层次感。

  ```ts
  import { UIContext } from '@kit.ArkUI';

  @Entry
  @Component
  struct KeyframeDemo {
    @State myScale: number = 1.0;
    @State brightNess: number = 1;
    uiContext: UIContext | undefined = undefined;

    aboutToAppear() {
      this.uiContext = this.getUIContext?.();
    }

    build() {
      Column() {
        Circle()
          .width(100)
          .height(100)
          .fill('#46B1E3')
          .margin(100)
          .brightness(this.brightNess)
          .scale({ x: this.myScale, y: this.myScale })
          .onClick(() => {
            if (!this.uiContext) {
              return;
            }
            this.myScale = 1;
            // 设置关键帧动画整体播放3次
            this.uiContext.keyframeAnimateTo({ iterations: 3 }, [
              {
                // 第一段关键帧动画时长为800ms，scale属性做从1到1.5的动画
                duration: 800,
                event: () => {
                  this.myScale = 1.5;
                  this.brightNess = 1.3;
                }
              },
              {
                // 第二段关键帧动画时长为500ms，scale属性做从1.5到1的动画
                duration: 500,
                event: () => {
                  this.myScale = 1;
                  this.brightNess = 1;
                }
              }
            ]);
          });
      }.width('100%').margin({ top: 5 });
    }
  }
  ```
* 场景二：如何实现直播头像的缩放动画，并在头像周围叠加具有动态变化的缩放圆环？
  1. 通过animateTo实现了一个圆环的循环缩放动画，利用[scale](../harmonyos-references/ts-universal-attributes-transformation.md#scale)属性在指定时间内完成放大与缩小的循环操作。
  2. 通过将[iterations](../harmonyos-references/js-apis-animator.md#iterations18)设置为-1，并配合[playMode](../harmonyos-references/ts-appendix-enums.md#playmode)：PlayMode.Alternate，实现了动画在正向与反向之间交替循环播放的效果。
  3. 结合[curve](../harmonyos-references/ts-appendix-enums.md#curve)：Curve.EaseInOut，为动画赋予了自然流畅的加速与减速效果，整体呈现出动态变化的缩放圆环效果。

  ```ts
  @Entry
  @Component
  struct RingAnimationExample {
    @State scaleValue: number = 1;

    startAnimation() {
      this.getUIContext().animateTo({
        duration: 1000,
        iterations: -1,
        playMode: PlayMode.Alternate,
        curve: Curve.EaseInOut
      }, () => {
        this.scaleValue = 1.2; // 仅作用于圆环
      });
    }

    build() {
      Column() {
        Stack() {
          // 此处仅为示例，请开发者自行替换为可用图片
          Image($r('app.media.startIcon'))
            .width(100)
            .height(100)
            .border({
              width: 4,
              color: Color.Red,
              radius: '100%'
            });
          // 独立圆环组件
          Stack()
            .width(150)
            .height(150)
            .scale({ x: this.scaleValue, y: this.scaleValue }) // 仅缩放圆环
            .border({
              width: 2,
              color: Color.Pink,
              radius: '100%'
            });
        };

        Text('直播中')
          .width(150)
          .height(50)
          .fontColor(Color.White)
          .fontWeight(600)
          .fontSize(26)
          .textAlign(TextAlign.Center)
          .backgroundColor(Color.Red)
          .border({
            width: 1,
            color: Color.Red,
            radius: '100%'
          })
          .margin({ top: -20 });

        Button('点击播放').onClick(() => {
          this.startAnimation();
        })
          .margin({ top: 30 });
      }
      .width('100%')
      .height('100%')
      .justifyContent(FlexAlign.Center)
      .alignItems(HorizontalAlign.Center);
    }
  }
  ```
* 场景三：如何实现点击组件时，触发动态的宽度拉伸与收缩动画效果？
  + 方案一：通过animation属性配置动画参数对象。该方式通过在组件上设置animation属性，传入包含动画参数（如duration、curve等）的对象，实现属性动画效果。

    ```ts
    @Entry
    @Component
    struct AnimationComponentPage0 {
      @State widthSize: number | string = '100%';

      build() {
        Column() {
          Column()
            .width(this.widthSize)
            .height(300)
            .backgroundColor(Color.Orange)
            .animation({
              duration: 2000,
              curve: Curve.EaseOut,
              iterations: 1,
              playMode: PlayMode.Normal
            })
            .onClick(() => {
              this.widthSize = this.widthSize === 44 ? '100%' : 44;
            });
        }
        .width('100%')
        .margin({ top: 20 })
        .alignItems(HorizontalAlign.Start);
      }
    }
    ```
  + 方案二：通过animateTo接口传入动画参数对象。该方式通过调用全局animateTo方法，传入目标值和动画配置对象，实现动画过渡效果。

    ```ts
    @Entry
    @Component
    struct AnimationComponentPage1 {
      @State widthSize: number | string = '100%';

      build() {
        Column() {
          Column()
            .width(this.widthSize)
            .height(300)
            .backgroundColor(Color.Orange)
            .onClick(() => {
              this.getUIContext()?.animateTo({
                duration: 2000,
                curve: Curve.EaseOut,
                iterations: 1,
                playMode: PlayMode.Normal
              }, () => {
                this.widthSize = this.widthSize === 44 ? '100%' : 44;
              });
            });
        }
        .width('100%')
        .margin({ top: 20 })
        .alignItems(HorizontalAlign.Start);
      }
    }
    ```

  两种方案对比：

  | 方案 | 优缺点 | 适用场景 |
  | --- | --- | --- |
  | 方案一：属性动画 (animation) | 简洁高效，直接绑定目标属性（如按钮点击后的颜色/大小变化）。仅修饰单一组件的特定属性，无法直接串联多个动画。 | 单组件属性渐变。 |
  | 方案二：显式动画 (animateTo) | 闭包内状态变化可同时驱动多个组件的属性动画。通过闭包函数批量触发多属性动画，可嵌套调用实现复杂动画序列。 | 多个组件联动动画，复杂动画序列。 |
