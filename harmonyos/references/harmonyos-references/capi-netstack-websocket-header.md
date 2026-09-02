---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netstack-websocket-header
title: WebSocket_Header
breadcrumb: API参考 > 系统 > 网络 > Network Kit（网络服务） > C API > 结构体 > WebSocket_Header
category: harmonyos-references
scraped_at: 2026-09-02T15:01:56+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:2a248c37f19637edc34e800579f6a8c41f67c1c7f47a4d02c46bb12243d1d5b2
---

```c
struct WebSocket_Header {...}
```

## 概述

WebSocket客户端增加header的链表节点。

**起始版本：** 11

**相关模块：** [netstack](capi-netstack.md)

**所在头文件：** [net\_websocket\_type.h](capi-net-websocket-type-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| const char \*fieldName | header的字段名。 |
| const char \*fieldValue | header的字段内容。 |
| struct [WebSocket\_Header](capi-netstack-websocket-header.md) \*next | header链表的next指针。 |
