---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-camera-capturesession
title: 废弃的Interface (CaptureSession, deprecated)
breadcrumb: API参考 > 媒体 > Camera Kit（相机服务） > ArkTS API > @ohos.multimedia.camera (相机管理) > 废弃的Interface (CaptureSession, deprecated)
category: harmonyos-references
scraped_at: 2026-04-28T08:12:42+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:73295d167a8b87013ce5389d5ba6c8f3413b57771072c3d7481c941f7ec3e793
---

拍照会话类，保存一次相机运行所需要的所有资源[CameraInput](arkts-apis-camera-camerainput.md)、[CameraOutput](arkts-apis-camera-cameraoutput.md)，并向相机设备申请完成相机功能(录像，拍照)。

说明

从 API version 10开始支持，从API version 11开始废弃。建议使用[PhotoSession](arkts-apis-camera-photosession.md)、[VideoSession](arkts-apis-camera-videosession.md)替代。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { camera } from '@kit.CameraKit';
```

## beginConfig(deprecated)

PhonePC/2in1TabletTVWearable

beginConfig(): void

开始配置会话。

说明

从 API version 10开始支持，从API version 11开始废弃。建议使用[Session.beginConfig](arkts-apis-camera-session.md#beginconfig11)替代。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](errorcode-camera.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400105 | Session config locked. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. function beginConfig(captureSession: camera.CaptureSession): void {
4. try {
5. captureSession.beginConfig();
6. } catch (error) {
7. // 失败返回错误码error.code并处理。
8. let err = error as BusinessError;
9. console.error(`The beginConfig call failed. error code: ${err.code}`);
10. }
11. }
```

## commitConfig(deprecated)

PhonePC/2in1TabletTVWearable

commitConfig(callback: AsyncCallback<void>): void

提交配置信息，通过注册回调函数获取结果。使用callback异步回调。

说明

