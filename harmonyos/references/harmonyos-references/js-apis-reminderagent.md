---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-reminderagent
title: @ohos.reminderAgent (后台代理提醒)
breadcrumb: API参考 > 应用框架 > Background Tasks Kit（后台任务开发服务） > ArkTS API > 已停止维护的接口 > @ohos.reminderAgent (后台代理提醒)
category: harmonyos-references
scraped_at: 2026-04-28T08:05:37+08:00
doc_updated_at: 2026-03-26
content_hash: sha256:269e5ff43df334d11390fb90b6de7f9f246214101b6d1175f0ed78a5d5f432c9
---

本模块提供后台代理提醒的能力。

开发应用时，开发者可以调用相关接口创建定时提醒，包括倒计时、日历、闹钟这三类提醒类型。使用后台代理提醒能力后，应用被冻结或退出后，计时和弹出提醒的功能将被后台系统服务代理。

说明

从API version 7开始支持，从API version 9开始废弃，建议使用[@ohos.reminderAgentManager (后台代理提醒)](js-apis-reminderagentmanager.md)替代。

本模块首批接口从API version 7开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import reminderAgent from'@ohos.reminderAgent';
```

## reminderAgent.publishReminder(deprecated)

PhonePC/2in1TabletTVWearable

publishReminder(reminderReq: ReminderRequest, callback: AsyncCallback<number>): void

发布一个后台代理提醒，使用回调的方式实现异步调用，该方法需要申请通知弹窗权限[Notification.requestEnableNotification](js-apis-notification.md#notificationrequestenablenotification8)后才能调用。

说明

从 API version 7开始支持，从API version 9开始废弃。建议使用[reminderAgentManager.publishReminder](js-apis-reminderagentmanager.md#reminderagentmanagerpublishreminder)替代。

**需要权限**：ohos.permission.PUBLISH\_AGENT\_REMINDER

**系统能力**：SystemCapability.Notification.ReminderAgent

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| reminderReq | [ReminderRequest](js-apis-reminderagent.md#reminderrequestdeprecated) | 是 | 需要发布的提醒实例。 |
| callback | AsyncCallback<number> | 是 | 异步回调，返回当前发布的提醒的id。 |

**示例**：

```
1. import { BusinessError } from '@ohos.base';

3. let timer:reminderAgent.ReminderRequestTimer = {
4. reminderType: reminderAgent.ReminderType.REMINDER_TYPE_TIMER,
5. triggerTimeInSeconds: 10
6. }

8. reminderAgent.publishReminder(timer, (err: BusinessError, reminderId: number) => {
9. console.info("callback, reminderId = " + reminderId);
10. });
```

## reminderAgent.publishReminder(deprecated)

PhonePC/2in1TabletTVWearable

publishReminder(reminderReq: ReminderRequest): Promise<number>

发布一个后台代理提醒，使用Promise方式实现异步调用，该方法需要申请通知弹窗权限[Notification.requestEnableNotification](js-apis-notification.md#notificationrequestenablenotification8)后才能调用。

说明

从 API version 7开始支持，从API version 9开始废弃。建议使用[reminderAgentManager.publishReminder](js-apis-reminderagentmanager.md#reminderagentmanagerpublishreminder-1)替代。

**需要权限**：ohos.permission.PUBLISH\_AGENT\_REMINDER

**系统能力**：SystemCapability.Notification.ReminderAgent

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| reminderReq | [ReminderRequest](js-apis-reminderagent.md#reminderrequestdeprecated) | 是 | 需要发布的提醒实例。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<number> | 返回提醒的Id。 |

**示例**：

```
1. let timer:reminderAgent.ReminderRequestTimer = {
2. reminderType: reminderAgent.ReminderType.REMINDER_TYPE_TIMER,
3. triggerTimeInSeconds: 10
4. }

