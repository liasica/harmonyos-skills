---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-reminderagentmanager
title: @ohos.reminderAgentManager (后台代理提醒)
breadcrumb: API参考 > 应用框架 > Background Tasks Kit（后台任务开发服务） > ArkTS API > @ohos.reminderAgentManager (后台代理提醒)
category: harmonyos-references
scraped_at: 2026-04-29T13:56:02+08:00
doc_updated_at: 2026-04-28
content_hash: sha256:547de2069fe5a5d58c0b797ea5eab9a1759a9c81fa3e6b3f686458b5ccdae2d3
---

本模块提供后台代理提醒的能力，即当应用被冻结或应用退出时，定时提醒功能将被系统服务代理。开发者可以调用本模块接口创建定时提醒，提醒类型支持倒计时、日历、闹钟三种。开发指导请参考[代理提醒开发指南](../harmonyos-guides/agent-powered-reminder.md)。

说明

本模块首批接口从API version 9开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { reminderAgentManager } from '@kit.BackgroundTasksKit';
```

## reminderAgentManager.publishReminder

PhonePC/2in1TabletTVWearable

publishReminder(reminderReq: ReminderRequest, callback: AsyncCallback<number>): void

发布后台代理提醒。使用callback异步回调。

说明

该接口需要申请通知弹窗权限[notificationManager.requestEnableNotification](js-apis-notificationmanager.md#notificationmanagerrequestenablenotification10)后调用。

为了防止代理提醒被滥用于广告、营销类提醒，影响用户体验，部分设备上代理提醒增加了管控机制。管控后的适配或申请权限的方法，请参考[约束与限制中的管控限制](../harmonyos-guides/agent-powered-reminder.md#约束与限制)。

**需要权限：** ohos.permission.PUBLISH\_AGENT\_REMINDER

**系统能力：** SystemCapability.Notification.ReminderAgent

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| reminderReq | [ReminderRequest](js-apis-reminderagentmanager.md#reminderrequest) | 是 | 需要发布的代理提醒实例。 |
| callback | AsyncCallback<number> | 是 | 回调函数，当代理提醒发布成功，err为undefined，data为当前发布提醒的id；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[reminderAgentManager错误码](errorcode-reminderagentmanager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | If the input parameter is not valid parameter. |
| 1700001 | Notification is not enabled. |
| 1700002 | The number of reminders exceeds the limit. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { reminderAgentManager } from '@kit.BackgroundTasksKit';

4. let timer: reminderAgentManager.ReminderRequestTimer = {
5. reminderType: reminderAgentManager.ReminderType.REMINDER_TYPE_TIMER,
6. triggerTimeInSeconds: 10
7. }

9. reminderAgentManager.publishReminder(timer, (err: BusinessError, reminderId: number) => {
10. if (err.code) {
11. console.error("callback err code:" + err.code + " message:" + err.message);
12. } else {
13. console.info("callback, reminderId = " + reminderId);
14. }
15. });
```

## reminderAgentManager.publishReminder

PhonePC/2in1TabletTVWearable

publishReminder(reminderReq: ReminderRequest): Promise<number>

发布后台代理提醒。使用Promise异步回调。

说明