从 API version 10开始支持，从API version 11开始废弃。建议使用[Session.commitConfig](arkts-apis-camera-session.md#commitconfig11)替代。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<void> | 是 | 回调函数。当提交配置信息成功，err为undefined，否则为错误对象。错误码类型[CameraErrorCode](arkts-apis-camera-e.md#cameraerrorcode) |

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](errorcode-camera.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400102 | Operation not allowed. |
| 7400201 | Camera service fatal error. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. function commitConfig(captureSession: camera.CaptureSession): void {
4. captureSession.commitConfig((err: BusinessError) => {
5. if (err) {
6. console.error(`The commitConfig call failed. error code: ${err.code}`);
7. return;
8. }
9. console.info('Callback invoked to indicate the commit config success.');
10. });
11. }
```

## commitConfig(deprecated)

PhonePC/2in1TabletTVWearable

commitConfig(): Promise<void>

提交配置信息。使用Promise异步回调。

说明

从 API version 10开始支持，从API version 11开始废弃。建议使用[Session.commitConfig](arkts-apis-camera-session.md#commitconfig11-1)替代。

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
| 7400201 | Camera service fatal error. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. function commitConfig(captureSession: camera.CaptureSession): void {
4. captureSession.commitConfig().then(() => {
5. console.info('Promise returned to indicate the commit config success.');
6. }).catch((error: BusinessError) => {
7. // 失败返回错误码error.code并处理。
8. console.error(`The commitConfig call failed. error code: ${error.code}`);
9. });
10. }
```

## addInput(deprecated)

PhonePC/2in1TabletTVWearable

addInput(cameraInput: CameraInput): void

把[CameraInput](arkts-apis-camera-camerainput.md)加入到会话。

说明

从 API version 10开始支持，从API version 11开始废弃。建议使用[Session.addInput](arkts-apis-camera-session.md#addinput11)替代。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| cameraInput | [CameraInput](arkts-apis-camera-camerainput.md) | 是 | 需要添加的CameraInput实例。 |

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](errorcode-camera.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400101 | Parameter missing or parameter type incorrect. |
| 7400102 | Operation not allowed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. function addInput(captureSession: camera.CaptureSession, cameraInput: camera.CameraInput): void {
4. try {
5. captureSession.addInput(cameraInput);
6. } catch (error) {
7. // 失败返回错误码error.code并处理。
8. let err = error as BusinessError;
9. console.error(`The addInput call failed. error code: ${err.code}`);
10. }
11. }
```

## removeInput(deprecated)

PhonePC/2in1TabletTVWearable

removeInput(cameraInput: CameraInput): void

移除[CameraInput](arkts-apis-camera-camerainput.md)。

说明

从 API version 10开始支持，从API version 11开始废弃。建议使用[Session.removeInput](arkts-apis-camera-session.md#removeinput11)替代。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| cameraInput | [CameraInput](arkts-apis-camera-camerainput.md) | 是 | 需要移除的CameraInput实例。 |

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](errorcode-camera.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400101 | Parameter missing or parameter type incorrect. |
| 7400102 | Operation not allowed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. function removeInput(captureSession: camera.CaptureSession, cameraInput: camera.CameraInput): void {
4. try {
5. captureSession.removeInput(cameraInput);
6. } catch (error) {
7. // 失败返回错误码error.code并处理。
8. let err = error as BusinessError;
9. console.error(`The removeInput call failed. error code: ${err.code}`);
10. }
11. }
```

## addOutput(deprecated)

PhonePC/2in1TabletTVWearable

addOutput(cameraOutput: CameraOutput): void

把[CameraOutput](arkts-apis-camera-cameraoutput.md)加入到会话。

说明

从 API version 10开始支持，从API version 11开始废弃。建议使用[Session.addOutput](arkts-apis-camera-session.md#addoutput11)替代。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| cameraOutput | [CameraOutput](arkts-apis-camera-cameraoutput.md) | 是 | 需要添加的CameraOutput实例。 |

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](errorcode-camera.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400101 | Parameter missing or parameter type incorrect. |
| 7400102 | Operation not allowed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. function addOutput(captureSession: camera.CaptureSession, cameraOutput: camera.CameraOutput): void {
4. try {
5. captureSession.addOutput(cameraOutput);
6. } catch (error) {
7. // 失败返回错误码error.code并处理。
8. let err = error as BusinessError;
9. console.error(`The addOutput call failed. error code: ${err.code}`);
10. }
11. }
```

## removeOutput(deprecated)

PhonePC/2in1TabletTVWearable

removeOutput(cameraOutput: CameraOutput): void

从会话中移除[CameraOutput](arkts-apis-camera-cameraoutput.md)。

说明

从 API version 10开始支持，从API version 11开始废弃。建议使用[Session.removeOutput](arkts-apis-camera-session.md#removeoutput11)替代。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| cameraOutput | [CameraOutput](arkts-apis-camera-cameraoutput.md) | 是 | 需要移除的CameraOutput实例。 |

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](errorcode-camera.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400101 | Parameter missing or parameter type incorrect. |
| 7400102 | Operation not allowed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. function removeOutput(captureSession: camera.CaptureSession, previewOutput: camera.PreviewOutput): void {
4. try {
5. captureSession.removeOutput(previewOutput);
6. } catch (error) {
7. // 失败返回错误码error.code并处理。
8. let err = error as BusinessError;
9. console.error(`The removeOutput call failed. error code: ${err.code}`);
10. }
11. }
```

## start(deprecated)

PhonePC/2in1TabletTVWearable

start(callback: AsyncCallback<void>): void

开始会话工作，通过注册回调函数获取结果。使用callback异步回调。

说明

从 API version 10开始支持，从API version 11开始废弃。建议使用[Session.start](arkts-apis-camera-session.md#start11)替代。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<void> | 是 | 回调函数。当开始会话工作成功，err为undefined，否则为错误对象。错误码类型[CameraErrorCode](arkts-apis-camera-e.md#cameraerrorcode)。 |

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](errorcode-camera.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400103 | Session not config. |
| 7400201 | Camera service fatal error. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. function startCaptureSession(captureSession: camera.CaptureSession): void {
4. captureSession.start((err: BusinessError) => {
5. if (err) {
6. console.error(`Failed to start the session, error code: ${err.code}.`);
7. return;
8. }
9. console.info('Callback invoked to indicate the session start success.');
10. });
11. }
```

## start(deprecated)

PhonePC/2in1TabletTVWearable

start(): Promise<void>

开始会话工作。使用Promise异步回调。

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
| 7400201 | Camera service fatal error. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. function startCaptureSession(captureSession: camera.CaptureSession): void {
4. captureSession.start().then(() => {
5. console.info('Promise returned to indicate the session start success.');
6. }).catch((err: BusinessError) => {
7. console.error(`Failed to start the session, error code: ${err.code}.`);
8. });
9. }
```

## stop(deprecated)

PhonePC/2in1TabletTVWearable

stop(callback: AsyncCallback<void>): void

停止会话工作，通过注册回调函数获取结果。使用callback异步回调。

说明

从 API version 10开始支持，从API version 11开始废弃。建议使用[Session.stop](arkts-apis-camera-session.md#stop11)替代。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<void> | 是 | 回调函数。当停止会话工作成功，err为undefined，否则为错误对象。错误码类型[CameraErrorCode](arkts-apis-camera-e.md#cameraerrorcode)。 |

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](errorcode-camera.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400201 | Camera service fatal error. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. function stopCaptureSession(captureSession: camera.CaptureSession): void {
4. captureSession.stop((err: BusinessError) => {
5. if (err) {
6. console.error(`Failed to stop the session, error code: ${err.code}.`);
7. return;
8. }
9. console.info('Callback invoked to indicate the session stop success.');
10. });
11. }
```

## stop(deprecated)

PhonePC/2in1TabletTVWearable

stop(): Promise<void>

停止会话工作。使用Promise异步回调。

说明

从 API version 10开始支持，从API version 11开始废弃。建议使用[Session.stop](arkts-apis-camera-session.md#stop11-1)替代。

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

3. function stopCaptureSession(captureSession: camera.CaptureSession): void {
4. captureSession.stop().then(() => {
5. console.info('Promise returned to indicate the session stop success.');
6. }).catch((err: BusinessError) => {
7. console.error(`Failed to stop the session, error code: ${err.code}.`);
8. });
9. }
```

## release(deprecated)

PhonePC/2in1TabletTVWearable

release(callback: AsyncCallback<void>): void

释放会话资源，通过注册回调函数获取结果。使用callback异步回调。

说明

从 API version 10开始支持，从API version 11开始废弃。建议使用[Session.release](arkts-apis-camera-session.md#release11)替代。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<void> | 是 | 回调函数。当释放会话资源成功，err为undefined，否则为错误对象。错误码类型[CameraErrorCode](arkts-apis-camera-e.md#cameraerrorcode)。 |

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](errorcode-camera.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400201 | Camera service fatal error. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. function releaseCaptureSession(captureSession: camera.CaptureSession): void {
4. captureSession.release((err: BusinessError) => {
5. if (err) {
6. console.error(`Failed to release the CaptureSession instance, error code: ${err.code}.`);
7. return;
8. }
9. console.info('Callback invoked to indicate that the CaptureSession instance is released successfully.');
10. });
11. }
```

## release(deprecated)

PhonePC/2in1TabletTVWearable

release(): Promise<void>

释放会话资源。使用Promise异步回调。

说明

从 API version 10开始支持，从API version 11开始废弃。建议使用[Session.release](arkts-apis-camera-session.md#release11-1)替代。

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

3. function releaseCaptureSession(captureSession: camera.CaptureSession): void {
4. captureSession.release().then(() => {
5. console.info('Promise returned to indicate that the CaptureSession instance is released successfully.');
6. }).catch((err: BusinessError) => {
7. console.error(`Failed to release the CaptureSession instance, error code: ${err.code}.`);
8. });
9. }
```

## hasFlash(deprecated)

PhonePC/2in1TabletTVWearable

hasFlash(): boolean

检测是否有闪光灯。

说明

从 API version 10开始支持，从API version 11开始废弃。建议使用[Flash.hasFlash](arkts-apis-camera-flashquery.md#hasflash11)替代。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 设备支持闪光灯。true表示支持，false表示不支持。接口调用失败会返回相应错误码，错误码类型[CameraErrorCode](arkts-apis-camera-e.md#cameraerrorcode)。 |

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](errorcode-camera.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400103 | Session not config. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. function hasFlash(captureSession: camera.CaptureSession): boolean {
4. let status: boolean = false;
5. try {
6. status = captureSession.hasFlash();
7. } catch (error) {
8. // 失败返回错误码error.code并处理。
9. let err = error as BusinessError;
10. console.error(`The hasFlash call failed. error code: ${err.code}`);
11. }
12. return status;
13. }
```

## isFlashModeSupported(deprecated)

PhonePC/2in1TabletTVWearable

isFlashModeSupported(flashMode: FlashMode): boolean

检测闪光灯模式是否支持。

说明

从 API version 10开始支持，从API version 11开始废弃。建议使用[Flash.isFlashModeSupported](arkts-apis-camera-flashquery.md#isflashmodesupported11)替代。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| flashMode | [FlashMode](arkts-apis-camera-e.md#flashmode) | 是 | 指定闪光灯模式。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 检测闪光灯模式是否支持。true表示支持，false表示不支持。接口调用失败会返回相应错误码，错误码类型[CameraErrorCode](arkts-apis-camera-e.md#cameraerrorcode)。 |

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](errorcode-camera.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400103 | Session not config. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. function isFlashModeSupported(captureSession: camera.CaptureSession): boolean {
4. let status: boolean = false;
5. try {
6. status = captureSession.isFlashModeSupported(camera.FlashMode.FLASH_MODE_AUTO);
7. } catch (error) {
8. // 失败返回错误码error.code并处理。
9. let err = error as BusinessError;
10. console.error(`The isFlashModeSupported call failed. error code: ${err.code}`);
11. }
12. return status;
13. }
```

## setFlashMode(deprecated)

PhonePC/2in1TabletTVWearable

setFlashMode(flashMode: FlashMode): void

设置闪光灯模式。

进行设置之前，需要先检查：

1. 设备是否支持闪光灯，可使用方法[hasFlash](arkts-apis-camera-capturesession.md#hasflashdeprecated)。
2. 设备是否支持指定的闪光灯模式，可使用方法[isFlashModeSupported](arkts-apis-camera-capturesession.md#isflashmodesupporteddeprecated)。

说明

从 API version 10开始支持，从API version 11开始废弃。建议使用[Flash.setFlashMode](arkts-apis-camera-flash.md#setflashmode11)替代。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| flashMode | [FlashMode](arkts-apis-camera-e.md#flashmode) | 是 | 指定闪光灯模式。 |

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](errorcode-camera.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400103 | Session not config. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. function setFlashMode(captureSession: camera.CaptureSession): void {
4. try {
5. captureSession.setFlashMode(camera.FlashMode.FLASH_MODE_AUTO);
6. } catch (error) {
7. // 失败返回错误码error.code并处理。
8. let err = error as BusinessError;
9. console.error(`The setFlashMode call failed. error code: ${err.code}`);
10. }
11. }
```

## getFlashMode(deprecated)

PhonePC/2in1TabletTVWearable

getFlashMode(): FlashMode

获取当前设备的闪光灯模式。

说明

从 API version 10开始支持，从API version 11开始废弃。建议使用[Flash.getFlashMode](arkts-apis-camera-flash.md#getflashmode11)替代。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [FlashMode](arkts-apis-camera-e.md#flashmode) | 获取当前设备的闪光灯模式。接口调用失败会返回相应错误码，错误码类型[CameraErrorCode](arkts-apis-camera-e.md#cameraerrorcode)。 |

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](errorcode-camera.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400103 | Session not config. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. function getFlashMode(captureSession: camera.CaptureSession): camera.FlashMode | undefined {
4. let flashMode: camera.FlashMode | undefined = undefined;
5. try {
6. flashMode = captureSession.getFlashMode();
7. } catch (error) {
8. // 失败返回错误码error.code并处理。
9. let err = error as BusinessError;
10. console.error(`The getFlashMode call failed.error code: ${err.code}`);
11. }
12. return flashMode;
13. }
```

## isExposureModeSupported(deprecated)

PhonePC/2in1TabletTVWearable

isExposureModeSupported(aeMode: ExposureMode): boolean

查询曝光模式是否支持。

说明

从 API version 10开始支持，从API version 11开始废弃。建议使用[AutoExposure.isExposureModeSupported](arkts-apis-camera-autoexposurequery.md#isexposuremodesupported11)替代。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| aeMode | [ExposureMode](arkts-apis-camera-e.md#exposuremode) | 是 | 曝光模式。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 获取是否支持曝光模式。true表示支持，false表示不支持。接口调用失败会返回相应错误码，错误码类型[CameraErrorCode](arkts-apis-camera-e.md#cameraerrorcode)。 |

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](errorcode-camera.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400103 | Session not config. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. function isExposureModeSupported(captureSession: camera.CaptureSession): boolean {
4. let isSupported: boolean = false;
5. try {
6. isSupported = captureSession.isExposureModeSupported(camera.ExposureMode.EXPOSURE_MODE_LOCKED);
7. } catch (error) {
8. // 失败返回错误码error.code并处理。
9. let err = error as BusinessError;
10. console.error(`The isExposureModeSupported call failed. error code: ${err.code}`);
11. }
12. return isSupported;
13. }
```

## getExposureMode(deprecated)

PhonePC/2in1TabletTVWearable

getExposureMode(): ExposureMode

获取当前曝光模式。

说明

从 API version 10开始支持，从API version 11开始废弃。建议使用[AutoExposure.getExposureMode](arkts-apis-camera-autoexposure.md#getexposuremode11)替代。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ExposureMode](arkts-apis-camera-e.md#exposuremode) | 获取当前曝光模式。接口调用失败会返回相应错误码，错误码类型[CameraErrorCode](arkts-apis-camera-e.md#cameraerrorcode)。 |

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](errorcode-camera.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400103 | Session not config. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. function getExposureMode(captureSession: camera.CaptureSession): camera.ExposureMode | undefined {
4. let exposureMode: camera.ExposureMode | undefined = undefined;
5. try {
6. exposureMode = captureSession.getExposureMode();
7. } catch (error) {
8. // 失败返回错误码error.code并处理。
9. let err = error as BusinessError;
10. console.error(`The getExposureMode call failed. error code: ${err.code}`);
11. }
12. return exposureMode;
13. }
```

## setExposureMode(deprecated)

PhonePC/2in1TabletTVWearable

setExposureMode(aeMode: ExposureMode): void

设置曝光模式。进行设置之前，需要先检查设备是否支持指定的曝光模式，可使用方法[isExposureModeSupported](arkts-apis-camera-capturesession.md#isexposuremodesupporteddeprecated)。

说明

从 API version 10开始支持，从API version 11开始废弃。建议使用[AutoExposure.setExposureMode](arkts-apis-camera-autoexposure.md#setexposuremode11)替代。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| aeMode | [ExposureMode](arkts-apis-camera-e.md#exposuremode) | 是 | 曝光模式。 |

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](errorcode-camera.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400103 | Session not config. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. function setExposureMode(captureSession: camera.CaptureSession): void {
4. try {
5. captureSession.setExposureMode(camera.ExposureMode.EXPOSURE_MODE_LOCKED);
6. } catch (error) {
7. // 失败返回错误码error.code并处理。
8. let err = error as BusinessError;
9. console.error(`The setExposureMode call failed. error code: ${err.code}`);
10. }
11. }
```

## getMeteringPoint(deprecated)

PhonePC/2in1TabletTVWearable

getMeteringPoint(): Point

查询曝光区域中心点。

说明

从 API version 10开始支持，从API version 11开始废弃。建议使用[AutoExposure.getMeteringPoint](arkts-apis-camera-autoexposure.md#getmeteringpoint11)替代。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Point](arkts-apis-camera-i.md#point) | 获取当前曝光点。接口调用失败会返回相应错误码，错误码类型[CameraErrorCode](arkts-apis-camera-e.md#cameraerrorcode)。 |

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](errorcode-camera.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400103 | Session not config. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. function getMeteringPoint(captureSession: camera.CaptureSession): camera.Point | undefined {
4. let exposurePoint: camera.Point | undefined = undefined;
5. try {
6. exposurePoint = captureSession.getMeteringPoint();
7. } catch (error) {
8. // 失败返回错误码error.code并处理。
9. let err = error as BusinessError;
10. console.error(`The getMeteringPoint call failed. error code: ${err.code}`);
11. }
12. return exposurePoint;
13. }
```

## setMeteringPoint(deprecated)

PhonePC/2in1TabletTVWearable

setMeteringPoint(point: Point): void

设置曝光区域中心点，曝光点应位于0-1坐标系内，该坐标系左上角为{0，0}，右下角为{1，1}。

此坐标系是以设备充电口在右侧时的横向设备方向为基准的，例如应用的预览界面布局以设备充电口在下侧时的竖向方向为基准，布局宽高为{w，h}，且触碰点为{x，y}，则转换后的坐标点为{y/h，1-x/w}。

说明

从 API version 10开始支持，从API version 11开始废弃。建议使用[AutoExposure.setMeteringPoint](arkts-apis-camera-autoexposure.md#setmeteringpoint11)替代。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| point | [Point](arkts-apis-camera-i.md#point) | 是 | 曝光点，x,y设置范围应在[0,1]之内，超过范围，如果小于0设置0，大于1设置1。 |

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](errorcode-camera.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400103 | Session not config. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. function setMeteringPoint(captureSession: camera.CaptureSession): void {
4. const point: camera.Point = {x: 1, y: 1};
5. try {
6. captureSession.setMeteringPoint(point);
7. } catch (error) {
8. // 失败返回错误码error.code并处理。
9. let err = error as BusinessError;
10. console.error(`The setMeteringPoint call failed. error code: ${err.code}`);
11. }
12. }
```

## getExposureBiasRange(deprecated)

PhonePC/2in1TabletTVWearable

getExposureBiasRange(): Array<number>

查询曝光补偿范围。

说明

从 API version 10开始支持，从API version 11开始废弃。建议使用[AutoExposure.getExposureBiasRange](arkts-apis-camera-autoexposurequery.md#getexposurebiasrange11)替代。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<number> | 获取补偿范围的数组。接口调用失败会返回相应错误码，错误码类型[CameraErrorCode](arkts-apis-camera-e.md#cameraerrorcode)。 |

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](errorcode-camera.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400103 | Session not config. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. function getExposureBiasRange(captureSession: camera.CaptureSession): Array<number> {
4. let biasRangeArray: Array<number> = [];
5. try {
6. biasRangeArray = captureSession.getExposureBiasRange();
7. } catch (error) {
8. // 失败返回错误码error.code并处理。
9. let err = error as BusinessError;
10. console.error(`The getExposureBiasRange call failed. error code: ${err.code}`);
11. }
12. return biasRangeArray;
13. }
```

## setExposureBias(deprecated)

PhonePC/2in1TabletTVWearable

setExposureBias(exposureBias: number): void

设置曝光补偿，曝光补偿值（EV）。

进行设置之前，建议先通过方法[getExposureBiasRange](arkts-apis-camera-capturesession.md#getexposurebiasrangedeprecated)查询支持的范围。

说明

从 API version 10开始支持，从API version 11开始废弃。建议使用[AutoExposure.setExposureBias](arkts-apis-camera-autoexposure.md#setexposurebias11)替代。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| exposureBias | number | 是 | 曝光补偿，[getExposureBiasRange](arkts-apis-camera-autoexposurequery.md#getexposurebiasrange11)查询支持的范围，如果设置超过支持范围的值，自动匹配到就近临界点。曝光补偿存在步长，如步长为0.5。则设置1.2时，获取到实际生效曝光补偿为1.0。接口调用失败会返回相应错误码，错误码类型[CameraErrorCode](arkts-apis-camera-e.md#cameraerrorcode)。传参为null或者undefined，作为0处理，曝光补偿设置0。 |

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](errorcode-camera.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400103 | Session not config. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. function setExposureBias(captureSession: camera.CaptureSession, biasRangeArray: Array<number>): void {
4. if (biasRangeArray && biasRangeArray.length > 0) {
5. let exposureBias = biasRangeArray[0];
6. try {
7. captureSession.setExposureBias(exposureBias);
8. } catch (error) {
9. // 失败返回错误码error.code并处理。
10. let err = error as BusinessError;
11. console.error(`The setExposureBias call failed. error code: ${err.code}`);
12. }
13. }
14. }
```

## getExposureValue(deprecated)

PhonePC/2in1TabletTVWearable

getExposureValue(): number

查询当前的曝光值。

说明

从 API version 10开始支持，从API version 11开始废弃。建议使用[AutoExposure.getExposureValue](arkts-apis-camera-autoexposure.md#getexposurevalue11)替代。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 获取曝光值。曝光补偿存在步长，如步长为0.5。则设置1.2时，获取到实际生效曝光补偿为1.0。接口调用失败会返回相应错误码，错误码类型[CameraErrorCode](arkts-apis-camera-e.md#cameraerrorcode)。 |

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](errorcode-camera.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400103 | Session not config. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. function getExposureValue(captureSession: camera.CaptureSession): number {
4. const invalidValue: number = -1;
5. let exposureValue: number = invalidValue;
6. try {
7. exposureValue = captureSession.getExposureValue();
8. } catch (error) {
9. // 失败返回错误码error.code并处理。
10. let err = error as BusinessError;
11. console.error(`The getExposureValue call failed. error code: ${err.code}`);
12. }
13. return exposureValue;
14. }
```

## isFocusModeSupported(deprecated)

PhonePC/2in1TabletTVWearable

isFocusModeSupported(afMode: FocusMode): boolean

查询对焦模式是否支持。

说明

从 API version 10开始支持，从API version 11开始废弃。建议使用[Focus.isFocusModeSupported](arkts-apis-camera-focusquery.md#isfocusmodesupported11)替代。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| afMode | [FocusMode](arkts-apis-camera-e.md#focusmode) | 是 | 指定的焦距模式。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 检测对焦模式是否支持。true表示支持，false表示不支持。接口调用失败会返回相应错误码，错误码类型[CameraErrorCode](arkts-apis-camera-e.md#cameraerrorcode)。 |

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](errorcode-camera.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400103 | Session not config. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. function isFocusModeSupported(captureSession: camera.CaptureSession): boolean {
4. let status: boolean = false;
5. try {
6. status = captureSession.isFocusModeSupported(camera.FocusMode.FOCUS_MODE_AUTO);
7. } catch (error) {
8. // 失败返回错误码error.code并处理。
9. let err = error as BusinessError;
10. console.error(`The isFocusModeSupported call failed. error code: ${err.code}`);
11. }
12. return status;
13. }
```

## setFocusMode(deprecated)

PhonePC/2in1TabletTVWearable

setFocusMode(afMode: FocusMode): void

设置对焦模式。

进行设置之前，需要先检查设备是否支持指定的焦距模式，可使用方法[isFocusModeSupported](arkts-apis-camera-capturesession.md#isfocusmodesupporteddeprecated)。

说明

从 API version 10开始支持，从API version 11开始废弃。建议使用[Focus.setFocusMode](arkts-apis-camera-focus.md#setfocusmode11)替代。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| afMode | [FocusMode](arkts-apis-camera-e.md#focusmode) | 是 | 指定的焦距模式。 |

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](errorcode-camera.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400103 | Session not config. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. function setFocusMode(captureSession: camera.CaptureSession): void {
4. try {
5. captureSession.setFocusMode(camera.FocusMode.FOCUS_MODE_AUTO);
6. } catch (error) {
7. // 失败返回错误码error.code并处理。
8. let err = error as BusinessError;
9. console.error(`The setFocusMode call failed. error code: ${err.code}`);
10. }
11. }
```

## getFocusMode(deprecated)

PhonePC/2in1TabletTVWearable

getFocusMode(): FocusMode

获取当前的对焦模式。

说明

从 API version 10开始支持，从API version 11开始废弃。建议使用[Focus.getFocusMode](arkts-apis-camera-focus.md#getfocusmode11)替代。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [FocusMode](arkts-apis-camera-e.md#focusmode) | 获取当前设备的焦距模式。接口调用失败会返回相应错误码，错误码类型[CameraErrorCode](arkts-apis-camera-e.md#cameraerrorcode)。 |

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](errorcode-camera.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400103 | Session not config. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. function getFocusMode(captureSession: camera.CaptureSession): camera.FocusMode | undefined {
4. let afMode: camera.FocusMode | undefined = undefined;
5. try {
6. afMode = captureSession.getFocusMode();
7. } catch (error) {
8. // 失败返回错误码error.code并处理。
9. let err = error as BusinessError;
10. console.error(`The getFocusMode call failed. error code: ${err.code}`);
11. }
12. return afMode;
13. }
```

## setFocusPoint(deprecated)

PhonePC/2in1TabletTVWearable

setFocusPoint(point: Point): void

设置焦点，焦点应在0-1坐标系内，该坐标系左上角为{0，0}，右下角为{1，1}。

此坐标系是以设备充电口在右侧时的横向设备方向为基准的，例如应用的预览界面布局以设备充电口在下侧时的竖向方向为基准，布局宽高为{w，h}，且触碰点为{x，y}，则转换后的坐标点为{y/h，1-x/w}。

说明

从 API version 10开始支持，从API version 11开始废弃。建议使用[Focus.setFocusPoint](arkts-apis-camera-focus.md#setfocuspoint11)替代。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| point | [Point](arkts-apis-camera-i.md#point) | 是 | 焦点。x,y设置范围应在[0,1]之内，超过范围，如果小于0设置0，大于1设置1。 |

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](errorcode-camera.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400103 | Session not config. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. function setFocusPoint(captureSession: camera.CaptureSession): void {
4. const focusPoint: camera.Point = {x: 1, y: 1};
5. try {
6. captureSession.setFocusPoint(focusPoint);
7. } catch (error) {
8. // 失败返回错误码error.code并处理。
9. let err = error as BusinessError;
10. console.error(`The setFocusPoint call failed. error code: ${err.code}`);
11. }
12. }
```

## getFocusPoint(deprecated)

PhonePC/2in1TabletTVWearable

getFocusPoint(): Point

查询焦点。

说明

从 API version 10开始支持，从API version 11开始废弃。建议使用[Focus.getFocusPoint](arkts-apis-camera-focus.md#getfocuspoint11)替代。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Point](arkts-apis-camera-i.md#point) | 用于获取当前焦点。接口调用失败会返回相应错误码，错误码类型[CameraErrorCode](arkts-apis-camera-e.md#cameraerrorcode)。 |

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](errorcode-camera.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400103 | Session not config. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. function getFocusPoint(captureSession: camera.CaptureSession): camera.Point | undefined {
4. let point: camera.Point | undefined = undefined;
5. try {
6. point = captureSession.getFocusPoint();
7. } catch (error) {
8. // 失败返回错误码error.code并处理。
9. let err = error as BusinessError;
10. console.error(`The getFocusPoint call failed. error code: ${err.code}`);
11. }
12. return point;
13. }
```

## getFocalLength(deprecated)

PhonePC/2in1TabletTVWearable

getFocalLength(): number

查询焦距值。

说明

从 API version 10开始支持，从API version 11开始废弃。建议使用[Focus.getFocalLength](arkts-apis-camera-focus.md#getfocallength11)替代。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 用于获取当前焦距。接口调用失败会返回相应错误码，错误码类型[CameraErrorCode](arkts-apis-camera-e.md#cameraerrorcode)。 |

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](errorcode-camera.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400103 | Session not config. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. function getFocalLength(captureSession: camera.CaptureSession): number {
4. const invalidValue: number = -1;
5. let focalLength: number = invalidValue;
6. try {
7. focalLength = captureSession.getFocalLength();
8. } catch (error) {
9. // 失败返回错误码error.code并处理。
10. let err = error as BusinessError;
11. console.error(`The getFocalLength call failed. error code: ${err.code}`);
12. }
13. return focalLength;
14. }
```

## getZoomRatioRange(deprecated)

PhonePC/2in1TabletTVWearable

getZoomRatioRange(): Array<number>

获取支持的变焦范围。

说明

从 API version 10开始支持，从API version 11开始废弃。建议使用[Zoom.getZoomRatioRange](arkts-apis-camera-zoomquery.md#getzoomratiorange11)替代。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<number> | 用于获取可变焦距比范围，返回的数组包括其最小值和最大值。接口调用失败会返回相应错误码，错误码类型[CameraErrorCode](arkts-apis-camera-e.md#cameraerrorcode)。 |

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](errorcode-camera.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400103 | Session not config. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. function getZoomRatioRange(captureSession: camera.CaptureSession): Array<number> {
4. let zoomRatioRange: Array<number> = [];
5. try {
6. zoomRatioRange = captureSession.getZoomRatioRange();
7. } catch (error) {
8. // 失败返回错误码error.code并处理。
9. let err = error as BusinessError;
10. console.error(`The getZoomRatioRange call failed. error code: ${err.code}`);
11. }
12. return zoomRatioRange;
13. }
```

## setZoomRatio(deprecated)

PhonePC/2in1TabletTVWearable

setZoomRatio(zoomRatio: number): void

设置变焦比，变焦精度最高为小数点后两位，如果设置超过支持的精度范围，则只保留精度范围内数值。

说明

从 API version 10开始支持，从API version 11开始废弃。建议使用[Zoom.setZoomRatio](arkts-apis-camera-zoom.md#setzoomratio11)替代。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| zoomRatio | number | 是 | 可变焦距比，通过[getZoomRatioRange](arkts-apis-camera-zoomquery.md#getzoomratiorange11)获取支持的变焦范围，如果设置超过支持范围的值，则只保留精度范围内数值。传参为null或者undefined，作为0处理，变焦设置最小值。 |

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](errorcode-camera.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400103 | Session not config. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. function setZoomRatio(captureSession: camera.CaptureSession, zoomRatioRange: Array<number>): void {
4. if (zoomRatioRange === undefined || zoomRatioRange.length <= 0) {
5. return;
6. }
7. let zoomRatio = zoomRatioRange[0];
8. try {
9. captureSession.setZoomRatio(zoomRatio);
10. } catch (error) {
11. // 失败返回错误码error.code并处理。
12. let err = error as BusinessError;
13. console.error(`The setZoomRatio call failed. error code: ${err.code}`);
14. }
15. }
```

## getZoomRatio(deprecated)

PhonePC/2in1TabletTVWearable

getZoomRatio(): number

获取当前的变焦比。

说明

从 API version 10开始支持，从API version 11开始废弃。建议使用[Zoom.getZoomRatio](arkts-apis-camera-zoom.md#getzoomratio11)替代。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 获取当前的变焦比结果。接口调用失败会返回相应错误码，错误码类型[CameraErrorCode](arkts-apis-camera-e.md#cameraerrorcode)。 |

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](errorcode-camera.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400103 | Session not config. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. function getZoomRatio(captureSession: camera.CaptureSession): number {
4. const invalidValue: number = -1;
5. let zoomRatio: number = invalidValue;
6. try {
7. zoomRatio = captureSession.getZoomRatio();
8. } catch (error) {
9. // 失败返回错误码error.code并处理。
10. let err = error as BusinessError;
11. console.error(`The getZoomRatio call failed. error code: ${err.code}`);
12. }
13. return zoomRatio;
14. }
```

## isVideoStabilizationModeSupported(deprecated)

PhonePC/2in1TabletTVWearable

isVideoStabilizationModeSupported(vsMode: VideoStabilizationMode): boolean

查询是否支持指定的视频防抖模式。

说明

从 API version 10开始支持，从API version 11开始废弃。建议使用[Stabilization.isVideoStabilizationModeSupported](arkts-apis-camera-stabilizationquery.md#isvideostabilizationmodesupported11)替代。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| vsMode | [VideoStabilizationMode](arkts-apis-camera-e.md#videostabilizationmode) | 是 | 视频防抖模式。传参为null或者undefined，作为0处理，超级防抖模式关闭。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回视频防抖模式是否支持。true表示支持，false表示不支持。接口调用失败会返回相应错误码，错误码类型[CameraErrorCode](arkts-apis-camera-e.md#cameraerrorcode)。 |

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](errorcode-camera.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400103 | Session not config. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. function isVideoStabilizationModeSupported(captureSession: camera.CaptureSession): boolean {
4. let isSupported: boolean = false;
5. try {
6. isSupported = captureSession.isVideoStabilizationModeSupported(camera.VideoStabilizationMode.OFF);
7. } catch (error) {
8. // 失败返回错误码error.code并处理。
9. let err = error as BusinessError;
10. console.error(`The isVideoStabilizationModeSupported call failed. error code: ${err.code}`);
11. }
12. return isSupported;
13. }
```

## getActiveVideoStabilizationMode(deprecated)

PhonePC/2in1TabletTVWearable

getActiveVideoStabilizationMode(): VideoStabilizationMode

查询当前正在使用的视频防抖模式。

说明

从 API version 10开始支持，从API version 11开始废弃。建议使用[Stabilization.getActiveVideoStabilizationMode](arkts-apis-camera-stabilization.md#getactivevideostabilizationmode11)替代。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [VideoStabilizationMode](arkts-apis-camera-e.md#videostabilizationmode) | 视频防抖是否正在使用。接口调用失败会返回相应错误码，错误码类型[CameraErrorCode](arkts-apis-camera-e.md#cameraerrorcode)。 |

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](errorcode-camera.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400103 | Session not config. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. function getActiveVideoStabilizationMode(captureSession: camera.CaptureSession): camera.VideoStabilizationMode | undefined {
4. let vsMode: camera.VideoStabilizationMode | undefined = undefined;
5. try {
6. vsMode = captureSession.getActiveVideoStabilizationMode();
7. } catch (error) {
8. // 失败返回错误码error.code并处理。
9. let err = error as BusinessError;
10. console.error(`The getActiveVideoStabilizationMode call failed. error code: ${err.code}`);
11. }
12. return vsMode;
13. }
```

## setVideoStabilizationMode(deprecated)

PhonePC/2in1TabletTVWearable

setVideoStabilizationMode(mode: VideoStabilizationMode): void

设置视频防抖模式。需要先检查设备是否支持对应的防抖模式，可以通过[isVideoStabilizationModeSupported](arkts-apis-camera-capturesession.md#isvideostabilizationmodesupporteddeprecated)方法判断所设置的模式是否支持。

说明

从 API version 10开始支持，从API version 11开始废弃。建议使用[Stabilization.setVideoStabilizationMode](arkts-apis-camera-stabilization.md#setvideostabilizationmode11)替代。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mode | [VideoStabilizationMode](arkts-apis-camera-e.md#videostabilizationmode) | 是 | 需要设置的视频防抖模式。传参为null或者undefined，作为0处理，超级防抖模式关闭。 |

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](errorcode-camera.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400103 | Session not config. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. function setVideoStabilizationMode(captureSession: camera.CaptureSession): void {
4. try {
5. captureSession.setVideoStabilizationMode(camera.VideoStabilizationMode.OFF);
6. } catch (error) {
7. // 失败返回错误码error.code并处理。
8. let err = error as BusinessError;
9. console.error(`The setVideoStabilizationMode call failed. error code: ${err.code}`);
10. }
11. }
```

## on('focusStateChange')(deprecated)

PhonePC/2in1TabletTVWearable

on(type: 'focusStateChange', callback: AsyncCallback<FocusState>): void

监听相机聚焦的状态变化，通过注册回调函数获取结果。使用callback异步回调。

说明

从 API version 10开始支持，从API version 11开始废弃。建议使用[VideoSession.on('focusStateChange')](arkts-apis-camera-videosession.md#onfocusstatechange11)替代。

当前注册监听接口，不支持在on监听的回调方法里，调用off注销回调。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'focusStateChange'，session 创建成功可监听。仅当自动对焦模式时,且相机对焦状态发生改变时可触发该事件。 |
| callback | AsyncCallback<[FocusState](arkts-apis-camera-e.md#focusstate)> | 是 | 回调函数，用于获取当前对焦状态。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. function registerFocusStateChange(captureSession: camera.CaptureSession): void {
4. captureSession.on('focusStateChange', (err: BusinessError, focusState: camera.FocusState) => {
5. if (err !== undefined && err.code !== 0) {
6. console.error(`Callback Error, errorCode: ${err.code}`);
7. return;
8. }
9. console.info(`Focus state: ${focusState}`);
10. });
11. }
```

## off('focusStateChange')(deprecated)

PhonePC/2in1TabletTVWearable

off(type: 'focusStateChange', callback?: AsyncCallback<FocusState>): void

注销监听相机聚焦的状态变化。

说明

从 API version 10开始支持，从API version 11开始废弃。建议使用[VideoSession.off('focusStateChange')](arkts-apis-camera-videosession.md#offfocusstatechange11)替代。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'focusStateChange'，session 创建成功可监听。 |
| callback | AsyncCallback<[FocusState](arkts-apis-camera-e.md#focusstate)> | 否 | 回调函数，如果指定参数则取消对应callback（callback对象不可是匿名函数），否则取消所有callback。 |

**示例：**

```
1. function unregisterFocusStateChange(captureSession: camera.CaptureSession): void {
2. captureSession.off('focusStateChange');
3. }
```

## on('error')(deprecated)

PhonePC/2in1TabletTVWearable

on(type: 'error', callback: ErrorCallback): void

监听拍照会话的错误事件，通过注册回调函数获取结果。使用callback异步回调。

说明

当前注册监听接口，不支持在on监听的回调方法里，调用off注销回调。

从 API version 10开始支持，从API version 11开始废弃。建议使用[VideoSession.on('error')](arkts-apis-camera-videosession.md#onerror11)替代。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'error'，session创建成功之后可监听该接口。session调用相关接口出现错误时会触发该事件，比如调用[beginConfig](arkts-apis-camera-capturesession.md#beginconfigdeprecated)，[commitConfig](arkts-apis-camera-capturesession.md#commitconfigdeprecated-1)，[addInput](arkts-apis-camera-capturesession.md#addinputdeprecated)等接口发生错误时返回错误信息。 |
| callback | [ErrorCallback](js-apis-base.md#errorcallback) | 是 | 回调函数，用于获取错误信息。返回错误码，错误码类型[CameraErrorCode](arkts-apis-camera-e.md#cameraerrorcode)。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. function registerCaptureSessionError(captureSession: camera.CaptureSession): void {
4. captureSession.on('error', (error: BusinessError) => {
5. console.error(`Capture session error code: ${error.code}`);
6. });
7. }
```

## off('error')(deprecated)

PhonePC/2in1TabletTVWearable

off(type: 'error', callback?: ErrorCallback): void

注销监听拍照会话的错误事件，通过注册回调函数获取结果。

说明

从 API version 10开始支持，从API version 11开始废弃。建议使用[VideoSession.off('error')](arkts-apis-camera-videosession.md#offerror11)替代。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'error'，session创建成功之后可监听该接口。 |
| callback | [ErrorCallback](js-apis-base.md#errorcallback) | 否 | 回调函数，如果指定参数则取消对应callback（callback对象不可是匿名函数），否则取消所有callback。 |

**示例：**

```
1. function unregisterCaptureSessionError(captureSession: camera.CaptureSession): void {
2. captureSession.off('error');
3. }
```
