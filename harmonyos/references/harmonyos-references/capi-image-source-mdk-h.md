---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-source-mdk-h
title: image_source_mdk.h
breadcrumb: API参考 > 媒体 > Image Kit（图片处理服务） > C API > 头文件 > image_source_mdk.h
category: harmonyos-references
scraped_at: 2026-04-28T08:13:21+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:573da28d77d93e22b0cadaca5fe804595ef97fe8eeab48f91880303e6e7d24fe
---

## 概述

PhonePC/2in1TabletTVWearable

声明将ImageSource解码成像素位图的方法。

**库：** libimage\_source\_ndk.z.so

**系统能力：** SystemCapability.Multimedia.Image.Core

**引用文件：** <multimedia/image\_framework/image\_source\_mdk.h>

**起始版本：** 10

**相关模块：** [Image](capi-image.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 结构体

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [OhosImageRegion](capi-image-ohosimageregion.md) | - | 定义图像源解码的范围选项。是[OhosImageDecodingOps](capi-image-ohosimagedecodingops.md)的成员变量。 |
| [ImageSourceNative\_](capi-image-imagesourcenative-.md) | ImageSourceNative | 为图像源方法定义native层图像源对象。 |
| [OhosImageSourceOps](capi-image-ohosimagesourceops.md) | - | 定义图像源选项信息。此选项给[OH\_ImageSource\_CreateFromUri](capi-image-source-mdk-h.md#oh_imagesource_createfromuri)、[OH\_ImageSource\_CreateFromFd](capi-image-source-mdk-h.md#oh_imagesource_createfromfd)、[OH\_ImageSource\_CreateFromData](capi-image-source-mdk-h.md#oh_imagesource_createfromdata)和[OH\_ImageSource\_CreateIncremental](capi-image-source-mdk-h.md#oh_imagesource_createincremental)接口使用。 |
| [OhosImageDecodingOps](capi-image-ohosimagedecodingops.md) | - | 定义图像源解码选项。此选项给[OH\_ImageSource\_CreatePixelMap](capi-image-source-mdk-h.md#oh_imagesource_createpixelmap)和[OH\_ImageSource\_CreatePixelMapList](capi-image-source-mdk-h.md#oh_imagesource_createpixelmaplist)接口使用。 |
| [OhosImageSourceInfo](capi-image-ohosimagesourceinfo.md) | - | 定义图像源信息，由[OH\_ImageSource\_GetImageInfo](capi-image-source-mdk-h.md#oh_imagesource_getimageinfo)获取。 |
| [OhosImageSource](capi-image-ohosimagesource.md) | - | 定义图像源输入资源，每次仅接收一种类型。由[OH\_ImageSource\_CreateFromUri](capi-image-source-mdk-h.md#oh_imagesource_createfromuri)、[OH\_ImageSource\_CreateFromFd](capi-image-source-mdk-h.md#oh_imagesource_createfromfd)和[OH\_ImageSource\_CreateFromData](capi-image-source-mdk-h.md#oh_imagesource_createfromdata)获取。 |
| [OhosImageSourceDelayTimeList](capi-image-ohosimagesourcedelaytimelist.md) | - | 定义图像源延迟时间列表。由[OH\_ImageSource\_GetDelayTime](capi-image-source-mdk-h.md#oh_imagesource_getdelaytime)获取。 |
| [OhosImageSourceSupportedFormat](capi-image-ohosimagesourcesupportedformat.md) | - | 定义图像源支持的格式字符串。此选项给[OhosImageSourceSupportedFormatList](capi-image-ohosimagesourcesupportedformatlist.md)和[OH\_ImageSource\_GetSupportedFormats](capi-image-source-mdk-h.md#oh_imagesource_getsupportedformats)接口使用。 |
| [OhosImageSourceSupportedFormatList](capi-image-ohosimagesourcesupportedformatlist.md) | - | 定义图像源支持的格式字符串列表。由[OH\_ImageSource\_GetSupportedFormats](capi-image-source-mdk-h.md#oh_imagesource_getsupportedformats)获取。 |
| [OhosImageSourceProperty](capi-image-ohosimagesourceproperty.md) | - | 定义图像源属性键值字符串。此选项给[OH\_ImageSource\_GetImageProperty](capi-image-source-mdk-h.md#oh_imagesource_getimageproperty)和[OH\_ImageSource\_ModifyImageProperty](capi-image-source-mdk-h.md#oh_imagesource_modifyimageproperty)接口使用。 |
| [OhosImageSourceUpdateData](capi-image-ohosimagesourceupdatedata.md) | - | 定义图像源更新数据选项，由[OH\_ImageSource\_UpdateData](capi-image-source-mdk-h.md#oh_imagesource_updatedata)获取。 |

### 函数

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [int32\_t OH\_ImageSource\_Create(napi\_env env, struct OhosImageSource\* src, struct OhosImageSourceOps\* ops, napi\_value \*res)](capi-image-source-mdk-h.md#oh_imagesource_create) | 通过给定的信息OhosImageSource和OhosImageSourceOps结构体，获取JavaScript native层API ImageSource对象。 |
| [int32\_t OH\_ImageSource\_CreateFromUri(napi\_env env, char\* uri, size\_t size, struct OhosImageSourceOps\* ops, napi\_value \*res)](capi-image-source-mdk-h.md#oh_imagesource_createfromuri) | 通过给定的标识符URI和[OhosImageSourceOps](capi-image-ohosimagesourceops.md)结构体，获取JavaScript native层API ImageSource对象。 |
| [int32\_t OH\_ImageSource\_CreateFromFd(napi\_env env, int32\_t fd, struct OhosImageSourceOps\* ops, napi\_value \*res)](capi-image-source-mdk-h.md#oh_imagesource_createfromfd) | 通过给定的文件描述符fd和[OhosImageSourceOps](capi-image-ohosimagesourceops.md)结构体，获取JavaScript native层API ImageSource对象。 |
| [int32\_t OH\_ImageSource\_CreateFromData(napi\_env env, uint8\_t\* data, size\_t dataSize, struct OhosImageSourceOps\* ops, napi\_value \*res)](capi-image-source-mdk-h.md#oh_imagesource_createfromdata) | 通过给定的图像源缓冲区资源data和[OhosImageSourceOps](capi-image-ohosimagesourceops.md)结构体，获取JavaScript native层API ImageSource对象。 |
| [int32\_t OH\_ImageSource\_CreateFromRawFile(napi\_env env, RawFileDescriptor rawFile, struct OhosImageSourceOps\* ops, napi\_value \*res)](capi-image-source-mdk-h.md#oh_imagesource_createfromrawfile) | 通过给定的资源描述符[RawFileDescriptor](capi-rawfile-rawfiledescriptor.md)和[OhosImageSourceOps](capi-image-ohosimagesourceops.md)结构体，获取JavaScript native层API ImageSource对象。 |
| [int32\_t OH\_ImageSource\_CreateIncremental(napi\_env env, struct OhosImageSource\* source, struct OhosImageSourceOps\* ops, napi\_value \*res)](capi-image-source-mdk-h.md#oh_imagesource_createincremental) | 通过给定的信息[OhosImageSource](capi-image-ohosimagesource.md)和[OhosImageSourceOps](capi-image-ohosimagesourceops.md)结构，获取增量类型的JavaScript Native API ImageSource对象，图像数据应通过[OH\_ImageSource\_UpdateData](capi-image-source-mdk-h.md#oh_imagesource_updatedata)更新。 |
| [int32\_t OH\_ImageSource\_CreateIncrementalFromData(napi\_env env, uint8\_t\* data, size\_t dataSize, struct OhosImageSourceOps\* ops, napi\_value \*res)](capi-image-source-mdk-h.md#oh_imagesource_createincrementalfromdata) | 通过给定的图像源缓冲区资源data和[OhosImageSourceOps](capi-image-ohosimagesourceops.md)结构体，获取增量类型的JavaScript Native API ImageSource对象，图像数据应通过[OH\_ImageSource\_UpdateData](capi-image-source-mdk-h.md#oh_imagesource_updatedata)更新。 |
| [int32\_t OH\_ImageSource\_GetSupportedFormats(struct OhosImageSourceSupportedFormatList\* res)](capi-image-source-mdk-h.md#oh_imagesource_getsupportedformats) | 获取所有支持的解码格式元标记。 |
| [ImageSourceNative\* OH\_ImageSource\_InitNative(napi\_env env, napi\_value source)](capi-image-source-mdk-h.md#oh_imagesource_initnative) | 从输入JavaScript native层ImageSource对象中，转换成[ImageSourceNative](capi-image-imagesourcenative-.md)值。 |
| [int32\_t OH\_ImageSource\_CreatePixelMap(const ImageSourceNative\* native, struct OhosImageDecodingOps\* ops, napi\_value \*res)](capi-image-source-mdk-h.md#oh_imagesource_createpixelmap) | 通过一个给定的选项[OhosImageDecodingOps](capi-image-ohosimagedecodingops.md)结构体，从ImageSource中解码JavaScript native层PixelMap对象。 |
| [int32\_t OH\_ImageSource\_CreatePixelMapList(const ImageSourceNative\* native, struct OhosImageDecodingOps\* ops, napi\_value \*res)](capi-image-source-mdk-h.md#oh_imagesource_createpixelmaplist) | 通过一个给定的选项[OhosImageDecodingOps](capi-image-ohosimagedecodingops.md)结构体，从ImageSource中解码所有的JavaScript native层PixelMap对象列表。 |
| [int32\_t OH\_ImageSource\_GetDelayTime(const ImageSourceNative\* native, struct OhosImageSourceDelayTimeList\* res)](capi-image-source-mdk-h.md#oh_imagesource_getdelaytime) | 从ImageSource（如GIF图像源）获取延迟时间列表。 |
| [int32\_t OH\_ImageSource\_GetFrameCount(const ImageSourceNative\* native, uint32\_t \*res)](capi-image-source-mdk-h.md#oh_imagesource_getframecount) | 从ImageSource中获取帧计数。 |
| [int32\_t OH\_ImageSource\_GetImageInfo(const ImageSourceNative\* native, int32\_t index, struct OhosImageSourceInfo\* info)](capi-image-source-mdk-h.md#oh_imagesource_getimageinfo) | 通过索引从ImageSource获取图像源信息。 |
| [int32\_t OH\_ImageSource\_GetImageProperty(const ImageSourceNative\* native, struct OhosImageSourceProperty\* key, struct OhosImageSourceProperty\* value)](capi-image-source-mdk-h.md#oh_imagesource_getimageproperty) | 通过关键字从ImageSource中获取图像源属性。 |
| [int32\_t OH\_ImageSource\_UpdateData(const ImageSourceNative\* native, struct OhosImageSourceUpdateData\* data)](capi-image-source-mdk-h.md#oh_imagesource_updatedata) | 为了增量类型的ImageSource更新源数据。 |
| [int32\_t OH\_ImageSource\_Release(ImageSourceNative\* native)](capi-image-source-mdk-h.md#oh_imagesource_release) | 释放native层图像源 **ImageSourceNative**。 |

### 变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| const char\* OHOS\_IMAGE\_PROPERTY\_BITS\_PER\_SAMPLE = "BitsPerSample" | 定义每个样本比特的图像属性关键字。  此标签给[OH\_ImageSource\_GetImageProperty](capi-image-source-mdk-h.md#oh_imagesource_getimageproperty)和[OH\_ImageSource\_ModifyImageProperty](capi-image-source-mdk-h.md#oh_imagesource_modifyimageproperty)接口使用。  **起始版本：** 10 |
| const char\* OHOS\_IMAGE\_PROPERTY\_ORIENTATION = "Orientation" | 定义方向的图像属性关键字。  此标签给[OH\_ImageSource\_GetImageProperty](capi-image-source-mdk-h.md#oh_imagesource_getimageproperty)和[OH\_ImageSource\_ModifyImageProperty](capi-image-source-mdk-h.md#oh_imagesource_modifyimageproperty)接口使用。  **起始版本：** 10 |
| const char\* OHOS\_IMAGE\_PROPERTY\_IMAGE\_LENGTH = "ImageLength" | 定义图像长度的图像属性关键字。  此标签给[OH\_ImageSource\_GetImageProperty](capi-image-source-mdk-h.md#oh_imagesource_getimageproperty)和[OH\_ImageSource\_ModifyImageProperty](capi-image-source-mdk-h.md#oh_imagesource_modifyimageproperty)接口使用。  **起始版本：** 10 |
| const char\* OHOS\_IMAGE\_PROPERTY\_IMAGE\_WIDTH = "ImageWidth" | 定义图像宽度的图像属性关键字。  此标签给[OH\_ImageSource\_GetImageProperty](capi-image-source-mdk-h.md#oh_imagesource_getimageproperty)和[OH\_ImageSource\_ModifyImageProperty](capi-image-source-mdk-h.md#oh_imagesource_modifyimageproperty)接口使用。  **起始版本：** 10 |
| const char\* OHOS\_IMAGE\_PROPERTY\_GPS\_LATITUDE = "GPSLatitude" | 定义GPS纬度的图像属性关键字。  此标签给[OH\_ImageSource\_GetImageProperty](capi-image-source-mdk-h.md#oh_imagesource_getimageproperty)和[OH\_ImageSource\_ModifyImageProperty](capi-image-source-mdk-h.md#oh_imagesource_modifyimageproperty)接口使用。  **起始版本：** 10 |
| const char\* OHOS\_IMAGE\_PROPERTY\_GPS\_LONGITUDE = "GPSLongitude" | 定义GPS经度的图像属性关键字。  此标签给[OH\_ImageSource\_GetImageProperty](capi-image-source-mdk-h.md#oh_imagesource_getimageproperty)和[OH\_ImageSource\_ModifyImageProperty](capi-image-source-mdk-h.md#oh_imagesource_modifyimageproperty)接口使用。  **起始版本：** 10 |
| const char\* OHOS\_IMAGE\_PROPERTY\_GPS\_LATITUDE\_REF = "GPSLatitudeRef" | 定义GPS纬度参考的图像属性关键字。  此标签给[OH\_ImageSource\_GetImageProperty](capi-image-source-mdk-h.md#oh_imagesource_getimageproperty)和[OH\_ImageSource\_ModifyImageProperty](capi-image-source-mdk-h.md#oh_imagesource_modifyimageproperty)接口使用。  **起始版本：** 10 |
| const char\* OHOS\_IMAGE\_PROPERTY\_GPS\_LONGITUDE\_REF = "GPSLongitudeRef" | 定义GPS经度参考的图像属性关键字。  此标签给[OH\_ImageSource\_GetImageProperty](capi-image-source-mdk-h.md#oh_imagesource_getimageproperty)和[OH\_ImageSource\_ModifyImageProperty](capi-image-source-mdk-h.md#oh_imagesource_modifyimageproperty)接口使用。  **起始版本：** 10 |
| const char\* OHOS\_IMAGE\_PROPERTY\_DATE\_TIME\_ORIGINAL = "DateTimeOriginal" | 定义初始日期时间的图像属性关键字。  此标签给[OH\_ImageSource\_GetImageProperty](capi-image-source-mdk-h.md#oh_imagesource_getimageproperty)和[OH\_ImageSource\_ModifyImageProperty](capi-image-source-mdk-h.md#oh_imagesource_modifyimageproperty)接口使用。  **起始版本：** 10 |
| const char\* OHOS\_IMAGE\_PROPERTY\_EXPOSURE\_TIME = "ExposureTime" | 定义曝光时间的图像属性关键字。  此标签给[OH\_ImageSource\_GetImageProperty](capi-image-source-mdk-h.md#oh_imagesource_getimageproperty)和[OH\_ImageSource\_ModifyImageProperty](capi-image-source-mdk-h.md#oh_imagesource_modifyimageproperty)接口使用。  **起始版本：** 10 |
| const char\* OHOS\_IMAGE\_PROPERTY\_SCENE\_TYPE = "SceneType" | 定义场景类型的图像属性关键字。  此标签给[OH\_ImageSource\_GetImageProperty](capi-image-source-mdk-h.md#oh_imagesource_getimageproperty)和[OH\_ImageSource\_ModifyImageProperty](capi-image-source-mdk-h.md#oh_imagesource_modifyimageproperty)接口使用。  **起始版本：** 10 |
| const char\* OHOS\_IMAGE\_PROPERTY\_ISO\_SPEED\_RATINGS = "ISOSpeedRatings" | 定义ISO速度等级的图像属性关键字。  此标签给[OH\_ImageSource\_GetImageProperty](capi-image-source-mdk-h.md#oh_imagesource_getimageproperty)和[OH\_ImageSource\_ModifyImageProperty](capi-image-source-mdk-h.md#oh_imagesource_modifyimageproperty)接口使用。  **起始版本：** 10 |
| const char\* OHOS\_IMAGE\_PROPERTY\_F\_NUMBER = "FNumber" | 定义FNumber的图像属性关键字。  此标签给[OH\_ImageSource\_GetImageProperty](capi-image-source-mdk-h.md#oh_imagesource_getimageproperty)和[OH\_ImageSource\_ModifyImageProperty](capi-image-source-mdk-h.md#oh_imagesource_modifyimageproperty)接口使用。  **起始版本：** 10 |
| const char\* OHOS\_IMAGE\_PROPERTY\_COMPRESSED\_BITS\_PER\_PIXEL = "CompressedBitsPerPixel" | 定义每个像素的压缩比特的图像属性关键字。  此标签给[OH\_ImageSource\_GetImageProperty](capi-image-source-mdk-h.md#oh_imagesource_getimageproperty)和[OH\_ImageSource\_ModifyImageProperty](capi-image-source-mdk-h.md#oh_imagesource_modifyimageproperty)接口使用。  **起始版本：** 10 |

## 函数说明

PhonePC/2in1TabletTVWearable

### OH\_ImageSource\_Create()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ImageSource_Create(napi_env env, struct OhosImageSource* src, struct OhosImageSourceOps* ops, napi_value *res)
```

**描述**

通过给定的信息OhosImageSource和OhosImageSourceOps结构体，获取JavaScript native层API ImageSource对象。

**起始版本：** 10

**废弃版本：** 11

**替代接口：** [OH\_ImageSource\_CreateFromUri](capi-image-source-mdk-h.md#oh_imagesource_createfromuri)，[OH\_ImageSource\_CreateFromFd](capi-image-source-mdk-h.md#oh_imagesource_createfromfd)，[OH\_ImageSource\_CreateFromData](capi-image-source-mdk-h.md#oh_imagesource_createfromdata)

**参数：**

| 参数项 | 描述 |
| --- | --- |
| napi\_env env | 表明JNI环境的指针。 |
| struct OhosImageSource\* src | 表明创建一个图像源的信息。 |
| struct [OhosImageSourceOps](capi-image-ohosimagesourceops.md)\* ops | 表明创建一个图像源的选项。 |
| napi\_value \*res | 表明JavaScript native层API ImageSource对象的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 参考[IRNdkErrCode](capi-image-mdk-common-h.md#irndkerrcode)：  OHOS\_IMAGE\_RESULT\_SUCCESS：操作成功。  IMAGE\_RESULT\_BAD\_PARAMETER：参数错误。  IMAGE\_RESULT\_JNI\_ENV\_ABNORMAL：JNI环境异常。  IMAGE\_RESULT\_INVALID\_PARAMETER：参数无效。  IMAGE\_RESULT\_SOURCE\_DATA\_INCOMPLETE：图像源数据不完整。  IMAGE\_RESULT\_SOURCE\_DATA：图像源数据错误。  IMAGE\_RESULT\_GET\_DATA\_ABNORMAL：图像获取数据错误。  IMAGE\_RESULT\_TOO\_LARGE：图像数据太大。  IMAGE\_RESULT\_DECODE\_FAILED：解码失败。  IMAGE\_RESULT\_DECODE\_HEAD\_ABNORMAL：图像解码头错误。  IMAGE\_RESULT\_DECODE\_EXIF\_UNSUPPORT：图像解码EXIF不支持。  IMAGE\_RESULT\_PROPERTY\_NOT\_EXIST：图像属性不存在。  IMAGE\_RESULT\_FILE\_DAMAGED：文件损坏。  IMAGE\_RESULT\_FILE\_FD\_ERROR：文件FD错误。  IMAGE\_RESULT\_STREAM\_SIZE\_ERROR：数据流错误。  IMAGE\_RESULT\_SEEK\_FAILED：查找文件失败。  IMAGE\_RESULT\_PEEK\_FAILED：速览文件失败。  IMAGE\_RESULT\_FREAD\_FAILED：读取文件失败。 |

### OH\_ImageSource\_CreateFromUri()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ImageSource_CreateFromUri(napi_env env, char* uri, size_t size,struct OhosImageSourceOps* ops, napi_value *res)
```

**描述**

通过给定的标识符URI和[OhosImageSourceOps](capi-image-ohosimagesourceops.md)结构体，获取JavaScript native层API ImageSource对象。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| napi\_env env | 表明JNI环境的指针。 |
| char\* uri | 表明图像源资源标识符，接受文件资源或者base64资源。当前文件资源只支持绝对路径。 |
| size\_t size | 表明图像源资源URI的长度。 |
| struct [OhosImageSourceOps](capi-image-ohosimagesourceops.md)\* ops | 表明创建一个图像源的选项。 |
| napi\_value \*res | 表明JavaScript native层API ImageSource对象的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 参考[IRNdkErrCode](capi-image-mdk-common-h.md#irndkerrcode)：  OHOS\_IMAGE\_RESULT\_SUCCESS：操作成功。  IMAGE\_RESULT\_BAD\_PARAMETER：参数错误。  IMAGE\_RESULT\_JNI\_ENV\_ABNORMAL：JNI环境异常。  IMAGE\_RESULT\_INVALID\_PARAMETER：参数无效。 |

### OH\_ImageSource\_CreateFromFd()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ImageSource_CreateFromFd(napi_env env, int32_t fd,struct OhosImageSourceOps* ops, napi_value *res)
```

**描述**

通过给定的文件描述符fd和[OhosImageSourceOps](capi-image-ohosimagesourceops.md)结构体，获取JavaScript native层API ImageSource对象。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| napi\_env env | 表明JNI环境的指针。 |
| int32\_t fd | 表明图像源文件资源描述符。 |
| struct [OhosImageSourceOps](capi-image-ohosimagesourceops.md)\* ops | 表明创建一个图像源的选项。 |
| napi\_value \*res | 表明JavaScript native层API ImageSource对象的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 参考[IRNdkErrCode](capi-image-mdk-common-h.md#irndkerrcode)：  OHOS\_IMAGE\_RESULT\_SUCCESS：操作成功。  IMAGE\_RESULT\_BAD\_PARAMETER：参数错误。  IMAGE\_RESULT\_JNI\_ENV\_ABNORMAL：JNI环境异常。  IMAGE\_RESULT\_INVALID\_PARAMETER：参数无效。 |

### OH\_ImageSource\_CreateFromData()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ImageSource_CreateFromData(napi_env env, uint8_t* data, size_t dataSize,struct OhosImageSourceOps* ops, napi_value *res)
```

**描述**

通过给定的图像源缓冲区资源data和[OhosImageSourceOps](capi-image-ohosimagesourceops.md)结构体，获取JavaScript native层API ImageSource对象。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| napi\_env env | 表明JNI环境的指针。 |
| uint8\_t\* data | 表明图像源缓冲区资源，接受格式化包缓冲区或者base64缓冲区。 |
| size\_t dataSize | 表明图像源缓冲区资源大小。 |
| struct [OhosImageSourceOps](capi-image-ohosimagesourceops.md)\* ops | 表明创建一个图像源的选项。 |
| napi\_value \*res | 表明JavaScript native层API ImageSource对象的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 参考[IRNdkErrCode](capi-image-mdk-common-h.md#irndkerrcode)：  OHOS\_IMAGE\_RESULT\_SUCCESS：操作成功。  IMAGE\_RESULT\_BAD\_PARAMETER：参数错误。  IMAGE\_RESULT\_JNI\_ENV\_ABNORMAL：JNI环境异常。  IMAGE\_RESULT\_INVALID\_PARAMETER：参数无效。 |

### OH\_ImageSource\_CreateFromRawFile()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ImageSource_CreateFromRawFile(napi_env env, RawFileDescriptor rawFile,struct OhosImageSourceOps* ops, napi_value *res)
```

**描述**

通过给定的资源描述符[RawFileDescriptor](capi-rawfile-rawfiledescriptor.md)和[OhosImageSourceOps](capi-image-ohosimagesourceops.md)结构体，获取JavaScript native层API ImageSource对象。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| napi\_env env | 表明JNI环境的指针。 |
| [RawFileDescriptor](capi-rawfile-rawfiledescriptor.md) rawFile | 表明图像源资源描述符。 |
| struct [OhosImageSourceOps](capi-image-ohosimagesourceops.md)\* ops | 表明创建一个图像源的选项。 |
| napi\_value \*res | 表明JavaScript native层API ImageSource对象的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 参考[IRNdkErrCode](capi-image-mdk-common-h.md#irndkerrcode)：  OHOS\_IMAGE\_RESULT\_SUCCESS：操作成功。  IMAGE\_RESULT\_BAD\_PARAMETER：参数错误。  IMAGE\_RESULT\_JNI\_ENV\_ABNORMAL：JNI环境异常。  IMAGE\_RESULT\_INVALID\_PARAMETER：参数无效。 |

### OH\_ImageSource\_CreateIncremental()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ImageSource_CreateIncremental(napi_env env, struct OhosImageSource* source, struct OhosImageSourceOps* ops, napi_value *res)
```

**描述**

通过给定的信息[OhosImageSource](capi-image-ohosimagesource.md)和[OhosImageSourceOps](capi-image-ohosimagesourceops.md)结构，获取增量类型的JavaScript Native API ImageSource对象，图像数据应通过[OH\_ImageSource\_UpdateData](capi-image-source-mdk-h.md#oh_imagesource_updatedata)更新。

**起始版本：** 10

**废弃版本：** 11

**替代接口：** [OH\_ImageSource\_CreateIncrementalFromData](capi-image-source-mdk-h.md#oh_imagesource_createincrementalfromdata)

**参数：**

| 参数项 | 描述 |
| --- | --- |
| napi\_env env | 表明JNI环境的指针。 |
| struct [OhosImageSource](capi-image-ohosimagesource.md)\* source | 表明创建一个图像源的信息，只接收缓冲区类型。 |
| struct [OhosImageSourceOps](capi-image-ohosimagesourceops.md)\* ops | 表明创建一个图像源的选项。 |
| napi\_value \*res | 表明JavaScript native层API ImageSource对象的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 参考[IRNdkErrCode](capi-image-mdk-common-h.md#irndkerrcode)：  OHOS\_IMAGE\_RESULT\_SUCCESS：操作成功。  IMAGE\_RESULT\_BAD\_PARAMETER：参数错误。  IMAGE\_RESULT\_JNI\_ENV\_ABNORMAL：JNI环境异常。  IMAGE\_RESULT\_INVALID\_PARAMETER：参数无效。 |

### OH\_ImageSource\_CreateIncrementalFromData()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ImageSource_CreateIncrementalFromData(napi_env env, uint8_t* data, size_t dataSize,struct OhosImageSourceOps* ops, napi_value *res)
```

**描述**

通过给定的图像源缓冲区资源data和[OhosImageSourceOps](capi-image-ohosimagesourceops.md)结构体，获取增量类型的JavaScript Native API ImageSource对象，图像数据应通过[OH\_ImageSource\_UpdateData](capi-image-source-mdk-h.md#oh_imagesource_updatedata)更新。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| napi\_env env | 表明JNI环境的指针。 |
| uint8\_t\* data | 表明图像源缓冲区资源，接受格式化包缓冲区或者base64缓冲区。 |
| size\_t dataSize | 表明图像源缓冲区资源大小。 |
| struct [OhosImageSourceOps](capi-image-ohosimagesourceops.md)\* ops | 表明创建一个图像源的选项。 |
| napi\_value \*res | 表明JavaScript native层API ImageSource对象的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 参考[IRNdkErrCode](capi-image-mdk-common-h.md#irndkerrcode)：  OHOS\_IMAGE\_RESULT\_SUCCESS：操作成功。  IMAGE\_RESULT\_BAD\_PARAMETER：参数错误。  IMAGE\_RESULT\_JNI\_ENV\_ABNORMAL：JNI环境异常。  IMAGE\_RESULT\_INVALID\_PARAMETER：参数无效。 |

### OH\_ImageSource\_GetSupportedFormats()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ImageSource_GetSupportedFormats(struct OhosImageSourceSupportedFormatList* res)
```

**描述**

获取所有支持的解码格式元标记。

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| struct OhosImageSourceSupportedFormatList\* res | 表明指向[OhosImageSourceSupportedFormatList](capi-image-ohosimagesourcesupportedformatlist.md)结构体的指针。该结构体包含supportedFormatList和size两个属性。  该接口需要调用两次才能正确获取支持的格式列表。  第一次调用需将res->supportedFormatList置空，res->size会获取支持的格式数量。  第二次调用前，需完成内存初始化，首先将res->supportedFormatList初始化为包含res->size个[OhosImageSourceSupportedFormat](capi-image-ohosimagesourcesupportedformat.md)的列表，再为每个[OhosImageSourceSupportedFormat](capi-image-ohosimagesourcesupportedformat.md)申请内存，确保其format属性有足够的空间获取图片格式信息。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 参考[IRNdkErrCode](capi-image-mdk-common-h.md#irndkerrcode)：  OHOS\_IMAGE\_RESULT\_SUCCESS：操作成功。  IMAGE\_RESULT\_BAD\_PARAMETER：参数错误。  IMAGE\_RESULT\_JNI\_ENV\_ABNORMAL：JNI环境异常。  IMAGE\_RESULT\_INVALID\_PARAMETER：参数无效。  IMAGE\_RESULT\_DECODE\_FAILED：解码失败。  IMAGE\_RESULT\_CHECK\_FORMAT\_ERROR：检查格式不对。 |

### OH\_ImageSource\_InitNative()

PhonePC/2in1TabletTVWearable

```
1. ImageSourceNative* OH_ImageSource_InitNative(napi_env env, napi_value source)
```

**描述**

从输入JavaScript native层ImageSource对象中，转换成[ImageSourceNative](capi-image-imagesourcenative-.md)值。

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| napi\_env env | 表明JNI环境的指针。 |
| napi\_value source | 表明JavaScript native层API ImageSource对象的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ImageSourceNative](capi-image-imagesourcenative-.md)\* | 如果操作成功返回[ImageSourceNative](capi-image-imagesourcenative-.md)指针；如果操作失败，返回空指针。 |

**参考：**

[OH\_ImageSource\_Release](capi-image-source-mdk-h.md#oh_imagesource_release)

### OH\_ImageSource\_CreatePixelMap()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ImageSource_CreatePixelMap(const ImageSourceNative* native,struct OhosImageDecodingOps* ops, napi_value *res)
```

**描述**

通过一个给定的选项[OhosImageDecodingOps](capi-image-ohosimagedecodingops.md)结构体，从ImageSource中解码JavaScript native层PixelMap对象。

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [ImageSourceNative](capi-image-imagesourcenative-.md)\* native | 表明native层ImageSourceNative值的指针。 |
| struct [OhosImageDecodingOps](capi-image-ohosimagedecodingops.md)\* ops | 表明为了解码图像源的选项。 |
| napi\_value \*res | 表明JavaScript native层PixelMap对象的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 参考[IRNdkErrCode](capi-image-mdk-common-h.md#irndkerrcode)：  OHOS\_IMAGE\_RESULT\_SUCCESS：操作成功。  IMAGE\_RESULT\_BAD\_PARAMETER：参数错误。  IMAGE\_RESULT\_JNI\_ENV\_ABNORMAL：JNI环境异常。  IMAGE\_RESULT\_INVALID\_PARAMETER：参数无效。  IMAGE\_RESULT\_GET\_DATA\_ABNORMAL：获取图片数据异常。  IMAGE\_RESULT\_DECODE\_FAILED：解码失败。  IMAGE\_RESULT\_DECODE\_HEAD\_ABNORMAL：图像解码头错误。  IMAGE\_RESULT\_CREATE\_DECODER\_FAILED：创建解码器失败。  IMAGE\_RESULT\_CREATE\_ENCODER\_FAILED：创建编码器失败。  IMAGE\_RESULT\_CHECK\_FORMAT\_ERROR：检查格式不对。  IMAGE\_RESULT\_THIRDPART\_SKIA\_ERROR：skia错误。  IMAGE\_RESULT\_DATA\_ABNORMAL：输入图片数据错误。  IMAGE\_RESULT\_ERR\_SHAMEM\_NOT\_EXIST：共享内存错误。  IMAGE\_RESULT\_ERR\_SHAMEM\_DATA\_ABNORMAL：共享内存数据异常。  IMAGE\_RESULT\_DECODE\_ABNORMAL：图片解码异常。  IMAGE\_RESULT\_MALLOC\_ABNORMAL：图像错误。  IMAGE\_RESULT\_DATA\_UNSUPPORT：图片初始化错误。  IMAGE\_RESULT\_INIT\_ABNORMAL：图片输入数据错误。  IMAGE\_RESULT\_CROP：裁剪错误。  IMAGE\_RESULT\_UNKNOWN\_FORMAT：图片格式未知。  IMAGE\_RESULT\_PLUGIN\_REGISTER\_FAILED：注册插件失败。  IMAGE\_RESULT\_PLUGIN\_CREATE\_FAILED：创建插件失败。  IMAGE\_RESULT\_ENCODE\_FAILED：增加位图失败。  IMAGE\_RESULT\_HW\_DECODE\_UNSUPPORT：不支持图片硬解码。  IMAGE\_RESULT\_HW\_DECODE\_FAILED：硬解码失败。  IMAGE\_RESULT\_ERR\_IPC：ipc失败。  IMAGE\_RESULT\_INDEX\_INVALID：索引无效。  IMAGE\_RESULT\_ALPHA\_TYPE\_ERROR：硬解码失败。  IMAGE\_RESULT\_ALLOCATER\_TYPE\_ERROR：硬解码失败。 |

### OH\_ImageSource\_CreatePixelMapList()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ImageSource_CreatePixelMapList(const ImageSourceNative* native,struct OhosImageDecodingOps* ops, napi_value *res)
```

**描述**

通过一个给定的选项[OhosImageDecodingOps](capi-image-ohosimagedecodingops.md)结构体，从ImageSource中解码所有的JavaScript native层PixelMap对象列表。

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [ImageSourceNative](capi-image-imagesourcenative-.md)\* native | 表明native层ImageSourceNative值的指针。 |
| struct [OhosImageDecodingOps](capi-image-ohosimagedecodingops.md)\* ops | 表明为了解码图像源的选项。 |
| napi\_value \*res | 表明JavaScript native层PixelMap列表对象的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 参考[IRNdkErrCode](capi-image-mdk-common-h.md#irndkerrcode)：  OHOS\_IMAGE\_RESULT\_SUCCESS：操作成功。  IMAGE\_RESULT\_BAD\_PARAMETER：参数错误。  IMAGE\_RESULT\_JNI\_ENV\_ABNORMAL：JNI环境异常。  IMAGE\_RESULT\_INVALID\_PARAMETER：参数无效。  IMAGE\_RESULT\_GET\_DATA\_ABNORMAL：获取图片数据异常。  IMAGE\_RESULT\_DECODE\_FAILED：解码失败。  IMAGE\_RESULT\_DECODE\_HEAD\_ABNORMAL：图像解码头错误。  IMAGE\_RESULT\_CREATE\_DECODER\_FAILED：创建解码器失败。  IMAGE\_RESULT\_CREATE\_ENCODER\_FAILED：创建编码器失败。  IMAGE\_RESULT\_CHECK\_FORMAT\_ERROR：检查格式不对。  IMAGE\_RESULT\_THIRDPART\_SKIA\_ERROR：skia错误。  IMAGE\_RESULT\_DATA\_ABNORMAL：输入图片数据错误。  IMAGE\_RESULT\_ERR\_SHAMEM\_NOT\_EXIST：共享内存错误。  IMAGE\_RESULT\_ERR\_SHAMEM\_DATA\_ABNORMAL：共享内存数据异常。  IMAGE\_RESULT\_DECODE\_ABNORMAL：图片解码异常。  IMAGE\_RESULT\_MALLOC\_ABNORMAL：图像错误。  IMAGE\_RESULT\_DATA\_UNSUPPORT：图片初始化错误。  IMAGE\_RESULT\_INIT\_ABNORMAL：图片输入数据错误。  IMAGE\_RESULT\_CROP：裁剪错误。  IMAGE\_RESULT\_UNKNOWN\_FORMAT：图片格式未知。  IMAGE\_RESULT\_PLUGIN\_REGISTER\_FAILED：注册插件失败。  IMAGE\_RESULT\_PLUGIN\_CREATE\_FAILED：创建插件失败。  IMAGE\_RESULT\_ENCODE\_FAILED：增加位图失败。  IMAGE\_RESULT\_HW\_DECODE\_UNSUPPORT：不支持图片硬解码。  IMAGE\_RESULT\_HW\_DECODE\_FAILED：硬解码失败。  IMAGE\_RESULT\_ERR\_IPC：ipc失败。  IMAGE\_RESULT\_INDEX\_INVALID：索引无效。  IMAGE\_RESULT\_ALPHA\_TYPE\_ERROR：硬解码失败。  IMAGE\_RESULT\_ALLOCATER\_TYPE\_ERROR：硬解码失败。  IMAGE\_RESULT\_DECODE\_EXIF\_UNSUPPORT：解码的EXIF不支持。  IMAGE\_RESULT\_PROPERTY\_NOT\_EXIST：图片属性不存在。 |

### OH\_ImageSource\_GetDelayTime()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ImageSource_GetDelayTime(const ImageSourceNative* native,struct OhosImageSourceDelayTimeList* res)
```

**描述**

从ImageSource（如GIF图像源）获取延迟时间列表。

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [ImageSourceNative](capi-image-imagesourcenative-.md)\* native | 表明native层ImageSourceNative值的指针。 |
| struct [OhosImageSourceDelayTimeList](capi-image-ohosimagesourcedelaytimelist.md)\* res | 表明延迟时间列表OhosImageSourceDelayTimeList的指针。  当输入的res中delayTimeList是空指针并且size是0时，将通过res的size中返回延迟时间列表大小为了获取延迟时间，需要比返回的delayTimeList大小值大的足够空间。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 参考[IRNdkErrCode](capi-image-mdk-common-h.md#irndkerrcode)：  OHOS\_IMAGE\_RESULT\_SUCCESS：操作成功。  IMAGE\_RESULT\_BAD\_PARAMETER：参数错误。  IMAGE\_RESULT\_JNI\_ENV\_ABNORMAL：JNI环境异常。  IMAGE\_RESULT\_INVALID\_PARAMETER：参数无效。  IMAGE\_RESULT\_GET\_DATA\_ABNORMAL：获取图片数据异常。  IMAGE\_RESULT\_DECODE\_FAILED：解码失败。  IMAGE\_RESULT\_DECODE\_HEAD\_ABNORMAL：图像解码头错误。  IMAGE\_RESULT\_CREATE\_DECODER\_FAILED：创建解码器失败。  IMAGE\_RESULT\_THIRDPART\_SKIA\_ERROR：skia错误。  IMAGE\_RESULT\_DATA\_ABNORMAL：输入图片数据错误。  IMAGE\_RESULT\_DECODE\_ABNORMAL：图片解码异常。  IMAGE\_RESULT\_DATA\_UNSUPPORT：图片初始化错误。  IMAGE\_RESULT\_UNKNOWN\_FORMAT：图片格式未知。  IMAGE\_RESULT\_PLUGIN\_REGISTER\_FAILED：注册插件失败。  IMAGE\_RESULT\_PLUGIN\_CREATE\_FAILED：创建插件失败。  IMAGE\_RESULT\_INDEX\_INVALID：索引无效。  IMAGE\_RESULT\_DECODE\_EXIF\_UNSUPPORT：解码的EXIF不支持。  IMAGE\_RESULT\_PROPERTY\_NOT\_EXIST：图片属性不存在。 |

### OH\_ImageSource\_GetFrameCount()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ImageSource_GetFrameCount(const ImageSourceNative* native, uint32_t *res)
```

**描述**

从ImageSource中获取帧计数。

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [ImageSourceNative](capi-image-imagesourcenative-.md)\* native | 表明native层ImageSourceNative值的指针。 |
| uint32\_t \*res | 表明帧计数的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 参考[IRNdkErrCode](capi-image-mdk-common-h.md#irndkerrcode)：  OHOS\_IMAGE\_RESULT\_SUCCESS：操作成功。  IMAGE\_RESULT\_BAD\_PARAMETER：参数错误。  IMAGE\_RESULT\_JNI\_ENV\_ABNORMAL：JNI环境异常。  IMAGE\_RESULT\_INVALID\_PARAMETER：参数无效。  IMAGE\_RESULT\_GET\_DATA\_ABNORMAL：获取图片数据异常。  IMAGE\_RESULT\_DECODE\_FAILED：解码失败。  IMAGE\_RESULT\_DECODE\_HEAD\_ABNORMAL：图像解码头错误。  IMAGE\_RESULT\_CREATE\_DECODER\_FAILED：创建解码器失败。  IMAGE\_RESULT\_THIRDPART\_SKIA\_ERROR：skia错误。  IMAGE\_RESULT\_DATA\_ABNORMAL：输入图片数据错误。  IMAGE\_RESULT\_DECODE\_ABNORMAL：图片解码异常。  IMAGE\_RESULT\_DATA\_UNSUPPORT：图片初始化错误。  IMAGE\_RESULT\_UNKNOWN\_FORMAT：图片格式未知。  IMAGE\_RESULT\_PLUGIN\_REGISTER\_FAILED：注册插件失败。  IMAGE\_RESULT\_PLUGIN\_CREATE\_FAILED：创建插件失败。  IMAGE\_RESULT\_INDEX\_INVALID：索引无效。  IMAGE\_RESULT\_DECODE\_EXIF\_UNSUPPORT：解码的EXIF不支持。  IMAGE\_RESULT\_PROPERTY\_NOT\_EXIST：图片属性不存在。 |

### OH\_ImageSource\_GetImageInfo()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ImageSource_GetImageInfo(const ImageSourceNative* native, int32_t index,struct OhosImageSourceInfo* info)
```

**描述**

通过索引从ImageSource获取图像源信息。

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [ImageSourceNative](capi-image-imagesourcenative-.md)\* native | 表明native层ImageSourceNative值的指针。 |
| int32\_t index | 表明帧计数的指针。 |
| struct [OhosImageSourceInfo](capi-image-ohosimagesourceinfo.md)\* info | 表明图像源信息OhosImageSourceInfo的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 参考[IRNdkErrCode](capi-image-mdk-common-h.md#irndkerrcode)：  OHOS\_IMAGE\_RESULT\_SUCCESS：操作成功。  IMAGE\_RESULT\_BAD\_PARAMETER：参数错误。  IMAGE\_RESULT\_JNI\_ENV\_ABNORMAL：JNI环境异常。  IMAGE\_RESULT\_INVALID\_PARAMETER：参数无效。  IMAGE\_RESULT\_GET\_DATA\_ABNORMAL：获取图片数据异常。  IMAGE\_RESULT\_DECODE\_FAILED：解码失败。  IMAGE\_RESULT\_DECODE\_HEAD\_ABNORMAL：图像解码头错误。  IMAGE\_RESULT\_CREATE\_DECODER\_FAILED：创建解码器失败。  IMAGE\_RESULT\_THIRDPART\_SKIA\_ERROR：skia错误。  IMAGE\_RESULT\_DATA\_ABNORMAL：输入图片数据错误。  IMAGE\_RESULT\_DECODE\_ABNORMAL：图片解码异常。  IMAGE\_RESULT\_DATA\_UNSUPPORT：图片初始化错误。  IMAGE\_RESULT\_UNKNOWN\_FORMAT：图片格式未知。  IMAGE\_RESULT\_PLUGIN\_REGISTER\_FAILED：注册插件失败。  IMAGE\_RESULT\_PLUGIN\_CREATE\_FAILED：创建插件失败。  IMAGE\_RESULT\_INDEX\_INVALID：索引无效。  IMAGE\_RESULT\_DECODE\_EXIF\_UNSUPPORT：解码的EXIF不支持。  IMAGE\_RESULT\_PROPERTY\_NOT\_EXIST：图片属性不存在。 |

### OH\_ImageSource\_GetImageProperty()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ImageSource_GetImageProperty(const ImageSourceNative* native, struct OhosImageSourceProperty* key, struct OhosImageSourceProperty* value)
```

**描述**

通过关键字从ImageSource中获取图像源属性。

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [ImageSourceNative](capi-image-imagesourcenative-.md)\* native | 表明native层ImageSourceNative值的指针。 |
| struct [OhosImageSourceProperty](capi-image-ohosimagesourceproperty.md)\* key | 表明属性关键字OhosImageSourceProperty的指针。 |
| struct [OhosImageSourceProperty](capi-image-ohosimagesourceproperty.md)\* value | 表明作为结果的属性值OhosImageSourceProperty的指针。当输入的value中value是空指针并且size是0时，将通过value中的size返回属性值的大小。为了获取属性值，需要比value中的结果大小大的足够的空间。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 参考[IRNdkErrCode](capi-image-mdk-common-h.md#irndkerrcode)：  OHOS\_IMAGE\_RESULT\_SUCCESS：操作成功。  IMAGE\_RESULT\_BAD\_PARAMETER：参数错误。  IMAGE\_RESULT\_JNI\_ENV\_ABNORMAL：JNI环境异常。  IMAGE\_RESULT\_INVALID\_PARAMETER：参数无效。  IMAGE\_RESULT\_GET\_DATA\_ABNORMAL：获取图片数据异常。  IMAGE\_RESULT\_DECODE\_FAILED：解码失败。  IMAGE\_RESULT\_DECODE\_HEAD\_ABNORMAL：图像解码头错误。  IMAGE\_RESULT\_CREATE\_DECODER\_FAILED：创建解码器失败。  IMAGE\_RESULT\_THIRDPART\_SKIA\_ERROR：skia错误。  IMAGE\_RESULT\_DATA\_ABNORMAL：输入图片数据错误。  IMAGE\_RESULT\_DECODE\_ABNORMAL：图片解码异常。  IMAGE\_RESULT\_DATA\_UNSUPPORT：图片初始化错误。  IMAGE\_RESULT\_UNKNOWN\_FORMAT：图片格式未知。  IMAGE\_RESULT\_PLUGIN\_REGISTER\_FAILED：注册插件失败。  IMAGE\_RESULT\_PLUGIN\_CREATE\_FAILED：创建插件失败。  IMAGE\_RESULT\_INDEX\_INVALID：索引无效。  IMAGE\_RESULT\_DECODE\_EXIF\_UNSUPPORT：解码的EXIF不支持。  IMAGE\_RESULT\_PROPERTY\_NOT\_EXIST：图片属性不存在。 |

### OH\_ImageSource\_ModifyImageProperty()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ImageSource_ModifyImageProperty(const ImageSourceNative* native, struct OhosImageSourceProperty* key, struct OhosImageSourceProperty* value)
```

**描述**

通过关键字为ImageSource修改图像源属性。

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [ImageSourceNative](capi-image-imagesourcenative-.md)\* native | 表明native层ImageSourceNative值的指针。 |
| struct [OhosImageSourceProperty](capi-image-ohosimagesourceproperty.md)\* key | 表明属性关键字OhosImageSourceProperty的指针。 |
| struct [OhosImageSourceProperty](capi-image-ohosimagesourceproperty.md)\* value | 为了修改表明属性值OhosImageSourceProperty的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 参考[IRNdkErrCode](capi-image-mdk-common-h.md#irndkerrcode)：  OHOS\_IMAGE\_RESULT\_SUCCESS：操作成功。  IMAGE\_RESULT\_BAD\_PARAMETER：参数错误。  IMAGE\_RESULT\_JNI\_ENV\_ABNORMAL：JNI环境异常。  IMAGE\_RESULT\_INVALID\_PARAMETER：参数无效。  IMAGE\_RESULT\_GET\_DATA\_ABNORMAL：获取图片数据异常。  IMAGE\_RESULT\_DECODE\_FAILED：解码失败。  IMAGE\_RESULT\_DECODE\_HEAD\_ABNORMAL：图像解码头错误。  IMAGE\_RESULT\_CREATE\_DECODER\_FAILED：创建解码器失败。  IMAGE\_RESULT\_THIRDPART\_SKIA\_ERROR：skia错误。  IMAGE\_RESULT\_DATA\_ABNORMAL：输入图片数据错误。  IMAGE\_RESULT\_DECODE\_ABNORMAL：图片解码异常。  IMAGE\_RESULT\_DATA\_UNSUPPORT：图片初始化错误。  IMAGE\_RESULT\_UNKNOWN\_FORMAT：图片格式未知。  IMAGE\_RESULT\_PLUGIN\_REGISTER\_FAILED：注册插件失败。  IMAGE\_RESULT\_PLUGIN\_CREATE\_FAILED：创建插件失败。  IMAGE\_RESULT\_INDEX\_INVALID：索引无效。  IMAGE\_RESULT\_DECODE\_EXIF\_UNSUPPORT：解码的EXIF不支持。  IMAGE\_RESULT\_PROPERTY\_NOT\_EXIST：图片属性不存在。 |

### OH\_ImageSource\_UpdateData()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ImageSource_UpdateData(const ImageSourceNative* native, struct OhosImageSourceUpdateData* data)
```

**描述**

为了增量类型的ImageSource更新源数据。

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [ImageSourceNative](capi-image-imagesourcenative-.md)\* native | 表明native层ImageSourceNative值的指针。 |
| struct [OhosImageSourceUpdateData](capi-image-ohosimagesourceupdatedata.md)\* data | 表明更新数据信息OhosImageSourceUpdateData的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 参考[IRNdkErrCode](capi-image-mdk-common-h.md#irndkerrcode)：  OHOS\_IMAGE\_RESULT\_SUCCESS：操作成功。  IMAGE\_RESULT\_BAD\_PARAMETER：参数错误。  IMAGE\_RESULT\_JNI\_ENV\_ABNORMAL：JNI环境异常。  IMAGE\_RESULT\_INVALID\_PARAMETER：参数无效。  IMAGE\_RESULT\_GET\_DATA\_ABNORMAL：获取图片数据异常。  IMAGE\_RESULT\_DECODE\_FAILED：解码失败。  IMAGE\_RESULT\_DECODE\_HEAD\_ABNORMAL：图像解码头错误。  IMAGE\_RESULT\_CREATE\_DECODER\_FAILED：创建解码器失败。  IMAGE\_RESULT\_CREATE\_ENCODER\_FAILED：创建编码器失败。  IMAGE\_RESULT\_CHECK\_FORMAT\_ERROR：检查格式不对。  IMAGE\_RESULT\_THIRDPART\_SKIA\_ERROR：Skia第三方库出错。  IMAGE\_RESULT\_DATA\_ABNORMAL：输入图片数据错误。  IMAGE\_RESULT\_ERR\_SHAMEM\_NOT\_EXIST：共享内存不存在。  IMAGE\_RESULT\_ERR\_SHAMEM\_DATA\_ABNORMAL：共享内存数据异常。  IMAGE\_RESULT\_DECODE\_ABNORMAL：图片解码异常。  IMAGE\_RESULT\_MALLOC\_ABNORMAL：图像内存分配异常。  IMAGE\_RESULT\_DATA\_UNSUPPORT：图片初始化错误。  IMAGE\_RESULT\_INIT\_ABNORMAL：图片输入数据错误。  IMAGE\_RESULT\_CROP：裁剪失败。  IMAGE\_RESULT\_UNKNOWN\_FORMAT：图片格式未知。  IMAGE\_RESULT\_PLUGIN\_REGISTER\_FAILED：注册插件失败。  IMAGE\_RESULT\_PLUGIN\_CREATE\_FAILED：创建插件失败。  IMAGE\_RESULT\_ENCODE\_FAILED：增加位图失败。  IMAGE\_RESULT\_HW\_DECODE\_UNSUPPORT：不支持图片硬解码。  IMAGE\_RESULT\_HW\_DECODE\_FAILED：硬解码失败。  IMAGE\_RESULT\_ERR\_IPC：IPC操作失败。  IMAGE\_RESULT\_INDEX\_INVALID：索引无效。  IMAGE\_RESULT\_ALPHA\_TYPE\_ERROR：Alpha类型错误。  IMAGE\_RESULT\_ALLOCATER\_TYPE\_ERROR：内存分配器类型错误。 |

### OH\_ImageSource\_Release()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ImageSource_Release(ImageSourceNative* native)
```

**描述**

释放native层图像源ImageSourceNative。

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ImageSourceNative](capi-image-imagesourcenative-.md)\* native | 表明native层ImageSourceNative值的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 参考[IRNdkErrCode](capi-image-mdk-common-h.md#irndkerrcode)：  OHOS\_IMAGE\_RESULT\_SUCCESS：操作成功。  IMAGE\_RESULT\_BAD\_PARAMETER：参数错误。  IMAGE\_RESULT\_JNI\_ENV\_ABNORMAL：JNI 环境异常。  IMAGE\_RESULT\_INVALID\_PARAMETER：参数无效。  IMAGE\_RESULT\_GET\_DATA\_ABNORMAL：获取图片数据异常。  IMAGE\_RESULT\_DATA\_ABNORMAL：输入图片数据错误。 |

**参考：**

[OH\_ImageSource\_Create](capi-image-source-mdk-h.md#oh_imagesource_create), [OH\_ImageSource\_CreateIncremental](capi-image-source-mdk-h.md#oh_imagesource_createincremental)
