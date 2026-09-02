---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-jsvm-10
title: 未捕获JS-Crash异常导致应用崩溃该如何处理
breadcrumb: FAQ > 应用框架开发 > NDK开发 > JSVM > 未捕获JS-Crash异常导致应用崩溃该如何处理
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:58+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:9e4c43c7869d4cb03960961a52ef20da62dd036394f560e4ec5812e4e88568dd
---

## 问题现象

应用运行过程中可能会出现JS crash异常，当出现未被捕获的JS crash异常时应用崩溃。如下图：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/eb/v3/ffwUgXORSvq8dHys1LWCgQ/zh-cn_image_0000002658907825.png "点击放大")

## 背景知识

[ErrorManager](../harmonyos-references/js-apis-app-ability-errormanager.md)模块提供对错误观察器的注册和注销的能力，在EntryAbility中配置即可实现统一处理（目前taskpool中不支持捕获异常）。

## 解决方案

1. 手动try-catch。

   针对出现异常的代码段手动try-catch捕获异常：

   ```txt
   error:  TypeError: Get Property index out-of-bounds
   ```

   ```ts
   import { ArrayList } from '@kit.ArkTS';

   @Entry
   @Component
   struct Index {

     build() {
       Row() {
         Column() {
           Button('Hello World')
             .fontSize(50)
             .fontWeight(FontWeight.Bold)
             .onClick(() => {
               this.testClick();
             });
         }
         .width('100%');
       }
       .height('100%');
     }

     doublePages = new ArrayList<number>();

     testClick() {
       try {
         let i: number = this.doublePages[1]; // index out-of-bounds
         console.info(`i is ${i}`);
       } catch (e) {
         console.error('error: ', e);
       }
     }
   }
   ```
2. ErrorManager模块统一捕获。

   虽然通过try-catch能捕获异常，但整体方案仍然存在一定缺陷，比如添加大量try-catch导致可读性变差、遗漏JS Crash未被捕获。因此建议通过ErrorManager模块统一捕获未知JS Crash。

   ```ts
   import { ConfigurationConstant, errorManager, UIAbility } from '@kit.AbilityKit';
   import { hilog } from '@kit.PerformanceAnalysisKit';
   import { window } from '@kit.ArkUI';
   import { BusinessError } from '@kit.BasicServicesKit';

   const DOMAIN = 0x0000;
   let observerId = -1;

   export default class EntryAbility extends UIAbility {
     onCreate(): void {
       let observer1: errorManager.ErrorObserver = {
         onUnhandledException(errorMsg) {
           console.error('onUnhandledException, errorMsg: ', errorMsg);
         },
         onException(errorObj) {
           console.error('onException, name: ', errorObj.name);
           console.error('onException, message: ', errorObj.message);
           if (typeof (errorObj.stack) === 'string') {
             console.error('onException, stack: ', errorObj.stack);
           }
         }
       };
       try {
         // 注册错误观测器。注册后可以捕获到应用产生的js crash，应用崩溃时进程不会退出。
         observerId = errorManager.on('error', observer1);
       } catch (paramError) {
         let code = (paramError as BusinessError).code;
         let message = (paramError as BusinessError).message;
         console.error(`error: ${code}, ${message}`);
       }
       try {
         this.context.getApplicationContext().setColorMode(ConfigurationConstant.ColorMode.COLOR_MODE_NOT_SET);
       } catch (err) {
         hilog.error(DOMAIN, 'testTag', 'Failed to set colorMode. Cause: %{public}s', JSON.stringify(err));
       }
       hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onCreate');
     }

     onDestroy(): void {
       try {
         errorManager.off('error', observerId)
           .then((data) => {
             console.info('----------- unregisterErrorObserver success ----------', data);
           })
           .catch((err: BusinessError) => {
             console.error('----------- unregisterErrorObserver fail ----------', err);
           });
       } catch (paramError) {
         let code = (paramError as BusinessError).code;
         let message = (paramError as BusinessError).message;
         console.error(`error: ${code}, ${message}`);
       }
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

   运行效果：出现JS Crash问题时应用无闪退并在日志中记录堆栈。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cd/v3/SbyJSD4BShCbe6ZGro3mBg/zh-cn_image_0000002658787889.png "点击放大")
