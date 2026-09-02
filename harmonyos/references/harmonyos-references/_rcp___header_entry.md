---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___header_entry
title: Rcp_HeaderEntry
breadcrumb: API参考 > 系统 > 网络 > Remote Communication Kit（远场通信服务） > C API > 结构体 > Rcp_HeaderEntry
category: harmonyos-references
scraped_at: 2026-09-02T15:01:59+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:12c645dfd65f5304e5c74258484f87a53d2ca59e344959bf2f5f396ad67116bd
---

## 概述

请求或响应的标头的所有键值对。

**起始版本：** 5.0.0(12)

**相关模块：** [RemoteCommunication](remote-communication-overview.md)

**所在头文件：** [rcp.h](rcp_8h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| char \* [key](_rcp___header_entry.md#key) | 键。如果用户希望使用自定义的content-type覆盖系统原有的content-type，键必须使用小写的“content-type”。 |
| [Rcp\_HeaderValue](_rcp___header_value.md) \* [value](_rcp___header_entry.md#value) | 值。 |
| struct [Rcp\_HeaderEntry](_rcp___header_entry.md) \* [next](_rcp___header_entry.md#next) | 链式存储。指向下一个键值对[Rcp\_HeaderEntry](_rcp___header_entry.md)。 |

## 结构体成员变量说明

### key

```cpp
char* Rcp_HeaderEntry::key
```

**描述**

键。如果用户希望使用自定义的content-type覆盖系统原有的content-type，键必须使用小写的“content-type”。

### next

```cpp
struct Rcp_HeaderEntry* Rcp_HeaderEntry::next
```

**描述**

链式存储。指向下一个键值对[Rcp\_HeaderEntry](_rcp___header_entry.md)。

### value

```cpp
Rcp_HeaderValue* Rcp_HeaderEntry::value
```

**描述**

标头键值对的值。
