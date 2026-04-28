---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-camera-camerainput
title: Interface (CameraInput)
breadcrumb: API参考 > 媒体 > Camera Kit（相机服务） > ArkTS API > @ohos.multimedia.camera (相机管理) > Interface (CameraInput)
category: harmonyos-references
scraped_at: 2026-04-28T08:12:33+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:4f62458b559c77e432924134d2777d2986b7877720cceebbf9111a6fbbbbc100
---

相机设备输入对象。

会话中[Session](arkts-apis-camera-session.md)使用的相机信息。

说明

本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { camera } from '@kit.CameraKit';
```

## open

PhonePC/2in1TabletTVWearable

open(callback: AsyncCallback<void>): void

打开相机，通过注册回调函数获取状态。使用callback异步回调。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<void> | 是 | 回调函数。当打开相机成功，err为undefined，否则为错误对象，错误码类型[CameraErrorCode](arkts-apis-camera-e.md#cameraerrorcode)。 |

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](errorcode-camera.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400107 | Can not use camera cause of conflict. |
| 7400108 | Camera disabled cause of security reason. |
| 7400201 | Camera service fatal error. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. function openCameraInput(cameraInput: camera.CameraInput): void {
4. cameraInput.open((err: BusinessError) => {
5. if (err) {
6. console.error(`Failed to open the camera, error code: ${err.code}.`);
7. return;
8. }
9. console.info('Callback returned with camera opened.');
10. });
11. }
```

## open

PhonePC/2in1TabletTVWearable

open(): Promise<void>

打开相机，使用Promise异步回调。

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
| 7400102 | Operation not allowed. |
| 7400107 | Can not use camera cause of conflict. |
| 7400108 | Camera disabled cause of security reason. |
| 7400201 | Camera service fatal error. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. function openCameraInput(cameraInput: camera.CameraInput): void {
4. cameraInput.open().then(() => {
5. console.info('Promise returned with camera opened.');
6. }).catch((error: BusinessError) => {
7. console.error(`Failed to open the camera, error code: ${error.code}.`);
8. });
9. }
```

## open12+

PhonePC/2in1TabletTVWearable

open(isSecureEnabled: boolean): Promise<bigint>

打开相机。使用Promise异步回调。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isSecureEnabled | boolean | 是 | 设置true为使能以安全的方式打开相机，设置false则反之。接口调用失败会返回相应错误码，错误码类型[CameraErrorCode](arkts-apis-camera-e.md#cameraerrorcode)。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<bigint> | Promise对象，返回安全相机的句柄。 |

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](errorcode-camera.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400107 | Can not use camera cause of conflict. |
| 7400108 | Camera disabled cause of security reason. |
| 7400201 | Camera service fatal error. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. function openCameraInput(cameraInput: camera.CameraInput): void {
4. cameraInput.open(true).then(() => {
5. console.info('Promise returned with camera opened.');
6. }).catch((error: BusinessError) => {
7. console.error(`Failed to open the camera, error code: ${error.code}.`);
8. });
9. }
```

## open18+

PhonePC/2in1TabletTVWearable

open(type: CameraConcurrentType): Promise<void>