6. reminderAgent.publishReminder(timer).then((reminderId: number) => {
7. console.info("promise, reminderId = " + reminderId);
8. });
```

## reminderAgent.cancelReminder(deprecated)

PhonePC/2in1TabletTVWearable

cancelReminder(reminderId: number, callback: AsyncCallback<void>): void

取消指定id的提醒，使用回调的方式实现异步调用。

说明

从 API version 7开始支持，从API version 9开始废弃。建议使用[reminderAgentManager.cancelReminder](js-apis-reminderagentmanager.md#reminderagentmanagercancelreminder)替代。

**系统能力**： SystemCapability.Notification.ReminderAgent

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| reminderId | number | 是 | 目标reminder的id号。 |
| callback | AsyncCallback<void> | 是 | 异步回调。 |

**示例**：

```
1. import { BusinessError } from '@ohos.base';

3. reminderAgent.cancelReminder(1, (err: BusinessError, data: void) => {
4. console.info("cancelReminder callback");
5. });
```

## reminderAgent.cancelReminder(deprecated)

PhonePC/2in1TabletTVWearable

cancelReminder(reminderId: number): Promise<void>

取消指定id的提醒，使用Promise方式实现异步调用。

说明

从 API version 7开始支持，从API version 9开始废弃。建议使用[reminderAgentManager.cancelReminder](js-apis-reminderagentmanager.md#reminderagentmanagercancelreminder-1)替代。

**系统能力**： SystemCapability.Notification.ReminderAgent

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| reminderId | number | 是 | 目标reminder的id号。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise类型异步回调。 |

**示例**：

```
1. reminderAgent.cancelReminder(1).then(() => {
2. console.info("cancelReminder promise");
3. });
```

## reminderAgent.getValidReminders(deprecated)

PhonePC/2in1TabletTVWearable

getValidReminders(callback: AsyncCallback<Array<ReminderRequest>>): void

获取当前应用已设置的所有有效（未过期）的提醒，使用回调的方式实现异步调用。

说明

从 API version 7开始支持，从API version 9开始废弃。建议使用[reminderAgentManager.getValidReminders](js-apis-reminderagentmanager.md#reminderagentmanagergetvalidreminders)替代。

**系统能力**： SystemCapability.Notification.ReminderAgent

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<Array<[ReminderRequest](js-apis-reminderagent.md#reminderrequestdeprecated)>> | 是 | 异步回调，返回当前应用已设置的所有有效（未过期）的提醒。 |

**示例**：

```
1. import { BusinessError } from '@ohos.base';

