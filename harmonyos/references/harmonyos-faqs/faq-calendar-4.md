---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faq-calendar-4
title: 应用创建了日程事件但无相关提醒功能
breadcrumb: FAQ > 应用服务开发 > 日历服务（Calendar Kit） > 应用创建了日程事件但无相关提醒功能
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:49+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:da315443a209a9864814da3327ca6cee2ca3e2ae6cfb3bc9ee604b38716b1325
---

## 问题现象

应用内申请了日历权限，并在日历中创建了一条日程，但是一直到活动结束都没有该日程的相关提醒。

## 背景知识

* [Calendar Kit（日历服务）](../harmonyos-guides/calendarmanager-overview.md)提供日历与日程管理能力，通常是指可以用于访问和操作日历数据的API（应用程序接口）。这些接口允许开发者将其他应用中的工作、生活中与时间相关的日程服务（如出行、餐饮、运动、娱乐等）与系统日历进行集成，从而实现日程管理、事件创建、查询等功能。
* 日程[Event](../harmonyos-references/js-apis-calendarmanager.md#event)：日程对象，包含日程标题、开始时间、结束时间等信息。其中的reminderTime字段是日程提醒时间，单位为分钟。填写x分钟，即距开始时间提前x分钟提醒，不填时，默认为不提醒。为负值时表示延期多长时间提醒。

## 问题定位

1. 在日志中筛选“AddEvent”关键字，该日志表明已经开始进入创建日程；继续筛选“AddEvent failed!”关键字，若有该日志则表示调用[addEvent](../harmonyos-references/js-apis-calendarmanager.md#addevent)创建日程失败；

   ```screen
   A0050A/com.nfd...t/CalendarApi  com.example.test      I     GetRowCount is 1
   A0050A/com.nfd...t/CalendarApi  com.example.test      I     GetCalendar succeeded
   A0050A/com.nfd...t/CalendarApi  com.example.test      I     AddEvent
   A0050A/com.nfd...t/CalendarApi  com.example.test      I     Insert Event eventId 242
   ```
2. 查看系统日历中该日程活动是否设置了提醒，若未设置日程对象[Event](../harmonyos-references/js-apis-calendarmanager.md#event)中的reminderTime字段，将导致该日程活动默认不提醒。

## 分析结论

应用在调用[addEvent](../harmonyos-references/js-apis-calendarmanager.md#addevent)接口向系统日历添加日程活动时，未设置日程对象[Event](../harmonyos-references/js-apis-calendarmanager.md#event)中的reminderTime字段。

## 修改建议

向系统日历添加日程活动时，若希望对用户进行提醒，需要设置日程对象[Event](../harmonyos-references/js-apis-calendarmanager.md#event)中的reminderTime字段。

示例代码如下，注意需在module.json5文件中配置[ohos.permission.WRITE\_CALENDAR](../harmonyos-guides/permissions-for-all-user.md#ohospermissionwrite_calendar)权限：

```screen
import { calendarManager } from '@kit.CalendarKit';
import { abilityAccessCtrl, common, PermissionRequestResult, Permissions } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  private context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
  calendarMgr: calendarManager.CalendarManager | undefined = undefined;
  // 指定日历账户信息
  private calendarAccount: calendarManager.CalendarAccount = {
    // 日历账户名称
    name: 'MyCalendar',
    // 日历账户类型
    type: calendarManager.CalendarType.LOCAL,
    // 日历账户显示名称，该字段如果不填，创建的日历账户在界面显示为空字符串。
    displayName: 'MyCalendar'
  };

  addEvent() {
    const date = new Date();
    // 日历提醒信息，可根据需要自定义配置
    const event: calendarManager.Event = {
      // 日程标题
      title: '测试日程提醒',
      // 日程类型，不推荐三方开发者使用calendarManager.EventType.IMPORTANT，重要日程类型不支持一键服务跳转功能及无法自定义提醒时间
      type: calendarManager.EventType.NORMAL,
      // 日程开始时间
      startTime: date.getTime() + 11 * 60 * 1000,
      // 日程结束时间
      endTime: date.getTime() + 60 * 60 * 1000,
      // 设置提醒：距开始时间提前10分钟提醒
      reminderTime: [10],
      // 日程重复规则，可选属性。如果日程为周期性日程需要填写该属性。
      recurrenceRule: {
        // 日程重复规则类型，支持按天、按周、按月、按年重复
        recurrenceFrequency: calendarManager.RecurrenceFrequency.DAILY,
        // 日程重复次数，该字段和expire属性只需要填写一个，如果两个都填写按照count属性计算。
        count: 10,
        // 重复日程间隔时间，与recurrenceFrequency相关，此示例表示日程每隔2天进行重复。
        interval: 2,
        // 日程过期时间，该字段和count属性只需要填写一个，如果两个都填写按照count属性计算。
        expire: date.getTime() + 60 * 60 * 1000 * 3,
        // 日程排除日期，将该日期从重复日程中排除掉
        excludedDates: [date.getTime() + 60 * 60 * 1000 * 2]
      }
    };

    // 创建日历账户
    this.calendarMgr?.createCalendar(this.calendarAccount).then((calendar: calendarManager.Calendar) => {
      console.info(`Succeeded in creating calendar.`);
      // 添加日程
      calendar.addEvent(event).then((data: number) => {
        console.info(`Succeeded in adding event, id -> ${data}`);
        this.getUIContext().getPromptAction().showToast({ message: '日程添加成功' });
      }).catch((err: BusinessError) => {
        console.error(`Failed to addEvent. Code: ${err.code}, message: ${err.message}`);
      });
    }).catch((error: BusinessError) => {
      console.error(`Failed to create calendar. Code: ${error.code}, message: ${error.message}`);
    });
  }

  requestPermissions() {
    // 需在module.json5文件中配置ohos.permission.WRITE_CALENDAR权限
    const permissions: Permissions[] = ['ohos.permission.WRITE_CALENDAR'];
    let atManager = abilityAccessCtrl.createAtManager();
    atManager.requestPermissionsFromUser(this.context, permissions).then((result: PermissionRequestResult) => {
      console.info(`get Permission success, result: ${JSON.stringify(result)}`);
      for (let i = 0; i < result.permissions.length; i++) {
        if (result.permissions[i] === 'ohos.permission.WRITE_CALENDAR' && result.authResults[i] === 0) {
          this.calendarMgr = calendarManager.getCalendarManager(this.context);
          this.getUIContext().getPromptAction().showToast({ message: '权限申请成功' });
        }
      }
    }).catch((error: BusinessError) => {
      console.error(`get Permission error, error. Code: ${error.code}, message: ${error.message}`);
    });
  }

  build() {
    Column({ space: 20 }) {
      Button('申请写入日历权限')
        .onClick(() => {
          this.requestPermissions();
        });

      Button('添加日程')
        .onClick(() => {
          this.addEvent();
        });
    }
    .justifyContent(FlexAlign.Center)
    .height('100%')
    .width('100%');
  }
}
```
