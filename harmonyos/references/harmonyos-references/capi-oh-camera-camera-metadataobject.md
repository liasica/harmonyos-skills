---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-camera-camera-metadataobject
title: Camera_MetadataObject
breadcrumb: API参考 > 媒体 > Camera Kit（相机服务） > C API > 结构体 > Camera_MetadataObject
category: harmonyos-references
scraped_at: 2026-04-28T08:12:50+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:95e0957713469c89e6488bb96e6555231e74c68e9741344efccb681247007d49
---

```
1. typedef struct Camera_MetadataObject {...} Camera_MetadataObject
```

## 概述

PhonePC/2in1TabletTVWearable

元数据对象基础。

**起始版本：** 11

**相关模块：** [OH\_Camera](capi-oh-camera.md)

**所在头文件：** [camera.h](capi-camera-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [Camera\_MetadataObjectType](capi-camera-h.md#camera_metadataobjecttype) type | 元数据对象类型。 |
| int64\_t timestamp | 元数据对象时间戳，单位为纳秒（ns）。 |
| [Camera\_Rect](capi-oh-camera-camera-rect.md)\* boundingBox | 检测到的元数据对象的轴对齐边界框。 |
