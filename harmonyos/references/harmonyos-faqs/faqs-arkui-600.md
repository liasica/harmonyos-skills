---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-600
title: 如何实现LED弹幕效果的滚动显示
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 如何实现LED弹幕效果的滚动显示
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:01+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:ddbef046ae98b9a5541da532575b2a32b15f071b9125ee1859768fecfd5be86b
---

## 问题现象

ArkTS如何实现点阵屏背景样式的弹幕滚动？效果如下图：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f0/v3/C-8YHyJ3REu4i0ZicC12Uw/zh-cn_image_0000002658791977.png "点击放大")

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f5/v3/TzF8nRuCS3SpX1cSjevqRA/zh-cn_image_0000002628552602.gif "点击放大")

## 背景知识

* [MeasureUtils](../harmonyos-references/arkts-apis-uicontext-measureutils.md)提供文本宽度、高度等相关计算。用于计算文本在不同条件下的尺寸、换行方式及布局参数，适用于动态界面设计、自适应布局等根据内容动态调整组件的大小或布局。
* [Marquee](../harmonyos-references/ts-basic-components-marquee.md)是跑马灯组件，用于滚动展示一段单行文本，仅当文本内容宽度大于等于组件宽度时滚动。创建组件时可以设置MarqueeOptions的不同参数，如step设置滚动动画的步长。
* [Canvas](../harmonyos-references/ts-components-canvas-canvas.md)提供画布组件，用于自定义绘制图形，开发者使用[CanvasRenderingContext2D](../harmonyos-references/ts-canvasrenderingcontext2d.md)对象和[OffscreenCanvasRenderingContext2D](../harmonyos-references/ts-offscreencanvasrenderingcontext2d.md)对象在Canvas组件上进行绘制，绘制对象可以是基础形状、文本、图片等。

## 解决方案

通过Marquee实现滚动播放的效果，Canvas组件画出一个LED效果的遮罩，具体步骤如下：

1. 计算文本是否超过Marquee的宽度，如果没有超过，用空格补齐，以保证正常滚动。

   ```screen
   // 计算文本是否超过Marquee的宽度，如果没有超过，用空格补齐，以保证正常滚动
   CompleteTextByTextWidth(src: string, fontSize: number, fontWeight: number) {
     let displayInfo = display.getDefaultDisplaySync();
     let displayWidth = displayInfo.width;
     let textWidth = this.getUIContext()
       .getMeasureUtils()
       .measureText({ textContent: src, fontSize: fontSize, fontWeight: fontWeight });
     while (textWidth <= displayWidth) {
       src += ' ';
       textWidth = this.getUIContext()
         .getMeasureUtils()
         .measureText({ textContent: src, fontSize: fontSize, fontWeight: fontWeight });
     }
     return src;
   }
   ```
2. 使用Marquee实现滚动显示。

   ```screen
   Marquee({
     start: this.start,
     step: this.step,
     fromStart: this.fromStart,
     src: this.danMuSrc
   })
     .width(this.danMuScreenWidth)
     .height(this.danMuScreenHeight)
     .fontColor('#ffc60f0f')
     .fontSize(48)
     .fontWeight(700)
     .backgroundColor('#182431')
   ```
3. 通过Canvas绘制网格遮罩，实现LED点阵屏的效果。

   ```screen
   // LED点阵屏模拟遮罩
   Canvas(this.canvasContext)
     .width(this.danMuScreenWidth)
     .height(this.danMuScreenHeight)
     .onReady(() => {
       this.canvasContext.beginPath();
       this.canvasContext.lineWidth = 0.55;
       let lineCountW = this.danMuScreenWidth / this.spaceWidth;
       let lineCountH = this.danMuScreenHeight / this.spaceWidth;
       // 相等间隔画出横线
       for (let index = 0; index <= lineCountH; index++) {
         let y = index === lineCountH ? (this.danMuScreenHeight) : this.spaceWidth * index;
         this.canvasContext.moveTo(0, y);
         this.canvasContext.lineTo(this.danMuScreenWidth, y);
       }
       // 相等间隔画出竖线
       for (let index = 0; index <= lineCountW; index++) {
         let x = index === lineCountW ? (this.danMuScreenWidth) : this.spaceWidth * index;
         this.canvasContext.moveTo(x, 0);
         this.canvasContext.lineTo(x, this.danMuScreenHeight);
       }
       this.canvasContext.stroke();
     })
   ```
