---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netstack-websocket-openresult
title: WebSocket_OpenResult
breadcrumb: API参考 > 系统 > 网络 > Network Kit（网络服务） > C API > 结构体 > WebSocket_OpenResult
category: harmonyos-references
scraped_at: 2026-04-28T08:08:38+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:3cac0e5300c50bbdabfe09d6d15fffb21a8dd4ec19e1888987b93ad486fa7283
---

```
1. struct WebSocket_OpenResult {...}
```

## 概述

PhonePC/2in1TabletTVWearable

websocket客户端来自服务端连接成功的参数。

**起始版本：** 11

**相关模块：** [netstack](capi-netstack.md)

**所在头文件：** [net\_websocket\_type.h](capi-net-websocket-type-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| uint32\_t code | websocket客户端连接成功码。 |
| const char \*reason | websocket客户端连接成功原因。 |
