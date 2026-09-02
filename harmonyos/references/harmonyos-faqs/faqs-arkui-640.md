---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-640
title: 修改被@State修饰的gesture属性参数不生效
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 修改被@State修饰的gesture属性参数不生效
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:02+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:0358c72e33906d62d7bdf222c6e31f319df256788e8a933ca8ed7a0d3958cb24
---

## 问题现象

对手势属性进行修改时，绑定手势gesture没有生效，如何解决该问题？

问题代码示例参考如下：

```screen
@Entry
@Component
struct PinchGesturePage {
  @State scaleValue: number = 1;
  private lastScale: number = 1;
  @State isGesture: boolean = false;

  build() {
    Stack() {
      Row()
        .width(200)
        .height(200)
        .margin({ top: 50 })
        .backgroundColor('#61CFBE')
        .scale(this.isGesture ? { x: this.scaleValue, y: this.scaleValue, z: 1 } : null)
        .gesture(this.isGesture ?
        PinchGesture({ fingers: 2 })
          .onActionStart(() => {
            // 在手势开始时，记录当前的缩放比例
            this.lastScale = this.scaleValue;
          })
          .onActionUpdate((event: GestureEvent | undefined) => {
            if (event) {
              // 计算新的缩放比例，将当前缩放比例乘以最后一次记录的缩放比例
              let newScale = this.lastScale * event.scale;
              // 进行边界检查
              if (newScale < 1) {
                newScale = 1;
              } else if (newScale > 5) {
                newScale = 5;
              }
              // 更新缩放值
              this.scaleValue = newScale;
            }
          })
          .onActionEnd(() => {
            // 手势结束时，不需要特殊处理
          }) : null
        );
      Row()
        .width(200)
        .height(200)
        .onClick(() => {
          this.isGesture = true;
          console.info(`TWT->onClick ${this.isGesture}`);
        })
        .hitTestBehavior(HitTestMode.Transparent)
        .backgroundColor('#5291FF');
    }
    .height('100%')
    .width('100%');
  }
}
```

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/SRfFAAEARqO1_x-q9mr1KA/zh-cn_image_0000002628554400.gif "点击放大")

## 背景知识

[自定义手势判定](../harmonyos-references/ts-gesture-customize-judge.md)为组件提供自定义手势判定能力。开发者可根据需要，在手势识别期间，决定是否响应手势。

## 问题定位

问题代码中通过this.isGesture的值判断是否执行手势事件。但参考[绑定手势方法](../harmonyos-references/ts-gesture-settings.md)的说明部分，gesture当前不支持使用三目运算符（条件? 表达式1 : 表达式2）切换手势绑定。

## 分析结论

gesture当前不支持使用三目运算符（条件? 表达式1 : 表达式2）切换手势绑定。但是可以通过[onGestureJudgeBegin](../harmonyos-references/ts-gesture-customize-judge.md#ongesturejudgebegin)来进行判断并决定是否识别手势。

## 解决方案

使用手势拦截onGestureJudgeBegin来判断是否识别手势。

```screen
@Entry
@Component
struct PinchGesturePage {
  @State scaleValue: number = 1;
  private lastScale: number = 1;
  @State isGesture: boolean = false;

  build() {
    Stack() {
      Row()
        .width(400)
        .height(400)
        .margin({ top: 50 })
        .backgroundColor('#61CFBE')
        .scale(this.isGesture ? { x: this.scaleValue, y: this.scaleValue, z: 1 } : null)
        .onGestureJudgeBegin(() => {
          if (this.isGesture) {
            return GestureJudgeResult.CONTINUE;
          } else {
            return GestureJudgeResult.REJECT;
          }
        })
        .gesture(PinchGesture({ fingers: 2 })
          .onActionStart(() => {
            // 在手势开始时，记录当前的缩放比例
            console.info(`The lastScale is ${this.lastScale}`);
            this.lastScale = this.scaleValue;
          })
          .onActionUpdate((event: GestureEvent | undefined) => {
            if (event) {
              // 计算新的缩放比例，将当前缩放比例乘以最后一次记录的缩放比例
              let newScale = this.lastScale * event.scale;
              // 进行边界检查
              if (newScale < 1) {
                newScale = 1;
              } else if (newScale > 5) {
                newScale = 5;
              }
              // 更新缩放值
              this.scaleValue = newScale;
              console.info(`The newScale is ${this.scaleValue}`);
            }
          })
          .onActionEnd(() => {
            // 手势结束时，不需要特殊处理
            console.info('The action is end');
          })
        );
      Row()
        .width(400)
        .height(400)
        .onClick(() => {
          this.isGesture = true;
          console.info(`TWT->onClick ${this.isGesture}`);
        })
        .hitTestBehavior(HitTestMode.Transparent)
        .backgroundColor('#5291FF');
    }
    .height('100%')
    .width('100%');
  }
}
```