该接口需要申请通知弹窗权限[notificationManager.requestEnableNotification](js-apis-notificationmanager.md#notificationmanagerrequestenablenotification10)后调用。

为了防止代理提醒被滥用于广告、营销类提醒，影响用户体验，部分设备上代理提醒增加了管控机制。管控后的适配或申请权限的方法，请参考[约束与限制中的管控限制](../harmonyos-guides/agent-powered-reminder.md#约束与限制)。

**需要权限：** ohos.permission.PUBLISH\_AGENT\_REMINDER

**系统能力：** SystemCapability.Notification.ReminderAgent

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| reminderReq | [ReminderRequest](js-apis-reminderagentmanager.md#reminderrequest) | 是 | 需要发布的代理提醒实例。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象，返回当前发布提醒的id。 |

**错误码：**

以下错误码的详细介绍请参见[reminderAgentManager错误码](errorcode-reminderagentmanager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | If the input parameter is not valid parameter. |
| 1700001 | Notification is not enabled. |
| 1700002 | The number of reminders exceeds the limit. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { reminderAgentManager } from '@kit.BackgroundTasksKit';

4. let timer: reminderAgentManager.ReminderRequestTimer = {
5. reminderType: reminderAgentManager.ReminderType.REMINDER_TYPE_TIMER,
6. triggerTimeInSeconds: 10
7. }

9. reminderAgentManager.publishReminder(timer).then((reminderId: number) => {
10. console.info("promise, reminderId = " + reminderId);
11. }).catch((err: BusinessError) => {
12. console.error("promise err code:" + err.code + " message:" + err.message);
13. });
```

## reminderAgentManager.cancelReminder

PhonePC/2in1TabletTVWearable

cancelReminder(reminderId: number, callback: AsyncCallback<void>): void

取消指定id的代理提醒。使用callback异步回调。

**系统能力：** SystemCapability.Notification.ReminderAgent

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| reminderId | number | 是 | 需要取消的代理提醒的id，代理提醒id会在[发布代理提醒](js-apis-reminderagentmanager.md#reminderagentmanagerpublishreminder)时作为返回值返回。 |
| callback | AsyncCallback<void> | 是 | 回调函数，当取消代理提醒成功，err为undefined；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[reminderAgentManager错误码](errorcode-reminderagentmanager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | If the input parameter is not valid parameter. |
| 1700003 | The reminder does not exist. |
| 1700004 | The bundle name does not exist. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { reminderAgentManager } from '@kit.BackgroundTasksKit';

4. let reminderId: number = 1;
5. reminderAgentManager.cancelReminder(reminderId, (err: BusinessError) => {
6. if (err.code) {
7. console.error("callback err code:" + err.code + " message:" + err.message);
8. } else {
9. console.info("cancelReminder callback");
10. }
11. });
```

## reminderAgentManager.cancelReminder

PhonePC/2in1TabletTVWearable

cancelReminder(reminderId: number): Promise<void>

取消指定id的代理提醒。使用Promise异步回调。

**系统能力：** SystemCapability.Notification.ReminderAgent

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| reminderId | number | 是 | 需要取消的代理提醒的id，代理提醒id会在[发布代理提醒](js-apis-reminderagentmanager.md#reminderagentmanagerpublishreminder)时作为返回值返回。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[reminderAgentManager错误码](errorcode-reminderagentmanager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | If the input parameter is not valid parameter. |
| 1700003 | The reminder does not exist. |
| 1700004 | The bundle name does not exist. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { reminderAgentManager } from '@kit.BackgroundTasksKit';

4. let reminderId: number = 1;
5. reminderAgentManager.cancelReminder(reminderId).then(() => {
6. console.info("cancelReminder promise");
7. }).catch((err: BusinessError) => {
8. console.error("promise err code:" + err.code + " message:" + err.message);
9. });
```

## reminderAgentManager.getValidReminders

PhonePC/2in1TabletTVWearable

getValidReminders(callback: AsyncCallback<Array<ReminderRequest>>): void

获取当前应用设置的所有[有效（未过期）的代理提醒](../harmonyos-guides/agent-powered-reminder.md#约束与限制)。使用callback异步回调。

**系统能力：** SystemCapability.Notification.ReminderAgent

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<Array<[ReminderRequest](js-apis-reminderagentmanager.md#reminderrequest)>> | 是 | 回调函数，当查询代理提醒成功，err为undefined，data为当前应用设置的所有有效（未过期）的代理提醒；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[reminderAgentManager错误码](errorcode-reminderagentmanager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | If the input parameter is not valid parameter. |
| 1700004 | The bundle name does not exist. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { reminderAgentManager } from '@kit.BackgroundTasksKit';

4. reminderAgentManager.getValidReminders((err: BusinessError, reminders: Array<reminderAgentManager.ReminderRequest>) => {
5. if (err.code) {
6. console.error("callback err code:" + err.code + " message:" + err.message);
7. } else {
8. console.info("callback, getValidReminders length = " + reminders.length);
9. for (let i = 0; i < reminders.length; i++) {
10. console.info("getValidReminders = " + reminders[i]);
11. console.info("getValidReminders, reminderType = " + reminders[i].reminderType);
12. const actionButton = reminders[i].actionButton || [];
13. for (let j = 0; j < actionButton.length; j++) {
14. console.info("getValidReminders, actionButton.title = " + actionButton[j]?.title);
15. console.info("getValidReminders, actionButton.type = " + actionButton[j]?.type);
16. }
17. console.info("getValidReminders, wantAgent.pkgName = " + reminders[i].wantAgent?.pkgName);
18. console.info("getValidReminders, wantAgent.abilityName = " + reminders[i].wantAgent?.abilityName);
19. console.info("getValidReminders, ringDuration = " + reminders[i].ringDuration);
20. console.info("getValidReminders, snoozeTimes = " + reminders[i].snoozeTimes);
21. console.info("getValidReminders, timeInterval = " + reminders[i].timeInterval);
22. console.info("getValidReminders, title = " + reminders[i].title);
23. console.info("getValidReminders, content = " + reminders[i].content);
24. console.info("getValidReminders, expiredContent = " + reminders[i].expiredContent);
25. console.info("getValidReminders, snoozeContent = " + reminders[i].snoozeContent);
26. console.info("getValidReminders, notificationId = " + reminders[i].notificationId);
27. console.info("getValidReminders, slotType = " + reminders[i].slotType);
28. }
29. }
30. });
```

## reminderAgentManager.getValidReminders

PhonePC/2in1TabletTVWearable

getValidReminders(): Promise<Array<ReminderRequest>>

获取当前应用设置的所有[有效（未过期）的代理提醒](../harmonyos-guides/agent-powered-reminder.md#约束与限制)。使用Promise异步回调。

**系统能力：** SystemCapability.Notification.ReminderAgent

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<[ReminderRequest](js-apis-reminderagentmanager.md#reminderrequest)>> | Promise对象，返回当前应用设置的所有有效（未过期）的代理提醒。 |

**错误码：**

以下错误码的详细介绍请参见[reminderAgentManager错误码](errorcode-reminderagentmanager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | If the input parameter is not valid parameter. |
| 1700004 | The bundle name does not exist. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { reminderAgentManager } from '@kit.BackgroundTasksKit';

4. reminderAgentManager.getValidReminders().then((reminders: Array<reminderAgentManager.ReminderRequest>) => {
5. console.info("promise, getValidReminders length = " + reminders.length);
6. for (let i = 0; i < reminders.length; i++) {
7. console.info("getValidReminders = " + reminders[i]);
8. console.info("getValidReminders, reminderType = " + reminders[i].reminderType);
9. const actionButton = reminders[i].actionButton || [];
10. for (let j = 0; j < actionButton.length; j++) {
11. console.info("getValidReminders, actionButton.title = " + actionButton[j]?.title);
12. console.info("getValidReminders, actionButton.type = " + actionButton[j]?.type);
13. }
14. console.info("getValidReminders, wantAgent.pkgName = " + reminders[i].wantAgent?.pkgName);
15. console.info("getValidReminders, wantAgent.abilityName = " + reminders[i].wantAgent?.abilityName);
16. console.info("getValidReminders, ringDuration = " + reminders[i].ringDuration);
17. console.info("getValidReminders, snoozeTimes = " + reminders[i].snoozeTimes);
18. console.info("getValidReminders, timeInterval = " + reminders[i].timeInterval);
19. console.info("getValidReminders, title = " + reminders[i].title);
20. console.info("getValidReminders, content = " + reminders[i].content);
21. console.info("getValidReminders, expiredContent = " + reminders[i].expiredContent);
22. console.info("getValidReminders, snoozeContent = " + reminders[i].snoozeContent);
23. console.info("getValidReminders, notificationId = " + reminders[i].notificationId);
24. console.info("getValidReminders, slotType = " + reminders[i].slotType);
25. }
26. }).catch((err: BusinessError) => {
27. console.error("promise err code:" + err.code + " message:" + err.message);
28. });
```

## reminderAgentManager.cancelAllReminders

PhonePC/2in1TabletTVWearable

cancelAllReminders(callback: AsyncCallback<void>): void

取消当前应用设置的所有代理提醒。使用callback异步回调。

**系统能力：** SystemCapability.Notification.ReminderAgent

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<void> | 是 | 回调函数，当取消代理提醒成功，err为undefined；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[reminderAgentManager错误码](errorcode-reminderagentmanager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | If the input parameter is not valid parameter. |
| 1700004 | The bundle name does not exist. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { reminderAgentManager } from '@kit.BackgroundTasksKit';

4. reminderAgentManager.cancelAllReminders((err: BusinessError) =>{
5. if (err.code) {
6. console.error("callback err code:" + err.code + " message:" + err.message);
7. } else {
8. console.info("cancelAllReminders callback")
9. }
10. });
```

## reminderAgentManager.cancelAllReminders

PhonePC/2in1TabletTVWearable

cancelAllReminders(): Promise<void>

取消当前应用设置的所有代理提醒。使用Promise异步回调。

**系统能力：** SystemCapability.Notification.ReminderAgent

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[reminderAgentManager错误码](errorcode-reminderagentmanager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | If the input parameter is not valid parameter. |
| 1700004 | The bundle name does not exist. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { reminderAgentManager } from '@kit.BackgroundTasksKit';

4. reminderAgentManager.cancelAllReminders().then(() => {
5. console.info("cancelAllReminders promise")
6. }).catch((err: BusinessError) => {
7. console.error("promise err code:" + err.code + " message:" + err.message);
8. });
```

## reminderAgentManager.addNotificationSlot

PhonePC/2in1TabletTVWearable

addNotificationSlot(slot: NotificationSlot, callback: AsyncCallback<void>): void

添加通知渠道。使用callback异步回调。

**系统能力：** SystemCapability.Notification.ReminderAgent

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| slot | [NotificationSlot](js-apis-inner-notification-notificationslot.md#notificationslot-1) | 是 | 通知渠道实例，仅支持设置其notificationType属性。 |
| callback | AsyncCallback<void> | 是 | 回调函数，当添加NotificationSlot成功，err为undefined；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | If the input parameter is not valid parameter. |

**示例：**

```
1. import { notificationManager } from '@kit.NotificationKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { reminderAgentManager } from '@kit.BackgroundTasksKit';

5. let mySlot: notificationManager.NotificationSlot = {
6. notificationType: notificationManager.SlotType.SOCIAL_COMMUNICATION
7. }

9. reminderAgentManager.addNotificationSlot(mySlot, (err: BusinessError) => {
10. if (err.code) {
11. console.error("callback err code:" + err.code + " message:" + err.message);
12. } else {
13. console.info("addNotificationSlot callback");
14. }
15. });
```

## reminderAgentManager.addNotificationSlot

PhonePC/2in1TabletTVWearable

addNotificationSlot(slot: NotificationSlot): Promise<void>

添加通知渠道。使用Promise异步回调。

**系统能力：** SystemCapability.Notification.ReminderAgent

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| slot | [NotificationSlot](js-apis-inner-notification-notificationslot.md#notificationslot-1) | 是 | 通知渠道实例，仅支持设置其notificationType属性。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | If the input parameter is not valid parameter. |

**示例：**

```
1. import { notificationManager } from '@kit.NotificationKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { reminderAgentManager } from '@kit.BackgroundTasksKit';

5. let mySlot: notificationManager.NotificationSlot = {
6. notificationType: notificationManager.SlotType.SOCIAL_COMMUNICATION
7. }
8. reminderAgentManager.addNotificationSlot(mySlot).then(() => {
9. console.info("addNotificationSlot promise");
10. }).catch((err: BusinessError) => {
11. console.error("promise err code:" + err.code + " message:" + err.message);
12. });
```

## reminderAgentManager.removeNotificationSlot

PhonePC/2in1TabletTVWearable

removeNotificationSlot(slotType: notification.SlotType, callback: AsyncCallback<void>): void

删除指定的通知渠道类型，使用callback异步回调。

**系统能力：** SystemCapability.Notification.ReminderAgent

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| slotType | [notification.SlotType](js-apis-notification.md#slottype) | 是 | 通知渠道类型。 |
| callback | AsyncCallback<void> | 是 | 回调函数，当删除成功，err为undefined；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | If the input parameter is not valid parameter. |

**示例：**

```
1. import { notificationManager } from '@kit.NotificationKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { reminderAgentManager } from '@kit.BackgroundTasksKit';

5. reminderAgentManager.removeNotificationSlot(notificationManager.SlotType.CONTENT_INFORMATION,
6. (err: BusinessError) => {
7. if (err.code) {
8. console.error("callback err code:" + err.code + " message:" + err.message);
9. } else {
10. console.info("removeNotificationSlot callback");
11. }
12. });
```

## reminderAgentManager.removeNotificationSlot

PhonePC/2in1TabletTVWearable

removeNotificationSlot(slotType: notification.SlotType): Promise<void>

删除指定的通知渠道类型，使用Promise异步回调。

**系统能力：** SystemCapability.Notification.ReminderAgent

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| slotType | [notification.SlotType](js-apis-notification.md#slottype) | 是 | 通知渠道类型。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | If the input parameter is not valid parameter. |

**示例：**

```
1. import { notificationManager } from '@kit.NotificationKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { reminderAgentManager } from '@kit.BackgroundTasksKit';

5. reminderAgentManager.removeNotificationSlot(notificationManager.SlotType.CONTENT_INFORMATION).then(() => {
6. console.info("removeNotificationSlot promise");
7. }).catch((err: BusinessError) => {
8. console.error("promise err code:" + err.code + " message:" + err.message);
9. });
```

## reminderAgentManager.getAllValidReminders12+

PhonePC/2in1TabletTVWearable

getAllValidReminders(): Promise<Array<ReminderInfo>>

获取当前应用设置的所有[有效（未过期）的代理提醒](../harmonyos-guides/agent-powered-reminder.md#约束与限制)。使用Promise异步回调。该接口调用需要申请ohos.permission.PUBLISH\_AGENT\_REMINDER权限。

**系统能力：** SystemCapability.Notification.ReminderAgent

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<[ReminderInfo](js-apis-reminderagentmanager.md#reminderinfo12)>> | Promise对象，返回当前应用设置的所有有效（未过期）的代理提醒。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { reminderAgentManager } from '@kit.BackgroundTasksKit';

4. reminderAgentManager.getAllValidReminders().then((reminders: Array<reminderAgentManager.ReminderInfo>) => {
5. console.info("promise, getAllValidReminders length = " + reminders.length);
6. for (let i = 0; i < reminders.length; i++) {
7. console.info("getAllValidReminders, reminderId = " + reminders[i].reminderId);
8. console.info("getAllValidReminders, reminderType = " + reminders[i].reminderReq.reminderType);
9. const actionButton = reminders[i].reminderReq.actionButton || [];
10. for (let j = 0; j < actionButton.length; j++) {
11. console.info("getAllValidReminders, actionButton.title = " + actionButton[j]?.title);
12. console.info("getAllValidReminders, actionButton.type = " + actionButton[j]?.type);
13. }
14. console.info("getAllValidReminders, wantAgent.pkgName = " + reminders[i].reminderReq.wantAgent?.pkgName);
15. console.info("getAllValidReminders, wantAgent.abilityName = " + reminders[i].reminderReq.wantAgent?.abilityName);
16. console.info("getAllValidReminders, ringDuration = " + reminders[i].reminderReq.ringDuration);
17. console.info("getAllValidReminders, snoozeTimes = " + reminders[i].reminderReq.snoozeTimes);
18. console.info("getAllValidReminders, timeInterval = " + reminders[i].reminderReq.timeInterval);
19. console.info("getAllValidReminders, title = " + reminders[i].reminderReq.title);
20. console.info("getAllValidReminders, content = " + reminders[i].reminderReq.content);
21. console.info("getAllValidReminders, expiredContent = " + reminders[i].reminderReq.expiredContent);
22. console.info("getAllValidReminders, snoozeContent = " + reminders[i].reminderReq.snoozeContent);
23. console.info("getAllValidReminders, notificationId = " + reminders[i].reminderReq.notificationId);
24. console.info("getAllValidReminders, slotType = " + reminders[i].reminderReq.slotType);
25. }
26. }).catch((err: BusinessError) => {
27. console.error("promise err code:" + err.code + " message:" + err.message);
28. });
```

## reminderAgentManager.addExcludeDate12+

PhonePC/2in1TabletTVWearable

addExcludeDate(reminderId: number, date: Date): Promise<void>

为指定id的周期性的日历提醒，添加不提醒日期（如每天提醒的日历，设置周二不提醒）。使用Promise异步回调。

**系统能力：** SystemCapability.Notification.ReminderAgent

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| reminderId | number | 是 | 需要添加不提醒日期的代理提醒id，代理提醒id会在[发布代理提醒](js-apis-reminderagentmanager.md#reminderagentmanagerpublishreminder)时作为返回值返回。 |
| date | Date | 是 | 不提醒的日期。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[reminderAgentManager错误码](errorcode-reminderagentmanager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | If the input parameter is not valid parameter. |
| 1700003 | The reminder does not exist. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { reminderAgentManager } from '@kit.BackgroundTasksKit';

4. let reminderId: number = 1;
5. let date = new Date();
6. reminderAgentManager.addExcludeDate(reminderId, date).then(() => {
7. console.info("addExcludeDate promise");
8. }).catch((err: BusinessError) => {
9. console.error("promise err code:" + err.code + " message:" + err.message);
10. });
```

## reminderAgentManager.deleteExcludeDates12+

PhonePC/2in1TabletTVWearable

deleteExcludeDates(reminderId: number): Promise<void>

为指定id的周期性的日历提醒，删除设置的所有不提醒日期。使用Promise异步回调。

**系统能力：** SystemCapability.Notification.ReminderAgent

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| reminderId | number | 是 | 需要删除不提醒日期的代理提醒id，代理提醒id会在[发布代理提醒](js-apis-reminderagentmanager.md#reminderagentmanagerpublishreminder)时作为返回值返回。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[reminderAgentManager错误码](errorcode-reminderagentmanager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 1700003 | The reminder does not exist. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { reminderAgentManager } from '@kit.BackgroundTasksKit';

4. let reminderId: number = 1;
5. reminderAgentManager.deleteExcludeDates(reminderId).then(() => {
6. console.info("deleteExcludeDates promise");
7. }).catch((err: BusinessError) => {
8. console.error("promise err code:" + err.code + " message:" + err.message);
9. });
```

## reminderAgentManager.getExcludeDates12+

PhonePC/2in1TabletTVWearable

getExcludeDates(reminderId: number): Promise<Array<Date>>

为指定id的周期性的日历提醒，查询设置的所有不提醒日期。使用Promise异步回调。

**系统能力：** SystemCapability.Notification.ReminderAgent

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| reminderId | number | 是 | 需要查询不提醒日期的代理提醒id，代理提醒id会在[发布代理提醒](js-apis-reminderagentmanager.md#reminderagentmanagerpublishreminder)时作为返回值返回。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<Date>> | Promise对象。返回特定日历设置的所有不提醒日期。 |

**错误码：**

以下错误码的详细介绍请参见[reminderAgentManager错误码](errorcode-reminderagentmanager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 1700003 | The reminder does not exist. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { reminderAgentManager } from '@kit.BackgroundTasksKit';

4. let reminderId: number = 1;
5. reminderAgentManager.getExcludeDates(reminderId).then((dates) => {
6. console.info("getExcludeDates promise length: " + dates.length);
7. for (let i = 0; i < dates.length; i++) {
8. console.info("getExcludeDates promise date is: " + dates[i].toString());
9. }
10. }).catch((err: BusinessError) => {
11. console.error("promise err code:" + err.code + " message:" + err.message);
12. });
```

## reminderAgentManager.updateReminder20+

PhonePC/2in1TabletTVWearable

updateReminder(reminderId: number, reminderReq: ReminderRequest): Promise<void>

更新指定id的代理提醒，使用Promise异步回调。仅[有效（未过期）](../harmonyos-guides/agent-powered-reminder.md#约束与限制)、未显示在通知中心的代理提醒支持更新。

**需要权限：** ohos.permission.PUBLISH\_AGENT\_REMINDER

**系统能力：** SystemCapability.Notification.ReminderAgent

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| reminderId | number | 是 | 需要更新的代理提醒的id，代理提醒id会在[发布代理提醒](js-apis-reminderagentmanager.md#reminderagentmanagerpublishreminder)时作为返回值返回。 |
| reminderReq | [ReminderRequest](js-apis-reminderagentmanager.md#reminderrequest) | 是 | 代理提醒对象实例，用于设置提醒类型、响铃时长等具体信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[reminderAgentManager错误码](errorcode-reminderagentmanager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 1700003 | The reminder does not exist. |
| 1700007 | If the input parameter is not valid parameter. |

**示例：**

```
1. import { reminderAgentManager } from '@kit.BackgroundTasksKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let timer: reminderAgentManager.ReminderRequestTimer = {
5. reminderType: reminderAgentManager.ReminderType.REMINDER_TYPE_TIMER,
6. triggerTimeInSeconds: 10
7. }

9. let reminderId: number = 1;
10. reminderAgentManager.updateReminder(reminderId, timer).then(() => {
11. console.info("update reminder succeed");
12. }).catch((err: BusinessError) => {
13. console.error("promise err code:" + err.code + " message:" + err.message);
14. });
```

## reminderAgentManager.cancelReminderOnDisplay23+

PhonePC/2in1TabletTVWearable

cancelReminderOnDisplay(reminderId: number): Promise<void>

取消当前通知中心内显示的通知卡片，不取消代理提醒数据。例如：每天重复的提醒，该提醒正在通知中心内显示，该接口将通知从通知中心内取消，并且会按照设定的周期，在第二天再次提醒。

**系统能力：** SystemCapability.Notification.ReminderAgent

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| reminderId | number | 是 | 需要取消的代理提醒的id，代理提醒id会在[发布代理提醒](js-apis-reminderagentmanager.md#reminderagentmanagerpublishreminder)时作为返回值返回。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[reminderAgentManager错误码](errorcode-reminderagentmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1700003 | The reminder does not exist. |
| 1700007 | If the input parameter is not valid parameter. |

**示例：**

```
1. import { reminderAgentManager } from '@kit.BackgroundTasksKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let reminderId: number = 1;
5. reminderAgentManager.cancelReminderOnDisplay(reminderId).then(() => {
6. console.info("cancel display reminder  succeed");
7. }).catch((err: BusinessError) => {
8. console.error("promise err code:" + err.code + " message:" + err.message);
9. });
```

## reminderAgentManager.subscribeReminderState23+

PhonePC/2in1TabletTVWearable

subscribeReminderState(callback: Callback<Array<ReminderState>>): Promise<void>

订阅代理提醒状态。使用Promise异步回调。

**需要权限：** ohos.permission.PUBLISH\_AGENT\_REMINDER

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Notification.ReminderAgent

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<Array<[ReminderState](js-apis-reminderagentmanager.md#reminderstate23)>> | 是 | 回调函数，返回代理提醒状态信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[reminderAgentManager错误码](errorcode-reminderagentmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 1700007 | If the input parameter is not valid parameter. |

**示例：**

```
1. import { reminderAgentManager } from '@kit.BackgroundTasksKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. function reminderStateCallback(states: Array<reminderAgentManager.ReminderState>) {
5. console.info('length is : ' + states.length);
6. }

8. reminderAgentManager.subscribeReminderState(reminderStateCallback).then(() => {
9. console.info('subscribe succeed');
10. }).catch((err: BusinessError) => {
11. console.error('promise err code:' + err.code + ' message:' + err.message);
12. });
```

## reminderAgentManager.unsubscribeReminderState23+

PhonePC/2in1TabletTVWearable

unsubscribeReminderState(callback?: Callback<Array<ReminderState>>): Promise<void>

取消订阅代理提醒状态。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Notification.ReminderAgent

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<Array<[ReminderState](js-apis-reminderagentmanager.md#reminderstate23)>> | 否 | 回调函数。如果不传参数callback，则取消所有订阅。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[reminderAgentManager错误码](errorcode-reminderagentmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1700007 | If the input parameter is not valid parameter. |

**示例：**

```
1. import { reminderAgentManager } from '@kit.BackgroundTasksKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. function reminderStateCallback(states: Array<reminderAgentManager.ReminderState>) {
5. console.info('length is : ' + states.length);
6. }

8. reminderAgentManager.unsubscribeReminderState(reminderStateCallback).then(() => {
9. console.info('unsubscribe succeed');
10. }).catch((err: BusinessError) => {
11. console.error('promise err code:' + err.code + ' message:' + err.message);
12. });
```

## ActionButtonType

PhonePC/2in1TabletTVWearable

提醒上的按钮的类型。

**系统能力：** SystemCapability.Notification.ReminderAgent

| 名称 | 值 | 说明 |
| --- | --- | --- |
| ACTION\_BUTTON\_TYPE\_CLOSE | 0 | 表示关闭提醒的按钮。 |
| ACTION\_BUTTON\_TYPE\_SNOOZE | 1 | 表示延时提醒的按钮，提醒次数和间隔通过[ReminderRequest](js-apis-reminderagentmanager.md#reminderrequest)中snoozeTimes和timeInterval设置。 |

## ReminderType

PhonePC/2in1TabletTVWearable

提醒的类型。

**系统能力：** SystemCapability.Notification.ReminderAgent

| 名称 | 值 | 说明 |
| --- | --- | --- |
| REMINDER\_TYPE\_TIMER | 0 | 表示提醒类型：倒计时。 |
| REMINDER\_TYPE\_CALENDAR | 1 | 表示提醒类型：日历。 |
| REMINDER\_TYPE\_ALARM | 2 | 表示提醒类型：闹钟。 |

## RingChannel20+

PhonePC/2in1TabletTVWearable

自定义提示音的音频播放通道。

**系统能力：** SystemCapability.Notification.ReminderAgent

| 名称 | 值 | 说明 |
| --- | --- | --- |
| RING\_CHANNEL\_ALARM | 0 | 闹钟通道。 |
| RING\_CHANNEL\_MEDIA | 1 | 媒体通道。 |
| RING\_CHANNEL\_NOTIFICATION23+ | 2 | 通知通道。 |

## ActionButton

PhonePC/2in1TabletTVWearable

弹出的提醒中按钮的类型和标题。

**系统能力：** SystemCapability.Notification.ReminderAgent

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| title | string | 否 | 否 | 按钮显示的标题。 |
| titleResource11+ | string | 否 | 是 | 标题的资源ID，用于切换系统语言后读取对应标题信息。 |
| type | [ActionButtonType](js-apis-reminderagentmanager.md#actionbuttontype) | 否 | 否 | 按钮的类型。 |

## WantAgent

PhonePC/2in1TabletTVWearable

跳转目标的ability信息。

**系统能力：** SystemCapability.Notification.ReminderAgent

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| pkgName | string | 否 | 否 | 指明跳转目标的包名。 |
| abilityName | string | 否 | 否 | 指明跳转目标的ability名称。 |
| parameters12+ | Record<string, Object> | 否 | 是 | 需要传递到目标的参数。 |
| uri12+ | string | 否 | 是 | 指明跳转目标的uri信息。 |

## MaxScreenWantAgent

PhonePC/2in1TabletTVWearable

通知中心弹出提醒时，全屏显示自动拉起目标的ability信息。该接口为预留接口，暂不支持使用。

**系统能力：** SystemCapability.Notification.ReminderAgent

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| pkgName | string | 否 | 否 | 指明提醒到达时自动拉起的目标包名（如果设备在使用中，则只弹出通知横幅框）。 |
| abilityName | string | 否 | 否 | 指明提醒到达时自动拉起的目标ability名（如果设备在使用中，则只弹出通知横幅框）。 |

## ReminderRequest

PhonePC/2in1TabletTVWearable

代理提醒对象，用于设置提醒类型、响铃时长等具体信息。

**系统能力：** SystemCapability.Notification.ReminderAgent

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| reminderType | [ReminderType](js-apis-reminderagentmanager.md#remindertype) | 否 | 否 | 指明代理提醒类型。 |
| actionButton | [[ActionButton?, ActionButton?, ActionButton?]](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-reminderagentmanager#actionbutton) | 否 | 是 | 弹出的提醒通知中显示的按钮。  针对三方应用：最多支持两个按钮。  针对系统应用：从API version 10开始最多支持三个按钮，API version 10之前的版本最多支持两个按钮。 |
| wantAgent | [WantAgent](js-apis-reminderagentmanager.md#wantagent) | 否 | 是 | 点击通知后需要跳转的目标ability信息。 |
| maxScreenWantAgent | [MaxScreenWantAgent](js-apis-reminderagentmanager.md#maxscreenwantagent) | 否 | 是 | 提醒到达时，全屏显示自动拉起目标的ability信息。如果设备正在使用中，则弹出一个通知横幅框。  说明：该接口为预留接口，暂不支持使用。 |
| ringDuration | number | 否 | 是 | 指明响铃时长。  单位：s，默认1s，范围：[0, 1800]。  值为0时：跟随系统设置中的通知铃声。  值大于0时：如果设置了[ReminderRequest.customRingUri](js-apis-reminderagentmanager.md#reminderrequest)，则在指定的通道[ReminderRequest.ringChannel](js-apis-reminderagentmanager.md#reminderrequest)上响铃。否则使用代理提醒默认的自定义提示音。  响铃同时会触发振动，响铃时会快速振动一次。 |
| snoozeTimes | number | 否 | 是 | 指明延时提醒次数，默认0次（不适用于倒计时提醒类型）。 |
| timeInterval | number | 否 | 是 | 执行延时提醒间隔。  单位：s，最少30s（不适用于倒计时提醒类型）。 |
| title | string | 否 | 是 | 指明提醒标题。 |
| titleResourceId18+ | number | 否 | 是 | 指明提醒标题的资源ID，通过$r(资源名称).id方法获取。 |
| content | string | 否 | 是 | 指明提醒内容。 |
| contentResourceId18+ | number | 否 | 是 | 指明提醒内容的资源ID，通过$r(资源名称).id方法获取。 |
| expiredContent | string | 否 | 是 | 指明提醒过期后需要显示的内容。 |
| expiredContentResourceId18+ | number | 否 | 是 | 指明提醒过期后内容的资源ID，通过$r(资源名称).id方法获取。 |
| snoozeContent | string | 否 | 是 | 指明延时提醒时需要显示的内容（不适用于倒计时提醒类型）。 |
| snoozeContentResourceId18+ | number | 否 | 是 | 指明延时提醒内容的资源ID，通过$r(资源名称).id方法获取。 |
| notificationId | number | 否 | 是 | 指明提醒使用的通知的id号，需开发者传入，相同id号的提醒会覆盖，默认值为0。 |
| groupId11+ | string | 否 | 是 | 指明提醒使用相同的组id。相同组id中，一个提醒被点击不在提醒后，组内其他提醒也会被取消。 |
| slotType | [notification.SlotType](js-apis-notificationmanager.md#slottype) | 否 | 是 | 指明提醒的通道渠道类型。 |
| tapDismissed10+ | boolean | 否 | 是 | 通知是否自动清除，默认值为true，具体请参考[NotificationRequest.tapDismissed](js-apis-inner-notification-notificationrequest.md#notificationrequest-1)。  - true：点击通知消息或通知按钮后，自动删除当前通知。  - false：点击通知消息或通知按钮后，保留当前通知。 |
| autoDeletedTime10+ | number | 否 | 是 | 自动清除的时间。  数据格式：时间戳，单位：ms，具体请参考[NotificationRequest.autoDeletedTime](js-apis-inner-notification-notificationrequest.md#notificationrequest-1)。 |
| snoozeSlotType11+ | [notification.SlotType](js-apis-notificationmanager.md#slottype) | 否 | 是 | 指明延时提醒的通道渠道类型（不适用于倒计时提醒类型）。 |
| customRingUri11+ | string | 否 | 是 | 指明自定义提示音的uri，提示音文件必须放在resources/rawfile目录下，支持m4a、aac、mp3、ogg、wav、flac、amr等格式。 |
| ringChannel20+ | [RingChannel](js-apis-reminderagentmanager.md#ringchannel20) | 否 | 是 | 指明自定义提示音的音频播放通道，默认为闹钟通道。 |

## ReminderRequestCalendar

PhonePC/2in1TabletTVWearable

ReminderRequestCalendar extends ReminderRequest

日历实例对象，用于设置提醒的时间。

**系统能力：** SystemCapability.Notification.ReminderAgent

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| dateTime | [LocalDateTime](js-apis-reminderagentmanager.md#localdatetime) | 否 | 否 | 指明提醒的目标时间。 |
| repeatMonths | Array<number> | 否 | 是 | 指明重复提醒的月份，范围：[1, 12]，默认为空。需和repeatDays一起使用。 |
| repeatDays | Array<number> | 否 | 是 | 指明重复提醒的日期，范围：[1, 31]，默认为空。需和repeatMonths一起使用。 |
| daysOfWeek11+ | Array<number> | 否 | 是 | 指明每周哪几天需要重复提醒。范围为周一到周日，对应数字为1到7，默认为空。 |
| endDateTime12+ | [LocalDateTime](js-apis-reminderagentmanager.md#localdatetime) | 否 | 是 | 指明提醒的结束时间。 |

## ReminderRequestAlarm

PhonePC/2in1TabletTVWearable

ReminderRequestAlarm extends ReminderRequest

闹钟实例对象，用于设置提醒的时间。

**系统能力：** SystemCapability.Notification.ReminderAgent

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| hour | number | 否 | 否 | 指明提醒的目标时刻，范围：[0, 23]。 |
| minute | number | 否 | 否 | 指明提醒的目标分钟，范围：[0, 59]。 |
| daysOfWeek | Array<number> | 否 | 是 | 指明每周哪几天需要重复提醒。范围为周一到周日，对应数字为1到7，默认为空。 |

## ReminderRequestTimer

PhonePC/2in1TabletTVWearable

ReminderRequestTimer extends ReminderRequest

倒计时实例对象，用于设置提醒的时间。

**系统能力：** SystemCapability.Notification.ReminderAgent

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| triggerTimeInSeconds | number | 否 | 否 | 指明倒计时的秒数。  单位：s |

## LocalDateTime

PhonePC/2in1TabletTVWearable

用于日历类提醒设置时指定时间信息。

**系统能力：** SystemCapability.Notification.ReminderAgent

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| year | number | 否 | 否 | 年 |
| month | number | 否 | 否 | 月，取值范围是[1, 12]。 |
| day | number | 否 | 否 | 日，取值范围是[1, 31]。 |
| hour | number | 否 | 否 | 时，取值范围是[0, 23]。 |
| minute | number | 否 | 否 | 分，取值范围是[0, 59]。 |
| second | number | 否 | 是 | 秒，取值范围是[0, 59]。 |

## ReminderInfo12+

PhonePC/2in1TabletTVWearable

代理提醒信息，包含 ReminderRequest 和 ReminderId。

**系统能力：** SystemCapability.Notification.ReminderAgent

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| reminderId | number | 否 | 否 | 发布提醒后返回的id。 |
| reminderReq | [ReminderRequest](js-apis-reminderagentmanager.md#reminderrequest) | 否 | 否 | 代理提醒对象。 |

## ReminderState23+

PhonePC/2in1TabletTVWearable

代理提醒状态信息。状态信息会在如下两种情况发送通知：

1. 用户点击代理提醒的通知按钮时，如果应用进程存在，则会发送用户点击的按钮类型的通知给应用。如果应用未运行，则无法收到通知。
2. 由于第1点不能保证应用可以收到通知，因此应用注册新的回调函数时，会将该应用下所有用户点击的按钮类型回调给应用。状态信息最多保存30天，应用注册新的回调函数时或者超过30天未注册回调函数，会删除缓存的状态信息。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Notification.ReminderAgent

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| reminderId | number | 否 | 否 | 发布提醒后返回的id。 |
| buttonType | [ActionButtonType](js-apis-reminderagentmanager.md#actionbuttontype) | 否 | 否 | 按钮类型。 |
| isMessageResent | boolean | 否 | 否 | 信息是否为重复发送。  - false：信息首次发送。具体场景包括：用户点击代理提醒的通知按钮时，应用进程存在；用户点击代理提醒的通知按钮时，应用未运行，后续应用注册新的回调函数。  - true：信息重复发送，具体场景为：应用进程存在，用户点击代理提醒的通知按钮后，应用注册新的回调函数。 |
