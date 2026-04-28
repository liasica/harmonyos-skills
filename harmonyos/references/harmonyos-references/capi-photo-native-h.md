---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-photo-native-h
title: photo_native.h
breadcrumb: API参考 > 媒体 > Camera Kit（相机服务） > C API > 头文件 > photo_native.h
category: harmonyos-references
scraped_at: 2026-04-28T08:12:45+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:be1a453442decd3bcec68b35c7a423d4dd811028c6d53cf1eef7833a6ee3f8bf
---

## 概述

PhonePC/2in1TabletTVWearable

声明相机照片的概念。

**引用文件：** <ohcamera/photo\_native.h>

**库：** libohcamera.so

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 12

**相关模块：** [OH\_Camera](capi-oh-camera.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 结构体

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [OH\_PhotoNative](capi-oh-camera-oh-photonative.md) | OH\_PhotoNative | 相机照片对象。  全质量图对象。 |

### 函数

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [Camera\_ErrorCode OH\_PhotoNative\_GetMainImage(OH\_PhotoNative\* photo, OH\_ImageNative\*\* mainImage)](capi-photo-native-h.md#oh_photonative_getmainimage) | 获取全质量图。 |
| [Camera\_ErrorCode OH\_PhotoNative\_GetUncompressedImage(OH\_PhotoNative\* photo, OH\_PictureNative\*\* picture)](capi-photo-native-h.md#oh_photonative_getuncompressedimage) | 获取非压缩图片。 |
| [Camera\_ErrorCode OH\_PhotoNative\_Release(OH\_PhotoNative\* photo)](capi-photo-native-h.md#oh_photonative_release) | 释放全质量图实例。 |

## 函数说明

PhonePC/2in1TabletTVWearable

### OH\_PhotoNative\_GetMainImage()

PhonePC/2in1TabletTVWearable

```
1. Camera_ErrorCode OH_PhotoNative_GetMainImage(OH_PhotoNative* photo, OH_ImageNative** mainImage)
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

PhonePC/2in1TabletTVWearable

```
1. Camera_ErrorCode OH_PhotoNative_GetUncompressedImage(OH_PhotoNative* photo, OH_PictureNative** picture)
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

PhonePC/2in1TabletTVWearable

```
1. Camera_ErrorCode OH_PhotoNative_Release(OH_PhotoNative* photo)
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
