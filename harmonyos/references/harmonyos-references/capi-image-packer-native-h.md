---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-packer-native-h
title: image_packer_native.h
breadcrumb: API参考 > 媒体 > Image Kit（图片处理服务） > C API > 头文件 > image_packer_native.h
category: harmonyos-references
scraped_at: 2026-09-02T15:02:31+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:69f9e85670f31a450ca9518086936d8c3f173099ef5620d4661aaeab625b8e3a
---

## 概述

图片编码API。

**引用文件：** <multimedia/image\_framework/image/image\_packer\_native.h>

**库：** libimage\_packer.so

**系统能力：** SystemCapability.Multimedia.Image.ImagePacker

**起始版本：** 12

**相关模块：** [Image\_NativeModule](capi-image-nativemodule.md)

## 汇总

### 结构体

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [OH\_ImagePackerNative](capi-image-nativemodule-oh-imagepackernative.md) | OH\_ImagePackerNative | ImagePacker结构体类型，用于执行ImagePacker相关操作。 |
| [OH\_PackingOptions](capi-image-nativemodule-oh-packingoptions.md) | OH\_PackingOptions | OH\_PackingOptions是native层封装的图像编码选项结构体，不可直接操作，而是采用函数调用方式创建、释放结构体以及操作具体字段。 |
| [OH\_PackingOptionsForSequence](capi-image-nativemodule-oh-packingoptionsforsequence.md) | OH\_PackingOptionsForSequence | OH\_PackingOptionsForSequence是native层封装的图像序列编码选项结构体，不可直接操作，而是采用函数调用方式创建、释放结构体以及操作具体字段。 |

