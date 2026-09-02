---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xeg-hpsradixsortdescription
title: XEG_HPSRadixSortDescription
breadcrumb: API参考 > 图形 > XEngine Kit（GPU加速引擎服务） > C API > 头文件和结构体 > 结构体 > XEG_HPSRadixSortDescription
category: harmonyos-references
scraped_at: 2026-09-02T15:02:49+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:970a99c0e7c9246870664575124d846722ccae666d35a0210de8d843a638d9e5
---

## 概述

此结构体描述使用[XEG\_HPS\_RADIX\_SORT\_EXTENSION\_NAME](xengine-kit-xengine.md#xeg_hps_radix_sort_extension_name)扩展进行排序时所需的信息。

**起始版本：** 6.0.0(20)

**相关模块：** [XEngine](xengine-kit-xengine.md)

**所在头文件：** [xeg\_vulkan\_hps.h](xengine-kit-xeg-vulkan-hps-8h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| XEG\_StructureType [sType](xengine-kit-xeg-hpsradixsortdescription.md#stype) | 识别此结构的[XEG\_StructureType](xengine-kit-xengine.md#xeg_structuretype)值，必须是XEG\_STRUCTURE\_TYPE\_HPS\_RADIX\_SORT\_DESCRIPTION。 |
| const void \* [pNext](xengine-kit-xeg-hpsradixsortdescription.md#pnext) | 指向扩展结构的指针。 |
| VkBuffer [sortCount](xengine-kit-xeg-hpsradixsortdescription.md#sortcount) | 存储要排序的索引数量的缓冲区，数量值从缓冲区第0位读取。 |
| VkBuffer [keyBuffer](xengine-kit-xeg-hpsradixsortdescription.md#keybuffer) | 存储排序使用的key值的缓冲区，数据格式为32位无符号整数。 |
| VkBuffer [indexBuffer](xengine-kit-xeg-hpsradixsortdescription.md#indexbuffer) | 存储待排序value值的缓冲区，数据格式为32位无符号整数。 |

## 结构体成员变量说明

### indexBuffer

```cpp
VkBuffer XEG_HPSRadixSortDescription::indexBuffer
```

**描述**

存储待排序value值的缓冲区，数据格式为32位无符号整数。

### keyBuffer

```cpp
VkBuffer XEG_HPSRadixSortDescription::keyBuffer
```

**描述**

存储排序使用的key值的缓冲区，数据格式为32位无符号整数。

### pNext

```cpp
const void* XEG_HPSRadixSortDescription::pNext
```

**描述**

指向扩展结构的指针。

### sortCount

```cpp
VkBuffer XEG_HPSRadixSortDescription::sortCount
```

**描述**

存储要排序的索引数量的缓冲区，数量值从缓冲区第0位读取。

### sType

```cpp
XEG_StructureType XEG_HPSRadixSortDescription::sType
```

**描述**

识别此结构的[XEG\_StructureType](xengine-kit-xengine.md#xeg_structuretype)值，必须是XEG\_STRUCTURE\_TYPE\_HPS\_RADIX\_SORT\_DESCRIPTION。
