---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xeg-rtreflectioncreateinfo
title: XEG_RTReflectionCreateInfo
breadcrumb: API参考 > 图形 > XEngine Kit（GPU加速引擎服务） > C API > 头文件和结构体 > 结构体 > XEG_RTReflectionCreateInfo
category: harmonyos-references
scraped_at: 2026-04-28T08:16:02+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:697977a70dfe4d33e839d8df86b8ad3f37b2b98aa246984d07a5823709a30027
---

## 概述

PhonePC/2in1TabletTV

此结构体描述创建[XEG\_RTReflection](xengine-kit-xengine.md#xeg_rtreflection)对象的信息。当结构体中的信息变化时，需要创建新的[XEG\_RTReflection](xengine-kit-xengine.md#xeg_rtreflection)对象。

**起始版本：** 6.0.0(20)

**相关模块：** [XEngine](xengine-kit-xengine.md)

**所在头文件：** [xeg\_vulkan\_rt\_reflection.h](xengine-kit-xeg-vulkan-rt-reflection-8h.md)

## 汇总

PhonePC/2in1TabletTV

### 成员变量

PhonePC/2in1TabletTV

| 名称 | 描述 |
| --- | --- |
| XEG\_StructureType [sType](xengine-kit-xeg-rtreflectioncreateinfo.md#stype) | 识别此结构的[XEG\_StructureType](xengine-kit-xengine.md#xeg_structuretype)值，必须是XEG\_STRUCTURE\_TYPE\_RT\_REFLECTION\_CREATE\_INFO。 |
| const void \* [pNext](xengine-kit-xeg-rtreflectioncreateinfo.md#pnext) | 指向扩展结构的指针。 |
| VkExtent2D [renderSize](xengine-kit-xeg-rtreflectioncreateinfo.md#rendersize) | 输入图像的尺寸。 |
| bool [enableFastTrace](xengine-kit-xeg-rtreflectioncreateinfo.md#enablefasttrace) | 是否开启快速求交模式，相较常规求交模式，快速求交模式的性能更好。true表示开启快速求交模式，false表示使用常规求交模式。 |

## 结构体成员变量说明

PhonePC/2in1TabletTV

### enableFastTrace

PhonePC/2in1TabletTV

```
1. bool XEG_RTReflectionCreateInfo::enableFastTrace
```

**描述**

是否开启快速求交模式，相较常规求交模式，快速求交模式的性能更好。true表示开启快速求交模式，false表示使用常规求交模式。

### pNext

PhonePC/2in1TabletTV

```
1. const void* XEG_RTReflectionCreateInfo::pNext
```

**描述**

指向扩展结构的指针。

### renderSize

PhonePC/2in1TabletTV

```
1. VkExtent2D XEG_RTReflectionCreateInfo::renderSize
```

**描述**

输入图像的尺寸。

### sType

PhonePC/2in1TabletTV

```
1. XEG_StructureType XEG_RTReflectionCreateInfo::sType
```

**描述**

识别此结构的[XEG\_StructureType](xengine-kit-xengine.md#xeg_structuretype)值，必须是XEG\_STRUCTURE\_TYPE\_RT\_REFLECTION\_CREATE\_INFO。
