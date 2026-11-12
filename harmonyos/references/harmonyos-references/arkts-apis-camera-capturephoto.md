---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-camera-capturephoto
title: Interface (CapturePhoto)
breadcrumb: API参考 > 媒体 > Camera Kit（相机服务） > ArkTS API > @ohos.multimedia.camera (相机管理) > Interface (CapturePhoto)
category: harmonyos-references
scraped_at: 2026-11-12T09:56:31+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:30f38f8eec204fa090db69ccdac9e8956d7a4cf87defd68028c8c2f2969cf4b8
---

获取全质量图和未压缩图的对象。

**说明** 

本模块首批接口从API version 23开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

```ts
import { camera } from '@kit.CameraKit';
```

## 属性

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| main | [ImageType](arkts-apis-camera-t.md#imagetype) | 否 | 否 | 全质量图和未压缩图的对象。  **元服务API：** 从API version 23开始，该接口支持在元服务中使用。 |
| oxygenPhoto | [ImageType](arkts-apis-camera-t.md#imagetype) | 否 | 是 | 血氧辅助图对象，用于血氧检测分析。  **起始版本：** 26.0.1  **元服务API：** 从API版本26.0.1开始，该接口支持在元服务中使用。 |
| pigmentationPhoto | [ImageType](arkts-apis-camera-t.md#imagetype) | 否 | 是 | 色斑辅助图对象，用于皮肤色斑分析。  **起始版本：** 26.0.1  **元服务API：** 从API版本26.0.1开始，该接口支持在元服务中使用。 |

## release

release(): Promise<void>

释放输出资源。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**示例：**

```ts
import { camera } from '@kit.CameraKit';

async function releaseCapturePhoto(capturePhoto: camera.CapturePhoto): Promise<void> {
  await capturePhoto.release();
}
```
