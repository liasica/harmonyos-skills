---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-783
title: 如何动态控制页面显示大小缩放跟随系统变化
breadcrumb: FAQ > 应用框架开发 > UI框架 > 窗口管理 > 如何动态控制页面显示大小缩放跟随系统变化
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:14+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:b24bd5ef005148b9bf3df952402546747b1d081458d8b02efb6684bbf44d814e
---

## 问题现象

如何动态控制页面显示大小缩放跟随系统变化，即在系统设置屏幕分辨率变化时，若页面已打开则不跟随系统变化；若页面未打开，则下次打开时跟随系统变化。

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e7/v3/r1cIGV-pSLmWJKmxYryJzQ/zh-cn_image_0000002628557634.gif "点击放大")

## 背景知识

* [WindowStage](../harmonyos-references/arkts-apis-window-windowstage.md)中提供的[setDefaultDensityEnabled方法](../harmonyos-references/arkts-apis-window-windowstage.md#setdefaultdensityenabled12)用于设置应用显示大小缩放是否跟随系统变化。不调用此接口进行设置，则表示不使用系统默认Density，即应用显示大小缩放将不会跟随系统的变化而自动调整。
* [AppStorage](../harmonyos-references/ts-state-management.md#appstorage)：是HarmonyOS应用全局状态管理的核心工具，通过装饰器实现与UI组件的灵活同步，适用于跨组件、跨UIAbility的共享状态场景。

## 解决方案

在EntryAbility中全局存储WindowStage对象，以便在整个应用中共享。在需要设置的页面中，通过页面的生命周期方法管理状态，并在页面显示时设置系统分辨率不跟随系统变化。具体实现如下：

1. 在EntryAbility里的onWindowStageCreate方法中使用AppStorage全局存储WindowStage对象，实现应用级全局状态共享。

   ```screen
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
2. 接着在需要设置的页面里通过onPageHide与onPageShow监听页面的显示与隐藏，从而将setDefaultDensityEnabled设置为true，使系统分辨率不跟随系统变化。

   ```screen
   import { window } from '@kit.ArkUI';

   @Entry
   @Component
   struct SetDefaultDensity {
     @State isShow: boolean = false;

     onPageShow(): void {
       if (this.isShow) {
         (AppStorage.get('windowStage') as window.WindowStage).setDefaultDensityEnabled(true);
       }
     }

     onPageHide(): void {
       this.isShow = true;
     }

     build() {
       Column() {
         Text(this.isShow ? '不跟随系统分辨率变化' : '跟随系统分辨率变化');
       }
       .height('100%')
       .width('100%');
     }
   }
   ```
