---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netstack-websocket
title: WebSocket
breadcrumb: API参考 > 系统 > 网络 > Network Kit（网络服务） > C API > 结构体 > WebSocket
category: harmonyos-references
scraped_at: 2026-04-28T08:08:38+08:00
doc_updated_at: 2026-03-12
content_hash: sha256:992bc357bb2b35bec5005ff910989c4c153d549db8c20afb4e48ebb8c584fa9b
---

```
1. struct WebSocket {...}
```

## 概述

PhonePC/2in1TabletTVWearable

WebSocket客户端结构体。

**起始版本：** 11

**相关模块：** [netstack](capi-netstack.md)

**所在头文件：** [net\_websocket\_type.h](capi-net-websocket-type-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [WebSocket\_OnOpenCallback](capi-net-websocket-type-h.md#websocket_onopencallback) onOpen | 客户端接收连接消息的回调指针。 |
| [WebSocket\_OnMessageCallback](capi-net-websocket-type-h.md#websocket_onmessagecallback) onMessage | 客户端接收消息的回调指针。 |
| [WebSocket\_OnErrorCallback](capi-net-websocket-type-h.md#websocket_onerrorcallback) onError | 客户端接收错误消息的回调指针。 |
| [WebSocket\_OnCloseCallback](capi-net-websocket-type-h.md#websocket_onclosecallback) onClose | 客户端接收关闭消息的回调指针。 |
| [WebSocket\_RequestOptions](capi-netstack-websocket-requestoptions.md) requestOptions | 客户端建立连接请求内容。 |
