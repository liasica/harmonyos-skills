---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/calendarmanager-event-developer
title: 日程管理
breadcrumb: 指南 > 应用服务 > Calendar Kit（日历服务） > 日程管理
category: harmonyos-guides
scraped_at: 2026-04-28T07:48:33+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:f5c8a6313f933f6ad0fb0819535146ecd044ed6de8cee8404c09e9a03b956b98
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
| addEvent(event: Event): Promise<number> | 创建日程，入参Event不填日程id，使用Promise异步回调。 |
| editEvent(event: Event): Promise<number> | 通过跳转到日程创建界面创建单个日程，入参Event不填日程id，使用Promise异步回调。 |
| deleteEvent(id: number): Promise<void> | 删除指定日程id的日程，使用Promise异步回调。 |
| updateEvent(event: Event): Promise<void> | 更新日程，使用Promise异步回调。 |
| getEvents(eventFilter?: EventFilter, eventKey?: (keyof Event)[]): Promise<Event[]> | 获取Calendar下符合查询条件的Event，使用Promise异步回调。 |

## 开发步骤

1. 导入相关依赖。

   ```
   1. import { abilityAccessCtrl, AbilityConstant, common, PermissionRequestResult, Permissions, UIAbility, Want } from '@kit.AbilityKit';
   2. import { BusinessError } from '@kit.BasicServicesKit';
   3. import { calendarManager } from '@kit.CalendarKit';
   4. import { window } from '@kit.ArkUI';
   5. import { hilog } from '@kit.PerformanceAnalysisKit';
   ```

   [EntryAbility.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Calendar/CalendarEvent/entry/src/main/ets/entryability/EntryAbility.ets#L16-L22)
2. 申请权限。使用Calendar Kit时，需要在module.json5中声明申请读写日历日程所需的权限：ohos.permission.READ\_CALENDAR和ohos.permission.WRITE\_CALENDAR。具体指导可见[声明权限](declare-permissions.md)。
3. 根据上下文获取日程管理器对象calendarMgr，用于对日历账户进行相关管理操作。推荐在EntryAbility.ets文件中进行操作。

   ```
   1. const DOMAIN = 0x0000;

   3. export let calendarMgr: calendarManager.CalendarManager | null = null;

   5. export let mContext: common.UIAbilityContext | null = null;

   7. export default class EntryAbility extends UIAbility {
   8. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
   9. hilog.info(DOMAIN, 'testTag', '%{public}s', "Ability onCreate");
   10. }

   12. onDestroy(): void {
   13. hilog.info(DOMAIN, 'testTag', '%{public}s', "Ability onDestroy");
   14. }

   16. onWindowStageCreate(windowStage: window.WindowStage): void {
   17. // Main window is created, set main page for this ability
   18. hilog.info(DOMAIN, 'testTag', '%{public}s', "Ability onWindowStageCreate");
   19. windowStage.loadContent('pages/Index', (err, data) => {
   20. if (err.code) {
   21. hilog.error(DOMAIN, 'testTag', 'Failed to load the content. Cause: %{public}s', JSON.stringify(err));
   22. return;
   23. }
   24. hilog.info(DOMAIN, 'testTag', 'Succeeded in loading the content.');
   25. });
   26. mContext = this.context;
   27. const permissions: Permissions[] = ['ohos.permission.READ_CALENDAR', 'ohos.permission.WRITE_CALENDAR'];
   28. let atManager = abilityAccessCtrl.createAtManager();
   29. atManager.requestPermissionsFromUser(mContext, permissions).then((result: PermissionRequestResult) => {
   30. hilog.info(DOMAIN, 'testTag', 'get Permission success');
   31. calendarMgr = calendarManager.getCalendarManager(mContext);
   32. }).catch((error: BusinessError) => {
   33. hilog.error(DOMAIN, 'testTag', 'get Permission error, Cause: %{public}s', JSON.stringify(error));
   34. })
   35. }

   37. onWindowStageDestroy(): void {
   38. // Main window is destroyed, release UI related resources
   39. hilog.info(DOMAIN, 'testTag', '%{public}s', "Ability onWindowStageDestroy");
   40. }

   42. onForeground(): void {
   43. // Ability has brought to foreground
   44. hilog.info(DOMAIN, 'testTag', '%{public}s', "Ability onForeground");
   45. }

   47. onBackground(): void {
   48. // Ability has back to background
   49. hilog.info(DOMAIN, 'testTag', '%{public}s', "Ability onBackground");
   50. }
   51. }
   ```

   [EntryAbility.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Calendar/CalendarEvent/entry/src/main/ets/entryability/EntryAbility.ets#L24-L76)
4. 根据日历账户信息创建Calendar对象，用于进行日程管理。设置日历配置信息，可以根据需要打开日程提醒、设置日历账户颜色。

   ```
   1. import { BusinessError } from '@kit.BasicServicesKit';
   2. import { calendarMgr } from '../entryability/EntryAbility';
   3. import { calendarManager } from '@kit.CalendarKit';
   4. import { hilog } from '@kit.PerformanceAnalysisKit';

   6. const DOMAIN = 0x0000;

   8. let calendar: calendarManager.Calendar | undefined = undefined;
   9. // 指定日历账户信息
   10. const calendarAccount: calendarManager.CalendarAccount = {
   11. name: 'MyCalendar',
   12. type: calendarManager.CalendarType.LOCAL,
   13. // 日历账户显示名称，该字段如果不填，创建的日历账户在界面显示为空字符串。
   14. displayName: 'MyCalendar'
   15. };
   16. // 日历配置信息
   17. const config: calendarManager.CalendarConfig = {
   18. // 打开日程提醒
   19. enableReminder: true,
   20. // 设置日历账户颜色
   21. color: '#aabbcc'
   22. };
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Calendar/CalendarEvent/entry/src/main/ets/pages/Index.ets#L16-L39)

   ```
   1. // 创建日历账户
   2. calendarMgr?.createCalendar(calendarAccount).then((data: calendarManager.Calendar) => {
   3. hilog.info(DOMAIN, 'testTag', `Succeeded in creating calendar data->${JSON.stringify(data)}`);
   4. calendar = data;
   5. // 请确保日历账户创建成功后，再进行相关日程的管理

   7. // 设置日历配置信息，打开日程提醒、设置日历账户颜色
   8. calendar.setConfig(config).then(() => {
   9. hilog.info(DOMAIN, 'testTag', `Succeeded in setting config, data->${JSON.stringify(config)}`);
   10. }).catch((err: BusinessError) => {
   11. hilog.error(DOMAIN, 'testTag', `Failed to set config. Code: ${err.code}, message: ${err.message}`);
   12. });
   13. // ...
   14. }).catch((error: BusinessError) => {
   15. hilog.error(DOMAIN, 'testTag', `Failed to create calendar. Code: ${error.code}, message: ${error.message}`);
   16. });
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Calendar/CalendarEvent/entry/src/main/ets/pages/Index.ets#L117-L134)
5. 在当前日历账户下添加日历日程，注意入参中不需要填写日程id。

   创建日程时，支持设置日程的标题、开始时间、结束时间、日程类型、日程地点、日程提醒时间、日程重复规则等相关信息。

   日程创建成功后会返回一个日程id，作为日程的唯一标识，后续可按照日程id进行指定日程的更新或删除。

   目前支持以下两种方式来创建日程。

   方式一：可以在日历账户下通过addEvent()或addEvents()接口创建日程。其中可使用addEvent()接口创建单个日程，也可以使用addEvents()接口批量创建日程，此处以创建单个日程为例。

   方式二：在获取到日历管理器对象后，可通过editEvent()接口创建单个日程。调用此接口创建日程时，会跳转到日程创建页面，在日程创建页面进行相关操作完成日程的创建, editEvent()不支持自定义周期性日程创建。

   ```
   1. let eventId : number | undefined = undefined;
   2. const date = new Date();
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Calendar/CalendarEvent/entry/src/main/ets/pages/Index.ets#L41-L44)

   ```
   1. const event: calendarManager.Event = {
   2. // 日程标题
   3. title: 'title',
   4. // 日程类型，不推荐三方开发者使用calendarManager.EventType.IMPORTANT，重要日程类型不支持一键服务跳转功能及无法自定义提醒时间
   5. type: calendarManager.EventType.NORMAL,
   6. // 日程开始时间
   7. startTime: date.getTime(),
   8. // 日程结束时间
   9. endTime: date.getTime() + 60 * 60 * 1000,
   10. // 距开始时间提前10分钟提醒
   11. reminderTime: [10],
   12. // 日程重复规则，可选属性。如果日程为周期性日程需要填写该属性。
   13. recurrenceRule: {
   14. // 日程重复规则类型，支持按天、按周、按月、按年重复
   15. recurrenceFrequency: calendarManager.RecurrenceFrequency.DAILY,
   16. // 日程重复次数，该字段和expire属性只需要填写一个，如果两个都填写按照count属性计算。
   17. count: 100,
   18. // 重复日程间隔时间，与recurrenceFrequency相关，此示例表示日程每隔2天进行重复。
   19. interval: 2,
   20. // 日程过期时间，该字段和count属性只需要填写一个，如果两个都填写按照count属性计算。
   21. expire: date.getTime() + 60 * 60 * 1000 * 3,
   22. // 日程排除日期，将该日期从重复日程中排除掉
   23. excludedDates: [date.getTime() + 60 * 60 * 1000 * 2]
   24. },
   25. // 日程服务，可选字段，需要一键服务功能的日程，填写该属性。
   26. service: {
   27. // 服务类型，比如一键查看、一键入会、一键追剧等。
   28. type: calendarManager.ServiceType.TRIP,
   29. // 服务的uri。可以跳转到三方应用相应界面，格式为DeepLink。使用DeepLink方式需要在华为HAG云侧进行注册，注册提供的信息为应用包名、应用的服务类型。
   30. // DeepLink包括scheme、host、path以及参数（不包含参数值）
   31. uri: 'xxx://xxx.xxx.com/xxx',
   32. // 服务辅助描述信息，可选字段
   33. description: '一键服务'
   34. }

   36. };
   37. // 方式一
   38. calendar.addEvent(event).then((data: number) => {
   39. hilog.info(DOMAIN, 'testTag', `Succeeded in adding event, id -> ${data}`);
   40. eventId = data;
   41. }).catch((err: BusinessError) => {
   42. hilog.error(DOMAIN, 'testTag', `Failed to addEvent. Code: ${err.code}, message: ${err.message}`);
   43. });
   44. // 方式二
   45. const eventInfo: calendarManager.Event = {
   46. // 日程标题
   47. title: 'title',
   48. // 日程类型
   49. type: calendarManager.EventType.NORMAL,
   50. // 日程开始时间
   51. startTime: date.getTime(),
   52. // 日程结束时间
   53. endTime: date.getTime() + 60 * 60 * 1000
   54. };
   55. calendarMgr?.editEvent(eventInfo).then((id: number): void => {
   56. hilog.info(DOMAIN, 'testTag', `create Event id = ${id}`);
   57. }).catch((err: BusinessError) => {
   58. hilog.error(DOMAIN, 'testTag', `Failed to create Event. Code: ${err.code}, message: ${err.message}`);
   59. });
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Calendar/CalendarEvent/entry/src/main/ets/pages/Index.ets#L145-L205)
6. 按照日程id进行指定日程的更新，更新日程相关信息。

   ```
   1. const updateEvent: calendarManager.Event = {
   2. title: 'updateTitle',
   3. description: 'updateEventTest',
   4. type: calendarManager.EventType.NORMAL,
   5. id: eventId,
   6. startTime: date.getTime(),
   7. endTime: date.getTime() + 60 * 60 * 1000
   8. };
   9. calendar.updateEvent(updateEvent).then(() => {
   10. hilog.info(DOMAIN, 'testTag', `Succeeded in updating event`);
   11. }).catch((err: BusinessError) => {
   12. hilog.error(DOMAIN, 'testTag', `Failed to update event. Code: ${err.code}, message: ${err.message}`);
   13. });
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Calendar/CalendarEvent/entry/src/main/ets/pages/Index.ets#L214-L228)
7. 查询当前日历账户下的所有日程。由于涉及数据隐私安全，进行了权限管控的应用无法获取其他创建的日程信息。根据不同的查询条件和查询字段，返回不同的查询结果。

   当没有查询条件和查询字段时，可查询指定日历账户下的所有日程。

   ```
   1. calendar.getEvents().then((data: calendarManager.Event[]) => {
   2. hilog.info(DOMAIN, 'testTag', `Succeeded in getting events, data -> ${JSON.stringify(data)}`);
   3. }).catch((err: BusinessError) => {
   4. hilog.error(DOMAIN, 'testTag', `Failed to get events. Code: ${err.code}, message: ${err.message}`);
   5. });
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Calendar/CalendarEvent/entry/src/main/ets/pages/Index.ets#L236-L242)

   还支持根据日程id、日程开始和结束时间、日程标题等查询条件来查询日程。

   ```
   1. // 根据日程id查询
   2. const filterId = calendarManager.EventFilter.filterById([eventId]);
   3. calendar.getEvents(filterId).then((data: calendarManager.Event[]) => {
   4. hilog.info(DOMAIN, 'testTag', `Succeeded in getting events filter by eventId, data -> ${JSON.stringify(data)}`);
   5. }).catch((err: BusinessError) => {
   6. hilog.error(DOMAIN, 'testTag', `Failed to get events. Code: ${err.code}, message: ${err.message}`);
   7. });

   9. // 根据日程标题查询
   10. const filterTitle = calendarManager.EventFilter.filterByTitle('update');
   11. calendar.getEvents(filterTitle).then((data: calendarManager.Event[]) => {
   12. hilog.info(DOMAIN, 'testTag', `Succeeded in getting events filter by title, data -> ${JSON.stringify(data)}`);
   13. }).catch((err: BusinessError) => {
   14. hilog.error(DOMAIN, 'testTag', `Failed to get events. Code: ${err.code}, message: ${err.message}`);
   15. });

   17. // 根据日程开始和结束时间查询
   18. const filterTime = calendarManager.EventFilter.filterByTime(1686931200000, 1687017600000);
   19. calendar.getEvents(filterTime).then((data: calendarManager.Event[]) => {
   20. hilog.info(DOMAIN, 'testTag', `Succeeded in getting events filter by time, data -> ${JSON.stringify(data)}`);
   21. }).catch((err: BusinessError) => {
   22. hilog.error(DOMAIN, 'testTag', `Failed to filter by time. Code: ${err.code}, message: ${err.message}`);
   23. });
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Calendar/CalendarEvent/entry/src/main/ets/pages/Index.ets#L251-L275)
8. 按照日程id进行指定日程的删除。可以通过deleteEvent()接口进行单个日程的删除，也可以通过deleteEvents()接口批量删除指定日程，此处以删除单个指定日程为例。

   ```
   1. calendar.deleteEvent(eventId).then(() => {
   2. hilog.info(DOMAIN, 'testTag', "Succeeded in deleting event");
   3. }).catch((err: BusinessError) => {
   4. hilog.error(DOMAIN, 'testTag', `Failed to delete event. Code: ${err.code}, message: ${err.message}`);
   5. });
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Calendar/CalendarEvent/entry/src/main/ets/pages/Index.ets#L283-L289)
