---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netstack-websocket-errorresult
title: WebSocket_ErrorResult
breadcrumb: API参考 > 系统 > 网络 > Network Kit（网络服务） > C API > 结构体 > WebSocket_ErrorResult
category: harmonyos-references
scraped_at: 2026-04-28T08:08:38+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:371ba7b25754c22a35a833d45a31ff5ce5659e9d48d07b03f2bde708b49a6bce
---

```
1. struct WebSocket_ErrorResult {...}
```

## 概述

PhonePC/2in1TabletTVWearable

websocket客户端来自服务端连接错误的参数。

**起始版本：** 11

**相关模块：** [netstack](capi-netstack.md)

**所在头文件：** [net\_websocket\_type.h](capi-net-websocket-type-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| uint32\_t errorCode | 错误码。 |
| const char \*errorMessage | 错误的消息。 |
