---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/pen-imagefeaturepicker-c
title: GlobalColorPicker
breadcrumb: API参考 > 系统 > 硬件 > Pen Kit（手写笔服务） > C API > 模块 > GlobalColorPicker
category: harmonyos-references
scraped_at: 2026-04-28T08:11:00+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:1a15745fbb3761983088d5174c915cbd101b525f6ef61a2b2281cad9a34322e2
---

## 概述

PhonePC/2in1Tablet

该模块对外提供全局取色能力。

**系统能力：** SystemCapability.Stylus.ColorPicker

**起始版本：** 5.0.0(12)

## 汇总

PhonePC/2in1Tablet

### 文件

PhonePC/2in1Tablet

| 名称 | 描述 |
| --- | --- |
| [native\_gcp\_api.h](pen-headerfile-declare.md) | 声明用于对外提供全局取色能力。 |

### 结构体

PhonePC/2in1Tablet

| 名称 | 描述 |
| --- | --- |
| struct [HMS\_GCP\_Color](pen-imagefeaturepicker-struct-color.md) | 定义颜色值的结构体。 |
| struct [HMS\_GCP\_PickedColorInfo](pen-imagefeaturepicker-struct-colorinfo.md) | 定义取色的颜色信息的结构体。 |

### 类型定义

PhonePC/2in1Tablet

