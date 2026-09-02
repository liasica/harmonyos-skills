---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1427
title: 如何给Span组件设置渐变背景色
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 如何给Span组件设置渐变背景色
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:10+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:eac59a1169678a4e416092ae6f7f45ddbfafd229ae62d3a442b341aa6def07bb
---

## 问题现象

Text里面的某个Span想设置一个渐变背景色，发现不生效，实现方式如下：

1. 给Span设置linearGradient属性，渐变色不生效。

   ```ts
   Text() {
     Span(this.goodsModel?.nameTag)
       .alignSelf(ItemAlign.Center)
       .width(30)
       .linearGradient({
         direction: GradientDirection.Right,
         colors: [[0xFFE574, 0], [0xFFC906, 1]]
       })
     Span(this.goodsModel?.goodsName)
   }
   ```
2. 通过CustomSpan自定义绘制Span，发现没有设置渐变色的方法。

   ```ts
   onDraw(context: DrawContext, options: CustomSpanDrawInfo) {
     let canvas = context.canvas;
     const brush = new drawing.Brush();
     // 此处是设置背景色的，但是没有设置渐变色的方法
     brush.setColor({ alpha: 255, red: 22, green: 22, blue: 22 });
     const font = new drawing.Font();
     font.setSize(25);
     const textBlob = drawing.TextBlob.makeFromString(this.word, font, drawing.TextEncoding.TEXT_ENCODING_UTF8);
     canvas.attachBrush(brush);
     canvas.drawRect({
       left: options.x+70,
       right: options.x + gUIContext.vp2px(this.width),
       top: options.lineTop ,
       bottom: options.lineBottom
     });
     brush.setColor({ alpha: 255, red: 255, green: 255, blue: 255 });
     canvas.attachBrush(brush);
     canvas.drawTextBlob(textBlob, options.x + 20, options.lineBottom - 15);
     canvas.detachBrush();
   }
   ```

如何给Span组件设置渐变的背景颜色？

## 背景知识

