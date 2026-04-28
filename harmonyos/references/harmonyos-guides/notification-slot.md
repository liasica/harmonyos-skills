---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/notification-slot
title: 管理通知渠道
breadcrumb: 指南 > 应用服务 > Notification Kit（用户通知服务） > 管理通知渠道
category: harmonyos-guides
scraped_at: 2026-04-28T07:49:59+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:75debaf78611319e918dcc1f660dc76d027a5566d8d95b07ebffe2ccc88af754
---

系统支持多种通知渠道，不同通知渠道对应的通知提醒方式不同，可以根据应用的实际场景选择适合的通知渠道，并对通知渠道进行管理（支持创建、查询、删除等操作）。

## 通知渠道类型说明

不同类型的通知渠道对应的通知提醒方式不同，详见下表。其中，Y代表支持，N代表不支持。

说明

用户可以通过“设置 > 通知和状态栏”进入对应的应用，管理该应用的通知渠道。当应用中的“允许通知”开关开启时，横幅通知默认关闭（不支持应用配置、用户可手动开启），锁屏通知、桌面角标、响铃和振动等默认开启。

| SlotType | 取值 | 分类 | 通知中心 | 横幅 | 锁屏 | 铃声/振动 | 状态栏图标 | 自动亮屏 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| UNKNOWN\_TYPE | 0 | 未知类型 | Y | N | N | N | N | N |
| SOCIAL\_COMMUNICATION | 1 | 社交通信 | Y | Y | Y | Y | Y | Y |
| SERVICE\_INFORMATION | 2 | 服务提醒 | Y | Y | Y | Y | Y | Y |
| CONTENT\_INFORMATION | 3 | 内容资讯 | Y | N | N | N | N | N |
| CUSTOMER\_SERVICE | 5 | 客服消息 | Y | N | N | Y | Y | N |
| OTHER\_TYPES | 0xFFFF | 其他 | Y | N | N | N | N | N |

## 接口说明

通知渠道主要接口如下。其他接口介绍详情参见[@ohos.notificationManager (NotificationManager模块)](../harmonyos-references/js-apis-notificationmanager.md)。

| **接口名** | **描述** |
| --- | --- |
| addSlot(type: SlotType): Promise<void> | 创建指定类型的通知渠道。 |
| getSlot(slotType: SlotType): Promise<NotificationSlot> | 获取一个指定类型的通知渠道。 |
| removeSlot(slotType: SlotType): Promise<void> | 删除此应用程序指定类型的通知渠道。 |

除了可以使用addSlot()创建通知渠道，还可以在发布通知的[NotificationRequest](../harmonyos-references/js-apis-inner-notification-notificationrequest.md#notificationrequest-1)中携带notificationSlotType字段，如果对应渠道不存在，会自动创建。

## 开发步骤

1. 导入notificationManager模块。

   ```
   1. import { notificationManager } from '@kit.NotificationKit';
   2. import { BusinessError } from '@kit.BasicServicesKit';
   3. import { hilog } from '@kit.PerformanceAnalysisKit';

   5. const TAG: string = '[PublishOperation]';
   6. const DOMAIN_NUMBER: number = 0xFF00;
   ```

   [ManageNotificationWays.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Notification-Kit/Notification/entry/src/main/ets/filemanager/ManageNotificationWays.ets#L16-L23)
2. 创建指定类型的通知渠道。

   ```
   1. // addSlot回调
   2. let addSlotCallBack = (err: BusinessError): void => {
   3. if (err) {
   4. hilog.error(DOMAIN_NUMBER, TAG, `addSlot failed, code is ${err.code}, message is ${err.message}`);
   5. } else {
   6. hilog.info(DOMAIN_NUMBER, TAG, `addSlot success`);
   7. }
   8. };
   9. notificationManager.addSlot(notificationManager.SlotType.SOCIAL_COMMUNICATION, addSlotCallBack);
   ```

   [ManageNotificationWays.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Notification-Kit/Notification/entry/src/main/ets/filemanager/ManageNotificationWays.ets#L34-L44)
3. 查询指定类型的通知渠道。

   获取对应渠道是否创建以及该渠道支持的通知提醒方式，比如是否有声音提示，是否有震动，锁屏是否可见等。

   ```
   1. // getSlot回调
   2. let getSlotCallback = (err: BusinessError, data: notificationManager.NotificationSlot): void => {
   3. if (err) {
   4. hilog.error(DOMAIN_NUMBER, TAG, `Failed to get slot. Code is ${err.code}, message is ${err.message}`);
   5. } else {
   6. hilog.info(DOMAIN_NUMBER, TAG, `Succeeded in getting slot.`);
   7. if (data != null) {
   8. hilog.info(DOMAIN_NUMBER, TAG, `slot enable status is ${JSON.stringify(data.enabled)}`);
   9. hilog.info(DOMAIN_NUMBER, TAG, `vibrationEnabled status is ${JSON.stringify(data.vibrationEnabled)}`);
   10. hilog.info(DOMAIN_NUMBER, TAG, `lightEnabled status is ${JSON.stringify(data.lightEnabled)}`);
   11. }
   12. }
   13. };
   14. let slotType: notificationManager.SlotType = notificationManager.SlotType.SOCIAL_COMMUNICATION;
   15. notificationManager.getSlot(slotType, getSlotCallback);
   ```

   [ManageNotificationWays.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Notification-Kit/Notification/entry/src/main/ets/filemanager/ManageNotificationWays.ets#L49-L65)
4. 删除指定类型的通知渠道。

   ```
   1. // removeSlot回调
   2. let removeSlotCallback = (err: BusinessError): void => {
   3. if (err) {
   4. hilog.error(DOMAIN_NUMBER, TAG,
   5. `removeSlot failed, code is ${JSON.stringify(err.code)}, message is ${JSON.stringify(err.message)}`);
   6. } else {
   7. hilog.info(DOMAIN_NUMBER, TAG, 'removeSlot success');
   8. }
   9. };
   10. let slotType: notificationManager.SlotType = notificationManager.SlotType.SOCIAL_COMMUNICATION;
   11. notificationManager.removeSlot(slotType, removeSlotCallback);
   ```

   [ManageNotificationWays.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Notification-Kit/Notification/entry/src/main/ets/filemanager/ManageNotificationWays.ets#L70-L82)
