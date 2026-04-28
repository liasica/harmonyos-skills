---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-camera-photooutput
title: Interface (PhotoOutput)
breadcrumb: API参考 > 媒体 > Camera Kit（相机服务） > ArkTS API > @ohos.multimedia.camera (相机管理) > Interface (PhotoOutput)
category: harmonyos-references
scraped_at: 2026-04-28T08:12:37+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:13227172789f085355353487b7230f39ca2edcd8c57f132b22f2d8ec39ce950b
---

拍照会话中使用的输出信息，继承[CameraOutput](arkts-apis-camera-cameraoutput.md)。

说明

本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { camera } from '@kit.CameraKit';
```

## capture

PhonePC/2in1TabletTVWearable

capture(callback: AsyncCallback<void>): void

以默认设置触发一次拍照，通过注册回调函数获取结果。使用callback异步回调。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<void> | 是 | 回调函数。当以默认设置触发拍照成功，err为undefined，否则为错误对象。错误码类型[CameraErrorCode](arkts-apis-camera-e.md#cameraerrorcode)。 |

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](errorcode-camera.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400104 | Session not running. |
| 7400201 | Camera service fatal error. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. function capture(photoOutput: camera.PhotoOutput): void {
4. photoOutput.capture((err: BusinessError) => {
5. if (err) {
6. console.error(`Failed to capture the photo, error code: ${err.code}.`);
7. return;
8. }
9. console.info('Callback invoked to indicate the photo capture request success.');
10. });
11. }
```

## capture

PhonePC/2in1TabletTVWearable

capture(): Promise<void>

以默认设置触发一次拍照。使用Promise异步回调。

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
| 7400104 | Session not running. |
| 7400201 | Camera service fatal error. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. function capture(photoOutput: camera.PhotoOutput): void {
4. photoOutput.capture().then(() => {
5. console.info('Promise returned to indicate that photo capture request success.');
6. }).catch((error: BusinessError) => {
7. console.error(`Failed to photo output capture, error code: ${error.code}.`);
8. });
9. }
```

## capture

PhonePC/2in1TabletTVWearable

capture(setting: PhotoCaptureSetting, callback: AsyncCallback<void>): void

以指定参数触发一次拍照，通过注册回调函数获取结果。使用callback异步回调。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| setting | [PhotoCaptureSetting](arkts-apis-camera-i.md#photocapturesetting) | 是 | 拍照设置，传入undefined类型数据按默认设置触发一次拍照处理。 |
| callback | AsyncCallback<void> | 是 | 回调函数，用于获取结果。接口调用失败会返回相应错误码，错误码类型[CameraErrorCode](arkts-apis-camera-e.md#cameraerrorcode)。 |

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](errorcode-camera.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400101 | Parameter missing or parameter type incorrect. |
| 7400104 | Session not running. |
| 7400201 | Camera service fatal error. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. function capture(photoOutput: camera.PhotoOutput): void {
4. let captureLocation: camera.Location = {
5. latitude: 0,
6. longitude: 0,
7. altitude: 0
8. }
9. let settings: camera.PhotoCaptureSetting = {
10. quality: camera.QualityLevel.QUALITY_LEVEL_LOW,
11. rotation: camera.ImageRotation.ROTATION_0,
12. location: captureLocation,
13. mirror: false
14. }
15. photoOutput.capture(settings, (err: BusinessError) => {
16. if (err) {
17. console.error(`Failed to capture the photo, error code: ${err.code}.`);
18. return;
19. }
20. console.info('Callback invoked to indicate the photo capture request success.');
21. });
22. }
```

## capture

PhonePC/2in1TabletTVWearable

capture(setting: PhotoCaptureSetting): Promise<void>

