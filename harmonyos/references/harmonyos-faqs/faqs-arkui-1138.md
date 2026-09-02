---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1138
title: 如何实现多行文本行中省略的效果
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 如何实现多行文本行中省略的效果
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:18+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:bdf87931f7a737c6679d5bda1a9525e5b4e685ad289a947b0f7ff6644975b36e
---

## 问题现象

Text文本多行时，可以利用[textOverflow](../harmonyos-references/ts-basic-components-text.md#textoverflow)来设置省略效果，但是设置[EllipsisMode.CENTER](../harmonyos-references/ts-appendix-enums.md#ellipsismode11)不生效。

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fb/v3/oud2BVZJTnW6ZoY1KuhC9Q/zh-cn_image_0000002628569602.png "点击放大")

## 背景知识

* 根据[ellipsisMode](../harmonyos-references/ts-basic-components-text.md#ellipsismode11)使用说明，可以看到EllipsisMode.START和EllipsisMode.CENTER仅在单行超长文本生效，所以文本多行时设置该属性不生效，需要使用其他方式实现。
* [measureTextSize](../harmonyos-references/arkts-apis-uicontext-measureutils.md#measuretextsize12)可以计算超长文本的宽度，利用文本计算可以算出超长文本的首行字符，然后把剩余的文本设置成一行即可使用ellipsisMode属性。

## 解决方案

1. 首先利用MeasureUtils.measureTextSize算得文本长度（px单位）。

   ```ts
   textSize: SizeOptions = this.uiContextMeasure.measureTextSize({
     textContent: this.textContent,
     fontSize: 16,
   });
   ```
2. 然后利用vp2px方法可以算得Text组件一行所占宽度（px单位）。

   ```ts
   this.textWidthPx = this.getUIContext().vp2px(this.textWidth);
   ```
3. 再然后根据公式文本字符数\*（Text组件一行所占宽度/文本总长度）即可算出一行所占字符数。

   ```ts
   this.oneLineLength = this.textContent.length * this.textWidthPx / (this.textSize.width as number);
   ```
4. 最后把文本分成两部分，第一个Text组件完整展示一行所占字符，第二个Text组件展示剩余字符，并且设置ellipsisMode效果。

完整示例参考如下：

```ts
import { MeasureUtils } from '@kit.ArkUI';

@Entry
@Component
struct MultipleLinesTest {
  private textContent: string = '超长的文本在这里展示出来了超长的文本在这里展示出来了超长的文本在这里展示出来了';
  uiContextMeasure: MeasureUtils = this.getUIContext().getMeasureUtils();
  textSize: SizeOptions = this.uiContextMeasure.measureTextSize({
    textContent: this.textContent,
    fontSize: 16,
  });
  // Text组件宽度
  private textWidth: number = 200;
  private textWidthPx: number = 0;
  private oneLineLength: number = 0;

  aboutToAppear(): void {
    this.textWidthPx = this.getUIContext().vp2px(this.textWidth);
    this.oneLineLength = this.textContent.length * this.textWidthPx / (this.textSize.width as number);
  }

  build() {
    Row() {
      Column() {
        // 计算出来的第一行文本
        Text(this.textContent.slice(0, this.oneLineLength))
          .width(this.textWidth)
          .fontSize(16);
        // 除去第一行文本的其他文本
        Text(this.textContent.slice(this.oneLineLength, this.textContent.length))
          .width(this.textWidth)
          .fontSize(16)
          .maxLines(1)
          .textOverflow({ overflow: TextOverflow.Ellipsis })
          .wordBreak(WordBreak.BREAK_ALL)
          .ellipsisMode(EllipsisMode.CENTER);
      }
      .width('100%');
    }
    .height('100%');
  }
}
```
