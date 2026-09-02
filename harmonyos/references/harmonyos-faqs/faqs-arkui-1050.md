---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1050
title: 基于属性字符串实现Span的边框效果
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 基于属性字符串实现Span的边框效果
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:27+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:32b8cbcdd02e98d97a87510be87715102e112d327a202b26dc7888216b33336f
---

## 问题现象

在HarmonyOS开发中，由于Span组件本身不支持设置margin、padding等布局属性，开发者可以通过属性字符串（StyledString）实现类似效果。

## 背景知识

* ArkUI提供轻量的UI元素复用机制[@Builder](../harmonyos-guides/arkts-builder.md)，其内部UI结构固定，仅与使用方进行数据传递。开发者可将重复使用的UI元素抽象成函数，在build函数中调用。
* 将[StyledString](../harmonyos-references/ts-universal-styled-string.md)应用到文本组件上，可以采用多种方式修改文本，包括调整字号、添加字体颜色、使文本具备可点击性，以及通过自定义方式绘制文本等。

## 解决方案

* 可以通过以下几点达成最终效果：
  1. 路径计算：定义calculateArcPoints方法，该方法用于生成圆弧边框的路径坐标点，确保边框形状符合预期。
  2. 自定义Span绘制：绘制边框与文本，在onDraw方法中调用canvas.drawPath绘制边框路径，并同步渲染文本内容。
  3. 样式绑定：将生成的styledString通过setStyledString方法设置到Text组件。

* 具体代码实现如下：

  ```ts
  import { DrawContext } from '@ohos.arkui.node';
  import { drawing } from '@kit.ArkGraphics2D';

  interface Point {
    x: number;
    y: number;
  }

  function calculateArcPoints(
    start: Point,
    end: Point,
    center: Point,
    numPoints: number = 20
  ): Point[] {
    const startVec: Point = {
      x: start.x - center.x,
      y: start.y - center.y
    };
    const endVec: Point = {
      x: end.x - center.x,
      y: end.y - center.y
    };
    const radius = Math.hypot(startVec.x, startVec.y);
    let thetaStart = Math.atan2(startVec.y, startVec.x);
    let thetaEnd = Math.atan2(endVec.y, endVec.x);

    if (thetaEnd < thetaStart) {
      thetaEnd += 2 * Math.PI;
    }
    const angleDiff = thetaEnd - thetaStart;

    const angles = Array.from({ length: numPoints + 1 }, (item: undefined, i) =>
    thetaStart + angleDiff * (i / numPoints)
    );
    let arr: Point[] = [];
    angles.forEach(item => {
      arr.push({
        x: center.x + radius * Math.cos(item),
        y: center.y + radius * Math.sin(item)
      });
    });
    return arr;
  }

  class MyCustomSpan extends CustomSpan {
    width: number = 300;
    word: string = '';
    height: number = 300;
    strokeWidth: number = 5;
    uiContext: UIContext | undefined = undefined;

    constructor(uiContext: UIContext, word: string, width: number, height: number, strokeWidth: number) {
      super();
      this.word = word;
      this.width = width;
      this.height = height;
      this.strokeWidth = strokeWidth;
      this.uiContext = uiContext;
    }

    onMeasure(): CustomSpanMetrics {
      return { width: this.width, height: this.height };
    }

    onDraw(context: DrawContext) {
      const canvas = context.canvas;

      const pen = new drawing.Pen();
      pen.setStrokeWidth(this.strokeWidth);
      pen.setColor({
        alpha: 255,
        red: 255,
        green: 0,
        blue: 0
      });
      let path = new drawing.Path();
      path.moveTo(this.uiContext?.vp2px(15), this.uiContext?.vp2px(5));

      let rightTopArr =
        calculateArcPoints({ x: this.width - 15, y: 5 }, { x: this.width - 10, y: 10 }, { x: this.width - 15, y: 10 });
      rightTopArr.forEach(item => {
        path.lineTo(this.uiContext?.vp2px(item.x), this.uiContext?.vp2px(item.y));
      });

      let rightBottomArr =
        calculateArcPoints({ x: this.width - 10, y: 20 }, { x: this.width - 15, y: 25 }, { x: this.width - 15, y: 20 });
      rightBottomArr.forEach(item => {
        path.lineTo(this.uiContext?.vp2px(item.x), this.uiContext?.vp2px(item.y));
      });

      let leftBottomArr = calculateArcPoints({ x: 15, y: 25 }, { x: 10, y: 20 }, { x: 15, y: 20 });
      leftBottomArr.forEach(item => {
        path.lineTo(this.uiContext?.vp2px(item.x), this.uiContext?.vp2px(item.y));
      });

      let leftTopArr = calculateArcPoints({ x: 10, y: 10 }, { x: 15, y: 5 }, { x: 15, y: 10 });
      leftTopArr.forEach(item => {
        path.lineTo(this.uiContext?.vp2px(item.x), this.uiContext?.vp2px(item.y));
      });
      path.close();
      canvas.attachPen(pen);
      canvas.drawPath(path);
      const font = new drawing.Font();
      font.setSize(45);
      const textBlob =
        drawing.TextBlob.makeFromString(this.word, font, drawing.TextEncoding.TEXT_ENCODING_UTF8);
      canvas.drawTextBlob(textBlob, 50, 65);
      canvas.detachPen();
    }
  }

  @Entry
  @Component
  struct StyledStringWithBorder {
    message: string = 'TESTING';
    strokeWidth: number = 5;
    borderW: number = 100;
    uiContext: UIContext = this.getUIContext();
    customSpan: MyCustomSpan = new MyCustomSpan(this.uiContext, this.message, 100, 30, 5);
    style: MutableStyledString = new MutableStyledString(this.customSpan);
    textController: TextController = new TextController();
    controller: TextInputController = new TextInputController();

    @Builder
    customInput(title: string, upValue: string, type: number) {
      Row() {
        Text(title)
          .width('25%')
          .height(40)
          .textAlign(TextAlign.Center)
          .margin(10);
        TextInput({ text: upValue!!, placeholder: 'input your word...', controller: this.controller })
          .placeholderColor(Color.Grey)
          .placeholderFont({ size: 14, weight: 400 })
          .caretColor(Color.Blue)
          .width('60%')
          .height(40)
          .margin(10)
          .fontSize(14)
          .fontColor(Color.Black)
          .onChange((value) => {
            if (type === 1) {
              this.message = value;
            } else if (type === 2) {
              this.strokeWidth = parseInt(value);
            } else if (type === 3) {
              this.borderW = parseInt(value);
            }
          })
          .inputFilter(type === 1 ? '*' : '[0-9]', (e) => {
            console.info(JSON.stringify(e));
          });
      }
      .width('75%');
    }

    build() {
      Column() {
        Row() {
          Text(undefined, { controller: this.textController })
            .copyOption(CopyOptions.InApp);
        }
        .height('20%');

        this.customInput('输入文本', this.message, 1);
        this.customInput('画笔线宽', this.strokeWidth + '', 2);
        this.customInput('标签总长', this.borderW + '', 3);

        Button('属性字符串生成')
          .margin(10)
          .onClick(() => {
            this.customSpan = new MyCustomSpan(this.uiContext, this.message, this.borderW, 30, this.strokeWidth);
            this.style = new MutableStyledString(this.customSpan);
            this.textController.setStyledString(this.style);
          });
      }
      .height('100%')
      .width('100%');
    }
  }
  ```
