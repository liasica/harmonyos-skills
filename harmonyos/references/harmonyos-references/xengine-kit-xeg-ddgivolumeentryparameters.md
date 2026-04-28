---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xeg-ddgivolumeentryparameters
title: XEG_DDGIVolumeEntryParameters
breadcrumb: API参考 > 图形 > XEngine Kit（GPU加速引擎服务） > C API > 头文件和结构体 > 结构体 > XEG_DDGIVolumeEntryParameters
category: harmonyos-references
scraped_at: 2026-04-28T08:16:00+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:1b87521a6bfbaeb89d656c12f456cad2508b8d5786509009ecb7afc023e8a3b7
---

## 概述

PhonePC/2in1TabletTV

此结构体描述每一个DDGI体积的必要参数。

**起始版本：** 6.0.0(20)

**相关模块：** [XEngine](xengine-kit-xengine.md)

**所在头文件：** [xeg\_vulkan\_rtgi.h](xengine-kit-xeg-vulkan-rtgi-8h.md)

## 汇总

PhonePC/2in1TabletTV

### 成员变量

PhonePC/2in1TabletTV

| 名称 | 描述 |
| --- | --- |
| uint32\_t [volumeIndex](xengine-kit-xeg-ddgivolumeentryparameters.md#volumeindex) | 体积索引范围为[0, 65535]，且唯一。 |
| uint32\_t [raysPerProbe](xengine-kit-xeg-ddgivolumeentryparameters.md#raysperprobe) | 探针发射光线数量，建议值为64，范围为[1, 1024]。 |
| float [probeMaxRayDistance](xengine-kit-xeg-ddgivolumeentryparameters.md#probemaxraydistance) | 探针发射光线最大求交距离，建议值为1000.0。 |
| float [volumePosition](xengine-kit-xeg-ddgivolumeentryparameters.md#volumeposition) [3] | 体积中心点坐标。 |
| float [probeSpacing](xengine-kit-xeg-ddgivolumeentryparameters.md#probespacing) [3] | 探针放置间距，必须大于0。 |
| uint32\_t [volumeLightingChannelMask](xengine-kit-xeg-ddgivolumeentryparameters.md#volumelightingchannelmask) | 体积光照通道标记，建议值为0xFFFFFFFF。 |
| uint32\_t [volumeProbeGridCounts](xengine-kit-xeg-ddgivolumeentryparameters.md#volumeprobegridcounts) [3] | 探针放置数量，必须大于0，范围为[1, 32]。 |
| float [volumeProbeIrradianceEncodingGamma](xengine-kit-xeg-ddgivolumeentryparameters.md#volumeprobeirradianceencodinggamma) | 辐照度的伽马校正系数，建议值为5.0，必须不为0。 |
| float [probeHysteresis](xengine-kit-xeg-ddgivolumeentryparameters.md#probehysteresis) | 探针辐照度历史权重，建议值为0.95，范围为[0, 1]。 |
| float [probeChangeThreshold](xengine-kit-xeg-ddgivolumeentryparameters.md#probechangethreshold) | 探针变化阈值，建议值为1.0。 |
| float [probeBrightnessThreshold](xengine-kit-xeg-ddgivolumeentryparameters.md#probebrightnessthreshold) | 探针亮度阈值，建议值为1.0。 |
| float [volumeNormalBias](xengine-kit-xeg-ddgivolumeentryparameters.md#volumenormalbias) | 探针法向偏移量，建议值为0.12。 |
| float [volumeViewBias](xengine-kit-xeg-ddgivolumeentryparameters.md#volumeviewbias) | 探针视角偏移量，建议值为0.48。 |
| float [volumeBlendDistance](xengine-kit-xeg-ddgivolumeentryparameters.md#volumeblenddistance) | 体积光照混合距离，建议值为1.0。 |
| float [volumeBlendDistanceBlack](xengine-kit-xeg-ddgivolumeentryparameters.md#volumeblenddistanceblack) | 体积边缘光照渐暗范围，建议值为1.0。 |
| float [probeBackfaceThreshold](xengine-kit-xeg-ddgivolumeentryparameters.md#probebackfacethreshold) | 探针反向判断阈值，建议值为0.0。 |
| float [probeMinFrontfaceDistance](xengine-kit-xeg-ddgivolumeentryparameters.md#probeminfrontfacedistance) | 探针正向最小距离，建议值为0.0。 |
| float [volumeIrradianceScalar](xengine-kit-xeg-ddgivolumeentryparameters.md#volumeirradiancescalar) | 体积辐照度缩放倍率，建议值为1.0，必须非负。 |
| float [emissiveMultiplier](xengine-kit-xeg-ddgivolumeentryparameters.md#emissivemultiplier) | 发射光线强度倍率，建议值为1.0，必须非负。 |
| float [lightingMultiplier](xengine-kit-xeg-ddgivolumeentryparameters.md#lightingmultiplier) | 光照倍率，建议值为1.0，必须非负。 |
| bool [bForceUpdate](xengine-kit-xeg-ddgivolumeentryparameters.md#bforceupdate) | 是否强制更新所有探针，true为强制全部更新，false为选择部分更新，建议值为false。 |
| VkImageView [probeIrradianceSH](xengine-kit-xeg-ddgivolumeentryparameters.md#probeirradiancesh) | 存储探针辐照度二阶球谐系数的3D图像，其宽度，高度和深度分别为：volumeProbeGridCounts.y \* 4（二阶球谐系数的个数），volumeProbeGridCounts.x，volumeProbeGridCounts.z，VkFormat为VK\_FORMAT\_R32G32B32A32\_SFLOAT。 |

## 结构体成员变量说明

PhonePC/2in1TabletTV

### bForceUpdate

PhonePC/2in1TabletTV

```
1. bool XEG_DDGIVolumeEntryParameters::bForceUpdate
```

**描述**

是否强制更新所有探针，true为强制全部更新，false为选择部分更新，建议值为false。

### emissiveMultiplier

PhonePC/2in1TabletTV

```
1. float XEG_DDGIVolumeEntryParameters::emissiveMultiplier
```

**描述**

发射光线强度倍率，建议值为1.0，必须非负。

### lightingMultiplier

PhonePC/2in1TabletTV

```
1. float XEG_DDGIVolumeEntryParameters::lightingMultiplier
```

**描述**

光照倍率，建议值为1.0，必须非负。

### probeBackfaceThreshold

PhonePC/2in1TabletTV

```
1. float XEG_DDGIVolumeEntryParameters::probeBackfaceThreshold
```

**描述**

探针反向判断阈值，建议值为0.0。

### probeBrightnessThreshold

PhonePC/2in1TabletTV

```
1. float XEG_DDGIVolumeEntryParameters::probeBrightnessThreshold
```

**描述**

探针亮度阈值，建议值为1.0。

### probeChangeThreshold

PhonePC/2in1TabletTV

```
1. float XEG_DDGIVolumeEntryParameters::probeChangeThreshold
```

**描述**

探针变化阈值，建议值为1.0。

### probeHysteresis

PhonePC/2in1TabletTV

```
1. float XEG_DDGIVolumeEntryParameters::probeHysteresis
```

**描述**

探针辐照度历史权重，建议值为0.95，范围为[0, 1]。

### probeIrradianceSH

PhonePC/2in1TabletTV

```
1. VkImageView XEG_DDGIVolumeEntryParameters::probeIrradianceSH
```

**描述**

存储探针辐照度二阶球谐系数的3D图像，其宽度，高度和深度分别为：volumeProbeGridCounts.y \* 4（二阶球谐系数的个数），volumeProbeGridCounts.x，volumeProbeGridCounts.z，VkFormat为VK\_FORMAT\_R32G32B32A32\_SFLOAT。

### probeMaxRayDistance

PhonePC/2in1TabletTV

```
1. float XEG_DDGIVolumeEntryParameters::probeMaxRayDistance
```

**描述**

探针发射光线最大求交距离，建议值为1000.0。

### probeMinFrontfaceDistance

PhonePC/2in1TabletTV

```
1. float XEG_DDGIVolumeEntryParameters::probeMinFrontfaceDistance
```

**描述**

探针正向最小距离，建议值为0.0。

### probeSpacing

PhonePC/2in1TabletTV

```
1. float XEG_DDGIVolumeEntryParameters::probeSpacing[3]
```

**描述**

探针放置间距，必须大于0。

### raysPerProbe

PhonePC/2in1TabletTV

```
1. uint32_t XEG_DDGIVolumeEntryParameters::raysPerProbe
```

**描述**

探针发射光线数量，建议值为64，范围为[1, 1024]。

### volumeBlendDistance

PhonePC/2in1TabletTV

```
1. float XEG_DDGIVolumeEntryParameters::volumeBlendDistance
```

**描述**

体积光照混合距离，建议值为1.0。

### volumeBlendDistanceBlack

PhonePC/2in1TabletTV

```
1. float XEG_DDGIVolumeEntryParameters::volumeBlendDistanceBlack
```

**描述**

体积边缘光照渐暗范围，建议值为1.0。

### volumeIndex

PhonePC/2in1TabletTV

```
1. uint32_t XEG_DDGIVolumeEntryParameters::volumeIndex
```

**描述**

体积索引范围为[0, 65535]，且唯一。

### volumeIrradianceScalar

PhonePC/2in1TabletTV

```
1. float XEG_DDGIVolumeEntryParameters::volumeIrradianceScalar
```

**描述**

体积辐照度缩放倍率，建议值为1.0，必须非负。

### volumeLightingChannelMask

PhonePC/2in1TabletTV

```
1. uint32_t XEG_DDGIVolumeEntryParameters::volumeLightingChannelMask
```

**描述**

体积光照通道标记，建议值为0xFFFFFFFF。

### volumeNormalBias

PhonePC/2in1TabletTV

```
1. float XEG_DDGIVolumeEntryParameters::volumeNormalBias
```

**描述**

探针法向偏移量，建议值为0.12。

### volumePosition

PhonePC/2in1TabletTV

```
1. float XEG_DDGIVolumeEntryParameters::volumePosition[3]
```

**描述**

体积中心点坐标。

### volumeProbeGridCounts

PhonePC/2in1TabletTV

```
1. uint32_t XEG_DDGIVolumeEntryParameters::volumeProbeGridCounts[3]
```

**描述**

探针放置数量，必须大于0，范围为[1, 32]。

### volumeProbeIrradianceEncodingGamma

PhonePC/2in1TabletTV

```
1. float XEG_DDGIVolumeEntryParameters::volumeProbeIrradianceEncodingGamma
```

**描述**

辐照度的伽马校正系数，建议值为5.0，必须不为0。

### volumeViewBias

PhonePC/2in1TabletTV

```
1. float XEG_DDGIVolumeEntryParameters::volumeViewBias
```

**描述**

探针视角偏移量，建议值为0.48。
