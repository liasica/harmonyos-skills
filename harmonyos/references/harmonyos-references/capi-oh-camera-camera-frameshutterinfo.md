---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-camera-camera-frameshutterinfo
title: Camera_FrameShutterInfo
breadcrumb: API参考 > 媒体 > Camera Kit（相机服务） > C API > 结构体 > Camera_FrameShutterInfo
category: harmonyos-references
scraped_at: 2026-09-02T15:02:28+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:a0527bf5f10a83724d89cb4fe457a631d4282debc612f5269b62fd52fe1d8fb3
---

```c
typedef struct Camera_FrameShutterInfo {...} Camera_FrameShutterInfo
```

## 概述

帧快门回调信息。

**起始版本：** 11

**相关模块：** [OH\_Camera](capi-oh-camera.md)

**所在头文件：** [camera.h](capi-camera-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| int32\_t captureId | 捕获id。 |
| uint64\_t timestamp | 帧的时间戳，单位毫秒。 |