以指定参数触发一次拍照。使用Promise异步回调。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| setting | [PhotoCaptureSetting](arkts-apis-camera-i.md#photocapturesetting) | 是 | 拍照设置，传入undefined类型数据按默认设置触发一次拍照处理。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](errorcode-camera.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400101 | Parameter missing or parameter type incorrect. |
| 7400104 | Session not running. |
| 7400201 | Camera service fatal error. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. function capture(photoOutput: camera.PhotoOutput): void {
4. let captureLocation: camera.Location = {
5. latitude: 0,
6. longitude: 0,
7. altitude: 0
8. }
9. let settings: camera.PhotoCaptureSetting = {
10. quality: camera.QualityLevel.QUALITY_LEVEL_LOW,
11. rotation: camera.ImageRotation.ROTATION_0,
12. location: captureLocation,
13. mirror: false
14. }
15. photoOutput.capture(settings).then(() => {
16. console.info('Promise returned to indicate that photo capture request success.');
17. }).catch((error: BusinessError) => {
18. console.error(`Failed to photo output capture, error code: ${error.code}.`);
19. });
20. }
```

## on('photoAvailable')11+

PhonePC/2in1TabletTVWearable

on(type: 'photoAvailable', callback: AsyncCallback<Photo>): void

注册监听拍照返回照片上报事件。使用callback异步回调。

说明

当前注册监听接口，不支持在on监听的回调方法里，调用off注销回调。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'photoAvailable'，photoOutput创建成功后可监听。 |
| callback | AsyncCallback<[Photo](arkts-apis-camera-photo.md)> | 是 | 回调函数，用于监听拍照返回照片上报事件。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { image } from '@kit.ImageKit';
3. import { camera } from '@kit.CameraKit';

5. function callback(err: BusinessError, photo: camera.Photo): void {
6. if (err !== undefined && err.code !== 0) {
7. console.error(`Callback Error, errorCode: ${err.code}`);
8. return;
9. }
10. let mainImage: image.Image = photo.main;
11. }

13. function registerPhotoOutputPhotoAvailable(photoOutput: camera.PhotoOutput): void {
14. photoOutput.on('photoAvailable', callback);
15. }
```

## off('photoAvailable')11+

PhonePC/2in1TabletTVWearable

off(type: 'photoAvailable', callback?: AsyncCallback<Photo>): void

注销监听拍照返回照片上报事件。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'photoAvailable'，photoOutput创建成功后可监听。 |
| callback | AsyncCallback<[Photo](arkts-apis-camera-photo.md)> | 否 | 回调函数，如果指定参数则取消对应callback（callback对象不可是匿名函数），否则取消所有callback。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { image } from '@kit.ImageKit';

4. function callback(err: BusinessError, photo: camera.Photo): void {
5. if (err !== undefined && err.code !== 0) {
6. console.error(`Callback Error, errorCode: ${err.code}`);
7. return;
8. }
9. let mainImage: image.Image = photo.main;
10. }

12. function unRegisterPhotoOutputPhotoAvailable(photoOutput: camera.PhotoOutput): void {
13. photoOutput.off('photoAvailable', callback);
14. }
```

## onCapturePhotoAvailable23+

PhonePC/2in1TabletTVWearable

onCapturePhotoAvailable(callback: Callback<CapturePhoto>): void

注册监听全质量图和未压缩图。使用callback异步回调。

说明

* 注册监听接口时，不支持在该接口监听的回调方法里调用[offCapturePhotoAvailable](arkts-apis-camera-photooutput.md#offcapturephotoavailable23)注销回调。
* 拍摄未压缩图（YUV）格式图片时，仅支持使用此接口注册监听。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<[CapturePhoto](arkts-apis-camera-capturephoto.md)> | 是 | 回调函数，用于监听全质量图和未压缩图上报事件。 |

**示例：**

```
1. import { camera } from '@kit.CameraKit';
2. import { image } from '@kit.ImageKit';

4. function callback(capturePhoto: camera.CapturePhoto): void {
5. let picture: image.Image | image.Picture = capturePhoto.main;
6. }

8. function registerCapturePhotoOutputPhotoAvailable(photoOutput: camera.PhotoOutput): void {
9. photoOutput.onCapturePhotoAvailable(callback);
10. }
```

## offCapturePhotoAvailable23+

PhonePC/2in1TabletTVWearable

offCapturePhotoAvailable(callback?: Callback<CapturePhoto>): void

注销监听全质量图和未压缩图。使用callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<[CapturePhoto](arkts-apis-camera-capturephoto.md)> | 否 | 回调函数，如果指定参数则取消对应callback，callback对象不可是匿名函数，否则取消所有callback。 |

**示例：**

```
1. import { camera } from '@kit.CameraKit';
2. import { image } from '@kit.ImageKit';

4. function callback(capturePhoto: camera.CapturePhoto): void {
5. let picture: image.Image | image.Picture = capturePhoto.main;
6. }

8. function unRegisterCapturePhotoOutputPhotoAvailable(photoOutput: camera.PhotoOutput): void {
9. photoOutput.offCapturePhotoAvailable(callback);
10. }
```

## on('captureStartWithInfo')11+

PhonePC/2in1TabletTVWearable

on(type: 'captureStartWithInfo', callback: AsyncCallback<CaptureStartInfo>): void

监听拍照开始，通过注册回调函数获取[CaptureStartInfo](arkts-apis-camera-i.md#capturestartinfo11)。使用callback异步回调。

说明

当前注册监听接口，不支持在on监听的回调方法里，调用off注销回调。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'captureStartWithInfo'，photoOutput创建成功后可监听。 |
| callback | AsyncCallback<[CaptureStartInfo](arkts-apis-camera-i.md#capturestartinfo11)> | 是 | 使用callback的方式获取Capture ID。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. function callback(err: BusinessError, captureStartInfo: camera.CaptureStartInfo): void {
4. if (err !== undefined && err.code !== 0) {
5. console.error(`Callback Error, errorCode: ${err.code}`);
6. return;
7. }
8. console.info(`photo capture started, captureStartInfo : ${captureStartInfo}`);
9. }

11. function registerCaptureStartWithInfo(photoOutput: camera.PhotoOutput): void {
12. photoOutput.on('captureStartWithInfo', callback);
13. }
```

## off('captureStartWithInfo')11+

PhonePC/2in1TabletTVWearable

off(type: 'captureStartWithInfo', callback?: AsyncCallback<CaptureStartInfo>): void

注销监听拍照。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'captureStartWithInfo'，photoOutput创建成功后可监听。 |
| callback | AsyncCallback<[CaptureStartInfo](arkts-apis-camera-i.md#capturestartinfo11)> | 否 | 回调函数，如果指定参数则取消对应callback（callback对象不可是匿名函数），否则取消所有callback。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. function unRegisterCaptureStartWithInfo(photoOutput: camera.PhotoOutput): void {
4. photoOutput.off('captureStartWithInfo');
5. }
```

## isMovingPhotoSupported12+

PhonePC/2in1TabletTVWearable

isMovingPhotoSupported(): boolean

查询是否支持动态照片拍摄。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回是否支持动态照片拍照。true表示支持，false表示不支持。若接口调用失败，返回undefined。 |

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](errorcode-camera.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400201 | Camera service fatal error. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. function isMovingPhotoSupported(photoOutput: camera.PhotoOutput): boolean {
4. let isSupported: boolean = false;
5. try {
6. isSupported = photoOutput.isMovingPhotoSupported();
7. } catch (error) {
8. // 失败返回错误码error.code并处理。
9. let err = error as BusinessError;
10. console.error(`The isMovingPhotoSupported call failed. error code: ${err.code}`);
11. }
12. return isSupported;
13. }
```

## enableMovingPhoto12+

PhonePC/2in1TabletTVWearable

enableMovingPhoto(enabled: boolean): void

使能动态照片拍照。

**需要权限：** ohos.permission.MICROPHONE

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enabled | boolean | 是 | 使能动态照片拍照。true为开启动态照片，false为关闭动态照片。 |

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](errorcode-camera.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | permission denied. |
| 7400101 | Parameter missing or parameter type incorrect. |
| 7400201 | Camera service fatal error. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. function enableMovingPhoto(photoOutput: camera.PhotoOutput): void {
4. try {
5. photoOutput.enableMovingPhoto(true);
6. } catch (error) {
7. // 失败返回错误码error.code并处理。
8. let err = error as BusinessError;
9. console.error(`The enableMovingPhoto call failed. error code: ${err.code}`);
10. }
11. }
```

## on('photoAssetAvailable')12+

PhonePC/2in1TabletTVWearable

on(type: 'photoAssetAvailable', callback: AsyncCallback<photoAccessHelper.PhotoAsset>): void

注册监听photoAsset上报。使用callback异步回调。

说明

当前注册监听接口，不支持在on监听的回调方法里，调用off注销回调。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'photoAssetAvailable'，photoOutput创建成功后可监听。 |
| callback | AsyncCallback<[photoAccessHelper.PhotoAsset](arkts-apis-photoaccesshelper-photoasset.md)> | 是 | 回调函数，用于监听photoAsset上报。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { photoAccessHelper } from '@kit.MediaLibraryKit';

4. function photoAssetAvailableCallback(err: BusinessError, photoAsset: photoAccessHelper.PhotoAsset): void {
5. if (err) {
6. console.info(`photoAssetAvailable error: ${JSON.stringify(err)}.`);
7. return;
8. }
9. console.info('photoOutPutCallBack photoAssetAvailable');
10. // 开发者可通过photoAsset获取图片相关信息。
11. }

13. function onPhotoOutputPhotoAssetAvailable(photoOutput: camera.PhotoOutput): void {
14. photoOutput.on('photoAssetAvailable', photoAssetAvailableCallback);
15. }
```

## off('photoAssetAvailable')12+

PhonePC/2in1TabletTVWearable

off(type: 'photoAssetAvailable', callback?: AsyncCallback<photoAccessHelper.PhotoAsset>): void

注销photoAsset上报。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'photoAssetAvailable'，photoOutput创建成功后可监听。 |
| callback | AsyncCallback<[photoAccessHelper.PhotoAsset](arkts-apis-photoaccesshelper-photoasset.md)> | 否 | 需要解监听的回调方法。如果callback不为空且与此对应的监听方法一致，不为匿名方法，则解注册该方法；如果callback为空，则解监听所有回调。 |

**示例：**

```
1. function offPhotoOutputPhotoAssetAvailable(photoOutput: camera.PhotoOutput): void {
2. photoOutput.off('photoAssetAvailable');
3. }
```

## isMirrorSupported

PhonePC/2in1TabletTVWearable

isMirrorSupported(): boolean

查询是否支持镜像拍照。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回是否支持镜像拍照，true表示支持，false表示不支持。若接口调用失败，返回undefined。 |

**示例：**

```
1. function isMirrorSupported(photoOutput: camera.PhotoOutput): boolean {
2. let isSupported: boolean = photoOutput.isMirrorSupported();
3. return isSupported;
4. }
```

## enableMirror13+

PhonePC/2in1TabletTVWearable

enableMirror(enabled: boolean): void

是否启用动态照片镜像拍照。

调用该接口前，需要通过[isMovingPhotoSupported](arkts-apis-camera-photooutput.md#ismovingphotosupported12)查询是否支持动态照片拍摄功能以及通过[isMirrorSupported](arkts-apis-camera-photooutput.md#ismirrorsupported)查询是否支持镜像拍照功能。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enabled | boolean | 是 | 是否启用动态照片镜像拍照。true为开启动态照片镜像拍照，false为关闭动态照片镜像拍照。 |

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](errorcode-camera.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400101 | Parameter missing or parameter type incorrect. |
| 7400103 | Session not config. |
| 7400201 | Camera service fatal error. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. function enableMirror(photoOutput: camera.PhotoOutput): void {
4. try {
5. photoOutput.enableMirror(true);
6. } catch (error) {
7. // 失败返回错误码error.code并处理。
8. let err = error as BusinessError;
9. console.error(`The enableMirror call failed. error code: ${err.code}`);
10. }
11. }
```

## getSupportedMovingPhotoVideoCodecTypes13+

PhonePC/2in1TabletTVWearable

getSupportedMovingPhotoVideoCodecTypes(): Array<VideoCodecType>

查询支持的动态照片短视频编码类型。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<[VideoCodecType](arkts-apis-camera-e.md#videocodectype13)> | 支持的动态照片短视频编码类型列表。若接口调用失败，返回undefined。 |

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](errorcode-camera.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400201 | Camera service fatal error. |

**示例：**

```
1. function getSupportedMovingPhotoVideoCodecType(photoOutput: camera.PhotoOutput): Array<camera.VideoCodecType> {
2. let supportedVideoCodecTypesArray: Array<camera.VideoCodecType> = photoOutput.getSupportedMovingPhotoVideoCodecTypes();
3. return supportedVideoCodecTypesArray;
4. }
```

## setMovingPhotoVideoCodecType13+

PhonePC/2in1TabletTVWearable

setMovingPhotoVideoCodecType(codecType: VideoCodecType): void

设置动态照片短视频编码类型。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| codecType | [VideoCodecType](arkts-apis-camera-e.md#videocodectype13) | 是 | 动态照片短视频编码类型。  如果设置不在枚举范围内，则该参数不会生效。 |

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](errorcode-camera.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400201 | Camera service fatal error. |

**示例：**

```
1. function setMovingPhotoVideoCodecTypes(photoOutput: camera.PhotoOutput, videoCodecType: camera.VideoCodecType): void {
2. photoOutput.setMovingPhotoVideoCodecType(videoCodecType);
3. }
```

## on('frameShutter')

PhonePC/2in1TabletTVWearable

on(type: 'frameShutter', callback: AsyncCallback<FrameShutterInfo>): void

监听拍照帧输出捕获，通过注册回调函数获取结果。使用callback异步回调。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'frameShutter'，photoOutput创建成功后可监听。 |
| callback | AsyncCallback<[FrameShutterInfo](arkts-apis-camera-i.md#frameshutterinfo)> | 是 | 回调函数，用于获取相关信息。该回调返回意味着可以再次下发拍照请求。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. function callback(err: BusinessError, frameShutterInfo: camera.FrameShutterInfo): void {
4. if (err !== undefined && err.code !== 0) {
5. console.error(`Callback Error, errorCode: ${err.code}`);
6. return;
7. }
8. console.info(`CaptureId for frame : ${frameShutterInfo.captureId}`);
9. console.info(`Timestamp for frame : ${frameShutterInfo.timestamp}`);
10. }

12. function registerPhotoOutputFrameShutter(photoOutput: camera.PhotoOutput): void {
13. photoOutput.on('frameShutter', callback);
14. }
```

## off('frameShutter')

PhonePC/2in1TabletTVWearable

off(type: 'frameShutter', callback?: AsyncCallback<FrameShutterInfo>): void

注销监听拍照帧输出捕获。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'frameShutter'，photoOutput创建成功后可监听。 |
| callback | AsyncCallback<[FrameShutterInfo](arkts-apis-camera-i.md#frameshutterinfo)> | 否 | 回调函数，如果指定参数则取消对应callback（callback对象不可是匿名函数），否则取消所有callback。 |

**示例：**

```
1. function unregisterPhotoOutputFrameShutter(photoOutput: camera.PhotoOutput): void {
2. photoOutput.off('frameShutter');
3. }
```

## on('captureEnd')

PhonePC/2in1TabletTVWearable

on(type: 'captureEnd', callback: AsyncCallback<CaptureEndInfo>): void

监听拍照结束，通过注册回调函数获取结果。使用callback异步回调。

说明

当前注册监听接口，不支持在on监听的回调方法里，调用off注销回调。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'captureEnd'。photoOutput创建成功后可监听。拍照完全结束可触发该事件发生并返回相应信息。 |
| callback | AsyncCallback<[CaptureEndInfo](arkts-apis-camera-i.md#captureendinfo)> | 是 | 回调函数，用于获取相关信息。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. function callback(err: BusinessError, captureEndInfo: camera.CaptureEndInfo): void {
4. if (err !== undefined && err.code !== 0) {
5. console.error(`Callback Error, errorCode: ${err.code}`);
6. return;
7. }
8. console.info(`photo capture end, captureId : ${captureEndInfo.captureId}`);
9. console.info(`frameCount : ${captureEndInfo.frameCount}`);
10. }

12. function registerPhotoOutputCaptureEnd(photoOutput: camera.PhotoOutput): void {
13. photoOutput.on('captureEnd', callback);
14. }
```

## off('captureEnd')

PhonePC/2in1TabletTVWearable

off(type: 'captureEnd', callback?: AsyncCallback<CaptureEndInfo>): void

注销监听拍照结束。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'captureEnd'，photoOutput创建成功后可监听。 |
| callback | AsyncCallback<[CaptureEndInfo](arkts-apis-camera-i.md#captureendinfo)> | 否 | 回调函数，如果指定参数则取消对应callback（callback对象不可是匿名函数），否则取消所有callback。 |

**示例：**

```
1. function unregisterPhotoOutputCaptureEnd(photoOutput: camera.PhotoOutput): void {
2. photoOutput.off('captureEnd');
3. }
```

## on('frameShutterEnd')12+

PhonePC/2in1TabletTVWearable

on(type: 'frameShutterEnd', callback: AsyncCallback<FrameShutterEndInfo>): void

监听拍照曝光结束捕获，通过注册回调函数获取结果。使用callback异步回调。

说明

当前注册监听接口，不支持在on监听的回调方法里，调用off注销回调。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'frameShutterEnd'，photoOutput创建成功后可监听。 |
| callback | AsyncCallback<[FrameShutterEndInfo](arkts-apis-camera-i.md#frameshutterendinfo12)> | 是 | 回调函数，用于获取相关信息。该回调返回表示拍照曝光结束。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. function callback(err: BusinessError, frameShutterEndInfo: camera.FrameShutterEndInfo): void {
4. if (err !== undefined && err.code !== 0) {
5. console.error(`Callback Error, errorCode: ${err.code}`);
6. return;
7. }
8. console.info(`CaptureId for frame : ${frameShutterEndInfo.captureId}`);
9. }

11. function registerPhotoOutputFrameShutterEnd(photoOutput: camera.PhotoOutput): void {
12. photoOutput.on('frameShutterEnd', callback);
13. }
```

## off('frameShutterEnd')12+

PhonePC/2in1TabletTVWearable

off(type: 'frameShutterEnd', callback?: AsyncCallback<FrameShutterEndInfo>): void

注销监听拍照曝光结束捕获。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'frameShutterEnd'，photoOutput创建成功后可监听。 |
| callback | AsyncCallback<[FrameShutterEndInfo](arkts-apis-camera-i.md#frameshutterendinfo12)> | 否 | 回调函数，如果指定参数则取消对应callback（callback对象不可是匿名函数），否则取消所有callback。 |

**示例：**

```
1. function unregisterPhotoOutputFrameShutterEnd(photoOutput: camera.PhotoOutput): void {
2. photoOutput.off('frameShutterEnd');
3. }
```

## on('captureReady')12+

PhonePC/2in1TabletTVWearable

on(type: 'captureReady', callback: AsyncCallback<void>): void

监听可拍下一张，通过注册回调函数获取结果。使用callback异步回调。

说明

当前注册监听接口，不支持在on监听的回调方法里，调用off注销回调。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'captureReady'，photoOutput创建成功后可监听。当下一张可拍时可触发该事件发生并返回相应信息。 |
| callback | AsyncCallback<void> | 是 | 回调函数，用于获取相关信息。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. function callback(err: BusinessError): void {
4. if (err !== undefined && err.code !== 0) {
5. console.error(`Callback Error, errorCode: ${err.code}`);
6. return;
7. }
8. console.info(`photo capture ready`);
9. }

11. function registerPhotoOutputCaptureReady(photoOutput: camera.PhotoOutput): void {
12. photoOutput.on('captureReady', callback);
13. }
```

## off('captureReady')12+

PhonePC/2in1TabletTVWearable

off(type: 'captureReady', callback?: AsyncCallback<void>): void

注销监听可拍下一张。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'captureReady'，photoOutput创建成功后可监听。 |
| callback | AsyncCallback<void> | 否 | 回调函数，如果指定参数则取消对应callback（callback对象不可是匿名函数），否则取消所有callback。 |

**示例：**

```
1. function unregisterPhotoOutputCaptureReady(photoOutput: camera.PhotoOutput): void {
2. photoOutput.off('captureReady');
3. }
```

## on('estimatedCaptureDuration')12+

PhonePC/2in1TabletTVWearable

on(type: 'estimatedCaptureDuration', callback: AsyncCallback<number>): void

监听预估的拍照时间，通过注册回调函数获取结果。使用callback异步回调。

说明

当前注册监听接口，不支持在on监听的回调方法里，调用off注销回调。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'estimatedCaptureDuration'，photoOutput创建成功后可监听。拍照完全结束可触发该事件发生并返回相应信息。 |
| callback | AsyncCallback<number> | 是 | 回调函数，用于获取预估的单次拍照底层出sensor采集帧时间，单位：毫秒。如果上报-1，代表没有预估时间。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. function callback(err: BusinessError, duration: number): void {
4. if (err !== undefined && err.code !== 0) {
5. console.error(`Callback Error, errorCode: ${err.code}`);
6. return;
7. }
8. console.info(`photo estimated capture duration : ${duration}`);
9. }

11. function registerPhotoOutputEstimatedCaptureDuration(photoOutput: camera.PhotoOutput): void {
12. photoOutput.on('estimatedCaptureDuration', callback);
13. }
```

## off('estimatedCaptureDuration')12+

PhonePC/2in1TabletTVWearable

off(type: 'estimatedCaptureDuration', callback?: AsyncCallback<number>): void

注销监听预估的拍照时间。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'estimatedCaptureDuration'，photoOutput创建成功后可监听。 |
| callback | AsyncCallback<number> | 否 | 回调函数，如果指定参数则取消对应callback（callback对象不可是匿名函数），否则取消所有callback。 |

**示例：**

```
1. function unregisterPhotoOutputEstimatedCaptureDuration(photoOutput: camera.PhotoOutput): void {
2. photoOutput.off('estimatedCaptureDuration');
3. }
```

## on('error')

PhonePC/2in1TabletTVWearable

on(type: 'error', callback: ErrorCallback): void

监听拍照输出发生错误，通过注册回调函数获取结果。使用callback异步回调。

说明

当前注册监听接口，不支持在on监听的回调方法里，调用off注销回调。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'error'，photoOutput创建成功后可监听。拍照接口调用时出现错误触发该事件并返回错误信息。 |
| callback | [ErrorCallback](js-apis-base.md#errorcallback) | 是 | 回调函数，用于获取错误信息。返回错误码，错误码类型[CameraErrorCode](arkts-apis-camera-e.md#cameraerrorcode)。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. function callback(err: BusinessError): void {
4. console.error(`Photo output error code: ${err.code}`);
5. }

7. function registerPhotoOutputError(photoOutput: camera.PhotoOutput): void {
8. photoOutput.on('error', callback);
9. }
```

## off('error')

PhonePC/2in1TabletTVWearable

off(type: 'error', callback?: ErrorCallback): void

注销监听拍照输出发生错误。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'error'，photoOutput创建成功后可监听。 |
| callback | [ErrorCallback](js-apis-base.md#errorcallback) | 否 | 回调函数，如果指定参数则取消对应callback（callback对象不可是匿名函数），否则取消所有callback。 |

**示例：**

```
1. function unregisterPhotoOutputError(photoOutput: camera.PhotoOutput): void {
2. photoOutput.off('error');
3. }
```

## getActiveProfile12+

PhonePC/2in1TabletTVWearable

getActiveProfile(): Profile

获取当前生效的配置信息。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Profile](arkts-apis-camera-i.md#profile) | 当前生效的配置信息 |

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](errorcode-camera.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400201 | Camera service fatal error. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. function testGetActiveProfile(photoOutput: camera.PhotoOutput): camera.Profile | undefined {
4. let activeProfile: camera.Profile | undefined = undefined;
5. try {
6. activeProfile = photoOutput.getActiveProfile();
7. } catch (error) {
8. // 失败返回错误码error.code并处理。
9. let err = error as BusinessError;
10. console.error(`The photoOutput.getActiveProfile call failed. error code: ${err.code}`);
11. }
12. return activeProfile;
13. }
```

## getPhotoRotation12+

PhonePC/2in1TabletTVWearable

getPhotoRotation(deviceDegree?: number): ImageRotation

获取拍照旋转角度。

* 设备自然方向：设备默认使用方向。例如，直板机默认使用方向为竖屏（充电口向下）。
* 相机镜头角度：值等于相机图像顺时针旋转到设备自然方向的角度。例如，直板机后置相机传感器是横屏安装的，所以需要顺时针旋转90度到设备自然方向。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceDegree | number | 否 | 设备旋转角度，单位度，取值范围：[0, 360]。  若入参超过该范围，则取入参除以360的余数。  从API version 23开始，入参deviceDegree为可选参数，当不传入参数时，由系统获取deviceDegree进行拍照旋转角度计算。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ImageRotation](arkts-apis-camera-e.md#imagerotation) | 返回拍照旋转角度。若接口调用失败，返回undefined。 |

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](errorcode-camera.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400201 | Camera service fatal error. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. function testGetPhotoRotation(photoOutput: camera.PhotoOutput, deviceDegree : number): camera.ImageRotation {
4. let photoRotation: camera.ImageRotation = camera.ImageRotation.ROTATION_0;
5. try {
6. photoRotation = photoOutput.getPhotoRotation(deviceDegree);
7. console.info(`Photo rotation is: ${photoRotation}`);
8. } catch (error) {
9. // 失败返回错误码error.code并处理。
10. let err = error as BusinessError;
11. console.error(`The photoOutput.getPhotoRotation call failed. error code: ${err.code}`);
12. }
13. return photoRotation;
14. }

16. function testGetPhotoRotationWithOutParam(photoOutput: camera.PhotoOutput): camera.ImageRotation {
17. let photoRotation: camera.ImageRotation = camera.ImageRotation.ROTATION_0;
18. try {
19. photoRotation = photoOutput.getPhotoRotation();
20. console.info(`Photo rotation is: ${photoRotation}`);
21. } catch (error) {
22. // 失败返回错误码error.code并处理。
23. let err = error as BusinessError;
24. console.error(`The photoOutput.testGetPhotoRotationWithOutParam call failed. error code: ${err.code}`);
25. }
26. return photoRotation;
27. }
```

## on('captureStart')(deprecated)

PhonePC/2in1TabletTVWearable

on(type: 'captureStart', callback: AsyncCallback<number>): void

监听拍照开始，通过注册回调函数获取Capture ID。使用callback异步回调。

说明

从 API version 10开始支持，从API version 11开始废弃。建议使用[on('captureStartWithInfo')](arkts-apis-camera-photooutput.md#oncapturestartwithinfo11)替代。

当前注册监听接口，不支持在on监听的回调方法里，调用off注销回调。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'captureStart'，photoOutput创建成功后可监听。每次拍照，底层开始曝光时触发该事件并返回。 |
| callback | AsyncCallback<number> | 是 | 使用callback的方式获取Capture ID。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. function callback(err: BusinessError, captureId: number): void {
4. if (err !== undefined && err.code !== 0) {
5. console.error(`Callback Error, errorCode: ${err.code}`);
6. return;
7. }
8. console.info(`photo capture started, captureId : ${captureId}`);
9. }

11. function registerPhotoOutputCaptureStart(photoOutput: camera.PhotoOutput): void {
12. photoOutput.on('captureStart', callback);
13. }
```

## off('captureStart')(deprecated)

PhonePC/2in1TabletTVWearable

off(type: 'captureStart', callback?: AsyncCallback<number>): void

注销拍照开始的监听。

说明

从 API version 10开始支持，从API version 11开始废弃。建议使用[off('captureStartWithInfo')](arkts-apis-camera-photooutput.md#offcapturestartwithinfo11)替代。

当前注册监听接口，不支持在on监听的回调方法里，调用off注销回调。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'captureStart'，photoOutput创建成功后可监听。 |
| callback | AsyncCallback<number> | 否 | 回调函数，如果指定参数则取消对应callback（callback对象不可是匿名函数），否则取消所有callback。 |

**示例：**

```
1. function unregisterPhotoOutputCaptureStart(photoOutput: camera.PhotoOutput): void {
2. photoOutput.off('captureStart');
3. }
```

## isPhotoQualityPrioritizationSupported21+

PhonePC/2in1TabletTVWearable

isPhotoQualityPrioritizationSupported(qualityPrioritization: PhotoQualityPrioritization): boolean

检查是否支持指定的拍照画质优先策略。

**元服务API：** 从API version 21开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| qualityPrioritization | [PhotoQualityPrioritization](arkts-apis-camera-e.md#photoqualityprioritization21) | 是 | 要检查的拍照画质优先策略。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 是否支持指定的拍照画质优先策略。true表示支持，false表示不支持。 |

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](errorcode-camera.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400201 | Camera service fatal error, reconfiguring streams is needed to recover from failure. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { camera } from '@kit.CameraKit';

4. let photoOutput: camera.PhotoOutput;

6. function isPhotoQualityPrioritizationSupported(qualityPrioritization: camera.PhotoQualityPrioritization): boolean {
7. let isSupported: boolean = false;
8. try {
9. isSupported = photoOutput.isPhotoQualityPrioritizationSupported(qualityPrioritization);
10. } catch (error) {
11. let err = error as BusinessError;
12. console.error(`The isPhotoQualityPrioritizationSupported call failed. error code: ${err.code}`);
13. }
14. return isSupported;
15. }
```

## setPhotoQualityPrioritization21+

PhonePC/2in1TabletTVWearable

setPhotoQualityPrioritization(qualityPrioritization: PhotoQualityPrioritization): void

设置拍照画质优先策略。

设置之前，可先使用方法[isPhotoQualityPrioritizationSupported](arkts-apis-camera-photooutput.md#isphotoqualityprioritizationsupported21)对设备是否支持指定的拍照画质优先策略进行检查。

**元服务API：** 从API version 21开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| qualityPrioritization | [PhotoQualityPrioritization](arkts-apis-camera-e.md#photoqualityprioritization21) | 是 | 要设置的拍照画质优先策略。 |

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](errorcode-camera.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400102 | Operation not allowed. |
| 7400201 | Camera service fatal error, reconfiguring streams is needed to recover from failure. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { camera } from '@kit.CameraKit';

4. let photoOutput: camera.PhotoOutput;

6. function setPhotoQualityPrioritization(qualityPrioritization: camera.PhotoQualityPrioritization): void {
7. try {
8. photoOutput.setPhotoQualityPrioritization(qualityPrioritization);
9. } catch (error) {
10. let err = error as BusinessError;
11. console.error(`The setPhotoQualityPrioritization call failed. error code: ${err.code}`);
12. }
13. }
```
