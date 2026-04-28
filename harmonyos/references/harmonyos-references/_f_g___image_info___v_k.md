---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_f_g___image_info___v_k
title: FG_ImageInfo_VK
breadcrumb: API参考 > 图形 > Graphics Accelerate Kit（图形加速服务） > C API > 头文件和结构体 > 结构体 > FG_ImageInfo_VK
category: harmonyos-references
scraped_at: 2026-04-28T08:15:46+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:b303357184412cd67d18766fdd3af51649d849e5f519036017d86b4304382f78
---

## 概述

PhoneTabletTV

此结构体描述超帧输入输出图像信息。

**起始版本：** 5.0.0(12)

**相关模块：** [GraphicsAccelerate](_graphics_accelerate.md)

**所在头文件：** [frame\_generation\_vk.h](frame__generation__vk_8h.md)

## 汇总

PhoneTabletTV

### 成员变量

PhoneTabletTV

| 名称 | 描述 |
| --- | --- |
| [FG\_Image\_VK](_graphics_accelerate.md#fg_image_vk)\* [image](_f_g___image_info___v_k.md#image) | 超帧输入输出图像结构体[FG\_Image\_VK](_graphics_accelerate.md#fg_image_vk)对象的指针，该图像实例需要通过[HMS\_FG\_CreateImage\_VK](_graphics_accelerate.md#hms_fg_createimage_vk)进行创建，通过[HMS\_FG\_DestroyImage\_VK](_graphics_accelerate.md#hms_fg_destroyimage_vk)进行销毁。 |
| [FG\_ImageSync\_VK](_f_g___image_sync___v_k.md) [initialSync](_f_g___image_info___v_k.md#initialsync) | [HMS\_FG\_Dispatch\_VK](_graphics_accelerate.md#hms_fg_dispatch_vk)执行前，该图像的同步状态。 |
| [FG\_ImageSync\_VK](_f_g___image_sync___v_k.md) [finalSync](_f_g___image_info___v_k.md#finalsync) | [HMS\_FG\_Dispatch\_VK](_graphics_accelerate.md#hms_fg_dispatch_vk)执行后，该图像的同步状态。 |

## 结构体成员变量说明

PhoneTabletTV

### finalSync

PhoneTabletTV

```
1. FG_ImageSync_VK FG_ImageInfo_VK::finalSync
```

**描述**

[HMS\_FG\_Dispatch\_VK](_graphics_accelerate.md#hms_fg_dispatch_vk)执行后，该图像的同步状态。

### image

PhoneTabletTV

```
1. FG_Image_VK* FG_ImageInfo_VK::image
```

**描述**

超帧输入输出图像结构体[FG\_Image\_VK](_graphics_accelerate.md#fg_image_vk)对象的指针，该图像实例需要通过[HMS\_FG\_CreateImage\_VK](_graphics_accelerate.md#hms_fg_createimage_vk)进行创建，通过[HMS\_FG\_DestroyImage\_VK](_graphics_accelerate.md#hms_fg_destroyimage_vk)进行销毁。

### initialSync

PhoneTabletTV

```
1. FG_ImageSync_VK FG_ImageInfo_VK::initialSync
```

**描述**

[HMS\_FG\_Dispatch\_VK](_graphics_accelerate.md#hms_fg_dispatch_vk)执行前，该图像的同步状态。
