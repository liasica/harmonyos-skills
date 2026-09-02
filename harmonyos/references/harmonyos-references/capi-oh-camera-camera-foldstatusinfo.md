---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-camera-camera-foldstatusinfo
title: Camera_FoldStatusInfo
breadcrumb: API参考 > 媒体 > Camera Kit（相机服务） > C API > 结构体 > Camera_FoldStatusInfo
category: harmonyos-references
scraped_at: 2026-09-02T15:02:28+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:1ac0d1897c0cc76e6bd2738d52e7a6c62f51e2df50057776ba0f00a66a15ee36
---

```c
typedef struct Camera_FoldStatusInfo {...} Camera_FoldStatusInfo
```

## 概述

折叠状态信息。

**起始版本：** 13

**相关模块：** [OH\_Camera](capi-oh-camera.md)

**所在头文件：** [camera.h](capi-camera-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| [Camera\_Device](capi-oh-camera-camera-device.md)\*\* supportedCameras | 相机实例列表。 |
| uint32\_t cameraSize | 相机列表数量。 |
| [Camera\_FoldStatus](capi-camera-h.md#camera_foldstatus) foldStatus | 当前折叠状态。 |
