---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hiappevent-hiappevent-appeventinfo
title: HiAppEvent_AppEventInfo
breadcrumb: API参考 > 系统 > 调测调优 > Performance Analysis Kit（性能分析服务） > C API > 结构体 > HiAppEvent_AppEventInfo
category: harmonyos-references
scraped_at: 2026-04-28T08:11:23+08:00
doc_updated_at: 2026-03-17
content_hash: sha256:d9d5b46ba7616bd4a817c33f0fb72f042a01afb92aa9bb6e1e4126e0df6ab9f6
---

```
1. typedef struct HiAppEvent_AppEventInfo {...} HiAppEvent_AppEventInfo
```

## 概述

PhonePC/2in1TabletTVWearable

单个事件信息，包含事件领域、事件名称、事件类型和事件携带的用json格式字符串表示的自定义参数列表。

**起始版本：** 12

**相关模块：** [HiAppEvent](capi-hiappevent.md)

**所在头文件：** [hiappevent.h](capi-hiappevent-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| const char\* domain | 事件领域。 |
| const char\* name | 事件名称。 |
| enum [EventType](capi-hiappevent-h.md#eventtype) type | 事件类型。 |
| const char\* params | json格式字符串类型的事件参数列表。 |
