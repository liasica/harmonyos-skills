---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-883
title: TextInput限制输入
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > TextInput限制输入
category: harmonyos-faqs
scraped_at: 2026-09-02T15:03:54+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:a95094bc3ed0b66f3da45608159b48b61cf44a5316685ea1659505777e3ff47d
---

## 问题现象

TextInput如何限制输入的内容格式以及限制输入的内容长度？

## 背景知识

[TextInput](../harmonyos-references/ts-basic-components-textinput.md)是单行文本输入框组件，常用于响应用户的输入操作，比如手机号输入，表单的输入等。针对输入的内容格式以及长度、行数，一些场景下需要进行限制，常见的场景如下：

1. 限制输入的格式：
   * 限制只能输入手机号或者邮箱。
   * 首位不允许出现空格。
   * 限制输入中文、英文、数字或者emoji表情包。
   * 限制输入两位小数。
   * 限制输入数字范围。
2. 限制输入的长度：
   * 限制文本的内容长度，比如不超过20个字符。
   * 限制文本的字节数量，比如不超过32个字节。

## 解决方案

1. 限制输入的格式：
   * 限制只能输入手机号或者邮箱。

     TextInput的[InputType](../harmonyos-references/ts-basic-components-textinput.md#inputtype枚举说明)属性支持设置不同的输入框类型，利用InputType.PhoneNumber、InputType.Email可拉起数字键盘，即可限制类型为手机号码、邮箱：

     ```ts
     @Entry
     @Component
     export struct TextInputExample1 {

       build() {
         Column() {
           TextInput({ placeholder: '请输入手机号码' })
             .width('70%')
             .height('58')
             .type(InputType.PhoneNumber)
             .maxLength(11)
         }
         .height('100%')
         .width('100%')
       }
     }
     ```

     如果对type的过滤效果不满意，可以使用inputFilter覆盖。
   * 限制只能输入身份证号。

     ```ts
     import { PromptAction } from '@kit.ArkUI';

     @Entry
     @Component
     struct TextInputExample2 {
       @State message: string = '';
       promptAction: PromptAction = this.getUIContext().getPromptAction();

       build() {
         Column() {
           TextInput({ placeholder: '请输入身份证号', text: $$this.message })
             .inputFilter('[0-9Xx]')
             .maxLength(18)
             .onWillChange((info: EditableTextChangeValue) => {
               if (!info.content) {
                 return false;
               }
               if (checkIncludeWord(info.content)) {
                 // 非最后一位为X，X输入无效
                 this.message = info.content.replace(/[xX]/, '');
                 this.promptAction.showToast({ message: '输入不符合身份证号规则，仅最后一位可以为x或X' });
                 return false;
               } else {
                 return true;
               }
             })
             .onPaste((content) => {
               if (content.length > 18) {
                 this.promptAction.showToast({ message: '身份证号长度不超过18位' });
               }
               if (checkIncludeWord(content)) {
                 this.promptAction.showToast({
                   message: '输入不符合身份证号规则，除最后一位可为数字或大小写X外，其余应为数字'
                 });
               }
             })
         }
       }
     }

     function checkIncludeWord(content: string) {
       // 检测粘贴内容包含英文字母且非最后一位为x的情况
       let groups = content.match('[a-zA-Z]');
       if (groups && groups.length > 0) {
         if (groups.length === 1 && (content.endsWith('x') || content.endsWith('X')) && content.length === 18) {
           return false;
         }
         return true;
       }
       return false;
     }
     ```
   * 首位不允许出现空格。

     利用[onWillChange](../harmonyos-references/ts-basic-components-textinput.md#onwillchange15)事件监听将要输入的字符，如果字符以空格开头则阻止输入：

     ```ts
     @Entry
     @Component
     struct TextInputExample3 {
       @State text: string = '';
       controller: TextInputController = new TextInputController();
       @State value: string = '';

       build() {
         Column() {
           TextInput({ text: this.text, placeholder: 'input your word...', controller: this.controller })
             .width('70%')
             .height('58')
             .onWillChange((info) => {
               // 在将要输入时调用的回调。在返回true时，表示正常插入，返回false时，表示不插入。
               this.value = info.content;
               if (this.value.startsWith(' ')) {
                 return false;
               } else {
                 return true;
               }
             })
         }
         .height('100%')
         .width('100%')
       }
     }
     ```
   * 限制输入中文、英文、数字或者emoji表情包。

     TextInput的[inputFilter](../harmonyos-references/ts-basic-components-textinput.md#inputfilter8)属性支持输入正则表达式，以下使用正则表达式限制中文字符输入：

     ```ts
     @Entry
     @Component
     struct TextInputExample4 {
       @State text: string = '';
       controller: TextInputController = new TextInputController();

       build() {
         Column() {
           TextInput({ text: this.text, placeholder: 'input your word...', controller: this.controller })
             .width('70%')
             .height('58')
             .inputFilter('[^\u4e00-\u9fa5]', (val) => {
               console.error('限制输入中文内容 ： ', val);
               return 0;
             })
         }
         .height('100%')
         .width('100%')
       }
     }
     ```

     使用TextInput的[onWillChange](../harmonyos-references/ts-basic-components-textinput.md#onwillchange15)属性限制emoji表情包输入：

     ```ts
     @Entry
     @Component
     struct TextInputExample5 {
       @State text: string = '';
       controller: TextInputController = new TextInputController();

       build() {
         Column() {
           TextInput({ text: this.text, placeholder: 'input your word...', controller: this.controller })
             .width('70%')
             .height('58')
             .onWillChange((info: EditableTextChangeValue) => {
               // 表情不包括数字
               let regx1 = /\p{Emoji}(?<!\p{N})/gu;
               // 数字表情
               let regx2 = /[\d#*]\uFE0F?\u20E3/gu;
               // 圆圈数字表情
               let regx3 = /[\u2460-\u24FF\u3250-\u32FF]/g;
               if (info.content.match(regx1) || info.content.match(regx2) || info.content.match(regx3)) {
                 return false;
               } else {
                 return true;
               }
             })
         }
         .height('100%')
         .width('100%')
       }
     }
     ```
   * 限制输入两位小数。

     利用inputFilter限制输入格式，并在[onWillChange](../harmonyos-references/ts-basic-components-textinput.md#onwillchange15)方法内使用parseFloat和toFixed方法组合使其保留两位小数，最后限制输入的小数不超过两位：

     ```ts
     @Entry
     @Component
     struct TextInputExample6 {
       @State text: string = '';
       @State insertValue: string = '';
       controller: TextInputController = new TextInputController();

       build() {
         Column() {
           Text(`输入的值: ${this.insertValue}`)
           TextInput({ text: this.text, placeholder: 'input your word...', controller: this.controller })
             .width('70%')
             .height('58')
             .type(InputType.NUMBER_DECIMAL)
             .onWillChange((info) => {
               let input = info.content;
               let number = parseFloat(input);
               // 使用toFixed方法将浮点数格式化为保留两位小数的字符串
               this.insertValue = number.toFixed(2);
               if (this.insertValue.toString().split('.').length <= 1) {
                 return true;
               } else if ((this.insertValue.toString().split('.')[1].length) > 2) {
                 return false;
               }
               return true;
             })
             .inputFilter('^-?\\d*\\.?\\d{0,2}$', (val) => {
               console.info('限制输入两位小数 ： ', val);
             })
         }
         .height('100%')
         .width('100%')
       }
     }
     ```
   * 限制输入数字范围。

     使用TextInput的inputFilter属性限制只能输入负号和数字，并通过[onWillChange](../harmonyos-references/ts-basic-components-textinput.md#onwillchange15)事件处理输入内容以满足要求。以下为限制输入数字范围-50~150：

     ```ts
     @Entry
     @Component
     struct TextInputExample7 {
       @State message: string = '';

       build() {
         Column() {
           TextInput({ placeholder: '请输入-50~150', text: $$this.message })
             .inputFilter('[\-0-9]', (val) => {
               console.error('TextInputExample ： ' + val);
               return 0;
             })
             .onChange((text) => {
               if (!text || text === '-') {
                 return;
               }
               let num: number = Number(text);
               if (isNaN(num)) {
                 this.message = '0';
                 return;
               }
               if (num < -50) {
                 this.message = '-50';
               } else if (num > 150) {
                 this.message = '150';
               } else {
                 this.message = num.toString();
               }
             })
         }
       }
     }
     ```
2. 限制输入的长度。
   * 限制文本的内容长度，比如不超过20个字符。

     TextInput的[maxLength](../harmonyos-references/ts-basic-components-textinput.md#maxlength)属性可以限制文本的最大输入字符数：

     ```screen
     @Entry
     @Component
     struct TextInputExample8 {
       build() {
         Column() {
           TextInput()
             .width('70%')
             .height('58')
             .maxLength(20)
         }
         .height('100%')
         .width('100%')
       }
     }
     ```
   * 限制文本的字节数量，比如不超过32个字节。

     TextInput的onWillChange事件在输入内容发生变化前触发，获取到输入的字符串后循环遍历内容，利用charCodeAt方法获取该字符的UniCode码，若UniCode码>255则为中文，可以判断为2个字符。代码实现如下：

     ```ts
     @Entry
     @Component
     struct TextInputExample9 {
       @State text: string = '';
       @State lastText: string = '';
       controller: TextInputController = new TextInputController();

       getByteLength(str: string) {
         let byteLength = 0;
         for (let i = 0; i < str.length; i++) {
           const charCode = str.charCodeAt(i);
           if (charCode <= 0xff) {
             byteLength += 1;
           } else {
             byteLength += 2;
           }
         }
         return byteLength;
       }

       build() {
         Column() {
           TextInput({ text: this.text, placeholder: 'input your word...', controller: this.controller })
             .width('70%')
             .height('58')
             .onWillChange((info) => {
               let input = info.content;
               let num = this.getByteLength(input);
               if (num > 32) {
                 this.text = ' ';
                 this.text = this.lastText;
                 return false;
               } else {
                 this.lastText = input;
                 this.text = input;
               }
               return true;
             })
         }
         .height('100%')
         .width('100%')
       }
     }
     ```

     **说明** 

     限制TextInput组件输入的文本长度，当输入超过限制长度时，输入框会闪烁一下，然后显示限制长度内的文本内容。

     解决方案：使用onWillChange回调，在输入前对输入内容做判断，限制显示内容的长度。

## 常见FAQ

Q：TextInput和TextArea如何禁止输入？

A：可以设置输入框组件enabled属性为false来禁用文本输入。

Q：常见的用正则表达式过滤的场景有哪些？

A：较为常见的有英文和数字的过滤、中文的过滤以及手机号、邮箱、身份证号、银行卡号等表单验证场景。

Q：TextInput组件使用inputFilter字符串匹配无效，怎么处理？

A：TextInput组件的inputFilter仅支持单个字符匹配，粘贴时，inputFilter可以多字符匹配。可通过onWillChange事件处理文本内容。

Q：以上方法在其他组件适用吗？

A：TextInput、TextArea、Search都是输入框组件，以上方法在TextArea上也适用。

Q：如何只禁用空格键？

A：可以通过TextInput的inputFilter属性设置支持输入的正则表达式。参考示例如下：

```ts
@Entry
@Component
struct TextInputExample10 {
  message: string = '';

  build() {
    Column() {
      TextInput({ placeholder: '禁止空格输入', text: $$this.message })
        .inputFilter('^[^\\s]*$', (val) => {
          console.error('TextInputExample ： ', val);
        })
    }
  }
}
```

Q：inputFilter( '^\\d\*$' )过滤，会让键盘输入不能是负数，为什么还会导致通过手动设置的方式也无法设置负数？

A：通过软键盘输入、粘贴板粘贴、TextInput的text属性直接赋值、addText的方式都可以触发inputFilter过滤，是规格如此，所以即使通过粘贴板粘贴、addText的方式都无法输入负数。

Q：TextInput如何实现多行显示？

A：给TextInput的[style](../harmonyos-references/ts-basic-components-textinput.md#style9)设置为[TextInputStyle.Inline](../harmonyos-references/ts-basic-components-textinput.md#textinputstyle9枚举说明)内联输入风格后，再设置maxLines可实现多行显示。

## 总结

TextInput限制输入主要在内容格式以及长度方面。设置type、inputFilter以及maxLength属性即可快速达到所需限制效果，如果需要自定义实现限制策略，则可以使用onWillChange事件获取到用户输入的内容，然后针对字符串进行限制处理。
