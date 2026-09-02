---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-535
title: 页面中的图片无法被放大
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 页面中的图片无法被放大
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:15+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:9108531ebd4f5975dd99ca3868550545dcc2992eb8aa9135e4bf3de0eb4416fc
---

## 问题现象

页面中图片无法通过点击或手势放大查看。

## 背景知识

* [matrix4](../harmonyos-references/js-apis-matrix4.md)：提供矩阵变换功能，支持对图形进行平移、旋转和缩放等。
* [transform](../harmonyos-references/ts-universal-attributes-transformation.md#transform)：可用于显示二维变换时的矩阵变换。当前仅支持Matrix4Transit矩阵对象类型。可以通过矩阵变换对图片进行平移、旋转、缩放等操作。
* [scale](../harmonyos-references/js-apis-matrix4.md#scale)：矩阵的缩放函数，可以为当前矩阵增加x轴/y轴/z轴缩放效果。会改变调用该函数的原始矩阵。
* [gesture](../harmonyos-guides/arkts-gesture-events-binding.md#gesture常规手势绑定方法)：为通用的一种手势绑定方法，可以将手势绑定到对应的组件上。
* [组合手势](../harmonyos-guides/arkts-gesture-events-combined-gestures.md)：组合手势由多种单一手势组合而成，通过在GestureGroup中使用不同的GestureMode来声明该组合手势的类型，支持[顺序识别](../harmonyos-guides/arkts-gesture-events-combined-gestures.md#顺序识别)、[并行识别](../harmonyos-guides/arkts-gesture-events-combined-gestures.md#并行识别)和[互斥识别](../harmonyos-guides/arkts-gesture-events-combined-gestures.md#互斥识别)三种类型。
* [Image](../harmonyos-references/ts-basic-components-image.md)：为图片组件，常用于在应用中显示图片。

## 问题定位

排查Image组件是否有使用transform属性并绑定手势对图片进行缩放操作。如果没有使用transform和matrix4矩阵，且没有配置gesture属性，则页面中图片无法通过点击或手势放大查看。

## 分析结论

没有使用transform属性通过matrix4矩阵对图片进行缩放操作，也没有绑定手势方法，导致无法点击放大或者通过手势放大图片。

## 修改建议

建议通过transform和matrix控制图片的放大。完整的图片预览缩放功能（包含手势捏合缩放等能力）可以参考[图片预览](https://gitee.com/harmonyos-cases/cases/tree/master/CommonAppDevelopment/feature/imageviewer)、[好友动态-图片预览](../architecture-guides/image_preview-0000002266277321.md)。

以下是简单的缩放功能的代码示例：

```screen
import { matrix4 } from '@kit.ArkUI';

@Entry
@Component
struct IndexMatrix {
  @State matrix: matrix4.Matrix4Transit = matrix4.identity().copy(); // 初始化矩阵对象并复制
  @State targetScale: number = 3;
  private lastScaleValue: number = 1; // 上次缩放的比例
  build() {
    Column() {
      Image($r('app.media.startIcon')) // 示例图片
        .width(100)
        .autoResize(false) // 设置图片解码过程中是否对图源自动缩放
        .transform(this.matrix) // 通过matrix控制图片的缩放
        .offset({
          // 上下偏移，避免超出屏幕，可以根据需要调整具体偏移的数值
          y: this.targetScale === 3 ? 100 : 200
        })
        .gesture(
          GestureGroup(
            GestureMode.Exclusive, // 互斥识别，仅识别一种手势
            TapGesture({ count: 1 }).onAction(() => {
              this.lastScaleValue = this.targetScale; // 记录缩放比例
              // 构造缩放矩阵，在原始比例和放大3倍之间切换
              this.matrix = matrix4.identity().scale({
                x: this.targetScale,
                y: this.targetScale
              });
              // 固定缩放比例在1、3之间切换，可以根据需要自行调整
              this.targetScale = this.targetScale === 3 ? 1 : 3;
            }),
            // 双指缩放
            PinchGesture({ fingers: 2, distance: 1 })
              .onActionUpdate((event: GestureEvent) => {
                // 根据双指缩放的事件调整matrix4矩阵的缩放比例
                this.matrix = matrix4.identity().scale({
                  x: this.lastScaleValue * event.scale,
                  y: this.lastScaleValue * event.scale
                }).copy();
              })
          )
        )
    }
    .height('100%')
    .width('100%')
    .padding({ top: 50 })
  }
}
```
