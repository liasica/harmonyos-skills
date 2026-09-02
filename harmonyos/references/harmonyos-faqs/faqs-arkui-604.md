---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-604
title: 如何控制TextArea最多显示多少行，超出尺寸的显示滚动条
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 如何控制TextArea最多显示多少行，超出尺寸的显示滚动条
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:01+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:575310676fcd9588c634dfd519d57712de0a859f51411a55363fc39dec642d13
---

## 问题现象

如何使用TextArea实现默认一行，最多展示四行，超出尺寸显示滚动条的文本输入效果？

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/54/v3/VlYN90_eSjKIbXHxNQtRwg/zh-cn_image_0000002658911935.png "点击放大")

## 背景知识

* [TextArea](../harmonyos-references/ts-basic-components-textarea.md)：多行文本输入框组件，当输入的文本内容超过组件宽度时会自动换行显示。
* [lineSpacing](../harmonyos-references/ts-basic-components-textarea.md#linespacing20)：设置文本的行间距。当不配置LineSpacingOptions时，首行上方和尾行下方默认会有行间距。
* [lineHeight](../harmonyos-references/ts-basic-components-textarea.md#lineheight12)：设置文本的文本行高，设置值不大于0时，不限制文本行高，自适应字体大小。

## 解决方案

根据TextArea的height和lineHeight可以计算出TextArea能容纳多少行文本。当文本总高度超过TextArea的height时，就会显示滚动条。根据公式来计算文本行高和文本框高度的关系，代码如下：

```ts
import { LengthMetrics } from '@kit.ArkUI';

@Entry
@Component
struct TextAreaDemo {
  @State text: string = '';
  num: number = 4;
  lineHeight: number = 20;
  @State areaHeight: number = 80;
  lineSpacing: number = 10;
  controller: TextAreaController = new TextAreaController();

  aboutToAppear(): void {
    this.areaHeight = this.lineHeight * this.num + (this.num - 1) * this.lineSpacing;
  }

  build() {
    Column({ space: 20 }) {
      TextArea({
        text: this.text,
        placeholder: 'placeholder',
        controller: this.controller
      })
        .placeholderFont({ size: 16, weight: 400 })
        .width('90%')
        .height(this.areaHeight)
        .lineHeight(this.lineHeight)
        .fontSize(14)
        .lineSpacing(LengthMetrics.px(this.lineSpacing))
        .fontColor($r('sys.color.font_primary'))
        .backgroundColor($r('sys.color.comp_background_list_card'))
        .onChange((value: string) => {
          this.text = value;
        });
    }.width('100%').height('100%')
    .alignItems(HorizontalAlign.Center);
  }
}
```

## 总结

1. 由于文本间默认会有一定的间距，而且无法消除，所以TextArea的height需要比文本的fontSize的四倍还要多出一些，才能刚好只能显示四行。
2. lineHeight控制每一行文本的高度，这个值必须大于等于fontSize。否则会出现文字重叠。
3. lineSpacing默认为0，如果设置了lineSpacing值，就需要把lineSpacing值也计算进去。
