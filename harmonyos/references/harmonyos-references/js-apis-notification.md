---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-notification
title: @ohos.notification (Notification模块)
breadcrumb: API参考 > 应用服务 > Notification Kit（用户通知服务） > ArkTS API > 已停止维护的接口 > @ohos.notification (Notification模块)
category: harmonyos-references
scraped_at: 2026-04-28T08:17:37+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:1ed1341d65ede8c07f7d141d3b782ccf654e764d1c3a30cada6581c37782a0ea
---

本模块提供通知管理的能力，包括发布、取消发布通知，创建、获取、移除通知通道，订阅、取消订阅通知，获取通知的使能状态、角标使能状态，获取通知的相关信息等。

说明

从API version 9开始，该模块不再维护，建议使用[@ohos.notificationManager](js-apis-notificationmanager.md)替代。

本模块首批接口从API version 7开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

通知订阅和取消订阅仅对系统应用开放。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import Notification from '@ohos.notification';
```

## Notification.publish

PhonePC/2in1TabletTVWearable

publish(request: NotificationRequest, callback: AsyncCallback<void>): void

发布通知（callback形式）。

**系统能力**：SystemCapability.Notification.Notification

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| request | [NotificationRequest](js-apis-notification.md#notificationrequest) | 是 | 用于设置要发布通知的内容和相关配置信息。 |
| callback | AsyncCallback<void> | 是 | 发布通知的回调方法。 |

**示例：**

```
1. import NotificationManager from '@ohos.notificationManager';
2. import Base from '@ohos.base';

4. // publish回调
5. let publishCallback = (err: Base.BusinessError) => {
6. if (err) {
7. console.error(`publish failed, code is ${err}`);
8. } else {
9. console.info("publish success");
10. }
11. }
12. // 通知Request对象
13. let notificationRequest: NotificationManager.NotificationRequest = {
14. id: 1,
15. content: {
16. contentType: Notification.ContentType.NOTIFICATION_CONTENT_BASIC_TEXT,
17. normal: {
18. title: "test_title",
19. text: "test_text",
20. additionalText: "test_additionalText"
21. }
22. }
23. };
24. Notification.publish(notificationRequest, publishCallback);
```

## Notification.publish

PhonePC/2in1TabletTVWearable

publish(request: NotificationRequest): Promise<void>

发布通知（Promise形式）。

**系统能力**：SystemCapability.Notification.Notification

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| request | [NotificationRequest](js-apis-notification.md#notificationrequest) | 是 | 用于设置要发布通知的内容和相关配置信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**示例：**

```
1. import NotificationManager from '@ohos.notificationManager';
2. import Base from '@ohos.base';

4. // 通知Request对象
5. let notificationRequest: NotificationManager.NotificationRequest = {
6. id: 1,
7. content: {
8. contentType: Notification.ContentType.NOTIFICATION_CONTENT_BASIC_TEXT,
9. normal: {
10. title: "test_title",
11. text: "test_text",
12. additionalText: "test_additionalText"
13. }
14. }
15. };
16. Notification.publish(notificationRequest).then(() => {
17. console.info("publish success");
18. }).catch((err: Base.BusinessError) => {
19. console.error(`publish failed, code is ${err}`);
20. });
```

## Notification.cancel

PhonePC/2in1TabletTVWearable

cancel(id: number, label: string, callback: AsyncCallback<void>): void

通过通知ID和通知标签取消已发布的通知（callback形式）。

**系统能力**：SystemCapability.Notification.Notification

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| id | number | 是 | 通知ID。 |
| label | string | 是 | 通知标签。 |
| callback | AsyncCallback<void> | 是 | 表示被指定的回调方法。 |

**示例：**

```
1. import Base from '@ohos.base';

3. // cancel回调
4. let cancelCallback = (err: Base.BusinessError) => {
5. if (err) {
6. console.error("cancel failed " + JSON.stringify(err));
7. } else {
8. console.info("cancel success");
9. }
10. }
11. Notification.cancel(0, "label", cancelCallback);
```

## Notification.cancel

PhonePC/2in1TabletTVWearable

cancel(id: number, label?: string): Promise<void>

取消与指定通知ID相匹配的已发布通知，label可以指定也可以不指定（Promise形式）。

**系统能力**：SystemCapability.Notification.Notification

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| id | number | 是 | 通知ID。 |
| label | string | 否 | 通知标签，默认为空。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**示例：**

```
1. import Base from '@ohos.base';

