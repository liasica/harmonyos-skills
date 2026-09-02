---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-camera-camera-device
title: Camera_Device
breadcrumb: API参考 > 媒体 > Camera Kit（相机服务） > C API > 结构体 > Camera_Device
category: harmonyos-references
scraped_at: 2026-09-02T15:02:28+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:19158e963f993c32ce3ab56dd55173961668e7b3e05c33cb3a5e96c90b577b2b
---

```c
typedef struct Camera_Device {...} Camera_Device
```

## 概述

相机设备对象。

**起始版本：** 11

**相关模块：** [OH\_Camera](capi-oh-camera.md)

**所在头文件：** [camera.h](capi-camera-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| char\* cameraId | 相机id属性。 |
| [Camera\_Position](capi-camera-h.md#camera_position) cameraPosition | 相机位置属性。 |
| [Camera\_Type](capi-camera-h.md#camera_type) cameraType | 相机类型属性。 |
| [Camera\_Connection](capi-camera-h.md#camera_connection) connectionType | 相机连接类型属性。 |
