---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1010
title: 如何实现窗口状态栏颜色根据页面背景色反转显示
breadcrumb: FAQ > 应用框架开发 > UI框架 > 窗口管理 > 如何实现窗口状态栏颜色根据页面背景色反转显示
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:14+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:fcb45037e33e3970ee78cb489f1212f0026ccc734f6c5be3c0edec0644a05854
---

## 问题现象

在HarmonyOS中，一个页面的上半部分为浅色背景色，下半部分为深色背景色，上下滚动页面时，状态栏的内容颜色不能自动反转。

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d1/v3/9z_Otgu0S4itrUIh5vzbVQ/zh-cn_image_0000002628404774.png "点击放大")

## 背景知识

* [onVisibleAreaChange](../harmonyos-references/ts-universal-component-visible-area-change-event.md#onvisibleareachange)是组件在屏幕中的显示区域面积变化时触发的事件，提供了判断组件是否完全或部分显示在屏幕中的能力，适用于广告曝光埋点之类的场景。
* [setWindowSystemBarProperties](../harmonyos-references/arkts-apis-window-window.md#setwindowsystembarproperties9)用于设置主窗口状态栏的属性，使用Promise异步回调。

## 解决方案

可监听组件onVisibleAreaChange事件，通过[setWindowSystemBarProperties](../harmonyos-references/arkts-apis-window-window.md#setwindowsystembarproperties9)主动设置窗口状态栏属性，达到状态栏显示颜色反转的效果。

1. 在EntryAbility.ets中的onWindowStageCreate方法内存储窗口实例，用于窗口属性设置。

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

       try {
         let windowClass = windowStage.getMainWindowSync();
         let isLayoutFullScreen = true;
         windowClass.setWindowLayoutFullScreen(isLayoutFullScreen);
         AppStorage.setOrCreate('windowClass', windowClass);
       } catch (exception) {
         console.error(`Failed to obtain the main window. Cause code: ${exception.code}, message: ${exception.message}`);
       }

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
2. 在CommonTopBar.ets页面通过监听可见区域变化，主动设置状态栏文字颜色反转。

   ```ts
   import { window } from '@kit.ArkUI';

   @Entry
   @Component
   struct CommonTopBar {
     private windowClass = AppStorage.get<window.Window>('windowClass') as window.Window;

     build() {
       Scroll() {
         Column() {
           Text('浅色页面部分')
             .fontSize(50)
             .height(500)
             .fontWeight(FontWeight.Bold)
             .onVisibleAreaChange([0.0, 0.1], (isExpanding: boolean) => {
               if (isExpanding) {
                 this.windowClass.setWindowSystemBarProperties({
                   statusBarContentColor: '#ff000000'
                 });
               }
               if (!isExpanding) {
                 this.windowClass.setWindowSystemBarProperties({
                   statusBarContentColor: '#fffafafa'
                 });
               }
             });
           Column() {
             Text('深色页面部分')
               .fontSize(50)
               .fontColor(Color.White)
               .height(500);
           }
           .height(1500)
           .width('100%')
           .backgroundColor(Color.Black);
         };
       }
       .height('100%')
       .width('100%');
     }
   }
   ```
