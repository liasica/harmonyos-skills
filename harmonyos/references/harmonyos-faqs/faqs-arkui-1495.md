---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1495
title: Text组件如何获取关键字相对组件的坐标进行绘制下划线
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > Text组件如何获取关键字相对组件的坐标进行绘制下划线
category: harmonyos-faqs
scraped_at: 2026-09-02T15:03:48+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:3a0fe07cd1ae6b87f6d04b88d4e43152359c9f4609f19fa75ed5ae0bceb0a80f
---

## 问题现象

给一段文本中关键字绘制下划线，文本采用Text组件中包含Span和ImageSpan的形式显示，如何获取关键字相对组件的坐标进行绘制下划线？

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/56/v3/Mht2r6e5SGmILchSquYbMw/zh-cn_image_0000002658845083.png "点击放大")

## 背景知识

* [ParagraphBuilder](../harmonyos-references/js-apis-graphics-text.md#paragraphbuilder)：段落生成器，控制生成不同的段落对象。
* [ParagraphStyle](../harmonyos-references/js-apis-graphics-text.md#paragraphstyle)：段落样式，控制整个段落的断行策略、断词策略等属性。
* [getRectsForRange](../harmonyos-references/js-apis-graphics-text.md#getrectsforrange)：获取给定的矩形区域宽度以及矩形区域高度的规格下，文本中该区间范围内的字符所占的矩形区域。
* [getRectangleById](../harmonyos-references/arkts-apis-uicontext-componentutils.md#getrectanglebyid)：获取组件大小、位置、平移、缩放、旋转及仿射矩阵属性信息。
* [onAreaChange](../harmonyos-references/ts-universal-component-area-change-event.md#onareachange)：组件区域变化时触发该回调。仅会响应由布局变化所导致的组件大小、位置发生变化时的回调。
* [alignRules](../harmonyos-references/ts-securitycomponent-attributes.md#alignrules15)：指定设置在相对容器中子组件的对齐规则，仅当父容器为RelativeContainer时生效。

## 解决方案

实现思路如下：

1. 根据提供文本字符串和关键字数组，计算出关键字在文本字符串中的索引，若文本中含有图片，在图片后的关键字开始索引start、结束索引end都需要+1。

   ```ts
   aboutToAppear(): void {
     // 筛选关键字索引，若文本中含有图片，在图片后的关键字start、end都需要+1，图片算一个索引。
     for (const targetString of this.target) {
       const index = this.text.indexOf(targetString);
       this.targetIndex.push({
         start: index + 1,
         end: index + targetString.length + 1
       });
     }
   }
   ```
2. 给Text和ImageSpan添加组件唯一标识id。

   ```ts
   Text() {
     ImageSpan($r('sys.media.app_lock_picture'))
       .height(18)
       .margin({ right: this.marginRight })
       .verticalAlign(ImageSpanAlignment.CENTER)
       .offset({
         x: 0,
         y: 2
       })
       .padding(1)
       .id('image');
     Span(this.text)
       .fontSize(19)
       .lineHeight(this.lineHeight);
   }
   .onAreaChange((oldValue: Area, newValue: Area) => {
     console.info('testTag', `获取到oldValue、newValue:${oldValue.width}、${newValue.width}`);
     this.getTextInfo('targetText');
     this.getTextInfo('image');
   })
   .id('targetText');
   ```
3. 在onAreaChange回调中通过getRectangleById分别获取Text和ImageSpan的宽度，若设置margin需要手动计算。

   ```ts
   // 获取Text、ImageSpan位置信息
   getTextInfo(value: string): Record<string, number> {
     let modePosition: componentUtils.ComponentInfo = this.getUIContext().getComponentUtils().getRectangleById(value);
     try {
       if (value === 'targetText') {
         this.textMaxWidth = modePosition.size.width; // 计算出最大的宽度
         return {
           'left': this.getUIContext().px2vp(modePosition.windowOffset.x),
           'width': this.getUIContext().px2vp(modePosition.size.width)
         };
       } else {
         this.imgWidth = modePosition.size.width + this.getUIContext().vp2px(this.marginRight); // 计算出图片的宽度
         this.calcWordsInfo();
         return {
           'left': this.getUIContext().px2vp(modePosition.windowOffset.x),
           'width': this.getUIContext().px2vp(modePosition.size.width)
         };
       }
     } catch (error) {
       return { 'left': 0, 'width': 0 };
     }
   }
   ```
4. 创建段落生成器ParagraphBuilder，通过ParagraphStyle、TextStyle，设置段落样式、文本样式。

   **说明** 

   若ui中有设置margin、padding，文本样式需要设置行高缩放倍数heightScale（行高缩放倍数：行高/文字大小），heightOnly设置为true，否则获取的位置信息不准确。

   ```ts
   // 行高缩放倍数：行高/文字大小
   const myHeightScale: number = this.getUIContext().vp2px(this.lineHeight) / this.getUIContext().vp2px(this.textSize);
   let myTextStyle: text.TextStyle = {
     // 文本样式
     fontSize: this.getUIContext().vp2px(this.textSize),
     heightScale: myHeightScale,
     heightOnly: true
   };
   let myParagraphStyle: text.ParagraphStyle = {
     // 段落样式
     textStyle: myTextStyle,
     align: text.TextAlign.START, // 文本对齐方式
     wordBreak: text.WordBreak.NORMAL,
   };
   let fontCollection = new text.FontCollection(); // 字体控制器
   let paragraphGraphBuilder = new text.ParagraphBuilder(myParagraphStyle, fontCollection); // 段落生成器。
   paragraphGraphBuilder.addPlaceholder({
     // 用于在构建文本段落时插入占位符
     width: this.imgWidth,
     height: this.getUIContext().vp2px(this.imgHeight),
     align: text.PlaceholderAlignment.BOTTOM_OF_ROW_BOX,
     baseline: text.TextBaseline.IDEOGRAPHIC,
     baselineOffset: 0,
   });
   paragraphGraphBuilder.addText(this.text); // 插入具体的文本字符串
   let paragraph = paragraphGraphBuilder.build();
   paragraph.layoutSync(this.textMaxWidth); // 设置最大宽度
   ```
5. 通过getRectsForRange获取给定的矩形区域宽度以及矩形区域高度的规格下，文本中该区间范围内的字符的所占的矩形区域，获取关键字起始点和结束点坐标。

   ```ts
   /**
    * getRectsForRange
    * 参数Range：需要获取的区域的文本区间  start：区间左侧端点索引，整数。end：区间右侧端点索引，整数。
    * 参数widthStyle：返回的矩形区域的宽度的规格
    * 参数heightStyle：返回的矩形区域的高度的规格
    *
    * */
   for (let i = 0; i < this.targetIndex.length; i++) {
     let rects =
       paragraph.getRectsForRange(this.targetIndex[i], text.RectWidthStyle.TIGHT, text.RectHeightStyle.TIGHT);
     // 返回的rect是基于每一行关键字矩形区域的左上角点
     for (const rect of rects) {
       this.textBox.push({
         start: {
           x: this.getUIContext().px2vp(rect.rect.left),
           y: this.getUIContext().px2vp(rect.rect.bottom)
         },
         end: {
           x: this.getUIContext().px2vp(rect.rect.right),
           y: this.getUIContext().px2vp(rect.rect.bottom)
         }
       });
     }
   }
   ```
6. Canvas设置alignRules指定在相对容器中子组件的对齐规则，再通过获取的关键字坐标信息，绘制下划线。

   ```ts
   Canvas(this.context).onReady(() => {
     this.textBox.forEach((line: line) => {
       this.context.lineCap = 'round'; // 设置线条圆角
       this.context.beginPath();
       this.context.lineWidth = 2; // 设置线条宽度
       this.context.strokeStyle = '#0a59F7'; // 设置线条颜色
       this.context.moveTo(line.start.x, line.start.y);
       this.context.lineTo(line.end.x, line.end.y);
       this.context.stroke();
     });
   })
     .alignRules({
       // 指定设置在相对容器中子组件的对齐规则
       top: { anchor: 'targetText', align: VerticalAlign.Top },
       left: { anchor: 'targetText', align: HorizontalAlign.Start },
       right: { anchor: 'targetText', align: HorizontalAlign.End },
       bottom: { anchor: 'targetText', align: VerticalAlign.Bottom }
     });
   ```
7. 完整示例参考如下：

   ```ts
   import { componentUtils } from '@kit.ArkUI';
   import { text } from '@kit.ArkGraphics2D';

   interface line {
     start: point;
     end: point;
   }

   interface point {
     x: number,
     y: number
   }

   @Entry
   @Component
   struct textLine {
     private settings: RenderingContextSettings = new RenderingContextSettings(true);
     private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
     @State textBox: line[] = [];
     text: string =
       '文本模块：提供一系列用于文本布局和字体管理的编程接口。文本布局相关的接口旨在提供高质量的排版，包括字符到字形的转换、字距调整、换行、对齐、文本测量等。字体管理接口提供字体注册、字体描述符、字体集管理等功能。';
     target: string[] = ['字形的转换', '换行', '字体集管理等功能。'];
     targetIndex: text.Range[] = [];
     textMaxWidth: number = 0;
     imgHeight: number = 18;
     imgWidth: number = 0;
     lineHeight: number = 30;
     marginRight: number = 6;
     textSize: number = 19;

     aboutToAppear(): void {
       // 筛选关键字索引，若文本中含有图片，在图片后的关键字start、end都需要+1，图片算一个索引。
       for (const targetString of this.target) {
         const index = this.text.indexOf(targetString);
         this.targetIndex.push({
           start: index + 1,
           end: index + targetString.length + 1
         });
       }
     }

     calcWordsInfo() {
       // 行高缩放倍数：行高/文字大小
       const myHeightScale: number = this.getUIContext().vp2px(this.lineHeight) / this.getUIContext().vp2px(this.textSize);
       let myTextStyle: text.TextStyle = {
         // 文本样式
         fontSize: this.getUIContext().vp2px(this.textSize),
         heightScale: myHeightScale,
         heightOnly: true
       };
       let myParagraphStyle: text.ParagraphStyle = {
         // 段落样式
         textStyle: myTextStyle,
         align: text.TextAlign.START, // 文本对齐方式
         wordBreak: text.WordBreak.NORMAL,
       };
       let fontCollection = new text.FontCollection(); // 字体控制器
       let paragraphGraphBuilder = new text.ParagraphBuilder(myParagraphStyle, fontCollection); // 段落生成器。
       paragraphGraphBuilder.addPlaceholder({
         // 用于在构建文本段落时插入占位符
         width: this.imgWidth,
         height: this.getUIContext().vp2px(this.imgHeight),
         align: text.PlaceholderAlignment.BOTTOM_OF_ROW_BOX,
         baseline: text.TextBaseline.IDEOGRAPHIC,
         baselineOffset: 0,
       });
       paragraphGraphBuilder.addText(this.text); // 插入具体的文本字符串
       let paragraph = paragraphGraphBuilder.build();
       paragraph.layoutSync(this.textMaxWidth); // 设置最大宽度
       /**
        * getRectsForRange
        * 参数Range：需要获取的区域的文本区间  start：区间左侧端点索引，整数。end：区间右侧端点索引，整数。
        * 参数widthStyle：返回的矩形区域的宽度的规格
        * 参数heightStyle：返回的矩形区域的高度的规格
        *
        * */
       for (let i = 0; i < this.targetIndex.length; i++) {
         let rects =
           paragraph.getRectsForRange(this.targetIndex[i], text.RectWidthStyle.TIGHT, text.RectHeightStyle.TIGHT);
         // 返回的rect是基于每一行关键字矩形区域的左上角点
         for (const rect of rects) {
           this.textBox.push({
             start: {
               x: this.getUIContext().px2vp(rect.rect.left),
               y: this.getUIContext().px2vp(rect.rect.bottom)
             },
             end: {
               x: this.getUIContext().px2vp(rect.rect.right),
               y: this.getUIContext().px2vp(rect.rect.bottom)
             }
           });
         }
       }
     }

     // 获取Text、ImageSpan位置信息
     getTextInfo(value: string): Record<string, number> {
       let modePosition: componentUtils.ComponentInfo = this.getUIContext().getComponentUtils().getRectangleById(value);
       try {
         if (value === 'targetText') {
           this.textMaxWidth = modePosition.size.width; // 计算出最大的宽度
           return {
             'left': this.getUIContext().px2vp(modePosition.windowOffset.x),
             'width': this.getUIContext().px2vp(modePosition.size.width)
           };
         } else {
           this.imgWidth = modePosition.size.width + this.getUIContext().vp2px(this.marginRight); // 计算出图片的宽度
           this.calcWordsInfo();
           return {
             'left': this.getUIContext().px2vp(modePosition.windowOffset.x),
             'width': this.getUIContext().px2vp(modePosition.size.width)
           };
         }
       } catch (error) {
         return { 'left': 0, 'width': 0 };
       }
     }

     build() {
       Scroll() {
         Column() {
           RelativeContainer() {
             Text() {
               ImageSpan($r('sys.media.app_lock_picture'))
                 .height(18)
                 .margin({ right: this.marginRight })
                 .verticalAlign(ImageSpanAlignment.CENTER)
                 .offset({
                   x: 0,
                   y: 2
                 })
                 .padding(1)
                 .id('image');
               Span(this.text)
                 .fontSize(19)
                 .lineHeight(this.lineHeight);
             }
             .onAreaChange((oldValue: Area, newValue: Area) => {
               console.info('testTag', `获取到oldValue、newValue:${oldValue.width}、${newValue.width}`);
               this.getTextInfo('targetText');
               this.getTextInfo('image');
             })
             .id('targetText');
             if (this.textBox.length > 0) {
               Canvas(this.context).onReady(() => {
                 this.textBox.forEach((line: line) => {
                   this.context.lineCap = 'round'; // 设置线条圆角
                   this.context.beginPath();
                   this.context.lineWidth = 2; // 设置线条宽度
                   this.context.strokeStyle = '#0a59F7'; // 设置线条颜色
                   this.context.moveTo(line.start.x, line.start.y);
                   this.context.lineTo(line.end.x, line.end.y);
                   this.context.stroke();
                 });
               })
                 .alignRules({
                   // 指定设置在相对容器中子组件的对齐规则
                   top: { anchor: 'targetText', align: VerticalAlign.Top },
                   left: { anchor: 'targetText', align: HorizontalAlign.Start },
                   right: { anchor: 'targetText', align: HorizontalAlign.End },
                   bottom: { anchor: 'targetText', align: VerticalAlign.Bottom }
                 });
             }
           };
         }
         .width('100%')
         .padding({
           top: 20,
           right: 16,
           bottom: 12,
           left: 16
         });
       };
     }
   }
   ```
