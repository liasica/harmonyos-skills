---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ime-7
title: 输入法预上屏如何实现
breadcrumb: FAQ > 应用框架开发 > 输入法框架 > 输入法开发（IME） > 输入法预上屏如何实现
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:28+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:5f88919c94cf47344c3d193ac0ec50052e2e5686f1af07a0bca221d47f3c3f1e
---

## 问题现象

在开发一个输入法应用中，如何实现用户在键盘输入内容后，在候选词尚未被用户确认上屏之前，就提前将正在输入的拼音或候选词临时显示在应用输入框中？

## 背景知识

* 预上屏是一种允许输入法将未最终确认的输入内容（如拼音串、首个候选词）提前显示在应用编辑框中的机制。
* [输入法服务](../harmonyos-references/js-apis-inputmethodengine.md)提供了[setPreviewText](../harmonyos-references/js-apis-inputmethodengine.md#setpreviewtext12)接口来设置预上屏文本，[finishTextPreview](../harmonyos-references/js-apis-inputmethodengine.md#finishtextpreview12)接口来结束预上屏。

## 解决方案

1. 设置输入法事件监听，实现文本插入、删除、预上屏等方法：

   ```ts
   import { display } from '@kit.ArkUI';
   import { inputMethodEngine, InputMethodExtensionContext } from '@kit.IMEKit';
   import { BusinessError } from '@kit.BasicServicesKit';

   // 调用输入法框架的getInputMethodAbility方法获取实例，并由此实例调用输入法框架功能接口
   const inputMethodAbility: inputMethodEngine.InputMethodAbility = inputMethodEngine.getInputMethodAbility();

   export class KeyboardController {
     private mContext: InputMethodExtensionContext | undefined = undefined; // 保存InputMethodExtensionAbility中的context属性
     private panel: inputMethodEngine.Panel | undefined = undefined;
     private textInputClient: inputMethodEngine.InputClient | undefined = undefined;
     private keyboardController: inputMethodEngine.KeyboardController | undefined = undefined;
     private intputText: string = '';
     private previewContent: string = '';

     constructor() {
     }

     public onCreate(context: InputMethodExtensionContext): void {
       this.mContext = context;
       this.initWindow(); // 初始化窗口
       this.registerListener(); // 注册对输入法框架的事件监听
     }

     public onDestroy(): void {
       // 应用生命周期销毁
       this.unRegisterListener(); // 去注册事件监听
       if (this.panel) { // 销毁窗口
         inputMethodAbility.destroyPanel(this.panel);
       }
       if (this.mContext) {
         this.mContext.destroy();
       }
     }

     public insertText(text: string): void {
       if (this.textInputClient) {
         this.textInputClient.insertText(text);
       }
     }

     public deleteForward(length: number): void {
       if (this.textInputClient) {
         this.textInputClient.deleteForward(length);
       }
     }

     setPreviewText(str: string) {
       if (this.textInputClient) {
         this.textInputClient.setPreviewText(str, { start: -1, end: -1 });
       }
     }

     // 初始化窗口
     private initWindow(): void {
       if (this.mContext === undefined) {
         return;
       }
       let dis = display.getDefaultDisplaySync();
       let dWidth = dis.width;
       let dHeight = dis.height;
       let keyHeightRate = 0.35;
       let keyHeight = dHeight * keyHeightRate;
       let nonBarPosition = dHeight - keyHeight;
       let panelInfo: inputMethodEngine.PanelInfo = {
         type: inputMethodEngine.PanelType.SOFT_KEYBOARD,
         flag: inputMethodEngine.PanelFlag.FLG_FIXED
       };
       inputMethodAbility.createPanel(this.mContext, panelInfo).then(async (inputPanel: inputMethodEngine.Panel) => {
         this.panel = inputPanel;
         if (this.panel) {
           await this.panel.resize(dWidth, keyHeight);
           await this.panel.moveTo(0, nonBarPosition);
           await this.panel.setUiContent('InputMethodExtensionAbility/pages/InputIndex');
           // 获取输入法键盘与系统面板偏移区域大小，实际开发中可以根据实际情况判断是否需要实现
           let defaultDisplay = display.getDefaultDisplaySync();
           if (defaultDisplay !== undefined) {
             this.panel.getSystemPanelCurrentInsets(defaultDisplay.id)
               .then((insets: inputMethodEngine.SystemPanelInsets) => {
                 console.info(`getSystemPanelCurrentInsets success, insets is { left: ${insets.left}, right: ${insets.right}, bottom: ${insets.bottom} }`);
               })
               .catch((error: BusinessError) => {
                 console.error(`getSystemPanelCurrentInsets failed, code: ${error.code}, message: ${error.message}`);
               });
           }
         }
       }).catch((err: BusinessError) => {
         console.error(`Failed to createPanel, code: ${err.code}, message: ${err.message}`);
       });
     }

     private registerListener(): void {
       this.registerInputListener(); // 注册对输入法框架服务的监听
       // 注册隐藏键盘事件监听等
     }

     private registerInputListener(): void {
       // 注册开始输入的事件监听
       inputMethodAbility.on('inputStart', (kbController, textInputClient) => {
         this.textInputClient = textInputClient; // 此为输入法客户端实例，由此调用输入法框架提供给输入法应用的功能接口
         this.keyboardController = kbController;
       });
       inputMethodAbility.on('inputStop', this.inputStopCallback);
     }

     private inputStopCallback(): void {
       this.onDestroy(); // 销毁KeyboardController
     }

     private unRegisterListener(): void {
       inputMethodAbility.off('inputStart');
       inputMethodAbility.off('inputStop', this.inputStopCallback);
     }
   }

   const keyboardController = new KeyboardController();

   export default keyboardController;
   ```
2. 定义软键盘的按键显示内容，候选词框，如按下数字键，内容不会直接上屏，而是在编辑框中显示预上屏内容，点击候选词才会正式插入文本：

   ```ts
   import keyboardController from '../model/KeyboardController';

   @Entry
   @Component
   struct InputIndex {
     @State numberList: Array<string> = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'];
     @Provide previewContent: string = '';

     build() {
       Stack() {
         Column() {
           Row() {
             Row({ space: 50 }) {
               Text(this.previewContent)
                 .fontColor('#000')
                 .backgroundColor('#fff')
                 .fontSize(25)
                 .opacity(0.7)
                 .onClick(() => {
                   keyboardController.insertText(this.previewContent);
                   this.previewContent = '';
                 })
             }
             .margin({ left: '16px', right: '16px' })
           }
           .width('100%')
           .justifyContent(FlexAlign.Start)
           .height(50)

           Row({ space: 20 }) {
             ForEach(this.numberList, (item: string) => {

               Text(item)
                 .fontSize(30)
                 .fontColor('#000')
                 .backgroundColor('#fff')
                 .borderRadius(6)
                 .onClick(() => {
                   this.previewContent += item;
                   keyboardController.setPreviewText('预上屏内容[' + this.previewContent + ']');
                 })
             }, (item: string) => item)

           }
           .borderRadius(6)
           .margin({ top: 50, bottom: 80 })

           Column() {
             Text('删除').fontSize(20).fontColor('#000')
           }
           .backgroundColor('#fff')
           .width('13%')
           .borderRadius(6)
           .onClick(() => {
             keyboardController.deleteForward(1);
             this.previewContent = this.previewContent.substring(0, this.previewContent.length - 1);
           })

         }
         .height('100%')
       }
       .height('100%')
     }
   }
   ```

## 常见FAQ

Q：输入法服务预上屏文本如何实现下划线效果？

A：HarmonyOS预上屏文本暂不支持下划线效果，此能力尚在规划中。

Q：[setPreviewTextSync](../harmonyos-references/js-apis-inputmethodengine.md#setpreviewtextsync12)接口中range参数是实际意义?

A：[setPreviewText](../harmonyos-references/js-apis-inputmethodengine.md#setpreviewtext12)(text: string, range: Range)设置预上屏文本。其中参数text是将被预上屏的文本，range是目标替换的文本范围：

* 假如输入框已有预上屏文本'aaa'，当range参数值为{start: -1, end: -1}时，默认将参数text替换当前预上屏区域全部文本。

  setPreviewText('', { start: -1, end: -1 })表示清除预上屏区域文本'aaa'。

  setPreviewText('bbb', { start: -1, end: -1 })表示'bbb'替换预上屏区域文本'aaa'。
* 假如输入框已有预上屏文本'aaa'，当range参数中的start等于end，默认将参数text插入start对应的光标位置。

  setPreviewText('bbb', { start: 2, end: 2 })表示将参数'bbb'插入到'aaa'中的第2个光标位置，即为abbbaa。
* 假如输入框已有预上屏文本'aaa'，当range参数中start不等于end，将参数text替换range对应区域的文本。

  setPreviewText('bbb', { start: 1, end: 2 })表示将参数'bbb'替换'aaa'中的1-2的位置，即为bbba。
* 假如输入框已有预上屏文本'aaa'，当start与end为其他含有负数值的组合，按照参数错误返回。

  setPreviewText('bbb', { start: -6, end: -1 })按参数错误返回。
* 当输入框已有预上屏文本'aaa'，参数range不得超过预上屏文本范围，否则按照参数错误返回。

  setPreviewText('bbb', { start: 2, end: 5 })按参数错误返回。
* 当输入框无预上屏文本，参数range不得超过输入框文本范围，否则按照参数错误返回。
