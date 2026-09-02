---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-625
title: 如何设置Text组件的缩进避让
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 如何设置Text组件的缩进避让
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:16+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:fda50c816636aa34eef957bb0e9ed90159250953f1cecdb5b06ab049c026db52
---

## 问题现象

当Text组件与其他组件堆叠出现时，Text的文字内容需获取其他组件的宽高数据，进行缩进避让。

## 背景知识

* [Stack](../harmonyos-references/ts-container-stack.md)堆叠容器，子组件按照顺序依次入栈，后一个子组件覆盖前一个子组件。
* [RelativeContainer](../harmonyos-references/ts-container-relativecontainer.md)，相对布局，子组件间通过相对位置的布局，实现多个组件层叠显示的效果。
* [onAreaChange](../harmonyos-references/ts-universal-component-area-change-event.md#onareachange)，获取组件的组件大小、位置信息。
* [textIndent](../harmonyos-references/ts-basic-components-text.md#textindent10)，设置Text组件首行文本缩进。
* [ContainerSpan](../harmonyos-references/ts-basic-components-containerspan.md)组件为Text组件的子组件，用于统一管理多个Span、ImageSpan的背景色及圆角弧度。可以包含Span、ImageSpan子组件。

## 解决方案

* **方案一**：问题描述提到组件堆叠，则可用Stack布局，通过设置缩进，为文本标签留下空间。

  ```ts
  @Entry
  @Component
  struct ExampleOne {
    private dynamicText: string = '标签';

    build() {
      Stack({ alignContent: Alignment.TopStart }) {
        Text('这是详细内容这是详细内容这是详细内容这是详细内容这是详细内容这是详细内容')
          .fontSize(30)
          .textIndent(60)
          .width('100%')

        Text(this.dynamicText)
          .fontSize(20)
          .width(50)
          .border({ width: 1, color: Color.Black, radius: 10 })
          .textAlign(TextAlign.Center)
      }
      .padding(20)
    }
  }
  ```

  效果预览：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cb/v3/XXMdXGLxSpyXpdpGr_RXxw/zh-cn_image_0000002658913485.png "点击放大")
* **方案二**：获取其他组件宽度并设置Text组件的缩进避让。
  1. 在通过RelativeContainer相对布局，实现标题Row组件和内容Text组件的相同位置显示，但此时两个组件内容会有重叠遮挡。
  2. 通过onAreaChange获取标题Row组件的宽度信息（this.titleWidth），转换为number类型。

     ```ts
     Row() {
       Text('短剧·中国版教父')
     }
     .justifyContent(FlexAlign.Center)
     .backgroundColor('#a3cf62')
     .padding(4)
     .borderRadius(4)
     .id('row1')
     .alignRules({
       top: { anchor: 'text', align: VerticalAlign.Top },
       left: { anchor: 'text', align: HorizontalAlign.Start }
     })
     .onAreaChange((oldValue: Area, newValue: Area) => {
       this.sizeValue = JSON.stringify(newValue);
       this.titleWidth = parseInt(this.sizeValue.split('width":')[1].split(',')[0]); // 获取标题组件的宽度
     })
     ```
  3. 配置Text组件的首行缩进长度为第二步获取的Row组件的宽度（this.titleWidth），实现文字避让。

     ```ts
     Text(this.message)
       .key('text')
       .maxLines(this.lines)
       .lineHeight(26)
       .textIndent(this.titleWidth + 2)
     ```

  完整示例参考如下：

  ```ts
  const COLLAPSE_LINES: number = 2;

  @Entry
  @Component
  struct ExampleTwo {
    private lines: number = COLLAPSE_LINES;
    @State sizeValue: string = '';
    @State titleWidth: number = 0;
    private message: string = '这里是详情内容，这里是详情内容，这里是详情内容，这里是详情内容';

    build() {
      RelativeContainer() {
        Text(this.message)
          .key('text')
          .maxLines(this.lines)
          .lineHeight(26)
          .textIndent(this.titleWidth + 2)
        Row() {
          Text('短剧·中国版教父')
        }
        .justifyContent(FlexAlign.Center)
        .backgroundColor('#a3cf62')
        .padding(4)
        .borderRadius(4)
        .id('row1')
        .alignRules({
          top: { anchor: 'text', align: VerticalAlign.Top },
          left: { anchor: 'text', align: HorizontalAlign.Start }
        })
        .onAreaChange((oldValue: Area, newValue: Area) => {
          this.sizeValue = JSON.stringify(newValue);
          this.titleWidth = parseInt(this.sizeValue.split('width":')[1].split(',')[0]); // 获取标题组件的宽度
        })
      }
      .height('auto')
      .borderWidth(1)
      .margin({ top: 100, left: 8, right: 8 })
    }
  }
  ```

  效果预览：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cd/v3/dLtkq2N1TuCblRA-N2Qsew/zh-cn_image_0000002658793535.png "点击放大")

* **方案三**：可以使用ContainerSpan组件，作为设置Text组件的缩进避让的替代方案，可参考官方文档[通过attributemodifier设置背景样式](../harmonyos-references/ts-basic-components-containerspan.md#示例2通过attributemodifier设置背景样式)。可在组件内使用Span、ImageSpan组件。但此方法不支持通用属性和通用事件，有一定局限性。
