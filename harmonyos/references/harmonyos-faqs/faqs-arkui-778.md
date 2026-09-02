---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-778
title: 如何将Canvas图像传递到Dialog子页面
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 如何将Canvas图像传递到Dialog子页面
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:23+08:00
doc_updated_at: 2026-08-13
content_hash: sha256:8d40d8061cde055132ed4c055880c9eb55e0b9babc58a0b0405b61efe30a5fdc
---

## 问题现象

如何将Canvas的图像信息保存到XLayer类中，并传递到Dialog的Item里面？

## 背景知识

@Prop装饰器[限制条件](../harmonyos-guides/arkts-prop.md#限制条件)：@Prop装饰变量时会进行深拷贝，在拷贝的过程中除了基本类型、Map、Set、Date、Array外，都会丢失类型。例如[PixelMap](../harmonyos-references/arkts-apis-image-pixelmap.md)等通过NAPI提供的复杂类型，由于有部分实现在Native侧，因此无法在ArkTS侧通过深拷贝获得完整的数据。

使用CanvasRenderingContext2D中[getPixelMap](../harmonyos-references/ts-components-canvas-common-method.md#getpixelmap)方法可将当前Canvas指定区域内的像素数据转换为PixelMap对象。

## 解决方案

1. 绘制Canvas图像，将Canvas的图像信息保存到XLayer类中。

   ```screen
   @Observed
   export class XLayer {
     static ID: number = 100;
     id: number = 0;
     pixelMap?: PixelMap;
     imageData?: ImageData;

     constructor() {
       this.id = ++XLayer.ID;
     }
   }

   @Entry
   @Component
   struct CanvasImageToDialogSubPage {
     WH: number = 200;
     message: string = '点击最大的方框进行绘图';
     private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(new RenderingContextSettings(false));
     @State layers: XLayer[] = [];
     xLayerDialog: CustomDialogController = new CustomDialogController({
       builder: XLayerDialog({
         layers: this.layers,
       })
     });

     build() {
       Row() {
         RelativeContainer() {
           Text(this.message)
             .id('DemoHelloWorld')
             .fontSize(28)
             .fontWeight(FontWeight.Bold)
             .alignRules({
               middle: { anchor: '__container__', align: HorizontalAlign.Center }
             });

           Row({ space: 20 }) {
             Canvas(this.context)
               .onReady(() => {
                 this.context.fillStyle = '#fcebff';
                 this.context.fillRect(0, 0, this.WH, this.WH);
                 this.context.lineWidth = 20;
                 this.context.strokeStyle = '#fa7fd9';
                 this.context.beginPath();
                 this.context.ellipse(this.WH / 2, this.WH / 2, this.WH / 2, this.WH / 2, 0, 0, Math.PI * 2);
                 this.context.stroke();
               })
               .width(200)
               .height(200)
               .borderWidth(2)
               .onClick(() => {
                 this.layers = this.getLayers();
                 this.xLayerDialog.open();
               });
           }
           .alignRules({
             top: { anchor: 'DemoHelloWorld', align: VerticalAlign.Bottom },
             middle: { anchor: 'DemoHelloWorld', align: HorizontalAlign.Center }
           });
         }
         .height('auto')
         .width('auto');
       }
       .height('100%');
     }

     getLayers(): XLayer[] {
       let layers: XLayer[] = [];
       for (let i = 0; i < 3; ++i) {
         let item = new XLayer();
         let pm = this.context.getPixelMap(0, 0, this.WH, this.WH);
         let im = undefined;
         console.info(`getLayers:${pm} - ${im}`);
         item.pixelMap = pm;
         item.imageData = im;
         layers.push(item);
       }
       return layers;
     }
   }
   ```
2. 定义Dialog弹窗中需要显示的XLayerItem，通过Image组件加载PixelMap。

   ```screen
   @Component
   export struct XLayerItem {
     layer: XLayer | null = null;

     build() {
       Stack() {
         // 使用pixelmap
         Image(this.layer?.pixelMap).width(90)
           .height(90);

         Text('' + this.layer?.id.toFixed(0))
           .fontSize(18)
           .fontWeight(FontWeight.Bold)
           .fontColor(Color.White)
           .padding({
             left: 5,
             right: 5,
             top: 2,
             bottom: 2
           })
           .backgroundColor(Color.Blue)
           .borderRadius(5);
       }
       .width(90)
       .height(90);
     }
   }
   ```
3. 定义Dialog弹窗，遍历加载XLayerItem。

   ```screen
   @CustomDialog
   export struct XLayerDialog {
     controller?: CustomDialogController;
     @Link layers: XLayer[];

     build() {
       Column() {
         Text('title')
           .fontSize(16)
           .margin({ top: 20, bottom: 0 })
           .fontWeight(FontWeight.Bold);
         Image(this.layers[0].pixelMap).width(100)
           .height(100);

         Grid() {
           ForEach(this.layers, (item: XLayer) => {
             GridItem() {
               XLayerItem({ layer: item });
             }
             .width(100)
             .height(100)
             .border({ color: Color.Blue, width: 5 });
           });
         }
         .width(320)
         .height(320)
         .columnsTemplate('1fr 1fr 1fr')
         .columnsGap(10)
         .rowsGap(10);
       };
     }
   }
   ```
