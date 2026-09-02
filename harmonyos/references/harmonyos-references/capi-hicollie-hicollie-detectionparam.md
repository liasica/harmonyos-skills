---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hicollie-hicollie-detectionparam
title: HiCollie_DetectionParam
breadcrumb: API参考 > 系统 > 调测调优 > Performance Analysis Kit（性能分析服务） > C API > 结构体 > HiCollie_DetectionParam
category: harmonyos-references
scraped_at: 2026-09-02T15:02:16+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:9f2b4143ea630083bcb73478a19ff1e2268bde42e301bd5d62cf2b1fecb263f6
---

```c
typedef struct HiCollie_DetectionParam {...} HiCollie_DetectionParam
```

## 概述

检测业务线程卡顿的相关参数，可用于应用线程卡顿检测与分析等场景。请注意，从API version 12及以上支持。

**起始版本：** 12

**相关模块：** [HiCollie](capi-hicollie.md)

**所在头文件：** [hicollie.h](capi-hicollie-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| int sampleStackTriggerTime | 保留字段，用于后续功能扩展。 |
| int reserved | 保留字段，用于后续功能扩展。 |
