---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/arkui-uimana-faq-0014
title: ArkUI-Canvas组件绘制功能常见问题
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 常见问题 > ArkUI-Canvas组件绘制功能常见问题
category: harmonyos-faqs
scraped_at: 2026-10-21T07:11:10+08:00
doc_updated_at: 2026-10-20
content_hash: sha256:381c3ad3b8c56f808aa79ad3d382850a049c4feb99288f196effd506acdff2c0
---

**Q：如何使用canvas绘制圆角矩形？**

A：利用[CanvasRenderingContext2D](../harmonyos-references/ts-canvasrenderingcontext2d.md)对象的arc绘制弧形路径，结合lineTo方法绘制直线，参考代码如下：

```ts
@Entry
@Component
struct CanvasDrawRoundedRectangle {
  private readonly settings: RenderingContextSettings = new RenderingContextSettings(true);
  private readonly ctx: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);

  drawRoundRect(x: number, y: number, width: number, height: number, radius: number, strokeColor?: string,
    fillColor?: string, lineDash?: Array<number>) {
    if (width < 2 * radius || height < 2 * radius) {
      radius = Math.min(width, height) / 2;
    }
    strokeColor = strokeColor || '#333';
    lineDash = lineDash ||
```

**Q：如何基于Canvas实现六边形雷达图以展示不同能力的数据？**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fc/v3/ZyAWsCo2TsCoW43tD3qySg/zh-cn_image_0000002765922228.png "点击放大")

**A**：实现方法如下：

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

**Q：通过Canvas绘制填充类文本时，如何实现整体文字的对齐方式？例如居中、居右或者居左？**

**A**：实现在Canvas上绘制不同对齐方式的文字，具体方法如下：

1. 创建RenderingContextSettings和CanvasRenderingContext2D对象，用于配置和管理Canvas的渲染上下文。同时定义leftText、centerText和rightText三个变量，分别用于展示左对齐、居中对齐和右对齐的文字内容；letterSpacing用于设置字符间距；lineX用于标识参考线的水平位置。

   ```ts
   private settings: RenderingContextSettings = new RenderingContextSettings(true);
     private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
     private leftText: string = '文字左对齐';
     private centerText: string = '文字居中对齐';
     private rightText: string = '文字右对齐';
     private letterSpacing: number = 1;
     private lineX: number = 200;
   ```
2. getTotalWidth方法用于计算指定文本的总宽度，其实现方式为逐个遍历文本中的字符，并累加每个字符的宽度及其对应的间距，最终得到文本整体的宽度总和。

   ```ts
   getTotalWidth(text: string): number {
       let totalWidth = 0;
       for (let i = 0; i < text.length; i++) {
         // 累计已占用宽度
         if (i === text.length - 1) {
           totalWidth += this.context.measureText(text[i]).width;
         } else {
           totalWidth += this.context.measureText(text[i]).width + this.letterSpacing;
         }
       }
       return totalWidth;
     }
   ```
3. 在Canvas的onReady事件中，首先将画笔颜色设置为蓝色，并绘制一条参考线作为对齐基准。随后，在该事件处理函数中，通过计算确定文本的绘制位置，并利用循环调用fillText方法，依次绘制具有不同对齐方式的文本内容：
   * 左对齐：通过累加每个字符的宽度和间距，确定文字绘制的起始位置。

     ```ts
     let leftTotalWidth = this.lineX;
               this.context.font = '24vp sans-serif';
               for (let i = 0; i < this.leftText.length; i++) {
                 this.context.fillText(this.leftText[i], leftTotalWidth, 50);
                 // 累计已占用宽度
                 if (i === this.leftText.length - 1) {
                   leftTotalWidth += this.context.measureText(this.leftText[i]).width;
                 } else {
                   leftTotalWidth += this.context.measureText(this.leftText[i]).width + this.letterSpacing;
                 }
               }
     ```
   * 居中对齐：先计算文本的总宽度，然后将起始位置设置为（lineX-总宽度一半），以实现居中对齐。

     ```ts
     let centerTotalWidth = 0;
               centerTotalWidth = this.getTotalWidth(this.centerText);
               centerTotalWidth = this.lineX - centerTotalWidth / 2;
               for (let i = 0; i < this.centerText.length; i++) {
                 this.context.fillText(this.centerText[i], centerTotalWidth, 90);
                 // 累计已占用宽度
                 if (i === this.centerText.length - 1) {
                   centerTotalWidth += this.context.measureText(this.centerText[i]).width;
                 } else {
                   centerTotalWidth += this.context.measureText(this.centerText[i]).width + this.letterSpacing;
                 }
               }
     ```
   * 右对齐：先计算文本的总宽度，然后将起始位置设置为（lineX-总宽度），以实现右对齐。

     ```ts
     let rightTotalWidth = 0;
               rightTotalWidth = this.getTotalWidth(this.rightText);
               rightTotalWidth = this.lineX - rightTotalWidth;
               for (let i = 0; i < this.rightText.length; i++) {
                 this.context.fillText(this.rightText[i], rightTotalWidth, 130);
                 // 累计已占用宽度
                 if (i === this.rightText.length - 1) {
                   rightTotalWidth += this.context.measureText(this.rightText[i]).width;
                 } else {
                   rightTotalWidth += this.context.measureText(this.rightText[i]).width + this.letterSpacing;
                 }
               }
     ```

