---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/notification-with-wantagent
title: 为通知添加行为意图
breadcrumb: 指南 > 应用服务 > Notification Kit（用户通知服务） > 发布通知 > 为通知添加行为意图
category: harmonyos-guides
scraped_at: 2026-04-28T07:50:01+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:3967d9fc741530938a0c19ae2dff832dfcb75f5560169782673feb769865ca52
---

应用向Ability Kit申请[WantAgent](../harmonyos-references/js-apis-app-ability-wantagent.md)，并将WantAgent封装至通知中。当发布通知时，用户便可以通过点击通知栏中的消息或按钮，拉起目标应用组件或发布公共事件。

携带了actionButtons的通知示意图如下。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3/v3/NoCgs32mQ46tHym1T9Bjww/zh-cn_image_0000002552799412.png?HW-CC-KV=V1&HW-CC-Date=20260427T235000Z&HW-CC-Expire=86400&HW-CC-Sign=7D6AD083AC20BE6C5C1E170C23B92FD5192241259D690E80C27BE4D8D7119484)

## 运行机制

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6d/v3/1gNsdCDTQO6Al5dDxBesng/zh-cn_image_0000002583439107.png?HW-CC-KV=V1&HW-CC-Date=20260427T235000Z&HW-CC-Expire=86400&HW-CC-Sign=EFD7D6D00103D7A6282FDA81DF7B7051790E00003A7A59D553D366494151529D)

## 接口说明

| **接口名** | **描述** |
| --- | --- |
| [publish](../harmonyos-references/js-apis-notificationmanager.md#notificationmanagerpublish-1)(request: NotificationRequest): Promise<void> | 发布通知。 |
| [getWantAgent](../harmonyos-references/js-apis-app-ability-wantagent.md#wantagentgetwantagent)(info: WantAgentInfo, callback: AsyncCallback<WantAgent>): void | 创建WantAgent。 |

## 开发步骤

1. 导入模块。

   ```
   1. import { notificationManager } from '@kit.NotificationKit';
   2. import { wantAgent, WantAgent } from '@kit.AbilityKit';
   3. import { BusinessError } from '@kit.BasicServicesKit';
   4. import { hilog } from '@kit.PerformanceAnalysisKit';

   6. const TAG: string = '[PublishOperation]';
   7. const DOMAIN_NUMBER: number = 0xFF00;
   ```

   [AddWantAgent.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Notification-Kit/Notification/entry/src/main/ets/filemanager/AddWantAgent.ets#L16-L24)
2. 创建WantAgentInfo信息。

   场景一：创建拉起UIAbility的WantAgent的[WantAgentInfo](../harmonyos-references/js-apis-inner-wantagent-wantagentinfo.md)信息。

   ```
   1. let wantAgentObj: WantAgent | null = null; // 用于保存创建成功的wantAgent对象，后续使用其完成触发的动作。

   3. // 通过WantAgentInfo的operationType设置动作类型
   4. let wantAgentInfo: wantAgent.WantAgentInfo = {
   5. wants: [
   6. {
   7. deviceId: '',
   8. bundleName: 'com.sample.eventnotification', // 需要替换为对应的bundleName。
   9. abilityName: 'EntryAbility', // 需要替换为对应的abilityName。
   10. action: '',
   11. entities: [],
   12. uri: '',
   13. parameters: {}
   14. }
   15. ],
   16. actionType: wantAgent.OperationType.START_ABILITY,
   17. requestCode: 0,
   18. actionFlags: [wantAgent.WantAgentFlags.CONSTANT_FLAG]
   19. };
   ```

   [AddWantAgent.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Notification-Kit/Notification/entry/src/main/ets/filemanager/AddWantAgent.ets#L92-L112)

   场景二：创建发布[公共事件](common-event-overview.md)的WantAgent的[WantAgentInfo](../harmonyos-references/js-apis-inner-wantagent-wantagentinfo.md)信息。

   ```
   1. let wantAgentObj: WantAgent | null = null; // 用于保存创建成功的WantAgent对象，后续使用其完成触发的动作。

   3. // 通过WantAgentInfo的operationType设置动作类型
   4. let wantAgentInfo: wantAgent.WantAgentInfo = {
   5. wants: [
   6. {
   7. action: 'event_name', // 设置事件名
   8. parameters: {},
   9. }
   10. ],
   11. actionType: wantAgent.OperationType.SEND_COMMON_EVENT,
   12. requestCode: 0,
   13. actionFlags: [wantAgent.WantAgentFlags.CONSTANT_FLAG],
   14. };
   ```

   [AddWantAgent.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Notification-Kit/Notification/entry/src/main/ets/filemanager/AddWantAgent.ets#L37-L52)
3. 调用[getWantAgent()](../harmonyos-references/js-apis-app-ability-wantagent.md#wantagentgetwantagent)方法进行创建WantAgent。

   ```
   1. // 创建WantAgent
   2. wantAgent.getWantAgent(wantAgentInfo, (err: BusinessError, data: WantAgent) => {
   3. if (err) {
   4. hilog.error(DOMAIN_NUMBER, TAG,
   5. `Failed to get want agent. Code is ${err.code}, message is ${err.message}`);
   6. return;
   7. }
   8. hilog.info(DOMAIN_NUMBER, TAG, 'Succeeded in getting want agent.');
   9. wantAgentObj = data;

   11. // ...
   12. });
   ```

   [AddWantAgent.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Notification-Kit/Notification/entry/src/main/ets/filemanager/AddWantAgent.ets#L114-L163)
4. 构造NotificationRequest对象，并发布携带WantAgent的通知。

   说明

   * 如果封装WantAgent至通知消息中，可以点击通知触发WantAgent。当通知消息存在actionButtons时，点击通知会先显示actionButtons，再次点击通知触发WantAgent。
   * 如果封装WantAgent至通知按钮中，点击通知后，该通知下方会出现通知按钮，可以点击按钮触发WantAgent。

   ```
   1. // 构造NotificationActionButton对象
   2. let actionButton: notificationManager.NotificationActionButton = {
   3. title: 'open_the_app',
   4. // wantAgentObj使用前需要保证已被赋值（即步骤3执行完成）
   5. // 通知按钮的WantAgent
   6. wantAgent: wantAgentObj!
   7. };

   9. // 构造NotificationRequest对象
   10. let notificationRequest: notificationManager.NotificationRequest = {
   11. content: {
   12. notificationContentType: notificationManager.ContentType.NOTIFICATION_CONTENT_BASIC_TEXT,
   13. normal: {
   14. title: 'one_button_notify',
   15. text: 'Click on this notification twice to open the app',
   16. additionalText: 'Test_AdditionalText',
   17. },
   18. },
   19. id: 6,
   20. // 通知消息的WantAgent
   21. wantAgent: wantAgentObj!,
   22. // 通知按钮
   23. actionButtons: [actionButton],
   24. };

   26. notificationManager.publish(notificationRequest, (err: BusinessError) => {
   27. if (err) {
   28. hilog.error(DOMAIN_NUMBER, TAG,
   29. `Failed to publish notification. Code is ${err.code}, message is ${err.message}`);
   30. return;
   31. }
   32. hilog.info(DOMAIN_NUMBER, TAG, 'Succeeded in publishing notification.');
   33. });
   ```

   [AddWantAgent.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Notification-Kit/Notification/entry/src/main/ets/filemanager/AddWantAgent.ets#L126-L160)

## 示例代码

* [自定义通知](https://gitcode.com/HarmonyOS_Samples/custom-notification-badge/blob/master/README.md)
