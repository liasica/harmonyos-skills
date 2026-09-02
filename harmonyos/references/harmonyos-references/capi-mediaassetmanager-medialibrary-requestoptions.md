---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-mediaassetmanager-medialibrary-requestoptions
title: MediaLibrary_RequestOptions
breadcrumb: API参考 > 媒体 > Media Library Kit（媒体文件管理服务） > C API > 结构体 > MediaLibrary_RequestOptions
category: harmonyos-references
scraped_at: 2026-09-02T15:02:38+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:7ea873e72adf78afd3d0c16f1587883ce671cb59a667dd24c74ddb81ec0a2748
---

```c
typedef struct MediaLibrary_RequestOptions {...} MediaLibrary_RequestOptions
```

## 概述

请求策略模式配置项。

用于配置媒体资源的请求策略模式。

**起始版本：** 12

**相关模块：** [MediaAssetManager](capi-mediaassetmanager.md)

**所在头文件：** [media\_asset\_base\_capi.h](capi-media-asset-base-capi-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| [MediaLibrary\_DeliveryMode](capi-media-asset-base-capi-h.md#medialibrary_deliverymode) deliveryMode | 请求资源分发模式，用于指定媒体资源的请求策略。 |
