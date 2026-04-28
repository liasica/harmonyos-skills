---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-c
title: Constants
breadcrumb: API参考 > 媒体 > Image Kit（图片处理服务） > ArkTS API > @ohos.multimedia.image (图片处理) > Constants
category: harmonyos-references
scraped_at: 2026-04-28T08:13:14+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:2220889ea0b33ef7c8a09c8222fbe27256ffb92b2aa29b25d6305f0f2dba0690
---

说明

本模块首批接口从API version 23开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

| 名称 | 类型 | 值 | 说明 |
| --- | --- | --- | --- |
| XMAGE\_WATERMARK\_MODE\_AT\_THE\_BOTTOM | number | 9 | XMAGE水印固定位于图像底部中央。 |
| XMAGE\_WATERMARK\_MODE\_BORDER | number | 10 | XMAGE水印会自动调整到边界位置，系统根据图像内容选择最适合的边界区域。 |
| CAPTURE\_MODE\_PROFESSIONAL | number | 2 | 拍摄模式：专业模式。 |
| CAPTURE\_MODE\_FRONT\_LENS\_NIGHT\_VIEW | number | 7 | 拍摄模式：前置摄像头夜景模式。 |
| CAPTURE\_MODE\_PANORAMA | number | 8 | 拍摄模式：全景模式。 |
| CAPTURE\_MODE\_TAIL\_LIGHT | number | 9 | 拍摄模式：尾灯模式。 |
| CAPTURE\_MODE\_LIGHT\_GRAFFITI | number | 10 | 拍摄模式：轻涂鸦模式。 |
| CAPTURE\_MODE\_SILKY\_WATER | number | 11 | 拍摄模式：缎面感水流模式。 |
| CAPTURE\_MODE\_STAR\_TRACK | number | 12 | 拍摄模式：星轨模式。 |
| CAPTURE\_MODE\_WIDEAPERTURE | number | 19 | 拍摄模式：广角模式。 |
| CAPTURE\_MODE\_MOVING\_PHOTO | number | 20 | 拍摄模式：动态照片模式。 |
| CAPTURE\_MODE\_PORTRAIT | number | 23 | 拍摄模式：人像模式。 |
| CAPTURE\_MODE\_REAR\_LENS\_NIGHT\_VIEW | number | 42 | 拍摄模式：后镜头夜景模式。 |
| CAPTURE\_MODE\_SUPER\_MACRO | number | 47 | 拍摄模式：超微距模式。 |
| CAPTURE\_MODE\_SNAP\_SHOT | number | 62 | 拍摄模式：抓拍模式。 |

**示例：**

```
1. import { image } from '@kit.ImageKit';

3. const defaultXmageWaterMarkModeAtTheBottom = image.XMAGE_WATERMARK_MODE_AT_THE_BOTTOM;
4. const defaultXmageWaterMarkModeBorder = image.XMAGE_WATERMARK_MODE_BORDER;
5. const defaultCaptureModeProfessional = image.CAPTURE_MODE_PROFESSIONAL;
6. const defaultCaptureModeFrontLensNightView = image.CAPTURE_MODE_FRONT_LENS_NIGHT_VIEW;
7. const defaultCaptureModePanorama = image.CAPTURE_MODE_PANORAMA;
8. const defaultCaptureModeTailLight = image.CAPTURE_MODE_TAIL_LIGHT;
9. const defaultCaptureModeLightGraffiti = image.CAPTURE_MODE_LIGHT_GRAFFITI;
10. const defaultCaptureModeSilkyWater = image.CAPTURE_MODE_SILKY_WATER;
11. const defaultCaptureModeStarTrack = image.CAPTURE_MODE_STAR_TRACK;
12. const defaultCaptureModeWideAperture = image.CAPTURE_MODE_WIDEAPERTURE;
13. const defaultCaptureModeMovingPhoto = image.CAPTURE_MODE_MOVING_PHOTO;
14. const defaultCaptureModePortrait = image.CAPTURE_MODE_PORTRAIT;
15. const defaultCaptureModeRearLensNightView = image.CAPTURE_MODE_REAR_LENS_NIGHT_VIEW;
16. const defaultCaptureModeSuperMacro = image.CAPTURE_MODE_SUPER_MACRO;
17. const defaultCaptureModeSnapShot = image.CAPTURE_MODE_SNAP_SHOT;
```