3. Notification.cancel(0).then(() => {
4. console.info("cancel success");
5. }).catch((err: Base.BusinessError) => {
6. console.error(`cancel failed, code is ${err}`);
7. });
```

## Notification.cancel

PhonePC/2in1TabletTVWearable

cancel(id: number, callback: AsyncCallback<void>): void

取消与指定通知ID相匹配的已发布通知（callback形式）。

**系统能力**：SystemCapability.Notification.Notification

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| id | number | 是 | 通知ID。 |
| callback | AsyncCallback<void> | 是 | 表示被指定的回调方法。 |

**示例：**

```
1. import Base from '@ohos.base';

3. // cancel回调
4. let cancelCallback = (err: Base.BusinessError) => {
5. if (err) {
6. console.error("cancel failed " + JSON.stringify(err));
7. } else {
8. console.info("cancel success");
9. }
10. }
11. Notification.cancel(0, cancelCallback);
```

## Notification.cancelAll

PhonePC/2in1TabletTVWearable

cancelAll(callback: AsyncCallback<void>): void

取消所有已发布的通知（callback形式）。

**系统能力**：SystemCapability.Notification.Notification

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<void> | 是 | 表示被指定的回调方法。 |

**示例：**

```
1. import Base from '@ohos.base';

3. // cancel回调
4. let cancelAllCallback = (err: Base.BusinessError) => {
5. if (err) {
6. console.error("cancelAll failed " + JSON.stringify(err));
7. } else {
8. console.info("cancelAll success");
9. }
10. }
11. Notification.cancelAll(cancelAllCallback);
```

## Notification.cancelAll

PhonePC/2in1TabletTVWearable

cancelAll(): Promise<void>

取消所有已发布的通知（Promise形式）。

**系统能力**：SystemCapability.Notification.Notification

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**示例：**

```
1. import Base from '@ohos.base';

3. Notification.cancelAll().then(() => {
4. console.info("cancelAll success");
5. }).catch((err: Base.BusinessError) => {
6. console.error(`cancelAll failed, code is ${err}`);
7. });
```

## Notification.addSlot

PhonePC/2in1TabletTVWearable

addSlot(type: SlotType, callback: AsyncCallback<void>): void

创建指定类型的通知通道（callback形式）。

**系统能力**：SystemCapability.Notification.Notification

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [SlotType](js-apis-notification.md#slottype) | 是 | 要创建的通知通道的类型。 |
| callback | AsyncCallback<void> | 是 | 表示被指定的回调方法。 |

**示例：**

```
1. import Base from '@ohos.base';

3. // addslot回调
4. let addSlotCallBack = (err: Base.BusinessError) => {
5. if (err) {
6. console.error("addSlot failed " + JSON.stringify(err));
7. } else {
8. console.info("addSlot success");
9. }
10. }
11. Notification.addSlot(Notification.SlotType.SOCIAL_COMMUNICATION, addSlotCallBack);
```

## Notification.addSlot

PhonePC/2in1TabletTVWearable

addSlot(type: SlotType): Promise<void>

创建指定类型的通知通道（Promise形式）。

**系统能力**：SystemCapability.Notification.Notification

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [SlotType](js-apis-notification.md#slottype) | 是 | 要创建的通知通道的类型。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**示例：**

```
1. import Base from '@ohos.base';

3. Notification.addSlot(Notification.SlotType.SOCIAL_COMMUNICATION).then(() => {
4. console.info("addSlot success");
5. }).catch((err: Base.BusinessError) => {
6. console.error(`addSlot failed, code is ${err}`);
7. });
```

## Notification.getSlot

PhonePC/2in1TabletTVWearable

getSlot(slotType: SlotType, callback: AsyncCallback<NotificationSlot>): void

获取一个指定类型的通知通道（callback形式）。

**系统能力**：SystemCapability.Notification.Notification

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| slotType | [SlotType](js-apis-notification.md#slottype) | 是 | 通知渠道类型，目前分为社交通信、服务提醒、内容咨询和其他类型。 |
| callback | AsyncCallback<[NotificationSlot](js-apis-notification.md#notificationslot)> | 是 | 表示被指定的回调方法。 |

**示例：**

```
1. import Base from '@ohos.base';

3. // getSlot回调
4. let getSlotCallback = (err: Base.BusinessError) => {
5. if (err) {
6. console.error("getSlot failed " + JSON.stringify(err));
7. } else {
8. console.info("getSlot success");
9. }
10. }
11. let slotType: Notification.SlotType = Notification.SlotType.SOCIAL_COMMUNICATION;
12. Notification.getSlot(slotType, getSlotCallback);
```

## Notification.getSlot

PhonePC/2in1TabletTVWearable

getSlot(slotType: SlotType): Promise<NotificationSlot>

获取一个指定类型的通知通道（Promise形式）。

**系统能力**：SystemCapability.Notification.Notification

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| slotType | [SlotType](js-apis-notification.md#slottype) | 是 | 通知渠道类型，目前分为社交通信、服务提醒、内容咨询和其他类型。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<NotificationSlot> | 以Promise形式返回获取一个通知通道。 |

**示例：**

```
1. import Base from '@ohos.base';

