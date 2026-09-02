---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-camera-cameramanager-callbacks
title: CameraManager_Callbacks
breadcrumb: API参考 > 媒体 > Camera Kit（相机服务） > C API > 结构体 > CameraManager_Callbacks
category: harmonyos-references
scraped_at: 2026-09-02T15:02:28+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:2567954a1e984bc246542c586f2b02ca580a7367a39ca1f6f57655f157ea2748
---

```c
typedef struct CameraManager_Callbacks {...} CameraManager_Callbacks
```

## 概述

相机设备状态的回调。

**起始版本：** 11

**相关模块：** [OH\_Camera](capi-oh-camera.md)

**所在头文件：** [camera\_manager.h](capi-camera-manager-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| [OH\_CameraManager\_StatusCallback](capi-camera-manager-h.md#oh_cameramanager_statuscallback) onCameraStatus | 相机状态更改事件。 |
