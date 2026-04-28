---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drm-drm-mediakeyrequestinfo
title: DRM_MediaKeyRequestInfo
breadcrumb: API参考 > 媒体 > DRM Kit（数字版权保护服务） > C API > 结构体 > DRM_MediaKeyRequestInfo
category: harmonyos-references
scraped_at: 2026-04-28T08:13:02+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:49a09b98146a427202994cc652bab65935d2a20884f8dc640ba0c97f20dd98fa
---

```
1. typedef struct DRM_MediaKeyRequestInfo {...} DRM_MediaKeyRequestInfo
```

## 概述

PhonePC/2in1TabletTVWearable

媒体密钥请求信息。

**起始版本：** 11

**相关模块：** [Drm](capi-drm.md)

**所在头文件：** [native\_drm\_common.h](capi-native-drm-common-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [DRM\_MediaKeyType](capi-native-drm-common-h.md#drm_mediakeytype) type | 密钥类型。 |
| int32\_t initDataLen | 初始数据长度。 |
| uint8\_t initData[MAX\_INIT\_DATA\_LEN] | base64解码后格式为PSSH的初始数据。 |
| char mimeType[MAX\_MIMETYPE\_LEN] | 媒体上下文的MIME类型。 |
| uint32\_t optionsCount | 选项数据计数。 |
| char optionName[MAX\_MEDIA\_KEY\_REQUEST\_OPTION\_COUNT][MAX\_MEDIA\_KEY\_REQUEST\_OPTION\_NAME\_LEN] | 选项名称集合。 |
| char optionData[MAX\_MEDIA\_KEY\_REQUEST\_OPTION\_COUNT][MAX\_MEDIA\_KEY\_REQUEST\_OPTION\_DATA\_LEN] | 选项数据集合。 |
