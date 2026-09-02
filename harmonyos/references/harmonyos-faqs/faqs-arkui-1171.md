---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1171
title: 如何实现光标跟随
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 如何实现光标跟随
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:24+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:de0db74a6c3a10ffbfd350a7238cc0ced30b4d78271af0a9408e4301417db1d9
---

## 问题现象

如何实现光标跟随，同时四个角线同步跟随的效果？

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/24/v3/Z-hrz3HPRUuYdDNzlhc_vQ/zh-cn_image_0000002658929093.png "点击放大")

## 背景知识

* [Canvas](../harmonyos-references/ts-components-canvas-canvas.md)提供画布组件，用于自定义绘制图形，开发者使用[CanvasRenderingContext2D](../harmonyos-references/ts-canvasrenderingcontext2d.md)对象和[OffscreenCanvasRenderingContext2D](../harmonyos-references/ts-offscreencanvasrenderingcontext2d.md)对象在Canvas组件上进行绘制，绘制对象可以是基础形状、文本、图片等。
* [触摸事件](../harmonyos-references/ts-universal-events-touch.md)：手指在组件上按下、滑动或抬起时触发，可以获取触摸点以及滑动位置。

## 解决方案

以画面作为背景，在其上方叠加一层透明的Canvas组件，用作光标载体。具体操作步骤如下：

1. 依据画面区域的定义，使用Canvas组件绘制背景图像，并在光标区域完成初始化后，获取光标中心点的初始坐标信息。

   ```ts
   // 绘制背景图
   Canvas(this.canvasBgContext)
     .width(this.sw)
     .height(this.sh)
     .onReady(() => {
       this.drawImage();
     })
     .onAreaChange((value: Area, newVal: Area) => {
       // 获取图片位置xy，以及菱形光标区域位置的初始化信息，和光标中心点的初始化坐标
       this.initPosition.x = Math.round(newVal.position.x as number);
       this.initPosition.y = Math.round(newVal.position.y as number);
       this.initPosition.width = this.sw;
       this.initPosition.height = this.sh;
       this.cursorPosition.x = (this.sw - this.cursorWH) / 2;
       this.cursorPosition.y = (this.sh - this.cursorWH) / 2;
       this.cursorPosition.width = this.cursorWH;
       this.cursorPosition.height = this.cursorWH;
       this.cursorCenterPosition = {
         x: this.cursorPosition.x + this.cursorPosition.width / 2,
         y: this.cursorPosition.y + this.cursorPosition.width / 2
       };
       console.info('initPosition() x= ' + this.initPosition.x + '  y = ' + this.initPosition.y);
     });
   ```
2. 根据菱形光标的初始化参数，利用Canvas组件进行图形绘制，生成对应的光标图像。

   ```ts
   // 绘制光标
   drawCursorImage() {
     // 算出菱形四个点
     let positionL: Position = { x: this.cursorPosition.x, y: this.cursorPosition.y + this.cursorPosition.height / 2 };
     let positionT: Position = { x: this.cursorPosition.x + this.cursorPosition.width / 2, y: this.cursorPosition.y };
     let positionR: Position = {
       x: this.cursorPosition.x + this.cursorPosition.width,
       y: this.cursorPosition.y + this.cursorPosition.height / 2
     };
     let positionB: Position = {
       x: this.cursorPosition.x + this.cursorPosition.width / 2,
       y: this.cursorPosition.y + this.cursorPosition.height
     };
     let lineWidth = 2;
     this.canvasContext2.clearRect(0, 0, this.sw, this.sh);
     this.canvasContext2.lineWidth = lineWidth;
     this.canvasContext2.strokeStyle = this.isTouchDown ? '#ff1a5cae' : '#ffffffff';
     // 画出四角
     this.canvasContext2.beginPath();
     this.canvasContext2.moveTo(positionL.x + this.dashedLineW, positionL.y - this.dashedLineW);
     this.canvasContext2.lineTo(positionL.x, positionL.y);
     this.canvasContext2.lineTo(positionL.x + this.dashedLineW, positionL.y + this.dashedLineW);

     this.canvasContext2.moveTo(positionT.x - this.dashedLineW, positionT.y + this.dashedLineW);
     this.canvasContext2.lineTo(positionT.x, positionT.y);
     this.canvasContext2.lineTo(positionT.x + this.dashedLineW, positionT.y + this.dashedLineW);

     this.canvasContext2.moveTo(positionR.x - this.dashedLineW, positionR.y - this.dashedLineW);
     this.canvasContext2.lineTo(positionR.x, positionR.y);
     this.canvasContext2.lineTo(positionR.x - this.dashedLineW, positionR.y + this.dashedLineW);

     this.canvasContext2.moveTo(positionB.x - this.dashedLineW, positionB.y - this.dashedLineW);
     this.canvasContext2.lineTo(positionB.x, positionB.y);
     this.canvasContext2.lineTo(positionB.x + this.dashedLineW, positionB.y - this.dashedLineW);

     this.canvasContext2.stroke();
     // 画出中心圆
     this.canvasContext2.beginPath();
     this.canvasContext2.strokeStyle = this.isTouchDown ? '#ff1a5cae' : '#ff9ba59b';
     this.canvasContext2.fillStyle = this.isTouchDown ? '#ff1a5cae' : '#ff9ba59b';
     this.canvasContext2.arc(this.cursorPosition.x + this.cursorPosition.width / 2,
       this.cursorPosition.y + this.cursorPosition.width / 2, this.arcRadius, 0, 2 * Math.PI);
     this.canvasContext2.fill();
     this.canvasContext2.stroke();

     // 画出四条线
     this.canvasContext2.beginPath();
     this.canvasContext2.lineWidth = 0.7;
     this.canvasContext2.moveTo(positionL.x, positionL.y);
     this.canvasContext2.lineTo(0, positionL.y);

     this.canvasContext2.moveTo(positionT.x, positionT.y);
     this.canvasContext2.lineTo(positionT.x, 0);

     this.canvasContext2.moveTo(positionR.x, positionR.y);
     this.canvasContext2.lineTo(this.sw, positionR.y);

     this.canvasContext2.moveTo(positionB.x, positionB.y);
     this.canvasContext2.lineTo(positionB.x, this.sh);

     this.canvasContext2.stroke();
   };
   ```
