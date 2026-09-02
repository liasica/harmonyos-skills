---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-videoprocessing-videoprocessing-colorspaceinfo
title: VideoProcessing_ColorSpaceInfo
breadcrumb: API参考 > 媒体 > Media Kit（媒体服务） > C API > 结构体 > VideoProcessing_ColorSpaceInfo
category: harmonyos-references
scraped_at: 2026-09-02T15:02:37+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:6468700d5e502462c303854ce3e3c748b929906f5fc5e64800ad979fca6d6f3b
---

```c
typedef struct VideoProcessing_ColorSpaceInfo {...} VideoProcessing_ColorSpaceInfo
```

## 概述

视频颜色空间信息数据结构。

**参考：** [OH\_VideoProcessing\_IsColorSpaceConversionSupported](capi-video-processing-h.md#oh_videoprocessing_iscolorspaceconversionsupported)

**起始版本：** 12

**相关模块：** [VideoProcessing](capi-videoprocessing.md)

**所在头文件：** [video\_processing\_types.h](capi-video-processing-types-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| int32\_t metadataType | 视频元数据类型，参考[OH\_NativeBuffer\_MetadataType](capi-buffer-common-h.md#oh_nativebuffer_metadatatype)。 |
| int32\_t colorSpace | 视频颜色空间类型，参考[OH\_NativeBuffer\_ColorSpace](capi-buffer-common-h.md#oh_nativebuffer_colorspace)。 |
| int32\_t pixelFormat | 视频像素格式，参考[OH\_NativeBuffer\_Format](capi-buffer-common-h.md#oh_nativebuffer_format)。 |
