---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-camera-securesession
title: Interface (SecureSession)
breadcrumb: API参考 > 媒体 > Camera Kit（相机服务） > ArkTS API > @ohos.multimedia.camera (相机管理) > Interface (SecureSession)
category: harmonyos-references
scraped_at: 2026-04-28T08:12:39+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:999f1fcebd5945de6f007b80837e6c7d35aa2d055b18d7ad8ff9f1434eb6cc2f
---

SecureSession 继承自 [Session](arkts-apis-camera-session.md)、[Flash](arkts-apis-camera-flash.md)、[AutoExposure](arkts-apis-camera-autoexposure.md)、[WhiteBalance](arkts-apis-camera-whitebalance.md)、[Focus](arkts-apis-camera-focus.md)、[Zoom](arkts-apis-camera-zoom.md)。

安全模式会话类，提供了对闪光灯、曝光、白平衡、对焦、变焦的操作。

通过[createSession](arkts-apis-camera-cameramanager.md#createsession11)接口传入[SceneMode](arkts-apis-camera-e.md#scenemode11)为SECURE\_PHOTO模式创建一个安全模式的会话。该模式开放给人脸识别、银行等有安全诉求的应用，需要结合Device Security Kit使用，支持同时输出普通预览流和安全流的业务场景。请参考[安全相机开发指导](../harmonyos-guides/camera-secure-photo.md)。

说明

* 本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 本Interface首批接口从API version 12开始支持。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { camera } from '@kit.CameraKit';
```

## addSecureOutput12+

PhonePC/2in1TabletTVWearable

addSecureOutput(previewOutput: PreviewOutput): void

将其中一条[PreviewOutput](arkts-apis-camera-previewoutput.md)标记成安全输出。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| previewOutput | [PreviewOutput](arkts-apis-camera-previewoutput.md) | 是 | 需要标记成安全输出的预览流，传参异常时，会返回错误码。 |

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](errorcode-camera.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400101 | Parameter missing or parameter type incorrect. |
| 7400102 | Operation not allowed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. function addSecureOutput(session: camera.SecureSession, previewOutput: camera.PreviewOutput): void {
4. try {
5. session.addSecureOutput(previewOutput);
6. } catch (error) {
7. // 失败返回错误码error.code并处理。
8. let err = error as BusinessError;
9. console.error(`The addOutput call failed. error code: ${err.code}`);
10. }
11. }
```

## on('error')12+

PhonePC/2in1TabletTVWearable

on(type: 'error', callback: ErrorCallback): void

监听安全相机会话的错误事件，通过注册回调函数获取结果。使用callback异步回调。

说明

当前注册监听接口，不支持在on监听的回调方法里，调用off注销回调。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'error'，session创建成功之后可监听该接口。session调用相关接口出现错误时会触发该事件，比如调用[beginConfig](arkts-apis-camera-session.md#beginconfig11)，[commitConfig](arkts-apis-camera-session.md#commitconfig11-1)，[addInput](arkts-apis-camera-session.md#addinput11)等接口发生错误时返回错误信息。 |
| callback | [ErrorCallback](js-apis-base.md#errorcallback) | 是 | 回调函数，用于获取错误信息。返回错误码，错误码类型[CameraErrorCode](arkts-apis-camera-e.md#cameraerrorcode)。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. function callback(err: BusinessError): void {
4. console.error(`Video session error code: ${err.code}`);
5. }

7. function registerSessionError(secureSession: camera.SecureSession): void {
8. secureSession.on('error', callback);
9. }
```

## off('error')12+

PhonePC/2in1TabletTVWearable

off(type: 'error', callback?: ErrorCallback): void

注销监听安全相机会话的错误事件，通过注册回调函数获取结果。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'error'，session创建成功之后可监听该接口。 |
| callback | [ErrorCallback](js-apis-base.md#errorcallback) | 否 | 回调函数，如果指定参数则取消对应callback（callback对象不可是匿名函数），否则取消所有callback。 |

**示例：**

```
1. function unregisterSessionError(secureSession: camera.SecureSession): void {
2. secureSession.off('error');
3. }
```

## on('focusStateChange')12+

PhonePC/2in1TabletTVWearable

on(type: 'focusStateChange', callback: AsyncCallback<FocusState>): void

监听相机聚焦的状态变化，通过注册回调函数获取结果。使用callback异步回调。

说明

当前注册监听接口，不支持在on监听的回调方法里，调用off注销回调。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'focusStateChange'，session创建成功可监听。仅当自动对焦模式时，且相机对焦状态发生改变时可触发该事件。 |
| callback | AsyncCallback<[FocusState](arkts-apis-camera-e.md#focusstate)> | 是 | 回调函数，用于获取当前对焦状态。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. function callback(err: BusinessError, focusState: camera.FocusState): void {
4. if (err !== undefined && err.code !== 0) {
5. console.error(`Callback Error, errorCode: ${err.code}`);
6. return;
7. }
8. console.info(`Focus state: ${focusState}`);
9. }

11. function registerFocusStateChange(secureSession: camera.SecureSession): void {
12. secureSession.on('focusStateChange', callback);
13. }
```

## off('focusStateChange')12+

PhonePC/2in1TabletTVWearable

off(type: 'focusStateChange', callback?: AsyncCallback<FocusState>): void

注销监听相机聚焦的状态变化。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'focusStateChange'，session创建成功可监听。 |
| callback | AsyncCallback<[FocusState](arkts-apis-camera-e.md#focusstate)> | 否 | 回调函数，如果指定参数则取消对应callback（callback对象不可是匿名函数），否则取消所有callback。 |

**示例：**

```
1. function unregisterFocusStateChange(secureSession: camera.SecureSession): void {
2. secureSession.off('focusStateChange');
3. }
```
