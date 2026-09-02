---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-media-access-helper-capi-h
title: media_access_helper_capi.h
breadcrumb: API参考 > 媒体 > Media Library Kit（媒体文件管理服务） > C API > 头文件 > media_access_helper_capi.h
category: harmonyos-references
scraped_at: 2026-09-02T15:02:38+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:b837809340a548aa5c63b865bd3d85aa9aaba99a970583396ecedcc1242d016c
---

## 概述

定义与相册管理模块相关的API。

提供创建相册的功能，以及访问和修改相册中的媒体数据信息的功能。

**库：** libmedia\_asset\_manager.so

**引用文件：** <multimedia/media\_library/media\_access\_helper\_capi.h>

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 12

**相关模块：** [MediaAssetManager](capi-mediaassetmanager.md)

## 汇总

### 函数

| 名称 | 描述 |
| --- | --- |
| [MediaLibrary\_ErrorCode OH\_MediaAccessHelper\_ApplyChanges(OH\_MediaAssetChangeRequest\* changeRequest)](capi-media-access-helper-capi-h.md#oh_mediaaccesshelper_applychanges) | 发起应用资产或相册的更改请求。 |

## 函数说明

### OH\_MediaAccessHelper\_ApplyChanges()

```c
MediaLibrary_ErrorCode OH_MediaAccessHelper_ApplyChanges(OH_MediaAssetChangeRequest* changeRequest)
```

**描述**

发起应用资产或相册的更改请求。

**需要权限：** ohos.permission.WRITE\_IMAGEVIDEO

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_MediaAssetChangeRequest](capi-mediaassetmanager-oh-mediaassetchangerequest.md)\* changeRequest | 变更请求实例。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [MediaLibrary\_ErrorCode](capi-media-asset-base-capi-h.md#medialibrary_errorcode) | MEDIA\_LIBRARY\_OK：方法调用成功。  MEDIA\_LIBRARY\_PARAMETER\_ERROR：参数错误。可能的原因：  1. 未指定强制参数。  2. 参数类型不正确。  3. 参数验证失败。  MEDIA\_LIBRARY\_PERMISSION\_DENIED：没有权限。  MEDIA\_LIBRARY\_INTERNAL\_SYSTEM\_ERROR：内部系统错误。 |
