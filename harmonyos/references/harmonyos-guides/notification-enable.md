---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/notification-enable
title: 请求通知授权
breadcrumb: 指南 > 应用服务 > Notification Kit（用户通知服务） > 请求通知授权
category: harmonyos-guides
scraped_at: 2026-04-28T07:49:59+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:959f54867d0e4bf243097d5675e061de900781ac1fa2d190c97733450a71672c
---

应用需要获取用户授权才能发送通知。在通知发布前调用[requestEnableNotification()](../harmonyos-references/js-apis-notificationmanager.md#notificationmanagerrequestenablenotification10-1)接口，弹窗让用户选择是否允许发送通知。当用户拒绝授权后，将无法通过该接口再次拉起弹窗。如果应用需要向用户再次申请通知授权，则可以使用[openNotificationSettings](../harmonyos-references/js-apis-notificationmanager.md#notificationmanageropennotificationsettings13)接口拉起通知管理半模态弹窗。

## 接口说明

接口详情参见[@ohos.notificationManager (NotificationManager模块)](../harmonyos-references/js-apis-notificationmanager.md)。

**表1** 通知授权接口功能介绍

| **接口名** | **描述** |
| --- | --- |
| isNotificationEnabled():Promise<boolean> | 查询通知是否授权。 |
| requestEnableNotification(context: UIAbilityContext): Promise<void> | 请求发送通知的许可，第一次调用会弹窗让用户选择。 |
| openNotificationSettings(context: UIAbilityContext): Promise<void> | 拉起通知管理弹窗。 |

## 开发步骤

1. 导入NotificationManager模块。

   ```
   1. import { notificationManager } from '@kit.NotificationKit';
   2. import { BusinessError } from '@kit.BasicServicesKit';
   3. import { hilog } from '@kit.PerformanceAnalysisKit';
   4. import { common } from '@kit.AbilityKit';

   6. const TAG: string = '[PublishOperation]';
   7. const DOMAIN_NUMBER: number = 0xFF00;
   ```

   [RequestEnableNotification.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Notification-Kit/Notification/entry/src/main/ets/filemanager/RequestEnableNotification.ets#L16-L24)
2. 拉起通知弹窗，向用户请求通知授权。

   可通过requestEnableNotification的错误码判断用户是否授权。若返回的错误码为1600004，即为拒绝授权。

   ```
   1. let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
   2. notificationManager.isNotificationEnabled().then((data: boolean) => {
   3. hilog.info(DOMAIN_NUMBER, TAG, `isNotificationEnabled success, data: ${data}` );
   4. if (!data) {
   5. notificationManager.requestEnableNotification(context).then(() => {
   6. hilog.info(DOMAIN_NUMBER, TAG, `[ANS] requestEnableNotification success`);
   7. }).catch((err: BusinessError) => {
   8. if (1600004 == err.code) {
   9. hilog.error(DOMAIN_NUMBER, TAG,
   10. `[ANS] requestEnableNotification refused, code is ${err.code}, message is ${err.message}`);
   11. } else {
   12. hilog.error(DOMAIN_NUMBER, TAG,
   13. `[ANS] requestEnableNotification failed, code is ${err.code}, message is ${err.message}`);
   14. }
   15. });
   16. }
   17. }).catch((err: BusinessError) => {
   18. hilog.error(DOMAIN_NUMBER, TAG,
   19. `isNotificationEnabled fail, code is ${err.code}, message is ${err.message}`);
   20. });
   ```

   [RequestEnableNotification.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Notification-Kit/Notification/entry/src/main/ets/filemanager/RequestEnableNotification.ets#L37-L58)
3. （可选）拉起通知管理半模态弹窗，向用户再次申请通知授权。

   ```
   1. let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
   2. notificationManager.isNotificationEnabled().then((data: boolean) => {
   3. hilog.info(DOMAIN_NUMBER, TAG, `isNotificationEnabled success, data:  ${data}`);
   4. if (!data) {
   5. notificationManager.openNotificationSettings(context).then(() => {
   6. hilog.info(DOMAIN_NUMBER, TAG, `[ANS] openNotificationSettings success`);
   7. }).catch((err: BusinessError) => {
   8. hilog.error(DOMAIN_NUMBER, TAG,
   9. `[ANS] openNotificationSettings failed, code is ${err.code}, message is ${err.message}`);
   10. });
   11. }
   12. }).catch((err: BusinessError) => {
   13. hilog.error(DOMAIN_NUMBER, TAG,
   14. `isNotificationEnabled fail, code is ${err.code}, message is ${err.message}`);
   15. });
   ```

   [RequestEnableNotification.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Notification-Kit/Notification/entry/src/main/ets/filemanager/RequestEnableNotification.ets#L64-L80)
