---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drm-drm-keysinfo
title: DRM_KeysInfo
breadcrumb: API参考 > 媒体 > DRM Kit（数字版权保护服务） > C API > 结构体 > DRM_KeysInfo
category: harmonyos-references
scraped_at: 2026-04-28T08:13:03+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:886c1de77ec34499101c77abf2a94200b42519143fbe6cade3c46cad563a5b6f
---

```
1. typedef struct DRM_KeysInfo {...} DRM_KeysInfo
```

## 概述

PhonePC/2in1TabletTVWearable

媒体密钥信息。

**起始版本：** 11

**相关模块：** [Drm](capi-drm.md)

**所在头文件：** [native\_drm\_common.h](capi-native-drm-common-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| uint32\_t keysInfoCount | 密钥计数。 |
| uint8\_t keyId[MAX\_KEY\_INFO\_COUNT][MAX\_KEY\_ID\_LEN] | 密钥ID集合。 |
| char statusValue[MAX\_KEY\_INFO\_COUNT][MAX\_KEY\_STATUS\_VALUE\_LEN] | 密钥状态值。 |