完整示例参考如下：

```screen
@Entry
@Component
struct Index {
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  private leftText: string = '文字左对齐';
  private centerText: string = '文字居中对齐';
  private rightText: string = '文字右对齐';
  private letterSpacing: number = 1;
  private lineX: number = 200;
  getTotalWidth(text: string): number {
    let totalWidth = 0;
    for (let i = 0; i < text.length; i++) {
      // 累计已占用宽度
      if (i === text.length - 1) {
        totalWidth += this.context.measureText(text[i]).width;
      } else {
        totalWidth += this.context.measureText(text[i]).width + this.letterSpacing;
      }
    }
    return totalWidth;
  }
  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor(Color.White)
        .onReady(() => {
          this.context.strokeStyle = Color.Black;
          this.context.moveTo(this.lineX, 10);
          this.context.lineTo(this.lineX, 160);
          this.context.stroke();
          // 左对齐
          let leftTotalWidth = this.lineX;
          this.context.font = '24vp sans-serif';
          for (let i = 0; i < this.leftText.length; i++) {
            this.context.fillText(this.leftText[i], leftTotalWidth, 50);
            // 累计已占用宽度
            if (i === this.leftText.length - 1) {
              leftTotalWidth += this.context.measureText(this.leftText[i]).width;
            } else {
              leftTotalWidth += this.context.measureText(this.leftText[i]).width + this.letterSpacing;
            }
          }
          // 居中对齐
          let centerTotalWidth = 0;
          centerTotalWidth = this.getTotalWidth(this.centerText);
          centerTotalWidth = this.lineX - centerTotalWidth / 2;
          for (let i = 0; i < this.centerText.length; i++) {
            this.context.fillText(this.centerText[i], centerTotalWidth, 90);
            // 累计已占用宽度
            if (i === this.centerText.length - 1) {
              centerTotalWidth += this.context.measureText(this.centerText[i]).width;
            } else {
              centerTotalWidth += this.context.measureText(this.centerText[i]).width + this.letterSpacing;
            }
          }
          // 右对齐
          let rightTotalWidth = 0;
          rightTotalWidth = this.getTotalWidth(this.rightText);
          rightTotalWidth = this.lineX - rightTotalWidth;
          for (let i = 0; i < this.rightText.length; i++) {
            this.context.fillText(this.rightText[i], rightTotalWidth, 130);
            // 累计已占用宽度
            if (i === this.rightText.length - 1) {
              rightTotalWidth += this.context.measureText(this.rightText[i]).width;
            } else {
              rightTotalWidth += this.context.measureText(this.rightText[i]).width + this.letterSpacing;
            }
          }
          })
        .margin({top:125})
    }
    .width('100%')
    .height('100%')
  }
}
```

代码运行效果图如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dd/v3/j2HrrkjwS6SLkrvrgXSaZA/zh-cn_image_0000002795480725.png "点击放大")

**Q：将UI组件绘制到Canvas上后，如何截取Canvas获取图片？**

**A**：使用[getPixelMap](../harmonyos-references/ts-canvasrenderingcontext2d.md#getpixelmap)方法即可。

**Q：解决方案里的方法能够实现多行文字的对齐效果吗？**

**A**：不能，解决方案是通过绘制参考线，计算和参考线的距离来实现对齐效果，仅供参考，使用多行文字会无法显示完整文字。

**Q：Canvas如何实现橡皮擦效果，清除已绘制的路径？具体演示如下：**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dc/v3/ioClJi4MTrKyg_Jdnvrtjw/zh-cn_image_0000002795480865.png "点击放大")

**A**：基于图层叠加实现橡皮擦效果，思路如下：

