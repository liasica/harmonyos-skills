---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-camera-manualisoquery
title: Interface (ManualIsoQuery)
breadcrumb: API参考 > 媒体 > Camera Kit（相机服务） > ArkTS API > @ohos.multimedia.camera (相机管理) > Interface (ManualIsoQuery)
category: harmonyos-references
scraped_at: 2026-09-02T15:02:26+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:3b23096968fd0f55bf5ab4980486ab809bacf2e5ab23ff8a1003c6df5d66a9bc
---

手动ISO查询对象。

**说明** 

* 本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 本Interface首批接口从API version 24开始支持。

## 导入模块

```ts
import { camera } from '@kit.CameraKit';
```

## getSupportedIsoRange24+

getSupportedIsoRange(): number[]

获取支持的标准ISO感光度值数组。

**元服务API：** 从API version 24开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number[] | ISO感光度值数组。 |

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](errorcode-camera.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400102 | Operation not allowed, the inputDevice or the session is abnormal. |
| 7400103 | Session not config, only throw in session usage. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

function getSupportedIsoRange(photoSession: camera.PhotoSession): number[] {
  let isoRange: number[] = [];
  try {
    isoRange = photoSession.getSupportedIsoRange();
  } catch (error) {
    let err = error as BusinessError;
    console.error(`The getSupportedIsoRange call failed. error code: ${err.code}`);
  }
  return isoRange;
}
```
