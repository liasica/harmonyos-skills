---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-camera-manualexposurequery
title: Interface (ManualExposureQuery)
breadcrumb: API参考 > 媒体 > Camera Kit（相机服务） > ArkTS API > @ohos.multimedia.camera (相机管理) > Interface (ManualExposureQuery)
category: harmonyos-references
scraped_at: 2026-09-02T15:02:26+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:4c720455160b96cee1d335d6bfc289632b2edbe2e74d56d25955376115eb7ecf
---

手动曝光查询对象。

**说明** 

* 本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 本Interface首批接口从API version 24开始支持。

## 导入模块

```ts
import { camera } from '@kit.CameraKit';
```

## getSupportedExposureDurationRange24+

getSupportedExposureDurationRange(): Array<number>

获取支持的手动曝光时长范围。单位：微秒。

**元服务API：** 从API version 24开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<number> | 支持的手动曝光时长范围。 |

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](errorcode-camera.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400102 | Operation not allowed, session or inputdevice maybe abnormal. |
| 7400103 | Session not config, only throw in session usage. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

function getSupportedExposureDurationRange(photoSession: camera.PhotoSession): Array<number> {
  let durationRange: Array<number> = [];
  try {
    durationRange = photoSession.getSupportedExposureDurationRange();
  } catch (error) {
    let err = error as BusinessError;
    console.error(`The getSupportedExposureDurationRange call failed. error code: ${err.code}`);
  }
  return durationRange;
}
```

## getExposureBiasStep24+

getExposureBiasStep(): number

获取曝光偏置步长。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API version 24开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 曝光偏置步长。 |

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](errorcode-camera.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400102 | Operation not allowed, session or inputdevice maybe abnormal. |
| 7400103 | Session not config. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

function getExposureBiasStep(photoSession: camera.PhotoSession): number {
  let biasStep = 0.0;
  try {
    biasStep = photoSession.getExposureBiasStep();
  } catch (error) {
    let err = error as BusinessError;
    console.error(`The getExposureBiasStep call failed. error code: ${err.code}`);
  }
  return biasStep;
}
```
