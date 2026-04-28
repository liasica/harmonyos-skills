---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hiappevent-hiappevent-appeventgroup
title: HiAppEvent_AppEventGroup
breadcrumb: API参考 > 系统 > 调测调优 > Performance Analysis Kit（性能分析服务） > C API > 结构体 > HiAppEvent_AppEventGroup
category: harmonyos-references
scraped_at: 2026-04-28T08:11:24+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:3fa89de5f2d08925f98c627bbdd17416eaa8c8bf59b0fca3379764e66b1063f7
---

```
1. typedef struct HiAppEvent_AppEventGroup {...} HiAppEvent_AppEventGroup
```

## 概述

PhonePC/2in1TabletTVWearable

一组事件信息，包含事件组的名称，按名称分组的单个事件信息数组，事件数组的长度。

**起始版本：** 12

**相关模块：** [HiAppEvent](capi-hiappevent.md)

**所在头文件：** [hiappevent.h](capi-hiappevent-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| const char\* name | 事件数组中相同的事件名称。 |
| const struct HiAppEvent\_AppEventInfo\* appEventInfos | 具有相同事件名称的事件数组。 |
| uint32\_t infoLen | 具有相同事件名称的事件数组的长度。 |
