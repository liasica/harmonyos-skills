---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-camera-previewoutput
title: Interface (PreviewOutput)
breadcrumb: API参考 > 媒体 > Camera Kit（相机服务） > ArkTS API > @ohos.multimedia.camera (相机管理) > Interface (PreviewOutput)
category: harmonyos-references
scraped_at: 2026-04-28T08:12:39+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:2abcd8a36d691f880ef3da282a1a61a0d4ab798e707850579c8fa9348cc3d2ad
---

预览输出类。继承[CameraOutput](arkts-apis-camera-cameraoutput.md)。

说明

本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { camera } from '@kit.CameraKit';
```

## on('frameStart')

PhonePC/2in1TabletTVWearable

on(type: 'frameStart', callback: AsyncCallback<void>): void

监听预览帧启动，通过注册回调函数获取结果。使用callback异步回调。

说明

当前注册监听接口，不支持在on监听的回调方法里，调用off注销回调。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'frameStart'，previewOutput创建成功可监听。底层第一次开始曝光时触发该事件并返回。 |
| callback | AsyncCallback<void> | 是 | 回调函数，用于获取结果。只要有该事件返回就证明预览开始。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. function callback(err: BusinessError): void {
4. if (err !== undefined && err.code !== 0) {
5. console.error(`Callback Error, errorCode: ${err.code}`);
6. return;
7. }
8. console.info('Preview frame started');
9. }

11. function registerPreviewOutputFrameStart(previewOutput: camera.PreviewOutput): void {
12. previewOutput.on('frameStart', callback);
13. }
```

## off('frameStart')

PhonePC/2in1TabletTVWearable

off(type: 'frameStart', callback?: AsyncCallback<void>): void

注销预览帧启动的监听。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'frameStart'，previewOutput创建成功可监听。 |
| callback | AsyncCallback<void> | 否 | 回调函数，如果指定参数则取消对应callback（callback对象不可是匿名函数），否则取消所有callback。 |

**示例：**

```
1. function unregisterPreviewOutputFrameStart(previewOutput: camera.PreviewOutput): void {
2. previewOutput.off('frameStart');
3. }
```

## on('frameEnd')

PhonePC/2in1TabletTVWearable

on(type: 'frameEnd', callback: AsyncCallback<void>): void

监听预览帧结束，通过注册回调函数获取结果。使用callback异步回调。

说明

当前注册监听接口，不支持在on监听的回调方法里，调用off注销回调。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'frameEnd'，previewOutput创建成功可监听。预览完全结束最后一帧时触发该事件并返回。 |
| callback | AsyncCallback<void> | 是 | 回调函数，用于获取结果。只要有该事件返回就证明预览结束。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. function callback(err: BusinessError): void {
4. if (err !== undefined && err.code !== 0) {
5. console.error(`Callback Error, errorCode: ${err.code}`);
6. return;
7. }
8. console.info('Preview frame ended');
9. }

11. function registerPreviewOutputFrameEnd(previewOutput: camera.PreviewOutput): void {
12. previewOutput.on('frameEnd', callback);
13. }
```

## off('frameEnd')

PhonePC/2in1TabletTVWearable

off(type: 'frameEnd', callback?: AsyncCallback<void>): void

注销监听预览帧结束。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'frameEnd'，previewOutput创建成功可监听。 |
| callback | AsyncCallback<void> | 否 | 回调函数，如果指定参数则取消对应callback（callback对象不可是匿名函数），否则取消所有callback。 |

**示例：**

```
1. function unregisterPreviewOutputFrameEnd(previewOutput: camera.PreviewOutput): void {
2. previewOutput.off('frameEnd');
3. }
```

## on('error')

PhonePC/2in1TabletTVWearable

on(type: 'error', callback: ErrorCallback): void

监听预览输出的错误事件，通过注册回调函数获取结果。使用callback异步回调。

说明

当前注册监听接口，不支持在on监听的回调方法里，调用off注销回调。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'error'，previewOutput创建成功可监听。预览接口使用错误时触发该事件，比如调用[Session.start](arkts-apis-camera-session.md#start11-1)，[CameraOutput.release](arkts-apis-camera-cameraoutput.md#release-1)等接口发生错误时返回对应错误信息。 |
| callback | [ErrorCallback](js-apis-base.md#errorcallback) | 是 | 回调函数，用于获取错误信息。返回错误码，错误码类型[CameraErrorCode](arkts-apis-camera-e.md#cameraerrorcode)。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. function callback(previewOutputError: BusinessError): void {
4. console.error(`Preview output error code: ${previewOutputError.code}`);
5. }

7. function registerPreviewOutputError(previewOutput: camera.PreviewOutput): void {
8. previewOutput.on('error', callback)
9. }
```

