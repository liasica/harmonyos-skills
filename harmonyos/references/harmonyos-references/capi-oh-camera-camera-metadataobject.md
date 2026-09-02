---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-camera-camera-metadataobject
title: Camera_MetadataObject
breadcrumb: API参考 > 媒体 > Camera Kit（相机服务） > C API > 结构体 > Camera_MetadataObject
category: harmonyos-references
scraped_at: 2026-09-02T15:02:28+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:03e78d1e113de3ab53ce6bb6e82bae8c8b5a446483173ca07af7f7fa7318a877
---

```c
typedef struct Camera_MetadataObject {...} Camera_MetadataObject
```

## 概述

元数据对象基础。

**起始版本：** 11

**相关模块：** [OH\_Camera](capi-oh-camera.md)

**所在头文件：** [camera.h](capi-camera-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| [Camera\_MetadataObjectType](capi-camera-h.md#camera_metadataobjecttype) type | 元数据对象类型。 |
| int64\_t timestamp | 元数据对象时间戳，单位为纳秒（ns）。 |
| [Camera\_Rect](capi-oh-camera-camera-rect.md)\* boundingBox | 检测到的元数据对象的轴对齐边界框。 |
