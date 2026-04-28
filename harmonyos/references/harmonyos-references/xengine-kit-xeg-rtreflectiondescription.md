---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xeg-rtreflectiondescription
title: XEG_RTReflectionDescription
breadcrumb: API参考 > 图形 > XEngine Kit（GPU加速引擎服务） > C API > 头文件和结构体 > 结构体 > XEG_RTReflectionDescription
category: harmonyos-references
scraped_at: 2026-04-28T08:16:02+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:8aa927c1f9aad906a1afc7acd34ce1afd866c7cc061179740e7935bee406d063
---

## 概述

PhonePC/2in1TabletTV

此结构体描述下发光线求交命令时的输入信息。

**起始版本：** 6.0.0(20)

**相关模块：** [XEngine](xengine-kit-xengine.md)

**所在头文件：** [xeg\_vulkan\_rt\_reflection.h](xengine-kit-xeg-vulkan-rt-reflection-8h.md)

## 汇总

PhonePC/2in1TabletTV

### 成员变量

PhonePC/2in1TabletTV

| 名称 | 描述 |
| --- | --- |
| XEG\_StructureType [sType](xengine-kit-xeg-rtreflectiondescription.md#stype) | 识别此结构的[XEG\_StructureType](xengine-kit-xengine.md#xeg_structuretype)值，必须是XEG\_STRUCTURE\_TYPE\_RT\_REFLECTION\_DESCRIPTION。 |
| const void \* [pNext](xengine-kit-xeg-rtreflectiondescription.md#pnext) | 指向扩展结构的指针。 |
| VkImageView [inputRayOriginImage](xengine-kit-xeg-rtreflectiondescription.md#inputrayoriginimage) | 光线原点图像，不能为空。格式必须是至少3通道的float类型，RGB通道分别存储原点的xyz坐标。 |
| VkImageView [inputRayDirectionImage](xengine-kit-xeg-rtreflectiondescription.md#inputraydirectionimage) | 光线方向图像，不能为空。格式必须是至少3通道的float类型，RGB通道分别存储方向的xyz坐标。 如果格式为有符号的float类型，不做特殊处理，如果格式为无符号的float类型，方向信息需要按照以下方式量化：direction = (direction + 1.0) / 2.0 。 |
| VkImageView [outputReflectionInfoImage](xengine-kit-xeg-rtreflectiondescription.md#outputreflectioninfoimage) | 输出的反射光线求交结果，格式必须为R32G32B32A32\_UINT。求交结果会将光线追踪最近的命中信息打包成128bit，解析方式参考结构体成员变量说明中[outputReflectionInfoImage](xengine-kit-xeg-rtreflectiondescription.md#outputreflectioninfoimage)描述。 |
| VkAccelerationStructureKHR [accelerationStructure](xengine-kit-xeg-rtreflectiondescription.md#accelerationstructure) | 场景的光线追踪加速结构。 |
| float [rayMin](xengine-kit-xeg-rtreflectiondescription.md#raymin) | 光线起点到最近可能相交点之间的最小距离。必须为非负值，且小于等于rayMax。 |
| float [rayMax](xengine-kit-xeg-rtreflectiondescription.md#raymax) | 光线起点到最远可能相交点之间的最大距离。超出此范围的任何相交都将被忽略。 |
| uint32\_t [reflectionCullMask](xengine-kit-xeg-rtreflectiondescription.md#reflectioncullmask) | 配置光线查询[rayQueryInitializeEXT](https://github.com/KhronosGroup/GLSL/blob/main/extensions/ext/GLSL_EXT_ray_query.txt)函数中的rayFlags和cullMask参数。高24bit表示rayFlags，低8bit表示cullMask。 |

## 结构体成员变量说明

PhonePC/2in1TabletTV

### accelerationStructure

PhonePC/2in1TabletTV

```
1. VkAccelerationStructureKHR XEG_RTReflectionDescription::accelerationStructure
```

**描述**

场景的光线追踪加速结构。

### inputRayDirectionImage

PhonePC/2in1TabletTV

```
1. VkImageView XEG_RTReflectionDescription::inputRayDirectionImage
```

**描述**

光线方向图像，不能为空。格式必须是至少3通道的float类型，RGB通道分别存储方向的xyz坐标。 如果格式为有符号的float类型，不做特殊处理，如果格式为无符号的float类型，方向信息需要按照以下方式量化：direction = (direction + 1.0) / 2.0 。

### inputRayOriginImage

PhonePC/2in1TabletTV

```
1. VkImageView XEG_RTReflectionDescription::inputRayOriginImage
```

**描述**

光线原点图像，不能为空。格式必须是至少3通道的float类型，RGB通道分别存储原点的xyz坐标。

### outputReflectionInfoImage

PhonePC/2in1TabletTV

```
1. VkImageView XEG_RTReflectionDescription::outputReflectionInfoImage
```

**描述**

输出的反射光线求交结果，格式必须为R32G32B32A32\_UINT。求交结果会将光线追踪最近的命中信息打包成128bit，解析方式如下：

```
1. uint raymiss = outputReflectionInfoImage.x & 1;
2. uint primitiveId = (outputReflectionInfoImage.x >> 1) & (0x3ffff);
3. uint instanceId = outputReflectionInfoImage.x >> 19;
4. vec2 barycentrics = unpackHalf2x16(outputReflectionInfoImage.z);
5. float hitT = uintBitsToFloat(outputReflectionInfoImage.w);
6. uint sbtOffest = (outputReflectionInfoImage.y >> 16);
7. uint geomtryIndex = (outputReflectionInfoImage.y) & 0xffff;
```

### pNext

PhonePC/2in1TabletTV

```
1. const void* XEG_RTReflectionDescription::pNext
```

**描述**

指向扩展结构的指针。

### rayMax

PhonePC/2in1TabletTV

```
1. float XEG_RTReflectionDescription::rayMax
```

**描述**

光线起点到最远可能相交点之间的最大距离。超出此范围的任何相交都将被忽略。

### rayMin

PhonePC/2in1TabletTV

```
1. float XEG_RTReflectionDescription::rayMin
```

**描述**

光线起点到最近可能相交点之间的最小距离。必须为非负值，且小于等于rayMax。

### reflectionCullMask

PhonePC/2in1TabletTV

```
1. uint32_t XEG_RTReflectionDescription::reflectionCullMask
```

**描述**

配置光线查询[rayQueryInitializeEXT](https://github.com/KhronosGroup/GLSL/blob/main/extensions/ext/GLSL_EXT_ray_query.txt)函数中的rayFlags和cullMask参数。高24bit表示rayFlags，低8bit表示cullMask。

### sType

PhonePC/2in1TabletTV

```
1. XEG_StructureType XEG_RTReflectionDescription::sType
```

**描述**

识别此结构的[XEG\_StructureType](xengine-kit-xengine.md#xeg_structuretype)值，必须是XEG\_STRUCTURE\_TYPE\_RT\_REFLECTION\_DESCRIPTION。
