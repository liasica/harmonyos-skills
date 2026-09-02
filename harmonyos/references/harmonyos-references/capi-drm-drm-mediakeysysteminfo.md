---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drm-drm-mediakeysysteminfo
title: DRM_MediaKeySystemInfo
breadcrumb: API参考 > 媒体 > DRM Kit（数字版权保护服务） > C API > 结构体 > DRM_MediaKeySystemInfo
category: harmonyos-references
scraped_at: 2026-09-02T15:02:29+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:2e067a0bfef6cfbc7feff611bf639c8a00bb7440d5865d04f3f7f18097a998fc
---

```c
typedef struct DRM_MediaKeySystemInfo {...} DRM_MediaKeySystemInfo
```

## 概述

加密媒体内容的DRM信息。

**起始版本：** 11

**相关模块：** [Drm](capi-drm.md)

**所在头文件：** [native\_drm\_common.h](capi-native-drm-common-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| uint32\_t psshCount | PSSH信息的数量，表示psshInfo数组中有效元素的个数。一个媒体文件可能包含多个DRM系统的PSSH，取值范围为[0, MAX\_PSSH\_INFO\_COUNT]。 |
| [DRM\_PsshInfo](capi-drm-drm-psshinfo.md) psshInfo[MAX\_PSSH\_INFO\_COUNT] | PSSH信息数组，每项包含一个DRM内容保护系统专用头的信息。数组长度由MAX\_PSSH\_INFO\_COUNT宏定义，每项包含DRM系统UUID和初始化数据。 |
