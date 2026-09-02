---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1631
title: 如何在子窗口为主窗口打开半模态弹窗
breadcrumb: FAQ > 应用框架开发 > UI框架 > 窗口管理 > 如何在子窗口为主窗口打开半模态弹窗
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:13+08:00
doc_updated_at: 2026-07-15
content_hash: sha256:5bb40b5ad4a66492e89489927b6f2e3d4d71aa3d0a6e386ba6303b240454dbec
---

## 问题现象

通过windowStage.createSubWindow创建应用子窗口，在该子窗口中给组件绑定bindSheet，点击该组件主窗口没有显示半模态窗口。如何在子窗口为主窗口打开半模态弹窗？

## 背景知识

[openBindSheet](../harmonyos-references/arkts-apis-uicontext-uicontext.md#openbindsheet12)创建并弹出以bindSheetContent作为内容的半模态页面。通过该接口弹出的半模态页面样式完全按照bindSheetContent中设置的样式显示。

## 解决方案

出现问题现象所示的效果，是由于bindSheet绑定在了子窗口的组件，因此半模态弹窗只会出现在子窗口中。为了解决该问题，有如下两种方案：

方案一:

要实现在子窗口为主窗口打开半模态弹窗，需要在子窗口中先使用windowStage.getMainWindowSync().getUIContext()方法获取主窗口UIContext实例，再通过此实例调用openBindSheet在主窗口弹出半模态弹窗。完整示例代码如下：

1. 通过[AppStorage.setOrCreate](../harmonyos-references/ts-state-management.md#setorcreate10)存储WindowStage后在使用处获取到WindowStage实例，然后创建子窗口：

   ```ts
   // Index.ets文件
   import { window } from '@kit.ArkUI';
   import { BusinessError } from '@kit.BasicServicesKit';

   let windowStage_: window.WindowStage | undefined = undefined;
   let sub_windowClass: window.Window | undefined = undefined;

   @Entry
   @Component
   struct Index {
     private CreateSubWindow() {
       // 获取windowStage
       windowStage_ = AppStorage.get('windowStage');
       // 创建应用子窗口。
       if (windowStage_ == null) {
         console.error('Failed to create the subwindow. Cause: windowStage_ is null');
       } else {
         windowStage_.createSubWindow('mySubWindow', (err: BusinessError, data) => {
           let errCode: number = err.code;
           if (errCode) {
             console.error(`Failed to create the subwindow. Cause: error code: ${errCode}`);
             return;
           }
           sub_windowClass = data;
           console.info(`Succeeded in creating the subwindow. Data: ${data}`);
           // 子窗口创建成功后，设置子窗口的位置、大小及相关属性等。
           sub_windowClass.moveWindowTo(30, 300, (err: BusinessError) => {
             let errCode: number = err.code;
             if (errCode) {
               console.error(`Failed to move the window. Cause: error code: ${errCode}`);
               return;
             }
             console.info('Succeeded in moving the window.');
           });
           sub_windowClass.resize(1200, 680, (err: BusinessError) => {
             let errCode: number = err.code;
             if (errCode) {
               console.error(`Failed to change the window size. Cause: error code: ${errCode}`);
               return;
             }
             console.info('Succeeded in changing the window size.');
           });
           // 为子窗口加载对应的目标页面。
           sub_windowClass.setUIContent('pages/Page', (err: BusinessError) => {
             let errCode: number = err.code;
             if (errCode) {
               console.error(`Failed to load the content. Cause: error code: ${errCode}`);
               return;
             }
             console.info('Succeeded in loading the content.');
             // 显示子窗口。
             (sub_windowClass as window.Window).showWindow((err: BusinessError) => {
               let errCode: number = err.code;
               if (errCode) {
                 console.error(`Failed to show the window. Cause: error code: ${errCode}`);
                 return;
               }
               console.info('Succeeded in showing the window.');
             });
           });
         });
       }
     }

     private moveSubWindow() {
       (sub_windowClass as window.Window).moveWindowTo(20, 1800);
     }

     private destroySubWindow() {
       // 销毁子窗口。当不再需要子窗口时，可根据具体实现逻辑，使用destroy对其进行销毁。
       (sub_windowClass as window.Window).destroyWindow((err: BusinessError) => {
         let errCode: number = err.code;
         if (errCode) {
           console.error(`Failed to destroy the window. Cause: error code: ${errCode}`);
           return;
         }
         console.info('Succeeded in destroying the window.');
       });
     }

     build() {
       Row() {
         Column({ space: 10 }) {
           Button('CreateSubWindow')
             .width(220)
             .height(50)
             .onClick(() => {
               this.CreateSubWindow();
             });
           Button('moveSubWindow')
             .width(220)
             .height(50)
             .onClick(() => {
               this.moveSubWindow();
             });
           Button('destroySubWindow')
             .width(220)
             .height(50)
             .onClick(() => {
               this.destroySubWindow();
             });
         }
         .width('100%');
       }
       .height('100%');
     }
   }
   ```
2. 子窗口中通过windowStage.getMainWindowSync().getUIContext().openBindSheet弹出半模态弹窗：

   ```ts
   // Page.ets文件
   import { ComponentContent, window } from '@kit.ArkUI';
   import { BusinessError } from '@kit.BasicServicesKit';

   class Params {
     text: string = '';

     constructor(text: string) {
       this.text = text;
     }
   }

   let contentNode: ComponentContent<Params>;
   let gUIContext: UIContext;
   let windowStage: window.WindowStage = AppStorage.get('windowStage') as window.WindowStage;

   @Builder
   function buildText(params: Params) {
     Column() {
       Text(params.text);

       Button('Close BindSheet')
         .fontSize(15)
         .margin({top: 10})
         .onClick(() => {
           gUIContext.closeBindSheet(contentNode)
             .then(() => {
               console.info('closeBindSheet success');
             })
             .catch((err: BusinessError) => {
               console.error(`closeBindSheet error: error code ${err.code}, error message ${err.message}`);
             });
         });
     };
   }

   @Entry
   @Component
   struct subwindow {
     message: string = 'BindSheet';

     aboutToAppear() {
       windowStage = AppStorage.get('windowStage') as window.WindowStage;
       gUIContext = windowStage.getMainWindowSync().getUIContext();
       contentNode = new ComponentContent(this.getUIContext(), wrapBuilder(buildText), new Params(this.message));
     }

     build() {
       Column() {
         Text('open bindSheet')
           .borderRadius(8)
           .margin({ top: 15})
           .backgroundColor(0x317aff)
           .fontColor(Color.White)
           .padding(10)
           .onClick(() => {
             let uiContext = windowStage.getMainWindowSync().getUIContext();
             let uniqueId = this.getUniqueId();
             let frameNode: FrameNode | null = uiContext.getFrameNodeByUniqueId(uniqueId);
             let targetId = frameNode?.getFirstChild()?.getUniqueId();
             uiContext.openBindSheet(contentNode, {
               height: 300,
               title: { title: 'Title', subtitle: 'subtitle' }
             }, targetId)
               .then(() => {
                 console.info('openBindSheet success');
               })
               .catch((err: BusinessError) => {
                 console.error(`openBindSheet error: ${err.code} ${err.message}`);
               });
           });
       }
       .backgroundColor('#dddddd')
       .width('100%')
       .height(680);
     }
   }
   ```

方案二:

使用[emitter](../harmonyos-references/js-apis-emitter.md)的事件订阅机制。当在子窗口为主窗口打开半模态弹窗时，开始发送事件，而主窗口内则订阅该事件，响应弹出半模态弹窗，此时则不再需要获取[WindowStage](../harmonyos-references/arkts-apis-window-windowstage.md)。完整的示例代码如下：

1. 子窗口需要在主窗口打开半模态弹窗时发送事件。

   ```ts
   // subwindow2.ets文件
   import { emitter } from '@kit.BasicServicesKit';

   @Entry
   @Component
   struct subwindow {
     build() {
       Column() {
         Text('open bindSheet method two.')
           .borderRadius(8)
           .backgroundColor(0x317aff)
           .fontColor(Color.White)
           .padding(10)
           .margin({top: 15})
           .onClick(() => {
             // 发送事件，在主窗口打开半模态弹窗
             emitter.emit('OpenBindSheet');
           });
       }
       .width('100%')
       .height(680)
       .padding(10)
       .backgroundColor('#dddddd');
     }
   }
   ```
2. 主窗口响应事件，通过this.getUIContext().openBindSheet打开半模态弹窗。

   ```ts
   // mainwindow.ets文件
   import { ComponentContent, window } from '@kit.ArkUI';
   import { BusinessError, emitter } from '@kit.BasicServicesKit';

   let windowStage_: window.WindowStage | undefined = undefined;
   let sub_windowClass: window.Window | undefined = undefined;

   class Params {
     text: string = '';
     context: UIContext | undefined;

     constructor(text: string, context: UIContext) {
       this.text = text;
       this.context = context;
     }
   }

   let contentNode: ComponentContent<Params> | undefined;

   @Builder
   function buildText(params: Params) {
     Column() {
       Text(params.text);

       Button('Close BindSheet')
         .fontSize(15)
         .margin({top: 10})
         .onClick(() => {
           if (params.context) {
             params.context.closeBindSheet(contentNode)
               .then(() => {
                 console.info('closeBindSheet success');
               })
               .catch((err: BusinessError) => {
                 console.error(`closeBindSheet error: error code ${err.code}, error message ${err.message}`);
               });
           }
         });
     };
   }

   @Entry
   @Component
   struct Index {
     private CreateSubWindow() {
       // 获取windowStage
       windowStage_ = AppStorage.get('windowStage');
       // 1.创建应用子窗口
       if (windowStage_ == null) {
         console.error('Failed to create the subwindow. Cause: windowStage_ is null');
       } else {
         windowStage_.createSubWindow('mySubWindow', (err: BusinessError, data) => {
           let errCode: number = err.code;
           if (errCode) {
             console.error(`Failed to create the subwindow. Cause: error code: ${errCode}`);
             return;
           }
           sub_windowClass = data;
           console.info(`Succeeded in creating the subwindow. Data: ${data}`);
           // 2.子窗口创建成功后，设置子窗口的位置、大小及相关属性等
           sub_windowClass.moveWindowTo(55, 300, (err: BusinessError) => {
             let errCode: number = err.code;
             if (errCode) {
               console.error(`Failed to move the window. Cause: error code: ${errCode}`);
               return;
             }
             console.info('Succeeded in moving the window.');
           });
           sub_windowClass.resize(1100, 680, (err: BusinessError) => {
             let errCode: number = err.code;
             if (errCode) {
               console.error(`Failed to change the window size. Cause: error code: ${errCode}`);
               return;
             }
             console.info('Succeeded in changing the window size.');
           });
           // 3.为子窗口加载对应的目标页面
           sub_windowClass.setUIContent('pages/subwindow2', (err: BusinessError) => {
             let errCode: number = err.code;
             if (errCode) {
               console.error(`Failed to load the content. Cause: error code: ${errCode}`);
               return;
             }
             console.info('Succeeded in loading the content.');
             // 4.显示子窗口
             (sub_windowClass as window.Window).showWindow((err: BusinessError) => {
               let errCode: number = err.code;
               if (errCode) {
                 console.error(`Failed to show the window. Cause: error code: ${errCode}`);
                 return;
               }
               console.info('Succeeded in showing the window.');
             });
           });
         });
       }
     }

     private moveSubWindow() {
       (sub_windowClass as window.Window).moveWindowTo(20, 1800);
     }

     private destroySubWindow() {
       // 5.销毁子窗口，当不再需要子窗口时，可根据具体实现逻辑，使用destroy对其进行销毁
       (sub_windowClass as window.Window).destroyWindow((err: BusinessError) => {
         let errCode: number = err.code;
         if (errCode) {
           console.error(`Failed to destroy the window. Cause: error code: ${errCode}`);
           return;
         }
         console.info('Succeeded in destroying the window.');
       });
     }

     aboutToAppear(): void {
       emitter.on('OpenBindSheet', () => {
         let uniqueId = this.getUniqueId();
         let targetId = this.getUIContext().getFrameNodeByUniqueId(uniqueId)?.getFirstChild()?.getUniqueId();
         contentNode =
           new ComponentContent(this.getUIContext(), wrapBuilder(buildText), new Params('BindSheet', this.getUIContext()));
         this.getUIContext().openBindSheet(contentNode, {
           height: 300, title: {
             title: 'Title',
             subtitle: 'subtitle'
           }
         }, targetId);
       });
     }

     build() {
       Row() {
         Column({ space: 15 }) {
           Button('CreateSubWindow')
             .width(220)
             .height(45)
             .onClick(() => {
               this.CreateSubWindow();
             });
           Button('moveSubWindow')
             .width(220)
             .height(45)
             .onClick(() => {
               this.moveSubWindow();
             });
           Button('destroySubWindow')
             .width(220)
             .height(45)
             .onClick(() => {
               this.destroySubWindow();
             });
         }
         .width('100%');
       }
       .height('100%')
       .backgroundColor(Color.White);
     }
   }
   ```
