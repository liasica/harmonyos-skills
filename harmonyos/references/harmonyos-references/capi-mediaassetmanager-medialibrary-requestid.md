---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-mediaassetmanager-medialibrary-requestid
title: MediaLibrary_RequestId
breadcrumb: API参考 > 媒体 > Media Library Kit（媒体文件管理服务） > C API > 结构体 > MediaLibrary_RequestId
category: harmonyos-references
scraped_at: 2026-04-28T08:14:22+08:00
doc_updated_at: 2026-03-19
content_hash: sha256:fdc1de3dbd9b22b56f50b019083a4d71e6b87cec34426467aee109692aa0d0fa
---

```
1. typedef struct MediaLibrary_RequestId {...} MediaLibrary_RequestId
```

## 概述

PhonePC/2in1TabletTV

定义请求ID。

当请求媒体库资源时，会返回此类型。

请求ID可用于取消请求。

如果请求失败，值将全为零，如 "00000000-0000-0000-0000-000000000000"。

**起始版本：** 12

**相关模块：** [MediaAssetManager](capi-mediaassetmanager.md)

**所在头文件：** [media\_asset\_base\_capi.h](capi-media-asset-base-capi-h.md)

## 汇总

PhonePC/2in1TabletTV

### 成员变量

PhonePC/2in1TabletTV

| 名称 | 描述 |
| --- | --- |
| char requestId[UUID\_STR\_MAX\_LENGTH] | 请求ID。 |
