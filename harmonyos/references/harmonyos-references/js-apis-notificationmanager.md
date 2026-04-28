---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-notificationmanager
title: @ohos.notificationManager (NotificationManager模块)
breadcrumb: API参考 > 应用服务 > Notification Kit（用户通知服务） > ArkTS API > @ohos.notificationManager (NotificationManager模块)
category: harmonyos-references
scraped_at: 2026-04-28T08:17:33+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:71fc1e51e8d27f02330aa71733009ac2cbe83cd078295a0d5a2e596220c98b54
---

本模块提供通知管理的能力，包括发布、更新、取消通知，创建、获取、移除通知渠道，获取发布通知应用的使能状态，获取通知的相关信息等。

说明

本模块首批接口从API version 9开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { notificationManager } from '@kit.NotificationKit';
```

## notificationManager.publish

PhonePC/2in1TabletTVWearable

publish(request: NotificationRequest, callback: AsyncCallback<void>): void

发布通知。使用callback异步回调。

如果新发布通知与已发布通知的ID和标签都相同，则新通知将取代原有通知。

**系统能力**：SystemCapability.Notification.Notification

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| request | [NotificationRequest](js-apis-inner-notification-notificationrequest.md#notificationrequest-1) | 是 | 设置发布通知的内容和相关配置信息。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当发布通知成功，err为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)、[通知错误码](errorcode-notification.md)、[HTTP错误码](errorcode-net-http.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |
| 1600001 | Internal error. |
| 1600002 | Marshalling or unmarshalling error. |
| 1600003 | Failed to connect to the service. |
| 1600004 | Notification disabled. |
| 1600005 | Notification slot disabled. |
| 1600007 | The notification does not exist. |
| 1600009 | The notification sending frequency reaches the upper limit. |
| 1600012 | No memory space. |
| 1600014 | No permission. |
| 1600015 | The current notification status does not support duplicate configurations. |
| 1600016 | The notification version for this update is too low. |
| 1600020 | The application is not allowed to send notifications due to permission settings. |
| 2300007 | Network unreachable. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. // publish回调
4. let publishCallback = (err: BusinessError): void => {
5. if (err) {
6. console.error(`Failed to publish notification. Code is ${err.code}, message is ${err.message}`);
7. } else {
8. console.info(`Succeeded in publishing notification.`);
9. }
10. }
11. // 通知Request对象
12. let notificationRequest: notificationManager.NotificationRequest = {
13. id: 1,
14. content: {
15. notificationContentType: notificationManager.ContentType.NOTIFICATION_CONTENT_BASIC_TEXT,
16. normal: {
17. title: "test_title",
18. text: "test_text",
19. additionalText: "test_additionalText"
20. }
21. }
22. };
23. notificationManager.publish(notificationRequest, publishCallback);
```

## notificationManager.publish

PhonePC/2in1TabletTVWearable

publish(request: NotificationRequest): Promise<void>

发布通知。使用Promise异步回调。

如果新发布通知与已发布通知的ID和标签都相同，则新通知将取代原有通知。

