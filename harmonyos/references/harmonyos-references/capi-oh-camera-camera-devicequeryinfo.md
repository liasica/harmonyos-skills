---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-camera-camera-devicequeryinfo
title: Camera_DeviceQueryInfo
breadcrumb: API参考 > 媒体 > Camera Kit（相机服务） > C API > 结构体 > Camera_DeviceQueryInfo
category: harmonyos-references
scraped_at: 2026-09-02T15:02:28+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:72797755df671bf75be8795cf9e2e75ca88f485740a40d2234ae007d62e7938f
---

```c
typedef struct {...} Camera_DeviceQueryInfo
```

## 概述

相机设备的查询信息。

**起始版本：** 23

**相关模块：** [OH\_Camera](capi-oh-camera.md)

**所在头文件：** [camera.h](capi-camera-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| Camera\_Type\* cameraType | 相机类型属性列表。 |
| uint32\_t cameraTypeSize | 相机类型属性列表的大小。 |
| [Camera\_Position](capi-camera-h.md#camera_position) cameraPosition | 相机位置属性。 |
| [Camera\_Connection](capi-camera-h.md#camera_connection) connectionType | 相机连接类型属性。 |
