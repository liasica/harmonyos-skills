---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-camera-macro
title: Interface (Macro)
breadcrumb: API参考 > 媒体 > Camera Kit（相机服务） > ArkTS API > @ohos.multimedia.camera (相机管理) > Interface (Macro)
category: harmonyos-references
scraped_at: 2026-04-28T08:12:36+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:79c2133c2c6a4b2508d749e11cd6a654c4840ac077ce629dc04ec6007b7c6af6
---

Macro 继承自 [MacroQuery](arkts-apis-camera-macroquery.md)。

提供使能微距能力的接口。

说明

* 本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 本Interface首批接口从API version 19开始支持。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { camera } from '@kit.CameraKit';
```

## enableMacro19+

PhonePC/2in1TabletTVWearable

enableMacro(enabled: boolean): void

使能当前的微距能力。

说明

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

```
1. function enableMacro(photoSession: camera.PhotoSession): void {
2. let isSupported: boolean = photoSession.isMacroSupported();
3. if (isSupported) {
4. photoSession.enableMacro(true);
5. }
6. }
```
