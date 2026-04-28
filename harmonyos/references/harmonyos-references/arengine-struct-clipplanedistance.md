---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arengine-struct-clipplanedistance
title: AREngine_ClipPlaneDistance
breadcrumb: API参考 > 图形 > AR Engine（AR引擎服务） > C API > 头文件和结构体 > 结构体 > AREngine_ClipPlaneDistance
category: harmonyos-references
scraped_at: 2026-04-28T08:14:34+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:d44626d6b9a86362ce2cc22208a389c14ba738814a9af7205c0cac2a52c75d1e
---

## 概述

PhoneTabletTV

裁剪平面距离数据。

作为[HMS\_AREngine\_ARCamera\_GetProjectionMatrix](arengine-capi-arengine.md#hms_arengine_arcamera_getprojectionmatrix)接口输入。

**起始版本：** 5.0.0(12)

**相关模块：** [AR Engine](arengine-capi-arengine.md)

**所在头文件：** [ar\_engine\_core.h](arengine-header-file.md)

## 汇总

PhoneTabletTV

### 成员变量

PhoneTabletTV

| 名称 | 描述 |
| --- | --- |
| float [near](arengine-struct-clipplanedistance.md#near) | OpenGL近裁剪平面距离，以m为单位。 |
| float [far](arengine-struct-clipplanedistance.md#far) | OpenGL远裁剪平面距离，以m为单位。 |

## 结构体成员变量说明

PhoneTabletTV

### far

PhoneTabletTV

```
1. float AREngine_ClipPlaneDistance::far
```

**描述**

OpenGL远裁剪平面距离，以m为单位。

### near

PhoneTabletTV

```
1. float AREngine_ClipPlaneDistance::near
```

**描述**

OpenGL近裁剪平面距离，以m为单位。
