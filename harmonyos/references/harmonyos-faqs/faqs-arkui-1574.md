---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1574
title: 如何通过计算和偏移实现消息气泡的效果
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 如何通过计算和偏移实现消息气泡的效果
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:11+08:00
doc_updated_at: 2026-07-02
content_hash: sha256:c30c0bb5765f95e0cb0e1a8c49b282ed093549e00d280e4dd4abe41c767724e3
---

## 问题现象

如何通过组件的搭配使用，实现类似如下消息气泡效果：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2e/v3/uII-_2jSQDG-AwNKKqp6uw/zh-cn_image_0000002631323906.png "点击放大")

## 背景知识

* [RelativeContainer](../harmonyos-references/ts-container-relativecontainer.md)：相对布局组件，用于复杂场景中元素对齐的布局。
* [vp2px](../harmonyos-references/arkts-apis-uicontext-uicontext.md#vp2px12)：将vp单位的数值转换为以px为单位的数值。
* [measureText](../harmonyos-references/arkts-apis-uicontext-measureutils.md#measuretext12)：计算指定文本作为单行文本显示时的宽度。如果文本包含多行（由换行符\n分隔），则返回其中最长的行的宽度。

## 解决方案

1. 通过MeasureUtils的measureText方法获取组件中主体文本单行布局的长度。
2. 使用RelativeContainer容器和alignRules属性将气泡文本和主体文本组件的一侧对齐。
3. 通过offset属性将数字文本偏移，偏移距离为数字文本的宽度。

完整示例参考如下：

```ts
import { MeasureUtils } from '@kit.ArkUI';

@Entry
@Component
struct MeasurePx2vpDemo {
  textTitle: string = '发货订单';
  textNumber: string = '123';
  uiContext: UIContext = this.getUIContext();
  uiContextMeasure: MeasureUtils = this.uiContext.getMeasureUtils();
  // 获取主体内容单行布局的长度
  @State titleSize: SizeOptions = this.uiContextMeasure.measureTextSize({
    textContent: this.textTitle,
    fontSize: '30vp'
  });
  // 获取数字角标单行布局的长度
  @State numberSize: SizeOptions = this.uiContextMeasure.measureTextSize({
    textContent: this.textNumber,
    fontSize: '15vp'
  });

  build() {
    Column() {
      RelativeContainer() {
        // 主体内容
        Row() {
          Text(this.textTitle).fontSize('30vp');
        }.id('row1');

        // 数字角标
        Row() {
          Text(this.textNumber).fontSize('15vp').textAlign(TextAlign.Start).maxLines(1);
        }.id('row2')
        // alignRules属性将组件的顶部和右侧对齐
        .alignRules({
          top: { anchor: '__container__', align: VerticalAlign.Top },
          right: { anchor: '__container__', align: HorizontalAlign.End }
        })
        // 通过offset属性将数字文本偏移
        .offset({
          x: this.getUIContext().px2vp(this.numberSize.width as number),
          y: 0
        });
      }
      .width(this.getUIContext().px2vp(this.titleSize.width as number))
      .height(this.getUIContext().px2vp(this.titleSize.height as number));
    }.width('100%').height('100%')
    .justifyContent(FlexAlign.Center)
    .alignItems(HorizontalAlign.Center);
  }
}
```

效果如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/85/v3/KlOaJj6AQiCY7n-Caw61lg/zh-cn_image_0000002631324324.png "点击放大")