4. 完整示例参考如下：

   ```screen
   import { display } from '@kit.ArkUI';

   @Entry
   @Component
   struct MarqueePage {
     @State start: boolean = false;
     @State danMuSrc: string = '';
     context = this.getUIContext().getHostContext() as Context;
     private fromStart: boolean = true;
     private step: number = 10;
     private danMuScreenWidth: number = this.getUIContext().px2vp(display.getDefaultDisplaySync().width);
     private danMuScreenHeight: number = 200;
     private spaceWidth: number = 3;
     private settings: RenderingContextSettings = new RenderingContextSettings(true);
     private canvasContext: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);

     aboutToAppear(): void {
       this.danMuSrc = this.CompleteTextByTextWidth(this.danMuSrc, 48, 700);
     }

     // 计算文本是否超过Marquee的宽度，如果没有超过，用空格补齐，以保证正常滚动
     CompleteTextByTextWidth(src: string, fontSize: number, fontWeight: number) {
       let displayInfo = display.getDefaultDisplaySync();
       let displayWidth = displayInfo.width;
       let textWidth = this.getUIContext()
         .getMeasureUtils()
         .measureText({ textContent: src, fontSize: fontSize, fontWeight: fontWeight });
       while (textWidth <= displayWidth) {
         src += ' ';
         textWidth = this.getUIContext()
           .getMeasureUtils()
           .measureText({ textContent: src, fontSize: fontSize, fontWeight: fontWeight });
       }
       return src;
     }

     build() {
       Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
         Stack() {
           Marquee({
             start: this.start,
             step: this.step,
             fromStart: this.fromStart,
             src: this.danMuSrc
           })
             .width(this.danMuScreenWidth)
             .height(this.danMuScreenHeight)
             .fontColor('#ffc60f0f')
             .fontSize(48)
             .fontWeight(700)
             .backgroundColor('#182431')
           // LED点阵屏模拟遮罩
           Canvas(this.canvasContext)
             .width(this.danMuScreenWidth)
             .height(this.danMuScreenHeight)
             .onReady(() => {
               this.canvasContext.beginPath();
               this.canvasContext.lineWidth = 0.55;
               let lineCountW = this.danMuScreenWidth / this.spaceWidth;
               let lineCountH = this.danMuScreenHeight / this.spaceWidth;
               // 相等间隔画出横线
               for (let index = 0; index <= lineCountH; index++) {
                 let y = index === lineCountH ? (this.danMuScreenHeight) : this.spaceWidth * index;
                 this.canvasContext.moveTo(0, y);
                 this.canvasContext.lineTo(this.danMuScreenWidth, y);
               }
               // 相等间隔画出竖线
               for (let index = 0; index <= lineCountW; index++) {
                 let x = index === lineCountW ? (this.danMuScreenWidth) : this.spaceWidth * index;
                 this.canvasContext.moveTo(x, 0);
                 this.canvasContext.lineTo(x, this.danMuScreenHeight);
               }
               this.canvasContext.stroke();
             })
         }

         TextInput({ placeholder: '输入弹幕' })
           .type(InputType.USER_NAME)
           .placeholderColor(0x182431)
           .showPasswordIcon(false)
           .placeholderFont({ size: 16, weight: FontWeight.Regular })
           .opacity(0.6)
           .width('90%')
           .margin({ top: 20 })
           .hitTestBehavior(HitTestMode.Default)
           .onChange((value: string) => {
             this.danMuSrc = this.CompleteTextByTextWidth(value, 48, 700);
           })
         Button('Start')
           .onClick(() => {
             this.start = true;
           })
           .width(120)
           .height(40)
           .fontSize(16)
           .margin({ top: 20 })
           .fontWeight(500)
           .backgroundColor('#007DFF')
       }
       .width('100%')
       .height('100%')
     }
   }
   ```
