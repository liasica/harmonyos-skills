---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/use-inputmethod-in-custom-edit-box
title: 在自绘编辑框中使用输入法
breadcrumb: 指南 > 应用框架 > IME Kit（输入法开发服务） > 在自绘编辑框中使用输入法
category: harmonyos-guides
scraped_at: 2026-09-02T14:49:57+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:ceff3003a57d38b4559f450f4360404c60dee02ede480840b9a254444ee131b2
---

在输入法框架中，可以通过[getController](../harmonyos-references/js-apis-inputmethod.md#inputmethodgetcontroller9)方法获取到[InputMethodController](../harmonyos-references/js-apis-inputmethod.md#inputmethodcontroller)实例来绑定输入法并监听输入法应用的各种操作，比如插入、删除、选择、光标移动等。这样就可以在自绘编辑框中使用输入法，并实现更加灵活和自由的编辑操作。

## 开发步骤

1. 开发者在自绘编辑框中使用输入法时，首先需要在DevEco Studio工程中新建一个ets文件，命名为自定义控件的名称，本示例中命名为CustomInput，在文件中定义一个自定义控件，并从@kit.IMEKit中导入inputMethod。

   ```ets
   import { inputMethod } from '@kit.IMEKit';

   @Component
   export struct CustomInput {
     build() {
     }
   }
   ```
2. 在控件中，使用Text组件作为自绘编辑框的文本显示组件，使用状态变量inputText作为Text组件要显示的内容。

   ```typescript
   import { BusinessError } from '@kit.BasicServicesKit';
   import { inputMethod } from '@kit.IMEKit';
   import Log from '../model/Log';

   const TAG = '[Submenu]';

   @Component
   export struct CustomInput {
     @State inputText: string = ''; // inputText作为Text组件要显示的内容
     private isAttach: boolean = false;
     private inputController: inputMethod.InputMethodController = inputMethod.getController();

     build() {
       Text(this.inputText) // Text组件作为自绘编辑框的文本显示组件。
         .fontSize(16)
         .width('100%')
         .lineHeight(40)
         .id('customInput')
         .height(45)
         .border({ color: '#554455', radius: 30, width: 1 })
         .maxLines(1)
         .onBlur(() => {
           this.off();
         })
         .onClick(() => {
           this.attachAndListener(); // 点击控件
         })
     }
   ```
3. 在控件中获取InputMethodController实例，先在文本点击时调用controller实例的attach方法绑定和拉起软键盘，再注册监听输入法插入文本、删除等方法。本示例仅展示插入、删除。

   ```typescript
   import { BusinessError } from '@kit.BasicServicesKit';
   import { inputMethod } from '@kit.IMEKit';
   import Log from '../model/Log';

   const TAG = '[Submenu]';

   @Component
   export struct CustomInput {
     @State inputText: string = ''; // inputText作为Text组件要显示的内容
     private isAttach: boolean = false;
     private inputController: inputMethod.InputMethodController = inputMethod.getController();

     build() {
       Text(this.inputText) // Text组件作为自绘编辑框的文本显示组件。
         .fontSize(16)
         .width('100%')
         .lineHeight(40)
         .id('customInput')
         .height(45)
         .border({ color: '#554455', radius: 30, width: 1 })
         .maxLines(1)
         .onBlur(() => {
           this.off();
         })
         .onClick(() => {
           this.attachAndListener(); // 点击控件
         })
     }
     async attachAndListener() { // 绑定和设置监听
       focusControl.requestFocus('customInput');
       try {
         await this.inputController.attach(true, {
           inputAttribute: {
             textInputType: inputMethod.TextInputType.TEXT,
             enterKeyType: inputMethod.EnterKeyType.SEARCH
           }
         });
         if (!this.isAttach) {
           this.inputController.on('insertText', (text) => {
             this.inputText += text;
           })
           this.inputController.on('deleteLeft', (length) => {
             this.inputText = this.inputText.substring(0, this.inputText.length - length);
           })
           this.isAttach = true;
         }
       } catch (err) {
         let error = err as BusinessError;
         Log.showError(TAG, `attach catch error: ${error.code} ${error.message}`);
       }
     }

     off() {
       this.isAttach = false;
       this.inputController.off('insertText');
       this.inputController.off('deleteLeft');
     }
   }
   ```
4. 在应用界面布局中引入该控件即可，此处假设使用界面为Index.ets和控件CustomInput.ets在同一目录下。

   ```typescript
   CustomInput()
   ```

## 示例效果图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9b/v3/W8t5wWLxRGKoLYcJdAgAHQ/zh-cn_image_0000002706834208.png)
