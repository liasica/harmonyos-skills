---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-792
title: 文本内容超出组件时，文本内容无法向右对齐
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 文本内容超出组件时，文本内容无法向右对齐
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:24+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:8bb63ba0feb4368a1eae60251c381225628a673d37410c1e487c612de2ba5f7b
---

## 问题现象

当文本内容增加时，期望显示是文本内容尾端对齐，但当文本内容增加并超出组件宽度时，文本不再尾端对齐，新增文本内容无法继续动态显示，只能通过滚动组件查看新增内容。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2b/v3/tSPgA1seSw-8xQoJOq_p4Q/zh-cn_image_0000002658916949.png "点击放大")

## 背景知识

* [textAlign](../harmonyos-references/ts-basic-components-text.md#textalign)属性的生效规则：当文本不可滚动时，textAlign属性生效；当文本可滚动时，textAlign属性不生效。
* [scrollEdge](../harmonyos-references/ts-container-scroll.md#scrolledge)可设置内容滚动到容器边缘，不区分滚动轴方向。

## 问题定位

1. 通过DevEco Testing-实用工具-UIViewer查看页面布局实现，发现文本组件外部包裹滚动组件，以便文本内容超过父容器时滑动查看文本内容。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bd/v3/CIULJS7nS7KdkDQ6myPAYA/zh-cn_image_0000002628397740.png "点击放大")
2. 同时查看Text组件布局实现，发现设置textAlign属性用于实现尾端对齐功能。

   ```ts
   Scroll(this.scroller) {
       Row() {
         Text(this.longText)
           .maxLines(1)
           .fontSize(18)
           .textAlign(TextAlign.End) // 右对齐，保证文字靠右排列，当文本可滚动时该属性不生效

       }
       .padding(10)
       .borderRadius(20)
       .backgroundColor('#f1f3f5')
       .justifyContent(FlexAlign.End) // 确保内容在行内右对齐
     }
     .height(100)
     .width('100%')
     .align(Alignment.End) // 容器内子元素尾端对齐
     .scrollBar(BarState.Off)
     .scrollable(ScrollDirection.Horizontal)
   ```

## 分析结论

文本组件外部包裹滚动组件，文本内容超过父容器时滚动组件生效，即文本可滚动，此时文本尾端对齐的属性失效，导致文本超出显示时，出现默认左对齐的现象，新增文本被截断无法继续动态显示。

## 修改建议

通过设置文本内容新增时，滚动容器中的内容自动滚动到容器边缘，实现文本始终右对齐的效果。

```ts
@Entry
@Component
struct TextExample1 {
  private scroller: Scroller = new Scroller();
  @State longText: string = 'TextAlign set to End.1111111111';

  build() {
    Column() {
      Text('textAlign')
        .fontSize(28)
        .fontColor(0xCCCCCC);
      Scroll(this.scroller) {
        Row() {
          Text(this.longText)
            .maxLines(1)
            .fontSize(18)
            .textAlign(TextAlign.End); // 右对齐，保证文字靠右排列

        }
        .padding(10)
        .borderRadius(20)
        .backgroundColor('#f1f3f5')
        .justifyContent(FlexAlign.End); // 确保内容在行内右对齐
      }
      .height(100)
      .width('100%')
      .align(Alignment.End)
      .scrollBar(BarState.Off)
      .scrollable(ScrollDirection.Horizontal);

      Button('PLUS')
        .height('5%')
        .onClick(() => {
          this.longText = this.longText + '2';
          this.scroller.scrollEdge(Edge.End); // 强制滚动到最右边
        });
    }
    .width('100%')
    .padding(28);
  }
}
```
