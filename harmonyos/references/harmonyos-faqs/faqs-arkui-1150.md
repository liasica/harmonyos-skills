---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1150
title: 使用RichEditor组件获取HTML的内容和样式
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 使用RichEditor组件获取HTML的内容和样式
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:20+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:d943b3190f4f104584bf89c3b37ae6d8163cfb9a0d7df776e382f6d835fe84f0
---

## 问题现象

在使用RichEditor组件时，需要将获取的字符串转换成HTML文本，再用RichEditor展示出HTML文本。

## 背景知识

[RichEditor](../harmonyos-references/ts-basic-components-richeditor.md)是ArkUI中支持图文混排和文本交互式编辑的组件，主要用于图文混合内容的输入和文本交互式编辑的场景。

* [onReady](../harmonyos-references/ts-basic-components-richeditor.md#onready)在富文本组件初始化完成后触发;
* [onIMEInputComplete](../harmonyos-references/ts-basic-components-richeditor.md#onimeinputcomplete)在输入法完成输入后触发。

## 解决方案

在RichEditor组件中使用onReady和onIMEInputComplete回调函数获取输入内容，其中onReady(callback:Callback<void>)和onIMEInputComplete(callback:Callback<RichEditorTextSpanResult>)参数callback都不可省略。

具体实现步骤为：

1. 创建[RichEditorController](../harmonyos-references/ts-basic-components-richeditor.md#richeditorcontroller)类的实例对象controller；
2. 在onReady回调函数中调用[controller.addTextSpan](../harmonyos-references/ts-basic-components-richeditor.md#addtextspan)方法传入HTML的内容部分data；
3. 在onIMEInputComplete回调函数中传入整个HTML标签字符串。

示例代码如下：

```ts
@Entry
@Component
struct RichEditorShow {
  private header: string = '<html>\n' +
    '<head>\n' +
    ' <meta charset=\'UTF-8\'>\n' +
    '</head>';
  private end: string = '</html>';
  @State data: string = '<h1 style= \'text-align: center; \'>h1标题</h1>' +
    '<h1 style=\'text-align: center;\'><i>h1斜体</i></h1>' +
    '<h1 style=\'text-align: center;\'><u>h1下划线</u></h1>' +
    '<h2 style=\'text-align: center;\'>h2标题</h2>' +
    '<h3 style=\'text-align: center;\'>h3标题</h3>';
  controller: RichEditorController = new RichEditorController();
  options: RichEditorOptions = { controller: this.controller };

  build() {
    Flex({
      direction: FlexDirection.Column, alignItems: ItemAlign.Start,
      justifyContent: FlexAlign.Start
    }) {
      RichText(this.data)
        .onStart(() => {
          console.info('RichText onStart');
        })
        .onComplete(() => {
          console.info('RichText onComplete');
        })
        .width('100%')
        .height(300)
        .backgroundColor(0XBDDB69);
      RichEditor(this.options)
        .onReady(() => {
          this.controller.addTextSpan(this.data,
            {
              style:
              {
                fontColor: Color.Orange,
                fontSize: 18
              }
            });
        })
        .onIMEInputComplete((value: RichEditorTextSpanResult) => {
          this.data = this.header + value.value + this.end;
        })
        .borderWidth(1)
        .borderColor(Color.Green)
        .width('100%')
        .height(400);
    };
  }
}
```
