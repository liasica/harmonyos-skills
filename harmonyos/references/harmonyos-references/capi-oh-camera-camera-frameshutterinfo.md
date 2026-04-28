---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-camera-camera-frameshutterinfo
title: Camera_FrameShutterInfo
breadcrumb: API参考 > 媒体 > Camera Kit（相机服务） > C API > 结构体 > Camera_FrameShutterInfo
category: harmonyos-references
scraped_at: 2026-04-28T08:12:49+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:bb915506e35ad838477971ae9775e0926922f66991a83e9304fcc7d9c5b7b2a9
---

```
1. typedef struct Camera_FrameShutterInfo {...} Camera_FrameShutterInfo
```

## 概述

PhonePC/2in1TabletTVWearable

帧快门回调信息。

**起始版本：** 11

**相关模块：** [OH\_Camera](capi-oh-camera.md)

**所在头文件：** [camera.h](capi-camera-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| int32\_t captureId | 捕获id。 |
| uint64\_t timestamp | 帧的时间戳，单位毫秒。 |
