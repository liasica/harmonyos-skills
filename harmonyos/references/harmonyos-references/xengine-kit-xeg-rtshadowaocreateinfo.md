---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xeg-rtshadowaocreateinfo
title: XEG_RTShadowAOCreateInfo
breadcrumb: API参考 > 图形 > XEngine Kit（GPU加速引擎服务） > C API > 头文件和结构体 > 结构体 > XEG_RTShadowAOCreateInfo
category: harmonyos-references
scraped_at: 2026-04-28T08:16:02+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:877e0d6cf7447285312f741b8af0a5e250898a240412ffb370ab259249f60d0a
---

## 概述

PhonePC/2in1TabletTV

此结构体描述创建支持光线追踪阴影和环境光遮蔽效果[XEG\_RTVisibleMask](xengine-kit-xengine.md#xeg_rtvisiblemask)实例的初始化信息。当结构体中的信息变化时，需要创建新的[XEG\_RTVisibleMask](xengine-kit-xengine.md#xeg_rtvisiblemask)对象。

**起始版本：** 6.0.0(20)

**相关模块：** [XEngine](xengine-kit-xengine.md)

**所在头文件：** [xeg\_vulkan\_rt\_visible\_mask.h](xengine-kit-xeg-vulkan-rt-visible-mask-8h.md)

## 汇总

PhonePC/2in1TabletTV

### 成员变量

PhonePC/2in1TabletTV

| 名称 | 描述 |
| --- | --- |
| XEG\_StructureType [sType](xengine-kit-xeg-rtshadowaocreateinfo.md#stype) | 识别此结构的[XEG\_StructureType](xengine-kit-xengine.md#xeg_structuretype)值，必须是XEG\_STRUCTURE\_TYPE\_RT\_SHADOWAO\_CREATE\_INFO。 |
| const void \* [pNext](xengine-kit-xeg-rtshadowaocreateinfo.md#pnext) | 指向扩展结构的指针。 |
| VkExtent2D [rtInputGbufferSize](xengine-kit-xeg-rtshadowaocreateinfo.md#rtinputgbuffersize) | 输入的GBuffer深度和法线图像的尺寸，深度图像和法线图像的尺寸必须相同。 |
| VkExtent2D [rtShadowAOSize](xengine-kit-xeg-rtshadowaocreateinfo.md#rtshadowaosize) | 输出的阴影和环境光遮蔽图像的尺寸，必须与rtInputGbufferSize等比例。 |
| bool [enableRTShadow](xengine-kit-xeg-rtshadowaocreateinfo.md#enablertshadow) | 是否开启光线追踪阴影效果，true为开启，false为不开启。阴影与环境光遮蔽效果至少需要开启一个。 |
| bool [enableRTAO](xengine-kit-xeg-rtshadowaocreateinfo.md#enablertao) | 是否开启光线追踪环境光遮蔽效果，true为开启，false为不开启。阴影与环境光遮蔽效果至少需要开启一个。 |
| XEG\_TraversalMode [traversalMode](xengine-kit-xeg-rtshadowaocreateinfo.md#traversalmode) | 遍历模式，光线追踪阴影和环境光遮蔽使用相同的遍历模式设置。 |
| XEG\_DenoiseQualityMode [denoiseMode](xengine-kit-xeg-rtshadowaocreateinfo.md#denoisemode) | 去噪质量模式，光线追踪阴影和环境光遮蔽使用相同的质量设置。 |
| bool [aoOnlyInShadow](xengine-kit-xeg-rtshadowaocreateinfo.md#aoonlyinshadow) | 仅在开启光线追踪阴影效果时生效，如果设置为true，将只计算处于阴影区域的像素的环境光遮蔽值。如果设置为false则计算所有像素。 |
| bool [reverseZ](xengine-kit-xeg-rtshadowaocreateinfo.md#reversez) | 场景是否开启了深度翻转，即远平面处的深度为0。深度翻转可以获取更高精度的深度值，建议开启。true表示已开启，false表示未开启。 |

## 结构体成员变量说明

PhonePC/2in1TabletTV

### aoOnlyInShadow

PhonePC/2in1TabletTV

```
1. bool XEG_RTShadowAOCreateInfo::aoOnlyInShadow
```

**描述**

仅在开启光线追踪阴影效果时生效，如果设置为true，将只计算处于阴影区域的像素的环境光遮蔽值。如果设置为false则计算所有像素。

### denoiseMode

PhonePC/2in1TabletTV

```
1. XEG_DenoiseQualityMode XEG_RTShadowAOCreateInfo::denoiseMode
```

**描述**

去噪质量模式，光线追踪阴影和环境光遮蔽使用相同的质量设置。

### enableRTAO

PhonePC/2in1TabletTV

```
1. bool XEG_RTShadowAOCreateInfo::enableRTAO
```

**描述**

是否开启光线追踪环境光遮蔽效果，true为开启，false为不开启。阴影与环境光遮蔽效果至少需要开启一个。

### enableRTShadow

PhonePC/2in1TabletTV

```
1. bool XEG_RTShadowAOCreateInfo::enableRTShadow
```

**描述**

是否开启光线追踪阴影效果，true为开启，false为不开启。阴影与环境光遮蔽效果至少需要开启一个。

### pNext

PhonePC/2in1TabletTV

```
1. const void* XEG_RTShadowAOCreateInfo::pNext
```

**描述**

指向扩展结构的指针。

### reverseZ

PhonePC/2in1TabletTV

```
1. bool XEG_RTShadowAOCreateInfo::reverseZ
```

**描述**

场景是否开启了深度翻转，即远平面处的深度为0。深度翻转可以获取更高精度的深度值，建议开启。true表示已开启，false表示未开启。

### rtInputGbufferSize

PhonePC/2in1TabletTV

```
1. VkExtent2D XEG_RTShadowAOCreateInfo::rtInputGbufferSize
```

**描述**

输入的GBuffer深度和法线图像的尺寸，深度图像和法线图像的尺寸必须相同。

### rtShadowAOSize

PhonePC/2in1TabletTV

```
1. VkExtent2D XEG_RTShadowAOCreateInfo::rtShadowAOSize
```

**描述**

输出的阴影和环境光遮蔽图像的尺寸，必须与rtInputGbufferSize等比例。

### sType

PhonePC/2in1TabletTV

```
1. XEG_StructureType XEG_RTShadowAOCreateInfo::sType
```

**描述**

识别此结构的[XEG\_StructureType](xengine-kit-xengine.md#xeg_structuretype)值，必须是XEG\_STRUCTURE\_TYPE\_RT\_SHADOWAO\_CREATE\_INFO。

### traversalMode

PhonePC/2in1TabletTV

```
1. XEG_TraversalMode XEG_RTShadowAOCreateInfo::traversalMode
```

**描述**

遍历模式，光线追踪阴影和环境光遮蔽使用相同的遍历模式设置。
