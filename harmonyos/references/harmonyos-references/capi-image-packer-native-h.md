---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-packer-native-h
title: image_packer_native.h
breadcrumb: API参考 > 媒体 > Image Kit（图片处理服务） > C API > 头文件 > image_packer_native.h
category: harmonyos-references
scraped_at: 2026-04-28T08:13:16+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:e8251c132abbf7b19f5b6cfb8667d83d374e6f58806d0afac4baedb3cfc9a1c0
---

## 概述

PhonePC/2in1TabletTVWearable

图片编码API。

**引用文件：** <multimedia/image\_framework/image/image\_packer\_native.h>

**库：** libimage\_packer.so

**系统能力：** SystemCapability.Multimedia.Image.ImagePacker

**起始版本：** 12

**相关模块：** [Image\_NativeModule](capi-image-nativemodule.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 结构体

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [OH\_ImagePackerNative](capi-image-nativemodule-oh-imagepackernative.md) | OH\_ImagePackerNative | ImagePacker结构体类型，用于执行ImagePacker相关操作。 |
| [OH\_PackingOptions](capi-image-nativemodule-oh-packingoptions.md) | OH\_PackingOptions | OH\_PackingOptions是native层封装的图像编码选项结构体，不可直接操作，而是采用函数调用方式创建、释放结构体以及操作具体字段。 |
| [OH\_PackingOptionsForSequence](pi-image-nativemodule-oh-packingoptionsforsequence.md) | OH\_PackingOptionsForSequence | OH\_PackingOptionsForSequence是native层封装的图像序列编码选项结构体，不可直接操作，而是采用函数调用方式创建、释放结构体以及操作具体字段。 |

### 枚举

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [IMAGE\_PACKER\_DYNAMIC\_RANGE](capi-image-packer-native-h.md#image_packer_dynamic_range) | IMAGE\_PACKER\_DYNAMIC\_RANGE | 编码指定动态范围。 |

### 函数

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [Image\_ErrorCode OH\_PackingOptions\_Create(OH\_PackingOptions \*\*options)](capi-image-packer-native-h.md#oh_packingoptions_create) | 创建PackingOptions结构体的指针。 |
| [Image\_ErrorCode OH\_PackingOptions\_GetMimeType(OH\_PackingOptions \*options, Image\_MimeType \*format)](capi-image-packer-native-h.md#oh_packingoptions_getmimetype) | 获取MIME类型。该接口获取到的value.data缺少字符串结束符'\0'，请谨慎使用。 |
| [Image\_ErrorCode OH\_PackingOptions\_GetMimeTypeWithNull(OH\_PackingOptions \*options, Image\_MimeType \*format)](capi-image-packer-native-h.md#oh_packingoptions_getmimetypewithnull) | 获取编解码参数中的MIME类型。输出的format.data以字符串结束符'\0'结尾。 |
| [Image\_ErrorCode OH\_PackingOptions\_SetMimeType(OH\_PackingOptions \*options, Image\_MimeType \*format)](capi-image-packer-native-h.md#oh_packingoptions_setmimetype) | 设置MIME类型。 |
| [Image\_ErrorCode OH\_PackingOptions\_GetQuality(OH\_PackingOptions \*options, uint32\_t \*quality)](capi-image-packer-native-h.md#oh_packingoptions_getquality) | 获取编码质量。 |
| [Image\_ErrorCode OH\_PackingOptions\_SetQuality(OH\_PackingOptions \*options, uint32\_t quality)](capi-image-packer-native-h.md#oh_packingoptions_setquality) | 设置编码质量。 |
| [Image\_ErrorCode OH\_PackingOptions\_GetNeedsPackProperties(OH\_PackingOptions \*options, bool \*needsPackProperties)](capi-image-packer-native-h.md#oh_packingoptions_getneedspackproperties) | 获取OH\_PackingOptions结构体的needsPackProperties参数。 |
| [Image\_ErrorCode OH\_PackingOptions\_SetNeedsPackProperties(OH\_PackingOptions \*options, bool needsPackProperties)](capi-image-packer-native-h.md#oh_packingoptions_setneedspackproperties) | 设置OH\_PackingOptions结构体的needsPackProperties参数。 |
| [Image\_ErrorCode OH\_PackingOptions\_GetDesiredDynamicRange(OH\_PackingOptions options, int32\_t desiredDynamicRange)](capi-image-packer-native-h.md#oh_packingoptions_getdesireddynamicrange) | 获取编码时期望的图片动态范围。 |
| [Image\_ErrorCode OH\_PackingOptions\_SetDesiredDynamicRange(OH\_PackingOptions \*options, int32\_t desiredDynamicRange)](capi-image-packer-native-h.md#oh_packingoptions_setdesireddynamicrange) | 设置编码时期望的图片动态范围。 |
| [Image\_ErrorCode OH\_PackingOptions\_Release(OH\_PackingOptions \*options)](capi-image-packer-native-h.md#oh_packingoptions_release) | 释放OH\_PackingOptions指针。 |
| [Image\_ErrorCode OH\_PackingOptionsForSequence\_Create(OH\_PackingOptionsForSequence \*\*options)](capi-image-packer-native-h.md#oh_packingoptionsforsequence_create) | 创建OH\_PackingOptionsForSequence结构体的指针。 |
| [Image\_ErrorCode OH\_PackingOptionsForSequence\_SetFrameCount(OH\_PackingOptionsForSequence \*options, uint32\_t frameCount)](capi-image-packer-native-h.md#oh_packingoptionsforsequence_setframecount) | 设置编码时指定的帧数。 |
| [Image\_ErrorCode OH\_PackingOptionsForSequence\_GetFrameCount(OH\_PackingOptionsForSequence \*options, uint32\_t \*frameCount)](capi-image-packer-native-h.md#oh_packingoptionsforsequence_getframecount) | 获取编码时指定的帧数。 |
| [Image\_ErrorCode OH\_PackingOptionsForSequence\_SetDelayTimeList(OH\_PackingOptionsForSequence \*options, int32\_t \*delayTimeList, size\_t delayTimeListLength)](capi-image-packer-native-h.md#oh_packingoptionsforsequence_setdelaytimelist) | 设定编码时图片的延迟时间数组。 |
| [Image\_ErrorCode OH\_PackingOptionsForSequence\_GetDelayTimeList(OH\_PackingOptionsForSequence \*options, int32\_t \*delayTimeList, size\_t delayTimeListLength)](capi-image-packer-native-h.md#oh_packingoptionsforsequence_getdelaytimelist) | 获取编码时图片的延迟时间数组。 |
| [Image\_ErrorCode OH\_PackingOptionsForSequence\_SetDisposalTypes(OH\_PackingOptionsForSequence \*options, uint32\_t \*disposalTypes, size\_t disposalTypesLength)](capi-image-packer-native-h.md#oh_packingoptionsforsequence_setdisposaltypes) | 设定编码时图片的过渡帧模式数组。 |
| [Image\_ErrorCode OH\_PackingOptionsForSequence\_GetDisposalTypes(OH\_PackingOptionsForSequence \*options, uint32\_t \*disposalTypes, size\_t disposalTypesLength)](capi-image-packer-native-h.md#oh_packingoptionsforsequence_getdisposaltypes) | 获取编码时图片的过渡帧模式数组。 |
| [Image\_ErrorCode OH\_PackingOptionsForSequence\_SetLoopCount(OH\_PackingOptionsForSequence \*options, uint32\_t loopCount)](capi-image-packer-native-h.md#oh_packingoptionsforsequence_setloopcount) | 设定编码时图片循环播放次数，取值范围为[0，65535]，0表示无限循环；若无此字段，则表示不循环播放。 |
| [Image\_ErrorCode OH\_PackingOptionsForSequence\_GetLoopCount(OH\_PackingOptionsForSequence \*options, uint32\_t \*loopCount)](capi-image-packer-native-h.md#oh_packingoptionsforsequence_getloopcount) | 获取编码时图片循环播放次数。 |
| [Image\_ErrorCode OH\_PackingOptionsForSequence\_Release(OH\_PackingOptionsForSequence \*options)](capi-image-packer-native-h.md#oh_packingoptionsforsequence_release) | 释放OH\_PackingOptionsForSequence指针。 |
| [Image\_ErrorCode OH\_ImagePackerNative\_Create(OH\_ImagePackerNative \*\*imagePacker)](capi-image-packer-native-h.md#oh_imagepackernative_create) | 创建OH\_ImagePackerNative指针。 |
| [Image\_ErrorCode OH\_ImagePackerNative\_PackToDataFromImageSource(OH\_ImagePackerNative \*imagePacker, OH\_PackingOptions \*options, OH\_ImageSourceNative \*imageSource, uint8\_t \*outData, size\_t \*size)](capi-image-packer-native-h.md#oh_imagepackernative_packtodatafromimagesource) | 将ImageSource编码为指定格式的数据。 |
| [Image\_ErrorCode OH\_ImagePackerNative\_PackToDataFromPixelmap(OH\_ImagePackerNative \*imagePacker, OH\_PackingOptions \*options, OH\_PixelmapNative \*pixelmap, uint8\_t \*outData, size\_t \*size)](capi-image-packer-native-h.md#oh_imagepackernative_packtodatafrompixelmap) | 将Pixelmap编码为指定格式的数据。 |
| [Image\_ErrorCode OH\_ImagePackerNative\_PackToDataFromPicture(OH\_ImagePackerNative \*imagePacker, OH\_PackingOptions \*options, OH\_PictureNative \*picture, uint8\_t \*outData, size\_t \*size)](capi-image-packer-native-h.md#oh_imagepackernative_packtodatafrompicture) | 将Picture编码为指定格式的数据。 |
| [Image\_ErrorCode OH\_ImagePackerNative\_PackToDataFromPixelmapSequence(OH\_ImagePackerNative \*imagePacker, OH\_PackingOptionsForSequence \*options, OH\_PixelmapNative \*\*pixelmapSequence,size\_t sequenceLength, uint8\_t \*outData, size\_t \*outDataSize)](capi-image-packer-native-h.md#oh_imagepackernative_packtodatafrompixelmapsequence) | 将Pixelmap序列编码为数据。 |
| [Image\_ErrorCode OH\_ImagePackerNative\_PackToFileFromImageSource(OH\_ImagePackerNative \*imagePacker, OH\_PackingOptions \*options, OH\_ImageSourceNative \*imageSource, int32\_t fd)](capi-image-packer-native-h.md#oh_imagepackernative_packtofilefromimagesource) | 将一个ImageSource编码到文件中。 |
| [Image\_ErrorCode OH\_ImagePackerNative\_PackToFileFromPixelmap(OH\_ImagePackerNative \*imagePacker, OH\_PackingOptions \*options, OH\_PixelmapNative \*pixelmap, int32\_t fd)](capi-image-packer-native-h.md#oh_imagepackernative_packtofilefrompixelmap) | 将一个Pixelmap编码到文件中。 |
| [Image\_ErrorCode OH\_ImagePackerNative\_PackToFileFromPicture(OH\_ImagePackerNative \*imagePacker, OH\_PackingOptions \*options, OH\_PictureNative \*picture, int32\_t fd)](capi-image-packer-native-h.md#oh_imagepackernative_packtofilefrompicture) | 将一个Picture编码到文件中。 |
| [Image\_ErrorCode OH\_ImagePackerNative\_PackToFileFromPixelmapSequence(OH\_ImagePackerNative \*imagePacker, OH\_PackingOptionsForSequence \*options, OH\_PixelmapNative \*\*pixelmapSequence, size\_t sequenceLength, int32\_t fd)](capi-image-packer-native-h.md#oh_imagepackernative_packtofilefrompixelmapsequence) | 将一个Pixelmap序列编码到文件中。 |
| [Image\_ErrorCode OH\_ImagePackerNative\_GetSupportedFormats(Image\_MimeType \*\*supportedFormats, size\_t \*length)](capi-image-packer-native-h.md#oh_imagepackernative_getsupportedformats) | 获取支持编码的图片格式。 |
| [Image\_ErrorCode OH\_ImagePackerNative\_Release(OH\_ImagePackerNative \*imagePacker)](capi-image-packer-native-h.md#oh_imagepackernative_release) | 释放OH\_ImagePackerNative指针。 |

## 枚举类型说明

PhonePC/2in1TabletTVWearable

### IMAGE\_PACKER\_DYNAMIC\_RANGE

PhonePC/2in1TabletTVWearable

```
1. enum IMAGE_PACKER_DYNAMIC_RANGE
```

**描述**

编码指定动态范围。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| IMAGE\_PACKER\_DYNAMIC\_RANGE\_AUTO = 0 | 编码动态范围根据图像信息自适应。 |
| IMAGE\_PACKER\_DYNAMIC\_RANGE\_SDR = 1 | 编码图片为标准动态范围。 |

## 函数说明

PhonePC/2in1TabletTVWearable

### OH\_PackingOptions\_Create()

PhonePC/2in1TabletTVWearable

```
1. Image_ErrorCode OH_PackingOptions_Create(OH_PackingOptions **options)
```

**描述**

创建PackingOptions结构体的指针。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_PackingOptions](capi-image-nativemodule-oh-packingoptions.md) \*\*options | 用于操作的PackingOptions指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_BAD\_PARAMETER：参数错误。 |

### OH\_PackingOptions\_GetMimeType()

PhonePC/2in1TabletTVWearable

```
1. Image_ErrorCode OH_PackingOptions_GetMimeType(OH_PackingOptions *options,Image_MimeType *format)
```

**描述**

获取MIME类型。该接口获取到的value.data缺少字符串结束符'\0'，请谨慎使用。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_PackingOptions](capi-image-nativemodule-oh-packingoptions.md) \*options | 被操作的OH\_PackingOptions指针。 |
| [Image\_MimeType](capi-image-nativemodule-image-string.md) \*format | 图像格式。可传入一个空指针和零大小，系统将分配内存，但必须在使用后释放内存。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_BAD\_PARAMETER：参数错误。 |

### OH\_PackingOptions\_GetMimeTypeWithNull()

PhonePC/2in1TabletTVWearable

```
1. Image_ErrorCode OH_PackingOptions_GetMimeTypeWithNull(OH_PackingOptions *options,Image_MimeType *format)
```

**描述**

获取编解码参数中的MIME类型。输出的format.data以字符串结束符'\0'结尾。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_PackingOptions](capi-image-nativemodule-oh-packingoptions.md) \*options | 编码参数指针。 |
| [Image\_MimeType](capi-image-nativemodule-image-string.md) \*format | 编码参数中的 MIME 类型的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_PACKER\_INVALID\_PARAMETER：options或format为空。 |

### OH\_PackingOptions\_SetMimeType()

PhonePC/2in1TabletTVWearable

```
1. Image_ErrorCode OH_PackingOptions_SetMimeType(OH_PackingOptions *options,Image_MimeType *format)
```

**描述**

设置MIME类型。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_PackingOptions](capi-image-nativemodule-oh-packingoptions.md) \*options | 被操作的OH\_PackingOptions指针。 |
| [Image\_MimeType](capi-image-nativemodule-image-string.md) \*format | 图像格式。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_BAD\_PARAMETER：参数错误。 |

### OH\_PackingOptions\_GetQuality()

PhonePC/2in1TabletTVWearable

```
1. Image_ErrorCode OH_PackingOptions_GetQuality(OH_PackingOptions *options,uint32_t *quality)
```

**描述**

获取编码质量。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_PackingOptions](capi-image-nativemodule-oh-packingoptions.md) \*options | 被操作的OH\_PackingOptions指针。 |
| uint32\_t \*quality | 编码质量。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_BAD\_PARAMETER：参数错误。 |

### OH\_PackingOptions\_SetQuality()

PhonePC/2in1TabletTVWearable

```
1. Image_ErrorCode OH_PackingOptions_SetQuality(OH_PackingOptions *options,uint32_t quality)
```

**描述**

设置编码质量。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_PackingOptions](capi-image-nativemodule-oh-packingoptions.md) \*options | 被操作的OH\_PackingOptions指针。 |
| uint32\_t quality | 编码质量。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_BAD\_PARAMETER：参数错误。 |

### OH\_PackingOptions\_GetNeedsPackProperties()

PhonePC/2in1TabletTVWearable

```
1. Image_ErrorCode OH_PackingOptions_GetNeedsPackProperties(OH_PackingOptions *options,bool *needsPackProperties)
```

**描述**

获取OH\_PackingOptions结构体的needsPackProperties参数。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_PackingOptions](capi-image-nativemodule-oh-packingoptions.md) \*options | 被操作的OH\_PackingOptions指针。 |
| bool \*needsPackProperties | 是否需要编码图片属性信息（例如Exif）。true表示需要，false表示不需要。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_BAD\_PARAMETER：参数错误。 |

### OH\_PackingOptions\_SetNeedsPackProperties()

PhonePC/2in1TabletTVWearable

```
1. Image_ErrorCode OH_PackingOptions_SetNeedsPackProperties(OH_PackingOptions *options,bool needsPackProperties)
```

**描述**

设置OH\_PackingOptions结构体的needsPackProperties参数。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_PackingOptions](capi-image-nativemodule-oh-packingoptions.md) \*options | 被操作的OH\_PackingOptions指针。 |
| bool needsPackProperties | 是否需要编码图片属性信息（例如Exif）。true表示需要，false表示不需要。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_BAD\_PARAMETER：参数错误。 |

### OH\_PackingOptions\_GetDesiredDynamicRange()

PhonePC/2in1TabletTVWearable

```
1. Image_ErrorCode OH_PackingOptions_GetDesiredDynamicRange(OH_PackingOptions *options, int32_t* desiredDynamicRange)
```

**描述**

获取编码时期望的图片动态范围。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_PackingOptions](capi-image-nativemodule-oh-packingoptions.md) \*options | 被操作的OH\_PackingOptions指针。 |
| int32\_t\* desiredDynamicRange | 期望的动态范围[IMAGE\_PACKER\_DYNAMIC\_RANGE]#image\_packer\_dynamic\_range)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_BAD\_PARAMETER：参数错误。 |

### OH\_PackingOptions\_SetDesiredDynamicRange()

PhonePC/2in1TabletTVWearable

```
1. Image_ErrorCode OH_PackingOptions_SetDesiredDynamicRange(OH_PackingOptions *options, int32_t desiredDynamicRange)
```

**描述**

设置编码时期望的图片动态范围。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_PackingOptions](capi-image-nativemodule-oh-packingoptions.md) \*options | 被操作的OH\_PackingOptions指针。 |
| int32\_t desiredDynamicRange | 期望的动态范围[IMAGE\_PACKER\_DYNAMIC\_RANGE]#image\_packer\_dynamic\_range)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_BAD\_PARAMETER：参数错误。 |

### OH\_PackingOptions\_Release()

PhonePC/2in1TabletTVWearable

```
1. Image_ErrorCode OH_PackingOptions_Release(OH_PackingOptions *options)
```

**描述**

释放OH\_PackingOptions指针。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_PackingOptions](capi-image-nativemodule-oh-packingoptions.md) \*options | 被操作的OH\_PackingOptions指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_BAD\_PARAMETER：参数错误。 |

### OH\_PackingOptionsForSequence\_Create()

PhonePC/2in1TabletTVWearable

```
1. Image_ErrorCode OH_PackingOptionsForSequence_Create(OH_PackingOptionsForSequence **options)
```

**描述**

创建OH\_PackingOptionsForSequence结构体的指针。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_PackingOptionsForSequence](pi-image-nativemodule-oh-packingoptionsforsequence.md) \*\*options | 用于操作的OH\_PackingOptionsForSequence指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_BAD\_PARAMETER：参数错误。 |

### OH\_PackingOptionsForSequence\_SetFrameCount()

PhonePC/2in1TabletTVWearable

```
1. Image_ErrorCode OH_PackingOptionsForSequence_SetFrameCount(OH_PackingOptionsForSequence *options,uint32_t frameCount)
```

**描述**

设置编码时指定的帧数。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_PackingOptionsForSequence](pi-image-nativemodule-oh-packingoptionsforsequence.md) \*options | 用于操作的OH\_PackingOptionsForSequence指针。 |
| uint32\_t frameCount | 图片的帧数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_BAD\_PARAMETER：参数错误。 |

### OH\_PackingOptionsForSequence\_GetFrameCount()

PhonePC/2in1TabletTVWearable

```
1. Image_ErrorCode OH_PackingOptionsForSequence_GetFrameCount(OH_PackingOptionsForSequence *options,uint32_t *frameCount)
```

**描述**

获取编码时指定的帧数。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_PackingOptionsForSequence](pi-image-nativemodule-oh-packingoptionsforsequence.md) \*options | 用于操作的OH\_PackingOptionsForSequence指针。 |
| uint32\_t \*frameCount | 图片的帧数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_BAD\_PARAMETER：参数错误。 |

### OH\_PackingOptionsForSequence\_SetDelayTimeList()

PhonePC/2in1TabletTVWearable

```
1. Image_ErrorCode OH_PackingOptionsForSequence_SetDelayTimeList(OH_PackingOptionsForSequence *options,int32_t *delayTimeList, size_t delayTimeListLength)
```

**描述**

设定编码时图片的延迟时间数组。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_PackingOptionsForSequence](pi-image-nativemodule-oh-packingoptionsforsequence.md) \*options | 用于操作的OH\_PackingOptionsForSequence指针。 |
| int32\_t \*delayTimeList | 图片延迟时间数组的指针。 |
| size\_t delayTimeListLength | 图片延迟时间数组的长度。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_BAD\_PARAMETER：参数错误。 |

### OH\_PackingOptionsForSequence\_GetDelayTimeList()

PhonePC/2in1TabletTVWearable

```
1. Image_ErrorCode OH_PackingOptionsForSequence_GetDelayTimeList(OH_PackingOptionsForSequence *options,int32_t *delayTimeList, size_t delayTimeListLength)
```

**描述**

获取编码时图片的延迟时间数组。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_PackingOptionsForSequence](pi-image-nativemodule-oh-packingoptionsforsequence.md) \*options | 用于操作的OH\_PackingOptionsForSequence指针。 |
| int32\_t \*delayTimeList | 图片延迟时间数组的指针。 |
| size\_t delayTimeListLength | 图片延迟时间数组的长度。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_BAD\_PARAMETER：参数错误。 |

### OH\_PackingOptionsForSequence\_SetDisposalTypes()

PhonePC/2in1TabletTVWearable

```
1. Image_ErrorCode OH_PackingOptionsForSequence_SetDisposalTypes(OH_PackingOptionsForSequence *options,uint32_t *disposalTypes, size_t disposalTypesLength)
```

**描述**

设定编码时图片的过渡帧模式数组。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_PackingOptionsForSequence](pi-image-nativemodule-oh-packingoptionsforsequence.md) \*options | 用于操作的OH\_PackingOptionsForSequence指针。 |
| uint32\_t \*disposalTypes | 图片过渡帧模式数组的指针，图片帧过渡模式的参数，如果长度小于frameCount，不足的部分将使用disposalTypes中的最后一个值进行填充，可取值如下：  0：不需要任何操作。  1：保持图形不变。  2：恢复背景色。  3：恢复到之前的状态。 |
| size\_t disposalTypesLength | 图片过渡帧模式数组的长度。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_BAD\_PARAMETER：参数错误。 |

### OH\_PackingOptionsForSequence\_GetDisposalTypes()

PhonePC/2in1TabletTVWearable

```
1. Image_ErrorCode OH_PackingOptionsForSequence_GetDisposalTypes(OH_PackingOptionsForSequence *options,uint32_t *disposalTypes, size_t disposalTypesLength)
```

**描述**

获取编码时图片的过渡帧模式数组。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_PackingOptionsForSequence](pi-image-nativemodule-oh-packingoptionsforsequence.md) \*options | 用于操作的OH\_PackingOptionsForSequence指针。 |
| uint32\_t \*disposalTypes | 图片过渡帧模式数组的指针。 |
| size\_t disposalTypesLength | 图片过渡帧模式数组的长度。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_BAD\_PARAMETER：参数错误。 |

### OH\_PackingOptionsForSequence\_SetLoopCount()

PhonePC/2in1TabletTVWearable

```
1. Image_ErrorCode OH_PackingOptionsForSequence_SetLoopCount(OH_PackingOptionsForSequence *options, uint32_t loopCount)
```

**描述**

设定编码时图片循环播放次数，取值范围为[0，65535]，0表示无限循环；若无此字段，则表示不循环播放。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_PackingOptionsForSequence](pi-image-nativemodule-oh-packingoptionsforsequence.md) \*options | 用于操作的OH\_PackingOptionsForSequence指针。 |
| uint32\_t loopCount | 图片循环播放次数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_BAD\_PARAMETER：参数错误。 |

### OH\_PackingOptionsForSequence\_GetLoopCount()

PhonePC/2in1TabletTVWearable

```
1. Image_ErrorCode OH_PackingOptionsForSequence_GetLoopCount(OH_PackingOptionsForSequence *options, uint32_t *loopCount)
```

**描述**

获取编码时图片循环播放次数。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_PackingOptionsForSequence](pi-image-nativemodule-oh-packingoptionsforsequence.md) \*options | 用于操作的OH\_PackingOptionsForSequence指针。 |
| uint32\_t \*loopCount | 图片循环播放次数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_BAD\_PARAMETER：参数错误。 |

### OH\_PackingOptionsForSequence\_Release()

PhonePC/2in1TabletTVWearable

```
1. Image_ErrorCode OH_PackingOptionsForSequence_Release(OH_PackingOptionsForSequence *options)
```

**描述**

释放OH\_PackingOptionsForSequence指针。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_PackingOptionsForSequence](pi-image-nativemodule-oh-packingoptionsforsequence.md) \*options | 用于操作的OH\_PackingOptionsForSequence指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_BAD\_PARAMETER：参数错误。 |

### OH\_ImagePackerNative\_Create()

PhonePC/2in1TabletTVWearable

```
1. Image_ErrorCode OH_ImagePackerNative_Create(OH_ImagePackerNative **imagePacker)
```

**描述**

创建OH\_ImagePackerNative指针。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ImagePackerNative](capi-image-nativemodule-oh-imagepackernative.md) \*\*imagePacker | 被操作的OH\_ImagePackerNative指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_BAD\_PARAMETER：参数错误。 |

### OH\_ImagePackerNative\_PackToDataFromImageSource()

PhonePC/2in1TabletTVWearable

```
1. Image_ErrorCode OH_ImagePackerNative_PackToDataFromImageSource(OH_ImagePackerNative *imagePacker,OH_PackingOptions *options, OH_ImageSourceNative *imageSource, uint8_t *outData, size_t *size)
```

**描述**

将ImageSource编码为指定格式的数据。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ImagePackerNative](capi-image-nativemodule-oh-imagepackernative.md) \*imagePacker | 被操作的OH\_ImagePackerNative指针。 |
| [OH\_PackingOptions](capi-image-nativemodule-oh-packingoptions.md) \*options | 编码选项参数。 |
| [OH\_ImageSourceNative](capi-image-nativemodule-oh-imagesourcenative.md) \*imageSource | 用于编码的image source指针。 |
| uint8\_t \*outData | 用于存储打包图像输出数据的缓冲区。 |
| size\_t \*size | 用于存储打包图像输出数据的缓冲区大小。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_BAD\_PARAMETER：参数错误。  IMAGE\_DECODE\_FAILED：解码失败。  IMAGE\_ALLOC\_FAILED：申请内存失败。  IMAGE\_TOO\_LARGE：数据或图片过大。  IMAGE\_UNKNOWN\_ERROR：未知错误。 |

### OH\_ImagePackerNative\_PackToDataFromPixelmap()

PhonePC/2in1TabletTVWearable

```
1. Image_ErrorCode OH_ImagePackerNative_PackToDataFromPixelmap(OH_ImagePackerNative *imagePacker,OH_PackingOptions *options, OH_PixelmapNative *pixelmap, uint8_t *outData, size_t *size)
```

**描述**

将Pixelmap编码为指定格式的数据。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ImagePackerNative](capi-image-nativemodule-oh-imagepackernative.md) \*imagePacker | 被操作的OH\_ImagePackerNative指针。 |
| [OH\_PackingOptions](capi-image-nativemodule-oh-packingoptions.md) \*options | 编码选项参数。 |
| [OH\_PixelmapNative](capi-image-nativemodule-oh-pixelmapnative.md) \*pixelmap | 用于编码的Pixelmap指针。 |
| uint8\_t \*outData | 用于存储打包图像输出数据的缓冲区。 |
| size\_t \*size | 用于存储打包图像输出数据的缓冲区大小。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_BAD\_PARAMETER：参数错误。  IMAGE\_DECODE\_FAILED：解码失败。  IMAGE\_ALLOC\_FAILED：申请内存失败。  IMAGE\_TOO\_LARGE：数据或图片过大。  IMAGE\_UNKNOWN\_ERROR：未知错误。 |

### OH\_ImagePackerNative\_PackToDataFromPicture()

PhonePC/2in1TabletTVWearable

```
1. Image_ErrorCode OH_ImagePackerNative_PackToDataFromPicture(OH_ImagePackerNative *imagePacker,OH_PackingOptions *options, OH_PictureNative *picture, uint8_t *outData, size_t *size)
```

**描述**

将Picture编码为指定格式的数据。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ImagePackerNative](capi-image-nativemodule-oh-imagepackernative.md) \*imagePacker | 被操作的OH\_ImagePackerNative指针。 |
| [OH\_PackingOptions](capi-image-nativemodule-oh-packingoptions.md) \*options | 编码选项参数。 |
| [OH\_PictureNative](capi-image-nativemodule-oh-picturenative.md) \*picture | 用于编码的Picture指针。 |
| uint8\_t \*outData | 用于存储打包图像输出数据的缓冲区。 |
| size\_t \*size | 用于存储打包图像输出数据的缓冲区大小。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_BAD\_PARAMETER：参数错误。  IMAGE\_DECODE\_FAILED：解码失败。 |

### OH\_ImagePackerNative\_PackToDataFromPixelmapSequence()

PhonePC/2in1TabletTVWearable

```
1. Image_ErrorCode OH_ImagePackerNative_PackToDataFromPixelmapSequence(OH_ImagePackerNative *imagePacker,OH_PackingOptionsForSequence *options, OH_PixelmapNative **pixelmapSequence,size_t sequenceLength, uint8_t *outData, size_t *outDataSize)
```

**描述**

将Pixelmap序列编码为数据。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ImagePackerNative](capi-image-nativemodule-oh-imagepackernative.md) \*imagePacker | 被操作的OH\_ImagePackerNative指针。 |
| [OH\_PackingOptionsForSequence](pi-image-nativemodule-oh-packingoptionsforsequence.md) \*options | 编码选项参数 [OH\_PackingOptionsForSequence](pi-image-nativemodule-oh-packingoptionsforsequence.md)。 |
| [OH\_PixelmapNative](capi-image-nativemodule-oh-pixelmapnative.md) \*\*pixelmapSequence | 用于编码的Pixelmap序列指针。 |
| size\_t sequenceLength | 用于编码的Pixelmap序列长度。 |
| uint8\_t \*outData | 用于存储编码后图像输出数据的缓冲区。 |
| size\_t \*outDataSize | 用于存储编码后图像输出数据的缓冲区大小。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_BAD\_PARAMETER：参数错误。  IMAGE\_DECODE\_FAILED：解码失败。 |

### OH\_ImagePackerNative\_PackToFileFromImageSource()

PhonePC/2in1TabletTVWearable

```
1. Image_ErrorCode OH_ImagePackerNative_PackToFileFromImageSource(OH_ImagePackerNative *imagePacker,OH_PackingOptions *options, OH_ImageSourceNative *imageSource, int32_t fd)
```

**描述**

将一个ImageSource编码到文件中。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ImagePackerNative](capi-image-nativemodule-oh-imagepackernative.md) \*imagePacker | 被操作的OH\_ImagePackerNative指针。 |
| [OH\_PackingOptions](capi-image-nativemodule-oh-packingoptions.md) \*options | 编码选项参数。 |
| [OH\_ImageSourceNative](capi-image-nativemodule-oh-imagesourcenative.md) \*imageSource | 用于编码的image source指针。 |
| int32\_t fd | 可写的文件描述符。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_BAD\_PARAMETER：参数错误。  IMAGE\_DECODE\_FAILED：解码失败。  IMAGE\_UNKNOWN\_ERROR：未知错误。 |

### OH\_ImagePackerNative\_PackToFileFromPixelmap()

PhonePC/2in1TabletTVWearable

```
1. Image_ErrorCode OH_ImagePackerNative_PackToFileFromPixelmap(OH_ImagePackerNative *imagePacker,OH_PackingOptions *options, OH_PixelmapNative *pixelmap, int32_t fd)
```

**描述**

将一个Pixelmap编码到文件中。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ImagePackerNative](capi-image-nativemodule-oh-imagepackernative.md) \*imagePacker | 被操作的OH\_ImagePackerNative指针。 |
| [OH\_PackingOptions](capi-image-nativemodule-oh-packingoptions.md) \*options | 编码选项参数。 |
| [OH\_PixelmapNative](capi-image-nativemodule-oh-pixelmapnative.md) \*pixelmap | 用于编码的pixelmap指针。 |
| int32\_t fd | 可写的文件描述符。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_BAD\_PARAMETER：参数错误。  IMAGE\_DECODE\_FAILED：解码失败。  IMAGE\_UNKNOWN\_ERROR：未知错误。 |

### OH\_ImagePackerNative\_PackToFileFromPicture()

PhonePC/2in1TabletTVWearable

```
1. Image_ErrorCode OH_ImagePackerNative_PackToFileFromPicture(OH_ImagePackerNative *imagePacker,OH_PackingOptions *options, OH_PictureNative *picture, int32_t fd)
```

**描述**

将一个Picture编码到文件中。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ImagePackerNative](capi-image-nativemodule-oh-imagepackernative.md) \*imagePacker | 被操作的OH\_ImagePackerNative指针。 |
| [OH\_PackingOptions](capi-image-nativemodule-oh-packingoptions.md) \*options | 编码选项参数。 |
| [OH\_PictureNative](capi-image-nativemodule-oh-picturenative.md) \*picture | 用于编码的picture指针。 |
| int32\_t fd | 可写的文件描述符。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_BAD\_PARAMETER：参数错误。  IMAGE\_DECODE\_FAILED：解码失败。  IMAGE\_UNKNOWN\_ERROR：未知错误。 |

### OH\_ImagePackerNative\_PackToFileFromPixelmapSequence()

PhonePC/2in1TabletTVWearable

```
1. Image_ErrorCode OH_ImagePackerNative_PackToFileFromPixelmapSequence(OH_ImagePackerNative *imagePacker,OH_PackingOptionsForSequence *options, OH_PixelmapNative **pixelmapSequence, size_t sequenceLength, int32_t fd)
```

**描述**

将一个Pixelmap序列编码到文件中。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ImagePackerNative](capi-image-nativemodule-oh-imagepackernative.md) \*imagePacker | 被操作的OH\_ImagePackerNative指针。 |
| [OH\_PackingOptionsForSequence](pi-image-nativemodule-oh-packingoptionsforsequence.md) \*options | 编码选项参数 [OH\_PackingOptionsForSequence](pi-image-nativemodule-oh-packingoptionsforsequence.md)。 |
| [OH\_PixelmapNative](capi-image-nativemodule-oh-pixelmapnative.md) \*\*pixelmapSequence | 用于编码的Pixelmap序列指针。 |
| size\_t sequenceLength | 用于编码的Pixelmap序列长度。 |
| int32\_t fd | 可写的文件描述符。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_BAD\_PARAMETER：参数错误。  IMAGE\_DECODE\_FAILED：解码失败。 |

### OH\_ImagePackerNative\_GetSupportedFormats()

PhonePC/2in1TabletTVWearable

```
1. Image_ErrorCode OH_ImagePackerNative_GetSupportedFormats(Image_MimeType **supportedFormats, size_t *length)
```

**描述**

获取支持编码的图片格式。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Image\_MimeType](capi-image-nativemodule-image-string.md) \*\*supportedFormats | 支持编码的图片格式。 |
| size\_t \*length | 数组长度。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：操作成功。  IMAGE\_PACKER\_INVALID\_PARAMETER：参数异常，supportedFormats或length为空。 |

### OH\_ImagePackerNative\_Release()

PhonePC/2in1TabletTVWearable

```
1. Image_ErrorCode OH_ImagePackerNative_Release(OH_ImagePackerNative *imagePacker)
```

**描述**

释放OH\_ImagePackerNative指针。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ImagePackerNative](capi-image-nativemodule-oh-imagepackernative.md) \*imagePacker | 被操作的OH\_ImagePackerNative指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_BAD\_PARAMETER：参数错误。 |
