---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xeg-hpsradixsort
title: XEG_HPSRadixSort
breadcrumb: API参考 > 图形 > XEngine Kit（GPU加速引擎服务） > C API > 头文件和结构体 > 结构体 > XEG_HPSRadixSort
category: harmonyos-references
scraped_at: 2026-04-28T08:16:01+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:c18a2bbd55150a7d1d12495dc86f56fb3ff17e3c1fe0bdfa015227490aaa0660
---

## 概述

PhonePC/2in1TabletTV

此结构体描述HPS基数排序扩展结构信息。

**起始版本：** 6.0.0(20)

**相关模块：** [XEngine](xengine-kit-xengine.md)

**所在头文件：** [xeg\_vulkan\_hps.h](xengine-kit-xeg-vulkan-hps-8h.md)

## 汇总

PhonePC/2in1TabletTV

### 成员变量

PhonePC/2in1TabletTV

| 名称 | 描述 |
| --- | --- |
| XEG\_StructureType [sType](xengine-kit-xeg-hpsradixsort.md#stype) | 识别此结构的[XEG\_StructureType](xengine-kit-xengine.md#xeg_structuretype)值，必须是XEG\_STRUCTURE\_TYPE\_HPS\_RADIX\_SORT。 |
| const void \* [pNext](xengine-kit-xeg-hpsradixsort.md#pnext) | 指向扩展结构的指针。 |

## 结构体成员变量说明

PhonePC/2in1TabletTV

### pNext

PhonePC/2in1TabletTV

```
1. const void* XEG_HPSRadixSort::pNext
```

**描述**

指向扩展结构的指针。

### sType

PhonePC/2in1TabletTV

```
1. XEG_StructureType XEG_HPSRadixSort::sType
```

**描述**

识别此结构的[XEG\_StructureType](xengine-kit-xengine.md#xeg_structuretype)值，必须是XEG\_STRUCTURE\_TYPE\_HPS\_RADIX\_SORT。