### 枚举

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [IMAGE\_PACKER\_DYNAMIC\_RANGE](capi-image-packer-native-h.md#image_packer_dynamic_range) | IMAGE\_PACKER\_DYNAMIC\_RANGE | 编码指定动态范围。 |

### 函数

| 名称 | 描述 |
| --- | --- |
| [Image\_ErrorCode OH\_PackingOptions\_Create(OH\_PackingOptions \*\*options)](capi-image-packer-native-h.md#oh_packingoptions_create) | 创建PackingOptions结构体的指针。 |
| [Image\_ErrorCode OH\_PackingOptions\_GetMimeType(OH\_PackingOptions \*options, Image\_MimeType \*format)](capi-image-packer-native-h.md#oh_packingoptions_getmimetype) | 获取编码参数中的MIME类型。该接口获取的format.data缺少字符串结束符'\0'，请谨慎使用。 |
| [Image\_ErrorCode OH\_PackingOptions\_GetMimeTypeWithNull(OH\_PackingOptions \*options, Image\_MimeType \*format)](capi-image-packer-native-h.md#oh_packingoptions_getmimetypewithnull) | 获取编码参数中的MIME类型。该接口获取的format.data以字符串结束符'\0'结尾。 |
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
| [Image\_ErrorCode OH\_PackingOptionsForSequence\_SetLoopCount(OH\_PackingOptionsForSequence \*options, uint32\_t loopCount)](capi-image-packer-native-h.md#oh_packingoptionsforsequence_setloopcount) | 设定编码时图片循环播放次数，取值范围为[0, 65535]，0表示无限循环；若无此字段，则表示不循环播放。 |
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

### IMAGE\_PACKER\_DYNAMIC\_RANGE

```c
enum IMAGE_PACKER_DYNAMIC_RANGE
```

**描述**

编码指定动态范围。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| IMAGE\_PACKER\_DYNAMIC\_RANGE\_AUTO = 0 | 编码动态范围根据图像信息自适应。 |
| IMAGE\_PACKER\_DYNAMIC\_RANGE\_SDR = 1 | 编码图片为标准动态范围。 |

## 函数说明

### OH\_PackingOptions\_Create()

```c
Image_ErrorCode OH_PackingOptions_Create(OH_PackingOptions **options)
```

**描述**

创建PackingOptions结构体的指针。

使用约束：options不能为空指针；接口返回失败时，输出参数内容不应使用。

资源管理：接口成功返回的OH\_PackingOptions对象由调用方管理，使用完成后应调用[OH\_PackingOptions\_Release](capi-image-packer-native-h.md#oh_packingoptions_release)释放。

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

```c
Image_ErrorCode OH_PackingOptions_GetMimeType(OH_PackingOptions *options,Image_MimeType *format)
```

**描述**

获取编码参数中的MIME类型。该接口获取的format.data缺少字符串结束符'\0'，请谨慎使用。

使用约束：options和format均不能为空指针。调用前若format->size不为0，则format->size必须大于或等于当前MIME类型长度。接口返回失败时，不应读取format.data。

资源管理：接口执行成功后，format.data由接口分配，调用方使用完成后应使用free()释放。该接口返回的format.data不以字符串结束符'\0'结尾，如需按C字符串处理，建议使用[OH\_PackingOptions\_GetMimeTypeWithNull](capi-image-packer-native-h.md#oh_packingoptions_getmimetypewithnull)。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_PackingOptions](capi-image-nativemodule-oh-packingoptions.md) \*options | 被操作的OH\_PackingOptions指针。 |
| [Image\_MimeType](capi-image-nativemodule-image-string.md) \*format | 图像格式。format无需手动初始化，系统将分配内存，但必须在使用后释放内存。  该接口获取到的format.data缺少字符串结束符'\0'，需要检查实际数据长度是否超出了申请缓冲区的长度。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_BAD\_PARAMETER：参数错误。 |

### OH\_PackingOptions\_GetMimeTypeWithNull()

```c
Image_ErrorCode OH_PackingOptions_GetMimeTypeWithNull(OH_PackingOptions *options,Image_MimeType *format)
```

**描述**

获取编码参数中的MIME类型。该接口获取的format.data以字符串结束符'\0'结尾。

使用场景：适用于读取字符串形式的MIME类型。与[OH\_PackingOptions\_GetMimeType](capi-image-packer-native-h.md#oh_packingoptions_getmimetype)相比，本接口返回的format.data以'\0'结尾，更适合直接按C字符串处理。

使用约束：options和format均不能为空指针。调用前若format->size不为0，则format->size必须大于或等于当前MIME类型长度。接口返回失败时，不应读取format.data。

资源管理：接口执行成功后，format.data由接口分配，调用方使用完成后应使用free()释放。

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

```c
Image_ErrorCode OH_PackingOptions_SetMimeType(OH_PackingOptions *options,Image_MimeType *format)
```

**描述**

设置MIME类型。

使用场景：用于设置OH\_PackingOptions的目标编码格式。使用OH\_PackingOptions进行ImageSource、PixelMap或Picture编码前，必须调用本接口设置MIME类型。未设置MIME类型时，编码接口会返回参数错误。

使用约束：options、format和format->data均不能为空指针，format->size必须大于0。format必须为支持编码的MIME类型，可通过[OH\_ImagePackerNative\_GetSupportedFormats](capi-image-packer-native-h.md#oh_imagepackernative_getsupportedformats)查询支持编码的图片格式。

资源管理：接口会拷贝传入的MIME类型数据，不持有调用方传入的format->data指针。接口返回后，调用方仍需自行管理format的生命周期。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_PackingOptions](capi-image-nativemodule-oh-packingoptions.md) \*options | 被操作的OH\_PackingOptions指针。 |
| [Image\_MimeType](capi-image-nativemodule-image-string.md) \*format | 目标编码格式。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_BAD\_PARAMETER：参数错误。 |

### OH\_PackingOptions\_GetQuality()

```c
Image_ErrorCode OH_PackingOptions_GetQuality(OH_PackingOptions *options,uint32_t *quality)
```

**描述**

获取编码质量。

使用约束：options和quality均不能为空指针。接口返回失败时，输出参数内容不应使用。

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

```c
Image_ErrorCode OH_PackingOptions_SetQuality(OH_PackingOptions *options,uint32_t quality)
```

**描述**

设置编码质量。

使用约束：options不能为空指针，quality取值范围为[0, 100]。OH\_PackingOptions创建后，quality默认值为0，建议设置quality不低于80。quality的实际效果取决于目标编码格式。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_PackingOptions](capi-image-nativemodule-oh-packingoptions.md) \*options | 被操作的OH\_PackingOptions指针。 |
| uint32\_t quality | 编码质量，取值范围为[0, 100]，默认值为0。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_BAD\_PARAMETER：参数错误。 |

### OH\_PackingOptions\_GetNeedsPackProperties()

```c
 Image_ErrorCode OH_PackingOptions_GetNeedsPackProperties(OH_PackingOptions *options,bool *needsPackProperties)
```

**描述**

获取OH\_PackingOptions结构体的needsPackProperties参数。

使用约束：options和needsPackProperties均不能为空指针。接口返回失败时，输出参数内容不应使用。

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

```c
Image_ErrorCode OH_PackingOptions_SetNeedsPackProperties(OH_PackingOptions *options,bool needsPackProperties)
```

**描述**

设置OH\_PackingOptions结构体的needsPackProperties参数。

使用场景：当需要在编码输出中保留或写入图片属性信息（例如Exif）时，将needsPackProperties设置为true。如果只关心像素内容、希望减少输出数据体积或目标格式不需要保留属性信息，可设置为false。

使用约束：options不能为空指针。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_PackingOptions](capi-image-nativemodule-oh-packingoptions.md) \*options | 被操作的OH\_PackingOptions指针。 |
| bool needsPackProperties | 是否需要编码图片属性信息（例如Exif）。true表示需要，false表示不需要。默认值为false。  如果原始图片本身没有Exif数据，那么即使设置needsPackProperties为true，输出文件也不会包含这些属性。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_BAD\_PARAMETER：参数错误。 |

### OH\_PackingOptions\_GetDesiredDynamicRange()

```c
Image_ErrorCode OH_PackingOptions_GetDesiredDynamicRange(OH_PackingOptions *options, int32_t* desiredDynamicRange)
```

**描述**

获取编码时期望的图片动态范围。

使用约束：options和desiredDynamicRange均不能为空指针。接口返回失败时，输出参数内容不应使用。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_PackingOptions](capi-image-nativemodule-oh-packingoptions.md) \*options | 被操作的OH\_PackingOptions指针。 |
| int32\_t\* desiredDynamicRange | 期望的动态范围[IMAGE\_PACKER\_DYNAMIC\_RANGE](capi-image-packer-native-h.md#image_packer_dynamic_range)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_BAD\_PARAMETER：参数错误。 |

### OH\_PackingOptions\_SetDesiredDynamicRange()

```c
Image_ErrorCode OH_PackingOptions_SetDesiredDynamicRange(OH_PackingOptions *options, int32_t desiredDynamicRange)
```

**描述**

设置编码时期望的图片动态范围。

使用约束：options不能为空指针。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_PackingOptions](capi-image-nativemodule-oh-packingoptions.md) \*options | 被操作的OH\_PackingOptions指针。 |
| int32\_t desiredDynamicRange | 期望的动态范围[IMAGE\_PACKER\_DYNAMIC\_RANGE](capi-image-packer-native-h.md#image_packer_dynamic_range)。默认值为IMAGE\_PACKER\_DYNAMIC\_RANGE\_SDR。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_BAD\_PARAMETER：参数错误。 |

### OH\_PackingOptions\_Release()

```c
Image_ErrorCode OH_PackingOptions_Release(OH_PackingOptions *options)
```

**描述**

释放OH\_PackingOptions指针。

使用约束：options不能为空指针。

资源管理：由[OH\_PackingOptions\_Create](capi-image-packer-native-h.md#oh_packingoptions_create)成功创建的对象，都应在编码完成后调用本接口释放。释放OH\_PackingOptions不会影响已经完成的编码输出，也不会释放OH\_ImagePackerNative对象；调用该接口后，options指向的OH\_PackingOptions对象会被释放，不应继续使用。

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

```c
Image_ErrorCode OH_PackingOptionsForSequence_Create(OH_PackingOptionsForSequence **options)
```

**描述**

创建OH\_PackingOptionsForSequence结构体的指针。

使用约束：options不能为空指针。接口返回失败时，输出参数内容不应使用。

资源管理：接口成功返回的OH\_PackingOptionsForSequence对象由调用方管理，使用完成后应调用[OH\_PackingOptionsForSequence\_Release](capi-image-packer-native-h.md#oh_packingoptionsforsequence_release)释放。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_PackingOptionsForSequence](capi-image-nativemodule-oh-packingoptionsforsequence.md) \*\*options | 用于操作的OH\_PackingOptionsForSequence指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_BAD\_PARAMETER：参数错误。 |

### OH\_PackingOptionsForSequence\_SetFrameCount()

```c
Image_ErrorCode OH_PackingOptionsForSequence_SetFrameCount(OH_PackingOptionsForSequence *options,uint32_t frameCount)
```

**描述**

设置编码时指定的帧数。

使用约束：options不能为空指针。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_PackingOptionsForSequence](capi-image-nativemodule-oh-packingoptionsforsequence.md) \*options | 用于操作的OH\_PackingOptionsForSequence指针。 |
| uint32\_t frameCount | 图片的帧数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_BAD\_PARAMETER：参数错误。 |

### OH\_PackingOptionsForSequence\_GetFrameCount()

```c
Image_ErrorCode OH_PackingOptionsForSequence_GetFrameCount(OH_PackingOptionsForSequence *options,uint32_t *frameCount)
```

**描述**

获取编码时指定的帧数。

使用约束：options和frameCount均不能为空指针。接口返回失败时，输出参数内容不应使用。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_PackingOptionsForSequence](capi-image-nativemodule-oh-packingoptionsforsequence.md) \*options | 用于操作的OH\_PackingOptionsForSequence指针。 |
| uint32\_t \*frameCount | 图片的帧数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_BAD\_PARAMETER：参数错误。 |

### OH\_PackingOptionsForSequence\_SetDelayTimeList()

```c
Image_ErrorCode OH_PackingOptionsForSequence_SetDelayTimeList(OH_PackingOptionsForSequence *options,int32_t *delayTimeList, size_t delayTimeListLength)
```

**描述**

设定编码时图片的延迟时间数组。

使用约束：options不能为空指针。

资源管理：接口会保存传入的delayTimeList指针，不拷贝数组内容。调用方需保证OH\_PackingOptionsForSequence对象使用期间delayTimeList指向的数据有效。多次调用该接口时，新的delayTimeList指针会替换此前保存的指针。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_PackingOptionsForSequence](capi-image-nativemodule-oh-packingoptionsforsequence.md) \*options | 用于操作的OH\_PackingOptionsForSequence指针。 |
| int32\_t \*delayTimeList | 图片延迟时间数组的指针。延迟时间的单位为10毫秒（ms）。 |
| size\_t delayTimeListLength | 图片延迟时间数组的长度。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_BAD\_PARAMETER：参数错误。 |

### OH\_PackingOptionsForSequence\_GetDelayTimeList()

```c
Image_ErrorCode OH_PackingOptionsForSequence_GetDelayTimeList(OH_PackingOptionsForSequence *options,int32_t *delayTimeList, size_t delayTimeListLength)
```

**描述**

获取编码时图片的延迟时间数组。

使用约束：options和delayTimeList均不能为空指针，delayTimeListLength必须大于0。接口会将已设置的延迟时间数组拷贝到调用方传入的delayTimeList缓冲区。接口返回失败时，输出缓冲区内容不应使用。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_PackingOptionsForSequence](capi-image-nativemodule-oh-packingoptionsforsequence.md) \*options | 用于操作的OH\_PackingOptionsForSequence指针。 |
| int32\_t \*delayTimeList | 图片延迟时间数组的指针。 |
| size\_t delayTimeListLength | 图片延迟时间数组的长度。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_BAD\_PARAMETER：参数错误。 |

### OH\_PackingOptionsForSequence\_SetDisposalTypes()

```c
Image_ErrorCode OH_PackingOptionsForSequence_SetDisposalTypes(OH_PackingOptionsForSequence *options,uint32_t *disposalTypes, size_t disposalTypesLength)
```

**描述**

设定编码时图片的过渡帧模式数组。

使用约束：options不能为空指针。

资源管理：接口会保存传入的disposalTypes指针，不拷贝数组内容。调用方需保证OH\_PackingOptionsForSequence对象使用期间disposalTypes指向的数据有效。多次调用该接口时，新的disposalTypes指针会替换此前保存的指针。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_PackingOptionsForSequence](capi-image-nativemodule-oh-packingoptionsforsequence.md) \*options | 用于操作的OH\_PackingOptionsForSequence指针。 |
| uint32\_t \*disposalTypes | 图片过渡帧模式数组的指针，图片帧过渡模式的参数，如果长度小于frameCount，不足的部分将使用disposalTypes中的最后一个值进行填充，可取值如下：  0：不需要任何操作。  1：保持图形不变。  2：恢复背景色。  3：恢复到之前的状态。 |
| size\_t disposalTypesLength | 图片过渡帧模式数组的长度。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_BAD\_PARAMETER：参数错误。 |

### OH\_PackingOptionsForSequence\_GetDisposalTypes()

```c
Image_ErrorCode OH_PackingOptionsForSequence_GetDisposalTypes(OH_PackingOptionsForSequence *options,uint32_t *disposalTypes, size_t disposalTypesLength)
```

**描述**

获取编码时图片的过渡帧模式数组。

使用约束：options和disposalTypes均不能为空指针，disposalTypesLength必须大于0。接口会将已设置的过渡帧模式数组拷贝到调用方传入的disposalTypes缓冲区。接口返回失败时，输出缓冲区内容不应使用。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_PackingOptionsForSequence](capi-image-nativemodule-oh-packingoptionsforsequence.md) \*options | 用于操作的OH\_PackingOptionsForSequence指针。 |
| uint32\_t \*disposalTypes | 图片过渡帧模式数组的指针。 |
| size\_t disposalTypesLength | 图片过渡帧模式数组的长度。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_BAD\_PARAMETER：参数错误。 |

### OH\_PackingOptionsForSequence\_SetLoopCount()

```c
Image_ErrorCode OH_PackingOptionsForSequence_SetLoopCount(OH_PackingOptionsForSequence *options, uint32_t loopCount)
```

**描述**

设定编码时图片循环播放次数，取值范围为[0, 65535]，0表示无限循环；若无此字段，则表示不循环播放。

使用约束：options不能为空指针。本接口仅保存传入的loopCount。当loopCount大于65535时，本接口仍会返回成功，但后续调用[OH\_ImagePackerNative\_PackToDataFromPixelmapSequence](capi-image-packer-native-h.md#oh_imagepackernative_packtodatafrompixelmapsequence)或[OH\_ImagePackerNative\_PackToFileFromPixelmapSequence](capi-image-packer-native-h.md#oh_imagepackernative_packtofilefrompixelmapsequence)编码时会返回参数错误。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_PackingOptionsForSequence](capi-image-nativemodule-oh-packingoptionsforsequence.md) \*options | 用于操作的OH\_PackingOptionsForSequence指针。 |
| uint32\_t loopCount | 图片循环播放次数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_BAD\_PARAMETER：参数错误。 |

### OH\_PackingOptionsForSequence\_GetLoopCount()

```c
Image_ErrorCode OH_PackingOptionsForSequence_GetLoopCount(OH_PackingOptionsForSequence *options, uint32_t *loopCount)
```

**描述**

获取编码时图片循环播放次数。

使用约束：options和loopCount均不能为空指针。接口返回失败时，输出参数内容不应使用。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_PackingOptionsForSequence](capi-image-nativemodule-oh-packingoptionsforsequence.md) \*options | 用于操作的OH\_PackingOptionsForSequence指针。 |
| uint32\_t \*loopCount | 图片循环播放次数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_BAD\_PARAMETER：参数错误。 |

### OH\_PackingOptionsForSequence\_Release()

```c
Image_ErrorCode OH_PackingOptionsForSequence_Release(OH_PackingOptionsForSequence *options)
```

**描述**

释放OH\_PackingOptionsForSequence指针。

使用约束：options不能为空指针。

资源管理：调用该接口后，options指向的OH\_PackingOptionsForSequence对象会被释放，不应继续使用。释放OH\_PackingOptionsForSequence对象不会释放通过[OH\_PackingOptionsForSequence\_SetDelayTimeList](capi-image-packer-native-h.md#oh_packingoptionsforsequence_setdelaytimelist)或[OH\_PackingOptionsForSequence\_SetDisposalTypes](capi-image-packer-native-h.md#oh_packingoptionsforsequence_setdisposaltypes)传入的数组。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_PackingOptionsForSequence](capi-image-nativemodule-oh-packingoptionsforsequence.md) \*options | 用于操作的OH\_PackingOptionsForSequence指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_BAD\_PARAMETER：参数错误。 |

### OH\_ImagePackerNative\_Create()

```c
Image_ErrorCode OH_ImagePackerNative_Create(OH_ImagePackerNative **imagePacker)
```

**描述**

创建OH\_ImagePackerNative指针。

使用场景：适用于将ImageSource、PixelMap、Picture或PixelMap序列编码为JPEG、PNG、WebP等格式的数据或文件。创建ImagePacker后，需要结合OH\_PackingOptions或OH\_PackingOptionsForSequence设置编码格式、质量、是否保留图片属性等参数。

使用约束：imagePacker不能为空指针。接口返回失败时，输出参数内容不应使用。

资源管理：成功创建的OH\_ImagePackerNative对象由调用方持有，使用完成后必须调用[OH\_ImagePackerNative\_Release](capi-image-packer-native-h.md#oh_imagepackernative_release)释放。Packer不会接管输入ImageSource、PixelMap、Picture或编码参数对象的生命周期。

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

```c
Image_ErrorCode OH_ImagePackerNative_PackToDataFromImageSource(OH_ImagePackerNative *imagePacker,OH_PackingOptions *options, OH_ImageSourceNative *imageSource, uint8_t *outData, size_t *size)
```

**描述**

将ImageSource编码为指定格式的数据。

使用场景：适用于将已有ImageSource转码为另一种图片格式，或在修改图片属性后重新输出为内存数据。

使用约束：imagePacker、options、imageSource、outData和size均不能为空指针。调用前，\*size应设置为outData的容量。接口返回失败时，不应使用outData中的内容或size输出值。

资源管理：outData由调用方申请和释放。调用前，\*size应设置为outData可写缓冲区大小。调用成功后，\*size会更新为实际写入的编码数据长度。imagePacker、options和imageSource的生命周期仍由调用方管理，本接口不会释放这些对象。

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

```c
Image_ErrorCode OH_ImagePackerNative_PackToDataFromPixelmap(OH_ImagePackerNative *imagePacker,OH_PackingOptions *options, OH_PixelmapNative *pixelmap, uint8_t *outData, size_t *size)
```

**描述**

将Pixelmap编码为指定格式的数据。

使用场景：适用于将解码、编辑、绘制或算法处理后的PixelMap编码为JPEG、PNG、WebP等格式的内存数据，以便上传、缓存或继续写入文件。

使用约束：imagePacker、options、pixelmap、outData和size均不能为空指针。调用前，\*size应设置为outData的容量；接口返回失败时，不应使用outData中的内容或size输出值。

资源管理：outData由调用方申请和释放。调用前，\*size应设置为outData可写缓冲区大小。调用成功后，\*size会更新为实际写入的编码数据长度。imagePacker、options和pixelmap的生命周期仍由调用方管理，本接口不会释放这些对象。

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

```c
Image_ErrorCode OH_ImagePackerNative_PackToDataFromPicture(OH_ImagePackerNative *imagePacker,OH_PackingOptions *options, OH_PictureNative *picture, uint8_t *outData, size_t *size)
```

**描述**

将Picture编码为指定格式的数据。

使用约束：imagePacker、options、picture、outData和size均不能为空指针。调用前，\*size应设置为outData的容量。接口返回失败时，不应使用outData中的内容或size输出值。

资源管理：outData由调用方申请和释放。调用前，\*size应设置为outData可写缓冲区大小。调用成功后，\*size会更新为实际写入的编码数据长度。imagePacker、options和picture的生命周期仍由调用方管理，本接口不会释放这些对象。

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

```c
Image_ErrorCode OH_ImagePackerNative_PackToDataFromPixelmapSequence(OH_ImagePackerNative *imagePacker,OH_PackingOptionsForSequence *options, OH_PixelmapNative **pixelmapSequence,size_t sequenceLength, uint8_t *outData, size_t *outDataSize)
```

**描述**

将Pixelmap序列编码为数据。

使用场景：适用于将多帧PixelMap编码为动图或其他支持序列帧的图片格式。编码前应通过OH\_PackingOptionsForSequence设置帧数、延迟时间、循环次数等参数。

使用约束：接口返回失败时，不应使用outData中的内容或outDataSize输出值。

资源管理：outData由调用方申请和释放。imagePacker、options和pixelmapSequence中PixelMap对象的生命周期仍由调用方管理，本接口不会释放这些对象。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ImagePackerNative](capi-image-nativemodule-oh-imagepackernative.md) \*imagePacker | 被操作的OH\_ImagePackerNative指针，不允许为NULL。 |
| [OH\_PackingOptionsForSequence](capi-image-nativemodule-oh-packingoptionsforsequence.md) \*options | 编码选项参数，不允许为NULL。frameCount必须大于0，需设置有效的delayTimeList，loopCount取值范围为[0, 65535]。delayTimeList中的每个延迟时间必须大于0且不超过65535，单位为10毫秒（ms）。disposalTypes中的每个取值必须小于等于3。 |
| [OH\_PixelmapNative](capi-image-nativemodule-oh-pixelmapnative.md) \*\*pixelmapSequence | 用于编码的Pixelmap序列指针，不允许为NULL。数组中用于编码的Pixelmap指针不允许为NULL。 |
| size\_t sequenceLength | 用于编码的Pixelmap序列长度，必须大于0。 |
| uint8\_t \*outData | 用于存储编码后图像输出数据的缓冲区，不允许为NULL。 |
| size\_t \*outDataSize | 用于存储编码后图像输出数据缓冲区大小的指针，不允许为NULL。调用前，\*outDataSize应设置为outData可写缓冲区大小；调用成功后，\*outDataSize会更新为实际写入的编码数据长度。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_BAD\_PARAMETER：参数错误。  IMAGE\_DECODE\_FAILED：解码失败。 |

### OH\_ImagePackerNative\_PackToFileFromImageSource()

```c
Image_ErrorCode OH_ImagePackerNative_PackToFileFromImageSource(OH_ImagePackerNative *imagePacker,OH_PackingOptions *options, OH_ImageSourceNative *imageSource, int32_t fd)
```

**描述**

将一个ImageSource编码到文件中。

使用场景：适用于将ImageSource转码后直接写入文件描述符，避免调用方自行管理编码后的内存缓冲区。

使用约束：imagePacker、options和imageSource均不能为空指针，fd必须为可写文件描述符。

资源管理：fd必须是可写文件描述符，文件描述符的打开和关闭由调用方负责。接口不会释放imagePacker、options或imageSource。

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

```c
Image_ErrorCode OH_ImagePackerNative_PackToFileFromPixelmap(OH_ImagePackerNative *imagePacker,OH_PackingOptions *options, OH_PixelmapNative *pixelmap, int32_t fd)
```

**描述**

将一个Pixelmap编码到文件中。

使用场景：适用于将处理后的PixelMap直接保存为文件。与PackToDataFromPixelmap相比，该接口不需要调用方预先分配输出数据缓冲区。

使用约束：imagePacker、options和pixelmap均不能为空指针，fd必须为可写文件描述符。

资源管理：fd必须是可写文件描述符，文件描述符的打开和关闭由调用方负责。接口不会释放imagePacker、options或pixelmap。

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

```c
Image_ErrorCode OH_ImagePackerNative_PackToFileFromPicture(OH_ImagePackerNative *imagePacker,OH_PackingOptions *options, OH_PictureNative *picture, int32_t fd)
```

**描述**

将一个Picture编码到文件中。

使用约束：imagePacker、options和picture均不能为空指针，fd必须为可写文件描述符。

资源管理：fd的打开和关闭由调用方负责。接口不会释放imagePacker、options或picture。

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

```c
Image_ErrorCode OH_ImagePackerNative_PackToFileFromPixelmapSequence(OH_ImagePackerNative *imagePacker,OH_PackingOptionsForSequence *options, OH_PixelmapNative **pixelmapSequence, size_t sequenceLength, int32_t fd)
```

**描述**

将一个Pixelmap序列编码到文件中。

使用约束：接口返回失败时，目标文件中的内容不应继续使用。

资源管理：fd的打开和关闭由调用方负责。接口不会释放imagePacker、options或pixelmapSequence中的PixelMap对象。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ImagePackerNative](capi-image-nativemodule-oh-imagepackernative.md) \*imagePacker | 被操作的OH\_ImagePackerNative指针，不允许为NULL。 |
| [OH\_PackingOptionsForSequence](capi-image-nativemodule-oh-packingoptionsforsequence.md) \*options | 编码选项参数，不允许为NULL。frameCount必须大于0，需设置有效的delayTimeList，loopCount取值范围为[0, 65535]。delayTimeList中的每个延迟时间必须大于0且不超过65535。disposalTypes中的每个取值必须小于等于3。 |
| [OH\_PixelmapNative](capi-image-nativemodule-oh-pixelmapnative.md) \*\*pixelmapSequence | 用于编码的Pixelmap序列指针，不允许为NULL。数组中用于编码的Pixelmap指针不允许为NULL。 |
| size\_t sequenceLength | 用于编码的Pixelmap序列长度，必须大于0。 |
| int32\_t fd | 文件描述符，必须为可写文件描述符。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_BAD\_PARAMETER：参数错误。  IMAGE\_DECODE\_FAILED：解码失败。 |

### OH\_ImagePackerNative\_GetSupportedFormats()

```c
Image_ErrorCode OH_ImagePackerNative_GetSupportedFormats(Image_MimeType **supportedFormats, size_t *length)
```

**描述**

获取支持编码的图片格式。

使用场景：适用于在编码前动态查询当前系统支持的目标格式，并据此设置[OH\_PackingOptions\_SetMimeType](capi-image-packer-native-h.md#oh_packingoptions_setmimetype)的MIME类型。

使用约束：supportedFormats和length均不能为空指针。接口返回失败时，输出参数内容不应使用。

资源管理：接口成功返回的supportedFormats数组由系统内部管理，调用方不需要也不应释放或修改。如需长期保存，应自行拷贝数组内容。

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

```c
Image_ErrorCode OH_ImagePackerNative_Release(OH_ImagePackerNative *imagePacker)
```

**描述**

释放OH\_ImagePackerNative指针。

使用约束：imagePacker不能为空指针。

资源管理：由[OH\_ImagePackerNative\_Create](capi-image-packer-native-h.md#oh_imagepackernative_create)成功创建的对象，在使用完毕后必须调用本接口释放。释放Packer不会释放OH\_PackingOptions、OH\_PackingOptionsForSequence、OH\_ImageSourceNative、OH\_PixelmapNative或OH\_PictureNative对象。调用该接口后，imagePacker指向的OH\_ImagePackerNative对象会被释放，不应继续使用。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ImagePackerNative](capi-image-nativemodule-oh-imagepackernative.md) \*imagePacker | 被操作的OH\_ImagePackerNative指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Image\_ErrorCode](capi-image-common-h.md#image_errorcode) | IMAGE\_SUCCESS：执行成功。  IMAGE\_BAD\_PARAMETER：参数错误。 |
