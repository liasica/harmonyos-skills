---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/free-flow-faqs-2
title: 不同APPID的应用如何实现应用接续
breadcrumb: FAQ > 多设备场景 > 自由流转 > 不同APPID的应用如何实现应用接续
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:49+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:eb5eaf0b68aaad5dc798f5042d7d13e77ff3abdea02693de9255667e5163b6ef
---

## 问题现象

HarmonyOS虽然能通过一多适配将一个功能发布到不同类型的设备上，由于不同设备（如手机、PC）的发布节奏和开发节奏不同，若将手机、PC拆分为2个不同的APPID，这种情况下，如何实现不同APPID的应用间应用接续功能呢？

## 背景知识

* [应用接续](../best-practices/bpta-continue-cast.md)：指当用户在一个设备上操作某个应用时，可以在另一个设备的同一个应用中快速切换，并无缝衔接上一个设备的应用体验。
* 应用接续[支持同应用不同BundleName的Ability跨端迁移](../best-practices/bpta-continue-cast.md#section1610864011610)。

## 解决方案

参考[支持同应用不同BundleName的Ability跨端迁移](../best-practices/bpta-continue-cast.md#section1610864011610)，不同APPID的应用需在module.json5配置文件中的abilities标签增加配置continueBundleName字段，指定当前ability需要接续的对端BundleName。

1. 应用A（BundleName：com.hw.mycontinuea），入口ability为EntryAbility：
   * 在module.json5的abilities标签中增加如下配置：

     ```json
     "continuable": true,
     "continueBundleName": [
       "com.hw.mycontinueb"
     ],
     "continueType": [
       "mainAbility"
     ],
     ```
   * 在EntryAbility中补充onContinue事件：

     ```ts
     onContinue(wantParam: Record<string, Object>) {
       hilog.info(DOMAIN, 'testTag', '%{public}s', 'EntryAbility onContinue');
       const targetVersion = wantParam.version; // 获取迁移对端应用的版本号
       // 应用可根据源端版本号设置支持接续的最小兼容版本号，源端版本号可从app.json5文件中的versionCode字段获取；防止目标端版本号过低导致不兼容。
       const versionThreshold: number = 0; // 替换为应用自己支持兼容的最小版本号
       // 兼容性校验
       if (targetVersion < versionThreshold) {
         // 建议在校验版本兼容性失败后，提示用户拒绝迁移的原因
         promptAction.openToast({
           message: '目标端应用版本号过低，不支持接续，请您升级应用版本后再试',
           duration: 2000
         });
         // 在兼容性校验不通过时返回MISMATCH
         return AbilityConstant.OnContinueResult.MISMATCH;
       }
       console.info(`onContinue version = ${wantParam.version}, targetDevice: ${wantParam.targetDevice}`);
       // 迁移数据保存
       const continueInput = '迁移的数据';
       if (continueInput) {
         // 将要迁移的数据保存在wantParam的自定义字段（如：data）中;
         wantParam['data'] = continueInput;
       }
       // ...
       return AbilityConstant.OnContinueResult.AGREE;
     }
     ```
   * 在EntryAbility中补充onCreate和onNewWant事件：

     ```ts
     onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
       try {
         this.context.getApplicationContext().setColorMode(ConfigurationConstant.ColorMode.COLOR_MODE_NOT_SET);
         // 设置是否开启应用接续，可在各页面动态设置
         this.context.setMissionContinueState(AbilityConstant.ContinueState.ACTIVE, (result) => {
           hilog.info(DOMAIN, 'testTag', `setMissionContinueState: ${JSON.stringify(result)}`);
         });
         // 判断是否为应用接续场景
         if (launchParam.launchReason === AbilityConstant.LaunchReason.CONTINUATION) {
           // 将上述的保存的数据取出恢复
           if (want.parameters !== undefined) {
             let continueInput = want.parameters.data as string;
             AppStorage.setOrCreate<string>('message', continueInput);
             console.info(`continue input ${continueInput}`);
           }
           // ...
           // 触发页面恢复
           this.context.restoreWindowStage(this.storage);
         }
         // ...
       } catch (err) {
         hilog.error(DOMAIN, 'testTag', 'Failed to set colorMode. Cause: %{public}s', JSON.stringify(err));
       }
       hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onCreate');
     }

     onNewWant(want: Want, launchParam: AbilityConstant.LaunchParam): void {
       hilog.info(DOMAIN, 'testTag', '%{public}s', `EntryAbility onNewWant ${AbilityConstant.LaunchReason.CONTINUATION}`);
       if (launchParam.launchReason === AbilityConstant.LaunchReason.CONTINUATION) {
         // 将上述的保存的数据取出恢复
         if (want.parameters !== undefined) {
           let continueInput = want.parameters.data as string;
           AppStorage.setOrCreate<string>('message', continueInput);
           console.info(`continue input ${continueInput}`);
         }
         // ...
         // 触发页面恢复
         this.context.restoreWindowStage(this.storage);
       }
       // ...
     }
     ```

   应用A的EntryAbility完整代码如下：

   ```ts
   import { AbilityConstant, ConfigurationConstant, UIAbility, Want } from '@kit.AbilityKit';
   import { hilog } from '@kit.PerformanceAnalysisKit';
   import { promptAction, window } from '@kit.ArkUI';

   const DOMAIN = 0x0000;

   export default class EntryAbility extends UIAbility {
     storage: LocalStorage = new LocalStorage();

     onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
       try {
         this.context.getApplicationContext().setColorMode(ConfigurationConstant.ColorMode.COLOR_MODE_NOT_SET);
         // 设置是否开启应用接续，可在各页面动态设置
         this.context.setMissionContinueState(AbilityConstant.ContinueState.ACTIVE, (result) => {
           hilog.info(DOMAIN, 'testTag', `setMissionContinueState: ${JSON.stringify(result)}`);
         });
         // 判断是否为应用接续场景
         if (launchParam.launchReason === AbilityConstant.LaunchReason.CONTINUATION) {
           // 将上述的保存的数据取出恢复
           if (want.parameters !== undefined) {
             let continueInput = want.parameters.data as string;
             AppStorage.setOrCreate<string>('message', continueInput);
             console.info(`continue input ${continueInput}`);
           }
           // ...
           // 触发页面恢复
           this.context.restoreWindowStage(this.storage);
         }
         // ...
       } catch (err) {
         hilog.error(DOMAIN, 'testTag', 'Failed to set colorMode. Cause: %{public}s', JSON.stringify(err));
       }
       hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onCreate');
     }

     onNewWant(want: Want, launchParam: AbilityConstant.LaunchParam): void {
       hilog.info(DOMAIN, 'testTag', '%{public}s', `EntryAbility onNewWant ${AbilityConstant.LaunchReason.CONTINUATION}`);
       if (launchParam.launchReason === AbilityConstant.LaunchReason.CONTINUATION) {
         // 将上述的保存的数据取出恢复
         if (want.parameters !== undefined) {
           let continueInput = want.parameters.data as string;
           AppStorage.setOrCreate<string>('message', continueInput);
           console.info(`continue input ${continueInput}`);
         }
         // ...
         // 触发页面恢复
         this.context.restoreWindowStage(this.storage);
       }
       // ...
     }

     onContinue(wantParam: Record<string, Object>) {
       hilog.info(DOMAIN, 'testTag', '%{public}s', 'EntryAbility onContinue');
       const targetVersion = wantParam.version; // 获取迁移对端应用的版本号
       // 应用可根据源端版本号设置支持接续的最小兼容版本号，源端版本号可从app.json5文件中的versionCode字段获取；防止目标端版本号过低导致不兼容。
       const versionThreshold: number = 0; // 替换为应用自己支持兼容的最小版本号
       // 兼容性校验
       if (targetVersion < versionThreshold) {
         // 建议在校验版本兼容性失败后，提示用户拒绝迁移的原因
         promptAction.openToast({
           message: '目标端应用版本号过低，不支持接续，请您升级应用版本后再试',
           duration: 2000
         });
         // 在兼容性校验不通过时返回MISMATCH
         return AbilityConstant.OnContinueResult.MISMATCH;
       }
       console.info(`onContinue version = ${wantParam.version}, targetDevice: ${wantParam.targetDevice}`);
       // 迁移数据保存
       const continueInput = '迁移的数据';
       if (continueInput) {
         // 将要迁移的数据保存在wantParam的自定义字段（如：data）中;
         wantParam['data'] = continueInput;
       }
       // ...
       return AbilityConstant.OnContinueResult.AGREE;
     }

     onDestroy(): void {
       hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onDestroy');
     }

     onWindowStageCreate(windowStage: window.WindowStage): void {
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

   应用A的module.json5完整代码如下：

   ```json
   {
     "module": {
       "name": "entry",
       "type": "entry",
       "description": "$string:module_desc",
       "mainElement": "EntryAbility",
       "deviceTypes": [
         "phone",
         "tablet",
         "2in1"
       ],
       "deliveryWithInstall": true,
       "installationFree": false,
       "pages": "$profile:main_pages",
       "abilities": [
         {
           "name": "EntryAbility",
           "srcEntry": "./ets/entryability/EntryAbility.ets",
           "description": "$string:EntryAbility_desc",
           "icon": "$media:layered_image",
           "label": "$string:EntryAbility_label",
           "startWindowIcon": "$media:startIcon",
           "startWindowBackground": "$color:start_window_background",
           "exported": true,
           "continuable": true,
           "continueBundleName": [
             "com.hw.mycontinueb"
           ],
           "continueType": [
             "mainAbility"
           ],
           "skills": [
             {
               "entities": [
                 "entity.system.home"
               ],
               "actions": [
                 "ohos.want.action.home"
               ]
             }
           ]
         }
       ],
       "extensionAbilities": [
         {
           "name": "EntryBackupAbility",
           "srcEntry": "./ets/entrybackupability/EntryBackupAbility.ets",
           "type": "backup",
           "exported": false,
           "metadata": [
             {
               "name": "ohos.extension.backup",
               "resource": "$profile:backup_config"
             }
           ],
         }
       ]
     }
   }
   ```
2. 应用B（BundleName：com.hw.mycontinueb），入口ability为ProductAbility：
   * 在module.json5的abilities标签中增加如下配置：

     ```json
     "continuable": true,
     "continueBundleName": [
       "com.hw.mycontinuea"
     ],
     "continueType": [
       "mainAbility"
     ],
     ```
   * 在EntryAbility中补充onContinue事件：

     ```ts
     onContinue(wantParam: Record<string, Object>) {
       hilog.info(DOMAIN, 'testTag', '%{public}s', 'EntryAbility onContinue');
       const targetVersion = wantParam.version; // 获取迁移对端应用的版本号
       // 应用可根据源端版本号设置支持接续的最小兼容版本号，源端版本号可从app.json5文件中的versionCode字段获取；防止目标端版本号过低导致不兼容。
       const versionThreshold: number = 0; // 替换为应用自己支持兼容的最小版本号
       // 兼容性校验
       if (targetVersion < versionThreshold) {
         // 建议在校验版本兼容性失败后，提示用户拒绝迁移的原因
         promptAction.openToast({
           message: '目标端应用版本号过低，不支持接续，请您升级应用版本后再试',
           duration: 2000
         });
         // 在兼容性校验不通过时返回MISMATCH
         return AbilityConstant.OnContinueResult.MISMATCH;
       }
       console.info(`onContinue version = ${wantParam.version}, targetDevice: ${wantParam.targetDevice}`);
       // 迁移数据保存
       const continueInput = '迁移的数据';
       if (continueInput) {
         // 将要迁移的数据保存在wantParam的自定义字段（如：data）中;
         wantParam['data'] = continueInput;
       }
       // ...
       return AbilityConstant.OnContinueResult.AGREE;
     }
     ```
   * 在EntryAbility中补充onCreate和onNewWant事件：

     ```ts
     onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
       try {
         this.context.getApplicationContext().setColorMode(ConfigurationConstant.ColorMode.COLOR_MODE_NOT_SET);
         // 设置是否开启应用接续，可在各页面动态设置
         this.context.setMissionContinueState(AbilityConstant.ContinueState.ACTIVE, (result) => {
           hilog.info(DOMAIN, 'testTag', `setMissionContinueState: ${JSON.stringify(result)}`);
         });
         // 判断是否为应用接续场景
         if (launchParam.launchReason === AbilityConstant.LaunchReason.CONTINUATION) {
           // 将上述的保存的数据取出恢复
           if (want.parameters !== undefined) {
             let continueInput = want.parameters.data as string;
             AppStorage.setOrCreate<string>('message', continueInput);
             console.info(`continue input ${continueInput}`);
           }
           // ...
           // 触发页面恢复
           this.context.restoreWindowStage(this.storage);
         }
         // ...
       } catch (err) {
         hilog.error(DOMAIN, 'testTag', 'Failed to set colorMode. Cause: %{public}s', JSON.stringify(err));
       }
       hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onCreate');
     }

     onNewWant(want: Want, launchParam: AbilityConstant.LaunchParam): void {
       hilog.info(DOMAIN, 'testTag', '%{public}s', `EntryAbility onNewWant ${AbilityConstant.LaunchReason.CONTINUATION}`);
       if (launchParam.launchReason === AbilityConstant.LaunchReason.CONTINUATION) {
         // 将上述的保存的数据取出恢复
         if (want.parameters !== undefined) {
           let continueInput = want.parameters.data as string;
           AppStorage.setOrCreate<string>('message', continueInput);
           console.info(`continue input ${continueInput}`);
         }
         // ...
         // 触发页面恢复
         this.context.restoreWindowStage(this.storage);
       }
       // ...
     }
     ```

   在EntryAbility中补充onCreate和onNewWant事件：

   ```ts
   import { AbilityConstant, ConfigurationConstant, UIAbility, Want } from '@kit.AbilityKit';
   import { hilog } from '@kit.PerformanceAnalysisKit';
   import { promptAction, window } from '@kit.ArkUI';

   const DOMAIN = 0x0000;

   export default class ProductAbility extends UIAbility {
     storage: LocalStorage = new LocalStorage();

     onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
       try {
         this.context.getApplicationContext().setColorMode(ConfigurationConstant.ColorMode.COLOR_MODE_NOT_SET);
         // 设置是否开启应用接续，可在各页面动态设置
         this.context.setMissionContinueState(AbilityConstant.ContinueState.ACTIVE, (result) => {
           hilog.info(DOMAIN, 'testTag', `setMissionContinueState: ${JSON.stringify(result)}`);
         });
         // 判断是否为应用接续场景
         if (launchParam.launchReason === AbilityConstant.LaunchReason.CONTINUATION) {
           // 将上述的保存的数据取出恢复
           if (want.parameters !== undefined) {
             let continueInput = want.parameters.data as string;
             AppStorage.setOrCreate<string>('message', continueInput);
             console.info(`continue input ${continueInput}`);
           }
           // ...
           // 触发页面恢复
           this.context.restoreWindowStage(this.storage);
         }
         // ...
       } catch (err) {
         hilog.error(DOMAIN, 'testTag', 'Failed to set colorMode. Cause: %{public}s', JSON.stringify(err));
       }
       hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onCreate');
     }

     onNewWant(want: Want, launchParam: AbilityConstant.LaunchParam): void {
       hilog.info(DOMAIN, 'testTag', '%{public}s', `EntryAbility onNewWant ${AbilityConstant.LaunchReason.CONTINUATION}`);
       if (launchParam.launchReason === AbilityConstant.LaunchReason.CONTINUATION) {
         // 将上述的保存的数据取出恢复
         if (want.parameters !== undefined) {
           let continueInput = want.parameters.data as string;
           AppStorage.setOrCreate<string>('message', continueInput);
           console.info(`continue input ${continueInput}`);
         }
         // ...
         // 触发页面恢复
         this.context.restoreWindowStage(this.storage);
       }
       // ...
     }

     onContinue(wantParam: Record<string, Object>) {
       hilog.info(DOMAIN, 'testTag', '%{public}s', 'EntryAbility onContinue');
       const targetVersion = wantParam.version; // 获取迁移对端应用的版本号
       // 应用可根据源端版本号设置支持接续的最小兼容版本号，源端版本号可从app.json5文件中的versionCode字段获取；防止目标端版本号过低导致不兼容。
       const versionThreshold: number = 0; // 替换为应用自己支持兼容的最小版本号
       // 兼容性校验
       if (targetVersion < versionThreshold) {
         // 建议在校验版本兼容性失败后，提示用户拒绝迁移的原因
         promptAction.openToast({
           message: '目标端应用版本号过低，不支持接续，请您升级应用版本后再试',
           duration: 2000
         });
         // 在兼容性校验不通过时返回MISMATCH
         return AbilityConstant.OnContinueResult.MISMATCH;
       }
       console.info(`onContinue version = ${wantParam.version}, targetDevice: ${wantParam.targetDevice}`);
       // 迁移数据保存
       const continueInput = '迁移的数据';
       if (continueInput) {
         // 将要迁移的数据保存在wantParam的自定义字段（如：data）中;
         wantParam['data'] = continueInput;
       }
       // ...
       return AbilityConstant.OnContinueResult.AGREE;
     }

     onDestroy(): void {
       hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onDestroy');
     }

     onWindowStageCreate(windowStage: window.WindowStage): void {
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

   应用B的module.json5完整代码如下：

   ```json
   {
     "module": {
       "name": "product",
       "type": "entry",
       "description": "$string:module_desc",
       "mainElement": "ProductAbility",
       "deviceTypes": [
         "phone",
         "tablet",
         "2in1"
       ],
       "deliveryWithInstall": true,
       "installationFree": false,
       "pages": "$profile:main_pages",
       "abilities": [
         {
           "name": "ProductAbility",
           "srcEntry": "./ets/productability/ProductAbility.ets",
           "description": "$string:ProductAbility_desc",
           "icon": "$media:layered_image",
           "label": "$string:ProductAbility_label",
           "startWindowIcon": "$media:startIcon",
           "startWindowBackground": "$color:start_window_background",
           "exported": true,
           "continuable": true,
           "continueBundleName": [
             "com.hw.mycontinuea"
           ],
           "continueType": [
             "mainAbility"
           ],
           "skills": [
             {
               "entities": [
                 "entity.system.home"
               ],
               "actions": [
                 "ohos.want.action.home"
               ]
             }
           ]
         }
       ],
       "extensionAbilities": [
         {
           "name": "ProductBackupAbility",
           "srcEntry": "./ets/productbackupability/ProductBackupAbility.ets",
           "type": "backup",
           "exported": false,
           "metadata": [
             {
               "name": "ohos.extension.backup",
               "resource": "$profile:backup_config"
             }
           ],
         }
       ]
     }
   }
   ```
