---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/arkui-kit-faq-0017
title: 如何控制TextArea最多显示多少行，超出尺寸的显示滚动条
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 常见问题 > 如何控制TextArea最多显示多少行，超出尺寸的显示滚动条
category: harmonyos-faqs
scraped_at: 2026-11-21T09:17:48+08:00
doc_updated_at: 2026-11-20
content_hash: sha256:b738e94dc521e55f1086c5607fcf4c727b9a1dcd72a314962de3a541ae30c094
---

**Q：如何使用TextArea实现默认一行，最多展示四行，超出尺寸显示滚动条的文本输入效果？**

**A**：根据TextArea的height和lineHeight可以计算出TextArea能容纳多少行文本。当文本总高度超过TextArea的height时，就会显示滚动条。根据公式来计算文本行高和文本框高度的关系，代码如下：

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
