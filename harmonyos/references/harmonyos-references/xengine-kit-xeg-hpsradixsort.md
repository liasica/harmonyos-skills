---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xeg-hpsradixsort
title: XEG_HPSRadixSort
breadcrumb: API参考 > 图形 > XEngine Kit（GPU加速引擎服务） > C API > 头文件和结构体 > 结构体 > XEG_HPSRadixSort
category: harmonyos-references
scraped_at: 2026-09-02T15:02:49+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:bac24ec065847f72e3b532ac051cb1306ca3ce00e47ebdce538fac6a11cd1ab7
---

## 概述

此结构体描述HPS基数排序扩展结构信息。

**起始版本：** 6.0.0(20)

**相关模块：** [XEngine](xengine-kit-xengine.md)

**所在头文件：** [xeg\_vulkan\_hps.h](xengine-kit-xeg-vulkan-hps-8h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| XEG\_StructureType [sType](xengine-kit-xeg-hpsradixsort.md#stype) | 识别此结构的[XEG\_StructureType](xengine-kit-xengine.md#xeg_structuretype)值，必须是XEG\_STRUCTURE\_TYPE\_HPS\_RADIX\_SORT。 |
| const void \* [pNext](xengine-kit-xeg-hpsradixsort.md#pnext) | 指向扩展结构的指针。 |

## 结构体成员变量说明

### pNext

```cpp
const void* XEG_HPSRadixSort::pNext
```

**描述**

指向扩展结构的指针。

### sType

```cpp
XEG_StructureType XEG_HPSRadixSort::sType
```

**描述**

识别此结构的[XEG\_StructureType](xengine-kit-xengine.md#xeg_structuretype)值，必须是XEG\_STRUCTURE\_TYPE\_HPS\_RADIX\_SORT。