3. 通过设置监听函数，实时检测光标位置的变化，当检测到位置变动时，触发页面的刷新操作，并同步更新光标的颜色状态。

   ```ts
   .onTouch(event => {
     if (event.type === TouchType.Down) {
       this.isReadyMove = this.isTouchCursorArea(event.touches[0]);
       if (this.isReadyMove) {
         this.isTouchDown = true;
       };

       this.touchPosition = {
         x: event.touches[0].displayX,
         y: event.touches[0].displayY
       };
     } else if (event.type === TouchType.Move) {
       if (this.isReadyMove) {
         let moveX = event.changedTouches[0].displayX - this.touchPosition.x;
         let moveY = event.changedTouches[0].displayY - this.touchPosition.y;
         this.touchPosition = {
           x: event.changedTouches[0].displayX,
           y: event.changedTouches[0].displayY
         };
         this.cursorPosition.x += moveX;
         this.cursorPosition.y += moveY;

         this.cursorCenterPosition = {
           x: this.cursorPosition.x + this.cursorPosition.width / 2,
           y: this.cursorPosition.y + this.cursorPosition.width / 2
         };
         // 光标区域中心点位置限制
         if (this.cursorCenterPosition.x < 0) {
           this.cursorPosition.x = -this.cursorPosition.width / 2;
         };
         if (this.cursorCenterPosition.y < 0) {
           this.cursorPosition.y = -this.cursorPosition.height / 2;
         };
         if (this.cursorCenterPosition.x > this.sw) {
           this.cursorPosition.x = this.sw - this.cursorPosition.width / 2;
         };
         if (this.cursorCenterPosition.y > this.sh) {
           this.cursorPosition.y = this.sh - this.cursorPosition.height / 2;
         };

       }
     } else {
       this.isTouchDown = false;
     }
   });
   ```
