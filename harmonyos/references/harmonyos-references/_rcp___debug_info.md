---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___debug_info
title: Rcp_DebugInfo
breadcrumb: API参考 > 系统 > 网络 > Remote Communication Kit（远场通信服务） > C API > 结构体 > Rcp_DebugInfo
category: harmonyos-references
scraped_at: 2026-04-28T08:09:01+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:241e4fb523a9d60397bf9e7cf45e8f7cb82d581b2f2d3d4507f266a7857dedb9
---

## 概述

PhonePC/2in1TabletTVWearable

描述存储在[Rcp\_Response](_rcp___response.md)中的调试信息的结构。

**起始版本：** 5.0.0(12)

**相关模块：** [RemoteCommunication](remote-communication-overview.md)

**所在头文件：** [rcp.h](rcp_8h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [Rcp\_DebugEvent](remote-communication-overview.md#rcp_debugevent)[type](_rcp___debug_info.md#type) | 调试事件类型。 |
| [Rcp\_Buffer](_rcp___buffer.md)[data](_rcp___debug_info.md#data) | 调试信息。 |
| struct [Rcp\_DebugInfo](_rcp___debug_info.md) \* [next](_rcp___debug_info.md#next) | 链式存储。指向下一个[Rcp\_DebugInfo](_rcp___debug_info.md)。 |

## 结构体成员变量说明

PhonePC/2in1TabletTVWearable

### data

PhonePC/2in1TabletTVWearable

```
1. Rcp_Buffer Rcp_DebugInfo::data
```

**描述**

调试信息。

### next

PhonePC/2in1TabletTVWearable

```
1. struct Rcp_DebugInfo* Rcp_DebugInfo::next
```

**描述**

链式存储。指向下一个[Rcp\_DebugInfo](_rcp___debug_info.md)。

### type

PhonePC/2in1TabletTVWearable

```
1. Rcp_DebugEvent Rcp_DebugInfo::type
```

**描述**

调试事件类型。