3. let slotType: Notification.SlotType = Notification.SlotType.SOCIAL_COMMUNICATION;
4. Notification.getSlot(slotType).then((data) => {
5. console.info("getSlot success, data: " + JSON.stringify(data));
6. }).catch((err: Base.BusinessError) => {
7. console.error(`getSlot failed, code is ${err}`);
8. });
```

## Notification.getSlots

PhonePC/2in1TabletTVWearable

getSlots(callback: AsyncCallback<Array<NotificationSlot>>): void

获取此应用程序的所有通知通道（callback形式）。

**系统能力**：SystemCapability.Notification.Notification

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<Array<[NotificationSlot](js-apis-notification.md#notificationslot)>> | 是 | 以callback形式返回获取此应用程序的所有通知通道的结果。 |

**示例：**

```
1. import Base from '@ohos.base';

3. // getSlots回调
4. function getSlotsCallback(err: Base.BusinessError) {
5. if (err) {
6. console.error("getSlots failed " + JSON.stringify(err));
7. } else {
8. console.info("getSlots success");
9. }
10. }
11. Notification.getSlots(getSlotsCallback);
```

## Notification.getSlots

PhonePC/2in1TabletTVWearable

getSlots(): Promise<Array<NotificationSlot>>

获取此应用程序的所有通知通道（Promise形式）。

**系统能力**：SystemCapability.Notification.Notification

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<[NotificationSlot](js-apis-notification.md#notificationslot)>> | 以Promise形式返回获取此应用程序的所有通知通道的结果。 |

**示例：**

```
1. import Base from '@ohos.base';

3. Notification.getSlots().then((data) => {
4. console.info("getSlots success, data: " + JSON.stringify(data));
5. }).catch((err: Base.BusinessError) => {
6. console.error(`getSlots failed, code is ${err}`);
7. });
```

## Notification.removeSlot

PhonePC/2in1TabletTVWearable

removeSlot(slotType: SlotType, callback: AsyncCallback<void>): void

删除指定类型的通知通道（callback形式）。

**系统能力**：SystemCapability.Notification.Notification

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| slotType | [SlotType](js-apis-notification.md#slottype) | 是 | 通知渠道类型,目前分为社交通信、服务提醒、内容咨询和其他类型。 |
| callback | AsyncCallback<void> | 是 | 表示被指定的回调方法。 |

**示例：**

```
1. import Base from '@ohos.base';

3. // removeSlot回调
4. let removeSlotCallback = (err: Base.BusinessError) => {
5. if (err) {
6. console.error("removeSlot failed " + JSON.stringify(err));
7. } else {
8. console.info("removeSlot success");
9. }
10. }
11. let slotType: Notification.SlotType = Notification.SlotType.SOCIAL_COMMUNICATION;
12. Notification.removeSlot(slotType, removeSlotCallback);
```

## Notification.removeSlot

PhonePC/2in1TabletTVWearable

removeSlot(slotType: SlotType): Promise<void>

删除指定类型的通知通道（Promise形式）。

**系统能力**：SystemCapability.Notification.Notification

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| slotType | [SlotType](js-apis-notification.md#slottype) | 是 | 通知渠道类型,目前分为社交通信、服务提醒、内容咨询和其他类型。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**示例：**

```
1. import Base from '@ohos.base';

3. let slotType: Notification.SlotType = Notification.SlotType.SOCIAL_COMMUNICATION;
4. Notification.removeSlot(slotType).then(() => {
5. console.info("removeSlot success");
6. }).catch((err: Base.BusinessError) => {
7. console.error(`removeSlot failed, code is ${err}`);
8. });
```

## Notification.removeAllSlots

PhonePC/2in1TabletTVWearable

removeAllSlots(callback: AsyncCallback<void>): void

删除所有通知通道（callback形式）。

**系统能力**：SystemCapability.Notification.Notification

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<void> | 是 | 表示被指定的回调方法。 |

**示例：**

```
1. import Base from '@ohos.base';

3. let removeAllCallBack = (err: Base.BusinessError) => {
4. if (err) {
5. console.error("removeAllSlots failed " + JSON.stringify(err));
6. } else {
7. console.info("removeAllSlots success");
8. }
9. }
10. Notification.removeAllSlots(removeAllCallBack);
```

## Notification.removeAllSlots

PhonePC/2in1TabletTVWearable

removeAllSlots(): Promise<void>

删除所有通知通道（Promise形式）。

**系统能力**：SystemCapability.Notification.Notification

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**示例：**

```
1. import Base from '@ohos.base';

