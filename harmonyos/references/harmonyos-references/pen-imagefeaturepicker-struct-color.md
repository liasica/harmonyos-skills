---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/pen-imagefeaturepicker-struct-color
title: HMS_GCP_Color
breadcrumb: API参考 > 系统 > 硬件 > Pen Kit（手写笔服务） > C API > 头文件和结构体 > 结构体 > HMS_GCP_Color
category: harmonyos-references
scraped_at: 2026-09-02T15:02:13+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:20bfdf6128cb2816b4a85a0e2f46e08952a8a3dcd40a83cdaacc1f91219ef665
---

## 概述

定义颜色值的结构体，用于显示全局取色提取的颜色值。

**系统能力：** SystemCapability.Stylus.ColorPicker

**起始版本：** 5.0.0(12)

**相关模块：** [GlobalColorPicker](pen-imagefeaturepicker-c.md)

**所在头文件：** [native\_gcp\_api.h](pen-headerfile-declare.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| int32\_t [red](pen-imagefeaturepicker-struct-color.md#red) | 红色域。 |
| int32\_t [green](pen-imagefeaturepicker-struct-color.md#green) | 绿色域。 |
| int32\_t [blue](pen-imagefeaturepicker-struct-color.md#blue) | 蓝色域。 |
| int32\_t [alpha](pen-imagefeaturepicker-struct-color.md#alpha) | 透明度。 |

## 结构体成员变量说明

### alpha

```c
int32_t HMS_GCP_Color::alpha
```

**描述**

透明度。

### blue

```c
int32_t HMS_GCP_Color::blue
```

**描述**

蓝色域。

### green

```c
int32_t HMS_GCP_Color::green
```

**描述**

绿色域。

### red

```c
int32_t HMS_GCP_Color::red
```

**描述**

红色域。
