---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xeg-hpscreateinfo
title: XEG_HPSCreateInfo
breadcrumb: API参考 > 图形 > XEngine Kit（GPU加速引擎服务） > C API > 头文件和结构体 > 结构体 > XEG_HPSCreateInfo
category: harmonyos-references
scraped_at: 2026-04-28T08:16:00+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:86619c40e2ffc3d43a4554be23f9ae78fffd5f93826a8de3059ad18cd85f9a7f
---

## 概述

PhonePC/2in1TabletTV

此结构体描述创建[XEG\_HPS](xengine-kit-xengine.md#xeg_hps)对象的信息。

**起始版本：** 6.0.0(20)

**相关模块：** [XEngine](xengine-kit-xengine.md)

**所在头文件：** [xeg\_vulkan\_hps.h](xengine-kit-xeg-vulkan-hps-8h.md)

## 汇总

PhonePC/2in1TabletTV

### 成员变量

PhonePC/2in1TabletTV

| 名称 | 描述 |
| --- | --- |
| XEG\_StructureType [sType](xengine-kit-xeg-hpscreateinfo.md#stype) | 识别此结构的[XEG\_StructureType](xengine-kit-xengine.md#xeg_structuretype)值，必须是XEG\_STRUCTURE\_TYPE\_HPS\_CREATE\_INFO。 |
| const void \* [pNext](xengine-kit-xeg-hpscreateinfo.md#pnext) | 指向扩展结构的指针，不允许为空。表示启用的XEngine HPS扩展，如当使用[XEG\_HPS\_RADIX\_SORT\_EXTENSION\_NAME](xengine-kit-xengine.md#xeg_hps_radix_sort_extension_name)扩展时，必须指定为[XEG\_HPSRadixSort](xengine-kit-xeg-hpsradixsort.md)。 |

## 结构体成员变量说明

PhonePC/2in1TabletTV

### pNext

PhonePC/2in1TabletTV

```
1. const void* XEG_HPSCreateInfo::pNext
```

**描述**

指向扩展结构的指针，不允许为空。表示启用的XEngine HPS扩展，如当使用[XEG\_HPS\_RADIX\_SORT\_EXTENSION\_NAME](xengine-kit-xengine.md#xeg_hps_radix_sort_extension_name)扩展时，必须指定为[XEG\_HPSRadixSort](xengine-kit-xeg-hpsradixsort.md)。

### sType

PhonePC/2in1TabletTV

```
1. XEG_StructureType XEG_HPSCreateInfo::sType
```

**描述**

识别此结构的[XEG\_StructureType](xengine-kit-xengine.md#xeg_structuretype)值，必须是XEG\_STRUCTURE\_TYPE\_HPS\_CREATE\_INFO。
