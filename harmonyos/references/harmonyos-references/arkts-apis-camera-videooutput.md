---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-camera-videooutput
title: Interface (VideoOutput)
breadcrumb: API参考 > 媒体 > Camera Kit（相机服务） > ArkTS API > @ohos.multimedia.camera (相机管理) > Interface (VideoOutput)
category: harmonyos-references
scraped_at: 2026-04-28T08:12:40+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:c9e1859c0ea2d8611cd9d3e8c78c22d2eae433446b5555d87b4b103c85738689
---

录像会话中使用的输出信息，继承[CameraOutput](arkts-apis-camera-cameraoutput.md)。

说明

本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { camera } from '@kit.CameraKit';
```

## start

PhonePC/2in1TabletTVWearable

start(callback: AsyncCallback<void>): void

启动录制，通过注册回调函数获取结果。使用callback异步回调。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<void> | 是 | 回调函数。当启动录制成功，err为undefined，否则为错误对象。错误码类型[CameraErrorCode](arkts-apis-camera-e.md#cameraerrorcode)。 |

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](errorcode-camera.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400103 | Session not config. |
| 7400201 | Camera service fatal error. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. function startVideoOutput(videoOutput: camera.VideoOutput): void {
4. videoOutput.start((err: BusinessError) => {
5. if (err.code) {
6. console.error(`Failed to start the video output, error code: ${err.code}.`);
7. return;
8. }
9. console.info('Callback invoked to indicate the video output start success.');
10. });
11. }
```

## start

PhonePC/2in1TabletTVWearable

start(): Promise<void>

