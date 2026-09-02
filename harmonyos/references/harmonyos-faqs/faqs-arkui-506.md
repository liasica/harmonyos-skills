---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-506
title: 如何实现Matrix2D图形在画布中心点放大并旋转角度
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 如何实现Matrix2D图形在画布中心点放大并旋转角度
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:16+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:e3c73193c0299b30d6f71a0091aa2651c0f02fb762fa2af213e125ea7c5a312b
---

## 问题现象

如何在画布中心点实现Matrix2D图形指定倍数的放大和指定角度的旋转？

## 背景知识

* [Matrix2D](../harmonyos-references/ts-components-canvas-matrix2d.md)组件的方法[rotate](../harmonyos-references/ts-components-canvas-matrix2d.md#rotate10)，能够以旋转点为中心、对当前矩阵进行右乘旋转运算，调用公式为：rotate(degree: number, rx?: number, ry?: number)，其中degree为旋转角度，rx和ry为旋转中心点相对[0,0]点的水平和垂直方向坐标，如果[0,0]点通过translate发生移动，则以新的点计算相对的rx和ry值。
* [translate](../harmonyos-references/ts-components-canvas-matrix2d.md#translate)方法能够对当前矩阵进行左乘平移运算，调用公式为：translate(tx?: number, ty?: number)。
* [scale](../harmonyos-references/ts-components-canvas-matrix2d.md#scale)方法能够对当前矩阵进行右乘缩放运算，调用公式为：scale(sx?: number, sy?: number)，其中sx和sy为水平和垂直缩放比例系数。以[0,0]为基准进行缩放，如果[0,0]点通过translate发生移动，则以移动后的点为基准点进行缩放。

## 解决方案

1. 使用[Flex布局](../harmonyos-references/ts-universal-attributes-flex-layout.md)将[Canvas](../harmonyos-references/ts-components-canvas-canvas.md)组件居中显示，创建矩形。
2. 使用rotate方法对矩阵进行旋转操作，旋转角度由angle决定，旋转中心为矩形的中心；使用scale方法对矩阵进行缩放操作，缩放倍数由scaleTimesX和scaleTimesY决定，以中心点为基准进行缩放。rotate和scale存在调用顺序，遵循就近原则，因此需要将scale方法的使用放在rotate上方。
3. 使用translate方法对矩阵进行平移操作，将画布的原点移动到画布的中心，即可将图形移动至画布中心。将经过变换的矩阵应用到[CanvasRenderingContext2D](../harmonyos-references/ts-canvasrenderingcontext2d.md)对象上。
4. 用[fillRect()](../harmonyos-references/js-lite-components-canvas-canvasrenderingcontext2d.md#fillrect)方法在画布上绘制矩形。

完整示例参考如下：

```ts
@Entry
@Component
struct MatrixChange {
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  private matrix: Matrix2D = new Matrix2D();
  x: number = 50; // 图形大小
  y: number = 50; // 图形大小
  canvasWidth: number = 200; // 画布大小
  canvasHeight: number = 200; // 画布大小
  scaleTimesX: number = 2; // 缩放设置
  scaleTimesY: number = 2; // 缩放设置
  angle: number = -30; // 旋转角度

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width(this.canvasWidth)
        .height(this.canvasHeight)
        .backgroundColor('#0D5AF5')
        .onReady(() => {
          this.matrix.scaleX = 1;
          this.matrix.scaleY = 1;
          this.matrix.scale(this.scaleTimesX, this.scaleTimesY);
          this.matrix.rotate(this.angle * Math.PI / 180, this.x / 2, this.y / 2);
          this.matrix.translate(this.canvasWidth / 2, this.canvasHeight / 2);
          this.matrix.translate(-this.x * this.scaleTimesX / 2, -this.y * this.scaleTimesY / 2);
          this.context.setTransform(this.matrix);
          this.context.fillRect(0, 0, this.x, this.y);
        });
    }
    .width('100%')
    .height('100%');
  }
}
```

## 总结

Matrix2D图形能够在画布中心点放大指定倍数并旋转指定角度，该功能适用于需要展示图形并对其进行各种变换的场景，例如数据可视化、图形编辑器等。
