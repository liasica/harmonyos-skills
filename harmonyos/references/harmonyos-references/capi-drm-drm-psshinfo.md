---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drm-drm-psshinfo
title: DRM_PsshInfo
breadcrumb: API参考 > 媒体 > DRM Kit（数字版权保护服务） > C API > 结构体 > DRM_PsshInfo
category: harmonyos-references
scraped_at: 2026-04-28T08:13:03+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:bbd253f3c4d1602feb9f61ea53403d9ed10c456d47b75741b5777a46daa0cbb0
---

```
1. typedef struct DRM_PsshInfo {...} DRM_PsshInfo
```

## 概述

PhonePC/2in1TabletTVWearable

DRM内容保护系统专用头（Protection System Specific Header）信息。

**起始版本：** 11

**相关模块：** [Drm](capi-drm.md)

**所在头文件：** [native\_drm\_common.h](capi-native-drm-common-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| uint8\_t uuid[DRM\_UUID\_LEN] | UUID的PSSH信息。 |
| int32\_t dataLen | PSSH数据长度。 |
| uint8\_t data[MAX\_PSSH\_DATA\_LEN] | PSSH数据。 |
