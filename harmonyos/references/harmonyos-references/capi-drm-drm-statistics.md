---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drm-drm-statistics
title: DRM_Statistics
breadcrumb: API参考 > 媒体 > DRM Kit（数字版权保护服务） > C API > 结构体 > DRM_Statistics
category: harmonyos-references
scraped_at: 2026-09-02T15:02:29+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:6c44603fa0eedfe5b1d9de173b6325ea39c9056c91d49b43bfb39b3dac418e3d
---

```c
typedef struct DRM_Statistics {...} DRM_Statistics
```

## 概述

MediaKeySystem的统计信息。

**起始版本：** 11

**相关模块：** [Drm](capi-drm.md)

**所在头文件：** [native\_drm\_common.h](capi-native-drm-common-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| uint32\_t statisticsCount | 度量信息的数量，表示statisticsName和statisticsDescription数组中有效元素的个数。取值范围为[0, MAX\_STATISTICS\_COUNT]。 |
| char statisticsName[MAX\_STATISTICS\_COUNT][MAX\_STATISTICS\_NAME\_LEN] | 度量信息名称数组，每行存储一个度量项的名称，如"DecryptionOperations"（解密操作次数）、"KeySessions"（密钥会话数）等。数组维度由MAX\_STATISTICS\_COUNT和MAX\_STATISTICS\_NAME\_LEN宏定义。 |
| char statisticsDescription[MAX\_STATISTICS\_COUNT][MAX\_STATISTICS\_BUFFER\_LEN] | 度量信息描述数组，每行存储对应statisticsName的度量值。描述内容通常包含数值、百分比或其他格式的统计数据。数组维度由MAX\_STATISTICS\_COUNT和MAX\_STATISTICS\_BUFFER\_LEN宏定义。 |
