---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/camera-rotation-angle-adaptation
title: 适配相机旋转角度(ArkTS)
breadcrumb: 指南 > 媒体 > Camera Kit（相机服务） > 开发相机应用基础能力(ArkTS) > 相机旋转 > 适配相机旋转角度(ArkTS)
category: harmonyos-guides
scraped_at: 2026-04-28T07:46:03+08:00
doc_updated_at: 2026-04-10
content_hash: sha256:76c2a309b582ebce7efac90c7de2a4196584d9c284398f77bcf5bbc72340504e
---

屏幕处于不同的屏幕状态时，原始图像需旋转不同的角度，以确保图像在合适的方向显示，效果如图所示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2c/v3/eaR2zP8SRsqG1gY4oMa5Rw/zh-cn_image_0000002583438617.png?HW-CC-KV=V1&HW-CC-Date=20260427T234601Z&HW-CC-Expire=86400&HW-CC-Sign=AB282118F9E9CF5F56FFE6236637941FAA989EC19729D215F4A62F6436AD6A8D)

本开发指导将指导开发者在预览、拍照、录像等不同场景下，如何适配相机的旋转角度。

* 在预览时，图像旋转角度与屏幕显示旋转角度（[Display](../harmonyos-references/js-apis-display.md#属性).rotation）相关。具体开发指导：[创建会话](camera-rotation-angle-adaptation.md#创建会话) > [预览](camera-rotation-angle-adaptation.md#预览)。
* 在拍照、录像时，图像旋转角度与设备重力方向（即[设备旋转角度](camera-rotation-angle-adaptation.md#计算设备旋转角度)）相关。

  拍照开发指导：[创建会话](camera-rotation-angle-adaptation.md#创建会话) > [计算设备旋转角度](camera-rotation-angle-adaptation.md#计算设备旋转角度) > [拍照](camera-rotation-angle-adaptation.md#拍照)。

  录像开发指导：[创建会话](camera-rotation-angle-adaptation.md#创建会话) > [计算设备旋转角度](camera-rotation-angle-adaptation.md#计算设备旋转角度) > [录像](camera-rotation-angle-adaptation.md#录像)。

详细的API参考说明，请参考[Camera API文档](../harmonyos-references/js-apis-camera.md)。

## 创建会话

1. 导入相机等相关模块。

   ```
   1. import { camera } from '@kit.CameraKit';
   2. import { BusinessError } from '@kit.BasicServicesKit';
   ```
2. 创建[Session](../harmonyos-references/arkts-apis-camera-session.md)会话。

   相机使用预览等功能前，均需创建相机会话，调用[CameraManager](../harmonyos-references/arkts-apis-camera-cameramanager.md)中的[createSession](../harmonyos-references/arkts-apis-camera-cameramanager.md#createsession11)方法创建一个会话，创建会话时需指定创建[SceneMode](../harmonyos-references/arkts-apis-camera-e.md#scenemode11)为NORMAL\_PHOTO或NORMAL\_VIDEO，创建的session处于拍照或者录像模式。

   ```
   1. function createPhotoSession(cameraManager: camera.CameraManager): camera.Session | undefined {
   2. let session: camera.Session | undefined = undefined;
   3. try {
   4. session = cameraManager.createSession(camera.SceneMode.NORMAL_PHOTO) as camera.PhotoSession;
   5. } catch (error) {
   6. let err = error as BusinessError;
   7. console.error(`Failed to create the session instance. error: ${err}`);
   8. }
   9. return session;
   10. }

   12. function createVideoSession(cameraManager: camera.CameraManager): camera.Session | undefined {
   13. let session: camera.Session | undefined = undefined;
   14. try {
   15. session = cameraManager.createSession(camera.SceneMode.NORMAL_VIDEO) as camera.VideoSession;
   16. } catch (error) {
   17. let err = error as BusinessError;
   18. console.error(`Failed to create the session instance. error: ${err}`);
   19. }
   20. return session;
   21. }
   ```

## 预览

完成[会话创建](camera-rotation-angle-adaptation.md#创建会话)后，开发者可根据实际需求，配置输出流。

1. 调用[PreviewOutput](../harmonyos-references/arkts-apis-camera-previewoutput.md)中的[getPreviewRotation](../harmonyos-references/arkts-apis-camera-previewoutput.md#getpreviewrotation12)接口，获取[预览旋转角度](camera-rotation-term.md#预览旋转角度)。

   displayRotation：[显示设备的屏幕旋转角度](camera-rotation-term.md#屏幕旋转角度)，可通过[display.getDefaultDisplaySync](../harmonyos-references/js-apis-display.md#displaygetdefaultdisplaysync9)获取[Display](../harmonyos-references/js-apis-display.md#属性)对象并读取其rotation属性值，并将对应角度填入。

   例：Display.rotation = 1，表示显示设备屏幕顺时针旋转为90°，此处displayRotation填入90。

   ```
   1. import { display } from '@kit.ArkUI';

   3. let initDisplayRotation = display.getDefaultDisplaySync().rotation;
   4. let imageRotation = initDisplayRotation * camera.ImageRotation.ROTATION_90;
   ```

   该接口需要在session调用[commitConfig](../harmonyos-references/arkts-apis-camera-session.md#commitconfig11)完成配流后调用，如果存在异步执行的情况，previewOutput未添加到session里或者已调用的session.release，导致两者关系未绑定，此时调用getPreviewRotation，则会调用失败，并抛出错误码[CameraErrorCode.SERVICE\_FATAL\_ERROR](../harmonyos-references/errorcode-camera.md#section7400201-相机服务异常)。

   ```
   1. function getPreviewRotation(previewOutput: camera.PreviewOutput, imageRotation : camera.ImageRotation): camera.ImageRotation {
   2. let previewRotation: camera.ImageRotation = camera.ImageRotation.ROTATION_0;
   3. try {
   4. previewRotation = previewOutput.getPreviewRotation(imageRotation);
   5. console.info(`Preview rotation is: ${previewRotation}`);
   6. } catch (error) {
   7. // 失败返回错误码error.code并处理
   8. let err = error as BusinessError;
   9. console.error(`The previewOutput.getPreviewRotation call failed. error code: ${err.code}`);
   10. }
   11. return previewRotation;
   12. }
   ```
2. 调用[PreviewOutput](../harmonyos-references/arkts-apis-camera-previewoutput.md)中的[setPreviewRotation](../harmonyos-references/arkts-apis-camera-previewoutput.md#setpreviewrotation12)，设置图像的预览旋转角度。

   该接口需要在session调用[commitConfig](../harmonyos-references/arkts-apis-camera-session.md#commitconfig11)完成配流后调用，如果多次调用，以最新调用设置的图像预览旋转角度为准。

   * previewRotation：预览旋转角度，取上一步[getPreviewRotation](../harmonyos-references/arkts-apis-camera-previewoutput.md#getpreviewrotation12)的返回值。
   * isDisplayLocked：可选入参，默认为false。当设置为false，即屏幕方向未锁定，[预览旋转角度](camera-rotation-term.md#预览旋转角度)将根据[相机镜头角度](camera-rotation-term.md#相机镜头安装角度)+[屏幕显示旋转角度](camera-rotation-term.md#屏幕旋转角度)的值计算；当设置为true，Surface旋转锁定，不跟随窗口变化，旋转角度仅取相机镜头角度计算。

   ```
   1. function setPreviewRotation(previewOutput: camera.PreviewOutput, previewRotation : camera.ImageRotation, isDisplayLocked: boolean): void {
   2. try {
   3. previewOutput.setPreviewRotation(previewRotation, isDisplayLocked);
   4. } catch (error) {
   5. // 失败返回错误码error.code并处理
   6. let err = error as BusinessError;
   7. console.error(`The previewOutput.setPreviewRotation call failed. error code: ${err.code}`);
   8. }
   9. }
   ```

**预览流旋转接口适配场景及示例：**

1. 在[会话配置](camera-session-management.md)过程中调用预览旋转接口，即：使用[commitConfig](../harmonyos-references/arkts-apis-camera-session.md#commitconfig11)接口提交相关配置后调用，建议在[Start](../harmonyos-references/arkts-apis-camera-session.md#start11)起流前调用。

   ```
   1. // previewOutput是创建的预览输出
   2. try {
   3. let initDisplayRotation = display.getDefaultDisplaySync().rotation;
   4. let initPreviewRotation = previewOutput.getPreviewRotation(initDisplayRotation * camera.ImageRotation.ROTATION_90);
   5. previewOutput.setPreviewRotation(initPreviewRotation, false);
   6. } catch (error) {
   7. // 失败返回错误码error.code并处理
   8. let err = error as BusinessError;
   9. console.error(`PreviewRotation call failed. error code: ${err.code}`);
   10. }
   ```
2. 应用使用相机时，通过监听[Display对象变化](../harmonyos-references/js-apis-display.md#displayonaddremovechange)，感知窗口当前状态，如当前相机窗口发生旋转时，需对预览流进行角度修正。推荐在[会话配置](camera-session-management.md)中完成调用预览旋转接口后，直接创建监听。

   ```
   1. import { display } from '@kit.ArkUI';

   3. // previewOutput是创建的预览输出
   4. display.off('change');
   5. display.on('change', () => {
   6. try {
   7. let displayRotation = display.getDefaultDisplaySync().rotation;
   8. let imageRotation = displayRotation * camera.ImageRotation.ROTATION_90;
   9. let previewRotation = previewOutput.getPreviewRotation(imageRotation);
   10. previewOutput.setPreviewRotation(previewRotation, false);
   11. } catch (error) {
   12. // 失败返回错误码error.code并处理
   13. let err = error as BusinessError;
   14. console.error(`display change PreviewRotation call failed. error code: ${err.code}`);
   15. }
   16. });
   ```

## 拍照

完成[会话创建](camera-rotation-angle-adaptation.md#创建会话)后，开发者可根据实际需求，配置输出流。

1. 调用[PhotoOutput](../harmonyos-references/arkts-apis-camera-photooutput.md)中的[getPhotoRotation](../harmonyos-references/arkts-apis-camera-photooutput.md#getphotorotation12)可以获取到拍照旋转角度。

   该接口需要在session调用[commitConfig](../harmonyos-references/arkts-apis-camera-session.md#commitconfig11)完成配流后调用。

   deviceDegree：设备旋转角度。拍照的旋转角度与重力方向（即设备旋转角度）相关，获取方式请见[计算设备旋转角度](camera-rotation-angle-adaptation.md#计算设备旋转角度)。

   ```
   1. function getPhotoRotation(photoOutput: camera.PhotoOutput, deviceDegree: number): camera.ImageRotation {
   2. let photoRotation: camera.ImageRotation = camera.ImageRotation.ROTATION_0;
   3. try {
   4. photoRotation = photoOutput.getPhotoRotation(deviceDegree);
   5. console.info(`Photo rotation is: ${photoRotation}`);
   6. } catch (error) {
   7. // 失败返回错误码error.code并处理
   8. let err = error as BusinessError;
   9. console.error(`The photoOutput.getPhotoRotation call failed. error code: ${err.code}`);
   10. }
   11. return photoRotation;
   12. }
   ```
2. 应用将拍照角度写入[PhotoCaptureSetting](../harmonyos-references/arkts-apis-camera-i.md#photocapturesetting).rotation。
3. 其余参数的配置及拍照，可参考[拍照开发指导](camera-shooting.md)。

## 录像

完成[会话创建](camera-rotation-angle-adaptation.md#创建会话)后，开发者可根据实际需求，配置输出流。

1. 调用[VideoOutput](../harmonyos-references/arkts-apis-camera-videooutput.md)中的[getVideoRotation](../harmonyos-references/arkts-apis-camera-videooutput.md#getvideorotation12)可以获取到录像的旋转角度。

   该接口需要在session调用[commitConfig](../harmonyos-references/arkts-apis-camera-session.md#commitconfig11)完成配流后调用。

   deviceDegree：设备旋转角度。录像的旋转角度与重力方向（即设备旋转角度）相关，获取方式请见[计算设备旋转角度](camera-rotation-angle-adaptation.md#计算设备旋转角度)。

   ```
   1. function getVideoRotation(videoOutput: camera.VideoOutput, deviceDegree: number): camera.ImageRotation {
   2. let videoRotation: camera.ImageRotation = camera.ImageRotation.ROTATION_0;
   3. try {
   4. videoRotation = videoOutput.getVideoRotation(deviceDegree);
   5. console.info(`Video rotation is: ${videoRotation}`);
   6. } catch (error) {
   7. // 失败返回错误码error.code并处理
   8. let err = error as BusinessError;
   9. console.error(`The videoOutput.getVideoRotation call failed. error code: ${err.code}`);
   10. }
   11. return videoRotation;
   12. }
   ```
2. 在[AVRecorder.prepare](../harmonyos-references/arkts-apis-media-avrecorder.md#prepare9)后使用[updateRotation](../harmonyos-references/arkts-apis-media-avrecorder.md#updaterotation12)设置录像角度。
3. 其余参数的配置及启动录像，可参考[录像开发指导](camera-recording.md)。

**录像流旋转接口适配示例代码：**

```
1. import { camera } from '@kit.CameraKit';
2. import { media } from '@kit.MediaKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. async function getVideoRotationAndUpdate(videoOutput: camera.VideoOutput, deviceDegree: number, avRecorder: media.AVRecorder) {
6. let videoRotation: camera.ImageRotation = camera.ImageRotation.ROTATION_0;
7. try {
8. videoRotation = videoOutput.getVideoRotation(deviceDegree);
9. console.info(`Video rotation is: ${videoRotation}`);
10. if (avRecorder.state === 'prepared') {
11. await avRecorder.updateRotation(videoRotation);
12. }
13. } catch (error) {
14. // 失败返回错误码error.code并处理
15. let err = error as BusinessError;
16. console.error(`getVideoRotationAndUpdate call failed. error code: ${err.code}`);
17. }
18. }
```

## 计算设备旋转角度

当前可通过调用[once(type: SensorId.GRAVITY, callback: Callback<GravityResponse>)](../harmonyos-references/js-apis-sensor.md#gravity9-1)获取一次重力传感器在x、y、z三个方向上的数据，计算得出设备旋转角度deviceDegree，示例如下所示。

如果无法获得重力传感器数据，需要申请重力传感器权限ohos.permission.ACCELEROMETER。权限申请请参考[声明权限](declare-permissions.md)，如何获取传感器数据请参考[传感器开发指导](sensor-guidelines.md)。

```
1. import { Decimal } from '@kit.ArkTS';
2. import { sensor } from '@kit.SensorServiceKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. let isSupported: boolean = false;
6. let getDeviceDegree: number = -1;
7. function getRealData(data: sensor.GravityResponse): number {
8. let getDeviceDegree: number = 0;
9. let x = data.x;
10. let y = data.y;
11. let z = data.z;
12. if ((x * x + y * y) * 3 < z * z) {
13. return getDeviceDegree;
14. } else {
15. try {
16. let sd: Decimal = Decimal.atan2(y, -x);
17. let sc: Decimal = Decimal.round(Number(sd) / 3.141592653589 * 180);
18. getDeviceDegree = 90 - Number(sc);
19. getDeviceDegree = getDeviceDegree >= 0 ? getDeviceDegree % 360 : getDeviceDegree % 360 + 360;
20. } catch (error) {
21. let err = error as BusinessError;
22. console.error(`decimal failed, error: ${err.code}`);
23. }
24. }
25. return getDeviceDegree;
26. }

28. async function getGravity() : Promise<number> {
29. let data: sensor.Sensor[];
30. try {
31. data = await sensor.getSensorList();
32. } catch (error) {
33. let err = error as BusinessError;
34. console.error(`getSensorList failed, error: ${err.code}`);
35. return -1; // 异常场景下返回默认值
36. }

38. for (let i = 0; i < data.length; i++) {
39. if (data[i].sensorId === sensor.SensorId.GRAVITY) {
40. isSupported = true;
41. break;
42. }
43. }
44. try {
45. if (isSupported === true) {
46. const promise: Promise<number> = new Promise((resolve) => {
47. sensor.once(sensor.SensorId.GRAVITY, (data: sensor.GravityResponse) => {
48. resolve(getRealData(data));
49. });
50. })
51. return promise;
52. } else {
53. const promise: Promise<number> = new Promise((resolve) => {
54. sensor.once(sensor.SensorId.ACCELEROMETER, (data: sensor.AccelerometerResponse) => {
55. resolve(getRealData(data as sensor.GravityResponse));
56. });
57. })
58. return promise;
59. }
60. } catch (error) {
61. let err = error as BusinessError;
62. console.error(`gePromise failed, error: ${err.code}`);
63. return -1; // 异常场景下返回默认值
64. }
65. }

67. // 获取当前设备旋转角度
68. async function getCurrentDeviceDegree() : Promise<number> {
69. getDeviceDegree = await getGravity(); // 调用使用await
70. return getDeviceDegree;
71. }
```

## 视频通话送远端场景

两个设备之间进行视频通话，存在设备间持握方向不一致问题，建议**在本端将画面转正**，再通过网络发送到对端，画面转正参考[自绘制场景预览角度的归一化处理](camera-rotation-angle-adaptation.md#自绘制场景预览角度的归一化处理)。

## 实现相机无损出图

在部分折叠屏设备上，[不同折叠状态](../best-practices/bpta-foldable-guide.md#section152264061715)下的[设备自然方向](camera-rotation-term.md#设备自然方向)会发生改变，导致不同折叠状态下真实的[相机镜头安装角度](camera-rotation-term.md#相机镜头安装角度)不同。为了屏蔽不同设备间的差异，使得不同折叠状态下的相机镜头安装角度一致，系统会自动调整部分折叠状态下的相机采集图像方向（通过旋转裁切的方式）和相机镜头安装角度，因此会存在视场角（Field of View, FOV）损失，可能会导致相机预览、拍照、录像可见范围降低，因此如果需要实现相机无损出图，可以通过[usePhysicalCameraOrientation](../harmonyos-references/arkts-apis-camera-camerainput.md#usephysicalcameraorientation22)接口来实现相机无损出图。具体方式如下：

设备是否支持无损出图，首先需要确认设备的相机镜头安装角度是否可变，可以通过[isPhysicalCameraOrientationVariable](../harmonyos-references/arkts-apis-camera-camerainput.md#isphysicalcameraorientationvariable22)接口查询。

1. 当相机镜头安装角度不可变时，不同折叠状态下的相机出图均为无损出图。
2. 当相机镜头安装角度可变时：

   * 如应用需要实现相机无损出图，由于相机镜头安装角度与相机旋转相关，需要应用完成[相机旋转的适配](camera-rotation-angle-adaptation.md#top)后，通过[getPhysicalCameraOrientation](../harmonyos-references/arkts-apis-camera-camerainput.md#getphysicalcameraorientation22)接口获取设备当前折叠状态下真实的相机镜头安装角度，并通过[usePhysicalCameraOrientation](../harmonyos-references/arkts-apis-camera-camerainput.md#usephysicalcameraorientation22)接口实现相机无损出图（相机镜头安装角度不可变时使用[usePhysicalCameraOrientation](../harmonyos-references/arkts-apis-camera-camerainput.md#usephysicalcameraorientation22)将会返回[7400102](../harmonyos-references/errorcode-camera.md#section7400102-非法操作)错误码，未适配相机旋转时使用相机无损出图会导致预览、拍照、录像旋转异常），推荐在[createCameraInput](../harmonyos-references/arkts-apis-camera-cameramanager.md#createcamerainput)后直接使用[usePhysicalCameraOrientation](../harmonyos-references/arkts-apis-camera-camerainput.md#usephysicalcameraorientation22)接口实现相机无损出图。

示例代码如下：

```
1. import { camera } from '@kit.CameraKit';

3. function enablePhysicalCameraOrientation(cameraInput: camera.CameraInput) {
4. // 查询设备的相机镜头安装角度是否可变
5. let isVarialbe: boolean = cameraInput.isPhysicalCameraOrientationVariable();

7. if (isVarialbe) {
8. // 获取设备当前折叠状态下真实的相机镜头安装角度
9. let physicalOrientation: number = cameraInput.getPhysicalCameraOrientation();
10. console.info(`physical Orientation is ${physicalOrientation}`);

12. // 选择是否使用真实的相机镜头安装角度, 以实现无损出图
13. let isUsed: boolean = true;
14. cameraInput.usePhysicalCameraOrientation(isUsed);
15. }
16. }
```

## 常见问题

### 指定XComponent的大小，防止旋转后图像拉伸变形

图像显示出现拉伸或压缩等变形，是因为图像分辨率与[XComponent](../harmonyos-references/ts-basic-components-xcomponent.md)的宽高比不匹配。以应用层下发的1920\*1080(16:9)竖屏和横屏为例，器件出图均是按照4:3比例出一张RAW图，在此基础上，根据应用层下发的16:9比例进行裁切，提供数据给应用层。因此，无论手机持握方向如何变化，应用层接收的数据始终是16:9比例的图片。具体图示如下：

| 设备和镜头方向 | 处理过程示意图 | XComponent布局 |
| --- | --- | --- |
| **设备条件：**  手机竖屏、充电口向下。  使用后置相机拍摄。  **可得：**  - 后置相机镜头角度 = 90°  - 屏幕旋转角度 = 0°，[Display.rotation](../harmonyos-references/js-apis-display.md#属性) = 0  - **图像预览旋转角度 = 0°+90° = 90°** |  | 出图与最终成像有90度夹角，布局宽高与图像宽高交换。 |
| **设备条件：**  手机横屏、充电口向右。  使用后置相机拍摄。  **可得：**  - 后置相机镜头角度 = 90°  - 屏幕旋转角度 = 270°，[Display.rotation](../harmonyos-references/js-apis-display.md#属性) = 3  - **图像预览旋转角度 = 270°+90° = 360° = 0°** |  | 出图与最终成像有0度夹角，布局与图像宽高比一致。 |

从上图可以看出，当手机从竖屏转换为横屏时，图像始终保持16:9的输出比例，但镜头与屏幕显示方向之间的夹角从90度变为0度。如果布局保持9:16不变，那么16:9的图像数据放置在9:16的空间内显示，会导致图像形变。因此，为确保图像显示正常，横屏时需要将布局的宽高比调整为16:9。

首先，将XComponent的宽度和高度作为状态变量进行监听，通过[Window.on('windowSizeChange')](../harmonyos-references/arkts-apis-window-window.md#onwindowsizechange7)监听窗口的变化，根据屏幕旋转角度（[Display.rotation](../harmonyos-references/js-apis-display.md#属性) ）与相机镜头角度（[CameraDevice.cameraOrientation](../harmonyos-references/js-apis-display.md#orientation10)）之间的角度来确定布局的宽高比，以确保布局能跟随窗口实时调整。

具体的实现方法如下，在需要进行横竖屏切换的页面中，通常建议在aboutToAppear中执行窗口变化的监听。

```
1. import { bundleManager } from '@kit.AbilityKit';
2. import { display } from '@kit.ArkUI';
3. import { common } from '@kit.AbilityKit';
4. import { BusinessError, deviceInfo  } from '@kit.BasicServicesKit';

6. // ....
7. let previewOutput : camera.PreviewOutput; // 根据具体使用场景创建的预览输出流
8. let cameraDevice : camera.CameraDevice; // 根据使用诉求选择符合的相机设备
9. @Entry
10. @Component
11. struct Index {
12. @State mXComponentWidth: number = 1280;
13. @State mXComponentHeight: number = 720;
14. @State mRotate: number = 0;
15. @State mConfigRatio: number = 16 / 9;
16. private targetVersion: number = 0;
17. private mWindowHeight = 0;
18. private mWindowWidth = 0;

20. private windowClass = (this.getUIContext().getHostContext() as common.UIAbilityContext).windowStage.getMainWindowSync();
21. getBundleInfoForSelf() { // 获取应用的编译版本
22. let bundleFlags = bundleManager.BundleFlag.GET_BUNDLE_INFO_WITH_APPLICATION | bundleManager.BundleFlag.GET_BUNDLE_INFO_WITH_METADATA;
23. try {
24. bundleManager.getBundleInfoForSelf(bundleFlags).then((data) => {
25. console.info(`getBundleInfoForSelf successfully. Data: ${data.targetVersion}`);
26. this.targetVersion = data.targetVersion;
27. }).catch((err: BusinessError) => {
28. console.error(`getBundleInfoForSelf failed ${err}`);
29. });
30. } catch (err) {
31. let message = (err as BusinessError).message;
32. console.error(`getBundleInfoForSelf failed ${message}`);
33. }
34. }

36. isIsolateForSpecialType(): boolean { // 兼容平板API14之前的设备
37. return deviceInfo.deviceType == "tablet" && this.targetVersion <= 50000013;
38. }

40. aboutToAppear(): void {
41. this.updateXComponentSize();
42. this.getBundleInfoForSelf();
43. this.windowClass.on('windowSizeChange', (size) => {
44. this.mWindowWidth = size.width;
45. this.mWindowHeight = size.height;
46. this.updateXComponentSize();
47. });
48. let rotation : number = 0;
49. try {
50. rotation = display.getDefaultDisplaySync().rotation;
51. this.mRotate = rotation * camera.ImageRotation.ROTATION_90;
52. } catch (error) {
53. const err = error as BusinessError;
54. console.error(`Failed to get display rotation: ${err.code}, ${err.message}`);
55. this.mRotate = 0;
56. }
57. display.on('change', () => {
58. if (this.mRotate!= rotation * camera.ImageRotation.ROTATION_90) {
59. this.mRotate= rotation * camera.ImageRotation.ROTATION_90; // 获取屏幕旋转角度
60. this.updateXComponentSize();
61. let imageRotation = this.getImageRotation();
62. if (!imageRotation) {
63. console.error(`current get image rotation is undefined`);
64. return;
65. }
66. let previewRotation = previewOutput.getPreviewRotation(imageRotation); // previewOutput是创建的预览流
67. previewOutput.setPreviewRotation(previewRotation, false);
68. }
69. });
70. }
71. getImageRotation() : camera.ImageRotation | undefined {
72. let displayRotation : number= 0;
73. try {
74. displayRotation = display.getDefaultDisplaySync().rotation
75. } catch (error) {
76. const err = error as BusinessError;
77. console.error(`Failed to get display rotation: ${err.code}, ${err.message}`);
78. return undefined;
79. }
80. let imageRotation = displayRotation * camera.ImageRotation.ROTATION_90;
81. return imageRotation;
82. }
83. updateXComponentSize(): void {
84. let angleDiff = (this.mRotate+ cameraDevice?.cameraOrientation) % 360;
85. if (this.isIsolateForSpecialType()) { // 如果设备为平板设备，且使用的API版本＜14，应进入此逻辑。
86. if (angleDiff === 90 || angleDiff=== 270) {
87. this.mXComponentWidth = this.mConfigRatio * this.mWindowHeight;
88. this.mXComponentHeight = this.mWindowHeight;
89. } else {
90. this.mXComponentWidth = this.mWindowWidth;
91. this.mXComponentHeight = this.mConfigRatio * this.mWindowWidth; // 1920 *1080
92. }
93. } else { // 如果使用API版本≥14，或是API14以下的非平板设备，应进入此逻辑。
94. if (angleDiff === 90 || angleDiff=== 270) {
95. this.mXComponentWidth = this.mWindowWidth;
96. this.mXComponentHeight = this.mConfigRatio * this.mWindowWidth; // 1920 *1080
97. } else {
98. this.mXComponentWidth = this.mConfigRatio * this.mWindowHeight;
99. this.mXComponentHeight = this.mWindowHeight;
100. }
101. }
102. }

104. async aboutToDisAppear(): Promise<void> {
105. display.off('change');
106. this.windowClass.off('windowSizeChange');
107. // 解注册
108. }
109. build() {
110. // 根据使用诉求补充界面处理逻辑。
111. }
112. }
```

除了指定XComponent的宽高外，还可以通过设置XComponent的renderFit来实现图片的自适应大小显示、居中裁剪显示等效果。具体详情请参考[RenderFit介绍](../harmonyos-references/ts-universal-attributes-renderfit.md#renderfit)。

### 自绘制场景预览角度的归一化处理

在自绘制场景中，对于后置摄像头，可以通过调用[getPreviewRotation](../harmonyos-references/arkts-apis-camera-previewoutput.md#getpreviewrotation12)获取旋转角度，将图像转正；对于前置摄像头，由于存在水平镜像和垂直镜像的差异，为了简化操作，需先对前置摄像头的图像角度进行归一化处理后，再将图像转正，并根据业务需求决定是否进行镜像处理。

pixelMap处理方式：

```
1. import { camera } from '@kit.CameraKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { image } from '@kit.ImageKit';
4. import { display } from '@kit.ArkUI';

6. let previewOutputReceiver: camera.PreviewOutput | undefined = undefined; // 回调流定义
7. let curCameraPosition = camera.CameraPosition.CAMERA_POSITION_FRONT; // 相机设备的位置定义，此处以前置为例。
8. // .....
9. function  onImageArrival(receiver: image.ImageReceiver): void {
10. receiver.on('imageArrival', () => { // imageRecevier回调
11. // 获取图像
12. receiver.readNextImage((err: BusinessError, nextImage: image.Image) => {
13. if (err || nextImage === undefined) {
14. console.error('readNextImage failed');
15. return;
16. }
17. // 解析图像内容
18. nextImage.getComponent(image.ComponentType.JPEG, async (err: BusinessError, imgComponent: image.Component) => {
19. if (err || imgComponent === undefined) {
20. console.error('getComponent failed');
21. }

23. if (imgComponent.byteBuffer) {
24. let width = nextImage.size.width; // 获取图片的宽
25. let height = nextImage.size.height; // 获取图片的高
26. let stride = imgComponent.rowStride; // 获取图片的stride
27. // stride与width一致
28. if (stride == width) {
29. let pixelMap = await image.createPixelMap(imgComponent.byteBuffer, {
30. size: { height: height, width: width },
31. srcPixelFormat: image.PixelMapFormat.NV21, // 此处以NV21为例
32. })
33. updatePixelMap(pixelMap);
34. } else {
35. // stride与width不一致
36. const dstBufferSize = width * height * 1.5 // 以NV21为例（YUV_420_SP格式的图片）YUV_420_SP内存计算公式：长x宽+(长x宽)/2
37. const dstArr = new Uint8Array(dstBufferSize)
38. for (let j = 0; j < height * 1.5; j++) {
39. const srcBuf = new Uint8Array(imgComponent.byteBuffer, j * stride, width)
40. dstArr.set(srcBuf, j * width)
41. }
42. let pixelMap = await image.createPixelMap(dstArr.buffer, {
43. size: { height: height, width: width },
44. srcPixelFormat: image.PixelMapFormat.NV21, // 此处以NV21为例
45. });
46. updatePixelMap(pixelMap);
47. }
48. } else {
49. console.error('byteBuffer is null');
50. }
51. // 确保当前buffer没有在使用的情况下，可进行资源释放。
52. // 如果对buffer进行异步操作，需要在异步操作结束后再释放该资源（nextImage.release()）。
53. nextImage.release();
54. console.info('image process done');
55. })
56. })
57. })
58. }
```

```
1. async function  updatePixelMap(pixelMap: image.PixelMap): Promise<void> {
2. let rotation : number = 0;
3. try {
4. rotation = display.getDefaultDisplaySync().rotation * camera.ImageRotation.ROTATION_90;
5. } catch (error) {
6. const err = error as BusinessError;
7. console.error(`Failed to get display rotation: ${err.code}, ${err.message}`);
8. return;
9. }
10. let angle = previewOutputReceiver?.getPreviewRotation(rotation);
11. if (angle === undefined) {
12. return;
13. }
14. // 在display.on中对该previewOutput设置过setPreviewRotation，此处可以不执行。
15. previewOutputReceiver?.setPreviewRotation(angle);
16. if (curCameraPosition === camera.CameraPosition.CAMERA_POSITION_FRONT) {
17. if (rotation ===90 || rotation === 270) {
18. angle = (angle + 180 ) % 360;
19. }
20. await pixelMap.rotate(angle);
21. await pixelMap.flip(true, false);
22. } else {
23. await pixelMap.rotate(angle);
24. }
25. }
```

### 适配一多设备

为了适配一多设备，主要分为以下几步：

1. 根据屏幕比例选择合适的预览分辨率。
2. 根据确定的预览分辨率，通过宽/高得到新的比例。
3. 根据上一步的比例计算XComponent宽高，可参考[指定XComponent的大小，防止旋转后图像拉伸变形](camera-rotation-angle-adaptation.md#指定xcomponent的大小防止旋转后图像拉伸变形)，将mConfigRatio应用于布局宽高的计算。

   说明

   在适配折叠屏设备时，每次折叠屏镜头变化都需要重新获取屏幕比例。

```
1. let mConfigRatio: number = 16 / 9; // 设置分辨率比例初始值，此处以16:9宽高比为例。
2. let reConfigType : number = 720;
3. let previewProfileObj: camera.Profile = {
4. format: 1003,
5. size: {
6. width: 1280,
7. height: 720
8. }
9. };
10. // 根据屏幕初步计算比例，长边/短边
11. function getConfigRation(cameraDevice: camera.CameraDevice, cameraManager: camera.CameraManager) : number {
12. let previewProfile = getSurfaceSize(cameraDevice, mConfigRatio, cameraManager); // 获取最接近的分辨率
13. if (previewProfile === undefined || previewProfile.size === undefined) {
14. return 0;
15. }
16. mConfigRatio = previewProfile.size.width / previewProfile.size.height; // 以新的比例重新计算显示宽高
17. return mConfigRatio;
18. }

20. // 获取最接近屏幕的分辨率
21. function getSurfaceSize(cameraDevice: camera.CameraDevice, configRatio: number, cameraManager: camera.CameraManager): camera.Profile | undefined {
22. console.info(`previewProfiles is ${configRatio}`);
23. let cameraOutputCapability =
24. cameraManager.getSupportedOutputCapability(cameraDevice, camera.SceneMode.NORMAL_PHOTO); // 此处以NORMAL_PHOTO为例
25. return getPreviewProfile(cameraOutputCapability, configRatio);
26. }
27. function getPreviewProfile(cameraOutputCapability: camera.CameraOutputCapability, configRatio: number): camera.Profile | undefined {
28. let previewProfiles = cameraOutputCapability.previewProfiles;
29. if (previewProfiles.length < 1) {
30. return undefined;
31. }
32. console.info(`previewProfiles this.foramt: ${previewProfileObj.format} configRatio = ${configRatio}`);
33. let optimalSize: camera.Profile|undefined;
34. let minDiff = Number.MAX_VALUE;
35. // 计算屏幕的宽高比
36. for (let i = 0; i < previewProfiles.length; i++) {
37. if (previewProfiles[i].format !== previewProfileObj.format) {
38. continue;
39. }
40. let ratio = previewProfiles[i].size.width / previewProfiles[i].size.height; // 1088*1080
41. // 检查宽高比是否匹配
42. if (Math.abs(ratio - configRatio) > 0.2) continue; // 0.2的误差可自行调整
43. // 选择最接近的分辨率
44. if (Math.abs(previewProfiles[i].size.height - reConfigType) < minDiff) {
45. optimalSize = previewProfiles[i];
46. minDiff = Math.abs(previewProfiles[i].size.height - reConfigType);
47. }
48. }

50. // 如果没有找到合适的分辨率，选择第一个
51. if (optimalSize === undefined) {
52. minDiff = Number.MAX_VALUE;
53. for (let i = 0; i < previewProfiles.length; i++) {
54. if (previewProfiles[i].format !== previewProfileObj.format) {
55. continue;
56. }
57. if (Math.abs(previewProfiles[i].size.height - reConfigType) < minDiff) { // 720
58. optimalSize = previewProfiles[i];
59. minDiff = Math.abs(previewProfiles[i].size.height - reConfigType);
60. }
61. }
62. }
63. return optimalSize;
64. }
```

### 拍照无法镜像

通过设置[PhotoCaptureSetting](../harmonyos-references/arkts-apis-camera-i.md#photocapturesetting)中的mirror属性改变拍照镜像。

```
1. // this.photoOutput是拍照输出output, this.getDeviceDegree是重力角度
2. let photoSettings: camera.PhotoCaptureSetting = {
3. quality: camera.QualityLevel.QUALITY_LEVEL_HIGH,
4. mirror: this.photoOutput?.isMirrorSupported() // 设置拍照镜像，true表示镜像，false表示非镜像
5. };
6. // ... 省略获取代码
7. this.photoRotation = getPhotoRotation(this.photoOutput!!,this.getDeviceDegree)
8. photoSettings.rotation = this.photoRotation // 指定拍照旋转角度
```
