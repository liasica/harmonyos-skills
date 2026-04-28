---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/notification-badge
title: 管理通知角标
breadcrumb: 指南 > 应用服务 > Notification Kit（用户通知服务） > 管理通知角标
category: harmonyos-guides
scraped_at: 2026-04-28T07:50:00+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:ce7eaab83cc47d8158f2685fc5c704b7ad054e3416a8ecdce63b3e4b5f56b705
---

针对未读的通知，系统提供了角标设置接口，将未读通知个数显示在桌面图标的右上角角标上。

通知增加时，角标上显示的未读通知个数需要增加。

通知被查看后，角标上显示的未读通知个数需要减少，没有未读通知时，不显示角标。

## 接口说明

当角标设定个数取值小于或等于0时，表示清除角标。取值大于99时，通知角标将显示99+。

* 增加角标数，支持如下两种方法：

  + 发布通知时，在[NotificationRequest](../harmonyos-references/js-apis-inner-notification-notificationrequest.md#notificationrequest-1)的badgeNumber字段里携带，桌面收到通知后，在原角标数上累加、呈现。
  + 调用接口[setBadgeNumber()](../harmonyos-references/js-apis-notificationmanager.md#notificationmanagersetbadgenumber10)设置，桌面按设置的角标数呈现。
* 减少角标数，目前仅支持通过[setBadgeNumber()](../harmonyos-references/js-apis-notificationmanager.md#notificationmanagersetbadgenumber10)设置。

  | **接口名** | **描述** |
  | --- | --- |
  | setBadgeNumber(badgeNumber: number): Promise<void> | 设置角标个数。 |

## 开发步骤

1. 导入NotificationManager模块。

   ```
   1. import { notificationManager } from '@kit.NotificationKit';
   2. import { hilog } from '@kit.PerformanceAnalysisKit';
   3. import { BusinessError } from '@kit.BasicServicesKit';

   5. const TAG: string = '[PublishOperation]';
   6. const DOMAIN_NUMBER: number = 0xFF00;
   ```

   [ManageNotificationBadges.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Notification-Kit/Notification/entry/src/main/ets/filemanager/ManageNotificationBadges.ets#L16-L24)
2. 增加角标个数。

   发布通知时，可在[NotificationRequest](../harmonyos-references/js-apis-inner-notification-notificationrequest.md#notificationrequest-1)的badgeNumber字段里携带相关信息，具体可参考[通知发布](text-notification.md)章节。

   示例为调用setBadgeNumber接口增加角标，在发布完新的通知后，调用该接口。

   ```
   1. let badgeNumber: number = 9;
   2. notificationManager.setBadgeNumber(badgeNumber).then(() => {
   3. hilog.info(DOMAIN_NUMBER, TAG, `Succeeded in setting badge number.`);
   4. }).catch((err: BusinessError) => {
   5. hilog.error(DOMAIN_NUMBER, TAG,
   6. `Failed to set badge number. Code is ${err.code}, message is ${err.message}`);
   7. });
   ```

   [ManageNotificationBadges.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Notification-Kit/Notification/entry/src/main/ets/filemanager/ManageNotificationBadges.ets#L64-L72)
3. 减少角标个数。

   一条通知被查看后，应用需要调用接口设置剩下未读通知个数，桌面刷新角标。

   ```
   1. let badgeNumber: number = 8;
   2. notificationManager.setBadgeNumber(badgeNumber).then(() => {
   3. hilog.info(DOMAIN_NUMBER, TAG, `Succeeded in setting badge number.`);
   4. }).catch((err: BusinessError) => {
   5. hilog.error(DOMAIN_NUMBER, TAG,
   6. `Failed to set badge number. Code is ${err.code}, message is ${err.message}`);
   7. });
   ```

   [ManageNotificationBadges.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Notification-Kit/Notification/entry/src/main/ets/filemanager/ManageNotificationBadges.ets#L78-L86)

## 常见问题

由于setBadgeNumber为异步接口，使用setBadgeNumber连续设置角标时，为了确保执行顺序符合预期，需要确保上一次设置完成后才能进行下一次设置。

* 反例

  每次接口调用是相互独立的、没有依赖关系的，实际执行时无法保证调用顺序。

  示例如下：

  ```
  1. let badgeNumber: number = 10;
  2. notificationManager.setBadgeNumber(badgeNumber).then(() => {
  3. hilog.info(DOMAIN_NUMBER, TAG, `setBadgeNumber 10 success.`);
  4. }).catch((err: BusinessError) => {
  5. hilog.error(DOMAIN_NUMBER, TAG,
  6. `Failed to set badge number. Code is ${err.code}, message is ${err.message}`);
  7. });
  8. badgeNumber = 11;
  9. notificationManager.setBadgeNumber(badgeNumber).then(() => {
  10. hilog.info(DOMAIN_NUMBER, TAG, `setBadgeNumber 11 success.`);
  11. }).catch((err: BusinessError) => {
  12. hilog.error(DOMAIN_NUMBER, TAG,
  13. `Failed to set badge number. Code is ${err.code}, message is ${err.message}`);
  14. });
  ```

  [ManageNotificationBadges.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Notification-Kit/Notification/entry/src/main/ets/filemanager/ManageNotificationBadges.ets#L92-L107)
* 正例

  多次接口调用存在依赖关系，确保上一次设置完成后才能进行下一次设置。

  示例如下：

  ```
  1. let badgeNumber: number = 10;
  2. notificationManager.setBadgeNumber(badgeNumber).then(() => {
  3. hilog.info(DOMAIN_NUMBER, TAG, `setBadgeNumber 10 success.`);
  4. badgeNumber = 11;
  5. notificationManager.setBadgeNumber(badgeNumber).then(() => {
  6. hilog.info(DOMAIN_NUMBER, TAG, `setBadgeNumber 11 success.`);
  7. }).catch((err: BusinessError) => {
  8. hilog.error(DOMAIN_NUMBER, TAG,
  9. `Failed to set badge number. Code is ${err.code}, message is ${err.message}`);
  10. });
  11. }).catch((err: BusinessError) => {
  12. hilog.error(DOMAIN_NUMBER, TAG,
  13. `Failed to set badge number. Code is ${err.code}, message is ${err.message}`);
  14. });
  ```

  [ManageNotificationBadges.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Notification-Kit/Notification/entry/src/main/ets/filemanager/ManageNotificationBadges.ets#L113-L128)