1. 用Canvas创建画布，设置属性，如宽高，背景等，并在onReady回调里完成画笔线宽，颜色，绘制路径等初始化。
2. 在onTouch回调里，根据TouchEvent的枚举类型，在枚举类型为Down时记录绘制路径，Move时实现路径绘制。
3. 使用globalCompositeOperation设置图层叠加模式，设置画笔大小，实现橡皮擦效果。

完整示例如下：

```ts
@Entry
@Component
struct CanvasDemo {
  @State paintSize: number = 5; // 当前画笔大小
  @State paintColor: Color = Color.Black; // 当前画笔颜色
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  canvasContext: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  tempPath: Path2D = new Path2D();
  @State pathArray: Array<Path2D | undefined> = []; // 所有画图路径信息
  @State text: string = '';
  @State eventType: string = '';

  build() {
    Column({ space: 7 }) {
      Row() {
        Button('橡皮擦')
          .onClick(() => {
            this.canvasContext.globalCompositeOperation = 'destination-out';
            this.paintSize = 150;
          })
        Button('画笔')
          .onClick(() => {
            this.canvasContext.globalCompositeOperation = 'source-over';
            this.paintSize = 5;
          })

        Button('清屏')
          .onClick(() => {
            this.canvasContext.clearRect(0, 0, 360, 720);
          })
      }
      .margin({ top: 25 })
      .width('100%')
      .justifyContent(FlexAlign.SpaceEvenly)

      Stack({ alignContent: Alignment.Top }) {
        Canvas(this.canvasContext)
          .width('100%')
          .height('100%')
          .backgroundColor('#bacaf3')
          .onReady(() => {
            this.pathArray = [];
            this.canvasContext.strokeStyle = this.paintColor;
            this.canvasContext.lineWidth = this.paintSize;
            this.canvasContext.stroke(this.tempPath);
            for (let index = 0; index < this.pathArray.length; index++) {
              this.canvasContext.stroke(this.pathArray[index]);
            }
          })
          .onTouch((event?: TouchEvent) => {
            if (event) {
              if (event.type === TouchType.Down) {
                this.eventType = 'Down';
                this.canvasContext.beginPath();
                this.tempPath = new Path2D();
                this.pathArray.push(this.tempPath);
                this.tempPath.moveTo(event.touches[0].x, event.touches[0].y);
                this.canvasContext.moveTo(event.touches[0].x, event.touches[0].y);
              }
              if (event.type === TouchType.Up) {
                this.eventType = 'Up';
              }
              if (event.type === TouchType.Move) {
                this.eventType = 'Move';
                this.tempPath.lineTo(event.touches[0].x, event.touches[0].y);
                this.canvasContext.stroke(this.tempPath);
              }
              this.text = 'TouchType:' + this.eventType + '\n touch point and touch element:\nx: ' +
              event.touches[0].x + '\n' + 'y: ' + event.touches[0].y + '\nwidth:' + event.target.area.width +
                '\nheight:' + event.target.area.height + '\npathArray size:' +
              this.pathArray.length;
            }
          })
        Text(this.text);
      }
    }
  }
}
```

**Q：利用Canvas绘制阅读页面，并且支持文字选中弹出菜单，支持点击查看评论，该场景如何实现？**

**A**：该场景可以利用Canvas结合文本模块绘制出段落，然后在Canvas上绑定长按手势实现文字选中以及单击手势实现查看评论，具体步骤如下：

1. 页面初始化时，拆分文本段落：

   ```ts
   aboutToAppear(): void {
       this.initParagraph();
       window.getLastWindow(this.uiCtx.getHostContext())
         .then(win => {
           try {
             this.TOP_HEIGHT = win.getWindowAvoidArea(window.AvoidAreaType.TYPE_SYSTEM).topRect.height;
           } catch (error) {
             console.error('getWindowAvoidArea error');
           }
         });
     }

     initParagraph() {
       let myTextStyle: text.TextStyle = {
         color: {
           alpha: 255,
           red: 0,
           green: 0,
           blue: 0
         },
         fontSize: this.uiCtx.vp2px(16),
       };
       let myParagraphStyle: text.ParagraphStyle = {
         textStyle: myTextStyle,
         align: text.TextAlign.START,
       };
       let fontCollection = new text.FontCollection();
       CONTENT.split('\n').forEach((item, index) => {
         let paragraphBuilder = new text.ParagraphBuilder(myParagraphStyle, fontCollection);
         if (item == '') {
           return;
         }
         paragraphBuilder.addPlaceholder({
           width: (myTextStyle.fontSize ?? 0) * 2,
           height: (myTextStyle.fontSize ?? -2) + 2,
           align: text.PlaceholderAlignment.OFFSET_AT_BASELINE,
           baseline: text.TextBaseline.ALPHABETIC,
           baselineOffset: 0
         });
         paragraphBuilder.addText(item + '\n');
         this.paragraphs.push({
           content: item + '\n',
           paragraph: paragraphBuilder.build(),
           x: 0,
           y: 0,
           arguments: {
             content: [`第${index + 1}段评论`],
             x: 0,
             y: 0,
             width: 100,
             height: 0,
             color: '#000'
           }
         });
       });
     }
   ```
