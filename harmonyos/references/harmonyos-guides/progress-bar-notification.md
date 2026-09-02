---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/progress-bar-notification
title: 发布进度条类型通知
breadcrumb: 指南 > 应用服务 > Notification Kit（用户通知服务） > 发布通知 > 发布进度条类型通知
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:59+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:5fba2c6ec717b3505ab1f842ec4ae2af37d2fcc14cf81da1bf50bd2744ee00dd
---

进度条通知也是常见的通知类型，主要应用于文件下载、事务处理进度显示。当前系统提供了进度条模板，发布通知应用应设置好进度条模板的属性值，如模板名、模板数据，通过通知子系统发送到通知栏显示。

目前系统模板仅支持进度条模板，通知模板[NotificationTemplate](../harmonyos-references/js-apis-inner-notification-notificationtemplate.md)中的data参数为用户自定义数据，用于显示与模板相关的数据。

## 接口说明

[isSupportTemplate()](../harmonyos-references/js-apis-notificationmanager.md#notificationmanagerissupporttemplate)是查询是否支持对应的通知模板，目前仅支持进度条模板。

| **接口名** | **描述** |
| --- | --- |
| isSupportTemplate(templateName: string): Promise<boolean> | 查询是否支持对应的通知模板。 |

## 开发步骤

1. 导入模块。

   ```typescript
   import { notificationManager } from '@kit.NotificationKit';
   import { BusinessError } from '@kit.BasicServicesKit';
   import { hilog } from '@kit.PerformanceAnalysisKit';

   const TAG: string = '[PublishOperation]';
   const DOMAIN_NUMBER: number = 0xFF00;
   ```
2. 查询系统是否支持进度条模板，查询结果为支持downloadTemplate模板类通知。

   ```typescript
   notificationManager.isSupportTemplate('downloadTemplate').then((data: boolean) => {
     let isSupportTemplate: boolean = data; // isSupportTemplate的值为true表示支持downloadTemplate模板类通知，false表示不支持
     hilog.info(DOMAIN_NUMBER, TAG,
       `Succeeded in supporting download template notification. data is ${isSupportTemplate}`);
   }).catch((err: BusinessError) => {
     hilog.error(DOMAIN_NUMBER, TAG,
       `Failed to support download template notification. Code is ${err.code}, message is ${err.message}`);
   });
   ```

   **说明** 

   查询系统支持进度条模板后，再进行后续的步骤操作。
3. 构造进度条模板对象，并发布通知。

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
       data: { title: 'File Title', fileName: 'music.mp4', progressValue: 45 }
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
