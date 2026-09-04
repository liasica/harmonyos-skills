---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/pen-point-prediction
title: 接入报点预测
breadcrumb: 指南 > 系统 > 硬件 > Pen Kit（手写笔服务） > 手写功能开发 > 接入报点预测
category: harmonyos-guides
scraped_at: 2026-09-05T06:14:35+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:41783e49d4c76539d46cdd006a8a58dc37441193296d17bacc5e43ad2b803eed
---

接入报点预测功能，可以优化应用中手写效果的绘制跟手性，提升应用中手写笔书写场景的跟手体验。

## 场景介绍

在应用的自定义界面中，获取到界面的触摸事件，通过调用报点预测的接口，可以得到预测的下一个报点的位置信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c9/v3/aH1SWljKTBqfELxr8T2oTA/zh-cn_image_0000002712404612.png)

## 接口说明

| 类名 | 接口名 | 描述 |
| --- | --- | --- |
| [PointPredictor](../harmonyos-references/pen-pointpredictor.md) | [getPredictionPoint](../harmonyos-references/pen-pointpredictor.md#getpredictionpoint)(event: [TouchEvent](../harmonyos-references/ts-universal-events-touch.md#touchevent对象说明)): [TouchPoint](../harmonyos-references/ts-types.md#touchpoint11) | 获取预测点 |

## 开发步骤

1. 导入相关模块。获取当前界面的触摸事件信息，调用接口计算预测点信息。

   ```typescript
   @Entry
   @Component
   struct PointPredictorDemo {
     @State actualXCoordinate: number = 0;
     @State actualYCoordinate: number = 0;
     @State predictorXCoordinate: Dimension = 0;
     @State predictorYCoordinate: Dimension = 0;
     pointPredictor: PointPredictor = new PointPredictor();

     aboutToAppear() {
       console.info('getPredictionPoint aboutToAppear');
     }

     aboutToDisappear() {
       console.info('getPredictionPoint aboutToDisappear');
     }

     build() {
       Stack({ alignContent: Alignment.TopEnd }) {
         this.canvas(); // 画布
       }.height('100%').width('100%')
     }

     // 画布
     @Builder
     canvas() {
       Column() {
         Text('实际点坐标： X: ' + this.actualXCoordinate + ' Y: ' + this.actualYCoordinate).textAlign(TextAlign.Start)
         Text('预测点坐标： X: ' + this.predictorXCoordinate + ' Y: ' + this.predictorYCoordinate)
           .textAlign(TextAlign.Start)
       }.position({ x: 0, y: 0 })
       .alignItems(HorizontalAlign.Start)

       Stack()
         .width('100%')
         .height('100%')
         .onTouch((event: TouchEvent) => {
           switch (event.type) {
             case TouchType.Down: // 按下时，新建一条画图路径
               break;
             case TouchType.Move: // 使用预测算法进行预测,获得预测点
               let point = this.pointPredictor?.getPredictionPoint(event);
               this.actualXCoordinate = event.touches[0]?.x;
               this.actualYCoordinate = event.touches[0]?.y;
               this.predictorXCoordinate = point?.x;
               this.predictorYCoordinate = point?.y;
               console.info('pointPredictor 实际点坐标 x:' + event.touches[0]?.x + ' y:' + event.touches[0]?.y);
               console.info('pointPredictor 预测点坐标 x:' + point?.x + '  y:' + point?.y);
               break;
             case TouchType.Up:
               break;
           }
         })
     }
   }
   ```
