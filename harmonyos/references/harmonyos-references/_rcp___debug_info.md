---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___debug_info
title: Rcp_DebugInfo
breadcrumb: API参考 > 系统 > 网络 > Remote Communication Kit（远场通信服务） > C API > 结构体 > Rcp_DebugInfo
category: harmonyos-references
scraped_at: 2026-09-02T15:01:58+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:1643d4e238217a77ddb952d9f93afcd7c90a862fe2b07a92f8efd272ea4c0c1e
---

## 概述

描述存储在[Rcp\_Response](_rcp___response.md)中的调试信息的结构。

**起始版本：** 5.0.0(12)

**相关模块：** [RemoteCommunication](remote-communication-overview.md)

**所在头文件：** [rcp.h](rcp_8h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| [Rcp\_DebugEvent](remote-communication-overview.md#rcp_debugevent) [type](_rcp___debug_info.md#type) | 调试事件类型。 |
| [Rcp\_Buffer](_rcp___buffer.md) [data](_rcp___debug_info.md#data) | 调试信息。 |
| struct [Rcp\_DebugInfo](_rcp___debug_info.md) \* [next](_rcp___debug_info.md#next) | 链式存储。指向下一个[Rcp\_DebugInfo](_rcp___debug_info.md)。 |

## 结构体成员变量说明

### data

```cpp
Rcp_Buffer Rcp_DebugInfo::data
```

**描述**

调试信息。

### next

```cpp
struct Rcp_DebugInfo* Rcp_DebugInfo::next
```

**描述**

链式存储。指向下一个[Rcp\_DebugInfo](_rcp___debug_info.md)。

### type

```cpp
Rcp_DebugEvent Rcp_DebugInfo::type
```

**描述**

调试事件类型。