2. 绘制文本以及可点击的矩形用于查看评论：

   ```ts
   repaint() {
       // 绘制背景
       let brush = new drawing.Brush();
       brush.setColor({
         red: 255,
         green: 255,
         blue: 255,
         alpha: 255
       });
       this.ctx.canvas.drawBackground(brush);
       this.ctx.canvas.detachBrush();
       // 绘制文本
       this.paragraphs.filter(item => item.content.length > 1).forEach(item => {
         item.paragraph.paint(this.ctx.canvas, 0, this.scrollOffset + item.y);
         // 绘制评论
         this.paintArgs(item);
       });
       // 绘制高亮选中文本
       brush.setColor({
         red: 255,
         green: 255,
         blue: 0,
         alpha: 125
       });
       this.ctx.canvas.attachBrush(brush);
       this.textInfos.forEach(info => {
         info.textRects.forEach((item, index) => {
           this.ctx.canvas.drawRect(info.itemRect.left + item.left +
             ((index == 0 && info.itemRect.left + item.left == 0) ? 2 * this.uiCtx.vp2px(16) : 0),
             info.itemRect.top + this.scrollOffset + item.top + info.yOffset, info.itemRect.left + item.right,
             info.itemRect.top + this.scrollOffset + item.bottom);
         });
       });
       this.ctx.canvas.detachBrush();
       this.ctx.invalidate();
     }
   ```
3. 绑定长按手势，通过isShowPopup变量控制是否弹出选中菜单：

   ```ts
   // 长按手势
                 LongPressGesture({ fingers: 1 })
                   .onAction(event => {
                     this.getCaretInfo(this.uiCtx.vp2px(event.fingerList[0].localX),
                       this.uiCtx.vp2px(event.fingerList[0].localY),
                       this.caret1, true);
                     this.caret2.listItemIndex = this.caret1.listItemIndex;
                     this.caret2.caretIndex = this.paragraphs[this.caret2.listItemIndex].content.length;
                     this.getTextInfos(this.caret1, this.caret2);
                     this.targetPopupInfo.x = this.uiCtx.px2vp(this.paragraphs[this.caret1.listItemIndex].x);
                     this.targetPopupInfo.y =
                       this.uiCtx.px2vp(this.paragraphs[this.caret1.listItemIndex].y + this.scrollOffset);
                     this.targetPopupInfo.width =
                       this.uiCtx.px2vp(this.paragraphs[this.caret1.listItemIndex].paragraph.getMaxWidth());
                     this.targetPopupInfo.height =
                       this.uiCtx.px2vp(this.paragraphs[this.caret1.listItemIndex].paragraph.getHeight() -
                         (this.paragraphs[this.caret1.listItemIndex].paragraph.getLineMetrics(
                           this.paragraphs[this.caret1.listItemIndex].paragraph.getLineCount() - 1)?.height ?? 0));
                     this.isShowPopup = true;
                     this.repaint();
                   }),
   ```
4. 绑定单击手势，通过isShowSheet变量控制是否弹出评论模态框：

   ```ts
   // 单击手势
                 TapGesture({ fingers: 1, count: 1 })
                   .onAction(event => {
                     if (event.fingerList.length <= 0) {
                       return;
                     }
                     let eventX = this.uiCtx.vp2px(event.fingerList[0].localX);
                     let eventY = this.uiCtx.vp2px(event.fingerList[0].localY) - this.scrollOffset;
                     let clickParagraph = this.paragraphs.filter((item) => {
                       return item.x <= eventX && eventX <= item.x + item.paragraph.getMaxWidth() && eventY >= item.y &&
                         eventY <= item.y + item.paragraph.getHeight();
                     });
                     if (clickParagraph.length <= 0) {
                       console.info('没有点击在任何段落上');
                       return;
                     }
                     if (clickParagraph[0].x + clickParagraph[0].arguments.x <= eventX &&
                       eventX <= clickParagraph[0].x + clickParagraph[0].arguments.x + clickParagraph[0].arguments.width &&
                       clickParagraph[0].y + clickParagraph[0].arguments.y <= eventY &&
                       eventY <= clickParagraph[0].y + clickParagraph[0].arguments.y + clickParagraph[0].arguments.height
                     ) {
                       this.clickArgument = clickParagraph[0].arguments;
                       this.isShowSheet = true;
                     } else {
                       console.info('没有点击在评论上');
                     }
                   })
   ```

