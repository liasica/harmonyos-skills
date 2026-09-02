---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1003
title: 如何让半透明颜色绘制时不进行叠加
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 如何让半透明颜色绘制时不进行叠加
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:25+08:00
doc_updated_at: 2026-08-13
content_hash: sha256:f7510685807a8018597551d27490055c1b130543a2ede64143160c718aadb375
---

## 问题现象

使用CanvasRenderingContext2D.stroke绘制path时，重合的半透明笔迹会叠加。如何实现颜色不叠加效果？颜色叠加代码如下：

```ts
@Entry
@Component
struct Page {
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);

  build() {
    Column() {
      Canvas(this.context)
        .onReady(() => {
          this.context.lineWidth = 40;
          this.context.strokeStyle = '#5164fff0';
          this.context.moveTo(80, 20);
          this.context.lineTo(80, 220);
          this.context.stroke();
          this.context.beginPath();
          this.context.moveTo(20, 80);
          this.context.lineTo(220, 80);
          this.context.stroke();
          this.context.beginPath();
          this.context.moveTo(160, 20);
          this.context.lineTo(160, 220);
          this.context.stroke();
          this.context.beginPath();
          this.context.moveTo(20, 160);
          this.context.lineTo(220, 160);
          this.context.stroke();
        });
    }
    .height('100%')
    .width('100%');
  }
}
```

问题效果预览：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/41/v3/PuYdK0YVTryPktXmkos0VQ/zh-cn_image_0000002628404770.png "点击放大")

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a9/v3/jfSLhmjCRGCUKh2s1QcErA/zh-cn_image_0000002628564676.png "点击放大")

## 背景知识

* [CanvasRenderingContext2D](../harmonyos-references/ts-canvasrenderingcontext2d.md)对象实例可在[Canvas](../harmonyos-references/ts-components-canvas-canvas.md)画布组件上进行绘制，绘制对象可以是图形、文本、线段、图片等。
* CanvasRenderingContext2D对象中有[stroke](../atomic-ascf/apis-canvas-rendering-context-2d.md#canvasrenderingcontext2dstroke)方法，可以根据当前的路径，进行边框绘制操作。

## 解决方案

在绘制过程中如果让多个路径分别绘制，会让绘制出的图案颜色多次覆盖。如果是绘制用的颜色为半透明，颜色会进行叠加直到不透明。如果想让绘制的颜色不叠加有以下两种方式。

* **方案一**：在同一个路径中绘制，颜色不叠加。

  ```ts
  @Entry
  @Component
  struct Page {
    private settings: RenderingContextSettings = new RenderingContextSettings(true);
    private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);

    build() {
      Column() {
        Canvas(this.context)
          .onReady(() => {
            this.context.lineWidth = 40;
            this.context.strokeStyle = '#5164fff0';
            this.context.moveTo(80, 20);
            this.context.lineTo(80, 220);
            this.context.moveTo(20, 80);
            this.context.lineTo(220, 80);
            this.context.moveTo(160, 20);
            this.context.lineTo(160, 220);
            this.context.moveTo(20, 160);
            this.context.lineTo(220, 160);
            this.context.stroke();
          });
      }
      .height('100%')
      .width('100%');
    }
  }
  ```
* **方案二**：在绘制第二段路径时，先设置[globalCompositeOperation](../harmonyos-references/ts-components-canvas-common-property.md#globalcompositeoperation)属性为destination-out进行绘制，去除新路径上原有的颜色。再改回source-over绘制。

  ```ts
  @Entry
  @Component
  struct Page2 {
    private settings: RenderingContextSettings = new RenderingContextSettings(true);
    private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);

    build() {
      Column() {
        Canvas(this.context)
          .onReady(() => {
            // 第一段，左边的垂直向下路径
            this.context.lineWidth = 40;
            this.context.strokeStyle = '#5164fff0';
            this.context.moveTo(80, 20);
            this.context.lineTo(80, 220);
            this.context.stroke();
            // 第二段，上面的水平向右路径
            this.context.beginPath();
            this.context.moveTo(20, 80);
            this.context.lineTo(220, 80);
            this.context.globalCompositeOperation = 'destination-out';
            this.context.strokeStyle = '#ff000000';
            this.context.stroke(); // 去除路径上原有的颜色
            this.context.globalCompositeOperation = 'source-over';
            this.context.strokeStyle = '#5164fff0';
            this.context.stroke(); // 绘制路径
            // 第三段，左边的垂直向下路径
            this.context.beginPath();
            this.context.moveTo(160, 20);
            this.context.lineTo(160, 220);
            this.context.globalCompositeOperation = 'destination-out';
            this.context.strokeStyle = '#ff000000';
            this.context.stroke(); // 去除路径上原有的颜色
            this.context.globalCompositeOperation = 'source-over';
            this.context.strokeStyle = '#5164fff0';
            this.context.stroke(); // 绘制路径
            // 第四段，下面的水平向右路径
            this.context.beginPath();
            this.context.moveTo(20, 160);
            this.context.lineTo(220, 160);
            this.context.globalCompositeOperation = 'destination-out';
            this.context.strokeStyle = '#ff000000';
            this.context.stroke(); // 去除路径上原有的颜色
            this.context.globalCompositeOperation = 'source-over';
            this.context.strokeStyle = '#5164fff0';
            this.context.stroke(); // 绘制路径
          });
      }
      .height('100%')
      .width('100%');
    }
  }
  ```
