---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-imagekit-7002
title: Image Kit
breadcrumb: 版本说明 > 最新版本(26.0.0) > 26.0.0 > OS平台能力 > API变更清单 > 26.0.0 Beta2引入的API > Image Kit
category: harmonyos-releases
scraped_at: 2026-09-02T14:49:04+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:3228ea514b8a458077d6c8e414a739dd42f3978adfb59abd6589fe850c624769
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：PixelMapFormat；  API声明：Y8 = 14  差异内容：Y8 = 14 | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：PixelMapFormat；  API声明：ALPHA\_F16 = 16  差异内容：ALPHA\_F16 = 16 | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：image；  API声明：interface PackingOptionsForTiff  差异内容：interface PackingOptionsForTiff | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：PackingOptionsForTiff；  API声明：compression?: number;  差异内容：compression?: number; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：PackingOptionsForTiff；  API声明：orientation?: Orientation;  差异内容：orientation?: Orientation; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：PackingOptionsForTiff；  API声明：xResolution?: number;  差异内容：xResolution?: number; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：PackingOptionsForTiff；  API声明：yResolution?: number;  差异内容：yResolution?: number; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：PackingOptionsForTiff；  API声明：resolutionUnit?: number;  差异内容：resolutionUnit?: number; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：image；  API声明：interface PackingSizeLimit  差异内容：interface PackingSizeLimit | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：PackingSizeLimit；  API声明：maxSize: Size;  差异内容：maxSize: Size; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：PackingSizeLimit；  API声明：level: AntiAliasingLevel;  差异内容：level: AntiAliasingLevel; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：PackingOption；  API声明：tiffPackingOptions?: PackingOptionsForTiff;  差异内容：tiffPackingOptions?: PackingOptionsForTiff; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：PackingOption；  API声明：backgroundColor?: number;  差异内容：backgroundColor?: number; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：PackingOption；  API声明：sizeLimit?: PackingSizeLimit;  差异内容：sizeLimit?: PackingSizeLimit; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：PackingOption；  API声明：needsPackGPS?: boolean;  差异内容：needsPackGPS?: boolean; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：Picture；  API声明：hdrComposeToMainPixelmap(): Promise<void>;  差异内容：hdrComposeToMainPixelmap(): Promise<void>; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：AuxiliaryPictureType；  API声明：LHDR\_GAINMAP = 10  差异内容：LHDR\_GAINMAP = 10 | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：image；  API声明：const XMAGE\_WATERMARK\_MODE\_AT\_THE\_BOTTOM: number;  差异内容：const XMAGE\_WATERMARK\_MODE\_AT\_THE\_BOTTOM: number; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：image；  API声明：const XMAGE\_WATERMARK\_MODE\_BORDER: number;  差异内容：const XMAGE\_WATERMARK\_MODE\_BORDER: number; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：image；  API声明：const CAPTURE\_MODE\_PROFESSIONAL: number;  差异内容：const CAPTURE\_MODE\_PROFESSIONAL: number; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：image；  API声明：const CAPTURE\_MODE\_FRONT\_LENS\_NIGHT\_VIEW: number;  差异内容：const CAPTURE\_MODE\_FRONT\_LENS\_NIGHT\_VIEW: number; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：image；  API声明：const CAPTURE\_MODE\_PANORAMA: number;  差异内容：const CAPTURE\_MODE\_PANORAMA: number; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：image；  API声明：const CAPTURE\_MODE\_TAIL\_LIGHT: number;  差异内容：const CAPTURE\_MODE\_TAIL\_LIGHT: number; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：image；  API声明：const CAPTURE\_MODE\_LIGHT\_GRAFFITI: number;  差异内容：const CAPTURE\_MODE\_LIGHT\_GRAFFITI: number; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：image；  API声明：const CAPTURE\_MODE\_SILKY\_WATER: number;  差异内容：const CAPTURE\_MODE\_SILKY\_WATER: number; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：image；  API声明：const CAPTURE\_MODE\_STAR\_TRACK: number;  差异内容：const CAPTURE\_MODE\_STAR\_TRACK: number; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：image；  API声明：const CAPTURE\_MODE\_WIDEAPERTURE: number;  差异内容：const CAPTURE\_MODE\_WIDEAPERTURE: number; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：image；  API声明：const CAPTURE\_MODE\_MOVING\_PHOTO: number;  差异内容：const CAPTURE\_MODE\_MOVING\_PHOTO: number; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：image；  API声明：const CAPTURE\_MODE\_PORTRAIT: number;  差异内容：const CAPTURE\_MODE\_PORTRAIT: number; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：image；  API声明：const CAPTURE\_MODE\_REAR\_LENS\_NIGHT\_VIEW: number;  差异内容：const CAPTURE\_MODE\_REAR\_LENS\_NIGHT\_VIEW: number; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：image；  API声明：const CAPTURE\_MODE\_SUPER\_MACRO: number;  差异内容：const CAPTURE\_MODE\_SUPER\_MACRO: number; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：image；  API声明：const CAPTURE\_MODE\_SNAP\_SHOT: number;  差异内容：const CAPTURE\_MODE\_SNAP\_SHOT: number; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：image；  API声明：interface BinaryBufferInfo  差异内容：interface BinaryBufferInfo | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：BinaryBufferInfo；  API声明：size: Size;  差异内容：size: Size; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：BinaryBufferInfo；  API声明：data: ArrayBuffer;  差异内容：data: ArrayBuffer; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：BinaryBufferInfo；  API声明：bytesPerRow?: number;  差异内容：bytesPerRow?: number; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：ImagePacker；  API声明：packBinaryImageToTiffFile(bufferInfo: BinaryBufferInfo, fd: number, options?: PackingOptionsForTiff): Promise<void>;  差异内容：packBinaryImageToTiffFile(bufferInfo: BinaryBufferInfo, fd: number, options?: PackingOptionsForTiff): Promise<void>; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：ImagePacker；  API声明：packBinaryImageToTiffData(bufferInfo: BinaryBufferInfo, options?: PackingOptionsForTiff): Promise<ArrayBuffer>;  差异内容：packBinaryImageToTiffData(bufferInfo: BinaryBufferInfo, options?: PackingOptionsForTiff): Promise<ArrayBuffer>; | api/@ohos.multimedia.image.d.ts |
| 删除API | 类名：image；  API声明：const XMAGE\_WATERMARK\_MODE\_AT\_THE\_BOTTOM: number = 9;  差异内容：const XMAGE\_WATERMARK\_MODE\_AT\_THE\_BOTTOM: number = 9; | NA | api/@ohos.multimedia.image.d.ts |
| 删除API | 类名：image；  API声明：const XMAGE\_WATERMARK\_MODE\_BORDER: number = 10;  差异内容：const XMAGE\_WATERMARK\_MODE\_BORDER: number = 10; | NA | api/@ohos.multimedia.image.d.ts |
| 删除API | 类名：image；  API声明：const CAPTURE\_MODE\_PROFESSIONAL: number = 2;  差异内容：const CAPTURE\_MODE\_PROFESSIONAL: number = 2; | NA | api/@ohos.multimedia.image.d.ts |
| 删除API | 类名：image；  API声明：const CAPTURE\_MODE\_FRONT\_LENS\_NIGHT\_VIEW: number = 7;  差异内容：const CAPTURE\_MODE\_FRONT\_LENS\_NIGHT\_VIEW: number = 7; | NA | api/@ohos.multimedia.image.d.ts |
| 删除API | 类名：image；  API声明：const CAPTURE\_MODE\_PANORAMA: number = 8;  差异内容：const CAPTURE\_MODE\_PANORAMA: number = 8; | NA | api/@ohos.multimedia.image.d.ts |
| 删除API | 类名：image；  API声明：const CAPTURE\_MODE\_TAIL\_LIGHT: number = 9;  差异内容：const CAPTURE\_MODE\_TAIL\_LIGHT: number = 9; | NA | api/@ohos.multimedia.image.d.ts |
| 删除API | 类名：image；  API声明：const CAPTURE\_MODE\_LIGHT\_GRAFFITI: number = 10;  差异内容：const CAPTURE\_MODE\_LIGHT\_GRAFFITI: number = 10; | NA | api/@ohos.multimedia.image.d.ts |
| 删除API | 类名：image；  API声明：const CAPTURE\_MODE\_SILKY\_WATER: number = 11;  差异内容：const CAPTURE\_MODE\_SILKY\_WATER: number = 11; | NA | api/@ohos.multimedia.image.d.ts |
| 删除API | 类名：image；  API声明：const CAPTURE\_MODE\_STAR\_TRACK: number = 12;  差异内容：const CAPTURE\_MODE\_STAR\_TRACK: number = 12; | NA | api/@ohos.multimedia.image.d.ts |
| 删除API | 类名：image；  API声明：const CAPTURE\_MODE\_WIDEAPERTURE: number = 19;  差异内容：const CAPTURE\_MODE\_WIDEAPERTURE: number = 19; | NA | api/@ohos.multimedia.image.d.ts |
| 删除API | 类名：image；  API声明：const CAPTURE\_MODE\_MOVING\_PHOTO: number = 20;  差异内容：const CAPTURE\_MODE\_MOVING\_PHOTO: number = 20; | NA | api/@ohos.multimedia.image.d.ts |
| 删除API | 类名：image；  API声明：const CAPTURE\_MODE\_PORTRAIT: number = 23;  差异内容：const CAPTURE\_MODE\_PORTRAIT: number = 23; | NA | api/@ohos.multimedia.image.d.ts |
| 删除API | 类名：image；  API声明：const CAPTURE\_MODE\_REAR\_LENS\_NIGHT\_VIEW: number = 42;  差异内容：const CAPTURE\_MODE\_REAR\_LENS\_NIGHT\_VIEW: number = 42; | NA | api/@ohos.multimedia.image.d.ts |
| 删除API | 类名：image；  API声明：const CAPTURE\_MODE\_SUPER\_MACRO: number = 47;  差异内容：const CAPTURE\_MODE\_SUPER\_MACRO: number = 47; | NA | api/@ohos.multimedia.image.d.ts |
| 删除API | 类名：image；  API声明：const CAPTURE\_MODE\_SNAP\_SHOT: number = 62;  差异内容：const CAPTURE\_MODE\_SNAP\_SHOT: number = 62; | NA | api/@ohos.multimedia.image.d.ts |
| 起始版本有变化 | 类名：Region；  API声明：size: Size;  差异内容：7 | 类名：Region；  API声明：size: Size;  差异内容：8 | api/@ohos.multimedia.image.d.ts |
| 起始版本有变化 | 类名：Region；  API声明：x: number;  差异内容：7 | 类名：Region；  API声明：x: number;  差异内容：8 | api/@ohos.multimedia.image.d.ts |
| 起始版本有变化 | 类名：Region；  API声明：y: number;  差异内容：7 | 类名：Region；  API声明：y: number;  差异内容：8 | api/@ohos.multimedia.image.d.ts |
