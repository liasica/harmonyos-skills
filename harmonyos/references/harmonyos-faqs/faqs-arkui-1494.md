---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1494
title: this.getUIContext().getPromptAction().openCustomDialog撑满全屏
breadcrumb: FAQ > 应用框架开发 > UI框架 > 窗口管理 > this.getUIContext().getPromptAction().openCustomDialog撑满全屏
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:13+08:00
doc_updated_at: 2026-08-13
content_hash: sha256:033720b4bd6a430873e18ddac49649428ce8a01d4fddc575d971a0a4f394cb84
---

## 问题现象

利用this.getUIContext().getPromptAction().openCustomDialog打开自定义弹窗，并且给dialog设置宽高100%依旧无法全屏。

问题效果预览：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5b/v3/etzr1ynER0i5wGbq-8D5QA/zh-cn_image_0000002658965035.png "点击放大")

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/70/v3/vUFVD6R9T0Cp-fukbcZ-uQ/zh-cn_image_0000002628605830.png "点击放大")

## 背景知识

* [沉浸式页面](../best-practices/bpta-multi-device-window-immersive.md)：沉浸式页面开发常通过将应用页面延伸到状态栏和导航栏，使用[setWindowLayoutFullScreen](../harmonyos-references/arkts-apis-window-window.md#setwindowlayoutfullscreen9)方法可以设置窗口为全屏模式。
* [@ohos.display (屏幕属性)](../harmonyos-references/js-apis-display.md)：屏幕属性提供管理显示设备的一些基础能力，包括获取默认显示设备的信息，display.getDefaultDisplaySync().height方法可以获取到设备的屏幕高度。

## 解决方案

1. 在EntryAbility中设置窗口全屏。

   ```screen
   import { ConfigurationConstant, UIAbility } from '@kit.AbilityKit';
   import { hilog } from '@kit.PerformanceAnalysisKit';
   import { window } from '@kit.ArkUI';
   import { BusinessError } from '@kit.BasicServicesKit';

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
       hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onWindowStageCreate');
       let windowClass: window.Window = windowStage.getMainWindowSync();
       // 1.设置窗口全屏
       let isLayoutFullScreen = true;
       windowClass.setWindowLayoutFullScreen(isLayoutFullScreen)
         .then(() => {
           console.info('Succeeded in setting the window layout to full-screen mode.');
         });
       // 2.设置状态栏和导航条隐藏
       windowClass.setSpecificSystemBarEnabled('status', false)
         .then(() => {
           console.info('Succeeded in setting the status bar to be invisible.');
         })
         .catch((err: BusinessError) => {
           console.error(`Failed to set the status bar to be invisible. Code is ${err.code}, message is ${err.message}`);
         });

       windowStage.loadContent('pages/Index', (err) => {
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
2. 把自定义弹窗的窗口高度设置为设备的屏幕高度displayHeight。

   ```screen
   import { display, PromptAction } from '@kit.ArkUI';

   @Entry
   @Component
   struct Index {
     private customDialogComponentId: number = 0;
     private promptAction: PromptAction = this.getUIContext().getPromptAction();
     @State displayHeight: number = 0;

     aboutToAppear() {
       this.displayHeight = this.getUIContext().px2vp(display.getDefaultDisplaySync().height);
     }

     @Builder
     customDialogComponent() {
       Column() {
         Text('弹窗').fontSize(30).margin({ top: 50});
         Row({ space: 50 }) {
           Button('取消')
             .backgroundColor(Color.Transparent)
             .fontColor('#0A59f7')
             .width('38%')
             .onClick(() => {
               this.promptAction.closeCustomDialog(this.customDialogComponentId);
             });
           Button('确认')
             .width('38%')
             .onClick(() => {
               this.promptAction.closeCustomDialog(this.customDialogComponentId);
             });
         };
       }.height(200).padding(5).justifyContent(FlexAlign.SpaceBetween);
     }

     build() {
       Row() {
         Column({ space: 20 }) {
           Text('组件内弹窗')
             .fontSize(30)
             .onClick(() => {
               this.promptAction.openCustomDialog({
                 builder: () => {
                   this.customDialogComponent();
                 },
                 width: '100%',
                 height: this.displayHeight,
               }).then((dialogId: number) => {
                 this.customDialogComponentId = dialogId;
               });
             });
         }
         .width('100%');
       }
       .height('100%');
     }
   }
   ```
