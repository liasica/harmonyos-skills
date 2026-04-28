---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-pixelmap-native-h
title: pixelmap_native.h
breadcrumb: API参考 > 媒体 > Image Kit（图片处理服务） > C API > 头文件 > pixelmap_native.h
category: harmonyos-references
scraped_at: 2026-04-28T08:13:19+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:00eec5ae73b0aaa7eb36abb6b5308ad53093253a0524f7111aeabcfadc630348
---

## 概述

PhonePC/2in1TabletTVWearable

访问Pixelmap的API。

**引用文件：** <multimedia/image\_framework/image/pixelmap\_native.h>

**库：** libpixelmap.so

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 12

**相关模块：** [Image\_NativeModule](capi-image-nativemodule.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 结构体

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [OH\_Pixelmap\_HdrStaticMetadata](i-image-nativemodule-oh-pixelmap-hdrstaticmetadata.md) | OH\_Pixelmap\_HdrStaticMetadata | HDR\_STATIC\_METADATA关键字对应的静态元数据值。 |
| [OH\_Pixelmap\_HdrDynamicMetadata](-image-nativemodule-oh-pixelmap-hdrdynamicmetadata.md) | OH\_Pixelmap\_HdrDynamicMetadata | HDR\_DYNAMIC\_METADATA关键字对应的动态元数据值。 |
| [OH\_Pixelmap\_HdrGainmapMetadata](-image-nativemodule-oh-pixelmap-hdrgainmapmetadata.md) | OH\_Pixelmap\_HdrGainmapMetadata | HDR\_GAINMAP\_METADATA关键字对应的gainmap相关元数据值，参考ISO 21496-1。 |
| [OH\_Pixelmap\_HdrMetadataValue](pi-image-nativemodule-oh-pixelmap-hdrmetadatavalue.md) | OH\_Pixelmap\_HdrMetadataValue | Pixelmap使用的HDR元数据值，和OH\_Pixelmap\_HdrMetadataKey关键字相对应。用于[OH\_PixelmapNative\_SetMetadata](capi-pixelmap-native-h.md#oh_pixelmapnative_setmetadata)及[OH\_PixelmapNative\_GetMetadata](capi-pixelmap-native-h.md#oh_pixelmapnative_getmetadata)，有相应[OH\_Pixelmap\_HdrMetadataKey](capi-pixelmap-native-h.md#oh_pixelmap_hdrmetadatakey)关键字作为入参时，设置或获取到本结构体中相对应的元数据类型的值。 |
| [OH\_PixelmapNative](capi-image-nativemodule-oh-pixelmapnative.md) | - | OH\_PixelmapNative结构体是native层封装的图像解码后无压缩的位图格式结构体。  函数创建OH\_PixelmapNative使用[OH\_PixelmapNative\_CreatePixelmap](capi-pixelmap-native-h.md#oh_pixelmapnative_createpixelmap)函数，默认采用BGRA\_8888格式处理数据。  释放OH\_PixelmapNative对象使用[OH\_PixelmapNative\_Release](capi-pixelmap-native-h.md#oh_pixelmapnative_release)函数。 |
| [OH\_NativeBuffer](ge-nativemodule-image-nativemodule-oh-nativebuffer.md) | - | NativeBuffer结构体类型，用于执行NativeBuffer相关操作。 |
| [OH\_NativeColorSpaceManager](capi-image-nativemodule-oh-nativecolorspacemanager.md) | OH\_NativeColorSpaceManager | NativeColorSpaceManager结构体类型，用于执行NativeColorSpaceManager相关操作。 |
| [OH\_Pixelmap\_InitializationOptions](age-nativemodule-oh-pixelmap-initializationoptions.md) | - | OH\_Pixelmap\_InitializationOptions是native层封装的初始化参数结构体，用于设置Pixelmap的初始化参数。  创建OH\_Pixelmap\_InitializationOptions对象使用[OH\_PixelmapInitializationOptions\_Create](capi-pixelmap-native-h.md#oh_pixelmapinitializationoptions_create)函数。  释放OH\_Pixelmap\_InitializationOptions对象使用[OH\_PixelmapInitializationOptions\_Release](capi-pixelmap-native-h.md#oh_pixelmapinitializationoptions_release)函数。 |
| [OH\_Pixelmap\_ImageInfo](capi-image-nativemodule-oh-pixelmap-imageinfo.md) | - | 图像像素信息结构体。 |

### 枚举

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [PIXELMAP\_ALPHA\_TYPE](capi-pixelmap-native-h.md#pixelmap_alpha_type) | PIXELMAP\_ALPHA\_TYPE | Pixelmap透明度类型。 |
| [PIXEL\_FORMAT](capi-pixelmap-native-h.md#pixel_format) | PIXEL\_FORMAT | 图片像素格式。 |
| [OH\_PixelmapNative\_AntiAliasingLevel](capi-pixelmap-native-h.md#oh_pixelmapnative_antialiasinglevel) | OH\_PixelmapNative\_AntiAliasingLevel | Pixelmap缩放时采用的缩放算法。 |
| [OH\_Pixelmap\_HdrMetadataKey](capi-pixelmap-native-h.md#oh_pixelmap_hdrmetadatakey) | OH\_Pixelmap\_HdrMetadataKey | Pixelmap使用的HDR相关元数据信息的关键字，用于[OH\_PixelmapNative\_SetMetadata](capi-pixelmap-native-h.md#oh_pixelmapnative_setmetadata)及[OH\_PixelmapNative\_GetMetadata](capi-pixelmap-native-h.md#oh_pixelmapnative_getmetadata)。 |
| [OH\_Pixelmap\_HdrMetadataType](capi-pixelmap-native-h.md#oh_pixelmap_hdrmetadatatype) | OH\_Pixelmap\_HdrMetadataType | HDR\_METADATA\_TYPE关键字对应的值。 |

### 函数

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [Image\_ErrorCode OH\_PixelmapInitializationOptions\_Create(OH\_Pixelmap\_InitializationOptions \*\*options)](capi-pixelmap-native-h.md#oh_pixelmapinitializationoptions_create) | 创建OH\_Pixelmap\_InitializationOptions指针。 |
| [Image\_ErrorCode OH\_PixelmapInitializationOptions\_GetWidth(OH\_Pixelmap\_InitializationOptions \*options, uint32\_t \*width)](capi-pixelmap-native-h.md#oh_pixelmapinitializationoptions_getwidth) | 获取图片宽。 |
| [Image\_ErrorCode OH\_PixelmapInitializationOptions\_SetWidth(OH\_Pixelmap\_InitializationOptions \*options, uint32\_t width)](capi-pixelmap-native-h.md#oh_pixelmapinitializationoptions_setwidth) | 设置图片宽。 |
| [Image\_ErrorCode OH\_PixelmapInitializationOptions\_GetHeight(OH\_Pixelmap\_InitializationOptions \*options, uint32\_t \*height)](capi-pixelmap-native-h.md#oh_pixelmapinitializationoptions_getheight) | 获取图片高。 |
| [Image\_ErrorCode OH\_PixelmapInitializationOptions\_SetHeight(OH\_Pixelmap\_InitializationOptions \*options, uint32\_t height)](capi-pixelmap-native-h.md#oh_pixelmapinitializationoptions_setheight) | 设置图片高。 |
| [Image\_ErrorCode OH\_PixelmapInitializationOptions\_GetPixelFormat(OH\_Pixelmap\_InitializationOptions \*options, int32\_t \*pixelFormat)](capi-pixelmap-native-h.md#oh_pixelmapinitializationoptions_getpixelformat) | 获取像素格式。 |
| [Image\_ErrorCode OH\_PixelmapInitializationOptions\_SetPixelFormat(OH\_Pixelmap\_InitializationOptions \*options, int32\_t pixelFormat)](capi-pixelmap-native-h.md#oh_pixelmapinitializationoptions_setpixelformat) | 设置像素格式。 |
| [Image\_ErrorCode OH\_PixelmapInitializationOptions\_GetSrcPixelFormat(OH\_Pixelmap\_InitializationOptions \*options, int32\_t \*srcpixelFormat)](capi-pixelmap-native-h.md#oh_pixelmapinitializationoptions_getsrcpixelformat) | 获取源像素格式。 |
| [Image\_ErrorCode OH\_PixelmapInitializationOptions\_SetSrcPixelFormat(OH\_Pixelmap\_InitializationOptions \*options, int32\_t srcpixelFormat)](capi-pixelmap-native-h.md#oh_pixelmapinitializationoptions_setsrcpixelformat) | 设置源像素格式。 |
| [Image\_ErrorCode OH\_PixelmapInitializationOptions\_GetRowStride(OH\_Pixelmap\_InitializationOptions \*options, int32\_t \*rowStride)](capi-pixelmap-native-h.md#oh_pixelmapinitializationoptions_getrowstride) | 获取行跨距。  跨距，图像每行占用的真实内存大小，单位为字节。跨距 = width \* 单位像素字节数 + padding，padding为每行为内存对齐做的填充区域。 |
| [Image\_ErrorCode OH\_PixelmapInitializationOptions\_SetRowStride(OH\_Pixelmap\_InitializationOptions \*options, int32\_t rowStride)](capi-pixelmap-native-h.md#oh_pixelmapinitializationoptions_setrowstride) | 设置图像跨距。  跨距，图像每行占用的真实内存大小，单位为字节。跨距 = width \* 单位像素字节数 + padding，padding为每行为内存对齐做的填充区域。 |
| [Image\_ErrorCode OH\_PixelmapInitializationOptions\_GetAlphaType(OH\_Pixelmap\_InitializationOptions \*options, int32\_t \*alphaType)](capi-pixelmap-native-h.md#oh_pixelmapinitializationoptions_getalphatype) | 获取透明度类型。 |
| [Image\_ErrorCode OH\_PixelmapInitializationOptions\_SetAlphaType(OH\_Pixelmap\_InitializationOptions \*options, int32\_t alphaType)](capi-pixelmap-native-h.md#oh_pixelmapinitializationoptions_setalphatype) | 设置透明度类型。 |
| [Image\_ErrorCode OH\_PixelmapInitializationOptions\_GetEditable(OH\_Pixelmap\_InitializationOptions \*options, bool \*editable)](capi-pixelmap-native-h.md#oh_pixelmapinitializationoptions_geteditable) | 获取可编辑标志。 |
| [Image\_ErrorCode OH\_PixelmapInitializationOptions\_SetEditable(OH\_Pixelmap\_InitializationOptions \*options, bool editable)](capi-pixelmap-native-h.md#oh_pixelmapinitializationoptions_seteditable) | 设置可编辑标志。 |
| [Image\_ErrorCode OH\_PixelmapInitializationOptions\_Release(OH\_Pixelmap\_InitializationOptions \*options)](capi-pixelmap-native-h.md#oh_pixelmapinitializationoptions_release) | 释放OH\_Pixelmap\_InitializationOptions指针。 |
| [Image\_ErrorCode OH\_PixelmapImageInfo\_Create(OH\_Pixelmap\_ImageInfo \*\*info)](capi-pixelmap-native-h.md#oh_pixelmapimageinfo_create) | 创建OH\_Pixelmap\_ImageInfo指针。 |
| [Image\_ErrorCode OH\_PixelmapImageInfo\_GetWidth(OH\_Pixelmap\_ImageInfo \*info, uint32\_t \*width)](capi-pixelmap-native-h.md#oh_pixelmapimageinfo_getwidth) | 获取图片宽。 |
| [Image\_ErrorCode OH\_PixelmapImageInfo\_GetHeight(OH\_Pixelmap\_ImageInfo \*info, uint32\_t \*height)](capi-pixelmap-native-h.md#oh_pixelmapimageinfo_getheight) | 获取图片高。 |
| [Image\_ErrorCode OH\_PixelmapImageInfo\_GetAlphaMode(OH\_Pixelmap\_ImageInfo \*info, int32\_t \*alphaMode)](capi-pixelmap-native-h.md#oh_pixelmapimageinfo_getalphamode) | 获取图片透明通道类型。 |
| [Image\_ErrorCode OH\_PixelmapImageInfo\_GetRowStride(OH\_Pixelmap\_ImageInfo \*info, uint32\_t \*rowStride)](capi-pixelmap-native-h.md#oh_pixelmapimageinfo_getrowstride) | 获取行跨距。 |
| [Image\_ErrorCode OH\_PixelmapImageInfo\_GetPixelFormat(OH\_Pixelmap\_ImageInfo \*info, int32\_t \*pixelFormat)](capi-pixelmap-native-h.md#oh_pixelmapimageinfo_getpixelformat) | 获取像素格式。 |
| [Image\_ErrorCode OH\_PixelmapImageInfo\_GetAlphaType(OH\_Pixelmap\_ImageInfo \*info, int32\_t \*alphaType)](capi-pixelmap-native-h.md#oh_pixelmapimageinfo_getalphatype) | 获取OH\_PixelmapImageInfo默认的透明通道类型。若要获取图片当前透明通道类型，请使用[OH\_PixelmapImageInfo\_GetAlphaMode](capi-pixelmap-native-h.md#oh_pixelmapimageinfo_getalphamode)。 |
| [Image\_ErrorCode OH\_PixelmapImageInfo\_GetDynamicRange(OH\_Pixelmap\_ImageInfo \*info, bool \*isHdr)](capi-pixelmap-native-h.md#oh_pixelmapimageinfo_getdynamicrange) | 获取Pixelmap是否为高动态范围的信息。 |
| [Image\_ErrorCode OH\_PixelmapImageInfo\_Release(OH\_Pixelmap\_ImageInfo \*info)](capi-pixelmap-native-h.md#oh_pixelmapimageinfo_release) | 释放OH\_Pixelmap\_ImageInfo指针。 |
| [Image\_ErrorCode OH\_PixelmapNative\_CreatePixelmap(uint8\_t \*data, size\_t dataLength, OH\_Pixelmap\_InitializationOptions \*options, OH\_PixelmapNative \*\*pixelmap)](capi-pixelmap-native-h.md#oh_pixelmapnative_createpixelmap) | 通过像素数据和图像属性创建PixelMap。传入的像素数据默认按BGRA\_8888格式解析，如果需要设置为其他格式，请参考[OH\_PixelmapInitializationOptions\_SetSrcPixelFormat](capi-pixelmap-native-h.md#oh_pixelmapinitializationoptions_setsrcpixelformat)。 |
| [Image\_ErrorCode OH\_PixelmapNative\_CreatePixelmapUsingAllocator(uint8\_t \*data, size\_t dataLength, OH\_Pixelmap\_InitializationOptions \*options, IMAGE\_ALLOCATOR\_MODE allocator, OH\_PixelmapNative \*\*pixelmap)](capi-pixelmap-native-h.md#oh_pixelmapnative_createpixelmapusingallocator) | 通过像素数据和图像属性创建PixelMap，可以通过allocator指定内存类型。传入的像素数据默认按BGRA\_8888格式解析，如果需要设置为其他格式，请参考[OH\_PixelmapInitializationOptions\_SetSrcPixelFormat](capi-pixelmap-native-h.md#oh_pixelmapinitializationoptions_setsrcpixelformat)。默认情况下，系统会根据图像类型、图像大小、平台能力等选择内存类型。在处理此接口返回的像素图时，需要考虑步长影响。 |
| [Image\_ErrorCode OH\_PixelmapNative\_ConvertPixelmapNativeToNapi(napi\_env env, OH\_PixelmapNative \*pixelmapNative, napi\_value \*pixelmapNapi)](capi-pixelmap-native-h.md#oh_pixelmapnative_convertpixelmapnativetonapi) | 将nativePixelMap对象转换为PixelMapnapi对象。 |
| [Image\_ErrorCode OH\_PixelmapNative\_ConvertPixelmapNativeFromNapi(napi\_env env, napi\_value pixelmapNapi, OH\_PixelmapNative \*\*pixelmapNative)](capi-pixelmap-native-h.md#oh_pixelmapnative_convertpixelmapnativefromnapi) | 将PixelMapnapi对象转换为nativePixelMap对象。 |
| [Image\_ErrorCode OH\_PixelmapNative\_ReadPixels(OH\_PixelmapNative \*pixelmap, uint8\_t \*destination, size\_t \*bufferSize)](capi-pixelmap-native-h.md#oh_pixelmapnative_readpixels) | 读取图像像素数据，并按照PixelMap的像素格式写入缓冲区中。 |
| [Image\_ErrorCode OH\_PixelmapNative\_WritePixels(OH\_PixelmapNative \*pixelmap, uint8\_t \*source, size\_t bufferSize)](capi-pixelmap-native-h.md#oh_pixelmapnative_writepixels) | 读取缓冲区中的图像像素数据，并按照PixelMap的像素格式将结果写入PixelMap。 |
| [Image\_ErrorCode OH\_PixelmapNative\_ReadPixelsFromArea(OH\_PixelmapNative \*pixelmap, Image\_PositionArea \*area)](capi-pixelmap-native-h.md#oh_pixelmapnative_readpixelsfromarea) | 从PixelMap的指定区域中读取像素数据并存入缓冲区。读取出来的数据为BGRA\_8888格式。 |
| [Image\_ErrorCode OH\_PixelmapNative\_WritePixelsToArea(OH\_PixelmapNative \*pixelmap, Image\_PositionArea \*area)](capi-pixelmap-native-h.md#oh_pixelmapnative_writepixelstoarea) | 将缓冲区中的像素数据写入PixelMap的指定区域。数据源应为BGRA\_8888格式。 |
| [Image\_ErrorCode OH\_PixelmapNative\_GetArgbPixels(OH\_PixelmapNative \*pixelmap, uint8\_t \*destination, size\_t \*bufferSize)](capi-pixelmap-native-h.md#oh_pixelmapnative_getargbpixels) | 从PixelMap中读取ARGB格式的数据。 |
| [Image\_ErrorCode OH\_PixelmapNative\_ToSdr(OH\_PixelmapNative \*pixelmap)](capi-pixelmap-native-h.md#oh_pixelmapnative_tosdr) | 将HDR的图像内容转换为SDR的图像内容。 |
| [Image\_ErrorCode OH\_PixelmapNative\_GetImageInfo(OH\_PixelmapNative \*pixelmap, OH\_Pixelmap\_ImageInfo \*imageInfo)](capi-pixelmap-native-h.md#oh_pixelmapnative_getimageinfo) | 获取图像像素信息。 |
| [Image\_ErrorCode OH\_PixelmapNative\_Opacity(OH\_PixelmapNative \*pixelmap, float rate)](capi-pixelmap-native-h.md#oh_pixelmapnative_opacity) | 通过设置透明比率来让PixelMap达到对应的透明效果。 |
| [Image\_ErrorCode OH\_PixelmapNative\_Scale(OH\_PixelmapNative \*pixelmap, float scaleX, float scaleY)](capi-pixelmap-native-h.md#oh_pixelmapnative_scale) | 根据输入的宽高对图片进行缩放。 |
| [Image\_ErrorCode OH\_PixelmapNative\_ScaleWithAntiAliasing(OH\_PixelmapNative \*pixelmap, float scaleX, float scaleY, OH\_PixelmapNative\_AntiAliasingLevel level)](capi-pixelmap-native-h.md#oh_pixelmapnative_scalewithantialiasing) | 根据指定的缩放算法和输入的宽高对图片进行缩放。 |
| [Image\_ErrorCode OH\_PixelmapNative\_CreateScaledPixelMap(OH\_PixelmapNative \*srcPixelmap, OH\_PixelmapNative \*\*dstPixelmap, float scaleX, float scaleY)](capi-pixelmap-native-h.md#oh_pixelmapnative_createscaledpixelmap) | 根据输入的宽高的缩放比例，创建一个新的缩放后的图片，生成的新PixelMap不可编辑。 |
| [Image\_ErrorCode OH\_PixelmapNative\_CreateScaledPixelMapWithAntiAliasing(OH\_PixelmapNative \*srcPixelmap, OH\_PixelmapNative \*\*dstPixelmap, float scaleX, float scaleY, OH\_PixelmapNative\_AntiAliasingLevel level)](capi-pixelmap-native-h.md#oh_pixelmapnative_createscaledpixelmapwithantialiasing) | 根据指定的缩放算法和输入的宽高的缩放比例，创建一个新的缩放后的图片，生成的新PixelMap不可编辑。 |
| [Image\_ErrorCode OH\_PixelmapNative\_CreateAlphaPixelmap(OH\_PixelmapNative \*srcPixelmap, OH\_PixelmapNative \*\*dstPixelmap)](capi-pixelmap-native-h.md#oh_pixelmapnative_createalphapixelmap) | 从源PixelMap创建一个仅含有Alpha通道的PixelMap，生成的新PixelMap不可编辑。 |
| [Image\_ErrorCode OH\_PixelmapNative\_Clone(OH\_PixelmapNative \*srcPixelmap, OH\_PixelmapNative \*\*dstPixelmap)](capi-pixelmap-native-h.md#oh_pixelmapnative_clone) | 从源PixelMap复制出一个新的PixelMap。 |
| [Image\_ErrorCode OH\_PixelmapNative\_CreateCroppedAndScaledPixelMap(OH\_PixelmapNative \*srcPixelmap, Image\_Region \*region, Image\_Scale \*scale, OH\_PixelmapNative\_AntiAliasingLevel level, OH\_PixelmapNative \*\*dstPixelmap)](capi-pixelmap-native-h.md#oh_pixelmapnative_createcroppedandscaledpixelmap) | 基于源PixelMap创建一个裁剪并缩放的新PixelMap。 |
| [Image\_ErrorCode OH\_PixelmapNative\_Translate(OH\_PixelmapNative \*pixelmap, float x, float y)](capi-pixelmap-native-h.md#oh_pixelmapnative_translate) | 根据输入的坐标对图片进行位置变换。 |
| [Image\_ErrorCode OH\_PixelmapNative\_Rotate(OH\_PixelmapNative \*pixelmap, float angle)](capi-pixelmap-native-h.md#oh_pixelmapnative_rotate) | 根据输入的角度对图片进行旋转。 |
| [Image\_ErrorCode OH\_PixelmapNative\_Flip(OH\_PixelmapNative \*pixelmap, bool shouldFlipHorizontally, bool shouldFlipVertically)](capi-pixelmap-native-h.md#oh_pixelmapnative_flip) | 根据输入的条件对图片进行翻转。 |
| [Image\_ErrorCode OH\_PixelmapNative\_Crop(OH\_PixelmapNative \*pixelmap, Image\_Region \*region)](capi-pixelmap-native-h.md#oh_pixelmapnative_crop) | 根据输入的尺寸对图片进行裁剪。 |
| [Image\_ErrorCode OH\_PixelmapNative\_Release(OH\_PixelmapNative \*pixelmap)](capi-pixelmap-native-h.md#oh_pixelmapnative_release) | 释放OH\_PixelmapNative指针，推荐使用[OH\_PixelmapNative\_Destroy](capi-pixelmap-native-h.md#oh_pixelmapnative_destroy)。 |
| [Image\_ErrorCode OH\_PixelmapNative\_Destroy(OH\_PixelmapNative \*\*pixelmap)](capi-pixelmap-native-h.md#oh_pixelmapnative_destroy) | 释放OH\_PixelmapNative指针。 |
| [Image\_ErrorCode OH\_PixelmapNative\_ConvertAlphaFormat(OH\_PixelmapNative\* srcpixelmap, OH\_PixelmapNative\* dstpixelmap, const bool isPremul)](capi-pixelmap-native-h.md#oh_pixelmapnative_convertalphaformat) | 将pixelmap的像素数据做预乘和非预乘之间的转换。 |
| [Image\_ErrorCode OH\_PixelmapNative\_CreateEmptyPixelmap(OH\_Pixelmap\_InitializationOptions \*options, OH\_PixelmapNative \*\*pixelmap)](capi-pixelmap-native-h.md#oh_pixelmapnative_createemptypixelmap) | 利用OH\_Pixelmap\_InitializationOptions创建空的pixelmap对象，内存数据为0。 |
| [Image\_ErrorCode OH\_PixelmapNative\_CreateEmptyPixelmapUsingAllocator(OH\_Pixelmap\_InitializationOptions \*options, IMAGE\_ALLOCATOR\_MODE allocator, OH\_PixelmapNative \*\*pixelmap)](capi-pixelmap-native-h.md#oh_pixelmapnative_createemptypixelmapusingallocator) | 根据入参options创建空的pixelmap，pixelmap使用的内存类型可以通过allocator指定。默认情况下，系统会根据图像类型、图像大小、平台能力等选择内存类型。在处理此接口返回的像素图时，需要考虑步长影响。 |
| [Image\_ErrorCode OH\_PixelmapNative\_CreatePixelmapFromSurface(const char \*surfaceId, size\_t length, OH\_PixelmapNative \*\*pixelmap)](capi-pixelmap-native-h.md#oh_pixelmapnative_createpixelmapfromsurface) | 通过Surface的Surface ID创建一个PixelMap。 |
| [Image\_ErrorCode OH\_PixelmapNative\_CreatePixelmapFromSurfaceWithTransformation(const char \*surfaceId, size\_t length, bool transformEnabled, OH\_PixelmapNative \*\*pixelmap)](capi-pixelmap-native-h.md#oh_pixelmapnative_createpixelmapfromsurfacewithtransformation) | 通过Surface的ID创建一个预览流画面的PixelMap对象。该Surface可能携带旋转或翻转的变换信息。 |
| [Image\_ErrorCode OH\_PixelmapNative\_CreatePixelmapFromNativeBuffer(OH\_NativeBuffer \*nativeBuffer, OH\_PixelmapNative \*\*pixelmap)](capi-pixelmap-native-h.md#oh_pixelmapnative_createpixelmapfromnativebuffer) | 通过NativeBuffer创建一个PixelMap。如果NativeBuffer的用途未配置[CPU访问权限](capi-native-buffer-h.md#oh_nativebuffer_usage)，则不支持创建。  支持创建的像素格式为RGBA\_8888、NV21、NV12、YCBCR\_P010、YCRCB\_P010。 |
| [Image\_ErrorCode OH\_PixelmapNative\_GetNativeBuffer(OH\_PixelmapNative \*pixelmap, OH\_NativeBuffer \*\*nativeBuffer)](capi-pixelmap-native-h.md#oh_pixelmapnative_getnativebuffer) | 从DMA内存的PixelMap中，获取NativeBuffer对象。 |
| [Image\_ErrorCode OH\_PixelmapNative\_GetMetadata(OH\_PixelmapNative \*pixelmap, OH\_Pixelmap\_HdrMetadataKey key, OH\_Pixelmap\_HdrMetadataValue \*\*value)](capi-pixelmap-native-h.md#oh_pixelmapnative_getmetadata) | 获取元数据。 |
| [Image\_ErrorCode OH\_PixelmapNative\_SetMetadata(OH\_PixelmapNative \*pixelmap, OH\_Pixelmap\_HdrMetadataKey key, OH\_Pixelmap\_HdrMetadataValue \*value)](capi-pixelmap-native-h.md#oh_pixelmapnative_setmetadata) | 设置元数据。 |
| [Image\_ErrorCode OH\_PixelmapNative\_SetColorSpaceNative(OH\_PixelmapNative \*pixelmap, OH\_NativeColorSpaceManager \*colorSpaceNative)](capi-pixelmap-native-h.md#oh_pixelmapnative_setcolorspacenative) | 设置NativeColorSpaceManager对象。 |
| [Image\_ErrorCode OH\_PixelmapNative\_GetColorSpaceNative(OH\_PixelmapNative \*pixelmap, OH\_NativeColorSpaceManager \*\*colorSpaceNative)](capi-pixelmap-native-h.md#oh_pixelmapnative_getcolorspacenative) | 获取NativeColorSpaceManager对象。 |
| [Image\_ErrorCode OH\_PixelmapNative\_SetMemoryName(OH\_PixelmapNative \*pixelmap, char \*name, size\_t \*size)](capi-pixelmap-native-h.md#oh_pixelmapnative_setmemoryname) | 设置pixelMap内存名字。 |
| [Image\_ErrorCode OH\_PixelmapNative\_GetByteCount(OH\_PixelmapNative \*pixelmap, uint32\_t \*byteCount)](capi-pixelmap-native-h.md#oh_pixelmapnative_getbytecount) | 获取Pixelmap中所有像素所占用的总字节数，不包含内存填充。 |
| [Image\_ErrorCode OH\_PixelmapNative\_GetAllocationByteCount(OH\_PixelmapNative \*pixelmap, uint32\_t \*allocationByteCount)](capi-pixelmap-native-h.md#oh_pixelmapnative_getallocationbytecount) | 获取Pixelmap用于储存像素数据的内存字节数。 |
| [Image\_ErrorCode OH\_PixelmapNative\_AccessPixels(OH\_PixelmapNative \*pixelmap, void \*\*addr)](capi-pixelmap-native-h.md#oh_pixelmapnative_accesspixels) | 获取Pixelmap像素数据的内存地址，并锁定这块内存。  当该内存被锁定时，任何修改或释放该Pixelmap的像素数据的操作均会失败或无效。 |
| [Image\_ErrorCode OH\_PixelmapNative\_UnaccessPixels(OH\_PixelmapNative \*pixelmap)](capi-pixelmap-native-h.md#oh_pixelmapnative_unaccesspixels) | 释放Pixelmap像素数据的内存锁。  该函数需要与[OH\_PixelmapNative\_AccessPixels](capi-pixelmap-native-h.md#oh_pixelmapnative_accesspixels)匹配使用。 |
| [Image\_ErrorCode OH\_PixelmapNative\_GetUniqueId(OH\_PixelmapNative \*pixelmap, uint32\_t \*uniqueId)](capi-pixelmap-native-h.md#oh_pixelmapnative_getuniqueid) | 获取PixelMap的唯一ID。 |
| [Image\_ErrorCode OH\_PixelmapNative\_IsReleased(OH\_PixelmapNative \*pixelmap, bool \*released)](capi-pixelmap-native-h.md#oh_pixelmapnative_isreleased) | 检测PixelMap是否已被释放。如果已被释放，则任何访问该对象内部数据的方法调用将会失效。 |

## 枚举类型说明

PhonePC/2in1TabletTVWearable

### PIXELMAP\_ALPHA\_TYPE

PhonePC/2in1TabletTVWearable

```
1. enum PIXELMAP_ALPHA_TYPE
```

**描述**

Pixelmap透明度类型。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| PIXELMAP\_ALPHA\_TYPE\_UNKNOWN = 0 | 未知格式。 |
| PIXELMAP\_ALPHA\_TYPE\_OPAQUE = 1 | 不透明的格式。 |
| PIXELMAP\_ALPHA\_TYPE\_PREMULTIPLIED = 2 | 预乘透明度格式。 |
| PIXELMAP\_ALPHA\_TYPE\_UNPREMULTIPLIED = 3 | 非预乘透明度格式。 |

### PIXEL\_FORMAT

PhonePC/2in1TabletTVWearable

```
1. enum PIXEL_FORMAT
```

**描述**

图片像素格式。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| PIXEL\_FORMAT\_UNKNOWN = 0 | 未知格式。 |
| PIXEL\_FORMAT\_RGB\_565 = 2 | RGB\_565格式。 |
| PIXEL\_FORMAT\_RGBA\_8888 = 3 | RGBA\_8888格式。 |
| PIXEL\_FORMAT\_BGRA\_8888 = 4 | BGRA\_8888格式。 |
| PIXEL\_FORMAT\_RGB\_888 = 5 | RGB\_888格式。 |
| PIXEL\_FORMAT\_ALPHA\_8 = 6 | ALPHA\_8格式。 |
| PIXEL\_FORMAT\_RGBA\_F16 = 7 | RGBA\_F16格式。 |
| PIXEL\_FORMAT\_NV21 = 8 | NV21格式。 |
| PIXEL\_FORMAT\_NV12 = 9 | NV12格式。 |
| PIXEL\_FORMAT\_RGBA\_1010102 = 10 | RGBA\_1010102格式。 |
| PIXEL\_FORMAT\_YCBCR\_P010 = 11 | YCBCR\_P010格式。 |
| PIXEL\_FORMAT\_YCRCB\_P010 = 12 | YCRCB\_P010格式。 |

### OH\_PixelmapNative\_AntiAliasingLevel

PhonePC/2in1TabletTVWearable

```
1. enum OH_PixelmapNative_AntiAliasingLevel
```

**描述**

Pixelmap缩放时采用的缩放算法。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| OH\_PixelmapNative\_AntiAliasing\_NONE = 0 | 最近邻插值算法。 |
| OH\_PixelmapNative\_AntiAliasing\_LOW = 1 | 双线性插值算法。 |
| OH\_PixelmapNative\_AntiAliasing\_MEDIUM = 2 | 双线性插值算法，同时开启Mipmap。缩小图片时建议使用。 |
| OH\_PixelmapNative\_AntiAliasing\_HIGH = 3 | 三次插值算法。 |

### OH\_Pixelmap\_HdrMetadataKey

PhonePC/2in1TabletTVWearable

```
1. enum OH_Pixelmap_HdrMetadataKey
```

**描述**

Pixelmap使用的HDR相关元数据信息的关键字，用于[OH\_PixelmapNative\_SetMetadata](capi-pixelmap-native-h.md#oh_pixelmapnative_setmetadata)及[OH\_PixelmapNative\_GetMetadata](capi-pixelmap-native-h.md#oh_pixelmapnative_getmetadata)。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| HDR\_METADATA\_TYPE = 0 | Pixelmap使用的元数据类型。 |
| HDR\_STATIC\_METADATA = 1 | 静态元数据。 |
| HDR\_DYNAMIC\_METADATA = 2 | 动态元数据。 |
| HDR\_GAINMAP\_METADATA = 3 | Gainmap使用的元数据。 |

### OH\_Pixelmap\_HdrMetadataType

PhonePC/2in1TabletTVWearable

```
1. enum OH_Pixelmap_HdrMetadataType
```

**描述**

HDR\_METADATA\_TYPE关键字对应的值。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| HDR\_METADATA\_TYPE\_NONE = 0 | 无元数据内容。 |
| HDR\_METADATA\_TYPE\_BASE = 1 | 表示用于基础图的元数据。 |
| HDR\_METADATA\_TYPE\_GAINMAP = 2 | 表示用于Gainmap图的元数据。 |
| HDR\_METADATA\_TYPE\_ALTERNATE = 3 | 表示用于合成后HDR图的元数据。 |

## 函数说明

PhonePC/2in1TabletTVWearable

### OH\_PixelmapInitializationOptions\_Create()

PhonePC/2in1TabletTVWearable

```
1. Image_ErrorCode OH_PixelmapInitializationOptions_Create(OH_Pixelmap_InitializationOptions **options)
```

**描述**

创建OH\_Pixelmap\_InitializationOptions指针。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Pixelmap\_InitializationOptions](age-nativemodule-oh-pixelmap-initializationoptions.md) \*\*options | 被创建的OH\_Pixelmap\_InitializationOptions指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_BAD\_PARAMETER：参数错误。 |

### OH\_PixelmapInitializationOptions\_GetWidth()

PhonePC/2in1TabletTVWearable

```
1. Image_ErrorCode OH_PixelmapInitializationOptions_GetWidth(OH_Pixelmap_InitializationOptions *options, uint32_t *width)
```

**描述**

获取图片宽。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Pixelmap\_InitializationOptions](age-nativemodule-oh-pixelmap-initializationoptions.md) \*options | 被操作的OH\_Pixelmap\_InitializationOptions指针。 |
| uint32\_t \*width | 图片的宽，单位：像素。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_BAD\_PARAMETER：参数错误。 |

### OH\_PixelmapInitializationOptions\_SetWidth()

PhonePC/2in1TabletTVWearable

```
1. Image_ErrorCode OH_PixelmapInitializationOptions_SetWidth(OH_Pixelmap_InitializationOptions *options, uint32_t width)
```

**描述**

设置图片宽。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Pixelmap\_InitializationOptions](age-nativemodule-oh-pixelmap-initializationoptions.md) \*options | 被操作的OH\_Pixelmap\_InitializationOptions指针。 |
| uint32\_t width | 图片的宽，单位：像素。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_BAD\_PARAMETER：参数错误。 |

### OH\_PixelmapInitializationOptions\_GetHeight()

PhonePC/2in1TabletTVWearable

```
1. Image_ErrorCode OH_PixelmapInitializationOptions_GetHeight(OH_Pixelmap_InitializationOptions *options, uint32_t *height)
```

**描述**

获取图片高。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Pixelmap\_InitializationOptions](age-nativemodule-oh-pixelmap-initializationoptions.md) \*options | 被操作的OH\_Pixelmap\_InitializationOptions指针。 |
| uint32\_t \*height | 图片的高，单位：像素。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_BAD\_PARAMETER：参数错误。 |

### OH\_PixelmapInitializationOptions\_SetHeight()

PhonePC/2in1TabletTVWearable

```
1. Image_ErrorCode OH_PixelmapInitializationOptions_SetHeight(OH_Pixelmap_InitializationOptions *options, uint32_t height)
```

**描述**

设置图片高。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Pixelmap\_InitializationOptions](age-nativemodule-oh-pixelmap-initializationoptions.md) \*options | 被操作的OH\_Pixelmap\_InitializationOptions指针。 |
| uint32\_t height | 图片的高，单位：像素。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_BAD\_PARAMETER：参数错误。 |

### OH\_PixelmapInitializationOptions\_GetPixelFormat()

PhonePC/2in1TabletTVWearable

```
1. Image_ErrorCode OH_PixelmapInitializationOptions_GetPixelFormat(OH_Pixelmap_InitializationOptions *options, int32_t *pixelFormat)
```

**描述**

获取像素格式。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Pixelmap\_InitializationOptions](age-nativemodule-oh-pixelmap-initializationoptions.md) \*options | 被操作的OH\_Pixelmap\_InitializationOptions指针。 |
| int32\_t \*pixelFormat | 像素格式[PIXEL\_FORMAT](capi-pixelmap-native-h.md#pixel_format)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_BAD\_PARAMETER：参数错误。 |

### OH\_PixelmapInitializationOptions\_SetPixelFormat()

PhonePC/2in1TabletTVWearable

```
1. Image_ErrorCode OH_PixelmapInitializationOptions_SetPixelFormat(OH_Pixelmap_InitializationOptions *options, int32_t pixelFormat)
```

**描述**

设置像素格式。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Pixelmap\_InitializationOptions](age-nativemodule-oh-pixelmap-initializationoptions.md) \*options | 被操作的OH\_Pixelmap\_InitializationOptions指针。 |
| int32\_t pixelFormat | 像素格式[PIXEL\_FORMAT](capi-pixelmap-native-h.md#pixel_format)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_BAD\_PARAMETER：参数错误。 |

### OH\_PixelmapInitializationOptions\_GetSrcPixelFormat()

PhonePC/2in1TabletTVWearable

```
1. Image_ErrorCode OH_PixelmapInitializationOptions_GetSrcPixelFormat(OH_Pixelmap_InitializationOptions *options, int32_t *srcpixelFormat)
```

**描述**

获取源像素格式。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Pixelmap\_InitializationOptions](age-nativemodule-oh-pixelmap-initializationoptions.md) \*options | 被操作的OH\_Pixelmap\_InitializationOptions指针。 |
| int32\_t \*srcpixelFormat | 像素格式[PIXEL\_FORMAT](capi-pixelmap-native-h.md#pixel_format)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_BAD\_PARAMETER：参数错误。 |

### OH\_PixelmapInitializationOptions\_SetSrcPixelFormat()

PhonePC/2in1TabletTVWearable

```
1. Image_ErrorCode OH_PixelmapInitializationOptions_SetSrcPixelFormat(OH_Pixelmap_InitializationOptions *options, int32_t srcpixelFormat)
```

**描述**

设置源像素格式。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Pixelmap\_InitializationOptions](age-nativemodule-oh-pixelmap-initializationoptions.md) \*options | 被操作的OH\_Pixelmap\_InitializationOptions指针。 |
| int32\_t srcpixelFormat | 源像素格式[PIXEL\_FORMAT](capi-pixelmap-native-h.md#pixel_format)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_BAD\_PARAMETER：参数错误。 |

### OH\_PixelmapInitializationOptions\_GetRowStride()

PhonePC/2in1TabletTVWearable

```
1. Image_ErrorCode OH_PixelmapInitializationOptions_GetRowStride(OH_Pixelmap_InitializationOptions *options, int32_t *rowStride)
```

**描述**

获取行跨距。

跨距，图像每行占用的真实内存大小，单位为字节。跨距 = width \* 单位像素字节数 + padding，padding为每行为内存对齐做的填充区域。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Pixelmap\_InitializationOptions](age-nativemodule-oh-pixelmap-initializationoptions.md) \*options | 被操作的OH\_Pixelmap\_InitializationOptions指针。 |
| int32\_t \*rowStride | 跨距，单位：字节。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_BAD\_PARAMETER：参数错误。  IMAGE\_UNKNOWN\_ERROR：options被释放。 |

### OH\_PixelmapInitializationOptions\_SetRowStride()

PhonePC/2in1TabletTVWearable

```
1. Image_ErrorCode OH_PixelmapInitializationOptions_SetRowStride(OH_Pixelmap_InitializationOptions *options, int32_t rowStride)
```

**描述**

设置图像跨距。

跨距，图像每行占用的真实内存大小，单位为字节。跨距 = width \* 单位像素字节数 + padding，padding为每行为内存对齐做的填充区域。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Pixelmap\_InitializationOptions](age-nativemodule-oh-pixelmap-initializationoptions.md) \*options | 被操作的OH\_Pixelmap\_InitializationOptions指针。 |
| int32\_t rowStride | 跨距，单位：字节。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_BAD\_PARAMETER：参数错误。  IMAGE\_UNKNOWN\_ERROR：options被释放。 |

### OH\_PixelmapInitializationOptions\_GetAlphaType()

PhonePC/2in1TabletTVWearable

```
1. Image_ErrorCode OH_PixelmapInitializationOptions_GetAlphaType(OH_Pixelmap_InitializationOptions *options, int32_t *alphaType)
```

**描述**

获取透明度类型。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Pixelmap\_InitializationOptions](age-nativemodule-oh-pixelmap-initializationoptions.md) \*options | 被操作的OH\_Pixelmap\_InitializationOptions指针。 |
| int32\_t \*alphaType | 透明度类型[PIXELMAP\_ALPHA\_TYPE](capi-pixelmap-native-h.md#pixelmap_alpha_type)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_BAD\_PARAMETER：参数错误。 |

### OH\_PixelmapInitializationOptions\_SetAlphaType()

PhonePC/2in1TabletTVWearable

```
1. Image_ErrorCode OH_PixelmapInitializationOptions_SetAlphaType(OH_Pixelmap_InitializationOptions *options, int32_t alphaType)
```

**描述**

设置透明度类型。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Pixelmap\_InitializationOptions](age-nativemodule-oh-pixelmap-initializationoptions.md) \*options | 被操作的OH\_Pixelmap\_InitializationOptions指针。 |
| int32\_t alphaType | 透明度类型[PIXELMAP\_ALPHA\_TYPE](capi-pixelmap-native-h.md#pixelmap_alpha_type)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_BAD\_PARAMETER：参数错误。 |

### OH\_PixelmapInitializationOptions\_GetEditable()

PhonePC/2in1TabletTVWearable

```
1. Image_ErrorCode OH_PixelmapInitializationOptions_GetEditable(OH_Pixelmap_InitializationOptions *options, bool *editable)
```

**描述**

获取可编辑标志。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Pixelmap\_InitializationOptions](age-nativemodule-oh-pixelmap-initializationoptions.md) \*options | 被操作的OH\_Pixelmap\_InitializationOptions指针。 |
| bool \*editable | 可编辑标志。true表示可编辑，false表示不可编辑。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_BAD\_PARAMETER：参数错误。 |

### OH\_PixelmapInitializationOptions\_SetEditable()

PhonePC/2in1TabletTVWearable

```
1. Image_ErrorCode OH_PixelmapInitializationOptions_SetEditable(OH_Pixelmap_InitializationOptions *options, bool editable)
```

**描述**

设置可编辑标志。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Pixelmap\_InitializationOptions](age-nativemodule-oh-pixelmap-initializationoptions.md) \*options | 被操作的OH\_Pixelmap\_InitializationOptions指针。 |
| bool editable | 可编辑标志。true表示可编辑，false表示不可编辑。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_BAD\_PARAMETER：参数错误。 |

### OH\_PixelmapInitializationOptions\_Release()

PhonePC/2in1TabletTVWearable

```
1. Image_ErrorCode OH_PixelmapInitializationOptions_Release(OH_Pixelmap_InitializationOptions *options)
```

**描述**

释放OH\_Pixelmap\_InitializationOptions指针。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Pixelmap\_InitializationOptions](age-nativemodule-oh-pixelmap-initializationoptions.md) \*options | 被释放的OH\_Pixelmap\_InitializationOptions指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_BAD\_PARAMETER：参数错误。 |

### OH\_PixelmapImageInfo\_Create()

PhonePC/2in1TabletTVWearable

```
1. Image_ErrorCode OH_PixelmapImageInfo_Create(OH_Pixelmap_ImageInfo **info)
```

**描述**

创建OH\_Pixelmap\_ImageInfo指针。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Pixelmap\_ImageInfo](capi-image-nativemodule-oh-pixelmap-imageinfo.md) \*\*info | 被创建的OH\_Pixelmap\_ImageInfo指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_BAD\_PARAMETER：参数错误。 |

### OH\_PixelmapImageInfo\_GetWidth()

PhonePC/2in1TabletTVWearable

```
1. Image_ErrorCode OH_PixelmapImageInfo_GetWidth(OH_Pixelmap_ImageInfo *info, uint32_t *width)
```

**描述**

获取图片宽。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Pixelmap\_ImageInfo](capi-image-nativemodule-oh-pixelmap-imageinfo.md) \*info | 被操作的OH\_Pixelmap\_ImageInfo指针。 |
| uint32\_t \*width | 图片宽，单位：像素。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_BAD\_PARAMETER：参数错误。 |

### OH\_PixelmapImageInfo\_GetHeight()

PhonePC/2in1TabletTVWearable

```
1. Image_ErrorCode OH_PixelmapImageInfo_GetHeight(OH_Pixelmap_ImageInfo *info, uint32_t *height)
```

**描述**

获取图片高。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Pixelmap\_ImageInfo](capi-image-nativemodule-oh-pixelmap-imageinfo.md) \*info | 被操作的OH\_Pixelmap\_ImageInfo指针。 |
| uint32\_t \*height | 图片高，单位：像素。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_BAD\_PARAMETER：参数错误。 |

### OH\_PixelmapImageInfo\_GetAlphaMode()

PhonePC/2in1TabletTVWearable

```
1. Image_ErrorCode OH_PixelmapImageInfo_GetAlphaMode(OH_Pixelmap_ImageInfo *info, int32_t *alphaMode)
```

**描述**

获取图片透明通道类型。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Pixelmap\_ImageInfo](capi-image-nativemodule-oh-pixelmap-imageinfo.md) \*info | 被操作的OH\_Pixelmap\_ImageInfo指针。 |
| int32\_t \*AlphaMode | 被操作的alpha格式的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_BAD\_PARAMETER：参数错误。 |

### OH\_PixelmapImageInfo\_GetRowStride()

PhonePC/2in1TabletTVWearable

```
1. Image_ErrorCode OH_PixelmapImageInfo_GetRowStride(OH_Pixelmap_ImageInfo *info, uint32_t *rowStride)
```

**描述**

获取行跨距。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Pixelmap\_ImageInfo](capi-image-nativemodule-oh-pixelmap-imageinfo.md) \*info | 被操作的OH\_Pixelmap\_ImageInfo指针。 |
| uint32\_t \*rowStride | 跨距，内存中每行像素所占的空间。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_BAD\_PARAMETER：参数错误。 |

### OH\_PixelmapImageInfo\_GetPixelFormat()

PhonePC/2in1TabletTVWearable

```
1. Image_ErrorCode OH_PixelmapImageInfo_GetPixelFormat(OH_Pixelmap_ImageInfo *info, int32_t *pixelFormat)
```

**描述**

获取像素格式。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Pixelmap\_ImageInfo](capi-image-nativemodule-oh-pixelmap-imageinfo.md) \*info | 被操作的OH\_Pixelmap\_ImageInfo指针。 |
| int32\_t \*pixelFormat | 像素格式[PIXEL\_FORMAT](capi-pixelmap-native-h.md#pixel_format)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_BAD\_PARAMETER：参数错误。 |

### OH\_PixelmapImageInfo\_GetAlphaType()

PhonePC/2in1TabletTVWearable

```
1. Image_ErrorCode OH_PixelmapImageInfo_GetAlphaType(OH_Pixelmap_ImageInfo *info, int32_t *alphaType)
```

**描述**

获取OH\_PixelmapImageInfo默认的透明通道类型。若要获取图片当前透明通道类型，请使用[OH\_PixelmapImageInfo\_GetAlphaMode](capi-pixelmap-native-h.md#oh_pixelmapimageinfo_getalphamode)。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Pixelmap\_ImageInfo](capi-image-nativemodule-oh-pixelmap-imageinfo.md) \*info | 被操作的OH\_Pixelmap\_ImageInfo指针。 |
| int32\_t \*alphaType | 透明度类型[PIXELMAP\_ALPHA\_TYPE](capi-pixelmap-native-h.md#pixelmap_alpha_type)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_BAD\_PARAMETER：参数错误。 |

### OH\_PixelmapImageInfo\_GetDynamicRange()

PhonePC/2in1TabletTVWearable

```
1. Image_ErrorCode OH_PixelmapImageInfo_GetDynamicRange(OH_Pixelmap_ImageInfo *info, bool *isHdr)
```

**描述**

获取Pixelmap是否为高动态范围的信息。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Pixelmap\_ImageInfo](capi-image-nativemodule-oh-pixelmap-imageinfo.md) \*info | 被操作的OH\_Pixelmap\_ImageInfo指针。 |
| bool \*isHdr | 表示是否为高动态范围（HDR）的信息。true表示是高动态范围的信息，false表示不是高动态范围的信息。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_BAD\_PARAMETER：参数校验错误。 |

### OH\_PixelmapImageInfo\_Release()

PhonePC/2in1TabletTVWearable

```
1. Image_ErrorCode OH_PixelmapImageInfo_Release(OH_Pixelmap_ImageInfo *info)
```

**描述**

释放OH\_Pixelmap\_ImageInfo指针。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Pixelmap\_ImageInfo](capi-image-nativemodule-oh-pixelmap-imageinfo.md) \*info | 被释放的OH\_Pixelmap\_ImageInfo指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_BAD\_PARAMETER：参数错误。 |

### OH\_PixelmapNative\_CreatePixelmap()

PhonePC/2in1TabletTVWearable

```
1. Image_ErrorCode OH_PixelmapNative_CreatePixelmap(uint8_t *data, size_t dataLength, OH_Pixelmap_InitializationOptions *options, OH_PixelmapNative **pixelmap)
```

**描述**

通过像素数据和图像属性创建PixelMap。传入的像素数据默认按BGRA\_8888格式解析，如果需要设置为其他格式，请参考[OH\_PixelmapInitializationOptions\_SetSrcPixelFormat](capi-pixelmap-native-h.md#oh_pixelmapinitializationoptions_setsrcpixelformat)。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| uint8\_t \*data | BGRA\_8888格式的颜色数组。 |
| size\_t dataLength | 数组长度。 |
| [OH\_Pixelmap\_InitializationOptions](age-nativemodule-oh-pixelmap-initializationoptions.md) \*options | 创建像素的属性。 |
| [OH\_PixelmapNative](capi-image-nativemodule-oh-pixelmapnative.md) \*\*pixelmap | 被创建的OH\_PixelmapNative对象指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_BAD\_PARAMETER：参数错误。  IMAGE\_UNSUPPORTED\_OPERATION：操作不支持。 |

### OH\_PixelmapNative\_CreatePixelmapUsingAllocator()

PhonePC/2in1TabletTVWearable

```
1. Image_ErrorCode OH_PixelmapNative_CreatePixelmapUsingAllocator(uint8_t *data, size_t dataLength, OH_Pixelmap_InitializationOptions *options, IMAGE_ALLOCATOR_MODE allocator, OH_PixelmapNative **pixelmap)
```

**描述**

通过像素数据和图像属性创建PixelMap，可以通过allocator指定内存类型。传入的像素数据默认按BGRA\_8888格式解析，如果需要设置为其他格式，请参考[OH\_PixelmapInitializationOptions\_SetSrcPixelFormat](capi-pixelmap-native-h.md#oh_pixelmapinitializationoptions_setsrcpixelformat)。默认情况下，系统会根据图像类型、图像大小、平台能力等选择内存类型。在处理此接口返回的像素图时，需要考虑步长影响。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| uint8\_t \*data | BGRA\_8888格式的数据。 |
| size\_t dataLength | 数组长度。 |
| [OH\_Pixelmap\_InitializationOptions](age-nativemodule-oh-pixelmap-initializationoptions.md) \*options | 创建pixelmap的选项。 |
| [IMAGE\_ALLOCATOR\_MODE](capi-image-common-h.md#image_allocator_mode) allocator | 决定pixelmap内存分配的类型。 |
| [OH\_PixelmapNative](capi-image-nativemodule-oh-pixelmapnative.md) \*\*pixelmap | 被创建的OH\_PixelmapNative对象指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_BAD\_PARAMETER：参数错误。  IMAGE\_UNSUPPORTED\_OPERATION：操作不支持。  IMAGE\_TOO\_LARGE：图像过大，无法分配内存。  IMAGE\_DMA\_OPERATION\_FAILED：DMA内存操作失败。  IMAGE\_ALLOCATOR\_MODE\_UNSUPPORTED：不支持分配当前内存类型。例如，使用共享内存创建HDR图。 |

### OH\_PixelmapNative\_ConvertPixelmapNativeToNapi()

PhonePC/2in1TabletTVWearable

```
1. Image_ErrorCode OH_PixelmapNative_ConvertPixelmapNativeToNapi(napi_env env, OH_PixelmapNative *pixelmapNative, napi_value *pixelmapNapi)
```

**描述**

将nativePixelMap对象转换为PixelMapnapi对象。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| napi\_env env | napi的环境指针。 |
| [OH\_PixelmapNative](capi-image-nativemodule-oh-pixelmapnative.md) \*pixelmapNative | 被操作的OH\_PixelmapNative指针。 |
| napi\_value \*pixelmapNapi | 转换出来的PixelMapnapi对象指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_BAD\_PARAMETER：pixelmapNative为空。 |

### OH\_PixelmapNative\_ConvertPixelmapNativeFromNapi()

PhonePC/2in1TabletTVWearable

```
1. Image_ErrorCode OH_PixelmapNative_ConvertPixelmapNativeFromNapi(napi_env env, napi_value pixelmapNapi, OH_PixelmapNative **pixelmapNative)
```

**描述**

将PixelMapnapi对象转换为nativePixelMap对象。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| napi\_env env | napi的环境指针。 |
| napi\_value pixelmapNapi | 需要转换的PixelMapnapi对象。 |
| [OH\_PixelmapNative](capi-image-nativemodule-oh-pixelmapnative.md) \*\*pixelmapNative | 转换出的OH\_PixelmapNative对象指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_BAD\_PARAMETER：pixelmapNative是nullptr，或者pixelmapNapi不是PixelMapNapi对象。 |

### OH\_PixelmapNative\_ReadPixels()

PhonePC/2in1TabletTVWearable

```
1. Image_ErrorCode OH_PixelmapNative_ReadPixels(OH_PixelmapNative *pixelmap, uint8_t *destination, size_t *bufferSize)
```

**描述**

读取图像像素数据，并按照PixelMap的像素格式写入缓冲区中。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_PixelmapNative](capi-image-nativemodule-oh-pixelmapnative.md) \*pixelmap | 被操作的OH\_PixelmapNative指针。 |
| uint8\_t \*destination | 缓冲区，获取的图像像素数据写入到该内存区域内。 |
| size\_t \*bufferSize | 缓冲区大小。RGBA格式的缓冲区大小等于width \* height \* 4，NV21与NV12格式的缓冲区大小等于width \* height+((width+1)/2) \* ((height+1)/2) \* 2。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_BAD\_PARAMETER：参数错误。  IMAGE\_UNKNOWN\_ERROR：未知错误。 |

### OH\_PixelmapNative\_WritePixels()

PhonePC/2in1TabletTVWearable

```
1. Image_ErrorCode OH_PixelmapNative_WritePixels(OH_PixelmapNative *pixelmap, uint8_t *source, size_t bufferSize)
```

**描述**

读取缓冲区中的图像像素数据，并按照PixelMap的像素格式将结果写入PixelMap。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_PixelmapNative](capi-image-nativemodule-oh-pixelmapnative.md) \*pixelmap | 被操作的OH\_PixelmapNative指针。 |
| uint8\_t \*source | 图像像素数据。 |
| size\_t bufferSize | 图像像素数据长度。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_BAD\_PARAMETER：参数错误。  IMAGE\_UNSUPPORTED\_OPERATION：操作不支持。  IMAGE\_UNKNOWN\_ERROR：未知错误。 |

### OH\_PixelmapNative\_ReadPixelsFromArea()

PhonePC/2in1TabletTVWearable

```
1. Image_ErrorCode OH_PixelmapNative_ReadPixelsFromArea(OH_PixelmapNative *pixelmap, Image_PositionArea *area)
```

**描述**

从PixelMap的指定区域中读取像素数据并存入缓冲区。读取出来的数据为BGRA\_8888格式。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_PixelmapNative](capi-image-nativemodule-oh-pixelmapnative.md) \*pixelmap | 被读取的PixelMap。 |
| [Image\_PositionArea](capi-image-nativemodule-image-positionarea.md) \*area | 读取数据的PixelMap指定区域。数据会被读取并拷贝至area->pixels。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：操作成功。  IMAGE\_BAD\_PARAMETER：参数无效，例如：pixelmap或area有误。  IMAGE\_UNKNOWN\_ERROR：未知的内部错误，例如：不支持的像素格式。 |

### OH\_PixelmapNative\_WritePixelsToArea()

PhonePC/2in1TabletTVWearable

```
1. Image_ErrorCode OH_PixelmapNative_WritePixelsToArea(OH_PixelmapNative *pixelmap, Image_PositionArea *area)
```

**描述**

将缓冲区中的像素数据写入PixelMap的指定区域。数据源应为BGRA\_8888格式。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_PixelmapNative](capi-image-nativemodule-oh-pixelmapnative.md) \*pixelmap | 被写入的PixelMap。 |
| [Image\_PositionArea](capi-image-nativemodule-image-positionarea.md) \*area | 写入数据的PixelMap指定区域。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：操作成功。  IMAGE\_BAD\_PARAMETER：参数无效，例如：pixelmap或area有误。  IMAGE\_UNSUPPORTED\_OPERATION：PixelMap不可编辑。  IMAGE\_UNKNOWN\_ERROR：未知的内部错误，例如：不支持的像素格式。 |

### OH\_PixelmapNative\_GetArgbPixels()

PhonePC/2in1TabletTVWearable

```
1. Image_ErrorCode OH_PixelmapNative_GetArgbPixels(OH_PixelmapNative *pixelmap, uint8_t *destination, size_t *bufferSize)
```

**描述**

从PixelMap中读取ARGB格式的数据。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_PixelmapNative](capi-image-nativemodule-oh-pixelmapnative.md) \*pixelmap | 被操作的OH\_PixelmapNative指针。 |
| uint8\_t \*destination | 缓冲区，获取的图像像素数据写入到该内存区域内。 |
| size\_t \*bufferSize | 缓冲区大小。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_BAD\_PARAMETER：参数错误。  IMAGE\_UNSUPPORTED\_CONVERSION：PixelMap格式不支持读取ARGB数据。  IMAGE\_ALLOC\_FAILED：内存申请失败。  IMAGE\_COPY\_FAILED：内存数据拷贝、读取、操作失败。 |

### OH\_PixelmapNative\_ToSdr()

PhonePC/2in1TabletTVWearable

```
1. Image_ErrorCode OH_PixelmapNative_ToSdr(OH_PixelmapNative *pixelmap)
```

**描述**

将HDR的图像内容转换为SDR的图像内容。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_PixelmapNative](capi-image-nativemodule-oh-pixelmapnative.md) \*pixelmap | 被操作的OH\_PixelmapNative指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_BAD\_PARAMETER：参数错误。  IMAGE\_UNSUPPORTED\_OPERATION：操作不支持。 |

### OH\_PixelmapNative\_GetImageInfo()

PhonePC/2in1TabletTVWearable

```
1. Image_ErrorCode OH_PixelmapNative_GetImageInfo(OH_PixelmapNative *pixelmap, OH_Pixelmap_ImageInfo *imageInfo)
```

**描述**

获取图像像素信息。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_PixelmapNative](capi-image-nativemodule-oh-pixelmapnative.md) \*pixelmap | 被操作的OH\_PixelmapNative指针。 |
| [OH\_Pixelmap\_ImageInfo](capi-image-nativemodule-oh-pixelmap-imageinfo.md) \*imageInfo | 图像像素信息。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_BAD\_PARAMETER：参数错误。 |

### OH\_PixelmapNative\_Opacity()

PhonePC/2in1TabletTVWearable

```
1. Image_ErrorCode OH_PixelmapNative_Opacity(OH_PixelmapNative *pixelmap, float rate)
```

**描述**

通过设置透明比率来让PixelMap达到对应的透明效果。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_PixelmapNative](capi-image-nativemodule-oh-pixelmapnative.md) \*pixelmap | 被操作的OH\_PixelmapNative指针。 |
| float rate | 透明比率的值。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_BAD\_PARAMETER：参数错误。 |

### OH\_PixelmapNative\_Scale()

PhonePC/2in1TabletTVWearable

```
1. Image_ErrorCode OH_PixelmapNative_Scale(OH_PixelmapNative *pixelmap, float scaleX, float scaleY)
```

**描述**

根据输入的宽高对图片进行缩放。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_PixelmapNative](capi-image-nativemodule-oh-pixelmapnative.md) \*pixelmap | 被操作的OH\_PixelmapNative指针。 |
| float scaleX | 宽度的缩放比例。 |
| float scaleY | 高度的缩放比例。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_BAD\_PARAMETER：参数错误。 |

### OH\_PixelmapNative\_ScaleWithAntiAliasing()

PhonePC/2in1TabletTVWearable

```
1. Image_ErrorCode OH_PixelmapNative_ScaleWithAntiAliasing(OH_PixelmapNative *pixelmap, float scaleX, float scaleY, OH_PixelmapNative_AntiAliasingLevel level)
```

**描述**

根据指定的缩放算法和输入的宽高对图片进行缩放。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_PixelmapNative](capi-image-nativemodule-oh-pixelmapnative.md) \*pixelmap | 被操作的OH\_PixelmapNative指针。 |
| float scaleX | 宽度的缩放比例。 |
| float scaleY | 高度的缩放比例。 |
| [OH\_PixelmapNative\_AntiAliasingLevel](capi-pixelmap-native-h.md#oh_pixelmapnative_antialiasinglevel) level | 缩放算法。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_BAD\_PARAMETER：参数错误。  IMAGE\_TOO\_LARGE：图片过大。  IMAGE\_ALLOC\_FAILED：内存申请失败。  IMAGE\_UNKNOWN\_ERROR：pixelmap已经被释放。 |

### OH\_PixelmapNative\_CreateScaledPixelMap()

PhonePC/2in1TabletTVWearable

```
1. Image_ErrorCode OH_PixelmapNative_CreateScaledPixelMap(OH_PixelmapNative *srcPixelmap, OH_PixelmapNative **dstPixelmap, float scaleX, float scaleY)
```

**描述**

根据输入的宽高的缩放比例，创建一个新的缩放后的图片，生成的新PixelMap不可编辑。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_PixelmapNative](capi-image-nativemodule-oh-pixelmapnative.md) \*srcPixelmap | 被操作的OH\_PixelmapNative指针，源pixelmap对象指针。 |
| [OH\_PixelmapNative](capi-image-nativemodule-oh-pixelmapnative.md) \*\*dstPixelmap | 被操作的OH\_PixelmapNative指针，目标pixelmap对象指针。 |
| float scaleX | 宽度的缩放比例。 |
| float scaleY | 高度的缩放比例。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_BAD\_PARAMETER：参数错误。 |

### OH\_PixelmapNative\_CreateScaledPixelMapWithAntiAliasing()

PhonePC/2in1TabletTVWearable

```
1. Image_ErrorCode OH_PixelmapNative_CreateScaledPixelMapWithAntiAliasing(OH_PixelmapNative *srcPixelmap, OH_PixelmapNative **dstPixelmap, float scaleX, float scaleY, OH_PixelmapNative_AntiAliasingLevel level)
```

**描述**

根据指定的缩放算法和输入的宽高的缩放比例，创建一个新的缩放后的图片，生成的新PixelMap不可编辑。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_PixelmapNative](capi-image-nativemodule-oh-pixelmapnative.md) \*srcPixelmap | 被操作的OH\_PixelmapNative指针，源pixelmap对象指针。 |
| [OH\_PixelmapNative](capi-image-nativemodule-oh-pixelmapnative.md) \*\*dstPixelmap | 被操作的OH\_PixelmapNative指针，目标pixelmap对象指针。 |
| float scaleX | 宽度的缩放比例。 |
| float scaleY | 高度的缩放比例。 |
| [OH\_PixelmapNative\_AntiAliasingLevel](capi-pixelmap-native-h.md#oh_pixelmapnative_antialiasinglevel) level | 缩放算法。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_BAD\_PARAMETER：参数错误。  IMAGE\_TOO\_LARGE：图片过大。  IMAGE\_ALLOC\_FAILED：内存申请失败。 |

### OH\_PixelmapNative\_CreateAlphaPixelmap()

PhonePC/2in1TabletTVWearable

```
1. Image_ErrorCode OH_PixelmapNative_CreateAlphaPixelmap(OH_PixelmapNative *srcPixelmap, OH_PixelmapNative **dstPixelmap)
```

**描述**

从源PixelMap创建一个仅含有Alpha通道的PixelMap，生成的新PixelMap不可编辑。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_PixelmapNative](capi-image-nativemodule-oh-pixelmapnative.md) \*srcPixelmap | 提供Alpha通道数据的源PixelMap。 |
| [OH\_PixelmapNative](capi-image-nativemodule-oh-pixelmapnative.md) \*\*dstPixelmap | 被创建的目标PixelMap。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：操作成功。  IMAGE\_BAD\_PARAMETER：参数无效，例如：srcPixelmap或dstPixelmap有误。 |

### OH\_PixelmapNative\_Clone()

PhonePC/2in1TabletTVWearable

```
1. Image_ErrorCode OH_PixelmapNative_Clone(OH_PixelmapNative *srcPixelmap, OH_PixelmapNative **dstPixelmap)
```

**描述**

从源PixelMap复制出一个新的PixelMap。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_PixelmapNative](capi-image-nativemodule-oh-pixelmapnative.md) \*srcPixelmap | 被复制的源PixelMap。 |
| [OH\_PixelmapNative](capi-image-nativemodule-oh-pixelmapnative.md) \*\*dstPixelmap | 被创建的目标PixelMap。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：操作成功。  IMAGE\_BAD\_PARAMETER：参数无效，例如：srcPixelmap或dstPixelmap有误。  IMAGE\_UNSUPPORTED\_DATA\_FORMAT：像素格式不支持。  IMAGE\_TOO\_LARGE：源PixelMap的尺寸过大。  IMAGE\_INIT\_FAILED：目标PixelMap初始化失败。  IMAGE\_ALLOC\_FAILED：内存申请或数据复制失败。 |

### OH\_PixelmapNative\_CreateCroppedAndScaledPixelMap()

PhonePC/2in1TabletTVWearable

```
1. Image_ErrorCode OH_PixelmapNative_CreateCroppedAndScaledPixelMap(OH_PixelmapNative *srcPixelmap, Image_Region *region, Image_Scale *scale, OH_PixelmapNative_AntiAliasingLevel level, OH_PixelmapNative **dstPixelmap)
```

**描述**

基于源PixelMap创建一个裁剪并缩放的新PixelMap。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_PixelmapNative](capi-image-nativemodule-oh-pixelmapnative.md) \*srcPixelmap | 源PixelMap。 |
| [Image\_Region](capi-image-nativemodule-image-region.md) \*region | 裁剪区域。 |
| [Image\_Scale](capi-image-nativemodule-image-scale.md) \*scale | 宽和高的缩放倍数。不能为0。 |
| [OH\_PixelmapNative\_AntiAliasingLevel](capi-pixelmap-native-h.md#oh_pixelmapnative_antialiasinglevel) level | 要使用的缩放插值算法。 |
| [OH\_PixelmapNative](capi-image-nativemodule-oh-pixelmapnative.md) \*\*dstPixelmap | 被创建的目标PixelMap。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：操作成功。  IMAGE\_BAD\_PARAMETER：参数无效，例如：srcPixelmap、region、scale或dstPixelmap有误。  IMAGE\_UNSUPPORTED\_DATA\_FORMAT：像素格式不支持。  IMAGE\_TOO\_LARGE：源PixelMap的尺寸过大。  IMAGE\_INIT\_FAILED：目标PixelMap初始化失败。  IMAGE\_ALLOC\_FAILED：内存申请或数据复制失败。 |

### OH\_PixelmapNative\_Translate()

PhonePC/2in1TabletTVWearable

```
1. Image_ErrorCode OH_PixelmapNative_Translate(OH_PixelmapNative *pixelmap, float x, float y)
```

**描述**

根据输入的坐标对图片进行位置变换。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_PixelmapNative](capi-image-nativemodule-oh-pixelmapnative.md) \*pixelmap | 被操作的OH\_PixelmapNative指针。 |
| float x | 区域横坐标。 |
| float y | 区域纵坐标。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_BAD\_PARAMETER：参数错误。 |

### OH\_PixelmapNative\_Rotate()

PhonePC/2in1TabletTVWearable

```
1. Image_ErrorCode OH_PixelmapNative_Rotate(OH_PixelmapNative *pixelmap, float angle)
```

**描述**

根据输入的角度对图片进行旋转。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_PixelmapNative](capi-image-nativemodule-oh-pixelmapnative.md) \*pixelmap | 被操作的OH\_PixelmapNative指针。 |
| float angle | 图片旋转的角度，单位为deg。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_BAD\_PARAMETER：参数错误。 |

### OH\_PixelmapNative\_Flip()

PhonePC/2in1TabletTVWearable

```
1. Image_ErrorCode OH_PixelmapNative_Flip(OH_PixelmapNative *pixelmap, bool shouldFlipHorizontally, bool shouldFlipVertically)
```

**描述**

根据输入的条件对图片进行翻转。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_PixelmapNative](capi-image-nativemodule-oh-pixelmapnative.md) \*pixelmap | 被操作的OH\_PixelmapNative指针。 |
| bool shouldFlipHorizontally | 是否水平翻转图像。true表示进行水平翻转，false表示不进行水平翻转。 |
| bool shouldFlipVertically | 是否垂直翻转图像。true表示进行垂直翻转，false表示不进行垂直翻转。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_BAD\_PARAMETER：参数错误。 |

### OH\_PixelmapNative\_Crop()

PhonePC/2in1TabletTVWearable

```
1. Image_ErrorCode OH_PixelmapNative_Crop(OH_PixelmapNative *pixelmap, Image_Region *region)
```

**描述**

根据输入的尺寸对图片进行裁剪。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_PixelmapNative](capi-image-nativemodule-oh-pixelmapnative.md) \*pixelmap | 被操作的OH\_PixelmapNative指针。 |
| [Image\_Region](capi-image-nativemodule-image-region.md) \*region | 裁剪的尺寸。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_BAD\_PARAMETER：参数错误。 |

### OH\_PixelmapNative\_Release()

PhonePC/2in1TabletTVWearable

```
1. Image_ErrorCode OH_PixelmapNative_Release(OH_PixelmapNative *pixelmap)
```

**描述**

释放OH\_PixelmapNative指针，推荐使用[OH\_PixelmapNative\_Destroy](capi-pixelmap-native-h.md#oh_pixelmapnative_destroy)。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_PixelmapNative](capi-image-nativemodule-oh-pixelmapnative.md) \*pixelmap | 被释放的OH\_PixelmapNative指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_BAD\_PARAMETER：参数错误。 |

### OH\_PixelmapNative\_Destroy()

PhonePC/2in1TabletTVWearable

```
1. Image_ErrorCode OH_PixelmapNative_Destroy(OH_PixelmapNative **pixelmap)
```

**描述**

释放OH\_PixelmapNative指针。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_PixelmapNative](capi-image-nativemodule-oh-pixelmapnative.md) \*\*pixelmap | 被释放的OH\_PixelmapNative指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_BAD\_PARAMETER：参数错误。 |

### OH\_PixelmapNative\_ConvertAlphaFormat()

PhonePC/2in1TabletTVWearable

```
1. Image_ErrorCode OH_PixelmapNative_ConvertAlphaFormat(OH_PixelmapNative* srcpixelmap, OH_PixelmapNative* dstpixelmap, const bool isPremul)
```

**描述**

将pixelmap的像素数据做预乘和非预乘之间的转换。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_PixelmapNative](capi-image-nativemodule-oh-pixelmapnative.md)\* srcpixelmap | 被操作的OH\_PixelmapNative指针，源pixelmap对象指针。 |
| [OH\_PixelmapNative](capi-image-nativemodule-oh-pixelmapnative.md)\* dstpixelmap | 被操作的OH\_PixelmapNative指针，目标pixelmap对象指针。 |
| const bool isPremul | 转换方式，true为非预乘转预乘，false为预乘转非预乘。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_BAD\_PARAMETER：参数错误。 |

### OH\_PixelmapNative\_CreateEmptyPixelmap()

PhonePC/2in1TabletTVWearable

```
1. Image_ErrorCode OH_PixelmapNative_CreateEmptyPixelmap(OH_Pixelmap_InitializationOptions *options, OH_PixelmapNative **pixelmap)
```

**描述**

利用OH\_Pixelmap\_InitializationOptions创建空的pixelmap对象，内存数据为0。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Pixelmap\_InitializationOptions](age-nativemodule-oh-pixelmap-initializationoptions.md) \*options | 创建像素的属性。 |
| [OH\_PixelmapNative](capi-image-nativemodule-oh-pixelmapnative.md) \*\*pixelmap | 被创建的OH\_PixelmapNative对象指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_BAD\_PARAMETER：参数错误。 |

### OH\_PixelmapNative\_CreateEmptyPixelmapUsingAllocator()

PhonePC/2in1TabletTVWearable

```
1. Image_ErrorCode OH_PixelmapNative_CreateEmptyPixelmapUsingAllocator(OH_Pixelmap_InitializationOptions *options, IMAGE_ALLOCATOR_MODE allocator, OH_PixelmapNative **pixelmap)
```

**描述**

根据入参options创建空的pixelmap，pixelmap使用的内存类型可以通过allocator指定。默认情况下，系统会根据图像类型、图像大小、平台能力等选择内存类型。在处理此接口返回的像素图时，需要考虑步长影响。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Pixelmap\_InitializationOptions](age-nativemodule-oh-pixelmap-initializationoptions.md) \*options | 创建pixelmap的选项。 |
| [IMAGE\_ALLOCATOR\_MODE](capi-image-common-h.md#image_allocator_mode) allocator | 决定pixelmap内存分配的类型。 |
| [OH\_PixelmapNative](capi-image-nativemodule-oh-pixelmapnative.md) \*\*pixelmap | 被创建的OH\_PixelmapNative对象指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_BAD\_PARAMETER：参数错误。  IMAGE\_UNSUPPORTED\_OPERATION：操作不支持。  IMAGE\_TOO\_LARGE：图像过大，无法分配内存。  IMAGE\_DMA\_OPERATION\_FAILED：DMA内存操作失败。  IMAGE\_ALLOCATOR\_MODE\_UNSUPPORTED：不支持分配当前内存类型。例如，使用共享内存创建HDR图。 |

### OH\_PixelmapNative\_CreatePixelmapFromSurface()

PhonePC/2in1TabletTVWearable

```
1. Image_ErrorCode OH_PixelmapNative_CreatePixelmapFromSurface(const char *surfaceId, size_t length, OH_PixelmapNative **pixelmap)
```

**描述**

通过Surface的Surface ID创建一个PixelMap。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const char \*surfaceId | Surface ID字符串。 |
| size\_t length | Surface ID字符串的长度。 |
| [OH\_PixelmapNative](capi-image-nativemodule-oh-pixelmapnative.md) \*\*pixelmap | 被创建的PixelMap。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：操作成功。  IMAGE\_BAD\_PARAMETER：参数无效，例如：surfaceId或pixelmap有误。  IMAGE\_CREATE\_PIXELMAP\_FAILED：PixelMap创建失败。 |

### OH\_PixelmapNative\_CreatePixelmapFromSurfaceWithTransformation()

PhonePC/2in1TabletTVWearable

```
1. Image_ErrorCode OH_PixelmapNative_CreatePixelmapFromSurfaceWithTransformation(const char *surfaceId, size_t length, bool transformEnabled, OH_PixelmapNative **pixelmap)
```

**描述**

通过Surface的ID创建一个预览流画面的PixelMap对象。该Surface可能携带旋转或翻转的变换信息。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const char \*surfaceId | 对应Surface的ID字符串。 |
| size\_t length | 对应Surface的ID字符串长度。 |
| bool transformEnabled | 是否对携带变换信息的Surface预先进行逆变换来消除PixelMap的旋转或翻转效果。若Surface未携带变换信息，本参数不生效。  如果是true，则进行逆变换，变换的角度与Surface携带的角度一致且方向相反，输出的PixelMap无旋转或翻转效果；  如果是false，则不进行逆变换，输出的PixelMap会根据Surface中的变换信息而带有旋转或翻转效果。 |
| [OH\_PixelmapNative](capi-image-nativemodule-oh-pixelmapnative.md) \*\*pixelmap | 被创建的PixelMap。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：操作成功。  IMAGE\_INVALID\_PARAMETER：参数无效，例如：surfaceId或pixelmap有误。  IMAGE\_UNSUPPORTED\_OPERATION：不支持的操作，例如：跨平台时调用。  IMAGE\_GET\_IMAGE\_DATA\_FAILED：获取Surface的数据失败。  IMAGE\_CREATE\_PIXELMAP\_FAILED：PixelMap创建失败。 |

**参考：**

[OH\_PixelmapNative](capi-image-nativemodule-oh-pixelmapnative.md)

### OH\_PixelmapNative\_CreatePixelmapFromNativeBuffer()

PhonePC/2in1TabletTVWearable

```
1. Image_ErrorCode OH_PixelmapNative_CreatePixelmapFromNativeBuffer(OH_NativeBuffer *nativeBuffer, OH_PixelmapNative **pixelmap)
```

**描述**

通过NativeBuffer创建一个PixelMap。如果NativeBuffer的用途未配置[CPU访问权限](capi-native-buffer-h.md#oh_nativebuffer_usage)，则不支持创建。

支持创建的像素格式为RGBA\_8888、NV21、NV12、YCBCR\_P010、YCRCB\_P010。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_NativeBuffer](ge-nativemodule-image-nativemodule-oh-nativebuffer.md) \*nativeBuffer | 含有PixelMap数据的NativeBuffer对象。 |
| [OH\_PixelmapNative](capi-image-nativemodule-oh-pixelmapnative.md) \*\*pixelmap | 被创建的PixelMap。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：操作成功。  IMAGE\_BAD\_PARAMETER：参数无效，例如：nativeBuffer或pixelmap有误，像素格式不支持，或未配置[CPU访问权限](capi-native-buffer-h.md#oh_nativebuffer_usage)。  IMAGE\_CREATE\_PIXELMAP\_FAILED：PixelMap创建失败。 |

### OH\_PixelmapNative\_GetNativeBuffer()

PhonePC/2in1TabletTVWearable

```
1. Image_ErrorCode OH_PixelmapNative_GetNativeBuffer(OH_PixelmapNative *pixelmap, OH_NativeBuffer **nativeBuffer)
```

**描述**

从DMA内存的PixelMap中，获取NativeBuffer对象。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_PixelmapNative](capi-image-nativemodule-oh-pixelmapnative.md) \*pixelmap | 要获取NativeBuffer的源PixelMap。 |
| [OH\_NativeBuffer](ge-nativemodule-image-nativemodule-oh-nativebuffer.md) \*\*nativeBuffer | 被创建的NativeBuffer对象指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_BAD\_PARAMETER：参数错误。  IMAGE\_DMA\_NOT\_EXIST：不是DMA内存。  IMAGE\_DMA\_OPERATION\_FAILED：DMA内存操作失败。 |

### OH\_PixelmapNative\_GetMetadata()

PhonePC/2in1TabletTVWearable

```
1. Image_ErrorCode OH_PixelmapNative_GetMetadata(OH_PixelmapNative *pixelmap, OH_Pixelmap_HdrMetadataKey key, OH_Pixelmap_HdrMetadataValue **value)
```

**描述**

获取元数据。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_PixelmapNative](capi-image-nativemodule-oh-pixelmapnative.md) \*pixelmap | 被操作的OH\_PixelmapNative指针。 |
| [OH\_Pixelmap\_HdrMetadataKey](capi-pixelmap-native-h.md#oh_pixelmap_hdrmetadatakey) key | 元数据的关键字。 |
| [OH\_Pixelmap\_HdrMetadataValue](pi-image-nativemodule-oh-pixelmap-hdrmetadatavalue.md) \*\*value | 元数据的值。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_BAD\_PARAMETER：参数错误。  IMAGE\_DMA\_NOT\_EXIST：不存在DMA内存。  IMAGE\_COPY\_FAILED：如果内存拷贝失败。 |

### OH\_PixelmapNative\_SetMetadata()

PhonePC/2in1TabletTVWearable

```
1. Image_ErrorCode OH_PixelmapNative_SetMetadata(OH_PixelmapNative *pixelmap, OH_Pixelmap_HdrMetadataKey key, OH_Pixelmap_HdrMetadataValue *value)
```

**描述**

设置元数据。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_PixelmapNative](capi-image-nativemodule-oh-pixelmapnative.md) \*pixelmap | 被操作的OH\_PixelmapNative指针。 |
| [OH\_Pixelmap\_HdrMetadataKey](capi-pixelmap-native-h.md#oh_pixelmap_hdrmetadatakey) key | 元数据的关键字。 |
| [OH\_Pixelmap\_HdrMetadataValue](pi-image-nativemodule-oh-pixelmap-hdrmetadatavalue.md) \*value | 元数据的值。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_BAD\_PARAMETER：参数错误。  IMAGE\_DMA\_NOT\_EXIST：不存在DMA内存。  IMAGE\_COPY\_FAILED：如果内存拷贝失败。 |

### OH\_PixelmapNative\_SetColorSpaceNative()

PhonePC/2in1TabletTVWearable

```
1. Image_ErrorCode OH_PixelmapNative_SetColorSpaceNative(OH_PixelmapNative *pixelmap, OH_NativeColorSpaceManager *colorSpaceNative)
```

**描述**

设置NativeColorSpaceManager对象。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_PixelmapNative](capi-image-nativemodule-oh-pixelmapnative.md) \*pixelmap | 要设置NativeColorSpaceManager的目标PixelMap。 |
| [OH\_NativeColorSpaceManager](capi-image-nativemodule-oh-nativecolorspacemanager.md) \*colorSpaceNative | 要设置的NativeColorSpaceManager对象。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_BAD\_PARAMETER：参数错误。 |

### OH\_PixelmapNative\_GetColorSpaceNative()

PhonePC/2in1TabletTVWearable

```
1. Image_ErrorCode OH_PixelmapNative_GetColorSpaceNative(OH_PixelmapNative *pixelmap, OH_NativeColorSpaceManager **colorSpaceNative)
```

**描述**

获取NativeColorSpaceManager对象。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_PixelmapNative](capi-image-nativemodule-oh-pixelmapnative.md) \*pixelmap | 获取到NativeColorSpaceManager的源PixelMap。 |
| [OH\_NativeColorSpaceManager](capi-image-nativemodule-oh-nativecolorspacemanager.md) \*\*colorSpaceNative | 获取到的NativeColorSpaceManager对象。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_BAD\_PARAMETER：参数错误。 |

### OH\_PixelmapNative\_SetMemoryName()

PhonePC/2in1TabletTVWearable

```
1. Image_ErrorCode OH_PixelmapNative_SetMemoryName(OH_PixelmapNative *pixelmap, char *name, size_t *size)
```

**描述**

设置pixelMap内存名字。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_PixelmapNative](capi-image-nativemodule-oh-pixelmapnative.md) \*pixelmap | 被操作的OH\_PixelmapNative指针。 |
| char \*name | 需要被设置的PixelMap内存名称。 |
| size\_t \*size | 需要被设置的PixelMap内存名称的字节大小。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_BAD\_PARAMETER：名字长度超过取值范围。DMA内存名字取值范围为[1, 255]，ASHMEM内存名字取值范围为[1, 244]，单位字节。  IMAGE\_UNSUPPORTED\_MEMORY\_FORMAT：既不是DMA内存也不是ASHMEM内存。 |

### OH\_PixelmapNative\_GetByteCount()

PhonePC/2in1TabletTVWearable

```
1. Image_ErrorCode OH_PixelmapNative_GetByteCount(OH_PixelmapNative *pixelmap, uint32_t *byteCount)
```

**描述**

获取Pixelmap中所有像素所占用的总字节数，不包含内存填充。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_PixelmapNative](capi-image-nativemodule-oh-pixelmapnative.md) \*pixelmap | 被操作的Pixelmap指针。 |
| uint32\_t \*byteCount | 获取的总字节数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_BAD\_PARAMETER：pixelmap或byteCount参数无效。 |

### OH\_PixelmapNative\_GetAllocationByteCount()

PhonePC/2in1TabletTVWearable

```
1. Image_ErrorCode OH_PixelmapNative_GetAllocationByteCount(OH_PixelmapNative *pixelmap, uint32_t *allocationByteCount)
```

**描述**

获取Pixelmap用于储存像素数据的内存字节数。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_PixelmapNative](capi-image-nativemodule-oh-pixelmapnative.md) \*pixelmap | 被操作的Pixelmap指针。 |
| uint32\_t \*allocationByteCount | 获取的内存字节数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_BAD\_PARAMETER：pixelmap或allocationByteCount参数无效。 |

### OH\_PixelmapNative\_AccessPixels()

PhonePC/2in1TabletTVWearable

```
1. Image_ErrorCode OH_PixelmapNative_AccessPixels(OH_PixelmapNative *pixelmap, void **addr)
```

**描述**

获取Pixelmap像素数据的内存地址，并锁定这块内存。

当该内存被锁定时，任何修改或释放该Pixelmap的像素数据的操作均会失败或无效。

**起始版本：** 15

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_PixelmapNative](capi-image-nativemodule-oh-pixelmapnative.md) \*pixelmap | 被操作的Pixelmap指针。 |
| void \*\*addr | Pixelmap内存地址的双指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_BAD\_PARAMETER：pixelmap或addr参数无效。  IMAGE\_LOCK\_UNLOCK\_FAILED：内存锁定失败。 |

### OH\_PixelmapNative\_UnaccessPixels()

PhonePC/2in1TabletTVWearable

```
1. Image_ErrorCode OH_PixelmapNative_UnaccessPixels(OH_PixelmapNative *pixelmap)
```

**描述**

释放Pixelmap像素数据的内存锁。

该函数需要与[OH\_PixelmapNative\_AccessPixels](capi-pixelmap-native-h.md#oh_pixelmapnative_accesspixels)匹配使用。

**起始版本：** 15

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_PixelmapNative](capi-image-nativemodule-oh-pixelmapnative.md) \*pixelmap | 被操作的Pixelmap指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_BAD\_PARAMETER：pixelmap参数无效。  IMAGE\_LOCK\_UNLOCK\_FAILED：内存解锁失败。 |

### OH\_PixelmapNative\_GetUniqueId()

PhonePC/2in1TabletTVWearable

```
1. Image_ErrorCode OH_PixelmapNative_GetUniqueId(OH_PixelmapNative *pixelmap, uint32_t *uniqueId)
```

**描述**

获取PixelMap的唯一ID。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_PixelmapNative](capi-image-nativemodule-oh-pixelmapnative.md) \*pixelmap | 获取唯一ID的PixelMap。 |
| uint32\_t \*uniqueId | 获取的唯一ID。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：操作成功。  IMAGE\_BAD\_PARAMETER：参数无效，例如：pixelmap或uniqueId有误。 |

### OH\_PixelmapNative\_IsReleased()

PhonePC/2in1TabletTVWearable

```
1. Image_ErrorCode OH_PixelmapNative_IsReleased(OH_PixelmapNative *pixelmap, bool *released)
```

**描述**

检测PixelMap是否已被释放。如果已被释放，则任何访问该对象内部数据的方法调用将会失效。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_PixelmapNative](capi-image-nativemodule-oh-pixelmapnative.md) \*pixelmap | 被检测的PixelMap。 |
| bool \*released | 获取的PixelMap的释放状态。true表示已被释放，false表示未被释放。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：操作成功。  IMAGE\_BAD\_PARAMETER：参数无效，例如：pixelmap或released有误。 |
