---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-processing-h
title: image_processing.h
breadcrumb: API参考 > 媒体 > Image Kit（图片处理服务） > C API > 头文件 > image_processing.h
category: harmonyos-references
scraped_at: 2026-04-28T08:13:23+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:281f9bfce1cb94ad22267d8a6b7c217b7496942de946376748c068c10e9ad01c
---

## 概述

PhonePC/2in1TabletTV

声明图片处理函数。提供图片处理能力，包括色彩空间转换，元数据生成及图片缩放。

**引用文件：** <multimedia/video\_processing\_engine/image\_processing.h>

**库：** libimage\_processing.so

**系统能力：** SystemCapability.Multimedia.VideoProcessingEngine

**起始版本：** 13

**相关模块：** [ImageProcessing](capi-imageprocessing.md)

## 汇总

PhonePC/2in1TabletTV

### 函数

PhonePC/2in1TabletTV

| 名称 | 描述 |
| --- | --- |
| [ImageProcessing\_ErrorCode OH\_ImageProcessing\_InitializeEnvironment(void)](capi-image-processing-h.md#oh_imageprocessing_initializeenvironment) | 初始化图片处理模块的全局环境。  此函数为非必需函数。通常此函数在主进程启动时被调用，用于图片处理模块的全局环境初始化并可以减少[OH\_ImageProcessing\_Create](capi-image-processing-h.md#oh_imageprocessing_create)的耗时。调用[OH\_ImageProcessing\_DeinitializeEnvironment](capi-image-processing-h.md#oh_imageprocessing_deinitializeenvironment)进行全局环境反初始化。可用于检查设备GPU是否正常工作。 |
| [ImageProcessing\_ErrorCode OH\_ImageProcessing\_DeinitializeEnvironment(void)](capi-image-processing-h.md#oh_imageprocessing_deinitializeenvironment) | 反初始化图片处理模块的全局环境。  如果[OH\_ImageProcessing\_InitializeEnvironment](capi-image-processing-h.md#oh_imageprocessing_initializeenvironment)被调用，则此函数为必需函数。通常此函数在主进程准备退出时被调用，用于反初始化图片处理模块的全局环境（由[OH\_ImageProcessing\_InitializeEnvironment](capi-image-processing-h.md#oh_imageprocessing_initializeenvironment)接口初始化）。如果此时存在图片处理实例，则不应调用此函数。如果[OH\_ImageProcessing\_InitializeEnvironment](capi-image-processing-h.md#oh_imageprocessing_initializeenvironment)未被调用，则不应调用此函数。 |
| [bool OH\_ImageProcessing\_IsColorSpaceConversionSupported(const ImageProcessing\_ColorSpaceInfo\* sourceImageInfo, const ImageProcessing\_ColorSpaceInfo\* destinationImageInfo)](capi-image-processing-h.md#oh_imageprocessing_iscolorspaceconversionsupported) | 查询是否支持当前图片色彩空间转换能力。 |
| [bool OH\_ImageProcessing\_IsCompositionSupported(const ImageProcessing\_ColorSpaceInfo\* sourceImageInfo, const ImageProcessing\_ColorSpaceInfo\* sourceGainmapInfo,const ImageProcessing\_ColorSpaceInfo\* destinationImageInfo)](capi-image-processing-h.md#oh_imageprocessing_iscompositionsupported) | 查询是否支持HDR双层图片转换为HDR单层图片。 |
| [bool OH\_ImageProcessing\_IsDecompositionSupported(const ImageProcessing\_ColorSpaceInfo\* sourceImageInfo, const ImageProcessing\_ColorSpaceInfo\* destinationImageInfo, const ImageProcessing\_ColorSpaceInfo\* destinationGainmapInfo)](capi-image-processing-h.md#oh_imageprocessing_isdecompositionsupported) | 查询是否支持HDR单层图片转换为HDR双层图片。 |
| [bool OH\_ImageProcessing\_IsMetadataGenerationSupported(const ImageProcessing\_ColorSpaceInfo\* sourceImageInfo)](capi-image-processing-h.md#oh_imageprocessing_ismetadatagenerationsupported) | 查询是否支持图片元数据生成能力。 |
| [ImageProcessing\_ErrorCode OH\_ImageProcessing\_Create(OH\_ImageProcessing\*\* imageProcessor, int32\_t type)](capi-image-processing-h.md#oh_imageprocessing_create) | 创建一个图片处理模块实例。 |
| [ImageProcessing\_ErrorCode OH\_ImageProcessing\_Destroy(OH\_ImageProcessing\* imageProcessor)](capi-image-processing-h.md#oh_imageprocessing_destroy) | 销毁当前图片处理模块实例。 |
| [ImageProcessing\_ErrorCode OH\_ImageProcessing\_SetParameter(OH\_ImageProcessing\* imageProcessor, const OH\_AVFormat\* parameter)](capi-image-processing-h.md#oh_imageprocessing_setparameter) | 设置图片处理模块参数。通过特定参数键添加参数。 |
| [ImageProcessing\_ErrorCode OH\_ImageProcessing\_GetParameter(OH\_ImageProcessing\* imageProcessor, OH\_AVFormat\* parameter)](capi-image-processing-h.md#oh_imageprocessing_getparameter) | 获取图片处理模块参数。通过特定参数键获取参数。 |
| [ImageProcessing\_ErrorCode OH\_ImageProcessing\_ConvertColorSpace(OH\_ImageProcessing\* imageProcessor, OH\_PixelmapNative\* sourceImage, OH\_PixelmapNative\* destinationImage)](capi-image-processing-h.md#oh_imageprocessing_convertcolorspace) | 实现单层图片间转换。此函数包括HDR图片到SDR图片的色彩空间转换，SDR图片到HDR图片的色彩空间转换，SDR图片到SDR图片的色彩空间转换和HDR图片的色彩空间转换。 |
| [ImageProcessing\_ErrorCode OH\_ImageProcessing\_Compose(OH\_ImageProcessing\* imageProcessor, OH\_PixelmapNative\* sourceImage, OH\_PixelmapNative\* sourceGainmap, OH\_PixelmapNative\* destinationImage)](capi-image-processing-h.md#oh_imageprocessing_compose) | 实现HDR双层图片到HDR单层图片的转换。此函数通过输入图片与输入Gainmap生成输出图片。 |
| [ImageProcessing\_ErrorCode OH\_ImageProcessing\_Decompose(OH\_ImageProcessing\* imageProcessor, OH\_PixelmapNative\* sourceImage, OH\_PixelmapNative\* destinationImage, OH\_PixelmapNative\* destinationGainmap)](capi-image-processing-h.md#oh_imageprocessing_decompose) | 实现HDR单层图片到HDR双层图片的转换。此函数通过输入图片生成输出图片和输出Gainmap。 |
| [ImageProcessing\_ErrorCode OH\_ImageProcessing\_GenerateMetadata(OH\_ImageProcessing\* imageProcessor, OH\_PixelmapNative\* sourceImage)](capi-image-processing-h.md#oh_imageprocessing_generatemetadata) | 生成HDR图片元数据。此函数为HDR图片生成元数据。 |
| [ImageProcessing\_ErrorCode OH\_ImageProcessing\_EnhanceDetail(OH\_ImageProcessing\* imageProcessor, OH\_PixelmapNative\* sourceImage, OH\_PixelmapNative\* destinationImage)](capi-image-processing-h.md#oh_imageprocessing_enhancedetail) | 进行图片清晰度/细节增强。此函数根据输入图片和输出图片预设的尺寸，对源图片进行必要的缩放操作生成目标图片，并提供了多种缩放方法以平衡性能和图像质量。 |

## 函数说明

PhonePC/2in1TabletTV

### OH\_ImageProcessing\_InitializeEnvironment()

PhonePC/2in1TabletTV

```
1. ImageProcessing_ErrorCode OH_ImageProcessing_InitializeEnvironment(void)
```

**描述**

初始化图片处理模块的全局环境。

此函数为非必需函数。通常此函数在主进程启动时被调用，用于图片处理模块的全局环境初始化并可以减少[OH\_ImageProcessing\_Create](capi-image-processing-h.md#oh_imageprocessing_create)的耗时。调用[OH\_ImageProcessing\_DeinitializeEnvironment](capi-image-processing-h.md#oh_imageprocessing_deinitializeenvironment)进行全局环境反初始化。可用于检查设备GPU是否正常工作。

**起始版本：** 13

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ImageProcessing\_ErrorCode](capi-image-processing-types-h.md#imageprocessing_errorcode) | 如果初始化成功，则返回IMAGE\_PROCESSING\_SUCCESS，否则返回IMAGE\_PROCESSING\_ERROR\_INITIALIZE\_FAILED。 |

### OH\_ImageProcessing\_DeinitializeEnvironment()

PhonePC/2in1TabletTV

```
1. ImageProcessing_ErrorCode OH_ImageProcessing_DeinitializeEnvironment(void)
```

**描述**

反初始化图片处理模块的全局环境。

如果[OH\_ImageProcessing\_InitializeEnvironment](capi-image-processing-h.md#oh_imageprocessing_initializeenvironment)被调用，则此函数为必需函数。通常此函数在主进程准备退出时被调用，用于反初始化图片处理模块的全局环境（由[OH\_ImageProcessing\_InitializeEnvironment](capi-image-processing-h.md#oh_imageprocessing_initializeenvironment)接口初始化）。如果此时存在图片处理实例，则不应调用此函数。如果[OH\_ImageProcessing\_InitializeEnvironment](capi-image-processing-h.md#oh_imageprocessing_initializeenvironment)未被调用，则不应调用此函数。

**起始版本：** 13

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ImageProcessing\_ErrorCode](capi-image-processing-types-h.md#imageprocessing_errorcode) | 如果反初始化成功，则返回IMAGE\_PROCESSING\_SUCCESS。  如果存在图片处理实例未被销毁或[OH\_ImageProcessing\_InitializeEnvironment](capi-image-processing-h.md#oh_imageprocessing_initializeenvironment)接口未被调用，则返回IMAGE\_PROCESSING\_ERROR\_OPERATION\_NOT\_PERMITTED。 |

### OH\_ImageProcessing\_IsColorSpaceConversionSupported()

PhonePC/2in1TabletTV

```
1. bool OH_ImageProcessing_IsColorSpaceConversionSupported(const ImageProcessing_ColorSpaceInfo* sourceImageInfo,const ImageProcessing_ColorSpaceInfo* destinationImageInfo)
```

**描述**

查询是否支持当前图片色彩空间转换能力。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [ImageProcessing\_ColorSpaceInfo](api-imageprocessing-imageprocessing-colorspaceinfo.md)\* sourceImageInfo | 指向输入图片色彩空间信息的指针。 |
| const [ImageProcessing\_ColorSpaceInfo](api-imageprocessing-imageprocessing-colorspaceinfo.md)\* destinationImageInfo | 指向输出图片色彩空间信息的指针， |

**返回：**

| 类型 | 说明 |
| --- | --- |
| bool | 如果支持当前色彩空间转换，返回true。  如果不支持当前色彩空间转换，返回false。 |

### OH\_ImageProcessing\_IsCompositionSupported()

PhonePC/2in1TabletTV

```
1. bool OH_ImageProcessing_IsCompositionSupported(const ImageProcessing_ColorSpaceInfo* sourceImageInfo,const ImageProcessing_ColorSpaceInfo* sourceGainmapInfo,const ImageProcessing_ColorSpaceInfo* destinationImageInfo)
```

**描述**

查询是否支持HDR双层图片转换为HDR单层图片。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [ImageProcessing\_ColorSpaceInfo](api-imageprocessing-imageprocessing-colorspaceinfo.md)\* sourceImageInfo | 指向输入图片色彩空间信息的指针。 |
| const [ImageProcessing\_ColorSpaceInfo](api-imageprocessing-imageprocessing-colorspaceinfo.md)\* sourceGainmapInfo | 指向输入Gainmap色彩空间信息的指针。 |
| const [ImageProcessing\_ColorSpaceInfo](api-imageprocessing-imageprocessing-colorspaceinfo.md)\* destinationImageInfo | 指向输出图片色彩空间信息的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| bool | 如果支持HDR双层图片转换HDR单层图片能力，返回true。  如果不支持此能力，返回false。 |

### OH\_ImageProcessing\_IsDecompositionSupported()

PhonePC/2in1TabletTV

```
1. bool OH_ImageProcessing_IsDecompositionSupported(const ImageProcessing_ColorSpaceInfo* sourceImageInfo,const ImageProcessing_ColorSpaceInfo* destinationImageInfo,const ImageProcessing_ColorSpaceInfo* destinationGainmapInfo)
```

**描述**

查询是否支持HDR单层图片转换为HDR双层图片。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [ImageProcessing\_ColorSpaceInfo](api-imageprocessing-imageprocessing-colorspaceinfo.md)\* sourceImageInfo | 指向输入图片色彩空间信息的指针。 |
| const [ImageProcessing\_ColorSpaceInfo](api-imageprocessing-imageprocessing-colorspaceinfo.md)\* destinationImageInfo | 指向输出图片色彩空间信息的指针。 |
| const [ImageProcessing\_ColorSpaceInfo](api-imageprocessing-imageprocessing-colorspaceinfo.md)\* destinationGainmapInfo | 指向输出Gainmap色彩空间信息的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| bool | 如果支持HDR单层图片转换为HDR双层图片能力，返回true。  如果不支持此能力，返回false。 |

### OH\_ImageProcessing\_IsMetadataGenerationSupported()

PhonePC/2in1TabletTV

```
1. bool OH_ImageProcessing_IsMetadataGenerationSupported(const ImageProcessing_ColorSpaceInfo* sourceImageInfo)
```

**描述**

查询是否支持图片元数据生成能力。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [ImageProcessing\_ColorSpaceInfo](api-imageprocessing-imageprocessing-colorspaceinfo.md)\* sourceImageInfo | 指向输入图片色彩空间信息的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| bool | 如果支持图片元数据生成能力，返回true。  如果不支持此能力，返回false。 |

### OH\_ImageProcessing\_Create()

PhonePC/2in1TabletTV

```
1. ImageProcessing_ErrorCode OH_ImageProcessing_Create(OH_ImageProcessing** imageProcessor, int32_t type)
```

**描述**

创建一个图片处理模块实例。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ImageProcessing](capi-imageprocessing-oh-imageprocessing.md)\*\* imageProcessor | 输出参数。指针\*imageProcessor指向一个新的图片处理对象。指针\*imageProcessor在传递前必须是一个空指针。 |
| int32\_t type | 使用IMAGE\_PROCESSING\_TYPE\_XXX来指定图片处理类型。此实例的类型在创建后不能更改。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ImageProcessing\_ErrorCode](capi-image-processing-types-h.md#imageprocessing_errorcode) | 如果创建成功，则返回IMAGE\_PROCESSING\_SUCCESS。  当指定的图片处理类型不支持时，返回IMAGE\_PROCESSING\_ERROR\_UNSUPPORTED\_PROCESSING，例如如果不支持图片元数据生成能力，则返回不支持该处理类型。  当创建失败时，返回IMAGE\_PROCESSING\_ERROR\_CREATE\_FAILED。  当该实例为空或指向该实例的指针为空时，返回IMAGE\_PROCESSING\_ERROR\_INVALID\_INSTANCE。  当指定的图片处理类型无效时，返回IMAGE\_PROCESSING\_ERROR\_INVALID\_PARAMETER。 |

### OH\_ImageProcessing\_Destroy()

PhonePC/2in1TabletTV

```
1. ImageProcessing_ErrorCode OH_ImageProcessing_Destroy(OH_ImageProcessing* imageProcessor)
```

**描述**

销毁当前图片处理模块实例。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ImageProcessing](capi-imageprocessing-oh-imageprocessing.md)\* imageProcessor | 指向图片处理模块实例的指针。当实例被销毁时，建议该指针设置为空。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ImageProcessing\_ErrorCode](capi-image-processing-types-h.md#imageprocessing_errorcode) | 如果销毁成功，则返回IMAGE\_PROCESSING\_SUCCESS。  当该实例为空或该实例不是图片处理模块实例时，返回IMAGE\_PROCESSING\_ERROR\_INVALID\_INSTANCE。 |

### OH\_ImageProcessing\_SetParameter()

PhonePC/2in1TabletTV

```
1. ImageProcessing_ErrorCode OH_ImageProcessing_SetParameter(OH_ImageProcessing* imageProcessor,const OH_AVFormat* parameter)
```

**描述**

设置图片处理模块参数。通过特定参数键添加参数。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ImageProcessing](capi-imageprocessing-oh-imageprocessing.md)\* imageProcessor | 指向图片处理模块实例的指针。 |
| const [OH\_AVFormat](capi-core-oh-avformat.md)\* parameter | 图片处理参数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ImageProcessing\_ErrorCode](capi-image-processing-types-h.md#imageprocessing_errorcode) | 如果设置参数成功，则返回IMAGE\_PROCESSING\_SUCCESS。  当该实例为空或该实例不是图片处理模块实例时，返回IMAGE\_PROCESSING\_ERROR\_INVALID\_INSTANCE。  当参数为空时，返回IMAGE\_PROCESSING\_ERROR\_INVALID\_PARAMETER。  当部分参数无效时，返回IMAGE\_PROCESSING\_ERROR\_INVALID\_VALUE，例如参数包含不支持的参数键或值。  当内存分配失败时，返回IMAGE\_PROCESSING\_ERROR\_NO\_MEMORY。 |

### OH\_ImageProcessing\_GetParameter()

PhonePC/2in1TabletTV

```
1. ImageProcessing_ErrorCode OH_ImageProcessing_GetParameter(OH_ImageProcessing* imageProcessor,OH_AVFormat* parameter)
```

**描述**

获取图片处理模块参数。通过特定参数键获取参数。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ImageProcessing](capi-imageprocessing-oh-imageprocessing.md)\* imageProcessor | 指向图片处理模块实例的指针。 |
| [OH\_AVFormat](capi-core-oh-avformat.md)\* parameter | 该图片处理模块实例使用的参数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ImageProcessing\_ErrorCode](capi-image-processing-types-h.md#imageprocessing_errorcode) | 如果获取参数成功，则返回IMAGE\_PROCESSING\_SUCCESS。  当该实例为空或该实例不是图片处理模块实例时，返回IMAGE\_PROCESSING\_ERROR\_INVALID\_INSTANCE。  当参数为空时，返回IMAGE\_PROCESSING\_ERROR\_INVALID\_PARAMETER。 |

### OH\_ImageProcessing\_ConvertColorSpace()

PhonePC/2in1TabletTV

```
1. ImageProcessing_ErrorCode OH_ImageProcessing_ConvertColorSpace(OH_ImageProcessing* imageProcessor,OH_PixelmapNative* sourceImage, OH_PixelmapNative* destinationImage)
```

**描述**

实现单层图片间转换。此函数包括HDR图片到SDR图片的色彩空间转换，SDR图片到HDR图片的色彩空间转换，SDR图片到SDR图片的色彩空间转换和HDR图片的色彩空间转换。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ImageProcessing](capi-imageprocessing-oh-imageprocessing.md)\* imageProcessor | 指向图片处理模块实例的指针。该实例应该由IMAGE\_PROCESSING\_TYPE\_COLOR\_SPACE\_CONVERSION类型创建。 |
| [OH\_PixelmapNative](capi-image-nativemodule-oh-pixelmapnative.md)\* sourceImage | 指向输入图片的指针，指向的OH\_PixelmapNative需为DMA内存，具体情况请参考[PixelMap的内存类型介绍](../harmonyos-guides/image-allocator-type.md#内存类型介绍)。 |
| [OH\_PixelmapNative](capi-image-nativemodule-oh-pixelmapnative.md)\* destinationImage | 指向输出图片的指针，指向的OH\_PixelmapNative需为DMA内存，具体情况请参考[PixelMap的内存类型介绍](../harmonyos-guides/image-allocator-type.md#内存类型介绍)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ImageProcessing\_ErrorCode](capi-image-processing-types-h.md#imageprocessing_errorcode) | 如果图片处理成功，则返回IMAGE\_PROCESSING\_SUCCESS。  当该实例为空或该实例不是图片处理模块实例时，返回IMAGE\_PROCESSING\_ERROR\_INVALID\_INSTANCE。  当图片为空时，返回IMAGE\_PROCESSING\_ERROR\_INVALID\_PARAMETER。  当图片的某些属性无效时，返回IMAGE\_PROCESSING\_ERROR\_INVALID\_VALUE，例如图片的色彩空间是不支持的。  当该图片处理不支持时，返回IMAGE\_PROCESSING\_ERROR\_UNSUPPORTED\_PROCESSING。  当该图片处理中返回错误时，返回IMAGE\_PROCESSING\_ERROR\_PROCESS\_FAILED。  当内存分配失败时，返回IMAGE\_PROCESSING\_ERROR\_NO\_MEMORY。 |

### OH\_ImageProcessing\_Compose()

PhonePC/2in1TabletTV

```
1. ImageProcessing_ErrorCode OH_ImageProcessing_Compose(OH_ImageProcessing* imageProcessor,OH_PixelmapNative* sourceImage, OH_PixelmapNative* sourceGainmap, OH_PixelmapNative* destinationImage)
```

**描述**

实现HDR双层图片到HDR单层图片的转换。此函数通过输入图片与输入Gainmap生成输出图片。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ImageProcessing](capi-imageprocessing-oh-imageprocessing.md)\* imageProcessor | 指向图片处理模块实例的指针。该实例应该由IMAGE\_PROCESSING\_TYPE\_COMPOSITION类型创建。 |
| [OH\_PixelmapNative](capi-image-nativemodule-oh-pixelmapnative.md)\* sourceImage | 指向输入图片的指针，指向的OH\_PixelmapNative需为DMA内存，具体情况请参考[PixelMap的内存类型介绍](../harmonyos-guides/image-allocator-type.md#内存类型介绍)。 |
| [OH\_PixelmapNative](capi-image-nativemodule-oh-pixelmapnative.md)\* sourceGainmap | 指向输入Gainmap的指针，指向的OH\_PixelmapNative需为DMA内存，具体情况请参考[PixelMap的内存类型介绍](../harmonyos-guides/image-allocator-type.md#内存类型介绍)。 |
| [OH\_PixelmapNative](capi-image-nativemodule-oh-pixelmapnative.md)\* destinationImage | 指向输出图片的指针，指向的OH\_PixelmapNative需为DMA内存，具体情况请参考[PixelMap的内存类型介绍](../harmonyos-guides/image-allocator-type.md#内存类型介绍)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ImageProcessing\_ErrorCode](capi-image-processing-types-h.md#imageprocessing_errorcode) | 如果图片处理成功，则返回IMAGE\_PROCESSING\_SUCCESS。  当该实例为空或该实例不是图片处理模块实例时，返回IMAGE\_PROCESSING\_ERROR\_INVALID\_INSTANCE。  当图片为空时，返回IMAGE\_PROCESSING\_ERROR\_INVALID\_PARAMETER。  当图片的某些属性无效时，返回IMAGE\_PROCESSING\_ERROR\_INVALID\_VALUE，例如图片的色彩空间是不支持的。  当该图片处理不支持时，返回IMAGE\_PROCESSING\_ERROR\_UNSUPPORTED\_PROCESSING。  当该图片处理中返回错误时，返回IMAGE\_PROCESSING\_ERROR\_PROCESS\_FAILED。  当内存分配失败时，返回IMAGE\_PROCESSING\_ERROR\_NO\_MEMORY。 |

### OH\_ImageProcessing\_Decompose()

PhonePC/2in1TabletTV

```
1. ImageProcessing_ErrorCode OH_ImageProcessing_Decompose(OH_ImageProcessing* imageProcessor,OH_PixelmapNative* sourceImage, OH_PixelmapNative* destinationImage, OH_PixelmapNative* destinationGainmap)
```

**描述**

实现HDR单层图片到HDR双层图片的转换。此函数通过输入图片生成输出图片和输出Gainmap。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ImageProcessing](capi-imageprocessing-oh-imageprocessing.md)\* imageProcessor | 指向图片处理模块实例的指针。该实例应该由IMAGE\_PROCESSING\_TYPE\_DECOMPOSITION类型创建。 |
| [OH\_PixelmapNative](capi-image-nativemodule-oh-pixelmapnative.md)\* sourceImage | 指向输入图片的指针，指向的OH\_PixelmapNative需为DMA内存，具体情况请参考[PixelMap的内存类型介绍](../harmonyos-guides/image-allocator-type.md#内存类型介绍)。 |
| [OH\_PixelmapNative](capi-image-nativemodule-oh-pixelmapnative.md)\* destinationImage | 指向输出图片的指针，指向的OH\_PixelmapNative需为DMA内存，具体情况请参考[PixelMap的内存类型介绍](../harmonyos-guides/image-allocator-type.md#内存类型介绍)。 |
| [OH\_PixelmapNative](capi-image-nativemodule-oh-pixelmapnative.md)\* destinationGainmap | 指向输出Gainmap的指针，指向的OH\_PixelmapNative需为DMA内存，具体情况请参考[PixelMap的内存类型介绍](../harmonyos-guides/image-allocator-type.md#内存类型介绍)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ImageProcessing\_ErrorCode](capi-image-processing-types-h.md#imageprocessing_errorcode) | 如果图片处理成功，则返回IMAGE\_PROCESSING\_SUCCESS。  当该实例为空或该实例不是图片处理模块实例时，返回IMAGE\_PROCESSING\_ERROR\_INVALID\_INSTANCE。  当图片为空时，返回IMAGE\_PROCESSING\_ERROR\_INVALID\_PARAMETER。  当图片的某些属性无效时，返回IMAGE\_PROCESSING\_ERROR\_INVALID\_VALUE，例如图片的色彩空间是不支持的。  当该图片处理不支持时，返回IMAGE\_PROCESSING\_ERROR\_UNSUPPORTED\_PROCESSING。  当该图片处理中返回错误时，返回IMAGE\_PROCESSING\_ERROR\_PROCESS\_FAILED。  当内存分配失败时，返回IMAGE\_PROCESSING\_ERROR\_NO\_MEMORY。 |

### OH\_ImageProcessing\_GenerateMetadata()

PhonePC/2in1TabletTV

```
1. ImageProcessing_ErrorCode OH_ImageProcessing_GenerateMetadata(OH_ImageProcessing* imageProcessor,OH_PixelmapNative* sourceImage)
```

**描述**

生成HDR图片元数据。此函数为HDR图片生成元数据。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ImageProcessing](capi-imageprocessing-oh-imageprocessing.md)\* imageProcessor | 指向图片处理模块实例的指针。该实例应该由IMAGE\_PROCESSING\_TYPE\_METADATA\_GENERATION类型创建。 |
| [OH\_PixelmapNative](capi-image-nativemodule-oh-pixelmapnative.md)\* sourceImage | 指向输入图片的指针，指向的OH\_PixelmapNative需为DMA内存，具体情况请参考[PixelMap的内存类型介绍](../harmonyos-guides/image-allocator-type.md#内存类型介绍)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ImageProcessing\_ErrorCode](capi-image-processing-types-h.md#imageprocessing_errorcode) | 如果图片处理成功，则返回IMAGE\_PROCESSING\_SUCCESS。  当该实例为空或该实例不是图片处理模块实例时，返回IMAGE\_PROCESSING\_ERROR\_INVALID\_INSTANCE。  当图片为空时，返回IMAGE\_PROCESSING\_ERROR\_INVALID\_PARAMETER。  当图片的某些属性无效时，返回IMAGE\_PROCESSING\_ERROR\_INVALID\_VALUE，例如图片的色彩空间是不支持的。  当该图片处理不支持时，返回IMAGE\_PROCESSING\_ERROR\_UNSUPPORTED\_PROCESSING。  当该图片处理中返回错误时，返回IMAGE\_PROCESSING\_ERROR\_PROCESS\_FAILED。  当内存分配失败时，返回IMAGE\_PROCESSING\_ERROR\_NO\_MEMORY。 |

### OH\_ImageProcessing\_EnhanceDetail()

PhonePC/2in1TabletTV

```
1. ImageProcessing_ErrorCode OH_ImageProcessing_EnhanceDetail(OH_ImageProcessing* imageProcessor,OH_PixelmapNative* sourceImage, OH_PixelmapNative* destinationImage)
```

**描述**

进行图片清晰度/细节增强。此函数根据输入图片和输出图片预设的尺寸，对源图片进行必要的缩放操作生成目标图片，并提供了多种缩放方法以平衡性能和图像质量。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ImageProcessing](capi-imageprocessing-oh-imageprocessing.md)\* imageProcessor | 指向图片处理模块实例的指针。该实例应该由IMAGE\_PROCESSING\_TYPE\_DETAIL\_ENHANCER类型创建。 |
| [OH\_PixelmapNative](capi-image-nativemodule-oh-pixelmapnative.md)\* sourceImage | 指向输入图片的指针，指向的OH\_PixelmapNative需为DMA内存，具体情况请参考[PixelMap的内存类型介绍](../harmonyos-guides/image-allocator-type.md#内存类型介绍)。 |
| [OH\_PixelmapNative](capi-image-nativemodule-oh-pixelmapnative.md)\* destinationImage | 指向输出图片的指针，指向的OH\_PixelmapNative需为DMA内存，具体情况请参考[PixelMap的内存类型介绍](../harmonyos-guides/image-allocator-type.md#内存类型介绍)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ImageProcessing\_ErrorCode](capi-image-processing-types-h.md#imageprocessing_errorcode) | 如果图片处理成功，则返回IMAGE\_PROCESSING\_SUCCESS。  当该实例为空或该实例不是图片处理模块实例时，返回IMAGE\_PROCESSING\_ERROR\_INVALID\_INSTANCE。  当图片为空时，返回IMAGE\_PROCESSING\_ERROR\_INVALID\_PARAMETER。  当图片的某些属性无效时，返回IMAGE\_PROCESSING\_ERROR\_INVALID\_VALUE，例如图片的色彩空间是不支持的。  当该图片处理不支持时，返回IMAGE\_PROCESSING\_ERROR\_UNSUPPORTED\_PROCESSING。  当该图片处理中返回错误时，返回IMAGE\_PROCESSING\_ERROR\_PROCESS\_FAILED。  当内存分配失败时，返回IMAGE\_PROCESSING\_ERROR\_NO\_MEMORY。 |
