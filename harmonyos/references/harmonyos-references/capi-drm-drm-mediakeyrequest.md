---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drm-drm-mediakeyrequest
title: DRM_MediaKeyRequest
breadcrumb: API参考 > 媒体 > DRM Kit（数字版权保护服务） > C API > 结构体 > DRM_MediaKeyRequest
category: harmonyos-references
scraped_at: 2026-09-02T15:02:29+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:1d39273cd9edf9cd14151f3e7b49d7adb9854c90734e67787b2dacc4eac2bb5e
---

```c
typedef struct DRM_MediaKeyRequest {...} DRM_MediaKeyRequest
```

## 概述

媒体密钥请求。

**起始版本：** 11

**相关模块：** [Drm](capi-drm.md)

**所在头文件：** [native\_drm\_common.h](capi-native-drm-common-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| [DRM\_MediaKeyRequestType](capi-native-drm-common-h.md#drm_mediakeyrequesttype) type | 媒体密钥请求类型，指示请求的用途。常见类型包括DRM\_MEDIA\_KEY\_REQUEST\_TYPE\_INITIAL（初始请求）、DRM\_MEDIA\_KEY\_REQUEST\_TYPE\_RENEWAL（续期请求）等，具体类型由DRM解决方案决定。 |
| int32\_t dataLen | 媒体密钥请求数据的长度，表示data数组中有效数据的字节数。单位为字节（Byte），取值范围为[0, MAX\_MEDIA\_KEY\_REQUEST\_DATA\_LEN]。 |
| uint8\_t data[MAX\_MEDIA\_KEY\_REQUEST\_DATA\_LEN] | 媒体密钥请求数据，需要发送到许可证服务器的数据。数据格式由DRM解决方案定义，通常为特定格式的二进制数据或JSON格式。数组长度由MAX\_MEDIA\_KEY\_REQUEST\_DATA\_LEN宏定义。 |
| char defaultUrl[MAX\_DEFAULT\_URL\_LEN] | 许可证服务器的默认URL，用于获取媒体密钥。该URL由DRM解决方案提供，应用可使用此URL或自定义URL发送请求。数组长度由MAX\_DEFAULT\_URL\_LEN宏定义。 |
