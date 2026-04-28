---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/calendarmanager-calendar-developer
title: 日历账户管理
breadcrumb: 指南 > 应用服务 > Calendar Kit（日历服务） > 日历账户管理
category: harmonyos-guides
scraped_at: 2026-04-28T07:48:33+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:a9b6865ba0ef9c5794b1099b5c1133b6c65f7a7a282e2a936b6a43179d741028
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

   ```
   1. import { abilityAccessCtrl, AbilityConstant, common, PermissionRequestResult, Permissions, UIAbility, Want } from '@kit.AbilityKit';
   2. import { BusinessError } from '@kit.BasicServicesKit';
   3. import { calendarManager } from '@kit.CalendarKit';
   4. import { window } from '@kit.ArkUI';
   5. import { hilog } from '@kit.PerformanceAnalysisKit';
   ```

   [EntryAbility.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Calendar/CalendarManager/entry/src/main/ets/entryability/EntryAbility.ets#L16-L22)
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

   [EntryAbility.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Calendar/CalendarManager/entry/src/main/ets/entryability/EntryAbility.ets#L25-L77)
4. 根据日历账户信息，创建一个日历账户Calendar对象。

   创建日历账户之前，开发者需要先根据账户信息进行查询，如果账户不存在则抛出异常信息，捕获到异常再进行日历账户的创建，否则可能会出现账户重复创建的问题。

   ```
   1. import { BusinessError } from '@kit.BasicServicesKit';
   2. import { calendarMgr } from '../entryability/EntryAbility';
   3. import { calendarManager } from '@kit.CalendarKit';
   4. import { hilog } from '@kit.PerformanceAnalysisKit';

   6. const DOMAIN = 0x0000;

   8. let calendar: calendarManager.Calendar | undefined = undefined;
   9. // 指定日历账户信息
   10. const calendarAccount: calendarManager.CalendarAccount = {
   11. // 日历账户名称
   12. name: 'MyCalendar',
   13. // 日历账户类型
   14. type: calendarManager.CalendarType.LOCAL,
   15. // 日历账户显示名称，该字段如果不填，创建的日历账户在界面显示为空字符串。
   16. displayName: 'MyCalendar'
   17. };
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Calendar/CalendarManager/entry/src/main/ets/pages/Index.ets#L16-L34)

   ```
   1. // 创建日历账户
   2. calendarMgr?.createCalendar(calendarAccount).then((data: calendarManager.Calendar) => {
   3. hilog.info(DOMAIN, 'testTag', '%{public}s', `Succeeded in creating calendar data->${JSON.stringify(data)}`);
   4. calendar = data;
   5. // 请确保日历账户创建成功后，再进行后续相关操作
   6. // ...
   7. }).catch((error: BusinessError) => {
   8. hilog.error(DOMAIN, 'testTag', `Failed to create calendar. Code: ${error.code}, message: ${error.message}`);
   9. });
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Calendar/CalendarManager/entry/src/main/ets/pages/Index.ets#L112-L122)
5. 日历账户创建之后，日历账户颜色默认为黑色，不指定日历账户颜色可能导致部分版本/设备深色模式下显示效果不佳。开发者需要调用setConfig()接口设置日历配置信息，包括是否打开日历账户下的日程提醒能力、设置日历账户颜色。

   ```
   1. const calendarAccounts: calendarManager.CalendarAccount = {
   2. name: 'MyCalendar',
   3. type: calendarManager.CalendarType.LOCAL,
   4. displayName: 'MyCalendar'
   5. };
   6. // 日历配置信息
   7. calendarMgr?.getCalendar(calendarAccounts, (err, data) => {
   8. //获取日历账户
   9. if (err) {
   10. hilog.error(DOMAIN, 'testTag', `Failed to get calendar, Code is ${err.code}, message is ${err.message}`);
   11. } else {
   12. const config: calendarManager.CalendarConfig = {
   13. // 打开日程提醒
   14. enableReminder: true,
   15. // 设置日历账户颜色
   16. color: '#aabbcc'
   17. };
   18. // 设置日历配置信息
   19. data.setConfig(config).then(() => {
   20. hilog.info(DOMAIN, 'testTag', '%{public}s', `Succeeded in setting config, data->${JSON.stringify(config)}`);
   21. }).catch((err: BusinessError) => {
   22. hilog.error(DOMAIN, 'testTag', `Failed to set config. Code: ${err.code}, message: ${err.message}`);
   23. })
   24. }
   25. });
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Calendar/CalendarManager/entry/src/main/ets/pages/Index.ets#L127-L153)
6. 可以查询指定日历账户。

   ```
   1. calendarMgr?.getCalendar(calendarAccount).then((data: calendarManager.Calendar) => {
   2. hilog.info(DOMAIN, 'testTag', '%{public}s', `Succeeded in getting calendar, data -> ${JSON.stringify(data)}`);
   3. }).catch((err: BusinessError) => {
   4. hilog.error(DOMAIN, 'testTag', `Failed to get calendar. Code: ${err.code}, message: ${err.message}`);
   5. });
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Calendar/CalendarManager/entry/src/main/ets/pages/Index.ets#L158-L164)
7. 也可以查询默认日历账户，默认日历账户是日历存储首次运行时创建的，若创建日程时不关注归属哪个账户，则无须单独创建日历账户，可以直接使用默认日历账户。

   ```
   1. calendarMgr?.getCalendar().then((data: calendarManager.Calendar) => {
   2. hilog.info(DOMAIN, 'testTag', '%{public}s', `Succeeded in getting calendar, data -> ${JSON.stringify(data)}`);
   3. }).catch((err: BusinessError) => {
   4. hilog.error(DOMAIN, 'testTag', `Failed to get calendar. Code: ${err.code}, message: ${err.message}`);
   5. });
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Calendar/CalendarManager/entry/src/main/ets/pages/Index.ets#L169-L175)
8. 获取当前应用所有创建的日历账户及默认日历账户Calendar对象。

   由于涉及数据隐私安全，进行了权限管控的应用无法获取其他应用创建的账户信息。

   ```
   1. calendarMgr?.getAllCalendars().then((data: calendarManager.Calendar[]) => {
   2. hilog.info(DOMAIN, 'testTag', '%{public}s', `Succeeded in getting all calendars, data -> ${JSON.stringify(data)}`);
   3. data.forEach((calendar) => {
   4. const account = calendar.getAccount();
   5. hilog.info(DOMAIN, 'testTag', '%{public}s', `account -> ${JSON.stringify(account)}`);
   6. })
   7. }).catch((err: BusinessError) => {
   8. hilog.error(DOMAIN, 'testTag', `Failed to get all calendars. Code: ${err.code}, message: ${err.message}`);
   9. });
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Calendar/CalendarManager/entry/src/main/ets/pages/Index.ets#L180-L190)
9. 删除指定的日历账户，删除账户后，该账户下的所有日程会全部删除。

   ```
   1. if (!calendar || calendar === null) {
   2. hilog.error(DOMAIN, 'testTag', 'Failed to delete calendar. calendar is null');
   3. return;
   4. }
   5. calendarMgr?.deleteCalendar(calendar).then(() => {
   6. hilog.info(DOMAIN, 'testTag', '%{public}s', "Succeeded in deleting calendar");
   7. }).catch((err: BusinessError) => {
   8. hilog.error(DOMAIN, 'testTag', `Failed to delete calendar. Code: ${err.code}, message: ${err.message}`);
   9. });
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Calendar/CalendarManager/entry/src/main/ets/pages/Index.ets#L195-L205)