3. Notification.removeAllSlots().then(() => {
4. console.info("removeAllSlots success");
5. }).catch((err: Base.BusinessError) => {
6. console.error(`removeAllSlots failed, code is ${err}`);
7. });
```

## Notification.getActiveNotificationCount

PhonePC/2in1TabletTVWearable

getActiveNotificationCount(callback: AsyncCallback<number>): void

获取当前应用未删除的通知数（Callback形式）。

**系统能力**：SystemCapability.Notification.Notification

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<number> | 是 | 获取未删除通知数回调函数。 |

**示例：**

```
1. import Base from '@ohos.base';

3. let getActiveNotificationCountCallback = (err: Base.BusinessError, data: number) => {
4. if (err) {
5. console.error("getActiveNotificationCount failed " + JSON.stringify(err));
6. } else {
7. console.info("getActiveNotificationCount success");
8. }
9. }

11. Notification.getActiveNotificationCount(getActiveNotificationCountCallback);
```

## Notification.getActiveNotificationCount

PhonePC/2in1TabletTVWearable

getActiveNotificationCount(): Promise<number>

获取当前应用未删除的通知数（Promise形式）。

**系统能力**：SystemCapability.Notification.Notification

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | 以Promise形式返回获取当前应用未删除通知数。 |

**示例：**

```
1. import Base from '@ohos.base';

3. Notification.getActiveNotificationCount().then((data: number) => {
4. console.info("getActiveNotificationCount success, data: " + JSON.stringify(data));
5. }).catch((err: Base.BusinessError) => {
6. console.error(`getActiveNotificationCount failed, code is ${err}`);
7. });
```

## Notification.getActiveNotifications

PhonePC/2in1TabletTVWearable

getActiveNotifications(callback: AsyncCallback<Array<NotificationRequest>>): void

获取当前应用未删除的通知列表（Callback形式）。

**系统能力**：SystemCapability.Notification.Notification

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<Array<[NotificationRequest](js-apis-notification.md#notificationrequest)>> | 是 | 获取当前应用通知列表回调函数。 |

**示例：**

```
1. import Base from '@ohos.base';
2. import NotificationManager from '@ohos.notificationManager';

4. let getActiveNotificationsCallback = (err: Base.BusinessError, data: NotificationManager.NotificationRequest[]) => {
5. if (err) {
6. console.error("getActiveNotifications failed " + JSON.stringify(err));
7. } else {
8. console.info("getActiveNotifications success");
9. }
10. }

12. Notification.getActiveNotifications(getActiveNotificationsCallback);
```

## Notification.getActiveNotifications

PhonePC/2in1TabletTVWearable

getActiveNotifications(): Promise<Array<[NotificationRequest](js-apis-notification.md#notificationrequest)>>

获取当前应用未删除的通知列表（Promise形式）。

**系统能力**：SystemCapability.Notification.Notification

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<[NotificationRequest](js-apis-notification.md#notificationrequest)>> | 以Promise形式返回获取当前应用通知列表。 |

**示例：**

```
1. import Base from '@ohos.base';
2. import NotificationManager from '@ohos.notificationManager';

4. Notification.getActiveNotifications().then((data: NotificationManager.NotificationRequest[]) => {
5. console.info("getActiveNotifications success, data: " + JSON.stringify(data));
6. }).catch((err: Base.BusinessError) => {
7. console.error(`getActiveNotifications failed, code is ${err}`);
8. });
```

## Notification.cancelGroup8+

PhonePC/2in1TabletTVWearable

cancelGroup(groupName: string, callback: AsyncCallback<void>): void

取消本应用指定组下的通知（Callback形式）。

**系统能力**：SystemCapability.Notification.Notification

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| groupName | string | 是 | 通知组名称，此名称需要在发布通知时通过[NotificationRequest](js-apis-notification.md#notificationrequest)对象指定。 |
| callback | AsyncCallback<void> | 是 | 取消本应用指定组下通知的回调函数。 |

**示例：**

```
1. import Base from '@ohos.base';

3. let cancelGroupCallback = (err: Base.BusinessError) => {
4. if (err) {
5. console.error("cancelGroup failed " + JSON.stringify(err));
6. } else {
7. console.info("cancelGroup success");
8. }
9. }

11. let groupName: string = "GroupName";

