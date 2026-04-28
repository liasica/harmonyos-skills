---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-notificationsubscriberextensionability
title: @ohos.application.NotificationSubscriberExtensionAbility (通知订阅扩展能力)
breadcrumb: API参考 > 应用服务 > Notification Kit（用户通知服务） > ArkTS API > @ohos.application.NotificationSubscriberExtensionAbility (通知订阅扩展能力)
category: harmonyos-references
scraped_at: 2026-04-28T08:17:33+08:00
doc_updated_at: 2026-04-02
content_hash: sha256:b277b1009f63af6a84fc9917cbeee05172a2b6fa7e38983208c2bff2020d5406
---

NotificationSubscriberExtensionAbility 是通知订阅者扩展能力的基类，提供通知订阅的相关功能。

说明

本模块首批接口从API version 22开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

本模块接口仅可在Stage模型下使用。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { notificationExtensionSubscription, NotificationSubscriberExtensionAbility } from '@kit.NotificationKit';
```

## NotificationSubscriberExtensionAbility

PhonePC/2in1TabletTVWearable

**系统能力**：SystemCapability.Notification.Notification

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| context | [NotificationSubscriberExtensionContext](js-apis-notificationsubscriberextensioncontext.md) | 否 | 否 | NotificationSubscriberExtensionAbility的上下文环境。 |

### onDestroy

PhonePC/2in1TabletTVWearable

onDestroy(): void

通知订阅扩展被销毁时的回调。

**系统能力**：SystemCapability.Notification.Notification

**示例：**

```
1. const TAG = 'NotificationSubscriberExtAbility';

3. export default class NotificationSubscriberExtAbility extends NotificationSubscriberExtensionAbility {
4. onDestroy(): void {
5. console.info(`${TAG} onDestroy`);
6. }
7. }
```

### onReceiveMessage

PhonePC/2in1TabletTVWearable

onReceiveMessage(notificationInfo: NotificationInfo): void

收到通知时回调。

**系统能力**：SystemCapability.Notification.Notification

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| notificationInfo | [NotificationInfo](js-apis-inner-notification-notificationinfo.md) | 是 | 通知订阅扩展能力中[onReceiveMessage](js-apis-notificationsubscriberextensionability.md#onreceivemessage)回调的通知信息。 |

**示例：**

```
1. const TAG = 'NotificationSubscriberExtAbility';

3. export default class NotificationSubscriberExtAbility extends NotificationSubscriberExtensionAbility {
4. onReceiveMessage(notificationInfo: notificationExtensionSubscription.NotificationInfo): void {
5. console.info(`${TAG} onReceiveMessage. notificationInfo: ${JSON.stringify(notificationInfo)}`);
6. }
7. }
```

### onCancelMessages

PhonePC/2in1TabletTVWearable

onCancelMessages(hashCodes: Array<string>): void

取消通知时的回调。

**系统能力**：SystemCapability.Notification.Notification

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| hashCodes | Array<string> | 是 | 要取消的通知的哈希码列表。 |

**示例：**

```
1. const TAG = 'NotificationSubscriberExtAbility';

3. export default class NotificationSubscriberExtAbility extends NotificationSubscriberExtensionAbility {
4. onCancelMessages(hashCodes: Array<string>): void {
5. console.info(`${TAG} onCancelMessages. hashCodes: ${JSON.stringify(hashCodes)}`);
6. }
7. }
```
