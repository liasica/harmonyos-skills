---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-pixel-map-napi-h
title: image_pixel_map_napi.h
breadcrumb: API参考 > 媒体 > Image Kit（图片处理服务） > C API > 头文件 > image_pixel_map_napi.h
category: harmonyos-references
scraped_at: 2026-04-28T08:13:19+08:00
doc_updated_at: 2026-03-19
content_hash: sha256:8fb51fde20cab447b3093357e710867adb05fa5ba75217de4cc3828224682591
---

## 概述

PhonePC/2in1TabletTVWearable

声明可以锁定并访问pixelmap数据的方法，声明解锁的方法。

**库：** libpixelmap\_ndk.z.so

**系统能力：** SystemCapability.Multimedia.Image.Core

**引用文件：** <multimedia/image\_framework/image\_pixel\_map\_napi.h>

**起始版本：** 8

**相关模块：** [Image](capi-image.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 结构体

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [OhosPixelMapInfo](capi-image-ohospixelmapinfo.md) | - | 用于定义PixelMap的相关信息。 |

### 枚举

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [方法返回的错误码](capi-image-pixel-map-napi-h.md#方法返回的错误码) | 函数方法返回值的错误码的枚举。 |
| [像素格式](capi-image-pixel-map-napi-h.md#像素格式) | 像素格式的枚举。 |
| [anonymous enum](capi-image-pixel-map-napi-h.md#pixelmap缩放类型) | PixelMap缩放类型的枚举。 |

### 函数

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [int32\_t OH\_GetImageInfo(napi\_env env, napi\_value value, OhosPixelMapInfo \*info)](capi-image-pixel-map-napi-h.md#oh_getimageinfo) | 获取PixelMap的信息，并记录信息到[OhosPixelMapInfo](capi-image-ohospixelmapinfo.md)结构体中。 |
| [int32\_t OH\_AccessPixels(napi\_env env, napi\_value value, void\*\* addrPtr)](capi-image-pixel-map-napi-h.md#oh_accesspixels) | 获取PixelMap对象数据的内存地址，并锁定该内存。  函数执行成功后，\*addrPtr就是获取的待访问的内存地址。访问操作完成后，必须要使用[OH\_UnAccessPixels](capi-image-pixel-map-napi-h.md#oh_unaccesspixels)来释放锁，否则的话资源无法被释放。待解锁后，内存地址就不可以再被访问和操作。 |
| [int32\_t OH\_UnAccessPixels(napi\_env env, napi\_value value)](capi-image-pixel-map-napi-h.md#oh_unaccesspixels) | 释放PixelMap对象数据的内存锁，用于匹配方法[OH\_AccessPixels](capi-image-pixel-map-napi-h.md#oh_accesspixels)。 |

## 枚举类型说明

PhonePC/2in1TabletTVWearable

### 方法返回的错误码

PhonePC/2in1TabletTVWearable

```
1. enum anonymous enum
```

**描述**

函数方法返回值的错误码的枚举。

**起始版本：** 8

**废弃版本：** 10

| 枚举项 | 描述 |
| --- | --- |
| OHOS\_IMAGE\_RESULT\_SUCCESS = 0 | 成功的结果。 |
| OHOS\_IMAGE\_RESULT\_BAD\_PARAMETER = -1 | 无效值。 |

### 像素格式

PhonePC/2in1TabletTVWearable

```
1. enum anonymous enum
```

**描述**

像素格式的枚举。

**起始版本：** 8

**废弃版本：** 10

| 枚举项 | 描述 |
| --- | --- |
| OHOS\_PIXEL\_MAP\_FORMAT\_NONE = 0 | 未知的格式。 |
| OHOS\_PIXEL\_MAP\_FORMAT\_RGBA\_8888 = 3 | RGBA\_8888格式。 |
| OHOS\_PIXEL\_MAP\_FORMAT\_RGB\_565 = 2 | RGB\_565格式。 |

### PixelMap缩放类型

PhonePC/2in1TabletTVWearable

```
1. enum anonymous enum
```

**描述**

PixelMap缩放类型的枚举。

**起始版本：** 10

| 枚举项 | 描述 |
| --- | --- |
| OHOS\_PIXEL\_MAP\_SCALE\_MODE\_FIT\_TARGET\_SIZE = 0 | 适应目标图片大小的格式。 |
| OHOS\_PIXEL\_MAP\_SCALE\_MODE\_CENTER\_CROP = 1 | 以中心进行缩放的格式。 |

## 函数说明

PhonePC/2in1TabletTVWearable

### OH\_GetImageInfo()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_GetImageInfo(napi_env env, napi_value value, OhosPixelMapInfo *info)
```

**描述**

获取PixelMap的信息，并记录信息到[OhosPixelMapInfo](capi-image-ohospixelmapinfo.md)结构体中。

**起始版本：** 8

**废弃版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| napi\_env env | napi的环境指针。 |
| napi\_value value | 应用层的PixelMap对象。 |
| [OhosPixelMapInfo](capi-image-ohospixelmapinfo.md) \*info | 用于保存信息的指针对象。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | [错误码](capi-image-pixel-map-napi-h.md#方法返回的错误码)：  OHOS\_IMAGE\_RESULT\_SUCCESS：操作成功。  OHOS\_IMAGE\_RESULT\_BAD\_PARAMETER：操作失败。 |

### OH\_AccessPixels()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_AccessPixels(napi_env env, napi_value value, void** addrPtr)
```

**描述**

获取PixelMap对象数据的内存地址，并锁定该内存。

函数执行成功后，\*addrPtr就是获取的待访问的内存地址。访问操作完成后，必须要使用[OH\_UnAccessPixels](capi-image-pixel-map-napi-h.md#oh_unaccesspixels)来释放锁，否则的话资源无法被释放。待解锁后，内存地址就不可以再被访问和操作。

**起始版本：** 8

**废弃版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| napi\_env env | napi的环境指针。 |
| napi\_value value | 应用层的PixelMap对象。 |
| void\*\* addrPtr | 用于指向的内存地址的双指针对象。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | [错误码](capi-image-pixel-map-napi-h.md#方法返回的错误码)：  OHOS\_IMAGE\_RESULT\_SUCCESS：操作成功。  OHOS\_IMAGE\_RESULT\_BAD\_PARAMETER：操作失败。 |

### OH\_UnAccessPixels()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_UnAccessPixels(napi_env env, napi_value value)
```

**描述**

释放PixelMap对象数据的内存锁，用于匹配方法[OH\_AccessPixels](capi-image-pixel-map-napi-h.md#oh_accesspixels)。

**起始版本：** 8

**废弃版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| napi\_env env | napi的环境指针。 |
| napi\_value value | 应用层的PixelMap对象。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | [错误码](capi-image-pixel-map-napi-h.md#方法返回的错误码)：  OHOS\_IMAGE\_RESULT\_SUCCESS：操作成功。  OHOS\_IMAGE\_RESULT\_BAD\_PARAMETER：操作失败。 |
