---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1393
title: 应用首次打开弹窗内容重叠
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 应用首次打开弹窗内容重叠
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:15+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:a62d142b6974f3c914e5c61a76a06799dc57ee3e9f6496fb574b6e3277cd6e60
---

## 问题现象

应用首次打开弹窗时，弹窗中的内容与按钮发生重叠。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1c/v3/X3SO5T93SEKlBtE1KegCbg/zh-cn_image_0000002628602670.png "点击放大")

## 背景知识

* 默认情况下，[Text](../harmonyos-references/ts-basic-components-text.md)文本是自动折行的，可以通过设置[maxLines](../harmonyos-references/ts-basic-components-text.md#maxlines)属性，指定文本最多不会超过指定的行。如果有多余的文本，可以通过[textOverflow](../harmonyos-references/ts-basic-components-text.md#textoverflow)来指定截断方式。
* [TextArea](../harmonyos-references/ts-basic-components-textarea.md)是多行文本输入框组件，高度未设置时，组件无默认高度，自适应内容高度。宽度未设置时，默认撑满最大宽度。
* [Scroll](../harmonyos-references/ts-container-scroll.md)为可滚动的容器组件，当子组件的布局尺寸超过父组件的尺寸时，内容可以滚动。

## 问题定位

1. 使用DevEco Testing查看问题组件，该问题组件为Dialog组件下的Text组件。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a7/v3/REUv_3nlQSqjWp94cvfNjA/zh-cn_image_0000002658841941.png "点击放大")
2. 查看该Dialog组件的设置，Text组件的父组件未设置Scroll滚动条组件，当Text组件的文本内容过多时会溢出Text组件，导致内容重叠。

   ```ts
   @CustomDialog
   struct CustomDialogExample {
     controller: CustomDialogController

     build() {
       Column() {
         Text(
           // 文本内容
         )
       }
       .height(500)
       .width(300)
       .justifyContent(FlexAlign.Center)
     }
   }
   ```

## 分析结论

Text组件的父组件未设置Scroll滚动条组件，当Text组件的文本内容过多时会溢出Text组件，导致内容重叠。

## 修改建议

可以参考如下代码，在Column中使用Scroll组件，使文本内容能够上下滚动。

```ts
@Entry
@Component
struct TextScroll {
  dialogController: CustomDialogController = new CustomDialogController({
    builder: CustomDialogExample(),
  });

  build() {
    Column() {
      Button('Text组件内容可滑动').onClick(() => {
        this.dialogController.open();
      })
    }
    .width('100%')
    .height('100%')
    .justifyContent(FlexAlign.SpaceAround)
  }
}

@CustomDialog
struct CustomDialogExample {
  controller?: CustomDialogController;
  private textValue: string = '开发\n' +
    '从HarmonyOS NEXT Developer Preview1（API 11）版本开始，HarmonyOS SDK以Kit维度提供丰富、完备的开放能力，涵盖应用框架、系统、媒体、图形、应用服务、AI六大领域，例如：\n' +
    '\n' +
    '1. 应用框架相关Kit开放能力：Ability Kit（程序框架服务）、ArkUI（方舟UI框架）等。\n' +
    '\n' +
    '2. 系统相关Kit开放能力：Universal Keystore Kit（密钥管理服务）、Network Kit（网络服务）等。\n' +
    '\n' +
    '3. 媒体相关Kit开放能力：Audio Kit（音频服务）、Media Library Kit（媒体文件管理服务）等。\n' +
    '\n' +
    '4. 图形相关Kit开放能力：ArkGraphics 2D（方舟2D图形服务）、Graphics Accelerate Kit（图形加速服务）等。\n' +
    '\n' +
    '5. 应用服务相关Kit开放能力：Game Service Kit（游戏服务）、Location Kit（位置服务）等。\n' +
    '\n' +
    '6. AI相关Kit开放能力：Intents Kit（意图框架服务）、CANN Kit（CANN 服务）等。\n' +
    '\n' +
    '我们针对重点开放能力提供了开发指导，助力开发者高效开发。详情请参见“开发”目录下相关内容。';

  build() {
    Column() {
      Scroll() {
        Text(this.textValue)
          .width('80%')
      }
      .scrollBar(BarState.Off)
    }
    .height(500)
    .padding({ top: 16, bottom: 16 })
    .justifyContent(FlexAlign.Center)
  }
}
```
