---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1575
title: 如何实现规定时间范围内，应用任何页面都可显示的计时弹窗
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 如何实现规定时间范围内，应用任何页面都可显示的计时弹窗
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:18+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:801f967b6c453185a7737186cbf2d986b10029b47850f2427866b49a516d1b6e
---

## 问题现象

如何设置一个计时器，在规定的时间范围内，弹出一个弹窗？且无论在当前处于哪个页面。

## 效果预览

以09点23分为例：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/82/v3/Y_lo67WSTC6LOWXa07_Mvg/zh-cn_image_0000002628769768.png "点击放大")

## 背景知识

[@ohos.promptAction（弹窗）](../harmonyos-references/js-apis-promptaction.md)：是一种创建并显示文本提示框、对话框和操作菜单的API，在API10以后可以通过使用UIContext中的[getPromptAction](../harmonyos-references/arkts-apis-uicontext-uicontext.md#getpromptaction)方法获取当前UI上下文关联的[PromptAction](../harmonyos-references/arkts-apis-uicontext-promptaction.md)对象。该方式在不设置[页面级弹窗](../harmonyos-guides/arkts-embedded-dialog.md)属性的前提下，弹窗总是显示在所有page页面的最上面。

## 解决方案

由于默认情况下弹窗的显示层级高于所有的page页面，所以只需要在弹窗内部实现一个计时器，并在进入应用时执行，满足条件时自动弹出即可。

以Toast弹窗为例：

1. 创建全局GlobalTimer类。

   ```ts
   import { window } from '@kit.ArkUI';

   export class GlobalTimer {
     static timeID: number;

     static checkTime() {
       let now = new Date();
       let hour = now.getHours();
       let minutes = now.getMinutes();

       // 如果当前时间是9点，且分钟是23分
       if (hour === 9 && minutes === 23) {
         // 这里放置想要定时执行的代码
         let mainWindow: ESObject = (AppStorage.get('windowStage') as window.WindowStage).getMainWindowSync();
         mainWindow.getUIContext().getPromptAction().showToast({
           message: '定时任务触发!!!!', // 显示内容。
           duration: 10000 // 提醒弹窗显示10秒钟。
         });
       }
     }

     // 每分钟检查一次时间
     public static toast() {
       GlobalTimer.timeID = setInterval(GlobalTimer.checkTime, 60000);
     }

     clearTime() {
       clearInterval(GlobalTimer.timeID);
     }
   }
   ```
2. 在EntryAbility入口onWindowStageCreate回调中执行计时器方法。

   ```ts
   import {UIAbility} from '@kit.AbilityKit';
   import { hilog } from '@kit.PerformanceAnalysisKit';
   import { window } from '@kit.ArkUI';
   import { GlobalTimer } from '../pages/GlobalTimer';

   const DOMAIN = 0x0000;

   export default class EntryAbility extends UIAbility {
     onDestroy(): void {
       hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onDestroy');
     }

     onWindowStageCreate(windowStage: window.WindowStage): void {
       // Main window is created, set main page for this ability
       hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onWindowStageCreate');
       windowStage.loadContent('pages/Index', (err) => {
         AppStorage.setOrCreate('windowStage', windowStage);
         GlobalTimer.toast();
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

   该处封装的Toast弹窗，其它更多样式布局弹窗详见[不依赖UI组件的全局自定义弹出框（openCustomDialog）](../harmonyos-guides/arkts-uicontext-custom-dialog.md)。
3. 创建主页面。

   ```ts
   @Entry
   @Component
   struct Index59 {
     message: string = '主页';

     build() {
       RelativeContainer() {
         Text(this.message)
           .id('Index59HelloWorld')
           .fontSize(35)
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