## off('error')

PhonePC/2in1TabletTVWearable

off(type: 'error', callback?: ErrorCallback): void

注销监听预览输出的错误事件。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'error'，previewOutput创建成功可监听。 |
| callback | [ErrorCallback](js-apis-base.md#errorcallback) | 否 | 回调函数，如果指定参数则取消对应callback（callback对象不可是匿名函数），否则取消所有callback。 |

**示例：**

```
1. function unregisterPreviewOutputError(previewOutput: camera.PreviewOutput): void {
2. previewOutput.off('error');
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
1. function getSupportedFrameRates(previewOutput: camera.PreviewOutput): Array<camera.FrameRateRange> {
2. let supportedFrameRatesArray: Array<camera.FrameRateRange> = previewOutput.getSupportedFrameRates();
3. return supportedFrameRatesArray;
4. }
```

## setFrameRate12+

PhonePC/2in1TabletTVWearable

setFrameRate(minFps: number, maxFps: number): void

设置预览流帧率范围，设置的范围必须在支持的帧率范围内。

进行设置前，可通过[getSupportedFrameRates](arkts-apis-camera-previewoutput.md#getsupportedframerates12)接口查询支持的帧率范围。

说明

仅在[PhotoSession](arkts-apis-camera-photosession.md)或[VideoSession](arkts-apis-camera-videosession.md)模式下支持。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| minFps | number | 是 | 最小帧率（单位：fps），当传入的最大值小于最小值时，传参异常，接口不生效。 |
| maxFps | number | 是 | 最大帧率（单位：fps），当传入的最小值大于最大值时，传参异常，接口不生效。 |

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](errorcode-camera.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400101 | Parameter missing or parameter type incorrect. |
| 7400110 | Unresolved conflicts with current configurations. |

**示例：**

```
1. function setFrameRateRange(previewOutput: camera.PreviewOutput, frameRateRange: Array<number>): void {
2. previewOutput.setFrameRate(frameRateRange[0], frameRateRange[1]);
3. }
```

## getActiveFrameRate12+

PhonePC/2in1TabletTVWearable

getActiveFrameRate(): FrameRateRange

获取已设置的帧率范围。

使用[setFrameRate](arkts-apis-camera-previewoutput.md#setframerate12)接口对预览流设置过帧率后可查询。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [FrameRateRange](arkts-apis-camera-i.md#frameraterange) | 帧率范围 |

**示例：**

```
1. function getActiveFrameRate(previewOutput: camera.PreviewOutput): camera.FrameRateRange {
2. let activeFrameRate: camera.FrameRateRange = previewOutput.getActiveFrameRate();
3. return activeFrameRate;
4. }
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

3. function testGetActiveProfile(previewOutput: camera.PreviewOutput): camera.Profile | undefined {
4. let activeProfile: camera.Profile | undefined = undefined;
5. try {
6. activeProfile = previewOutput.getActiveProfile();
7. } catch (error) {
8. // 失败返回错误码error.code并处理。
9. let err = error as BusinessError;
10. console.error(`The previewOutput.getActiveProfile call failed. error code: ${err.code}`);
11. }
12. return activeProfile;
13. }
```

## getPreviewRotation12+

PhonePC/2in1TabletTVWearable

getPreviewRotation(displayRotation?: number): ImageRotation

获取预览旋转角度。

* 设备自然方向：设备默认使用方向。例如，直板机默认使用方向为竖屏（充电口向下）。
* 相机镜头角度：值等于相机图像顺时针旋转到设备自然方向的角度。例如，直板机后置相机传感器是横屏安装的，所以需要顺时针旋转90度到设备自然方向。
* [屏幕旋转角度](../best-practices/bpta-multi-device-window-direction.md#section15598121101615)：显示设备的屏幕顺时针旋转角度。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| displayRotation | number | 否 | 显示设备的屏幕旋转角度，通过[display.getDefaultDisplaySync](js-apis-display.md#displaygetdefaultdisplaysync9)获得。  从API version 23开始，入参displayRotation为可选参数，当不传入参数时，由系统获取displayRotation进行预览旋转角度计算。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ImageRotation](arkts-apis-camera-e.md#imagerotation) | 返回预览旋转角度。若接口调用失败，返回undefined。 |

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](errorcode-camera.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400201 | Camera service fatal error. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. function testGetPreviewRotation(previewOutput: camera.PreviewOutput, imageRotation : camera.ImageRotation): camera.ImageRotation {
4. let previewRotation: camera.ImageRotation = camera.ImageRotation.ROTATION_0;
5. try {
6. previewRotation = previewOutput.getPreviewRotation(imageRotation);
7. console.info(`Preview rotation is: ${previewRotation}`);
8. } catch (error) {
9. // 失败返回错误码error.code并处理。
10. let err = error as BusinessError;
11. console.error(`The previewOutput.getPreviewRotation call failed. error code: ${err.code}`);
12. }
13. return previewRotation;
14. }

16. function testGetPreviewRotationWithOutParam(previewOutput: camera.PreviewOutput): camera.ImageRotation {
17. let previewRotation: camera.ImageRotation = camera.ImageRotation.ROTATION_0;
18. try {
19. previewRotation = previewOutput.getPreviewRotation();
20. console.info(`Preview rotation is: ${previewRotation}`);
21. } catch (error) {
22. // 失败返回错误码error.code并处理。
23. let err = error as BusinessError;
24. console.error(`The previewOutput.testGetPreviewRotationWithOutParam call failed. error code: ${err.code}`);
25. }
26. return previewRotation;
27. }
```

## setPreviewRotation12+

PhonePC/2in1TabletTVWearable

setPreviewRotation(previewRotation: ImageRotation, isDisplayLocked?: boolean): void

设置预览旋转角度。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| previewRotation | [ImageRotation](arkts-apis-camera-e.md#imagerotation) | 是 | 预览旋转角度 |
| isDisplayLocked | boolean | 否 | Surface在屏幕旋转时是否锁定方向，未设置时默认取值为false，即不锁定方向。true表示锁定方向，false表示不锁定方向。详情请参考[SurfaceRotationOptions](ts-basic-components-xcomponent.md#surfacerotationoptions12对象说明) |

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](errorcode-camera.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400101 | Parameter missing or parameter type incorrect. |
| 7400201 | Camera service fatal error. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. function testSetPreviewRotation(previewOutput: camera.PreviewOutput, previewRotation : camera.ImageRotation, isDisplayLocked: boolean): void {
4. try {
5. previewOutput.setPreviewRotation(previewRotation, isDisplayLocked);
6. } catch (error) {
7. // 失败返回错误码error.code并处理。
8. let err = error as BusinessError;
9. console.error(`The previewOutput.setPreviewRotation call failed. error code: ${err.code}`);
10. }
11. return;
12. }
```

## start(deprecated)

PhonePC/2in1TabletTVWearable

start(callback: AsyncCallback<void>): void

开始输出预览流，通过注册回调函数获取结果。使用callback异步回调。

说明

从 API version 10开始支持，从API version 11开始废弃。建议使用[Session.start](arkts-apis-camera-session.md#start11)替代。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<void> | 是 | 回调函数。当开始输出预览流成功，err为undefined，否则为错误对象。错误码类型[CameraErrorCode](arkts-apis-camera-e.md#cameraerrorcode)。 |

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](errorcode-camera.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400103 | Session not config. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. function startPreviewOutput(previewOutput: camera.PreviewOutput): void {
4. previewOutput.start((err: BusinessError) => {
5. if (err) {
6. console.error(`Failed to start the preview output, error code: ${err.code}.`);
7. return;
8. }
9. console.info('Callback returned with preview output started.');
10. });
11. }
```

## start(deprecated)

PhonePC/2in1TabletTVWearable

start(): Promise<void>

开始输出预览流。使用Promise异步回调。

说明

从 API version 10开始支持，从API version 11开始废弃。建议使用[Session.start](arkts-apis-camera-session.md#start11-1)替代。

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

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. function startPreviewOutput(previewOutput: camera.PreviewOutput): void {
4. previewOutput.start().then(() => {
5. console.info('Promise returned with preview output started.');
6. }).catch((error: BusinessError) => {
7. console.error(`Failed to preview output start, error code: ${error.code}.`);
8. });
9. }
```

## stop(deprecated)

PhonePC/2in1TabletTVWearable

stop(callback: AsyncCallback<void>): void

停止输出预览流，通过注册回调函数获取结果。使用callback异步回调。

说明

从 API version 10开始支持，从API version 11开始废弃。建议使用[Session.stop](arkts-apis-camera-session.md#stop11)替代。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<void> | 是 | 回调函数。当停止输出预览流成功，err为undefined，否则为错误对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. function stopPreviewOutput(previewOutput: camera.PreviewOutput): void {
4. previewOutput.stop((err: BusinessError) => {
5. if (err) {
6. console.error(`Failed to stop the preview output, error code: ${err.code}.`);
7. return;
8. }
9. console.info('Returned with preview output stopped.');
10. })
11. }
```

## stop(deprecated)

PhonePC/2in1TabletTVWearable

stop(): Promise<void>

停止输出预览流。使用Promise异步回调。

说明

从 API version 10开始支持，从API version 11开始废弃。建议使用[Session.stop](arkts-apis-camera-session.md#stop11-1)替代。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. function stopPreviewOutput(previewOutput: camera.PreviewOutput): void {
4. previewOutput.stop().then(() => {
5. console.info('Callback returned with preview output stopped.');
6. }).catch((error: BusinessError) => {
7. console.error(`Failed to preview output stop, error code: ${error.code}.`);
8. });
9. }
```

## isBandwidthCompressionSupported23+

PhonePC/2in1TabletTVWearable

isBandwidthCompressionSupported(): boolean

检查是否支持预览带宽压缩（指通过编码减少数据量，降低其在传输链路中的带宽占用）。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 是否支持预览带宽压缩。true表示支持，false表示不支持。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. function isBandwidthCompressionSupported(previewOutput: camera.PreviewOutput): boolean {
4. let supported: boolean = false;
5. try {
6. supported = previewOutput.isBandwidthCompressionSupported();
7. } catch (error) {
8. // 失败返回错误码error.code并处理。
9. let err = error as BusinessError;
10. console.error(`The previewOutput.isBandwidthCompressionSupported call failed. error code: ${err.code}`);
11. }
12. return supported;
13. }
```

## enableBandwidthCompression23+

PhonePC/2in1TabletTVWearable

enableBandwidthCompression(enabled: boolean): void

使能预览带宽压缩。

使能之前，可先使用方法[isBandwidthCompressionSupported](arkts-apis-camera-previewoutput.md#isbandwidthcompressionsupported23)对设备是否支持预览带宽压缩进行检查。

说明

该接口只能在使用[Session.commitConfig](arkts-apis-camera-session.md#commitconfig11)接口之前调用，否则会影响预览流出流格式。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enabled | boolean | 是 | 是否使能预览带宽压缩。true表示使能，false表示不使能。 |

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](errorcode-camera.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400102 | Operation not allowed. |
| 7400103 | Session not config. |
| 7400201 | Camera service fatal error. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. function enableBandwidthCompression(previewOutput: camera.PreviewOutput, enabled: boolean): void {
4. try {
5. previewOutput.enableBandwidthCompression(enabled);
6. } catch (error) {
7. // 失败返回错误码error.code并处理。
8. let err = error as BusinessError;
9. console.error(`The previewOutput.enableBandwidthCompression call failed. error code: ${err.code}`);
10. }
11. }
```
