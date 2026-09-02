---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-c
title: Constants
breadcrumb: API参考 > 媒体 > Image Kit（图片处理服务） > ArkTS API > @ohos.multimedia.image (图片处理) > Constants
category: harmonyos-references
scraped_at: 2026-09-02T15:02:30+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:d5d28650377bf2a9c85225747c16f914668320a8c09d338e1ad4e96de2ee469e
---

**说明** 

本模块首批接口从API version 23开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

```ts
import { image } from '@kit.ImageKit';
```

## 常量

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

| 名称 | 类型 | 值 | 说明 |
| --- | --- | --- | --- |
| XMAGE\_WATERMARK\_MODE\_AT\_THE\_BOTTOM | number | 9 | XMAGE水印模式：XMAGE水印固定位于图像底部中央。 |
| XMAGE\_WATERMARK\_MODE\_BORDER | number | 10 | XMAGE水印模式：XMAGE水印会自动调整到边界位置，系统根据图像内容选择最适合的边界区域。 |
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
| XMP\_BASIC | [XMPNamespace](arkts-apis-image-i.md#xmpnamespace) | uri: "http://ns.adobe.com/xap/1.0/"  prefix: "xmp" | XMP基础命名空间。  **起始版本：** 26.0.0 |
| XMP\_RIGHTS | [XMPNamespace](arkts-apis-image-i.md#xmpnamespace) | uri: "http://ns.adobe.com/xap/1.0/rights/"  prefix: "xmpRights" | XMP版权与权限命名空间。  **起始版本：** 26.0.0 |
| EXIF | [XMPNamespace](arkts-apis-image-i.md#xmpnamespace) | uri: "http://ns.adobe.com/exif/1.0/"  prefix: "exif" | EXIF元数据命名空间。  **起始版本：** 26.0.0 |
| DUBLIN\_CORE | [XMPNamespace](arkts-apis-image-i.md#xmpnamespace) | uri: "http://purl.org/dc/elements/1.1/"  prefix: "dc" | Dublin Core元数据命名空间。  **起始版本：** 26.0.0 |
| TIFF | [XMPNamespace](arkts-apis-image-i.md#xmpnamespace) | uri: "http://ns.adobe.com/tiff/1.0/"  prefix: "tiff" | TIFF图像格式参数命名空间。  **起始版本：** 26.0.0 |

## 示例

### XMAGE水印模式

```ts
import { BusinessError } from '@kit.BasicServicesKit';

async function SetXmageWatermarkMode(imageSourceObj : image.ImageSource) {
  let makerNoteHuaweiMetadata = image.MakerNoteHuaweiMetadata.createInstance();
  // 设置XMAGE水印模式为底部中央。
  makerNoteHuaweiMetadata.xmageWatermarkMode = image.XMAGE_WATERMARK_MODE_AT_THE_BOTTOM;
  console.info(`Succeeded in setting the XMAGE watermark mode. Mode: ${makerNoteHuaweiMetadata.xmageWatermarkMode}.`);
  await imageSourceObj.writeImageMetadata({ makerNoteHuaweiMetadata: makerNoteHuaweiMetadata }).then(() => {
    console.info(`Succeeded in writing image metadata.`);
  }).catch((error: BusinessError) => {
    console.error(`Failed to write image metadata. Code: ${error.code}, message: ${error.message}.`);
  });
}
```

### 拍摄模式

```ts
import { BusinessError } from '@kit.BasicServicesKit';

async function SetCaptureMode(imageSourceObj : image.ImageSource) {
  let makerNoteHuaweiMetadata = image.MakerNoteHuaweiMetadata.createInstance();
  // 设置拍摄模式为专业模式。
  makerNoteHuaweiMetadata.captureMode = image.CAPTURE_MODE_PROFESSIONAL;
  console.info(`Succeeded in setting the capture mode. Mode: ${makerNoteHuaweiMetadata.captureMode}.`);
  await imageSourceObj.writeImageMetadata({ makerNoteHuaweiMetadata: makerNoteHuaweiMetadata }).then(() => {
    console.info(`Succeeded in writing image metadata.`);
  }).catch((error: BusinessError) => {
    console.error(`Failed to write image metadata. Code: ${error.code}, message: ${error.message}.`);
  });
}
```

### XMP Namespaces

可以参考XMPMetadata中的[setValue](arkts-apis-image-xmpmetadata.md#setvalue)和[getTag](arkts-apis-image-xmpmetadata.md#gettag)等方法的示例来使用这些命名空间。
