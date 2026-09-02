---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-396
title: 如何实现在图片进行绘制马赛克的效果
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 如何实现在图片进行绘制马赛克的效果
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:28+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:7dbbdb9ec0b3df96894c5822edf5e8ffd06cc8e9ad0282cdc15052a43036c519
---

在图片上进行绘制马赛克的效果可通过以下步骤来实现。

1. 给画布添加移动手势。

   ```typescript
   import { DrawPathType, DrawViewModel } from '../viewmodel/DrawViewModel';

   @Component
   export struct DrawView {
     @ObjectLink viewModel: DrawViewModel;

     build() {
       Column({ space: 8 }) {
         Text('Please select the brush type')
           .fontColor(Color.Red)
           .textAlign(TextAlign.Center)
           .fontSize(30)
           .width('80%')
           .margin('10%')

         Canvas(this.viewModel.context)
           .width('100%')
           .height('75%')
           .onAreaChange((oldValue: Area, newValue: Area) => {
             this.viewModel.canvasAreaChange(newValue);
           })
           .gesture(
             GestureGroup(GestureMode.Exclusive,
               PanGesture()
                 .onActionStart((event: GestureEvent) => {
                   let finger: FingerInfo = event.fingerList[0];
                   if (finger == undefined) {
                     return;
                   }
                   let x = finger.localX;
                   let y = finger.localY;
                   this.viewModel.moveStart(x, y);
                 })
                 .onActionUpdate((event: GestureEvent) => {
                   let finger: FingerInfo = event.fingerList[0];
                   if (finger == undefined) {
                     return;
                   }
                   let x = finger.localX;
                   let y = finger.localY;
                   this.viewModel.moveUpdate(x, y);
                 })
                 .onActionEnd((event: GestureEvent) => {
                   let finger: FingerInfo = event.fingerList[0];
                   if (finger == undefined) {
                     return;
                   }
                   this.viewModel.moveEnd();
                 })
             )
           )

         Flex({ direction: FlexDirection.Row, justifyContent: FlexAlign.SpaceAround }) {
           Button('Ordinary paintbrush')
             .onClick(() => {
               this.viewModel.drawModel.pathType = DrawPathType.pen;
             })
           Button('Mosaic brush')
             .onClick(() => {
               this.viewModel.drawModel.pathType = DrawPathType.pattern;
             })
           Button('Clear the content')
             .onClick(() => {
               this.viewModel.clearPath();
             })
         }
       }
     }
   }
   ```
2. 绘制路径以及马赛克。

   ```ts
   export class DrawPathPointModel {
     x: number = 0;
     y: number = 0;
   }

   export enum DrawPathType {
     pen = 0, // Brush
     pattern // Mosaic
   }

   // Configure the brush
   export class DrawPathModel {
     public pathType: DrawPathType = DrawPathType.pen;
     public color: string = '#ED1B1B';
     public lineWidth: number = 8;
     public img: ImageBitmap = new ImageBitmap('Images/startIcon.png');
   }

   @Observed
   export class DrawViewModel {
     public settings: RenderingContextSettings = new RenderingContextSettings(true);
     public context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
     public drawModel: DrawPathModel = new DrawPathModel();
     public canvasHeight: number = 0;
     public canvasWidth: number = 0;
     private pattern: CanvasPattern | null = null;
     private points: DrawPathPointModel[] = [];
     // Draw a path
     private drawPath = new Path2D();

     constructor() {
       this.pattern = this.context.createPattern(this.drawModel.img, 'repeat');
     }

     moveStart(x: number, y: number) {
       this.points.push({ x: x, y: y });
       this.drawPath.moveTo(x, y);
       this.drawCurrentPathModel();
     }

     moveUpdate(x: number, y: number) {
       let lastPoint = this.points[this.points.length - 1];
       this.points.push({ x: x, y: y });
       this.drawPath.quadraticCurveTo((x + lastPoint.x) / 2, (y + lastPoint.y) / 2, x, y);
       this.drawCurrentPathModel();
     }

     moveEnd() {
       this.points = [];
       this.drawPath = new Path2D();
     }

     clearPath() {
       this.points = [];
       this.drawPath = new Path2D();
       this.context.clearRect(0, 0, this.canvasWidth, this.canvasHeight);
     }

     canvasAreaChange(area: Area) {
       this.canvasHeight = area.height as number;
       this.canvasWidth = area.width as number;
     }

     private drawCurrentPathModel() {
       this.context.globalCompositeOperation = 'source-over';
       this.context.lineWidth = this.drawModel.lineWidth;
       if (this.drawModel.pathType == DrawPathType.pen) {
         this.context.strokeStyle = this.drawModel.color;
       } else {
         if (this.pattern) {
           this.context.strokeStyle = this.pattern;
         }
       }
       this.context.lineJoin = 'round';
       this.context.stroke(this.drawPath);
     }
   }
   ```
3. 使用Stack组件进行页面布局。

   ```typescript
   import { DrawView } from './MosaicEffect';
   import { DrawViewModel } from '../viewmodel/DrawViewModel';

   @Entry
   @Component
   struct Index {
     @State viewModel: DrawViewModel = new DrawViewModel();

     build() {
       Stack() {
         Image($rawfile('test.jpg'))
           .objectFit(ImageFit.Fill)
           .width('100%')
           .height('100%')

         DrawView({ viewModel: this.viewModel })
           .width('100%')
           .height('100%')
       }
     }
   }
   ```
