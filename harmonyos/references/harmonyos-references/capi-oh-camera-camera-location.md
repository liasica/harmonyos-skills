---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-camera-camera-location
title: Camera_Location
breadcrumb: API参考 > 媒体 > Camera Kit（相机服务） > C API > 结构体 > Camera_Location
category: harmonyos-references
scraped_at: 2026-04-28T08:12:49+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:19bdb4f3f194860fa02c2c41b55878474b9bffe3861260acb87f7cac058d8b94
---

```
1. typedef struct Camera_Location {...} Camera_Location
```

## 概述

PhonePC/2in1TabletTVWearable

拍照位置。

**起始版本：** 11

**相关模块：** [OH\_Camera](capi-oh-camera.md)

**所在头文件：** [camera.h](capi-camera-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| double latitude | 纬度。 |
| double longitude | 经度。 |
| double altitude | 海拔高度，单位为米。 |
