---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-camera-macro
title: Interface (Macro)
breadcrumb: API参考 > 媒体 > Camera Kit（相机服务） > ArkTS API > @ohos.multimedia.camera (相机管理) > Interface (Macro)
category: harmonyos-references
scraped_at: 2026-09-02T15:02:26+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:d4aa3a567bf187d0cf7799e00564d5e0bbd28df906ed0642beae3dc026b83270
---

Macro继承自[MacroQuery](arkts-apis-camera-macroquery.md)。

提供使能微距能力的接口。

**说明** 

* 本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 本Interface首批接口从API version 19开始支持。

## 导入模块

```ts
import { camera } from '@kit.CameraKit';
```

## enableMacro19+

enableMacro(enabled: boolean): void

使能当前的微距能力。

**说明** 

使用该接口前，需要先通过[isMacroSupported](arkts-apis-camera-macroquery.md#ismacrosupported19)接口查询当前设备是否支持微距能力。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enabled | boolean | 是 | 是否开启微距能力。true表示开启微距能力，false表示关闭微距能力。 |

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](errorcode-camera.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400102 | Operation not allowed. |
| 7400103 | Session not config. |

**示例：**

```ts
function enableMacro(photoSession: camera.PhotoSession): void {
  let isSupported: boolean = photoSession.isMacroSupported();
  if (isSupported) {
    photoSession.enableMacro(true);
  }
}
```
