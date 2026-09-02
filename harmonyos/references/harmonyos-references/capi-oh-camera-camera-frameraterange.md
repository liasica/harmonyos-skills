---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-camera-camera-frameraterange
title: Camera_FrameRateRange
breadcrumb: API参考 > 媒体 > Camera Kit（相机服务） > C API > 结构体 > Camera_FrameRateRange
category: harmonyos-references
scraped_at: 2026-09-02T15:02:28+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:98bacea72e98cee5343e466b53e2fa8eb203d7931c0ecdf6ea081829a84c0530
---

```c
typedef struct Camera_FrameRateRange {...} Camera_FrameRateRange
```

## 概述

帧速率范围。

**起始版本：** 11

**相关模块：** [OH\_Camera](capi-oh-camera.md)

**所在头文件：** [camera.h](capi-camera-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| uint32\_t min | 最小帧速率，单位帧每秒。 |
| uint32\_t max | 最大帧速率，单位帧每秒。 |
