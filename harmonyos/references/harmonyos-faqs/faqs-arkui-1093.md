---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1093
title: 如何实现全局loading控件
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 如何实现全局loading控件
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:06+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:1c0594a0727f6ae957b0d083c4ee1e870dfd51dde231eca63343b37e641fc1ed
---

## 问题现象

实现一个可以作用于全局网络请求时，类似拦截器的loading弹窗，并在请求成功时关闭。

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f1/v3/v6vUWTP3QIqGH-1Mh-QCKw/zh-cn_image_0000002628407366.png "点击放大")

## 背景知识

* [LoadingProgress](../harmonyos-references/ts-basic-components-loadingprogress.md)：用于显示加载动效的组件。
* [window](../harmonyos-references/arkts-apis-window-window.md)：当前窗口实例，窗口管理器管理的基本单元。

## 解决方案

构建一个新窗口用作全局loading控件，可在UI页面直接调用。使用window接口模拟实现网络请求拦截。定义新窗口，模拟弹窗，在窗口中自定义loading组件。并且实现沉浸式效果。

**实现思路**：HarmonyOS中自定义弹窗需要在@Component中才可以调用，而问题现象需要用在全局，window窗口可以实现此功能。在EntryAbility.ets文件中定义一个新窗口，封装window方法类用于后续调用，最后在UI页面中调用实现用作全局网络请求时拦截的loading弹窗。

1. 在EntryAbility.ets定义窗口，并在onWindowStageCreate()函数中调用。代码如下：

   ```ts
   // 定义窗口
   subWindowStage: window.WindowStage | null = null;

   onWindowStageCreate(windowStage: window.WindowStage): void {
     // Main window is created, set main page for this ability
     hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onWindowStageCreate');

     // onWindowStageCreate()函数，并且增加监听
     this.subWindowStage = windowStage;
     const that: EntryAbility = this;
     this.context.eventHub.on('createWindow', (data: Data) => {
       if (that.subWindowStage != undefined) {
         data.subWindowStage = that.subWindowStage;
       } else {
         hilog.info(0x0000, 'testTag', '%{public}s', 'that.subWindowStage == undefined');
       }
     });

     windowStage.loadContent('pages/Index', (err) => {
       if (err.code) {
         hilog.error(DOMAIN, 'testTag', 'Failed to load the content. Cause: %{public}s', JSON.stringify(err));
         return;
       }
       hilog.info(DOMAIN, 'testTag', 'Succeeded in loading the content.');
     });
   }
   ```
2. 封装window方法，CommonWindow.ets文件。

   ```ts
   import window from '@ohos.window';
   import common from '@ohos.app.ability.common';
   import { BusinessError } from '@ohos.base';
   import { entryName } from './MainPage';

   export class CommonWindow {
     private storage: LocalStorage | null = null;
     private subWindow: window.Window | null = null;
     private windowStageUtils: window.WindowStage | null = null;

     private init(ctx: common.UIAbilityContext) {
       let data: Data = { subWindowStage: null, storage: null };
       ctx.eventHub.emit('createWindow', data);
       this.windowStageUtils = data.subWindowStage;
       this.storage = data.storage;
       console.info('aboutToAppear end createWindowStage');
       ctx.eventHub.on('closeWindow', (data: Data) => {
         this.destroySubWindow();
         console.info(`data: ${JSON.stringify(data)}`);
       });
     }

     showWindow(ctx: common.UIAbilityContext) {
       this.init(ctx);
       if (this.subWindow) {
         console.info('subWindow is already exist');
         return;
       }
       try {
         if (!this.windowStageUtils) {
           console.error('this.windowStage1 is null');
           return;
         }
         this.windowStageUtils.createSubWindow('mySubWindow', (err: BusinessError, data) => {
           const errCode: number = err.code;
           if (errCode) {
             console.error(`Failed to create the subWindow. Cause: ${JSON.stringify(err)}`);
             return;
           }
           this.subWindow = (data as window.Window);
           console.info(`Succeeded in creating the subWindow. Data: ${JSON.stringify(data)}`);
           if (!this.subWindow) {
             console.info('Failed to load the content. Cause: windowClass is null');
           } else {
             let names: Array<'status' | 'navigation'> = [];
             this.subWindow.setWindowSystemBarEnable(names);
             this.subWindow.setWindowTouchable(false); // 设置是否可以点击
             this.loadContent(entryName);
             this.showSubWindow();
           }
         });
       } catch (exception) {
         console.error(`Failed to create the window. Cause: ${JSON.stringify(exception)}`);
       }
     }

     private showSubWindow() {
       if (this.subWindow) {
         this.subWindow.showWindow((err: BusinessError) => {
           const errCode: number = err.code;
           if (errCode) {
             console.error(`Failed to show the window. Cause: ${JSON.stringify(err)} `);
             return;
           }
           console.info('Succeeded in showing the window.');
         });
       } else {
         console.info('showSubWindow subWindow not created.');
       }
     }

     destroySubWindow() {
       if (this.subWindow) {
         this.subWindow.destroyWindow((err) => {
           const errCode: number = err.code;
           if (errCode) {
             console.error(`Failed to destroy the window. Cause: ${JSON.stringify(err)}`);
             return;
           }
           this.subWindow = null;
         });
       } else {
         console.info('showSubWindow subWindow not created.');
       }
     }

     private loadContent(path: string) {
       if (this.subWindow) {
         let that = this;
         let pAra: Record<string, number> = { 'PropA': 66 };
         that.storage = new LocalStorage(pAra);
         if (that.storage != null && this.subWindow != null) {
           that.storage.setOrCreate('windowObj', this.subWindow);
         }
         this.subWindow.loadContentByName(path, this.storage, (err: BusinessError) => {
           const errCode: number = err.code;
           if (errCode) {
             return;
           }
           if (this.subWindow) {
             this.subWindow.setWindowBackgroundColor('#88000000');
           }
         });
       } else {
         console.info('loadContent subWindow not created.');
       }
     }
   }

   export interface Data {
     subWindowStage: window.WindowStage | null,
     storage: LocalStorage | null
   }
   ```
