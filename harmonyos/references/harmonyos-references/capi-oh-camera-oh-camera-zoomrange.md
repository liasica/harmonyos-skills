---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-camera-oh-camera-zoomrange
title: OH_Camera_ZoomRange
breadcrumb: API参考 > 媒体 > Camera Kit（相机服务） > C API > 结构体 > OH_Camera_ZoomRange
category: harmonyos-references
scraped_at: 2026-09-02T15:02:28+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:3c6cc9c02787865c6e23092eddfe8d9197b6c233ee2eed14d8f73531c184ca2c
---

```c
typedef struct OH_Camera_ZoomRange {...} OH_Camera_ZoomRange
```

## 概述

变焦范围配置。

**起始版本：** 24

**相关模块：** [OH\_Camera](capi-oh-camera.md)

**所在头文件：** [camera.h](capi-camera-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| float minZoom | 最小变焦值。 |
| float maxZoom | 最大变焦值。 |
