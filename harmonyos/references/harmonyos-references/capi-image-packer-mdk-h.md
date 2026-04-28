---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-packer-mdk-h
title: image_packer_mdk.h
breadcrumb: API参考 > 媒体 > Image Kit（图片处理服务） > C API > 头文件 > image_packer_mdk.h
category: harmonyos-references
scraped_at: 2026-04-28T08:13:19+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:a8539ef744affbe8d6b6a31bf63c38bd62f83a8d80bc5b2783968367e255f261
---

## 概述

PhonePC/2in1TabletTVWearable

声明用于将图像编码到缓冲区或文件的api。可用于将像素数据编码到目标缓冲区或文件中。

编码过程如下：

通过OH\_ImagePacker\_Create方法创建编码器对象。

然后通过OH\_ImagePacker\_InitNative将编码器对象转换为编码器原生对象。

接下来用OH\_ImagePacker\_PackToData或者OH\_ImagePacker\_PackToFile将源以特定的编码选项编码进目标区域。

最后通过OH\_ImagePacker\_Release释放编码器对象。

**引用文件：** <multimedia/image\_framework/image\_packer\_mdk.h>

**库：** libimage\_packer\_ndk.z.so

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 11

**相关模块：** [Image](capi-image.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 结构体

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [ImagePacker\_Opts\_](capi-image-imagepacker-opts-.md) | ImagePacker\_Opts | 定义图像编码选项信息。 |
| [ImagePacker\_Native\_](capi-image-imagepacker-native-.md) | ImagePacker\_Native | 为编码器方法定义native层编码器对象。 |

### 函数

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [int32\_t OH\_ImagePacker\_Create(napi\_env env, napi\_value \*res)](capi-image-packer-mdk-h.md#oh_imagepacker_create) | 获取JavaScript native层ImagePacker对象。 |
| [ImagePacker\_Native\* OH\_ImagePacker\_InitNative(napi\_env env, napi\_value packer)](capi-image-packer-mdk-h.md#oh_imagepacker_initnative) | 从输入JavaScript native层ImagePacker对象中，转换成ImagePacker\_Native值。 |
| [int32\_t OH\_ImagePacker\_PackToData(ImagePacker\_Native\* native, napi\_value source,ImagePacker\_Opts\* opts, uint8\_t\* outData, size\_t\* size)](capi-image-packer-mdk-h.md#oh_imagepacker_packtodata) | 通过一个给定的选项ImagePacker\_Opts结构体，将输入JavaScript native层PixelMap对象或者ImageSource对象编码并输出到指定的缓存区outData中。 |
| [int32\_t OH\_ImagePacker\_PackToFile(ImagePacker\_Native\* native, napi\_value source, ImagePacker\_Opts\* opts, int fd)](capi-image-packer-mdk-h.md#oh_imagepacker_packtofile) | 通过一个给定的选项ImagePacker\_Opts结构体，将输入JavaScript native层PixelMap对象或者ImageSource对象编码并输出到指定的文件中。 |
| [int32\_t OH\_ImagePacker\_Release(ImagePacker\_Native\* native)](capi-image-packer-mdk-h.md#oh_imagepacker_release) | 释放native层编码器对象[ImagePacker\_Native](capi-image-imagepacker-native-.md)。  此API不用于释放JavaScript原生API ImagePacker对象，它用于释放native层对象ImagePacker\_Native。 |

## 函数说明

PhonePC/2in1TabletTVWearable

### OH\_ImagePacker\_Create()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ImagePacker_Create(napi_env env, napi_value *res)
```

**描述**

获取JavaScript native层ImagePacker对象。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| napi\_env env | 表明JNI环境的指针。 |
| napi\_value \*res | 表明JavaScript native层ImagePacker对象的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | [IRNdkErrCode](capi-image-mdk-common-h.md#irndkerrcode)：  IMAGE\_RESULT\_SUCCESS：执行成功。  IMAGE\_RESULT\_INVALID\_PARAMETER：参数无效。 |

### OH\_ImagePacker\_InitNative()

PhonePC/2in1TabletTVWearable

```
1. ImagePacker_Native* OH_ImagePacker_InitNative(napi_env env, napi_value packer)
```

**描述**

从输入JavaScript native层ImagePacker对象中，转换成ImagePacker\_Native值。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| napi\_env env | 表明JNI环境的指针。 |
| napi\_value packer | 表明JavaScript native层ImagePacker对象。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ImagePacker\_Native](capi-image-imagepacker-native-.md)\* | 如果操作成功则返回ImagePacker\_Native指针，否则返回空指针。 |

**参考：**

[OH\_ImagePacker\_Release](capi-image-packer-mdk-h.md#oh_imagepacker_release)

### OH\_ImagePacker\_PackToData()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ImagePacker_PackToData(ImagePacker_Native* native, napi_value source,ImagePacker_Opts* opts, uint8_t* outData, size_t* size)
```

**描述**

通过一个给定的选项ImagePacker\_Opts结构体，将输入JavaScript native层PixelMap对象或者ImageSource对象编码并输出到指定的缓存区outData中。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ImagePacker\_Native](capi-image-imagepacker-native-.md)\* native | 表明指向native层ImagePacker的指针。 |
| napi\_value source | 表明待编码JavaScript native层PixelMap对象或者ImageSource对象。 |
| [ImagePacker\_Opts](capi-image-imagepacker-opts-.md)\* opts | 表明位图编码的选项。 |
| uint8\_t\* outData | 输出的指定缓存区。 |
| size\_t\* size | 输出的指定缓存区大小。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | [IRNdkErrCode](capi-image-mdk-common-h.md#irndkerrcode)：  IMAGE\_RESULT\_SUCCESS：执行成功。  IMAGE\_RESULT\_INVALID\_PARAMETER：参数无效。  ERR\_IMAGE\_DATA\_ABNORMAL：输出缓冲区异常。  ERR\_IMAGE\_MISMATCHED\_FORMAT：格式不匹配。  ERR\_IMAGE\_MALLOC\_ABNORMAL：malloc内部缓冲区错误。  ERR\_IMAGE\_DECODE\_ABNORMAL：init编解码器内部错误。  ERR\_IMAGE\_ENCODE\_FAILED：编码器在编码过程中出现错误。 |

**参考：**

[OH\_ImagePacker\_PackToFile](capi-image-packer-mdk-h.md#oh_imagepacker_packtofile)

### OH\_ImagePacker\_PackToFile()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ImagePacker_PackToFile(ImagePacker_Native* native, napi_value source,ImagePacker_Opts* opts, int fd)
```

**描述**

通过一个给定的选项ImagePacker\_Opts结构体，将输入JavaScript native层PixelMap对象或者ImageSource对象编码并输出到指定的文件中。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ImagePacker\_Native](capi-image-imagepacker-native-.md)\* native | 表明指向native层ImagePacker的指针。 |
| napi\_value source | 表明待编码JavaScript native层PixelMap对象或者ImageSource对象。 |
| [ImagePacker\_Opts](capi-image-imagepacker-opts-.md)\* opts | 表明位图编码的选项。 |
| int fd | 输出的指定文件描述符。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | [IRNdkErrCode](capi-image-mdk-common-h.md#irndkerrcode)：  IMAGE\_RESULT\_SUCCESS：执行成功。  IMAGE\_RESULT\_INVALID\_PARAMETER：参数无效。  ERR\_IMAGE\_DATA\_ABNORMAL：输出缓冲区异常。  ERR\_IMAGE\_MISMATCHED\_FORMAT：格式不匹配。  ERR\_IMAGE\_MALLOC\_ABNORMAL：malloc内部缓冲区错误。  ERR\_IMAGE\_DECODE\_ABNORMAL：init编解码器内部错误。  ERR\_IMAGE\_ENCODE\_FAILED：编码器在编码过程中出现错误。 |

**参考：**

[OH\_ImagePacker\_PackToData](capi-image-packer-mdk-h.md#oh_imagepacker_packtodata)

### OH\_ImagePacker\_Release()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ImagePacker_Release(ImagePacker_Native* native)
```

**描述**

释放native层编码器对象[ImagePacker\_Native](capi-image-imagepacker-native-.md)。

此API不用于释放JavaScript原生API ImagePacker对象，它用于释放native层对象ImagePacker\_Native。

通过调用[OH\_ImagePacker\_InitNative](capi-image-packer-mdk-h.md#oh_imagepacker_initnative)解析。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ImagePacker\_Native](capi-image-imagepacker-native-.md)\* native | 表明native层ImagePacker\_Native值的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | [IRNdkErrCode](capi-image-mdk-common-h.md#irndkerrcode)：  IMAGE\_RESULT\_SUCCESS：执行成功。 |

**参考：**

[OH\_ImagePacker\_InitNative](capi-image-packer-mdk-h.md#oh_imagepacker_initnative)
