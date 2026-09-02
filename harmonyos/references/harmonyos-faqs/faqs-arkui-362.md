---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-362
title: 如何实现折叠屏折叠态不适配旋转，展示态适配旋转
breadcrumb: FAQ > 应用框架开发 > UI框架 > 窗口管理 > 如何实现折叠屏折叠态不适配旋转，展示态适配旋转
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:14+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:928ac6b2717f98e111aa63175fb81e6cd472d21b586f665b242b064d9ed14c7a
---

1. 在module.json5添加属性"orientation": "unspecified"。

   ```son
   // module.json5
   {
     "module": {
       "abilities": [
         {
           "name": "EntryAbility",
           "orientation":"unspecified"  // Unspecified orientation mode, determined by the system
         }
       ]
     }
   }
   ```
2. 在EntryAbility.ets的onWindowStageCreate方法中设置监听。如果设备处于完全展开状态，设置跟随系统方向，包括竖屏、横屏、反向竖屏和反向横屏。如果设备处于完全折叠状态，设置固定竖屏。

   ```ts
   import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
   import { hilog } from '@kit.PerformanceAnalysisKit';
   import { display, window } from '@kit.ArkUI';
   import { BusinessError } from '@kit.BasicServicesKit';

   export default class EntryAbility extends UIAbility {
     onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
       hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onCreate');
     }

     onDestroy(): void {
       hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onDestroy');
     }

     onWindowStageCreate(windowStage: window.WindowStage): void {
       // Main window is created, set main page for this ability
       hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onWindowStageCreate');

       windowStage.loadContent('pages/Index', (err) => {
         if (err.code) {
           hilog.error(0x0000, 'testTag', 'Failed to load the content. Cause: %{public}s', JSON.stringify(err) ?? '');
           return;
         }
         hilog.info(0x0000, 'testTag', 'Succeeded in loading the content.');
       });

       windowStage.getMainWindow().then((windowObj) => {
         // Set orientation based on fold status: auto-rotation when expanded, portrait when folded
         let orientation = display.getFoldStatus() === display.FoldStatus.FOLD_STATUS_EXPANDED ?
           window.Orientation.AUTO_ROTATION : window.Orientation.PORTRAIT;
         windowObj?.setPreferredOrientation(orientation);

         // Monitor the unfolded or folded state of the foldable screen
         display.on('foldStatusChange', (foldStatus: display.FoldStatus) => {
           orientation = foldStatus === display.FoldStatus.FOLD_STATUS_EXPANDED ? window.Orientation.AUTO_ROTATION :
             window.Orientation.PORTRAIT;
           try {
             windowObj?.setPreferredOrientation(orientation, (err: BusinessError) => {
               if (err.code) {
                 console.error(`Failed to set window orientation. Cause code: ${err.code}, message: ${err.message}`);
                 return;
               }
               console.info('Succeeded in setting window orientation.');
             });
           } catch (exception) {
             console.error(`Failed to set window orientation. Cause code: ${exception.code}, message: ${exception.message}`);
           }
         })
       });
     }

     onWindowStageDestroy(): void {
       // Main window is destroyed, release UI related resources
       hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onWindowStageDestroy');
     }

     onForeground(): void {
       // Ability has brought to foreground
       hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onForeground');
     }

     onBackground(): void {
       // Ability has back to background
       hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onBackground');
     }
   }
   ```
