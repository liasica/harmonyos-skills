---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-mediaassetmanager-medialibrary-requestid
title: MediaLibrary_RequestId
breadcrumb: API参考 > 媒体 > Media Library Kit（媒体文件管理服务） > C API > 结构体 > MediaLibrary_RequestId
category: harmonyos-references
scraped_at: 2026-09-02T15:02:38+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:0036bb972c11b1584688472dea91d99c22b8ff312e205c50265aa44de1ee7497
---

```c
typedef struct MediaLibrary_RequestId {...} MediaLibrary_RequestId
```

## 概述

定义请求ID。

当请求媒体库资源时，会返回此类型。

请求ID可用于取消对应的媒体库资源请求。

如果请求失败，值将全为零，如 "00000000-0000-0000-0000-000000000000"。

**起始版本：** 12

**相关模块：** [MediaAssetManager](capi-mediaassetmanager.md)

**所在头文件：** [media\_asset\_base\_capi.h](capi-media-asset-base-capi-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| char requestId[UUID\_STR\_MAX\_LENGTH] | 请求ID，用于标识媒体库资源请求，可用于取消该请求。 |