**系统能力**：SystemCapability.Notification.Notification

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| request | [NotificationRequest](js-apis-inner-notification-notificationrequest.md#notificationrequest-1) | 是 | 设置发布通知的内容和相关配置信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)、[通知错误码](errorcode-notification.md)、[HTTP错误码](errorcode-net-http.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |
| 1600001 | Internal error. |
| 1600002 | Marshalling or unmarshalling error. |
| 1600003 | Failed to connect to the service. |
| 1600004 | Notification disabled. |
| 1600005 | Notification slot disabled. |
| 1600007 | The notification does not exist. |
| 1600009 | The notification sending frequency reaches the upper limit. |
| 1600012 | No memory space. |
| 1600014 | No permission. |
| 1600015 | The current notification status does not support duplicate configurations. |
| 1600016 | The notification version for this update is too low. |
| 1600020 | The application is not allowed to send notifications due to permission settings. |
| 2300007 | Network unreachable. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. // 通知Request对象
4. let notificationRequest: notificationManager.NotificationRequest = {
5. id: 1,
6. content: {
7. notificationContentType: notificationManager.ContentType.NOTIFICATION_CONTENT_BASIC_TEXT,
8. normal: {
9. title: "test_title",
10. text: "test_text",
11. additionalText: "test_additionalText"
12. }
13. }
14. };
15. notificationManager.publish(notificationRequest).then(() => {
16. console.info(`Succeeded in publishing notification.`);
17. }).catch((err: BusinessError) => {
18. console.error(`Failed to publish notification. Code is ${err.code}, message is ${err.message}`);
19. });
```

## notificationManager.cancel

PhonePC/2in1TabletTVWearable

cancel(id: number, label: string, callback: AsyncCallback<void>): void

根据通知ID和标签取消已发布的通知。使用callback异步回调。

**系统能力**：SystemCapability.Notification.Notification

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| id | number | 是 | 通知ID。 |
| label | string | 是 | 通知标签。 |
| callback | AsyncCallback<void> | 是 | 回调函数。根据通知ID和标签取消已发布的通知成功，err为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[通知错误码](errorcode-notification.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |
| 1600001 | Internal error. |
| 1600002 | Marshalling or unmarshalling error. |
| 1600003 | Failed to connect to the service. |
| 1600007 | The notification does not exist. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. // cancel回调
4. let cancelCallback = (err: BusinessError): void => {
5. if (err) {
6. console.error(`Failed to cancel notification. Code is ${err.code}, message is ${err.message}`);
7. } else {
8. console.info(`Succeeded in canceling notification.`);
9. }
10. }
11. notificationManager.cancel(0, "label", cancelCallback);
```

## notificationManager.cancel

PhonePC/2in1TabletTVWearable

cancel(id: number, label?: string): Promise<void>

根据通知ID和标签取消已发布的通知，若标签为空，则取消与指定通知ID匹配的已发布通知。使用Promise异步回调。

**系统能力**：SystemCapability.Notification.Notification

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| id | number | 是 | 通知ID。 |
| label | string | 否 | 通知标签，默认为空。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[通知错误码](errorcode-notification.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |
| 1600001 | Internal error. |
| 1600002 | Marshalling or unmarshalling error. |
| 1600003 | Failed to connect to the service. |
| 1600007 | The notification does not exist. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. notificationManager.cancel(0).then(() => {
4. console.info(`Succeeded in canceling notification.`);
5. }).catch((err: BusinessError) => {
6. console.error(`Failed to cancel notification. Code is ${err.code}, message is ${err.message}`);
7. });
```

## notificationManager.cancel

PhonePC/2in1TabletTVWearable

cancel(id: number, callback: AsyncCallback<void>): void

根据指定的通知ID取消已发布的通知。使用callback异步回调。

**系统能力**：SystemCapability.Notification.Notification

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| id | number | 是 | 通知ID。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当取消已发布的通知成功，err为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[通知错误码](errorcode-notification.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |
| 1600001 | Internal error. |
| 1600002 | Marshalling or unmarshalling error. |
| 1600003 | Failed to connect to the service. |
| 1600007 | The notification does not exist. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. // cancel回调
4. let cancelCallback = (err: BusinessError): void => {
5. if (err) {
6. console.error(`Failed to cancel notification. Code is ${err.code}, message is ${err.message}`);
7. } else {
8. console.info(`Succeeded in canceling notification.`);
9. }
10. }
11. notificationManager.cancel(0, cancelCallback);
```

## notificationManager.cancelAll

PhonePC/2in1TabletTVWearable

cancelAll(callback: AsyncCallback<void>): void

取消当前应用所有已发布的通知。使用callback异步回调。

**系统能力**：SystemCapability.Notification.Notification

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<void> | 是 | 回调函数。当取消当前应用所有已发布的通知成功，err为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[通知错误码](errorcode-notification.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |
| 1600001 | Internal error. |
| 1600002 | Marshalling or unmarshalling error. |
| 1600003 | Failed to connect to the service. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. // cancel回调
4. let cancelAllCallback = (err: BusinessError): void => {
5. if (err) {
6. console.error(`Failed to cancel all notification. Code is ${err.code}, message is ${err.message}`);
7. } else {
8. console.info(`Succeeded in canceling all notification.`);
9. }
10. }
11. notificationManager.cancelAll(cancelAllCallback);
```

## notificationManager.cancelAll

PhonePC/2in1TabletTVWearable

cancelAll(): Promise<void>

取消当前应用所有已发布的通知。使用Promise异步回调。

**系统能力**：SystemCapability.Notification.Notification

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通知错误码](errorcode-notification.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1600001 | Internal error. |
| 1600002 | Marshalling or unmarshalling error. |
| 1600003 | Failed to connect to the service. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. notificationManager.cancelAll().then(() => {
4. console.info(`Succeeded in canceling all notification.`);
5. }).catch((err: BusinessError) => {
6. console.error(`Failed to cancel all notification. Code is ${err.code}, message is ${err.message}`);
7. });
```

## notificationManager.addSlot

PhonePC/2in1TabletTVWearable

addSlot(type: SlotType, callback: AsyncCallback<void>): void

创建指定类型的通知渠道。使用callback异步回调。

**系统能力**：SystemCapability.Notification.Notification

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [SlotType](js-apis-notificationmanager.md#slottype) | 是 | 要创建的通知渠道的类型。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当创建指定类型的通知渠道成功，err为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[通知错误码](errorcode-notification.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |
| 1600001 | Internal error. |
| 1600002 | Marshalling or unmarshalling error. |
| 1600003 | Failed to connect to the service. |
| 1600012 | No memory space. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. // addSlot回调
4. let addSlotCallBack = (err: BusinessError): void => {
5. if (err) {
6. console.error(`Failed to add slot. Code is ${err.code}, message is ${err.message}`);
7. } else {
8. console.info(`Succeeded in adding slot.`);
9. }
10. }
11. notificationManager.addSlot(notificationManager.SlotType.SOCIAL_COMMUNICATION, addSlotCallBack);
```

## notificationManager.addSlot

PhonePC/2in1TabletTVWearable

addSlot(type: SlotType): Promise<void>

创建指定类型的通知渠道。使用Promise异步回调。

**系统能力**：SystemCapability.Notification.Notification

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [SlotType](js-apis-notificationmanager.md#slottype) | 是 | 要创建的通知渠道的类型。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[通知错误码](errorcode-notification.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |
| 1600001 | Internal error. |
| 1600002 | Marshalling or unmarshalling error. |
| 1600003 | Failed to connect to the service. |
| 1600012 | No memory space. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. notificationManager.addSlot(notificationManager.SlotType.SOCIAL_COMMUNICATION).then(() => {
4. console.info(`Succeeded in adding slot.`);
5. }).catch((err: BusinessError) => {
6. console.error(`Failed to add slot. Code is ${err.code}, message is ${err.message}`);
7. });
```

## notificationManager.getSlot

PhonePC/2in1TabletTVWearable

getSlot(slotType: SlotType, callback: AsyncCallback<NotificationSlot>): void

获取指定类型的通知渠道。使用callback异步回调。

**系统能力**：SystemCapability.Notification.Notification

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| slotType | [SlotType](js-apis-notificationmanager.md#slottype) | 是 | 通知渠道类型，例如社交通信、服务提醒、内容咨询等类型。 |
| callback | AsyncCallback<[NotificationSlot](js-apis-inner-notification-notificationslot.md)> | 是 | 回调函数。当获取通知渠道成功，err为undefined，data为获取到的NotificationSlot，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[通知错误码](errorcode-notification.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |
| 1600001 | Internal error. |
| 1600002 | Marshalling or unmarshalling error. |
| 1600003 | Failed to connect to the service. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. // getSlot回调
4. let getSlotCallback = (err: BusinessError, data: notificationManager.NotificationSlot): void => {
5. if (err) {
6. console.error(`Failed to get slot. Code is ${err.code}, message is ${err.message}`);
7. } else {
8. console.info(`Succeeded in getting slot, data is ${JSON.stringify(data)}`);
9. }
10. }
11. let slotType: notificationManager.SlotType = notificationManager.SlotType.SOCIAL_COMMUNICATION;
12. notificationManager.getSlot(slotType, getSlotCallback);
```

## notificationManager.getSlot

PhonePC/2in1TabletTVWearable

getSlot(slotType: SlotType): Promise<NotificationSlot>

获取指定类型的通知渠道。使用Promise异步回调。

**系统能力**：SystemCapability.Notification.Notification

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| slotType | [SlotType](js-apis-notificationmanager.md#slottype) | 是 | 通知渠道类型，例如社交通信、服务提醒、内容咨询等类型。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[NotificationSlot](js-apis-inner-notification-notificationslot.md)> | Promise对象，返回通知渠道对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[通知错误码](errorcode-notification.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |
| 1600001 | Internal error. |
| 1600002 | Marshalling or unmarshalling error. |
| 1600003 | Failed to connect to the service. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let slotType: notificationManager.SlotType = notificationManager.SlotType.SOCIAL_COMMUNICATION;
4. notificationManager.getSlot(slotType).then((data: notificationManager.NotificationSlot) => {
5. console.info(`Succeeded in getting slot, data is ${JSON.stringify(data)}`);
6. }).catch((err: BusinessError) => {
7. console.error(`Failed to get slot. Code is ${err.code}, message is ${err.message}`);
8. });
```

## notificationManager.getSlots

PhonePC/2in1TabletTVWearable

getSlots(callback: AsyncCallback<Array<NotificationSlot>>): void

获取当前应用的所有通知渠道。使用callback异步回调。

**系统能力**：SystemCapability.Notification.Notification

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<Array<[NotificationSlot](js-apis-inner-notification-notificationslot.md)>> | 是 | 回调函数。当获取通知渠道成功，err为undefined，data为获取到的NotificationSlot数组，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[通知错误码](errorcode-notification.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |
| 1600001 | Internal error. |
| 1600002 | Marshalling or unmarshalling error. |
| 1600003 | Failed to connect to the service. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. // getSlots回调
4. let getSlotsCallback = (err: BusinessError, data: Array<notificationManager.NotificationSlot>): void => {
5. if (err) {
6. console.error(`Failed to get slots. Code is ${err.code}, message is ${err.message}`);
7. } else {
8. console.info(`Succeeded in getting slots, data is ${JSON.stringify(data)}`);
9. }
10. }
11. notificationManager.getSlots(getSlotsCallback);
```

## notificationManager.getSlots

PhonePC/2in1TabletTVWearable

getSlots(): Promise<Array<NotificationSlot>>

获取当前应用的所有通知渠道。使用Promise异步回调。

**系统能力**：SystemCapability.Notification.Notification

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<[NotificationSlot](js-apis-inner-notification-notificationslot.md)>> | Promise对象，返回通知渠道对象。 |

**错误码：**

以下错误码的详细介绍请参见[通知错误码](errorcode-notification.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1600001 | Internal error. |
| 1600002 | Marshalling or unmarshalling error. |
| 1600003 | Failed to connect to the service. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. notificationManager.getSlots().then((data: Array<notificationManager.NotificationSlot>) => {
4. console.info(`Succeeded in getting slots, data is ${JSON.stringify(data)}`);
5. }).catch((err: BusinessError) => {
6. console.error(`Failed to get slots. Code is ${err.code}, message is ${err.message}`);
7. });
```

## notificationManager.removeSlot

PhonePC/2in1TabletTVWearable

removeSlot(slotType: SlotType, callback: AsyncCallback<void>): void

删除当前应用指定类型的通知渠道。使用callback异步回调。

**系统能力**：SystemCapability.Notification.Notification

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| slotType | [SlotType](js-apis-notificationmanager.md#slottype) | 是 | 通知渠道类型，例如社交通信、服务提醒、内容咨询等类型。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当删除指定类型的通知渠道成功，err为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[通知错误码](errorcode-notification.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |
| 1600001 | Internal error. |
| 1600002 | Marshalling or unmarshalling error. |
| 1600003 | Failed to connect to the service. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. // removeSlot回调
4. let removeSlotCallback = (err: BusinessError): void => {
5. if (err) {
6. console.error(`Failed to remove slot. Code is ${err.code}, message is ${err.message}`);
7. } else {
8. console.info(`Succeeded in removing slot.`);
9. }
10. }
11. let slotType: notificationManager.SlotType = notificationManager.SlotType.SOCIAL_COMMUNICATION;
12. notificationManager.removeSlot(slotType, removeSlotCallback);
```

## notificationManager.removeSlot

PhonePC/2in1TabletTVWearable

removeSlot(slotType: SlotType): Promise<void>

删除当前应用指定类型的通知渠道。使用Promise异步回调。

**系统能力**：SystemCapability.Notification.Notification

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| slotType | [SlotType](js-apis-notificationmanager.md#slottype) | 是 | 通知渠道类型，例如社交通信、服务提醒、内容咨询等类型。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[通知错误码](errorcode-notification.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |
| 1600001 | Internal error. |
| 1600002 | Marshalling or unmarshalling error. |
| 1600003 | Failed to connect to the service. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let slotType: notificationManager.SlotType = notificationManager.SlotType.SOCIAL_COMMUNICATION;
4. notificationManager.removeSlot(slotType).then(() => {
5. console.info(`Succeeded in removing slot.`);
6. }).catch((err: BusinessError) => {
7. console.error(`Failed to remove slot. Code is ${err.code}, message is ${err.message}`);
8. });
```

## notificationManager.removeAllSlots

PhonePC/2in1TabletTVWearable

removeAllSlots(callback: AsyncCallback<void>): void

删除当前应用所有通知渠道。使用callback异步回调。

**系统能力**：SystemCapability.Notification.Notification

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<void> | 是 | 回调函数。当删除当前应用所有通知渠道成功，err为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[通知错误码](errorcode-notification.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |
| 1600001 | Internal error. |
| 1600002 | Marshalling or unmarshalling error. |
| 1600003 | Failed to connect to the service. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let removeAllSlotsCallback = (err: BusinessError): void => {
4. if (err) {
5. console.error(`Failed to remove all slots. Code is ${err.code}, message is ${err.message}`);
6. } else {
7. console.info(`Succeeded in removing all slots.`);
8. }
9. }
10. notificationManager.removeAllSlots(removeAllSlotsCallback);
```

## notificationManager.removeAllSlots

PhonePC/2in1TabletTVWearable

removeAllSlots(): Promise<void>

删除当前应用所有通知渠道。使用Promise异步回调。

**系统能力**：SystemCapability.Notification.Notification

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通知错误码](errorcode-notification.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1600001 | Internal error. |
| 1600002 | Marshalling or unmarshalling error. |
| 1600003 | Failed to connect to the service. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. notificationManager.removeAllSlots().then(() => {
4. console.info(`Succeeded in removing all slots.`);
5. }).catch((err: BusinessError) => {
6. console.error(`Failed to remove all slots. Code is ${err.code}, message is ${err.message}`);
7. });
```

## notificationManager.isNotificationEnabled11+

PhonePC/2in1TabletTVWearable

isNotificationEnabled(callback: AsyncCallback<boolean>): void

查询当前应用通知使能状态。使用callback异步回调。

**系统能力**：SystemCapability.Notification.Notification

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<boolean> | 是 | 回调函数。返回true，表示允许发布通知；返回false，表示禁止发布通知；调用失败返回错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)、[通知错误码](errorcode-notification.md)、[包管理子系统通用错误码](errorcode-bundle.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |
| 1600001 | Internal error. |
| 1600002 | Marshalling or unmarshalling error. |
| 1600003 | Failed to connect to the service. |
| 1600008 | The user does not exist. |
| 17700001 | The specified bundle name was not found. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let isNotificationEnabledCallback = (err: BusinessError, data: boolean): void => {
4. if (err) {
5. console.error(`isNotificationEnabled failed, code is ${err.code}, message is ${err.message}`);
6. } else {
7. console.info(`isNotificationEnabled success, data is ${JSON.stringify(data)}`);
8. }
9. }

11. notificationManager.isNotificationEnabled(isNotificationEnabledCallback);
```

## notificationManager.isNotificationEnabled11+

PhonePC/2in1TabletTVWearable

isNotificationEnabled(): Promise<boolean>

查询当前应用通知使能状态。使用Promise异步回调。

**系统能力**：SystemCapability.Notification.Notification

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象。返回true，表示允许发布通知；返回false，表示禁止发布通知。 |

**错误码：**

以下错误码的详细介绍请参见[通知错误码](errorcode-notification.md)、[包管理子系统通用错误码](errorcode-bundle.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1600001 | Internal error. |
| 1600002 | Marshalling or unmarshalling error. |
| 1600003 | Failed to connect to the service. |
| 1600008 | The user does not exist. |
| 17700001 | The specified bundle name was not found. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. notificationManager.isNotificationEnabled().then((data: boolean) => {
4. console.info(`isNotificationEnabled success, data: ${JSON.stringify(data)}`);
5. }).catch((err: BusinessError) => {
6. console.error(`isNotificationEnabled failed, code is ${err.code}, message is ${err.message}`);
7. });
```

## notificationManager.isNotificationEnabledSync12+

PhonePC/2in1TabletTVWearable

isNotificationEnabledSync(): boolean

同步查询当前应用通知使能状态。

**系统能力**：SystemCapability.Notification.Notification

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回查询通知使能状态的结果。返回true，表示允许发布通知；返回false，表示禁止发布通知。 |

**错误码：**

以下错误码的详细介绍请参见[通知错误码](errorcode-notification.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1600001 | Internal error. |
| 1600002 | Marshalling or unmarshalling error. |
| 1600003 | Failed to connect to the service. |

**示例：**

```
1. let enabled: boolean = notificationManager.isNotificationEnabledSync();
2. console.info(`isNotificationEnabledSync success, data is : ${JSON.stringify(enabled)}`);
```

## notificationManager.setBadgeNumber10+

PhonePC/2in1TabletTVWearable

setBadgeNumber(badgeNumber: number): Promise<void>

设定角标个数，在应用的桌面图标上呈现。使用Promise异步回调。

**系统能力**：SystemCapability.Notification.Notification

**设备行为差异**：该接口在Wearable中返回801错误码，在其他设备类型中可正常调用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| badgeNumber | number | 是 | 角标个数。当角标设定个数取值小于或等于0时，清除角标。取值大于99时，通知角标将显示99+。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[通知错误码](errorcode-notification.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |
| 801 | Capability not supported. |
| 1600001 | Internal error. |
| 1600002 | Marshalling or unmarshalling error. |
| 1600003 | Failed to connect to the service. |
| 1600012 | No memory space. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let badgeNumber: number = 10;
4. notificationManager.setBadgeNumber(badgeNumber).then(() => {
5. console.info(`Succeeded in setting badge number.`);
6. }).catch((err: BusinessError) => {
7. console.error(`Failed to set badge number. Code is ${err.code}, message is ${err.message}`);
8. });
```

## notificationManager.setBadgeNumber10+

PhonePC/2in1TabletTVWearable

setBadgeNumber(badgeNumber: number, callback: AsyncCallback<void>): void

设定角标个数，在应用的桌面图标上呈现。使用callback异步回调。

**系统能力**：SystemCapability.Notification.Notification

**设备行为差异**：该接口在Wearable中返回801错误码，在其他设备类型中可正常调用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| badgeNumber | number | 是 | 角标个数。当角标设定个数取值小于或等于0时，清除角标。取值大于99时，通知角标将显示99+。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当设定角标个数成功，err为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[通知错误码](errorcode-notification.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |
| 801 | Capability not supported. |
| 1600001 | Internal error. |
| 1600002 | Marshalling or unmarshalling error. |
| 1600003 | Failed to connect to the service. |
| 1600012 | No memory space. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let setBadgeNumberCallback = (err: BusinessError): void => {
4. if (err) {
5. console.error(`Failed to set badge number. Code is ${err.code}, message is ${err.message}`);
6. } else {
7. console.info(`Succeeded in setting badge number.`);
8. }
9. }
10. let badgeNumber: number = 10;
11. notificationManager.setBadgeNumber(badgeNumber, setBadgeNumberCallback);
```

## notificationManager.getBadgeNumber22+

PhonePC/2in1TabletTVWearable

getBadgeNumber(): Promise<number>

获取当前应用角标数量。使用Promise异步回调。

**系统能力**：SystemCapability.Notification.Notification

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象，返回当前应用角标数量。（查询的角标数量与当前应用通知开关，桌面角标开关是否开启无关） |

**错误码：**

以下错误码的详细介绍请参见[通知错误码](errorcode-notification.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1600001 | Internal error. |
| 1600002 | Marshalling or unmarshalling error. |
| 1600003 | Failed to connect to the service. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. notificationManager.getBadgeNumber().then((badgeNumber: number) => {
4. console.info(`Succeeded in getting badge number, badgeNumber is ${JSON.stringify(badgeNumber)}`);
5. }).catch((err: BusinessError) => {
6. console.error(`Failed to get badge number. Code is ${err.code}, message is ${err.message}`);
7. });
```

## notificationManager.getActiveNotificationCount

PhonePC/2in1TabletTVWearable

getActiveNotificationCount(callback: AsyncCallback<number>): void

获取当前应用未删除的通知数。使用callback异步回调。

**系统能力**：SystemCapability.Notification.Notification

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<number> | 是 | 回调函数。当获取当前应用未删除的通知数成功，err为undefined，data为当前应用未删除的通知数，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[通知错误码](errorcode-notification.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |
| 1600001 | Internal error. |
| 1600002 | Marshalling or unmarshalling error. |
| 1600003 | Failed to connect to the service. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let getActiveNotificationCountCallback = (err: BusinessError, data: number): void => {
4. if (err) {
5. console.error(`Failed to get active notification count. Code is ${err.code}, message is ${err.message}`);
6. } else {
7. console.info(`Succeeded in getting active notification count, data is ${JSON.stringify(data)}`);
8. }
9. }

11. notificationManager.getActiveNotificationCount(getActiveNotificationCountCallback);
```

## notificationManager.getActiveNotificationCount

PhonePC/2in1TabletTVWearable

getActiveNotificationCount(): Promise<number>

获取当前应用未删除的通知数。使用Promise异步回调。

**系统能力**：SystemCapability.Notification.Notification

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象，返回当前应用未删除通知数。 |

**错误码：**

以下错误码的详细介绍请参见[通知错误码](errorcode-notification.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1600001 | Internal error. |
| 1600002 | Marshalling or unmarshalling error. |
| 1600003 | Failed to connect to the service. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. notificationManager.getActiveNotificationCount().then((data: number) => {
4. console.info(`Succeeded in getting active notification count, data is ${JSON.stringify(data)}`);
5. }).catch((err: BusinessError) => {
6. console.error(`Failed to get active notification count. Code is ${err.code}, message is ${err.message}`);
7. });
```

## notificationManager.getActiveNotifications

PhonePC/2in1TabletTVWearable

getActiveNotifications(callback: AsyncCallback<Array<NotificationRequest>>): void

获取当前应用未删除的通知列表。使用callback异步回调。

**系统能力**：SystemCapability.Notification.Notification

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<Array<[NotificationRequest](js-apis-inner-notification-notificationrequest.md#notificationrequest-1)>> | 是 | 回调函数。当获取未删除的通知列表成功，err为undefined，data为获取到的通知列表，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[通知错误码](errorcode-notification.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |
| 1600001 | Internal error. |
| 1600002 | Marshalling or unmarshalling error. |
| 1600003 | Failed to connect to the service. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let getActiveNotificationsCallback = (err: BusinessError, data: Array<notificationManager.NotificationRequest>): void => {
4. if (err) {
5. console.error(`Failed to get active notifications. Code is ${err.code}, message is ${err.message}`);
6. } else {
7. console.info(`Succeeded in getting active notifications, data is ${JSON.stringify(data)}`);
8. }
9. }
10. notificationManager.getActiveNotifications(getActiveNotificationsCallback);
```

## notificationManager.getActiveNotifications

PhonePC/2in1TabletTVWearable

getActiveNotifications(): Promise<Array<NotificationRequest>>

获取当前应用未删除的通知列表。使用Promise异步回调。

**系统能力**：SystemCapability.Notification.Notification

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<[NotificationRequest](js-apis-inner-notification-notificationrequest.md#notificationrequest-1)>> | Promise对象，返回当前应用的通知列表。 |

**错误码：**

以下错误码的详细介绍请参见[通知错误码](errorcode-notification.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1600001 | Internal error. |
| 1600002 | Marshalling or unmarshalling error. |
| 1600003 | Failed to connect to the service. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. notificationManager.getActiveNotifications().then((data: Array<notificationManager.NotificationRequest>) => {
4. console.info(`Succeeded in getting active notifications, data is ${JSON.stringify(data)}`);
5. }).catch((err: BusinessError) => {
6. console.error(`Failed to get active notifications. Code is ${err.code}, message is ${err.message}`);
7. });
```

## notificationManager.cancelGroup

PhonePC/2in1TabletTVWearable

cancelGroup(groupName: string, callback: AsyncCallback<void>): void

取消当前应用指定组下的通知。使用callback异步回调。

**系统能力**：SystemCapability.Notification.Notification

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| groupName | string | 是 | 通知组名称，此名称需要在发布通知时通过[NotificationRequest](js-apis-inner-notification-notificationrequest.md#notificationrequest-1)对象指定。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当取消当前应用指定组下的通知成功，err为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[通知错误码](errorcode-notification.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |
| 1600001 | Internal error. |
| 1600002 | Marshalling or unmarshalling error. |
| 1600003 | Failed to connect to the service. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let cancelGroupCallback = (err: BusinessError): void => {
4. if (err) {
5. console.error(`Failed to cancel group. Code is ${err.code}, message is ${err.message}`);
6. } else {
7. console.info(`Succeeded in canceling group.`);
8. }
9. }
10. let groupName: string = "GroupName";
11. notificationManager.cancelGroup(groupName, cancelGroupCallback);
```

## notificationManager.cancelGroup

PhonePC/2in1TabletTVWearable

cancelGroup(groupName: string): Promise<void>

取消当前应用指定组下的通知。使用Promise异步回调。

**系统能力**：SystemCapability.Notification.Notification

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| groupName | string | 是 | 通知组名称，此名称需要在发布通知时通过[NotificationRequest](js-apis-inner-notification-notificationrequest.md#notificationrequest-1)对象指定。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[通知错误码](errorcode-notification.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |
| 1600001 | Internal error. |
| 1600002 | Marshalling or unmarshalling error. |
| 1600003 | Failed to connect to the service. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let groupName: string = "GroupName";
4. notificationManager.cancelGroup(groupName).then(() => {
5. console.info(`Succeeded in canceling group.`);
6. }).catch((err: BusinessError) => {
7. console.error(`Failed to cancel group. Code is ${err.code}, message is ${err.message}`);
8. });
```

## notificationManager.isSupportTemplate

PhonePC/2in1TabletTVWearable

isSupportTemplate(templateName: string, callback: AsyncCallback<boolean>): void

在使用[通知模板](js-apis-inner-notification-notificationtemplate.md)发布通知前，可以通过该接口查询是否支持对应的通知模板。使用callback异步回调。

**系统能力**：SystemCapability.Notification.Notification

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| templateName | string | 是 | 模板名称。当前仅支持'downloadTemplate'。 |
| callback | AsyncCallback<boolean> | 是 | 回调函数。返回true表示支持该模板；返回false表示不支持该模板；调用失败返回错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[通知错误码](errorcode-notification.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |
| 1600001 | Internal error. |
| 1600002 | Marshalling or unmarshalling error. |
| 1600003 | Failed to connect to the service. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let templateName: string = 'downloadTemplate';
4. let isSupportTemplateCallback = (err: BusinessError, data: boolean): void => {
5. if (err) {
6. console.error(`isSupportTemplate failed, code is ${err.code}, message is ${err.message}`);
7. } else {
8. console.info(`isSupportTemplate success, data: ${JSON.stringify(data)}`);
9. }
10. }
11. notificationManager.isSupportTemplate(templateName, isSupportTemplateCallback);
```

## notificationManager.isSupportTemplate

PhonePC/2in1TabletTVWearable

isSupportTemplate(templateName: string): Promise<boolean>

在使用[通知模板](js-apis-inner-notification-notificationtemplate.md)发布通知前，可以通过该接口查询是否支持对应的通知模板。使用Promise异步回调。

**系统能力**：SystemCapability.Notification.Notification

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| templateName | string | 是 | 模板名称。当前仅支持'downloadTemplate'。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象。返回true表示支持该模板；返回false表示不支持该模板。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[通知错误码](errorcode-notification.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |
| 1600001 | Internal error. |
| 1600002 | Marshalling or unmarshalling error. |
| 1600003 | Failed to connect to the service. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let templateName: string = 'downloadTemplate';
4. notificationManager.isSupportTemplate(templateName).then((data: boolean) => {
5. console.info(`isSupportTemplate success, data: ${JSON.stringify(data)}`);
6. }).catch((err: BusinessError) => {
7. console.error(`isSupportTemplate failed, code is ${err.code}, message is ${err.message}`);
8. });
```

## notificationManager.requestEnableNotification10+

PhonePC/2in1TabletTVWearable

requestEnableNotification(context: UIAbilityContext, callback: AsyncCallback<void>): void

应用需要获取用户授权才能发送通知。在通知发布前调用该接口，可以拉起通知授权弹窗，让用户选择是否允许发送通知。使用callback异步回调。

说明

* 仅当应用界面加载完成后（即调用[loadContent](js-apis-app-ability-uiextensioncontentsession.md#loadcontent)成功），方可使用该接口。
* 在使用该接口拉起通知授权弹窗后，如果用户拒绝授权，将无法使用该接口再次拉起弹窗。开发者可以调用[openNotificationSettings](js-apis-notificationmanager.md#notificationmanageropennotificationsettings13)二次申请授权，拉起通知管理弹窗。

**模型约束**：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.Notification.Notification

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [UIAbilityContext](js-apis-inner-application-uiabilitycontext.md) | 是 | 通知弹窗绑定Ability的上下文。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当应用通过弹窗获取用户授权成功，err为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[通知错误码](errorcode-notification.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |
| 1600001 | Internal error. |
| 1600002 | Marshalling or unmarshalling error. |
| 1600003 | Failed to connect to the service. |
| 1600004 | Notification disabled. |
| 1600013 | A notification dialog box is already displayed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { UIAbility } from '@kit.AbilityKit';
3. import { window } from '@kit.ArkUI';
4. import { hilog } from '@kit.PerformanceAnalysisKit';

6. class MyAbility extends UIAbility {
7. onWindowStageCreate(windowStage: window.WindowStage) {
8. hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onWindowStageCreate');
9. windowStage.loadContent('pages/Index', (err, data) => {
10. if (err.code) {
11. hilog.error(0x0000, 'testTag', `Failed to load the content. Cause: ${JSON.stringify(err) ?? ''}`);
12. return;
13. }
14. hilog.info(0x0000, 'testTag', `Succeeded in loading the content. Data: ${JSON.stringify(data) ?? ''}`);
15. let requestEnableNotificationCallback = (err: BusinessError): void => {
16. if (err) {
17. hilog.error(0x0000, 'testTag', `[ANS] requestEnableNotification failed, code is ${err.code}, message is ${err.message}`);
18. } else {
19. hilog.info(0x0000, 'testTag', `[ANS] requestEnableNotification success`);
20. }
21. };
22. notificationManager.requestEnableNotification(this.context, requestEnableNotificationCallback);
23. });
24. }
25. }
```

## notificationManager.requestEnableNotification10+

PhonePC/2in1TabletTVWearable

requestEnableNotification(context: UIAbilityContext): Promise<void>

应用需要获取用户授权才能发送通知。在通知发布前调用该接口，可以拉起通知授权弹窗，让用户选择是否允许发送通知。使用Promise异步回调。

说明

* 仅当应用界面加载完成后（即调用[loadContent](js-apis-app-ability-uiextensioncontentsession.md#loadcontent)成功），方可使用该接口。
* 在使用该接口拉起通知授权弹窗后，如果用户拒绝授权，将无法使用该接口再次拉起弹窗。开发者可以调用[openNotificationSettings](js-apis-notificationmanager.md#notificationmanageropennotificationsettings13)二次申请授权，拉起通知管理弹窗。

**模型约束**：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.Notification.Notification

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [UIAbilityContext](js-apis-inner-application-uiabilitycontext.md) | 是 | 通知弹窗绑定的Ability上下文。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[通知错误码](errorcode-notification.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |
| 1600001 | Internal error. |
| 1600002 | Marshalling or unmarshalling error. |
| 1600003 | Failed to connect to the service. |
| 1600004 | Notification disabled. |
| 1600013 | A notification dialog box is already displayed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { UIAbility } from '@kit.AbilityKit';
3. import { window } from '@kit.ArkUI';
4. import { hilog } from '@kit.PerformanceAnalysisKit';

6. class MyAbility extends UIAbility {
7. onWindowStageCreate(windowStage: window.WindowStage) {
8. hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onWindowStageCreate');
9. windowStage.loadContent('pages/Index', (err, data) => {
10. if (err.code) {
11. hilog.error(0x0000, 'testTag', `Failed to load the content. Cause: ${JSON.stringify(err) ?? ''}`);
12. return;
13. }
14. hilog.info(0x0000, 'testTag', `Succeeded in loading the content. Data: ${JSON.stringify(data) ?? ''}`);
15. notificationManager.requestEnableNotification(this.context).then(() => {
16. hilog.info(0x0000, 'testTag', `[ANS] requestEnableNotification success`);
17. }).catch((err: BusinessError) => {
18. hilog.error(0x0000, 'testTag', `[ANS] requestEnableNotification failed, code is ${err.code}, message is ${err.message}`);
19. });
20. });
21. }
22. }
```

## notificationManager.requestEnableNotification(deprecated)

PhonePC/2in1TabletTVWearable

requestEnableNotification(callback: AsyncCallback<void>): void

当前应用请求通知使能。使用callback异步回调。

说明

从API version 9开始支持，从API version 12开始废弃，建议使用有context入参的[requestEnableNotification](js-apis-notificationmanager.md#notificationmanagerrequestenablenotification10)替代。

**系统能力**：SystemCapability.Notification.Notification

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<void> | 是 | 回调函数。当应用请求通知使能成功，err为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[通知错误码](errorcode-notification.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |
| 1600001 | Internal error. |
| 1600002 | Marshalling or unmarshalling error. |
| 1600003 | Failed to connect to the service. |
| 1600004 | Notification disabled. |
| 1600013 | A notification dialog box is already displayed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let requestEnableNotificationCallback = (err: BusinessError): void => {
4. if (err) {
5. console.error(`requestEnableNotification failed, code is ${err.code}, message is ${err.message}`);
6. } else {
7. console.info("requestEnableNotification success");
8. }
9. };
10. notificationManager.requestEnableNotification(requestEnableNotificationCallback);
```

## notificationManager.requestEnableNotification(deprecated)

PhonePC/2in1TabletTVWearable

requestEnableNotification(): Promise<void>

当前应用请求通知使能。使用Promise异步回调。

说明

从API version 9开始支持，从API version 12开始废弃，建议使用有context入参的[requestEnableNotification](js-apis-notificationmanager.md#notificationmanagerrequestenablenotification10-1)替代。

**系统能力**：SystemCapability.Notification.Notification

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通知错误码](errorcode-notification.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1600001 | Internal error. |
| 1600002 | Marshalling or unmarshalling error. |
| 1600003 | Failed to connect to the service. |
| 1600004 | Notification disabled. |
| 1600013 | A notification dialog box is already displayed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. notificationManager.requestEnableNotification().then(() => {
4. console.info("requestEnableNotification success");
5. }).catch((err: BusinessError) => {
6. console.error(`requestEnableNotification failed, code is ${err.code}, message is ${err.message}`);
7. });
```

## notificationManager.isDistributedEnabled

PhonePC/2in1TabletTVWearable

isDistributedEnabled(callback: AsyncCallback<boolean>): void

查询设备是否支持跨设备协同通知。使用callback异步回调。

**设备行为差异**：该接口在Wearable/TV中回调返回恒为false，在其他设备类型中回调正常。

**系统能力**：SystemCapability.Notification.Notification

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<boolean> | 是 | 回调函数。返回true表示支持跨设备协同通知；返回false表示不支持跨设备协同通知；调用失败返回错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[通知错误码](errorcode-notification.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |
| 1600001 | Internal error. |
| 1600002 | Marshalling or unmarshalling error. |
| 1600003 | Failed to connect to the service. |
| 1600010 | Distributed operation failed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let isDistributedEnabledCallback = (err: BusinessError, data: boolean): void => {
4. if (err) {
5. console.error(`isDistributedEnabled failed, code is ${err.code}, message is ${err.message}`);
6. } else {
7. console.info(`isDistributedEnabled success ${JSON.stringify(data)}`);
8. }
9. };
10. notificationManager.isDistributedEnabled(isDistributedEnabledCallback);
```

## notificationManager.isDistributedEnabled

PhonePC/2in1TabletTVWearable

isDistributedEnabled(): Promise<boolean>

查询设备是否支持跨设备协同通知。使用Promise异步回调。

**设备行为差异**：该接口在Wearable/TV中回调返回恒为false，在其他设备类型中回调正常。

**系统能力**：SystemCapability.Notification.Notification

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象。返回true表示支持跨设备协同通知；返回false表示不支持跨设备协同通知。 |

**错误码：**

以下错误码的详细介绍请参见[通知错误码](errorcode-notification.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1600001 | Internal error. |
| 1600002 | Marshalling or unmarshalling error. |
| 1600003 | Failed to connect to the service. |
| 1600010 | Distributed operation failed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. notificationManager.isDistributedEnabled().then((data: boolean) => {
4. console.info(`isDistributedEnabled success, data: ${JSON.stringify(data)}`);
5. }).catch((err: BusinessError) => {
6. console.error(`isDistributedEnabled failed, code is ${err.code}, message is ${err.message}`);
7. });
```

## notificationManager.openNotificationSettings13+

PhonePC/2in1TabletTV

openNotificationSettings(context: UIAbilityContext): Promise<void>

拉起应用的通知设置界面，该页面以半模态形式呈现，可用于设置通知开关、通知提醒方式等。使用Promise异步回调。

**模型约束**：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.Notification.NotificationSettings

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [UIAbilityContext](js-apis-inner-application-uiabilitycontext.md) | 是 | 通知设置页面绑定Ability的上下文。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[通知错误码](errorcode-notification.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. |
| 1600001 | Internal error. |
| 1600003 | Failed to connect to the service. |
| 1600018 | The notification settings window is already displayed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { UIAbility } from '@kit.AbilityKit';
3. import { window } from '@kit.ArkUI';
4. import { hilog } from '@kit.PerformanceAnalysisKit';

6. class MyAbility extends UIAbility {
7. onWindowStageCreate(windowStage: window.WindowStage) {
8. hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onWindowStageCreate');
9. windowStage.loadContent('pages/Index', (err, data) => {
10. if (err.code) {
11. hilog.error(0x0000, 'testTag', `Failed to load the content. Cause: ${JSON.stringify(err) ?? ''}`);
12. return;
13. }
14. hilog.info(0x0000, 'testTag', `Succeeded in loading the content. Data: ${JSON.stringify(data) ?? ''}`);
15. notificationManager.openNotificationSettings(this.context).then(() => {
16. hilog.info(0x0000, 'testTag', `[ANS] openNotificationSettings success`);
17. }).catch((err: BusinessError) => {
18. hilog.error(0x0000, 'testTag', `[ANS] openNotificationSettings failed, code is ${err.code}, message is ${err.message}`);
19. });
20. });
21. }
22. }
```

## notificationManager.getNotificationSetting20+

PhonePC/2in1TabletTVWearable

getNotificationSetting(): Promise<NotificationSetting>

获取应用程序的通知设置。使用Promise异步回调。

**系统能力**：SystemCapability.Notification.Notification

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[NotificationSetting](js-apis-notificationmanager.md#notificationsetting20)> | Promise对象，返回此应用程序的通知设置。 |

**错误码：**

以下错误码的详细介绍请参见[通知错误码](errorcode-notification.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1600001 | Internal error. |
| 1600002 | Marshalling or unmarshalling error. |
| 1600003 | Failed to connect to the service. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. notificationManager.getNotificationSetting().then((data: notificationManager.NotificationSetting) => {
4. console.info(`getNotificationSetting success, data: ${JSON.stringify(data)}`);
5. }).catch((err: BusinessError) => {
6. console.error(`getNotificationSetting failed, code is ${err.code}, message is ${err.message}`);
7. });
```

## notificationManager.isGeofenceEnabled23+

PhonePC/2in1TabletTVWearable

isGeofenceEnabled(): Promise<boolean>

检查地理围栏功能是否已启用。使用Promise异步回调。

**系统能力**：SystemCapability.Notification.Notification

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象，返回地理围栏开关状态的Promise对象。返回true表示地理围栏功能已启用，返回false表示地理围栏功能未启用。 |

**错误码**：

以下错误码的详细介绍请参见[通知错误码](errorcode-notification.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1600001 | Internal error. |
| 1600002 | Marshalling or unmarshalling error. |
| 1600003 | Failed to connect to the service. |
| 1600012 | No memory space. |

**示例：**

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. notificationManager.isGeofenceEnabled().then((data: boolean) => {
5. hilog.info(0x0000, 'testTag', '%{public}s', `isGeofenceEnabled success, enabled:  ${JSON.stringify(data)}.`);
6. }).catch((err: BusinessError) => {
7. hilog.error(0x0000, 'testTag', '%{public}s',`isGeofenceEnabled failed, code is ${err.code}, message is ${err.message}`);
8. });
```

## ContentType

PhonePC/2in1TabletTVWearable

通知内容类型。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Notification.Notification

| 名称 | 值 | 说明 |
| --- | --- | --- |
| NOTIFICATION\_CONTENT\_BASIC\_TEXT | 0 | 普通文本类型通知。 |
| NOTIFICATION\_CONTENT\_LONG\_TEXT | 1 | 长文本类型通知。 |
| NOTIFICATION\_CONTENT\_PICTURE | 2 | 图片类型通知。 |
| NOTIFICATION\_CONTENT\_CONVERSATION | 3 | 社交类型通知。预留能力，暂未支持。 |
| NOTIFICATION\_CONTENT\_MULTILINE | 4 | 多行文本类型通知。 |
| NOTIFICATION\_CONTENT\_SYSTEM\_LIVE\_VIEW11+ | 5 | 系统实况窗类型通知。不支持三方应用直接创建该类型通知。系统代理创建系统实况窗类型通知后，三方应用可以通过发布相同ID的通知来更新指定内容。 |
| NOTIFICATION\_CONTENT\_LIVE\_VIEW11+ | 6 | 普通实况窗类型通知。仅系统应用可用。 |

## SlotLevel

PhonePC/2in1TabletTVWearable

通知级别。

**系统能力**：SystemCapability.Notification.Notification

| 名称 | 值 | 说明 |
| --- | --- | --- |
| LEVEL\_NONE | 0 | 表示关闭通知功能。 |
| LEVEL\_MIN | 1 | 表示通知功能已启用，状态栏中不显示通知图标，无横幅，无提示音。 |
| LEVEL\_LOW | 2 | 表示通知功能已启用，状态栏中显示通知图标，无横幅，无提示音。 |
| LEVEL\_DEFAULT | 3 | 表示通知功能已启用，状态栏中显示通知图标，无横幅，有提示音。 |
| LEVEL\_HIGH | 4 | 表示通知功能已启用，状态栏中显示通知图标，有横幅，有提示音。 |

## SlotType

PhonePC/2in1TabletTVWearable

通知渠道类型。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Notification.Notification

| 名称 | 值 | 说明 |
| --- | --- | --- |
| UNKNOWN\_TYPE | 0 | 未知类型。该类型对应[SlotLevel](js-apis-notificationmanager.md#slotlevel)为LEVEL\_MIN。 |
| SOCIAL\_COMMUNICATION | 1 | 社交通信。该类型对应[SlotLevel](js-apis-notificationmanager.md#slotlevel)为LEVEL\_HIGH。 |
| SERVICE\_INFORMATION | 2 | 服务提醒。该类型对应[SlotLevel](js-apis-notificationmanager.md#slotlevel)为LEVEL\_HIGH。 |
| CONTENT\_INFORMATION | 3 | 内容资讯。该类型对应[SlotLevel](js-apis-notificationmanager.md#slotlevel)为LEVEL\_MIN。 |
| LIVE\_VIEW11+ | 4 | 实况窗。不支持三方应用直接创建该渠道类型通知，可以由系统代理创建后，三方应用发布同ID的通知来更新指定内容，更新时默认无提示音。该类型对应[SlotLevel](js-apis-notificationmanager.md#slotlevel)为LEVEL\_DEFAULT。 |
| CUSTOMER\_SERVICE11+ | 5 | 客服消息。该类型用于用户与商家之间的客服消息，需由用户主动发起。该类型对应[SlotLevel](js-apis-notificationmanager.md#slotlevel)为LEVEL\_DEFAULT。 |
| OTHER\_TYPES | 0xFFFF | 其他。该类型对应[SlotLevel](js-apis-notificationmanager.md#slotlevel)为LEVEL\_MIN。 |

## NotificationSetting20+

PhonePC/2in1TabletTVWearable

通知设置状态，包括是否开启振动、是否开启响铃。

**系统能力**：SystemCapability.Notification.Notification

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| vibrationEnabled | boolean | 否 | 否 | 表示是否开启振动。  - true：开启。  - false：关闭。 |
| soundEnabled | boolean | 否 | 否 | 表示是否开启响铃。  - true：开启。  - false：关闭。 |

## BundleOption

PhonePC/2in1TabletTVWearable

type BundleOption = \_BundleOption

指定应用的包信息。

**系统能力**： SystemCapability.Notification.Notification

| 类型 | 说明 |
| --- | --- |
| [\_BundleOption](js-apis-inner-notification-notificationcommondef.md#bundleoption) | 指定应用的包信息。 |

## NotificationActionButton

PhonePC/2in1TabletTVWearable

type NotificationActionButton = \_NotificationActionButton

通知中显示的操作按钮。

**系统能力**： SystemCapability.Notification.Notification

| 类型 | 说明 |
| --- | --- |
| [\_NotificationActionButton](s-apis-inner-notification-notificationactionbutton.md) | 通知中显示的操作按钮。 |

## NotificationBasicContent

PhonePC/2in1TabletTVWearable

type NotificationBasicContent = \_NotificationBasicContent

普通文本通知。

**系统能力**： SystemCapability.Notification.Notification

| 类型 | 说明 |
| --- | --- |
| [\_NotificationBasicContent](js-apis-inner-notification-notificationcontent.md#notificationbasiccontent) | 描述普通文本通知。 |

## NotificationContent

PhonePC/2in1TabletTVWearable

type NotificationContent = \_NotificationContent

通知内容。

**系统能力**： SystemCapability.Notification.Notification

| 类型 | 说明 |
| --- | --- |
| [\_NotificationContent](js-apis-inner-notification-notificationcontent.md#notificationcontent-1) | 描述通知内容。 |

## NotificationLongTextContent

PhonePC/2in1TabletTVWearable

type NotificationLongTextContent = \_NotificationLongTextContent

长文本通知。

**系统能力**： SystemCapability.Notification.Notification

| 类型 | 说明 |
| --- | --- |
| [\_NotificationLongTextContent](js-apis-inner-notification-notificationcontent.md#notificationlongtextcontent) | 描述长文本通知。 |

## NotificationMultiLineContent

PhonePC/2in1TabletTVWearable

type NotificationMultiLineContent = \_NotificationMultiLineContent

多行文本通知。

**系统能力**： SystemCapability.Notification.Notification

| 类型 | 说明 |
| --- | --- |
| [\_NotificationMultiLineContent](js-apis-inner-notification-notificationcontent.md#notificationmultilinecontent) | 描述多行文本通知。 |

## NotificationPictureContent

PhonePC/2in1TabletTVWearable

type NotificationPictureContent = \_NotificationPictureContent

附有图片的通知。

**系统能力**： SystemCapability.Notification.Notification

| 类型 | 说明 |
| --- | --- |
| [\_NotificationPictureContent](js-apis-inner-notification-notificationcontent.md#notificationpicturecontent) | 附有图片的通知。 |

## NotificationSystemLiveViewContent11+

PhonePC/2in1TabletTVWearable

type NotificationSystemLiveViewContent = \_NotificationSystemLiveViewContent

系统实况窗通知内容。

**系统能力**： SystemCapability.Notification.Notification

| 类型 | 说明 |
| --- | --- |
| [\_NotificationSystemLiveViewContent](js-apis-inner-notification-notificationcontent.md#notificationsystemliveviewcontent) | 系统实况窗通知内容。 |

## NotificationRequest

PhonePC/2in1TabletTVWearable

type NotificationRequest = \_NotificationRequest

通知请求。

**系统能力**： SystemCapability.Notification.Notification

| 类型 | 说明 |
| --- | --- |
| [\_NotificationRequest](js-apis-inner-notification-notificationrequest.md#notificationrequest-1) | 通知请求。 |

## DistributedOptions

PhonePC/2in1TabletTVWearable

type DistributedOptions = \_DistributedOptions

分布式选项。

**系统能力**： SystemCapability.Notification.Notification

| 类型 | 说明 |
| --- | --- |
| [\_DistributedOptions](js-apis-inner-notification-notificationrequest.md#distributedoptions8) | 分布式选项。 |

## NotificationSlot

PhonePC/2in1TabletTVWearable

type NotificationSlot = \_NotificationSlot

通知渠道。

**系统能力**： SystemCapability.Notification.Notification

| 类型 | 说明 |
| --- | --- |
| [\_NotificationSlot](js-apis-inner-notification-notificationslot.md) | 通知渠道。 |

## NotificationTemplate

PhonePC/2in1TabletTVWearable

type NotificationTemplate = \_NotificationTemplate

通知模板。

**系统能力**： SystemCapability.Notification.Notification

| 类型 | 说明 |
| --- | --- |
| [\_NotificationTemplate](js-apis-inner-notification-notificationtemplate.md) | 通知模板。 |

## NotificationUserInput

PhonePC/2in1TabletTVWearable

type NotificationUserInput = \_NotificationUserInput

保存用户输入的通知消息。

**系统能力**： SystemCapability.Notification.Notification

| 类型 | 说明 |
| --- | --- |
| [\_NotificationUserInput](js-apis-inner-notification-notificationuserinput.md) | 保存用户输入的通知消息。 |

## NotificationCapsule11+

PhonePC/2in1TabletTVWearable

type NotificationCapsule = \_NotificationCapsule

通知胶囊。

**系统能力**： SystemCapability.Notification.Notification

| 类型 | 说明 |
| --- | --- |
| [\_NotificationCapsule](js-apis-inner-notification-notificationcontent.md#notificationcapsule11) | 通知胶囊。 |

## NotificationButton11+

PhonePC/2in1TabletTVWearable

type NotificationButton = \_NotificationButton

通知按钮。

**系统能力**： SystemCapability.Notification.Notification

| 类型 | 说明 |
| --- | --- |
| [\_NotificationButton](js-apis-inner-notification-notificationcontent.md#notificationbutton11) | 通知按钮。 |

## NotificationTime11+

PhonePC/2in1TabletTVWearable

type NotificationTime = \_NotificationTime

通知计时信息。

**系统能力**： SystemCapability.Notification.Notification

| 类型 | 说明 |
| --- | --- |
| [\_NotificationTime](js-apis-inner-notification-notificationcontent.md#notificationtime11) | 描述通知计时信息。 |

## NotificationProgress11+

PhonePC/2in1TabletTVWearable

type NotificationProgress = \_NotificationProgress

通知进度。

**系统能力**： SystemCapability.Notification.Notification

| 类型 | 说明 |
| --- | --- |
| [\_NotificationProgress](js-apis-inner-notification-notificationcontent.md#notificationprogress11) | 描述通知进度。 |

## PriorityNotificationType23+

PhonePC/2in1TabletTVWearable

描述通知的优先级类型。

**系统能力**：SystemCapability.Notification.Notification

| 名称 | 值 | 说明 |
| --- | --- | --- |
| OTHER | "OTHER" | 表示通知优先级类型为默认。 |
| PRIMARY\_CONTACT | "PRIMARY\_CONTACT" | 表示通知优先级类型为重要联系人。 |
| AT\_ME | "AT\_ME" | 表示通知优先级类型为@我。 |
| URGENT\_MESSAGE | "URGENT\_MESSAGE" | 表示通知优先级类型为加急消息。 |
| SCHEDULE\_REMINDER | "SCHEDULE\_REMINDER" | 表示通知优先级类型为日程待办。 |
