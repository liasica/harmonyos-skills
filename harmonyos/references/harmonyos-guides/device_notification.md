---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/device_notification
title: 穿戴设备模板化通知
breadcrumb: 指南 > 系统 > 硬件 > Wear Engine Kit（穿戴服务） > 手机侧应用开发 > 应用开发 > 穿戴设备模板化通知
category: harmonyos-guides
scraped_at: 2026-04-29T13:33:46+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:06eca22be01f54c808c558d4813fb766ff7b27eb280c34bfca382aee9ac9528e
---

手机侧应用向穿戴设备发送通知，并在穿戴设备上按模板显示，支持穿戴设备收到通知后同步振动或响铃（跟随穿戴设备系统设置）。执行成功后，穿戴设备上会显示下图所示通知界面。

该接口无需用户授权，仅需要确保应用已申请消息通知权限（参见[申请接入Wear Engine服务](wearengine_apply.md)），否则接口将调用失败。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fe/v3/nktrZ4hEQyeFbozMmx3rxQ/zh-cn_image_0000002558605332.png?HW-CC-KV=V1&HW-CC-Date=20260429T053345Z&HW-CC-Expire=86400&HW-CC-Sign=493B05DB7506FD596BDC4D1E47DFA1F86FCD796FF77A6C14A7AF0B76CD2AF8B1)

说明

* 穿戴设备侧无对应的应用也可以显示模板化通知。
* 请确保穿戴设备和华为运动健康App处于连接状态。用户可进入App“设备”界面查看设备是否在线。开发者可调用[getConnectedDevices](../harmonyos-references/wearengine_api.md#getconnecteddevices)方法了解设备是否在线，如果返回列表中不包含目标设备，则提醒用户重新连接该设备。
* 穿戴设备振动或响铃的条件：

  1. 穿戴设备侧已开启振动或响铃；
  2. 穿戴设备处于佩戴状态；
  3. 穿戴设备未开启勿扰模式。
* 通知在穿戴设备上自动弹出通知的条件：

  1. 穿戴设备处于佩戴状态；
  2. 穿戴设备未开启勿扰模式。

## 向穿戴设备侧发送通知

说明

该接口的调用需要在开发者联盟申请消息通知权限（请参考[申请接入Wear Engine服务](wearengine_apply.md)）。

1. 参见[已连接穿戴设备查询](query_connected_devices.md)章节，获取已连接设备列表。
2. 参见[目标设备选择](we-device-selection.md)章节，从已连接设备列表中选定需要通信的设备。
3. 调用[wearEngine](../harmonyos-references/wearengine_api.md)中的[getNotifyClient](../harmonyos-references/wearengine_api.md#wearenginegetnotifyclient)方法，获取[NotifyClient](../harmonyos-references/wearengine_api.md#notifyclient)对象。
4. 定义[NotificationOptions](../harmonyos-references/wearengine_api.md#notificationoptions)配置参数类。
5. 调用[notify](../harmonyos-references/wearengine_api.md#notify)方法，从手机上的应用发送通知到穿戴设备侧。

   ```
   1. // 步骤3 获取NotifyClient对象
   2. let notifyClient: wearEngine.NotifyClient = wearEngine.getNotifyClient(this.getUIContext().getHostContext());

   4. // 步骤4 构造NotificationOptions对象
   5. let button1: wearEngine.NotificationButton = {
   6. buttonId: wearEngine.ButtonId.FIRST_BUTTON,
   7. // 按钮内容最大长度为12字节
   8. content: 'button_1'
   9. }
   10. let type1Notification: wearEngine.Notification = {
   11. type: wearEngine.NotificationType.NOTIFICATION_WITH_ONE_BUTTON,
   12. // 包名与标题的最大长度为28字节
   13. bundleName: 'bundleName',
   14. title: 'title',
   15. // 消息内容最大长度为400字节
   16. text: 'text',
   17. buttons: [button1]
   18. }
   19. let options: wearEngine.NotificationOptions = {
   20. notification: type1Notification,
   21. onAction: (feedback: wearEngine.NotificationFeedback) => {
   22. console.info(`one button notify get feedback is ${feedback.action ? feedback.action : feedback.errorCode}`);
   23. }
   24. }

   26. // 步骤5 发送模板化通知至设备侧
   27. notifyClient.notify(targetDevice.randomId, options).then(result => {
   28. console.info(`Succeeded in sending notification.`);
   29. }).catch((error: BusinessError) => {
   30. console.error(`Failed to send notification. Code is ${error.code}, message is ${error.message}`);
   31. })
   ```
