---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/arkui-kit-faq-0017
title: 如何控制TextArea最多显示多少行，超出尺寸的显示滚动条
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 常见问题 > 如何控制TextArea最多显示多少行，超出尺寸的显示滚动条
category: harmonyos-faqs
scraped_at: 2026-10-28T07:46:59+08:00
doc_updated_at: 2026-10-20
content_hash: sha256:d5719997a643ecd94986d8017f01baf0a7317ba299aece60e8605895abf5335f
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

效果图如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1e/v3/4Olk0KLzSmeRoar_Y02uFA/zh-cn_image_0000002767956462.png "点击放大")
