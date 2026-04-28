---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xeg-ddgidescription
title: XEG_DDGIDescription
breadcrumb: API参考 > 图形 > XEngine Kit（GPU加速引擎服务） > C API > 头文件和结构体 > 结构体 > XEG_DDGIDescription
category: harmonyos-references
scraped_at: 2026-04-28T08:16:00+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:fe390eff7cf8ca7a80a01dcc344cd0b9763b3ed420f300b46b900bf3c348e52f
---

## 概述

PhonePC/2in1TabletTV

此结构体描述更新DDGI探针辐照度及渲染输出GI图像所需的信息。

**起始版本：** 6.0.0(20)

**相关模块：** [XEngine](xengine-kit-xengine.md)

**所在头文件：** [xeg\_vulkan\_rtgi.h](xengine-kit-xeg-vulkan-rtgi-8h.md)

## 汇总

PhonePC/2in1TabletTV

### 成员变量

PhonePC/2in1TabletTV

| 名称 | 描述 |
| --- | --- |
| XEG\_StructureType [sType](xengine-kit-xeg-ddgidescription.md#stype) | 识别此结构的[XEG\_StructureType](xengine-kit-xengine.md#xeg_structuretype)值，必须是XEG\_STRUCTURE\_TYPE\_DDGI\_DESCRIPTION。 |
| const void \* [pNext](xengine-kit-xeg-ddgidescription.md#pnext) | 指向扩展结构的指针。 |
| float [viewMatrix](xengine-kit-xeg-ddgidescription.md#viewmatrix) [16] | 相机观察矩阵，必须是4\*4列主序矩阵。 |
| float [projectionMatrix](xengine-kit-xeg-ddgidescription.md#projectionmatrix) [16] | 相机投影矩阵，必须是4\*4列主序矩阵。 |
| VkImageView [inputNormalImage](xengine-kit-xeg-ddgidescription.md#inputnormalimage) | 输入Gbuffer法向量图像，其宽高必须和[XEG\_DDGICreateInfo](xengine-kit-xeg-ddgicreateinfo.md)中viewSize的宽高保持一致。 |
| VkImageView [inputDepthImage](xengine-kit-xeg-ddgidescription.md#inputdepthimage) | 输入Gbuffer深度图像，其宽高必须和[XEG\_DDGICreateInfo](xengine-kit-xeg-ddgicreateinfo.md)中viewSize的宽高保持一致。 |
| VkImageView [inputBasecolorMetallicImage](xengine-kit-xeg-ddgidescription.md#inputbasecolormetallicimage) | 输入Gbuffer基础颜色和金属度图像，其宽高必须和[XEG\_DDGICreateInfo](xengine-kit-xeg-ddgicreateinfo.md)中viewSize的宽高保持一致。 |
| VkImageView [inputDirectionImage](xengine-kit-xeg-ddgidescription.md#inputdirectionimage) | 输入探针发射光线方向图像，其宽高分别为：探针发射光线数量，输入探针数量。 |
| VkImageView [inputRayRadianceDistanceImage](xengine-kit-xeg-ddgidescription.md#inputrayradiancedistanceimage) | 输入探针发射光线交点的辐射率及距离图像，其宽高分别为：探针发射光线数量，输入探针数量。 |
| VkImageView [inputRayHitNormalAndMetallicImage](xengine-kit-xeg-ddgidescription.md#inputrayhitnormalandmetallicimage) | 输入探针发射光线交点的法向量及金属度图像，其宽高分别为：探针发射光线数量，输入探针数量。 |
| VkBuffer [inputVolumeIndexAndProbeIndex](xengine-kit-xeg-ddgidescription.md#inputvolumeindexandprobeindex) | 输入探针的索引信息，对应于探针发射光线的信息，每个数据为两个uint值（探针索引/体积索引）。 |
| uint32\_t [inputProbeCount](xengine-kit-xeg-ddgidescription.md#inputprobecount) | 输入探针数量，对应于inputVolumeIndexAndProbeIndex中的有效数据个数。 |
| VkBuffer [outputVolumeIndexAndProbeIndex](xengine-kit-xeg-ddgidescription.md#outputvolumeindexandprobeindex) | 输出探针的索引信息，指示用户下一帧如何发射光线，每个数据为两个uint值（探针索引/体积索引）。 |
| VkBuffer [outputProbeCount](xengine-kit-xeg-ddgidescription.md#outputprobecount) | 输出探针数量，对应于outputVolumeIndexAndProbeIndex中的有效数据个数。 |
| VkImageView [outputGIImage](xengine-kit-xeg-ddgidescription.md#outputgiimage) | 输出GI 2D图像，其宽高必须和[XEG\_DDGICreateInfo](xengine-kit-xeg-ddgicreateinfo.md)中viewSize的宽高保持一致，VkFormat为VK\_FORMAT\_R8G8B8A8\_UNORM。 |
| uint32\_t [enableVolumeNumber](xengine-kit-xeg-ddgidescription.md#enablevolumenumber) | 使用的体积数量，必须不大于[XEG\_DDGICreateInfo](xengine-kit-xeg-ddgicreateinfo.md)中的numberVolume值。 |
| const struct [XEG\_DDGIVolumeEntryParameters](xengine-kit-xeg-ddgivolumeentryparameters.md) \* [pVolumeEntryParameters](xengine-kit-xeg-ddgidescription.md#pvolumeentryparameters) | 输入体积参数信息，对应于[XEG\_DDGIVolumeEntryParameters](xengine-kit-xeg-ddgivolumeentryparameters.md)。该结构体数组的大小必须等于enableVolumeNumber的值。 |

## 结构体成员变量说明

PhonePC/2in1TabletTV

### enableVolumeNumber

PhonePC/2in1TabletTV

```
1. uint32_t XEG_DDGIDescription::enableVolumeNumber
```

**描述**

使用的体积数量，必须不大于[XEG\_DDGICreateInfo](xengine-kit-xeg-ddgicreateinfo.md)中的numberVolume值。

### inputBasecolorMetallicImage

PhonePC/2in1TabletTV

```
1. VkImageView XEG_DDGIDescription::inputBasecolorMetallicImage
```

**描述**

输入Gbuffer基础颜色和金属度图像，其宽高必须和[XEG\_DDGICreateInfo](xengine-kit-xeg-ddgicreateinfo.md)中viewSize的宽高保持一致。

### inputDepthImage

PhonePC/2in1TabletTV

```
1. VkImageView XEG_DDGIDescription::inputDepthImage
```

**描述**

输入Gbuffer深度图像，其宽高必须和[XEG\_DDGICreateInfo](xengine-kit-xeg-ddgicreateinfo.md)中viewSize的宽高保持一致。

### inputDirectionImage

PhonePC/2in1TabletTV

```
1. VkImageView XEG_DDGIDescription::inputDirectionImage
```

**描述**

输入探针发射光线方向图像，其宽高分别为：探针发射光线数量，输入探针数量。

### inputNormalImage

PhonePC/2in1TabletTV

```
1. VkImageView XEG_DDGIDescription::inputNormalImage
```

**描述**

输入Gbuffer法向量图像，其宽高必须和[XEG\_DDGICreateInfo](xengine-kit-xeg-ddgicreateinfo.md)中viewSize的宽高保持一致。

### inputProbeCount

PhonePC/2in1TabletTV

```
1. uint32_t XEG_DDGIDescription::inputProbeCount
```

**描述**

输入探针数量，对应于inputVolumeIndexAndProbeIndex中的有效数据个数。

### inputRayHitNormalAndMetallicImage

PhonePC/2in1TabletTV

```
1. VkImageView XEG_DDGIDescription::inputRayHitNormalAndMetallicImage
```

**描述**

输入探针发射光线交点的法向量及金属度图像，其宽高分别为：探针发射光线数量，输入探针数量。

### inputRayRadianceDistanceImage

PhonePC/2in1TabletTV

```
1. VkImageView XEG_DDGIDescription::inputRayRadianceDistanceImage
```

**描述**

输入探针发射光线交点的辐射率及距离图像，其宽高分别为：探针发射光线数量，输入探针数量。

### inputVolumeIndexAndProbeIndex

PhonePC/2in1TabletTV

```
1. VkBuffer XEG_DDGIDescription::inputVolumeIndexAndProbeIndex
```

**描述**

输入探针的索引信息，对应于探针发射光线的信息，每个数据为两个uint值（探针索引/体积索引）。

### outputGIImage

PhonePC/2in1TabletTV

```
1. VkImageView XEG_DDGIDescription::outputGIImage
```

**描述**

输出GI 2D图像，其宽高必须和[XEG\_DDGICreateInfo](xengine-kit-xeg-ddgicreateinfo.md)中viewSize的宽高保持一致，VkFormat为VK\_FORMAT\_R8G8B8A8\_UNORM。

### outputProbeCount

PhonePC/2in1TabletTV

```
1. VkBuffer XEG_DDGIDescription::outputProbeCount
```

**描述**

输出探针数量，对应于outputVolumeIndexAndProbeIndex中的有效数据个数。

### outputVolumeIndexAndProbeIndex

PhonePC/2in1TabletTV

```
1. VkBuffer XEG_DDGIDescription::outputVolumeIndexAndProbeIndex
```

**描述**

输出探针的索引信息，指示用户下一帧如何发射光线，每个数据为两个uint值（探针索引/体积索引）。

### pNext

PhonePC/2in1TabletTV

```
1. const void* XEG_DDGIDescription::pNext
```

**描述**

指向扩展结构的指针。

### projectionMatrix

PhonePC/2in1TabletTV

```
1. float XEG_DDGIDescription::projectionMatrix[16]
```

**描述**

相机投影矩阵，必须是4\*4列主序矩阵。

### pVolumeEntryParameters

PhonePC/2in1TabletTV

```
1. const struct XEG_DDGIVolumeEntryParameters* XEG_DDGIDescription::pVolumeEntryParameters
```

**描述**

输入体积参数信息，对应于[XEG\_DDGIVolumeEntryParameters](xengine-kit-xeg-ddgivolumeentryparameters.md)。该结构体数组的大小必须等于enableVolumeNumber的值。

### sType

PhonePC/2in1TabletTV

```
1. XEG_StructureType XEG_DDGIDescription::sType
```

**描述**

识别此结构的[XEG\_StructureType](xengine-kit-xengine.md#xeg_structuretype)值，必须是XEG\_STRUCTURE\_TYPE\_DDGI\_DESCRIPTION。

### viewMatrix

PhonePC/2in1TabletTV

```
1. float XEG_DDGIDescription::viewMatrix[16]
```

**描述**

相机观察矩阵，必须是4\*4列主序矩阵。