3. reminderAgent.getValidReminders((err: BusinessError, reminders: Array<reminderAgent.ReminderRequest>) => {
4. console.info("callback, getValidReminders length = " + reminders.length);
5. for (let i = 0; i < reminders.length; i++) {
6. console.info("getValidReminders = " + reminders[i]);
7. console.info("getValidReminders, reminderType = " + reminders[i].reminderType);
8. const actionButton = reminders[i].actionButton || [];
9. for (let j = 0; j < actionButton.length; j++) {
10. console.info("getValidReminders, actionButton.title = " + actionButton[j]?.title);
11. console.info("getValidReminders, actionButton.type = " + actionButton[j]?.type);
12. }
13. console.info("getValidReminders, wantAgent.pkgName = " + reminders[i].wantAgent?.pkgName);
14. console.info("getValidReminders, wantAgent.abilityName = " + reminders[i].wantAgent?.abilityName);
15. console.info("getValidReminders, ringDuration = " + reminders[i].ringDuration);
16. console.info("getValidReminders, snoozeTimes = " + reminders[i].snoozeTimes);
17. console.info("getValidReminders, timeInterval = " + reminders[i].timeInterval);
18. console.info("getValidReminders, title = " + reminders[i].title);
19. console.info("getValidReminders, content = " + reminders[i].content);
20. console.info("getValidReminders, expiredContent = " + reminders[i].expiredContent);
21. console.info("getValidReminders, snoozeContent = " + reminders[i].snoozeContent);
22. console.info("getValidReminders, notificationId = " + reminders[i].notificationId);
23. console.info("getValidReminders, slotType = " + reminders[i].slotType);
24. }
25. })
```

## reminderAgent.getValidReminders(deprecated)

PhonePC/2in1TabletTVWearable

getValidReminders(): Promise<Array<ReminderRequest>>

获取当前应用已设置的所有有效（未过期）的提醒，使用Promise方式实现异步调用。

说明

从 API version 7开始支持，从API version 9开始废弃。建议使用[reminderAgentManager.getValidReminders](js-apis-reminderagentmanager.md#reminderagentmanagergetvalidreminders-1)替代。

**系统能力**： SystemCapability.Notification.ReminderAgent

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<Array<[ReminderRequest](js-apis-reminderagent.md#reminderrequestdeprecated)>> | 返回当前应用已设置的所有有效（未过期）的提醒。 |

**示例**：

```
1. reminderAgent.getValidReminders().then((reminders: Array<reminderAgent.ReminderRequest>) => {
2. console.info("promise, getValidReminders length = " + reminders.length);
3. for (let i = 0; i < reminders.length; i++) {
4. console.info("getValidReminders = " + reminders[i]);
5. console.info("getValidReminders, reminderType = " + reminders[i].reminderType);
6. const actionButton = reminders[i].actionButton || [];
7. for (let j = 0; j < actionButton.length; j++) {
8. console.info("getValidReminders, actionButton.title = " + actionButton[j]?.title);
9. console.info("getValidReminders, actionButton.type = " + actionButton[j]?.type);
10. }
11. console.info("getValidReminders, wantAgent.pkgName = " + reminders[i].wantAgent?.pkgName);
12. console.info("getValidReminders, wantAgent.abilityName = " + reminders[i].wantAgent?.abilityName);
13. console.info("getValidReminders, ringDuration = " + reminders[i].ringDuration);
14. console.info("getValidReminders, snoozeTimes = " + reminders[i].snoozeTimes);
15. console.info("getValidReminders, timeInterval = " + reminders[i].timeInterval);
16. console.info("getValidReminders, title = " + reminders[i].title);
17. console.info("getValidReminders, content = " + reminders[i].content);
18. console.info("getValidReminders, expiredContent = " + reminders[i].expiredContent);
19. console.info("getValidReminders, snoozeContent = " + reminders[i].snoozeContent);
20. console.info("getValidReminders, notificationId = " + reminders[i].notificationId);
21. console.info("getValidReminders, slotType = " + reminders[i].slotType);
22. }
23. })
```

## reminderAgent.cancelAllReminders(deprecated)

PhonePC/2in1TabletTVWearable

cancelAllReminders(callback: AsyncCallback<void>): void

取消当前应用所有的提醒，使用回调的方式实现异步调用。

说明

从 API version 7开始支持，从API version 9开始废弃。建议使用[reminderAgentManager.cancelAllReminders](js-apis-reminderagentmanager.md#reminderagentmanagercancelallreminders)替代。

**系统能力**： SystemCapability.Notification.ReminderAgent

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<void> | 是 | 异步回调。 |

**示例**：

```
1. import { BusinessError } from '@ohos.base';

3. reminderAgent.cancelAllReminders((err: BusinessError, data: void) =>{
4. console.info("cancelAllReminders callback")
5. })
```

## reminderAgent.cancelAllReminders(deprecated)

PhonePC/2in1TabletTVWearable

cancelAllReminders(): Promise<void>

取消当前应用所有的提醒，使用Promise方式实现异步调用。

说明

从 API version 7开始支持，从API version 9开始废弃。建议使用[reminderAgentManager.cancelAllReminders](js-apis-reminderagentmanager.md#reminderagentmanagercancelallreminders-1)替代。

**系统能力**： SystemCapability.Notification.ReminderAgent

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise类型异步回调。 |

**示例**：

```
1. reminderAgent.cancelAllReminders().then(() => {
2. console.info("cancelAllReminders promise")
3. })
```

## reminderAgent.addNotificationSlot(deprecated)

PhonePC/2in1TabletTVWearable

addNotificationSlot(slot: NotificationSlot, callback: AsyncCallback<void>): void

添加一个NotificationSlot，使用回调的方式实现异步调用。

说明

从 API version 7开始支持，从API version 9开始废弃。建议使用[reminderAgentManager.addNotificationSlot](js-apis-reminderagentmanager.md#reminderagentmanageraddnotificationslot)替代。

**系统能力**： SystemCapability.Notification.ReminderAgent

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| slot | [NotificationSlot](js-apis-notification.md#notificationslot) | 是 | notification.slot实例，仅支持设置其type属性。 |
| callback | AsyncCallback<void> | 是 | 异步回调。 |

**示例**：

```
1. import notification from '@ohos.notificationManager'
2. import { BusinessError } from '@ohos.base';