13. Notification.cancelGroup(groupName, cancelGroupCallback);
```

## Notification.cancelGroup8+

PhonePC/2in1TabletTVWearable

cancelGroup(groupName: string): Promise<void>

取消本应用指定组下的通知（Promise形式）。

**系统能力**：SystemCapability.Notification.Notification

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| groupName | string | 是 | 通知组名称。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**示例：**

```
1. import Base from '@ohos.base';

3. let groupName: string = "GroupName";
4. Notification.cancelGroup(groupName).then(() => {
5. console.info("cancelGroup success");
6. }).catch((err: Base.BusinessError) => {
7. console.error(`cancelGroup failed, code is ${err}`);
8. });
```

## Notification.isSupportTemplate8+

PhonePC/2in1TabletTVWearable

isSupportTemplate(templateName: string, callback: AsyncCallback<boolean>): void

查询模板是否存在（Callback形式）。

**系统能力**：SystemCapability.Notification.Notification

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| templateName | string | 是 | 模板名称。 |
| callback | AsyncCallback<boolean> | 是 | 查询模板是否存在的回调函数。 |

**示例：**

```
1. import Base from '@ohos.base';

3. let templateName: string = 'process';
4. function isSupportTemplateCallback(err: Base.BusinessError, data: boolean) {
5. if (err) {
6. console.error("isSupportTemplate failed " + JSON.stringify(err));
7. } else {
8. console.info("isSupportTemplate success");
9. }
10. }

12. Notification.isSupportTemplate(templateName, isSupportTemplateCallback);
```

## Notification.isSupportTemplate8+

PhonePC/2in1TabletTVWearable

isSupportTemplate(templateName: string): Promise<boolean>

查询模板是否存在（Promise形式）。

**系统能力**：SystemCapability.Notification.Notification

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| templateName | string | 是 | 模板名称。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise方式返回模板是否存在的结果。 |

**示例：**

```
1. import Base from '@ohos.base';

3. let templateName: string = 'process';
4. Notification.isSupportTemplate(templateName).then((data: boolean) => {
5. console.info("isSupportTemplate success, data: " + JSON.stringify(data));
6. }).catch((err: Base.BusinessError) => {
7. console.error(`isSupportTemplate failed, code is ${err}`);
8. });
```

## Notification.requestEnableNotification8+

PhonePC/2in1TabletTVWearable

requestEnableNotification(callback: AsyncCallback<void>): void

应用请求通知使能（Callback形式）。

**系统能力**：SystemCapability.Notification.Notification

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<void> | 是 | 应用请求通知使能的回调函数。 |

**示例：**

```
1. import Base from '@ohos.base';

3. let requestEnableNotificationCallback = (err: Base.BusinessError) => {
4. if (err) {
5. console.error("requestEnableNotification failed " + JSON.stringify(err));
6. } else {
7. console.info("requestEnableNotification success");
8. }
9. };

11. Notification.requestEnableNotification(requestEnableNotificationCallback);
```

## Notification.requestEnableNotification8+

PhonePC/2in1TabletTVWearable

requestEnableNotification(): Promise<void>

应用请求通知使能（Promise形式）。

**系统能力**：SystemCapability.Notification.Notification

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**示例：**

```
1. import Base from '@ohos.base';

3. Notification.requestEnableNotification().then(() => {
4. console.info("requestEnableNotification success");
5. }).catch((err: Base.BusinessError) => {
6. console.error(`requestEnableNotification failed, code is ${err}`);
7. });
```

## Notification.isDistributedEnabled8+

PhonePC/2in1TabletTVWearable

isDistributedEnabled(callback: AsyncCallback<boolean>): void

查询设备是否支持分布式通知（Callback形式）。

**系统能力**：SystemCapability.Notification.Notification

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<boolean> | 是 | 设备是否支持分布式通知的回调函数。 |

**示例：**

```
1. import Base from '@ohos.base';

3. let isDistributedEnabledCallback = (err: Base.BusinessError, data: boolean) => {
4. if (err) {
5. console.error("isDistributedEnabled failed " + JSON.stringify(err));
6. } else {
7. console.info("isDistributedEnabled success " + JSON.stringify(data));
8. }
9. };

11. Notification.isDistributedEnabled(isDistributedEnabledCallback);
```

## Notification.isDistributedEnabled8+

PhonePC/2in1TabletTVWearable

isDistributedEnabled(): Promise<boolean>

查询设备是否支持分布式通知（Promise形式）。

**系统能力**：SystemCapability.Notification.Notification

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise方式返回设备是否支持分布式通知的结果。 |

**示例：**

```
1. import Base from '@ohos.base';

