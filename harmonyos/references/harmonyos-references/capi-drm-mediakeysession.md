---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drm-mediakeysession
title: MediaKeySession
breadcrumb: API参考 > 媒体 > DRM Kit（数字版权保护服务） > C API > 结构体 > MediaKeySession
category: harmonyos-references
scraped_at: 2026-09-02T14:52:53+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:93bbff3f98a1a8c1037468bb02a1ba7ea1b96144ed4d841d05dce11a2e180dfd
---

```c
typedef struct MediaKeySession MediaKeySession
```

## 概述

MediaKeySession结构，用于表示一个媒体密钥会话实例。MediaKeySession是DRM解密流程的核心组件，负责生成许可证请求、处理许可证响应、管理密钥状态等功能。每个MediaKeySession实例对应一个播放会话的密钥解密过程。

通过OH\_MediaKeySystem\_CreateMediaKeySession接口创建实例，通过OH\_MediaKeySession\_Destroy接口销毁实例。每个MediaKeySystem可创建多个MediaKeySession实例，用于处理不同的播放会话。

**起始版本：** 11

**相关模块：** [Drm](capi-drm.md)

**所在头文件：** [native\_drm\_common.h](capi-native-drm-common-h.md)
