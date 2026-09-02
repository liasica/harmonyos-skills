---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1232
title: 如何实现应用窗口在指定时间内无交互的弹框提示功能
breadcrumb: FAQ > 应用框架开发 > UI框架 > 窗口管理 > 如何实现应用窗口在指定时间内无交互的弹框提示功能
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:14+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:bd80bf950b1f0815cfc4ac125a1de4c94bdf55b20591f29e83be75f1c881c45c
---

## 问题现象

超过一定时间没操作过应用，则弹出弹窗提示。如何实现？

## 背景知识

* [on('noInteractionDetected')](../harmonyos-references/arkts-apis-window-window.md#onnointeractiondetected12)：开启本窗口在指定超时时间内无交互事件的监听，交互事件支持物理键盘输入事件和屏幕触控点击事件，不支持软键盘输入事件。
* [AlertDialog](../harmonyos-references/ts-methods-alert-dialog-box.md)：显示警告弹窗组件，可设置文本内容与响应回调。

## 解决方案

实现思路：参考AlertDialog实现方案设计警告弹窗，然后在aboutToAppear中添加对超时无交互时间的监听，实现超时监听触发后打开警告弹窗的效果。具体实现步骤如下：

1. 在EntryAbility.ets文件中获取到对应的WindowStage实例，并将其存储到AppStorage中。示例代码如下：

   ```screen
   onWindowStageCreate(windowStage: window.WindowStage): void {
     // 第一步：通过AppStorage保存WindowStage实例
     AppStorage.setOrCreate('windowStage', windowStage);

     // Main window is created, set main page for this ability
     hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onWindowStageCreate');

     windowStage.loadContent('pages/Index', (err) => {
       if (err.code) {
         hilog.error(DOMAIN, 'testTag', 'Failed to load the content. Cause: %{public}s', JSON.stringify(err));
         return;
       }
       hilog.info(DOMAIN, 'testTag', 'Succeeded in loading the content.');
     });
   }
   ```
2. 实现警告弹窗，示例代码如下：

   ```screen
   dialogControllerConfirm: CustomDialogController = new CustomDialogController({
     builder: AlertDialog({
       primaryTitle: '警告',
       secondaryTitle: '超时提醒',
       content: '超过6秒未使用屏幕',
       primaryButton: {
         value: '取消',
         action: () => {
         },
       },
       secondaryButton: {
         value: '确认',
         role: ButtonRole.ERROR,
         action: () => {
           console.info('Callback when the second button is clicked');
         }
       },
     }),
   });
   ```
3. 在aboutToAppear阶段，使用on('noInteractionDetected')开启本窗口在指定超时时间内无交互事件的监听，示例代码如下：

   ```screen
   aboutToAppear(): void {
     let windowClass: window.Window | undefined = undefined;
     if (this.windowStage){
       this.windowStage.getMainWindow((err: BusinessError, data) => {
         const errCode: number = err.code;
         if (errCode) {
           console.error(`Failed to obtain the main window. Cause code: ${err.code}, message: ${err.message}`);
           return;
         };
         windowClass = data;
         try {
           windowClass.on('noInteractionDetected', 6, () => {
             console.info('no interaction in 6s');
             this.dialogControllerConfirm.open();
           });
         } catch (exception) {
           console.error(`Failed to register callback. Cause code: ${exception.code}, message: ${exception.message}`);
         };
       });
     };
   };
   ```
4. 完整代码：

   ```screen
   import { window } from '@kit.ArkUI';
   import { BusinessError } from '@kit.BasicServicesKit';
   import { AlertDialog } from '@kit.ArkUI';

   @Entry
   @Component
   struct Index {
     @State message: string = 'Hello World';
     @StorageLink('windowStage') windowStage: window.WindowStage | undefined = AppStorage.get('windowStage');
     dialogControllerConfirm: CustomDialogController = new CustomDialogController({
       builder: AlertDialog({
         primaryTitle: '警告',
         secondaryTitle: '超时提醒',
         content: '超过6秒未使用屏幕',
         primaryButton: {
           value: '取消',
           action: () => {
           },
         },
         secondaryButton: {
           value: '确认',
           role: ButtonRole.ERROR,
           action: () => {
             console.info('Callback when the second button is clicked');
           }
         },
       }),
     });

     aboutToAppear(): void {
       let windowClass: window.Window | undefined = undefined;
       if (this.windowStage){
         this.windowStage.getMainWindow((err: BusinessError, data) => {
           const errCode: number = err.code;
           if (errCode) {
             console.error(`Failed to obtain the main window. Cause code: ${err.code}, message: ${err.message}`);
             return;
           };
           windowClass = data;
           try {
             windowClass.on('noInteractionDetected', 6, () => {
               console.info('no interaction in 6s');
               this.dialogControllerConfirm.open();
             });
           } catch (exception) {
             console.error(`Failed to register callback. Cause code: ${exception.code}, message: ${exception.message}`);
           };
         });
       };
     };

     build() {
       RelativeContainer() {
         Text(this.message)
           .id('HelloWorld')
           .fontSize($r('app.float.page_text_font_size'))
           .fontWeight(FontWeight.Bold)
           .alignRules({
             center: { anchor: '__container__', align: VerticalAlign.Center },
             middle: { anchor: '__container__', align: HorizontalAlign.Center }
           })
           .onClick(() => {
             this.message = 'Welcome';
           });
       }
       .height('100%')
       .width('100%');
     };
   };
   ```

   效果：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f6/v3/PsnasKpHSIiwNsiOOtJVGw/zh-cn_image_0000002658953255.png "点击放大")
