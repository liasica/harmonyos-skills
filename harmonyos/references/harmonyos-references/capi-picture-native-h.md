---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-picture-native-h
title: picture_native.h
breadcrumb: API参考 > 媒体 > Image Kit（图片处理服务） > C API > 头文件 > picture_native.h
category: harmonyos-references
scraped_at: 2026-09-02T15:02:31+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:351a690ced6234b3bc1ef2da53dd8a0a9b94ad826382926f84722faa6d1e57ca
---

## 概述

提供获取picture数据和信息的API。

**引用文件：** <multimedia/image\_framework/image/picture\_native.h>

**库：** libpicture.so

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 13

**相关模块：** [Image\_NativeModule](capi-image-nativemodule.md)

## 汇总

### 结构体

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [OH\_PictureNative\_AuxiliaryPictureCopyItem](capi-image-nativemodule-oh-picturenative-auxiliarypicturecopyitem.md) | OH\_PictureNative\_AuxiliaryPictureCopyItem | 此结构体用于在创建PictureNative对象的深拷贝时指定辅助图的拷贝规则。描述如何将辅助图从一种类型拷贝到另一种类型。 |
| [OH\_PictureNative\_MetadataCopyItem](capi-image-nativemodule-oh-picturenative-metadatacopyitem.md) | OH\_PictureNative\_MetadataCopyItem | 此结构体用于在创建PictureNative对象的深拷贝时指定元数据的拷贝规则。描述如何将元数据从一种类型拷贝到另一种类型。 |
| [OH\_PictureNative](capi-image-nativemodule-oh-picturenative.md) | - | Picture结构体类型，用于执行picture相关操作。  Picture为多图对象结构体，包含主图、辅助图和元数据。  主图包含图像的大部分信息，主要用于显示图像内容。  辅助图用于存储与主图相关但不同的数据，展示图像更丰富的信息。  元数据一般用来存储关于图像文件的信息。 |
| [OH\_AuxiliaryPictureNative](capi-image-nativemodule-oh-auxiliarypicturenative.md) | - | AuxiliaryPicture结构体类型，用于执行AuxiliaryPicture相关操作。 |
| [OH\_AuxiliaryPictureInfo](capi-image-nativemodule-oh-auxiliarypictureinfo.md) | - | AuxiliaryPictureInfo结构体类型，用于执行AuxiliaryPictureInfo相关操作。 |
| [OH\_ComposeOptions](capi-image-nativemodule-oh-composeoptions.md) | OH\_ComposeOptions | OH\_ComposeOptions是native层封装的合成HDR选项参数结构体，用于设置合成选项参数。用于指定合成HDR所用的参数，例如目标像素格式。 |

