---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-camera-camera-occlusiondetectionresult
title: Camera_OcclusionDetectionResult
breadcrumb: API参考 > 媒体 > Camera Kit（相机服务） > C API > 结构体 > Camera_OcclusionDetectionResult
category: harmonyos-references
scraped_at: 2026-04-28T08:12:56+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:3f712486f3c7b998581b9a6cea896fd8d94f1f711c51bd64316616638ca74836
---

```
1. typedef struct {...} Camera_OcclusionDetectionResult
```

## 概述

PhonePC/2in1TabletTVWearable

相机镜头遮挡、脏污检测结果。

**起始版本：** 23

**相关模块：** [OH\_Camera](capi-oh-camera.md)

**所在头文件：** [camera.h](capi-camera-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| bool isCameraOccluded | 检查相机镜头是否被遮挡。true表示被遮挡，false表示未被遮挡。 |
| bool isCameraLensDirty | 检查相机镜头是否有脏污。true表示有脏污，false表示没有脏污。 |
