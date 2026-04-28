---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-pixel-map-mdk-h
title: image_pixel_map_mdk.h
breadcrumb: API参考 > 媒体 > Image Kit（图片处理服务） > C API > 头文件 > image_pixel_map_mdk.h
category: harmonyos-references
scraped_at: 2026-04-28T08:13:20+08:00
doc_updated_at: 2026-04-10
content_hash: sha256:b37a2773a496a3275ff8dede7417c5cec8fee45d177b6bf7b0a9507dfcc920e3
---

## 概述

PhonePC/2in1TabletTVWearable

声明可以锁定并访问pixelmap数据的方法，声明解锁的方法。推荐使用[pixelmap\_native.h](capi-pixelmap-native-h.md)。

**引用文件：** <multimedia/image\_framework/image\_pixel\_map\_mdk.h>

**库：** libpixelmap\_ndk.z.so

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 10

**相关模块：** [Image](capi-image.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 结构体

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [OhosPixelMapInfos](capi-image-ohospixelmapinfos.md) | OhosPixelMapInfos | 用于定义PixelMap的相关信息。 |
| [NativePixelMap\_](capi-image-nativepixelmap-.md) | NativePixelMap | 定义native层像素位图信息。表示native层PixelMap数据类型名称。 |
| [OhosPixelMapCreateOps](capi-image-ohospixelmapcreateops.md) | - | 用于定义创建PixelMap设置选项的相关信息。 |

### 枚举

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [anonymous enum](capi-image-pixel-map-mdk-h.md#pixelmap透明度类型) | - | PixelMap透明度类型的枚举。 |
| [anonymous enum](capi-image-pixel-map-mdk-h.md#pixelmap编辑类型) | - | PixelMap编辑类型的枚举。 |
| [OH\_PixelMap\_AntiAliasingLevel](capi-image-pixel-map-mdk-h.md#oh_pixelmap_antialiasinglevel) | OH\_PixelMap\_AntiAliasingLevel | Pixelmap缩放时采用的缩放算法。 |

### 函数

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [int32\_t OH\_PixelMap\_CreatePixelMap(napi\_env env, OhosPixelMapCreateOps info, void\* buf, size\_t len, napi\_value\* res)](capi-image-pixel-map-mdk-h.md#oh_pixelmap_createpixelmap) | 创建PixelMap对象。当前只支持输入流为BGRA格式的流。  该接口传入的buf不支持stride。  该接口不支持DMA内存。 |
| [int32\_t OH\_PixelMap\_CreatePixelMapWithStride(napi\_env env, OhosPixelMapCreateOps info, void\* buf, size\_t len, int32\_t rowStride, napi\_value\* res)](capi-image-pixel-map-mdk-h.md#oh_pixelmap_createpixelmapwithstride) | 创建PixelMap对象。  当前只支持输入流为BGRA格式的流。pixelmap内存在RGBA格式下，默认为DMA内存（图片512\*512以上）。 |
| [int32\_t OH\_PixelMap\_CreateAlphaPixelMap(napi\_env env, napi\_value source, napi\_value\* alpha)](capi-image-pixel-map-mdk-h.md#oh_pixelmap_createalphapixelmap) | 根据Alpha通道的信息，来生成一个仅包含Alpha通道信息的PixelMap对象。 |
| [NativePixelMap\* OH\_PixelMap\_InitNativePixelMap(napi\_env env, napi\_value source)](capi-image-pixel-map-mdk-h.md#oh_pixelmap_initnativepixelmap) | 初始化NativePixelMap对象。 |
| [int32\_t OH\_PixelMap\_GetBytesNumberPerRow(const NativePixelMap\* native, int32\_t\* num)](capi-image-pixel-map-mdk-h.md#oh_pixelmap_getbytesnumberperrow) | 获取PixelMap对象每行字节数。 |
| [int32\_t OH\_PixelMap\_GetIsEditable(const NativePixelMap\* native, int32\_t\* editable)](capi-image-pixel-map-mdk-h.md#oh_pixelmap_getiseditable) | 获取PixelMap对象是否可编辑的状态。 |
| [int32\_t OH\_PixelMap\_IsSupportAlpha(const NativePixelMap\* native, int32\_t\* alpha)](capi-image-pixel-map-mdk-h.md#oh_pixelmap_issupportalpha) | 获取PixelMap对象是否支持Alpha通道。 |
| [int32\_t OH\_PixelMap\_SetAlphaAble(const NativePixelMap\* native, int32\_t alpha)](capi-image-pixel-map-mdk-h.md#oh_pixelmap_setalphaable) | 设置PixelMap对象的Alpha通道。 |
| [int32\_t OH\_PixelMap\_GetDensity(const NativePixelMap\* native, int32\_t\* density)](capi-image-pixel-map-mdk-h.md#oh_pixelmap_getdensity) | 获取PixelMap对象像素密度。 |
| [int32\_t OH\_PixelMap\_SetDensity(const NativePixelMap\* native, int32\_t density)](capi-image-pixel-map-mdk-h.md#oh_pixelmap_setdensity) | 设置PixelMap对象像素密度。 |
| [int32\_t OH\_PixelMap\_SetOpacity(const NativePixelMap\* native, float opacity)](capi-image-pixel-map-mdk-h.md#oh_pixelmap_setopacity) | 设置PixelMap对象的透明度。 |
| [int32\_t OH\_PixelMap\_Scale(const NativePixelMap\* native, float x, float y)](capi-image-pixel-map-mdk-h.md#oh_pixelmap_scale) | 设置PixelMap对象的缩放。  从API version 12开始，推荐使用新接口[OH\_PixelmapNative\_Scale](capi-pixelmap-native-h.md#oh_pixelmapnative_scale)。 |
| [int32\_t OH\_PixelMap\_ScaleWithAntiAliasing(const NativePixelMap\* native, float x, float y, OH\_PixelMap\_AntiAliasingLevel level)](capi-image-pixel-map-mdk-h.md#oh_pixelmap_scalewithantialiasing) | 根据指定的缩放算法和输入的宽高对图片进行缩放。  从API version 12开始，推荐使用新接口[OH\_PixelmapNative\_ScaleWithAntiAliasing](capi-pixelmap-native-h.md#oh_pixelmapnative_scalewithantialiasing)。 |
| [int32\_t OH\_PixelMap\_Translate(const NativePixelMap\* native, float x, float y)](capi-image-pixel-map-mdk-h.md#oh_pixelmap_translate) | 设置PixelMap对象的偏移。  从API version 12开始，推荐使用新接口[OH\_PixelmapNative\_Translate](capi-pixelmap-native-h.md#oh_pixelmapnative_translate)。 |
| [int32\_t OH\_PixelMap\_Rotate(const NativePixelMap\* native, float angle)](capi-image-pixel-map-mdk-h.md#oh_pixelmap_rotate) | 设置PixelMap对象的旋转。  从API version 12开始，推荐使用新接口[OH\_PixelmapNative\_Rotate](capi-pixelmap-native-h.md#oh_pixelmapnative_rotate)。 |
| [int32\_t OH\_PixelMap\_Flip(const NativePixelMap\* native, int32\_t x, int32\_t y)](capi-image-pixel-map-mdk-h.md#oh_pixelmap_flip) | 设置PixelMap对象的翻转。  从API version 12开始，推荐使用新接口[OH\_PixelmapNative\_Flip](capi-pixelmap-native-h.md#oh_pixelmapnative_flip)。 |
| [int32\_t OH\_PixelMap\_Crop(const NativePixelMap\* native, int32\_t x, int32\_t y, int32\_t width, int32\_t height)](capi-image-pixel-map-mdk-h.md#oh_pixelmap_crop) | 设置PixelMap对象的裁剪。  从API version 12开始，推荐使用新接口[OH\_PixelmapNative\_Crop](capi-pixelmap-native-h.md#oh_pixelmapnative_crop)。 |
| [int32\_t OH\_PixelMap\_GetImageInfo(const NativePixelMap\* native, OhosPixelMapInfos \*info)](capi-image-pixel-map-mdk-h.md#oh_pixelmap_getimageinfo) | 获取PixelMap对象图像信息。  从API version 12开始，推荐使用新接口[OH\_PixelmapNative\_GetImageInfo](capi-pixelmap-native-h.md#oh_pixelmapnative_getimageinfo)。 |
| [int32\_t OH\_PixelMap\_AccessPixels(const NativePixelMap\* native, void\*\* addr)](capi-image-pixel-map-mdk-h.md#oh_pixelmap_accesspixels) | 获取native PixelMap对象数据的内存地址，并锁定该内存。 |
| [int32\_t OH\_PixelMap\_UnAccessPixels(const NativePixelMap\* native)](capi-image-pixel-map-mdk-h.md#oh_pixelmap_unaccesspixels) | 释放native PixelMap对象数据的内存锁，用于匹配方法[OH\_PixelMap\_AccessPixels](capi-image-pixel-map-mdk-h.md#oh_pixelmap_accesspixels)。 |

## 枚举类型说明

PhonePC/2in1TabletTVWearable

### PixelMap透明度类型

PhonePC/2in1TabletTVWearable

```
1. enum anonymous enum
```

**描述**

PixelMap 透明度类型的枚举。

**起始版本：** 10

| 枚举项 | 描述 |
| --- | --- |
| OHOS\_PIXEL\_MAP\_ALPHA\_TYPE\_UNKNOWN = 0 | 未知的格式。 |
| OHOS\_PIXEL\_MAP\_ALPHA\_TYPE\_OPAQUE = 1 | 不透明的格式。 |
| OHOS\_PIXEL\_MAP\_ALPHA\_TYPE\_PREMUL = 2 | 预乘的格式。 |
| OHOS\_PIXEL\_MAP\_ALPHA\_TYPE\_UNPREMUL = 3 | 预除的格式。 |

### PixelMap编辑类型

PhonePC/2in1TabletTVWearable

```
1. enum anonymous enum
```

**描述**

PixelMap编辑类型的枚举。

**起始版本：** 10

| 枚举项 | 描述 |
| --- | --- |
| OHOS\_PIXEL\_MAP\_READ\_ONLY = 0 | 只读的格式。 |
| OHOS\_PIXEL\_MAP\_EDITABLE = 1 | 可编辑的格式。 |

### OH\_PixelMap\_AntiAliasingLevel

PhonePC/2in1TabletTVWearable

```
1. enum OH_PixelMap_AntiAliasingLevel
```

**描述**

Pixelmap缩放时采用的缩放算法。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| OH\_PixelMap\_AntiAliasing\_NONE = 0 | 最近邻插值算法。 |
| OH\_PixelMap\_AntiAliasing\_LOW = 1 | 双线性插值算法。 |
| OH\_PixelMap\_AntiAliasing\_MEDIUM = 2 | 双线性插值算法，同时开启Mipmap。缩小图片时建议使用。 |
| OH\_PixelMap\_AntiAliasing\_HIGH = 3 | 三次插值算法。 |

## 函数说明

PhonePC/2in1TabletTVWearable

### OH\_PixelMap\_CreatePixelMap()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_PixelMap_CreatePixelMap(napi_env env, OhosPixelMapCreateOps info,void* buf, size_t len, napi_value* res)
```

**描述**

创建PixelMap对象。当前只支持输入流为BGRA格式的流。

该接口传入的buf不支持stride。

该接口不支持DMA内存。

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| napi\_env env | napi的环境指针。 |
| [OhosPixelMapCreateOps](capi-image-ohospixelmapcreateops.md) info | PixelMap数据设置项。 |
| void\* buf | 图片的buffer数据。 |
| size\_t len | 图片大小信息。 |
| napi\_value\* res | 应用层的PixelMap对象的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | [IRNdkErrCode](capi-image-mdk-common-h.md#irndkerrcode)：  IMAGE\_RESULT\_SUCCESS：操作成功。  IMAGE\_RESULT\_BAD\_PARAMETER：参数错误。  IMAGE\_RESULT\_JNI\_ENV\_ABNORMAL：JNI环境异常。  IMAGE\_RESULT\_INVALID\_PARAMETER：参数无效。  IMAGE\_RESULT\_GET\_DATA\_ABNORMAL：图像获取数据失败。  IMAGE\_RESULT\_DECODE\_FAILED：解码失败。  IMAGE\_RESULT\_DECODE\_HEAD\_ABNORMAL：图像头解码失败。  IMAGE\_RESULT\_CREATE\_DECODER\_FAILED：创建解码器失败。  IMAGE\_RESULT\_CREATE\_ENCODER\_FAILED：创建编码器失败。  IMAGE\_RESULT\_CHECK\_FORMAT\_ERROR：检查格式失败。  IMAGE\_RESULT\_THIRDPART\_SKIA\_ERROR：skia能力失败。  IMAGE\_RESULT\_DATA\_ABNORMAL：图像输入数据失败。  IMAGE\_RESULT\_ERR\_SHAMEM\_NOT\_EXIST：共享内存失败。  IMAGE\_RESULT\_ERR\_SHAMEM\_DATA\_ABNORMAL：共享内存数据错误。  IMAGE\_RESULT\_DECODE\_ABNORMAL：图像解码失败。  IMAGE\_RESULT\_DECODE\_FAILED：解码失败。  IMAGE\_RESULT\_MALLOC\_ABNORMAL：图像分配内存失败。  IMAGE\_RESULT\_DATA\_UNSUPPORT：图像数据不支持。  IMAGE\_RESULT\_INIT\_ABNORMAL：图像初始化失败。  IMAGE\_RESULT\_CROP：裁剪失败。  IMAGE\_RESULT\_UNKNOWN\_FORMAT：图像格式未知。  IMAGE\_RESULT\_PLUGIN\_REGISTER\_FAILED：注册插件失败。  IMAGE\_RESULT\_PLUGIN\_CREATE\_FAILED：创建插件失败。  IMAGE\_RESULT\_ENCODE\_FAILED：图像添加像素位图失败。  IMAGE\_RESULT\_HW\_DECODE\_UNSUPPORT：图像不支持硬件解码。  IMAGE\_RESULT\_HW\_DECODE\_FAILED：硬件解码失败。  IMAGE\_RESULT\_INDEX\_INVALID：ipc失败。  IMAGE\_RESULT\_DATA\_UNSUPPORT：属性无效。  IMAGE\_RESULT\_ALPHA\_TYPE\_ERROR：透明度类型错误。  IMAGE\_RESULT\_ALLOCATER\_TYPE\_ERROR：内存分配类型错误。 |

### OH\_PixelMap\_CreatePixelMapWithStride()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_PixelMap_CreatePixelMapWithStride(napi_env env, OhosPixelMapCreateOps info,void* buf, size_t len, int32_t rowStride, napi_value* res)
```

**描述**

创建PixelMap对象。

当前只支持输入流为BGRA格式的流。pixelmap内存在RGBA格式下，默认为DMA内存（图片512\*512以上）。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| napi\_env env | napi的环境指针。 |
| [OhosPixelMapCreateOps](capi-image-ohospixelmapcreateops.md) info | PixelMap数据设置项。 |
| void\* buf | 图片的buffer数据。 |
| size\_t len | 图片buffer大小信息。 |
| int32\_t rowStride | 图片跨距信息。跨距，图像每行占用的真实内存大小，单位为字节。跨距 = width \* 单位像素字节数 + padding，padding为每行为内存对齐做的填充区域。 |
| napi\_value\* res | 应用层的PixelMap对象的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | [IRNdkErrCode](capi-image-mdk-common-h.md#irndkerrcode)：  IMAGE\_RESULT\_SUCCESS：操作成功。  IMAGE\_RESULT\_BAD\_PARAMETER：参数错误。  IMAGE\_RESULT\_JNI\_ENV\_ABNORMAL：JNI环境异常。  IMAGE\_RESULT\_GET\_DATA\_ABNORMAL：图像获取数据失败。  IMAGE\_RESULT\_CHECK\_FORMAT\_ERROR：检查格式失败。  IMAGE\_RESULT\_DATA\_ABNORMAL：图像输入数据失败。  IMAGE\_RESULT\_ERR\_SHAMEM\_DATA\_ABNORMAL：共享内存数据错误。  IMAGE\_RESULT\_DATA\_UNSUPPORT：属性无效或图像数据不支持。  IMAGE\_RESULT\_UNKNOWN\_FORMAT：图像格式未知。 |

### OH\_PixelMap\_CreateAlphaPixelMap()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_PixelMap_CreateAlphaPixelMap(napi_env env, napi_value source, napi_value* alpha)
```

**描述**

根据Alpha通道的信息，来生成一个仅包含Alpha通道信息的PixelMap对象。

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| napi\_env env | napi的环境指针。 |
| napi\_value source | 应用层的PixelMap对象。 |
| napi\_value\* alpha | alpha通道的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | [IRNdkErrCode](capi-image-mdk-common-h.md#irndkerrcode)：  IMAGE\_RESULT\_SUCCESS：操作成功。  IMAGE\_RESULT\_BAD\_PARAMETER：参数错误。  IMAGE\_RESULT\_JNI\_ENV\_ABNORMAL：JNI环境异常。  IMAGE\_RESULT\_INVALID\_PARAMETER：参数无效。  IMAGE\_RESULT\_GET\_DATA\_ABNORMAL：图像获取数据失败。  IMAGE\_RESULT\_DECODE\_FAILED：解码失败。  IMAGE\_RESULT\_DECODE\_HEAD\_ABNORMAL：图像头解码失败。  IMAGE\_RESULT\_CREATE\_DECODER\_FAILED：创建解码器失败。  IMAGE\_RESULT\_CREATE\_ENCODER\_FAILED：创建编码器失败。  IMAGE\_RESULT\_CHECK\_FORMAT\_ERROR：检查格式失败。  IMAGE\_RESULT\_THIRDPART\_SKIA\_ERROR：skia能力失败。  IMAGE\_RESULT\_DATA\_ABNORMAL：图像输入数据失败。  IMAGE\_RESULT\_ERR\_SHAMEM\_NOT\_EXIST：共享内存失败。  IMAGE\_RESULT\_ERR\_SHAMEM\_DATA\_ABNORMAL：共享内存数据错误。  IMAGE\_RESULT\_DECODE\_ABNORMAL：图像解码失败。  IMAGE\_RESULT\_MALLOC\_ABNORMAL：图像分配内存失败。  IMAGE\_RESULT\_DATA\_UNSUPPORT：图像数据不支持。  IMAGE\_RESULT\_INIT\_ABNORMAL：图像初始化失败。  IMAGE\_RESULT\_CROP：裁剪失败。  IMAGE\_RESULT\_UNKNOWN\_FORMAT：图像格式未知。  IMAGE\_RESULT\_PLUGIN\_REGISTER\_FAILED：注册插件失败。  IMAGE\_RESULT\_PLUGIN\_CREATE\_FAILED：创建插件失败。  IMAGE\_RESULT\_ENCODE\_FAILED：图像添加像素位图失败。  IMAGE\_RESULT\_HW\_DECODE\_UNSUPPORT：图像不支持硬件解码。  IMAGE\_RESULT\_HW\_DECODE\_FAILED：硬件解码失败。  IMAGE\_RESULT\_INDEX\_INVALID：ipc失败。  IMAGE\_RESULT\_DATA\_UNSUPPORT：属性无效。  IMAGE\_RESULT\_ALPHA\_TYPE\_ERROR：透明度类型错误。  IMAGE\_RESULT\_ALLOCATER\_TYPE\_ERROR：内存分配类型错误。 |

### OH\_PixelMap\_InitNativePixelMap()

PhonePC/2in1TabletTVWearable

```
1. NativePixelMap* OH_PixelMap_InitNativePixelMap(napi_env env, napi_value source)
```

**描述**

初始化NativePixelMap对象。

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| napi\_env env | napi的环境指针。 |
| napi\_value source | 应用层的PixelMap对象。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [NativePixelMap](capi-image-nativepixelmap-.md)\* | 操作成功则返回NativePixelMap的指针；如果操作失败，则返回错误码。 |

### OH\_PixelMap\_GetBytesNumberPerRow()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_PixelMap_GetBytesNumberPerRow(const NativePixelMap* native, int32_t* num)
```

**描述**

获取PixelMap对象每行字节数。

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [NativePixelMap](capi-image-nativepixelmap-.md)\* native | NativePixelMap的指针。 |
| int32\_t\* num | PixelMap对象的每行字节数指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | [IRNdkErrCode](capi-image-mdk-common-h.md#irndkerrcode)：  IMAGE\_RESULT\_SUCCESS：操作成功。  IMAGE\_RESULT\_BAD\_PARAMETER：参数错误。  IMAGE\_RESULT\_JNI\_ENV\_ABNORMAL：JNI环境异常。  IMAGE\_RESULT\_INVALID\_PARAMETER：参数无效。  IMAGE\_RESULT\_DATA\_ABNORMAL：图像输入数据失败。  IMAGE\_RESULT\_DATA\_UNSUPPORT：属性无效。 |

### OH\_PixelMap\_GetIsEditable()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_PixelMap_GetIsEditable(const NativePixelMap* native, int32_t* editable)
```

**描述**

获取PixelMap对象是否可编辑的状态。

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [NativePixelMap](capi-image-nativepixelmap-.md)\* native | NativePixelMap的指针。 |
| int32\_t\* editable | PixelMap对象是否可编辑的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | [IRNdkErrCode](capi-image-mdk-common-h.md#irndkerrcode)：  IMAGE\_RESULT\_SUCCESS：操作成功。  IMAGE\_RESULT\_BAD\_PARAMETER：参数错误。  IMAGE\_RESULT\_JNI\_ENV\_ABNORMAL：JNI环境异常。  IMAGE\_RESULT\_INVALID\_PARAMETER：参数无效。  IMAGE\_RESULT\_DATA\_ABNORMAL：图像输入数据失败。  IMAGE\_RESULT\_DATA\_UNSUPPORT：属性无效。 |

### OH\_PixelMap\_IsSupportAlpha()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_PixelMap_IsSupportAlpha(const NativePixelMap* native, int32_t* alpha)
```

**描述**

获取PixelMap对象是否支持Alpha通道。

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [NativePixelMap](capi-image-nativepixelmap-.md)\* native | NativePixelMap的指针。 |
| int32\_t\* alpha | 是否支持Alpha的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | [IRNdkErrCode](capi-image-mdk-common-h.md#irndkerrcode)：  IMAGE\_RESULT\_SUCCESS：操作成功。  IMAGE\_RESULT\_BAD\_PARAMETER：参数错误。  IMAGE\_RESULT\_JNI\_ENV\_ABNORMAL：JNI环境异常。  IMAGE\_RESULT\_INVALID\_PARAMETER：参数无效。  IMAGE\_RESULT\_DATA\_ABNORMAL：图像输入数据失败。  IMAGE\_RESULT\_DATA\_UNSUPPORT：属性无效。 |

### OH\_PixelMap\_SetAlphaAble()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_PixelMap_SetAlphaAble(const NativePixelMap* native, int32_t alpha)
```

**描述**

设置PixelMap对象的Alpha通道。

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [NativePixelMap](capi-image-nativepixelmap-.md)\* native | NativePixelMap的指针。 |
| int32\_t alpha | Alpha通道。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | [IRNdkErrCode](capi-image-mdk-common-h.md#irndkerrcode)：  IMAGE\_RESULT\_SUCCESS：操作成功。  IMAGE\_RESULT\_BAD\_PARAMETER：参数错误。  IMAGE\_RESULT\_JNI\_ENV\_ABNORMAL：JNI环境异常。  IMAGE\_RESULT\_INVALID\_PARAMETER：参数无效。  IMAGE\_RESULT\_DATA\_ABNORMAL：图像输入数据失败。  IMAGE\_RESULT\_DATA\_UNSUPPORT：属性无效。 |

### OH\_PixelMap\_GetDensity()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_PixelMap_GetDensity(const NativePixelMap* native, int32_t* density)
```

**描述**

获取PixelMap对象像素密度。

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [NativePixelMap](capi-image-nativepixelmap-.md)\* native | NativePixelMap的指针。 |
| int32\_t\* density | 像素密度指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | [IRNdkErrCode](capi-image-mdk-common-h.md#irndkerrcode)：  IMAGE\_RESULT\_SUCCESS：操作成功。  IMAGE\_RESULT\_BAD\_PARAMETER：参数错误。  IMAGE\_RESULT\_JNI\_ENV\_ABNORMAL：JNI环境异常。  IMAGE\_RESULT\_INVALID\_PARAMETER：参数无效。  IMAGE\_RESULT\_DATA\_ABNORMAL：图像输入数据失败。  IMAGE\_RESULT\_DATA\_UNSUPPORT：属性无效。 |

### OH\_PixelMap\_SetDensity()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_PixelMap_SetDensity(const NativePixelMap* native, int32_t density)
```

**描述**

设置PixelMap对象像素密度。

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [NativePixelMap](capi-image-nativepixelmap-.md)\* native | NativePixelMap的指针。 |
| int32\_t density | 像素密度。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | [IRNdkErrCode](capi-image-mdk-common-h.md#irndkerrcode)：  IMAGE\_RESULT\_SUCCESS：操作成功。  IMAGE\_RESULT\_BAD\_PARAMETER：参数错误。  IMAGE\_RESULT\_JNI\_ENV\_ABNORMAL：JNI环境异常。  IMAGE\_RESULT\_INVALID\_PARAMETER：参数无效。  IMAGE\_RESULT\_DATA\_ABNORMAL：图像输入数据失败。  IMAGE\_RESULT\_DATA\_UNSUPPORT：属性无效。 |

### OH\_PixelMap\_SetOpacity()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_PixelMap_SetOpacity(const NativePixelMap* native, float opacity)
```

**描述**

设置PixelMap对象的透明度。

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [NativePixelMap](capi-image-nativepixelmap-.md)\* native | NativePixelMap的指针。 |
| float opacity | 透明度。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | [IRNdkErrCode](capi-image-mdk-common-h.md#irndkerrcode)：  IMAGE\_RESULT\_SUCCESS：操作成功。  IMAGE\_RESULT\_BAD\_PARAMETER：参数错误。  IMAGE\_RESULT\_JNI\_ENV\_ABNORMAL：JNI环境异常。  IMAGE\_RESULT\_INVALID\_PARAMETER：参数无效。  IMAGE\_RESULT\_DATA\_ABNORMAL：图像输入数据失败。  IMAGE\_RESULT\_DATA\_UNSUPPORT：属性无效。 |

### OH\_PixelMap\_Scale()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_PixelMap_Scale(const NativePixelMap* native, float x, float y)
```

**描述**

设置PixelMap对象的缩放。

从API version 12开始，推荐使用新接口[OH\_PixelmapNative\_Scale](capi-pixelmap-native-h.md#oh_pixelmapnative_scale)。

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [NativePixelMap](capi-image-nativepixelmap-.md)\* native | NativePixelMap的指针。 |
| float x | 宽度的缩放比例。 |
| float y | 高度的缩放比例。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | [IRNdkErrCode](capi-image-mdk-common-h.md#irndkerrcode)：  IMAGE\_RESULT\_SUCCESS：操作成功。  IMAGE\_RESULT\_BAD\_PARAMETER：参数错误。  IMAGE\_RESULT\_JNI\_ENV\_ABNORMAL：JNI环境异常。  IMAGE\_RESULT\_INVALID\_PARAMETER：参数无效。  IMAGE\_RESULT\_GET\_DATA\_ABNORMAL：图像获取数据失败。  IMAGE\_RESULT\_DECODE\_FAILED：解码失败。  IMAGE\_RESULT\_CHECK\_FORMAT\_ERROR：检查格式失败。  IMAGE\_RESULT\_THIRDPART\_SKIA\_ERROR：skia能力失败。  IMAGE\_RESULT\_DATA\_ABNORMAL：图像输入数据失败。  IMAGE\_RESULT\_ERR\_SHAMEM\_NOT\_EXIST：共享内存失败。  IMAGE\_RESULT\_ERR\_SHAMEM\_DATA\_ABNORMAL：共享内存数据错误。  IMAGE\_RESULT\_MALLOC\_ABNORMAL：图像分配内存失败。  IMAGE\_RESULT\_DATA\_UNSUPPORT：图像数据不支持。  IMAGE\_RESULT\_INIT\_ABNORMAL：图像初始化失败。  IMAGE\_RESULT\_CROP：裁剪失败。  IMAGE\_RESULT\_UNKNOWN\_FORMAT：图像格式未知。  IMAGE\_RESULT\_PLUGIN\_REGISTER\_FAILED：注册插件失败。  IMAGE\_RESULT\_PLUGIN\_CREATE\_FAILED：创建插件失败。  IMAGE\_RESULT\_DATA\_UNSUPPORT：属性无效。  IMAGE\_RESULT\_ALPHA\_TYPE\_ERROR：透明度类型错误。  IMAGE\_RESULT\_ALLOCATER\_TYPE\_ERROR：内存分配类型错误。 |

### OH\_PixelMap\_ScaleWithAntiAliasing()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_PixelMap_ScaleWithAntiAliasing(const NativePixelMap* native, float x, float y,OH_PixelMap_AntiAliasingLevel level)
```

**描述**

根据指定的缩放算法和输入的宽高对图片进行缩放。

从API version 12开始，推荐使用新接口[OH\_PixelmapNative\_ScaleWithAntiAliasing](capi-pixelmap-native-h.md#oh_pixelmapnative_scalewithantialiasing)。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [NativePixelMap](capi-image-nativepixelmap-.md)\* native | NativePixelMap的指针。 |
| float x | 宽度的缩放比例。 |
| float y | 高度的缩放比例。 |
| [OH\_PixelMap\_AntiAliasingLevel](capi-image-pixel-map-mdk-h.md#oh_pixelmap_antialiasinglevel) level | 缩放算法。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | [IRNdkErrCode](capi-image-mdk-common-h.md#irndkerrcode)：  IMAGE\_RESULT\_SUCCESS：操作成功。  IMAGE\_RESULT\_JNI\_ENV\_ABNORMAL：JNI环境异常。  IMAGE\_RESULT\_INVALID\_PARAMETER：参数无效。  IMAGE\_RESULT\_GET\_DATA\_ABNORMAL：图像获取数据失败。  IMAGE\_RESULT\_CHECK\_FORMAT\_ERROR：检查格式失败。  IMAGE\_RESULT\_THIRDPART\_SKIA\_ERROR：skia能力失败。  IMAGE\_RESULT\_ERR\_SHAMEM\_DATA\_ABNORMAL：共享内存数据错误。  IMAGE\_RESULT\_MALLOC\_ABNORMAL：图像分配内存失败。  IMAGE\_RESULT\_UNKNOWN\_FORMAT：图像格式未知。 |

### OH\_PixelMap\_Translate()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_PixelMap_Translate(const NativePixelMap* native, float x, float y)
```

**描述**

设置PixelMap对象的偏移。

从API version 12开始，推荐使用新接口[OH\_PixelmapNative\_Translate](capi-pixelmap-native-h.md#oh_pixelmapnative_translate)。

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [NativePixelMap](capi-image-nativepixelmap-.md)\* native | NativePixelMap的指针。 |
| float x | 水平偏移量。 |
| float y | 垂直偏移量。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | [IRNdkErrCode](capi-image-mdk-common-h.md#irndkerrcode)：  IMAGE\_RESULT\_SUCCESS：操作成功。  IMAGE\_RESULT\_BAD\_PARAMETER：参数错误。  IMAGE\_RESULT\_JNI\_ENV\_ABNORMAL：JNI环境异常。  IMAGE\_RESULT\_INVALID\_PARAMETER：参数无效。  IMAGE\_RESULT\_GET\_DATA\_ABNORMAL：图像获取数据失败。  IMAGE\_RESULT\_DECODE\_FAILED：解码失败。  IMAGE\_RESULT\_CHECK\_FORMAT\_ERROR：检查格式失败。  IMAGE\_RESULT\_THIRDPART\_SKIA\_ERROR：skia能力失败。  IMAGE\_RESULT\_DATA\_ABNORMAL：图像输入数据失败。  IMAGE\_RESULT\_ERR\_SHAMEM\_NOT\_EXIST：共享内存失败。  IMAGE\_RESULT\_ERR\_SHAMEM\_DATA\_ABNORMAL：共享内存数据错误。  IMAGE\_RESULT\_MALLOC\_ABNORMAL：图像分配内存失败。  IMAGE\_RESULT\_DATA\_UNSUPPORT：图像数据不支持。  IMAGE\_RESULT\_CROP：裁剪失败。  IMAGE\_RESULT\_UNKNOWN\_FORMAT：图像格式未知。  IMAGE\_RESULT\_PLUGIN\_REGISTER\_FAILED：注册插件失败。  IMAGE\_RESULT\_PLUGIN\_CREATE\_FAILED：创建插件失败。  IMAGE\_RESULT\_DATA\_UNSUPPORT：属性无效。  IMAGE\_RESULT\_ALPHA\_TYPE\_ERROR：透明度类型错误。  IMAGE\_RESULT\_ALLOCATER\_TYPE\_ERROR：内存分配类型错误。 |

### OH\_PixelMap\_Rotate()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_PixelMap_Rotate(const NativePixelMap* native, float angle)
```

**描述**

设置PixelMap对象的旋转。

从API version 12开始，推荐使用新接口[OH\_PixelmapNative\_Rotate](capi-pixelmap-native-h.md#oh_pixelmapnative_rotate)。

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [NativePixelMap](capi-image-nativepixelmap-.md)\* native | NativePixelMap的指针。 |
| float angle | 旋转角度。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | [IRNdkErrCode](capi-image-mdk-common-h.md#irndkerrcode)：  IMAGE\_RESULT\_SUCCESS：操作成功。  IMAGE\_RESULT\_BAD\_PARAMETER：参数错误。  IMAGE\_RESULT\_JNI\_ENV\_ABNORMAL：JNI环境异常。  IMAGE\_RESULT\_INVALID\_PARAMETER：参数无效。  IMAGE\_RESULT\_GET\_DATA\_ABNORMAL：图像获取数据失败。  IMAGE\_RESULT\_DECODE\_FAILED：解码失败。  IMAGE\_RESULT\_CHECK\_FORMAT\_ERROR：检查格式失败。  IMAGE\_RESULT\_THIRDPART\_SKIA\_ERROR：skia能力失败。  IMAGE\_RESULT\_DATA\_ABNORMAL：图像输入数据失败。  IMAGE\_RESULT\_ERR\_SHAMEM\_NOT\_EXIST：共享内存失败。  IMAGE\_RESULT\_ERR\_SHAMEM\_DATA\_ABNORMAL：共享内存数据错误。  IMAGE\_RESULT\_MALLOC\_ABNORMAL：图像分配内存失败。  IMAGE\_RESULT\_DATA\_UNSUPPORT：图像数据不支持。  IMAGE\_RESULT\_CROP：裁剪失败。  IMAGE\_RESULT\_UNKNOWN\_FORMAT：图像格式未知。  IMAGE\_RESULT\_PLUGIN\_REGISTER\_FAILED：注册插件失败。  IMAGE\_RESULT\_PLUGIN\_CREATE\_FAILED：创建插件失败。  IMAGE\_RESULT\_DATA\_UNSUPPORT：属性无效。  IMAGE\_RESULT\_ALPHA\_TYPE\_ERROR：透明度类型错误。  IMAGE\_RESULT\_ALLOCATER\_TYPE\_ERROR：内存分配类型错误。 |

### OH\_PixelMap\_Flip()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_PixelMap_Flip(const NativePixelMap* native, int32_t x, int32_t y)
```

**描述**

设置PixelMap对象的翻转。

从API version 12开始，推荐使用新接口[OH\_PixelmapNative\_Flip](capi-pixelmap-native-h.md#oh_pixelmapnative_flip)。

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [NativePixelMap](capi-image-nativepixelmap-.md)\* native | NativePixelMap的指针。 |
| int32\_t x | 根据水平方向x轴进行图片翻转。 |
| int32\_t y | 根据垂直方向y轴进行图片翻转。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | [IRNdkErrCode](capi-image-mdk-common-h.md#irndkerrcode)：  IMAGE\_RESULT\_SUCCESS：操作成功。  IMAGE\_RESULT\_BAD\_PARAMETER：参数错误。  IMAGE\_RESULT\_JNI\_ENV\_ABNORMAL：JNI环境异常。  IMAGE\_RESULT\_INVALID\_PARAMETER：参数无效。  IMAGE\_RESULT\_GET\_DATA\_ABNORMAL：图像获取数据失败。  IMAGE\_RESULT\_DECODE\_FAILED：解码失败。  IMAGE\_RESULT\_CHECK\_FORMAT\_ERROR：检查格式失败。  IMAGE\_RESULT\_THIRDPART\_SKIA\_ERROR：skia能力失败。  IMAGE\_RESULT\_DATA\_ABNORMAL：图像输入数据失败。  IMAGE\_RESULT\_ERR\_SHAMEM\_NOT\_EXIST：共享内存失败。  IMAGE\_RESULT\_ERR\_SHAMEM\_DATA\_ABNORMAL：共享内存数据错误。  IMAGE\_RESULT\_MALLOC\_ABNORMAL：图像分配内存失败。  IMAGE\_RESULT\_DATA\_UNSUPPORT：图像数据不支持。  IMAGE\_RESULT\_CROP：裁剪失败。  IMAGE\_RESULT\_UNKNOWN\_FORMAT：图像格式未知。  IMAGE\_RESULT\_PLUGIN\_REGISTER\_FAILED：注册插件失败。  IMAGE\_RESULT\_PLUGIN\_CREATE\_FAILED：创建插件失败。  IMAGE\_RESULT\_DATA\_UNSUPPORT：属性无效。  IMAGE\_RESULT\_ALPHA\_TYPE\_ERROR：透明度类型错误。  IMAGE\_RESULT\_ALLOCATER\_TYPE\_ERROR：内存分配类型错误。 |

### OH\_PixelMap\_Crop()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_PixelMap_Crop(const NativePixelMap* native, int32_t x, int32_t y, int32_t width, int32_t height)
```

**描述**

设置PixelMap对象的裁剪。

从API version 12开始，推荐使用新接口[OH\_PixelmapNative\_Crop](capi-pixelmap-native-h.md#oh_pixelmapnative_crop)。

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [NativePixelMap](capi-image-nativepixelmap-.md)\* native | NativePixelMap的指针。 |
| int32\_t x | 目标图片左上角的x坐标。 |
| int32\_t y | 目标图片左上角的y坐标。 |
| int32\_t width | 裁剪区域的宽度。 |
| int32\_t height | 裁剪区域的高度。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | [IRNdkErrCode](capi-image-mdk-common-h.md#irndkerrcode)：  IMAGE\_RESULT\_SUCCESS：操作成功。  IMAGE\_RESULT\_BAD\_PARAMETER：参数错误。  IMAGE\_RESULT\_JNI\_ENV\_ABNORMAL：JNI环境异常。  IMAGE\_RESULT\_INVALID\_PARAMETER：参数无效。  IMAGE\_RESULT\_GET\_DATA\_ABNORMAL：图像获取数据失败。  IMAGE\_RESULT\_DECODE\_FAILED：解码失败。  IMAGE\_RESULT\_CHECK\_FORMAT\_ERROR：检查格式失败。  IMAGE\_RESULT\_THIRDPART\_SKIA\_ERROR：skia能力失败。  IMAGE\_RESULT\_DATA\_ABNORMAL：图像输入数据失败。  IMAGE\_RESULT\_ERR\_SHAMEM\_NOT\_EXIST：共享内存失败。  IMAGE\_RESULT\_ERR\_SHAMEM\_DATA\_ABNORMAL：共享内存数据错误。  IMAGE\_RESULT\_MALLOC\_ABNORMAL：图像分配内存失败。  IMAGE\_RESULT\_DATA\_UNSUPPORT：图像数据不支持。  IMAGE\_RESULT\_CROP：裁剪失败。  IMAGE\_RESULT\_UNKNOWN\_FORMAT：图像格式未知。  IMAGE\_RESULT\_PLUGIN\_REGISTER\_FAILED：注册插件失败。  IMAGE\_RESULT\_PLUGIN\_CREATE\_FAILED：创建插件失败。  IMAGE\_RESULT\_DATA\_UNSUPPORT：属性无效。  IMAGE\_RESULT\_ALPHA\_TYPE\_ERROR：透明度类型错误。  IMAGE\_RESULT\_ALLOCATER\_TYPE\_ERROR：内存分配类型错误。 |

### OH\_PixelMap\_GetImageInfo()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_PixelMap_GetImageInfo(const NativePixelMap* native, OhosPixelMapInfos *info)
```

**描述**

获取PixelMap对象图像信息。

从API version 12开始，推荐使用新接口[OH\_PixelmapNative\_GetImageInfo](capi-pixelmap-native-h.md#oh_pixelmapnative_getimageinfo)。

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [NativePixelMap](capi-image-nativepixelmap-.md)\* native | NativePixelMap的指针。 |
| [OhosPixelMapInfos](capi-image-ohospixelmapinfos.md) \*info | 图像信息指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | [IRNdkErrCode](capi-image-mdk-common-h.md#irndkerrcode)：  IMAGE\_RESULT\_SUCCESS：操作成功。  IMAGE\_RESULT\_BAD\_PARAMETER：参数错误。  IMAGE\_RESULT\_JNI\_ENV\_ABNORMAL：JNI环境异常。  IMAGE\_RESULT\_INVALID\_PARAMETER：参数无效。  IMAGE\_RESULT\_GET\_DATA\_ABNORMAL：图像获取数据失败。  IMAGE\_RESULT\_DECODE\_FAILED：解码失败。  IMAGE\_RESULT\_CHECK\_FORMAT\_ERROR：检查格式失败。  IMAGE\_RESULT\_THIRDPART\_SKIA\_ERROR：skia能力失败。  IMAGE\_RESULT\_DATA\_ABNORMAL：图像输入数据失败。  IMAGE\_RESULT\_ERR\_SHAMEM\_NOT\_EXIST：共享内存失败。  IMAGE\_RESULT\_ERR\_SHAMEM\_DATA\_ABNORMAL：共享内存数据错误。  IMAGE\_RESULT\_MALLOC\_ABNORMAL：图像分配内存失败。  IMAGE\_RESULT\_DATA\_UNSUPPORT：图像数据不支持。  IMAGE\_RESULT\_CROP：裁剪失败。  IMAGE\_RESULT\_UNKNOWN\_FORMAT：图像格式未知。  IMAGE\_RESULT\_PLUGIN\_REGISTER\_FAILED：注册插件失败。  IMAGE\_RESULT\_PLUGIN\_CREATE\_FAILED：创建插件失败。  IMAGE\_RESULT\_DATA\_UNSUPPORT：属性无效。  IMAGE\_RESULT\_ALPHA\_TYPE\_ERROR：透明度类型错误。  IMAGE\_RESULT\_ALLOCATER\_TYPE\_ERROR：内存分配类型错误。 |

### OH\_PixelMap\_AccessPixels()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_PixelMap_AccessPixels(const NativePixelMap* native, void** addr)
```

**描述**

获取native PixelMap对象数据的内存地址，并锁定该内存。

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [NativePixelMap](capi-image-nativepixelmap-.md)\* native | NativePixelMap的指针。 |
| void\*\* addr | 用于指向的内存地址的双指针对象。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | [IRNdkErrCode](capi-image-mdk-common-h.md#irndkerrcode)：  IMAGE\_RESULT\_SUCCESS：操作成功。  IMAGE\_RESULT\_BAD\_PARAMETER：参数错误。  IMAGE\_RESULT\_JNI\_ENV\_ABNORMAL：JNI环境异常。  IMAGE\_RESULT\_INVALID\_PARAMETER：参数无效。  IMAGE\_RESULT\_GET\_DATA\_ABNORMAL：图像获取数据失败。  IMAGE\_RESULT\_DECODE\_FAILED：解码失败。  IMAGE\_RESULT\_CHECK\_FORMAT\_ERROR：检查格式失败。  IMAGE\_RESULT\_THIRDPART\_SKIA\_ERROR：skia能力失败。  IMAGE\_RESULT\_DATA\_ABNORMAL：图像输入数据失败。  IMAGE\_RESULT\_ERR\_SHAMEM\_NOT\_EXIST：共享内存失败。  IMAGE\_RESULT\_ERR\_SHAMEM\_DATA\_ABNORMAL：共享内存数据错误。  IMAGE\_RESULT\_MALLOC\_ABNORMAL：图像分配内存失败。  IMAGE\_RESULT\_DATA\_UNSUPPORT：图像数据不支持。  IMAGE\_RESULT\_CROP：裁剪失败。  IMAGE\_RESULT\_UNKNOWN\_FORMAT：图像格式未知。  IMAGE\_RESULT\_PLUGIN\_REGISTER\_FAILED：注册插件失败。  IMAGE\_RESULT\_PLUGIN\_CREATE\_FAILED：创建插件失败。  IMAGE\_RESULT\_DATA\_UNSUPPORT：属性无效。  IMAGE\_RESULT\_ALPHA\_TYPE\_ERROR：透明度类型错误。  IMAGE\_RESULT\_ALLOCATER\_TYPE\_ERROR：内存分配类型错误。 |

### OH\_PixelMap\_UnAccessPixels()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_PixelMap_UnAccessPixels(const NativePixelMap* native)
```

**描述**

释放native PixelMap对象数据的内存锁，用于匹配方法[OH\_PixelMap\_AccessPixels](capi-image-pixel-map-mdk-h.md#oh_pixelmap_accesspixels)。

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [NativePixelMap](capi-image-nativepixelmap-.md)\* native | NativePixelMap的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | [IRNdkErrCode](capi-image-mdk-common-h.md#irndkerrcode)：  IMAGE\_RESULT\_SUCCESS：操作成功。  IMAGE\_RESULT\_BAD\_PARAMETER：参数错误。  IMAGE\_RESULT\_JNI\_ENV\_ABNORMAL：JNI环境异常。  IMAGE\_RESULT\_INVALID\_PARAMETER：参数无效。  IMAGE\_RESULT\_GET\_DATA\_ABNORMAL：图像获取数据失败。  IMAGE\_RESULT\_DECODE\_FAILED：解码失败。  IMAGE\_RESULT\_CHECK\_FORMAT\_ERROR：检查格式失败。  IMAGE\_RESULT\_THIRDPART\_SKIA\_ERROR：skia能力失败。  IMAGE\_RESULT\_DATA\_ABNORMAL：图像输入数据失败。  IMAGE\_RESULT\_ERR\_SHAMEM\_NOT\_EXIST：共享内存失败。  IMAGE\_RESULT\_ERR\_SHAMEM\_DATA\_ABNORMAL：共享内存数据错误。  IMAGE\_RESULT\_MALLOC\_ABNORMAL：图像分配内存失败。  IMAGE\_RESULT\_DATA\_UNSUPPORT：图像数据不支持。  IMAGE\_RESULT\_CROP：裁剪失败。  IMAGE\_RESULT\_UNKNOWN\_FORMAT：图像格式未知。  IMAGE\_RESULT\_PLUGIN\_REGISTER\_FAILED：注册插件失败。  IMAGE\_RESULT\_PLUGIN\_CREATE\_FAILED：创建插件失败。  IMAGE\_RESULT\_DATA\_UNSUPPORT：属性无效。  IMAGE\_RESULT\_ALPHA\_TYPE\_ERROR：透明度类型错误。  IMAGE\_RESULT\_ALLOCATER\_TYPE\_ERROR：内存分配类型错误。 |