4. let mySlot:notification.NotificationSlot = {
5. type: notification.SlotType.SOCIAL_COMMUNICATION
6. }
7. reminderAgent.addNotificationSlot(mySlot, (err: BusinessError, data: void) => {
8. console.info("addNotificationSlot callback");
9. });
```

## reminderAgent.addNotificationSlot(deprecated)

PhonePC/2in1TabletTVWearable

addNotificationSlot(slot: NotificationSlot): Promise<void>

添加一个NotificationSlot，使用Promise方式实现异步调用。

说明

从 API version 7开始支持，从API version 9开始废弃。建议使用[reminderAgentManager.addNotificationSlot](js-apis-reminderagentmanager.md#reminderagentmanageraddnotificationslot-1)替代。

**系统能力**： SystemCapability.Notification.ReminderAgent

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| slot | [NotificationSlot](js-apis-notification.md#notificationslot) | 是 | notification.slot实例，仅支持设置其type属性。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise类型异步回调。 |

**示例**：

```
1. import notification from '@ohos.notificationManager'

3. let mySlot:notification.NotificationSlot = {
4. type: notification.SlotType.SOCIAL_COMMUNICATION
5. }
6. reminderAgent.addNotificationSlot(mySlot).then(() => {
7. console.info("addNotificationSlot promise");
8. });
```

## reminderAgent.removeNotificationSlot(deprecated)

PhonePC/2in1TabletTVWearable

removeNotificationSlot(slotType: notification.SlotType, callback: AsyncCallback<void>): void

删除目标NotificationSlot，使用callback方式实现异步调用。

说明

从 API version 7开始支持，从API version 9开始废弃。建议使用[reminderAgentManager.removeNotificationSlot](js-apis-reminderagentmanager.md#reminderagentmanagerremovenotificationslot)替代。

**系统能力**：SystemCapability.Notification.ReminderAgent

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| slotType | [notification.SlotType](js-apis-notification.md#slottype) | 是 | 目标notification.slot的类型。 |
| callback | AsyncCallback<void> | 是 | 异步回调。 |

**示例**：

```
1. import notification from '@ohos.notification'
2. import { BusinessError } from '@ohos.base';

4. reminderAgent.removeNotificationSlot(notification.SlotType.CONTENT_INFORMATION, (err: BusinessError, data: void) => {
5. console.info("removeNotificationSlot callback");
6. });
```

## reminderAgent.removeNotificationSlot(deprecated)

PhonePC/2in1TabletTVWearable

removeNotificationSlot(slotType: notification.SlotType): Promise<void>

删除目标NotificationSlot，使用Promise方式实现异步调用。

说明

从 API version 7开始支持，从API version 9开始废弃。建议使用[reminderAgentManager.removeNotificationSlot](js-apis-reminderagentmanager.md#reminderagentmanagerremovenotificationslot-1)替代。

**系统能力**：SystemCapability.Notification.ReminderAgent

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| slotType | [notification.SlotType](js-apis-notification.md#slottype) | 是 | 目标notification.slot的类型。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise类型异步回调。 |

**示例**：

```
1. import notification from '@ohos.notification'

