---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netstack-websocket-openresult
title: WebSocket_OpenResult
breadcrumb: API参考 > 系统 > 网络 > Network Kit（网络服务） > C API > 结构体 > WebSocket_OpenResult
category: harmonyos-references
scraped_at: 2026-09-02T15:01:56+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:aa9528319027df8e324e82ae9445c6ba9034589da4dff2e8f0613dc11f2bb60e
---

```c
struct WebSocket_OpenResult {...}
```

## 概述

WebSocket客户端来自服务端连接成功的参数。

**起始版本：** 11

**相关模块：** [netstack](capi-netstack.md)

**所在头文件：** [net\_websocket\_type.h](capi-net-websocket-type-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| uint32\_t code | WebSocket客户端连接成功码。 |
| const char \*reason | WebSocket客户端连接成功原因。 |
