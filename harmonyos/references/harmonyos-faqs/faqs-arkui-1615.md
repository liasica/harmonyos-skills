---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1615
title: 任意位置删除字符时光标总会跳转到最后删除字符
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 任意位置删除字符时光标总会跳转到最后删除字符
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:12+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:eca6078f35acbba6b086175eaab04fb15e88060467e8bc9d5637c05a9d1c5f05
---

## 问题现象

在聊天框任何位置删除字符，光标都会跳转到最后并删除最后一个字符。

## 背景知识

* [TextArea](../harmonyos-references/ts-basic-components-textarea.md)：TextArea为多行文本输入框组件，当输入的文本内容超过组件宽度时会自动换行显示。
* [onChange](../harmonyos-references/ts-basic-components-textarea.md#onchange)：输入内容发生变化时，触发该回调。
* TextAreaOptions.text：设置输入框当前的文本内容。建议通过onChange事件将状态变量与文本实时绑定，避免组件刷新时TextArea中的文本内容异常。

  从API version 10开始，该参数支持$$双向绑定变量。

  从API version 18开始，该参数支持!!双向绑定变量。

## 问题定位

1. 使用DevEco Testing软件的UIViewer工具查看问题页面中的组件树，发现聊天框使用的是TextArea组件。
2. 因为是聊天框内容变化时发生的问题，所以需要排查onChange回调函数的逻辑，查看关键代码如下：

   ```ts
   @Entry
   @Component
   struct TextAreaExample {
     @State inputTxt: string = '';
     controller: TextAreaController = new TextAreaController();

     back(): string | undefined {
       if (this.inputTxt.length <= 0) {
         return undefined;
       } else {
         return this.inputTxt.substring(0, this.inputTxt.length - 1);
       }
     }

     build() {
       Column() {
         TextArea({
           text: this.inputTxt,
           placeholder: '请输入消息...',
           controller: this.controller
         })
           .placeholderFont({ size: 16, weight: 400 })
           .width(336)
           .height(56)
           .margin(20)
           .fontSize(16)
           .fontColor('#182431')
           .backgroundColor('#FFFFFF')
           .onChange((value: string) => {
             if (value.length < this.inputTxt.length) {
               let str = this.back();
               if ((str == null) || (str == undefined)) {
                 this.inputTxt = '';
               } else {
                 this.inputTxt = str;
               }
             } else {
               this.inputTxt = value;
             }
           })
       }.width('100%').height('100%').backgroundColor('#F1F3F5')
     }
   }
   ```

   可以看到onChange回调函数中，对返回值value和之前的输入内容inputTxt做了判断比较。如果执行了删除操作，那么无论光标在什么位置，都会删除inputTxt末尾的字符并重新赋值。

## 分析结论

TextAreaOptions.text没有进行双向绑定，且每次删除操作总是在onChange回调中删除被@State装饰的状态变量inputTxt末尾的字符并重新赋值，导致了光标无论处于什么位置，点击软键盘的删除按钮，光标都会跳转到最后并删除最后一个字符。

## 修改建议

* 方案一：对于需要移动光标删除输入框内容中间部分的字符时，需要将onChange回调函数的返回值赋值给TextAreaOptions.text对应的被@State装饰的状态变量，示例代码如下：

  ```ts
  @Entry
  @Component
  struct TextAreaExample {
    @State inputTxt: string = '无';
    controller: TextAreaController = new TextAreaController();

    build() {
      Column() {
        TextArea({
          text: this.inputTxt,
          placeholder: '请输入消息...',
          controller: this.controller
        })
          .placeholderFont({ size: 16, weight: 400 })
          .width(336)
          .height(56)
          .margin(20)
          .fontSize(16)
          .fontColor('#182431')
          .backgroundColor('#FFFFFF')
          .onChange((value: string) => {
            this.inputTxt = value;
          });
      }.width('100%').height('100%').backgroundColor('#F1F3F5');
    }
  }
  ```

* 方案二：TextAreaOptions.text使用$$双向绑定变量，示例代码如下：

  ```ts
  @Entry
  @Component
  struct TextAreaExampleV2 {
    @State inputTxt: string = '无';
    controller: TextAreaController = new TextAreaController();

    build() {
      Column() {
        TextArea({
          text: $$this.inputTxt,
          placeholder: '请输入消息...',
          controller: this.controller
        })
          .placeholderFont({ size: 16, weight: 400 })
          .width(336)
          .height(56)
          .margin(20)
          .fontSize(16)
          .fontColor('#182431')
          .backgroundColor('#FFFFFF');
      }.width('100%').height('100%').backgroundColor('#F1F3F5');
    }
  }
  ```
