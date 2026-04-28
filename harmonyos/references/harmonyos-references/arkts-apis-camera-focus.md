---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-camera-focus
title: Interface (Focus)
breadcrumb: API参考 > 媒体 > Camera Kit（相机服务） > ArkTS API > @ohos.multimedia.camera (相机管理) > Interface (Focus)
category: harmonyos-references
scraped_at: 2026-04-28T08:12:35+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:c078d68587ec2d967a8394325a0f7e8bccdaaf906bbe077b72a9aa0f3b43ba14
---

Focus 继承自 [FocusQuery](arkts-apis-camera-focusquery.md)。

对焦类，对设备对焦操作。

说明

* 本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 本Interface首批接口从API version 11开始支持。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { camera } from '@kit.CameraKit';
```

## setFocusMode11+

PhonePC/2in1TabletTVWearable

setFocusMode(afMode: FocusMode): void

设置对焦模式。

进行设置之前，需要先检查设备是否支持指定的焦距模式，可使用方法[isFocusModeSupported](arkts-apis-camera-focusquery.md#isfocusmodesupported11)。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| afMode | [FocusMode](arkts-apis-camera-e.md#focusmode) | 是 | 指定的焦距模式。传参为null或者undefined，作为0处理，手动对焦模式。 |

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](errorcode-camera.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400103 | Session not config. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. function setFocusMode(photoSession: camera.PhotoSession): void {
4. try {
5. photoSession.setFocusMode(camera.FocusMode.FOCUS_MODE_AUTO);
6. } catch (error) {
7. // 失败返回错误码error.code并处理。
8. let err = error as BusinessError;
9. console.error(`The setFocusMode call failed. error code: ${err.code}`);
10. }
11. }
```

## getFocusMode11+

PhonePC/2in1TabletTVWearable

getFocusMode(): FocusMode

获取当前的对焦模式。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [FocusMode](arkts-apis-camera-e.md#focusmode) | 获取当前设备的焦距模式。接口调用失败会抛出相应错误码并返回undefined，错误码类型[CameraErrorCode](arkts-apis-camera-e.md#cameraerrorcode)。 |

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](errorcode-camera.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400103 | Session not config. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. function getFocusMode(photoSession: camera.PhotoSession): camera.FocusMode | undefined {
4. let afMode: camera.FocusMode | undefined = undefined;
5. try {
6. afMode = photoSession.getFocusMode();
7. } catch (error) {
8. // 失败返回错误码error.code并处理。
9. let err = error as BusinessError;
10. console.error(`The getFocusMode call failed. error code: ${err.code}`);
11. }
12. return afMode;
13. }
```

## setFocusPoint11+

PhonePC/2in1TabletTVWearable

setFocusPoint(point: Point): void

设置焦点，焦点应在0-1坐标系内，该坐标系左上角为{0，0}，右下角为{1，1}。

此坐标系是以设备充电口在右侧时的横向设备方向为基准的，例如应用的预览界面布局以设备充电口在下侧时的竖向方向为基准，布局宽高为{w，h}，且触碰点为{x，y}，则转换后的坐标点为{y/h，1-x/w}。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| point | [Point](arkts-apis-camera-i.md#point) | 是 | 焦点。x、y设置范围应在[0，1]之内，超过范围，如果小于0设置0，大于1设置1。 |

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](errorcode-camera.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400103 | Session not config. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. function setFocusPoint(photoSession: camera.PhotoSession): void {
4. const focusPoint: camera.Point = {x: 1, y: 1};
5. try {
6. photoSession.setFocusPoint(focusPoint);
7. } catch (error) {
8. // 失败返回错误码error.code并处理。
9. let err = error as BusinessError;
10. console.error(`The setFocusPoint call failed. error code: ${err.code}`);
11. }
12. }
```

## getFocusPoint11+

PhonePC/2in1TabletTVWearable

getFocusPoint(): Point

查询当前的焦点。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Point](arkts-apis-camera-i.md#point) | 用于获取当前的焦点。接口调用失败会返回相应错误码，错误码类型为[CameraErrorCode](arkts-apis-camera-e.md#cameraerrorcode)。 |

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](errorcode-camera.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400103 | Session not config. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. function getFocusPoint(photoSession: camera.PhotoSession): camera.Point | undefined {
4. let point: camera.Point | undefined = undefined;
5. try {
6. point = photoSession.getFocusPoint();
7. } catch (error) {
8. // 失败返回错误码error.code并处理。
9. let err = error as BusinessError;
10. console.error(`The getFocusPoint call failed. error code: ${err.code}`);
11. }
12. return point;
13. }
```

## getFocalLength11+

PhonePC/2in1TabletTVWearable

getFocalLength(): number

查询当前的焦距值。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 用于获取当前焦距，单位mm。接口调用失败会返回相应错误码，错误码类型[CameraErrorCode](arkts-apis-camera-e.md#cameraerrorcode)。 |

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](errorcode-camera.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400103 | Session not config. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. function getFocalLength(photoSession: camera.PhotoSession): number {
4. const invalidValue: number = -1;
5. let focalLength: number = invalidValue;
6. try {
7. focalLength = photoSession.getFocalLength();
8. } catch (error) {
9. // 失败返回错误码error.code并处理。
10. let err = error as BusinessError;
11. console.error(`The getFocalLength call failed. error code: ${err.code}`);
12. }
13. return focalLength;
14. }
```
