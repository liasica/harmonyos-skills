---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hiappevent-hiappevent-externallog
title: OH_HiAppEvent_ExternalLog
breadcrumb: API参考 > 系统 > 调测调优 > Performance Analysis Kit（性能分析服务） > C API > 结构体 > OH_HiAppEvent_ExternalLog
category: harmonyos-references
scraped_at: 2026-11-12T09:56:16+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:42365db10b1faefd4eeb5d489af22ebde42304094559e904793aa26bd47f3503
---

```c
typedef struct OH_HiAppEvent_ExternalLog {...} OH_HiAppEvent_ExternalLog
```

## 概述

OH\_HiAppEvent\_ExternalLog结构体用于描述external\_log故障文件信息，包含文件路径，文件生成时间戳，文件大小和系统事件类型。

**起始版本：** 26.0.1

**相关模块：** [HiAppEvent](capi-hiappevent.md)

**所在头文件：** [hiappevent.h](capi-hiappevent-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| const char\* filePath | 故障文件路径。 |
| long long generationTs | 故障文件生成时间戳。 |
| long fileSize | 故障文件大小，单位KB。 |
| [OH\_HiAppEvent\_SysEvent](capi-hiappevent-h.md#oh_hiappevent_sysevent) event | 系统事件类型。 |