| 名称 | 描述 |
| --- | --- |
| typedef void(\* [HMS\_GCP\_OnResult](pen-imagefeaturepicker-c.md#hms_gcp_onresult)) (void \*userData, [HMS\_GCP\_PickedColorInfo](pen-imagefeaturepicker-struct-colorinfo.md) colorInfo, const int32\_t code) | 此回调用于接收拾取的颜色结果。 |

### 枚举

PhonePC/2in1Tablet

| 名称 | 描述 |
| --- | --- |
| [HMS\_GCP\_ColorSpace](pen-imagefeaturepicker-c.md#hms_gcp_colorspace) {  HMS\_GCP\_UNKNOWN = 0,  HMS\_GCP\_ADOBE\_RGB\_1998 = 1,  HMS\_GCP\_DCI\_P3 = 2,  HMS\_GCP\_DISPLAY\_P3 = 3,  HMS\_GCP\_SRGB = 4,  HMS\_GCP\_BT709 = 6,  HMS\_GCP\_BT601\_EBU = 7,  HMS\_GCP\_BT601\_SMPTE\_C = 8,  HMS\_GCP\_BT2020\_HLG = 9,  HMS\_GCP\_BT2020\_PQ = 10,  HMS\_GCP\_P3\_HLG = 11,  HMS\_GCP\_P3\_PQ = 12,  HMS\_GCP\_ADOBE\_RGB\_1998\_LIMIT = 13,  HMS\_GCP\_DISPLAY\_P3\_LIMIT = 14,  HMS\_GCP\_SRGB\_LIMIT = 15,  HMS\_GCP\_BT709\_LIMIT = 16,  HMS\_GCP\_BT601\_EBU\_LIMIT = 17,  HMS\_GCP\_BT601\_SMPTE\_C\_LIMIT = 18,  HMS\_GCP\_BT2020\_HLG\_LIMIT = 19,  HMS\_GCP\_BT2020\_PQ\_LIMIT = 20,  HMS\_GCP\_P3\_HLG\_LIMIT = 21,  HMS\_GCP\_P3\_PQ\_LIMIT = 22,  HMS\_GCP\_LINEAR\_P3 = 23,  HMS\_GCP\_LINEAR\_SRGB = 24,  HMS\_GCP\_LINEAR\_BT2020 = 25,  CUSTOM = 5  } | 颜色空间枚举。 |

### 函数

PhonePC/2in1Tablet

| 名称 | 描述 |
| --- | --- |
| int32\_t [HMS\_GCP\_StartColorPicker](pen-imagefeaturepicker-c.md#hms_gcp_startcolorpicker) (int32\_t initialPosX, int32\_t initialPosY, [HMS\_GCP\_OnResult](pen-imagefeaturepicker-c.md#hms_gcp_onresult) onResultCallback, void \*userData) | 启动全局取色器。此API用于启动取色器，在取色器移动时不显示值。 |
| int32\_t [HMS\_GCP\_StartColorPickerWithColorValue](pen-imagefeaturepicker-c.md#hms_gcp_startcolorpickerwithcolorvalue) (int32\_t initialPosX, int32\_t initialPosY, [HMS\_GCP\_OnResult](pen-imagefeaturepicker-c.md#hms_gcp_onresult) onResultCallback, void \*userData) | 启动全局取色器。此API用于启动取色器，在取色器移动时显示值。  **起始版本：** 5.1.0(18) |

## 类型定义说明

PhonePC/2in1Tablet

### HMS\_GCP\_OnResult

PhonePC/2in1Tablet

```
1. typedef void(* HMS_GCP_OnResult) (void *userData, HMS_GCP_PickedColorInfo colorInfo, const int32_t code)
```

**描述**

此回调用于接收拾取的颜色结果。

**起始版本：** 5.0.0(12)

**参数:**

| 名称 | 描述 |
| --- | --- |
| userData | 指针类型，指向用户数据。可以是空指针。 |
| colorInfo | 需要用户保存的提取的颜色信息。 |
| code | 结果码。  0：取色成功  1013900001：IPC通信失败  1013900002：内存不足  1013900003：服务无效  1013900004：多应用调用  1013900005：后台服务呼叫 |

## 枚举类型说明

PhonePC/2in1Tablet

### HMS\_GCP\_ColorSpace

PhonePC/2in1Tablet

```
1. enum HMS_GCP_ColorSpace
```

**描述**

颜色空间枚举。

**起始版本：** 5.0.0(12)

| 枚举值 | 描述 |
| --- | --- |
| HMS\_GCP\_UNKNOWN | 未知的色彩空间。 |
| HMS\_GCP\_ADOBE\_RGB\_1998 | 基于Adobe RGB的色彩空间。 |
| HMS\_GCP\_DCI\_P3 | 基于SMPTE RP 431-2-2007和IEC 61966-2.1:1999的颜色空间。 |
| HMS\_GCP\_DISPLAY\_P3 | 基于SMPTE RP 431-2-2007和IEC 61966-2.1:1999的颜色空间。 |
| HMS\_GCP\_SRGB | 基于IEC 61966-2.1:1999的标准红绿蓝（SRGB）颜色空间。 |
| HMS\_GCP\_BT709 | 颜色空间基于ITU-R BT.709、PRIMARY\_BT709 | TRANSFUNC\_BT709 | Range\_FULL。 |
| HMS\_GCP\_BT601\_EBU | 颜色空间基于ITU-R BT.601、PRIMARY\_BT601\_P | TRANSFUNC\_BT709 | Range\_FULL。 |
| HMS\_GCP\_BT601\_SMPTE\_C | 颜色空间基于ITU-R BT.601、PRIMARY\_BT601\_N | TRANSFUNC\_BT709 | Range\_FULL。 |
| HMS\_GCP\_BT2020\_HLG | 颜色空间基于ITU-R BT.2020、PRIMARY\_BT2020 | TRANSFUNC\_HLG | Range\_FULL。 |
| HMS\_GCP\_BT2020\_PQ | 颜色空间基于ITU-R BT.2020、PRIMARY\_BT2020 | TRANSFUNC\_PQ | Range\_FULL。 |
| HMS\_GCP\_P3\_HLG | 颜色空间基于ITU-R BT.2020、PRIMARIES\_P3\_D65 | TRANSFUNC\_HLG | RANGE\_FULL。 |
| HMS\_GCP\_P3\_PQ | 颜色空间基于ITU-R BT.2020、PRIMARIES\_P3\_D65 | TRANSFUNC\_PQ | RANGE\_FULL。 |
| HMS\_GCP\_ADOBE\_RGB\_1998\_LIMIT | 颜色空间基于ITU-R BT.2020、PRIMARIES\_ADOBE\_RGB | TRANSFUNC\_ADOBE\_RGB | RANGE\_LIMIT。 |
| HMS\_GCP\_DISPLAY\_P3\_LIMIT | 颜色空间基于ITU-R BT.2020、PRIMARIES\_P3\_D65 | TRANSFUNC\_SRGB | RANGE\_LIMIT。 |
| HMS\_GCP\_SRGB\_LIMIT | 颜色空间基于ITU-R BT.2020、PRIMARIES\_SRGB | TRANSFUNC\_SRGB | RANGE\_LIMIT。 |
| HMS\_GCP\_BT709\_LIMIT | 颜色空间基于ITU-R BT.2020、PRIMARIES\_BT709 | TRANSFUNC\_BT709 | RANGE\_LIMIT。 |
| HMS\_GCP\_BT601\_EBU\_LIMIT | 颜色空间基于ITU-R BT.2020、PRIMARIES\_BT601\_P | TRANSFUNC\_BT709 | RANGE\_LIMIT。 |
| HMS\_GCP\_BT601\_SMPTE\_C\_LIMIT | 颜色空间基于ITU-R BT.2020、PRIMARIES\_BT601\_N | TRANSFUNC\_BT709 | RANGE\_LIMIT。 |
| HMS\_GCP\_BT2020\_HLG\_LIMIT | 颜色空间基于ITU-R BT.2020、PRIMARIES\_BT2020 | TRANSFUNC\_HLG | RANGE\_LIMIT。 |
| HMS\_GCP\_BT2020\_PQ\_LIMIT | 颜色空间基于ITU-R BT.2020、PRIMARIES\_BT2020 | TRANSFUNC\_PQ | RANGE\_LIMIT。 |
| HMS\_GCP\_P3\_HLG\_LIMIT | 颜色空间基于ITU-R BT.2020、PRIMARIES\_P3\_D65 | TRANSFUNC\_HLG | RANGE\_LIMIT。 |
| HMS\_GCP\_P3\_PQ\_LIMIT | 颜色空间基于ITU-R BT.2020、PRIMARIES\_P3\_D65 | TRANSFUNC\_PQ | RANGE\_LIMIT。 |
| HMS\_GCP\_LINEAR\_P3 | 颜色空间基于ITU-R BT.2020、PRIMARIES\_P3\_D65 | TRANSFUNC\_LINEAR。 |
| HMS\_GCP\_LINEAR\_SRGB | 颜色空间基于ITU-R BT.2020、PRIMARIES\_SRGB | TRANSFUNC\_LINEAR。 |
| HMS\_GCP\_LINEAR\_BT2020 | 颜色空间基于ITU-R BT.2020、PRIMARIES\_BT2020 | TRANSFUNC\_LINEAR。 |
| CUSTOM | 开发者自定义的色彩空间。 |

## 函数说明

PhonePC/2in1Tablet

### HMS\_GCP\_StartColorPicker()

PhonePC/2in1Tablet

```
1. int32_t HMS_GCP_StartColorPicker (int32_t initialPosX, int32_t initialPosY, HMS_GCP_OnResult onResultCallback, void *userData)
```

**描述**

启动全局取色器，并且在取色器移动时不显示值。

**起始版本：** 5.0.0(12)

**参数:**

| 名称 | 描述 |
| --- | --- |
| initialPosX | 取色器初始位置的x轴坐标。取值范围：0~屏幕的实际宽度，单位px。 |
| initialPosY | 取色器初始位置的y轴坐标。取值范围：0~屏幕的实际高度，单位px。 |
| onResultCallback | 接收提取的颜色信息的回调。 |
| userData | 指针类型，指向用户数据。可以是空指针。 |

### HMS\_GCP\_StartColorPickerWithColorValue()

PhonePC/2in1Tablet

```
1. int32_t HMS_GCP_StartColorPickerWithColorValue (int32_t initialPosX, int32_t initialPosY, HMS_GCP_OnResult onResultCallback, void *userData)
```

**描述**

启动全局取色器。

此API用于启动取色器，在取色器移动时显示值。

**起始版本：** 5.1.0(18)

**参数：**

| 名称 | 描述 |
| --- | --- |
| initialPosX | 取色器初始位置的x轴坐标。取值范围：0~屏幕的实际宽度，单位px。 |
| initialPosY | 取色器初始位置的y轴坐标。取值范围：0~屏幕的实际高度，单位px。 |
| onResultCallback | 接收提取的颜色信息的回调。 |
| userData | 指针类型，指向用户数据。可以是空指针。 |

**返回：** 结果码。

0 - 取色成功

1013900001 - IPC通信失败

1013900002 - 内存不足

1013900003 - 服务无效

1013900004 - 多应用调用

1013900005 - 后台服务呼叫
