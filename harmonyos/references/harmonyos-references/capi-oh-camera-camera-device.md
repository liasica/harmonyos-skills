---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-camera-camera-device
title: Camera_Device
breadcrumb: API参考 > 媒体 > Camera Kit（相机服务） > C API > 结构体 > Camera_Device
category: harmonyos-references
scraped_at: 2026-04-28T08:12:48+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:539fed3b11ee3e13abf166d54051ea57456fdea3217652ea4eb6c060963e9af9
---

```
1. typedef struct Camera_Device {...} Camera_Device
```

## 概述

PhonePC/2in1TabletTVWearable

相机设备对象。

**起始版本：** 11

**相关模块：** [OH\_Camera](capi-oh-camera.md)

**所在头文件：** [camera.h](capi-camera-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| char\* cameraId | 相机id属性。 |
| [Camera\_Position](capi-camera-h.md#camera_position) cameraPosition | 相机位置属性。 |
| [Camera\_Type](capi-camera-h.md#camera_type) cameraType | 相机类型属性。 |
| [Camera\_Connection](capi-camera-h.md#camera_connection) connectionType | 相机连接类型属性。 |
