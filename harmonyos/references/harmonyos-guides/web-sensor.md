---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/web-sensor
title: 使用运动和方向传感器监测设备状态
breadcrumb: 指南 > 应用框架 > ArkWeb（方舟Web） > 设置基本属性和事件 > 使用运动和方向传感器监测设备状态
category: harmonyos-guides
scraped_at: 2026-04-28T07:40:52+08:00
doc_updated_at: 2026-04-02
content_hash: sha256:41df9069e384116fb52943fbb576c2c258fad8b327712ff10896fcca8a000b18
---

## 概述

运动和方向传感器，如加速度计、陀螺仪等，能够监测设备的运动状态和方向变化，例如设备的旋转、倾斜等。

通过W3C标准协议接口，Web组件能够访问这些传感器的数据，进而实现更加丰富的用户交互功能。例如，开发者在网页应用中可以利用加速度计识别运动模式，指导用户进行健身运动，利用陀螺仪捕获玩家手中设备的倾斜和旋转动作，实现无按钮操控的游戏体验。

通过在JavaScript中调用以下支持的W3C标准协议接口，可以访问运动和方向传感器。

| 接口 | 名称 | 说明 |
| --- | --- | --- |
| Accelerometer | 加速度 | 可获取设备X、Y、Z轴方向的加速度数据。 |
| Gyroscope | 陀螺仪 | 可获取设备X、Y、Z轴方向的角速度数据。 |
| AbsoluteOrientationSensor | 绝对定向 | 可获取表示设备绝对定位方向的四元数，包含X、Y、Z和W分量。 |
| RelativeOrientationSensor | 相对定向 | 可获取表示设备相对定位方向的四元数，包含X、Y、Z和W分量。 |
| DeviceMotionEvent | 设备运动事件 | 通过监听该事件，可获取设备在X、Y、Z轴方向上的加速度数据，设备在X、Y、Z轴方向上包含重力的加速度数据，以及设备在alpha、beta、gamma轴方向上旋转的速率数据。 |
| DeviceOrientationEvent | 设备方向事件 | 通过监听该事件，可获取设备绕X、Y、Z轴的角度。 |

## 需要权限

