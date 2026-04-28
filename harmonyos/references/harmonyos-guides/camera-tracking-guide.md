---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/camera-tracking-guide
title: 目标拍摄跟踪开发指南
breadcrumb: 指南 > 系统 > 硬件 > Mechanic Kit（机械设备管理服务） > 目标拍摄跟踪开发指南
category: harmonyos-guides
scraped_at: 2026-04-28T07:44:49+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:f8b72aa85306331452ef4b579c6da28f15b12cfcf7522ab5582caaea53418c90
---

从API version 20开始，支持使用机械体设备控制器，提供更丰富的拍摄体验，如目标跟踪和自动构图等专业功能，支持第三方应用。

目标拍摄跟踪功能通过机械体设备实现人脸和物体的自动化跟踪，提升拍摄质量和用户体验，助力开发者构建更自动化、高效的拍摄解决方案。

## 接口介绍

机械体设备控制器API的接口使用指导请参见[MechanicManager API参考](../harmonyos-references/js-apis-mechanicmanager.md)。

| 接口名 | 描述 |
| --- | --- |
| on(type: 'attachStateChange', callback: Callback<AttachStateChangeInfo>): void | 注册attachStateChange事件的回调监听，等待连接状态变化。  **说明**：从API version 20开始支持。 |
| off(type: 'attachStateChange', callback?: Callback<AttachStateChangeInfo>): void | 取消注册attachStateChange事件的回调监听。  **说明**：从API version 20开始支持。 |
| getAttachedMechDevices(): MechInfo[] | 获取已连接的机械体设备列表。  **说明**：从API version 20开始支持。 |
| setCameraTrackingEnabled(isEnabled: boolean): void | 启用或禁用摄像头跟踪。  **说明**：从API version 20开始支持。 |
| getCameraTrackingEnabled(): boolean | 检查是否启用了摄像头跟踪。  **说明**：从API version 20开始支持。 |
| on(type: 'trackingStateChange', callback: Callback<TrackingEventInfo>): void | 注册trackingStateChange事件的回调监听。  **说明**：从API version 20开始支持。 |
| off(type: 'trackingStateChange', callback?: Callback<TrackingEventInfo>): void | 取消注册trackingStateChange事件的回调监听。  **说明**：从API version 20开始支持。 |
| setCameraTrackingLayout(trackingLayout: CameraTrackingLayout): void | 设置摄像头跟踪布局。  **说明**：从API version 20开始支持。 |
| getCameraTrackingLayout(): CameraTrackingLayout | 获取此机械设备摄像头跟踪布局。  **说明**：从API version 20开始支持。 |
| on(type: 'rotationAxesStatusChange', callback: Callback<RotationAxesStateChangeInfo>): void | 注册rotationAxesStatusChange事件的回调监听。  **说明**：从API version 20开始支持。 |
| off(type: 'rotationAxesStatusChange', callback?: Callback<RotationAxesStateChangeInfo>): void | 取消注册rotationAxesStatusChange事件的回调监听。  **说明**：从API version 20开始支持。 |

## 开发步骤

### 开发准备

1. 支持Mechanic Kit协议的机械体设备。
2. 若要验证目标跟踪功能，主设备的相机驱动必须支持人脸检测。
3. 请将SDK更新到API 20或以上版本，具体操作参见[更新指南](ide-software-install.md)。
4. 请确保机械体设备已通过蓝牙与主设备连接。

### 管理设备连接状态

确保机械体设备连接或断开时，应用能及时响应，支持设备连接状态的动态管理。

