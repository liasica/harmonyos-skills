---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-camera-oh-camera-physicalaperture
title: OH_Camera_PhysicalAperture
breadcrumb: API参考 > 媒体 > Camera Kit（相机服务） > C API > 结构体 > OH_Camera_PhysicalAperture
category: harmonyos-references
scraped_at: 2026-09-02T15:02:28+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:19893d9b1354af00cc2f030af318e74eae90509078ad24b4c2141c9c1e5e3296
---

```c
typedef struct OH_Camera_PhysicalAperture {...} OH_Camera_PhysicalAperture
```

## 概述

物理光圈配置。

**起始版本：** 24

**相关模块：** [OH\_Camera](capi-oh-camera.md)

**所在头文件：** [camera.h](capi-camera-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| [OH\_Camera\_ZoomRange](capi-oh-camera-oh-camera-zoomrange.md) zoomRange | 变焦范围。 |
| float\* apertures | 支持的光圈值数组。 |
| size\_t apertureCount | 光圈值数量。 |
