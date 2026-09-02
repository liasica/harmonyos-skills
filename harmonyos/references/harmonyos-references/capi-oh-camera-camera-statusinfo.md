---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-camera-camera-statusinfo
title: Camera_StatusInfo
breadcrumb: API参考 > 媒体 > Camera Kit（相机服务） > C API > 结构体 > Camera_StatusInfo
category: harmonyos-references
scraped_at: 2026-09-02T15:02:28+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:ad454a9ec48faf518460695ceed99aab9d58e09f8acf20b6314476e6080eb739
---

```c
typedef struct Camera_StatusInfo {...} Camera_StatusInfo
```

## 概述

相机状态信息。

**起始版本：** 11

**相关模块：** [OH\_Camera](capi-oh-camera.md)

**所在头文件：** [camera.h](capi-camera-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| [Camera\_Device](capi-oh-camera-camera-device.md)\* camera | 相机实例。 |
| [Camera\_Status](capi-camera-h.md#camera_status) status | 当前相机状态。 |
