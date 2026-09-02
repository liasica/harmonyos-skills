---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1022
title: 如何判断子窗口是否存在
breadcrumb: FAQ > 应用框架开发 > UI框架 > 窗口管理 > 如何判断子窗口是否存在
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:14+08:00
doc_updated_at: 2026-07-30
content_hash: sha256:90378ebc7f8b459471ff36d5aa834d2f589ca78397a9a09852c157866e252410
---

## 问题现象

通过子窗口实现悬浮窗，如何判断悬浮窗是否被关闭？

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/32/v3/8yvHZlT5QNGESOwUMJ9C7g/zh-cn_image_0000002628404810.png "点击放大")

## 背景知识

* [Interface(WindowStage)](../harmonyos-references/arkts-apis-window-windowstage.md)：窗口管理器，管理各个基本窗口单元。
* [findWindow](../harmonyos-references/arkts-apis-window-f.md#windowfindwindow9)：通过窗口名称查找对应的窗口。
* [destroyWindow](../harmonyos-references/arkts-apis-window-window.md#destroywindow9-1)：销毁当前窗口，使用Promise异步回调，支持系统窗口及应用子窗口，全局悬浮窗和模态窗。

## 解决方案

通过findWindow方法获取窗口对象，根据返回的结果判断查询的窗口是否存在。

1. 在EntryAbility.ets中保存WindowStage。

   ```ts
   import { UIAbility } from '@kit.AbilityKit';
   import { hilog } from '@kit.PerformanceAnalysisKit';
   import { window } from '@kit.ArkUI';

   const DOMAIN = 0x0000;

   export default class EntryAbility extends UIAbility {
     onWindowStageCreate(windowStage: window.WindowStage): void {
       // Main window is created, set main page for this ability
       hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onWindowStageCreate');

       windowStage.loadContent('pages/Index', (err) => {
         if (err.code) {
           hilog.error(DOMAIN, 'testTag', 'Failed to load the content. Cause: %{public}s', JSON.stringify(err));
           return;
         }
         AppStorage.setOrCreate('windowStage', windowStage);
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
2. 通过findWindow查询该子窗口是否存在。

   ```ts
   import { display, window } from '@kit.ArkUI';

   @Entry
   @Component
   struct Page1 {
     @State message: string = '子窗口状态：不存在';
     private windowStage: window.WindowStage = AppStorage.get('windowStage') as window.WindowStage;
     @State screenWidth: number = 0;
     @State screenHeight: number = 0;

     showSubWindow() {
       this.windowStage.createSubWindow('testSubWindow', (err, windowClass) => {
         if (err.code > 0) {
           return;
         }
         try {
           // 设置子窗口加载页
           windowClass.setUIContent('pages/Page2', () => {
             windowClass.setWindowBackgroundColor('#ffdddbda');
           });
           // 设置子窗口左上角坐标
           windowClass.moveWindowTo(this.screenWidth * 0.1, this.screenHeight / 2);
           // 设置子窗口大小
           windowClass.resize(this.screenWidth * 0.8, this.screenWidth * 0.8);
           // 展示子窗口
           windowClass.showWindow();
         } catch (err) {
         }
       });
     }

     aboutToAppear() {
       display.getAllDisplays((err, data) => {
         if (err.code !== 0) {
           return;
         }
         this.screenWidth = data[0].width;
         this.screenHeight = data[0].height;
       });
     }

     build() {
       Column() {
         Row({ space: 20 }) {
           Button('打开子窗口')
             .backgroundColor('#0a59f7')
             .onClick(() => {
               this.showSubWindow();
             });
           Button('关闭子窗口')
             .backgroundColor('#0a59f7')
             .onClick(() => {
               try {
                 window.findWindow('testSubWindow').destroyWindow();
               } catch (exception) {
                 console.info('窗口不存在', exception);
               }
             });
         }
         .margin({ top: 50 })
         .width('100%');

         Row() {
           Button('查询子窗口是否存在')
             .backgroundColor('#0a59f7')
             .onClick(() => {
               try {
                 window.findWindow('testSubWindow');
                 this.message = '子窗口状态：存在';
               } catch (exception) {
                 this.message = '子窗口状态：不存在';
               }
             });
           Text(this.message)
             .margin({ left: 20 });
         }
         .margin({ top: 20 })
         .width('100%');
       }
       .width('100%')
       .padding({ left: 30 });
     }
   }
   ```
3. 创建子窗口页面。

   ```ts
   @Entry
   @Component
   struct Page2 {

     build() {
       RelativeContainer() {
         Text('子窗口')
           .fontSize(20)
           .fontWeight(FontWeight.Bold)
           .alignRules({
             center: { anchor: '__container__', align: VerticalAlign.Center },
             middle: { anchor: '__container__', align: HorizontalAlign.Center }
           })

       }
       .height('100%')
       .width('100%');
     }
   }
   ```

## 常见FAQ

Q：子窗口调用[minimize](../harmonyos-references/arkts-apis-window-window.md#minimize11)后如何恢复？

A：通过findWindow获取到[Window实例](../harmonyos-references/arkts-apis-window-window.md)，再通过此实例调用[showWindow](../harmonyos-references/arkts-apis-window-window.md#showwindow9)恢复子窗口。

Q：如何根据窗口实例获取到对应的[UIContext](../harmonyos-references/arkts-apis-uicontext-uicontext.md)，或如何关闭已知窗口？

A：用window.findWindow('windowName').getUIContext()获取到UIContext，或者window.findWindow('windowName').destroyWindow销毁窗口。

Q：如何判断子窗口是否创建成功？

A：可通过[getSubWindow](../harmonyos-references/arkts-apis-window-windowstage.md#getsubwindow9-1)获取当前WindowStage实例下的所有子窗口来判断。

Q：子窗口白屏可能的原因是什么？

A：请按如下进行排查：

* 子窗口内容未正确设置：在创建子窗口后，需要通过[setUIContent](../harmonyos-references/arkts-apis-window-window.md#setuicontent9-1)和showWindow接口来加载和显示子窗口的具体内容。如果这些接口没有被正确调用，或者调用的参数错误，可能会导致子窗口无法显示内容。
* 资源或路径配置错误：请确保所有资源和路径配置正确无误。特别是，如果子窗口试图加载的资源或路径不存在，将无法显示内容，从而导致白屏。
* 检查一下，是否存在未初始化的属性或方法。

Q：如何为子窗口设置三键导航？

A：可以使用[createSubWindowWithOptions](../harmonyos-references/arkts-apis-window-window.md#createsubwindowwithoptions12)并配置参数decorEnabled为true。

Q：三折叠上如何去除子窗口的阴影？

A：使用[setWindowShadowRadius](../harmonyos-references/arkts-apis-window-window.md#setwindowshadowradius17)将值设置为0.0关闭窗口边缘阴影。