3. reminderAgent.removeNotificationSlot(notification.SlotType.CONTENT_INFORMATION).then(() => {
4. console.info("removeNotificationSlot promise");
5. });
```

## ActionButtonType(deprecated)

PhonePC/2in1TabletTVWearable

按钮的类型。

说明

从 API version 7开始支持，从API version 9开始废弃。建议使用[reminderAgentManager.ActionButtonType](js-apis-reminderagentmanager.md#actionbuttontype)替代。

**系统能力**：SystemCapability.Notification.ReminderAgent

| 名称 | 值 | 说明 |
| --- | --- | --- |
| ACTION\_BUTTON\_TYPE\_CLOSE | 0 | 表示关闭提醒的按钮。 |
| ACTION\_BUTTON\_TYPE\_SNOOZE | 1 | 表示延迟提醒的按钮。 |

## ReminderType(deprecated)

PhonePC/2in1TabletTVWearable

提醒的类型。

说明

从 API version 7开始支持，从API version 9开始废弃。建议使用[reminderAgentManager.ReminderType](js-apis-reminderagentmanager.md#remindertype)替代。

**系统能力**：SystemCapability.Notification.ReminderAgent

| 名称 | 值 | 说明 |
| --- | --- | --- |
| REMINDER\_TYPE\_TIMER | 0 | 表示提醒类型：倒计时。 |
| REMINDER\_TYPE\_CALENDAR | 1 | 表示提醒类型：日历。 |
| REMINDER\_TYPE\_ALARM | 2 | 表示提醒类型：闹钟。 |

## ActionButton(deprecated)

PhonePC/2in1TabletTVWearable

用于设置弹出的提醒通知信息上显示的按钮类型和标题。

说明

从 API version 7开始支持，从API version 9开始废弃。建议使用[reminderAgentManager.ActionButton](js-apis-reminderagentmanager.md#actionbutton)替代。

**系统能力**：SystemCapability.Notification.ReminderAgent

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| title | string | 否 | 否 | 按钮显示的标题。 |
| type | [ActionButtonType](js-apis-reminderagent.md#actionbuttontypedeprecated) | 否 | 否 | 按钮的类型。 |

## WantAgent(deprecated)

PhonePC/2in1TabletTVWearable

点击提醒通知后跳转的目标ability信息。

说明

从 API version 7开始支持，从API version 9开始废弃。建议使用[reminderAgentManager.WantAgent](js-apis-reminderagentmanager.md#wantagent)替代。

**系统能力**：SystemCapability.Notification.ReminderAgent

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| pkgName | string | 否 | 否 | 指明点击提醒通知栏后跳转的目标HAP名。 |
| abilityName | string | 否 | 否 | 指明点击提醒通知栏后跳转的目标ability名称。 |

## MaxScreenWantAgent(deprecated)

PhonePC/2in1TabletTVWearable

全屏显示提醒到达时自动拉起的目标ability信息，该接口预留。

说明

从 API version 7开始支持，从API version 9开始废弃。建议使用[reminderAgentManager.MaxScreenWantAgent](js-apis-reminderagentmanager.md#maxscreenwantagent)替代。

**系统能力**：SystemCapability.Notification.ReminderAgent

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| pkgName | string | 否 | 否 | 指明提醒到达时自动拉起的目标HAP名（如果设备在使用中，则只弹出通知横幅框）。 |
| abilityName | string | 否 | 否 | 指明提醒到达时自动拉起的目标ability名（如果设备在使用中，则只弹出通知横幅框）。 |

## ReminderRequest(deprecated)

PhonePC/2in1TabletTVWearable

提醒实例对象，用于设置提醒类型、响铃时长等具体信息。

说明

从 API version 7开始支持，从API version 9开始废弃。建议使用[reminderAgentManager.ReminderRequest](js-apis-reminderagentmanager.md#reminderrequest)替代。

**系统能力**：SystemCapability.Notification.ReminderAgent

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| reminderType | [ReminderType](js-apis-reminderagent.md#remindertypedeprecated) | 否 | 否 | 指明提醒类型。 |
| actionButton | [[ActionButton](js-apis-reminderagent.md#actionbuttondeprecated)?, [ActionButton](js-apis-reminderagent.md#actionbuttondeprecated)?] | 否 | 是 | 弹出的提醒通知栏中显示的按钮（参数可选，支持0/1/2个按钮）。 |
| wantAgent | WantAgent | 否 | 是 | 点击通知后需要跳转的目标ability信息。 |
| maxScreenWantAgent | [MaxScreenWantAgent](js-apis-reminderagent.md#maxscreenwantagentdeprecated) | 否 | 是 | 提醒到达时跳转的目标包。如果设备正在使用中，则弹出一个通知框。 |
| ringDuration | number | 否 | 是 | 指明响铃时长（单位：秒），默认1秒。 |
| snoozeTimes | number | 否 | 是 | 指明延迟提醒次数，默认0次。 |
| timeInterval | number | 否 | 是 | 执行延迟提醒间隔（单位：秒），默认0秒。 |
| title | string | 否 | 是 | 指明提醒标题。 |
| content | string | 否 | 是 | 指明提醒内容。 |
| expiredContent | string | 否 | 是 | 指明提醒过期后需要显示的内容。 |
| snoozeContent | string | 否 | 是 | 指明延迟提醒时需要显示的内容。 |
| notificationId | number | 否 | 是 | 指明提醒使用的通知的id号，相同id号的提醒会覆盖。 |
| slotType | [notification.SlotType](js-apis-notification.md#slottype) | 否 | 是 | 指明提醒的slot类型。 |

## ReminderRequestCalendar(deprecated)

PhonePC/2in1TabletTVWearable

日历实例对象，用于设置提醒的时间。

说明

从 API version 7开始支持，从API version 9开始废弃。建议使用[reminderAgentManager.ReminderRequestCalendar](js-apis-reminderagentmanager.md#reminderrequestcalendar)替代。

**系统能力**：SystemCapability.Notification.ReminderAgent

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| dateTime | [LocalDateTime](js-apis-reminderagent.md#localdatetimedeprecated) | 否 | 否 | 指明提醒的目标时间。 |
| repeatMonths | Array<number> | 否 | 是 | 指明重复提醒的月份。 |
| repeatDays | Array<number> | 否 | 是 | 指明重复提醒的日期。 |

## ReminderRequestAlarm(deprecated)

PhonePC/2in1TabletTVWearable

闹钟实例对象，用于设置提醒的时间。

说明

从 API version 7开始支持，从API version 9开始废弃。建议使用[reminderAgentManager.ReminderRequestAlarm](js-apis-reminderagentmanager.md#reminderrequestalarm)替代。

**系统能力**：SystemCapability.Notification.ReminderAgent

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| hour | number | 否 | 否 | 指明提醒的目标时刻。 |
| minute | number | 否 | 否 | 指明提醒的目标分钟。 |
| daysOfWeek | Array<number> | 否 | 是 | 指明每周哪几天需要重复提醒。范围为周一到周末，对应数字为1到7。 |

## ReminderRequestTimer(deprecated)

PhonePC/2in1TabletTVWearable

倒计时实例对象，用于设置提醒的时间。

说明

从 API version 7开始支持，从API version 9开始废弃。建议使用[reminderAgentManager.ReminderRequestTimer](js-apis-reminderagentmanager.md#reminderrequesttimer)替代。

**系统能力**：SystemCapability.Notification.ReminderAgent

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| triggerTimeInSeconds | number | 否 | 否 | 指明倒计时的秒数。 |

## LocalDateTime(deprecated)

PhonePC/2in1TabletTVWearable

用于日历类提醒设置时指定时间信息。

说明

从 API version 7开始支持，从API version 9开始废弃。建议使用[reminderAgentManager.LocalDateTime](js-apis-reminderagentmanager.md#localdatetime)替代。

**系统能力**：SystemCapability.Notification.ReminderAgent

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| year | number | 否 | 否 | 年 |
| month | number | 否 | 否 | 月 |
| day | number | 否 | 否 | 日 |
| hour | number | 否 | 否 | 时 |
| minute | number | 否 | 否 | 分 |
| second | number | 否 | 是 | 秒 |
