---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-614
title: 使用Canvas绘制阅读页，并实现文字选中与评论功能
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 使用Canvas绘制阅读页，并实现文字选中与评论功能
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:26+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:a89a7f1f20adbeefed4ceb3aa04d50fab4754efc6400cde80de24b97877ac317
---

## 问题现象

利用Canvas绘制阅读页面，并且支持文字选中弹出菜单，支持点击查看评论，该场景如何实现？

## 背景知识

* [DrawingRenderingContext](../harmonyos-references/ts-drawingrenderingcontext.md)：DrawingRenderingContext对象与Canvas组件绑定后，可在Canvas组件上进行绘制，绘制对象可以是形状、文本、图片等。
* [@ohos.graphics.text (文本模块)](../harmonyos-references/js-apis-graphics-text.md)：提供一系列用于文本布局和字体管理的编程接口。
* [组合手势](../harmonyos-references/ts-combined-gestures.md)：手势识别组合，即两种及以上手势组合为复合手势，支持顺序识别、并发识别和互斥识别。

## 解决方案

该场景可以利用Canvas结合文本模块绘制出段落，然后在Canvas上绑定长按手势实现文字选中以及单击手势实现查看评论，具体步骤如下：

1. 页面初始化时，拆分文本段落。

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
2. 绘制文本以及可点击的矩形用于查看评论。

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
3. 绑定长按手势，通过isShowPopup变量控制是否弹出选中菜单。

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
4. 绑定单击手势，通过isShowSheet变量控制是否弹出评论模态框。

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