1. 导入机械体设备管理模块。

   ```
   1. import { mechanicManager } from '@kit.MechanicKit';
   ```

   [ApiTestPage.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/MechanicKit/MechanicManagerSample/entry/src/main/ets/pages/ApiTestPage.ets#L16-L18)
2. 获取已连接的机械体列表。

   ```
   1. let savedMechanicIds: number[] = [];

   3. try {
   4. const devices = mechanicManager.getAttachedMechDevices();
   5. console.info('Connected devices:', devices);

   7. devices.forEach(device => {
   8. console.info(`Device ID: ${device.mechId}`);
   9. console.info(`Device Name: ${device.mechName}`);
   10. console.info(`Device Type: ${device.mechDeviceType}`);

   12. //保存设备类型为GIMBAL_DEVICE的设备的MechId
   13. if (device.mechDeviceType === mechanicManager.MechDeviceType.GIMBAL_DEVICE) {
   14. savedMechanicIds.push(device.mechId);
   15. console.info(`GIMBAL_TYPE device saved ID: ${device.mechId}`);
   16. } else {
   17. console.info(`Skip non-gimbal devices: ${device.mechId}`);
   18. }
   19. });

   21. console.info('List of saved gimbal device IDs:', savedMechanicIds);
   22. } catch (err) {
   23. console.error('Error getting attached devices:', err);
   24. }
   ```

   [ApiTestPage.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/MechanicKit/MechanicManagerSample/entry/src/main/ets/pages/ApiTestPage.ets#L179-L204)
3. 监听设备的连接状态变化，以便及时响应。

   ```
   1. const attachStateChangeCallback = (info: mechanicManager.AttachStateChangeInfo) => {
   2. if (info.state === mechanicManager.AttachState.ATTACHED) {
   3. console.info('Device attached:', info.mechInfo);
   4. // 执行设备连接的相关操作
   5. handleDeviceAttached(info.mechInfo);
   6. } else if (info.state === mechanicManager.AttachState.DETACHED) {
   7. console.info('Device detached:', info.mechInfo);
   8. // 执行设备断开的相关操作
   9. handleDeviceDetached(info.mechInfo);
   10. }
   11. };

   13. // 注册监听
   14. mechanicManager.on('attachStateChange', attachStateChangeCallback);
   ```

   [AttachStateChangeCallbackRegister.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/MechanicKit/MechanicManagerSample/entry/src/main/ets/pages/AttachStateChangeCallbackRegister.ets#L72-L87)
4. 处理设备的连接与断开的事件。

   ```
   1. function handleDeviceAttached(mechInfo: mechanicManager.MechInfo) {
   2. console.info(`New device is connected: ${mechInfo.mechName} (ID: ${mechInfo.mechId})`);
   3. savedMechanicIds.push(mechInfo.mechId);
   4. // To do sth.
   5. }

   7. function handleDeviceDetached(mechInfo: mechanicManager.MechInfo) {
   8. console.info(`Device disconnected: ${mechInfo.mechName} (ID: ${mechInfo.mechId})`);
   9. savedMechanicIds.filter(id => id !== mechInfo.mechId);
   10. // To do sth.
   11. }
   ```

   [AttachStateChangeCallbackRegister.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/MechanicKit/MechanicManagerSample/entry/src/main/ets/pages/AttachStateChangeCallbackRegister.ets#L22-L34)
5. 取消连接状态的监听。

   ```
   1. // 取消连接状态的监听
   2. mechanicManager.off('attachStateChange', attachStateChangeCallback);
   ```

   [AttachStateChangeCallbackRegister.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/MechanicKit/MechanicManagerSample/entry/src/main/ets/pages/AttachStateChangeCallbackRegister.ets#L108-L111)

### 控制设备目标跟踪拍摄

启用目标拍摄功能后，设备将自动识别人脸并进行跟踪拍摄。

1. 启用摄像头的目标拍摄功能。

   ```
   1. try {
   2. //检查前判断savedMechIds不为空
   3. // 检查跟踪状态
   4. const isEnabled = mechanicManager.getCameraTrackingEnabled();

   6. if (isEnabled == false) {
   7. // 开启摄像头跟踪
   8. mechanicManager.setCameraTrackingEnabled(true);
   9. console.info('Camera tracking enabled');
   10. }

   12. console.info('Is tracking currently enabled:', isEnabled);
   13. } catch (err) {
   14. console.error('Failed to enable camera tracking:', err);
   15. }
   ```

   [ApiTestPage.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/MechanicKit/MechanicManagerSample/entry/src/main/ets/pages/ApiTestPage.ets#L334-L350)
2. 监听相机跟踪状态的变化。

   ```
   1. const trackingStateCallback = (eventInfo : mechanicManager.TrackingEventInfo) => {
   2. switch (eventInfo.event) {
   3. case mechanicManager.TrackingEvent.CAMERA_TRACKING_USER_ENABLED:
   4. console.info('The user has enabled camera tracking');
   5. handleTrackingEnabled();
   6. break;
   7. case mechanicManager.TrackingEvent.CAMERA_TRACKING_USER_DISABLED:
   8. console.info('The user has disabled camera tracking');
   9. handleTrackingDisabled();
   10. break;
   11. case mechanicManager.TrackingEvent.CAMERA_TRACKING_LAYOUT_CHANGED:
   12. console.info('Tracking layout has changed');
   13. handleLayoutChanged();
   14. break;
   15. }
   16. };

   18. // 注册跟踪状态监听
   19. mechanicManager.on('trackingStateChange', trackingStateCallback);
   ```

   [ApiTestPage.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/MechanicKit/MechanicManagerSample/entry/src/main/ets/pages/ApiTestPage.ets#L404-L424)
3. 处理跟踪状态变化事件。

   ```
   1. function handleTrackingEnabled() {
   2. console.info('Handling camera tracking enable events');
   3. // 可以在此处更新UI状态
   4. updateTrackingUI(true);
   5. }

   7. function handleTrackingDisabled() {
   8. console.info('Handling camera tracking disabled events');
   9. // 可以在此处更新UI状态
   10. updateTrackingUI(false);
   11. }

   13. function handleLayoutChanged() {
   14. try {
   15. const newLayout = mechanicManager.getCameraTrackingLayout();
   16. console.info('New Tracking Layout:', newLayout);
   17. // 根据新布局更新UI
   18. updateLayoutUI(newLayout);
   19. } catch (err) {
   20. console.error('Failed to get new layout:', err);
   21. }
   22. }

   24. function updateTrackingUI(enabled: boolean) {
   25. // 更新UI显示跟踪状态
   26. // To do sth.
   27. console.info('Update tracking UI status:', enabled);
   28. }

   30. function updateLayoutUI(layout : mechanicManager.CameraTrackingLayout) {
   31. // 更新UI显示布局状态
   32. // To do sth.
   33. console.info('Update layout UI:', layout);
   34. }
   ```

   [ApiTestPage.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/MechanicKit/MechanicManagerSample/entry/src/main/ets/pages/ApiTestPage.ets#L25-L60)
4. 取消跟踪状态变化的监听。

   ```
   1. // 取消跟踪状态监听
   2. mechanicManager.off('trackingStateChange', trackingStateCallback);

   4. // 或者取消所有跟踪状态监听
   5. mechanicManager.off('trackingStateChange');
   ```

   [ApiTestPage.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/MechanicKit/MechanicManagerSample/entry/src/main/ets/pages/ApiTestPage.ets#L449-L455)

### 调试验证

请按照以下步骤调试验证，确保机械体设备管理功能正常：

**建立连接**

1. 确保机械体与开发设备已通过蓝牙配对并连接。
2. 将开发设备放置在机械体设备上。

**功能验证步骤**

1. **设备列表查询**：调用 getAttachedMechDevices 接口查询当前已连接的机械体设备列表，验证设备是否正确识别。
2. **目标拍摄跟踪**：调用 setCameraTrackingEnabled 启用摄像头目标跟踪功能，使用 getCameraTrackingEnabled 验证状态，测试设备是否能跟随目标自动旋转。

**验证结果说明**

* 如果 getAttachedMechDevices 返回设备列表，表示设备识别成功。
* 如果 getCameraTrackingEnabled 返回真，目标拍摄跟踪启用成功。应用打开相机后，画面中出现人脸时，设备会跟随人脸转动。
