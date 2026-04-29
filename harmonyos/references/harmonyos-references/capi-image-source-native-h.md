---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-source-native-h
title: image_source_native.h
breadcrumb: API参考 > 媒体 > Image Kit（图片处理服务） > C API > 头文件 > image_source_native.h
category: harmonyos-references
scraped_at: 2026-04-29T14:03:54+08:00
doc_updated_at: 2026-04-28
content_hash: sha256:d97b1cb9c245fa099170fd0e0022e08d701018d4ef1479c7019dbd2311e20471
---

## 概述

PhonePC/2in1TabletTVWearable

图片解码API。

**引用文件：** <multimedia/image\_framework/image/image\_source\_native.h>

**库：** libimage\_source.so

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**起始版本：** 12

**相关模块：** [Image\_NativeModule](capi-image-nativemodule.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 结构体

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [OH\_ImageSourceNative](capi-image-nativemodule-oh-imagesourcenative.md) | OH\_ImageSourceNative | OH\_ImageSourceNative是native层封装的ImageSource结构体，用于创建图片数据。 |
| [OH\_ImageSource\_Info](capi-image-nativemodule-imagesource-info.md) | OH\_ImageSource\_Info | OH\_ImageSource\_Info是native层封装的ImageSource信息结构体，OH\_ImageSource\_Info结构体不可直接操作，而是采用函数调用方式创建、释放结构体以及操作具体字段。 |
| [OH\_DecodingOptionsForPicture](pi-image-nativemodule-oh-decodingoptionsforpicture.md) | OH\_DecodingOptionsForPicture | Picture解码参数结构体。通过[OH\_DecodingOptionsForPicture\_Create](capi-image-source-native-h.md#oh_decodingoptionsforpicture_create)获取。 |
| [OH\_DecodingOptions](capi-image-nativemodule-oh-decodingoptions.md) | OH\_DecodingOptions | OH\_DecodingOptions是native层封装的解码选项参数结构体，用于设置解码选项参数，在创建Pixelmap时作为入参传入，详细信息见[OH\_ImageSourceNative\_CreatePixelmap](capi-image-source-native-h.md#oh_imagesourcenative_createpixelmap)。 |

### 枚举

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [IMAGE\_DYNAMIC\_RANGE](capi-image-source-native-h.md#image_dynamic_range) | IMAGE\_DYNAMIC\_RANGE | 解码指定期望动态范围。 |
| [IMAGE\_ALLOCATOR\_TYPE](capi-image-source-native-h.md#image_allocator_type) | IMAGE\_ALLOCATOR\_TYPE | 用于分配PixelMap内存的分配器类型。 |
| [Image\_CropAndScaleStrategy](capi-image-source-native-h.md#image_cropandscalestrategy) | Image\_CropAndScaleStrategy | 在同时指定desiredSize和desiredRegion时执行裁剪和缩放的策略。 |

### 函数

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [Image\_ErrorCode OH\_ImageSourceInfo\_Create(OH\_ImageSource\_Info \*\*info)](capi-image-source-native-h.md#oh_imagesourceinfo_create) | 创建OH\_ImageSource\_Info指针。 |
| [Image\_ErrorCode OH\_ImageSourceInfo\_GetWidth(OH\_ImageSource\_Info \*info, uint32\_t \*width)](capi-image-source-native-h.md#oh_imagesourceinfo_getwidth) | 获取图片的宽。对于没有width标签的SVG图片，返回默认值0。 |
| [Image\_ErrorCode OH\_ImageSourceInfo\_GetHeight(OH\_ImageSource\_Info \*info, uint32\_t \*height)](capi-image-source-native-h.md#oh_imagesourceinfo_getheight) | 获取图片的高。对于没有height标签的SVG图片，返回默认值0。 |
| [Image\_ErrorCode OH\_ImageSourceInfo\_GetDynamicRange(OH\_ImageSource\_Info \*info, bool \*isHdr)](capi-image-source-native-h.md#oh_imagesourceinfo_getdynamicrange) | 获取图片是否为高动态范围的信息。 |
| [Image\_ErrorCode OH\_ImageSourceInfo\_GetMimeType(OH\_ImageSource\_Info \*info, Image\_MimeType \*mimetype)](capi-image-source-native-h.md#oh_imagesourceinfo_getmimetype) | 获取图片源的MIME类型。 |
| [Image\_ErrorCode OH\_ImageSourceInfo\_Release(OH\_ImageSource\_Info \*info)](capi-image-source-native-h.md#oh_imagesourceinfo_release) | 释放OH\_ImageSource\_Info指针。调用该接口之后，与OH\_ImageSourceInfo结构体相关的属性均会被释放。因此在调用该接口前，请务必确认相关属性已不再被需要或对相关属性已完成深拷贝操作。 |
| [Image\_ErrorCode OH\_DecodingOptions\_Create(OH\_DecodingOptions \*\*options)](capi-image-source-native-h.md#oh_decodingoptions_create) | 创建OH\_DecodingOptions指针。 |
| [Image\_ErrorCode OH\_DecodingOptions\_GetPixelFormat(OH\_DecodingOptions \*options, int32\_t \*pixelFormat)](capi-image-source-native-h.md#oh_decodingoptions_getpixelformat) | 获取pixel格式。 |
| [Image\_ErrorCode OH\_DecodingOptions\_SetPixelFormat(OH\_DecodingOptions \*options, int32\_t pixelFormat)](capi-image-source-native-h.md#oh_decodingoptions_setpixelformat) | 设置pixel格式。 |
| [Image\_ErrorCode OH\_DecodingOptions\_GetIndex(OH\_DecodingOptions \*options, uint32\_t \*index)](capi-image-source-native-h.md#oh_decodingoptions_getindex) | 获取解码图片序号。 |
| [Image\_ErrorCode OH\_DecodingOptions\_SetIndex(OH\_DecodingOptions \*options, uint32\_t index)](capi-image-source-native-h.md#oh_decodingoptions_setindex) | 设置解码图片序号。 |
| [Image\_ErrorCode OH\_DecodingOptions\_GetRotate(OH\_DecodingOptions \*options, float \*rotate)](capi-image-source-native-h.md#oh_decodingoptions_getrotate) | 获取旋转角度。 |
| [Image\_ErrorCode OH\_DecodingOptions\_SetRotate(OH\_DecodingOptions \*options, float rotate)](capi-image-source-native-h.md#oh_decodingoptions_setrotate) | 设置旋转角度。 |
| [Image\_ErrorCode OH\_DecodingOptions\_GetDesiredSize(OH\_DecodingOptions \*options, Image\_Size \*desiredSize)](capi-image-source-native-h.md#oh_decodingoptions_getdesiredsize) | 获取期望输出大小。 |
| [Image\_ErrorCode OH\_DecodingOptions\_SetDesiredSize(OH\_DecodingOptions \*options, Image\_Size \*desiredSize)](capi-image-source-native-h.md#oh_decodingoptions_setdesiredsize) | 设置期望输出大小。desiredSize参数决定解码得到的PixelMap大小，且宽、高须为正整数。若与原尺寸比例不一致，则会进行拉伸/缩放到指定尺寸。默认为原始尺寸。 |
| [Image\_ErrorCode OH\_DecodingOptions\_GetDesiredRegion(OH\_DecodingOptions \*options, Image\_Region \*desiredRegion)](capi-image-source-native-h.md#oh_decodingoptions_getdesiredregion) | 获取解码区域。  由于对应SetDesiredRegion接口无法满足区域解码诉求，从API version 19开始，推荐配套使用[OH\_DecodingOptions\_GetCropRegion](capi-image-source-native-h.md#oh_decodingoptions_getcropregion)接口替代。 |
| [Image\_ErrorCode OH\_DecodingOptions\_SetDesiredRegion(OH\_DecodingOptions \*options, Image\_Region \*desiredRegion)](capi-image-source-native-h.md#oh_decodingoptions_setdesiredregion) | 设置解码区域。  实际解码结果会按照原图解码，无区域解码效果。从API version 19开始，推荐使用接口[OH\_DecodingOptions\_SetCropRegion](capi-image-source-native-h.md#oh_decodingoptions_setcropregion)替代。 |
| [Image\_ErrorCode OH\_DecodingOptions\_GetDesiredDynamicRange(OH\_DecodingOptions \*options, int32\_t \*desiredDynamicRange)](capi-image-source-native-h.md#oh_decodingoptions_getdesireddynamicrange) | 获取解码时设置的期望动态范围。 |
| [Image\_ErrorCode OH\_DecodingOptions\_SetDesiredDynamicRange(OH\_DecodingOptions \*options, int32\_t desiredDynamicRange)](capi-image-source-native-h.md#oh_decodingoptions_setdesireddynamicrange) | 设置解码时的期望动态范围。 |
| [Image\_ErrorCode OH\_DecodingOptions\_GetDesiredColorSpace(OH\_DecodingOptions \*options, int32\_t \*colorSpace)](capi-image-source-native-h.md#oh_decodingoptions_getdesiredcolorspace) | 获取解码参数中设置的色彩空间。 |
| [Image\_ErrorCode OH\_DecodingOptions\_SetDesiredColorSpace(OH\_DecodingOptions \*options, int32\_t colorSpace)](capi-image-source-native-h.md#oh_decodingoptions_setdesiredcolorspace) | 设置解码期望得到的色彩空间。 |
| [Image\_ErrorCode OH\_DecodingOptions\_SetCropAndScaleStrategy(OH\_DecodingOptions \*options, int32\_t cropAndScaleStrategy)](capi-image-source-native-h.md#oh_decodingoptions_setcropandscalestrategy) | 设置解码选项的裁剪和缩放策略。 |
| [Image\_ErrorCode OH\_DecodingOptions\_GetCropAndScaleStrategy(OH\_DecodingOptions \*options, int32\_t \*cropAndScaleStrategy)](capi-image-source-native-h.md#oh_decodingoptions_getcropandscalestrategy) | 获取解码选项的裁剪和缩放策略。 |
| [Image\_ErrorCode OH\_DecodingOptions\_GetCropRegion(OH\_DecodingOptions \*options, Image\_Region \*cropRegion)](capi-image-source-native-h.md#oh_decodingoptions_getcropregion) | 获取解码参数中的裁剪区域。 |
| [Image\_ErrorCode OH\_DecodingOptions\_SetCropRegion(OH\_DecodingOptions \*options, Image\_Region \*cropRegion)](capi-image-source-native-h.md#oh_decodingoptions_setcropregion) | 设置解码参数中的裁剪区域。 |
| [Image\_ErrorCode OH\_DecodingOptions\_Release(OH\_DecodingOptions \*options)](capi-image-source-native-h.md#oh_decodingoptions_release) | 释放OH\_DecodingOptions指针。 |
| [Image\_ErrorCode OH\_ImageSourceNative\_CreateFromUri(char \*uri, size\_t uriSize, OH\_ImageSourceNative \*\*res)](capi-image-source-native-h.md#oh_imagesourcenative_createfromuri) | 通过uri创建OH\_ImageSourceNative指针。 |
| [Image\_ErrorCode OH\_ImageSourceNative\_CreateFromFd(int32\_t fd, OH\_ImageSourceNative \*\*res)](capi-image-source-native-h.md#oh_imagesourcenative_createfromfd) | 通过fd创建OH\_ImageSourceNative指针。 |
| [Image\_ErrorCode OH\_ImageSourceNative\_CreateFromData(uint8\_t \*data, size\_t dataSize, OH\_ImageSourceNative \*\*res)](capi-image-source-native-h.md#oh_imagesourcenative_createfromdata) | 通过缓冲区数据创建OH\_ImageSourceNative指针。  data数据应该是未解码的数据，不要传入类似于RGBA，YUV的像素buffer数据，如果想通过像素buffer数据创建pixelMap，可以调用[OH\_PixelmapNative\_CreatePixelmap](capi-pixelmap-native-h.md#oh_pixelmapnative_createpixelmap)这一类接口。 |
| [Image\_ErrorCode OH\_ImageSourceNative\_CreateFromDataWithUserBuffer(uint8\_t \*data, size\_t datalength, OH\_ImageSourceNative \*\*imageSource)](capi-image-source-native-h.md#oh_imagesourcenative_createfromdatawithuserbuffer) | 由数据缓存创建图片源。传入的数据缓存将在图片源对象中直接访问，在图片源对象的生命周期内，数据缓存需要保持可用。 |
| [Image\_ErrorCode OH\_ImageSourceNative\_CreateFromRawFile(RawFileDescriptor \*rawFile, OH\_ImageSourceNative \*\*res)](capi-image-source-native-h.md#oh_imagesourcenative_createfromrawfile) | 通过图像资源文件的RawFileDescriptor创建OH\_ImageSourceNative指针。 |
| [Image\_ErrorCode OH\_ImageSourceNative\_CreatePixelmap(OH\_ImageSourceNative \*source, OH\_DecodingOptions \*options, OH\_PixelmapNative \*\*pixelmap)](capi-image-source-native-h.md#oh_imagesourcenative_createpixelmap) | 通过图片解码参数创建OH\_PixelmapNative指针。 |
| [Image\_ErrorCode OH\_ImageSourceNative\_CreatePixelmapUsingAllocator(OH\_ImageSourceNative \*source, OH\_DecodingOptions \*options, IMAGE\_ALLOCATOR\_TYPE allocator, OH\_PixelmapNative \*\*pixelmap)](capi-image-source-native-h.md#oh_imagesourcenative_createpixelmapusingallocator) | 根据解码参数创建一个PixelMap，PixelMap使用的内存类型可以通过allocatorType来指定。  默认情况下，系统会根据图像类型、图像大小、平台能力等选择内存类型。在处理通过此接口返回的PixelMap时，请始终考虑步幅（stride）的影响。 |
| [Image\_ErrorCode OH\_ImageSourceNative\_CreatePixelmapList(OH\_ImageSourceNative \*source, OH\_DecodingOptions \*options, OH\_PixelmapNative \*resVecPixMap[], size\_t size)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-source-native-h#oh_imagesourcenative_createpixelmaplist) | 通过图片解码参数创建OH\_PixelmapNative数组。  注意，此接口会一次性解码全部帧，当帧数过多或单帧图像过大时，会占用较大内存，造成系统内存紧张，此种情况推荐使用Image组件显示动图，Image组件采用逐帧解码，占用内存比此接口少。 |
| [Image\_ErrorCode OH\_ImageSourceNative\_CreatePicture(OH\_ImageSourceNative \*source, OH\_DecodingOptionsForPicture \*options, OH\_PictureNative \*\*picture)](capi-image-source-native-h.md#oh_imagesourcenative_createpicture) | 通过图片解码创建OH\_PictureNative指针。 |
| [Image\_ErrorCode OH\_ImageSourceNative\_CreatePictureAtIndex(OH\_ImageSourceNative \*source, uint32\_t index, OH\_PictureNative \*\*picture)](capi-image-source-native-h.md#oh_imagesourcenative_createpictureatindex) | 通过指定序号的图片解码创建OH\_PictureNative指针。 |
| [Image\_ErrorCode OH\_ImageSourceNative\_GetDelayTimeList(OH\_ImageSourceNative \*source, int32\_t \*delayTimeList, size\_t size)](capi-image-source-native-h.md#oh_imagesourcenative_getdelaytimelist) | 获取图像延迟时间数组。 |
| [Image\_ErrorCode OH\_ImageSourceNative\_GetImageInfo(OH\_ImageSourceNative \*source, int32\_t index, OH\_ImageSource\_Info \*info)](capi-image-source-native-h.md#oh_imagesourcenative_getimageinfo) | 获取指定序号的图片信息。 |
| [Image\_ErrorCode OH\_ImageSourceNative\_GetImageProperty(OH\_ImageSourceNative \*source, Image\_String \*key, Image\_String \*value)](capi-image-source-native-h.md#oh_imagesourcenative_getimageproperty) | 获取图片指定属性键的值。该接口获取到的value.data缺少字符串结束符'\0'，请谨慎使用。 |
| [Image\_ErrorCode OH\_ImageSourceNative\_GetImagePropertyShort(OH\_ImageSourceNative \*source, Image\_String \*key, uint16\_t \*value)](capi-image-source-native-h.md#oh_imagesourcenative_getimagepropertyshort) | 以短整型类型获取图像属性的值。 |
| [Image\_ErrorCode OH\_ImageSourceNative\_GetImagePropertyLong(OH\_ImageSourceNative \*source, Image\_String \*key, uint32\_t \*value)](capi-image-source-native-h.md#oh_imagesourcenative_getimagepropertylong) | 以长整型类型获取图像属性的值。 |
| [Image\_ErrorCode OH\_ImageSourceNative\_GetImagePropertyDouble(OH\_ImageSourceNative \*source, Image\_String \*key, double \*value)](capi-image-source-native-h.md#oh_imagesourcenative_getimagepropertydouble) | 以浮点型类型获取图像属性的值。 |
| [Image\_ErrorCode OH\_ImageSourceNative\_GetImagePropertyArraySize(OH\_ImageSourceNative \*source, Image\_String \*key, size\_t \*size)](capi-image-source-native-h.md#oh_imagesourcenative_getimagepropertyarraysize) | 获取数组类型属性的数组长度或字符串类型属性的字符串长度。 |
| [Image\_ErrorCode OH\_ImageSourceNative\_GetImagePropertyString(OH\_ImageSourceNative \*source, Image\_String \*key, char \*value, size\_t size)](capi-image-source-native-h.md#oh_imagesourcenative_getimagepropertystring) | 以字符串类型获取图像属性的值。 |
| [Image\_ErrorCode OH\_ImageSourceNative\_GetImagePropertyIntArray(OH\_ImageSourceNative \*source, Image\_String \*key, int32\_t \*value, size\_t size)](capi-image-source-native-h.md#oh_imagesourcenative_getimagepropertyintarray) | 以整型数组类型获取图像属性的值。 |
| [Image\_ErrorCode OH\_ImageSourceNative\_GetImagePropertyDoubleArray(OH\_ImageSourceNative \*source, Image\_String \*key, double \*value, size\_t size)](capi-image-source-native-h.md#oh_imagesourcenative_getimagepropertydoublearray) | 以浮点型数组类型获取图像属性的值。 |
| [Image\_ErrorCode OH\_ImageSourceNative\_GetImagePropertyBlob(OH\_ImageSourceNative \*source, Image\_String \*key, void \*value, size\_t size)](capi-image-source-native-h.md#oh_imagesourcenative_getimagepropertyblob) | 以二进制对象类型获取图像属性的值。 |
| [Image\_ErrorCode OH\_ImageSourceNative\_ModifyImagePropertyShort(OH\_ImageSourceNative \*source, Image\_String \*key, uint16\_t value)](capi-image-source-native-h.md#oh_imagesourcenative_modifyimagepropertyshort) | 修改图像属性中短整型的值。 |
| [Image\_ErrorCode OH\_ImageSourceNative\_ModifyImagePropertyLong(OH\_ImageSourceNative \*source, Image\_String \*key, uint32\_t value)](capi-image-source-native-h.md#oh_imagesourcenative_modifyimagepropertylong) | 修改图像属性中长整型的值。 |
| [Image\_ErrorCode OH\_ImageSourceNative\_ModifyImagePropertyDouble(OH\_ImageSourceNative \*source, Image\_String \*key, double value)](capi-image-source-native-h.md#oh_imagesourcenative_modifyimagepropertydouble) | 修改图像属性中浮点型的值。 |
| [Image\_ErrorCode OH\_ImageSourceNative\_ModifyImagePropertyIntArray(OH\_ImageSourceNative \*source, Image\_String \*key, int32\_t \*value, size\_t size)](capi-image-source-native-h.md#oh_imagesourcenative_modifyimagepropertyintarray) | 修改图像属性中整型数组型的值。 |
| [Image\_ErrorCode OH\_ImageSourceNative\_ModifyImagePropertyDoubleArray(OH\_ImageSourceNative \*source, Image\_String \*key, double \*value, size\_t size)](capi-image-source-native-h.md#oh_imagesourcenative_modifyimagepropertydoublearray) | 修改图像属性中浮点型数组型的值。 |
| [Image\_ErrorCode OH\_ImageSourceNative\_ModifyImagePropertyBlob(OH\_ImageSourceNative \*source, Image\_String \*key, void \*value, size\_t size)](capi-image-source-native-h.md#oh_imagesourcenative_modifyimagepropertyblob) | 修改图像属性中二进制对象的值。 |
| [Image\_ErrorCode OH\_ImageSourceNative\_GetImagePropertyWithNull(OH\_ImageSourceNative \*source, Image\_String \*key, Image\_String \*value)](capi-image-source-native-h.md#oh_imagesourcenative_getimagepropertywithnull) | 获取图像属性值。输出的value.data以字符串结束符'\0'结尾。 |
| [Image\_ErrorCode OH\_ImageSourceNative\_ModifyImageProperty(OH\_ImageSourceNative \*source, Image\_String \*key, Image\_String \*value)](capi-image-source-native-h.md#oh_imagesourcenative_modifyimageproperty) | 通过指定的键修改图片属性的值。 |
| [Image\_ErrorCode OH\_ImageSourceNative\_GetFrameCount(OH\_ImageSourceNative \*source, uint32\_t \*frameCount)](capi-image-source-native-h.md#oh_imagesourcenative_getframecount) | 获取图像帧数。 |
| [Image\_ErrorCode OH\_ImageSourceNative\_GetSupportedFormats(Image\_MimeType \*\*supportedFormats, size\_t \*length)](capi-image-source-native-h.md#oh_imagesourcenative_getsupportedformats) | 获取支持解码的图片格式。 |
| [Image\_ErrorCode OH\_ImageSourceNative\_Release(OH\_ImageSourceNative \*source)](capi-image-source-native-h.md#oh_imagesourcenative_release) | 释放OH\_ImageSourceNative指针。 |
| [Image\_ErrorCode OH\_DecodingOptionsForPicture\_Create(OH\_DecodingOptionsForPicture \*\*options)](capi-image-source-native-h.md#oh_decodingoptionsforpicture_create) | 创建OH\_DecodingOptionsForPicture指针。 |
| [Image\_ErrorCode OH\_DecodingOptionsForPicture\_GetDesiredAuxiliaryPictures(OH\_DecodingOptionsForPicture \*options, Image\_AuxiliaryPictureType \*\*desiredAuxiliaryPictures, size\_t \*length)](capi-image-source-native-h.md#oh_decodingoptionsforpicture_getdesiredauxiliarypictures) | 获取解码时设置的期望辅助图（期望解码出的picture包含的辅助图）。 |
| [Image\_ErrorCode OH\_DecodingOptionsForPicture\_SetDesiredAuxiliaryPictures(OH\_DecodingOptionsForPicture \*options, Image\_AuxiliaryPictureType \*desiredAuxiliaryPictures, size\_t length)](capi-image-source-native-h.md#oh_decodingoptionsforpicture_setdesiredauxiliarypictures) | 设置解码选项中的期望辅助图。 |
| [Image\_ErrorCode OH\_DecodingOptionsForPicture\_Release(OH\_DecodingOptionsForPicture \*options)](capi-image-source-native-h.md#oh_decodingoptionsforpicture_release) | 释放OH\_DecodingOptionsForPicture指针。 |

## 枚举类型说明

PhonePC/2in1TabletTVWearable

### IMAGE\_DYNAMIC\_RANGE

PhonePC/2in1TabletTVWearable

```
1. enum IMAGE_DYNAMIC_RANGE
```

**描述**

解码指定期望动态范围。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| IMAGE\_DYNAMIC\_RANGE\_AUTO = 0 | 根据图片自适应处理。 |
| IMAGE\_DYNAMIC\_RANGE\_SDR = 1 | 标准动态范围。 |
| IMAGE\_DYNAMIC\_RANGE\_HDR = 2 | 高动态范围。 |

### IMAGE\_ALLOCATOR\_TYPE

PhonePC/2in1TabletTVWearable

```
1. enum IMAGE_ALLOCATOR_TYPE
```

**描述**

用于分配PixelMap内存的分配器类型。

**起始版本：** 15

| 枚举项 | 描述 |
| --- | --- |
| IMAGE\_ALLOCATOR\_TYPE\_AUTO = 0 | 由系统决定使用DMA内存或共享内存来创建PixelMap。 |
| IMAGE\_ALLOCATOR\_TYPE\_DMA = 1 | 使用DMA内存来创建PixelMap。 |
| IMAGE\_ALLOCATOR\_TYPE\_SHARE\_MEMORY = 2 | 使用共享内存来创建PixelMap。 |

### Image\_CropAndScaleStrategy

PhonePC/2in1TabletTVWearable

```
1. enum Image_CropAndScaleStrategy
```

**描述**

在同时指定desiredSize和desiredRegion时执行裁剪和缩放的策略。

如果在配置解码选项[OH\_DecodingOptions](capi-image-nativemodule-oh-decodingoptions.md)时，未填入参数Image\_CropAndScaleStrategy，并且同时设置了desiredRegion和desiredSize，由于系统对于不同图片格式采用的解码算法不同，最终解码效果将略有差异。

例如原始图片大小200x200，传入desiredSize:{width: 150, height: 150}，desiredRegion:{x: 0, y: 0, width: 100, height: 100}，即预期解码原图左上角1/4区域，最终将pixelMap大小缩放至150x150返回。

对于jpeg、webp图片（部分dng图片解码时会优先解码图片中的jpeg预览图，在此场景下也会被视为jpeg图片格式）会先进行下采样，例如按照7/8下采样，再基于175x175的图片大小进行区域裁剪，因此最终的区域内容稍大于原图的左上角1/4区域。

对于svg图片，由于是矢量图，可以任意缩放不损失清晰度，在解码时会根据desiredSize与原图Size的比例选择缩放比例，在基于缩放后的图片大小进行区域裁剪，因此最终返回的解码区域会有所差异。

针对该场景，建议在解码选项同时设置了desiredRegion与desiredSize时，参数Image\_CropAndScaleStrategy应传入CROP\_FIRST参数保证效果一致。

**起始版本：** 18

| 枚举项 | 描述 |
| --- | --- |
| IMAGE\_CROP\_AND\_SCALE\_STRATEGY\_SCALE\_FIRST = 1 | 先缩放，后裁剪。 |
| IMAGE\_CROP\_AND\_SCALE\_STRATEGY\_CROP\_FIRST = 2 | 先裁剪，后缩放。 |

## 函数说明

PhonePC/2in1TabletTVWearable

### OH\_ImageSourceInfo\_Create()

PhonePC/2in1TabletTVWearable

```
1. Image_ErrorCode OH_ImageSourceInfo_Create(OH_ImageSource_Info **info)
```

**描述**

创建OH\_ImageSource\_Info指针。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ImageSource\_Info](capi-image-nativemodule-imagesource-info.md) \*\*info | 被操作的OH\_ImageSource\_Info指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_BAD\_PARAMETER：参数错误。 |

### OH\_ImageSourceInfo\_GetWidth()

PhonePC/2in1TabletTVWearable

```
1. Image_ErrorCode OH_ImageSourceInfo_GetWidth(OH_ImageSource_Info *info, uint32_t *width)
```

**描述**

获取图片的宽。对于没有width标签的SVG图片，返回默认值0。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ImageSource\_Info](capi-image-nativemodule-imagesource-info.md) \*info | 被操作的OH\_ImageSource\_Info指针。 |
| uint32\_t \*width | 图片的宽，单位：像素。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_BAD\_PARAMETER：参数错误。 |

### OH\_ImageSourceInfo\_GetHeight()

PhonePC/2in1TabletTVWearable

```
1. Image_ErrorCode OH_ImageSourceInfo_GetHeight(OH_ImageSource_Info *info, uint32_t *height)
```

**描述**

获取图片的高。对于没有height标签的SVG图片，返回默认值0。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ImageSource\_Info](capi-image-nativemodule-imagesource-info.md) \*info | 被操作的OH\_ImageSource\_Info指针。 |
| uint32\_t \*height | 图片的高，单位：像素 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_BAD\_PARAMETER：参数错误。 |

### OH\_ImageSourceInfo\_GetDynamicRange()

PhonePC/2in1TabletTVWearable

```
1. Image_ErrorCode OH_ImageSourceInfo_GetDynamicRange(OH_ImageSource_Info *info, bool *isHdr)
```

**描述**

获取图片是否为高动态范围的信息。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ImageSource\_Info](capi-image-nativemodule-imagesource-info.md) \*info | 被操作的OH\_ImageSource\_Info指针。 |
| bool \*isHdr | 表示是否为高动态范围（HDR）的信息。true表示是高动态范围的信息，false表示不是高动态范围的信息。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_BAD\_PARAMETER：参数校验错误。 |

### OH\_ImageSourceInfo\_GetMimeType()

PhonePC/2in1TabletTVWearable

```
1. Image_ErrorCode OH_ImageSourceInfo_GetMimeType(OH_ImageSource_Info *info, Image_MimeType *mimetype)
```

**描述**

获取图片源的MIME类型。

说明

* [mimeType结构体的成员变量](capi-image-nativemodule-image-string.md#成员变量)data为char \*类型指针，其指向info结构体内部持有的mimeType地址，释放info会导致该地址对应的内存也被释放。
* 开发者可以自行深拷贝一份mimeType.data，或者等mimeType使用完成后再释放info，以免出现乱码现象。
* mimeType.data没有以'\0'结尾，需要配合mimeType.size一起使用。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ImageSource\_Info](capi-image-nativemodule-imagesource-info.md) \*info | OH\_ImageSource\_Info指针。 |
| [Image\_MimeType](capi-image-nativemodule-image-string.md) \*mimeType | 图片源的MIME类型。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_SOURCE\_INVALID\_PARAMETER：参数错误，INFO或者MIME类型为空。 |

### OH\_ImageSourceInfo\_Release()

PhonePC/2in1TabletTVWearable

```
1. Image_ErrorCode OH_ImageSourceInfo_Release(OH_ImageSource_Info *info)
```

**描述**

释放OH\_ImageSource\_Info指针。调用该接口之后，与OH\_ImageSourceInfo结构体相关的属性均会被释放。因此在调用该接口前，请务必确认相关属性已不再被需要或对相关属性已完成深拷贝操作。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ImageSource\_Info](capi-image-nativemodule-imagesource-info.md) \*info | 被操作的OH\_ImageSource\_Info指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_BAD\_PARAMETER：参数错误。 |

### OH\_DecodingOptions\_Create()

PhonePC/2in1TabletTVWearable

```
1. Image_ErrorCode OH_DecodingOptions_Create(OH_DecodingOptions **options)
```

**描述**

创建OH\_DecodingOptions指针。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_DecodingOptions](capi-image-nativemodule-oh-decodingoptions.md) \*\*options | 被操作的OH\_DecodingOptions指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_BAD\_PARAMETER：参数错误。 |

### OH\_DecodingOptions\_GetPixelFormat()

PhonePC/2in1TabletTVWearable

```
1. Image_ErrorCode OH_DecodingOptions_GetPixelFormat(OH_DecodingOptions *options, int32_t *pixelFormat)
```

**描述**

获取pixel格式。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_DecodingOptions](capi-image-nativemodule-oh-decodingoptions.md) \*options | 被操作的OH\_DecodingOptions指针。 |
| int32\_t \*pixelFormat | pixel格式[PIXEL\_FORMAT](capi-pixelmap-native-h.md#pixel_format)，默认值为RGBA\_8888。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_BAD\_PARAMETER：参数错误。 |

### OH\_DecodingOptions\_SetPixelFormat()

PhonePC/2in1TabletTVWearable

```
1. Image_ErrorCode OH_DecodingOptions_SetPixelFormat(OH_DecodingOptions *options,int32_t pixelFormat)
```

**描述**

设置pixel格式。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_DecodingOptions](capi-image-nativemodule-oh-decodingoptions.md) \*options | 被操作的OH\_DecodingOptions指针。 |
| int32\_t pixelFormat | pixel格式[PIXEL\_FORMAT](capi-pixelmap-native-h.md#pixel_format)，默认值为RGBA\_8888。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_BAD\_PARAMETER：参数错误。 |

### OH\_DecodingOptions\_GetIndex()

PhonePC/2in1TabletTVWearable

```
1. Image_ErrorCode OH_DecodingOptions_GetIndex(OH_DecodingOptions *options, uint32_t *index)
```

**描述**

获取解码图片序号。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_DecodingOptions](capi-image-nativemodule-oh-decodingoptions.md) \*options | 被操作的OH\_DecodingOptions指针。 |
| uint32\_t \*index | 解码图片序号，默认值为0。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_BAD\_PARAMETER：参数错误。 |

### OH\_DecodingOptions\_SetIndex()

PhonePC/2in1TabletTVWearable

```
1. Image_ErrorCode OH_DecodingOptions_SetIndex(OH_DecodingOptions *options, uint32_t index)
```

**描述**

设置解码图片序号。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_DecodingOptions](capi-image-nativemodule-oh-decodingoptions.md) \*options | 被操作的OH\_DecodingOptions指针。 |
| uint32\_t index | 解码图片序号，默认值为0。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_BAD\_PARAMETER：参数错误。 |

### OH\_DecodingOptions\_GetRotate()

PhonePC/2in1TabletTVWearable

```
1. Image_ErrorCode OH_DecodingOptions_GetRotate(OH_DecodingOptions *options, float *rotate)
```

**描述**

获取旋转角度。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_DecodingOptions](capi-image-nativemodule-oh-decodingoptions.md) \*options | 被操作的OH\_DecodingOptions指针。 |
| float \*rotate | 旋转角度，单位为deg，默认值为0。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_BAD\_PARAMETER：参数错误。 |

### OH\_DecodingOptions\_SetRotate()

PhonePC/2in1TabletTVWearable

```
1. Image_ErrorCode OH_DecodingOptions_SetRotate(OH_DecodingOptions *options, float rotate)
```

**描述**

设置旋转角度。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_DecodingOptions](capi-image-nativemodule-oh-decodingoptions.md) \*options | 被操作的OH\_DecodingOptions指针。 |
| float rotate | 旋转角度，单位为deg，默认值为0。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_BAD\_PARAMETER：参数错误。 |

### OH\_DecodingOptions\_GetDesiredSize()

PhonePC/2in1TabletTVWearable

```
1. Image_ErrorCode OH_DecodingOptions_GetDesiredSize(OH_DecodingOptions *options, Image_Size *desiredSize)
```

**描述**

获取期望输出大小。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_DecodingOptions](capi-image-nativemodule-oh-decodingoptions.md) \*options | 被操作的OH\_DecodingOptions指针。 |
| [Image\_Size](capi-image-nativemodule-image-size.md) \*desiredSize | 期望输出大小，默认为原始图片尺寸。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_BAD\_PARAMETER：参数错误。 |

### OH\_DecodingOptions\_SetDesiredSize()

PhonePC/2in1TabletTVWearable

```
1. Image_ErrorCode OH_DecodingOptions_SetDesiredSize(OH_DecodingOptions *options, Image_Size *desiredSize)
```

**描述**

设置期望输出大小。desiredSize参数决定解码得到的PixelMap大小，且宽、高须为正整数。若与原尺寸比例不一致，则会进行拉伸/缩放到指定尺寸。默认为原始尺寸。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_DecodingOptions](capi-image-nativemodule-oh-decodingoptions.md) \*options | 被操作的OH\_DecodingOptions指针。 |
| [Image\_Size](capi-image-nativemodule-image-size.md) \*desiredSize | 期望输出大小，默认为原始图片尺寸。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_BAD\_PARAMETER：参数错误。 |

### OH\_DecodingOptions\_GetDesiredRegion()

PhonePC/2in1TabletTVWearable

```
1. Image_ErrorCode OH_DecodingOptions_GetDesiredRegion(OH_DecodingOptions *options, Image_Region *desiredRegion)
```

**描述**

获取解码区域。

由于对应SetDesiredRegion接口无法满足区域解码诉求，从API version 19开始，推荐配套使用[OH\_DecodingOptions\_GetCropRegion](capi-image-source-native-h.md#oh_decodingoptions_getcropregion)接口替代。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_DecodingOptions](capi-image-nativemodule-oh-decodingoptions.md) \*options | 被操作的OH\_DecodingOptions指针。 |
| [Image\_Region](capi-image-nativemodule-image-region.md) \*desiredRegion | 解码区域，默认为完整图片大小的区域。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_BAD\_PARAMETER：参数错误。 |

### OH\_DecodingOptions\_SetDesiredRegion()

PhonePC/2in1TabletTVWearable

```
1. Image_ErrorCode OH_DecodingOptions_SetDesiredRegion(OH_DecodingOptions *options, Image_Region *desiredRegion)
```

**描述**

设置解码区域。

实际解码结果会按照原图解码，无区域解码效果。从API version 19开始，推荐使用接口[OH\_DecodingOptions\_SetCropRegion](capi-image-source-native-h.md#oh_decodingoptions_setcropregion)替代。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_DecodingOptions](capi-image-nativemodule-oh-decodingoptions.md) \*options | 被操作的OH\_DecodingOptions指针。 |
| [Image\_Region](capi-image-nativemodule-image-region.md) \*desiredRegion | 解码区域，默认为完整图片大小的区域。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_BAD\_PARAMETER：参数错误。 |

### OH\_DecodingOptions\_GetDesiredDynamicRange()

PhonePC/2in1TabletTVWearable

```
1. Image_ErrorCode OH_DecodingOptions_GetDesiredDynamicRange(OH_DecodingOptions *options, int32_t *desiredDynamicRange)
```

**描述**

获取解码时设置的期望动态范围。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_DecodingOptions](capi-image-nativemodule-oh-decodingoptions.md) \*options | 被操作的OH\_DecodingOptions指针。 |
| int32\_t \*desiredDynamicRange | 期望的动态范围值[IMAGE\_DYNAMIC\_RANGE](capi-image-source-native-h.md#image_dynamic_range)，默认值为SDR。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_BAD\_PARAMETER：参数校验错误。 |

### OH\_DecodingOptions\_SetDesiredDynamicRange()

PhonePC/2in1TabletTVWearable

```
1. Image_ErrorCode OH_DecodingOptions_SetDesiredDynamicRange(OH_DecodingOptions *options, int32_t desiredDynamicRange)
```

**描述**

设置解码时的期望动态范围。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_DecodingOptions](capi-image-nativemodule-oh-decodingoptions.md) \*options | 被操作的OH\_DecodingOptions指针。 |
| int32\_t desiredDynamicRange | 期望的动态范围值[IMAGE\_DYNAMIC\_RANGE](capi-image-source-native-h.md#image_dynamic_range)，默认值为SDR。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_BAD\_PARAMETER：参数校验错误。 |

### OH\_DecodingOptions\_GetDesiredColorSpace()

PhonePC/2in1TabletTVWearable

```
1. Image_ErrorCode OH_DecodingOptions_GetDesiredColorSpace(OH_DecodingOptions *options, int32_t *colorSpace)
```

**描述**

获取解码参数中设置的色彩空间。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_DecodingOptions](capi-image-nativemodule-oh-decodingoptions.md) \*options | 解码参数。 |
| int32\_t \*colorSpace | 解码参数中设置的色彩空间，参考[ColorSpaceName](capi-native-color-space-manager-h.md#colorspacename)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_SOURCE\_INVALID\_PARAMETER：参数错误。options或colorSpace为空。 |

### OH\_DecodingOptions\_SetDesiredColorSpace()

PhonePC/2in1TabletTVWearable

```
1. Image_ErrorCode OH_DecodingOptions_SetDesiredColorSpace(OH_DecodingOptions *options, int32_t colorSpace)
```

**描述**

设置解码期望得到的色彩空间。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_DecodingOptions](capi-image-nativemodule-oh-decodingoptions.md) \*options | 解码参数。 |
| int32\_t colorSpace | 期望的色彩空间，参考[ColorSpaceName](capi-native-color-space-manager-h.md#colorspacename)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_SOURCE\_INVALID\_PARAMETER：参数错误。options为空，或者传入了不支持的colorSpace。 |

### OH\_DecodingOptions\_SetCropAndScaleStrategy()

PhonePC/2in1TabletTVWearable

```
1. Image_ErrorCode OH_DecodingOptions_SetCropAndScaleStrategy(OH_DecodingOptions *options, int32_t cropAndScaleStrategy)
```

**描述**

设置解码选项的裁剪和缩放策略。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_DecodingOptions](capi-image-nativemodule-oh-decodingoptions.md) \*options | 被操作的OH\_DecodingOptions指针。 |
| int32\_t cropAndScaleStrategy | 在同时指定desiredSize和desiredRegion时执行裁剪和缩放的策略。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_BAD\_PARAMETER：options空指针或者cropAndScaleStrategy取值不在Image\_CropAndScaleStrategy枚举值定义之中。 |

### OH\_DecodingOptions\_GetCropAndScaleStrategy()

PhonePC/2in1TabletTVWearable

```
1. Image_ErrorCode OH_DecodingOptions_GetCropAndScaleStrategy(OH_DecodingOptions *options, int32_t *cropAndScaleStrategy)
```

**描述**

获取解码选项的裁剪和缩放策略。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_DecodingOptions](capi-image-nativemodule-oh-decodingoptions.md) \*options | 被操作的OH\_DecodingOptions指针。 |
| int32\_t \*cropAndScaleStrategy | 指向在同时指定desiredSize和desiredRegion时执行裁剪和缩放策略的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_BAD\_PARAMETER：options或者cropAndScaleStrategy为空指针。 |

### OH\_DecodingOptions\_GetCropRegion()

PhonePC/2in1TabletTVWearable

```
1. Image_ErrorCode OH_DecodingOptions_GetCropRegion(OH_DecodingOptions *options, Image_Region *cropRegion)
```

**描述**

获取解码参数中的裁剪区域。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_DecodingOptions](capi-image-nativemodule-oh-decodingoptions.md) \*options | 指向解码参数指针。 |
| [Image\_Region](capi-image-nativemodule-image-region.md) \*cropRegion | 指向要裁剪的目标区域指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：操作成功。  IMAGE\_SOURCE\_INVALID\_PARAMETER：options或cropRegion为空。 |

### OH\_DecodingOptions\_SetCropRegion()

PhonePC/2in1TabletTVWearable

```
1. Image_ErrorCode OH_DecodingOptions_SetCropRegion(OH_DecodingOptions *options, Image_Region *cropRegion)
```

**描述**

设置解码参数中的裁剪区域。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_DecodingOptions](capi-image-nativemodule-oh-decodingoptions.md) \*options | 指向解码参数指针。 |
| [Image\_Region](capi-image-nativemodule-image-region.md) \*cropRegion | 指向要裁剪的目标区域指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：操作成功。  IMAGE\_SOURCE\_INVALID\_PARAMETER：options或cropRegion为空。 |

### OH\_DecodingOptions\_Release()

PhonePC/2in1TabletTVWearable

```
1. Image_ErrorCode OH_DecodingOptions_Release(OH_DecodingOptions *options)
```

**描述**

释放OH\_DecodingOptions指针。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_DecodingOptions](capi-image-nativemodule-oh-decodingoptions.md) \*options | 被操作的OH\_DecodingOptions指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_BAD\_PARAMETER：参数错误。 |

### OH\_ImageSourceNative\_CreateFromUri()

PhonePC/2in1TabletTVWearable

```
1. Image_ErrorCode OH_ImageSourceNative_CreateFromUri(char *uri, size_t uriSize, OH_ImageSourceNative **res)
```

**描述**

通过uri创建OH\_ImageSourceNative指针。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| char \*uri | 指向图像源URI的指针。只接受文件URI或Base64 URI。当前文件资源只支持绝对路径。 |
| size\_t uriSize | URI长度。 |
| [OH\_ImageSourceNative](capi-image-nativemodule-oh-imagesourcenative.md) \*\*res | 指向c++本地层创建的OH\_ImageSourceNative对象的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_BAD\_PARAMETER：参数错误。  IMAGE\_BAD\_SOURCE：解码数据源异常。 |

### OH\_ImageSourceNative\_CreateFromFd()

PhonePC/2in1TabletTVWearable

```
1. Image_ErrorCode OH_ImageSourceNative_CreateFromFd(int32_t fd, OH_ImageSourceNative **res)
```

**描述**

通过fd创建OH\_ImageSourceNative指针。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| int32\_t fd | 文件描述符fd。 |
| [OH\_ImageSourceNative](capi-image-nativemodule-oh-imagesourcenative.md) \*\*res | 指向c++本地层创建的OH\_ImageSourceNative对象的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_BAD\_PARAMETER：参数错误。 |

### OH\_ImageSourceNative\_CreateFromData()

PhonePC/2in1TabletTVWearable

```
1. Image_ErrorCode OH_ImageSourceNative_CreateFromData(uint8_t *data, size_t dataSize, OH_ImageSourceNative **res)
```

**描述**

通过缓冲区数据创建OH\_ImageSourceNative指针。

data数据应该是未解码的数据，不要传入类似于RGBA，YUV的像素buffer数据。

如果想通过像素buffer数据创建pixelMap，可以调用[OH\_PixelmapNative\_CreatePixelmap](capi-pixelmap-native-h.md#oh_pixelmapnative_createpixelmap)这一类接口。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| uint8\_t \*data | 图像缓冲区数据。 |
| size\_t dataSize | 图像缓冲区数据长度。 |
| [OH\_ImageSourceNative](capi-image-nativemodule-oh-imagesourcenative.md) \*\*res | 指向c++本地层创建的OH\_ImageSourceNative对象的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_BAD\_PARAMETER：参数错误。  IMAGE\_BAD\_SOURCE：解码数据源异常。 |

### OH\_ImageSourceNative\_CreateFromDataWithUserBuffer()

PhonePC/2in1TabletTVWearable

```
1. Image_ErrorCode OH_ImageSourceNative_CreateFromDataWithUserBuffer(uint8_t *data, size_t datalength, OH_ImageSourceNative **imageSource)
```

**描述**

由数据缓存创建图片源。传入的数据缓存将在图片源对象中直接访问，在图片源对象的生命周期内，数据缓存需要保持可用。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| uint8\_t \*data | 数据缓存指针。 |
| size\_t datalength | 数据缓存长度。 |
| [OH\_ImageSourceNative](capi-image-nativemodule-oh-imagesourcenative.md) \*\*imageSource | 图片源的二级指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_SOURCE\_INVALID\_PARAMETER：data或imageSource是空指针，datalength为0。 |

### OH\_ImageSourceNative\_CreateFromRawFile()

PhonePC/2in1TabletTVWearable

```
1. Image_ErrorCode OH_ImageSourceNative_CreateFromRawFile(RawFileDescriptor *rawFile, OH_ImageSourceNative **res)
```

**描述**

通过图像资源文件的RawFileDescriptor创建OH\_ImageSourceNative指针。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [RawFileDescriptor](capi-rawfile-rawfiledescriptor.md) \*rawFile | 指示raw文件的文件描述符。 |
| [OH\_ImageSourceNative](capi-image-nativemodule-oh-imagesourcenative.md) \*\*res | 指向c++本地层创建的OH\_ImageSourceNative对象的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_BAD\_PARAMETER：参数错误。 |

### OH\_ImageSourceNative\_CreatePixelmap()

PhonePC/2in1TabletTVWearable

```
1. Image_ErrorCode OH_ImageSourceNative_CreatePixelmap(OH_ImageSourceNative *source, OH_DecodingOptions *options, OH_PixelmapNative **pixelmap)
```

**描述**

通过图片解码参数创建OH\_PixelmapNative指针。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ImageSourceNative](capi-image-nativemodule-oh-imagesourcenative.md) \*source | 被操作的OH\_ImageSourceNative指针。 |
| [OH\_DecodingOptions](capi-image-nativemodule-oh-decodingoptions.md) \*options | 解码参数。 |
| [OH\_PixelmapNative](capi-image-nativemodule-oh-pixelmapnative.md) \*\*pixelmap | 指向c++本地层创建的OH\_PixelmapNative对象的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_BAD\_PARAMETER：参数错误。 |

### OH\_ImageSourceNative\_CreatePixelmapUsingAllocator()

PhonePC/2in1TabletTVWearable

```
1. Image_ErrorCode OH_ImageSourceNative_CreatePixelmapUsingAllocator(OH_ImageSourceNative *source, OH_DecodingOptions *options, IMAGE_ALLOCATOR_TYPE allocator, OH_PixelmapNative **pixelmap)
```

**描述**

根据解码参数创建一个PixelMap，PixelMap使用的内存类型可以通过allocatorType来指定。

默认情况下，系统会根据图像类型、图像大小、平台能力等选择内存类型。在处理通过此接口返回的PixelMap时，请始终考虑步幅（stride）的影响。

**起始版本：** 15

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ImageSourceNative](capi-image-nativemodule-oh-imagesourcenative.md) \*source | 被操作的OH\_ImageSourceNative指针。 |
| [OH\_DecodingOptions](capi-image-nativemodule-oh-decodingoptions.md) \*options | 解码参数。 |
| [IMAGE\_ALLOCATOR\_TYPE](capi-image-source-native-h.md#image_allocator_type) allocator | 指示返回的PixelMap将使用哪种内存类型。 |
| [OH\_PixelmapNative](capi-image-nativemodule-oh-pixelmapnative.md) \*\*pixelmap | 指向c++本地层创建的OH\_PixelmapNative对象的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_BAD\_PARAMETER：参数错误。  IMAGE\_BAD\_SOURCE：数据源异常。  IMAGE\_SOURCE\_UNSUPPORTED\_MIME\_TYPE：不支持的MIME类型。  IMAGE\_SOURCE\_TOO\_LARGE：图像过大。  IMAGE\_SOURCE\_UNSUPPORTED\_ALLOCATOR\_TYPE：不支持的分配器类型。例如，使用共享内存解码HDR图像，因为只有DMA支持HDR元数据。  IMAGE\_SOURCE\_UNSUPPORTED\_OPTIONS：不支持的选项。例如，无法将图像转换为所需的像素格式。  IMAGE\_DECODE\_FAILED：解码失败。  IMAGE\_SOURCE\_ALLOC\_FAILED：内存分配失败。 |

### OH\_ImageSourceNative\_CreatePixelmapList()

PhonePC/2in1TabletTVWearable

```
1. Image_ErrorCode OH_ImageSourceNative_CreatePixelmapList(OH_ImageSourceNative *source, OH_DecodingOptions *options, OH_PixelmapNative *resVecPixMap[], size_t size)
```

**描述**

通过图片解码参数创建OH\_PixelmapNative数组。

注意，此接口会一次性解码全部帧，当帧数过多或单帧图像过大时，会占用较大内存，造成系统内存紧张，此种情况推荐使用Image组件显示动图，Image组件采用逐帧解码，占用内存比此接口少。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ImageSourceNative](capi-image-nativemodule-oh-imagesourcenative.md) \*source | 被操作的OH\_ImageSourceNative指针。 |
| [OH\_DecodingOptions](capi-image-nativemodule-oh-decodingoptions.md) \*options | 解码参数。 |
| [OH\_PixelmapNative](capi-image-nativemodule-oh-pixelmapnative.md) \*resVecPixMap[] | 指向c++本地层创建的OH\_PixelmapNative对象的指针数组。 |
| size\_t size | 数组长度。 用户可以使用[OH\_ImageSourceNative\_GetFrameCount](capi-image-source-native-h.md#oh_imagesourcenative_getframecount)获取。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_BAD\_PARAMETER：参数错误。  IMAGE\_UNSUPPORTED\_OPERATION：操作不支持。 |

### OH\_ImageSourceNative\_CreatePicture()

PhonePC/2in1TabletTVWearable

```
1. Image_ErrorCode OH_ImageSourceNative_CreatePicture(OH_ImageSourceNative *source, OH_DecodingOptionsForPicture *options, OH_PictureNative **picture)
```

**描述**

通过图片解码创建OH\_PictureNative指针。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ImageSourceNative](capi-image-nativemodule-oh-imagesourcenative.md) \*source | 被操作的OH\_ImageSourceNative指针。 |
| [OH\_DecodingOptionsForPicture](pi-image-nativemodule-oh-decodingoptionsforpicture.md) \*options | 解码参数。 |
| [OH\_PictureNative](capi-image-nativemodule-oh-picturenative.md) \*\*picture | 指向c++本地层创建的OH\_PictureNative对象的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_BAD\_PARAMETER：参数错误。  IMAGE\_DECODE\_FAILED：解码失败。 |

### OH\_ImageSourceNative\_CreatePictureAtIndex()

PhonePC/2in1TabletTVWearable

```
1. Image_ErrorCode OH_ImageSourceNative_CreatePictureAtIndex(OH_ImageSourceNative *source, uint32_t index, OH_PictureNative **picture)
```

**描述**

通过指定序号的图片解码创建OH\_PictureNative指针。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ImageSourceNative](capi-image-nativemodule-oh-imagesourcenative.md) \*source | 被操作的OH\_ImageSourceNative指针。 |
| uint32\_t index | 解码图片序号。 |
| [OH\_PictureNative](capi-image-nativemodule-oh-picturenative.md) \*\*picture | 指向c++本地层创建的OH\_PictureNative对象的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_BAD\_SOURCE：数据源异常。  IMAGE\_SOURCE\_UNSUPPORTED\_MIME\_TYPE：不支持的MIME类型。  IMAGE\_SOURCE\_TOO\_LARGE：图像过大。  IMAGE\_SOURCE\_UNSUPPORTED\_OPTIONS：不支持的选项。例如，无效的图片序号。  IMAGE\_DECODE\_FAILED：解码失败。 |

### OH\_ImageSourceNative\_GetDelayTimeList()

PhonePC/2in1TabletTVWearable

```
1. Image_ErrorCode OH_ImageSourceNative_GetDelayTimeList(OH_ImageSourceNative *source, int32_t *delayTimeList, size_t size)
```

**描述**

获取图像延迟时间数组。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ImageSourceNative](capi-image-nativemodule-oh-imagesourcenative.md) \*source | 被操作的OH\_ImageSourceNative指针。 |
| int32\_t \*delayTimeList | 指向获得的延迟时间列表的指针。它不能是空指针。 |
| size\_t size | delayTimeList的大小。用户可以从[OH\_ImageSourceNative\_GetFrameCount](capi-image-source-native-h.md#oh_imagesourcenative_getframecount)获得大小。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_BAD\_PARAMETER：参数错误。 |

### OH\_ImageSourceNative\_GetImageInfo()

PhonePC/2in1TabletTVWearable

```
1. Image_ErrorCode OH_ImageSourceNative_GetImageInfo(OH_ImageSourceNative *source, int32_t index, OH_ImageSource_Info *info)
```

**描述**

获取指定序号的图片信息。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ImageSourceNative](capi-image-nativemodule-oh-imagesourcenative.md) \*source | 被操作的OH\_ImageSourceNative指针。 |
| int32\_t index | 图片序号。对GIF图片可传入[0,N-1],N表示GIF的帧数。对只有一帧数据的图片格式，可传入0。 |
| [OH\_ImageSource\_Info](capi-image-nativemodule-imagesource-info.md) \*info | 指向获取的图像源信息的OH\_ImageSource\_Info指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_BAD\_PARAMETER：参数错误。 |

### OH\_ImageSourceNative\_GetImageProperty()

PhonePC/2in1TabletTVWearable

```
1. Image_ErrorCode OH_ImageSourceNative_GetImageProperty(OH_ImageSourceNative *source, Image_String *key, Image_String *value)
```

**描述**

获取图片指定属性键的值。

该接口获取到的value.data缺少字符串结束符'\0'，请谨慎使用。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ImageSourceNative](capi-image-nativemodule-oh-imagesourcenative.md) \*source | 被操作的OH\_ImageSourceNative指针。OH\_ImageSourceNative使用完成后需要主动释放，参见[OH\_ImageSourceNative\_Release](capi-image-source-native-h.md#oh_imagesourcenative_release)。 |
| [Image\_String](capi-image-nativemodule-image-string.md) \*key | 指向属性的指针。key的取值范围请参考image\_common.h的[变量](capi-image-common-h.md#变量)中定义的OHOS\_IMAGE\_PROPERTY\_XXX系列常量。 |
| [Image\_String](capi-image-nativemodule-image-string.md) \*value | 指向获取的值的指针（输出参数）。调用本接口前，用户应将value->data置为空指针，并将value->size设为0。接口会为value->data自动分配所需内存，并对value->size赋值。完成对该内存的使用后，用户必须使用C标准库提供的free()函数释放value->data指向的内存，否则会出现内存泄漏。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_BAD\_PARAMETER：参数错误。 |

### OH\_ImageSourceNative\_GetImagePropertyShort()

PhonePC/2in1TabletTVWearable

```
1. Image_ErrorCode OH_ImageSourceNative_GetImagePropertyShort(OH_ImageSourceNative *source, Image_String *key, uint16_t *value)
```

**描述**

以短整型类型获取图像属性的值。

说明

读取DNG格式图片时，该接口对部分key有特殊处理。以下字段的字符串取值请参考[变量](capi-image-common-h.md#变量)中定义的OHOS\_IMAGE\_PROPERTY\_XXX系列常量的值：

* NewSubfileType、ImageWidth、ImageLength、DefaultCropSize、Orientation、Compression、PhotometricInterpretation、PlanarConfiguration、RowsPerStrip、StripOffsets、StripByteCounts、SamplesPerPixel、BitsPerSample、YCbCrCoefficients、YCbCrSubSampling、YCbCrPositioning、ReferenceBlackWhite、XResolution、YResolution、ResolutionUnit字段：返回主图相关的字段值。
* ImageUniqueID字段：根据规范进行校验，不符合规范时会返回空字符串。
* ExifVersion、FlashpixVersion、ColorSpace字段：当图片中不存在该标签时，返回错误码。
* DNGVersion字段：当版本号小于1.0.0.0时，统一返回1.0.0.0。
* GPSVersionID字段：当没有有效的GPS数据时，会清除GPS版本号并返回0。
* GPSAltitudeRef字段：当未设置GPSAltitude时，会设置为0xFFFFFFFF。
* ISOSpeedRatings字段：当该标签值为0或65535时，会优先使用推荐曝光指数，若不存在则依次使用标准输出灵敏度、ISO速度、曝光指数。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ImageSourceNative](capi-image-nativemodule-oh-imagesourcenative.md) \*source | 被查询属性的ImageSource。 |
| [Image\_String](capi-image-nativemodule-image-string.md) \*key | 被查询的属性。 |
| uint16\_t \*value | 被查询的属性的查询结果。输出参数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_SOURCE\_INVALID\_PARAMETER：source、key或value为nullptr。  IMAGE\_SOURCE\_UNSUPPORTED\_MIME\_TYPE：不支持查询当前mimetype的图像属性。  IMAGE\_SOURCE\_UNSUPPORTED\_METADATA：指定的元数据不存在，或者不是短整型的值。 |

### OH\_ImageSourceNative\_GetImagePropertyLong()

PhonePC/2in1TabletTVWearable

```
1. Image_ErrorCode OH_ImageSourceNative_GetImagePropertyLong(OH_ImageSourceNative *source, Image_String *key, uint32_t *value)
```

**描述**

以长整型类型获取图像属性的值。

说明

读取DNG格式图片时，该接口对部分key有特殊处理。以下字段的字符串取值请参考[变量](capi-image-common-h.md#变量)中定义的OHOS\_IMAGE\_PROPERTY\_XXX系列常量的值：

* NewSubfileType、ImageWidth、ImageLength、DefaultCropSize、Orientation、Compression、PhotometricInterpretation、PlanarConfiguration、RowsPerStrip、StripOffsets、StripByteCounts、SamplesPerPixel、BitsPerSample、YCbCrCoefficients、YCbCrSubSampling、YCbCrPositioning、ReferenceBlackWhite、XResolution、YResolution、ResolutionUnit字段：返回主图相关的字段值。
* ImageUniqueID字段：根据规范进行校验，不符合规范时会返回空字符串。
* ExifVersion、FlashpixVersion、ColorSpace字段：当图片中不存在该标签时，返回错误码。
* DNGVersion字段：当版本号小于1.0.0.0时，统一返回1.0.0.0。
* GPSVersionID字段：当没有有效的GPS数据时，会清除GPS版本号并返回0。
* GPSAltitudeRef字段：当未设置GPSAltitude时，会设置为0xFFFFFFFF。
* ISOSpeedRatings字段：当该标签值为0或65535时，会优先使用推荐曝光指数，若不存在则依次使用标准输出灵敏度、ISO速度、曝光指数。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ImageSourceNative](capi-image-nativemodule-oh-imagesourcenative.md) \*source | 被查询属性的ImageSource。 |
| [Image\_String](capi-image-nativemodule-image-string.md) \*key | 被查询的属性。 |
| uint32\_t \*value | 被查询属性的查询结果。输出参数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_SOURCE\_INVALID\_PARAMETER：source、key或value为nullptr。  IMAGE\_SOURCE\_UNSUPPORTED\_MIME\_TYPE：不支持查询当前mimetype的图像属性。  IMAGE\_SOURCE\_UNSUPPORTED\_METADATA：指定的元数据不存在，或者不是长整型的值。 |

### OH\_ImageSourceNative\_GetImagePropertyDouble()

PhonePC/2in1TabletTVWearable

```
1. Image_ErrorCode OH_ImageSourceNative_GetImagePropertyDouble(OH_ImageSourceNative *source, Image_String *key, double *value)
```

**描述**

以浮点型类型获取图像属性的值。

说明

读取DNG格式图片时，该接口对部分key有特殊处理。以下字段的字符串取值请参考[变量](capi-image-common-h.md#变量)中定义的OHOS\_IMAGE\_PROPERTY\_XXX系列常量的值：

* NewSubfileType、ImageWidth、ImageLength、DefaultCropSize、Orientation、Compression、PhotometricInterpretation、PlanarConfiguration、RowsPerStrip、StripOffsets、StripByteCounts、SamplesPerPixel、BitsPerSample、YCbCrCoefficients、YCbCrSubSampling、YCbCrPositioning、ReferenceBlackWhite、XResolution、YResolution、ResolutionUnit字段：返回主图相关的字段值。
* ImageUniqueID字段：根据规范进行校验，不符合规范时会返回空字符串。
* ExifVersion、FlashpixVersion、ColorSpace字段：当图片中不存在该标签时，返回错误码。
* DNGVersion字段：当版本号小于1.0.0.0时，统一返回1.0.0.0。
* GPSVersionID字段：当没有有效的GPS数据时，会清除GPS版本号并返回0。
* GPSAltitudeRef字段：当未设置GPSAltitude时，会设置为0xFFFFFFFF。
* ISOSpeedRatings字段：当该标签值为0或65535时，会优先使用推荐曝光指数，若不存在则依次使用标准输出灵敏度、ISO速度、曝光指数。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ImageSourceNative](capi-image-nativemodule-oh-imagesourcenative.md) \*source | 被查询属性的ImageSource。 |
| [Image\_String](capi-image-nativemodule-image-string.md) \*key | 被查询的属性。 |
| double \*value | 被查询属性的查询结果。输出参数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_SOURCE\_INVALID\_PARAMETER：source、key或value为nullptr。  IMAGE\_SOURCE\_UNSUPPORTED\_MIME\_TYPE：不支持查询当前mimetype的图像属性。  IMAGE\_SOURCE\_UNSUPPORTED\_METADATA：指定的元数据不存在，或者不是浮点型的值。 |

### OH\_ImageSourceNative\_GetImagePropertyArraySize()

PhonePC/2in1TabletTVWearable

```
1. Image_ErrorCode OH_ImageSourceNative_GetImagePropertyArraySize(OH_ImageSourceNative *source, Image_String *key, size_t *size)
```

**描述**

获取数组类型属性的数组长度或字符串类型属性的字符串长度。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ImageSourceNative](capi-image-nativemodule-oh-imagesourcenative.md) \*source | 被查询属性的ImageSource。 |
| [Image\_String](capi-image-nativemodule-image-string.md) \*key | 被查询的属性。 |
| size\_t \*size | 数组类型属性的数组长度，字符串类型属性的字符串长度。输出参数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_SOURCE\_INVALID\_PARAMETER：source、key或value为nullptr。  IMAGE\_SOURCE\_UNSUPPORTED\_MIME\_TYPE：不支持查询当前mimetype的图像属性。  IMAGE\_SOURCE\_UNSUPPORTED\_METADATA：指定的元数据不存在，或者不是数组或字符串类型的值。 |

### OH\_ImageSourceNative\_GetImagePropertyString()

PhonePC/2in1TabletTVWearable

```
1. Image_ErrorCode OH_ImageSourceNative_GetImagePropertyString(OH_ImageSourceNative *source, Image_String *key, char *value, size_t size)
```

**描述**

以字符串类型获取图像属性的值。

说明

读取DNG格式图片时，该接口对部分key有特殊处理。以下字段的字符串取值请参考[变量](capi-image-common-h.md#变量)中定义的OHOS\_IMAGE\_PROPERTY\_XXX系列常量的值：

* NewSubfileType、ImageWidth、ImageLength、DefaultCropSize、Orientation、Compression、PhotometricInterpretation、PlanarConfiguration、RowsPerStrip、StripOffsets、StripByteCounts、SamplesPerPixel、BitsPerSample、YCbCrCoefficients、YCbCrSubSampling、YCbCrPositioning、ReferenceBlackWhite、XResolution、YResolution、ResolutionUnit字段：返回主图相关的字段值。
* ImageUniqueID字段：根据规范进行校验，不符合规范时会返回空字符串。
* ExifVersion、FlashpixVersion、ColorSpace字段：当图片中不存在该标签时，返回错误码。
* DNGVersion字段：当版本号小于1.0.0.0时，统一返回1.0.0.0。
* GPSVersionID字段：当没有有效的GPS数据时，会清除GPS版本号并返回0。
* GPSAltitudeRef字段：当未设置GPSAltitude时，会设置为0xFFFFFFFF。
* ISOSpeedRatings字段：当该标签值为0或65535时，会优先使用推荐曝光指数，若不存在则依次使用标准输出灵敏度、ISO速度、曝光指数。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ImageSourceNative](capi-image-nativemodule-oh-imagesourcenative.md) \*source | 被查询属性的ImageSource。 |
| [Image\_String](capi-image-nativemodule-image-string.md) \*key | 被查询的属性。 |
| char \*value | 被查询属性的查询结果。输出参数。调用者需要管理内存应用程序并释放。 |
| size\_t size | 字符串长度。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_SOURCE\_INVALID\_PARAMETER：source、key或value为nullptr。  IMAGE\_SOURCE\_UNSUPPORTED\_MIME\_TYPE：不支持查询当前mimetype的图像属性。  IMAGE\_SOURCE\_UNSUPPORTED\_METADATA：指定的元数据不存在，或者不是字符串类型的值。 |

### OH\_ImageSourceNative\_GetImagePropertyIntArray()

PhonePC/2in1TabletTVWearable

```
1. Image_ErrorCode OH_ImageSourceNative_GetImagePropertyIntArray(OH_ImageSourceNative *source, Image_String *key, int32_t *value, size_t size)
```

**描述**

以整型数组类型获取图像属性的值。

说明

读取DNG格式图片时，该接口对部分key有特殊处理。以下字段的字符串取值请参考[变量](capi-image-common-h.md#变量)中定义的OHOS\_IMAGE\_PROPERTY\_XXX系列常量的值：

* NewSubfileType、ImageWidth、ImageLength、DefaultCropSize、Orientation、Compression、PhotometricInterpretation、PlanarConfiguration、RowsPerStrip、StripOffsets、StripByteCounts、SamplesPerPixel、BitsPerSample、YCbCrCoefficients、YCbCrSubSampling、YCbCrPositioning、ReferenceBlackWhite、XResolution、YResolution、ResolutionUnit字段：返回主图相关的字段值。
* ImageUniqueID字段：根据规范进行校验，不符合规范时会返回空字符串。
* ExifVersion、FlashpixVersion、ColorSpace字段：当图片中不存在该标签时，返回错误码。
* DNGVersion字段：当版本号小于1.0.0.0时，统一返回1.0.0.0。
* GPSVersionID字段：当没有有效的GPS数据时，会清除GPS版本号并返回0。
* GPSAltitudeRef字段：当未设置GPSAltitude时，会设置为0xFFFFFFFF。
* ISOSpeedRatings字段：当该标签值为0或65535时，会优先使用推荐曝光指数，若不存在则依次使用标准输出灵敏度、ISO速度、曝光指数。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ImageSourceNative](capi-image-nativemodule-oh-imagesourcenative.md) \*source | 被查询属性的ImageSource。 |
| [Image\_String](capi-image-nativemodule-image-string.md) \*key | 被查询的属性。 |
| int32\_t \*value | 被查询属性的查询结果。输出参数。调用者需要管理内存应用程序并释放。 |
| size\_t size | 字符串长度。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_SOURCE\_INVALID\_PARAMETER：source、key或value为nullptr。  IMAGE\_SOURCE\_UNSUPPORTED\_MIME\_TYPE：不支持查询当前mimetype的图像属性。  IMAGE\_SOURCE\_UNSUPPORTED\_METADATA：指定的元数据不存在，或者不是整型数组类型的值。 |

### OH\_ImageSourceNative\_GetImagePropertyDoubleArray()

PhonePC/2in1TabletTVWearable

```
1. Image_ErrorCode OH_ImageSourceNative_GetImagePropertyDoubleArray(OH_ImageSourceNative *source, Image_String *key, double *value, size_t size)
```

**描述**

以浮点型数组类型获取图像属性的值。

说明

读取DNG格式图片时，该接口对部分key有特殊处理。以下字段的字符串取值请参考[变量](capi-image-common-h.md#变量)中定义的OHOS\_IMAGE\_PROPERTY\_XXX系列常量的值：

* NewSubfileType、ImageWidth、ImageLength、DefaultCropSize、Orientation、Compression、PhotometricInterpretation、PlanarConfiguration、RowsPerStrip、StripOffsets、StripByteCounts、SamplesPerPixel、BitsPerSample、YCbCrCoefficients、YCbCrSubSampling、YCbCrPositioning、ReferenceBlackWhite、XResolution、YResolution、ResolutionUnit字段：返回主图相关的字段值。
* ImageUniqueID字段：根据规范进行校验，不符合规范时会返回空字符串。
* ExifVersion、FlashpixVersion、ColorSpace字段：当图片中不存在该标签时，返回错误码。
* DNGVersion字段：当版本号小于1.0.0.0时，统一返回1.0.0.0。
* GPSVersionID字段：当没有有效的GPS数据时，会清除GPS版本号并返回0。
* GPSAltitudeRef字段：当未设置GPSAltitude时，会设置为0xFFFFFFFF。
* ISOSpeedRatings字段：当该标签值为0或65535时，会优先使用推荐曝光指数，若不存在则依次使用标准输出灵敏度、ISO速度、曝光指数。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ImageSourceNative](capi-image-nativemodule-oh-imagesourcenative.md) \*source | 被查询属性的ImageSource。 |
| [Image\_String](capi-image-nativemodule-image-string.md) \*key | 被查询的属性。 |
| double \*value | 被查询属性的查询结果。输出参数。调用者需要管理内存应用程序并释放。 |
| size\_t size | 数组长度。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_SOURCE\_INVALID\_PARAMETER：source、key或value为nullptr。  IMAGE\_SOURCE\_UNSUPPORTED\_MIME\_TYPE：不支持查询当前mimetype的图像属性。  IMAGE\_SOURCE\_UNSUPPORTED\_METADATA：指定的元数据不存在，或者不是浮点型数组类型的值。 |

### OH\_ImageSourceNative\_GetImagePropertyBlob()

PhonePC/2in1TabletTVWearable

```
1. Image_ErrorCode OH_ImageSourceNative_GetImagePropertyBlob(OH_ImageSourceNative *source, Image_String *key, void *value, size_t size)
```

**描述**

以二进制对象类型获取图像属性的值。

说明

读取DNG格式图片时，该接口对部分key有特殊处理。以下字段的字符串取值请参考[变量](capi-image-common-h.md#变量)中定义的OHOS\_IMAGE\_PROPERTY\_XXX系列常量的值：

* NewSubfileType、ImageWidth、ImageLength、DefaultCropSize、Orientation、Compression、PhotometricInterpretation、PlanarConfiguration、RowsPerStrip、StripOffsets、StripByteCounts、SamplesPerPixel、BitsPerSample、YCbCrCoefficients、YCbCrSubSampling、YCbCrPositioning、ReferenceBlackWhite、XResolution、YResolution、ResolutionUnit字段：返回主图相关的字段值。
* ImageUniqueID字段：根据规范进行校验，不符合规范时会返回空字符串。
* ExifVersion、FlashpixVersion、ColorSpace字段：当图片中不存在该标签时，返回错误码。
* DNGVersion字段：当版本号小于1.0.0.0时，统一返回1.0.0.0。
* GPSVersionID字段：当没有有效的GPS数据时，会清除GPS版本号并返回0。
* GPSAltitudeRef字段：当未设置GPSAltitude时，会设置为0xFFFFFFFF。
* ISOSpeedRatings字段：当该标签值为0或65535时，会优先使用推荐曝光指数，若不存在则依次使用标准输出灵敏度、ISO速度、曝光指数。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ImageSourceNative](capi-image-nativemodule-oh-imagesourcenative.md) \*source | 被查询属性的ImageSource。 |
| [Image\_String](capi-image-nativemodule-image-string.md) \*key | 被查询的属性。 |
| void \*value | 被查询属性的查询结果。输出参数。调用者需要管理内存应用程序并释放。 |
| size\_t size | 数组长度。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_SOURCE\_INVALID\_PARAMETER：source、key或value为nullptr。  IMAGE\_SOURCE\_UNSUPPORTED\_MIME\_TYPE：不支持查询当前mimetype的图像属性。  IMAGE\_SOURCE\_UNSUPPORTED\_METADATA：指定的元数据不存在，或者不是二进制对象类型的值。 |

### OH\_ImageSourceNative\_ModifyImagePropertyShort()

PhonePC/2in1TabletTVWearable

```
1. Image_ErrorCode OH_ImageSourceNative_ModifyImagePropertyShort(OH_ImageSourceNative *source, Image_String *key, uint16_t value)
```

**描述**

修改图像属性中短整型的值。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ImageSourceNative](capi-image-nativemodule-oh-imagesourcenative.md) \*source | 被修改属性的ImageSource。 |
| [Image\_String](capi-image-nativemodule-image-string.md) \*key | 被修改的属性。 |
| uint16\_t value | 为属性设置的值。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_SOURCE\_INVALID\_PARAMETER：source、key或value为nullptr。  IMAGE\_SOURCE\_UNSUPPORTED\_MIME\_TYPE：不支持查询当前mimetype的图像属性。  IMAGE\_SOURCE\_UNSUPPORTED\_METADATA：指定的元数据不存在，或者不是短整型的值。 |

### OH\_ImageSourceNative\_ModifyImagePropertyLong()

PhonePC/2in1TabletTVWearable

```
1. Image_ErrorCode OH_ImageSourceNative_ModifyImagePropertyLong(OH_ImageSourceNative *source, Image_String *key, uint32_t value)
```

**描述**

修改图像属性中长整型的值。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ImageSourceNative](capi-image-nativemodule-oh-imagesourcenative.md) \*source | 被修改属性的ImageSource。 |
| [Image\_String](capi-image-nativemodule-image-string.md) \*key | 被修改的属性。 |
| uint32\_t value | 为属性设置的值。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_SOURCE\_INVALID\_PARAMETER：source、key或value为nullptr。  IMAGE\_SOURCE\_UNSUPPORTED\_MIME\_TYPE：不支持查询当前mimetype的图像属性。  IMAGE\_SOURCE\_UNSUPPORTED\_METADATA：指定的元数据不存在，或者不是长整型的值。 |

### OH\_ImageSourceNative\_ModifyImagePropertyDouble()

PhonePC/2in1TabletTVWearable

```
1. Image_ErrorCode OH_ImageSourceNative_ModifyImagePropertyDouble(OH_ImageSourceNative *source, Image_String *key, double value)
```

**描述**

修改图像属性中浮点型的值。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ImageSourceNative](capi-image-nativemodule-oh-imagesourcenative.md) \*source | 被修改属性的ImageSource。 |
| [Image\_String](capi-image-nativemodule-image-string.md) \*key | 被修改的属性。 |
| double value | 为属性设置的值。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_SOURCE\_INVALID\_PARAMETER：source、key或value为nullptr。  IMAGE\_SOURCE\_UNSUPPORTED\_MIME\_TYPE：不支持查询当前mimetype的图像属性。  IMAGE\_SOURCE\_UNSUPPORTED\_METADATA：指定的元数据不存在，或者不是浮点型的值。 |

### OH\_ImageSourceNative\_ModifyImagePropertyIntArray()

PhonePC/2in1TabletTVWearable

```
1. Image_ErrorCode OH_ImageSourceNative_ModifyImagePropertyIntArray(OH_ImageSourceNative *source, Image_String *key, int32_t *value, size_t size)
```

**描述**

修改图像属性中整型数组型的值。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ImageSourceNative](capi-image-nativemodule-oh-imagesourcenative.md) \*source | 被修改属性的ImageSource。 |
| [Image\_String](capi-image-nativemodule-image-string.md) \*key | 被修改的属性。 |
| int32\_t \*value | 为属性设置的值。 |
| size\_t size | 数组长度。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_SOURCE\_INVALID\_PARAMETER：source、key或value为nullptr。  IMAGE\_SOURCE\_UNSUPPORTED\_MIME\_TYPE：不支持查询当前mimetype的图像属性。  IMAGE\_SOURCE\_UNSUPPORTED\_METADATA：指定的元数据不存在，或者不是整型数组类型的值。 |

### OH\_ImageSourceNative\_ModifyImagePropertyDoubleArray()

PhonePC/2in1TabletTVWearable

```
1. Image_ErrorCode OH_ImageSourceNative_ModifyImagePropertyDoubleArray(OH_ImageSourceNative *source, Image_String *key, double *value, size_t size)
```

**描述**

修改图像属性中浮点型数组型的值。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ImageSourceNative](capi-image-nativemodule-oh-imagesourcenative.md) \*source | 被修改属性的ImageSource。 |
| [Image\_String](capi-image-nativemodule-image-string.md) \*key | 被修改的属性。 |
| double \*value | 为属性设置的值。 |
| size\_t size | 数组长度。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_SOURCE\_INVALID\_PARAMETER：source、key或value为nullptr。  IMAGE\_SOURCE\_UNSUPPORTED\_MIME\_TYPE：不支持查询当前mimetype的图像属性。  IMAGE\_SOURCE\_UNSUPPORTED\_METADATA：指定的元数据不存在，或者不是浮点型数组类型的值。 |

### OH\_ImageSourceNative\_ModifyImagePropertyBlob()

PhonePC/2in1TabletTVWearable

```
1. Image_ErrorCode OH_ImageSourceNative_ModifyImagePropertyBlob(OH_ImageSourceNative *source, Image_String *key, void *value, size_t size)
```

**描述**

修改图像属性中二进制对象的值。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ImageSourceNative](capi-image-nativemodule-oh-imagesourcenative.md) \*source | 被修改属性的ImageSource。 |
| [Image\_String](capi-image-nativemodule-image-string.md) \*key | 被修改的属性。 |
| void \*value | 为属性设置的值。 |
| size\_t size | 数组长度。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_SOURCE\_INVALID\_PARAMETER：source、key或value为nullptr。  IMAGE\_SOURCE\_UNSUPPORTED\_MIME\_TYPE：不支持查询当前mimetype的图像属性。  IMAGE\_SOURCE\_UNSUPPORTED\_METADATA：指定的元数据不存在，或者不是二进制对象类型的值。 |

### OH\_ImageSourceNative\_GetImagePropertyWithNull()

PhonePC/2in1TabletTVWearable

```
1. Image_ErrorCode OH_ImageSourceNative_GetImagePropertyWithNull(OH_ImageSourceNative *source, Image_String *key, Image_String *value)
```

**描述**

获取图像属性值。输出的value.data以字符串结束符'\0'结尾。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ImageSourceNative](capi-image-nativemodule-oh-imagesourcenative.md) \*source | 被操作的OH\_ImageSourceNative指针。OH\_ImageSourceNative使用完成后需要主动释放，参见[OH\_ImageSourceNative\_Release](capi-image-source-native-h.md#oh_imagesourcenative_release)。 |
| [Image\_String](capi-image-nativemodule-image-string.md) \*key | 指向属性键的指针。key的取值范围请参考image\_common.h的[变量](capi-image-common-h.md#变量)中定义的OHOS\_IMAGE\_PROPERTY\_XXX系列常量。 |
| [Image\_String](capi-image-nativemodule-image-string.md) \*value | 指向属性值的指针（输出参数）。调用本接口前，用户应将value->data置为空指针，并将value->size设为0。接口会为value->data自动分配所需内存，并对value->size赋值。完成对该内存的使用后，用户必须使用C标准库提供的free()函数释放value->data指向的内存，否则可能导致内存泄漏。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_SOURCE\_INVALID\_PARAMETER：source、key或value为空。 |

### OH\_ImageSourceNative\_ModifyImageProperty()

PhonePC/2in1TabletTVWearable

```
1. Image_ErrorCode OH_ImageSourceNative_ModifyImageProperty(OH_ImageSourceNative *source, Image_String *key, Image_String *value)
```

**描述**

通过指定的键修改图片属性的值。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ImageSourceNative](capi-image-nativemodule-oh-imagesourcenative.md) \*source | 被操作的OH\_ImageSourceNative指针。OH\_ImageSourceNative使用完成后需要主动释放，参见[OH\_ImageSourceNative\_Release](capi-image-source-native-h.md#oh_imagesourcenative_release)。 |
| [Image\_String](capi-image-nativemodule-image-string.md) \*key | 指向属性键的指针。key的取值范围请参考image\_common.h的[变量](capi-image-common-h.md#变量)中定义的OHOS\_IMAGE\_PROPERTY\_XXX系列常量。 |
| [Image\_String](capi-image-nativemodule-image-string.md) \*value | 需要修改的属性值。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_BAD\_PARAMETER：参数错误。 |

### OH\_ImageSourceNative\_GetFrameCount()

PhonePC/2in1TabletTVWearable

```
1. Image_ErrorCode OH_ImageSourceNative_GetFrameCount(OH_ImageSourceNative *source, uint32_t *frameCount)
```

**描述**

获取图像帧数。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ImageSourceNative](capi-image-nativemodule-oh-imagesourcenative.md) \*source | 被操作的OH\_ImageSourceNative指针。 |
| uint32\_t \*frameCount | 图像帧数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_BAD\_PARAMETER：参数错误。 |

### OH\_ImageSourceNative\_GetSupportedFormats()

PhonePC/2in1TabletTVWearable

```
1. Image_ErrorCode OH_ImageSourceNative_GetSupportedFormats(Image_MimeType **supportedFormats, size_t *length)
```

**描述**

获取支持解码的图片格式。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Image\_MimeType](capi-image-nativemodule-image-string.md) \*\*supportedFormats | 支持解码的图片格式。 |
| size\_t \*length | 数组长度。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：操作成功。  IMAGE\_SOURCE\_INVALID\_PARAMETER：参数异常，supportedFormats或length为空。 |

### OH\_ImageSourceNative\_Release()

PhonePC/2in1TabletTVWearable

```
1. Image_ErrorCode OH_ImageSourceNative_Release(OH_ImageSourceNative *source)
```

**描述**

释放OH\_ImageSourceNative指针。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ImageSourceNative](capi-image-nativemodule-oh-imagesourcenative.md) \*source | 要释放的OH\_ImageSourceNative指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_BAD\_PARAMETER：参数错误。 |

### OH\_DecodingOptionsForPicture\_Create()

PhonePC/2in1TabletTVWearable

```
1. Image_ErrorCode OH_DecodingOptionsForPicture_Create(OH_DecodingOptionsForPicture **options)
```

**描述**

创建OH\_DecodingOptionsForPicture指针。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_DecodingOptionsForPicture](pi-image-nativemodule-oh-decodingoptionsforpicture.md) \*\*options | 被操作的OH\_DecodingOptionsForPicture指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_BAD\_PARAMETER：参数错误。 |

### OH\_DecodingOptionsForPicture\_GetDesiredAuxiliaryPictures()

PhonePC/2in1TabletTVWearable

```
1. Image_ErrorCode OH_DecodingOptionsForPicture_GetDesiredAuxiliaryPictures(OH_DecodingOptionsForPicture *options, Image_AuxiliaryPictureType **desiredAuxiliaryPictures, size_t *length)
```

**描述**

获取解码时设置的期望辅助图（期望解码出的picture包含的辅助图）。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_DecodingOptionsForPicture](pi-image-nativemodule-oh-decodingoptionsforpicture.md) \*options | 被操作的OH\_DecodingOptionsForPicture指针。 |
| [Image\_AuxiliaryPictureType](capi-picture-native-h.md#image_auxiliarypicturetype) \*\*desiredAuxiliaryPictures | 解码选项中的期望辅助图。 |
| size\_t \*length | 期望辅助图长度。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_BAD\_PARAMETER：参数错误。 |

### OH\_DecodingOptionsForPicture\_SetDesiredAuxiliaryPictures()

PhonePC/2in1TabletTVWearable

```
1. Image_ErrorCode OH_DecodingOptionsForPicture_SetDesiredAuxiliaryPictures(OH_DecodingOptionsForPicture *options, Image_AuxiliaryPictureType *desiredAuxiliaryPictures, size_t length)
```

**描述**

设置解码选项中的期望辅助图。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_DecodingOptionsForPicture](pi-image-nativemodule-oh-decodingoptionsforpicture.md) \*options | 被操作的OH\_DecodingOptionsForPicture指针。 |
| [Image\_AuxiliaryPictureType](capi-picture-native-h.md#image_auxiliarypicturetype) \*desiredAuxiliaryPictures | 将要设置的期望辅助图。 |
| size\_t length | 期望辅助图长度。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_BAD\_PARAMETER：参数错误。 |

### OH\_DecodingOptionsForPicture\_Release()

PhonePC/2in1TabletTVWearable

```
1. Image_ErrorCode OH_DecodingOptionsForPicture_Release(OH_DecodingOptionsForPicture *options)
```

**描述**

释放OH\_DecodingOptionsForPicture指针。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_DecodingOptionsForPicture](pi-image-nativemodule-oh-decodingoptionsforpicture.md) \*options | 要释放的OH\_DecodingOptionsForPicture指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_BAD\_PARAMETER：参数错误。 |
