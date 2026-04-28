---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-processing-types-h
title: image_processing_types.h
breadcrumb: API参考 > 媒体 > Image Kit（图片处理服务） > C API > 头文件 > image_processing_types.h
category: harmonyos-references
scraped_at: 2026-04-28T08:13:23+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:1bcf319ed25a819ffc45702319cce13d852bc5ba664a49075a1c5d8f89694efd
---

## 概述

PhonePC/2in1TabletTV

图片处理的类型定义。

**引用文件：** <multimedia/video\_processing\_engine/image\_processing\_types.h>

**库：** libimage\_processing.so

**系统能力：** SystemCapability.Multimedia.VideoProcessingEngine

**起始版本：** 13

**相关模块：** [ImageProcessing](capi-imageprocessing.md)

## 汇总

PhonePC/2in1TabletTV

### 结构体

PhonePC/2in1TabletTV

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [ImageProcessing\_ColorSpaceInfo](api-imageprocessing-imageprocessing-colorspaceinfo.md) | ImageProcessing\_ColorSpaceInfo | 色彩空间信息，用于色彩空间转换能力查询。 |
| [OH\_ImageProcessing](capi-imageprocessing-oh-imageprocessing.md) | OH\_ImageProcessing | 提供OH\_ImageProcessing结构体声明。  定义了OH\_ImageProcessing的空指针并调用[OH\_ImageProcessing\_Create](capi-image-processing-h.md#oh_imageprocessing_create)来创建图片处理实例。在创建实例之前，指针应为空。用户可以为不同的处理类型创建多个图片实例。 |
| [OH\_PixelmapNative](capi-image-nativemodule-oh-pixelmapnative.md) | OH\_PixelmapNative | 提供OH\_PixelmapNative结构体声明。 |
| [OH\_AVFormat](capi-core-oh-avformat.md) | OH\_AVFormat | 提供OH\_AVFormat结构体声明。 |

### 枚举

PhonePC/2in1TabletTV

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [ImageDetailEnhancer\_QualityLevel](capi-image-processing-types-h.md#imagedetailenhancer_qualitylevel) | ImageDetailEnhancer\_QualityLevel | 质量级别，用于细节增强能力。  键参数的值IMAGE\_DETAIL\_ENHANCER\_PARAMETER\_KEY\_QUALITY\_LEVEL。 |
| [ImageProcessing\_ErrorCode](capi-image-processing-types-h.md#imageprocessing_errorcode) | ImageProcessing\_ErrorCode | 图片处理接口错误码说明。 |

### 变量

PhonePC/2in1TabletTV

| 名称 | 描述 |
| --- | --- |
| const int32\_t IMAGE\_PROCESSING\_TYPE\_COLOR\_SPACE\_CONVERSION | 用于创建色彩空间转换的图片处理实例。  色彩空间转换包括单层HDR图片转换SDR图片，SDR图片之间的转换，以及SDR图片转换单层HDR图片，部分能力由厂商支持。使用[OH\_ImageProcessing\_IsColorSpaceConversionSupported](capi-image-processing-h.md#oh_imageprocessing_iscolorspaceconversionsupported)查询某种转换是否支持在单层图片之间进行。  **起始版本：** 13  **参考：**[OH\_ImageProcessing\_Create](capi-image-processing-h.md#oh_imageprocessing_create) |
| const int32\_t IMAGE\_PROCESSING\_TYPE\_COMPOSITION | 用于创建双层HDR图片转换单层HDR图片的图片处理实例。  包括从双层HDR图片转换为单层HDR图片的能力。部分能力由厂商支持。使用[OH\_ImageProcessing\_IsCompositionSupported](capi-image-processing-h.md#oh_imageprocessing_iscompositionsupported)查询是否支持从双层HDR图片到单层HDR图片的转换。  **起始版本：** 13  **参考：**[OH\_ImageProcessing\_Create](capi-image-processing-h.md#oh_imageprocessing_create) |
| const int32\_t IMAGE\_PROCESSING\_TYPE\_DECOMPOSITION | 用于创建单层HDR图片转换双层HDR图片的图片处理实例。  包括从单层HDR图片转换为双层HDR图片的能力。部分能力由厂商支持。使用[OH\_ImageProcessing\_IsDecompositionSupported](capi-image-processing-h.md#oh_imageprocessing_isdecompositionsupported)查询是否支持从单层HDR图片到双层HDR图片的转换。  **起始版本：** 13  **参考：**[OH\_ImageProcessing\_Create](capi-image-processing-h.md#oh_imageprocessing_create) |
| const int32\_t IMAGE\_PROCESSING\_TYPE\_METADATA\_GENERATION | 用于创建元数据生成的图片处理实例。  生成单层HDR图片的HDR Vivid元数据。该能力由厂商支持。如果不支持该能力，[OH\_ImageProcessing\_Create](capi-image-processing-h.md#oh_imageprocessing_create)将返回[IMAGE\_PROCESSING\_ERROR\_UNSUPPORTED\_PROCESSING](capi-image-processing-types-h.md#imageprocessing_errorcode)。  **起始版本：** 13  **参考：**[OH\_ImageProcessing\_Create](capi-image-processing-h.md#oh_imageprocessing_create) |
| const int32\_t IMAGE\_PROCESSING\_TYPE\_DETAIL\_ENHANCER | 用于创建细节增强的图片处理实例。  按指定图像质量缩放或调整图片大小，或仅增强图像细节以在不更改分辨率的情况下渲染图片。  **起始版本：** 13  **参考：**[OH\_ImageProcessing\_Create](capi-image-processing-h.md#oh_imageprocessing_create) |
| const char \* IMAGE\_DETAIL\_ENHANCER\_PARAMETER\_KEY\_QUALITY\_LEVEL | 用于设定图像细节增强的质量级别。  使用[ImageDetailEnhancer\_QualityLevel](capi-image-processing-types-h.md#imagedetailenhancer_qualitylevel)获取其值。使用[OH\_ImageProcessing\_SetParameter](capi-image-processing-h.md#oh_imageprocessing_setparameter)设置质量级别。使用[OH\_ImageProcessing\_GetParameter](capi-image-processing-h.md#oh_imageprocessing_getparameter)获取当前质量级别。  **起始版本：** 13 |

## 枚举类型说明

PhonePC/2in1TabletTV

### ImageDetailEnhancer\_QualityLevel

PhonePC/2in1TabletTV

```
1. enum ImageDetailEnhancer_QualityLevel
```

**描述**

质量级别，用于细节增强能力。

键参数的值IMAGE\_DETAIL\_ENHANCER\_PARAMETER\_KEY\_QUALITY\_LEVEL。

**起始版本：** 13

| 枚举项 | 描述 |
| --- | --- |
| IMAGE\_DETAIL\_ENHANCER\_QUALITY\_LEVEL\_NONE | 无细节增强。  支持输入分辨率（px）：宽：[32, 3000]，高：[32, 3000]。  支持输出分辨率（px）：宽：[32, 3000]，高：[32, 3000]。 |
| IMAGE\_DETAIL\_ENHANCER\_QUALITY\_LEVEL\_LOW | 细节增强质量较低，但速度较快。默认级别。  支持输入分辨率（px）：宽：[32, 3000]，高：[32, 3000]。  支持输出分辨率（px）：宽：[32, 3000]，高：[32, 3000]。 |
| IMAGE\_DETAIL\_ENHANCER\_QUALITY\_LEVEL\_MEDIUM | 细节增强质量中等，速度介于低级别与高级别之间。  支持输入分辨率（px）：宽：[32, 3000]，高：[32, 3000]。  支持输出分辨率（px）：宽：[32, 3000]，高：[32, 3000]。 |
| IMAGE\_DETAIL\_ENHANCER\_QUALITY\_LEVEL\_HIGH | 细节增强质量较高，但速度较慢。  API version 13-22支持输入分辨率（px）：宽：[512, 2000]，高：[512, 2000]。  API version 13-22支持输出分辨率（px）：宽：[512, 2000]，高：[512, 2000]。  API version 23及以后支持输入分辨率（px）：宽：[180, 2000]，高：[180, 2000]。  API version 23及以后支持输出分辨率（px）：宽：[512, 2000]，高：[512, 2000]。 |

**参考：**

[OH\_ImageProcessing\_SetParameter](capi-image-processing-h.md#oh_imageprocessing_setparameter)，[OH\_ImageProcessing\_GetParameter](capi-image-processing-h.md#oh_imageprocessing_getparameter)

### ImageProcessing\_ErrorCode

PhonePC/2in1TabletTV

```
1. enum ImageProcessing_ErrorCode
```

**描述**

图片处理接口错误码说明。

**起始版本：** 13

| 枚举项 | 描述 |
| --- | --- |
| IMAGE\_PROCESSING\_SUCCESS | 成功。 |
| IMAGE\_PROCESSING\_ERROR\_INVALID\_PARAMETER = 401 | 输入参数无效。  在以下错误条件下返回该错误码：  1. 输入或输出buffer无效，例如图片buffer为空。  2. 参数无效，例如参数为空。  3. 类型无效，例如在创建函数中传入的类型不存在。 |
| IMAGE\_PROCESSING\_ERROR\_UNKNOWN = 29200001 | 未知错误，例如GPU计算失败或memcpy失败。 |
| IMAGE\_PROCESSING\_ERROR\_INITIALIZE\_FAILED | 全局环境初始化失败，例如GPU环境初始化失败。 |
| IMAGE\_PROCESSING\_ERROR\_CREATE\_FAILED | 创建图片处理实例失败，例如实例数量超过上限。 |
| IMAGE\_PROCESSING\_ERROR\_PROCESS\_FAILED | 处理图片buffer失败，例如处理超时。 |
| IMAGE\_PROCESSING\_ERROR\_UNSUPPORTED\_PROCESSING | 当前处理不支持，可以通过“OH\_ImageProcessing\_IsXXXSupported”接口查询是否支持该能力。 |
| IMAGE\_PROCESSING\_ERROR\_OPERATION\_NOT\_PERMITTED | 无权限操作，可能由于状态不正确导致。 |
| IMAGE\_PROCESSING\_ERROR\_NO\_MEMORY | 内存不足。 |
| IMAGE\_PROCESSING\_ERROR\_INVALID\_INSTANCE | 无效的图片处理实例，可能由于实例为空导致。 |
| IMAGE\_PROCESSING\_ERROR\_INVALID\_VALUE | 输入值无效。  在以下错误条件下返回该错误码：  1. 输入或输出图片buffer无效，例如图片buffer的宽度（高度）过大或颜色空间不正确。  2. 参数无效，例如参数不包括有效信息，例如细节增强的质量级别不正确。 |
