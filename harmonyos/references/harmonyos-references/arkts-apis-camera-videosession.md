---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-camera-videosession
title: Interface (VideoSession)
breadcrumb: API参考 > 媒体 > Camera Kit（相机服务） > ArkTS API > @ohos.multimedia.camera (相机管理) > Interface (VideoSession)
category: harmonyos-references
scraped_at: 2026-04-28T08:12:39+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:a2fcbc3150c592a0f4527e12818a8e1ad97596a59d042d9ba6b83f05c2f2d7a5
---

VideoSession 继承自 [Session](arkts-apis-camera-session.md)、[Flash](arkts-apis-camera-flash.md)、[AutoExposure](arkts-apis-camera-autoexposure.md)、 [WhiteBalance](arkts-apis-camera-whitebalance.md)、[Focus](arkts-apis-camera-focus.md)、[Zoom](arkts-apis-camera-zoom.md)、[Stabilization](arkts-apis-camera-stabilization.md)、[ColorManagement](arkts-apis-camera-colormanagement.md)、[AutoDeviceSwitch](arkts-apis-camera-autodeviceswitch.md)、[Macro](arkts-apis-camera-macro.md)、[ControlCenter](arkts-apis-camera-controlcenter.md)。

普通录像模式会话类，提供了对闪光灯、曝光、白平衡、对焦、变焦、视频防抖、色彩空间、微距及控制器的操作。

默认的视频录制模式，适用于一般场景。支持720P、1080p等多种分辨率的录制，可选择不同帧率（如30fps、60fps）。

说明

* 本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 本Interface首批接口从API version 11开始支持。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { camera } from '@kit.CameraKit';
```

## canPreconfig12+

PhonePC/2in1TabletTVWearable

canPreconfig(preconfigType: PreconfigType, preconfigRatio?: PreconfigRatio): boolean

查询当前Session是否支持指定的预配置类型。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| preconfigType | [PreconfigType](arkts-apis-camera-e.md#preconfigtype12) | 是 | 指定配置预期分辨率。 |
| preconfigRatio | [PreconfigRatio](arkts-apis-camera-e.md#preconfigratio12) | 否 | 可选画幅比例，默认为16:9。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true: 支持指定预配置类型。  false: 不支持指定预配置类型。 |

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](errorcode-camera.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400201 | Camera service fatal error. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. function testCanPreconfig(videoSession: camera.VideoSession, preconfigType: camera.PreconfigType,
4. preconfigRatio: camera.PreconfigRatio): void {
5. try {
6. let result = videoSession.canPreconfig(preconfigType, preconfigRatio);
7. console.info(`canPreconfig ${preconfigType} ${preconfigRatio} result is : ${result}`);
8. } catch (error) {
9. let err = error as BusinessError;
10. console.error(`The canPreconfig call failed. error code: ${err.code}`);
11. }
12. }
```

## preconfig12+

PhonePC/2in1TabletTVWearable

preconfig(preconfigType: PreconfigType, preconfigRatio?: PreconfigRatio): void

