---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-camera-camera-point
title: Camera_Point
breadcrumb: API参考 > 媒体 > Camera Kit（相机服务） > C API > 结构体 > Camera_Point
category: harmonyos-references
scraped_at: 2026-09-02T15:02:28+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:bc57935fdc1d97df1a3c509b487e558f2697da62ae42bdb93be1650641e0116e
---

```c
typedef struct Camera_Point {...} Camera_Point
```

## 概述

点参数。

**起始版本：** 11

**相关模块：** [OH\_Camera](capi-oh-camera.md)

**所在头文件：** [camera.h](capi-camera-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| double x | X坐标，取值范围为[0,1]。 |
| double y | Y坐标，取值范围为[0,1]。 |
