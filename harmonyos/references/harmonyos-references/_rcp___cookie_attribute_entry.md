---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___cookie_attribute_entry
title: Rcp_CookieAttributeEntry
breadcrumb: API参考 > 系统 > 网络 > Remote Communication Kit（远场通信服务） > C API > 结构体 > Rcp_CookieAttributeEntry
category: harmonyos-references
scraped_at: 2026-09-02T15:01:58+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:1bff5470784ecab839bf54407471b848f2fd45e22131a78e8ac05fde60eaacc8
---

## 概述

响应Cookie属性条目。

**起始版本：** 5.0.0(12)

**相关模块：** [RemoteCommunication](remote-communication-overview.md)

**所在头文件：** [rcp.h](rcp_8h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| const char \* [key](_rcp___cookie_attribute_entry.md#key) | 键。 |
| const char \* [value](_rcp___cookie_attribute_entry.md#value) | 值。 |
| struct [Rcp\_CookieAttributeEntry](_rcp___cookie_attribute_entry.md) \* [next](_rcp___cookie_attribute_entry.md#next) | 链式存储。指向下一个[Rcp\_CookieAttributeEntry](_rcp___cookie_attribute_entry.md)的指针。 |

## 结构体成员变量说明

### key

```cpp
const char* Rcp_CookieAttributeEntry::key
```

**描述**

键。

### next

```cpp
struct Rcp_CookieAttributeEntry* Rcp_CookieAttributeEntry::next
```

**描述**

链式存储。指向下一个[Rcp\_CookieAttributeEntry](_rcp___cookie_attribute_entry.md)的指针。

### value

```cpp
const char* Rcp_CookieAttributeEntry::value
```

**描述**

值。
