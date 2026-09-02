---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/notification-badge
title: 管理通知角标
breadcrumb: 指南 > 应用服务 > Notification Kit（用户通知服务） > 管理通知角标
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:29+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:af0bd2d905fcc6051d315c79693a3810d2907cdfaecbb111aee1a78692bdc5c4
---

针对未读的通知，系统提供了角标设置接口，将未读通知个数显示在桌面图标的右上角角标上。

通知增加时，角标上显示的未读通知个数需要增加。

通知被查看后，角标上显示的未读通知个数需要减少，没有未读通知时，不显示角标。

## 接口说明

当角标设定个数取值小于或等于0时，表示清除角标。取值大于99时，[通知角标](notification-glossary.md#notification-badge通知角标)将显示99+。

* 增加角标数，支持如下两种方法：

  + 发布通知时，在[NotificationRequest](../harmonyos-references/js-apis-inner-notification-notificationrequest.md#notificationrequest-1)的badgeNumber字段里携带，桌面收到通知后，在原角标数上累加、呈现。
  + 调用接口[setBadgeNumber()](../harmonyos-references/js-apis-notificationmanager.md#notificationmanagersetbadgenumber10)设置，桌面按设置的角标数呈现。
* 减少角标数，目前仅支持通过[setBadgeNumber()](../harmonyos-references/js-apis-notificationmanager.md#notificationmanagersetbadgenumber10)设置。

  | **接口名** | **描述** |
  | --- | --- |
  | setBadgeNumber(badgeNumber: number): Promise<void> | 设置角标个数。 |

## 开发步骤

1. 导入NotificationManager模块。

   ```typescript
   import { notificationManager } from '@kit.NotificationKit';
   import { hilog } from '@kit.PerformanceAnalysisKit';
   import { BusinessError } from '@kit.BasicServicesKit';

   const TAG: string = '[PublishOperation]';
   const DOMAIN_NUMBER: number = 0xFF00;
   ```
2. 增加角标个数。

   发布通知时，可在[NotificationRequest](../harmonyos-references/js-apis-inner-notification-notificationrequest.md#notificationrequest-1)的badgeNumber字段里携带相关信息，具体可参考[通知发布](text-notification.md)章节。

   示例为调用setBadgeNumber接口增加角标，在发布完新的通知后，调用该接口。

   ```typescript
   let badgeNumber: number = 9;
   notificationManager.setBadgeNumber(badgeNumber).then(() => {
     hilog.info(DOMAIN_NUMBER, TAG, `Succeeded in setting badge number.`);
   }).catch((err: BusinessError) => {
     hilog.error(DOMAIN_NUMBER, TAG,
       `Failed to set badge number. Code is ${err.code}, message is ${err.message}`);
   });
   ```
3. 减少角标个数。

   一条通知被查看后，应用需要调用接口设置剩下未读通知个数，桌面刷新角标。

   ```typescript
   let badgeNumber: number = 8;
   notificationManager.setBadgeNumber(badgeNumber).then(() => {
     hilog.info(DOMAIN_NUMBER, TAG, `Succeeded in setting badge number.`);
   }).catch((err: BusinessError) => {
     hilog.error(DOMAIN_NUMBER, TAG,
       `Failed to set badge number. Code is ${err.code}, message is ${err.message}`);
   });
   ```

## 常见问题

由于setBadgeNumber为异步接口，使用setBadgeNumber连续设置角标时，为了确保执行顺序符合预期，需要确保上一次设置完成后才能进行下一次设置。

* 反例

  每次接口调用是相互独立的、没有依赖关系的，实际执行时无法保证调用顺序。

  示例如下：

  ```typescript
  let badgeNumber: number = 10;
  notificationManager.setBadgeNumber(badgeNumber).then(() => {
    hilog.info(DOMAIN_NUMBER, TAG, `setBadgeNumber 10 success.`);
  }).catch((err: BusinessError) => {
    hilog.error(DOMAIN_NUMBER, TAG,
      `Failed to set badge number. Code is ${err.code}, message is ${err.message}`);
  });
  badgeNumber = 11;
  notificationManager.setBadgeNumber(badgeNumber).then(() => {
    hilog.info(DOMAIN_NUMBER, TAG, `setBadgeNumber 11 success.`);
  }).catch((err: BusinessError) => {
    hilog.error(DOMAIN_NUMBER, TAG,
      `Failed to set badge number. Code is ${err.code}, message is ${err.message}`);
  });
  ```
* 正例

  多次接口调用存在依赖关系，确保上一次设置完成后才能进行下一次设置。

  示例如下：

  ```typescript
  let badgeNumber: number = 10;
  notificationManager.setBadgeNumber(badgeNumber).then(() => {
    hilog.info(DOMAIN_NUMBER, TAG, `setBadgeNumber 10 success.`);
    badgeNumber = 11;
    notificationManager.setBadgeNumber(badgeNumber).then(() => {
      hilog.info(DOMAIN_NUMBER, TAG, `setBadgeNumber 11 success.`);
    }).catch((err: BusinessError) => {
      hilog.error(DOMAIN_NUMBER, TAG,
        `Failed to set badge number. Code is ${err.code}, message is ${err.message}`);
    });
  }).catch((err: BusinessError) => {
    hilog.error(DOMAIN_NUMBER, TAG,
      `Failed to set badge number. Code is ${err.code}, message is ${err.message}`);
  });
  ```
