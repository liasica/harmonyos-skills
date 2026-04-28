---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-t
title: Types
breadcrumb: API参考 > 媒体 > Image Kit（图片处理服务） > ArkTS API > @ohos.multimedia.image (图片处理) > Types
category: harmonyos-references
scraped_at: 2026-04-28T08:13:14+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:6bacd514ae84c4600d553ba6aff17a63ad155a7fcf7c55e2155f458f2f7992c4
---

说明

本模块首批接口从API version 6开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## HdrMetadataValue12+

PhonePC/2in1TabletTVWearable

type HdrMetadataValue = HdrMetadataType | HdrStaticMetadata | ArrayBuffer | HdrGainmapMetadata

PixelMap使用的HDR元数据值类型，和[HdrMetadataKey](arkts-apis-image-e.md#hdrmetadatakey12)关键字相对应。

**系统能力：** SystemCapability.Multimedia.Image.Core

| 类型 | 说明 |
| --- | --- |
| [HdrMetadataType](arkts-apis-image-e.md#hdrmetadatatype12) | [HdrMetadataKey](arkts-apis-image-e.md#hdrmetadatakey12)中HDR\_METADATA\_TYPE关键字对应的元数据值类型。 |
| [HdrStaticMetadata](arkts-apis-image-i.md#hdrstaticmetadata12) | [HdrMetadataKey](arkts-apis-image-e.md#hdrmetadatakey12)中HDR\_STATIC\_METADATA关键字对应的元数据值类型。 |
| ArrayBuffer | [HdrMetadataKey](arkts-apis-image-e.md#hdrmetadatakey12)中HDR\_DYNAMIC\_METADATA关键字对应的元数据值类型。 |
| [HdrGainmapMetadata](arkts-apis-image-i.md#hdrgainmapmetadata12) | [HdrMetadataKey](arkts-apis-image-e.md#hdrmetadatakey12)中HDR\_GAINMAP\_METADATA关键字对应的元数据值类型。 |
