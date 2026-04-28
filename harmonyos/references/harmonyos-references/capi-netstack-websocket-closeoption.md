---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netstack-websocket-closeoption
title: WebSocket_CloseOption
breadcrumb: API参考 > 系统 > 网络 > Network Kit（网络服务） > C API > 结构体 > WebSocket_CloseOption
category: harmonyos-references
scraped_at: 2026-04-28T08:08:38+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:175f5b584b9d43b5ba4f9cb3db55d608fad290302e486fa2ef6d1403cd2193ab
---

```
1. struct WebSocket_CloseOption {...}
```

## 概述

PhonePC/2in1TabletTVWearable

websocket客户端主动关闭的参数。

**起始版本：** 11

**相关模块：** [netstack](capi-netstack.md)

**所在头文件：** [net\_websocket\_type.h](capi-net-websocket-type-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| uint32\_t code | 错误值。 |
| const char \*reason | 错误原因。 |
