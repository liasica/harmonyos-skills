---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faq-calendar-1
title: 系统日历无法同步应用的日程信息
breadcrumb: FAQ > 应用服务开发 > 日历服务（Calendar Kit） > 系统日历无法同步应用的日程信息
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:49+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:14c94992b1d1cb398a437f2101b3094bfabec8ceae8c4ea7fbe62def01bb3bd4
---

## 问题现象

系统的日历不能同步应用设置的会议等日程信息。

## 背景知识

* [Calendar Kit](../harmonyos-guides/calendar-kit.md)：日历服务。
* 导入相关依赖。

  ```screen
  // EntryAbility.ets
  import { abilityAccessCtrl, AbilityConstant, common, PermissionRequestResult, Permissions, UIAbility, Want } from '@kit.AbilityKit';
  import { BusinessError } from '@kit.BasicServicesKit';
  import { calendarManager } from '@kit.CalendarKit';
  import { window } from '@kit.ArkUI';
  ```
* 申请权限。使用Calendar Kit时，需要在module.json5中声明申请读写日历日程所需的权限：ohos.permission.READ\_CALENDAR和ohos.permission.WRITE\_CALENDAR。具体指导可见[声明权限](../harmonyos-guides/declare-permissions.md)。
* 根据上下文获取日程管理器对象calendarMgr，用于对日历账户进行相关管理操作。推荐在EntryAbility.ets文件中进行操作。

  ```screen
    // EntryAbility.ets
   export let calendarMgr: calendarManager.CalendarManager | null = null;
   export let mContext: common.UIAbilityContext | null = null;

   export default class EntryAbility extends UIAbility {
     onWindowStageCreate(windowStage: window.WindowStage): void {
       console.info('Ability onWindowStageCreate');
       windowStage.loadContent('pages/Index', (err, data) => {
         if (err.code) {
           console.error(`Failed to load the content. Code: ${err.code}, message: ${err.message}`);
           return;
         }
         let dataStr = JSON.stringify(data);
         console.info(`Succeeded in loading the content. Data: ${dataStr}`);
       });
       mContext = this.context;
       const permissions: Permissions[] = ['ohos.permission.READ_CALENDAR', 'ohos.permission.WRITE_CALENDAR'];
       let atManager = abilityAccessCtrl.createAtManager();
       atManager.requestPermissionsFromUser(mContext, permissions).then((result: PermissionRequestResult) => {
       let resultStr = JSON.stringify(result);
         console.info(`get Permission success, result: ${resultStr}`);
         calendarMgr = calendarManager.getCalendarManager(mContext);
       }).catch((error: BusinessError) => {
         console.error(`get Permission error, error. Code: ${error.code}, message: ${error.message}`);
       })
     }
   }
  ```
* 根据日历账户信息，创建一个日历账户Calendar对象。

  ```screen
  // Index.ets
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
  // 创建日历账户
  calendarMgr?.createCalendar(calendarAccount).then((data: calendarManager.Calendar) => {
    console.info(`Succeeded in creating calendar data`);
    calendar = data;
    // 请确保日历账户创建成功后，再进行后续相关操作
    // ...
  }).catch((error: BusinessError) => {
    console.error(`Failed to create calendar. Code: ${error.code}, message: ${error.message}`);
  });
  ```
* 日程管理等操作，参考[@ohos.calendarManager](../harmonyos-references/js-apis-calendarmanager.md)。

## 问题定位

1. 查看module.json5文件是否声明申请读写日历日程所需的权限：ohos.permission.READ\_CALENDAR和ohos.permission.WRITE\_CALENDAR。
2. 查看[calendarManager.getCalendar](../harmonyos-references/js-apis-calendarmanager.md#getcalendar)参数传递是否有效。

   ```screen
   mContext = this.context;
   calendarMgr = calendarManager.getCalendarManager(mContext);
   ```
3. 查看是否日历能力支持。参考日历[能力范围](../harmonyos-guides/calendarmanager-overview.md#能力范围)，确认业务类型是否为日历能力支持范围。

## 分析结论

未申请ohos.permission.READ\_CALENDAR和ohos.permission.WRITE\_CALENDAR权限或未实现日程管理功能。

## 修改建议

参考[日程管理](../harmonyos-guides/calendarmanager-event-developer.md)中的[开发步骤](../harmonyos-guides/calendarmanager-event-developer.md#开发步骤)示例代码，实现日程管理功能。