以指定的并发类型打开相机。使用Promise异步回调。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [CameraConcurrentType](arkts-apis-camera-e.md#cameraconcurrenttype18) | 是 | 以指定的并发类型打开相机。接口调用失败会返回相应错误码。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](errorcode-camera.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400102 | Operation not allowed. |
| 7400107 | Can not use camera cause of conflict. |
| 7400108 | Camera disabled cause of security reason. |
| 7400201 | Camera service fatal error. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. function openCameraInput(cameraInput: camera.CameraInput): void {
4. cameraInput.open(0).then(() => {
5. console.info('Promise returned with camera opened.');
6. }).catch((error: BusinessError) => {
7. console.error(`Failed to open the camera, error code: ${error.code}.`);
8. });
9. }
```

## close

PhonePC/2in1TabletTVWearable

close(callback: AsyncCallback<void>): void

关闭相机，通过注册回调函数获取状态。使用callback异步回调。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<void> | 是 | 回调函数。当关闭相机成功，err为undefined，否则为错误对象。错误码类型[CameraErrorCode](arkts-apis-camera-e.md#cameraerrorcode)。 |

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](errorcode-camera.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400201 | Camera service fatal error. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. function closeCameraInput(cameraInput: camera.CameraInput): void {
4. cameraInput.close((err: BusinessError) => {
5. if (err) {
6. console.error(`Failed to close the cameras, error code: ${err.code}.`);
7. return;
8. }
9. console.info('Callback returned with camera closed.');
10. });
11. }
```

## close

PhonePC/2in1TabletTVWearable

close(): Promise<void>

关闭相机，使用Promise异步回调。

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
| 7400201 | Camera service fatal error. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. function closeCameraInput(cameraInput: camera.CameraInput): void {
4. cameraInput.close().then(() => {
5. console.info('Promise returned with camera closed.');
6. }).catch((error: BusinessError) => {
7. console.error(`Failed to close the cameras, error code: ${error.code}.`);
8. });
9. }
```

## on('error')

PhonePC/2in1TabletTVWearable

on(type: 'error', camera: CameraDevice, callback: ErrorCallback): void

监听CameraInput的错误事件，通过注册回调函数获取结果。使用callback异步回调。

说明

当前注册监听接口，不支持在on监听的回调方法里，调用off注销回调。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'error'，CameraInput对象创建成功可监听。相机设备出错情况下可触发该事件并返回结果，比如设备不可用或者冲突等返回对应错误信息。 |
| camera | [CameraDevice](arkts-apis-camera-i.md#cameradevice) | 是 | CameraDevice对象。 |
| callback | [ErrorCallback](js-apis-base.md#errorcallback) | 是 | 回调函数，用于获取结果。返回错误码，错误码类型[CameraErrorCode](arkts-apis-camera-e.md#cameraerrorcode)。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. function callback(err: BusinessError): void {
4. console.error(`Camera input error code: ${err.code}`);
5. }

7. function registerCameraInputError(cameraInput: camera.CameraInput, camera: camera.CameraDevice): void {
8. cameraInput.on('error', camera, callback);
9. }
```

## off('error')

PhonePC/2in1TabletTVWearable

off(type: 'error', camera: CameraDevice, callback?: ErrorCallback): void

注销监听CameraInput的错误事件。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'error'，CameraInput对象创建成功可监听。相机设备出错情况下可触发该事件并返回结果，比如设备不可用或者冲突等返回对应错误信息。 |
| camera | [CameraDevice](arkts-apis-camera-i.md#cameradevice) | 是 | CameraDevice对象。 |
| callback | [ErrorCallback](js-apis-base.md#errorcallback) | 否 | 回调函数，如果指定参数则取消对应callback（callback对象不能是匿名函数），否则取消所有callback。 |

**示例：**

```
1. function unregisterCameraInputError(cameraInput: camera.CameraInput, camera: camera.CameraDevice): void {
2. cameraInput.off('error', camera);
3. }
```

## isPhysicalCameraOrientationVariable22+

PhonePC/2in1TabletTVWearable

isPhysicalCameraOrientationVariable(): boolean

查询设备不同折叠状态下，相机物理镜头角度是否可变。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 查询设备不同折叠状态下，相机物理镜头角度是否可变。true表示可变，false表示不可变。若接口调用失败，返回undefined。 |

**示例：**

```
1. function isPhysicalCameraOrientationVariable(cameraInput: camera.CameraInput): boolean {
2. let isVariable: boolean = cameraInput.isPhysicalCameraOrientationVariable();
3. return isVariable;
4. }
```

## getPhysicalCameraOrientation22+

PhonePC/2in1TabletTVWearable

getPhysicalCameraOrientation(): number

获取设备当前折叠状态下的物理镜头角度。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 返回设备当前折叠状态下的物理镜头角度。 |

**示例：**

```
1. function getPhysicalCameraOrientation(cameraInput: camera.CameraInput): number {
2. let physicalCameraOrientation: number = cameraInput.getPhysicalCameraOrientation();
3. return physicalCameraOrientation;
4. }
```

## usePhysicalCameraOrientation22+

PhonePC/2in1TabletTVWearable

usePhysicalCameraOrientation(isUsed: boolean): void

选择是否使用物理镜头角度。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isUsed | boolean | 是 | 选择是否使用物理镜头角度。true表示使用，false表示不使用。 |

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](errorcode-camera.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400102 | Operation not allowed. |
| 7400201 | Camera service fatal error. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. function usePhysicalCameraOrientation(cameraInput: camera.CameraInput, isUsed: boolean): void {
4. try {
5. cameraInput.usePhysicalCameraOrientation(isUsed);
6. } catch (error) {
7. let err = error as BusinessError;
8. console.error(`The usePhysicalCameraOrientation call failed. error code: ${err.code}`);
9. }
10. }
```

## on('cameraOcclusionDetection')23+

PhonePC/2in1TabletTVWearable

on(type: 'cameraOcclusionDetection', callback: AsyncCallback<CameraOcclusionDetectionResult>): void

监听CameraInput的镜头遮挡或脏污事件，通过注册回调函数获取结果。使用callback异步回调。

说明

当前注册监听接口，不支持在on监听的回调方法里，调用off注销回调。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'cameraOcclusionDetection'，CameraInput对象创建成功可监听。相机镜头被遮挡或有脏污可触发该事件并返回结果。 |
| callback | AsyncCallback<[CameraOcclusionDetectionResult](arkts-apis-camera-i.md#cameraocclusiondetectionresult23)> | 是 | 回调函数，用于获取结果。返回遮挡状态。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. function callback(err: BusinessError, result: camera.CameraOcclusionDetectionResult): void {
4. if (err !== undefined && err.code !== 0) {
5. console.error('cameraOcclusionDetection with errorCode = ' + err.code);
6. return;
7. }
8. if (!result) {
9. console.error(`cameraOcclusionDetection result: undefined`);
10. return;
11. }
12. console.info(`onCameraOcclusionDetection isCameraOccluded: ${result.isCameraOccluded}`);
13. console.info(`onCameraOcclusionDetection isCameraLensDirty: ${result.isCameraLensDirty}`);
14. }

16. function registerCameraOcclusionDetection(cameraInput: camera.CameraInput): void {
17. cameraInput.on('cameraOcclusionDetection', callback);
18. }
```

## off('cameraOcclusionDetection')23+

PhonePC/2in1TabletTVWearable

off(type: 'cameraOcclusionDetection', callback?: AsyncCallback<CameraOcclusionDetectionResult>): void

注销监听CameraInput的镜头遮挡或脏污事件。使用callback异步回调。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'cameraOcclusionDetection'，CameraInput对象创建成功可监听。相机镜头被遮挡或有脏污可触发该事件并返回结果。 |
| callback | AsyncCallback<[CameraOcclusionDetectionResult](arkts-apis-camera-i.md#cameraocclusiondetectionresult23)> | 否 | 回调函数，如果指定参数则取消对应callback（callback对象不可是匿名函数），否则取消所有callback。 |

**示例：**

```
1. function callback(err: BusinessError, result: camera.CameraOcclusionDetectionResult): void {
2. if (err !== undefined && err.code !== 0) {
3. console.error('cameraOcclusionDetection with errorCode = ' + err.code);
4. return;
5. }
6. if (!result) {
7. console.error(`cameraOcclusionDetection result: undefined`);
8. return;
9. }
10. console.info(`onCameraOcclusionDetection isCameraOccluded: ${result.isCameraOccluded}`);
11. console.info(`onCameraOcclusionDetection isCameraLensDirty: ${result.isCameraLensDirty}`);
12. }

14. function unregisterCameraOcclusionDetection(cameraInput: camera.CameraInput): void {
15. cameraInput.off('cameraOcclusionDetection', callback);
16. }

18. function unregisterAllCameraOcclusionDetection(cameraInput: camera.CameraInput): void {
19. cameraInput.off('cameraOcclusionDetection');
20. }
```
