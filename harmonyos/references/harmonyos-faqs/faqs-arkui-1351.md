---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1351
title: 组件旋转动效实现
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 组件旋转动效实现
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:17+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:7f0d0e302e4bbed4815d65e2af21fed7cddd8b3d561ba985db8a08a16f3f582c
---

## 问题现象

如何实现组件的旋转动态效果？

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/60/v3/3_umIvT2TSGYdghtsZTuhQ/zh-cn_image_0000002658960739.png "点击放大")

## 背景知识

* [Circle](../harmonyos-references/ts-drawing-components-circle.md)是HarmonyOS提供的可用于绘制圆形的组件，其[stroke](../harmonyos-references/ts-drawing-components-circle.md#stroke)属性用于设置边框颜色。
* [Rect](../harmonyos-references/ts-drawing-components-rect.md)是一种矩形绘制组件。
* [rotate](../harmonyos-references/ts-universal-attributes-transformation.md#rotate)是用于控制图形变换的通用属性。
* [opacity](../harmonyos-references/ts-universal-attributes-opacity.md#opacity)用于设置组件的不透明度。
* [animateTo](../harmonyos-references/arkts-apis-uicontext-uicontext.md#animateto)提供全局animateTo显式动画接口来指定由于闭包代码导致的状态变化插入过渡动效。

## 解决方案

1. 在Stack中定义Circle组件，它的stroke属性的值用boolean类型的recording变量来控制，recording的值为true时，将边框设置为白色，为false时设置为宇宙蓝。
2. 在Stack中继续创建两个矩形组件，分别设置不同的填充颜色及宽高，其中一个矩形的opacity值设置为opacityValue，另一个值设为1-opacityValue。
3. 为组件创建onClick方法，在点击后对recording进行取反，在animateTo方法中将动画曲线设置为curve，并根据recording值的真假对角度、透明度、缩放比例进行修改，以实现两种矩形组件的过渡效果。

```ts
@Entry
@Component
struct Riders {
  @State recording: boolean = false;
  @State angleSize: number = 0;
  @State opacityValue: number = 1;
  @State scaleSize: number = 1;

  build() {
    Column() {
      Button() {
        Stack({ alignContent: Alignment.Center }) {
          // 外环（动态颜色）
          Circle()
            .width(70)
            .height(70)
            .stroke(this.recording ? '#fff' : '#0A59F7')
            .strokeWidth(1.5)
            .fill(Color.Transparent);

          // 内矩形（动态切换）
          Rect()
            .width(48)
            .height(48)
            .radius(16)
            .fill('#fff')
            .rotate({ z: 1, angle: this.angleSize })
            .opacity(1 - this.opacityValue);

          Rect()
            .width(58)
            .height(58)
            .radius(29)
            .fill('#0A59F7')
            .rotate({ z: 1, angle: this.angleSize })
            .scale({ x: this.scaleSize, y: this.scaleSize })
            .opacity(this.opacityValue);
        }
        .width('100%')
        .height('100%');
      }
      .width(50)
      .height(50)
      .backgroundColor(Color.Transparent)
      .onClick(() => {
        this.recording = !this.recording;
        this.getUIContext().animateTo({
          duration: 1000,
          curve: Curve.Linear
        }, () => {
          if (this.recording) {
            this.opacityValue = 0;
            this.angleSize = 90;
            this.scaleSize = 0.5;
          } else {
            this.opacityValue = 1;
            this.angleSize = 0;
            this.scaleSize = 1;
          }
        });
      });
    }
    .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.TOP, SafeAreaEdge.BOTTOM])
    .width('100%')
    .height('100%')
    .backgroundColor('#f1f3f5')
    .justifyContent(FlexAlign.Center)
    .alignItems(HorizontalAlign.Center);
  }
}
```

## 总结

该解决方案的核心在于两个Rect组件opacity属性的值共享同一个opacityValue变量，一个值设置为opacityValue，另一个设置为1-opacityValue，以实现平滑的组件动态旋转过程。
