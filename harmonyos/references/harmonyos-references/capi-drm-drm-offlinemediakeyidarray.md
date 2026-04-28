---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drm-drm-offlinemediakeyidarray
title: DRM_OfflineMediakeyIdArray
breadcrumb: API参考 > 媒体 > DRM Kit（数字版权保护服务） > C API > 结构体 > DRM_OfflineMediakeyIdArray
category: harmonyos-references
scraped_at: 2026-04-28T08:13:03+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:edd913e9b9f3a4d6584172a18691677def96ac36b37bb9ea9b976644e8434201
---

```
1. typedef struct DRM_OfflineMediakeyIdArray {...} DRM_OfflineMediakeyIdArray
```

## 概述

PhonePC/2in1TabletTVWearable

离线媒体密钥ID数组。

**起始版本：** 11

**相关模块：** [Drm](capi-drm.md)

**所在头文件：** [native\_drm\_common.h](capi-native-drm-common-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| uint32\_t idsCount | ID计数。 |
| int32\_t idsLen[MAX\_OFFLINE\_MEDIA\_KEY\_ID\_COUNT] | ID长度集合。 |
| uint8\_t ids[MAX\_OFFLINE\_MEDIA\_KEY\_ID\_COUNT][MAX\_OFFLINE\_MEDIA\_KEY\_ID\_LEN] | ID数据集合。 |