使用加速度、陀螺仪及设备运动事件接口时，需在配置文件module.json5中声明相应的传感器权限。具体配置方法请参考[在配置文件中声明权限](declare-permissions.md#在配置文件中声明权限)。

```
1. "requestPermissions":[
2. {
3. "name" : "ohos.permission.ACCELEROMETER" // 加速度权限
4. },
5. {
6. "name" : "ohos.permission.GYROSCOPE"     // 陀螺仪权限
7. }
8. ]
```

Web组件在对接运动和方向传感器时，需配置[onPermissionRequest](../harmonyos-references/arkts-basic-components-web-events.md#onpermissionrequest9)接口，通过该接口接收权限请求通知。

## 开发步骤

1. 应用侧代码中，Web组件配置[onPermissionRequest](../harmonyos-references/arkts-basic-components-web-events.md#onpermissionrequest9)接口，可通过[PermissionRequest](../harmonyos-references/arkts-basic-components-web-permissionrequest.md)的[getAccessibleResource](../harmonyos-references/arkts-basic-components-web-permissionrequest.md#getaccessibleresource9)接口获取请求权限的资源类型，当资源类型为TYPE\_SENSOR时，进行传感器授权处理。

   ```
   1. import { UIContext } from '@kit.ArkUI';
   2. import { webview } from '@kit.ArkWeb';
   3. import { abilityAccessCtrl, PermissionRequestResult } from '@kit.AbilityKit';
   4. import { BusinessError } from '@kit.BasicServicesKit';

   6. @Entry
   7. @Component
   8. struct WebComponent {
   9. controller: webview.WebviewController = new webview.WebviewController();
   10. uiContext: UIContext = this.getUIContext();

   12. aboutToAppear() {
   13. // 配置Web开启调试模式
   14. webview.WebviewController.setWebDebuggingAccess(true);
   15. // 访问控制管理, 获取访问控制模块对象。
   16. let atManager = abilityAccessCtrl.createAtManager();
   17. try {
   18. atManager.requestPermissionsFromUser(this.uiContext.getHostContext(), ['ohos.permission.ACCELEROMETER', 'ohos.permission.GYROSCOPE']
   19. , (err: BusinessError, data: PermissionRequestResult) => {
   20. if (err) {
   21. console.error(`requestPermissionsFromUser fail, err->${JSON.stringify(err)}`);
   22. } else {
   23. console.info('data permissions:' + data.permissions);
   24. console.info('data authResults:' + data.authResults);
   25. }
   26. })
   27. } catch (error) {
   28. console.error(`ErrorCode: ${(error as BusinessError).code}, Message: ${(error as BusinessError).message}`);
   29. }
   30. }

   32. build() {
   33. Column() {
   34. Web({ src: $rawfile('index.html'), controller: this.controller })
   35. .onPermissionRequest((event) => {
   36. if (event) {
   37. this.uiContext.showAlertDialog({
   38. title: 'title',
   39. message: 'text',
   40. primaryButton: {
   41. value: 'deny',
   42. action: () => {
   43. event.request.deny();
   44. }
   45. },
   46. secondaryButton: {
   47. value: 'onConfirm',
   48. action: () => {
   49. event.request.grant(event.request.getAccessibleResource());
   50. }
   51. },
   52. autoCancel: false,
   53. cancel: () => {
   54. event.request.deny();
   55. }
   56. })
   57. }
   58. })
   59. }
   60. }
   61. }
   ```
2. 在前端页面代码中，利用JavaScript调用传感器相关的W3C标准协议接口。

   ```
   1. <!DOCTYPE HTML>
   2. <html>
   3. <head>
   4. <meta charset="utf-8" />
   5. <meta name="viewport" content="initial-scale=1.0, maximum-scale=1.0, user-scalable=no" />
   6. <meta name="msapplication-tap-highlight" content="no" />
   7. <meta name="HandheldFriendly" content="true" />
   8. <meta name="MobileOptimized" content="320" />
   9. <title>运动和方向传感器</title>
   10. <style>
   11. body {
   12. font-family: Arial, sans-serif;
   13. }
   14. </style>
   15. <script type="text/javascript">
   16. // 访问设备的加速度计传感器，并获取其数据。
   17. function getAccelerometer() {
   18. var acc = new Accelerometer({frequency: 60});
   19. acc.addEventListener('activate', () => console.info('Ready to measure.'));
   20. acc.addEventListener('error', error => console.info('Error type: ' + error.type + ', error: ' + error.error ));
   21. acc.addEventListener('reading', () => {
   22. console.info(`Accelerometer ${acc.timestamp}, ${acc.x}, ${acc.y}, ${acc.z}.`);
   23. });
   24. acc.start();
   25. }

   27. // 访问设备的陀螺仪传感器，并获取其数据。
   28. function getGyroscope() {
   29. var gyr = new Gyroscope({frequency: 60});
   30. gyr.addEventListener('activate', () => console.info('Ready to measure.'));
   31. gyr.addEventListener('error', error => console.info('Error type: ' + error.type + ', error: ' + error.error ));
   32. gyr.addEventListener('reading', () => {
   33. console.info(`Gyroscope ${gyr.timestamp}, ${gyr.x}, ${gyr.y}, ${gyr.z}.`);
   34. });
   35. gyr.start();
   36. }

   38. // 访问设备的方向传感器，并获取其数据。
   39. function getAbsoluteOrientationSensor() {
   40. var aos = new AbsoluteOrientationSensor({frequency: 60});
   41. aos.addEventListener('activate', () => console.info('Ready to measure.'));
   42. aos.addEventListener('error', error => console.info('Error type: ' + error.type + ', error: ' + error.error ));
   43. aos.addEventListener('reading', () => {
   44. console.info(`AbsoluteOrientationSensor data: ${aos.timestamp}, ${aos.quaternion}`);
   45. });
   46. aos.start();
   47. }

   49. // 监听设备的运动事件，并执行相应的处理逻辑。
   50. function listenDeviceMotionEvent() {
   51. removeDeviceMotionEvent();
   52. if ('DeviceMotionEvent' in window) {
   53. window.addEventListener('devicemotion', handleMotionEvent, false);
   54. } else {
   55. console.info('不支持DeviceMotionEvent');
   56. }
   57. }

   59. // 移除之前添加的设备运动事件监听器。
   60. function removeDeviceMotionEvent() {
   61. if ('DeviceMotionEvent' in window) {
   62. window.removeEventListener('devicemotion', handleMotionEvent, false);
   63. } else {
   64. console.info('不支持DeviceMotionEvent');
   65. }
   66. }

   68. // 处理运动事件。
   69. function handleMotionEvent(event) {
   70. const x = event.accelerationIncludingGravity.x;
   71. const y = event.accelerationIncludingGravity.y;
   72. const z = event.accelerationIncludingGravity.z;
   73. console.info(`DeviceMotionEvent data: ${event.timeStamp}, ${x}, ${y}, ${z}`);
   74. }

   76. // 监听设备方向的变化，并执行相应的处理逻辑。
   77. function listenDeviceOrientationEvent() {
   78. removeDeviceOrientationEvent();
   79. if ('DeviceOrientationEvent' in window) {
   80. window.addEventListener('deviceorientation', handleOrientationEvent, false);
   81. } else {
   82. console.info('不支持DeviceOrientationEvent');
   83. }
   84. }

   86. // 移除之前添加的设备方向事件监听器。
   87. function removeDeviceOrientationEvent() {
   88. if ('DeviceOrientationEvent' in window) {
   89. window.removeEventListener('deviceorientation', handleOrientationEvent, false);
   90. } else {
   91. console.info('不支持DeviceOrientationEvent');
   92. }
   93. }

   95. // 监听设备方向的变化，并执行相应的处理逻辑。
   96. function listenDeviceOrientationEvent2() {
   97. removeDeviceOrientationEvent2();
   98. if ('DeviceOrientationEvent' in window) {
   99. window.addEventListener('deviceorientationabsolute', handleOrientationEvent, false);
   100. } else {
   101. console.info('不支持DeviceOrientationEvent');
   102. }
   103. }

   105. // 移除之前添加的设备方向事件监听器。
   106. function removeDeviceOrientationEvent2() {
   107. if ('DeviceOrientationEvent' in window) {
   108. window.removeEventListener('deviceorientationabsolute', handleOrientationEvent, false);
   109. } else {
   110. console.info('不支持DeviceOrientationEvent');
   111. }
   112. }

   114. // 处理方向事件。
   115. function handleOrientationEvent(event) {
   116. console.info(`DeviceOrientationEvent data: ${event.timeStamp}, ${event.absolute}, ${event.alpha}, ${event.beta}, ${event.gamma}`);
   117. }
   118. </script>
   119. </head>
   120. <body>
   121. <div id="dcontent" class="dcontent">
   122. <h3>运动和方向:</h3>
   123. <ul class="dlist">
   124. <li><button type="button" onclick="getAccelerometer()">加速度</button></li>
   125. <li><button type="button" onclick="getGyroscope()">陀螺仪</button></li>
   126. <li><button type="button" onclick="getAbsoluteOrientationSensor()">设备方向(绝对定位)</button></li>
   127. <li><button type="button" onclick="listenDeviceMotionEvent()">设备运动事件</button></li>
   128. <li><button type="button" onclick="listenDeviceOrientationEvent()">设备方向事件</button></li>
   129. <li><button type="button" onclick="listenDeviceOrientationEvent2()">设备方向事件(绝对定位)</button></li>
   130. </ul>
   131. </div>
   132. </body>
   133. </html>
   ```