4. 完整示例参考如下：

   ```ts
   import { image } from '@kit.ImageKit';
   import { resourceManager } from '@kit.LocalizationKit';
   import { common } from '@kit.AbilityKit';
   // 矩形框信息类
   export interface RectPosition {
     x: number;
     y: number;
     height: number;
     width: number;
   }
   // 位置信息类
   export interface Position {
     x: number;
     y: number;
   }
   @Entry
   @Component
   struct CursorFollowing {
     @State pixelMap: image.PixelMap | undefined = undefined;
     @State imageInfo: image.ImageInfo | undefined = undefined;
     // 监听是否按下，刷新光标颜色
     @State @Watch('changeCursorColor') isTouchDown: boolean = false;
     // 监听位置变化，刷新页面
     @State @Watch('drawCursorImage') cursorPosition: RectPosition = {
       x: 0,
       y: 0,
       width: 0,
       height: 0,
     };
     // 初始化画面区域信息
     @State initPosition: RectPosition = {
       x: 0,
       y: 0,
       width: 0,
       height: 0,
     };
     private settings: RenderingContextSettings = new RenderingContextSettings(true);
     private canvasBgContext: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
     private settings2: RenderingContextSettings = new RenderingContextSettings(true);
     private canvasContext2: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings2);
     private sw: number = 360; // 图片展示框固定宽度
     private sh: number = 270; // 图片展示框固定高度
     private cursorWH: number = 50; // 光标区域宽高
     private dashedLineW: number = 7; // 菱形光标线长
     private arcRadius: number = 6; // 光标中心圆半径
     private isReadyMove: boolean = false;
     // 触摸点坐标
     private touchPosition: Position = {
       x: 0,
       y: 0,
     };
     // 当前光标中心点坐标
     private cursorCenterPosition: Position = {
       x: 0,
       y: 0,
     };
     aboutToAppear() {
       let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
       const resourceMgr: resourceManager.ResourceManager = context.resourceManager;
       let buffer = resourceMgr.getMediaByNameSync('background').buffer.slice(0); // 'background'仅作示例，请替换为实际使用的资源
       let imageSource = image.createImageSource(buffer);
       this.pixelMap = imageSource.createPixelMapSync();
       let imageInfo = this.pixelMap.getImageInfoSync();
       this.imageInfo = imageInfo;
     };
     build() {
       Column() {
         // 绘制背景图
         Canvas(this.canvasBgContext)
           .width(this.sw)
           .height(this.sh)
           .onReady(() => {
             this.drawImage();
           })
           .onAreaChange((value: Area, newVal: Area) => {
             // 获取图片位置xy，以及菱形光标区域位置的初始化信息，和光标中心点的初始化坐标
             this.initPosition.x = Math.round(newVal.position.x as number);
             this.initPosition.y = Math.round(newVal.position.y as number);
             this.initPosition.width = this.sw;
             this.initPosition.height = this.sh;
             this.cursorPosition.x = (this.sw - this.cursorWH) / 2;
             this.cursorPosition.y = (this.sh - this.cursorWH) / 2;
             this.cursorPosition.width = this.cursorWH;
             this.cursorPosition.height = this.cursorWH;
             this.cursorCenterPosition = {
               x: this.cursorPosition.x + this.cursorPosition.width / 2,
               y: this.cursorPosition.y + this.cursorPosition.width / 2
             };
             console.info('initPosition() x= ' + this.initPosition.x + '  y = ' + this.initPosition.y);
           });
         // 绘制光标
         Canvas(this.canvasContext2)
           .position({
             x: this.initPosition.x,
             y: this.initPosition.y
           })
           .width(this.sw)
           .height(this.sh)
           .hitTestBehavior(HitTestMode.Transparent)
           .onReady(() => {
             this.drawCursorImage();
           })
           .onTouch(event => {
             if (event.type === TouchType.Down) {
               this.isReadyMove = this.isTouchCursorArea(event.touches[0]);
               if (this.isReadyMove) {
                 this.isTouchDown = true;
               };

               this.touchPosition = {
                 x: event.touches[0].displayX,
                 y: event.touches[0].displayY
               };
             } else if (event.type === TouchType.Move) {
               if (this.isReadyMove) {
                 let moveX = event.changedTouches[0].displayX - this.touchPosition.x;
                 let moveY = event.changedTouches[0].displayY - this.touchPosition.y;
                 this.touchPosition = {
                   x: event.changedTouches[0].displayX,
                   y: event.changedTouches[0].displayY
                 };
                 this.cursorPosition.x += moveX;
                 this.cursorPosition.y += moveY;

                 this.cursorCenterPosition = {
                   x: this.cursorPosition.x + this.cursorPosition.width / 2,
                   y: this.cursorPosition.y + this.cursorPosition.width / 2
                 };
                 // 光标区域中心点位置限制
                 if (this.cursorCenterPosition.x < 0) {
                   this.cursorPosition.x = -this.cursorPosition.width / 2;
                 };
                 if (this.cursorCenterPosition.y < 0) {
                   this.cursorPosition.y = -this.cursorPosition.height / 2;
                 };
                 if (this.cursorCenterPosition.x > this.sw) {
                   this.cursorPosition.x = this.sw - this.cursorPosition.width / 2;
                 };
                 if (this.cursorCenterPosition.y > this.sh) {
                   this.cursorPosition.y = this.sh - this.cursorPosition.height / 2;
                 };

               }
             } else {
               this.isTouchDown = false;
             }
           });
       }
       .height('100%')
       .width('100%')
       .justifyContent(FlexAlign.Center)
       .backgroundColor('#fff5f3f3')
     }
     // 绘制背景图
     drawImage() {
       if (this.imageInfo !== undefined) {
         this.canvasBgContext.drawImage(this.pixelMap, 0, 0, this.imageInfo.size.width, this.imageInfo.size.height, 0, 0,
           this.getUIContext().vp2px(this.sw), this.getUIContext().vp2px(this.sh));
         this.canvasBgContext.save();
       }
     };
     changeCursorColor() {
       this.drawCursorImage();
     };
     // 绘制光标
     drawCursorImage() {
       // 算出菱形四个点
       let positionL: Position = { x: this.cursorPosition.x, y: this.cursorPosition.y + this.cursorPosition.height / 2 };
       let positionT: Position = { x: this.cursorPosition.x + this.cursorPosition.width / 2, y: this.cursorPosition.y };
       let positionR: Position = {
         x: this.cursorPosition.x + this.cursorPosition.width,
         y: this.cursorPosition.y + this.cursorPosition.height / 2
       };
       let positionB: Position = {
         x: this.cursorPosition.x + this.cursorPosition.width / 2,
         y: this.cursorPosition.y + this.cursorPosition.height
       };
       let lineWidth = 2;
       this.canvasContext2.clearRect(0, 0, this.sw, this.sh);
       this.canvasContext2.lineWidth = lineWidth;
       this.canvasContext2.strokeStyle = this.isTouchDown ? '#ff1a5cae' : '#ffffffff';
       // 画出四角
       this.canvasContext2.beginPath();
       this.canvasContext2.moveTo(positionL.x + this.dashedLineW, positionL.y - this.dashedLineW);
       this.canvasContext2.lineTo(positionL.x, positionL.y);
       this.canvasContext2.lineTo(positionL.x + this.dashedLineW, positionL.y + this.dashedLineW);

       this.canvasContext2.moveTo(positionT.x - this.dashedLineW, positionT.y + this.dashedLineW);
       this.canvasContext2.lineTo(positionT.x, positionT.y);
       this.canvasContext2.lineTo(positionT.x + this.dashedLineW, positionT.y + this.dashedLineW);

       this.canvasContext2.moveTo(positionR.x - this.dashedLineW, positionR.y - this.dashedLineW);
       this.canvasContext2.lineTo(positionR.x, positionR.y);
       this.canvasContext2.lineTo(positionR.x - this.dashedLineW, positionR.y + this.dashedLineW);

       this.canvasContext2.moveTo(positionB.x - this.dashedLineW, positionB.y - this.dashedLineW);
       this.canvasContext2.lineTo(positionB.x, positionB.y);
       this.canvasContext2.lineTo(positionB.x + this.dashedLineW, positionB.y - this.dashedLineW);

       this.canvasContext2.stroke();
       // 画出中心圆
       this.canvasContext2.beginPath();
       this.canvasContext2.strokeStyle = this.isTouchDown ? '#ff1a5cae' : '#ff9ba59b';
       this.canvasContext2.fillStyle = this.isTouchDown ? '#ff1a5cae' : '#ff9ba59b';
       this.canvasContext2.arc(this.cursorPosition.x + this.cursorPosition.width / 2,
         this.cursorPosition.y + this.cursorPosition.width / 2, this.arcRadius, 0, 2 * Math.PI);
       this.canvasContext2.fill();
       this.canvasContext2.stroke();

       // 画出四条线
       this.canvasContext2.beginPath();
       this.canvasContext2.lineWidth = 0.7;
       this.canvasContext2.moveTo(positionL.x, positionL.y);
       this.canvasContext2.lineTo(0, positionL.y);

       this.canvasContext2.moveTo(positionT.x, positionT.y);
       this.canvasContext2.lineTo(positionT.x, 0);

       this.canvasContext2.moveTo(positionR.x, positionR.y);
       this.canvasContext2.lineTo(this.sw, positionR.y);

       this.canvasContext2.moveTo(positionB.x, positionB.y);
       this.canvasContext2.lineTo(positionB.x, this.sh);

       this.canvasContext2.stroke();
     };
     // 判断点击位置是否在圆心中
     isTouchCursorArea(touch: TouchObject) {
       let tempLength = Math.sqrt((touch.x - this.cursorCenterPosition.x) * (touch.x - this.cursorCenterPosition.x) +
         (touch.y - this.cursorCenterPosition.y) * (touch.y - this.cursorCenterPosition.y));
       if (tempLength < this.arcRadius) {
         return true;
       }
       return false;
     };
   }
   ```

代码效果如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d2/v3/gUIAV4AnQaOhJG2XlODiJw/zh-cn_image_0000002658809145.png "点击放大")
