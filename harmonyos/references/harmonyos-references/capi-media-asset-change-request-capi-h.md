---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-media-asset-change-request-capi-h
title: media_asset_change_request_capi.h
breadcrumb: API参考 > 媒体 > Media Library Kit（媒体文件管理服务） > C API > 头文件 > media_asset_change_request_capi.h
category: harmonyos-references
scraped_at: 2026-09-02T15:02:38+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:dc87c0e36388cde42f1bb48486d9d4cb49295001e87bf47ac84f47eded06eafe
---

## 概述

定义与媒体资产更改请求相关的API。提供更改资产的能力。

**库：** libmedia\_asset\_manager.so

**引用文件：** <multimedia/media\_library/media\_asset\_change\_request\_capi.h>

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 12

**相关模块：** [MediaAssetManager](capi-mediaassetmanager.md)

## 汇总

### 函数

| 名称 | 描述 |
| --- | --- |
| [OH\_MediaAssetChangeRequest\* OH\_MediaAssetChangeRequest\_Create(OH\_MediaAsset\* mediaAsset)](capi-media-asset-change-request-capi-h.md#oh_mediaassetchangerequest_create) | 创建[OH\_MediaAssetChangeRequest](capi-mediaassetmanager-oh-mediaassetchangerequest.md)实例。 |
| [MediaLibrary\_ErrorCode OH\_MediaAssetChangeRequest\_AddResourceWithUri(OH\_MediaAssetChangeRequest\* changeRequest, MediaLibrary\_ResourceType resourceType, char\* fileUri)](capi-media-asset-change-request-capi-h.md#oh_mediaassetchangerequest_addresourcewithuri) | 通过文件uri添加资源。 |
| [MediaLibrary\_ErrorCode OH\_MediaAssetChangeRequest\_AddResourceWithBuffer(OH\_MediaAssetChangeRequest\* changeRequest, MediaLibrary\_ResourceType resourceType, uint8\_t\* buffer, uint32\_t length)](capi-media-asset-change-request-capi-h.md#oh_mediaassetchangerequest_addresourcewithbuffer) | 通过ArrayBuffer数据添加资源。 |
| [MediaLibrary\_ErrorCode OH\_MediaAssetChangeRequest\_GetWriteCacheHandler(OH\_MediaAssetChangeRequest\* changeRequest, int32\_t\* fd)](capi-media-asset-change-request-capi-h.md#oh_mediaassetchangerequest_getwritecachehandler) | 获取临时文件写句柄。 |
| [MediaLibrary\_ErrorCode OH\_MediaAssetChangeRequest\_SaveCameraPhoto(OH\_MediaAssetChangeRequest\* changeRequest, MediaLibrary\_ImageFileType imageFileType)](capi-media-asset-change-request-capi-h.md#oh_mediaassetchangerequest_savecameraphoto) | 保存相机拍摄的照片资源。 |
| [MediaLibrary\_ErrorCode OH\_MediaAssetChangeRequest\_DiscardCameraPhoto(OH\_MediaAssetChangeRequest\* changeRequest)](capi-media-asset-change-request-capi-h.md#oh_mediaassetchangerequest_discardcameraphoto) | 丢弃相机拍摄的照片资源。 |
| [MediaLibrary\_ErrorCode OH\_MediaAssetChangeRequest\_Release(OH\_MediaAssetChangeRequest\* changeRequest)](capi-media-asset-change-request-capi-h.md#oh_mediaassetchangerequest_release) | 释放[OH\_MediaAssetChangeRequest](capi-mediaassetmanager-oh-mediaassetchangerequest.md)实例。 |

## 函数说明

### OH\_MediaAssetChangeRequest\_Create()

```c
OH_MediaAssetChangeRequest* OH_MediaAssetChangeRequest_Create(OH_MediaAsset* mediaAsset)
```

**描述**

创建[OH\_MediaAssetChangeRequest](capi-mediaassetmanager-oh-mediaassetchangerequest.md)实例。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_MediaAsset](capi-mediaassetmanager-oh-mediaasset.md)\* mediaAsset | [OH\_MediaAsset](capi-mediaassetmanager-oh-mediaasset.md)实例。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_MediaAssetChangeRequest](capi-mediaassetmanager-oh-mediaassetchangerequest.md)\* | MEDIA\_LIBRARY\_OK：方法调用成功。  MEDIA\_LIBRARY\_PARAMETER\_ERROR：参数错误。可能的原因：  1. 未指定强制参数。  2. 参数类型不正确。  3. 参数验证失败。  MEDIA\_LIBRARY\_INTERNAL\_SYSTEM\_ERROR：内部系统错误。 |

### OH\_MediaAssetChangeRequest\_AddResourceWithUri()

```c
MediaLibrary_ErrorCode OH_MediaAssetChangeRequest_AddResourceWithUri(OH_MediaAssetChangeRequest* changeRequest,MediaLibrary_ResourceType resourceType, char* fileUri)
```

**描述**

通过文件uri添加资源。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_MediaAssetChangeRequest](capi-mediaassetmanager-oh-mediaassetchangerequest.md)\* changeRequest | [OH\_MediaAssetChangeRequest](capi-mediaassetmanager-oh-mediaassetchangerequest.md)实例。 |
| [MediaLibrary\_ResourceType](capi-media-asset-base-capi-h.md#medialibrary_resourcetype) resourceType | 要添加的资源的[MediaLibrary\_ResourceType](capi-media-asset-base-capi-h.md#medialibrary_resourcetype)。 |
| char\* fileUri | 文件uri。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [MediaLibrary\_ErrorCode](capi-media-asset-base-capi-h.md#medialibrary_errorcode) | MEDIA\_LIBRARY\_OK：方法调用成功。  MEDIA\_LIBRARY\_PARAMETER\_ERROR：参数错误。可能的原因：  1. 未指定强制参数。  2. 参数类型不正确。  3. 参数验证失败。  MEDIA\_LIBRARY\_NO\_SUCH\_FILE：文件不存在。  MEDIA\_LIBRARY\_INTERNAL\_SYSTEM\_ERROR：内部系统错误。  MEDIA\_LIBRARY\_OPERATION\_NOT\_SUPPORTED：不支持该操作。 |

### OH\_MediaAssetChangeRequest\_AddResourceWithBuffer()

```c
MediaLibrary_ErrorCode OH_MediaAssetChangeRequest_AddResourceWithBuffer(OH_MediaAssetChangeRequest* changeRequest,MediaLibrary_ResourceType resourceType, uint8_t* buffer, uint32_t length)
```

**描述**

通过ArrayBuffer数据添加资源。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_MediaAssetChangeRequest](capi-mediaassetmanager-oh-mediaassetchangerequest.md)\* changeRequest | [OH\_MediaAssetChangeRequest](capi-mediaassetmanager-oh-mediaassetchangerequest.md)实例。 |
| [MediaLibrary\_ResourceType](capi-media-asset-base-capi-h.md#medialibrary_resourcetype) resourceType | 要添加的资源的类型。 |
| uint8\_t\* buffer | 要添加的数据缓冲区。 |
| uint32\_t length | 数据缓冲区的长度，单位：字节（Byte）。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [MediaLibrary\_ErrorCode](capi-media-asset-base-capi-h.md#medialibrary_errorcode) | MEDIA\_LIBRARY\_OK：方法调用成功。  MEDIA\_LIBRARY\_PARAMETER\_ERROR：参数错误。可能的原因：  1. 未指定强制参数。  2. 参数类型不正确。  3. 参数验证失败。  MEDIA\_LIBRARY\_INTERNAL\_SYSTEM\_ERROR：内部系统错误。  MEDIA\_LIBRARY\_OPERATION\_NOT\_SUPPORTED：不支持该操作。 |

### OH\_MediaAssetChangeRequest\_GetWriteCacheHandler()

```c
MediaLibrary_ErrorCode OH_MediaAssetChangeRequest_GetWriteCacheHandler(OH_MediaAssetChangeRequest* changeRequest,int32_t* fd)
```

**描述**

获取临时文件写句柄。

**需要权限：** ohos.permission.WRITE\_IMAGEVIDEO

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_MediaAssetChangeRequest](capi-mediaassetmanager-oh-mediaassetchangerequest.md)\* changeRequest | [OH\_MediaAssetChangeRequest](capi-mediaassetmanager-oh-mediaassetchangerequest.md)实例。 |
| int32\_t\* fd | 输出参数，用于获取临时文件的写句柄，通过该句柄可以向临时文件写入数据。使用完毕后请及时关闭句柄，避免资源泄漏。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [MediaLibrary\_ErrorCode](capi-media-asset-base-capi-h.md#medialibrary_errorcode) | MEDIA\_LIBRARY\_OK：方法调用成功。  MEDIA\_LIBRARY\_PARAMETER\_ERROR：参数错误。可能的原因：  1. 未指定强制参数。  2. 参数类型不正确。  3. 参数验证失败。  MEDIA\_LIBRARY\_INTERNAL\_SYSTEM\_ERROR：内部系统错误。  MEDIA\_LIBRARY\_PERMISSION\_DENIED：没有权限。  MEDIA\_LIBRARY\_OPERATION\_NOT\_SUPPORTED：不支持该操作。 |

### OH\_MediaAssetChangeRequest\_SaveCameraPhoto()

```c
MediaLibrary_ErrorCode OH_MediaAssetChangeRequest_SaveCameraPhoto(OH_MediaAssetChangeRequest* changeRequest,MediaLibrary_ImageFileType imageFileType)
```

**描述**

保存相机拍摄的照片资源。

**说明** 

* 非YUV拍摄模式下，照片资源保存的编码格式与[Camera\_Format](capi-camera-h.md#camera_format)中的编码格式保持一致。
* YUV拍摄模式下，该接口根据[MediaLibrary\_ImageFileType](capi-media-asset-base-capi-h.md#medialibrary_imagefiletype)将YUV对象编码保存为指定格式。
* 当该接口与[OH\_MediaAssetChangeRequest\_AddResourceWithUri](capi-media-asset-change-request-capi-h.md#oh_mediaassetchangerequest_addresourcewithuri)或[OH\_MediaAssetChangeRequest\_AddResourceWithBuffer](capi-media-asset-change-request-capi-h.md#oh_mediaassetchangerequest_addresourcewithbuffer)组合使用时，照片资源保存的编码格式与[OH\_MediaAssetChangeRequest\_AddResourceWithUri](capi-media-asset-change-request-capi-h.md#oh_mediaassetchangerequest_addresourcewithuri)或[OH\_MediaAssetChangeRequest\_AddResourceWithBuffer](capi-media-asset-change-request-capi-h.md#oh_mediaassetchangerequest_addresourcewithbuffer)添加资源的编码格式保持一致。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_MediaAssetChangeRequest](capi-mediaassetmanager-oh-mediaassetchangerequest.md)\* changeRequest | [OH\_MediaAssetChangeRequest](capi-mediaassetmanager-oh-mediaassetchangerequest.md)实例。 |
| [MediaLibrary\_ImageFileType](capi-media-asset-base-capi-h.md#medialibrary_imagefiletype) imageFileType | 要保存的照片的图像文件类型。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [MediaLibrary\_ErrorCode](capi-media-asset-base-capi-h.md#medialibrary_errorcode) | MEDIA\_LIBRARY\_OK：方法调用成功。  MEDIA\_LIBRARY\_PARAMETER\_ERROR：参数错误。可能的原因：  1. 未指定强制参数。  2. 参数类型不正确。  3. 参数验证失败。  MEDIA\_LIBRARY\_INTERNAL\_SYSTEM\_ERROR：内部系统错误。  MEDIA\_LIBRARY\_OPERATION\_NOT\_SUPPORTED：不支持该操作。 |

### OH\_MediaAssetChangeRequest\_DiscardCameraPhoto()

```c
MediaLibrary_ErrorCode OH_MediaAssetChangeRequest_DiscardCameraPhoto(OH_MediaAssetChangeRequest* changeRequest)
```

**描述**

丢弃相机拍摄的照片资源。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_MediaAssetChangeRequest](capi-mediaassetmanager-oh-mediaassetchangerequest.md)\* changeRequest | [OH\_MediaAssetChangeRequest](capi-mediaassetmanager-oh-mediaassetchangerequest.md)实例。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [MediaLibrary\_ErrorCode](capi-media-asset-base-capi-h.md#medialibrary_errorcode) | MEDIA\_LIBRARY\_OK：方法调用成功。  MEDIA\_LIBRARY\_PARAMETER\_ERROR：参数错误。可能的原因：  1. 未指定强制参数。  2. 参数类型不正确。  3. 参数验证失败。  MEDIA\_LIBRARY\_INTERNAL\_SYSTEM\_ERROR：内部系统错误。  MEDIA\_LIBRARY\_OPERATION\_NOT\_SUPPORTED：不支持该操作。 |

### OH\_MediaAssetChangeRequest\_Release()

```c
MediaLibrary_ErrorCode OH_MediaAssetChangeRequest_Release(OH_MediaAssetChangeRequest* changeRequest)
```

**描述**

释放[OH\_MediaAssetChangeRequest](capi-mediaassetmanager-oh-mediaassetchangerequest.md)实例。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_MediaAssetChangeRequest](capi-mediaassetmanager-oh-mediaassetchangerequest.md)\* changeRequest | [OH\_MediaAssetChangeRequest](capi-mediaassetmanager-oh-mediaassetchangerequest.md)实例。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [MediaLibrary\_ErrorCode](capi-media-asset-base-capi-h.md#medialibrary_errorcode) | MEDIA\_LIBRARY\_OK：方法调用成功。  MEDIA\_LIBRARY\_PARAMETER\_ERROR：参数错误。可能的原因：  1. 未指定强制参数。  2. 参数类型不正确。  3. 参数验证失败。 |
