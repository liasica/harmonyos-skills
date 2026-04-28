---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/text-notification
title: 发布文本类型通知
breadcrumb: 指南 > 应用服务 > Notification Kit（用户通知服务） > 发布通知 > 发布文本类型通知
category: harmonyos-guides
scraped_at: 2026-04-28T07:49:59+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:f22bce321824464c660c8a3093de0c683dde00892a0a102eb4206945bde75cf0
---

文本类型通知主要应用于发送短信息、提示信息等，支持普通文本类型和多行文本类型。

**表1** 基础类型通知中的内容分类

| 类型 | 描述 |
| --- | --- |
| NOTIFICATION\_CONTENT\_BASIC\_TEXT | 普通文本类型。 |
| NOTIFICATION\_CONTENT\_MULTILINE | 多行文本类型。 |

## 接口说明

通知发布接口说明详见下表，通知发布的详情可通过入参[NotificationRequest](../harmonyos-references/js-apis-inner-notification-notificationrequest.md#notificationrequest-1)来进行指定，可以包括通知内容、通知ID、通知的通道类型和通知发布时间等信息。

| **接口名** | **描述** |
| --- | --- |
| publish(request: NotificationRequest, callback: AsyncCallback<void>): void | 发布通知。 |

## 开发步骤

1. 导入模块。

   ```
   1. import { notificationManager } from '@kit.NotificationKit';
   2. import { BusinessError } from '@kit.BasicServicesKit';
   3. import { hilog } from '@kit.PerformanceAnalysisKit';

   5. const TAG: string = '[PublishOperation]';
   6. const DOMAIN_NUMBER: number = 0xFF00;
   ```

   [PublishNotification.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Notification-Kit/Notification/entry/src/main/ets/filemanager/PublishNotification.ets#L16-L23)
2. 构造NotificationRequest对象，并发布通知。

   * 普通文本类型通知由标题、文本内容和附加信息三个字段组成。详情请参考[NotificationBasicContent](../harmonyos-references/js-apis-inner-notification-notificationcontent.md#notificationbasiccontent)。

     ```
     1. let notificationRequest: notificationManager.NotificationRequest = {
     2. id: 1,
     3. content: {
     4. notificationContentType: notificationManager.ContentType.NOTIFICATION_CONTENT_BASIC_TEXT, // 普通文本类型通知
     5. normal: {
     6. title: 'test_title',
     7. text: 'test_text',
     8. additionalText: 'test_additionalText',
     9. }
     10. }
     11. };
     12. notificationManager.publish(notificationRequest, (err: BusinessError) => {
     13. if (err) {
     14. hilog.error(DOMAIN_NUMBER, TAG,
     15. `Failed to publish notification. Code is ${err.code}, message is ${err.message}`);
     16. return;
     17. }
     18. hilog.info(DOMAIN_NUMBER, TAG, 'Succeeded in publishing notification.');
     19. });
     ```

     [PublishNotification.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Notification-Kit/Notification/entry/src/main/ets/filemanager/PublishNotification.ets#L34-L54)
   * 多行文本类型通知继承了普通文本类型的字段，同时新增了多行文本内容、内容概要和通知展开时的标题。详情请参考[NotificationMultiLineContent](../harmonyos-references/js-apis-inner-notification-notificationcontent.md#notificationmultilinecontent)。

     ```
     1. let notificationRequest: notificationManager.NotificationRequest = {
     2. id: 3,
     3. content: {
     4. notificationContentType: notificationManager.ContentType.NOTIFICATION_CONTENT_MULTILINE, // 多行文本类型通知
     5. multiLine: {
     6. title: 'test_multi_line_title',
     7. text: 'test_text',
     8. briefText: 'test_briefText',
     9. longTitle: 'test_longTitle',
     10. lines: ['line_01', 'line_02', 'line_03'],
     11. }
     12. }
     13. };
     14. // 发布通知
     15. notificationManager.publish(notificationRequest, (err: BusinessError) => {
     16. if (err) {
     17. hilog.error(DOMAIN_NUMBER, TAG,
     18. `Failed to publish notification. Code is ${err.code}, message is ${err.message}`);
     19. return;
     20. }
     21. hilog.info(DOMAIN_NUMBER, TAG, 'Succeeded in publishing notification.');
     22. });
     ```

     [PublishNotification.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Notification-Kit/Notification/entry/src/main/ets/filemanager/PublishNotification.ets#L59-L82)
