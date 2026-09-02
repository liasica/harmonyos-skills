---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/calendarmanager-calendar-developer
title: 日历账户管理
breadcrumb: 指南 > 应用服务 > Calendar Kit（日历服务） > 日历账户管理
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:24+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:d0276e5f47c0c474a468577f69785dc2646144fc47b81ac737e40eb4b0840b7f
---

日历账户‌用于存储和管理个人或团队的日程，通过日历账户，用户可以方便地查看、编辑和共享日程信息。

日历管理器[CalendarManager](../harmonyos-references/js-apis-calendarmanager.md#calendarmanager)用于管理日历账户[Calendar](../harmonyos-references/js-apis-calendarmanager.md#calendar)。日历账户主要包含账户信息[CalendarAccount](../harmonyos-references/js-apis-calendarmanager.md#calendaraccount)和配置信息[CalendarConfig](../harmonyos-references/js-apis-calendarmanager.md#calendarconfig)。

开发者可以创建属于应用特有的日历账户，还可以对日历账户进行新增、删除、更新和查询。此外，每个日程[Event](../harmonyos-references/js-apis-calendarmanager.md#event)归属于某一个特定的日历账户，可以通过日历账户对该账户下面的日程进行管理，具体相关指导可见[日程管理](calendarmanager-event-developer.md)。

## 接口说明

以下是日历账户管理的相关接口，更多详细接口及使用请参考[@ohos.calendarManager](../harmonyos-references/js-apis-calendarmanager.md)。

| 接口名称 | 描述 |
| --- | --- |
| getCalendarManager(context: Context): CalendarManager | 根据上下文获取日历管理器对象CalendarManager，用于管理日历。 |
| createCalendar(calendarAccount: CalendarAccount): Promise<Calendar> | 根据日历账户信息，创建一个Calendar对象，使用Promise异步回调。 |
| getCalendar(calendarAccount?: CalendarAccount): Promise<Calendar> | 获取默认Calendar对象或者指定Calendar对象，使用Promise异步回调。  默认Calendar是日历存储首次运行时创建的，若创建Event时不关注其Calendar归属，则无须通过createCalendar()创建Calendar，直接使用默认Calendar。 |
| getAllCalendars(): Promise<Calendar[]> | 获取当前应用所有创建的Calendar对象以及默认Calendar对象，使用Promise异步回调。 |
| deleteCalendar(calendar: Calendar): Promise<void> | 删除指定Calendar对象，使用Promise异步回调。 |
| getConfig(): CalendarConfig | 获取日历配置信息。 |
| setConfig(config: CalendarConfig): Promise<void> | 设置日历配置信息，使用Promise异步回调。 |
| getAccount(): CalendarAccount | 获取日历账户信息。 |

## 开发步骤

1. 导入相关依赖。

   ```typescript
   import { abilityAccessCtrl, AbilityConstant, common, PermissionRequestResult, Permissions, UIAbility, Want } from '@kit.AbilityKit';
   import { BusinessError } from '@kit.BasicServicesKit';
   import { calendarManager } from '@kit.CalendarKit';
   import { window } from '@kit.ArkUI';
   import { hilog } from '@kit.PerformanceAnalysisKit';
   ```
2. 申请权限。使用Calendar Kit时，需要在module.json5中声明申请读写日历日程所需的权限：ohos.permission.READ\_CALENDAR和ohos.permission.WRITE\_CALENDAR。具体指导可见[声明权限](declare-permissions.md)。
3. 根据上下文获取日历管理器对象calendarMgr，用于对日历账户进行相关管理操作。推荐在EntryAbility.ets文件中进行操作。

   ```typescript
   const DOMAIN = 0x0000;
       
   export let calendarMgr: calendarManager.CalendarManager | null = null;

   export let mContext: common.UIAbilityContext | null = null;

   export default class EntryAbility extends UIAbility {
     onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
       hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onCreate');
     }

     onDestroy(): void {
       hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onDestroy');
     }

     onWindowStageCreate(windowStage: window.WindowStage): void {
       // 主窗口已创建，请为此Ability设置主页
       hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onWindowStageCreate');
       windowStage.loadContent('pages/Index', (err, data) => {
         if (err.code) {
           hilog.error(DOMAIN, 'testTag', 'Failed to load the content. Cause: %{public}s', JSON.stringify(err));
           return;
         }
         hilog.info(DOMAIN, 'testTag', 'Succeeded in loading the content.');
       });
       mContext = this.context;
       const permissions: Permissions[] = ['ohos.permission.READ_CALENDAR', 'ohos.permission.WRITE_CALENDAR'];
       let atManager = abilityAccessCtrl.createAtManager();
       atManager.requestPermissionsFromUser(mContext, permissions).then((result: PermissionRequestResult) => {
         hilog.info(DOMAIN, 'testTag', 'get Permission success');
         calendarMgr = calendarManager.getCalendarManager(mContext);
       }).catch((error: BusinessError) => {
         hilog.error(DOMAIN, 'testTag', 'get Permission error, Cause: %{public}s', JSON.stringify(error));
       })
     }

     onWindowStageDestroy(): void {
       // 主窗口已销毁，释放 UI 相关资源
       hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onWindowStageDestroy');
     }

     onForeground(): void {
       // Ability 进入前台
       hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onForeground');
     }

     onBackground(): void {
       // Ability 进入后台
       hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onBackground');
     }
   }
   ```
4. 根据日历账户信息，创建一个日历账户Calendar对象。

   ```typescript
   import { BusinessError } from '@kit.BasicServicesKit';
   import { calendarMgr } from '../entryability/EntryAbility';
   import { calendarManager } from '@kit.CalendarKit';

   let calendar: calendarManager.Calendar | undefined = undefined;
   // 指定日历账户信息
   const calendarAccount: calendarManager.CalendarAccount = {
     // 日历账户名称
     name: 'MyCalendar',
     // 日历账户类型
     type: calendarManager.CalendarType.LOCAL,
     // 日历账户显示名称，该字段如果不填，创建的日历账户在界面显示为空字符串。
     displayName: 'MyCalendar'
   };
   ```

   ```typescript
   // 创建日历账户
   calendarMgr?.createCalendar(calendarAccount).then((data: calendarManager.Calendar) => {
     console.info('%{public}s', `Succeeded in creating calendar data->${JSON.stringify(data)}`);
     calendar = data;
     // 请确保日历账户创建成功后，再进行后续相关操作
     // ...
   }).catch((error: BusinessError) => {
     console.error(`Failed to create calendar. Code: ${error.code}, message: ${error.message}`);
   });
   ```
5. 日历账户创建之后，日历账户颜色默认为黑色，不指定日历账户颜色可能导致部分版本/设备深色模式下显示效果不佳。开发者需要调用setConfig()接口设置日历配置信息，包括是否打开日历账户下的日程提醒能力、设置日历账户颜色。

   ```typescript
   const calendarAccounts: calendarManager.CalendarAccount = {
     name: 'MyCalendar',
     type: calendarManager.CalendarType.LOCAL,
     displayName: 'MyCalendar'
   };
   // 日历配置信息
   calendarMgr?.getCalendar(calendarAccounts, (err, data) => {
     // 获取日历账户
     if (err) {
       console.error(`Failed to get calendar, Code is ${err.code}, message is ${err.message}`);
     } else {
       const config: calendarManager.CalendarConfig = {
         // 打开日程提醒
         enableReminder: true,
         // 设置日历账户颜色
         color: '#aabbcc'
       };
       // 设置日历配置信息
       data.setConfig(config).then(() => {
         console.info('%{public}s', `Succeeded in setting config, data->${JSON.stringify(config)}`);
       }).catch((err: BusinessError) => {
         console.error(`Failed to set config. Code: ${err.code}, message: ${err.message}`);
       })
     }
   });
   ```
6. 可以查询指定日历账户。

   ```typescript
   calendarMgr?.getCalendar(calendarAccount).then((data: calendarManager.Calendar) => {
     console.info('%{public}s', `Succeeded in getting calendar, data -> ${JSON.stringify(data)}`);
   }).catch((err: BusinessError) => {
     console.error(`Failed to get calendar. Code: ${err.code}, message: ${err.message}`);
   });
   ```
7. 也可以查询默认日历账户，默认日历账户是日历存储首次运行时创建的，若创建日程时不关注归属哪个账户，则无须单独创建日历账户，可以直接使用默认日历账户。

   ```typescript
   calendarMgr?.getCalendar().then((data: calendarManager.Calendar) => {
     console.info('%{public}s', `Succeeded in getting calendar, data -> ${JSON.stringify(data)}`);
   }).catch((err: BusinessError) => {
     console.error(`Failed to get calendar. Code: ${err.code}, message: ${err.message}`);
   });
   ```
8. 获取当前应用所有创建的日历账户及默认日历账户Calendar对象。

   由于涉及数据隐私安全，进行了权限管控的应用无法获取其他应用创建的账户信息。

   ```typescript
   calendarMgr?.getAllCalendars().then((data: calendarManager.Calendar[]) => {
     console.info('%{public}s', `Succeeded in getting all calendars, data -> ${JSON.stringify(data)}`);
     data.forEach((calendar) => {
       const account = calendar.getAccount();
       console.info('%{public}s', `account -> ${JSON.stringify(account)}`);
     })
   }).catch((err: BusinessError) => {
     console.error(`Failed to get all calendars. Code: ${err.code}, message: ${err.message}`);
   });
   ```
9. 删除指定的日历账户，删除账户后，该账户下的所有日程会全部删除。

   ```typescript
   if (!calendar || calendar === null) {
     console.error('Failed to delete calendar. calendar is null');
     return;
   }
   calendarMgr?.deleteCalendar(calendar).then(() => {
     console.info('%{public}s', 'Succeeded in deleting calendar');
   }).catch((err: BusinessError) => {
     console.error(`Failed to delete calendar. Code: ${err.code}, message: ${err.message}`);
   });
   ```
