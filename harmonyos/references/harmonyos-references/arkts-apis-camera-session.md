---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-camera-session
title: Interface (Session)
breadcrumb: API参考 > 媒体 > Camera Kit（相机服务） > ArkTS API > @ohos.multimedia.camera (相机管理) > Interface (Session)
category: harmonyos-references
scraped_at: 2026-04-28T08:12:39+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:8c048d0690db47514f8547df6c29d6dd27e36f97ee2c8df466e530e990c3da25
---

会话类，保存一次相机运行所需要的所有资源[CameraInput](arkts-apis-camera-camerainput.md)、[CameraOutput](arkts-apis-camera-cameraoutput.md)，并向相机设备申请完成相机功能（录像，拍照）。

说明

* 本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 本Interface首批接口从API version 11开始支持。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { camera } from '@kit.CameraKit';
```

## beginConfig11+

PhonePC/2in1TabletTVWearable

beginConfig(): void

开始配置会话。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](errorcode-camera.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400105 | Session config locked. |
| 7400201 | Camera service fatal error. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. function beginConfig(session: camera.Session): void {
4. try {
5. session.beginConfig();
6. } catch (error) {
7. // 失败返回错误码error.code并处理。
8. let err = error as BusinessError;
9. console.error(`The beginConfig call failed. error code: ${err.code}`);
10. }
11. }
```

## commitConfig11+

PhonePC/2in1TabletTVWearable

commitConfig(callback: AsyncCallback<void>): void

