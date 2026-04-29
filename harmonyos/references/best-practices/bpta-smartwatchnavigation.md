---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-smartwatchnavigation
title: 智能穿戴导航协同
breadcrumb: 最佳实践 > 自由流转 > 典型全场景协同开发案例 > 智能穿戴导航协同
category: best-practices
scraped_at: 2026-04-29T14:12:54+08:00
doc_updated_at: 2026-04-01
content_hash: sha256:c7cda243b997d4480b3d36a21c2701ebc4800ee5627df72a64ef82973743cbe1
---

## 概述

本文以智能手表的协同导航功能为典型案例，系统阐述了手机与智能穿戴设备通过通信协作实现地图导航的技术方案，主要包含了智能穿戴设备协同导航的体验设计、方案设计、界面开发及功能开发。

* [体验设计](bpta-smartwatchnavigation.md#section1736651042110)：从设计与交互层面，展示智能穿戴设备协同导航的体验设计要点。
* [方案设计](bpta-smartwatchnavigation.md#section8229111792118)：从交互流程层面，展示智能穿戴设备协同导航应用整体的实现方案。
* [界面开发](bpta-smartwatchnavigation.md#section15111857670)：从手机与智能穿戴设备双端，展示手机与智能穿戴设备协同导航中的界面开发要点。
* [功能开发](bpta-smartwatchnavigation.md#section88311141387)：展示智能穿戴设备协同导航应用中的核心功能开发的原理与开发步骤。

## 体验设计

本章节从[UX设计](bpta-smartwatchnavigation.md#section10370135220120)和[UI交互](bpta-smartwatchnavigation.md#section1914862101311)两个维度，详细阐述智能穿戴设备协同导航的体验设计方案。

### UX设计

在智能穿戴设备协同导航实践中，涉及手机与智能穿戴设备的互联通信，双方协同完成导航功能，因此UX设计需要同时考虑手机端与智能穿戴设备端。手机端UX设计以地图展示页为核心，智能穿戴设备端UX设计以地图展示页、导航页为核心，具体设计如下表所示。

**表1** 智能穿戴设备协同导航手机与智能穿戴设备侧UX设计

| 手机侧页面 | 效果图（手机） | 效果图（智能穿戴设备） |
| --- | --- | --- |
| 首页（地图展示页） |  |  |
| 导航页 | 不涉及 |  |

### UI交互

智能穿戴设备协同导航的UI交互设计主要包含以下关键特性：

1. 导航提醒：手表通过振动反馈提示用户。
2. 双端同步：目的地选择在手机与手表端实时同步。
3. 常亮显示：导航过程中保持手表屏幕常亮，导航结束后关闭常亮。
4. 交互控制：支持通过旋转表冠缩放地图视图。

## 方案设计

本章节将系统阐述智能穿戴设备协同导航的交互逻辑，完整呈现手机与智能穿戴设备协同的实现方案。

### 实现方案

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/86/v3/MciEBTUHQYaFzduOoLMJmQ/zh-cn_image_0000002353086117.jpg?HW-CC-KV=V1&HW-CC-Date=20260429T061246Z&HW-CC-Expire=86400&HW-CC-Sign=2C4683F92A0EF8C9D8B9258925EEB7383C9FC0C71E8E6790045FEBE3F7472C60 "点击放大")

## 界面开发

本章节将详细阐述协同导航场景下手机端与智能穿戴设备端的核心界面开发规范，重点解析双端界面开发的关键技术要点。

### 手机端界面开发核心要点

手机端界面开发规范要点：

1. 沉浸式地图展示：全屏适配，优化视觉呈现。
2. 交互设计：采用半模态转场实现操作按钮唤起。

说明

沉浸式地图展示，开发者可参考[窗口沉浸式](bpta-multi-device-window-immersive.md)。

操作按钮的拉起，开发者可以参考[半模态转场](../harmonyos-references/ts-universal-attributes-sheet-transition.md)。

### 智能穿戴设备端界面开发核心要点

由于智能穿戴设备屏幕尺寸有限且采用圆形表盘设计，界面开发需特别注意：

1. 内容适配：确保显示内容完整居中，避免挤压或截断。
2. 布局优化：针对圆形屏幕特性进行UX适配。

说明

智能穿戴设备界面开发具体可参考[智能穿戴应用开发](bpta-smartwatch.md)。

## 功能开发

本章节将详细解析智能穿戴设备协同导航的核心功能开发，重点阐述[地图操作](bpta-smartwatchnavigation.md#section1084068101014)、[互联通信](bpta-smartwatchnavigation.md#section5132818141013)、[消息通知](bpta-smartwatchnavigation.md#section113733017108)和[振感提示](bpta-smartwatchnavigation.md#section15991113613101)四大核心功能的实现方案，为开发者提供明确的技术指导。

### 地图操作

地图操作主要涉及地图展示以及地图绘制两个功能，地图展示能力开发者可以参考[显示地图](../harmonyos-guides/map-presenting.md)。

智能穿戴设备协同导航的地图绘制功能通过[MapComponentController](../harmonyos-references/map-map-mapcomponentcontroller.md)实现，具体包含以下核心操作：

**地图点击（目的地标记）：**

**图1** 地图点击操作时序图   
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/19/v3/pbsmQ_aRQzyg7tYelGB6Xw/zh-cn_image_0000002318967344.jpg?HW-CC-KV=V1&HW-CC-Date=20260429T061246Z&HW-CC-Expire=86400&HW-CC-Sign=3CDAC5AA2B2E602CFDE6047FA496DF1C4D3706A66BE188D9A6E6B2AC0CA35D3F "点击放大")

开发步骤如下：

1. 注册地图点击事件监听器，在回调函数中将触点的地理坐标持久化存储至destination\_Position状态变量中。

   ```
   1. // Destination location information obtained based on the map click event.
   2. @StorageLink('destination_Position') @Watch('changeDestinationPositionMark') destination_Position: mapCommon.LatLng =
   3. {
   4. longitude: 0,
   5. latitude: 0
   6. };
   7. // ...
   8. aboutToAppear(): void {
   9. // ...
   10. // Map initialization callback
   11. this.callback = async (err, mapController) => {
   12. if (!err) {
   13. // ...
   14. let mapOnclickCallBack = async (position: mapCommon.LatLng) => {
   15. if (this.isStartNavigation) {
   16. // If the navigation has started, you are not allowed to click on the mobile phone.
   17. this.isBarShow = false;
   18. } else {
   19. // Send destination information to the watch for synchronization
   20. this.connectUtils.sendMessage(JSON.stringify(new CommunicationInformation(1, undefined, position)));
   21. // Modify destination_Position to trigger changeDestinationPositionMark
   22. // To refresh the destination mark on the map.
   23. this.destination_Position = position;
   24. this.isBarShow = true;
   25. }
   26. };
   27. this.mapEventManager.on('mapLoad', mapLoadCallback);
   28. this.mapEventManager.on('mapClick', mapOnclickCallBack);
   29. }
   30. };
   31. // Obtains the connected watch device and subscribes to the watch's message sending event.
   32. this.connectUtils.getConnectedDevices();
   33. try {
   34. this.connectUtils.notifyClient = wearEngine.getNotifyClient(this.getUIContext().getHostContext());
   35. } catch (err) {
   36. hilog.error(0x0000, TAG,
   37. `Failed to get notify client. Cause code: ${err.code}, message: ${err.message}`);
   38. }
   39. }
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/SmartWatchMapNavigation/blob/master/products/phone/src/main/ets/pages/Index.ets#L49-L168)
2. 监听destination\_Position变化，调用[addMarker()](../harmonyos-references/map-map-mapcomponentcontroller.md#section0810361284)动态更新目的地地图标记。

   ```
   1. // Destination location information obtained based on the map click event.
   2. @StorageLink('destination_Position') @Watch('changeDestinationPositionMark') destination_Position: mapCommon.LatLng =
   3. {
   4. longitude: 0,
   5. latitude: 0
   6. };
   7. // ...
   8. /*
   9. * Triggered when destination_Position changes.
   10. * Used to refresh the destination marker on the map when the destination changes.
   11. */
   12. async changeDestinationPositionMark() {
   13. if (this.mapController) {
   14. this.mapController.clear();
   15. let markerOptions: mapCommon.MarkerOptions = {
   16. position: this.destination_Position,
   17. rotation: 0,
   18. visible: true,
   19. zIndex: 0,
   20. alpha: 1,
   21. anchorU: 0.5,
   22. anchorV: 1,
   23. clickable: true,
   24. draggable: true,
   25. flat: false,
   26. };
   27. try {
   28. await this.mapController.addMarker(markerOptions);
   29. } catch (err) {
   30. hilog.error(0x0000, TAG,
   31. `Failed to add marker. Cause code: ${err.code}, message: ${err.message}`);
   32. }
   33. }
   34. }
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/SmartWatchMapNavigation/blob/master/products/phone/src/main/ets/pages/Index.ets#L48-L112)

**路径导航：**

1. 根据当前位置与目的地位置，生成导航路线信息。

   ```
   1. Button($r('app.string.DrawRoute'))
   2. .width(158)
   3. .height(40)
   4. .onClick(async () => {
   5. let params: navi.RouteParams = {
   6. origins: [
   7. {
   8. latitude: this.myLocation.latitude,
   9. longitude: this.myLocation.longitude
   10. }
   11. ],
   12. destination: this.destination_Position,
   13. language: 'zh_CN'
   14. };
   15. const result = await navi.getWalkingRoutes(params);
   16. let drawRouteUtil: DrawRouteUtils = new DrawRouteUtils();
   17. // Draw a route on a map using navigation route information.
   18. drawRouteUtil.drawRoute(this.mapController, result.routes[0].steps[0].roads)
   19. })
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/SmartWatchMapNavigation/blob/master/products/phone/src/main/ets/pages/Index.ets#L196-L214)
2. 通过调用[addPolyline()](../harmonyos-references/map-map-mapcomponentcontroller.md#section6818109112812)接口，结合导航路线信息，绘制可视化路径。

   ```
   1. /*
   2. * Draw a navigation route on a map
   3. * The first parameter needs to be transferred to MapComponentController to operate the map.
   4. * The second parameter needs to pass in the navigation information to draw the navigation route.
   5. * @param mapController : map controller for drawing markers or routes on a map.
   6. * @param steps : Navigation route information obtained through the Map Kit
   7. */
   8. async drawRoute(mapController: map.MapComponentController | undefined, steps: Array<navi.RouteRoad>) {
   9. if (mapController === undefined) {
   10. hilog.info(0X0000, TAG, 'Drawing failed');
   11. return;
   12. }
   13. let roads: Array<mapCommon.LatLng> = [];
   14. let des_arr: RouteInfomation[] = [];
   15. for (let index = 0; index < steps.length; index++) {
   16. for (let i = 0; i < steps[index].polyline.length; i++) {
   17. roads.push(steps[index].polyline[i]);
   18. des_arr.push(new RouteInfomation(steps[index].action as string, steps[index].distance, steps[index].duration))
   19. }
   20. }

   22. // The route segment information is stored in the AppStorage and then sent to the watch through the WearEngine.
   23. AppStorage.setOrCreate('routeInfomation', des_arr);

   25. let polylineOption: mapCommon.MapPolylineOptions = {
   26. points: roads,
   27. color: 0xFF089C57,
   28. jointType: mapCommon.JointType.ROUND,
   29. width: 24
   30. };

   32. // Use MapComponentController to draw a route on a map
   33. mapController.addPolyline(polylineOption).catch((error: Error) => {
   34. let err = error as BusinessError;
   35. if (err.code) {
   36. hilog.error(0x0000, TAG,
   37. `Failed to add poly line. Cause code: ${err.code}, message: ${err.message}`);
   38. }
   39. }).then(() => {
   40. hilog.info(0X0000, TAG, 'Drawing success');
   41. });
   42. }
   ```

   [DrawRouteUtils.ets](https://gitcode.com/HarmonyOS_Samples/SmartWatchMapNavigation/blob/master/commons/map/src/main/ets/common/utils/DrawRouteUtils.ets#L26-L67)

说明

地图实现依赖Map Kit能力，使用前首先需要申请Map服务，详情请参考Map Kit[开发准备](../harmonyos-guides/map-config-agc.md)。

### 互联通信

智能穿戴设备协同导航系统通过设备间通信协议实现双端数据同步，各类消息通过头部TAG标志位进行区分，具体消息类型定义如下表所示：

**表2** 消息实体类消息类型表

| 消息类型 | TAG标志位取值 | 作用 |
| --- | --- | --- |
| 路线信息 | 0 | 用于同步导航路线信息。 |
| 目的地定位 | 1 | 用于同步目的地定位信息。 |
| 信号信息 | 2及以上 | 用于信号，包括手机侧告知手表侧导航已开启、手表侧告知手机侧导航结束等。 |

在对端消息监听（手机端与智能穿戴设备端均使用，监听对方发来的消息）的回调中，会对发送的消息进行转码，并根据TAG标志位进行数据的存储，分别用于不同的逻辑。

```
1. /**
2. * Callback Method for Listening to Peer Communication.
3. */
4. private onMsgCallback: Callback<wearEngine.P2pMessage> = (data: wearEngine.P2pMessage): void => {
5. let str: string = '';
6. // Decodes the intercepted content into a character string.
7. if (canIUse('SystemCapability.Utils.Lang')) {
8. let decoder: util.TextDecoder = util.TextDecoder.create();
9. str = decoder.decodeToString(data.content);
10. }
11. // Convert the JSON character string to the CommunicationInformation type.
12. let communicationInformation: CommunicationInformation = JSON.parse(str);
13. // Determine the information type based on the tag.
14. if (communicationInformation.tag === 0) {
15. // When tag is set to 0,Indicates that the transferred information is path description information,
16. // which is stored in AppStorage to refresh the watch navigation page.
17. AppStorage.setOrCreate('route_information', communicationInformation.routeInfomation);
18. } else if (communicationInformation.tag === 1) {
19. // When tag is set to 1, Indicates that the transferred information is destination location information
20. // and is saved to the AppStorage for synchronizing the destination logo of the mobile phone and watch.
21. AppStorage.setOrCreate('destination_Position', communicationInformation.location);
22. } else if (communicationInformation.tag === 2) {
23. // Signal sent from your phone to your watch when navigation starts, indicating that navigation starts.
24. AppStorage.setOrCreate('isStartNavigation', true);
25. } else {
26. // Signal sent from your watch to your phone when navigation ends, indicating that navigation ends.
27. AppStorage.setOrCreate('isStartNavigation', false);
28. }
29. }
```

[CommunicationUtils.ets](https://gitcode.com/harmonyos_samples/SmartWatchMapNavigation/blob/master/commons/Communication/src/main/ets/common/utils/CommunicationUtils.ets#L69-L97)

说明

手机手表互联通信的具体实现，详情可参考[智能穿戴](bpta-smartwatch.md)与[应用间消息通信](../harmonyos-guides/p2p_communication.md)。

### 消息通知

在导航启动阶段，手机端需通过WearEngine提供的notify()接口向智能穿戴设备端发送通知消息，告知手表端导航开始。

```
1. /*
2. * Method of notifying a message to watch.
3. */
4. notifyMessage() {
5. // Configure the notification content.
6. // Including the package name of the notification source, notification title, and notification content.
7. let type1Notification: wearEngine.Notification = {
8. type: wearEngine.NotificationType.NOTIFICATION_WITHOUT_BUTTONS,
9. bundleName: 'com.example.smartwatchmapnavigation',
10. title: 'smartwatchmapnavigation',
11. text: 'walk navigation start',
12. }
13. let options: wearEngine.NotificationOptions = {
14. notification: type1Notification,
15. onAction: (feedback: wearEngine.NotificationFeedback) => {
16. hilog.info(0x000, TAG,
17. `one button notify get feedback is ${feedback.action ? feedback.action : feedback.errorCode}`);
18. }
19. }

21. // Sends a notification to the watch based on notifyClient.
22. // This method can be invoked only by apps on mobile phones.
23. this.notifyClient!.notify(this.deviceRandomId, options).then(result => {
24. hilog.info(0x000, TAG, `Succeeded in sending notification.`);
25. }).catch((error: BusinessError) => {
26. hilog.error(0x000, TAG, `Failed to send notification. Code is ${error.code}, message is ${error.message}`);
27. })
28. }
```

[CommunicationUtils.ets](https://gitcode.com/harmonyos_samples/SmartWatchMapNavigation/blob/master/commons/Communication/src/main/ets/common/utils/CommunicationUtils.ets#L154-L181)

说明

消息通知依赖wearengine服务，详情可参考[智能穿戴](bpta-smartwatch.md)与[穿戴设备模板化通知](../harmonyos-guides/device_notification.md)。

### 振感提示

在导航过程中，智能穿戴设备需要使用振动向开发者提供振感提示。

```
1. // Vibration Tools Class
2. export class VibratorUtil {
3. /*
4. * The method of  Vibration.
5. */
6. Vibrator() {
7. try {
8. // Use the startVibration method to enable vibration and set the duration.
9. vibrator.startVibration({
10. type: 'time',
11. duration: 1000,
12. }, {
13. id: 0,
14. usage: 'alarm'
15. }, (error: BusinessError) => {
16. if (error) {
17. hilog.error(0x0000, TAG, `Failed to start vibration. Code: ${error.code}, message: ${error.message}`);
18. return;
19. }
20. hilog.info(0x0000, TAG, 'Succeed in starting vibration');
21. });
22. } catch (err) {
23. let e: BusinessError = err as BusinessError;
24. hilog.error(0x00000, TAG, `An unexpected error occurred. Code: ${e.code}, message: ${e.message}`);
25. }
26. }
27. }
```

[VibratorUtil.ets](https://gitcode.com/harmonyos_samples/SmartWatchMapNavigation/blob/master/commons/vibrator/src/main/ets/commons/VibratorUtil.ets#L23-L49)

说明

使用振动需要进行权限申请，详情可参考[振动开发指导(ArkTS)](../harmonyos-guides/vibrator-guidelines.md)。

## 示例代码

* [基于WearEngine实现协同导航应用](https://gitcode.com/harmonyos_samples/SmartWatchMapNavigation)
