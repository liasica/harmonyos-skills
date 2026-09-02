---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-hdrcapability
title: "@ohos.graphics.hdrCapability (HDR能力)"
breadcrumb: API参考 > 图形 > ArkGraphics 2D（方舟2D图形服务） > ArkTS API > @ohos.graphics.hdrCapability (HDR能力)
category: harmonyos-references
scraped_at: 2026-09-02T15:02:42+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:9b22125ed0d4c928353236ef41707a50dfc988c93e0f009329341d38d0954b33
---

本模块提供HDR（高动态显示范围）能力涉及到的相关枚举类型。HDR技术能够显著扩展图像的动态范围和色彩表现力，适用于视频播放、图像显示等场景，可解决传统SDR在高对比度场景下亮部过曝、暗部细节丢失的问题，带来更真实、更丰富的视觉体验。

**说明** 

本模块首批接口从API version 11开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

```ts
import { hdrCapability } from '@kit.ArkGraphics2D';
```

## HDRFormat

HDR格式枚举。

**系统能力：** SystemCapability.Graphic.Graphic2D.ColorManager.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| NONE | 0 | 不支持HDR类型。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| VIDEO\_HLG | 1 | 支持视频的HLG格式。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| VIDEO\_HDR10 | 2 | 支持视频的HDR10格式。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| VIDEO\_HDR\_VIVID | 3 | 支持视频的HDR\_VIVID格式。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| IMAGE\_HDR\_VIVID\_DUAL | 4 | 支持图片的HDR\_VIVID格式，以dual JPEG格式存储。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| IMAGE\_HDR\_VIVID\_SINGLE | 5 | 支持图片的HDR\_VIVID格式，以single HEIF格式存储。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| IMAGE\_HDR\_ISO\_DUAL | 6 | 支持图片的HDR\_ISO格式，以dual JPEG格式存储。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| IMAGE\_HDR\_ISO\_SINGLE | 7 | 支持图片的HDR\_ISO格式，以single HEIF格式存储。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| VIDEO\_AIHDR24+ | 8 | 支持视频的AIHDR格式。  **元服务API：** 从API version 24开始，该接口支持在元服务中使用。  **模型约束**：此接口仅可在Stage模型下使用。 |
