---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-346
title: 使用Canvas如何实现部分区域镂空的效果
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 使用Canvas如何实现部分区域镂空的效果
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:28+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:e20caf8d833572dd8f960264cf046ad363dc55433104145bc5c7443ecd355bc9
---

1. 利用[Canvas](../harmonyos-references/ts-components-canvas-canvas.md)绘制镂空圆形；
2. 使用Stack组件在需要透明展示的区域上叠加。

**参考代码**

```ts
@Entry
@Component
struct HollowOutWithCanvas {
  @State circleCenterX: number = 0;
  @State circleCenterY: number = 0;
  @State circleRadius: number = 1000;
  private contextSettings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.contextSettings);

  build() {
    Row() {
      Column() {
        Stack() {
          Image($r('app.media.startIcon'))
            .height(300)
          // Use Canvas to draw masks to cover images, cameras, etc
          Canvas(this.context)
            .width('100%')
            .height('100%')
            .backgroundColor('#00000000')
            .onReady(() => {
              this.circleCenterX = this.context.width / 2;
              this.circleCenterY = this.context.height / 2;
              this.context.fillStyle = 'rgba(0,0,0,0.67)';
              if (this.circleRadius > this.circleCenterX) {
                this.circleRadius = this.circleCenterX / 2;
              }
              // Draw a circular path for semi transparent filling
              this.context.beginPath();
              this.context.moveTo(0, 0);
              this.context.lineTo(0, this.context.height);
              this.context.lineTo(this.context.width, this.context.height);
              this.context.lineTo(this.context.width, 0);
              this.context.lineTo(0, 0);
              this.context.arc(this.circleCenterX, this.circleCenterY, this.circleRadius, 0, Math.PI * 2);
              this.context.fill();
              this.context.closePath();
            })
        }
        .width('1456px')
        .height('1456px')
      }
      .width('100%')
    }
    .height('100%')
  }
}
```
