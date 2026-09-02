---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-camera-camera-occlusiondetectionresult
title: Camera_OcclusionDetectionResult
breadcrumb: API参考 > 媒体 > Camera Kit（相机服务） > C API > 结构体 > Camera_OcclusionDetectionResult
category: harmonyos-references
scraped_at: 2026-09-02T15:02:28+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:1ba4f5c03b54e864ec9dee5e083afa254c81ebc3ec3810d6bd2fc91f94436d77
---

```c
typedef struct {...} Camera_OcclusionDetectionResult
```

## 概述

相机镜头遮挡、脏污检测结果。

**起始版本：** 23

**相关模块：** [OH\_Camera](capi-oh-camera.md)

**所在头文件：** [camera.h](capi-camera-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| bool isCameraOccluded | 检查相机镜头是否被遮挡。true表示被遮挡，false表示未被遮挡。 |
| bool isCameraLensDirty | 检查相机镜头是否有脏污。true表示有脏污，false表示没有脏污。 |
