---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-camera-autoexposure
title: Interface (AutoExposure)
breadcrumb: API参考 > 媒体 > Camera Kit（相机服务） > ArkTS API > @ohos.multimedia.camera (相机管理) > Interface (AutoExposure)
category: harmonyos-references
scraped_at: 2026-04-28T08:12:32+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:adf807ebeed8e882c8edab9ae20e60454b9faa095c33d530c54e09691c581d03
---

AutoExposure 继承自 [AutoExposureQuery](arkts-apis-camera-autoexposurequery.md)。

自动曝光类，对设备自动曝光（AE）操作。

说明

* 本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 本Interface首批接口从API version 11开始支持。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { camera } from '@kit.CameraKit';
```

## getExposureMode11+

PhonePC/2in1TabletTVWearable

getExposureMode(): ExposureMode

获取当前曝光模式。

说明

若未通过[setExposureMode](arkts-apis-camera-autoexposure.md#setexposuremode11)接口进行设置，直接调用该接口查询当前曝光模式，会返回无效值。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ExposureMode](arkts-apis-camera-e.md#exposuremode) | 获取当前曝光模式。接口调用失败会抛出相应错误码并返回undefined，错误码类型[CameraErrorCode](arkts-apis-camera-e.md#cameraerrorcode)。 |

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](errorcode-camera.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400103 | Session not config. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. function getExposureMode(photoSession: camera.PhotoSession): camera.ExposureMode | undefined {
4. let exposureMode: camera.ExposureMode | undefined = undefined;
5. try {
6. exposureMode = photoSession.getExposureMode();
7. } catch (error) {
8. // 失败返回错误码error.code并处理。
9. let err = error as BusinessError;
10. console.error(`The getExposureMode call failed. error code: ${err.code}`);
11. }
12. return exposureMode;
13. }
```

## setExposureMode11+

PhonePC/2in1TabletTVWearable

setExposureMode(aeMode: ExposureMode): void

设置曝光模式。进行设置之前，需要先检查设备是否支持指定的曝光模式，可使用方法[isExposureModeSupported](arkts-apis-camera-autoexposurequery.md#isexposuremodesupported11)。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| aeMode | [ExposureMode](arkts-apis-camera-e.md#exposuremode) | 是 | 曝光模式。传参为null或者undefined，作为0处理，曝光锁定。 |

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](errorcode-camera.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400102 | Operation not allowed. |
| 7400103 | Session not config. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. function setExposureMode(photoSession: camera.PhotoSession): void {
4. try {
5. photoSession.setExposureMode(camera.ExposureMode.EXPOSURE_MODE_LOCKED);
6. } catch (error) {
7. // 失败返回错误码error.code并处理。
8. let err = error as BusinessError;
9. console.error(`The setExposureMode call failed. error code: ${err.code}`);
10. }
11. }
```

## getMeteringPoint11+

PhonePC/2in1TabletTVWearable

getMeteringPoint(): Point

查询曝光区域中心点。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

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

3. function getMeteringPoint(photoSession: camera.PhotoSession): camera.Point | undefined {
4. let exposurePoint: camera.Point | undefined = undefined;
5. try {
6. exposurePoint = photoSession.getMeteringPoint();
7. } catch (error) {
8. // 失败返回错误码error.code并处理。
9. let err = error as BusinessError;
10. console.error(`The getMeteringPoint call failed. error code: ${err.code}`);
11. }
12. return exposurePoint;
13. }
```

## setMeteringPoint11+

PhonePC/2in1TabletTVWearable

setMeteringPoint(point: Point): void

设置曝光区域中心点，曝光点应在0-1坐标系内，该坐标系左上角为{0，0}，右下角为{1，1}。

此坐标系是以设备充电口在右侧时的横向设备方向为基准的，例如应用的预览界面布局以设备充电口在下侧时的竖向方向为基准，布局宽高为{w，h}，且触摸点为{x，y}，则转换后的坐标点为{y/h，1-x/w}。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| point | [Point](arkts-apis-camera-i.md#point) | 是 | 曝光点，x、y设置范围应在[0，1]之内，超过范围，如果小于0设置0，大于1设置1。 |

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](errorcode-camera.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400103 | Session not config. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. function setMeteringPoint(photoSession: camera.PhotoSession): void {
4. const point: camera.Point = {x: 1, y: 1};
5. try {
6. photoSession.setMeteringPoint(point);
7. } catch (error) {
8. // 失败返回错误码error.code并处理。
9. let err = error as BusinessError;
10. console.error(`The setMeteringPoint call failed. error code: ${err.code}`);
11. }
12. }
```

## setExposureBias11+

PhonePC/2in1TabletTVWearable

setExposureBias(exposureBias: number): void

设置曝光补偿，曝光补偿值（EV）。

进行设置之前，建议先通过方法[getExposureBiasRange](arkts-apis-camera-autoexposurequery.md#getexposurebiasrange11)查询支持的范围。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| exposureBias | number | 是 | 曝光补偿，[getExposureBiasRange](arkts-apis-camera-autoexposurequery.md#getexposurebiasrange11)查询支持的范围，如果设置超过支持范围的值，自动匹配到就近临界点。  曝光补偿存在步长，由于设备差异，步长也存在差异。例如步长为0.5，则设置1.2时，获取到实际生效曝光补偿为1.0。  接口调用失败会返回相应错误码，错误码类型[CameraErrorCode](arkts-apis-camera-e.md#cameraerrorcode)。 |

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](errorcode-camera.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400102 | Operation not allowed. |
| 7400103 | Session not config. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. function setExposureBias(photoSession: camera.PhotoSession, biasRangeArray: Array<number>): void {
4. if (biasRangeArray && biasRangeArray.length > 0) {
5. let exposureBias = biasRangeArray[0];
6. try {
7. photoSession.setExposureBias(exposureBias);
8. } catch (error) {
9. // 失败返回错误码error.code并处理。
10. let err = error as BusinessError;
11. console.error(`The setExposureBias call failed. error code: ${err.code}`);
12. }
13. }
14. }
```

## getExposureValue11+

PhonePC/2in1TabletTVWearable

getExposureValue(): number

查询当前曝光值。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 获取曝光值。曝光补偿存在步长，如步长为0.5。则设置1.2时，获取到实际生效曝光补偿为1.0。  接口调用失败会返回相应错误码，错误码类型[CameraErrorCode](arkts-apis-camera-e.md#cameraerrorcode)。 |

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](errorcode-camera.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400103 | Session not config. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. function getExposureValue(photoSession: camera.PhotoSession): number {
4. const invalidValue: number = -1;
5. let exposureValue: number = invalidValue;
6. try {
7. exposureValue = photoSession.getExposureValue();
8. } catch (error) {
9. // 失败返回错误码error.code并处理。
10. let err = error as BusinessError;
11. console.error(`The getExposureValue call failed. error code: ${err.code}`);
12. }
13. return exposureValue;
14. }
```