* [Span](../harmonyos-references/ts-basic-components-span.md)：作为[Text](../harmonyos-references/ts-basic-components-text.md)、[ContainerSpan](../harmonyos-references/ts-basic-components-containerspan.md)组件的子组件，用于显示行内文本的组件。不支持通用属性设置，所以[linearGradient](../harmonyos-references/ts-universal-attributes-gradient-color.md#lineargradient)属性设置无效。若需设置通用属性，应使用Text进行设置，或改用属性字符串中的[CustomSpan](../harmonyos-references/ts-universal-styled-string.md#customspan)自行绘制。
* CustomSpan可以通过[setShaderEffect](../harmonyos-references/arkts-apis-graphics-drawing-pen.md#setshadereffect12)接口设置drawing.ShaderEffect.createLinearGradient实现渐变背景色。

## 解决方案

* **方案一**：CustomSpan方式实现Span渐变背景色。

  渐变背景：

  ```ts
  // 设置渐变背景色
  let startPt: common2D.Point = { x: 0, y: 0 };
  let endPt: common2D.Point = { x: gUIContext.vp2px(this.width), y: gUIContext.vp2px(this.height) };
  let shaderEffect =
    drawing.ShaderEffect.createLinearGradient(startPt, endPt, [0x3300FF00, 0x33FF0000], drawing.TileMode.REPEAT);
  brush.setShaderEffect(shaderEffect);
  ```

  完整示例参考如下：

  ```screen
  import { common2D, drawing } from '@kit.ArkGraphics2D';
  import { LengthMetrics } from '@kit.ArkUI';

  let gUIContext: UIContext;

  class MyCustomSpan extends CustomSpan {
    constructor(word: string, width: number, height: number) {
      super();
      this.word = word;
      this.width = width;
      this.height = height;
    }

    onMeasure(): CustomSpanMetrics {
      return { width: this.width, height: this.height };
    }

    onDraw(context: DrawContext, options: CustomSpanDrawInfo) {
      let canvas = context.canvas;
      const brush = new drawing.Brush();
      // 设置渐变背景色
      let startPt: common2D.Point = { x: 0, y: 0 };
      let endPt: common2D.Point = { x: gUIContext.vp2px(this.width), y: gUIContext.vp2px(this.height) };
      let shaderEffect =
        drawing.ShaderEffect.createLinearGradient(startPt, endPt, [0x3300FF00, 0x33FF0000], drawing.TileMode.REPEAT);
      brush.setShaderEffect(shaderEffect);
      const font = new drawing.Font();
      font.setSize(50);
      const textBlob = drawing.TextBlob.makeFromString(this.word, font, drawing.TextEncoding.TEXT_ENCODING_UTF8);
      canvas.attachBrush(brush);
      canvas.drawRect({
        left: options.x + 10,
        right: options.x + gUIContext.vp2px(this.width) - 10,
        top: options.lineTop + 10,
        bottom: options.lineBottom - 10
      });
      brush.setColor({
        alpha: 255,
        red: 23,
        green: 169,
        blue: 141
      });
      canvas.attachBrush(brush);
      canvas.drawTextBlob(textBlob, options.x + 20, options.lineBottom - 15);
      canvas.detachBrush();
    }

    setWord(word: string) {
      this.word = word;
    }

    width: number = 160;
    word: string = 'drawing';
    height: number = 10;
  }

  @Entry
  @Component
  struct styled_string_demo6 {
    customSpan1: MyCustomSpan = new MyCustomSpan('Hello', 80, 10);
    customSpan2: MyCustomSpan = new MyCustomSpan('World', 80, 40);
    style1: MutableStyledString = new MutableStyledString(this.customSpan1);
    textController: TextController = new TextController();
    isPageShow: boolean = true;

    aboutToAppear() {
      gUIContext = this.getUIContext();
    }

    async onPageShow() {
      if (!this.isPageShow) {
        return;
      }
      this.isPageShow = false;
      this.style1.appendStyledString(new MutableStyledString('文本绘制 示例代码 CustomSpan', [
        {
          start: 0,
          length: 5,
          styledKey: StyledStringKey.FONT,
          styledValue: new TextStyle({ fontColor: Color.Pink })
        }, {
        start: 5,
        length: 5,
        styledKey: StyledStringKey.FONT,
        styledValue: new TextStyle({ fontColor: Color.Orange, fontStyle: FontStyle.Italic })
      }, {
        start: 10,
        length: 500,
        styledKey: StyledStringKey.FONT,
        styledValue: new TextStyle({ fontColor: Color.Green, fontWeight: FontWeight.Bold })
      }
      ]));
      this.style1.appendStyledString(new StyledString(this.customSpan2));
      this.style1.appendStyledString(new StyledString('自定义绘制', [{
        start: 0,
        length: 5,
        styledKey: StyledStringKey.FONT,
        styledValue: new TextStyle({ fontColor: Color.Green, fontSize: LengthMetrics.px(50) })
      }]));
      this.textController.setStyledString(this.style1);
    }

    build() {
      Row() {
        Column() {
          Text(undefined, { controller: this.textController })
            .copyOption(CopyOptions.InApp)
            .fontSize(30);
          Button('invalidate').onClick(() => {
            this.customSpan1.setWord('你好');
            this.customSpan1.invalidate();
          });
        }
        .width('100%');
      }
      .height('100%');
    }
  }
  ```

  效果预览：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8a/v3/ubexCInDQ3eHjrqlP6hMLg/zh-cn_image_0000002658962961.png "点击放大")
* **方案二**：可直接采用Text组件代替Span组件，实现渐变背景色设置。

  ```ts
  @Entry
  @Component
  export struct OptionTwo {
    build() {
      Column() {
        Row() {
          Text() {
            Span('Hello')
              .fontSize(30)
              .alignSelf(ItemAlign.Center)
              .width(30);
          }
          .linearGradient({
            direction: GradientDirection.Right,
            colors: [['#ff46f6f6', 0], ['#ff46a4f6', 1]]
          });

          Text() {
            Span(' World!')
              .fontSize(30);
          };
        }
        .margin({
          left: 15
        });
      }
      .justifyContent(FlexAlign.Center)
      .width('100%')
      .height('100%');
    }
  }
  ```

  效果预览：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/YEA3YyPTRS-VjnKd3GADCw/zh-cn_image_0000002628603746.png "点击放大")
