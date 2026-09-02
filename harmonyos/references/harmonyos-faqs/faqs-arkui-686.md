---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-686
title: 如何在HAR模块中实现创建子窗口的方法并加载HAR模块中的页面
breadcrumb: FAQ > 应用框架开发 > UI框架 > 窗口管理 > 如何在HAR模块中实现创建子窗口的方法并加载HAR模块中的页面
category: harmonyos-faqs
scraped_at: 2026-09-02T15:03:51+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:4cfb4fcff6333f00c9b53c4d83949354777a104f3679579cb5aa65871256d4e9
---

## 问题现象

如何在HAR模块A中写创建子窗口的方法，在HAP模块B中调用模块A创建子窗口，同时在B中传递参数给A中方法用于给子窗口中的页面展示信息？

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a3/v3/GBj1N_fqQcujz8r9AYoRig/zh-cn_image_0000002658794117.png "点击放大")

## 背景知识

* 通过[AppStorage](../harmonyos-guides/arkts-appstorage.md)可以存储EntryAbility中用于创建子窗口的windowStage，以便在应用的其他地方使用。
* 通过调用HAP模块中存储的windowStage的[createSubWindow](../harmonyos-references/arkts-apis-window-windowstage.md#createsubwindow9-1)方法创建子窗口。
* 创建子窗口后可以通过[loadContentByName](../harmonyos-references/arkts-apis-window-windowstage.md#loadcontentbyname11)将页面加载到子窗口中，并通过[LocalStorage](../harmonyos-guides/arkts-localstorage.md)为加载到窗口的页面内容传递状态属性。

## 解决方案

1. 首先在HAP模块的EntryAbility中存储windowStage至AppStorage，用于子窗口的创建。

   ```ts
   onWindowStageCreate(windowStage: window.WindowStage): void {
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
2. HAR中定义创建子窗口函数：本示例中，HAR模块名为hara，定义了一个用于创建子窗口的函数func。该函数接收两个参数，将参数值赋给LocalStorage类型的变量storage，用于向加载到窗口的页面内容传递状态属性。子窗口通过loadContentByName加载HAR模块的页面page1和接收storage传递的属性。（本示例中，该文件目录为：*项目名\hara\src\main\ets\func.ets*）

   ```ts
   import { display, UIContext, window } from '@kit.ArkUI';

   export function func(value: string, value2: string) {
     let uiContext: UIContext = new UIContext;
     let screenWidth: number = 0;
     let screenHeight: number = 0;
     let storage: LocalStorage = new LocalStorage();
     let newValue: string = value;
     let newValue2: string = value2;
     storage.setOrCreate('storageSimpleProp', newValue);
     storage.setOrCreate('storageSimpleProp2', newValue2);

     let windowStage = AppStorage.get('windowStage') as window.WindowStage;
     windowStage.createSubWindow('SubWindow', (err, windowClass) => {
       // 获取屏幕宽高以设置子窗口坐标
       let displayClass = display.getPrimaryDisplaySync();
       screenWidth = displayClass.width;
       screenHeight = displayClass.height;
       if (err.code > 0) {
         console.error(`failed to create subWindow Cause: ${err.message}`);
         return;
       }
       try {
         // 设置子窗口加载页
         windowClass.loadContentByName('page1', storage);
         // 设置子窗口左上角坐标
         windowClass.moveWindowTo((screenWidth - uiContext.vp2px(300)) / 2, (screenHeight - uiContext.vp2px(300)) / 2);
         // 设置子窗口大小
         windowClass.resize(uiContext.vp2px(300), uiContext.vp2px(300));
         // 设置子窗口圆角
         windowClass.setWindowCornerRadius(16);
         // 展示子窗口
         windowClass.showWindow();

       } catch (err) {
         console.error(`failed to create subWindow Cause:${err}`);
       }
     });
     return 'har func';
   }
   ```
3. 在HAR模块中，page1页面通过routeName定义了命名路由页面，并定义了两个LocalStorage共享变量，用于接收页面加载时传递的参数。（本示例中，该文件目录为：*项目名\hara\src\main\ets\components\MainPage.ets*）

   ```ts
   import { window } from '@kit.ArkUI';

   @Entry({ routeName: 'page1', useSharedStorage: true })
   @Component
   export struct Page1 {
     @LocalStorageLink('storageSimpleProp') storageSimpleProp: string = '';
     @LocalStorageLink('storageSimpleProp2') storageSimpleProp2: string = '';

     build() {
       Column() {
         Text('HAR页面')
           .width('100%')
           .padding({ top: 8, bottom: 8, left: 16 });
         Column({ space: 16 }) {
           Text(this.storageSimpleProp);
           Button('关闭子窗口')
             .onClick(() => {
               let windowClass: window.Window | undefined = undefined;
               try {
                 windowClass = window.findWindow('SubWindow');
                 windowClass.destroyWindow((err) => {
                   const errCode: number = err.code;
                   if (errCode) {
                     console.error(`Failed to destroy the window. Cause code: ${err.code}, message: ${err.message}`);
                     return;
                   }
                   console.info('Succeeded in destroying the window.');
                 });
               } catch (exception) {
                 console.error(`Failed to find the Window. Cause code: ${exception.code}, message: ${exception.message}`);
               }
             });
           Image($r(this.storageSimpleProp2))
             .width(100)
             .height(100);

         }
         .justifyContent(FlexAlign.Center)
         .borderRadius(16)
         .backgroundColor('#E5E5EA')
         .height('100%')
         .width('100%');
       }
       .backgroundColor('#F1F3F5')
       .height('100%')
       .width('100%');
     }
   }
   ```
4. 导出HAR模块的页面和方法。（本示例中，该文件目录为：*项目名\hara\Index.ets*）

   ```ts
   export { Page1 } from './src/main/ets/components/MainPage';
   export { func } from './src/main/ets/func';
   ```
5. 在HAP模块的oh-package.json5文件中通过dependencies字段来导入对HAR模块的依赖。

   ```json
   {
     "name": "entry",
     "version": "1.0.0",
     "description": "Please describe the basic information.",
     "main": "",
     "author": "",
     "license": "",
     "dependencies": {
       "hara": "file:../hara"
     }
   }
   ```
6. 在HAP模块的主窗口页面index中调用HAR模块中的func创建子窗口并传递参数用于子窗口页面的信息展示。

   ```ts
   import { func } from 'hara';
   import 'hara/src/main/ets/components/MainPage';

   @Entry
   @Component
   struct Index {
     build() {
       Column() {
         Text('Index页面')
           .fontSize(18);
         Blank()
           .height(16);
         Button('打开子窗口')
           .onClick(() => {
             // 调用HAR模块方法
             func('来自Index', 'app.media.startIcon');
           });
       }
       .justifyContent(FlexAlign.Center)
       .width('100%')
       .height('100%');
     }
   }
   ```

   **说明** 

   本文中使用的HAP模块指的是创建项目时的entry模块。