启动录制。使用Promise异步回调。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](errorcode-camera.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400103 | Session not config. |
| 7400201 | Camera service fatal error. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. function startVideoOutput(videoOutput: camera.VideoOutput): void {
4. videoOutput.start().then(() => {
5. console.info('Promise returned to indicate that start method execution success.');
6. }).catch((error: BusinessError) => {
7. console.error(`Failed to video output start, error code: ${error.code}.`);
8. });
9. }
```

## stop

PhonePC/2in1TabletTVWearable

stop(callback: AsyncCallback<void>): void

结束录制，通过注册回调函数获取结果。使用callback异步回调。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<void> | 是 | 回调函数。当结束录制成功，err为undefined，否则为错误对象。 |

**示例：**

```
1. function stopVideoOutput(videoOutput: camera.VideoOutput): void {
2. videoOutput.stop(() => {
3. console.info('Callback invoked to indicate the video output stop success.');
4. });
5. }
```

## stop

PhonePC/2in1TabletTVWearable

stop(): Promise<void>

结束录制。使用Promise异步回调。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. function stopVideoOutput(videoOutput: camera.VideoOutput): void {
4. videoOutput.stop().then(() => {
5. console.info('Promise returned to indicate that stop method execution success.');
6. }).catch((error: BusinessError) => {
7. console.error(`Failed to video output stop, error code: ${error.code}.`);
8. });
9. }
```

## on('frameStart')

PhonePC/2in1TabletTVWearable

on(type: 'frameStart', callback: AsyncCallback<void>): void

监听录像开始，通过注册回调函数获取结果。使用callback异步回调。

说明

当前注册监听接口，不支持在on监听的回调方法里，调用off注销回调。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'frameStart'，videoOutput创建成功后可监听。底层第一次曝光时触发该事件并返回。 |
| callback | AsyncCallback<void> | 是 | 回调函数，用于获取结果。 只要有该事件返回就证明录像开始。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. function callback(err: BusinessError): void {
4. if (err.code) {
5. console.error(`Callback Error, errorCode: ${err.code}`);
6. return;
7. }
8. console.info('Video frame started');
9. }

11. function registerVideoOutputFrameStart(videoOutput: camera.VideoOutput): void {
12. videoOutput.on('frameStart', callback);
13. }
```

## off('frameStart')

PhonePC/2in1TabletTVWearable

off(type: 'frameStart', callback?: AsyncCallback<void>): void

注销监听录像开始。

说明

当前注册监听接口，不支持在on监听的回调方法里，调用off注销回调。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'frameStart'，videoOutput创建成功后可监听。 |
| callback | AsyncCallback<void> | 否 | 回调函数，如果指定参数则取消对应callback（callback对象不可是匿名函数），否则取消所有callback。 |

**示例：**

```
1. function unregisterVideoOutputFrameStart(videoOutput: camera.VideoOutput): void {
2. videoOutput.off('frameStart');
3. }
```

## on('frameEnd')

PhonePC/2in1TabletTVWearable

on(type: 'frameEnd', callback: AsyncCallback<void>): void

监听录像结束，通过注册回调函数获取结果。使用callback异步回调。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'frameEnd'，videoOutput创建成功后可监听。录像完全结束最后一帧时触发该事件并返回。 |
| callback | AsyncCallback<void> | 是 | 回调函数，用于获取结果。 只要有该事件返回就证明录像结束。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. function callback(err: BusinessError): void {
4. if (err.code) {
5. console.error(`Callback Error, errorCode: ${err.code}`);
6. return;
7. }
8. console.info('Video frame ended');
9. }

11. function registerVideoOutputFrameEnd(videoOutput: camera.VideoOutput): void {
12. videoOutput.on('frameEnd', callback);
13. }
```

## off('frameEnd')

PhonePC/2in1TabletTVWearable

off(type: 'frameEnd', callback?: AsyncCallback<void>): void

注销监听录像结束。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'frameEnd'，videoOutput创建成功后可监听。 |
| callback | AsyncCallback<void> | 否 | 回调函数，如果指定参数则取消对应callback（callback对象不可是匿名函数），否则取消所有callback。 |

**示例：**

```
1. function unregisterVideoOutputFrameEnd(videoOutput: camera.VideoOutput): void {
2. videoOutput.off('frameEnd');
3. }
```

## on('error')

PhonePC/2in1TabletTVWearable

on(type: 'error', callback: ErrorCallback): void

监听录像输出发生错误，通过注册回调函数获取结果。使用callback异步回调。

说明

当前注册监听接口，不支持在on监听的回调方法里，调用off注销回调。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'error'，videoOutput创建成功后可监听。录像接口调用出现错误时触发该事件并返回对应错误码，比如调用[start](arkts-apis-camera-videooutput.md#start-1)，[CameraOutput.release](arkts-apis-camera-cameraoutput.md#release-1)接口时出现错误返回对应错误信息。 |
| callback | [ErrorCallback](js-apis-base.md#errorcallback) | 是 | 回调函数，用于获取错误信息。返回错误码，错误码类型[CameraErrorCode](arkts-apis-camera-e.md#cameraerrorcode)。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. function callback(err: BusinessError): void {
4. console.error(`Video output error code: ${err.code}`);
5. }

7. function registerVideoOutputError(videoOutput: camera.VideoOutput): void {
8. videoOutput.on('error', callback);
9. }
```

## off('error')

PhonePC/2in1TabletTVWearable

off(type: 'error', callback?: ErrorCallback): void

注销监听录像输出发生错误。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'error'，photoOutput创建成功后可监听。 |
| callback | [ErrorCallback](js-apis-base.md#errorcallback) | 否 | 回调函数，如果指定参数则取消对应callback（callback对象不可是匿名函数），否则取消所有callback。 |

**示例：**

```
1. function unregisterVideoOutputError(videoOutput: camera.VideoOutput): void {
2. videoOutput.off('error');
3. }
```

## getSupportedFrameRates12+

PhonePC/2in1TabletTVWearable

getSupportedFrameRates(): Array<FrameRateRange>

查询支持的帧率范围。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<[FrameRateRange](arkts-apis-camera-i.md#frameraterange)> | 支持的帧率范围列表。若接口调用失败，返回undefined。 |

**示例：**

```
1. function getSupportedFrameRates(videoOutput: camera.VideoOutput): Array<camera.FrameRateRange> {
2. let supportedFrameRatesArray: Array<camera.FrameRateRange> = videoOutput.getSupportedFrameRates();
3. return supportedFrameRatesArray;
4. }
```

## setFrameRate12+

PhonePC/2in1TabletTVWearable

setFrameRate(minFps: number, maxFps: number): void

设置录像流帧率范围，设置的范围必须在支持的帧率范围内。

进行设置前，可通过[getSupportedFrameRates](arkts-apis-camera-videooutput.md#getsupportedframerates12)查询支持的帧率范围。

说明

仅在[PhotoSession](arkts-apis-camera-photosession.md)或[VideoSession](arkts-apis-camera-videosession.md)模式下支持。

接口调用前，先调用[getActiveFrameRate](arkts-apis-camera-videooutput.md#getactiveframerate12)接口查询当前VideoSession的帧率，若下发的帧率与当前帧率相等，则下发的帧率不会生效。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| minFps | number | 是 | 最小帧率，单位：fps。当传入的最大值小于最小值时，传参异常，接口不生效。 |
| maxFps | number | 是 | 最大帧率，单位：fps。当传入的最小值大于最大值时，传参异常，接口不生效。 |

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](errorcode-camera.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400101 | Parameter missing or parameter type incorrect. |
| 7400110 | Unresolved conflicts with current configurations. |

**示例：**

```
1. function setFrameRateRange(videoOutput: camera.VideoOutput, frameRateRange: Array<number>): void {
2. videoOutput.setFrameRate(frameRateRange[0], frameRateRange[1]);
3. }
```

## getActiveFrameRate12+

PhonePC/2in1TabletTVWearable

getActiveFrameRate(): FrameRateRange

获取已设置的帧率范围。

使用[setFrameRate](arkts-apis-camera-videooutput.md#setframerate12)对录像流设置过帧率后可查询。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [FrameRateRange](arkts-apis-camera-i.md#frameraterange) | 帧率范围 |

**示例：**

```
1. function getActiveFrameRate(videoOutput: camera.VideoOutput): camera.FrameRateRange {
2. let activeFrameRate: camera.FrameRateRange = videoOutput.getActiveFrameRate();
3. return activeFrameRate;
4. }
```

## getActiveProfile12+

PhonePC/2in1TabletTVWearable

getActiveProfile(): VideoProfile

获取当前生效的配置信息。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [VideoProfile](arkts-apis-camera-i.md#videoprofile) | 当前生效的配置信息 |

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](errorcode-camera.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400201 | Camera service fatal error. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. function testGetActiveProfile(videoOutput: camera.VideoOutput): camera.Profile | undefined {
4. let activeProfile: camera.VideoProfile | undefined = undefined;
5. try {
6. activeProfile = videoOutput.getActiveProfile();
7. } catch (error) {
8. // 失败返回错误码error.code并处理。
9. let err = error as BusinessError;
10. console.error(`The videoOutput.getActiveProfile call failed. error code: ${err.code}`);
11. }
12. return activeProfile;
13. }
```

## isMirrorSupported15+

PhonePC/2in1TabletTVWearable

isMirrorSupported(): boolean

查询是否支持镜像录像。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回是否支持镜像录像，true表示支持，false表示不支持。若接口调用失败，返回undefined。 |

**示例：**

```
1. function testIsMirrorSupported(videoOutput: camera.VideoOutput): boolean {
2. let isSupported: boolean = videoOutput.isMirrorSupported();
3. return isSupported;
4. }
```

## enableMirror15+

PhonePC/2in1TabletTVWearable

enableMirror(enabled: boolean): void

启用/关闭镜像录像。

* 调用该接口前，需要通过[isMirrorSupported](arkts-apis-camera-videooutput.md#ismirrorsupported15)查询是否支录像镜像功能。
* 启用/关闭录像镜像后，需要通过[getVideoRotation](arkts-apis-camera-videooutput.md#getvideorotation12)获取录像旋转角度以及[updateRotation](arkts-apis-media-avrecorder.md#updaterotation12)更新旋转角度。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enabled | boolean | 是 | 启用/关闭镜像录像。true为开启镜像录像，false为关闭镜像录像。 |

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](errorcode-camera.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400101 | Parameter missing or parameter type incorrect. |
| 7400103 | Session not config. |

**示例：**

```
1. import { camera } from '@kit.CameraKit';
2. import { media } from '@kit.MediaKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. function enableMirror(videoOutput: camera.VideoOutput, mirrorMode: boolean, aVRecorder: media.AVRecorder, deviceDegree : number): void {
6. try {
7. videoOutput.enableMirror(mirrorMode);
8. aVRecorder.updateRotation(videoOutput.getVideoRotation(deviceDegree));
9. } catch (error) {
10. let err = error as BusinessError;
11. }
12. }
```

## getVideoRotation12+

PhonePC/2in1TabletTVWearable

getVideoRotation(deviceDegree?: number): ImageRotation

获取录像旋转角度。

* 设备自然方向：设备默认使用方向。例如，直板机默认使用方向为竖屏（充电口向下）。
* 相机镜头角度：值等于相机图像顺时针旋转到设备自然方向的角度。例如，直板机后置相机传感器是横屏安装的，所以需要顺时针旋转90度到设备自然方向。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceDegree | number | 否 | 设备旋转角度，单位度，取值范围[0, 360]。  从API version 23开始，入参deviceDegree为可选参数，当不传入参数时，由系统获取deviceDegree进行录像旋转角度计算。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ImageRotation](arkts-apis-camera-e.md#imagerotation) | 返回录像旋转角度。若接口调用失败，返回undefined。 |

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](errorcode-camera.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400201 | Camera service fatal error. |

**示例：**

```
1. import { camera } from '@kit.CameraKit';
2. import { Decimal } from '@kit.ArkTS';
3. import { sensor } from '@kit.SensorServiceKit';
4. import { BusinessError } from '@kit.BasicServicesKit';

6. async function getVideoRotation(videoOutput: camera.VideoOutput): Promise<camera.ImageRotation> {
7. let deviceDegree = await getDeviceDegree();
8. let videoRotation: camera.ImageRotation = camera.ImageRotation.ROTATION_0;
9. try {
10. videoRotation = videoOutput.getVideoRotation(deviceDegree);
11. } catch (error) {
12. let err = error as BusinessError;
13. console.error('Failed to get video rotation: ' + JSON.stringify(err));
14. }
15. return videoRotation;
16. }

18. function testGetVideoRotationWithOutParam(videoOutput: camera.VideoOutput): camera.ImageRotation {
19. let videoRotation: camera.ImageRotation = camera.ImageRotation.ROTATION_0;
20. try {
21. videoRotation = videoOutput.getVideoRotation();
22. console.info(`Video rotation is: ${videoRotation}`);
23. } catch (error) {
24. // 失败返回错误码error.code并处理。
25. let err = error as BusinessError;
26. console.error(`The videoOutput.testGetVideoRotationWithOutParam call failed. error code: ${err.code}`);
27. }
28. return videoRotation;
29. }

31. // 获取设备旋转角度
32. function getDeviceDegree(): Promise<number> {
33. return new Promise<number>((resolve) => {
34. try {
35. sensor.once(sensor.SensorId.GRAVITY, (data: sensor.GravityResponse) => {
36. console.info('Succeeded in invoking once. X-coordinate component: ' + data.x);
37. console.info('Succeeded in invoking once. Y-coordinate component: ' + data.y);
38. console.info('Succeeded in invoking once. Z-coordinate component: ' + data.z);
39. let x = data.x;
40. let y = data.y;
41. let z = data.z;
42. let deviceDegree: number;
43. if ((x * x + y * y) * 3 < z * z) {
44. deviceDegree = -1;
45. } else {
46. let sd: Decimal = Decimal.atan2(y, -x);
47. let sc: Decimal = Decimal.round(Number(sd) / 3.141592653589 * 180)
48. deviceDegree = 90 - Number(sc);
49. deviceDegree = deviceDegree >= 0 ? deviceDegree% 360 : deviceDegree% 360 + 360;
50. }
51. resolve(deviceDegree);
52. });
53. } catch (error) {
54. let err = error as BusinessError;
55. console.error('Failed to register gravity sensor: ' + JSON.stringify(err));
56. resolve(-1); // 异常时返回默认值
57. }
58. });
59. }
```
