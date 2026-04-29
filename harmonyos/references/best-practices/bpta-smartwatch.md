---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-smartwatch
title: 智能穿戴应用开发
breadcrumb: 最佳实践 > 多端设备体验提升 > 穿戴 > 智能穿戴应用开发
category: best-practices
scraped_at: 2026-04-29T14:13:00+08:00
doc_updated_at: 2026-03-12
content_hash: sha256:e6fb60e0cab91c654a8976f27f52375e0c11c2d281a8fe7799ee583fd8f3d621
---

## 概述

智能穿戴是一种腕部可穿戴设备，提供沟通功能和与移动设备的数据交互功能。

### 设备特点

智能穿戴设备具有以下显著特点：

* 表盘屏幕尺寸较小，多为圆形表盘。
* 随腕携带，查看表盘屏幕更为便捷。
* 电池容量较小，一般小于1000mAh。
* 具备特有表冠旋转交互功能。
* 支持更为丰富的传感器。

### 主要型号

支持HarmonyOS 5及以上的智能穿戴设备主要有Watch 5。

| 产品名称 | 示意图 |
| --- | --- |
| Watch 5 |  |

## 硬件说明

### 屏幕规格信息

以Watch 5设备为例，智能穿戴设备屏幕不支持旋转，屏幕旋转角度为0°，屏幕方向为竖屏，更多屏幕规格信息参考下表。

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 屏幕旋转角度(rotation) | 0（0度） | 1（90度） | 2（180度） | 3（270度） |
| 示意图 |  | NA | NA | NA |
| [屏幕方向orientation](../harmonyos-references/js-apis-display.md#orientation10) | 0-PORTRAIT | NA | NA | NA |
| 分辨率（px） | 466 \* 466 | NA | NA | NA |
| 分辨率（vp） | 233 \* 233 | NA | NA | NA |
| 横纵断点 | 横向断点xs，纵向断点md | NA | NA | NA |

## 体验标准

应用体验建议分为功能与兼容性、稳定性、性能、功耗、安全和UX六个部分，详细信息如下所示。

| 名称 | 简介 |
| --- | --- |
| [应用基础功能和兼容性体验建议](../harmonyos-guides/experience-suggestions-compatibility.md) | 应用与OS兼容、应用与设备兼容、应用升级兼容、功能体验相关等 |
| [应用稳定性体验建议](../harmonyos-guides/experience-suggestions-stability.md) | 长时间运行故障率（崩溃、冻屏等）、长时间运行内存资源异常 |
| [应用性能体验建议](../harmonyos-guides/performance-experience-suggestions.md) | 时延、帧率流畅体验和内存占用、CPU占用、线程数等资源占用约束 |
| [应用功耗体验建议](../harmonyos-guides/app-power-experience-standards.md) | 后台任务使用、后台硬件器件资源/软件系统资源占用管控，分布式资源占用等 |
| [应用安全隐私体验建议](../harmonyos-guides/security-privacy-experience-standards.md) | 基础安全、恶意软件、应用安全、隐私合规等 |
| [应用UX体验建议](../harmonyos-guides/experience-suggestions-ux.md) | 设计规范、设计约束的符合性，UX精致体验要求等 |

智能穿戴设备主要在UX和性能体验上有着特殊的适配体验和建议。

### UX体验建议

**体验设计标准**

* 使用系统控件：利用系统提供的按钮及导航点等标准控件，确保良好基础体验，同时减少设计和开发的工作量。必要时自定义控件样式和大小，以体现品牌特征。
* 使用合适的应用架构：根据业务特点采用适宜架构。例如，单一功能类应用采用页面横向或纵向平铺的平级架构，确保主要功能在首屏展示。
* 保证页面正常显示：根据智能穿戴设备的屏幕形状合理设计界面，确保界面正常显示，不影响用户使用。
* 充分利用表冠和按键交互：除屏幕手势交互外，表冠和按键交互可帮助用户在盲操场景下快速完成特定操作。例如，单击表冠快速开始或暂停运动记录。

**体验设计差异点**

智能穿戴设备采用独特的圆形屏幕设计，显示面积远小于手机。开发时需确保应用界面完整适配圆形显示区域，避免内容截断、变形或关键元素被遮挡。

**应用设计最佳实践**

根据上述UX体验标准和设计差异点，各垂域应用应根据功能和场景特点进行智能穿戴UX设计。例如，运动健康类应用可充分利用表冠进行运动模式切换或强度调节，更多垂域设计信息和方案可参考[应用设计最佳实践](../design-guides/practices-overview-0000001746498066.md)。通用设计场景请参考[智能穿戴](../design-guides/wearable-0000002164711032.md)。

### 性能体验建议

**体验设计标准**

优化续航表现。合理控制应用的CPU、传感器及网络资源使用，避免后台频繁唤醒，延长设备续航时间，提升用户使用体验。

**体验设计差异点**

为提升智能穿戴设备续航能力并优化用户体验，系统应执行严格功耗管理措施，详情参见[功耗管理优化](bpta-smartwatch.md#section7617165395315)章节。

**应用设计最佳实践**

参考[应用功耗体验设计](bpta-power-consumption-experience.md#section818174004918)。

## 工程管理

### 工程配置

开发在智能穿戴设备上的应用，需要在module.json5配置文件的module字段中，为deviceTypes字段设置wearable类型。更多详情可参考[deviceTypes标签](../harmonyos-guides/module-structure.md#devicetype标签)。若当前已有适配轻量级智能穿戴的工程，需要迁移适配智能穿戴设备，可以参考[FA工程迁移指导](bpta-smartwatch.md#section1219382121110)。

### 包管理策略

由于应用在智能穿戴设备上的页面设计、功能形态会与其他设备有明显差异，因此推荐独立HAP精准适配的HAP包的管理策略：

* 独立HAP精准适配：智能穿戴设备与其他设备在页面设计、功能形态上存在显著差异，应创建独立HAP包，分别构建面向phone/tablet与wearable等设备的模块化组件，实现设备专属的UX设计、资源优化与体验定制。

更多详情可参见[分层架构设计](bpta-layered-architecture-design.md)的产品定制层相关内容。

### 工程调试

智能穿戴设备工程调试规范如下：

* 调试模式：智能穿戴设备推荐使用WiFi无线调试（支持自动签名）。无线调试内容可参考[使用无线调试连接方式](../harmonyos-guides/ide-run-device.md#section9315596477)。
* 调试稳定性：设备熄屏后WiFi调试连接会断开，建议在系统设置中延长自动熄屏时间，确保调试过程稳定。
* 设备授权：首次调试时，手表将弹出“信任设备”提示，需点击“信任”以允许IDE连接。

## 界面开发

### 圆形屏适配建议

智能穿戴设备特殊的圆形表盘，需要在设计智能穿戴设备页面时进行考虑。详情开发指导可参考[圆形屏](bpta-multi-device-screen-layout.md#section1298815351411)。

## 交互体验

智能穿戴的交互方式为触控屏，常见的操作有点击、双击、长按、拖拽、滑动等，应用可根据这些操作进行功能适配，详情可参考[多设备交互](bpta-multi-interaction.md)。除上述触控屏交互方式外，智能穿戴设备还支持表冠交互和智慧手势。

### 旋转表冠交互

华为智能穿戴的表冠（上键）支持按压与旋转两种交互方式，其旋转操作可触发实时交互响应。系统通过[onDigitalCrown()](../harmonyos-references/ts-universal-events-crown.md#ondigitalcrown)回调函数处理表冠旋转事件，并已为常用组件内置了表冠交互支持。

主要特性：

* 事件响应：旋转操作实时触发onDigitalCrown回调

  ```
  1. Text(this.count.toString())
  2. // ...
  3. .onDigitalCrown((event: CrownEvent) => {
  4. event.stopPropagation();
  5. this.count += event.degree;
  6. })
  ```

  [DigitalCrownEvent.ets](https://gitcode.com/harmonyos_samples/multi-device-interaction/blob/master/wearable/src/main/ets/view/DigitalCrownEvent.ets#L34-L46)
* 系统集成：滚动条等组件自动响应表冠旋转方向

默认支持表冠交互的组件包括：

* 滑动选择类：Slider、Scroll、ArcSwiper、Refresh
* 列表展示类：List、Grid、WaterFlow、ArcList
* 时间日期类：DatePicker、TimePicker
* 文本选择类：TextPicker

开发者可通过开放接口自定义表冠事件处理逻辑，实现更丰富的交互体验。

说明

关于智能穿戴表冠旋转事件的开发，可以参考[表冠事件](../harmonyos-references/ts-universal-events-crown.md)。

### 智慧手势

智慧手势是智能穿戴设备除屏幕交互、表冠交互和按键交互外的独特感知交互方式。在情景障碍，需要单手处理的场景，用户可以使用敲击手指和滑动指关节实现控制和切换选择诉求。

说明

使用智慧手势功能要确保设备上的智慧手势识别开关已打开。

**交互场景**

* 提醒场景，需及时处理的控制，如电话、闹钟等。
* 高频使用场景的便捷操控，如播控中心“下一首”。
* 不方便双手点击操作的场景，如遥控拍照。

**手势类型**

* 捏合确认：拇指和食指快速触碰两下，表示确认当前焦点的操作。常用于确认键、音乐暂停/播放等场景。

实现原理：系统识别手势后，会触发组件的[onKeyEvent](../harmonyos-references/ts-universal-events-key.md#onkeyevent)事件，KeyCode为KEYCODE\_ENTER，type为KeyType.Down，应用可以在该条件触发后进行功能执行，如暂停音乐。

示例代码：

```
1. .onKeyEvent((event: KeyEvent) => {
2. if (event.keyCode === KeyCode.KEYCODE_ENTER && event.type === KeyType.Down) {
3. // Trigger the pinching gesture
4. this.oneButton1Color = '#ffe3ba51';
5. this.oneButton1Text = 'Confirm';
6. }
7. })
```

[SmartGestureEvent.ets](https://gitcode.com/harmonyos_samples/multi-device-interaction/blob/master/wearable/src/main/ets/view/SmartGestureEvent.ets#L81-L87)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f6/v3/iycdYj5NSEqjrSF4_NxOfA/zh-cn_image_0000002493762393.png?HW-CC-KV=V1&HW-CC-Date=20260429T061258Z&HW-CC-Expire=86400&HW-CC-Sign=DE5B4451DA8D156EC101239C9FDF5CCE1F2E9B329760E5F0A91C7DA04D2091C0 "点击放大")

* 滑动切焦：切换当前焦点，以确认下一步操作，通过将拇指沿食指第二关节向指尖快速滑动两下切换焦点，后续再进行确认操作，可以用于切换到取消按钮，或切换到播放下一首按钮上，用于取消消息、切换歌曲等操作场景。

实现原理：系统识别手势后，会分别触发失焦组件和获焦组件的[onBlur](../harmonyos-references/ts-universal-focus-event.md#onblur)和[onFocus](../harmonyos-references/ts-universal-focus-event.md#onfocus)事件，应用可以在该条件触发后进行功能执行，如更改获焦组件的样式为高亮展示。

示例代码：

```
1. .onFocus(() => {
2. this.oneButton1Color = '#ff57c853';
3. this.oneButton1Text = 'Hover';
4. this.oneButton2Text = 'Two';
5. })
6. .onBlur(() => {
7. this.oneButton1Color = '';
8. this.oneButton1Text = 'One';
9. })
```

[SmartGestureEvent.ets](https://gitcode.com/harmonyos_samples/multi-device-interaction/blob/master/wearable/src/main/ets/view/SmartGestureEvent.ets#L74-L82)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d9/v3/i28jdO1-RQ2rzAMyzmx0wQ/zh-cn_image_0000002460802852.png?HW-CC-KV=V1&HW-CC-Date=20260429T061258Z&HW-CC-Expire=86400&HW-CC-Sign=D6CFD263F32A834D8041E4223CB18C43C4B867DFEC64FD1BBED41713C2AC2351 "点击放大")

智慧手势交互的前提是组件获焦。首先使用[activate](../harmonyos-references/arkts-apis-uicontext-focuscontroller.md#activate14)激活当前界面的焦点激活态。

```
1. this.getUIContext().getFocusController().activate(true, false);
```

[SmartGestureEvent.ets](https://gitcode.com/HarmonyOS_Samples/multi-device-interaction/blob/master/wearable/src/main/ets/view/SmartGestureEvent.ets#L36-L36)

激活焦点激活态后，可调用[requestFocus()](../harmonyos-references/arkts-apis-uicontext-focuscontroller.md#requestfocus12)方法使目标组件获得焦点，随后手势操作方可生效。示例代码如下，页面渲染后默认使得id为"btn1"的按钮获焦：

```
1. // register a button to get focus by default.
2. this.getUIContext().getFocusController().requestFocus('btn1');
```

[SmartGestureEvent.ets](https://gitcode.com/HarmonyOS_Samples/multi-device-interaction/blob/master/wearable/src/main/ets/view/SmartGestureEvent.ets#L43-L44)

退出页面时，设置当前界面的焦点激活态为false，退出焦点激活态。

```
1. aboutToDisappear(): void {
2. this.getUIContext().getFocusController().activate(false);
3. }
```

[SmartGestureEvent.ets](https://gitcode.com/HarmonyOS_Samples/multi-device-interaction/blob/master/wearable/src/main/ets/view/SmartGestureEvent.ets#L52-L54)

## 功能开发

### 消息通知

华为智能穿戴的消息通知来源包括：

* 手机应用通知：应用通过华为运动健康授权消息通知权限后，配对手机的应用通知将同步至穿戴设备。
* 手机主动推送：手机应用使用WearEngine接口直接向穿戴设备发送消息通知。
* 穿戴设备本地通知：手表应用通过Notification Kit自主发送通知。

**手机应用通知**

在华为运动健康APP中，进入消息通知设置界面，为指定手机应用开启通知权限，即可将该应用的消息实时同步至已配对的华为智能穿戴设备。

**手机主动推送**

手机应用可以通过[WearEngine](../harmonyos-references/wearengine_api.md)的[NotifyClient.notify()](../harmonyos-references/wearengine_api.md#section087562072313)实现手机向智能穿戴设备主动推送消息通知，开发步骤如下：

1. 通过[wearEngine.getNotifyClient()](../harmonyos-references/wearengine_api.md#section552416431386)获取Notify客户端类。

   ```
   1. // Used to notify message
   2. notifyClient: wearEngine.NotifyClient | undefined;
   ```

   [CommunicationUtils.ets](https://gitcode.com/harmonyos_samples/SmartWatchMapNavigation/blob/master/commons/Communication/src/main/ets/common/utils/CommunicationUtils.ets#L44-L45)

   使用当前组件所在Ability的Context，获取Notify模块的客户端。

   ```
   1. try {
   2. this.connectUtils.notifyClient = wearEngine.getNotifyClient(this.getUIContext().getHostContext());
   3. } catch (err) {
   4. hilog.error(0x0000, TAG,
   5. `Failed to get notify client. Cause code: ${err.code}, message: ${err.message}`);
   6. }
   ```

   [Index.ets](https://gitcode.com/harmonyos_samples/SmartWatchMapNavigation/blob/master/products/phone/src/main/ets/pages/Index.ets#L161-L166)
2. 通过NotifyClient.notify()实现手机向智能穿戴设备发送模板化通知。

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

使用WearEngine的NotifyClient.notify()需要获取WearEngine权限，具体可以参考[申请接入Wear Engine服务](../harmonyos-guides/wearengine_apply.md)。

**智能穿戴设备本地通知**

智能穿戴设备应用可以通过[Notification Kit（用户通知服务）](../harmonyos-references/js-apis-notificationmanager.md)实现自主发送通知。

1. 请求通知授权。

   可通过requestEnableNotification的错误码判断用户是否授权。若返回的错误码为1600004，即为拒绝授权。

   ```
   1. aboutToAppear() {
   2. let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
   3. notificationManager.isNotificationEnabled().then((data: boolean) => {
   4. hilog.info(DOMAIN_NUMBER, TAG, "isNotificationEnabled success, data: " + JSON.stringify(data));
   5. if (!data) {
   6. notificationManager.requestEnableNotification(context).then(() => {
   7. hilog.info(DOMAIN_NUMBER, TAG, `[ANS] requestEnableNotification success`);
   8. }).catch((err: BusinessError) => {
   9. if (1600004 == err.code) {
   10. hilog.error(DOMAIN_NUMBER, TAG,
   11. `[ANS] requestEnableNotification refused, code is ${err.code}, message is ${err.message}`);
   12. } else {
   13. hilog.error(DOMAIN_NUMBER, TAG,
   14. `[ANS] requestEnableNotification failed, code is ${err.code}, message is ${err.message}`);
   15. }
   16. });
   17. }
   18. }).catch((err: BusinessError) => {
   19. hilog.error(DOMAIN_NUMBER, TAG, `isNotificationEnabled fail, code is ${err.code}, message is ${err.message}`);
   20. });
   21. }
   ```

   [NotifyPage.ets](https://gitcode.com/harmonyos_samples/Phone_Connection/blob/master/products/phone/src/main/ets/pages/NotifyPage.ets#L30-L50)
2. 构造NotificationRequest对象，并发布通知。

   ```
   1. Button('发送通知')
   2. .onClick(()=>{
   3. let notificationRequest: notificationManager.NotificationRequest = {
   4. id: 1,
   5. content: {
   6. // General text type notification.
   7. notificationContentType: notificationManager.ContentType.NOTIFICATION_CONTENT_BASIC_TEXT,
   8. normal: {
   9. title: 'test_title',
   10. text: 'test_text',
   11. additionalText: 'test_additionalText',
   12. }
   13. }
   14. };
   15. notificationManager.publish(notificationRequest, (err: BusinessError) => {
   16. if (err) {
   17. hilog.error(DOMAIN_NUMBER, TAG, `Failed to publish notification. Code is ${err.code}, message is ${err.message}`);
   18. return;
   19. }
   20. hilog.info(DOMAIN_NUMBER, TAG, 'Succeeded in publishing notification.');
   21. });
   22. })
   ```

   [NotifyPage.ets](https://gitcode.com/harmonyos_samples/Phone_Connection/blob/master/products/phone/src/main/ets/pages/NotifyPage.ets#L56-L77)

### 手机与智能穿戴设备互联通信

手机与智能穿戴设备的互联通信是智能穿戴设备的核心开发场景，开发者可通过[WearEngine](../harmonyos-references/wearengine_api.md)提供的标准化接口实现跨设备交互，具体开发流程如下：

1. 通过wearEngine.getDeviceClient()获取Device模块的客户端用于获取连接设备。

   ```
   1. export class ConnectUtil {
   2. // Peer communication device entity class object
   3. device?: wearEngine.Device;
   4. // Unique ID of the peer communication device.
   5. deviceRandomId?: string;
   6. // Used to obtain linked devices
   7. deviceClient?: wearEngine.DeviceClient;
   8. // ...

   10. constructor(context: Context) {
   11. if (canIUse('SystemCapability.Health.WearEngine')) {
   12. this.deviceClient = wearEngine.getDeviceClient(context);
   13. // ...
   14. }
   15. }
   16. // ...
   17. }
   ```

   [ConnectUtil.ets](https://gitcode.com/harmonyos_samples/Phone_Connection/blob/master/commons/utils/src/main/ets/utils/ConnectUtil.ets#L35-L176)
2. 通过Device客户端获取当前已连接且支持wearEngine能力集的设备。

   ```
   1. // Obtains the information about the peer device connected to the peer device
   2. // and listens on the communication between the peer device and the peer device.
   3. async getConnectedDevices(): Promise<void> {
   4. try {
   5. if (canIUse('SystemCapability.Health.WearEngine')) {
   6. let devices: wearEngine.Device[] = await this.deviceClient?.getConnectedDevices() as wearEngine.Device[];
   7. this.device = devices[0];
   8. this.deviceRandomId = devices[0].randomId;
   9. }
   10. await this.registerMessageReceiver();
   11. } catch (err) {
   12. hilog.error(0x0000, TAG, 'getConnectedDevices is err' + JSON.stringify(err));
   13. }
   14. }
   ```

   [ConnectUtil.ets](https://gitcode.com/harmonyos_samples/Phone_Connection/blob/master/commons/utils/src/main/ets/utils/ConnectUtil.ets#L68-L82)
3. 通过获取P2P模块的客户端用于互联通信。

   ```
   1. export class ConnectUtil {
   2. // ...
   3. // Used to p2p
   4. p2pClient?: wearEngine.P2pClient;
   5. // ...

   7. constructor(context: Context) {
   8. if (canIUse('SystemCapability.Health.WearEngine')) {
   9. // ...
   10. this.p2pClient = wearEngine.getP2pClient(context);
   11. }
   12. }
   13. // ...
   14. }
   ```

   [ConnectUtil.ets](https://gitcode.com/harmonyos_samples/Phone_Connection/blob/master/commons/utils/src/main/ets/utils/ConnectUtil.ets#L36-L175)
4. 订阅对端设备应用向本侧发送消息的事件。

   ```
   1. // Callback Method for Listening to Peer Communication.
   2. private onMsgCallback: Callback<wearEngine.P2pMessage> = (data: wearEngine.P2pMessage): void => {
   3. // Decodes the intercepted content into a character string.
   4. let decoder: util.TextDecoder = util.TextDecoder.create();
   5. if (canIUse('SystemCapability.Health.WearEngine')) {
   6. let str: string = decoder.decodeToString(data.content);
   7. promptAction.openToast({
   8. message: 'message: ' + str,
   9. duration: 2000
   10. });
   11. }
   12. }

   14. // Listening to the communication between the peer end.
   15. async registerMessageReceiver(): Promise<void> {
   16. try {
   17. if (canIUse('SystemCapability.Health.WearEngine')) {
   18. await this.p2pClient?.registerMessageReceiver(this.deviceRandomId, appParam, this.onMsgCallback);
   19. hilog.info(0x0000, TAG, 'registerMessageReceiver is ok');
   20. }
   21. } catch (err) {
   22. hilog.error(0x0000, TAG, 'registerMessageReceiver is err ', JSON.stringify(err));
   23. }
   24. }

   26. // Disabling the Interception of Peer Communication。
   27. async unregisterMessageReceiver(): Promise<void> {
   28. try {
   29. if (canIUse('SystemCapability.Health.WearEngine')) {
   30. await this.p2pClient?.unregisterMessageReceiver(this.deviceRandomId, appParam, this.onMsgCallback);
   31. hilog.info(0x0000, TAG, 'unregisterMessageReceiver is ok');
   32. }
   33. } catch (err) {
   34. hilog.error(0x0000, TAG, 'unregisterMessageReceiver is err ', JSON.stringify(err));
   35. }
   36. }
   ```

   [ConnectUtil.ets](https://gitcode.com/harmonyos_samples/Phone_Connection/blob/master/commons/utils/src/main/ets/utils/ConnectUtil.ets#L102-L138)
5. 向对端设备发送消息。

   ```
   1. // Method of sending messages to the peer end
   2. async sendMessage(message: string): Promise<void> {
   3. try {
   4. let p2pMessage: wearEngine.P2pMessage = this.getP2pMessage(message);
   5. if (canIUse('SystemCapability.Health.WearEngine')) {
   6. let value = await this.p2pClient?.sendMessage(this.deviceRandomId, appParam, p2pMessage);
   7. hilog.info(0x0000, TAG, 'sendMessage value is' + JSON.stringify(value))
   8. }
   9. } catch (err) {
   10. hilog.error(0x0000, TAG, 'sys sendMessage is err ' + JSON.stringify(err));
   11. }
   12. }
   ```

   [ConnectUtil.ets](https://gitcode.com/harmonyos_samples/Phone_Connection/blob/master/commons/utils/src/main/ets/utils/ConnectUtil.ets#L86-L98)

说明

* 使用WearEngine实现互联通信功能需要获取WearEngine权限，具体可以参考[申请接入Wear Engine服务](../harmonyos-guides/wearengine_apply.md)。
* 手机端与智能穿戴端应用实现与对端互连通信的原理一致，详细开发方案可参考[实现手机手表互联通信与手表心率监听](https://gitcode.com/harmonyos_samples/Phone_Connection)。

### 功耗管理优化

为提升智能穿戴设备续航能力并给用户带来更持久、更流畅的使用体验，可以采取以下措施：

* 显示优化配置
  1. 默认启用深色主题模式降低显示能耗。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/34/v3/ytmtGZIZS9qBdl5-CMf6zw/zh-cn_image_0000002460643240.png?HW-CC-KV=V1&HW-CC-Date=20260429T061258Z&HW-CC-Expire=86400&HW-CC-Sign=8121107BAB659ACA9F227CA6D9BC9ABAAA737D318E71936010C53EED11D03DCD "点击放大")
  2. 仅允许视频、游戏、导航等必要场景保持屏幕常亮。
* 后台应用管理
  1. 关键服务类应用（闹钟、日程提醒、邮件、IM类应用）可依据实际需求启动。
  2. 除被前台应用拉起的情况外，闹钟、日程提醒、邮件、IM类应用按需自启，禁止非必要应用以任何形式自启动。
* 定位服务规范
  1. 后台GPS仅对导航、运动健康等核心功能开放。
  2. 严禁非用户交互场景在后台调用定位服务。

若应用设计导航、视频等需要保持应用常亮，可以根据如下步骤实现：

1. 设定应用屏幕常亮首先需要在EntryAbility获取window实例。

   ```
   1. onWindowStageCreate(windowStage: window.WindowStage): void {
   2. let windowClass: window.Window | undefined = undefined;
   3. window.getLastWindow(this.context, (err: BusinessError, data: window.Window) => {
   4. const errCode: number = err.code;
   5. if (errCode) {
   6. hilog.error(0x0000, TAG, 'Failed to obtain the top window. Cause: ' + JSON.stringify(err));
   7. return;
   8. }
   9. windowClass = data;
   10. hilog.info(0x0000, TAG, 'Succeeded in obtaining the top window. Data: ' + JSON.stringify(data));
   11. AppStorage.setOrCreate('windowClass', windowClass);
   12. });
   13. // ...
   14. }
   ```

   [WearableAbility.ets](https://gitcode.com/harmonyos_samples/SmartWatchMapNavigation/blob/master/products/wearable/src/main/ets/wearableability/WearableAbility.ets#L40-L86)
2. 调用window的[setWindowKeepScreenOn()](../harmonyos-references/arkts-apis-window-window.md#setwindowkeepscreenon9)接口，设置屏幕常亮。详细的接口信息请参考[窗口管理](../harmonyos-references/arkts-apis-window-window.md#setwindowkeepscreenon9-1)。

   ```
   1. // Window object obtained from EntryAbility, which is used to ensure that the screen is steady on during navigation.
   2. @StorageLink('windowClass') windowClass: window.Window | undefined = undefined;
   3. // ...

   5. aboutToAppear(): void {
   6. // ...
   7. if (this.windowClass) {
   8. this.windowClass.setWindowKeepScreenOn(true, (err: BusinessError) => {
   9. const errCode: number = err.code;
   10. if (errCode) {
   11. hilog.error(0x0000, TAG,
   12. `Failed to set the screen to be always on. Cause code: ${err.code}, message: ${err.message}`);
   13. return;
   14. }
   15. hilog.info(0x0000, TAG, 'Succeeded in setting the screen to be always on.');
   16. });
   17. }
   18. }
   ```

   [NavigationPageView.ets](https://gitcode.com/harmonyos_samples/SmartWatchMapNavigation/blob/master/products/wearable/src/main/ets/view/NavigationPageView.ets#L37-L108)

## 常见问题

### 同步/异步接口无法正常调用或功能异常

**问题现象**

迁移项目后，原项目中的同步/异步接口无法正常调用或功能异常。

**解决方案**

需要改写接口调用方式，以[huks.generateKeyItem()](../harmonyos-references/js-apis-huks.md#huksgeneratekeyitem9)接口为例，原项目中：

```
1. huks.generateKeyItem(alias, options, callback);
```

迁移项目后，改写为：

```
1. try {
2. const data = await huks.generateKeyItem(alias, options);
3. // Result of successful processing.
4. } catch (error) {
5. // Capture and handle exceptions.
6. }
```

### FA工程迁移后，无法与手机侧通信

**问题现象**

完成项目迁移后，原项目有与手机侧通信交互的功能，但是新项目该功能无法使用。

**问题原因**

应用使用指纹信息来验证进行应用间的通信，迁移后应查询新应用的APP ID并在配置文件中更改值。

**解决方案**

通过"hdc shell bm dump –n YourBundleName | grep appIdentifier"获取穿戴侧应用的APP ID，在两侧应用的配置文件中更改fingerprint。

### 一多应用中如何区分智能穿戴设备

**问题现象**

智能穿戴设备与手机、平板等设备差异较大，在一多应用中如何区分智能穿戴设备与其他设备。

**解决方案**

可以通过在工程架构中创建单独的模块进行区分。在product层为智能穿戴单独创建HAP包独立开发。详情可以参考[包管理策略](bpta-smartwatch.md#section1870515318482)。

### 手表应用发布注意事项

**问题现象**

手表应用在涉及到智能穿戴设备与轻量级智能穿戴设备时，应用发布的常见问题以及注意事项。

1. 手表应用在发布时，仅可选择“手表”设备，无法对智能穿戴与轻量级智能穿戴做区分。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/74/v3/-wIaOIleRImka9bFTGyGTA/zh-cn_image_0000002504130021.png?HW-CC-KV=V1&HW-CC-Date=20260429T061258Z&HW-CC-Expire=86400&HW-CC-Sign=F60E3BA541B17F8717C8E7B6423385C1516043081540ACC915BBA428263FDB28 "点击放大")
2. 应用涉及两种穿戴设备时，应用发布是否需要上传两个对应的发布包。

**解决方案**

1. 点击确认后跳转至发布页，可在发布页具体选择设备类型。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/32/v3/CCYvHaNLQgeT4K1irU6wag/zh-cn_image_0000002504014565.png?HW-CC-KV=V1&HW-CC-Date=20260429T061258Z&HW-CC-Expire=86400&HW-CC-Sign=54D8261A53EFF6779ED4AADF45D0C361568DF934A2C8E74DA38CBAAE3C452941 "点击放大")
2. 智能穿戴支持ArkTS与JS，轻量级智能穿戴仅支持JS，若应用发布包支持在智能穿戴与轻量级智能穿戴上运行，则无需对应用发布包做区分，若应用发布包仅支持某一种穿戴设备，则需要分别为智能穿戴设备与轻量级智能穿戴设备创建AppID，并上传其对应的发布包。
3. APP创建流程可参考[创建HarmonyOS应用](../app/agc-help-create-app-0000002247955506.md)。

## 附：FA工程迁移指导

智能穿戴设备兼容FA模型，本章节提供了如何将使用JS构建的[轻量级智能穿戴](bpta-lite-wearable-guide.md)项目迁移到智能穿戴设备上继续使用，实现功能的延续与适配。

以[轻量级智能穿戴应用开发](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/tree/master/LiteWearable)为例，按照如下步骤，可以将使用JS构建的项目迁移到智能穿戴设备上：

1. 使用DevEco Studio创建项目。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/oljar3n5TmiuV80ROqGfOg/zh-cn_image_0000002493882313.png?HW-CC-KV=V1&HW-CC-Date=20260429T061258Z&HW-CC-Expire=86400&HW-CC-Sign=033E509E3AD09E920F09549C0A4F414AAF092AA04460A015FBA159E1A7EA23DE "点击放大")

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/11/v3/ePXiM9GzSZ6bWWH8hKq9yA/zh-cn_image_0000002493762397.png?HW-CC-KV=V1&HW-CC-Date=20260429T061258Z&HW-CC-Expire=86400&HW-CC-Sign=695F023B576CEFAF65EF498289AAD9F22836A22C24EDB7D3675E0221552EF5D6 "点击放大")

   工程名目录右键选择“New”->“Module”创建模块。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/fjiHiGG9QUWgRjmXBd1xBg/zh-cn_image_0000002460802860.png?HW-CC-KV=V1&HW-CC-Date=20260429T061258Z&HW-CC-Expire=86400&HW-CC-Sign=E6FCD24468865CA6DAE0D4695B15C142C934D1D46E9DE9C68516D01705678C3E "点击放大")

   选择“Empty Ability”，点击“Next”进入下一步。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b4/v3/PkswLByTS7Cl7nW89kf26w/zh-cn_image_0000002460643248.png?HW-CC-KV=V1&HW-CC-Date=20260429T061258Z&HW-CC-Expire=86400&HW-CC-Sign=F88E384D6CCD8FB0C5B2B2E5C089B90614F8E0447E2B0C2B5FC3EAF6D640C563 "点击放大")

   默认配置无需修改，点击“Next”进入下一步。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/df/v3/QQUNf1dQQ5C-PPumRjXMVQ/zh-cn_image_0000002493882333.png?HW-CC-KV=V1&HW-CC-Date=20260429T061258Z&HW-CC-Expire=86400&HW-CC-Sign=54147E299CC42F0D860B0C7023244BFC912820C96D64ADBEC3D6A564B7C5ABFF "点击放大")

   为了兼容智能穿戴，需要修改Ability name为“HiWearMainAbility”。点击“Finish”完成智能穿戴兼容模块创建。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d0/v3/NDVECewLTf6oapGtCw8nDg/zh-cn_image_0000002493762401.png?HW-CC-KV=V1&HW-CC-Date=20260429T061258Z&HW-CC-Expire=86400&HW-CC-Sign=81E856834C8D066010908FFBA2880C79ECDB07E9CFA200542B7AD3D15F207837 "点击放大")

   删除工程默认创建的entry模块，此时实现轻量级智能穿戴项目迁移的基础框架创建完成。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/23/v3/4Ae6XAwSRDamKaGDqR5GUQ/zh-cn_image_0000002460802864.png?HW-CC-KV=V1&HW-CC-Date=20260429T061258Z&HW-CC-Expire=86400&HW-CC-Sign=C51B483309291E97C22DEDEA5276818851A5A8D26C1D2618CFAD279B3BEA92B4 "点击放大")
2. 将原轻量级智能穿戴项目/entry/src/main/js目录下的代码文件及资源文件按对应位置迁移至新工程。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/66/v3/CLofC5KnRTKtWuCpcfzNCg/zh-cn_image_0000002460643268.png?HW-CC-KV=V1&HW-CC-Date=20260429T061258Z&HW-CC-Expire=86400&HW-CC-Sign=DB445E21BA167573362FBB37FB5DB544A837349E4AE9E22E2F6BC021FDF2E531 "点击放大")
3. 修改适配智能穿戴所需的配置文件。

   迁移的文件后需要修改config.json。修改资源文件的引用；pages目录下如果有新页面文件需添加至config.json；修改页面设计基线宽度为466。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5d/v3/4KiNMUfJRpeXpb9caMZ5pQ/zh-cn_image_0000002493882345.png?HW-CC-KV=V1&HW-CC-Date=20260429T061258Z&HW-CC-Expire=86400&HW-CC-Sign=0F41D714CB2800F07B13C95E9DD8B1FCE80974DC4AFB1CD9EFB631D7E9937BF4 "点击放大")

   config.json文件中补充所需的权限。如果原项目中使用了震动功能，需添加震动权限。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/49/v3/3YC-CJVLRIuqPEn94AzIdQ/zh-cn_image_0000002493762405.png?HW-CC-KV=V1&HW-CC-Date=20260429T061258Z&HW-CC-Expire=86400&HW-CC-Sign=834DEB806F6A61792E97081EB7BA1D1EFCBC0E770799DCC366E52DC5D8A4B63D "点击放大")
4. 代码适配。由于轻量级智能穿戴和智能穿戴的同步/异步机制不同，因此在迁移时时，需要对相关接口进行修改。以Huks接口为例，说明如何进行这些修改。

   ```
   1. huks.generateKeyItem(alias, options, callback);
   ```

   在轻量级智能穿戴设备上，回调将同步执行。但在智能穿戴设备上是异步的，因此需要更改书写样式增加await，保证代码同轻量级智能穿戴设备一样同步执行，代码如下所示：

   ```
   1. try {
   2. const data = await huks.generateKeyItem(alias, options);
   3. // Result of successful processing.
   4. } catch (error) {
   5. // Capture and handle exceptions.
   6. }
   ```
