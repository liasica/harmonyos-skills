---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-media-asset-capi-h
title: media_asset_capi.h
breadcrumb: API参考 > 媒体 > Media Library Kit（媒体文件管理服务） > C API > 头文件 > media_asset_capi.h
category: harmonyos-references
scraped_at: 2026-04-28T08:14:21+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:cd1ec55812c5f9aa74225bae4bac6ad16eaf9d3e8936e061efe76f889c01fe5b
---

## 概述

PhonePC/2in1TabletTV

定义与媒体资源相关的API。提供获取图像或视频信息的能力。

**库：** libmedia\_asset\_manager.so

**引用文件：** <multimedia/media\_library/media\_asset\_capi.h>

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 12

**相关模块：** [MediaAssetManager](capi-mediaassetmanager.md)

## 汇总

PhonePC/2in1TabletTV

### 函数

PhonePC/2in1TabletTV

| 名称 | 描述 |
| --- | --- |
| [MediaLibrary\_ErrorCode OH\_MediaAsset\_GetUri(OH\_MediaAsset\* mediaAsset, const char\*\* uri)](capi-media-asset-capi-h.md#oh_mediaasset_geturi) | 获取媒体资产的uri。 |
| [MediaLibrary\_ErrorCode OH\_MediaAsset\_GetMediaType(OH\_MediaAsset\* mediaAsset, MediaLibrary\_MediaType\* mediaType)](capi-media-asset-capi-h.md#oh_mediaasset_getmediatype) | 获取媒体资源类型。 |
| [MediaLibrary\_ErrorCode OH\_MediaAsset\_GetMediaSubType(OH\_MediaAsset\* mediaAsset, MediaLibrary\_MediaSubType\* mediaSubType)](capi-media-asset-capi-h.md#oh_mediaasset_getmediasubtype) | 获取媒体资源子类型。 |
| [MediaLibrary\_ErrorCode OH\_MediaAsset\_GetDisplayName(OH\_MediaAsset\* mediaAsset, const char\*\* displayName)](capi-media-asset-capi-h.md#oh_mediaasset_getdisplayname) | 获取媒体资源的显示名称。 |
| [MediaLibrary\_ErrorCode OH\_MediaAsset\_GetSize(OH\_MediaAsset\* mediaAsset, uint32\_t\* size)](capi-media-asset-capi-h.md#oh_mediaasset_getsize) | 获取媒体资产的文件大小。 |
| [MediaLibrary\_ErrorCode OH\_MediaAsset\_GetDateAdded(OH\_MediaAsset\* mediaAsset, uint32\_t\* dateAdded)](capi-media-asset-capi-h.md#oh_mediaasset_getdateadded) | 获取资产添加日期。 |
| [MediaLibrary\_ErrorCode OH\_MediaAsset\_GetDateModified(OH\_MediaAsset\* mediaAsset, uint32\_t\* dateModified)](capi-media-asset-capi-h.md#oh_mediaasset_getdatemodified) | 获取资产的修改日期。 |
| [MediaLibrary\_ErrorCode OH\_MediaAsset\_GetDateTaken(OH\_MediaAsset\* mediaAsset, uint32\_t\* dateTaken)](capi-media-asset-capi-h.md#oh_mediaasset_getdatetaken) | 获取资产的拍摄日期。 |
| [MediaLibrary\_ErrorCode OH\_MediaAsset\_GetDateAddedMs(OH\_MediaAsset\* mediaAsset, uint32\_t\* dateAddedMs)](capi-media-asset-capi-h.md#oh_mediaasset_getdateaddedms) | 获取资产的添加时间（毫秒）。 |
| [MediaLibrary\_ErrorCode OH\_MediaAsset\_GetDateModifiedMs(OH\_MediaAsset\* mediaAsset, uint32\_t\* dateModifiedMs)](capi-media-asset-capi-h.md#oh_mediaasset_getdatemodifiedms) | 获取资产的修改时间（毫秒）。 |
| [MediaLibrary\_ErrorCode OH\_MediaAsset\_GetDuration(OH\_MediaAsset\* mediaAsset, uint32\_t\* duration)](capi-media-asset-capi-h.md#oh_mediaasset_getduration) | 获取媒体资源的持续时间（毫秒）。 |
| [MediaLibrary\_ErrorCode OH\_MediaAsset\_GetWidth(OH\_MediaAsset\* mediaAsset, uint32\_t\* width)](capi-media-asset-capi-h.md#oh_mediaasset_getwidth) | 获取媒体资源的图像宽度（像素）。 |
| [MediaLibrary\_ErrorCode OH\_MediaAsset\_GetHeight(OH\_MediaAsset\* mediaAsset, uint32\_t\* height)](capi-media-asset-capi-h.md#oh_mediaasset_getheight) | 获取媒体资源的图像高度（像素）。 |
| [MediaLibrary\_ErrorCode OH\_MediaAsset\_GetOrientation(OH\_MediaAsset\* mediaAsset, uint32\_t\* orientation)](capi-media-asset-capi-h.md#oh_mediaasset_getorientation) | 获取图像的旋转角度，单位为度。 |
| [MediaLibrary\_ErrorCode OH\_MediaAsset\_IsFavorite(OH\_MediaAsset\* mediaAsset, uint32\_t\* favorite)](capi-media-asset-capi-h.md#oh_mediaasset_isfavorite) | 获取资产的收藏状态。 |
| [MediaLibrary\_ErrorCode OH\_MediaAsset\_GetTitle(OH\_MediaAsset\* mediaAsset, const char\*\* title)](capi-media-asset-capi-h.md#oh_mediaasset_gettitle) | 获取媒体资产的标题。 |
| [MediaLibrary\_ErrorCode OH\_MediaAsset\_Release(OH\_MediaAsset\* mediaAsset)](capi-media-asset-capi-h.md#oh_mediaasset_release) | 释放媒体资产。 |

## 函数说明

PhonePC/2in1TabletTV

### OH\_MediaAsset\_GetUri()

PhonePC/2in1TabletTV

```
1. MediaLibrary_ErrorCode OH_MediaAsset_GetUri(OH_MediaAsset* mediaAsset, const char** uri)
```

**描述**

获取媒体资产的uri。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_MediaAsset](capi-mediaassetmanager-oh-mediaasset.md)\* mediaAsset | [OH\_MediaAsset](capi-mediaassetmanager-oh-mediaasset.md)实例。 |
| const char\*\* uri | 媒体资产的uri。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [MediaLibrary\_ErrorCode](capi-media-asset-base-capi-h.md#medialibrary_errorcode) | MEDIA\_LIBRARY\_OK：方法调用成功。  MEDIA\_LIBRARY\_PARAMETER\_ERROR：参数错误。可能的原因：  1. 未指定强制参数。  2. 参数类型不正确。  3. 参数验证失败。  MEDIA\_LIBRARY\_INTERNAL\_SYSTEM\_ERROR：内部系统错误。 |

### OH\_MediaAsset\_GetMediaType()

PhonePC/2in1TabletTV

```
1. MediaLibrary_ErrorCode OH_MediaAsset_GetMediaType(OH_MediaAsset* mediaAsset, MediaLibrary_MediaType* mediaType)
```

**描述**

获取媒体资源类型。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_MediaAsset](capi-mediaassetmanager-oh-mediaasset.md)\* mediaAsset | [OH\_MediaAsset](capi-mediaassetmanager-oh-mediaasset.md)实例。 |
| [MediaLibrary\_MediaType](capi-media-asset-base-capi-h.md#medialibrary_mediatype)\* mediaType | 媒体资源类型。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [MediaLibrary\_ErrorCode](capi-media-asset-base-capi-h.md#medialibrary_errorcode) | MEDIA\_LIBRARY\_OK：方法调用成功。  MEDIA\_LIBRARY\_PARAMETER\_ERROR：参数错误。可能的原因：  1. 未指定强制参数。  2. 参数类型不正确。  3. 参数验证失败。  MEDIA\_LIBRARY\_INTERNAL\_SYSTEM\_ERROR：内部系统错误。 |

### OH\_MediaAsset\_GetMediaSubType()

PhonePC/2in1TabletTV

```
1. MediaLibrary_ErrorCode OH_MediaAsset_GetMediaSubType(OH_MediaAsset* mediaAsset,MediaLibrary_MediaSubType* mediaSubType)
```

**描述**

获取媒体资源子类型。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_MediaAsset](capi-mediaassetmanager-oh-mediaasset.md)\* mediaAsset | [OH\_MediaAsset](capi-mediaassetmanager-oh-mediaasset.md)实例。 |
| [MediaLibrary\_MediaSubType](capi-media-asset-base-capi-h.md#medialibrary_mediasubtype)\* mediaSubType | 媒体资源子类型。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [MediaLibrary\_ErrorCode](capi-media-asset-base-capi-h.md#medialibrary_errorcode) | MEDIA\_LIBRARY\_OK：方法调用成功。  MEDIA\_LIBRARY\_PARAMETER\_ERROR：参数错误。可能的原因：  1. 未指定强制参数。  2. 参数类型不正确。  3. 参数验证失败。  MEDIA\_LIBRARY\_INTERNAL\_SYSTEM\_ERROR：内部系统错误。 |

### OH\_MediaAsset\_GetDisplayName()

PhonePC/2in1TabletTV

```
1. MediaLibrary_ErrorCode OH_MediaAsset_GetDisplayName(OH_MediaAsset* mediaAsset, const char** displayName)
```

**描述**

获取媒体资源的显示名称。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_MediaAsset](capi-mediaassetmanager-oh-mediaasset.md)\* mediaAsset | [OH\_MediaAsset](capi-mediaassetmanager-oh-mediaasset.md)实例。 |
| const char\*\* displayName | 媒体资源的显示名称。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [MediaLibrary\_ErrorCode](capi-media-asset-base-capi-h.md#medialibrary_errorcode) | MEDIA\_LIBRARY\_OK：方法调用成功。  MEDIA\_LIBRARY\_PARAMETER\_ERROR：参数错误。可能的原因：  1. 未指定强制参数。  2. 参数类型不正确。  3. 参数验证失败。  MEDIA\_LIBRARY\_INTERNAL\_SYSTEM\_ERROR：内部系统错误。 |

### OH\_MediaAsset\_GetSize()

PhonePC/2in1TabletTV

```
1. MediaLibrary_ErrorCode OH_MediaAsset_GetSize(OH_MediaAsset* mediaAsset, uint32_t* size)
```

**描述**

获取媒体资产的文件大小。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_MediaAsset](capi-mediaassetmanager-oh-mediaasset.md)\* mediaAsset | [OH\_MediaAsset](capi-mediaassetmanager-oh-mediaasset.md)实例。 |
| uint32\_t\* size | 媒体资源的文件大小（以字节为单位）。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [MediaLibrary\_ErrorCode](capi-media-asset-base-capi-h.md#medialibrary_errorcode) | MEDIA\_LIBRARY\_OK：方法调用成功。  MEDIA\_LIBRARY\_PARAMETER\_ERROR：参数错误。可能的原因：  1. 未指定强制参数。  2. 参数类型不正确。  3. 参数验证失败。  MEDIA\_LIBRARY\_INTERNAL\_SYSTEM\_ERROR：内部系统错误。 |

### OH\_MediaAsset\_GetDateAdded()

PhonePC/2in1TabletTV

```
1. MediaLibrary_ErrorCode OH_MediaAsset_GetDateAdded(OH_MediaAsset* mediaAsset, uint32_t* dateAdded)
```

**描述**

获取资产添加日期。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_MediaAsset](capi-mediaassetmanager-oh-mediaasset.md)\* mediaAsset | [OH\_MediaAsset](capi-mediaassetmanager-oh-mediaasset.md)实例。 |
| uint32\_t\* dateAdded | 资产添加日期。该值是添加文件时间距1970年1月1日的秒数值。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [MediaLibrary\_ErrorCode](capi-media-asset-base-capi-h.md#medialibrary_errorcode) | MEDIA\_LIBRARY\_OK：方法调用成功。  MEDIA\_LIBRARY\_PARAMETER\_ERROR：参数错误。可能的原因：  1. 未指定强制参数。  2. 参数类型不正确。  3. 参数验证失败。  MEDIA\_LIBRARY\_INTERNAL\_SYSTEM\_ERROR：内部系统错误。 |

### OH\_MediaAsset\_GetDateModified()

PhonePC/2in1TabletTV

```
1. MediaLibrary_ErrorCode OH_MediaAsset_GetDateModified(OH_MediaAsset* mediaAsset, uint32_t* dateModified)
```

**描述**

获取资产的修改日期。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_MediaAsset](capi-mediaassetmanager-oh-mediaasset.md)\* mediaAsset | [OH\_MediaAsset](capi-mediaassetmanager-oh-mediaasset.md)实例。 |
| uint32\_t\* dateModified | 资产的修改日期。该值是修改文件时间距1970年1月1日的秒数值，修改文件名不会改变此值，当文件内容发生修改时才会更新。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [MediaLibrary\_ErrorCode](capi-media-asset-base-capi-h.md#medialibrary_errorcode) | MEDIA\_LIBRARY\_OK：方法调用成功。  MEDIA\_LIBRARY\_PARAMETER\_ERROR：参数错误。可能的原因：  1. 未指定强制参数。  2. 参数类型不正确。  3. 参数验证失败。  MEDIA\_LIBRARY\_INTERNAL\_SYSTEM\_ERROR：内部系统错误。 |

### OH\_MediaAsset\_GetDateTaken()

PhonePC/2in1TabletTV

```
1. MediaLibrary_ErrorCode OH_MediaAsset_GetDateTaken(OH_MediaAsset* mediaAsset, uint32_t* dateTaken)
```

**描述**

获取资产的拍摄日期。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_MediaAsset](capi-mediaassetmanager-oh-mediaasset.md)\* mediaAsset | [OH\_MediaAsset](capi-mediaassetmanager-oh-mediaasset.md)实例。 |
| uint32\_t\* dateTaken | 资产的拍摄日期。该值是文件拍照时间距1970年1月1日的秒数值。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [MediaLibrary\_ErrorCode](capi-media-asset-base-capi-h.md#medialibrary_errorcode) | MEDIA\_LIBRARY\_OK：方法调用成功。  MEDIA\_LIBRARY\_PARAMETER\_ERROR：参数错误。可能的原因：  1. 未指定强制参数。  2. 参数类型不正确。  3. 参数验证失败。  MEDIA\_LIBRARY\_INTERNAL\_SYSTEM\_ERROR：内部系统错误。 |

### OH\_MediaAsset\_GetDateAddedMs()

PhonePC/2in1TabletTV

```
1. MediaLibrary_ErrorCode OH_MediaAsset_GetDateAddedMs(OH_MediaAsset* mediaAsset, uint32_t* dateAddedMs)
```

**描述**

获取资产的添加时间（毫秒）。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_MediaAsset](capi-mediaassetmanager-oh-mediaasset.md)\* mediaAsset | [OH\_MediaAsset](capi-mediaassetmanager-oh-mediaasset.md)实例。 |
| uint32\_t\* dateAddedMs | 资产的添加时间（毫秒）。该值是添加文件时间距1970年1月1日的毫秒数值。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [MediaLibrary\_ErrorCode](capi-media-asset-base-capi-h.md#medialibrary_errorcode) | MEDIA\_LIBRARY\_OK：方法调用成功。  MEDIA\_LIBRARY\_PARAMETER\_ERROR：参数错误。可能的原因：  1. 未指定强制参数。  2. 参数类型不正确。  3. 参数验证失败。  MEDIA\_LIBRARY\_INTERNAL\_SYSTEM\_ERROR：内部系统错误。 |

### OH\_MediaAsset\_GetDateModifiedMs()

PhonePC/2in1TabletTV

```
1. MediaLibrary_ErrorCode OH_MediaAsset_GetDateModifiedMs(OH_MediaAsset* mediaAsset, uint32_t* dateModifiedMs)
```

**描述**

获取资产的修改时间（毫秒）。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_MediaAsset](capi-mediaassetmanager-oh-mediaasset.md)\* mediaAsset | [OH\_MediaAsset](capi-mediaassetmanager-oh-mediaasset.md)实例。 |
| uint32\_t\* dateModifiedMs | 资产的修改时间（毫秒）。该值是修改文件时间距1970年1月1日的毫秒数值，修改文件名不会改变此值，当文件内容发生修改时才会更新。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [MediaLibrary\_ErrorCode](capi-media-asset-base-capi-h.md#medialibrary_errorcode) | MEDIA\_LIBRARY\_OK：方法调用成功。  MEDIA\_LIBRARY\_PARAMETER\_ERROR：参数错误。可能的原因：  1. 未指定强制参数。  2. 参数类型不正确。  3. 参数验证失败。  MEDIA\_LIBRARY\_INTERNAL\_SYSTEM\_ERROR：内部系统错误。 |

### OH\_MediaAsset\_GetDuration()

PhonePC/2in1TabletTV

```
1. MediaLibrary_ErrorCode OH_MediaAsset_GetDuration(OH_MediaAsset* mediaAsset, uint32_t* duration)
```

**描述**

获取媒体资源的持续时间（毫秒）。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_MediaAsset](capi-mediaassetmanager-oh-mediaasset.md)\* mediaAsset | [OH\_MediaAsset](capi-mediaassetmanager-oh-mediaasset.md)实例。 |
| uint32\_t\* duration | 媒体资源的持续时间（毫秒）。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [MediaLibrary\_ErrorCode](capi-media-asset-base-capi-h.md#medialibrary_errorcode) | MEDIA\_LIBRARY\_OK：方法调用成功。  MEDIA\_LIBRARY\_PARAMETER\_ERROR：参数错误。可能的原因：  1. 未指定强制参数。  2. 参数类型不正确。  3. 参数验证失败。  MEDIA\_LIBRARY\_INTERNAL\_SYSTEM\_ERROR：内部系统错误。 |

### OH\_MediaAsset\_GetWidth()

PhonePC/2in1TabletTV

```
1. MediaLibrary_ErrorCode OH_MediaAsset_GetWidth(OH_MediaAsset* mediaAsset, uint32_t* width)
```

**描述**

获取媒体资源的图像宽度（像素）。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_MediaAsset](capi-mediaassetmanager-oh-mediaasset.md)\* mediaAsset | [OH\_MediaAsset](capi-mediaassetmanager-oh-mediaasset.md)实例。 |
| uint32\_t\* width | 媒体资源的图像宽度（像素）。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [MediaLibrary\_ErrorCode](capi-media-asset-base-capi-h.md#medialibrary_errorcode) | MEDIA\_LIBRARY\_OK：方法调用成功。  MEDIA\_LIBRARY\_PARAMETER\_ERROR：参数错误。可能的原因：  1. 未指定强制参数。  2. 参数类型不正确。  3. 参数验证失败。  MEDIA\_LIBRARY\_INTERNAL\_SYSTEM\_ERROR：内部系统错误。 |

### OH\_MediaAsset\_GetHeight()

PhonePC/2in1TabletTV

```
1. MediaLibrary_ErrorCode OH_MediaAsset_GetHeight(OH_MediaAsset* mediaAsset, uint32_t* height)
```

**描述**

获取媒体资源的图像高度（像素）。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_MediaAsset](capi-mediaassetmanager-oh-mediaasset.md)\* mediaAsset | [OH\_MediaAsset](capi-mediaassetmanager-oh-mediaasset.md)实例。 |
| uint32\_t\* height | 媒体资源的图像高度（像素）。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [MediaLibrary\_ErrorCode](capi-media-asset-base-capi-h.md#medialibrary_errorcode) | MEDIA\_LIBRARY\_OK：方法调用成功。  MEDIA\_LIBRARY\_PARAMETER\_ERROR：参数错误。可能的原因：  1. 未指定强制参数。  2. 参数类型不正确。  3. 参数验证失败。  MEDIA\_LIBRARY\_INTERNAL\_SYSTEM\_ERROR：内部系统错误。 |

### OH\_MediaAsset\_GetOrientation()

PhonePC/2in1TabletTV

```
1. MediaLibrary_ErrorCode OH_MediaAsset_GetOrientation(OH_MediaAsset* mediaAsset, uint32_t* orientation)
```

**描述**

获取图像的旋转角度，单位为度。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_MediaAsset](capi-mediaassetmanager-oh-mediaasset.md)\* mediaAsset | [OH\_MediaAsset](capi-mediaassetmanager-oh-mediaasset.md)实例。 |
| uint32\_t\* orientation | 图像的旋转角度，单位为度。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [MediaLibrary\_ErrorCode](capi-media-asset-base-capi-h.md#medialibrary_errorcode) | MEDIA\_LIBRARY\_OK：方法调用成功。  MEDIA\_LIBRARY\_PARAMETER\_ERROR：参数错误。可能的原因：  1. 未指定强制参数。  2. 参数类型不正确。  3. 参数验证失败。  MEDIA\_LIBRARY\_INTERNAL\_SYSTEM\_ERROR：内部系统错误。 |

### OH\_MediaAsset\_IsFavorite()

PhonePC/2in1TabletTV

```
1. MediaLibrary_ErrorCode OH_MediaAsset_IsFavorite(OH_MediaAsset* mediaAsset, uint32_t* favorite)
```

**描述**

获取资产的收藏状态。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_MediaAsset](capi-mediaassetmanager-oh-mediaasset.md)\* mediaAsset | [OH\_MediaAsset](capi-mediaassetmanager-oh-mediaasset.md)实例。 |
| uint32\_t\* favorite | 资产的收藏状态。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [MediaLibrary\_ErrorCode](capi-media-asset-base-capi-h.md#medialibrary_errorcode) | MEDIA\_LIBRARY\_OK：方法调用成功。  MEDIA\_LIBRARY\_PARAMETER\_ERROR：参数错误。可能的原因：  1. 未指定强制参数。  2. 参数类型不正确。  3. 参数验证失败。  MEDIA\_LIBRARY\_INTERNAL\_SYSTEM\_ERROR：内部系统错误。 |

### OH\_MediaAsset\_GetTitle()

PhonePC/2in1TabletTV

```
1. MediaLibrary_ErrorCode OH_MediaAsset_GetTitle(OH_MediaAsset* mediaAsset, const char** title)
```

**描述**

获取媒体资产的标题。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_MediaAsset](capi-mediaassetmanager-oh-mediaasset.md)\* mediaAsset | [OH\_MediaAsset](capi-mediaassetmanager-oh-mediaasset.md)实例。 |
| const char\*\* title | 媒体资产的标题。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [MediaLibrary\_ErrorCode](capi-media-asset-base-capi-h.md#medialibrary_errorcode) | MEDIA\_LIBRARY\_OK：方法调用成功。  MEDIA\_LIBRARY\_PARAMETER\_ERROR：参数错误。可能的原因：  1. 未指定强制参数。  2. 参数类型不正确。  3. 参数验证失败。  MEDIA\_LIBRARY\_INTERNAL\_SYSTEM\_ERROR：内部系统错误。 |

### OH\_MediaAsset\_Release()

PhonePC/2in1TabletTV

```
1. MediaLibrary_ErrorCode OH_MediaAsset_Release(OH_MediaAsset* mediaAsset)
```

**描述**

释放媒体资产。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_MediaAsset](capi-mediaassetmanager-oh-mediaasset.md)\* mediaAsset | [OH\_MediaAsset](capi-mediaassetmanager-oh-mediaasset.md)实例。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [MediaLibrary\_ErrorCode](capi-media-asset-base-capi-h.md#medialibrary_errorcode) | MEDIA\_LIBRARY\_OK：方法调用成功。  MEDIA\_LIBRARY\_PARAMETER\_ERROR：参数错误。可能的原因：  1. 未指定强制参数。  2. 参数类型不正确。  3. 参数验证失败。 |
