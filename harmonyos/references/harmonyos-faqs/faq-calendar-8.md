---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faq-calendar-8
title: 如何使用editEvent接口新建日程
breadcrumb: FAQ > 应用服务开发 > 日历服务（Calendar Kit） > 如何使用editEvent接口新建日程
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:49+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:e81aed87f26c645d53ceaf2faad0554961995b237e05cefb646eab87dac5887f
---

## 问题现象

如何在系统日历中使用editEvent接口添加日程？

## 背景知识

* [日程管理](../harmonyos-guides/calendarmanager-event-developer.md)即对这些事件、活动进行规划和控制，详细接口及使用请参考[@ohos.calendarManager](../harmonyos-references/js-apis-calendarmanager.md)。
* editEvent接口通过跳转到日程创建界面创建，入参Event不填日程id，使用Promise异步回调。

## 解决方案

1. 申请权限：申请ohos.permission.READ\_CALENDAR和ohos.permission.WRITE\_CALENDAR权限。
2. 创建全局共享对象：使用日程管理器对象calendarMgr对日历账户进行相关管理操作。

   ```ts
   import { hilog } from '@kit.PerformanceAnalysisKit';
   import { window } from '@kit.ArkUI';
   import {
     abilityAccessCtrl,
     common,
     PermissionRequestResult,
     Permissions,
     AbilityConstant,
     ConfigurationConstant,
     UIAbility,
     Want
   } from '@kit.AbilityKit';
   import { BusinessError } from '@kit.BasicServicesKit';
   import { calendarManager } from '@kit.CalendarKit';

   const DOMAIN = 0x0000;

   interface AppGlobalType {
     calendarMgr: calendarManager.CalendarManager | null;
     mContext: common.UIAbilityContext | null;
   }

   export const AppGlobal: AppGlobalType = {
     calendarMgr: null,
     mContext: null
   };

   export default class EntryAbility extends UIAbility {
     onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
       this.context.getApplicationContext().setColorMode(ConfigurationConstant.ColorMode.COLOR_MODE_NOT_SET);
       hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onCreate', want, launchParam);
     }

     onDestroy(): void {
       hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onDestroy');
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

       // 将上下文存储到AppGlobal中
       AppGlobal.mContext = this.context;
       const permissions: Permissions[] = ['ohos.permission.READ_CALENDAR', 'ohos.permission.WRITE_CALENDAR'];
       let atManager = abilityAccessCtrl.createAtManager();

       atManager.requestPermissionsFromUser(this.context, permissions).then((result: PermissionRequestResult) => {
         let resultStr = JSON.stringify(result);
         console.info(`get Permission success, result: ${resultStr}`);
         // 将calendarManager存储到AppGlobal中
         AppGlobal.calendarMgr = calendarManager.getCalendarManager(this.context);
       }).catch((error: BusinessError) => {
         console.error(`get Permission error, error. Code: ${error.code}, message: ${error.message}`);
       });
     }

     onWindowStageDestroy(): void {
       hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onWindowStageDestroy');
     }

     onForeground(): void {
       hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onForeground');
     }

     onBackground(): void {
       hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onBackground');
     }
   };
   ```
3. 在获取到calendarMgr对象后，可通过[editEvent](../harmonyos-references/js-apis-calendarmanager.md#editevent12)接口创建日程。

   ```ts
   import { calendarManager } from '@kit.CalendarKit';
   import { AppGlobal } from '../entryability/EntryAbility';
   import { BusinessError } from '@kit.BasicServicesKit';

   @Entry
   @Component
   struct Index {
     private getCalendarMgr(): calendarManager.CalendarManager | null {
       if (!AppGlobal.calendarMgr) {
         console.error('CalendarManager is not initialized');
         return null;
       }
       return AppGlobal.calendarMgr;
     }

     addEvent(): void {
       const mgr = this.getCalendarMgr();
       if (!mgr) {
         return;
       }

       const now = Date.now();
       const event: calendarManager.Event = {
         title: 'My Event',
         type: calendarManager.EventType.NORMAL,
         startTime: now,
         endTime: now + 60 * 60 * 1000
       };

       mgr.editEvent(event)
         .then((id: number) => {
           console.info(`Event created successfully, id = ${id}`);
         })
         .catch((err: BusinessError) => {
           console.error(`Create event failed. Code: ${err.code}, message: ${err.message}`);
         });
     }

     build() {
       Column() {
         Text('点击按钮创建日程')
           .fontSize(18)
           .fontWeight(FontWeight.Medium)
           .margin({ bottom: 16 })

         Button('Add Event')
           .onClick(() => {
             this.addEvent();
           });
       }
       .height('100%')
       .width('100%')
       .justifyContent(FlexAlign.Center)
       .alignItems(HorizontalAlign.Center);
     }
   }
   ```

## 常见FAQ

Q：新增了多条日程，并且回调都是成功的，但系统日历中只显示了一条。

A：时间及标题相同时，会被系统日历界面去重隐藏。
