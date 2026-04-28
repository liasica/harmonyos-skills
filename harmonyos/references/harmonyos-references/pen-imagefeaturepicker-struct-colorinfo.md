---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/pen-imagefeaturepicker-struct-colorinfo
title: HMS_GCP_PickedColorInfo
breadcrumb: API参考 > 系统 > 硬件 > Pen Kit（手写笔服务） > C API > 头文件和结构体 > 结构体 > HMS_GCP_PickedColorInfo
category: harmonyos-references
scraped_at: 2026-04-28T08:11:01+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:1878058acf9aaa9713b4faf84fec22fb5266fe1dac4c24b3825ddbfc1a6a25e0
---

## 概述

PhonePC/2in1Tablet

定义取色颜色信息的结构体。

**系统能力：** SystemCapability.Stylus.ColorPicker

**起始版本：** 5.0.0(12)

**相关模块：** [GlobalColorPicker](pen-imagefeaturepicker-c.md)

**所在头文件：** [native\_gcp\_api.h](pen-headerfile-declare.md)

## 汇总

PhonePC/2in1Tablet

### 成员变量

PhonePC/2in1Tablet

| 名称 | 描述 |
| --- | --- |
| [HMS\_GCP\_Color](pen-imagefeaturepicker-struct-color.md) color | 提取的颜色值。 |
| [HMS\_GCP\_ColorSpace](pen-imagefeaturepicker-c.md#hms_gcp_colorspace) colorSpace | 颜色所属的颜色空间。 |
| int64\_t [timestamp](pen-imagefeaturepicker-struct-colorinfo.md#timestamp) | 提取颜色的时间戳。 |

## 结构体成员变量说明

PhonePC/2in1Tablet

### color

PhonePC/2in1Tablet

```
1. HMS_GCP_Color HMS_GCP_PickedColorInfo::color
```

**描述**

提取的颜色值。

### colorSpace

PhonePC/2in1Tablet

```
1. HMS_GCP_ColorSpace HMS_GCP_PickedColorInfo::colorSpace
```

**描述**

颜色所属的颜色空间。

### timestamp

PhonePC/2in1Tablet

```
1. int64_t HMS_GCP_PickedColorInfo::timestamp
```

**描述**

提取颜色的时间戳。
