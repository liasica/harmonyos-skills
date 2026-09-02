---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___request_cookie_entry
title: Rcp_RequestCookieEntry
breadcrumb: API参考 > 系统 > 网络 > Remote Communication Kit（远场通信服务） > C API > 结构体 > Rcp_RequestCookieEntry
category: harmonyos-references
scraped_at: 2026-09-02T15:01:59+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:5a7ca9c10773212f35148ebd9ab8c8abb7311abe21e4712be4c0918b7700b44a
---

## 概述

描述请求的所有Cookie键值对。

**起始版本：** 5.0.0(12)

**相关模块：** [RemoteCommunication](remote-communication-overview.md)

**所在头文件：** [rcp.h](rcp_8h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| char \* [key](_rcp___request_cookie_entry.md#key) | 请求Cookie键值对的键。 |
| char \* [value](_rcp___request_cookie_entry.md#value) | 请求Cookie键值对的值。 |
| struct [Rcp\_RequestCookieEntry](_rcp___request_cookie_entry.md) \* [next](_rcp___request_cookie_entry.md#next) | 链式存储。指向下一个[Rcp\_RequestCookieEntry](_rcp___request_cookie_entry.md)的指针。 |

## 结构体成员变量说明

### key

```cpp
char* Rcp_RequestCookieEntry::key
```

**描述**

请求Cookie键值对的键。

### next

```cpp
struct Rcp_RequestCookieEntry* Rcp_RequestCookieEntry::next
```

**描述**

链式存储。指向下一个[Rcp\_RequestCookieEntry](_rcp___request_cookie_entry.md)的指针。

### value

```cpp
char* Rcp_RequestCookieEntry::value
```

**描述**

请求Cookie键值对的值。
