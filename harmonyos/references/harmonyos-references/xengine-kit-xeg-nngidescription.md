---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xeg-nngidescription
title: XEG_NNGIDescription
breadcrumb: API参考 > 图形 > XEngine Kit（GPU加速引擎服务） > C API > 头文件和结构体 > 结构体 > XEG_NNGIDescription
category: harmonyos-references
scraped_at: 2026-04-29T14:06:40+08:00
doc_updated_at: 2026-04-28
content_hash: sha256:2d8703b86ac0a3c6370546ee3aa91ab3b37d142075cfb044212ffb468e48d050
---

## 概述

PhonePC/2in1TabletTV

此结构体描述更新NNGI用于计算光线追踪全局光照的所需的信息。

**起始版本：** 6.0.0(20)

**相关模块：** [XEngine](xengine-kit-xengine.md)

**所在头文件：** [xeg\_vulkan\_rtgi.h](xengine-kit-xeg-vulkan-rtgi-8h.md)

## 汇总

PhonePC/2in1TabletTV

### 成员变量

PhonePC/2in1TabletTV

| 名称 | 描述 |
| --- | --- |
| XEG\_StructureType [sType](xengine-kit-xeg-nngidescription.md#stype) | 识别此结构的[XEG\_StructureType](xengine-kit-xengine.md#xeg_structuretype)值，必须是XEG\_STRUCTURE\_TYPE\_NNGI\_DESCRIPTION。 |
| const void \* [pNext](xengine-kit-xeg-nngidescription.md#pnext) | 指向扩展结构的指针。 |
| float [inferenceCameraViewMatrix](xengine-kit-xeg-nngidescription.md#inferencecameraviewmatrix) [16] | 推理图像的相机观察矩阵，与用户生成Gbuffer使用的矩阵保持一致，必须是4\*4列主序矩阵。 |
| float [inferenceCameraProjectionMatrix](xengine-kit-xeg-nngidescription.md#inferencecameraprojectionmatrix) [16] | 推理图像的相机投影矩阵，与用户生成Gbuffer使用的矩阵保持一致，必须是4\*4列主序矩阵。 |
| VkImageView [inferenceInputDepthImage](xengine-kit-xeg-nngidescription.md#inferenceinputdepthimage) | 推理输入深度图像，不能为空，格式必须支持深度模板附件，存储Gbuffer的depth纹理。其分辨率和[XEG\_NNGICreateInfo](xengine-kit-xeg-nngicreateinfo.md)中inferenceInputSize的分辨率保持一致。 |
| VkImageView [inferenceInputNormalImage](xengine-kit-xeg-nngidescription.md#inferenceinputnormalimage) | 推理输入法线向量图像，不能为空，格式必须是至少3通道数据，RGB通道分别存储法线的xyz分量。其分辨率和[XEG\_NNGICreateInfo](xengine-kit-xeg-nngicreateinfo.md)中inferenceInputSize的分辨率保持一致。 |
| VkImageView [inferenceInputBaseColorMetallicImage](xengine-kit-xeg-nngidescription.md#inferenceinputbasecolormetallicimage) | 推理输入基础颜色图像，不能为空，格式必须是至少3通道数据，RGB通道分别存储红绿蓝分量，忽略alpha通道信息。其分辨率和[XEG\_NNGICreateInfo](xengine-kit-xeg-nngicreateinfo.md)中inferenceInputSize的分辨率保持一致。 |
| VkImageView [inferenceOutputGIImage](xengine-kit-xeg-nngidescription.md#inferenceoutputgiimage) | 推理输出GI图像，格式必须是至少3通道数据，RGB通道分别存储红绿蓝分量的间接光照值，忽略alpha通道信息。其分辨率和[XEG\_NNGICreateInfo](xengine-kit-xeg-nngicreateinfo.md)中inferenceOutputSize的分辨率保持一致。 |
| float [trainingCameraViewMatrix](xengine-kit-xeg-nngidescription.md#trainingcameraviewmatrix) [16] | 训练图像的相机观察矩阵，该矩阵与用户生成PathTracing使用的矩阵保持一致，必须是4\*4列主序矩阵。 |
| float [trainingCameraProjectionMatrix](xengine-kit-xeg-nngidescription.md#trainingcameraprojectionmatrix) [16] | 训练图像的相机投影矩阵，该矩阵与用户生成PathTracing使用的矩阵保持一致，必须是4\*4列主序矩阵。 |
| VkImageView [trainingInputPositionImage](xengine-kit-xeg-nngidescription.md#traininginputpositionimage) | 训练输入位置图像，不能为空，格式必须是至少3通道数据，RGB通道分别存储每个像素的xyz轴坐标。其分辨率和[XEG\_NNGICreateInfo](xengine-kit-xeg-nngicreateinfo.md)中trainingSize的分辨率保持一致。 |
| VkImageView [trainingInputNormalImage](xengine-kit-xeg-nngidescription.md#traininginputnormalimage) | 训练输入法向量图像，不能为空，格式必须是至少3通道数据，RGB通道分别存储法线的xyz分量。其分辨率和[XEG\_NNGICreateInfo](xengine-kit-xeg-nngicreateinfo.md)中trainingSize的分辨率保持一致。 |
| VkImageView [trainingInputBaseColorMetallicImage](xengine-kit-xeg-nngidescription.md#traininginputbasecolormetallicimage) | 训练输入基础颜色图像，不能为空，格式必须是至少3通道数据，RGB通道分别存储红绿蓝分量，忽略alpha通道信息。其分辨率和[XEG\_NNGICreateInfo](xengine-kit-xeg-nngicreateinfo.md)中trainingSize的分辨率保持一致。 |
| VkImageView [trainingInputGIImage](xengine-kit-xeg-nngidescription.md#traininginputgiimage) | 训练输入GI图像，不能为空，格式必须是至少3通道数据，RGB通道分别存储红绿蓝分量的辐射度值，忽略alpha通道信息。该训练图像的GI结果的质量越高，推理输出的GI结果的质量就越高。其分辨率和[XEG\_NNGICreateInfo](xengine-kit-xeg-nngicreateinfo.md)中trainingSize的分辨率保持一致。 |
| VkAabbPositionsKHR [sceneAabb](xengine-kit-xeg-nngidescription.md#sceneaabb) | 渲染包围盒范围。 |
| bool [isSceneUnbounded](xengine-kit-xeg-nngidescription.md#issceneunbounded) = false | 渲染场景是否无界，true表示场景无边界，false表示场景有边界，当前只支持false。 |
| float [spatialScaleFactor](xengine-kit-xeg-nngidescription.md#spatialscalefactor) = 0 | 场景缩放因子，对于有界场景，无需设置，XEngine根据sceneAabb计算该值，对于无界场景，建议设置为平均深度。 |

## 结构体成员变量说明

PhonePC/2in1TabletTV

### inferenceCameraProjectionMatrix

PhonePC/2in1TabletTV

```
1. float XEG_NNGIDescription::inferenceCameraProjectionMatrix[16]
```

**描述**

推理图像的相机投影矩阵，与用户生成Gbuffer使用的矩阵保持一致，必须是4\*4列主序矩阵。

### inferenceCameraViewMatrix

PhonePC/2in1TabletTV

```
1. float XEG_NNGIDescription::inferenceCameraViewMatrix[16]
```

**描述**

推理图像的相机观察矩阵，与用户生成Gbuffer使用的矩阵保持一致，必须是4\*4列主序矩阵。

### inferenceInputBaseColorMetallicImage

PhonePC/2in1TabletTV

```
1. VkImageView XEG_NNGIDescription::inferenceInputBaseColorMetallicImage
```

**描述**

推理输入基础颜色图像，不能为空，格式必须是至少3通道数据，RGB通道分别存储红绿蓝分量，忽略alpha通道信息。其分辨率和[XEG\_NNGICreateInfo](xengine-kit-xeg-nngicreateinfo.md)中inferenceInputSize的分辨率保持一致。

### inferenceInputDepthImage

PhonePC/2in1TabletTV

```
1. VkImageView XEG_NNGIDescription::inferenceInputDepthImage
```

**描述**

推理输入深度图像，不能为空，格式必须支持深度模板附件，存储Gbuffer的depth纹理。其分辨率和[XEG\_NNGICreateInfo](xengine-kit-xeg-nngicreateinfo.md)中inferenceInputSize的分辨率保持一致。

### inferenceInputNormalImage

PhonePC/2in1TabletTV

```
1. VkImageView XEG_NNGIDescription::inferenceInputNormalImage
```

**描述**

推理输入法线向量图像，不能为空，格式必须是至少3通道数据，RGB通道分别存储法线的xyz分量。其分辨率和[XEG\_NNGICreateInfo](xengine-kit-xeg-nngicreateinfo.md)中inferenceInputSize的分辨率保持一致。

### inferenceOutputGIImage

PhonePC/2in1TabletTV

```
1. VkImageView XEG_NNGIDescription::inferenceOutputGIImage
```

**描述**

推理输出GI图像，格式必须是至少3通道数据，RGB通道分别存储红绿蓝分量的间接光照值，忽略alpha通道信息。其分辨率和[XEG\_NNGICreateInfo](xengine-kit-xeg-nngicreateinfo.md)中inferenceOutputSize的分辨率保持一致。

### isSceneUnbounded

PhonePC/2in1TabletTV

```
1. bool XEG_NNGIDescription::isSceneUnbounded = false
```

**描述**

渲染场景是否无界，当前只支持false。

### pNext

PhonePC/2in1TabletTV

```
1. const void* XEG_NNGIDescription::pNext
```

**描述**

指向扩展结构的指针。

### sceneAabb

PhonePC/2in1TabletTV

```
1. VkAabbPositionsKHR XEG_NNGIDescription::sceneAabb
```

**描述**

渲染包围盒范围。

### spatialScaleFactor

PhonePC/2in1TabletTV

```
1. float XEG_NNGIDescription::spatialScaleFactor = 0
```

**描述**

场景缩放因子，对于有界场景，无需设置，XEngine根据sceneAabb计算该值，对于无界场景，建议设置为平均深度。

### sType

PhonePC/2in1TabletTV

```
1. XEG_StructureType XEG_NNGIDescription::sType
```

**描述**

识别此结构的[XEG\_StructureType](xengine-kit-xengine.md#xeg_structuretype)值，必须是XEG\_STRUCTURE\_TYPE\_NNGI\_DESCRIPTION。

### trainingCameraProjectionMatrix

PhonePC/2in1TabletTV

```
1. float XEG_NNGIDescription::trainingCameraProjectionMatrix[16]
```

**描述**

训练图像的相机投影矩阵，该矩阵与用户生成PathTracing使用的矩阵保持一致，必须是4\*4列主序矩阵。

### trainingCameraViewMatrix

PhonePC/2in1TabletTV

```
1. float XEG_NNGIDescription::trainingCameraViewMatrix[16]
```

**描述**

训练图像的相机观察矩阵，该矩阵与用户生成PathTracing使用的矩阵保持一致，必须是4\*4列主序矩阵。

### trainingInputBaseColorMetallicImage

PhonePC/2in1TabletTV

```
1. VkImageView XEG_NNGIDescription::trainingInputBaseColorMetallicImage
```

**描述**

训练输入基础颜色图像，不能为空，格式必须是至少3通道数据，RGB通道分别存储红绿蓝分量，忽略alpha通道信息。其分辨率和[XEG\_NNGICreateInfo](xengine-kit-xeg-nngicreateinfo.md)中trainingSize的分辨率保持一致。

### trainingInputGIImage

PhonePC/2in1TabletTV

```
1. VkImageView XEG_NNGIDescription::trainingInputGIImage
```

**描述**

训练输入GI图像，不能为空，格式必须是至少3通道数据，RGB通道分别存储红绿蓝分量的辐射度值，忽略alpha通道信息。该训练图像的GI结果的质量越高，推理输出的GI结果的质量就越高。其分辨率和[XEG\_NNGICreateInfo](xengine-kit-xeg-nngicreateinfo.md)中trainingSize的分辨率保持一致。

### trainingInputNormalImage

PhonePC/2in1TabletTV

```
1. VkImageView XEG_NNGIDescription::trainingInputNormalImage
```

**描述**

训练输入法向量图像，不能为空，格式必须是至少3通道数据，RGB通道分别存储法线的xyz分量。其分辨率和[XEG\_NNGICreateInfo](xengine-kit-xeg-nngicreateinfo.md)中trainingSize的分辨率保持一致。

### trainingInputPositionImage

PhonePC/2in1TabletTV

```
1. VkImageView XEG_NNGIDescription::trainingInputPositionImage
```

**描述**

训练输入位置图像，不能为空，格式必须是至少3通道数据，RGB通道分别存储每个像素的xyz轴坐标。其分辨率和[XEG\_NNGICreateInfo](xengine-kit-xeg-nngicreateinfo.md)中trainingSize的分辨率保持一致。
