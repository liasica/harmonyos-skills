---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drm-drm-psshinfo
title: DRM_PsshInfo
breadcrumb: API参考 > 媒体 > DRM Kit（数字版权保护服务） > C API > 结构体 > DRM_PsshInfo
category: harmonyos-references
scraped_at: 2026-09-02T15:02:29+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:439820f5a5564c0049c8b65d5afeb209db5b0889c66e6e0590a61a2406a1de51
---

```c
typedef struct DRM_PsshInfo {...} DRM_PsshInfo
```

## 概述

DRM内容保护系统专用头（Protection System Specific Header）信息。

**起始版本：** 11

**相关模块：** [Drm](capi-drm.md)

**所在头文件：** [native\_drm\_common.h](capi-native-drm-common-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| uint8\_t uuid[DRM\_UUID\_LEN] | DRM系统的UUID（通用唯一标识符），用于唯一标识一个DRM内容保护系统。UUID长度为16字节，由DRM解决方案提供商分配。 |
| int32\_t dataLen | PSSH数据的长度，表示data数组中有效数据的字节数。单位为字节（Byte），取值范围为[0, MAX\_PSSH\_DATA\_LEN]。 |
| uint8\_t data[MAX\_PSSH\_DATA\_LEN] | PSSH数据，包含DRM系统特定的初始化数据。数据格式通常包含密钥ID、内容ID等信息。数组长度由MAX\_PSSH\_DATA\_LEN宏定义。 |
