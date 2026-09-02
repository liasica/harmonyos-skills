---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ability-153
title: 如何在HAR/HSP包中监听系统环境变量变化
breadcrumb: FAQ > 应用框架开发 > 程序框架 > 程序框架（Ability） > 如何在HAR/HSP包中监听系统环境变量变化
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:55+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:3b0ac0c17b3a2a4eba4f80b7e980d32e564af0acf006e5f3902af397bae2de37
---

## 问题现象

HAR/HSP中需要监听系统环境变量变化，如何实现？

## 背景知识

* [HAR](../harmonyos-guides/har-package.md)包是静态共享包，不能包含动态注册的组件，仅限于代码复用，如果需要在包中定义UIAbility，也需要在HAP中module.json5文件中声明对应的UIAbility，不能在HAR包中直接声明。
* [HSP](../harmonyos-guides/in-app-hsp.md)是动态共享包，包含代码、C++库、资源和配置文件，通过HSP可以实现代码和资源的共享。
* [EnvironmentCallback](../harmonyos-references/js-apis-app-ability-environmentcallback.md)模块提供应用上下文ApplicationContext对系统环境变化监听回调的能力。
* [Ability](../harmonyos-references/js-apis-app-ability-ability.md#abilityonconfigurationupdate)类是应用生命周期调度的基本单元，也是UIAbility类的基类，也提供了对系统环境变化监听回调的能力。

## 解决方案

提供以下两种解决方案：

* 方案一：[EnvironmentCallback](../harmonyos-references/js-apis-app-ability-environmentcallback.md)模块提供对系统环境变化监听回调的能力。
  1. HAR/HSP包中定义一个EnvironmentMonitor，参考代码如下：

     ```ts
     import { AbilityConstant, common, Configuration, EnvironmentCallback } from '@kit.AbilityKit';

     export class EnvironmentMonitor {
       private context: common.UIAbilityContext | null = null;
       private callbackId: number | null = null;

       constructor(context: common.UIAbilityContext) {
         this.context = context;
       }

       onEnvironmentMonitor() {
         if (!this.context) {
           return;
         }
         let environmentCallback: EnvironmentCallback = {
           onConfigurationUpdated(config: Configuration) {
             console.info(`应用当前语言：${config.language}`);
             console.info(`应用深浅色模式[-1:未设置颜色; 0:深色; 1:浅色]：${config.colorMode}`);
             console.info(`指针设备是否已连接（鼠标、触控板等）：${config.hasPointerDevice}`);
             console.info(`应用字体的唯一ID：${config.fontId}`);
             console.info(`字体大小缩放比例：${config.fontSizeScale}`);
             console.info(`字体粗细缩放比例：${config.fontWeightScale}`);
             console.info(`移动设备国家代码：${config.mcc}`);
             console.info(`区域设置：${config.locale}`);
           },

           onMemoryLevel(level) {
             console.info(`监听内存变化: ${JSON.stringify(level)}`);
             switch (level) {
               case AbilityConstant.MemoryLevel.MEMORY_LEVEL_MODERATE:
                 console.info('MEMORY_LEVEL_MODERATE');
                 break;
               case AbilityConstant.MemoryLevel.MEMORY_LEVEL_LOW:
                 console.info('MEMORY_LEVEL_LOW');
                 break;
               case AbilityConstant.MemoryLevel.MEMORY_LEVEL_CRITICAL:
                 console.info('MEMORY_LEVEL_CRITICAL');
                 break;
               default:
                 console.info(`default`);
             }
           }
         };
         this.callbackId = this.context.getApplicationContext().on('environment', environmentCallback);
       }

       offEnvironmentMonitor() {
         if (!this.callbackId || !this.context) {
           return;
         }
         this.context.getApplicationContext().off('environment', this.callbackId);
       }
     }
     ```
  2. 在HAR/HSP包入口文件index.ets导出定义的EnvironmentMonitor：

     ```ts
     export { EnvironmentMonitor } from './src/main/ets/monitor/EnvironmentMonitor';
     ```
  3. 宿主HAP包中EntryAbility初始化并开启监听内存变化：

     ```ts
     import { UIAbility } from '@kit.AbilityKit';
     import { hilog } from '@kit.PerformanceAnalysisKit';
     import { window } from '@kit.ArkUI';
     import { EnvironmentMonitor } from 'hara';

     const DOMAIN = 0x0000;

     export default class EntryAbility extends UIAbility {
       private monitor: EnvironmentMonitor | null = null;

       onCreate(): void {
         this.monitor = new EnvironmentMonitor(this.context);
         this.monitor.onEnvironmentMonitor();
       }

       onDestroy(): void {
         this.monitor?.offEnvironmentMonitor();
       }

       onWindowStageCreate(windowStage: window.WindowStage): void {
         hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onWindowStageCreate');
         windowStage.loadContent('pages/Index', (err) => {
           if (err.code) {
             hilog.error(DOMAIN, 'testTag', 'Failed to load the content. Cause: %{public}s', JSON.stringify(err));
             return;
           }
           hilog.info(DOMAIN, 'testTag', 'Succeeded in loading the content.');
         });
       }
     }
     ```

* 方案二：在HAR/HSP包中定义一个类CustomUIAbility，继承自UIAbility，其中实现onMemoryLevel、onConfigurationUpdated方法。并且宿主HAP包当中的EntryAbility不再直接继承UIAbility，而是继承自定义的CustomUIAbility。
  1. 在HAR/HSP包中定义一个类CustomUIAbility，继承自UIAbility，其中实现onMemoryLevel、onConfigurationUpdated方法，代码案例如下：

     ```ts
     import { AbilityConstant, Configuration, UIAbility } from '@kit.AbilityKit';

     export class CustomUIAbility extends UIAbility {
       onMemoryLevel(level: AbilityConstant.MemoryLevel): void {
         switch (level) {
           case AbilityConstant.MemoryLevel.MEMORY_LEVEL_MODERATE:
             console.info('MEMORY_LEVEL_MODERATE');
             break;
           case AbilityConstant.MemoryLevel.MEMORY_LEVEL_LOW:
             console.info('MEMORY_LEVEL_LOW');
             break;
           case AbilityConstant.MemoryLevel.MEMORY_LEVEL_CRITICAL:
             console.info('MEMORY_LEVEL_CRITICAL');
             break;
           default:
             console.info(`default`);
         }
       }

       onConfigurationUpdate(newConfig: Configuration): void {
         console.info(`应用当前语言：${newConfig.language}`);
         console.info(`应用深浅色模式[-1:未设置颜色; 0:深色; 1:浅色]：${newConfig.colorMode}`);
         console.info(`屏幕方向[-1:未设置方向; 0:垂直; 1:水平]：${newConfig.direction}`);
         console.info(`屏幕显示密度：${newConfig.screenDensity}`);
         console.info(`应用所在的物理屏幕ID：${newConfig.displayId}`);
         console.info(`指针设备是否已连接（鼠标、触控板等）：${newConfig.hasPointerDevice}`);
         console.info(`应用字体的唯一ID：${newConfig.fontId}`);
         console.info(`字体大小缩放比例：${newConfig.fontSizeScale}`);
         console.info(`字体粗细缩放比例：${newConfig.fontWeightScale}`);
         console.info(`移动设备国家代码：${newConfig.mcc}`);
         console.info(`区域设置：${newConfig.locale}`);
       }
     }
     ```
  2. 在HAR/HSP包入口文件index.ets导出定义的CustomUIAbility：

     ```ts
     export { CustomUIAbility } from './src/main/ets/ability/CustomUIAbility';
     ```
  3. 宿主HAP中EntryAbility不再直接继承UIAbility，而是继承HAR包中定义的CustomUIAbility。

     ```screen
     import { hilog } from '@kit.PerformanceAnalysisKit';
     import { window } from '@kit.ArkUI';
     import { CustomUIAbility } from 'hara';

     const DOMAIN = 0x0000;

     export default class EntryAbility extends CustomUIAbility {

       onWindowStageCreate(windowStage: window.WindowStage): void {
         windowStage.loadContent('pages/Index', (err) => {
           if (err.code) {
             hilog.error(DOMAIN, 'testTag', 'Failed to load the content. Cause: %{public}s', JSON.stringify(err));
             return;
           }
           hilog.info(DOMAIN, 'testTag', 'Succeeded in loading the content.');
         });
       }

     }
     ```