对当前Session进行预配置。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| preconfigType | [PreconfigType](arkts-apis-camera-e.md#preconfigtype12) | 是 | 指定配置预期分辨率。 |
| preconfigRatio | [PreconfigRatio](arkts-apis-camera-e.md#preconfigratio12) | 否 | 可选画幅比例，默认为16:9。 |

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](errorcode-camera.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400201 | Camera service fatal error. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. function testPreconfig(videoSession: camera.VideoSession, preconfigType: camera.PreconfigType,
4. preconfigRatio: camera.PreconfigRatio): void {
5. try {
6. videoSession.preconfig(preconfigType, preconfigRatio);
7. console.info(`preconfig ${preconfigType} ${preconfigRatio} success`);
8. } catch (error) {
9. let err = error as BusinessError;
10. console.error(`The preconfig call failed. error code: ${err.code}`);
11. }
12. }
```

## on('error')11+

PhonePC/2in1TabletTVWearable

on(type: 'error', callback: ErrorCallback): void

监听普通录像会话的错误事件，通过注册回调函数获取结果。使用callback异步回调。

说明

当前注册监听接口，不支持在on监听的回调方法里，调用off注销回调。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'error'，session创建成功之后可监听该接口。session调用相关接口出现错误时会触发该事件，比如调用[beginConfig](arkts-apis-camera-session.md#beginconfig11)，[commitConfig](arkts-apis-camera-session.md#commitconfig11)，[addInput](arkts-apis-camera-session.md#addinput11)等接口发生错误时返回错误信息。 |
| callback | [ErrorCallback](js-apis-base.md#errorcallback) | 是 | 回调函数，用于获取错误信息。返回错误码，错误码类型[CameraErrorCode](arkts-apis-camera-e.md#cameraerrorcode)。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. function callback(err: BusinessError): void {
4. console.error(`Video session error code: ${err.code}`);
5. }

7. function registerSessionError(videoSession: camera.VideoSession): void {
8. videoSession.on('error', callback);
9. }
```

## off('error')11+

PhonePC/2in1TabletTVWearable

off(type: 'error', callback?: ErrorCallback): void

注销监听普通录像会话的错误事件，通过注册回调函数获取结果。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'error'，session创建成功之后可监听该接口。 |
| callback | [ErrorCallback](js-apis-base.md#errorcallback) | 否 | 回调函数，如果指定参数则取消对应callback（callback对象不可是匿名函数），否则取消所有callback。 |

**示例：**

```
1. function unregisterSessionError(videoSession: camera.VideoSession): void {
2. videoSession.off('error');
3. }
```

## on('focusStateChange')11+

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

11. function registerFocusStateChange(videoSession: camera.VideoSession): void {
12. videoSession.on('focusStateChange', callback);
13. }
```

## off('focusStateChange')11+

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
1. function unregisterFocusStateChange(videoSession: camera.VideoSession): void {
2. videoSession.off('focusStateChange');
3. }
```

## on('smoothZoomInfoAvailable')11+

PhonePC/2in1TabletTVWearable

on(type: 'smoothZoomInfoAvailable', callback: AsyncCallback<SmoothZoomInfo>): void

监听相机平滑变焦的状态变化，通过注册回调函数获取结果。使用callback异步回调。

说明

当前注册监听接口，不支持在on监听的回调方法里，调用off注销回调。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'smoothZoomInfoAvailable'，session创建成功可监听。 |
| callback | AsyncCallback<[SmoothZoomInfo](arkts-apis-camera-i.md#smoothzoominfo11)> | 是 | 回调函数，用于获取当前平滑变焦状态。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. function callback(err: BusinessError, smoothZoomInfo: camera.SmoothZoomInfo): void {
4. if (err !== undefined && err.code !== 0) {
5. console.error(`Callback Error, errorCode: ${err.code}`);
6. return;
7. }
8. console.info(`The duration of smooth zoom: ${smoothZoomInfo.duration}`);
9. }

11. function registerSmoothZoomInfo(videoSession: camera.VideoSession): void {
12. videoSession.on('smoothZoomInfoAvailable', callback);
13. }
```

## off('smoothZoomInfoAvailable')11+

PhonePC/2in1TabletTVWearable

off(type: 'smoothZoomInfoAvailable', callback?: AsyncCallback<SmoothZoomInfo>): void

注销监听相机平滑变焦的状态变化。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'smoothZoomInfoAvailable'，session创建成功可监听。 |
| callback | AsyncCallback<[SmoothZoomInfo](arkts-apis-camera-i.md#smoothzoominfo11)> | 否 | 回调函数，如果指定参数则取消对应callback（callback对象不可是匿名函数），否则取消所有callback。 |

**示例：**

```
1. function unregisterSmoothZoomInfo(videoSession: camera.VideoSession): void {
2. videoSession.off('smoothZoomInfoAvailable');
3. }
```

## on('autoDeviceSwitchStatusChange')13+

PhonePC/2in1TabletTVWearable

on(type: 'autoDeviceSwitchStatusChange', callback: AsyncCallback<AutoDeviceSwitchStatus>): void

监听相机自动切换镜头状态变化，通过注册回调函数获取结果。使用callback异步回调。

说明

当前注册监听接口，不支持在on监听的回调方法里，调用off注销回调。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'autoDeviceSwitchStatusChange'，session创建成功可监听。 |
| callback | AsyncCallback<[AutoDeviceSwitchStatus](arkts-apis-camera-i.md#autodeviceswitchstatus13)> | 是 | 回调函数，用于获取当前自动切换镜头的状态。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. function callback(err: BusinessError, autoDeviceSwitchStatus: camera.AutoDeviceSwitchStatus): void {
4. if (err !== undefined && err.code !== 0) {
5. console.error(`Callback Error, errorCode: ${err.code}`);
6. return;
7. }
8. console.info(`isDeviceSwitched: ${autoDeviceSwitchStatus.isDeviceSwitched}, isDeviceCapabilityChanged: ${autoDeviceSwitchStatus.isDeviceCapabilityChanged}`);
9. }

11. function registerAutoDeviceSwitchStatus(videoSession: camera.VideoSession): void {
12. videoSession.on('autoDeviceSwitchStatusChange', callback);
13. }
```

## off('autoDeviceSwitchStatusChange')13+

PhonePC/2in1TabletTVWearable

off(type: 'autoDeviceSwitchStatusChange', callback?: AsyncCallback<AutoDeviceSwitchStatus>): void

注销监听相机自动切换镜头状态变化。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'autoDeviceSwitchStatusChange'，session创建成功可监听。 |
| callback | AsyncCallback<[AutoDeviceSwitchStatus](arkts-apis-camera-i.md#autodeviceswitchstatus13)> | 否 | 回调函数，如果指定参数则取消对应callback（callback对象不可是匿名函数），否则取消所有callback。 |

**示例：**

```
1. function unregisterSmoothZoomInfo(videoSession: camera.VideoSession): void {
2. videoSession.off('autoDeviceSwitchStatusChange');
3. }
```

## setQualityPrioritization14+

PhonePC/2in1TabletTVWearable

setQualityPrioritization(quality : QualityPrioritization) : void;

设置录像质量优先级。

说明

* 默认为高录像质量，设置为功耗平衡将降低录像质量以减少功耗。实际功耗收益因平台而异。
* 建议该接口在[commitConfig](arkts-apis-camera-session.md#commitconfig11)和[start](arkts-apis-camera-session.md#start11-1)之间调用。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| quality | [QualityPrioritization](arkts-apis-camera-e.md#qualityprioritization14) | 是 | 需要设置的视频质量优先级（默认为高录像质量）。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[Camera错误码](errorcode-camera.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 7400103 | Session not config. The session has not been committed or configured. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. function setQualityPrioritization(videoSession: camera.VideoSession): void {
4. try {
5. videoSession.setQualityPrioritization(camera.QualityPrioritization.POWER_BALANCE);
6. } catch (error) {
7. // 失败返回错误码error.code并处理。
8. let err = error as BusinessError;
9. console.error(`The setQualityPrioritization call failed. error code: ${err.code}`);
10. }
11. }
```

## on('systemPressureLevelChange')20+

PhonePC/2in1TabletTVWearable

on(type: 'systemPressureLevelChange', callback: AsyncCallback<SystemPressureLevel>): void

监听系统压力状态变化，通过注册回调函数获取结果。使用callback异步回调。

说明

当前注册监听接口，不支持在on监听的回调方法里，调用off注销回调。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'systemPressureLevelChange'，session创建成功可监听。 |
| callback | AsyncCallback<[SystemPressureLevel](arkts-apis-camera-e.md#systempressurelevel20)> | 是 | 回调函数，用于获取当前系统压力状态。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. function callback(err: BusinessError, systemPressureLevel: camera.SystemPressureLevel): void {
4. if (err !== undefined && err.code !== 0) {
5. console.error(`Callback Error, errorCode: ${err.code}`);
6. return;
7. }
8. console.info(`systemPressureLevel: ${systemPressureLevel}`);
9. }

11. function registerSystemPressureLevelChangeCallback(videoSession: camera.VideoSession): void {
12. videoSession.on('systemPressureLevelChange', callback);
13. }
```

## off('systemPressureLevelChange')20+

PhonePC/2in1TabletTVWearable

off(type: 'systemPressureLevelChange', callback?: AsyncCallback<SystemPressureLevel>): void

注销监听系统压力状态变化。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 注销监听事件，固定为'systemPressureLevelChange'，session创建成功可触发此事件。 |
| callback | AsyncCallback<[SystemPressureLevel](arkts-apis-camera-e.md#systempressurelevel20)> | 否 | 回调函数，如果指定参数则取消对应callback (callback对象不可是匿名函数)，否则参数默认为空，取消所有callback。 |

**示例：**

```
1. function unregisterSystemPressureLevelChangeCallback(videoSession: camera.VideoSession): void {
2. videoSession.off('systemPressureLevelChange');
3. }
```

## on('controlCenterEffectStatusChange')20+

PhonePC/2in1TabletTVWearable

on(type: 'controlCenterEffectStatusChange', callback: AsyncCallback<ControlCenterStatusInfo>): void

监听相机控制器效果激活状态变化，通过注册回调函数获取结果。使用callback异步回调。

说明

当前注册监听接口，不支持在on监听的回调方法里，调用off注销回调。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'controlCenterEffectStatusChange'，session创建成功可监听。 |
| callback | AsyncCallback<[ControlCenterStatusInfo](arkts-apis-camera-i.md#controlcenterstatusinfo20)> | 是 | 回调函数，用于获取当前控制器激活状态。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. function callback(err: BusinessError, status: camera.ControlCenterStatusInfo): void {
4. if (err !== undefined && err.code !== 0) {
5. console.error(`Callback Error, errorCode: ${err.code}`);
6. return;
7. }
8. console.info(`controlCenterEffectStatusChange: ${status}`);
9. }

11. function registerControlCenterEffectStatusChangeCallback(videoSession: camera.VideoSession): void {
12. videoSession.on('controlCenterEffectStatusChange', callback);
13. }
```

## off('controlCenterEffectStatusChange')20+

PhonePC/2in1TabletTVWearable

off(type: 'controlCenterEffectStatusChange', callback?: AsyncCallback<ControlCenterStatusInfo>): void

注销监听相机控制器激活状态变化。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 注销监听事件，固定为'controlCenterEffectStatusChange'，session创建成功可触发此事件。 |
| callback | AsyncCallback<[ControlCenterStatusInfo](arkts-apis-camera-i.md#controlcenterstatusinfo20)> | 否 | 回调函数，如果指定参数则取消对应callback (callback对象不可是匿名函数)，否则参数默认为空，取消所有callback。 |

**示例：**

```
1. function unregisterControlCenterEffectStatusChange(videoSession: camera.VideoSession): void {
2. videoSession.off('controlCenterEffectStatusChange');
3. }
```

## on('macroStatusChanged')20+

PhonePC/2in1TabletTVWearable

on(type: 'macroStatusChanged', callback: AsyncCallback<boolean>): void

监听相机微距状态变化，通过注册回调函数获取结果。使用callback异步回调。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'macroStatusChanged'，session创建成功可监听。 |
| callback | AsyncCallback<boolean> | 是 | 回调函数，用于获取当前微距状态，返回true是开启状态，返回false是禁用状态。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. function callback(err: BusinessError, macroStatus: boolean): void {
4. if (err !== undefined && err.code !== 0) {
5. console.error(`Callback Error, errorCode: ${err.code}`);
6. return;
7. }
8. console.info(`Macro state: ${macroStatus}`);
9. }

11. function registerMacroStatusChanged(videoSession: camera.VideoSession): void {
12. videoSession.on('macroStatusChanged', callback);
13. }
```

## off('macroStatusChanged')20+

PhonePC/2in1TabletTVWearable

off(type: 'macroStatusChanged', callback?: AsyncCallback<boolean>): void

注销相机微距状态变化的监听。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 注销监听事件，固定为'macroStatusChanged'，session创建成功可触发此事件。 |
| callback | AsyncCallback<boolean> | 否 | 回调函数，如果指定参数则取消对应callback（callback对象不可是匿名函数），否则参数默认为空，取消所有callback, 返回true表示成功，false表示失败。 |

**示例：**

```
1. function unregisterMacroStatusChanged(videoSession: camera.VideoSession): void {
2. videoSession.off('macroStatusChanged');
3. }
```

## onIsoInfoChange22+

PhonePC/2in1TabletTVWearable

onIsoInfoChange(callback: Callback<IsoInfo>): void

监听相机感光度（ISO）状态变化，通过注册回调函数获取最新ISO值。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<[IsoInfo](arkts-apis-camera-i.md#isoinfo22)> | 是 | 回调函数，用于获取相机当前的ISO值。 |

**示例：**

```
1. function callback(isoInfo: camera.IsoInfo): void {
2. console.info(`Iso : ${isoInfo}`);
3. }

5. function registerIsoInfoChanged(videoSession: camera.VideoSession): void {
6. videoSession.onIsoInfoChange(callback);
7. }
```

## offIsoInfoChange22+

PhonePC/2in1TabletTVWearable

offIsoInfoChange(callback?: Callback<IsoInfo>): void

取消监听相机感光度（ISO）状态的变化。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<[IsoInfo](arkts-apis-camera-i.md#isoinfo22)> | 否 | 回调函数，可选。  如果指定callback参数则注销该callback监听，callback不可是匿名函数。  如果未指定callback，则注销所有已存在的callback监听。 |

**示例：**

```
1. function callback(isoInfo: camera.IsoInfo): void {
2. console.info(`Iso : ${isoInfo}`);
3. }

5. function unregisterIsoInfoChanged(videoSession: camera.VideoSession): void {
6. videoSession.offIsoInfoChange(callback);
7. }

9. function unregisterAllIsoInfoChanged(videoSession: camera.VideoSession): void {
10. videoSession.offIsoInfoChange();
11. }
```