3. MainPage页面，沉浸式弹窗页面。

   ```ts
   import window from '@ohos.window';

   export const entryName: string = 'loadingPage';

   @Entry({ routeName: entryName })
   @Component
   export struct MainPage {
     @LocalStorageLink('PropA') varA: number | undefined = 1;
     localStorage = this.getUIContext().getSharedLocalStorage();

     // 页面生命周期：打开沉浸式
     onPageShow() {
       window.getLastWindow(this.getUIContext().getHostContext(), (err, win) => {
         // 获取当前窗口的属性
         let prop: window.WindowProperties = win.getWindowProperties();
         // 打印当前窗口属性
         console.info(JSON.stringify(prop));
         console.error(`err: ${err}`);
         win.setWindowLayoutFullScreen(true);
       });
     }

     // 页面生命周期：关闭沉浸式
     onPageHide() {
       window.getLastWindow(this.getUIContext().getHostContext(), (err, win) => {
         console.error(`err: ${err}`);
         win.setWindowLayoutFullScreen(false);
       });
     }

     aboutToAppear() {
       this.varA = this.localStorage?.get<number>('PropA');
     }

     build() {
       Column() {
         LoadingProgress()
           .width(72)
           .color('#88ffffff')
       }
       .justifyContent(FlexAlign.Center)
       .height('100%')
       .width('100%');
     }
   }
   ```
4. UI页面，初始页，调用window类，按钮唤出弹窗。

   ```ts
   import { CommonWindow } from '../utils/CommonWindow';
   import { common } from '@kit.AbilityKit';

   @Entry
   @Component
   struct Index {
     ctx: common.UIAbilityContext | undefined = undefined;

     aboutToAppear(): void {
       this.ctx = this.getUIContext().getHostContext() as common.UIAbilityContext;
     }

     testSubWindowDialog() {
       let window = new CommonWindow();
       if (!this.ctx) {
         return;
       }
       window.showWindow(this.ctx);
       setTimeout(() => {
         window.destroySubWindow();
       }, 2000);
     }

     build() {
       Row() {
         Column() {
           Button('子窗口弹窗')
             .margin({ top: 20 })
             .onClick(() => {
               this.testSubWindowDialog();
             });
         }
         .width('100%');
       }
       .height('100%');
     }
   }
   ```

## 总结

运用窗口特性，封装类似弹窗的效果，相比于常规弹窗[CustomDialog](../harmonyos-references/ts-methods-custom-dialog-box.md#customdialogcontroller)和[getPromptAction()](../harmonyos-references/arkts-apis-uicontext-uicontext.md#getpromptaction).[openCustomDialog](../harmonyos-references/arkts-apis-uicontext-promptaction.md#opencustomdialog12)不局限于依赖UI页面，在使用时自定义UI样式，可直接调用。
