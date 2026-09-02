---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hiappevent-hiappevent-appeventgroup
title: HiAppEvent_AppEventGroup
breadcrumb: API参考 > 系统 > 调测调优 > Performance Analysis Kit（性能分析服务） > C API > 结构体 > HiAppEvent_AppEventGroup
category: harmonyos-references
scraped_at: 2026-09-02T15:02:16+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:c7c2b333e0c8ab10815cdaba258fa7989442d0ac61fd157f1a4c60ee102b64bf
---

```c
typedef struct HiAppEvent_AppEventGroup {...} HiAppEvent_AppEventGroup
```

## 概述

一组事件信息，用于管理和组织具有相同名称的事件信息。该结构体包含事件组的名称，按名称分组的单个事件信息数组，事件数组的长度。

**起始版本：** 12

**相关模块：** [HiAppEvent](capi-hiappevent.md)

**所在头文件：** [hiappevent.h](capi-hiappevent-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| const char\* name | 事件数组中相同的事件名称。 |
| const struct HiAppEvent\_AppEventInfo\* appEventInfos | 具有相同事件名称的事件数组。 |
| uint32\_t infoLen | 具有相同事件名称的事件数组的长度。 |
