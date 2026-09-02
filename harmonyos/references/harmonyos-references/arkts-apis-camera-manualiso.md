---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-camera-manualiso
title: Interface (ManualIso)
breadcrumb: API参考 > 媒体 > Camera Kit（相机服务） > ArkTS API > @ohos.multimedia.camera (相机管理) > Interface (ManualIso)
category: harmonyos-references
scraped_at: 2026-09-02T15:02:26+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:0b31e77c1f3524c54fe926f60127391dd9e56c70b4c274ca36f2233a4fef9d0c
---

ManualIso继承自[ManualIsoQuery](arkts-apis-camera-manualisoquery.md)。

手动ISO对象。

**说明** 

* 本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 本Interface首批接口从API version 24开始支持。

## 导入模块

```ts
import { camera } from '@kit.CameraKit';
```

## getIso24+

getIso(): number

获取当前ISO值。

**元服务API：** 从API version 24开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 当前ISO值。 |

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](errorcode-camera.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400102 | Operation not allowed, the inputDevice or the session is abnormal. |
| 7400103 | Session not config. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

function getIso(photoSession: camera.PhotoSession): number {
  let iso: number = 0;
  try {
    iso = photoSession.getIso();
  } catch (error) {
    // 失败返回错误码error.code并处理。
    let err = error as BusinessError;
    console.error(`The getIso call failed. error code: ${err.code}`);
  }
  return iso;
}
```

## setIso24+

setIso(iso: number): void

设置ISO感光度值。

当曝光锁定模式[ExposureMode](arkts-apis-camera-e.md#exposuremode)为EXPOSURE\_MODE\_LOCKED时，不支持设置ISO感光度值。设置的值需在[getSupportedIsoRange](arkts-apis-camera-manualisoquery.md#getsupportedisorange24)范围内。

**元服务API：** 从API version 24开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| iso | number | 是 | ISO感光度值。 |

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](errorcode-camera.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400102 | Operation not allowed, the inputDevice or the session is abnormal. |
| 7400103 | Session not config. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

function setIso(photoSession: camera.PhotoSession, iso: number): void {
  try {
    photoSession.setIso(iso);
  } catch (error) {
    // 失败返回错误码error.code并处理。
    let err = error as BusinessError;
    console.error(`The setIso call failed. error code: ${err.code}`);
  }
}
```
