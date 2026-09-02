---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1181
title: 如何实现图片平滑切换动画效果
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 如何实现图片平滑切换动画效果
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:25+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:a3cd743f974216efbbf7fe256a39b56ba6d9b753bbee299f659f43b2cddffd25
---

## 问题现象

在开发过程中需要实现一些动画效果使应用界面自然过渡，从而增强用户从界面获得的反馈感和互动感。如何实现点击图片时产生从上往下滑动的动画效果？

## 背景知识

* [属性动画 (animation)](../harmonyos-references/ts-animatorproperty.md)：组件的某些通用属性变化时，可以通过属性动画实现渐变过渡效果，提升用户体验。
* [rotate](../harmonyos-references/ts-universal-attributes-transformation.md#rotate)：是HarmonyOS提供的一种通用属性，可用于设置组件的旋转。
* [translate](../harmonyos-references/ts-universal-attributes-transformation.md#translate)：可用于设置组件平移，使得组件在以组件左上角为坐标原点的坐标系中进行移动。

## 解决方案

1. 添加boolean型状态变量flag，并为组件添加translate属性，当flag的值为true时，将y设置为400；为false则设置为0。
2. 为Image添加onClick方法，在该方法中使用getUIContext获取页面的UIContext，再使用animateTo方法实现组件的动画效果。

完整示例参考如下：

```ts
@Entry
@Component
struct TranslateIndex {
  @State flag: boolean = false;

  build() {
    Column() {
      Image($r('app.media.startIcon')) // 根据场景需要添加图片
        .width('50%')
        .height('50%')
        .objectFit(ImageFit.Auto)
        .onClick(() => {
          this.getUIContext()?.animateTo({
            duration: 1000,
            curve: Curve.EaseOut,
            playMode: PlayMode.Normal,
          }, () => {
            this.flag = true;
          });
        });
    }
    .width('80%')
    .translate({ y: this.flag ? 400 : 0 })
    .height('100%')
    .width('100%');
  }
}
```
