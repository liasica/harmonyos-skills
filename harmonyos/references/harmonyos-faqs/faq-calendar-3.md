---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faq-calendar-3
title: HarmonyOS下如何通过Calendar Kit实现日程提醒功能
breadcrumb: FAQ > 应用服务开发 > 日历服务（Calendar Kit） > HarmonyOS下如何通过Calendar Kit实现日程提醒功能
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:49+08:00
doc_updated_at: 2026-07-30
content_hash: sha256:8291d7df7b2e4b6322d6ccd75530b9bc0574aec61dcdac73d0aab75fc6711cdf
---

## 问题现象

后台任务的代理提醒功能在实现上有很多限制，如何使用日历[Calendar Kit](../harmonyos-guides/calendarmanager-overview.md)的日程提醒实现类似功能？

## 背景知识

后台任务的代理提醒有[严格的约束限制](../harmonyos-guides/agent-powered-reminder.md#约束与限制)，且对权限（需要邮件申请权限）和场景（只有工具类应用才能申请）有要求，对绝大部分应用来说不是一个好的选择，建议使用日历[Calendar Kit](../harmonyos-guides/calendarmanager-overview.md)替代代理提醒，以日程提醒方案实现类似功能。

## 解决方案

日程提醒实现步骤：

1. 权限声明，module.json5中配置权限声明：

   获取写日历使用权限：[ohos.permission.WRITE\_CALENDAR](../harmonyos-guides/permissions-for-all-user.md#ohospermissionwrite_calendar)。

   获取读日历使用权限：[ohos.permission.READ\_CALENDAR](../harmonyos-guides/permissions-for-all-user.md#ohospermissionread_calendar)。
2. 日程提醒创建完整代码：

   ```ts
   import { BusinessError } from '@kit.BasicServicesKit';
   import { calendarManager } from '@kit.CalendarKit';
   import { abilityAccessCtrl, common, PermissionRequestResult, Permissions } from '@kit.AbilityKit';

   @Entry
   @Component
   struct Index {
     @State calendar: calendarManager.Calendar | undefined = undefined;
     @State calendarMgr: calendarManager.CalendarManager | null = null;
     private queryCalendarByAccount: string = 'QueryCalendarByAccount';
     private addCalendarEvent: string = 'AddCalendarEvent';
     private queryCalendarEvents: string = 'QueryCalendarEvents';
     private conditionalQueryCalendarEvents: string = 'ConditionalQueryCalendarEvents';
     private deleteCalendarEvents: string = 'DeleteCalendarEvent';
     private updateCalendarEvents: string = 'UpdateCalendarEvent';
     // 1.配置日历账户信息
     private calendarAccount: calendarManager.CalendarAccount = {
       // 日历账户名称（面向开发者）
       name: 'HarmonyOSCalendar',
       // 日历账户类型（LOCAL，本地账号；EMAIL，邮箱账号；BIRTHDAY，生日账号；BIRTHDAY，支持CalDAV协议账户；SUBSCRIBED，订阅账户）
       type: calendarManager.CalendarType.LOCAL,
       // 日历账户显示名称，该字段如果不填，创建的日历账户在界面显示为空字符串。
       displayName: 'MyCalendar'
     };
     // 2.配置日历配置信息
     private calendarConfig: calendarManager.CalendarConfig = {
       // 是否打开Calendar下所有Event提醒能力
       enableReminder: true,
       // 设置日历账户颜色
       color: '#aabbcc'
     };
     async requestPermission() {
       let context = this.getUIContext()?.getHostContext() as common.UIAbilityContext;
       let atManager = abilityAccessCtrl.createAtManager();
       const permissions: Permissions[] = ['ohos.permission.READ_CALENDAR', 'ohos.permission.WRITE_CALENDAR'];
       try {
         let result: PermissionRequestResult = await atManager.requestPermissionsFromUser(context, permissions);
         console.info(`get Permission success, result: ${JSON.stringify(result)}`);
         let isPermitted: boolean = true;
         for (let element of result.authResults) {
           if (element !== 0) {
             isPermitted = false;
             break;
           }
         }
         if (isPermitted) {
           // 有权限，获取日历管理对象
           this.calendarMgr = calendarManager.getCalendarManager(context);
           console.info(`get CalendarManager success.`);
         } else {
           // 没有权限，无法获取日历管理对象
           console.error(`Get Permissions failed.`);
         }
       } catch (error) {
         console.error(`get Permission error, error. Code: ${error.code}, message: ${error.message}`);
       }
     }
     async aboutToAppear(): Promise<void> {
       await this.requestPermission();
       // 3.创建日历账户
       this.calendarMgr?.createCalendar(this.calendarAccount).then((data: calendarManager.Calendar) => {
         console.info(`Succeeded in creating calendar data->${JSON.stringify(data)}`);
         this.calendar = data;
         // 设置日历配置信息
         this.calendar.setConfig(this.calendarConfig).then(() => {
           console.info(`Succeeded in setting config, data->${JSON.stringify(this.calendarConfig)}`);
         }).catch((err: BusinessError) => {
           console.error(`Failed to set config. Code: ${err.code}, message: ${err.message}`);
         });
       }).catch((error: BusinessError) => {
         console.error(`Failed to create calendar. Code: ${error.code}, message: ${error.message}`);
       });
     }

     build() {
       Column() {
         Button() {
           Text(this.queryCalendarByAccount).fontSize(30)
         }
         .onClick(() => { // 查询日历账号信息
           this.calendarMgr?.getCalendar(this.calendarAccount).then((data: calendarManager.Calendar) => {
             console.info(`Succeeded in getting calendar, data -> ${JSON.stringify(data)}`);
           }).catch((err: BusinessError) => {
             console.error(`Failed to get calendar. Code: ${err.code}, message: ${err.message}`);
           });
         });

         Button() {
           Text(this.addCalendarEvent).fontSize(30)
         }
         .onClick(() => { // 添加日历提醒信息
           const date = new Date();

           // 日历提醒信息，可根据需要自定义配置
           const event: calendarManager.Event = {
             // 日程标题
             title: '我的日历',
             // 日程类型，不推荐三方开发者使用calendarManager.EventType.IMPORTANT，重要日程类型不支持一键服务跳转功能及无法自定义提醒时间
             type: calendarManager.EventType.NORMAL,
             // 日程开始时间
             startTime: date.getTime(),
             // 日程结束时间
             endTime: date.getTime() + 60 * 60 * 1000,
             // 距开始时间提前10分钟提醒
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
             },
             // 日程服务，可选字段，需要一键服务功能的日程，填写该属性。
             service: {
               // 服务类型，比如一键查看、一键入会、一键追剧等。
               type: calendarManager.ServiceType.TRIP,
               // 服务的uri。可以跳转到三方应用相应界面，格式为deeplink。使用deeplink方式需要在华为HAG云侧进行注册，注册提供的信息为应用包名、应用的服务类型。
               // deeplink包括scheme、host、path以及参数（不包含参数值）
               uri: 'weixin://',
               // 服务辅助描述信息，可选字段
               description: '一键服务'
             }
           };

           this.calendar?.addEvent(event).then((data: number) => { // 日历提醒添加成功
             console.info(`Succeeded in adding event, id -> ${data}`);
           }).catch((err: BusinessError) => { // 日历提醒添加失败
             console.error(`Failed to addEvent. Code: ${err.code}, message: ${err.message}`);
           });
         })

         Button() {
           Text(this.queryCalendarEvents).fontSize(30)
         }
         .onClick(() => { // 查询日历提醒信息
           this.calendar?.getEvents().then((data: calendarManager.Event[]) => {
             console.info(`Succeeded in getting events, data -> ${JSON.stringify(data)}`);
           }).catch((err: BusinessError) => { // 查询日历提醒失败
             console.error(`Failed to get events. Code: ${err.code}, message: ${err.message}`);

           });
         });

         Button() {
           Text(this.conditionalQueryCalendarEvents).fontSize(30)
         }
         .onClick(() => { // 条件查询日历提醒信息，可根据title（模糊查询），startTime和endTime以及id进行条件查询
           const filter = calendarManager.EventFilter.filterByTitle('我');
           this.calendar?.getEvents(filter).then((data: calendarManager.Event[]) => {
             console.info(`Succeeded in getting events, data -> ${JSON.stringify(data)}`);
           }).catch((err: BusinessError) => { // 查询日历提醒失败
             console.error(`Failed to get events. Code: ${err.code}, message: ${err.message}`);
           });
         });

         Button() {
           Text(this.deleteCalendarEvents).fontSize(30)
         }
         .onClick(() => { // 删除日历提醒信息
           this.calendar?.getEvents().then((data: calendarManager.Event[]) => {
             if (data.length === 0) { // 如果没有日历提醒，返回
               return;
             }
             // 如果有多个日历提醒内容，删除第一个
             this.calendar?.deleteEvent(data[0].id, (err: BusinessError) => {
               if (err) {
                 console.error(`Failed to delete event. Code: ${err.code}, message: ${err.message}`);
               } else {
                 console.info(`Succeeded in deleting event, ${JSON.stringify(data[0])}`);
               }
             });
           }).catch((err: BusinessError) => {
             console.error(`Failed to get events. Code: ${err.code}, message: ${err.message}`);
           });
         });

         Button() {
           Text(this.updateCalendarEvents).fontSize(30)
         }
         .onClick(() => { // 更新日历提醒信息
           this.calendar?.getEvents().then((data: calendarManager.Event[]) => {
             if (data.length === 0) { // 如果没有日历提醒，返回
               return;
             }
             let newEvent = data[0];
             newEvent.title = 'MyEvent';
             // 如果有多个日历提醒内容，更新第一个
             this.calendar?.updateEvent(newEvent, (err: BusinessError) => {
               if (err) {
                 console.error(`Failed to update event. Code: ${err.code}, message: ${err.message}`);
               } else {
                 console.info(`Succeeded in updating event, ${JSON.stringify(data[0])}`);
               }
             });
           }).catch((err: BusinessError) => {
             console.error(`Failed to get events. Code: ${err.code}, message: ${err.message}`);
           });
         });
       }
       .justifyContent(FlexAlign.SpaceAround)
       .height('100%')
       .width('100%')
     }
   }
   ```

## 总结

使用[Calendar Kit](../harmonyos-guides/calendarmanager-overview.md)实现日程提醒简单步骤：

1. 配置权限：module.json5文件中配置日历的读写权限；
2. 在使用前获取用户授权；获取权限后获取日历管理类；
3. 设置日历账户信息和配置信息，并创建日历对象（参见Index.ets中的aboutToAppear()方法）；
4. 根据需要新增、删除、更新、查找日历事件。

## 常见FAQ

Q：CalendarConfig中将enableReminder值设置为true，但日历仍然没有提醒功能，是否还需要打开其他配置？

A：创建[Event](../harmonyos-references/js-apis-calendarmanager.md#event)日程对象时，需要指定reminderTime参数表示日程提醒时间，单位为分钟。填写x分钟，即距开始时间提前x分钟提醒，不填时，默认为不提醒。

Q：应用设置了日历提醒，日历中也能查看到该日历提醒，到提醒时间，为什么没有push推送日历提醒？

A：参考[Calendar Kit（日历服务）](../harmonyos-references/calendar-api.md)中的日程对象[Event](../harmonyos-references/js-apis-calendarmanager.md#event)参数：reminderTime（日程提醒时间，单位为分钟），当未填写该参数时，默认为不提醒。需要在应用创建日程提醒时，添加该参数信息即可。

Q：应用设置了日历提醒，enableReminder值设置为true，也设置了reminderTime，日历中也能查看到该日历提醒，但是到提醒时间，为什么没有弹出日历提醒？

A：不满足日历提醒设计规格导致的，需要设置秒数+毫秒数都是0的时候才能提醒。其他时候不触发提醒。例：12:01:00:000.

Q：[Calendar.getEvents](../harmonyos-references/js-apis-calendarmanager.md#getevents)返回值没有[RecurrenceRule](../harmonyos-references/js-apis-calendarmanager.md#recurrencerule)字段？

A：getEvent在不设置[查询字段](../harmonyos-references/js-apis-calendarmanager.md#getevents-2)时仅返回默认字段（id、startTime、endTime、location、type、isAllDay、timeZone、reminderTime、description），如需要返回RecurrenceRule需要在参数中配置[查询字段](../harmonyos-references/js-apis-calendarmanager.md#getevents-2)。

Q：日历权限需要开启ACL吗？

A：读写日历属于normal级别的普通权限，不需要进行ACL使能的操作。

Q：calendar.addEvent是否支持自定义id？

A：目前不支持日程id自定义。

Q：使用[Calendar.getEvents](../harmonyos-references/js-apis-calendarmanager.md#getevents)查询日程信息未返回identifier信息是为什么？

A：getEvents默认查询identifier信息需要使用API 20设备，API 20版本之前不会查询此字段，建议使用[getEvents](../harmonyos-references/js-apis-calendarmanager.md#getevents-1)添加eventKey查询identifier字段。

Q：使用addEvent接口向日历账户添加日程后，打开系统日历，对该日程进行修改，如：修改标题、时间、重复规则等。查询日历时带上RecurrenceRule参数，无法返回结果，是什么原因？

A：添加日历日程时[RecurrenceFrequency](../harmonyos-references/js-apis-calendarmanager.md#recurrencefrequency)未使用规定的字段，如：calendarManager.RecurrenceFrequency.MONTHLY，而是传入该字段对应的数字"1"，导致写入的日程的信息不对从而查询失败。

Q：getEvent接口查询日程信息时，eventKey中携带'instanceStartTime'或'instanceEndTime'后，getEvent回调结果返回的是空数组，是什么原因？

A：查询日程信息接口使用不对导致，查询重复日程使用[queryEventInstances](../harmonyos-references/js-apis-calendarmanager.md#queryeventinstances18)接口。
