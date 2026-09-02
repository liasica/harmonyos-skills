---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drm-drm-mediakeysystemdescription
title: DRM_MediaKeySystemDescription
breadcrumb: API参考 > 媒体 > DRM Kit（数字版权保护服务） > C API > 结构体 > DRM_MediaKeySystemDescription
category: harmonyos-references
scraped_at: 2026-09-02T15:02:29+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:b8fb918a3fc6b9d72bc3e2eec39f106bef34436939cb05ec8905958b441abd3b
---

```c
typedef struct DRM_MediaKeySystemDescription {...} DRM_MediaKeySystemDescription
```

## 概述

DRM解决方案名称及其UUID的列表。

**起始版本：** 12

**相关模块：** [Drm](capi-drm.md)

**所在头文件：** [native\_drm\_common.h](capi-native-drm-common-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| char name[MAX\_MEDIA\_KEY\_SYSTEM\_NAME\_LEN] | DRM插件的名称，用于唯一标识一个DRM解决方案。名称格式由DRM解决方案定义，如"com.widevine.alpha"、"com.microsoft.playready"等。数组长度由MAX\_MEDIA\_KEY\_SYSTEM\_NAME\_LEN宏定义。 |
| uint8\_t uuid[DRM\_UUID\_LEN] | DRM系统的UUID（通用唯一标识符），用于唯一标识一个DRM内容保护系统。UUID长度为16字节（DRM\_UUID\_LEN），由DRM解决方案提供商分配。UUID与name对应同一DRM解决方案的不同表示形式。 |
