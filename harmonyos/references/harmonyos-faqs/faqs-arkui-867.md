---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-867
title: 文本超出显示的高度范围
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 文本超出显示的高度范围
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:15+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:e148400b1ef3f7acd542fe665d3a88784a0f23553fd47c8e82f95e0a625ce7d5
---

## 问题现象

文本超出了当前显示的高度范围，与背景框冲突。

## 背景知识

* [Text](../harmonyos-references/ts-basic-components-text.md)：显示一段文本的组件，默认自动折行。
* [textOverflow](../harmonyos-references/ts-basic-components-text.md#textoverflow)：设置文本超长时的显示方式。
* [maxLines](../harmonyos-references/ts-basic-components-text.md#maxlines)：设置文本的最大行数。默认情况下，文本是自动折行的，如果指定此属性，则文本最多不会超过指定的行。如果有多余的文本，可以通过[textOverflow](../harmonyos-references/ts-basic-components-text.md#textoverflow)来指定截断方式。
* [bindContextMenu](../harmonyos-references/ts-universal-attributes-menu.md#bindcontextmenu8)：给组件绑定菜单，控制菜单显隐的触发方式为长按或右键点击，弹出的菜单项需自定义。

## 问题定位

1. 通过DevEco Testing For Device的UIViewer工具可以看到[Text](../harmonyos-references/ts-basic-components-text.md)组件的宽为1197，高为130。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d0/v3/OqD60qTqQTS8_cm5p2dhmQ/zh-cn_image_0000002628558798.png "点击放大")
2. 父组件Column的宽为1216，高为260。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/29/v3/iIJnOdhRTHO0D3KqHaIuzQ/zh-cn_image_0000002658918115.png "点击放大")
3. [Text](../harmonyos-references/ts-basic-components-text.md)文本组件和其父组件宽高属性正常，但文本显示高度明显超过了[Text](../harmonyos-references/ts-basic-components-text.md)和其父组件的高度范围。

## 分析结论

[Text](../harmonyos-references/ts-basic-components-text.md)文本组件是默认自动折行，当文本内容过多时，会超过组件的显示区域。

## 修改建议

* 方案一：使用滚动组件嵌套[Text](../harmonyos-references/ts-basic-components-text.md)组件，当[Text](../harmonyos-references/ts-basic-components-text.md)的文本内容超出范围时，可以通过滚动显示。

  ```screen
  @Entry
  @Component
  struct LongTextSolution1 {
    textContent: string =
      "这是一段测试文本。这是一段测试文本。这是一段测试文本。这是一段测试文本。这是一段测试文本。这是一段测试文本。这是一段测试文本。" +
        "这是一段测试文本。这是一段测试文本。这是一段测试文本。这是一段测试文本。这是一段测试文本。这是一段测试文本。";

    build() {
      Column() {
        Scroll() {
          Column() {
            Text(this.textContent)
              .fontSize(16);
          }
          .width('100%');
        }
        .width('90%')
        .height(100)
        .padding(10)
        .borderRadius(12)
        .scrollBar(BarState.Off)
        .backgroundColor('#f1f3f5');
      }
      .width('100%')
      .alignItems(HorizontalAlign.Center)
      .margin({ top: 16 });
    }
  }
  ```

  效果图如下：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c5/v3/U_9m6HgdRcepYYXnWFD1-w/zh-cn_image_0000002628398898.png "点击放大")
* 方案二：配置[Text](../harmonyos-references/ts-basic-components-text.md)组件的[maxLines](../harmonyos-references/ts-basic-components-text.md#maxlines)和[textOverflow](../harmonyos-references/ts-basic-components-text.md#textoverflow)属性，使得文本最大显示行数在组件高度范围内，并且超出部分通过省略号显示。长按文本通过bindContextMenu绑定菜单显示完整内容。

  ```screen
  @Entry
  @Component
  struct LongTextSolution2 {
    textContent: string =
      "这是一段测试文本。这是一段测试文本。这是一段测试文本。这是一段测试文本。这是一段测试文本。这是一段测试文本。这是一段测试文本。" +
        "这是一段测试文本。这是一段测试文本。这是一段测试文本。这是一段测试文本。这是一段测试文本。这是一段测试文本。";

    build() {
      Column() {
        Column() {
          Text(this.textContent)
            .fontSize(16)
            .maxLines(4)
            .width('100%')
            .textOverflow({ overflow: TextOverflow.Ellipsis })
            .bindContextMenu(this.buildContextMenu, ResponseType.LongPress, { backgroundColor: Color.White });
        }
        .width('90%')
        .height(100)
        .padding(10)
        .borderRadius(12)
        .backgroundColor('#f1f3f5');
      }
      .width('100%')
      .alignItems(HorizontalAlign.Center)
      .margin({ top: 16 });
    }

    @Builder
    buildContextMenu() {
      Text(this.textContent)
        .fontSize(16)
        .margin(24);
    }
  }
  ```

  效果图如下：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dd/v3/dE1yMlqRSSWXaFfKYuRRzg/zh-cn_image_0000002658798175.png "点击放大")
* 方案三：[Text](../harmonyos-references/ts-basic-components-text.md)父组件高度设置为auto或自定义高度。

  ```screen
  @Entry
  @Component
  struct LongTextSolution3 {
    textContent: string =
      "这是一段测试文本。这是一段测试文本。这是一段测试文本。这是一段测试文本。这是一段测试文本。这是一段测试文本。这是一段测试文本。" +
        "这是一段测试文本。这是一段测试文本。这是一段测试文本。这是一段测试文本。这是一段测试文本。这是一段测试文本。";

    build() {
      Column() {
        Column() {
          Text(this.textContent)
            .fontSize(16)
            .height('auto');

        }
        .width('90%')
        .height('auto')
        .padding(10)
        .borderRadius(12)
        .backgroundColor('#f1f3f5');
      }
      .width('100%')
      .alignItems(HorizontalAlign.Center)
      .margin({ top: 16 });
    }
  }
  ```

  效果图如下：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d4/v3/1Pc3BEDGSaqemlPQcaCJiA/zh-cn_image_0000002628558802.png "点击放大")
