---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/arkui-uimana-faq-0016
title: 居中显示TimePicker的文本
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 常见问题 > 居中显示TimePicker的文本
category: harmonyos-faqs
scraped_at: 2026-10-28T07:47:32+08:00
doc_updated_at: 2026-10-20
content_hash: sha256:35413a04dd73b11338c3b0c83e5145a6b8b56fb49424c2ee6bfe3441aab9c8fb
---

**Q：在使用TimePicker组件时，小时和分钟文本的默认间距及对齐方式如下图所示。请问如何调整设置以减小两者之间的间距并使文本居中显示？**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/71/v3/I9o0mDOaSgGyL06OmHa41w/zh-cn_image_0000002795484095.png "点击放大")

**A**：可以考虑通过调整TimePicker组件的宽度，其中的小时和分钟会自适应调整占用宽度。用在两边加入水平分割线的方法来间接实现对文本间距的调整。具体实现方式请参考以下代码：

```ts
@Entry
@Component
struct CenterAlignPage {
  private selectedTime: Date = new Date('2022-07-22T08:00:00');

  build() {
    Row() {
      Column() {
        // 加入水平分割线
        Text("")
          .width('35%')
          .height(0.2)
          .backgroundColor(('#A0A0A4')).margin({ top: 72 });
        Text("")
          .width('35%')
          .height(0.2)
          .backgroundColor(('#A0A0A4')).margin({ top: 56 });
      };

      TimePicker({
        selected: this.selectedTime,
      })
        .useMilitaryTime(true)
        .loop(true)
        .disappearTextStyle({
          color: Color.White,
          font: {
            size: 16,
            weight: FontWeight.Lighter
          }
        })
        .textStyle({
          font: {
            size: 18, weight: FontWeight.Normal
          }
        })
        .selectedTextStyle({
          font: {
            size: 20, weight: FontWeight.Bolder
          }
        })
        .onChange((value: TimePickerResult) => {
          this.selectedTime.setHours(value.hour, value.minute);
          console.info('select current date is: ', JSON.stringify(value));
        })
        // 调整TimePicker组件的宽度
        .width('30%');
      Column() {
        // 加入水平分割线
        Text("")
          .width('35%')
          .height(0.2)
          .backgroundColor(('#A0A0A4')).margin({ top: 72 });
        Text("")
          .width('35%')
          .height(0.2)
          .backgroundColor(('#A0A0A4')).margin({ top: 56 });
      };
    }.alignItems(VerticalAlign.Top)
    .height('100%');
  }
}
```

代码运行效果图如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/20/v3/fv2oW1HeStyPeXpBTtHHRQ/zh-cn_image_0000002766085522.png "点击放大")
