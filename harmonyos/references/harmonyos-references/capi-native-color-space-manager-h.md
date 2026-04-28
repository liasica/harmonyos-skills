---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-color-space-manager-h
title: native_color_space_manager.h
breadcrumb: API参考 > 图形 > ArkGraphics 2D（方舟2D图形服务） > C API > 头文件 > native_color_space_manager.h
category: harmonyos-references
scraped_at: 2026-04-28T08:14:51+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:9cea835fc3f467ab3144b3d15f2feee634f0f0210181ecdf6942339b7a0a295f
---

## 概述

PhonePC/2in1TabletTVWearable

定义创建和使用色彩空间的相关函数。

**引用文件：** <native\_color\_space\_manager/native\_color\_space\_manager.h>

**库：** libnative\_color\_space\_manager.so

**系统能力：** SystemCapability.Graphic.Graphic2D.ColorManager.Core

**起始版本：** 13

**相关模块：** [NativeColorSpaceManager](capi-nativecolorspacemanager.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 结构体

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [ColorSpacePrimaries](capi-nativecolorspacemanager-colorspaceprimaries.md) | ColorSpacePrimaries | 提供色彩原色结构体声明。 |
| [WhitePointArray](capi-nativecolorspacemanager-whitepointarray.md) | WhitePointArray | 提供白点数组结构体，白点是指在当前色域中表示白色的坐标。 |
| [OH\_NativeColorSpaceManager](nativecolorspacemanager-oh-nativecolorspacemanager.md) | OH\_NativeColorSpaceManager | 提供OH\_NativeColorSpaceManager结构体声明。 |

### 枚举

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [ColorSpaceName](capi-native-color-space-manager-h.md#colorspacename) | ColorSpaceName | 色彩空间枚举。 |

### 函数

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [OH\_NativeColorSpaceManager\* OH\_NativeColorSpaceManager\_CreateFromName(ColorSpaceName colorSpaceName)](capi-native-color-space-manager-h.md#oh_nativecolorspacemanager_createfromname) | 通过colorSpaceName创建OH\_NativeColorSpaceManager实例。  每次调用此函数时，都会创建一个新的OH\_NativeColorSpaceManager实例。 |
| [OH\_NativeColorSpaceManager\* OH\_NativeColorSpaceManager\_CreateFromPrimariesAndGamma(ColorSpacePrimaries primaries, float gamma)](capi-native-color-space-manager-h.md#oh_nativecolorspacemanager_createfromprimariesandgamma) | 通过原色和伽马值创建OH\_NativeColorSpaceManager实例。  每次调用此函数时，都会创建一个新的OH\_NativeColorSpaceManager实例。 |
| [void OH\_NativeColorSpaceManager\_Destroy(OH\_NativeColorSpaceManager\* nativeColorSpaceManager)](capi-native-color-space-manager-h.md#oh_nativecolorspacemanager_destroy) | 销毁OH\_NativeColorSpaceManager实例。 |
| [int OH\_NativeColorSpaceManager\_GetColorSpaceName(OH\_NativeColorSpaceManager\* nativeColorSpaceManager)](capi-native-color-space-manager-h.md#oh_nativecolorspacemanager_getcolorspacename) | 获取色彩空间名称。 |
| [WhitePointArray OH\_NativeColorSpaceManager\_GetWhitePoint(OH\_NativeColorSpaceManager\* nativeColorSpaceManager)](capi-native-color-space-manager-h.md#oh_nativecolorspacemanager_getwhitepoint) | 获取白点。 |
| [float OH\_NativeColorSpaceManager\_GetGamma(OH\_NativeColorSpaceManager\* nativeColorSpaceManager)](capi-native-color-space-manager-h.md#oh_nativecolorspacemanager_getgamma) | 获取伽马值。 |

## 枚举类型说明

PhonePC/2in1TabletTVWearable

### ColorSpaceName

PhonePC/2in1TabletTVWearable

```
1. enum ColorSpaceName
```

**描述**

色彩空间枚举。

**起始版本：** 13

| 枚举项 | 描述 |
| --- | --- |
| NONE = 0 | 表示未知的色彩空间。 |
| ADOBE\_RGB = 1 | 表示基于Adobe RGB的色彩空间。 |
| DCI\_P3 = 2 | 表示基于SMPTE RP 431-2-2007和IEC 61966-2.1：1999的色彩空间。 |
| DISPLAY\_P3 = 3 | 表示基于SMPTE RP 431-2-2007和IEC 61966-2.1：1999的色彩空间。 |
| SRGB = 4 | 表示基于IEC 61966-2.1：1999的标准红绿蓝（SRGB）色彩空间。 |
| BT709 = 6 | 表示基于ITU-R BT.709的色彩空间。 |
| BT601\_EBU = 7 | 表示基于ITU-R BT.601的色彩空间。 |
| BT601\_SMPTE\_C = 8 | 表示基于ITU-R BT.601的色彩空间。 |
| BT2020\_HLG = 9 | 表示基于ITU-R BT.2020的色彩空间。 |
| BT2020\_PQ = 10 | 表示基于ITU-R BT.2020的色彩空间。 |
| P3\_HLG = 11 | 表示色彩原色为P3\_D65，传输特性为HLG，色彩范围为Full的色彩空间。 |
| P3\_PQ = 12 | 表示色彩原色为P3\_D65，传输特性为PQ，色彩范围为Full的色彩空间。 |
| ADOBE\_RGB\_LIMIT = 13 | 表示色彩原色为ADOBE\_RGB，传输特性为ADOBE\_RGB，色彩范围为LIMIT的色彩空间。 |
| DISPLAY\_P3\_LIMIT = 14 | 表示色彩原色为P3\_D65，传输特性为SRGB，色彩范围为LIMIT的色彩空间。 |
| SRGB\_LIMIT = 15 | 表示色彩原色为SRGB，传输特性为SRGB，色彩范围为LIMIT的色彩空间。 |
| BT709\_LIMIT = 16 | 表示色彩原色为BT709，传输特性为BT709，色彩范围为LIMIT的色彩空间。 |
| BT601\_EBU\_LIMIT = 17 | 表示色彩原色为BT601\_P，传输特性为BT709，色彩范围为LIMIT的色彩空间。 |
| BT601\_SMPTE\_C\_LIMIT = 18 | 表示色彩原色为BT601\_N，传输特性为BT709，色彩范围为LIMIT的色彩空间。 |
| BT2020\_HLG\_LIMIT = 19 | 表示色彩原色为BT2020，传输特性为HLG，色彩范围为LIMIT的色彩空间。 |
| BT2020\_PQ\_LIMIT = 20 | 表示色彩原色为BT2020，传输特性为PQ，色彩范围为LIMIT的色彩空间。 |
| P3\_HLG\_LIMIT = 21 | 表示色彩原色为P3\_D65，传输特性为HLG，色彩范围为LIMIT的色彩空间。 |
| P3\_PQ\_LIMIT = 22 | 表示色彩原色为P3\_D65，传输特性为PQ，色彩范围为LIMIT的色彩空间。 |
| LINEAR\_P3 = 23 | 表示色彩原色为P3\_D65，传输特性为LINEAR的色彩空间。 |
| LINEAR\_SRGB = 24 | 表示色彩原色为SRGB，传输特性为LINEAR的色彩空间。 |
| LINEAR\_BT709 = LINEAR\_SRGB | 表示色彩原色为BT709，传输特性为LINEAR的色彩空间。 |
| LINEAR\_BT2020 = 25 | 表示色彩原色为BT2020，传输特性为LINEAR的色彩空间。 |
| DISPLAY\_SRGB = SRGB | 表示色彩原色为SRGB，传输特性为SRGB，色彩范围为Full的色彩空间。 |
| DISPLAY\_P3\_SRGB = DISPLAY\_P3 | 表示色彩原色为P3\_D65，传输特性为SRGB，色彩范围为Full的色彩空间。 |
| DISPLAY\_P3\_HLG = P3\_HLG | 表示色彩原色为P3\_D65，传输特性为HLG，色彩范围为Full的色彩空间。 |
| DISPLAY\_P3\_PQ = P3\_PQ | 表示色彩原色为P3\_D65，传输特性为PQ，色彩范围为Full的色彩空间。 |
| CUSTOM = 5 | 表示自定义色彩空间。 |

## 函数说明

PhonePC/2in1TabletTVWearable

### OH\_NativeColorSpaceManager\_CreateFromName()

PhonePC/2in1TabletTVWearable

```
1. OH_NativeColorSpaceManager* OH_NativeColorSpaceManager_CreateFromName(ColorSpaceName colorSpaceName)
```

**描述**

通过colorSpaceName创建OH\_NativeColorSpaceManager实例。

每次调用此函数时，都会创建一个新的OH\_NativeColorSpaceManager实例。

**系统能力：** SystemCapability.Graphic.Graphic2D.ColorManager.Core

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ColorSpaceName](capi-native-color-space-manager-h.md#colorspacename) colorSpaceName | 表示创建[OH\_NativeColorSpaceManager](nativecolorspacemanager-oh-nativecolorspacemanager.md)的色彩空间名称。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_NativeColorSpaceManager](nativecolorspacemanager-oh-nativecolorspacemanager.md)\* | 返回一个指向[OH\_NativeColorSpaceManager](nativecolorspacemanager-oh-nativecolorspacemanager.md)实例的指针。内存不足时，会导致创建OH\_NativeColorSpaceManager实例失败。 |

### OH\_NativeColorSpaceManager\_CreateFromPrimariesAndGamma()

PhonePC/2in1TabletTVWearable

```
1. OH_NativeColorSpaceManager* OH_NativeColorSpaceManager_CreateFromPrimariesAndGamma(ColorSpacePrimaries primaries, float gamma)
```

**描述**

通过原色和伽马值创建OH\_NativeColorSpaceManager实例。

每次调用此函数时，都会创建一个新的OH\_NativeColorSpaceManager实例。

**系统能力：** SystemCapability.Graphic.Graphic2D.ColorManager.Core

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ColorSpacePrimaries](capi-nativecolorspacemanager-colorspaceprimaries.md) primaries | 表示创建[OH\_NativeColorSpaceManager](nativecolorspacemanager-oh-nativecolorspacemanager.md)的色彩原色。 |
| float gamma | 表示创建[OH\_NativeColorSpaceManager](nativecolorspacemanager-oh-nativecolorspacemanager.md)的伽马值，伽马值为一个浮点数，用于校正亮度范围。  伽马值通常为正值，负值会使弱光区域更亮，强光区域变暗，伽马值为0表示线性色彩空间。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_NativeColorSpaceManager](nativecolorspacemanager-oh-nativecolorspacemanager.md)\* | 返回一个指向[OH\_NativeColorSpaceManager](nativecolorspacemanager-oh-nativecolorspacemanager.md)实例的指针。  内存不足时，会导致创建OH\_NativeColorSpaceManager实例失败。 |

### OH\_NativeColorSpaceManager\_Destroy()

PhonePC/2in1TabletTVWearable

```
1. void OH_NativeColorSpaceManager_Destroy(OH_NativeColorSpaceManager* nativeColorSpaceManager)
```

**描述**

销毁OH\_NativeColorSpaceManager实例。

**系统能力：** SystemCapability.Graphic.Graphic2D.ColorManager.Core

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_NativeColorSpaceManager](nativecolorspacemanager-oh-nativecolorspacemanager.md)\* nativeColorSpaceManager | 表示指向OH\_NativeColorSpaceManager实例的指针。 |

### OH\_NativeColorSpaceManager\_GetColorSpaceName()

PhonePC/2in1TabletTVWearable

```
1. int OH_NativeColorSpaceManager_GetColorSpaceName(OH_NativeColorSpaceManager* nativeColorSpaceManager)
```

**描述**

获取色彩空间名称。

**系统能力：** SystemCapability.Graphic.Graphic2D.ColorManager.Core

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_NativeColorSpaceManager](nativecolorspacemanager-oh-nativecolorspacemanager.md)\* nativeColorSpaceManager | 表示指向OH\_NativeColorSpaceManager实例的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回色彩空间枚举[ColorSpaceName](capi-native-color-space-manager-h.md#colorspacename)对应的值。其中，当返回值为0时，表示接口操作失败。 |

### OH\_NativeColorSpaceManager\_GetWhitePoint()

PhonePC/2in1TabletTVWearable

```
1. WhitePointArray OH_NativeColorSpaceManager_GetWhitePoint(OH_NativeColorSpaceManager* nativeColorSpaceManager)
```

**描述**

获取白点。

**系统能力：** SystemCapability.Graphic.Graphic2D.ColorManager.Core

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_NativeColorSpaceManager](nativecolorspacemanager-oh-nativecolorspacemanager.md)\* nativeColorSpaceManager | 表示指向OH\_NativeColorSpaceManager实例的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [WhitePointArray](capi-nativecolorspacemanager-whitepointarray.md) | 返回值为float数组，返回值为<0.0, 0.0>表示接口操作失败，其余返回值表示操作成功。 |

### OH\_NativeColorSpaceManager\_GetGamma()

PhonePC/2in1TabletTVWearable

```
1. float OH_NativeColorSpaceManager_GetGamma(OH_NativeColorSpaceManager* nativeColorSpaceManager)
```

**描述**

获取伽马值。

**系统能力：** SystemCapability.Graphic.Graphic2D.ColorManager.Core

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_NativeColorSpaceManager](nativecolorspacemanager-oh-nativecolorspacemanager.md)\* nativeColorSpaceManager | 表示指向OH\_NativeColorSpaceManager实例的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| float | 返回值为float类型，返回值为0.0表示接口操作失败，其余返回值表示操作成功。 |