提交配置信息，通过注册回调函数获取结果。使用callback异步回调。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<void> | 是 | 回调函数。当提交配置信息成功，err为undefined，否则为错误对象。错误码类型[CameraErrorCode](arkts-apis-camera-e.md#cameraerrorcode)，比如预览流与录像输出流的分辨率的宽高比不一致，会返回7400201。 |

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](errorcode-camera.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400102 | Operation not allowed. |
| 7400201 | Camera service fatal error. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. function commitConfig(session: camera.Session): void {
4. session.commitConfig((err: BusinessError) => {
5. if (err) {
6. console.error(`The commitConfig call failed. error code: ${err.code}`);
7. return;
8. }
9. console.info('Callback invoked to indicate the commit config success.');
10. });
11. }
```

## commitConfig11+

PhonePC/2in1TabletTVWearable

commitConfig(): Promise<void>

提交配置信息。使用Promise异步回调。

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
| 7400201 | Camera service fatal error. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. function commitConfig(session: camera.Session): void {
4. session.commitConfig().then(() => {
5. console.info('Promise returned to indicate the commit config success.');
6. }).catch((error: BusinessError) => {
7. // 失败返回错误码error.code并处理。
8. console.error(`The commitConfig call failed. error code: ${error.code}`);
9. });
10. }
```

## canAddInput11+

PhonePC/2in1TabletTVWearable

canAddInput(cameraInput: CameraInput): boolean

判断当前cameraInput是否可以添加到session中。当前函数需要在[beginConfig](arkts-apis-camera-session.md#beginconfig11)和[commitConfig](arkts-apis-camera-session.md#commitconfig11-1)之间生效。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| cameraInput | [CameraInput](arkts-apis-camera-camerainput.md) | 是 | 需要添加的CameraInput实例。传参异常（如超出范围、传入null、未定义等），实际接口不会生效。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 判断当前cameraInput是否可以添加到session中。true表示支持添加当前cameraInput，false表示不支持添加。 |

**示例：**

```
1. function canAddInput(session: camera.Session, cameraInput: camera.CameraInput): void {
2. let canAdd: boolean = session.canAddInput(cameraInput);
3. console.info(`The input canAddInput: ${canAdd}`);
4. }
```

## addInput11+

PhonePC/2in1TabletTVWearable

addInput(cameraInput: CameraInput): void

把[CameraInput](arkts-apis-camera-camerainput.md)加入到会话。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

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
| 7400201 | Camera service fatal error. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. function addInput(session: camera.Session, cameraInput: camera.CameraInput): void {
4. try {
5. session.addInput(cameraInput);
6. } catch (error) {
7. // 失败返回错误码error.code并处理。
8. let err = error as BusinessError;
9. console.error(`The addInput call failed. error code: ${err.code}`);
10. }
11. }
```

## removeInput11+

PhonePC/2in1TabletTVWearable

removeInput(cameraInput: CameraInput): void

移除[CameraInput](arkts-apis-camera-camerainput.md)。当前函数需要在[beginConfig](arkts-apis-camera-session.md#beginconfig11)和[commitConfig](arkts-apis-camera-session.md#commitconfig11-1)之间生效。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

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
| 7400201 | Camera service fatal error. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. function removeInput(session: camera.Session, cameraInput: camera.CameraInput): void {
4. try {
5. session.removeInput(cameraInput);
6. } catch (error) {
7. // 失败返回错误码error.code并处理。
8. let err = error as BusinessError;
9. console.error(`The removeInput call failed. error code: ${err.code}`);
10. }
11. }
```

## canAddOutput11+

PhonePC/2in1TabletTVWearable

canAddOutput(cameraOutput: CameraOutput): boolean

判断当前cameraOutput是否可以添加到session中。当前函数需要在[addInput](arkts-apis-camera-session.md#addinput11)和[commitConfig](arkts-apis-camera-session.md#commitconfig11-1)之间生效。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| cameraOutput | [CameraOutput](arkts-apis-camera-cameraoutput.md) | 是 | 需要添加的CameraOutput实例。传参异常（如超出范围、传入null、未定义等），实际接口不会生效。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 是否可以添加当前cameraOutput到session中，true为可添加，false为不可添加。 |

**示例：**

```
1. function canAddOutput(session: camera.Session, cameraOutput: camera.CameraOutput): void {
2. let canAdd: boolean = session.canAddOutput(cameraOutput);
3. console.info(`This addOutput can add: ${canAdd}`);
4. }
```

## addOutput11+

PhonePC/2in1TabletTVWearable

addOutput(cameraOutput: CameraOutput): void

把[CameraOutput](arkts-apis-camera-cameraoutput.md)加入到会话。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

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
| 7400201 | Camera service fatal error. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. function addOutput(session: camera.Session, cameraOutput: camera.CameraOutput): void {
4. try {
5. session.addOutput(cameraOutput);
6. } catch (error) {
7. // 失败返回错误码error.code并处理。
8. let err = error as BusinessError;
9. console.error(`The addOutput call failed. error code: ${err.code}`);
10. }
11. }
```

## removeOutput11+

PhonePC/2in1TabletTVWearable

removeOutput(cameraOutput: CameraOutput): void

从会话中移除[CameraOutput](arkts-apis-camera-cameraoutput.md)。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

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
| 7400201 | Camera service fatal error. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. function removeOutput(session: camera.Session, previewOutput: camera.PreviewOutput): void {
4. try {
5. session.removeOutput(previewOutput);
6. } catch (error) {
7. // 失败返回错误码error.code并处理。
8. let err = error as BusinessError;
9. console.error(`The removeOutput call failed. error code: ${err.code}`);
10. }
11. }
```

## start11+

PhonePC/2in1TabletTVWearable

start(callback: AsyncCallback<void>): void

开始会话工作，通过注册回调函数获取结果。使用callback异步回调。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<void> | 是 | 回调函数。当开始会话工作成功，err为undefined，否则为错误对象。错误码类型[CameraErrorCode](arkts-apis-camera-e.md#cameraerrorcode)。 |

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

3. function startCaptureSession(session: camera.Session): void {
4. session.start((err: BusinessError) => {
5. if (err) {
6. console.error(`Failed to start the session, error code: ${err.code}.`);
7. return;
8. }
9. console.info('Callback invoked to indicate the session start success.');
10. });
11. }
```

## start11+

PhonePC/2in1TabletTVWearable

start(): Promise<void>

开始会话工作。使用Promise异步回调。

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
| 7400103 | Session not config. |
| 7400201 | Camera service fatal error. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. function startCaptureSession(session: camera.Session): void {
4. session.start().then(() => {
5. console.info('Promise returned to indicate the session start success.');
6. }).catch((error: BusinessError) => {
7. console.error(`Failed to start the session, error code: ${error.code}.`);
8. });
9. }
```

## stop11+

PhonePC/2in1TabletTVWearable

stop(callback: AsyncCallback<void>): void

停止会话工作，通过注册回调函数获取结果。使用callback异步回调。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

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

3. function stopCaptureSession(session: camera.Session): void {
4. session.stop((err: BusinessError) => {
5. if (err) {
6. console.error(`Failed to stop the session, error code: ${err.code}.`);
7. return;
8. }
9. console.info('Callback invoked to indicate the session stop success.');
10. });
11. }
```

## stop11+

PhonePC/2in1TabletTVWearable

stop(): Promise<void>

停止会话工作。使用Promise异步回调。

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

3. function stopCaptureSession(session: camera.Session): void {
4. session.stop().then(() => {
5. console.info('Promise returned to indicate the session stop success.');
6. }).catch((error: BusinessError) => {
7. console.error(`Failed to stop the session, error code: ${error.code}.`);
8. });
9. }
```

## release11+

PhonePC/2in1TabletTVWearable

release(callback: AsyncCallback<void>): void

释放会话资源，通过注册回调函数获取结果。使用callback异步回调。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

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

3. function releaseCaptureSession(session: camera.Session): void {
4. session.release((err: BusinessError) => {
5. if (err) {
6. console.error(`Failed to release the session instance, error code: ${err.code}.`);
7. return;
8. }
9. console.info('Callback invoked to indicate that the session instance is released successfully.');
10. });
11. }
```

## release11+

PhonePC/2in1TabletTVWearable

release(): Promise<void>

释放会话资源。使用Promise异步回调。

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

3. function releaseCaptureSession(session: camera.Session): void {
4. session.release().then(() => {
5. console.info('Promise returned to indicate that the session instance is released successfully.');
6. }).catch((error: BusinessError) => {
7. console.error(`Failed to release the session instance, error code: ${error.code}.`);
8. });
9. }
```
