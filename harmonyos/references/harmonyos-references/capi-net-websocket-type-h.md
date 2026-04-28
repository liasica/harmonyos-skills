---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-net-websocket-type-h
title: net_websocket_type.h
breadcrumb: API参考 > 系统 > 网络 > Network Kit（网络服务） > C API > 头文件 > net_websocket_type.h
category: harmonyos-references
scraped_at: 2026-04-28T08:08:33+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:bda73f1c263824753209f9a9e0c837af3d1527ef760a65cb6994d75f54f5f8fb
---

## 概述

PhonePC/2in1TabletTVWearable

定义websocket客户端模块的C接口需要的数据结构。

**引用文件：** <network/netstack/net\_websocket\_type.h>

**库：** libnet\_websocket.so

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 11

**相关模块：** [netstack](capi-netstack.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 结构体

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [WebSocket\_CloseResult](capi-netstack-websocket-closeresult.md) | websocket客户端来自服务端关闭的参数。 |
| [WebSocket\_CloseOption](capi-netstack-websocket-closeoption.md) | websocket客户端主动关闭的参数。 |
| [WebSocket\_ErrorResult](capi-netstack-websocket-errorresult.md) | websocket客户端来自服务端连接错误的参数。 |
| [WebSocket\_OpenResult](capi-netstack-websocket-openresult.md) | websocket客户端来自服务端连接成功的参数。 |
| [WebSocket\_Header](capi-netstack-websocket-header.md) | websocket客户端增加header头的链表节点。 |
| [WebSocket\_RequestOptions](capi-netstack-websocket-requestoptions.md) | webSocket客户端和服务端建立连接的参数。 |
| [WebSocket](capi-netstack-websocket.md) | webSocket客户端结构体。 |

### 函数

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [typedef void (\*WebSocket\_OnOpenCallback)(struct WebSocket \*client, WebSocket\_OpenResult openResult)](capi-net-websocket-type-h.md#websocket_onopencallback) | WebSocket\_OnOpenCallback | websocket客户端接收open消息的回调函数定义。 |
| [typedef void (\*WebSocket\_OnMessageCallback)(struct WebSocket \*client, char \*data, uint32\_t length)](capi-net-websocket-type-h.md#websocket_onmessagecallback) | WebSocket\_OnMessageCallback | websocket客户端接收数据的回调函数定义。 |
| [typedef void (\*WebSocket\_OnErrorCallback)(struct WebSocket \*client, WebSocket\_ErrorResult errorResult)](capi-net-websocket-type-h.md#websocket_onerrorcallback) | WebSocket\_OnErrorCallback | websocket客户端接收error错误消息的回调函数定义。 |
| [typedef void (\*WebSocket\_OnCloseCallback)(struct WebSocket \*client, WebSocket\_CloseResult closeResult)](capi-net-websocket-type-h.md#websocket_onclosecallback) | WebSocket\_OnCloseCallback | webSocket客户端接收close消息的回调函数定义。 |

## 枚举类型说明

PhonePC/2in1TabletTVWearable

### WebSocket\_ErrCode

PhonePC/2in1TabletTVWearable

```
1. enum WebSocket_ErrCode
```

**描述**

定义websocket请求的错误码。

**起始版本：** 11

| 枚举项 | 描述 |
| --- | --- |
| WEBSOCKET\_OK = 0 | 操作成功。 |
| E\_BASE = 1000 | 错误码基准值。 |
| WEBSOCKET\_CLIENT\_NULL = (E\_BASE + 1) | websocket客户端为空。 |
| WEBSOCKET\_CLIENT\_NOT\_CREATED = (E\_BASE + 2) | websocket客户端未创建。 |
| WEBSOCKET\_CONNECTION\_ERROR = (E\_BASE + 3) | 建立websocket连接时发生错误。 |
| WEBSOCKET\_CONNECTION\_PARSE\_URL\_ERROR = (E\_BASE + 5) | 解析websocket连接参数时出错。 |
| WEBSOCKET\_CONNECTION\_NO\_MEMORY = (E\_BASE + 6) | websocket客户端建立连接过程中内存不足。 |
| WEBSOCKET\_CONNECTION\_CLOSED\_BY\_PEER = (E\_BASE + 7) | websocket连接被对端关闭。 |
| WEBSOCKET\_DESTROYED = (E\_BASE + 8) | websocket连接断开。 |
| WEBSOCKET\_PROTOCOL\_ERROR = (E\_BASE + 9) | 协议错误。 |
| WEBSOCKET\_SEND\_NO\_MEMORY = (E\_BASE + 10) | websocket客户端发送数据时系统内存不足。 |
| WEBSOCKET\_SEND\_DATA\_NULL = (E\_BASE + 11) | 发送数据为空。 |
| WEBSOCKET\_DATA\_LENGTH\_EXCEEDED = (E\_BASE + 12) | 发送数据长度超出限制。 |
| WEBSOCKET\_QUEUE\_LENGTH\_EXCEEDED = (E\_BASE + 13) | 发送数据队列长度超出限制。 |
| WEBSOCKET\_NO\_CLIENT\_CONTEXT = (E\_BASE + 14) | websocket客户端的上下文为空。 |
| WEBSOCKET\_NO\_HEADER\_CONTEXT = (E\_BASE + 15) | webSocket客户端协议头为空。 |
| WEBSOCKET\_HEADER\_EXCEEDED = (E\_BASE + 16) | webSocket客户端协议头超出限制。 |
| WEBSOCKET\_NO\_CONNECTION = (E\_BASE + 17) | websocket客户端未连接。 |
| WEBSOCKET\_NO\_CONNECTION\_CONTEXT = (E\_BASE + 18) | 释放websocket连接上下文时无相应上下文。 |

## 函数说明

PhonePC/2in1TabletTVWearable

### WebSocket\_OnOpenCallback()

PhonePC/2in1TabletTVWearable

```
1. typedef void (*WebSocket_OnOpenCallback)(struct WebSocket *client, WebSocket_OpenResult openResult)
```

**描述**

websocket客户端接收open消息的回调函数定义。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [struct WebSocket](capi-netstack-websocket.md) \*client | websocket客户端。 |
| [WebSocket\_OpenResult](capi-netstack-websocket-openresult.md) openResult | websocket客户端接收建立连接消息的内容。 |

### WebSocket\_OnMessageCallback()

PhonePC/2in1TabletTVWearable

```
1. typedef void (*WebSocket_OnMessageCallback)(struct WebSocket *client, char *data, uint32_t length)
```

**描述**

websocket客户端接收数据的回调函数定义。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [struct WebSocket](capi-netstack-websocket.md) \*client | websocket客户端。 |
| char \*data | websocket客户端接收的数据。 |
| uint32\_t length | websocket客户端接收的数据长度。 |

### WebSocket\_OnErrorCallback()

PhonePC/2in1TabletTVWearable

```
1. typedef void (*WebSocket_OnErrorCallback)(struct WebSocket *client, WebSocket_ErrorResult errorResult)
```

**描述**

websocket客户端接收error错误消息的回调函数定义。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [struct WebSocket](capi-netstack-websocket.md) \*client | websocket客户端。 |
| [WebSocket\_ErrorResult](capi-netstack-websocket-errorresult.md) errorResult | websocket客户端接收连接错误消息的内容。 |

### WebSocket\_OnCloseCallback()

PhonePC/2in1TabletTVWearable

```
1. typedef void (*WebSocket_OnCloseCallback)(struct WebSocket *client, WebSocket_CloseResult closeResult)
```

**描述**

webSocket客户端接收close消息的回调函数定义。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [struct WebSocket](capi-netstack-websocket.md) \*client | websocket客户端。 |
| [WebSocket\_CloseResult](capi-netstack-websocket-closeresult.md) closeResult | webSocket客户端接收关闭消息的内容。 |
