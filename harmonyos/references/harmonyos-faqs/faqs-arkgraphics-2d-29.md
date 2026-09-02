---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkgraphics-2d-29
title: Canvas实现六边形雷达图
breadcrumb: FAQ > 图形开发 > 2D图形（ArkGraphics 2D） > Canvas实现六边形雷达图
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:46+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:11250666370455e86e978a274df130812e6eba358ae019644f4772e70fdd7816
---

## 问题现象

如何基于Canvas实现六边形雷达图以展示不同能力的数据？

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ae/v3/w4hzU0C5S7yXAbsKNjFTKw/zh-cn_image_0000002628393358.png "点击放大")

## 背景知识

* [Canvas](../harmonyos-references/ts-components-canvas-canvas.md)组件用于自定义绘制图形，[onReady](../harmonyos-references/ts-components-canvas-canvas.md#onready)事件之后可使用Canvas相关API进行绘制。
* [CanvasRenderingContext2D](../harmonyos-references/ts-canvasrenderingcontext2d.md)可在Canvas组件上进行绘制，绘制对象可以是矩形、文本、图片等。
* [Path2D](../harmonyos-references/ts-components-canvas-path2d.md)支持通过对象的接口进行路径的描述，并通过Canvas的stroke接口或者fill接口进行绘制。

## 解决方案

1. 根据画布的中心点以及雷达图的半径，计算雷达图各点对应的坐标，并将这些坐标点存入positionList中。利用Path2D对象的moveTo方法和lineTo方法绘制折线图，并通过closePath方法闭合路径，最后使用stroke方法绘制边框。整个过程需绘制五个具有不同半径的六边形：

   ```ts
   for (let index = 0; index < 6; index++) {
     this.baseRadius = 150 - (index * 30);
     const firstX = this.baseRadius * Math.sin(0) + this.canvasRadius;
     const firstY = this.baseRadius * Math.cos(0) + this.canvasRadius;
     if (index === 0) {
       let firstModel = new PositionModel(firstX, firstY);
       this.positionList.push(firstModel);
     }
     this.path2Db.moveTo(firstX, firstY);
     for (let i = 1; i < 6; i++) {
       const angle = i * this.angleOffset;
       const x = this.baseRadius * Math.sin(angle) + this.canvasRadius;
       const y = this.baseRadius * Math.cos(angle) + this.canvasRadius;
       this.path2Db.lineTo(x, y);
       if (index === 0) {
         let model = new PositionModel(x, y);
         this.positionList.push(model);
       }
     }
     this.path2Db.closePath();
     this.context.stroke(this.path2Db);
   }
   ```
2. 将绘制能力对应的名字，positionList存储的坐标点，来调整各点文本对应的绘制位置，使用CanvasRenderingContext的font设置文字大小，通过fillStyle设置文字颜色，通过font设置文字大小，再根据fillText，传入展示的文本和起始坐标点来绘制文字：

   ```ts
   this.context.font = '50px sans-serif';
   this.context.fillStyle = '#333333';
   for (let i = 0; i < this.positionList.length; i++) {
     let model = this.positionList[i];
     let name = this.nameList[i];
     if (i === 0) {
       model.positionX -= 15;
       model.positionY += 20;
     } else if (i === 1 || i === 2) {
       model.positionX += 10;
       model.positionY += 5;
     } else if (i === 3) {
       model.positionX -= 15;
       model.positionY -= 8;
     } else if (i === 4 || i === 5) {
       model.positionX -= 40;
       model.positionY += 5;
     }
     this.context.fillText(name, model.positionX, model.positionY);
   }
   ```
3. 根据给定的能力值数组rateArray，以画布中心点为基准，结合雷达图的半径，利用Math.sin(angle)和Math.cos(angle)计算各点坐标。通过Path2D的moveTo和lineTo方法绘制折线，并用closePath闭合路径：

   ```ts
   for (let index = 0; index < this.rateArray.length; index++) {
     if (index === 0) {
       let tempRadius: number = this.rateArray[index] * 125 + 25;
       this.ratePath2Db.moveTo(tempRadius * Math.sin(0) + this.canvasRadius,
         tempRadius * Math.cos(0) + this.canvasRadius);
     } else {
       let tempRadius: number = this.rateArray[index] * 125 + 25;
       const angle = index * this.angleOffset;
       const x = tempRadius * Math.sin(angle) + this.canvasRadius;
       const y = tempRadius * Math.cos(angle) + this.canvasRadius;
       this.ratePath2Db.lineTo(x, y);
     }
   }
   this.ratePath2Db.closePath();
   this.context.stroke(this.ratePath2Db);
   this.context.fillStyle = '#00ff00';
   this.context.globalAlpha = 0.4;
   this.context.fill(this.ratePath2Db, 'evenodd');
   ```

完整示例参考如下：

```ts
@Entry
@Component
struct RadarChartPage {
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  // 背景
  private path2Db: Path2D = new Path2D();
  // 能力值展示
  private ratePath2Db: Path2D = new Path2D();
  // 计算正六边形的顶点坐标
  private baseRadius: number = 150;
  // 画布半径
  private canvasRadius: number = 200;
  private angleOffset: number = (Math.PI * 2) / 6;
  // 圈数
  private count: number = 5;
  // 各能力值
  private rateArray: number[] = [0.5, 1.0, 0.15, 0.7, 0.4, 0.65];
  // 各能力名称
  private nameList: string[] = ['推进', '战绩', '生存', '团战', '发育', '输出'];
  // 各能力对应的坐标点
  private positionList: PositionModel[] = [];

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('400')
        .height('400')
        .backgroundColor(Color.White)
        .onReady(() => {
          // 绘制背景
          for (let index = 0; index < 6; index++) {
            this.baseRadius = 150 - (index * 30);
            const firstX = this.baseRadius * Math.sin(0) + this.canvasRadius;
            const firstY = this.baseRadius * Math.cos(0) + this.canvasRadius;
            if (index === 0) {
              let firstModel = new PositionModel(firstX, firstY);
              this.positionList.push(firstModel);
            }
            this.path2Db.moveTo(firstX, firstY);
            for (let i = 1; i < 6; i++) {
              const angle = i * this.angleOffset;
              const x = this.baseRadius * Math.sin(angle) + this.canvasRadius;
              const y = this.baseRadius * Math.cos(angle) + this.canvasRadius;
              this.path2Db.lineTo(x, y);
              if (index === 0) {
                let model = new PositionModel(x, y);
                this.positionList.push(model);
              }
            }
            this.path2Db.closePath();
            this.context.stroke(this.path2Db);
          }
          // 绘制能力值对应的路径
          for (let index = 0; index < this.rateArray.length; index++) {
            if (index === 0) {
              let tempRadius: number = this.rateArray[index] * 125 + 25;
              this.ratePath2Db.moveTo(tempRadius * Math.sin(0) + this.canvasRadius,
                tempRadius * Math.cos(0) + this.canvasRadius);
            } else {
              let tempRadius: number = this.rateArray[index] * 125 + 25;
              const angle = index * this.angleOffset;
              const x = tempRadius * Math.sin(angle) + this.canvasRadius;
              const y = tempRadius * Math.cos(angle) + this.canvasRadius;
              this.ratePath2Db.lineTo(x, y);
            }
          }
          this.ratePath2Db.closePath();
          this.context.stroke(this.ratePath2Db);
          this.context.fillStyle = '#00ff00';
          this.context.globalAlpha = 0.4;
          this.context.fill(this.ratePath2Db, 'evenodd');
          // 绘制各坐标对应的名称
          this.context.font = '50px sans-serif';
          this.context.fillStyle = '#333333';
          for (let i = 0; i < this.positionList.length; i++) {
            let model = this.positionList[i];
            let name = this.nameList[i];
            if (i === 0) {
              model.positionX -= 15;
              model.positionY += 20;
            } else if (i === 1 || i === 2) {
              model.positionX += 10;
              model.positionY += 5;
            } else if (i === 3) {
              model.positionX -= 15;
              model.positionY -= 8;
            } else if (i === 4 || i === 5) {
              model.positionX -= 40;
              model.positionY += 5;
            }
            this.context.fillText(name, model.positionX, model.positionY);
          }
        });
    }
    .width('100%')
    .height('100%');
  }
}

export class PositionModel {
  positionX: number = 0;
  positionY: number = 0;

  constructor(positionX: number, positionY: number) {
    this.positionX = positionX;
    this.positionY = positionY;
  }
}
```

## 总结

在需要对不同能力的数据进行更为直观展示与对比的场景中，可以利用Canvas组件进行自定义图形的绘制，从而实现上述雷达图的构建。
