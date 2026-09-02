---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1573
title: 子窗口控制主窗口的页面跳转
breadcrumb: FAQ > 应用框架开发 > UI框架 > 窗口管理 > 子窗口控制主窗口的页面跳转
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:13+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:d9e38d1b60c6cf6a091baae9329b1b43d7f104a92c8cae6c828826d6d1b23ed6
---

## 问题现象

页面中有子窗口的场景下，需要通过Router操作主窗口页面，但是调用pushUrl、replaceUrl等方法后，操作的是子窗口的页面，怎么才能获取到主窗口的Router对象操作主窗口的页面？

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/91/v3/94Mn0xSESM-k1O0_lE6lZA/zh-cn_image_0000002658969081.png "点击放大")

## 背景知识

* [Router](../harmonyos-references/arkts-apis-uicontext-router.md)提供通过不同的url访问不同的页面，包括跳转到应用内的指定页面、同应用内的某个页面替换当前页面、返回上一页面或指定的页面等。
* [createSubWindow](../harmonyos-references/arkts-apis-window-windowstage.md#createsubwindow9)：可以创建当前WindowStage实例下的子窗口。

## 解决方案

子窗口和主窗口是两个独立的路由栈，子窗口中使用[pushUrl](../harmonyos-references/arkts-apis-uicontext-router.md#pushurl)、[back](../harmonyos-references/arkts-apis-uicontext-router.md#back12)等方法只能控制子窗口页面的跳转和返回。

若需要在子窗口控制主窗口页面跳转，需要在子窗口中获取到主窗口的路由栈。

1. 在EntryAbility中的onWindowStageCreate方法中使用AppStorage保存WindowStage实例。

   ```ts
   import { ConfigurationConstant, UIAbility } from '@kit.AbilityKit';
   import { hilog } from '@kit.PerformanceAnalysisKit';
   import { window } from '@kit.ArkUI';

   const DOMAIN = 0x0000;

   export default class EntryAbility extends UIAbility {
     onCreate(): void {
       try {
         this.context.getApplicationContext().setColorMode(ConfigurationConstant.ColorMode.COLOR_MODE_NOT_SET);
       } catch (err) {
         hilog.error(DOMAIN, 'testTag', 'Failed to set colorMode. Cause: %{public}s', JSON.stringify(err));
       }
       hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onCreate');
     }

     onDestroy(): void {
       hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onDestroy');
     }

     onWindowStageCreate(windowStage: window.WindowStage): void {
       // Main window is created, set main page for this ability
       hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onWindowStageCreate');
       // 第一步：通过AppStorage保存WindowStage实例
       AppStorage.setOrCreate('windowStage', windowStage);
       windowStage.loadContent('pages/SubWindowDemo', (err) => {
         if (err.code) {
           hilog.error(DOMAIN, 'testTag', 'Failed to load the content. Cause: %{public}s', JSON.stringify(err));
           return;
         }
         hilog.info(DOMAIN, 'testTag', 'Succeeded in loading the content.');
       });
     }

     onWindowStageDestroy(): void {
       // Main window is destroyed, release UI related resources
       hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onWindowStageDestroy');
     }

     onForeground(): void {
       // Ability has brought to foreground
       hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onForeground');
     }

     onBackground(): void {
       // Ability has back to background
       hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onBackground');
     }
   };
   ```

2. 创建子窗口需要加载的页面SubWindowPage.ets，在该页面中获取WindowStage实例下的主窗口对象，通过[getUIContext()](../harmonyos-references/ts-custom-component-api.md#getuicontext)获取UIContext实例，再通过[getRouter()](../harmonyos-references/arkts-apis-uicontext-uicontext.md#getrouter)获取Router对象。

   ```ts
   import { router, window } from '@kit.ArkUI';

   @Entry
   @Component
   struct SubWindowPage {

     onBackPress(): boolean | void {
       // 侧滑返回首页
       let uiContext: UIContext | null = null;
       let windowStage = AppStorage.get('windowStage') as window.WindowStage;
       // 通过getMainWindowSync获取WindowStage实例下的主窗口
       let windowClass: window.Window = windowStage.getMainWindowSync();
       uiContext = windowClass.getUIContext();
       // 获取Router对象
       uiContext.getRouter().pushUrl({
         url: 'pages/SubWindowDemo',
       }, router.RouterMode.Single);
     }

     build() {
       Column({ space: 10 }) {
         Text('子窗口 SubWindow');
         Button('主窗口页面跳转')
           .onClick(() => {
             try {
               console.info('主窗口页面跳转');
               let uiContext: UIContext | null = null;
               let windowStage = AppStorage.get('windowStage') as window.WindowStage;
               // 通过getMainWindowSync获取WindowStage实例下的主窗口
               let windowClass: window.Window = windowStage.getMainWindowSync();
               uiContext = windowClass.getUIContext();
               // 获取Router对象
               uiContext.getRouter().pushUrl({
                 url: 'pages/Page', // 需要自行创建一个Page页面
               }, router.RouterMode.Single);
             } catch (exception) {
               console.error(`Failed to create the subwindow. Cause code: ${exception.code}, message: ${exception.message}`);
             };
           });
       }
       .borderRadius('16vp')
       .backgroundColor('#F1F3F5')
       .justifyContent(FlexAlign.Center)
       .height('100%')
       .width('100%')
     }
   }
   ```
3. 在SubWindowDemo.ets文件中，创建子窗口，并通过[loadContent](../harmonyos-references/arkts-apis-window-window.md#loadcontent9)方法加载步骤2创建的SubWindowPage页面。

   ```ts
   import { display, window } from '@kit.ArkUI';
   import { BusinessError } from '@kit.BasicServicesKit';

   @Entry
   @Component
   struct SubWindowDemo {
     build() {
       Column() {
         Button('创建子窗口')
           .onClick(() => {
             let windowStage = AppStorage.get('windowStage') as window.WindowStage;
             try {
               windowStage.createSubWindow('mySubWindow').then((windowClass: window.Window) => {
                 windowClass.loadContent('pages/SubWindowPage', null);
                 const screenWidth = display.getDefaultDisplaySync().width;
                 // 子窗口居中
                 windowClass.moveWindowTo(screenWidth / 2 - this.getUIContext().vp2px(200) / 2, 400);
                 // 设置子窗口大小
                 windowClass.resize(this.getUIContext().vp2px(200), this.getUIContext().vp2px(200));
                 // 展示子窗口
                 windowClass.showWindow();
                 console.info(`Succeeded in creating the subwindow. Data: ${JSON.stringify(windowClass)}`);
               }).catch((err: BusinessError) => {
                 console.error(`Failed to create the subwindow. Cause code: ${err.code}, message: ${err.message}`);
               });
             } catch (exception) {
               console.error(`Failed to create the subwindow. Cause code: ${exception.code}, message: ${exception.message}`);
             }
           })
       }
       .justifyContent(FlexAlign.Center)
       .height('100%')
       .width('100%')
     }
   }
   ```
