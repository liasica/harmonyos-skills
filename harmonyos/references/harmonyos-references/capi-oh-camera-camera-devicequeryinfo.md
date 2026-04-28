---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-camera-camera-devicequeryinfo
title: Camera_DeviceQueryInfo
breadcrumb: API参考 > 媒体 > Camera Kit（相机服务） > C API > 结构体 > Camera_DeviceQueryInfo
category: harmonyos-references
scraped_at: 2026-04-28T08:12:48+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:fea5b85f7d8e1bb91a3b2756708036dfc5ded02dcd3576790f388170b4e2ec59
---

```
1. typedef struct {...} Camera_DeviceQueryInfo
```

## 概述

PhonePC/2in1TabletTVWearable

相机设备的查询信息。

**起始版本：** 23

**相关模块：** [OH\_Camera](capi-oh-camera.md)

**所在头文件：** [camera.h](capi-camera-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| Camera\_Type\* cameraType | 相机类型属性列表。 |
| uint32\_t cameraTypeSize | 相机类型属性列表的大小。 |
| [Camera\_Position](capi-camera-h.md#camera_position) cameraPosition | 相机位置属性。 |
| [Camera\_Connection](capi-camera-h.md#camera_connection) connectionType | 相机连接类型属性。 |
