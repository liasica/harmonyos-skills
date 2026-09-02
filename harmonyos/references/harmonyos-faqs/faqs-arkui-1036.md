---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1036
title: PersistenceV2如何实现数据持久化存储和修改
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > PersistenceV2如何实现数据持久化存储和修改
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:06+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:1b817348a2e2c144edccb7437a5ef81625b5ddbe530d4c66dd555c2caacf7b50
---

## 问题现象

为了增强状态管理框架对持久化存储UI的能力，开发者可以使用PersistenceV2存储持久化的数据。PersistenceV2不但可以和UI组件同步，还可以在应用业务逻辑中被访问和修改。下面就这两种常见的场景给出案例，详细讲解两种场景下PersistenceV2的使用和注意事项。

## 背景知识

* [PersistenceV2](../harmonyos-guides/arkts-new-persistencev2.md)是在应用UI启动时被创建的单例，必须与UI实例关联，持久化操作需在UI实例初始化完成后调用（即[loadContent](../harmonyos-references/arkts-apis-window-windowstage.md#loadcontent9)回调触发后）。
* 只有[@Trace](../harmonyos-guides/arkts-new-observedv2-and-trace.md)的数据改变会触发自动持久化，如V1状态变量、@Observed对象、普通数据的改变不会触发持久化。
* 如果对数据持久化能力有较强的诉求，例如持久化时机，建议使用[Preferences](../harmonyos-guides/preferences-guidelines.md)进行数据持久化。
* PersistenceV2不宜大量持久化数据，可能会导致页面卡顿。

## 解决方案

如何在UI组件和应用业务逻辑中使用PersistenceV2，下面用一个案例说清楚PersistenceV2在两种场景中的使用：

1. 首先定义一个PData类作为持久化类，将需要和UI页面同步刷新的属性用@Trace进行装饰。需要注意的是PData需要用@ObservedV2和@Trace装饰器进行装饰。
2. 定义一个在应用业务逻辑中使用的MyUtils类，类中定义需要使用的更新持久化数据的方法upDatePDataById和upDatePData。需要注意的是如果是使用整个对象对PersistenceV2存储的数据进行更新，需要逐个属性进行赋值。
3. 在需要更新数据的地方调用MyUtils类中的更新方法即可。
   * 在UI页面中调用：

     ```ts
     import { PersistenceV2 } from '@kit.ArkUI';

     @ObservedV2
     export class PData {
       // 被PersistenceV2持久化的类属性必须要有初值，否则不支持持久化。
       @Trace id: string = '';
       // 只有@Trace的数据改变会触发自动持久化，普通数据的改变不会触发持久化。
       data: string = '';
     }

     export class MyUtils {
       static upDatePDataById(id: string) {
         let pData: PData = PersistenceV2.globalConnect({ type: PData, defaultCreator: () => new PData() })!;
         console.info(`upDatePDataById, before pData.id = ${pData.id}, pData.data = ${pData.data}`);
         // id是@Trace装饰的，直接修改即可触发持久化
         pData.id = id;
         console.info(`upDatePDataById, after pData.id = ${pData.id}, pData.data = ${pData.data}`);
       }

       static upDatePData(pDataTmp: PData) {
         let pData: PData = PersistenceV2.globalConnect({ type: PData, defaultCreator: () => new PData() })!;

         console.info(`upDatePData, before pData.id = ${pData.id}, pData.data = ${pData.data}`);
         // 普通数据的改变不会触发持久化，不能对整个对象进行赋值。所以属性值需要逐个赋值，可在赋值普通数据之后赋值@Trace装饰的数据，触发持久化
         pData.data = pDataTmp.data;
         pData.id = pDataTmp.id;
         console.info(`upDatePData, after pData.id = ${pData.id}, pData.data = ${pData.data}`);
       }
     }

     @Entry
     @ComponentV2
     struct Index {
       @Local pData: PData = PersistenceV2.globalConnect({ type: PData, defaultCreator: () => new PData() })!;

       build() {
         Row() {
           Column() {
             Text(this.pData.id)
               .fontSize(30)
               .fontWeight(FontWeight.Bold)
             Text(this.pData.data) // data非@Trace修饰，数据变化UI不会刷新
               .fontSize(30)
               .fontWeight(FontWeight.Bold)
             Button('更新PersistenceV2中的属性')
               .onClick(() => {
                 MyUtils.upDatePDataById(new Date().getTime().toString());
               })
             Button('更新PersistenceV2中的对象')
               .onClick(() => {
                 let pDataTmp = new PData();
                 pDataTmp.id = new Date().getTime().toString();
                 pDataTmp.data = new Date().getTime().toString() + '-data';
                 MyUtils.upDatePData(pDataTmp);
               }).margin({ top: 20 })
           }.width('100%')
         }.height('100%')
       }
     }
     ```
   * 在应用业务逻辑中调用：在应用业务逻辑中使用PersistenceV2，需要注意持久化操作需在UI实例初始化完成后调用（即loadContent回调触发后）。应用的生命周期可以参考官网[UIAbility组件生命周期](../harmonyos-guides/uiability-lifecycle.md)。基于此，在应用的onWindowStageDestroy和onDestroy中可以正常读取PersistenceV2中的内容，但是不能进行数据的修改，持久化过程会失败。

     ```ts
     import { ConfigurationConstant, UIAbility } from '@kit.AbilityKit';
     import { hilog } from '@kit.PerformanceAnalysisKit';
     import { PersistenceV2, window } from '@kit.ArkUI';
     import { MyUtils, PData } from '../pages/Index';

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
         // 可以正常读取
         let pData: PData = PersistenceV2.globalConnect({ type: PData, defaultCreator: () => new PData() })!;
         console.info(`onDestroy, pData.id = ${pData.id}, pData.data = ${pData.data}`);

         // PersistenceV2必须与UI实例关联，在销毁过程中进行数据持久化修改，修改不生效
         MyUtils.upDatePDataById(new Date().getTime().toString());
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

           // 可以正常读取
           let pData: PData = PersistenceV2.globalConnect({ type: PData, defaultCreator: () => new PData() })!;
           console.info(`onWindowStageCreate, pData.id = ${pData.id}, pData.data = ${pData.data}`);

           // PersistenceV2必须与UI实例关联，持久化操作需在UI实例初始化完成后调用（即loadContent回调触发后），修改生效
           MyUtils.upDatePDataById(new Date().getTime().toString());
         });
       }

       onWindowStageDestroy(): void {
         // Main window is destroyed, release UI related resources
         hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onWindowStageDestroy');

         // 可以正常读取
         let pData: PData = PersistenceV2.globalConnect({ type: PData, defaultCreator: () => new PData() })!;
         console.info(`onWindowStageDestroy, pData.id = ${pData.id}, pData.data = ${pData.data}`);

         // PersistenceV2必须与UI实例关联，在销毁过程中进行数据持久化修改，修改不生效
         MyUtils.upDatePDataById(new Date().getTime().toString());
       }

       onForeground(): void {
         // Ability has brought to foreground
         hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onForeground');
       }

       onBackground(): void {
         // 可以正常读取
         let pData: PData = PersistenceV2.globalConnect({ type: PData, defaultCreator: () => new PData() })!;
         console.info(`onBackground, pData.id = ${pData.id}, pData.data = ${pData.data}`);

         // PersistenceV2必须与UI实例关联，持久化操作需在UI实例初始化完成后调用（即loadContent回调触发后），修改生效
         MyUtils.upDatePDataById(new Date().getTime().toString());
         hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onDestroy');

         // Ability has back to background
         hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onBackground');
       }
     }
     ```

## 常见FAQ

Q：报错PersistenceV2==error key: XXXX, reason: serialization, message: TypeError: Cannot read property **proto** of null如何解决？

A：PersistenceV2持久化的对象需要是一个状态变量，不能是一个json字符串。可以new一个对象实例，然后定义一个方法，方法中逐个对实例的属性进行赋值。
