---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1322
title: CanvasRenderingContext2D绘制长文本自动换行
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > CanvasRenderingContext2D绘制长文本自动换行
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:16+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:d77e1f14228889e67f16af3efe14b1982675ddccb1e0406a738550a025c77cfa
---

## 问题现象

使用CanvasRenderingContext2D绘制长文本时，这些长文本既没有换行符，也没有空格符，如何对绘制的文本进行自动换行？效果图如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b8/v3/UBEmRlnjSXuqm1tgTU0wzg/zh-cn_image_0000002658838901.png "点击放大")

## 背景知识

[Canvas](../harmonyos-references/ts-components-canvas-canvas.md)提供画布组件，用于自定义绘制图形，开发者使用[CanvasRenderingContext2D](../harmonyos-references/ts-canvasrenderingcontext2d.md)对象和[OffscreenCanvasRenderingContext2D](../harmonyos-references/ts-offscreencanvasrenderingcontext2d.md)对象在Canvas组件上进行绘制，绘制对象可以是基础形状、文本、图片等。

## 解决方案

1. 通过MeasureText方法确定文本的宽度，如果绘制的文本总宽度并没有超过单行最大宽度，那么直接绘制。
2. 如果绘制的文本总宽度超过单行最大宽度，则按字符逐字检查，当超出单行最大宽度做换行处理，最终得到一个文本数组。

完整参考示例如下：

```ts
import { PromptAction } from '@kit.ArkUI';

@Entry
@Component
struct CanvasExample {
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  testText =
    '人生恰似逆旅，我们皆是行者。在时光长河中穿梭，所遇挫折是暗礁，亦是磨砺心智的基石；收获的喜乐为星光，却也不可溺于其中。万物恒变，心守正道，以清醒之思驾驭命运扁舟，于起伏间悟存在真意，方不负这一路奔逐。';
  lineHeight: number = 0;
  letterSpacing: number = 0;
  fontSize: number = 16;
  isBold: boolean = false;
  isUnderline: boolean = false;
  isItalic: boolean = false;
  promptAction: PromptAction = this.getUIContext().getPromptAction();

  handleDrawText() {
    // 多个连续空格只保留一个
    let tempText = this.testText.replace(/(^\s*)|(\s*$)/g, ' ').replace(/ +/g, ' ');
    let textLen = tempText.length;
    this.context.font = `${this.fontSize}vp YaHei`;

    // 如果绘制的文本总宽度并没有超过最大宽度，那么直接绘制
    if (this.context.measureText(tempText).width + textLen * this.letterSpacing < this.context.width) {
      this.context.fillText(tempText, 0, 0);
    } else {
      let strArray: string[] = [];
      let tempStr = '';
      for (let i = 0; i < textLen; i++) {
        let currStr = tempText[i];
        // 判断当前字符是否是换行符，如果是，那么新增下一行
        let isWrap = !/\r?\n/.test(currStr);
        if (isWrap && (this.context.measureText(tempStr + currStr).width + (tempStr.length + 1) * this.letterSpacing) <
        this.context.width) {
          // 如果不是换行符且当前绘制的文本宽度加字距小于最大宽度，直接当前行字符串直接拼接
          tempStr += currStr;
        } else {
          // 否则就是当前行的宽度已经达到极限，进行换行
          strArray.push(tempStr);
          if (isWrap) {
            // 如果不是换行符，直接新的一行开头就是这个字符
            tempStr = currStr;
          } else {
            // 否则，新的一行开头将换行符替换为空字符串
            tempStr = '';
          }
        }
      }
      // 如果还有剩余结尾的字符串，直接就算作一行
      if (tempStr !== '') {
        strArray.push(tempStr);
        tempStr = '';
      }

      strArray.forEach((str, index) => {
        // 逐行绘制，绘制的y坐标当前行行数加上字体大小加上行高近似的模拟
        this.handleDrawOneLineText(str, (index + 1) * (this.fontSize + this.lineHeight));
      });
    }
  }

  handleDrawOneLineText(str: string, y: number) {
    let tempStr = '';
    for (let i = 0, len = str.length; i < len; i++) {
      // 逐字绘制，每行的y不变，单个字符的x是前面绘制文本的宽度加上每个字符的间距和
      this.context.fillText(str[i], i * this.letterSpacing + (this.context.measureText(tempStr).width), y);
      tempStr += str[i];
    }
  }

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Row({ space: 10 }) {
        Button('字间距+').controlSize(ControlSize.SMALL).onClick(() => {
          this.letterSpacing++;
          this.context.clearRect(0, 0, this.context.width, this.context.height);
          this.handleDrawText();
        });
        Button('字间距-').controlSize(ControlSize.SMALL).onClick(() => {
          if (this.letterSpacing <= 0) {
            this.promptAction.openToast({ message: '最小字间距为0' });
            return;
          }
          this.letterSpacing--;
          this.context.clearRect(0, 0, this.context.width, this.context.height);
          this.handleDrawText();
        });
        Button('字号+').controlSize(ControlSize.SMALL).onClick(() => {
          this.fontSize++;
          this.context.clearRect(0, 0, this.context.width, this.context.height);
          this.handleDrawText();
        });
        Button('字号-').controlSize(ControlSize.SMALL).onClick(() => {
          if (this.fontSize <= 10) {
            this.promptAction.openToast({ message: '最小字号为10' });
            return;
          }
          this.fontSize--;
          this.context.clearRect(0, 0, this.context.width, this.context.height);
          this.handleDrawText();
        });
      };

      Column() {
        Canvas(this.context)
          .width('100%')
          .layoutWeight(1)
          .backgroundColor('#aaccee')
          .onReady(() => {
            this.handleDrawText();
          });
      }
      .width('100%')
      .padding({ left: 16, right: 16 })
      .margin(10)
      .backgroundColor('#aaccee');
    }
    .width('100%')
    .height('100%');
  }
}
```
