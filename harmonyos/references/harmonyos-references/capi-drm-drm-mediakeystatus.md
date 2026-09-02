---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drm-drm-mediakeystatus
title: DRM_MediaKeyStatus
breadcrumb: API参考 > 媒体 > DRM Kit（数字版权保护服务） > C API > 结构体 > DRM_MediaKeyStatus
category: harmonyos-references
scraped_at: 2026-09-02T15:02:29+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:f252f5161eb99bdb10fea89725f658e4d3f4afc42dad90002e0be28675c9df00
---

```c
typedef struct DRM_MediaKeyStatus {...} DRM_MediaKeyStatus
```

## 概述

媒体密钥状态。

**起始版本：** 11

**相关模块：** [Drm](capi-drm.md)

**所在头文件：** [native\_drm\_common.h](capi-native-drm-common-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| uint32\_t statusCount | 媒体密钥状态项的数量，表示statusName和statusValue数组中有效元素的个数。取值范围为[0, MAX\_MEDIA\_KEY\_STATUS\_COUNT]。 |
| char statusName[MAX\_MEDIA\_KEY\_STATUS\_COUNT][MAX\_MEDIA\_KEY\_STATUS\_NAME\_LEN] | 媒体密钥状态名称数组，每行存储一个状态的名称。常见状态名称包括"Usable"（可用）、"Expired"（已过期）、"OutputRestricted"（输出受限）等，具体由DRM解决方案定义。数组维度由MAX\_MEDIA\_KEY\_STATUS\_COUNT和MAX\_MEDIA\_KEY\_STATUS\_NAME\_LEN宏定义。 |
| char statusValue[MAX\_MEDIA\_KEY\_STATUS\_COUNT][MAX\_MEDIA\_KEY\_STATUS\_VALUE\_LEN] | 媒体密钥状态值数组，每行存储对应statusName的状态值。状态值格式由DRM解决方案定义，可能包含时间戳、级别等信息。数组维度由MAX\_MEDIA\_KEY\_STATUS\_COUNT和MAX\_MEDIA\_KEY\_STATUS\_VALUE\_LEN宏定义。 |
