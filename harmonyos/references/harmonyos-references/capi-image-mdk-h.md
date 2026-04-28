---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-mdk-h
title: image_mdk.h
breadcrumb: API参考 > 媒体 > Image Kit（图片处理服务） > C API > 头文件 > image_mdk.h
category: harmonyos-references
scraped_at: 2026-04-28T08:13:19+08:00
doc_updated_at: 2026-03-19
content_hash: sha256:a9f81ebd45ae552d740ec583d34170f7b848988bce9b96a2a9aff7861f69b6cc
---

## 概述

PhonePC/2in1TabletTVWearable

声明访问图像矩形、大小、格式和组件数据的函数。

**引用文件：** <multimedia/image\_framework/image\_mdk.h>

**库：** libimage\_ndk.z.so

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 10

**相关模块：** [Image](capi-image.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 结构体

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [OhosImageRect](capi-image-ohosimagerect.md) | - | 定义图像矩形信息。 |
| [ImageNative\_](capi-image-imagenative-.md) | ImageNative | 为图像接口定义native层图像对象。 |
| [OhosImageComponent](capi-image-ohosimagecomponent.md) | - | 定义图像组成信息。 |

### 枚举

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [图像格式](capi-image-mdk-h.md#图像格式) | 图像格式枚举值。 |
| [图像颜色通道类型](capi-image-mdk-h.md#图像颜色通道类型) | 图像颜色通道类型枚举值。 |

### 函数

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [ImageNative\* OH\_Image\_InitImageNative(napi\_env env, napi\_value source)](capi-image-mdk-h.md#oh_image_initimagenative) | 从输入的JavaScript Native API图像对象中解析native ImageNative对象。 |
| [int32\_t OH\_Image\_ClipRect(const ImageNative\* native, struct OhosImageRect\* rect)](capi-image-mdk-h.md#oh_image_cliprect) | 获取native ImageNative对象OhosImageRect信息。 |
| [int32\_t OH\_Image\_Size(const ImageNative\* native, struct OhosImageSize\* size)](capi-image-mdk-h.md#oh_image_size) | 获取native ImageNative对象的OhosImageSize信息。 |
| [int32\_t OH\_Image\_Format(const ImageNative\* native, int32\_t\* format)](capi-image-mdk-h.md#oh_image_format) | 获取native ImageNative对象的图像格式。 |
| [int32\_t OH\_Image\_GetComponent(const ImageNative\* native, int32\_t componentType, struct OhosImageComponent\* componentNative)](capi-image-mdk-h.md#oh_image_getcomponent) | 从native ImageNative对象中获取OhosImageComponent。 |
| [int32\_t OH\_Image\_Release(ImageNative\* native)](capi-image-mdk-h.md#oh_image_release) | 释放ImageNative native对象。  这个方法无法释放JavaScript Native API Image对象，而是释放被[OH\_Image\_InitImageNative](capi-image-mdk-h.md#oh_image_initimagenative)解析的ImageNative native对象。 |

## 枚举类型说明

PhonePC/2in1TabletTVWearable

### 图像格式

PhonePC/2in1TabletTVWearable

```
1. enum anonymous enum
```

**描述**

图像格式枚举值。

**起始版本：** 10

| 枚举项 | 描述 |
| --- | --- |
| OHOS\_IMAGE\_FORMAT\_YCBCR\_422\_SP = 1000 | YCBCR422 semi-planar格式。 |
| OHOS\_IMAGE\_FORMAT\_JPEG = 2000 | JPEG编码格式。 |

### 图像颜色通道类型

PhonePC/2in1TabletTVWearable

```
1. enum anonymous enum
```

**描述**

图像颜色通道类型枚举值。

**起始版本：** 10

| 枚举项 | 描述 |
| --- | --- |
| OHOS\_IMAGE\_COMPONENT\_FORMAT\_YUV\_Y = 1 | 亮度信息。 |
| OHOS\_IMAGE\_COMPONENT\_FORMAT\_YUV\_U = 2 | 色度信息。 |
| OHOS\_IMAGE\_COMPONENT\_FORMAT\_YUV\_V = 3 | 色差值信息。 |
| OHOS\_IMAGE\_COMPONENT\_FORMAT\_JPEG = 4 | JPEG格式。 |

## 函数说明

PhonePC/2in1TabletTVWearable

### OH\_Image\_InitImageNative()

PhonePC/2in1TabletTVWearable

```
1. ImageNative* OH_Image_InitImageNative(napi_env env, napi_value source)
```

**描述**

从输入的JavaScript Native API图像对象中解析native ImageNative对象。

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| napi\_env env | 表示指向JNI环境的指针。 |
| napi\_value source | 表示JavaScript Native API图像对象。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ImageNative](capi-image-imagenative-.md)\* | 如果操作成功返回ImageNative指针对象，如果操作失败返回空指针。 |

**参考：**

[OH\_Image\_Release](capi-image-mdk-h.md#oh_image_release)

### OH\_Image\_ClipRect()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_Image_ClipRect(const ImageNative* native, struct OhosImageRect* rect)
```

**描述**

获取native ImageNative对象OhosImageRect信息。

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [ImageNative](capi-image-imagenative-.md)\* native | 表示指向ImageNative native层对象的指针。 |
| struct [OhosImageRect](capi-image-ohosimagerect.md)\* rect | 表示作为转换结果的OhosImageRect对象指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | [IRNdkErrCode](capi-image-mdk-common-h.md#irndkerrcode)：  IMAGE\_RESULT\_SUCCESS：操作成功。  IMAGE\_RESULT\_JNI\_ENV\_ABNORMAL：JNI环境异常。  IMAGE\_RESULT\_INVALID\_PARAMETER：参数无效。  IMAGE\_RESULT\_SURFACE\_GET\_PARAMETER\_FAILED：从surface获取参数失败。  IMAGE\_RESULT\_BAD\_PARAMETER：参数错误。 |

### OH\_Image\_Size()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_Image_Size(const ImageNative* native, struct OhosImageSize* size)
```

**描述**

获取native ImageNative对象的OhosImageSize信息。

如果ImageNative对象所存储的是相机预览流数据，即YUV图像数据，那么获取到的OhosImageSize中的宽高分别对应YUV图像的宽高；如果ImageNative对象所存储的是相机拍照流数据，即JPEG图像，由于已经是编码后的数据，OhosImageSize中的宽等于JPEG数据大小，高等于1。

ImageNative对象所存储的数据是预览流还是拍照流，取决于应用将receiver中的surfaceId传给相机的previewOutput还是captureOutput。相机预览与拍照最佳实践请参考[预览流二次处理(C/C++)](../harmonyos-guides/native-camera-preview-imagereceiver.md)与[拍照(C/C++)](../harmonyos-guides/native-camera-shooting.md)。

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [ImageNative](capi-image-imagenative-.md)\* native | 表示ImageNative native对象的指针。 |
| struct [OhosImageSize](capi-image-ohosimagesize.md)\* size | 表示作为转换结果的OhosImageSize对象的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | [IRNdkErrCode](capi-image-mdk-common-h.md#irndkerrcode)：  IMAGE\_RESULT\_SUCCESS：操作成功。  IMAGE\_RESULT\_JNI\_ENV\_ABNORMAL：JNI环境异常。  IMAGE\_RESULT\_INVALID\_PARAMETER：参数无效。  IMAGE\_RESULT\_SURFACE\_GET\_PARAMETER\_FAILED：从surface获取参数失败。  IMAGE\_RESULT\_BAD\_PARAMETER：参数错误。 |

### OH\_Image\_Format()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_Image_Format(const ImageNative* native, int32_t* format)
```

**描述**

获取native ImageNative对象的图像格式。

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [ImageNative](capi-image-imagenative-.md)\* native | 表示ImageNative native对象的指针。 |
| int32\_t\* format | 表示作为转换结果的图像格式对象的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | [IRNdkErrCode](capi-image-mdk-common-h.md#irndkerrcode)：  IMAGE\_RESULT\_SUCCESS：操作成功。  IMAGE\_RESULT\_JNI\_ENV\_ABNORMAL：JNI环境异常。  IMAGE\_RESULT\_INVALID\_PARAMETER：参数无效。  IMAGE\_RESULT\_SURFACE\_GET\_PARAMETER\_FAILED：从surface获取参数失败。  IMAGE\_RESULT\_BAD\_PARAMETER：参数错误。 |

### OH\_Image\_GetComponent()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_Image_GetComponent(const ImageNative* native, int32_t componentType, struct OhosImageComponent* componentNative)
```

**描述**

从native ImageNative对象中获取OhosImageComponent。

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [ImageNative](capi-image-imagenative-.md)\* native | 表示ImageNative native对象的指针。 |
| int32\_t componentType | 表示所需组件的组件类型。 |
| struct [OhosImageComponent](capi-image-ohosimagecomponent.md)\* componentNative | 表示转换结果的OhosImageComponent对象的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | [IRNdkErrCode](capi-image-mdk-common-h.md#irndkerrcode)：  IMAGE\_RESULT\_SUCCESS：操作成功。  IMAGE\_RESULT\_JNI\_ENV\_ABNORMAL：JNI环境异常。  IMAGE\_RESULT\_INVALID\_PARAMETER：参数无效。  IMAGE\_RESULT\_SURFACE\_GET\_PARAMETER\_FAILED：从surface获取参数失败。  IMAGE\_RESULT\_BAD\_PARAMETER：参数错误。 |

### OH\_Image\_Release()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_Image_Release(ImageNative* native)
```

**描述**

释放ImageNative native对象。

这个方法无法释放JavaScript Native API Image对象，而是释放被[OH\_Image\_InitImageNative](capi-image-mdk-h.md#oh_image_initimagenative)解析的ImageNative native对象。

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ImageNative](capi-image-imagenative-.md)\* native | 表示ImageNative native对象的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | [IRNdkErrCode](capi-image-mdk-common-h.md#irndkerrcode)：  IMAGE\_RESULT\_SUCCESS：操作成功。  IMAGE\_RESULT\_JNI\_ENV\_ABNORMAL：JNI环境异常。  IMAGE\_RESULT\_INVALID\_PARAMETER：参数无效。  IMAGE\_RESULT\_BAD\_PARAMETER：参数错误。 |

**参考：**

[OH\_Image\_InitImageNative](capi-image-mdk-h.md#oh_image_initimagenative)
