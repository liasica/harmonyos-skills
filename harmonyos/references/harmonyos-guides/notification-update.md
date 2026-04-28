---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/notification-update
title: 更新通知
breadcrumb: 指南 > 应用服务 > Notification Kit（用户通知服务） > 更新通知
category: harmonyos-guides
scraped_at: 2026-04-28T07:50:02+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:145fa7f71084422ed03b58f051a934479404892983f0f6926306616c794e9f02
---

从API version 18开始，支持应用只更新已发布的通知。主要用于上传下载进度更新、IM会话消息更新等场景。

## 接口说明

通知发布更新接口说明详见下表，通知更新可通过入参[NotificationRequest](../harmonyos-references/js-apis-inner-notification-notificationrequest.md#notificationrequest-1)携带updateOnly字段来指定，不指定该字段默认为false。

* 当updateOnly为true时，若相同ID通知存在，则更新通知；若相同ID通知不存在，则更新失败，并且不创建新的通知。
* 当updateOnly为false时，若相同ID通知存在，则更新通知；若相同ID通知不存在，则创建通知。

| **接口名** | **描述** |
| --- | --- |
| [publish](../harmonyos-references/js-apis-notificationmanager.md#notificationmanagerpublish)(request: NotificationRequest, callback: AsyncCallback<void>): void | 发布更新通知。 |

## 开发步骤

下面以进度条通知发布更新为例。

1. 导入模块。

   ```
   1. import { notificationManager } from '@kit.NotificationKit';
   2. import { BusinessError } from '@kit.BasicServicesKit';
   3. import { hilog } from '@kit.PerformanceAnalysisKit';

   5. const TAG: string = '[PublishOperation]';
   6. const DOMAIN_NUMBER: number = 0xFF00;
   ```

   [UpdateNotification.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Notification-Kit/Notification/entry/src/main/ets/filemanager/UpdateNotification.ets#L16-L23)
2. 发布进度条通知。

   ```
   1. let notificationRequest: notificationManager.NotificationRequest = {
   2. id: 5,
   3. content: {
   4. notificationContentType: notificationManager.ContentType.NOTIFICATION_CONTENT_BASIC_TEXT,
   5. normal: {
   6. title: 'test_title',
   7. text: 'test_text',
   8. additionalText: 'test_additionalText'
   9. }
   10. },
   11. // 构造进度条模板，name字段当前需要固定配置为downloadTemplate
   12. template: {
   13. name: 'downloadTemplate',
   14. data: { title: 'File Title', fileName: 'music.mp4', progressValue: 50 }
   15. }
   16. };

   18. // 发布通知
   19. notificationManager.publish(notificationRequest, (err: BusinessError) => {
   20. if (err) {
   21. hilog.error(DOMAIN_NUMBER, TAG,
   22. `Failed to publish notification. Code is ${err.code}, message is ${err.message}`);
   23. return;
   24. }
   25. hilog.info(DOMAIN_NUMBER, TAG, 'Succeeded in publishing notification.');
   26. });
   ```

   [UpdateNotification.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Notification-Kit/Notification/entry/src/main/ets/filemanager/UpdateNotification.ets#L36-L63)
3. 通过[NotificationRequest](../harmonyos-references/js-apis-inner-notification-notificationrequest.md#notificationrequest-1)接口携带updateOnly字段更新进度条通知。

   ```
   1. let notificationRequest: notificationManager.NotificationRequest = {
   2. id: 5,
   3. updateOnly: true,
   4. content: {
   5. notificationContentType: notificationManager.ContentType.NOTIFICATION_CONTENT_BASIC_TEXT,
   6. normal: {
   7. title: 'test_title',
   8. text: 'test_text',
   9. additionalText: 'test_additionalText'
   10. }
   11. },
   12. // 构造进度条模板，name字段当前需要固定配置为downloadTemplate
   13. template: {
   14. name: 'downloadTemplate',
   15. data: { title: 'File Title', fileName: 'music.mp4', progressValue: 99 }
   16. }
   17. };

   19. // 更新发布通知
   20. notificationManager.publish(notificationRequest, (err: BusinessError) => {
   21. if (err) {
   22. hilog.error(DOMAIN_NUMBER, TAG,
   23. `Failed to update notification. Code is ${err.code}, message is ${err.message}`);
   24. return;
   25. }
   26. hilog.info(DOMAIN_NUMBER, TAG, 'Succeeded in updating notification.');
   27. });
   ```

   [UpdateNotification.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Notification-Kit/Notification/entry/src/main/ets/filemanager/UpdateNotification.ets#L68-L96)
