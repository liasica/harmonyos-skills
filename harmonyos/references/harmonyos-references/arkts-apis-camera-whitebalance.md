---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-camera-whitebalance
title: Interface (WhiteBalance)
breadcrumb: API参考 > 媒体 > Camera Kit（相机服务） > ArkTS API > @ohos.multimedia.camera (相机管理) > Interface (WhiteBalance)
category: harmonyos-references
scraped_at: 2026-09-02T15:02:26+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:bafbc1da7d9f0d7ba79ca1feffe4ec7e4cfc68b58f709f1780444707ba7ab3b2
---

WhiteBalance继承自[WhiteBalanceQuery](arkts-apis-camera-whitebalancequery.md)。

提供了处理设备白平衡的相关功能，包括获取和设置白平衡模式以及白平衡值。

**说明** 

* 本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 本Interface首批接口从API version 20开始支持。

## 导入模块

```ts
import { camera } from '@kit.CameraKit';
```

## setWhiteBalanceMode20+

setWhiteBalanceMode(mode: WhiteBalanceMode): void

设置白平衡模式。设置之前需要先检查设备是否支持指定的白平衡模式，具体方法请参考[isWhiteBalanceModeSupported](arkts-apis-camera-whitebalancequery.md#iswhitebalancemodesupported20)。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mode | [WhiteBalanceMode](arkts-apis-camera-e.md#whitebalancemode20) | 是 | 白平衡模式。 |

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](errorcode-camera.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400101 | Parameter missing or parameter type incorrect. |
| 7400103 | Session not config. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

function setWhiteBalanceMode(session: camera.PhotoSession | camera.VideoSession): void {
  try {
    session.setWhiteBalanceMode(camera.WhiteBalanceMode.DAYLIGHT);
  } catch (error) {
    let err = error as BusinessError;
    console.error(`The setWhiteBalanceMode call failed. error code: ${err.code}`);
  }
}
```

## getWhiteBalanceMode20+

getWhiteBalanceMode(): WhiteBalanceMode

获取当前白平衡模式。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [WhiteBalanceMode](arkts-apis-camera-e.md#whitebalancemode20) | 获取当前白平衡模式。若接口调用失败，返回undefined。 |

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](errorcode-camera.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400103 | Session not config. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

function getWhiteBalanceMode(session: camera.PhotoSession | camera.VideoSession): camera.WhiteBalanceMode | undefined {
  let whiteBalanceMode: camera.WhiteBalanceMode | undefined = undefined;
  try {
    whiteBalanceMode = session.getWhiteBalanceMode();
  } catch (error) {
    let err = error as BusinessError;
    console.error(`The getWhiteBalanceMode call failed. error code: ${err.code}`);
  }
  return whiteBalanceMode;
}
```

## setWhiteBalance20+

setWhiteBalance(whiteBalance: number): void

设置手动白平衡值。

设置之前需要先检查设备支持的白平衡值范围，具体方法请参考[getWhiteBalanceRange](arkts-apis-camera-whitebalancequery.md#getwhitebalancerange20)。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| whiteBalance | number | 是 | 设置手动白平衡值，单位为K（Kelvin，温度单位）。 |

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](errorcode-camera.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400101 | Parameter missing or parameter type incorrect. |
| 7400103 | Session not config. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

function setWhiteBalance(session: camera.PhotoSession | camera.VideoSession): void {
  try {
    let whiteBalance: number = 1000;
    session.setWhiteBalance(whiteBalance);
  } catch (error) {
    let err = error as BusinessError;
    console.error(`The setWhiteBalance call failed. error code: ${err.code}`);
  }
}
```

## getWhiteBalance20+

getWhiteBalance(): number

获取当前手动白平衡的值。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 返回当前白平衡值，单位为K（Kelvin，温度单位）。 |

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](errorcode-camera.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400103 | Session not config. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

function getWhiteBalance(session: camera.PhotoSession | camera.VideoSession): number {
  let whiteBalance: number = 0;
  try {
    whiteBalance = session.getWhiteBalance();
  } catch (error) {
    let err = error as BusinessError;
    console.error(`The getWhiteBalance call failed. error code: ${err.code}`);
  }
  return whiteBalance;
}
```

## setColorTint

setColorTint(colorTint: number): void

设置白平衡的色调调节值。

设置之前需要先检查设备支持配置的白平衡色调调节范围，具体方法请参考[getColorTintRange](arkts-apis-camera-whitebalancequery.md#getcolortintrange)。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| colorTint | number | 是 | 设置手动白平衡色调调节值。 |

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](errorcode-camera.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400103 | Session not config. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

function setColorTint(session: camera.PhotoSession | camera.VideoSession): void {
  let colorTint: number = 0;
  try {
    session.setColorTint(colorTint);
  } catch (error) {
    let err = error as BusinessError;
    console.error(`The setColorTint call failed. error code: ${err.code}`);
  }
}
```

## getColorTint

getColorTint(): number

获取当前白平衡的色调调节值。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 返回当前白平衡色调调节值。 |

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](errorcode-camera.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400103 | Session not config. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

function getColorTint(session: camera.PhotoSession | camera.VideoSession): number {
  let colorTint: number = 0;
  try {
    colorTint = session.getColorTint();
  } catch (error) {
    let err = error as BusinessError;
    console.error(`The getColorTint call failed. error code: ${err.code}`);
  }
  return colorTint;
}
```
