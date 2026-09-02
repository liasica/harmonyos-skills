---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/calendarmanager-event-developer
title: 日程管理
breadcrumb: 指南 > 应用服务 > Calendar Kit（日历服务） > 日程管理
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:24+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:e56d961de7ee261f27aa695f69762a3b681933aae034d3db890e757cea9b731b
---

日程指特定的事件或者活动安排，日程管理即对这些事件、活动进行规划和控制，能更有效地利用相关资源、提高生产力和效率，使人们更好地管理时间和任务。

Calendar Kit中的日程[Event](../harmonyos-references/js-apis-calendarmanager.md#event)归属于某个对应的日历账户[Calendar](../harmonyos-references/js-apis-calendarmanager.md#calendar)，一个日历账户下可以有多个日程，一个日程只属于一个Calendar。

获取到日历账户对象之后，即可对该账户下的日程进行管理，包括日程的创建、删除、修改、查询等操作。在创建、修改日程时，支持对日程的标题、开始时间、结束时间、日程类型、日程地点、日程提醒时间、日程重复规则等相关信息进行设置，以便进行更丰富更有效的日程管理。

## 接口说明

以下是日程管理的相关接口，更多详细接口及使用请参考[@ohos.calendarManager](../harmonyos-references/js-apis-calendarmanager.md)。

| 接口名称 | 描述 |
| --- | --- |
| getCalendarManager(context: Context): CalendarManager | 根据上下文获取CalendarManager对象，用于管理日历。 |
| createCalendar(calendarAccount: CalendarAccount): Promise<Calendar> | 根据日历账户信息，创建一个Calendar对象，使用Promise异步回调。 |
| addEvent(event: Event): Promise<number> | 创建日程，入参Event不填日程id、instanceStartTime和instanceEndTime，使用Promise异步回调。 |
| editEvent(event: Event): Promise<number> | 通过跳转到日程创建界面创建单个日程，入参Event不填日程id，不支持设置instanceStartTime、instanceEndTime、identifier、attendee、service、isLunar和timeZone属性，使用Promise异步回调。 |
| deleteEvent(id: number): Promise<void> | 删除指定日程id的日程，使用Promise异步回调。 |
| updateEvent(event: Event): Promise<void> | 更新日程，入参Event需要填写被修改日程的id，使用Promise异步回调。 |
| getEvents(eventFilter?: EventFilter, eventKey?: (keyof Event)[]): Promise<Event[]> | 获取Calendar下符合查询条件的Event，使用Promise异步回调。 |

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
3. 根据上下文获取日程管理器对象calendarMgr，用于对日历账户进行相关管理操作。推荐在EntryAbility.ets文件中进行操作。

   ```typescript
   export let calendarMgr: calendarManager.CalendarManager | null = null;

   export let mContext: common.UIAbilityContext | null = null;

   export default class EntryAbility extends UIAbility {
     onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
       console.info('%{public}s', 'Ability onCreate');
     }

     onDestroy(): void {
       console.info('%{public}s', 'Ability onDestroy');
     }

     onWindowStageCreate(windowStage: window.WindowStage): void {
       // 主窗口已创建，请为此Ability设置主页
       console.info('%{public}s', 'Ability onWindowStageCreate');
       windowStage.loadContent('pages/Index', (err, data) => {
         if (err.code) {
           console.error('Failed to load the content. Cause: %{public}s', JSON.stringify(err));
           return;
         }
         console.info('Succeeded in loading the content.');
       });
       mContext = this.context;
       const permissions: Permissions[] = ['ohos.permission.READ_CALENDAR', 'ohos.permission.WRITE_CALENDAR'];
       let atManager = abilityAccessCtrl.createAtManager();
       atManager.requestPermissionsFromUser(mContext, permissions).then((result: PermissionRequestResult) => {
         console.info('get Permission success');
         calendarMgr = calendarManager.getCalendarManager(mContext);
       }).catch((error: BusinessError) => {
         console.error('get Permission error, Cause: %{public}s', JSON.stringify(error));
       })
     }

     onWindowStageDestroy(): void {
       // 主窗口已销毁，释放 UI 相关资源
       console.info('%{public}s', 'Ability onWindowStageDestroy');
     }

     onForeground(): void {
       // Ability 进入前台
       console.info('%{public}s', 'Ability onForeground');
     }

     onBackground(): void {
       // Ability 进入后台
       console.info('%{public}s', 'Ability onBackground');
     }
   }
   ```
4. 根据日历账户信息创建Calendar对象，用于进行日程管理。设置日历配置信息，可以根据需要打开日程提醒、设置日历账户颜色。

   ```typescript
   import { BusinessError } from '@kit.BasicServicesKit';
   import { calendarMgr } from '../entryability/EntryAbility';
   import { calendarManager } from '@kit.CalendarKit';

   let calendar: calendarManager.Calendar | undefined = undefined;
   // 指定日历账户信息
   const calendarAccount: calendarManager.CalendarAccount = {
     name: 'MyCalendar',
     type: calendarManager.CalendarType.LOCAL,
     // 日历账户显示名称，该字段如果不填，创建的日历账户在界面显示为空字符串。
     displayName: 'MyCalendar'
   };
   // 日历配置信息
   const config: calendarManager.CalendarConfig = {
     // 打开日程提醒
     enableReminder: true,
     // 设置日历账户颜色
     color: '#aabbcc'
   };
   ```

   ```typescript
   // 创建日历账户
   calendarMgr?.createCalendar(calendarAccount).then((data: calendarManager.Calendar) => {
     console.info(`Succeeded in creating calendar data->${JSON.stringify(data)}`);
     calendar = data;
     // 请确保日历账户创建成功后，再进行相关日程的管理

     // 设置日历配置信息，打开日程提醒、设置日历账户颜色
     calendar.setConfig(config).then(() => {
       console.info(`Succeeded in setting config, data->${JSON.stringify(config)}`);
     }).catch((err: BusinessError) => {
       console.error(`Failed to set config. Code: ${err.code}, message: ${err.message}`);
     });
     // ...
   }).catch((error: BusinessError) => {
     console.error(`Failed to create calendar. Code: ${error.code}, message: ${error.message}`);
   });
   ```
5. 在当前日历账户下添加日历日程，注意入参中不需要填写日程id。

   创建日程时，支持设置日程的标题、开始时间、结束时间、日程类型、日程地点、日程提醒时间、日程重复规则等相关信息。

   日程创建成功后会返回一个日程id，作为日程的唯一标识，后续可按照日程id进行指定日程的更新或删除。

   目前支持以下两种方式来创建日程。

   方式一：可以在日历账户下通过addEvent()或addEvents()接口创建日程。其中可使用addEvent()接口创建单个日程，也可以使用addEvents()接口批量创建日程，此处以创建单个日程为例。

   方式二：在获取到日历管理器对象后，可通过editEvent()接口创建单个日程。调用此接口创建日程时，会跳转到日程创建页面，在日程创建页面进行相关操作完成日程的创建，editEvent()不支持自定义周期性日程创建。

   ```typescript
   let eventId : number | undefined = undefined;
   const date = new Date();
   ```

   ```typescript
   const event: calendarManager.Event = {
     // 日程标题
     title: 'title',
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
       count: 100,
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
       // 服务的uri。可以跳转到三方应用相应界面，格式为DeepLink。使用DeepLink方式需要在华为HAG云侧进行注册，注册提供的信息为应用包名、应用的服务类型。
       // DeepLink包括scheme、host、path以及参数（不包含参数值）
       uri: 'xxx://xxx.xxx.com/xxx',
       // 服务辅助描述信息，可选字段
       description: '一键服务'
     }

   };
   // 方式一
   calendar.addEvent(event).then((data: number) => {
     console.info(`Succeeded in adding event, id -> ${data}`);
     eventId = data;
   }).catch((err: BusinessError) => {
     console.error(`Failed to addEvent. Code: ${err.code}, message: ${err.message}`);
   });
   // 方式二
   const eventInfo: calendarManager.Event = {
     // 日程标题
     title: 'title',
     // 日程类型
     type: calendarManager.EventType.NORMAL,
     // 日程开始时间
     startTime: date.getTime(),
     // 日程结束时间
     endTime: date.getTime() + 60 * 60 * 1000
   };
   calendarMgr?.editEvent(eventInfo).then((id: number): void => {
     console.info(`create Event id = ${id}`);
   }).catch((err: BusinessError) => {
     console.error(`Failed to create Event. Code: ${err.code}, message: ${err.message}`);
   });
   ```
6. 按照日程id进行指定日程的更新，更新日程相关信息。

   ```typescript
   const updateEvent: calendarManager.Event = {
     title: 'updateTitle',
     description: 'updateEventTest',
     type: calendarManager.EventType.NORMAL,
     id: eventId,
     startTime: date.getTime(),
     endTime: date.getTime() + 60 * 60 * 1000
   };
   calendar.updateEvent(updateEvent).then(() => {
     console.info(`Succeeded in updating event`);
   }).catch((err: BusinessError) => {
     console.error(`Failed to update event. Code: ${err.code}, message: ${err.message}`);
   });
   ```
7. 查询当前日历账户下的所有日程。由于涉及数据隐私安全，进行了权限管控的应用无法获取其他创建的日程信息。根据不同的查询条件和查询字段，返回不同的查询结果。

   当没有查询条件和查询字段时，可查询指定日历账户下的所有日程。

   ```typescript
   calendar.getEvents().then((data: calendarManager.Event[]) => {
     console.info(`Succeeded in getting events, data -> ${JSON.stringify(data)}`);
   }).catch((err: BusinessError) => {
     console.error(`Failed to get events. Code: ${err.code}, message: ${err.message}`);
   });
   ```

   还支持根据日程id、日程开始和结束时间、日程标题等查询条件来查询日程。

   ```typescript
   // 根据日程id查询
   const filterId = calendarManager.EventFilter.filterById([eventId]);
   calendar.getEvents(filterId).then((data: calendarManager.Event[]) => {
     console.info(`Succeeded in getting events filter by eventId, data -> ${JSON.stringify(data)}`);
   }).catch((err: BusinessError) => {
     console.error(`Failed to get events. Code: ${err.code}, message: ${err.message}`);
   });

   // 根据日程标题查询
   const filterTitle = calendarManager.EventFilter.filterByTitle('update');
   calendar.getEvents(filterTitle).then((data: calendarManager.Event[]) => {
     console.info(`Succeeded in getting events filter by title, data -> ${JSON.stringify(data)}`);
   }).catch((err: BusinessError) => {
     console.error(`Failed to get events. Code: ${err.code}, message: ${err.message}`);
   });

   // 根据日程开始和结束时间查询
   const filterTime = calendarManager.EventFilter.filterByTime(1686931200000, 1687017600000);
   calendar.getEvents(filterTime).then((data: calendarManager.Event[]) => {
     console.info(`Succeeded in getting events filter by time, data -> ${JSON.stringify(data)}`);
   }).catch((err: BusinessError) => {
     console.error(`Failed to filter by time. Code: ${err.code}, message: ${err.message}`);
   });
   ```
8. 按照日程id进行指定日程的删除。可以通过deleteEvent()接口进行单个日程的删除，也可以通过deleteEvents()接口批量删除指定日程，此处以删除单个指定日程为例。

   ```typescript
   calendar.deleteEvent(eventId).then(() => {
     console.info('Succeeded in deleting event');
   }).catch((err: BusinessError) => {
     console.error(`Failed to delete event. Code: ${err.code}, message: ${err.message}`);
   });
   ```
