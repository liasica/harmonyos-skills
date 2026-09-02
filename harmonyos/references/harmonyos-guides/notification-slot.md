---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/notification-slot
title: 管理通知渠道
breadcrumb: 指南 > 应用服务 > Notification Kit（用户通知服务） > 管理通知渠道
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:59+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:1d4fadf51021e205fbebd27b80032970417b427b03f39195c05642a104e24c03
---

系统支持多种[通知渠道](notification-glossary.md#notification-slot通知渠道)，不同通知渠道对应的[通知提醒方式](notification-glossary.md#notification-reminder-mode通知提醒方式)不同，可以根据应用的实际场景选择适合的通知渠道，并对通知渠道进行管理（支持创建、查询、删除等操作）。

## 通知渠道类型说明

不同类型的[通知渠道](notification-glossary.md#notification-slot通知渠道)对应的[通知提醒方式](notification-glossary.md#notification-reminder-mode通知提醒方式)不同，详见下表。其中，Y代表支持，N代表不支持。

**说明** 

用户可以通过“设置 > 通知和状态栏”进入对应的应用，管理该应用的通知渠道。当应用中的“允许通知”开关开启时，横幅通知默认关闭（不支持应用配置、用户可手动开启），锁屏通知、桌面角标、铃声和振动等默认开启。

| SlotType | 取值 | 分类 | [对应Push消息分类标准](push-apply-right.md#通知消息分类标准与提醒方式) | 通知中心 | 横幅 | 锁屏 | 铃声/振动 | 状态栏图标 | 自动亮屏 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SOCIAL\_COMMUNICATION | 1 | 社交通信 | IM  VOIP  MISS\_CALL | Y | Y | Y | Y | Y | Y |
| SERVICE\_INFORMATION | 2 | 服务提醒 | TRAVEL  HEALTH  WORK  ACCOUNT  EXPRESS  FINANCE  DEVICE\_REMINDER  MAIL  PLAY\_VOICE  SUBSCRIPTION | Y | Y | Y | Y | Y | Y |
| CUSTOMER\_SERVICE | 5 | 客服消息 | -- | Y | N | N | Y | Y | N |
| CONTENT\_INFORMATION | 3 | 内容资讯 | MARKETING | Y | N | N | N | N | N |
| UNKNOWN\_TYPE | 0 | 未知类型 | MARKETING | Y | N | N | N | N | N |
| OTHER\_TYPES | 0xFFFF | 其他 | MARKETING | Y | N | N | N | N | N |

## 接口说明

[通知渠道](notification-glossary.md#notification-slot通知渠道)主要接口如下。其他接口介绍详情参见[@ohos.notificationManager (NotificationManager模块)](../harmonyos-references/js-apis-notificationmanager.md)。

| **接口名** | **描述** |
| --- | --- |
| addSlot(type: SlotType): Promise<void> | 创建指定类型的通知渠道。 |
| getSlot(slotType: SlotType): Promise<NotificationSlot> | 获取一个指定类型的通知渠道。 |
| removeSlot(slotType: SlotType): Promise<void> | 删除此应用程序指定类型的通知渠道。 |

除了可以使用addSlot()创建通知渠道，还可以在发布通知的[NotificationRequest](../harmonyos-references/js-apis-inner-notification-notificationrequest.md#notificationrequest-1)中携带notificationSlotType字段，如果对应渠道不存在，会自动创建。

## 开发步骤

1. 导入notificationManager模块。

   ```typescript
   import { notificationManager } from '@kit.NotificationKit';
   import { BusinessError } from '@kit.BasicServicesKit';
   import { hilog } from '@kit.PerformanceAnalysisKit';

   const TAG: string = '[PublishOperation]';
   const DOMAIN_NUMBER: number = 0xFF00;
   ```
2. 创建指定类型的[通知渠道](notification-glossary.md#notification-slot通知渠道)。

   ```typescript
   // addSlot回调
   let addSlotCallBack = (err: BusinessError): void => {
     if (err) {
       hilog.error(DOMAIN_NUMBER, TAG, `addSlot failed, code is ${err.code}, message is ${err.message}`);
     } else {
       hilog.info(DOMAIN_NUMBER, TAG, `addSlot success`);
     }
   };
   notificationManager.addSlot(notificationManager.SlotType.SOCIAL_COMMUNICATION, addSlotCallBack);
   ```
3. 查询指定类型的通知渠道。

   获取对应渠道是否创建以及该渠道支持的[通知提醒方式](notification-glossary.md#notification-reminder-mode通知提醒方式)，比如是否有铃声，是否有振动，锁屏是否可见等。

   ```typescript
   // getSlot回调
   let getSlotCallback = (err: BusinessError, data: notificationManager.NotificationSlot): void => {
     if (err) {
       hilog.error(DOMAIN_NUMBER, TAG, `Failed to get slot. Code is ${err.code}, message is ${err.message}`);
     } else {
       hilog.info(DOMAIN_NUMBER, TAG, `Succeeded in getting slot.`);
       if (data != null) {
         hilog.info(DOMAIN_NUMBER, TAG, `slot enable status is ${JSON.stringify(data.enabled)}`);
         hilog.info(DOMAIN_NUMBER, TAG, `vibrationEnabled status is ${JSON.stringify(data.vibrationEnabled)}`);
         hilog.info(DOMAIN_NUMBER, TAG, `lightEnabled status is ${JSON.stringify(data.lightEnabled)}`);
       }
     }
   };
   let slotType: notificationManager.SlotType = notificationManager.SlotType.SOCIAL_COMMUNICATION;
   notificationManager.getSlot(slotType, getSlotCallback);
   ```
4. 删除指定类型的通知渠道。

   ```typescript
   // removeSlot回调
   let removeSlotCallback = (err: BusinessError): void => {
     if (err) {
       hilog.error(DOMAIN_NUMBER, TAG,
         `removeSlot failed, code is ${JSON.stringify(err.code)}, message is ${JSON.stringify(err.message)}`);
     } else {
       hilog.info(DOMAIN_NUMBER, TAG, 'removeSlot success');
     }
   };
   let slotType: notificationManager.SlotType = notificationManager.SlotType.SOCIAL_COMMUNICATION;
   notificationManager.removeSlot(slotType, removeSlotCallback);
   ```
