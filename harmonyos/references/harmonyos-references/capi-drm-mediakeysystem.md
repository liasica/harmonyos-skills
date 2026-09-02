---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drm-mediakeysystem
title: MediaKeySystem
breadcrumb: API参考 > 媒体 > DRM Kit（数字版权保护服务） > C API > 结构体 > MediaKeySystem
category: harmonyos-references
scraped_at: 2026-09-02T14:52:53+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:c33f47730ad6fc4719e89fef687c0c899f0da4fd76384ce349c21575e65dd4f5
---

```c
typedef struct MediaKeySystem MediaKeySystem
```

## 概述

MediaKeySystem结构，用于表示一个媒体密钥系统实例。MediaKeySystem提供数字版权保护能力，负责DRM插件配置管理、设备证书管理、统计信息获取、内容保护级别查询以及创建MediaKeySession等功能。通过OH\_MediaKeySystem\_Create接口创建实例，通过OH\_MediaKeySystem\_Destroy接口销毁实例。

**起始版本：** 11

**相关模块：** [Drm](capi-drm.md)

**所在头文件：** [native\_drm\_common.h](capi-native-drm-common-h.md)