* **方案三**：将文本绘制成图片显示。

  通过drawing绘制出一张包含文字的渐变背景的图片，使用[ImageSpan](../harmonyos-references/ts-basic-components-imagespan.md)或者属性字符串的[ImageAttachment](../harmonyos-references/ts-universal-styled-string.md#imageattachment)显示文字图片。

  ```ts
  import { common2D, drawing } from '@kit.ArkGraphics2D';
  import { image } from '@kit.ImageKit';
  import { LengthMetrics } from '@kit.ArkUI';

  @Entry
  @Component
  struct OptionThree {
    textController: TextController = new TextController();
    @State pixelMap: image.PixelMap | undefined = undefined;

    onPageShow() {
      this.draw(); // 页面显示时绘制
    }

    build() {
      Row() {
        Column() {
          Text() {
            ImageSpan(this.pixelMap)
              .width(40)
              .height(16);
            Span(' World!')
              .baselineOffset(new LengthMetrics(0))
              .fontSize(16);
          }
          .height(16)
          .clip(true);
        }
        .width('100%');
      }
      .height('100%');
    }

    draw() {
      // 计算文本长款宽
      let size: SizeOptions =
        this.getUIContext().getMeasureUtils().measureTextSize({ textContent: 'Hello', fontSize: 16 });
      // 绘制图片
      const color = new ArrayBuffer(200 * 200 * 4);
      let opts: image.InitializationOptions = {
        editable: true,
        pixelFormat: 3,
        size: {
          height: size.height as number,
          width: size.width as number
        }
      };
      image.createPixelMap(color, opts).then((pixelMap: PixelMap) => {
        let width: number = size.width as number;
        let height: number = size.height as number;
        // 1.构造canvas对象
        const canvas = new drawing.Canvas(pixelMap);
        // 2.构造一个新的画刷对象，绘制背景
        const brush = new drawing.Brush();
        let startPt: common2D.Point = { x: 0, y: 0 };
        let endPt: common2D.Point = { x: width, y: height };
        let shaderEffect =
          drawing.ShaderEffect.createLinearGradient(startPt, endPt, [0x3300FF00, 0x33FF0000], drawing.TileMode.REPEAT);
        brush.setShaderEffect(shaderEffect);
        let path = new drawing.Path();
        const rect: common2D.Rect = {
          left: 0,
          top: 0,
          right: width,
          bottom: height
        };
        let roundRect = new drawing.RoundRect(rect, 0, 0);
        path.addRoundRect(roundRect, drawing.PathDirection.CLOCKWISE);
        canvas.clipPath(path, drawing.ClipOp.INTERSECT, true);
        canvas.drawBackground(brush);
        canvas.attachBrush(brush);
        canvas.drawPath(path);
        canvas.detachBrush();
        // 3.构造一个新的画刷对象，绘制文字
        const brush2 = new drawing.Brush();
        brush2.setColor({
          alpha: 255,
          red: 0,
          green: 0,
          blue: 0
        });
        const font = new drawing.Font();
        font.setSize(50);
        const textBlob = drawing.TextBlob.makeFromString('Hello', font, drawing.TextEncoding.TEXT_ENCODING_UTF8);
        canvas.attachBrush(brush2);
        canvas.drawTextBlob(textBlob, 0, height - this.getUIContext().vp2px(4)); // 设置文字位置
        canvas.detachBrush();
        this.pixelMap = pixelMap as PixelMap;
      });
    }
  }
  ```

  效果预览：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8/v3/0RVs7A_6R3WtaxskSV1BZA/zh-cn_image_0000002658843013.png "点击放大")

## 总结

暂时没有对Span组件设置渐变背景色的API，本文主要简述Span组件设置渐变背景色的替代方案。

| 方案 | 简易程度 | 局限性 |
| --- | --- | --- |
| 方案一 | 较难 | 设置的渐变色背景的文字不宜过长，超过一行时，会导致文本不衔接。 |
| 方案二 | 简单 | 设置的渐变色背景的文字不宜过长，超过一行时，会导致文本不衔接；后续Text组件的文本较长时，会导致Text组件自动换行显示，也会导致文本不衔接。 |
| 方案三 | 较难 | 设置的渐变色背景的文字不宜过长，超过一行时，会导致文本不衔接。 |

推荐使用方案一的CustomSpan方式，自定义实现Span渐变背景色。
