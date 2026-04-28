---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-native-h
title: image_native.h
breadcrumb: API参考 > 媒体 > Image Kit（图片处理服务） > C API > 头文件 > image_native.h
category: harmonyos-references
scraped_at: 2026-04-28T08:13:17+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:f999964e2034514bbc7173b1aa440767f38c897ce15be1227e6d4ca904ef6d09
---

## 概述

PhonePC/2in1TabletTVWearable

声明图像的剪辑矩形、大小和组件数据的接口函数。

**引用文件：** <multimedia/image\_framework/image/image\_native.h>

**库：** libohimage.so

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 12

**相关模块：** [Image\_NativeModule](capi-image-nativemodule.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 结构体

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [OH\_ImageBufferData](capi-image-nativemodule-oh-imagebufferdata.md) | OH\_ImageBufferData | OH\_ImageBufferData是native层封装的图像数据结构体。 |
| [OH\_ImageNative](capi-image-nativemodule-oh-imagenative.md) | OH\_ImageNative | 为图像接口定义native层图像对象的别名。 |

### 函数

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [Image\_ErrorCode OH\_ImageNative\_GetImageSize(OH\_ImageNative \*image, Image\_Size \*size)](capi-image-native-h.md#oh_imagenative_getimagesize) | 获取Native [OH\_ImageNative](capi-image-nativemodule-oh-imagenative.md)对象的[Image\_Size](capi-image-nativemodule-image-size.md)信息。 |
| [Image\_ErrorCode OH\_ImageNative\_GetComponentTypes(OH\_ImageNative \*image, uint32\_t \*\*types, size\_t \*typeSize)](capi-image-native-h.md#oh_imagenative_getcomponenttypes) | 获取Native [OH\_ImageNative](capi-image-nativemodule-oh-imagenative.md)对象的组件列表信息。 |
| [Image\_ErrorCode OH\_ImageNative\_GetByteBuffer(OH\_ImageNative \*image, uint32\_t componentType, OH\_NativeBuffer \*\*nativeBuffer)](capi-image-native-h.md#oh_imagenative_getbytebuffer) | 获取Native [OH\_ImageNative](capi-image-nativemodule-oh-imagenative.md)对象中某个组件类型所对应的缓冲区。 |
| [Image\_ErrorCode OH\_ImageNative\_GetBufferSize(OH\_ImageNative \*image, uint32\_t componentType, size\_t \*size)](capi-image-native-h.md#oh_imagenative_getbuffersize) | 获取Native [OH\_ImageNative](capi-image-nativemodule-oh-imagenative.md)对象中某个组件类型所对应的缓冲区的大小。 |
| [Image\_ErrorCode OH\_ImageNative\_GetRowStride(OH\_ImageNative \*image, uint32\_t componentType, int32\_t \*rowStride)](capi-image-native-h.md#oh_imagenative_getrowstride) | 获取Native [OH\_ImageNative](capi-image-nativemodule-oh-imagenative.md)对象中某个组件类型所对应的像素行宽。 |
| [Image\_ErrorCode OH\_ImageNative\_GetPixelStride(OH\_ImageNative \*image, uint32\_t componentType, int32\_t \*pixelStride)](capi-image-native-h.md#oh_imagenative_getpixelstride) | 获取Native [OH\_ImageNative](capi-image-nativemodule-oh-imagenative.md)对象中某个组件类型所对应的像素大小。 |
| [Image\_ErrorCode OH\_ImageNative\_GetTimestamp(OH\_ImageNative \*image, int64\_t \*timestamp)](capi-image-native-h.md#oh_imagenative_gettimestamp) | 获取Native [OH\_ImageNative](capi-image-nativemodule-oh-imagenative.md)对象中的时间戳信息。 |
| [Image\_ErrorCode OH\_ImageNative\_Release(OH\_ImageNative \*image)](capi-image-native-h.md#oh_imagenative_release) | 释放Native [OH\_ImageNative](capi-image-nativemodule-oh-imagenative.md)对象。 |
| [Image\_ErrorCode OH\_ImageNative\_GetColorSpace(OH\_ImageNative \*image, int32\_t \*colorSpaceName)](capi-image-native-h.md#oh_imagenative_getcolorspace) | 获取图像OH\_ImageNative对象中的色彩空间。 |
| [Image\_ErrorCode OH\_ImageNative\_GetFormat(OH\_ImageNative \*image, OH\_NativeBuffer\_Format \*format)](capi-image-native-h.md#oh_imagenative_getformat) | 获取图像OH\_ImageNative对象中的图像格式。 |
| [Image\_ErrorCode OH\_ImageNative\_GetBufferData(OH\_ImageNative \*image, OH\_ImageBufferData \*imageBufferData)](capi-image-native-h.md#oh_imagenative_getbufferdata) | 获取图像OH\_ImageNative对象中的图像缓冲区数据对象。 |

## 函数说明

PhonePC/2in1TabletTVWearable

### OH\_ImageNative\_GetImageSize()

PhonePC/2in1TabletTVWearable

```
1. Image_ErrorCode OH_ImageNative_GetImageSize(OH_ImageNative *image, Image_Size *size)
```

**描述**

获取Native [OH\_ImageNative](capi-image-nativemodule-oh-imagenative.md)对象的[Image\_Size](capi-image-nativemodule-image-size.md)信息。

如果OH\_ImageNative对象所存储的是相机预览流数据，即YUV图像数据，那么获取到的Image\_Size中的宽高分别对应YUV图像的宽高；如果OH\_ImageNative对象所存储的是相机拍照流数据，即JPEG图像，由于已经是编码后的数据，Image\_Size中的宽等于JPEG数据大小，高等于1。

OH\_ImageNative对象所存储的数据是预览流还是拍照流，取决于应用将receiver中的surfaceId传给相机的previewOutput还是captureOutput。相机预览与拍照最佳实践请参考[预览流二次处理(C/C++)](../harmonyos-guides/native-camera-preview-imagereceiver.md)与[拍照(C/C++)](../harmonyos-guides/native-camera-shooting.md)。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ImageNative](capi-image-nativemodule-oh-imagenative.md) \*image | 表示OH\_ImageNative native对象的指针。 |
| [Image\_Size](capi-image-nativemodule-image-size.md) \*size | 表示作为获取结果的Image\_Size对象的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_BAD\_PARAMETER：参数错误。  IMAGE\_UNKNOWN\_ERROR：未知原因错误。 |

### OH\_ImageNative\_GetComponentTypes()

PhonePC/2in1TabletTVWearable

```
1. Image_ErrorCode OH_ImageNative_GetComponentTypes(OH_ImageNative *image,uint32_t **types, size_t *typeSize)
```

**描述**

获取Native [OH\_ImageNative](capi-image-nativemodule-oh-imagenative.md)对象的组件列表信息。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ImageNative](capi-image-nativemodule-oh-imagenative.md) \*image | 表示OH\_ImageNative native对象的指针。 |
| uint32\_t \*\*types | 表示作为获取结果的组件类型列表对象的指针。由于不确定组件个数，需要调用该接口两次：第一次传入types参数为NULL，获取组件个数typeSize；第二次根据typeSize给types申请对应内存，获取组件类型列表。 |
| size\_t \*typeSize | 表示作为获取结果的组件列表中，元素个数的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_BAD\_PARAMETER：参数错误。 |

### OH\_ImageNative\_GetByteBuffer()

PhonePC/2in1TabletTVWearable

```
1. Image_ErrorCode OH_ImageNative_GetByteBuffer(OH_ImageNative *image,uint32_t componentType, OH_NativeBuffer **nativeBuffer)
```

**描述**

获取Native [OH\_ImageNative](capi-image-nativemodule-oh-imagenative.md)对象中某个组件类型所对应的缓冲区。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ImageNative](capi-image-nativemodule-oh-imagenative.md) \*image | 表示OH\_ImageNative native对象的指针。 |
| uint32\_t componentType | 表示组件的类型。通过[OH\_ImageNative\_GetComponentTypes](capi-image-native-h.md#oh_imagenative_getcomponenttypes)接口获取。 |
| [OH\_NativeBuffer](capi-oh-nativebuffer-oh-nativebuffer.md) \*\*nativeBuffer | 表示作为获取结果的OH\_NativeBuffer缓冲区对象的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_BAD\_PARAMETER：参数错误。 |

### OH\_ImageNative\_GetBufferSize()

PhonePC/2in1TabletTVWearable

```
1. Image_ErrorCode OH_ImageNative_GetBufferSize(OH_ImageNative *image,uint32_t componentType, size_t *size)
```

**描述**

获取Native [OH\_ImageNative](capi-image-nativemodule-oh-imagenative.md)对象中某个组件类型所对应的缓冲区的大小。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ImageNative](capi-image-nativemodule-oh-imagenative.md) \*image | 表示OH\_ImageNative native对象的指针。 |
| uint32\_t componentType | 表示组件的类型。通过[OH\_ImageNative\_GetComponentTypes](capi-image-native-h.md#oh_imagenative_getcomponenttypes)接口获取。 |
| size\_t \*size | 表示作为获取结果的缓冲区大小的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_BAD\_PARAMETER：参数错误。 |

### OH\_ImageNative\_GetRowStride()

PhonePC/2in1TabletTVWearable

```
1. Image_ErrorCode OH_ImageNative_GetRowStride(OH_ImageNative *image,uint32_t componentType, int32_t *rowStride)
```

**描述**

获取Native [OH\_ImageNative](capi-image-nativemodule-oh-imagenative.md)对象中某个组件类型所对应的像素行宽。

读取相机预览流数据时，需要考虑按stride进行读取，具体用法参考[预览流二次处理(C/C++)](../harmonyos-guides/native-camera-preview-imagereceiver.md)。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ImageNative](capi-image-nativemodule-oh-imagenative.md) \*image | 表示OH\_ImageNative native对象的指针。 |
| uint32\_t componentType | 表示组件的类型。通过[OH\_ImageNative\_GetComponentTypes](capi-image-native-h.md#oh_imagenative_getcomponenttypes)接口获取。 |
| int32\_t \*rowStride | 表示作为获取结果的像素行宽的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_BAD\_PARAMETER：参数错误。 |

### OH\_ImageNative\_GetPixelStride()

PhonePC/2in1TabletTVWearable

```
1. Image_ErrorCode OH_ImageNative_GetPixelStride(OH_ImageNative *image,uint32_t componentType, int32_t *pixelStride)
```

**描述**

获取Native [OH\_ImageNative](capi-image-nativemodule-oh-imagenative.md)对象中某个组件类型所对应的像素大小。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ImageNative](capi-image-nativemodule-oh-imagenative.md) \*image | 表示OH\_ImageNative native对象的指针。 |
| uint32\_t componentType | 表示组件的类型。通过[OH\_ImageNative\_GetComponentTypes](capi-image-native-h.md#oh_imagenative_getcomponenttypes)接口获取。 |
| int32\_t \*pixelStride | 表示作为获取结果的像素大小的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_BAD\_PARAMETER：参数错误。 |

### OH\_ImageNative\_GetTimestamp()

PhonePC/2in1TabletTVWearable

```
1. Image_ErrorCode OH_ImageNative_GetTimestamp(OH_ImageNative *image, int64_t *timestamp)
```

**描述**

获取Native [OH\_ImageNative](capi-image-nativemodule-oh-imagenative.md)对象中的时间戳信息。时间戳以纳秒为单位，通常是单调递增的。

时间戳的具体含义和基准取决于图像的生产者，在相机预览/拍照场景，生产者就是相机。来自不同生产者的图像的时间戳可能有不同的含义和基准，因此可能无法进行比较。

如果要获取某张照片的生成时间，可以通过[OH\_ImageSourceNative\_GetImageProperty](capi-image-source-native-h.md#oh_imagesourcenative_getimageproperty)接口读取相关的EXIF信息。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ImageNative](capi-image-nativemodule-oh-imagenative.md) \*image | 表示OH\_ImageNative native对象的指针。 |
| int64\_t \*timestamp | 表示作为获取结果的时间戳信息的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_BAD\_PARAMETER：参数错误。 |

### OH\_ImageNative\_Release()

PhonePC/2in1TabletTVWearable

```
1. Image_ErrorCode OH_ImageNative_Release(OH_ImageNative *image)
```

**描述**

释放Native [OH\_ImageNative](capi-image-nativemodule-oh-imagenative.md)对象。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ImageNative](capi-image-nativemodule-oh-imagenative.md) \*image | 表示OH\_ImageNative native对象的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_BAD\_PARAMETER：参数错误。 |

### OH\_ImageNative\_GetColorSpace()

PhonePC/2in1TabletTVWearable

```
1. Image_ErrorCode OH_ImageNative_GetColorSpace(OH_ImageNative *image, int32_t *colorSpaceName)
```

**描述**

获取图像OH\_ImageNative对象中的色彩空间。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ImageNative](capi-image-nativemodule-oh-imagenative.md) \*image | 表示OH\_ImageNative native对象的指针。 |
| int32\_t \*colorSpaceName | 表示图像色彩空间的指针，colorSpaceName的对应色彩空间请参考[ColorSpaceName](capi-native-color-space-manager-h.md#colorspacename)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_BAD\_PARAMETER：参数错误。 |

### OH\_ImageNative\_GetFormat()

PhonePC/2in1TabletTVWearable

```
1. Image_ErrorCode OH_ImageNative_GetFormat(OH_ImageNative *image, OH_NativeBuffer_Format *format)
```

**描述**

获取图像OH\_ImageNative对象中的图像格式。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ImageNative](capi-image-nativemodule-oh-imagenative.md) \*image | 表示OH\_ImageNative native对象的指针。 |
| OH\_NativeBuffer\_Format \*format | 表示图像格式的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_BAD\_PARAMETER：参数错误。 |

### OH\_ImageNative\_GetBufferData()

PhonePC/2in1TabletTVWearable

```
1. Image_ErrorCode OH_ImageNative_GetBufferData(OH_ImageNative *image, OH_ImageBufferData *imageBufferData)
```

**描述**

获取图像OH\_ImageNative对象中的图像缓冲区数据对象。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ImageNative](capi-image-nativemodule-oh-imagenative.md) \*image | 表示OH\_ImageNative native对象的指针。 |
| [OH\_ImageBufferData](capi-image-nativemodule-oh-imagebufferdata.md) \*imageBufferData | 表示图像缓冲区数据对象的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_BAD\_PARAMETER：参数错误。 |
