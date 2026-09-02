---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netstack-websocket-errorresult
title: WebSocket_ErrorResult
breadcrumb: API参考 > 系统 > 网络 > Network Kit（网络服务） > C API > 结构体 > WebSocket_ErrorResult
category: harmonyos-references
scraped_at: 2026-09-02T15:01:56+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:01e5b19c564a8e28be68a3a901f15bc4d17922d751c67a804175917006bdfb3d
---

```c
struct WebSocket_ErrorResult {...}
```

## 概述

WebSocket客户端来自服务端连接错误的参数。

**起始版本：** 11

**相关模块：** [netstack](capi-netstack.md)

**所在头文件：** [net\_websocket\_type.h](capi-net-websocket-type-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| uint32\_t errorCode | 错误码。 |
| const char \*errorMessage | 错误的消息。 |