3. Notification.isDistributedEnabled().then((data: boolean) => {
4. console.info("isDistributedEnabled success, data: " + JSON.stringify(data));
5. }).catch((err: Base.BusinessError) => {
6. console.error(`isDistributedEnabled failed, code is ${err}`);
7. });
```

## ContentType

PhonePC/2in1TabletTVWearable

**系统能力**：SystemCapability.Notification.Notification

| 名称 | 值 | 说明 |
| --- | --- | --- |
| NOTIFICATION\_CONTENT\_BASIC\_TEXT | NOTIFICATION\_CONTENT\_BASIC\_TEXT | 普通类型通知。 |
| NOTIFICATION\_CONTENT\_LONG\_TEXT | NOTIFICATION\_CONTENT\_LONG\_TEXT | 长文本类型通知。 |
| NOTIFICATION\_CONTENT\_PICTURE | NOTIFICATION\_CONTENT\_PICTURE | 图片类型通知。 |
| NOTIFICATION\_CONTENT\_CONVERSATION | NOTIFICATION\_CONTENT\_CONVERSATION | 社交类型通知。 |
| NOTIFICATION\_CONTENT\_MULTILINE | NOTIFICATION\_CONTENT\_MULTILINE | 多行文本类型通知。 |

## SlotLevel

PhonePC/2in1TabletTVWearable

**系统能力**：SystemCapability.Notification.Notification

| 名称 | 值 | 说明 |
| --- | --- | --- |
| LEVEL\_NONE | 0 | 表示关闭通知功能。 |
| LEVEL\_MIN | 1 | 表示通知功能已启用，但状态栏中不显示通知图标，且没有横幅或提示音。 |
| LEVEL\_LOW | 2 | 表示通知功能已启用，且状态栏中显示通知图标，但没有横幅或提示音。 |
| LEVEL\_DEFAULT | 3 | 表示通知功能已启用，状态栏中显示通知图标，没有横幅但有提示音。 |
| LEVEL\_HIGH | 4 | 表示通知功能已启用，状态栏中显示通知图标，有横幅和提示音。 |

## BundleOptiondeprecated

PhonePC/2in1TabletTVWearable

**系统能力**：SystemCapability.Notification.Notification

说明

从 API version 7开始支持，从API version 9开始废弃。建议使用[notificationManager.BundleOption](js-apis-inner-notification-notificationcommondef.md#bundleoption)替代。

| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| bundle | string | 是 | 应用的包信息。 |
| uid | number | 否 | 用户ID，默认为0。 |

## NotificationKeydeprecated

PhonePC/2in1TabletTVWearable

**系统能力**：SystemCapability.Notification.Notification

说明

从 API version 7开始支持，从API version 9开始废弃。

| 名称 | 类型 | 可读 | 可写 | 说明 |
| --- | --- | --- | --- | --- |
| id | number | 是 | 是 | 通知ID。 |
| label | string | 是 | 是 | 通知标签。 |

## SlotType

PhonePC/2in1TabletTVWearable

**系统能力**：SystemCapability.Notification.Notification

| 名称 | 值 | 说明 |
| --- | --- | --- |
| UNKNOWN\_TYPE | 0 | 未知类型。 |
| SOCIAL\_COMMUNICATION | 1 | 社交类型。 |
| SERVICE\_INFORMATION | 2 | 服务类型。 |
| CONTENT\_INFORMATION | 3 | 内容类型。 |
| OTHER\_TYPES | 0xFFFF | 其他类型。 |

## NotificationActionButton

PhonePC/2in1TabletTVWearable

描述通知中显示的操作按钮。

**系统能力**：SystemCapability.Notification.Notification

| 名称 | 类型 | 可读 | 可写 | 说明 |
| --- | --- | --- | --- | --- |
| title | string | 是 | 是 | 按钮标题。 |
| wantAgent | [WantAgent](js-apis-wantagent.md) | 是 | 是 | 点击按钮时触发的WantAgent。 |
| extras | { [key: string]: any } | 是 | 是 | 按钮扩展信息。 |
| userInput8+ | [NotificationUserInput](js-apis-notification.md#notificationuserinput8) | 是 | 是 | 用户输入对象实例。 |

## NotificationBasicContent

PhonePC/2in1TabletTVWearable

描述普通文本通知。

**系统能力**：SystemCapability.Notification.Notification

| 名称 | 类型 | 可读 | 可写 | 说明 |
| --- | --- | --- | --- | --- |
| title | string | 是 | 是 | 通知标题。 |
| text | string | 是 | 是 | 通知内容。 |
| additionalText | string | 是 | 是 | 通知附加内容，是对通知内容的补充。 |

## NotificationLongTextContent

PhonePC/2in1TabletTVWearable

描述长文本通知。

**系统能力**：SystemCapability.Notification.Notification

| 名称 | 类型 | 可读 | 可写 | 说明 |
| --- | --- | --- | --- | --- |
| title | string | 是 | 是 | 通知标题。 |
| text | string | 是 | 是 | 通知内容。 |
| additionalText | string | 是 | 是 | 通知附加内容，是对通知内容的补充。 |
| longText | string | 是 | 是 | 通知的长文本。 |
| briefText | string | 是 | 是 | 通知概要内容，是对通知内容的总结。 |
| expandedTitle | string | 是 | 是 | 通知展开时的标题。 |

## NotificationMultiLineContent

PhonePC/2in1TabletTVWearable

描述多行文本通知。

**系统能力**：SystemCapability.Notification.Notification

| 名称 | 类型 | 可读 | 可写 | 说明 |
| --- | --- | --- | --- | --- |
| title | string | 是 | 是 | 通知标题。 |
| text | string | 是 | 是 | 通知内容。 |
| additionalText | string | 是 | 是 | 通知附加内容，是对通知内容的补充。 |
| briefText | string | 是 | 是 | 通知概要内容，是对通知内容的总结。 |
| longTitle | string | 是 | 是 | 通知展开时的标题。 |
| lines | Array<string> | 是 | 是 | 通知的多行文本。 |

## NotificationPictureContent

PhonePC/2in1TabletTVWearable

描述附有图片的通知。

**系统能力**：SystemCapability.Notification.Notification

| 名称 | 类型 | 可读 | 可写 | 说明 |
| --- | --- | --- | --- | --- |
| title | string | 是 | 是 | 通知标题。 |
| text | string | 是 | 是 | 通知内容。 |
| additionalText | string | 是 | 是 | 通知附加内容，是对通知内容的补充。 |
| briefText | string | 是 | 是 | 通知概要内容，是对通知内容的总结。 |
| expandedTitle | string | 是 | 是 | 通知展开时的标题。 |
| picture | [image.PixelMap](arkts-apis-image-pixelmap.md) | 是 | 是 | 通知的图片内容。 |

## NotificationContent

PhonePC/2in1TabletTVWearable

描述通知类型。

**系统能力**：SystemCapability.Notification.Notification

| 名称 | 类型 | 可读 | 可写 | 说明 |
| --- | --- | --- | --- | --- |
| contentType | [notification.ContentType](js-apis-notification.md#contenttype) | 是 | 是 | 通知内容类型。 |
| normal | [NotificationBasicContent](js-apis-notification.md#notificationbasiccontent) | 是 | 是 | 基本类型通知内容。 |
| longText | [NotificationLongTextContent](js-apis-notification.md#notificationlongtextcontent) | 是 | 是 | 长文本类型通知内容。 |
| multiLine | [NotificationMultiLineContent](js-apis-notification.md#notificationmultilinecontent) | 是 | 是 | 多行类型通知内容。 |
| picture | [NotificationPictureContent](js-apis-notification.md#notificationpicturecontent) | 是 | 是 | 图片类型通知内容。 |

## NotificationRequest

PhonePC/2in1TabletTVWearable

描述通知的请求。

**系统能力**：SystemCapability.Notification.Notification

| 名称 | 类型 | 可读 | 可写 | 说明 |
| --- | --- | --- | --- | --- |
| content | [NotificationContent](js-apis-notification.md#notificationcontent) | 是 | 是 | 通知内容。 |
| id | number | 是 | 是 | 通知ID。 |
| slotType | [notification.SlotType](js-apis-notification.md#slottype) | 是 | 是 | 通道类型。 |
| isOngoing | boolean | 是 | 是 | 是否进行时通知。 |
| isUnremovable | boolean | 是 | 是 | 是否可移除。 |
| deliveryTime | number | 是 | 是 | 通知发送时间。 |
| tapDismissed | boolean | 是 | 是 | 通知是否自动清除。 |
| autoDeletedTime | number | 是 | 是 | 自动清除的时间。 |
| wantAgent | [WantAgent](js-apis-wantagent.md) | 是 | 是 | WantAgent封装了应用的行为意图，点击通知时触发该行为。 |
| extraInfo | {[key: string]: any} | 是 | 是 | 扩展参数。 |
| color | number | 是 | 是 | 通知背景颜色。预留能力，暂未支持。 |
| colorEnabled | boolean | 是 | 是 | 通知背景颜色是否使能。预留能力，暂未支持。 |
| isAlertOnce | boolean | 是 | 是 | 设置是否仅有一次此通知提醒。 |
| isStopwatch | boolean | 是 | 是 | 是否显示已用时间。 |
| isCountDown | boolean | 是 | 是 | 是否显示倒计时时间。 |
| isFloatingIcon | boolean | 是 | 是 | 是否显示状态栏图标。 |
| label | string | 是 | 是 | 通知标签。 |
| badgeIconStyle | number | 是 | 是 | 通知角标类型。 |
| showDeliveryTime | boolean | 是 | 是 | 是否显示分发时间。 |
| actionButtons | Array<[NotificationActionButton](js-apis-notification.md#notificationactionbutton)> | 是 | 是 | 通知按钮，最多两个按钮。 |
| smallIcon | [image.PixelMap](arkts-apis-image-pixelmap.md) | 是 | 是 | 通知小图标。可选字段，大小不超过30KB。 |
| largeIcon | [image.PixelMap](arkts-apis-image-pixelmap.md) | 是 | 是 | 通知大图标。可选字段，大小不超过30KB。 |
| creatorBundleName | string | 是 | 否 | 创建通知的包名。 |
| creatorUid | number | 是 | 否 | 创建通知的UID。 |
| creatorPid | number | 是 | 否 | 创建通知的PID。 |
| creatorUserId8+ | number | 是 | 否 | 创建通知的UserId。 |
| hashCode | string | 是 | 否 | 通知唯一标识。 |
| groupName8+ | string | 是 | 是 | 组通知名称。 |
| template8+ | [NotificationTemplate](js-apis-notification.md#notificationtemplate8) | 是 | 是 | 通知模板。 |
| distributedOption8+ | [DistributedOptions](js-apis-notification.md#distributedoptions8) | 是 | 是 | 分布式通知的选项。 |
| notificationFlags8+ | [NotificationFlags](js-apis-inner-notification-notificationflags.md) | 是 | 否 | 获取NotificationFlags。 |
| removalWantAgent9+ | [WantAgent](js-apis-wantagent.md) | 是 | 是 | 当移除通知时，通知将被重定向到的WantAgent实例。 |
| badgeNumber9+ | number | 是 | 是 | 应用程序图标上显示的通知数。 |

## DistributedOptions8+

PhonePC/2in1TabletTVWearable

描述分布式选项。

**系统能力**：SystemCapability.Notification.Notification

| 名称 | 类型 | 可读 | 可写 | 说明 |
| --- | --- | --- | --- | --- |
| isDistributed | boolean | 是 | 是 | 是否为分布式通知。 |
| supportDisplayDevices | Array<string> | 是 | 是 | 可以同步通知到的设备列表。 |
| supportOperateDevices | Array<string> | 是 | 是 | 可以打开通知的设备列表。 |

## NotificationSlot

PhonePC/2in1TabletTVWearable

描述通知槽

**系统能力**：SystemCapability.Notification.Notification

| 名称 | 类型 | 可读 | 可写 | 说明 |
| --- | --- | --- | --- | --- |
| type | [notification.SlotType](js-apis-notification.md#slottype) | 是 | 是 | 通道类型。 |
| level | [notification.SlotLevel](js-apis-notification.md#slotlevel) | 是 | 是 | 通知级别，不设置则根据通知渠道类型有默认值。 |
| desc | string | 是 | 是 | 通知渠道描述信息。 |
| badgeFlag | boolean | 是 | 是 | 是否显示角标。 |
| bypassDnd | boolean | 是 | 是 | 设置是否在系统中绕过免打扰模式。 |
| lockscreenVisibility | number | 是 | 是 | 在锁定屏幕上显示通知的模式。 |
| vibrationEnabled | boolean | 是 | 是 | 是否可振动。 |
| sound | string | 是 | 是 | 通知提示音。 |
| lightEnabled | boolean | 是 | 是 | 是否闪灯。 |
| lightColor | number | 是 | 是 | 通知灯颜色。 |
| vibrationValues | Array<number> | 是 | 是 | 通知振动样式。 |
| enabled9+ | boolean | 是 | 否 | 此通知插槽中的启停状态。 |

## NotificationTemplate8+

PhonePC/2in1TabletTVWearable

通知模板。

**系统能力**：SystemCapability.Notification.Notification

| 名称 | 类型 | 可读 | 可写 | 说明 |
| --- | --- | --- | --- | --- |
| name | string | 是 | 是 | 模板名称。 |
| data | Record<string, Object> | 是 | 是 | 模板数据。 |

## NotificationUserInput8+

PhonePC/2in1TabletTVWearable

保存用户输入的通知消息。

**系统能力**：SystemCapability.Notification.Notification

| 名称 | 类型 | 可读 | 可写 | 说明 |
| --- | --- | --- | --- | --- |
| inputKey | string | 是 | 是 | 用户输入时用于标识此输入的key。 |
