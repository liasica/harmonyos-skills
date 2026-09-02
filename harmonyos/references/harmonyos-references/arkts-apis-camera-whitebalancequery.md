---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-camera-whitebalancequery
title: Interface (WhiteBalanceQuery)
breadcrumb: API参考 > 媒体 > Camera Kit（相机服务） > ArkTS API > @ohos.multimedia.camera (相机管理) > Interface (WhiteBalanceQuery)
category: harmonyos-references
scraped_at: 2026-09-02T15:02:26+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:d6e11d465f0240e2128b759eb2be47c12a115f35e30791c1c9fc9402f9b475da
---

提供了查询设备对指定的白平衡模式是否支持，以及获取设备支持的白平衡模式范围的方法。

**说明** 

* 本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 本Interface首批接口从API version 20开始支持。

## 导入模块

```ts
import { camera } from '@kit.CameraKit';
```

## isWhiteBalanceModeSupported20+

isWhiteBalanceModeSupported(mode: WhiteBalanceMode): boolean

检测是否支持当前传入的白平衡模式。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mode | [WhiteBalanceMode](arkts-apis-camera-e.md#whitebalancemode20) | 是 | 白平衡模式。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 表示是否支持白平衡模式。true表示支持，false表示不支持。若接口调用失败，返回undefined。 |

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](errorcode-camera.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400101 | Parameter missing or parameter type incorrect. |
| 7400103 | Session not config, only throw in session usage. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

function isWhiteBalanceModeSupported(session: camera.PhotoSession | camera.VideoSession): boolean {
  let status: boolean = false;
  try {
  let mode: camera.WhiteBalanceMode = camera.WhiteBalanceMode.DAYLIGHT;
    status = session.isWhiteBalanceModeSupported(mode);
  } catch (error) {
    let err = error as BusinessError;
    console.error(`The isWhiteBalanceModeSupported call failed. error code: ${err.code}`);
  }
  return status;
}
```

## getWhiteBalanceRange20+

getWhiteBalanceRange(): Array<number>

获取手动白平衡模式下，白平衡值的范围。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<number> | 用于获取手动白平衡值的可调范围，如[2800，10000]，单位为K（Kelvin，温度单位），实际情况根据底层能力返回为准。若接口调用失败，返回undefined。 |

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](errorcode-camera.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400103 | Session not config, only throw in session usage. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

function getWhiteBalanceRange(session: camera.PhotoSession | camera.VideoSession): Array<number> {
  let range: Array<number> = [];
  try {
    range = session.getWhiteBalanceRange();
  } catch (error) {
    let err = error as BusinessError;
    console.error(`The getWhiteBalanceRange call failed. error code: ${err.code}`);
  }
  return range;
}
```

## getColorTintRange

getColorTintRange(): Array<number>

获取支持配置的白平衡色调调节范围。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<number> | 用于获取色调调节值的可调范围。若接口调用失败，返回undefined。 |

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](errorcode-camera.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400103 | Session not config, only throw in session usage. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

function getColorTintRange(session: camera.PhotoSession | camera.VideoSession): Array<number> {
  let range: Array<number> = [];
  try {
    range = session.getColorTintRange();
  } catch (error) {
    let err = error as BusinessError;
    console.error(`The getColorTintRange call failed. error code: ${err.code}`);
  }
  return range;
}
```
