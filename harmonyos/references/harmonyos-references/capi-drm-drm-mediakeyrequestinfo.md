---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drm-drm-mediakeyrequestinfo
title: DRM_MediaKeyRequestInfo
breadcrumb: API参考 > 媒体 > DRM Kit（数字版权保护服务） > C API > 结构体 > DRM_MediaKeyRequestInfo
category: harmonyos-references
scraped_at: 2026-09-02T15:02:29+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:bbf7c7b43dc273ab00a6aab6c4ffa079289d08a046a9f1fde24577631d00eca1
---

```c
typedef struct DRM_MediaKeyRequestInfo {...} DRM_MediaKeyRequestInfo
```

## 概述

媒体密钥请求信息。

**起始版本：** 11

**相关模块：** [Drm](capi-drm.md)

**所在头文件：** [native\_drm\_common.h](capi-native-drm-common-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| [DRM\_MediaKeyType](capi-native-drm-common-h.md#drm_mediakeytype) type | 媒体密钥类型，指定请求的密钥用途。取值为DRM\_MEDIA\_KEY\_TYPE\_STREAMING（在线流媒体）或DRM\_MEDIA\_KEY\_TYPE\_OFFLINE（离线播放）。 |
| int32\_t initDataLen | 初始化数据的长度，表示initData数组中有效数据的字节数。单位为字节（Byte），取值范围为[1, MAX\_INIT\_DATA\_LEN]。 |
| uint8\_t initData[MAX\_INIT\_DATA\_LEN] | 初始化数据，包含DRM内容保护系统特定头（PSSH）格式的数据。通常从媒体内容的PSSH box中提取，需进行base64解码后传入。数组长度由MAX\_INIT\_DATA\_LEN宏定义。 |
| char mimeType[MAX\_MIMETYPE\_LEN] | 媒体内容的MIME类型，用于标识媒体内容的格式。常见取值如"video/mp4"、"video/webm"等，具体支持类型由DRM解决方案决定。数组长度由MAX\_MIMETYPE\_LEN宏定义。 |
| uint32\_t optionsCount | 选项数据的数量，表示optionName和optionData数组中有效元素的个数。取值范围为[0, MAX\_MEDIA\_KEY\_REQUEST\_OPTION\_COUNT]。 |
| char optionName[MAX\_MEDIA\_KEY\_REQUEST\_OPTION\_COUNT][MAX\_MEDIA\_KEY\_REQUEST\_OPTION\_NAME\_LEN] | 选项名称数组，每行存储一个选项的名称。选项名称由DRM解决方案定义，用于传递特定的请求参数。数组维度由MAX\_MEDIA\_KEY\_REQUEST\_OPTION\_COUNT和MAX\_MEDIA\_KEY\_REQUEST\_OPTION\_NAME\_LEN宏定义。 |
| char optionData[MAX\_MEDIA\_KEY\_REQUEST\_OPTION\_COUNT][MAX\_MEDIA\_KEY\_REQUEST\_OPTION\_DATA\_LEN] | 选项数据数组，每行存储对应optionName的选项值。数组维度由MAX\_MEDIA\_KEY\_REQUEST\_OPTION\_COUNT和MAX\_MEDIA\_KEY\_REQUEST\_OPTION\_DATA\_LEN宏定义。 |
