---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-photo-native-h
title: photo_native.h
breadcrumb: API参考 > 媒体 > Camera Kit（相机服务） > C API > 头文件 > photo_native.h
category: harmonyos-references
scraped_at: 2026-11-12T09:56:33+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:378bd3b861da4c90c41ffca0cc4c7ec0d4de051e583f8558f4ed04c56d2306f1
---

## 概述

声明相机照片的概念。

**引用文件：** <ohcamera/photo\_native.h>

**库：** libohcamera.so

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 12

**相关模块：** [OH\_Camera](capi-oh-camera.md)

## 汇总

### 结构体

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [OH\_PhotoNative](capi-oh-camera-oh-photonative.md) | OH\_PhotoNative | 相机照片对象。  全质量图对象。 |

### 函数

| 名称 | 描述 |
| --- | --- |
| [Camera\_ErrorCode OH\_PhotoNative\_GetMainImage(OH\_PhotoNative\* photo, OH\_ImageNative\*\* mainImage)](capi-photo-native-h.md#oh_photonative_getmainimage) | 获取全质量图。 |
| [Camera\_ErrorCode OH\_PhotoNative\_GetUncompressedImage(OH\_PhotoNative\* photo, OH\_PictureNative\*\* picture)](capi-photo-native-h.md#oh_photonative_getuncompressedimage) | 获取非压缩图片。 |
| [Camera\_ErrorCode OH\_PhotoNative\_GetAuxiliaryImage(const OH\_PhotoNative\* photo, OH\_Camera\_AuxiliaryPhotoType type, OH\_ImageNative\*\* outImage)](capi-photo-native-h.md#oh_photonative_getauxiliaryimage) | 获取指定类型的辅助图。 |
| [Camera\_ErrorCode OH\_PhotoNative\_GetUncompressedAuxiliaryImage(const OH\_PhotoNative\* photo, OH\_Camera\_AuxiliaryPhotoType type, OH\_PictureNative\*\* outImage)](capi-photo-native-h.md#oh_photonative_getuncompressedauxiliaryimage) | 获取指定类型的未压缩辅助图。 |
| [Camera\_ErrorCode OH\_PhotoNative\_Release(OH\_PhotoNative\* photo)](capi-photo-native-h.md#oh_photonative_release) | 释放全质量图实例。 |
| [Camera\_ErrorCode OH\_PhotoNative\_ReleasePicture(OH\_PictureNative\* picture)](capi-photo-native-h.md#oh_photonative_releasepicture) | 释放OH\_PictureNative实例。 |
| [Camera\_ErrorCode OH\_PhotoNative\_ReleaseImage(OH\_ImageNative\* image)](capi-photo-native-h.md#oh_photonative_releaseimage) | 释放OH\_ImageNative实例。 |

## 函数说明

### OH\_PhotoNative\_GetMainImage()

```c
Camera_ErrorCode OH_PhotoNative_GetMainImage(OH_PhotoNative* photo, OH_ImageNative** mainImage)
```

**描述**

获取全质量图。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_PhotoNative](capi-oh-camera-oh-photonative.md)\* photo | OH\_PhotoNative实例。 |
| [OH\_ImageNative](capi-image-nativemodule-oh-imagenative.md)\*\* mainImage | 用于获取全质量图的OH\_ImageNative。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或参数类型不正确。 |

### OH\_PhotoNative\_GetUncompressedImage()

```c
Camera_ErrorCode OH_PhotoNative_GetUncompressedImage(OH_PhotoNative* photo, OH_PictureNative** picture)
```

**描述**

获取非压缩图片。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_PhotoNative](capi-oh-camera-oh-photonative.md)\* photo | OH\_PhotoNative实例。 |
| [OH\_PictureNative](capi-image-nativemodule-oh-picturenative.md)\*\* picture | 用于获取非压缩图片的OH\_PictureNative。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或参数类型不正确。 |

### OH\_PhotoNative\_Release()

```c
Camera_ErrorCode OH_PhotoNative_Release(OH_PhotoNative* photo)
```

**描述**

释放全质量图实例。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_PhotoNative](capi-oh-camera-oh-photonative.md)\* photo | 要被释放的OH\_PhotoNative实例。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：方法调用成功。  CAMERA\_INVALID\_ARGUMENT：参数丢失或参数类型不正确。 |

### OH\_PhotoNative\_GetAuxiliaryImage()

```c
Camera_ErrorCode OH_PhotoNative_GetAuxiliaryImage(const OH_PhotoNative* photo, OH_Camera_AuxiliaryPhotoType type, OH_ImageNative** outImage)
```

**描述**

获取指定类型的辅助图。

使用场景：使用本接口前需先通过[OH\_PhotoOutput\_SetAutoAuxiliaryPhotosDeliveryEnabled()](capi-photo-output-h.md#oh_photooutput_setautoauxiliaryphotosdeliveryenabled)开启指定类型辅助图的自动回传功能，拍照获得的OH\_PhotoNative对象中才会包含辅助图，并通过本接口按类型获取辅助图，用于后续分析处理。支持的辅助图类型及各自用途请参考[OH\_Camera\_AuxiliaryPhotoType](capi-camera-h.md#oh_camera_auxiliaryphototype)。

**起始版本：** 26.0.1

**资源释放：** [OH\_PhotoNative\_ReleaseImage](capi-photo-native-h.md#oh_photonative_releaseimage)

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [OH\_PhotoNative](capi-oh-camera-oh-photonative.md)\* photo | 指向OH\_PhotoNative实例的指针。 |
| [OH\_Camera\_AuxiliaryPhotoType](capi-camera-h.md#oh_camera_auxiliaryphototype) type | 辅助图类型。 |
| [OH\_ImageNative](capi-image-nativemodule-oh-imagenative.md)\*\* outImage | 指向OH\_ImageNative实例的双重指针，用于接收获取的辅助图。调用成功时，指向有效的辅助图实例；调用失败时，该参数返回NULL。该实例由调用方管理，使用完成后应调用OH\_PhotoNative\_ReleaseImage()释放。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：操作成功。  CAMERA\_INVALID\_ARGUMENT：缺少参数或参数类型不正确。  CAMERA\_ERROR\_PARAM\_OUT\_OF\_RANGE：参数超出范围。 |

### OH\_PhotoNative\_GetUncompressedAuxiliaryImage()

```c
Camera_ErrorCode OH_PhotoNative_GetUncompressedAuxiliaryImage(const OH_PhotoNative* photo,
    OH_Camera_AuxiliaryPhotoType type, OH_PictureNative** outImage)
```

**描述**

获取指定类型的未压缩辅助图。

使用场景：使用本接口前需先通过[OH\_PhotoOutput\_SetAutoAuxiliaryPhotosDeliveryEnabled()](capi-photo-output-h.md#oh_photooutput_setautoauxiliaryphotosdeliveryenabled)开启指定类型辅助图的自动回传功能，拍照获得的OH\_PhotoNative对象中才会包含辅助图，并通过本接口按类型获取未压缩的辅助图，用于后续分析处理。支持的辅助图类型及各自用途请参考[OH\_Camera\_AuxiliaryPhotoType](capi-camera-h.md#oh_camera_auxiliaryphototype)。

**起始版本：** 26.0.1

**资源释放：** [OH\_PhotoNative\_ReleasePicture](capi-photo-native-h.md#oh_photonative_releasepicture)

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [OH\_PhotoNative](capi-oh-camera-oh-photonative.md)\* photo | 指向OH\_PhotoNative实例的指针。 |
| [OH\_Camera\_AuxiliaryPhotoType](capi-camera-h.md#oh_camera_auxiliaryphototype) type | 辅助图类型。 |
| [OH\_PictureNative](capi-image-nativemodule-oh-picturenative.md)\*\* outImage | 指向OH\_PictureNative实例的双重指针，用于接收获取的未压缩辅助图。调用成功时，指向有效的辅助图实例；调用失败时，该参数返回NULL。该实例由调用方管理，使用完成后应调用OH\_PhotoNative\_ReleasePicture()释放。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：操作成功。  CAMERA\_INVALID\_ARGUMENT：缺少参数或参数类型不正确。  CAMERA\_ERROR\_PARAM\_OUT\_OF\_RANGE：参数超出范围。 |

### OH\_PhotoNative\_ReleasePicture()

```c
Camera_ErrorCode OH_PhotoNative_ReleasePicture(OH_PictureNative* picture)
```

**描述**

释放OH\_PictureNative实例。

**起始版本：** 26.0.1

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_PictureNative](capi-image-nativemodule-oh-picturenative.md)\* picture | 指向要释放的OH\_PictureNative实例的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：操作成功。  CAMERA\_INVALID\_ARGUMENT：缺少参数或参数类型不正确。 |

### OH\_PhotoNative\_ReleaseImage()

```c
Camera_ErrorCode OH_PhotoNative_ReleaseImage(OH_ImageNative* image)
```

**描述**

释放OH\_ImageNative实例。

**起始版本：** 26.0.1

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ImageNative](capi-image-nativemodule-oh-imagenative.md)\* image | 指向要释放的OH\_ImageNative实例的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Camera\_ErrorCode](capi-camera-h.md#camera_errorcode) | CAMERA\_OK：操作成功。  CAMERA\_INVALID\_ARGUMENT：缺少参数或参数类型不正确。 |
