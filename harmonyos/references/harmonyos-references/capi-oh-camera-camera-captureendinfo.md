---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-camera-camera-captureendinfo
title: Camera_CaptureEndInfo
breadcrumb: API参考 > 媒体 > Camera Kit（相机服务） > C API > 结构体 > Camera_CaptureEndInfo
category: harmonyos-references
scraped_at: 2026-09-02T15:02:28+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:a99b1537ba6c0bacd3cbe46587e4d7acad5980b69e418ed01f003a9dc77de242
---

```c
typedef struct Camera_CaptureEndInfo {...} Camera_CaptureEndInfo
```

## 概述

捕获结束信息。

**起始版本：** 11

**相关模块：** [OH\_Camera](capi-oh-camera.md)

**所在头文件：** [camera.h](capi-camera-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| int32\_t captureId | 捕获id。 |
| int64\_t frameCount | 帧数。 |
