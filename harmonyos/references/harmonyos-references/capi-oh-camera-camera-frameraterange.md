---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-camera-camera-frameraterange
title: Camera_FrameRateRange
breadcrumb: API参考 > 媒体 > Camera Kit（相机服务） > C API > 结构体 > Camera_FrameRateRange
category: harmonyos-references
scraped_at: 2026-04-28T08:12:47+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:be4ef6bd762334a959550a9c197473cdc00433d80415526716a138499c4cd8ea
---

```
1. typedef struct Camera_FrameRateRange {...} Camera_FrameRateRange
```

## 概述

PhonePC/2in1TabletTVWearable

帧速率范围。

**起始版本：** 11

**相关模块：** [OH\_Camera](capi-oh-camera.md)

**所在头文件：** [camera.h](capi-camera-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| uint32\_t min | 最小帧速率，单位帧每秒。 |
| uint32\_t max | 最大帧速率，单位帧每秒。 |
