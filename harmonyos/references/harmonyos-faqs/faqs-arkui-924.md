---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-924
title: 按钮设置渐变属性后如何设置按压效果
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 按钮设置渐变属性后如何设置按压效果
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:20+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:012ce9231702bf2b383040e1476739f78750cd18af2c49fe586405409626aeaa
---

## 问题现象

按钮设置了linearGradient渐变属性后，长按没有按压态显示效果，该如何设置呢？

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6d/v3/2BHu45BQQ1GMFjjY7KeKJw/zh-cn_image_0000002658919519.gif "点击放大")

## 背景知识

* 组件可通过设置[linearGradient](../harmonyos-references/ts-universal-attributes-gradient-color.md)属性设置组件的颜色渐变效果。
* [hdsEffect](../harmonyos-references/ui-design-hdseffect.md)：本模块提供组件的拓展视效能力，包括组件点光源效果、按压光效、动画控制。

## 解决方案

* **方案一**：参考[按压阴影](../harmonyos-guides/ui-design-visual-effect-background-color.md)实现。hdsEffect模块从6.0.0(20)Beta1版本开始，新增支持。
* **方案二**：设置颜色渐变后，长按按钮不会让渐变色变暗。需要识别长按事件[LongPressGesture](../harmonyos-references/ts-basic-gestures-longpressgesture.md)，在其中修改linearGradient参数。

  ```ts
  @Entry
  @Component
  struct GradientDemo {
    normalSet: Array<[ResourceColor, number]> = [[0xEBD7FF, 0.0], [0x0000ff, 0.3], [0x19CEFF, 1.0]];
    // 按压态渐变色，可以根据需求调配颜色
    pressedSet: Array<[ResourceColor, number]> = [[0x92859E, 0.0], [0x0000AA, 0.3], [0x1084A3, 1.0]];
    @State bgColorSet: Array<[ResourceColor, number]> = this.normalSet;

    build() {
      Column() {
        Button('test', { type: ButtonType.Capsule})
          .width(200)
          .height(50)
          .backgroundColor(Color.Transparent) // 设置渐变色
          .linearGradient({
            angle: 90,
            colors: this.bgColorSet
          })
          .gesture(GestureGroup(GestureMode.Parallel,
            // 触发长按的最短时间为1ms，duration小于等于0时，按照默认值500ms处理
            LongPressGesture({ duration: 1 })
              .onAction(() => {
                this.bgColorSet = this.pressedSet;
              })
              .onActionEnd(() => {
                this.bgColorSet = this.normalSet;
              })
              .tag('long press')
          ));
        Button('test', { type: ButtonType.Capsule})
          .width(200)
          .height(50)
          .margin({ top: 50})
      }
      .width('100%')
      .height('100%')
      .justifyContent(FlexAlign.Center)
      .alignItems(HorizontalAlign.Center)
    }
  }
  ```

## 总结

只使用backgroundColor修改按钮背景，支持按压态，将背景变灰。但如果使用linearGradient、backgroundImage等属性修改背景，则渐变色、背景图部分不会自动变灰，需要开发者自行实现。

修改opacity有类似的效果，对于上述按钮，调低会使按钮变白，不能满足要求。
