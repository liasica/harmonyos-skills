---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hiappevent-hiappevent-appeventinfo
title: HiAppEvent_AppEventInfo
breadcrumb: API参考 > 系统 > 调测调优 > Performance Analysis Kit（性能分析服务） > C API > 结构体 > HiAppEvent_AppEventInfo
category: harmonyos-references
scraped_at: 2026-09-02T15:02:16+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:6894c6c02f11caf2d09ad79b9cd1ff0f4de107b7890246496f9d56558249a7b9
---

```c
typedef struct HiAppEvent_AppEventInfo {...} HiAppEvent_AppEventInfo
```

## 概述

单个事件信息，包含事件领域、事件名称、事件类型和事件携带的用json格式字符串表示的自定义参数列表。

**起始版本：** 12

**相关模块：** [HiAppEvent](capi-hiappevent.md)

**所在头文件：** [hiappevent.h](capi-hiappevent-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| const char\* domain | 事件领域。表示事件所属的业务领域或功能模块，用于事件分类和管理。 |
| const char\* name | 事件名称。与domain配合使用唯一标识具体的事件。 |
| enum [EventType](capi-hiappevent-h.md#eventtype) type | 事件类型。 |
| const char\* params | JSON格式字符串类型的事件参数列表。 |
