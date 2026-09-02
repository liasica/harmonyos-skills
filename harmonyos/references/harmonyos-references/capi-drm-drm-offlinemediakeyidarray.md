---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drm-drm-offlinemediakeyidarray
title: DRM_OfflineMediaKeyIdArray
breadcrumb: API参考 > 媒体 > DRM Kit（数字版权保护服务） > C API > 结构体 > DRM_OfflineMediaKeyIdArray
category: harmonyos-references
scraped_at: 2026-09-02T15:02:29+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:3eeafeee4208e45f8961080a377b223851aded0443bb9967c3efb08d9e4276cd
---

```c
typedef struct DRM_OfflineMediakeyIdArray {...} DRM_OfflineMediakeyIdArray
```

## 概述

离线媒体密钥ID数组。

**起始版本：** 11

**相关模块：** [Drm](capi-drm.md)

**所在头文件：** [native\_drm\_common.h](capi-native-drm-common-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| uint32\_t idsCount | 离线媒体密钥ID的数量，表示idsLen和ids数组中有效元素的个数。取值范围为[0, MAX\_OFFLINE\_MEDIA\_KEY\_ID\_COUNT]。 |
| int32\_t idsLen[MAX\_OFFLINE\_MEDIA\_KEY\_ID\_COUNT] | 离线媒体密钥ID长度数组，每个元素表示对应ids数组行中有效数据的字节数。数组长度由MAX\_OFFLINE\_MEDIA\_KEY\_ID\_COUNT宏定义。 |
| uint8\_t ids[MAX\_OFFLINE\_MEDIA\_KEY\_ID\_COUNT][MAX\_OFFLINE\_MEDIA\_KEY\_ID\_LEN] | 离线媒体密钥ID数据数组，用于存储离线媒体密钥的标识符。每行存储一个密钥ID，有效长度由对应的idsLen元素指定。数组维度由MAX\_OFFLINE\_MEDIA\_KEY\_ID\_COUNT和MAX\_OFFLINE\_MEDIA\_KEY\_ID\_LEN宏定义。 |
