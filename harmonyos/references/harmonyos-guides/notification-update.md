---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/notification-update
title: 更新通知
breadcrumb: 指南 > 应用服务 > Notification Kit（用户通知服务） > 更新通知
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:29+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:a6cc6bbf2d50f739e1510ba2011363b048f5fe256cf7d02354d3a327cb84a52f
---

从API version 18开始，支持应用只更新已发布的通知。主要用于上传下载进度更新、IM会话消息更新等场景。

## 接口说明

通知发布更新接口说明详见下表，[通知更新](notification-glossary.md#notification-update通知更新)可通过入参[NotificationRequest](../harmonyos-references/js-apis-inner-notification-notificationrequest.md#notificationrequest-1)携带updateOnly字段来指定，不指定该字段默认为false。

* 当updateOnly为true时，若相同ID通知存在，则更新通知；若相同ID通知不存在，则更新失败，并且不创建新的通知。
* 当updateOnly为false时，若相同ID通知存在，则更新通知；若相同ID通知不存在，则创建通知。

| **接口名** | **描述** |
| --- | --- |
| [publish](../harmonyos-references/js-apis-notificationmanager.md#notificationmanagerpublish)(request: NotificationRequest, callback: AsyncCallback<void>): void | 发布更新通知。 |

## 开发步骤

下面以进度条通知发布更新为例。

1. 导入模块。

   ```typescript
   import { notificationManager } from '@kit.NotificationKit';
   import { BusinessError } from '@kit.BasicServicesKit';
   import { hilog } from '@kit.PerformanceAnalysisKit';

   const TAG: string = '[PublishOperation]';
   const DOMAIN_NUMBER: number = 0xFF00;
   ```
2. 发布进度条通知。

   ```typescript
   let notificationRequest: notificationManager.NotificationRequest = {
     id: 5,
     content: {
       notificationContentType: notificationManager.ContentType.NOTIFICATION_CONTENT_BASIC_TEXT,
       normal: {
         title: 'test_title',
         text: 'test_text',
         additionalText: 'test_additionalText'
       }
     },
     // 构造进度条模板，name字段当前需要固定配置为downloadTemplate
     template: {
       name: 'downloadTemplate',
       data: { title: 'File Title', fileName: 'music.mp4', progressValue: 50 }
     }
   };

   // 发布通知
   notificationManager.publish(notificationRequest, (err: BusinessError) => {
     if (err) {
       hilog.error(DOMAIN_NUMBER, TAG,
         `Failed to publish notification. Code is ${err.code}, message is ${err.message}`);
       return;
     }
     hilog.info(DOMAIN_NUMBER, TAG, 'Succeeded in publishing notification.');
   });
   ```
3. 通过[NotificationRequest](../harmonyos-references/js-apis-inner-notification-notificationrequest.md#notificationrequest-1)接口携带updateOnly字段更新进度条通知。

   ```typescript
   let notificationRequest: notificationManager.NotificationRequest = {
     id: 5,
     updateOnly: true,
     content: {
       notificationContentType: notificationManager.ContentType.NOTIFICATION_CONTENT_BASIC_TEXT,
       normal: {
         title: 'test_title',
         text: 'test_text',
         additionalText: 'test_additionalText'
       }
     },
     // 构造进度条模板，name字段当前需要固定配置为downloadTemplate
     template: {
       name: 'downloadTemplate',
       data: { title: 'File Title', fileName: 'music.mp4', progressValue: 99 }
     }
   };

   // 更新发布通知
   notificationManager.publish(notificationRequest, (err: BusinessError) => {
     if (err) {
       hilog.error(DOMAIN_NUMBER, TAG,
         `Failed to update notification. Code is ${err.code}, message is ${err.message}`);
       return;
     }
     hilog.info(DOMAIN_NUMBER, TAG, 'Succeeded in updating notification.');
   });
   ```
