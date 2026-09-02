---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-local-database-management-54
title: 如何解决传入错误的上下文对象而导致获取首选项实例失败的问题
breadcrumb: FAQ > 应用框架开发 > 本地数据和文件 > 本地数据库管理 > 如何解决传入错误的上下文对象而导致获取首选项实例失败的问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:29+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:86a0b7b36699f6550287497a766fb76969a8435bcc6bceb171702d89d0b99612
---

## 问题现象

开发者在使用Preferences(用户首选项)来进行持久化数据操作中会出现15500000报错，如何排查？

## 背景知识

* [15500000](../harmonyos-references/errorcode-preferences.md#section15500000-内部错误)为用户首选项内部发生错误。
* [getPreferencesSync()](../harmonyos-references/js-apis-data-preferences.md#preferencesgetpreferencessync10)或者[getPreferences()](../harmonyos-references/js-apis-data-preferences.md#preferencesgetpreferences)获取Preferences实例时，须传入应用上下文。

## 解决方案

发生用户首选项内部错误，一般是因为获取Preferences实例时，传入的context存在问题。可以在应用初始化的过程当中，设置一个全局的应用上下文对象，在获取Preferences实例时，传入这个全局对象。

1. 在GlobalContext.ets中定义全局上下文对象：

   ```ts
   import { common } from '@kit.AbilityKit';

   export class GlobalContext {
     private static context: common.UIAbilityContext;

     public static initContext(context: common.UIAbilityContext): void {
       GlobalContext.context = context;
     }

     public static getGlobalContext(): common.UIAbilityContext {
       return GlobalContext.context;
     }
   }
   ```
2. 在EntryAbility.ets中初始化全局Context。

   ```ts
   import { UIAbility } from '@kit.AbilityKit';
   import { hilog } from '@kit.PerformanceAnalysisKit';
   import { window } from '@kit.ArkUI';
   import { GlobalContext } from '../pages/GlobalContext';

   const DOMAIN = 0x0000;

   export default class EntryAbility extends UIAbility {

     onDestroy(): void {
       hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onDestroy');
     }

     onWindowStageCreate(windowStage: window.WindowStage): void {
       // Main window is created, set main page for this ability
       hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onWindowStageCreate');

       windowStage.loadContent('pages/Index', (err) => {
         if (err.code) {
           return;
         }
         GlobalContext.initContext(this.context);
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
3. 通过定义的全局应用上下文对象，来获取对应的首选项实例，并定义存取方法。

   ```ts
   import { preferences } from '@kit.ArkData';
   import { GlobalContext } from './GlobalContext';

   export class PreferenceUtil {
     public static getPreference() {
       let options: preferences.Options = { name: 'myStore' };
       let preference = preferences.getPreferencesSync(GlobalContext.getGlobalContext(), options);
       return preference;
     }

     public static put(preference: preferences.Preferences, val: string) {
       preference.putSync('myStore', val);
     }

     public static get(preference: preferences.Preferences) {
       return preference.getSync('myStore', 'default');
     }
   }
   ```
4. 在Index.ets中调用存取方法。

   ```ts
   import { PreferenceUtil } from './PreferenceUtil';

   @Entry
   @Component
   struct Index {
     @State message: string = '未获取到时间';

     build() {
       Column() {
         Text(this.message)
           .margin({ top: 50 });
         Row({ space: 50 }) {
           Button('存值')
             .onClick(() => {
               PreferenceUtil.put(PreferenceUtil.getPreference(), new Date().toString());
             });
           Button('取值')
             .onClick(() => {
               this.message = PreferenceUtil.get(PreferenceUtil.getPreference()) as string;
             });
         }
         .margin({ top: 20 });
       }
       .height('100%')
       .width('100%');
     }
   }
   ```

## 总结

开发者在使用用户首选项来进行持久化数据操作中，出现15500000报错，往往是使用getPreferencesSync()或者getPreferences()获取Preferences实例时，传入的context存在问题，建议获取一个全局的context，在调用方法时使用全局context来确保传入应用上下文的正确性。
