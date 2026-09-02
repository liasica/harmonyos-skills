---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drm-drm-keysinfo
title: DRM_KeysInfo
breadcrumb: API参考 > 媒体 > DRM Kit（数字版权保护服务） > C API > 结构体 > DRM_KeysInfo
category: harmonyos-references
scraped_at: 2026-09-02T15:02:29+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:764cf1c51c56f56366337fb3972fed4ebdc44ea2fd9ca2ff16fd2d2ed01bff5d
---

```c
typedef struct DRM_KeysInfo {...} DRM_KeysInfo
```

## 概述

媒体密钥信息。

**起始版本：** 11

**相关模块：** [Drm](capi-drm.md)

**所在头文件：** [native\_drm\_common.h](capi-native-drm-common-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| uint32\_t keysInfoCount | 媒体密钥信息的数量，表示keyId和statusValue数组中有效元素的个数。取值范围为[0, MAX\_KEY\_INFO\_COUNT]。 |
| uint8\_t keyId[MAX\_KEY\_INFO\_COUNT][MAX\_KEY\_ID\_LEN] | 媒体密钥ID数组，每行存储一个密钥的标识符。密钥ID用于标识唯一的一个媒体密钥。数组维度由MAX\_KEY\_INFO\_COUNT和MAX\_KEY\_ID\_LEN宏定义。 |
| char statusValue[MAX\_KEY\_INFO\_COUNT][MAX\_KEY\_STATUS\_VALUE\_LEN] | 媒体密钥状态值数组，每行存储对应keyId的密钥状态。状态值由DRM解决方案定义，常见状态包括"usable"（可用）、"expired"（已过期）等。数组维度由MAX\_KEY\_INFO\_COUNT和MAX\_KEY\_STATUS\_VALUE\_LEN宏定义。 |
