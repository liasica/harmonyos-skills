---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-computer-15
title: 如何实现PC登录流程的窗口变化效果
breadcrumb: FAQ > 多设备场景 > 电脑 > 常见问题 > 如何实现PC登录流程的窗口变化效果
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:49+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:8561c06ad502ea2ba09b4a439d9702513d03d8870c8cb96a81cebd72e98ee245
---

## 问题现象

如何实现PC登录流程的窗口变化效果？期待的效果是：启动应用时，先出现一个用于登录的小窗，窗口没有标题栏，登录后变为全屏具有标题栏的主界面。

## 背景知识

* module.json5配置文件中[abilities标签](../harmonyos-guides/module-configuration-file.md#abilities标签)中的startWindowIcon和startWindowBackground分别设置应用启动页的图标和背景颜色。
* [resize](../harmonyos-references/arkts-apis-window-window.md#resize9-1)用于调整窗口大小。
* [moveWindowTo](../harmonyos-references/arkts-apis-window-window.md#movewindowto9-1)用于移动窗口位置。
* [setWindowDecorVisible](../harmonyos-references/arkts-apis-window-window.md#setwindowdecorvisible11)用于设置标题栏是否可见。该接口需要在loadContent()调用生效后使用。
* [setWindowTitleButtonVisible](../harmonyos-references/arkts-apis-window-window.md#setwindowtitlebuttonvisible14)用于设置主窗口标题栏上的最大化、最小化、关闭按钮是否可见。

## 解决方案

1. 将module.json5配置文件中abilities标签的startWindowIcon设置为透明图片，startWindowBackground设置为透明背景。这一步可以隐藏应用启动时系统自带的启动页，直接显示用于登录的小窗。
2. 在EntryAbility.ets文件中的onWindowStageCreate方法中通过resize将窗口尺寸设为小尺寸，并通过moveWindowTo实现居中放置；loadContent执行后通过setWindowDecorVisible和setWindowTitleButtonVisible将标题栏设为隐藏状态。这一步可以初始化窗口形态，用于实现登录用的小窗。

   ```ts
   import { AbilityConstant, ConfigurationConstant, UIAbility, Want } from '@kit.AbilityKit';
   import { hilog } from '@kit.PerformanceAnalysisKit';
   import { display, window } from '@kit.ArkUI';

   const DOMAIN = 0x0000;

   export default class EntryAbility extends UIAbility {
     onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
       console.info(`want: ${want}`);
       console.info(`launchParam: ${launchParam}`);
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
       AppStorage.setOrCreate('windowStage', windowStage);
       const windowClass = windowStage.getMainWindowSync();
       windowClass.resize(500, 500);
       windowClass.moveWindowTo(display.getDefaultDisplaySync().width / 2 - 250,
         display.getDefaultDisplaySync().height / 2 - 250, (err) => {
           console.info(`want: ${err}`);
         });
       // Main window is created, set main page for this ability
       hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onWindowStageCreate');

       windowStage.loadContent('pages/Index', (err) => {
         windowClass.setWindowDecorVisible(false);
         windowClass.setWindowTitleButtonVisible(false, false, false);
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
3. 登录后恢复标题栏并将窗口设为全屏。这一步用于实现主界面的全屏窗口。

   ```ts
   import { window } from '@kit.ArkUI';

   @Entry
   @Component
   struct Index {
     context: Context | undefined = this.getUIContext().getHostContext();

     build() {
       RelativeContainer() {
         Text('登录')
           .id('HelloWorld')
           .fontSize($r('app.float.page_text_font_size'))
           .fontWeight(FontWeight.Bold)
           .alignRules({
             center: { anchor: '__container__', align: VerticalAlign.Center },
             middle: { anchor: '__container__', align: HorizontalAlign.Center }
           })
           .onClick(() => {
             let windowStage = AppStorage.get('windowStage') as window.WindowStage;
             let windowClass: window.Window = windowStage.getMainWindowSync(); // 获取应用主窗口
             windowClass.setWindowDecorVisible(true);
             windowClass.setWindowTitleButtonVisible(true, true, true);
             windowClass.maximize(window.MaximizePresentation.FOLLOW_APP_IMMERSIVE_SETTING);
             this.getUIContext().getRouter().pushUrl({ url: 'pages/MainPage', });
           });
       }
       .height('100%')
       .width('100%');
     }
   }
   ```
4. 登录后显示主页面。

   ```ts
   @Entry
   @Component
   struct MainPage {
     message: string = '主界面';

     build() {
       RelativeContainer() {
         Text(this.message)
           .id('HelloWorld')
           .fontSize($r('app.float.page_text_font_size'))
           .fontWeight(FontWeight.Bold)
           .alignRules({
             center: { anchor: '__container__', align: VerticalAlign.Center },
             middle: { anchor: '__container__', align: HorizontalAlign.Center }
           });
       }
       .height('100%')
       .width('100%');
     }
   }
   ```
