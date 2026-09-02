---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-multimedia-drm-drmsubsample
title: DrmSubsample
breadcrumb: API参考 > 媒体 > AVCodec Kit（音视频编解码服务） > C API > 结构体 > DrmSubsample
category: harmonyos-references
scraped_at: 2026-09-02T15:02:23+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:f78bccaf7d1e14caab1873ede7dca1f44968a57b1a3edb875397224843871df7
---

```c
typedef struct DrmSubsample {...} DrmSubsample
```

## 概述

Subsample结构类型定义。

**起始版本：** 12

**相关模块：** [Multimedia\_Drm](capi-multimedia-drm.md)

**所在头文件：** [native\_cencinfo.h](capi-native-cencinfo-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| uint32\_t clearHeaderLen | 头部清流数据的长度。 |
| uint32\_t payLoadLen | 加密数据的长度。 |
