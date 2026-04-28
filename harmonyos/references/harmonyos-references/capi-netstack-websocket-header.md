---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netstack-websocket-header
title: WebSocket_Header
breadcrumb: API参考 > 系统 > 网络 > Network Kit（网络服务） > C API > 结构体 > WebSocket_Header
category: harmonyos-references
scraped_at: 2026-04-28T08:08:39+08:00
doc_updated_at: 2026-03-12
content_hash: sha256:fda7af01a877b11e2ef8bd206d228fe1a213a3dc5d1ccf93707f66d4c77cab33
---

```
1. struct WebSocket_Header {...}
```

## 概述

PhonePC/2in1TabletTVWearable

websocket客户端增加header的链表节点。

**起始版本：** 11

**相关模块：** [netstack](capi-netstack.md)

**所在头文件：** [net\_websocket\_type.h](capi-net-websocket-type-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| const char \*fieldName | header的字段名。 |
| const char \*fieldValue | header的字段内容。 |
| struct [WebSocket\_Header](capi-netstack-websocket-header.md) \*next | header链表的next指针。 |
