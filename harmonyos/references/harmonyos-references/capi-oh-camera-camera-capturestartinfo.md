---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-camera-camera-capturestartinfo
title: Camera_CaptureStartInfo
breadcrumb: API参考 > 媒体 > Camera Kit（相机服务） > C API > 结构体 > Camera_CaptureStartInfo
category: harmonyos-references
scraped_at: 2026-09-02T15:02:28+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:1a517659780836d3aedf33bbfd77420245b8fd3905a4767357a219ba487fe460
---

```c
typedef struct Camera_CaptureStartInfo {...} Camera_CaptureStartInfo
```

## 概述

拍照开始信息。

**起始版本：** 12

**相关模块：** [OH\_Camera](capi-oh-camera.md)

**所在头文件：** [camera.h](capi-camera-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| int32\_t captureId | 拍照id。 |
| int64\_t time | 预估的单次拍照底层出sensor采集帧时间，如果上报-1，代表没有预估时间。 |
