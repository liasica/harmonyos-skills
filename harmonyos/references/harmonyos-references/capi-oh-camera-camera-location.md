---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-camera-camera-location
title: Camera_Location
breadcrumb: API参考 > 媒体 > Camera Kit（相机服务） > C API > 结构体 > Camera_Location
category: harmonyos-references
scraped_at: 2026-09-02T15:02:28+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:c0cdac5598e3cd632107d61d7aa7222b4929b73483027f376619683cb0688487
---

```c
typedef struct Camera_Location {...} Camera_Location
```

## 概述

拍照位置。

**起始版本：** 11

**相关模块：** [OH\_Camera](capi-oh-camera.md)

**所在头文件：** [camera.h](capi-camera-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| double latitude | 纬度。 |
| double longitude | 经度。 |
| double altitude | 海拔高度，单位为米。 |