### 枚举

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [Image\_AuxiliaryPictureType](capi-picture-native-h.md#image_auxiliarypicturetype) | Image\_AuxiliaryPictureType | 辅助图类型。 |

### 函数

| 名称 | 描述 |
| --- | --- |
| [Image\_ErrorCode OH\_ComposeOptions\_Create(OH\_ComposeOptions \*\*options)](capi-picture-native-h.md#oh_composeoptions_create) | 创建OH\_ComposeOptions实例。 |
| [Image\_ErrorCode OH\_ComposeOptions\_SetDesiredPixelFormat(OH\_ComposeOptions \*options, PIXEL\_FORMAT desiredPixelFormat)](capi-picture-native-h.md#oh_composeoptions_setdesiredpixelformat) | 设置OH\_ComposeOptions中的目标像素格式。 |
| [Image\_ErrorCode OH\_ComposeOptions\_GetDesiredPixelFormat(OH\_ComposeOptions \*options, PIXEL\_FORMAT \*desiredPixelFormat)](capi-picture-native-h.md#oh_composeoptions_getdesiredpixelformat) | 获取OH\_ComposeOptions中的像素格式。 |
| [Image\_ErrorCode OH\_ComposeOptions\_Release(OH\_ComposeOptions \*options)](capi-picture-native-h.md#oh_composeoptions_release) | 释放OH\_ComposeOptions指针。 |
| [Image\_ErrorCode OH\_PictureNative\_CreatePicture(OH\_PixelmapNative \*mainPixelmap, OH\_PictureNative \*\*picture)](capi-picture-native-h.md#oh_picturenative_createpicture) | 创建OH\_PictureNative指针。 |
| [Image\_ErrorCode OH\_PictureNative\_GetMainPixelmap(OH\_PictureNative \*picture, OH\_PixelmapNative \*\*mainPixelmap)](capi-picture-native-h.md#oh_picturenative_getmainpixelmap) | 获取主图的OH\_PixelmapNative指针。 |
| [Image\_ErrorCode OH\_PictureNative\_GetHdrComposedPixelmap(OH\_PictureNative \*picture, OH\_PixelmapNative \*\*hdrPixelmap)](capi-picture-native-h.md#oh_picturenative_gethdrcomposedpixelmap) | 获取hdr图的OH\_PixelmapNative指针。 |
| [Image\_ErrorCode OH\_PictureNative\_GetHdrComposedPixelmapWithOptions(OH\_PictureNative \*picture, OH\_ComposeOptions \*options, OH\_PixelmapNative \*\*hdrPixelmap)](capi-picture-native-h.md#oh_picturenative_gethdrcomposedpixelmapwithoptions) | 通过设置合成选项OH\_ComposeOptions获取HDR图的OH\_PixelmapNative指针。 |
| [Image\_ErrorCode OH\_PictureNative\_GetGainmapPixelmap(OH\_PictureNative \*picture, OH\_PixelmapNative \*\*gainmapPixelmap)](capi-picture-native-h.md#oh_picturenative_getgainmappixelmap) | 获取增益图的OH\_PixelmapNative指针。 |
| [Image\_ErrorCode OH\_PictureNative\_SetAuxiliaryPicture(OH\_PictureNative \*picture, Image\_AuxiliaryPictureType type, OH\_AuxiliaryPictureNative \*auxiliaryPicture)](capi-picture-native-h.md#oh_picturenative_setauxiliarypicture) | 设置辅助图。 |
| [Image\_ErrorCode OH\_PictureNative\_GetAuxiliaryPicture(OH\_PictureNative \*picture, Image\_AuxiliaryPictureType type, OH\_AuxiliaryPictureNative \*\*auxiliaryPicture)](capi-picture-native-h.md#oh_picturenative_getauxiliarypicture) | 根据类型获取辅助图。 |
| [Image\_ErrorCode OH\_PictureNative\_GetMetadata(OH\_PictureNative \*picture, Image\_MetadataType metadataType, OH\_PictureMetadata \*\*metadata)](capi-picture-native-h.md#oh_picturenative_getmetadata) | 获取主图的元数据。 |
| [Image\_ErrorCode OH\_PictureNative\_SetMetadata(OH\_PictureNative \*picture, Image\_MetadataType metadataType, OH\_PictureMetadata \*metadata)](capi-picture-native-h.md#oh_picturenative_setmetadata) | 设置主图的元数据。 |
| [Image\_ErrorCode OH\_PictureNative\_GetAuxiliaryPictureCount(OH\_PictureNative \*picture, uint32\_t \*count)](capi-picture-native-h.md#oh_picturenative_getauxiliarypicturecount) | 获取辅助图数量。 |
| [Image\_ErrorCode OH\_PictureNative\_GetAuxiliaryPictureTypes(OH\_PictureNative \*picture, Image\_AuxiliaryPictureType \*auxiliaryPictureTypes, uint32\_t \*count)](capi-picture-native-h.md#oh_picturenative_getauxiliarypicturetypes) | 获取辅助图类型。 |
| [Image\_ErrorCode OH\_PictureNative\_GetMetadataCount(OH\_PictureNative \*picture, uint32\_t \*count)](capi-picture-native-h.md#oh_picturenative_getmetadatacount) | 获取Picture对象中元数据的数量。 |
| [Image\_ErrorCode OH\_PictureNative\_GetMetadataTypes(OH\_PictureNative \*picture, Image\_MetadataType \*metadataTypes, uint32\_t \*count)](capi-picture-native-h.md#oh_picturenative_getmetadatatypes) | 获取Picture对象中元数据的类型。 |
| [Image\_ErrorCode OH\_PictureNative\_RemoveAuxiliaryPicture(OH\_PictureNative \*picture, Image\_AuxiliaryPictureType type)](capi-picture-native-h.md#oh_picturenative_removeauxiliarypicture) | 从Picture对象中移除辅助图。 |
| [Image\_ErrorCode OH\_PictureNative\_RemoveMetadata(OH\_PictureNative \*picture, Image\_MetadataType type)](capi-picture-native-h.md#oh_picturenative_removemetadata) | 从Picture对象中移除元数据。 |
| [Image\_ErrorCode OH\_PictureNative\_DeepCopyWithItems(OH\_PictureNative \*source, const OH\_PictureNative\_AuxiliaryPictureCopyItem \*auxiliaryPictureCopyItems, uint32\_t auxiliaryPictureCopyCount, const OH\_PictureNative\_MetadataCopyItem \*metadataCopyItems, uint32\_t metadataCopyCount, Image\_AuxiliaryPictureType \*sourceAuxPictureAsMainPixelMap, OH\_PictureNative \*\*picture)](capi-picture-native-h.md#oh_picturenative_deepcopywithitems) | 创建PictureNative对象的深拷贝，并将指定的辅助图和元数据拷贝到指定的目标类型。 |
| [Image\_ErrorCode OH\_PictureNative\_Release(OH\_PictureNative \*picture)](capi-picture-native-h.md#oh_picturenative_release) | 释放OH\_PictureNative指针。 |
| [Image\_ErrorCode OH\_AuxiliaryPictureNative\_Create(uint8\_t \*data, size\_t dataLength, Image\_Size \*size, Image\_AuxiliaryPictureType type, OH\_AuxiliaryPictureNative \*\*auxiliaryPicture)](capi-picture-native-h.md#oh_auxiliarypicturenative_create) | 创建OH\_AuxiliaryPictureNative指针。该接口仅支持传入[PIXEL\_FORMAT](capi-pixelmap-native-h.md#pixel_format)为BGRA\_8888的连续像素数据，会创建出RGBA\_8888的辅助图。 |
| [Image\_ErrorCode OH\_AuxiliaryPictureNative\_WritePixels(OH\_AuxiliaryPictureNative \*auxiliaryPicture, uint8\_t \*source, size\_t bufferSize)](capi-picture-native-h.md#oh_auxiliarypicturenative_writepixels) | 读取缓冲区的图像像素数据，并将结果写入辅助图中。 |
| [Image\_ErrorCode OH\_AuxiliaryPictureNative\_ReadPixels(OH\_AuxiliaryPictureNative \*auxiliaryPicture, uint8\_t \*destination, size\_t \*bufferSize)](capi-picture-native-h.md#oh_auxiliarypicturenative_readpixels) | 读取辅助图的像素数据，结果写入缓冲区。 |
| [Image\_ErrorCode OH\_AuxiliaryPictureNative\_GetType(OH\_AuxiliaryPictureNative \*auxiliaryPicture, Image\_AuxiliaryPictureType \*type)](capi-picture-native-h.md#oh_auxiliarypicturenative_gettype) | 获取辅助图类型。 |
| [Image\_ErrorCode OH\_AuxiliaryPictureNative\_GetInfo(OH\_AuxiliaryPictureNative \*auxiliaryPicture, OH\_AuxiliaryPictureInfo \*\*info)](capi-picture-native-h.md#oh_auxiliarypicturenative_getinfo) | 获取辅助图信息。 |
| [Image\_ErrorCode OH\_AuxiliaryPictureNative\_SetInfo(OH\_AuxiliaryPictureNative \*auxiliaryPicture, OH\_AuxiliaryPictureInfo \*info)](capi-picture-native-h.md#oh_auxiliarypicturenative_setinfo) | 设置辅助图信息。 |
| [Image\_ErrorCode OH\_AuxiliaryPictureNative\_GetMetadata(OH\_AuxiliaryPictureNative \*auxiliaryPicture, Image\_MetadataType metadataType, OH\_PictureMetadata \*\*metadata)](capi-picture-native-h.md#oh_auxiliarypicturenative_getmetadata) | 获取辅助图的元数据。 |
| [Image\_ErrorCode OH\_AuxiliaryPictureNative\_SetMetadata(OH\_AuxiliaryPictureNative \*auxiliaryPicture, Image\_MetadataType metadataType, OH\_PictureMetadata \*metadata)](capi-picture-native-h.md#oh_auxiliarypicturenative_setmetadata) | 设置辅助图的元数据。 |
| [Image\_ErrorCode OH\_AuxiliaryPictureNative\_AcquirePixelmap(OH\_AuxiliaryPictureNative \*auxiliaryPicture, OH\_PixelmapNative \*\*pixelmap)](capi-picture-native-h.md#oh_auxiliarypicturenative_acquirepixelmap) | 获取辅助图的OH\_PixelmapNative对象。 |
| [Image\_ErrorCode OH\_AuxiliaryPictureNative\_Release(OH\_AuxiliaryPictureNative \*picture)](capi-picture-native-h.md#oh_auxiliarypicturenative_release) | 释放OH\_AuxiliaryPictureNative指针。 |
| [Image\_ErrorCode OH\_AuxiliaryPictureInfo\_Create(OH\_AuxiliaryPictureInfo \*\*info)](capi-picture-native-h.md#oh_auxiliarypictureinfo_create) | 创建一个OH\_AuxiliaryPictureInfo对象。 |
| [Image\_ErrorCode OH\_AuxiliaryPictureInfo\_GetType(OH\_AuxiliaryPictureInfo \*info, Image\_AuxiliaryPictureType \*type)](capi-picture-native-h.md#oh_auxiliarypictureinfo_gettype) | 获取OH\_AuxiliaryPictureInfo中的辅助图类型。 |
| [Image\_ErrorCode OH\_AuxiliaryPictureInfo\_SetType(OH\_AuxiliaryPictureInfo \*info, Image\_AuxiliaryPictureType type)](capi-picture-native-h.md#oh_auxiliarypictureinfo_settype) | 设置OH\_AuxiliaryPictureInfo中的辅助图类型。 |
| [Image\_ErrorCode OH\_AuxiliaryPictureInfo\_GetSize(OH\_AuxiliaryPictureInfo \*info, Image\_Size \*size)](capi-picture-native-h.md#oh_auxiliarypictureinfo_getsize) | 获取OH\_AuxiliaryPictureInfo中的图片尺寸。 |
| [Image\_ErrorCode OH\_AuxiliaryPictureInfo\_SetSize(OH\_AuxiliaryPictureInfo \*info, Image\_Size \*size)](capi-picture-native-h.md#oh_auxiliarypictureinfo_setsize) | 设置OH\_AuxiliaryPictureInfo中的图片尺寸。 |
| [Image\_ErrorCode OH\_AuxiliaryPictureInfo\_GetRowStride(OH\_AuxiliaryPictureInfo \*info, uint32\_t \*rowStride)](capi-picture-native-h.md#oh_auxiliarypictureinfo_getrowstride) | 获取OH\_AuxiliaryPictureInfo中的行跨距。 |
| [Image\_ErrorCode OH\_AuxiliaryPictureInfo\_SetRowStride(OH\_AuxiliaryPictureInfo \*info, uint32\_t rowStride)](capi-picture-native-h.md#oh_auxiliarypictureinfo_setrowstride) | 设置OH\_AuxiliaryPictureInfo中的行跨距。 |
| [Image\_ErrorCode OH\_AuxiliaryPictureInfo\_GetPixelFormat(OH\_AuxiliaryPictureInfo \*info, PIXEL\_FORMAT \*pixelFormat)](capi-picture-native-h.md#oh_auxiliarypictureinfo_getpixelformat) | 获取OH\_AuxiliaryPictureInfo中的像素格式。 |
| [Image\_ErrorCode OH\_AuxiliaryPictureInfo\_SetPixelFormat(OH\_AuxiliaryPictureInfo \*info, PIXEL\_FORMAT pixelFormat)](capi-picture-native-h.md#oh_auxiliarypictureinfo_setpixelformat) | 设置OH\_AuxiliaryPictureInfo中的像素格式。 |
| [Image\_ErrorCode OH\_AuxiliaryPictureInfo\_Release(OH\_AuxiliaryPictureInfo \*info)](capi-picture-native-h.md#oh_auxiliarypictureinfo_release) | 释放OH\_AuxiliaryPictureInfo指针。 |

## 枚举类型说明

### Image\_AuxiliaryPictureType

```c
enum Image_AuxiliaryPictureType
```

**描述**

辅助图类型。

**起始版本：** 13

| 枚举项 | 描述 |
| --- | --- |
| AUXILIARY\_PICTURE\_TYPE\_GAINMAP = 1 | 增益图，代表了一种增强SDR图像以产生具有可变显示调整能力的HDR图像的机制。它是一组描述如何应用gainmap元数据的组合。 |
| AUXILIARY\_PICTURE\_TYPE\_DEPTH\_MAP = 2 | 深度图，储存图像的深度数据，通过捕捉每个像素与摄像机之间的距离，提供场景的三维结构信息，通常用于3D重建和场景理解。 |
| AUXILIARY\_PICTURE\_TYPE\_UNREFOCUS\_MAP = 3 | 人像未对焦的原图，提供了一种在人像拍摄中突出背景模糊效果的方式，能够帮助用户在后期处理中选择焦点区域，增加创作自由度。 |
| AUXILIARY\_PICTURE\_TYPE\_LINEAR\_MAP = 4 | 线性图，用于提供额外的数据视角或补充信息，通常用于视觉效果的增强，它可以包含场景中光照、颜色或其他视觉元素的线性表示。 |
| AUXILIARY\_PICTURE\_TYPE\_FRAGMENT\_MAP = 5 | 水印裁剪图，表示在原图中被水印覆盖的区域，该图像用于修复或移除水印影响，恢复图像的完整性和可视性。 |

## 函数说明

### OH\_ComposeOptions\_Create()

```c
Image_ErrorCode OH_ComposeOptions_Create(OH_ComposeOptions **options)
```

**描述**

创建OH\_ComposeOptions实例。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ComposeOptions](capi-image-nativemodule-oh-composeoptions.md) \*\*options | 被操作的OH\_ComposeOptions指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_BAD\_PARAMETER：参数错误。 |

### OH\_ComposeOptions\_SetDesiredPixelFormat()

```c
Image_ErrorCode OH_ComposeOptions_SetDesiredPixelFormat(OH_ComposeOptions *options, PIXEL_FORMAT desiredPixelFormat)
```

**描述**

设置OH\_ComposeOptions中的目标像素格式。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ComposeOptions](capi-image-nativemodule-oh-composeoptions.md) \*options | 被操作的OH\_ComposeOptions指针。 |
| [PIXEL\_FORMAT](capi-pixelmap-native-h.md#pixel_format) desiredPixelFormat | 被设置的像素格式，支持RGBA\_1010102、YCBCR\_P010和YCRCB\_P010格式。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_BAD\_PARAMETER：参数错误，例如options为nullptr或传入了不支持的desiredPixelFormat。 |

### OH\_ComposeOptions\_GetDesiredPixelFormat()

```c
Image_ErrorCode OH_ComposeOptions_GetDesiredPixelFormat(OH_ComposeOptions *options, PIXEL_FORMAT *desiredPixelFormat)
```

**描述**

获取OH\_ComposeOptions中的像素格式。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ComposeOptions](capi-image-nativemodule-oh-composeoptions.md) \*options | 被操作的OH\_ComposeOptions指针。 |
| [PIXEL\_FORMAT](capi-pixelmap-native-h.md#pixel_format) \*desiredPixelFormat | 合成选项中的像素格式。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_BAD\_PARAMETER：参数错误。 |

### OH\_ComposeOptions\_Release()

```c
Image_ErrorCode OH_ComposeOptions_Release(OH_ComposeOptions *options)
```

**描述**

释放OH\_ComposeOptions指针。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ComposeOptions](capi-image-nativemodule-oh-composeoptions.md) \*options | 被操作的OH\_ComposeOptions指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_BAD\_PARAMETER：参数错误。 |

### OH\_PictureNative\_CreatePicture()

```c
Image_ErrorCode OH_PictureNative_CreatePicture(OH_PixelmapNative *mainPixelmap, OH_PictureNative **picture)
```

**描述**

创建OH\_PictureNative指针。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_PixelmapNative](capi-image-nativemodule-oh-pixelmapnative.md) \*mainPixelmap | 主图的OH\_PixelmapNative指针。 |
| [OH\_PictureNative](capi-image-nativemodule-oh-picturenative.md) \*\*picture | 被创建的OH\_PictureNative指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_BAD\_PARAMETER：参数错误。 |

### OH\_PictureNative\_GetMainPixelmap()

```c
Image_ErrorCode OH_PictureNative_GetMainPixelmap(OH_PictureNative *picture, OH_PixelmapNative **mainPixelmap)
```

**描述**

获取主图的OH\_PixelmapNative指针。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_PictureNative](capi-image-nativemodule-oh-picturenative.md) \*picture | 被操作的OH\_PictureNative指针。 |
| [OH\_PixelmapNative](capi-image-nativemodule-oh-pixelmapnative.md) \*\*mainPixelmap | 获取的OH\_PixelmapNative指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_BAD\_PARAMETER：参数错误。 |

### OH\_PictureNative\_GetHdrComposedPixelmap()

```c
Image_ErrorCode OH_PictureNative_GetHdrComposedPixelmap(OH_PictureNative *picture, OH_PixelmapNative **hdrPixelmap)
```

**描述**

获取hdr图的OH\_PixelmapNative指针。

使用约束：picture和hdrPixelmap均不能为空指针。Picture不支持HDR合成时，接口会返回IMAGE\_UNSUPPORTED\_OPERATION。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_PictureNative](capi-image-nativemodule-oh-picturenative.md) \*picture | 被操作的OH\_PictureNative指针。 |
| [OH\_PixelmapNative](capi-image-nativemodule-oh-pixelmapnative.md) \*\*hdrPixelmap | 获取的hdr图OH\_PixelmapNative指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_BAD\_PARAMETER：参数错误。  IMAGE\_UNSUPPORTED\_OPERATION：操作不支持，例如picture对象中不包含增益图。 |

### OH\_PictureNative\_GetHdrComposedPixelmapWithOptions()

```c
Image_ErrorCode OH_PictureNative_GetHdrComposedPixelmapWithOptions(OH_PictureNative *picture, OH_ComposeOptions *options, OH_PixelmapNative **hdrPixelmap)
```

**描述**

通过设置合成选项OH\_ComposeOptions获取HDR图的OH\_PixelmapNative指针。

使用约束：picture、options和hdrPixelmap均不能为空指针。Picture不支持HDR合成时，接口会返回IMAGE\_UNSUPPORTED\_OPERATION。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_PictureNative](capi-image-nativemodule-oh-picturenative.md) \*picture | 被操作的OH\_PictureNative指针。 |
| [OH\_ComposeOptions](capi-image-nativemodule-oh-composeoptions.md) \*options | 合成选项OH\_ComposeOptions指针。 |
| [OH\_PixelmapNative](capi-image-nativemodule-oh-pixelmapnative.md) \*\*hdrPixelmap | 获取的HDR图OH\_PixelmapNative指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_BAD\_PARAMETER：参数错误。  IMAGE\_UNSUPPORTED\_OPERATION：操作不支持，例如picture对象中不包含增益图。 |

### OH\_PictureNative\_GetGainmapPixelmap()

```c
Image_ErrorCode OH_PictureNative_GetGainmapPixelmap(OH_PictureNative *picture, OH_PixelmapNative **gainmapPixelmap)
```

**描述**

获取增益图的OH\_PixelmapNative指针。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_PictureNative](capi-image-nativemodule-oh-picturenative.md) \*picture | 被操作的OH\_PictureNative指针。 |
| [OH\_PixelmapNative](capi-image-nativemodule-oh-pixelmapnative.md) \*\*gainmapPixelmap | 获取的增益图OH\_PixelmapNative指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_BAD\_PARAMETER：参数错误。 |

### OH\_PictureNative\_SetAuxiliaryPicture()

```c
Image_ErrorCode OH_PictureNative_SetAuxiliaryPicture(OH_PictureNative *picture, Image_AuxiliaryPictureType type, OH_AuxiliaryPictureNative *auxiliaryPicture)
```

**描述**

设置辅助图。

使用约束：picture和auxiliaryPicture均不能为空指针，type必须为当前支持的辅助图类型，且必须与auxiliaryPicture对象自身的辅助图类型一致。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_PictureNative](capi-image-nativemodule-oh-picturenative.md) \*picture | 被操作的OH\_PictureNative指针。 |
| [Image\_AuxiliaryPictureType](capi-picture-native-h.md#image_auxiliarypicturetype) type | 辅助图的类型。 |
| [OH\_AuxiliaryPictureNative](capi-image-nativemodule-oh-auxiliarypicturenative.md) \*auxiliaryPicture | 设置的OH\_AuxiliaryPictureNative指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_BAD\_PARAMETER：参数错误。 |

### OH\_PictureNative\_GetAuxiliaryPicture()

```c
Image_ErrorCode OH_PictureNative_GetAuxiliaryPicture(OH_PictureNative *picture, Image_AuxiliaryPictureType type, OH_AuxiliaryPictureNative **auxiliaryPicture)
```

**描述**

根据类型获取辅助图。

使用约束：picture和auxiliaryPicture均不能为空指针，type必须为当前支持的辅助图类型。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_PictureNative](capi-image-nativemodule-oh-picturenative.md) \*picture | 被操作的OH\_PictureNative指针。 |
| [Image\_AuxiliaryPictureType](capi-picture-native-h.md#image_auxiliarypicturetype) type | 辅助图类型。 |
| [OH\_AuxiliaryPictureNative](capi-image-nativemodule-oh-auxiliarypicturenative.md) \*\*auxiliaryPicture | 获取的OH\_AuxiliaryPictureNative指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_BAD\_PARAMETER：参数错误。 |

### OH\_PictureNative\_GetMetadata()

```c
Image_ErrorCode OH_PictureNative_GetMetadata(OH_PictureNative *picture, Image_MetadataType metadataType, OH_PictureMetadata **metadata)
```

**描述**

获取主图的元数据。

使用约束：picture和metadata均不能为空指针，metadataType必须为Picture允许的元数据类型；不支持的元数据类型会返回IMAGE\_UNSUPPORTED\_METADATA。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_PictureNative](capi-image-nativemodule-oh-picturenative.md) \*picture | 被操作的OH\_PictureNative指针。 |
| [Image\_MetadataType](capi-image-common-h.md#image_metadatatype) metadataType | 元数据类型。 |
| [OH\_PictureMetadata](capi-image-nativemodule-oh-picturemetadata.md) \*\*metadata | 主图的元数据。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_BAD\_PARAMETER：参数错误。  IMAGE\_UNSUPPORTED\_METADATA：不支持的元数据类型。 |

### OH\_PictureNative\_SetMetadata()

```c
Image_ErrorCode OH_PictureNative_SetMetadata(OH_PictureNative *picture, Image_MetadataType metadataType, OH_PictureMetadata *metadata)
```

**描述**

设置主图的元数据。

使用约束：picture和metadata均不能为空指针，metadataType必须为Picture允许的元数据类型。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_PictureNative](capi-image-nativemodule-oh-picturenative.md) \*picture | 被操作的OH\_PictureNative指针。 |
| [Image\_MetadataType](capi-image-common-h.md#image_metadatatype) metadataType | 元数据类型。 |
| [OH\_PictureMetadata](capi-image-nativemodule-oh-picturemetadata.md) \*metadata | 将设置的元数据。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_BAD\_PARAMETER：参数错误。  IMAGE\_UNSUPPORTED\_METADATA：不支持的元数据类型。 |

### OH\_PictureNative\_GetAuxiliaryPictureCount()

```c
Image_ErrorCode OH_PictureNative_GetAuxiliaryPictureCount(OH_PictureNative *picture, uint32_t *count)
```

**描述**

获取辅助图数量。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_PictureNative](capi-image-nativemodule-oh-picturenative.md) \*picture | 指向OH\_PictureNative对象的指针。 |
| uint32\_t \*count | 辅助图数量。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | * IMAGE\_SUCCESS：执行成功。  * IMAGE\_INVALID\_PARAMETER：picture或count为空指针、获取picture失败。 |

### OH\_PictureNative\_GetAuxiliaryPictureTypes()

```c
Image_ErrorCode OH_PictureNative_GetAuxiliaryPictureTypes(OH_PictureNative *picture, Image_AuxiliaryPictureType *auxiliaryPictureTypes, uint32_t *count)
```

**描述**

获取辅助图类型。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_PictureNative](capi-image-nativemodule-oh-picturenative.md) \*picture | 指向OH\_PictureNative对象的指针。 |
| [Image\_AuxiliaryPictureType](capi-picture-native-h.md#image_auxiliarypicturetype) \*auxiliaryPictureTypes | 指向接收辅助图类型的数组的指针。 |
| uint32\_t \*count | 输入时，为辅助图类型数组的大小。输出时，为辅助图的实际数量。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | * IMAGE\_SUCCESS：执行成功。  * IMAGE\_INVALID\_PARAMETER：picture、auxiliaryPictureTypes或count为空指针、无法获取图片、count小于要求。 |

### OH\_PictureNative\_GetMetadataCount()

```c
Image_ErrorCode OH_PictureNative_GetMetadataCount(OH_PictureNative *picture, uint32_t *count)
```

**描述**

获取Picture对象中元数据的数量。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_PictureNative](capi-image-nativemodule-oh-picturenative.md) \*picture | 指向OH\_PictureNative对象的指针。 |
| uint32\_t \*count | 元数据数量。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | * IMAGE\_SUCCESS：执行成功。  * IMAGE\_INVALID\_PARAMETER：picture或count为空指针、获取picture失败。 |

### OH\_PictureNative\_GetMetadataTypes()

```c
Image_ErrorCode OH_PictureNative_GetMetadataTypes(OH_PictureNative *picture, Image_MetadataType *metadataTypes, uint32_t *count)
```

**描述**

获取Picture对象中元数据的类型。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_PictureNative](capi-image-nativemodule-oh-picturenative.md) \*picture | 指向OH\_PictureNative对象的指针。 |
| [Image\_MetadataType](capi-image-common-h.md#image_metadatatype) \*metadataTypes | 接收元数据类型的数组指针。 |
| uint32\_t \*count | 输入时，metadataTypes数组的大小。输出时，元数据的实际数量。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | * IMAGE\_SUCCESS：执行成功。  * IMAGE\_INVALID\_PARAMETER：picture、metadataTypes或count为空指针、获取picture失败、count小于所需大小。 |

### OH\_PictureNative\_RemoveAuxiliaryPicture()

```c
Image_ErrorCode OH_PictureNative_RemoveAuxiliaryPicture(OH_PictureNative *picture, Image_AuxiliaryPictureType type)
```

**描述**

从Picture对象中移除辅助图。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_PictureNative](capi-image-nativemodule-oh-picturenative.md) \*picture | 指向OH\_PictureNative对象的指针。 |
| [Image\_AuxiliaryPictureType](capi-picture-native-h.md#image_auxiliarypicturetype) type | 移除的辅助图类型。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | * IMAGE\_SUCCESS：辅助图被成功移除或不存在。  * IMAGE\_INVALID\_PARAMETER：picture为空指针、获取picture失败、辅助图类型不支持。 |

### OH\_PictureNative\_RemoveMetadata()

```c
Image_ErrorCode OH_PictureNative_RemoveMetadata(OH_PictureNative *picture, Image_MetadataType type)
```

**描述**

从Picture对象中移除元数据。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_PictureNative](capi-image-nativemodule-oh-picturenative.md) \*picture | 指向OH\_PictureNative对象的指针。 |
| [Image\_MetadataType](capi-image-common-h.md#image_metadatatype) type | 移除的元数据类型。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | * IMAGE\_SUCCESS：元数据被成功移除或不存在。  * IMAGE\_INVALID\_PARAMETER：picture为空指针、获取picture失败。  * IMAGE\_UNSUPPORTED\_METADATA：不支持的元数据类型。 |

### OH\_PictureNative\_DeepCopyWithItems()

```c
Image_ErrorCode OH_PictureNative_DeepCopyWithItems(OH_PictureNative *source, const OH_PictureNative_AuxiliaryPictureCopyItem *auxiliaryPictureCopyItems, uint32_t auxiliaryPictureCopyCount, const OH_PictureNative_MetadataCopyItem *metadataCopyItems, uint32_t metadataCopyCount, Image_AuxiliaryPictureType *sourceAuxPictureAsMainPixelMap, OH_PictureNative **picture)
```

**描述**

创建PictureNative对象的深拷贝，并将指定的辅助图和元数据拷贝到指定的目标类型。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_PictureNative](capi-image-nativemodule-oh-picturenative.md) \*source | 源PictureNative对象，不能为NULL。 |
| [const OH\_PictureNative\_AuxiliaryPictureCopyItem](capi-image-nativemodule-oh-picturenative-auxiliarypicturecopyitem.md) \*auxiliaryPictureCopyItems | 描述需要拷贝的辅助图的结构体。包括源辅助图和目标辅助图类型。如果auxiliaryPictureCopyCount为0，可以为NULL。 |
| uint32\_t auxiliaryPictureCopyCount | 需要拷贝的辅助图数量。 |
| [const OH\_PictureNative\_MetadataCopyItem](capi-image-nativemodule-oh-picturenative-metadatacopyitem.md) \*metadataCopyItems | 描述需要拷贝的元数据的结构体。包括源元数据类型和目标元数据类型。如果metadataCopyCount为0，可以为NULL。 |
| uint32\_t metadataCopyCount | 需要拷贝的元数据数量。 |
| [Image\_AuxiliaryPictureType](capi-picture-native-h.md#image_auxiliarypicturetype) \*sourceAuxPictureAsMainPixelMap | 指定源图片中作为拷贝图片主图的辅助图类型。如果应使用原始主图，可以为NULL。 |
| [OH\_PictureNative](capi-image-nativemodule-oh-picturenative.md) \*\*picture | 输出参数，用于接收新创建的PictureNative对象。当调用者不再需要时释放该对象。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | * IMAGE\_SUCCESS：执行成功。  * IMAGE\_INVALID\_PARAMETER：source或picture为空指针、获取picture失败或数量不匹配、数量不为零但对应数组为空指针。  * IMAGE\_ALLOC\_FAILED：内存分配失败。 |

### OH\_PictureNative\_Release()

```c
Image_ErrorCode OH_PictureNative_Release(OH_PictureNative *picture)
```

**描述**

释放OH\_PictureNative指针。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_PictureNative](capi-image-nativemodule-oh-picturenative.md) \*picture | 被操作的OH\_PictureNative指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_BAD\_PARAMETER：参数错误。 |

### OH\_AuxiliaryPictureNative\_Create()

```c
Image_ErrorCode OH_AuxiliaryPictureNative_Create(uint8_t *data, size_t dataLength, Image_Size *size, Image_AuxiliaryPictureType type, OH_AuxiliaryPictureNative **auxiliaryPicture)
```

**描述**

创建OH\_AuxiliaryPictureNative指针。该接口仅支持传入[PIXEL\_FORMAT](capi-pixelmap-native-h.md#pixel_format)为BGRA\_8888的连续像素数据，会创建出RGBA\_8888的辅助图。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| uint8\_t \*data | 图像数据。 |
| size\_t dataLength | 图像数据长度。 |
| [Image\_Size](capi-image-nativemodule-image-size.md) \*size | 辅助图尺寸。 |
| [Image\_AuxiliaryPictureType](capi-picture-native-h.md#image_auxiliarypicturetype) type | 辅助图类型。 |
| [OH\_AuxiliaryPictureNative](capi-image-nativemodule-oh-auxiliarypicturenative.md) \*\*auxiliaryPicture | 被创建的OH\_AuxiliaryPictureNative指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_BAD\_PARAMETER：参数错误。 |

### OH\_AuxiliaryPictureNative\_WritePixels()

```c
Image_ErrorCode OH_AuxiliaryPictureNative_WritePixels(OH_AuxiliaryPictureNative *auxiliaryPicture, uint8_t *source, size_t bufferSize)
```

**描述**

读取缓冲区的图像像素数据，并将结果写入辅助图中。

使用约束：auxiliaryPicture和source均不能为空指针，bufferSize需与待写入像素数据大小匹配。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AuxiliaryPictureNative](capi-image-nativemodule-oh-auxiliarypicturenative.md) \*auxiliaryPicture | 被操作的OH\_AuxiliaryPictureNative指针。 |
| uint8\_t \*source | 将被写入的图像像素数据。 |
| size\_t bufferSize | 图像像素数据长度。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_BAD\_PARAMETER：参数错误。  IMAGE\_ALLOC\_FAILED：内存分配失败。  IMAGE\_COPY\_FAILED：内存拷贝失败。 |

### OH\_AuxiliaryPictureNative\_ReadPixels()

```c
Image_ErrorCode OH_AuxiliaryPictureNative_ReadPixels(OH_AuxiliaryPictureNative *auxiliaryPicture, uint8_t *destination, size_t *bufferSize)
```

**描述**

读取辅助图的像素数据，结果写入缓冲区。

使用约束：auxiliaryPicture、destination和bufferSize均不能为空指针，bufferSize需表示destination可写入的缓冲区大小；接口执行成功后，bufferSize会更新为实际读取的数据大小。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AuxiliaryPictureNative](capi-image-nativemodule-oh-auxiliarypicturenative.md) \*auxiliaryPicture | 被操作的OH\_AuxiliaryPictureNative指针。 |
| uint8\_t \*destination | 缓冲区，获取的辅助图像素数据写入到该内存区域内。 |
| size\_t \*bufferSize | 缓冲区大小。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_BAD\_PARAMETER：参数错误。  IMAGE\_ALLOC\_FAILED：内存分配失败。  IMAGE\_COPY\_FAILED：内存拷贝失败。 |

### OH\_AuxiliaryPictureNative\_GetType()

```c
Image_ErrorCode OH_AuxiliaryPictureNative_GetType(OH_AuxiliaryPictureNative *auxiliaryPicture, Image_AuxiliaryPictureType *type)
```

**描述**

获取辅助图类型。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AuxiliaryPictureNative](capi-image-nativemodule-oh-auxiliarypicturenative.md) \*auxiliaryPicture | 被操作的OH\_AuxiliaryPictureNative指针。 |
| [Image\_AuxiliaryPictureType](capi-picture-native-h.md#image_auxiliarypicturetype) \*type | 辅助图类型。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_BAD\_PARAMETER：参数错误。 |

### OH\_AuxiliaryPictureNative\_GetInfo()

```c
Image_ErrorCode OH_AuxiliaryPictureNative_GetInfo(OH_AuxiliaryPictureNative *auxiliaryPicture, OH_AuxiliaryPictureInfo **info)
```

**描述**

获取辅助图信息。

资源管理：接口成功返回的OH\_AuxiliaryPictureInfo对象由调用方管理，使用完成后应调用OH\_AuxiliaryPictureInfo\_Release()释放。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AuxiliaryPictureNative](capi-image-nativemodule-oh-auxiliarypicturenative.md) \*auxiliaryPicture | 被操作的OH\_AuxiliaryPictureNative指针。 |
| [OH\_AuxiliaryPictureInfo](capi-image-nativemodule-oh-auxiliarypictureinfo.md) \*\*info | 辅助图信息。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_BAD\_PARAMETER：参数错误。 |

### OH\_AuxiliaryPictureNative\_SetInfo()

```c
Image_ErrorCode OH_AuxiliaryPictureNative_SetInfo(OH_AuxiliaryPictureNative *auxiliaryPicture, OH_AuxiliaryPictureInfo *info)
```

**描述**

设置辅助图信息。

资源管理：接口会读取并保存OH\_AuxiliaryPictureInfo中的信息值，接口返回后调用方仍需自行管理该OH\_AuxiliaryPictureInfo对象的生命周期。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AuxiliaryPictureNative](capi-image-nativemodule-oh-auxiliarypicturenative.md) \*auxiliaryPicture | 将操作的OH\_AuxiliaryPictureNative指针。 |
| [OH\_AuxiliaryPictureInfo](capi-image-nativemodule-oh-auxiliarypictureinfo.md) \*info | 将要设置的辅助图信息。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_BAD\_PARAMETER：参数错误。 |

### OH\_AuxiliaryPictureNative\_GetMetadata()

```c
Image_ErrorCode OH_AuxiliaryPictureNative_GetMetadata(OH_AuxiliaryPictureNative *auxiliaryPicture, Image_MetadataType metadataType, OH_PictureMetadata **metadata)
```

**描述**

获取辅助图的元数据。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AuxiliaryPictureNative](capi-image-nativemodule-oh-auxiliarypicturenative.md) \*auxiliaryPicture | 将操作的OH\_AuxiliaryPictureNative指针。 |
| [Image\_MetadataType](capi-image-common-h.md#image_metadatatype) metadataType | 元数据类型。 |
| [OH\_PictureMetadata](capi-image-nativemodule-oh-picturemetadata.md) \*\*metadata | 获取的元数据。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_BAD\_PARAMETER：参数错误。  IMAGE\_UNSUPPORTED\_METADATA：不支持的元数据类型，或者元数据类型与辅助图片类型不匹配。 |

### OH\_AuxiliaryPictureNative\_SetMetadata()

```c
Image_ErrorCode OH_AuxiliaryPictureNative_SetMetadata(OH_AuxiliaryPictureNative *auxiliaryPicture, Image_MetadataType metadataType, OH_PictureMetadata *metadata)
```

**描述**

设置辅助图的元数据。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AuxiliaryPictureNative](capi-image-nativemodule-oh-auxiliarypicturenative.md) \*auxiliaryPicture | 将操作的OH\_AuxiliaryPictureNative指针。 |
| [Image\_MetadataType](capi-image-common-h.md#image_metadatatype) metadataType | 元数据类型。 |
| [OH\_PictureMetadata](capi-image-nativemodule-oh-picturemetadata.md) \*metadata | 将要设置的元数据。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_BAD\_PARAMETER：参数错误。  IMAGE\_UNSUPPORTED\_METADATA：不支持的元数据类型，或者元数据类型与辅助图片类型不匹配。 |

### OH\_AuxiliaryPictureNative\_AcquirePixelmap()

```c
Image_ErrorCode OH_AuxiliaryPictureNative_AcquirePixelmap(OH_AuxiliaryPictureNative *auxiliaryPicture, OH_PixelmapNative **pixelmap)
```

**描述**

获取辅助图的OH\_PixelmapNative对象。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AuxiliaryPictureNative](capi-image-nativemodule-oh-auxiliarypicturenative.md) \*auxiliaryPicture | 指向OH\_AuxiliaryPictureNative对象的指针。 |
| [OH\_PixelmapNative](capi-image-nativemodule-oh-pixelmapnative.md) \*\*pixelmap | 输出参数，用于接收获取到的OH\_PixelmapNative对象地址。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | * IMAGE\_SUCCESS：执行成功。  * IMAGE\_INVALID\_PARAMETER：auxiliaryPicture或pixelmap为空指针。  * IMAGE\_GET\_IMAGE\_DATA\_FAILED：无法获取辅助图或像素数据。  * IMAGE\_ALLOC\_FAILED：内存分配失败。 |

### OH\_AuxiliaryPictureNative\_Release()

```c
Image_ErrorCode OH_AuxiliaryPictureNative_Release(OH_AuxiliaryPictureNative *picture)
```

**描述**

释放OH\_AuxiliaryPictureNative指针。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AuxiliaryPictureNative](capi-image-nativemodule-oh-auxiliarypicturenative.md) \*picture | 将操作的OH\_AuxiliaryPictureNative指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_BAD\_PARAMETER：参数错误。 |

### OH\_AuxiliaryPictureInfo\_Create()

```c
Image_ErrorCode OH_AuxiliaryPictureInfo_Create(OH_AuxiliaryPictureInfo **info)
```

**描述**

创建一个OH\_AuxiliaryPictureInfo对象。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AuxiliaryPictureInfo](capi-image-nativemodule-oh-auxiliarypictureinfo.md) \*\*info | 将操作的OH\_AuxiliaryPictureInfo指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_BAD\_PARAMETER：参数错误。 |

### OH\_AuxiliaryPictureInfo\_GetType()

```c
Image_ErrorCode OH_AuxiliaryPictureInfo_GetType(OH_AuxiliaryPictureInfo *info, Image_AuxiliaryPictureType *type)
```

**描述**

获取OH\_AuxiliaryPictureInfo中的辅助图类型。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AuxiliaryPictureInfo](capi-image-nativemodule-oh-auxiliarypictureinfo.md) \*info | 将操作的OH\_AuxiliaryPictureInfo指针。 |
| [Image\_AuxiliaryPictureType](capi-picture-native-h.md#image_auxiliarypicturetype) \*type | 获取的辅助图类型。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_BAD\_PARAMETER：参数错误。 |

### OH\_AuxiliaryPictureInfo\_SetType()

```c
Image_ErrorCode OH_AuxiliaryPictureInfo_SetType(OH_AuxiliaryPictureInfo *info, Image_AuxiliaryPictureType type)
```

**描述**

设置OH\_AuxiliaryPictureInfo中的辅助图类型。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AuxiliaryPictureInfo](capi-image-nativemodule-oh-auxiliarypictureinfo.md) \*info | 将操作的OH\_AuxiliaryPictureInfo指针。 |
| [Image\_AuxiliaryPictureType](capi-picture-native-h.md#image_auxiliarypicturetype) type | 将要设置的辅助图类型。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_BAD\_PARAMETER：参数错误。 |

### OH\_AuxiliaryPictureInfo\_GetSize()

```c
Image_ErrorCode OH_AuxiliaryPictureInfo_GetSize(OH_AuxiliaryPictureInfo *info, Image_Size *size)
```

**描述**

获取OH\_AuxiliaryPictureInfo中的图片尺寸。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AuxiliaryPictureInfo](capi-image-nativemodule-oh-auxiliarypictureinfo.md) \*info | 将操作的OH\_AuxiliaryPictureInfo指针。 |
| [Image\_Size](capi-image-nativemodule-image-size.md) \*size | 获取的图片尺寸。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_BAD\_PARAMETER：参数错误。 |

### OH\_AuxiliaryPictureInfo\_SetSize()

```c
Image_ErrorCode OH_AuxiliaryPictureInfo_SetSize(OH_AuxiliaryPictureInfo *info, Image_Size *size)
```

**描述**

设置OH\_AuxiliaryPictureInfo中的图片尺寸。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AuxiliaryPictureInfo](capi-image-nativemodule-oh-auxiliarypictureinfo.md) \*info | 将操作的OH\_AuxiliaryPictureInfo指针。 |
| [Image\_Size](capi-image-nativemodule-image-size.md) \*size | 将要设置的图片尺寸。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_BAD\_PARAMETER：参数错误。 |

### OH\_AuxiliaryPictureInfo\_GetRowStride()

```c
Image_ErrorCode OH_AuxiliaryPictureInfo_GetRowStride(OH_AuxiliaryPictureInfo *info, uint32_t *rowStride)
```

**描述**

获取OH\_AuxiliaryPictureInfo中的行跨距。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AuxiliaryPictureInfo](capi-image-nativemodule-oh-auxiliarypictureinfo.md) \*info | 将操作的OH\_AuxiliaryPictureInfo指针。 |
| uint32\_t \*rowStride | 跨距，内存中每行像素所占的空间。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_BAD\_PARAMETER：参数错误。 |

### OH\_AuxiliaryPictureInfo\_SetRowStride()

```c
Image_ErrorCode OH_AuxiliaryPictureInfo_SetRowStride(OH_AuxiliaryPictureInfo *info, uint32_t rowStride)
```

**描述**

设置OH\_AuxiliaryPictureInfo中的行跨距。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AuxiliaryPictureInfo](capi-image-nativemodule-oh-auxiliarypictureinfo.md) \*info | 将操作的OH\_AuxiliaryPictureInfo指针。 |
| uint32\_t rowStride | 跨距，内存中每行像素所占的空间。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_BAD\_PARAMETER：参数错误。 |

### OH\_AuxiliaryPictureInfo\_GetPixelFormat()

```c
Image_ErrorCode OH_AuxiliaryPictureInfo_GetPixelFormat(OH_AuxiliaryPictureInfo *info, PIXEL_FORMAT *pixelFormat)
```

**描述**

获取OH\_AuxiliaryPictureInfo中的像素格式。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AuxiliaryPictureInfo](capi-image-nativemodule-oh-auxiliarypictureinfo.md) \*info | 将操作的OH\_AuxiliaryPictureInfo指针。 |
| [PIXEL\_FORMAT](capi-pixelmap-native-h.md#pixel_format) \*pixelFormat | 获取的像素格式。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_BAD\_PARAMETER：参数错误。 |

### OH\_AuxiliaryPictureInfo\_SetPixelFormat()

```c
Image_ErrorCode OH_AuxiliaryPictureInfo_SetPixelFormat(OH_AuxiliaryPictureInfo *info, PIXEL_FORMAT pixelFormat)
```

**描述**

设置OH\_AuxiliaryPictureInfo中的像素格式。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AuxiliaryPictureInfo](capi-image-nativemodule-oh-auxiliarypictureinfo.md) \*info | 将操作的OH\_AuxiliaryPictureInfo指针。 |
| [PIXEL\_FORMAT](capi-pixelmap-native-h.md#pixel_format) pixelFormat | 将要设置的像素格式。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_BAD\_PARAMETER：参数错误。 |

### OH\_AuxiliaryPictureInfo\_Release()

```c
Image_ErrorCode OH_AuxiliaryPictureInfo_Release(OH_AuxiliaryPictureInfo *info)
```

**描述**

释放OH\_AuxiliaryPictureInfo指针。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AuxiliaryPictureInfo](capi-image-nativemodule-oh-auxiliarypictureinfo.md) \*info | 将操作的OH\_AuxiliaryPictureInfo指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_BAD\_PARAMETER：参数错误。 |
