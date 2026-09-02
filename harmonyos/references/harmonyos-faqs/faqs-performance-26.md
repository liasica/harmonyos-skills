---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-performance-26
title: 文字翻转有延迟
breadcrumb: FAQ > 应用质量 > 技术质量 > 性能 > 文字翻转有延迟
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:51+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:fe5aac45bb8a7f554760a6b28804fb32341f10ca4f4a8faedfca97ff7e7561af
---

## 问题现象

文字翻转有延迟，如下图所示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ec/v3/bzz7p7xWTJ65Rkm74W5plg/zh-cn_image_0000002658914391.png "点击放大")

## 背景知识

* [animateTo](../harmonyos-references/arkts-apis-uicontext-uicontext.md#animateto)：显示动画接口，可用于实现属性动画比如改变宽高的动画、内容出现和消失的动效。
* [组件内转场 (transition)](../harmonyos-references/ts-transition-animation-component.md)：主要用于容器组件中的子组件插入和删除时增加过渡动效，可提升用户体验。

## 问题定位

* 根据问题现象可知，文字从上方翻转到下方后跳变回上方，推测应用设置组件执行旋转角度从0°变化到180°的动画，然后又将其旋转角度设置成0°，可在代码中搜索animateTo确认组件旋转动效的实现。
* 如下代码中可看到在点击按钮时有执行旋转动效，动效起始旋转角度设置为0，动效终止旋转角度设置为180或-180，动效执行完成后又将旋转角度设置成0，因此出现文字翻转有延迟的现象，属于动效实现问题。

```ts
@Entry
@Component
struct FlipDemoPage {
  @State flag: boolean = false;
  @State rotateAngle: number = 0;

  build() {
    Column() {
      Button('翻转')
        .onClick(() => {
          this.flag = !this.flag;
          this.rotateAngle = 0;
          this.getUIContext().animateTo({
            duration: 500,
            curve: Curve.EaseInOut,
            onFinish: () => {
              this.rotateAngle = 0;
            }
          }, () => {
            if (this.flag) {
              this.rotateAngle = 180;
            } else {
              this.rotateAngle = -180;
            }
          })
        })
        .margin(50)

      Stack() {
        if (this.flag) {
          Text('0000')
            .fontColor(Color.Blue)
        } else {
          Text('1111')
            .fontColor(Color.Blue)
        }
      }.rotate({
        x: 1,
        y: 0,
        z: 0,
        angle: this.rotateAngle
      })
    }
    .height('100%')
    .width('100%')
  }
}
```

## 分析结论

在执行旋转动效实现文字翻转效果时，将动效起始旋转角度设置为0，动效终止旋转角度设置为180或-180，动效执行完成后又将旋转角度设置成0，因此出现文字翻转有延迟的现象。

## 修改建议

使用[组件内转场 (transition)](../harmonyos-references/ts-transition-animation-component.md)来实现文字翻转动效，在文字显示和消失时增加过渡效果。

```ts
@Entry
@Component
struct FlipDemoPage {
  @State flag: boolean = false;

  build() {
    Column() {
      Button('翻转')
        .onClick(() => {
          this.flag = !this.flag;
        })
        .margin(50)

      Stack() {
        if (this.flag) {
          Text('0000')
            .fontColor(Color.Blue)
            .transition(TransitionEffect.OPACITY.animation({ duration: 500, curve: Curve.ExtremeDeceleration })
              .combine(TransitionEffect.rotate({ x: 1, angle: 180 })))
        } else  {
          Text('1111')
            .fontColor(Color.Blue)
            .transition(TransitionEffect.OPACITY.animation({ duration: 500, curve: Curve.ExtremeDeceleration })
              .combine(TransitionEffect.rotate({ x: 1, angle: 180 })))
        }
      }
    }
    .height('100%')
    .width('100%')
  }
}
```
