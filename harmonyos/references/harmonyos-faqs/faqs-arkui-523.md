---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-523
title: 如何判断用户的点击事件是否落在目标区域
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 如何判断用户的点击事件是否落在目标区域
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:23+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:8ed548d61e076434db466ad9eca5c84ec9367d698d677f2d7f00d901d3674170
---

## 问题现象

如下图，一个圆形区域被分为四个区域，如何判断用户点击在相应目标区域？

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ff/v3/4w1KikTvRqm2fclnfACI7Q/zh-cn_image_0000002658910377.png "点击放大")

## 背景知识

* [触摸事件](../harmonyos-references/ts-universal-events-touch.md)：手指在组件上按下、滑动或抬起时触发。
* [onTouch](../harmonyos-references/ts-universal-events-touch.md#ontouch)：手指触摸动作触发该回调。可以获取触摸行为的数据。

## 解决方案

通过触摸事件获得触点位置信息，计算落点所在区域，步骤如下：

1. 计算整个可点击范围的中心点。

   ```ts
   let centerX = Number(area.width) / 2;
   let centerY = Number(area.height) / 2;
   ```
2. 以中心点为原点设置坐标系，将整个可点击区域分为四个象限。根据触摸点和中心点，计算出触摸点在坐标系中的坐标，再根据坐标点在象限的上半部分还是下半部分判断出落点所在区域。

   ```ts
   // 判断触摸点在哪个象限
   if (touch.x - centerX < 0 && touch.y - centerY < 0) { // 触摸点在第2象限
     let xNum = centerX - touch.x;
     let yNum = centerY - touch.y;
     // 判断触摸点在上边还是左边
     if (xNum > yNum) {
       actionType = ActionType.left;
     } else {
       actionType = ActionType.top;
     }

   } else if (touch.x - centerX < 0 && touch.y - centerY > 0) { // 触摸点在第3象限
     let xNum = centerX - touch.x;
     let yNum = touch.y - centerY;
     // 判断触摸点在下边还是左边
     if (xNum > yNum) {
       actionType = ActionType.left;
     } else {
       actionType = ActionType.bottom;
     }
   } else if (touch.x - centerX > 0 && touch.y - centerY < 0) { // 触摸点在第1象限
     let xNum = touch.x - centerX;
     let yNum = centerY - touch.y;
     // 判断触摸点在上边还是右边
     if (xNum > yNum) {
       actionType = ActionType.right;
     } else {
       actionType = ActionType.top;
     }
   } else { // 触摸点在第4象限
     let xNum = touch.x - centerX;
     let yNum = touch.y - centerY;
     // 判断触摸点在下边还是右边
     if (xNum > yNum) {
       actionType = ActionType.right;
     } else {
       actionType = ActionType.bottom;
     }
   }
   ```
3. 在视频监控场景中，点击监控云台确认摄像头移动方向。

   ```ts
   export enum ActionType {
     left,
     right,
     top,
     bottom,
     null
   }

   @Entry
   @Component
   struct Index {
     @State rateNum: number = 0;
     private settings: RenderingContextSettings = new RenderingContextSettings(true);
     private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
     private actionType: ActionType = ActionType.null;

     build() {
       Column() {
         Stack() {
           Image($r('app.media.startIcon')) // startIcon是测试图片，开发者需要替换为实际图片
             .objectFit(ImageFit.Cover)
             .width(200)
             .height(200)
             .borderRadius(100)
             .rotate({
               centerX: '50%',
               centerY: '50%',
               angle: this.rateNum
             })
           Canvas(this.context)
             .width(200)
             .height(200)
             .backgroundColor('#00e9a112')
             .borderRadius(100)
             .onReady(() => {
               this.context.font = '18vp sans-serif';
               this.context.textAlign = 'center';
               this.context.fillStyle = Color.Black;
               this.context.fillText('1', this.context.width / 2, this.context.height / 4);
               this.context.fillText('2', this.context.width * 3 / 4 + 10, this.context.height / 2 + 10);
               this.context.fillText('3', this.context.width / 2, this.context.height * 3 / 4 + 10);
               this.context.fillText('4', this.context.width / 4 - 10, this.context.height / 2 + 10);
               this.context.fill();
             })
             .onTouch(event => {
               if (event.type === TouchType.Down) {
                 this.actionType = this.calculateLandingArea(event.target.area, event.touches[0]);
               } else if (event.type === TouchType.Up) {
                 if (this.actionType === ActionType.left) {
                   this.rateNum = 270;
                 } else if (this.actionType === ActionType.right) {
                   this.rateNum = 90;
                 } else if (this.actionType === ActionType.top) {
                   this.rateNum = 0;
                 } else {
                   this.rateNum = 180;
                 }
               }
             })
         }
         .width(200)
         .height(200)
       }
       .backgroundColor('#fff9f9f9')
       .justifyContent(FlexAlign.Center)
       .height('100%')
       .width('100%')
     }

     // 计算落点区域
     calculateLandingArea(area: Area, touch: TouchObject) {
       let actionType: ActionType = ActionType.null;
       // 计算整个可点击范围的中心点
       let centerX = Number(area.width) / 2;
       let centerY = Number(area.height) / 2;
       // 判断触摸点在哪个象限
       if (touch.x - centerX < 0 && touch.y - centerY < 0) { // 触摸点在第2象限
         let xNum = centerX - touch.x;
         let yNum = centerY - touch.y;
         // 判断触摸点在上边还是左边
         if (xNum > yNum) {
           actionType = ActionType.left;
         } else {
           actionType = ActionType.top;
         }

       } else if (touch.x - centerX < 0 && touch.y - centerY > 0) { // 触摸点在第3象限
         let xNum = centerX - touch.x;
         let yNum = touch.y - centerY;
         // 判断触摸点在下边还是左边
         if (xNum > yNum) {
           actionType = ActionType.left;
         } else {
           actionType = ActionType.bottom;
         }
       } else if (touch.x - centerX > 0 && touch.y - centerY < 0) { // 触摸点在第1象限
         let xNum = touch.x - centerX;
         let yNum = centerY - touch.y;
         // 判断触摸点在上边还是右边
         if (xNum > yNum) {
           actionType = ActionType.right;
         } else {
           actionType = ActionType.top;
         }
       } else { // 触摸点在第4象限
         let xNum = touch.x - centerX;
         let yNum = touch.y - centerY;
         // 判断触摸点在下边还是右边
         if (xNum > yNum) {
           actionType = ActionType.right;
         } else {
           actionType = ActionType.bottom;
         }
       }
       console.info('判断方向：', actionType);
       return actionType;
     }
   }
   ```
