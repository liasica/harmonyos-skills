---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xeg-rtshadowaodescription
title: XEG_RTShadowAODescription
breadcrumb: API参考 > 图形 > XEngine Kit（GPU加速引擎服务） > C API > 头文件和结构体 > 结构体 > XEG_RTShadowAODescription
category: harmonyos-references
scraped_at: 2026-04-28T08:16:03+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:12cfa8a4b044541710f7de428f9eac35b642fcfe79a21168a5089e49456b0b71
---

## 概述

PhonePC/2in1TabletTV

此结构体描述光线追踪阴影和环境光遮蔽算法渲染命令的输入信息。

**起始版本：** 6.0.0(20)

**相关模块：** [XEngine](xengine-kit-xengine.md)

**所在头文件：** [xeg\_vulkan\_rt\_visible\_mask.h](xengine-kit-xeg-vulkan-rt-visible-mask-8h.md)

## 汇总

PhonePC/2in1TabletTV

### 成员变量

PhonePC/2in1TabletTV

| 名称 | 描述 |
| --- | --- |
| XEG\_StructureType [sType](xengine-kit-xeg-rtshadowaodescription.md#stype) | 识别此结构的[XEG\_StructureType](xengine-kit-xengine.md#xeg_structuretype)值，必须是XEG\_STRUCTURE\_TYPE\_RT\_SHADOWAO\_DESCRIPTION。 |
| const void \* [pNext](xengine-kit-xeg-rtshadowaodescription.md#pnext) | 指向扩展结构的指针。 |
| VkImageView [inputDepthImage](xengine-kit-xeg-rtshadowaodescription.md#inputdepthimage) | 深度图像，不能为空。 |
| VkImageView [inputNormalImage](xengine-kit-xeg-rtshadowaodescription.md#inputnormalimage) | 法线图像，不能为空。需要是无符号浮点格式并包含3个以上通道，如VK\_FORMAT\_R8G8B8\_UNORM。XEngine将按照Normal=textureLod(inputNormalImage).xyz\*2.0–1.0的方式解析法线。 |
| VkImageView [inputMotionVectorImage](xengine-kit-xeg-rtshadowaodescription.md#inputmotionvectorimage) | 运动矢量图像，可以为空。运动矢量的计算方式为当前渲染像素的NDC坐标的XY值减去其上一帧的NDC坐标的XY值。图像格式需要是VK\_FORMAT\_R16G16\_SFLOAT或更高精度。保留字段，暂不支持。 |
| VkImageView [outputShadowAOImage](xengine-kit-xeg-rtshadowaodescription.md#outputshadowaoimage) | 输出的阴影和环境光遮蔽图像，不能为空，格式必须为VK\_FORMAT\_R8G8\_UNORM。阴影值将写入R通道，环境光遮蔽值将写入G通道。 |
| VkAccelerationStructureKHR [accelerationStructure](xengine-kit-xeg-rtshadowaodescription.md#accelerationstructure) | 场景的光线追踪加速结构。 |
| bool [isAsInTranslatedSpace](xengine-kit-xeg-rtshadowaodescription.md#isasintranslatedspace) | 光线追踪加速结构是否在Translated世界空间构建。true表示在Translated世界空间构建，false表示在绝对世界空间构建。默认值为false。 |
| float [translatedViewMatrix](xengine-kit-xeg-rtshadowaodescription.md#translatedviewmatrix) | 相机Translated观察矩阵，必须是4\*4列主序矩阵。当isAsInTranslatedSpace值为false时可以不赋值。 |
| float [viewMatrix](xengine-kit-xeg-rtshadowaodescription.md#viewmatrix) [16] | 相机观察矩阵，必须是4\*4列主序矩阵。 |
| float [projectionMatrix](xengine-kit-xeg-rtshadowaodescription.md#projectionmatrix) [16] | 相机投影矩阵，必须是4\*4列主序矩阵。 |
| float [worldCameraOrigin](xengine-kit-xeg-rtshadowaodescription.md#worldcameraorigin) [3] | 相机在世界空间中的位置坐标。 |
| bool [ndcFilpY](xengine-kit-xeg-rtshadowaodescription.md#ndcfilpy) | 标识NDC空间与世界空间是否存在Y轴翻转关系。true表示翻转，false表示不翻转。默认值为false。 |
| const [XEG\_RTShadowParameters](xengine-kit-xeg-rtshadowparameters.md) \* [pRtShadowParameters](xengine-kit-xeg-rtshadowaodescription.md#prtshadowparameters) | 光线追踪阴影算法参数，当XEG\_RTShadowAOCreateInfo::enableRTShadow=true时不能为空。 |
| const [XEG\_RTAOParameters](xengine-kit-xeg-rtaoparameters.md) \* [pRtAOParameters](xengine-kit-xeg-rtshadowaodescription.md#prtaoparameters) | 光线追踪环境光算法参数，当XEG\_RTShadowAOCreateInfo::enableRTAO=true时不能为空。 |
| const [XEG\_RTShadowAODenoiserParameters](xengine-kit-xeg-rtshadowaodenoiserparameters.md) \* [pRtShadowAODenoiserParameters](xengine-kit-xeg-rtshadowaodescription.md#prtshadowaodenoiserparameters) | 去噪参数，不能为空。光线追踪阴影和环境光遮蔽使用相同的去噪参数。 |

## 结构体成员变量说明

PhonePC/2in1TabletTV

### accelerationStructure

PhonePC/2in1TabletTV

```
1. VkAccelerationStructureKHR XEG_RTShadowAODescription::accelerationStructure
```

**描述**

场景的光线追踪加速结构。

### inputDepthImage

PhonePC/2in1TabletTV

```
1. VkImageView XEG_RTShadowAODescription::inputDepthImage
```

**描述**

深度图像，不能为空。

### inputMotionVectorImage

PhonePC/2in1TabletTV

```
1. VkImageView XEG_RTShadowAODescription::inputMotionVectorImage
```

**描述**

运动矢量图像，可以为空。运动矢量的计算方式为当前渲染像素的NDC坐标的XY值减去其上一帧的NDC坐标的XY值。图像格式需要是VK\_FORMAT\_R16G16\_SFLOAT或更高精度。保留字段，暂不支持。

### inputNormalImage

PhonePC/2in1TabletTV

```
1. VkImageView XEG_RTShadowAODescription::inputNormalImage
```

**描述**

法线图像，不能为空。需要是无符号浮点格式并包含3个以上通道，如VK\_FORMAT\_R8G8B8\_UNORM。XEngine将按照Normal=textureLod(inputNormalImage).xyz\*2.0–1.0的方式解析法线。

### outputShadowAOImage

PhonePC/2in1TabletTV

```
1. VkImageView XEG_RTShadowAODescription::outputShadowAOImage
```

**描述**

输出的阴影和环境光遮蔽图像，不能为空，格式必须为VK\_FORMAT\_R8G8\_UNORM。阴影值将写入R通道，环境光遮蔽值将写入G通道。

### pNext

PhonePC/2in1TabletTV

```
1. const void* XEG_RTShadowAODescription::pNext
```

**描述**

指向扩展结构的指针。

### projectionMatrix

PhonePC/2in1TabletTV

```
1. float XEG_RTShadowAODescription::projectionMatrix[16]
```

**描述**

相机投影矩阵，必须是4\*4列主序矩阵。

### pRtAOParameters

PhonePC/2in1TabletTV

```
1. const XEG_RTAOParameters* XEG_RTShadowAODescription::pRtAOParameters
```

**描述**

光线追踪环境光算法参数，当XEG\_RTShadowAOCreateInfo::enableRTAO=true时不能为空。

### pRtShadowAODenoiserParameters

PhonePC/2in1TabletTV

```
1. const XEG_RTShadowAODenoiserParameters* XEG_RTShadowAODescription::pRtShadowAODenoiserParameters
```

**描述**

去噪参数，不能为空。光线追踪阴影和环境光遮蔽使用相同的去噪参数。

### pRtShadowParameters

PhonePC/2in1TabletTV

```
1. const XEG_RTShadowParameters* XEG_RTShadowAODescription::pRtShadowParameters
```

**描述**

光线追踪阴影算法参数，当XEG\_RTShadowAOCreateInfo::enableRTShadow=true时不能为空。

### sType

PhonePC/2in1TabletTV

```
1. XEG_StructureType XEG_RTShadowAODescription::sType
```

**描述**

识别此结构的[XEG\_StructureType](xengine-kit-xengine.md#xeg_structuretype)值，必须是XEG\_STRUCTURE\_TYPE\_RT\_SHADOWAO\_DESCRIPTION。

### viewMatrix

PhonePC/2in1TabletTV

```
1. float XEG_RTShadowAODescription::viewMatrix[16]
```

**描述**

相机观察矩阵，必须是4\*4列主序矩阵。

### worldCameraOrigin

PhonePC/2in1TabletTV

```
1. float XEG_RTShadowAODescription::worldCameraOrigin[3]
```

**描述**

相机在世界空间中的位置坐标。

### isAsInTranslatedSpace

PhonePC/2in1TabletTV

```
1. bool XEG_RTShadowAODescription::isAsInTranslatedSpace = false;
```

**描述**

光线追踪加速结构是否在Translated世界空间构建。true表示在Translated世界空间构建，false表示在绝对世界空间构建。默认值为false。

### translatedViewMatrix

PhonePC/2in1TabletTV

```
1. float XEG_RTShadowAODescription::translatedViewMatrix[16];
```

**描述**

相机Translated观察矩阵，必须是4\*4列主序矩阵。当isAsInTranslatedSpace值为false时可以不赋值。

### ndcFilpY

PhonePC/2in1TabletTV

```
1. bool XEG_RTShadowAODescription::ndcFilpY  = false;
```

**描述**

标识NDC空间与世界空间是否存在Y轴翻转关系。true表示翻转，false表示不翻转。默认值为false。