完整示例参考如下：

```ts
import { LengthMetricsUnit, window } from '@kit.ArkUI';
import { common2D, drawing, text } from '@kit.ArkGraphics2D';

// 这里文本仅演示使用
const CONTENT: string =
  `明月出天山，苍茫云海间\n` +
    `长风几万里，吹度玉门关\n` +
    `汉下白登道，胡窥青海湾\n` +
    `由来征战地，不见有人还\n` +
    `金樽清酒斗十千，玉盘珍羞直万钱\n` +
    `停杯投箸不能食，拔剑四顾心茫然\n` +
    `欲渡黄河冰塞川，将登太行雪满山\n` +
    `闲来垂钓碧溪上，忽复乘舟梦日边\n` +
    `君不见黄河之水天上来\n` +
    `奔流到海不复回\n` +
    `君不见高堂明镜悲白发\n` +
    `朝如青丝暮成雪\n` +
    `仰天大笑出门去，我辈岂是蓬蒿人\n` +
    `十步杀一人，千里不留行\n` +
    `事了拂衣去，深藏身与名\n` +
    `闲过信陵饮，脱剑膝前横\n` +
    `云想衣裳花想容，春风拂槛露华浓\n` +
    `若非群玉山头见，会向瑶台月下逢\n` +
    `名花倾国两相欢，长得君王带笑看\n` +
    `解释春风无限恨，沉香亭北倚阑干\n` +
    `浮云游子意，落日故人情\n` +
    `挥手自兹去，萧萧班马鸣\n` +
    `我本楚狂人，凤歌笑孔丘\n` +
    `手持绿玉杖, 朝别黄鹤楼\n` +
    `天地一逆旅, 同悲万古尘\n` +
    `月下飞天镜, 云生结海楼\n` +
    `仍怜故乡水, 万里送行舟\n` +
    `挥手自兹去, 萧萧班马鸣\n`;

interface ParagraphInfo {
  content: string,
  paragraph: text.Paragraph,
  x: number,
  y: number,
  arguments: Argument
}

interface TargetInfo {
  x: number,
  y: number,
  width: number,
  height: number
}

interface Argument {
  content: string[],
  x: number,
  y: number,
  width: number,
  height: number,
  color: ResourceColor
}

@ObservedV2
class CaretInfo {
  listItemIndex: number = -1;
  caretIndex: number = -1;
  @Trace position: Position = { x: -100, y: -100 };

  lessThan(another: CaretInfo) {
    return !(this.listItemIndex > another.listItemIndex) &&
      (this.listItemIndex < another.listItemIndex || this.caretIndex < another.caretIndex);
  }
}

// 文本信息
class TextInfo {
  index: number;
  itemRect: common2D.Rect;
  textRects: common2D.Rect[] = [];
  start: number;
  end: number;
  yOffset: number;

  constructor(index: number, itemRect: common2D.Rect, textRects: common2D.Rect[], start: number, end: number,
    yOffset: number) {
    this.index = index;
    this.itemRect = itemRect;
    this.textRects = textRects;
    this.start = start;
    this.end = end;
    this.yOffset = yOffset;
  }

  getPosition(isEnd: boolean = true, uiCtx: UIContext): Position | undefined {
    if (this.textRects.length <= 0) {
      return;
    }
    if (isEnd) {
      return {
        x: uiCtx.px2vp(this.itemRect.left + this.textRects[this.textRects.length - 1].right) - 10,
        y: uiCtx.px2vp(this.itemRect.top + this.textRects[this.textRects.length - 1].top)
      };
    } else {
      return {
        x: uiCtx.px2vp(this.itemRect.left + this.textRects[0].left +
          (this.textRects[0].left == 0 ? uiCtx.vp2px(16) * 2 : 0)) - 10,
        y: uiCtx.px2vp(this.itemRect.top + this.textRects[0].top)
      };
    }
  }
}

@Entry
@Component
struct CanvasDrawParagraph {
  private ctx = new DrawingRenderingContext(LengthMetricsUnit.PX);
  private paragraphs: ParagraphInfo[] = [];
  private scrollOffset: number = 0;
  private lastScrollOffset: number = 0;
  private selectedParagraphIndex: number = -1;
  private textInfos: TextInfo[] = [];
  private TOP_HEIGHT: number = 0;
  private caret1: CaretInfo = new CaretInfo();
  private caret2: CaretInfo = new CaretInfo();
  private uiCtx: UIContext = this.getUIContext();
  @State isShowPopup: boolean = false;
  @State isShowSheet: boolean = false;
  @State clickArgument?: Argument = undefined;
  @State targetPopupInfo: TargetInfo = {
    x: 0,
    y: 0,
    width: 0,
    height: 0
  };

  @Builder
  popupBuilder() {
    Row({ space: 10 }) {
      ForEach([0, 1, 2, 3], (item: number) => {
        Text(`菜单${item}`);
      });
    };
  }

  @Builder
  commandBuilder(argument: Argument) {
    Column() {
      ForEach(argument.content, (item: string) => {
        Text(item);
      });
    };
  }

  aboutToAppear(): void {
    this.initParagraph();
    window.getLastWindow(this.uiCtx.getHostContext())
      .then(win => {
        try {
          this.TOP_HEIGHT = win.getWindowAvoidArea(window.AvoidAreaType.TYPE_SYSTEM).topRect.height;
        } catch (error) {
          console.error('getWindowAvoidArea error');
        }
      });
  }

  initParagraph() {
    let myTextStyle: text.TextStyle = {
      color: {
        alpha: 255,
        red: 0,
        green: 0,
        blue: 0
      },
      fontSize: this.uiCtx.vp2px(16),
    };
    let myParagraphStyle: text.ParagraphStyle = {
      textStyle: myTextStyle,
      align: text.TextAlign.START,
    };
    let fontCollection = new text.FontCollection();
    CONTENT.split('\n').forEach((item, index) => {
      let paragraphBuilder = new text.ParagraphBuilder(myParagraphStyle, fontCollection);
      if (item == '') {
        return;
      }
      paragraphBuilder.addPlaceholder({
        width: (myTextStyle.fontSize ?? 0) * 2,
        height: (myTextStyle.fontSize ?? -2) + 2,
        align: text.PlaceholderAlignment.OFFSET_AT_BASELINE,
        baseline: text.TextBaseline.ALPHABETIC,
        baselineOffset: 0
      });
      paragraphBuilder.addText(item + '\n');
      this.paragraphs.push({
        content: item + '\n',
        paragraph: paragraphBuilder.build(),
        x: 0,
        y: 0,
        arguments: {
          content: [`第${index + 1}段评论`],
          x: 0,
          y: 0,
          width: 100,
          height: 0,
          color: '#000'
        }
      });
    });
  }
  repaint() {
    // 绘制背景
    let brush = new drawing.Brush();
    brush.setColor({
      red: 255,
      green: 255,
      blue: 255,
      alpha: 255
    });
    this.ctx.canvas.drawBackground(brush);
    this.ctx.canvas.detachBrush();
    // 绘制文本
    this.paragraphs.filter(item => item.content.length > 1).forEach(item => {
      item.paragraph.paint(this.ctx.canvas, 0, this.scrollOffset + item.y);
      // 绘制评论
      this.paintArgs(item);
    });
    // 绘制高亮选中文本
    brush.setColor({
      red: 255,
      green: 255,
      blue: 0,
      alpha: 125
    });
    this.ctx.canvas.attachBrush(brush);
    this.textInfos.forEach(info => {
      info.textRects.forEach((item, index) => {
        this.ctx.canvas.drawRect(info.itemRect.left + item.left +
          ((index == 0 && info.itemRect.left + item.left == 0) ? 2 * this.uiCtx.vp2px(16) : 0),
          info.itemRect.top + this.scrollOffset + item.top + info.yOffset, info.itemRect.left + item.right,
          info.itemRect.top + this.scrollOffset + item.bottom);
      });
    });
    this.ctx.canvas.detachBrush();
    this.ctx.invalidate();
  }
  // 绘制评论数气泡
  paintArgs(paragraph: ParagraphInfo) {
    let pen = new drawing.Pen();
    pen.setColor({
      red: 255,
      green: 0,
      blue: 0,
      alpha: 255
    });
    this.ctx.canvas.attachPen(pen);
    this.ctx.canvas.drawRoundRect(new drawing.RoundRect({
      left: paragraph.x + paragraph.arguments.x,
      right: paragraph.x + paragraph.arguments.x + paragraph.arguments.width,
      top: paragraph.y + paragraph.arguments.y + this.scrollOffset,
      bottom: paragraph.y + paragraph.arguments.y + paragraph.arguments.height + this.scrollOffset
    }, 10, 10));
    this.ctx.canvas.detachPen();
  }

  getTextIndex(x: number, y: number, paragraph: text.Paragraph) {
    let lineCount = paragraph.getLineCount();
    let lineNum: number = -1;
    for (let i = 0; i < lineCount; i++) {
      let lineMetrics = paragraph.getLineMetrics(i)!;
      if (y >= lineMetrics.topHeight && y <= lineMetrics.topHeight + lineMetrics.height) {
        lineNum = i;
        break;
      }
    }
    // 获取文本度量
    let line = paragraph.getLineMetrics(lineNum)!;
    let textIndex: number = -1;
    if (x >= (line.left + line.width)) {
      return line.endIndex + 1;
    }
    for (let i = line.startIndex; i < line.endIndex; i++) {
      let rects = this.getRectForRange(i, line.endIndex, paragraph);
      if (x < rects[0].left) {
        textIndex = i - 1;
        break;
      }
    }
    return textIndex;
  }

  getCaretInfo(x: number, y: number, info: CaretInfo, isLongGesture = false): void {
    info.listItemIndex = this.getSelectedIndex(y);
    let paragraph = this.paragraphs[info.listItemIndex].paragraph;
    let itemRect: common2D.Rect = {
      left: this.paragraphs[info.listItemIndex].x,
      top: this.paragraphs[info.listItemIndex].y + this.scrollOffset,
      right: this.paragraphs[info.listItemIndex].x + paragraph.getMaxWidth(),
      bottom: this.paragraphs[info.listItemIndex].y + this.scrollOffset + paragraph.getHeight()
    };
    let textIndex = this.getTextIndex(x - itemRect.left, y - itemRect.top, paragraph);
    info.caretIndex = isLongGesture ? 0 : textIndex;
  }

  getRectForRange(start: number, end: number, paragraph: text.Paragraph) {
    return paragraph.getRectsForRange({ start: start, end: end }, text.RectWidthStyle.TIGHT, text.RectHeightStyle.TIGHT)
      .map(item => item.rect);
  }

  getTextInfos(start: CaretInfo, end: CaretInfo) {
    this.textInfos = [];
    for (let i = start.listItemIndex; i <= end.listItemIndex; i++) {
      let paragraph = this.paragraphs[i].paragraph;
      let itemRect: common2D.Rect = {
        left: this.paragraphs[i].x,
        top: this.paragraphs[i].y + this.scrollOffset,
        right: this.paragraphs[i].x + paragraph.getMaxWidth(),
        bottom: this.paragraphs[i].y + this.scrollOffset + paragraph.getHeight()
      };
      let startIndex = start.listItemIndex == i ? start.caretIndex : 0;
      let endIndex = end.listItemIndex == i ? end.caretIndex : this.paragraphs[i].content.length;
      let rects = this.getRectForRange(startIndex, endIndex, paragraph);
      this.textInfos.push(new TextInfo(i, itemRect, rects, startIndex, endIndex, this.scrollOffset));
    }
    if (this.textInfos.length <= 0) {
      return;
    }
    let startCaretPosition = this.textInfos[0].getPosition(false, this.uiCtx);
    let endCaretPosition = this.textInfos[this.textInfos.length - 1].getPosition(true, this.uiCtx);
    if (startCaretPosition) {
      start.position = startCaretPosition;
    }
    if (endCaretPosition) {
      end.position = endCaretPosition;
    }
    this.repaint();
  }

  getSelectedIndex(y: number) {
    let item: ParagraphInfo;
    for (let i = 0; i < this.paragraphs.length; i++) {
      item = this.paragraphs[i];
      if (y > item.y + this.scrollOffset && y <= item.y + this.scrollOffset + item.paragraph.getHeight()) {
        return i;
      }
    }
    return -1;
  }

  build() {
    RelativeContainer() {
      Stack() {
        Canvas(this.ctx)
          .bindSheet($$this.isShowSheet, this.commandBuilder(this.clickArgument!))
          .onReady(() => {
            let preHeight = 0;
            this.paragraphs.forEach(item => {
              item.paragraph.layoutSync(this.ctx.size.width);
              item.x = 0;
              item.y = preHeight;
              preHeight += item.paragraph.getHeight();
              let line = item.paragraph.getLineMetrics(item.paragraph.getLineCount() - 2);
              if (line) {
                item.arguments.height = line.height;
                if (line.left + line.width + item.arguments.width > this.ctx.size.width) {
                  item.arguments.x = 0;
                  item.arguments.y = line.topHeight + line.height;
                } else {
                  item.arguments.x = line.left + line.width;
                  item.arguments.y = line.topHeight;
                }
              }
            });
            // 绘制
            this.repaint();
          })
          .gesture(
            GestureGroup(GestureMode.Exclusive,
              // 滑动手势
              PanGesture({ fingers: 1, direction: PanDirection.Vertical })
                .onActionStart(() => {
                  this.lastScrollOffset = this.scrollOffset;
                })
                .onActionUpdate(event => {
                  this.scrollOffset = this.lastScrollOffset + this.uiCtx.vp2px(event.offsetY);
                  this.repaint();
                }),
              // 长按手势
              LongPressGesture({ fingers: 1 })
                .onAction(event => {
                  this.getCaretInfo(this.uiCtx.vp2px(event.fingerList[0].localX),
                    this.uiCtx.vp2px(event.fingerList[0].localY),
                    this.caret1, true);
                  this.caret2.listItemIndex = this.caret1.listItemIndex;
                  this.caret2.caretIndex = this.paragraphs[this.caret2.listItemIndex].content.length;
                  this.getTextInfos(this.caret1, this.caret2);
                  this.targetPopupInfo.x = this.uiCtx.px2vp(this.paragraphs[this.caret1.listItemIndex].x);
                  this.targetPopupInfo.y =
                    this.uiCtx.px2vp(this.paragraphs[this.caret1.listItemIndex].y + this.scrollOffset);
                  this.targetPopupInfo.width =
                    this.uiCtx.px2vp(this.paragraphs[this.caret1.listItemIndex].paragraph.getMaxWidth());
                  this.targetPopupInfo.height =
                    this.uiCtx.px2vp(this.paragraphs[this.caret1.listItemIndex].paragraph.getHeight() -
                      (this.paragraphs[this.caret1.listItemIndex].paragraph.getLineMetrics(
                        this.paragraphs[this.caret1.listItemIndex].paragraph.getLineCount() - 1)?.height ?? 0));
                  this.isShowPopup = true;
                  this.repaint();
                }),
              // 单击手势
              TapGesture({ fingers: 1, count: 1 })
                .onAction(event => {
                  if (event.fingerList.length <= 0) {
                    return;
                  }
                  let eventX = this.uiCtx.vp2px(event.fingerList[0].localX);
                  let eventY = this.uiCtx.vp2px(event.fingerList[0].localY) - this.scrollOffset;
                  let clickParagraph = this.paragraphs.filter((item) => {
                    return item.x <= eventX && eventX <= item.x + item.paragraph.getMaxWidth() && eventY >= item.y &&
                      eventY <= item.y + item.paragraph.getHeight();
                  });
                  if (clickParagraph.length <= 0) {
                    console.info('没有点击在任何段落上');
                    return;
                  }
                  if (clickParagraph[0].x + clickParagraph[0].arguments.x <= eventX &&
                    eventX <= clickParagraph[0].x + clickParagraph[0].arguments.x + clickParagraph[0].arguments.width &&
                    clickParagraph[0].y + clickParagraph[0].arguments.y <= eventY &&
                    eventY <= clickParagraph[0].y + clickParagraph[0].arguments.y + clickParagraph[0].arguments.height
                  ) {
                    this.clickArgument = clickParagraph[0].arguments;
                    this.isShowSheet = true;
                  } else {
                    console.info('没有点击在评论上');
                  }
                })
              )
          );

        Text()
          .width(this.targetPopupInfo.width)
          .height(this.targetPopupInfo.height)
          .position({ x: this.targetPopupInfo.x, y: this.targetPopupInfo.y })
          .bindPopup(this.isShowPopup!!, {
            builder: this.popupBuilder(),
          });

        this.caretBuilder(this.caret1);
        this.caretBuilder(this.caret2);
      };

    };
  }

  @Builder
  caretBuilder(info: CaretInfo) {
    Column() {
      Column()
        .width(1)
        .height(20)
        .backgroundColor('#f00');
      Column()
        .width(20)
        .aspectRatio(1)
        .borderRadius(10)
        .backgroundColor('#0f0');
    }
    .position(info.position)
    .gesture(
      PanGesture()
        .onActionStart(() => {

        })
        .onActionUpdate(event => {
          this.getCaretInfo(this.uiCtx.vp2px(event.fingerList[event.fingerList.length - 1].globalX),
            this.uiCtx.vp2px(event.fingerList[event.fingerList.length - 1].globalY) - this.TOP_HEIGHT, info);
          if (this.caret1.lessThan(this.caret2)) {
            this.getTextInfos(this.caret1, this.caret2);
          } else {
            this.getTextInfos(this.caret2, this.caret1);
          }
        })
    );
  }
}
```
