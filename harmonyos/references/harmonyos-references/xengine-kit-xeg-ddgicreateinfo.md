---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xeg-ddgicreateinfo
title: XEG_DDGICreateInfo
breadcrumb: API参考 > 图形 > XEngine Kit（GPU加速引擎服务） > C API > 头文件和结构体 > 结构体 > XEG_DDGICreateInfo
category: harmonyos-references
scraped_at: 2026-09-02T15:02:49+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:0097736a06d853598d84bcad6af50a30257a1b14232581d5eec5d4f8274948b6
---

## 概述

此结构体描述创建具有DDGI特性的[XEG\_RTGI](xengine-kit-xengine.md#xeg_rtgi)对象的信息，当结构体中的信息变化时，需要创建新的[XEG\_RTGI](xengine-kit-xengine.md#xeg_rtgi)对象。

**起始版本：** 6.0.0(20)

**相关模块：** [XEngine](xengine-kit-xengine.md)

**所在头文件：** [xeg\_vulkan\_rtgi.h](xengine-kit-xeg-vulkan-rtgi-8h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| XEG\_StructureType [sType](xengine-kit-xeg-ddgicreateinfo.md#stype) | 识别此结构的[XEG\_StructureType](xengine-kit-xengine.md#xeg_structuretype)值，必须是XEG\_STRUCTURE\_TYPE\_DDGI\_CREATE\_INFO。 |
| const void \* [pNext](xengine-kit-xeg-ddgicreateinfo.md#pnext) | 指向扩展结构的指针。 |
| XEG\_RTGIQualityMode [qualityMode](xengine-kit-xeg-ddgicreateinfo.md#qualitymode) | 输出图像的质量模式，必须为[XEG\_RTGIQualityMode](xengine-kit-xengine.md#xeg_rtgiqualitymode)中的枚举值。 |
| uint32\_t [numberVolume](xengine-kit-xeg-ddgicreateinfo.md#numbervolume) | 需要同时渲染的最大体积数量，范围为[1, 9]，若超出范围，将被限制为范围内最接近该数值的值。 |
| VkExtent2D [scaledView](xengine-kit-xeg-ddgicreateinfo.md#scaledview) | 渲染宽高缩小倍率，不能小于1，建议范围为[1, 4]，数值越大，性能越好，但画质会相应下降。 |
| VkExtent2D [viewSize](xengine-kit-xeg-ddgicreateinfo.md#viewsize) | 输出GI图像的渲染宽高。 |
| bool [enableCloud](xengine-kit-xeg-ddgicreateinfo.md#enablecloud) | 是否开启端云模式，true为开启，false为关闭。 |

## 结构体成员变量说明

### enableCloud

```cpp
bool XEG_DDGICreateInfo::enableCloud
```

**描述**

是否开启端云模式，true为开启，false为关闭。

### numberVolume

```cpp
uint32_t XEG_DDGICreateInfo::numberVolume
```

**描述**

需要同时渲染的最大体积数量，范围为[1, 9]，若超出范围，将被限制为范围内最接近该数值的值。

### pNext

```cpp
const void* XEG_DDGICreateInfo::pNext
```

**描述**

指向扩展结构的指针。

### qualityMode

```cpp
XEG_RTGIQualityMode XEG_DDGICreateInfo::qualityMode
```

**描述**

输出图像的质量模式，必须为[XEG\_RTGIQualityMode](xengine-kit-xengine.md#xeg_rtgiqualitymode)中的枚举值。

### scaledView

```cpp
VkExtent2D XEG_DDGICreateInfo::scaledView
```

**描述**

渲染宽高缩小倍率，不能小于1，建议范围为[1, 4]，数值越大，性能越好，但画质会相应下降。

### sType

```cpp
XEG_StructureType XEG_DDGICreateInfo::sType
```

**描述**

识别此结构的[XEG\_StructureType](xengine-kit-xengine.md#xeg_structuretype)值，必须是XEG\_STRUCTURE\_TYPE\_DDGI\_CREATE\_INFO。

### viewSize

```cpp
VkExtent2D XEG_DDGICreateInfo::viewSize
```

**描述**

输出GI图像的渲染宽高。
