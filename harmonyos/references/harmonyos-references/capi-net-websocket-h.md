---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-net-websocket-h
title: net_websocket.h
breadcrumb: API参考 > 系统 > 网络 > Network Kit（网络服务） > C API > 头文件 > net_websocket.h
category: harmonyos-references
scraped_at: 2026-04-28T08:08:34+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:498fd35d1a6545c00deb47c5183ecf17392e4ccffa90c71f1d5c3de1aa02ee45
---

## 概述

PhonePC/2in1TabletTVWearable

定义WebSocket客户端模块的接口。

**引用文件：** <network/netstack/net\_websocket.h>

**库：** libnet\_websocket.so

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 11

**相关模块：** [netstack](capi-netstack.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 函数

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [struct WebSocket \*OH\_WebSocketClient\_Constructor(WebSocket\_OnOpenCallback onOpen, WebSocket\_OnMessageCallback onMessage,WebSocket\_OnErrorCallback onError, WebSocket\_OnCloseCallback onclose)](capi-net-websocket-h.md#oh_websocketclient_constructor) | WebSocket客户端的构造函数。 |
| [int OH\_WebSocketClient\_AddHeader(struct WebSocket \*client, struct WebSocket\_Header header)](capi-net-websocket-h.md#oh_websocketclient_addheader) | 将header头信息添加到client客户端request中。 |
| [int OH\_WebSocketClient\_Connect(struct WebSocket \*client, const char \*url, struct WebSocket\_RequestOptions options)](capi-net-websocket-h.md#oh_websocketclient_connect) | 客户端连接服务端。 |
| [int OH\_WebSocketClient\_Send(struct WebSocket \*client, char \*data, size\_t length)](capi-net-websocket-h.md#oh_websocketclient_send) | 客户端向服务端发送数据。 |
| [int OH\_WebSocketClient\_Close(struct WebSocket \*client, struct WebSocket\_CloseOption options)](capi-net-websocket-h.md#oh_websocketclient_close) | 客户端主动关闭WebSocket连接。 |
| [int OH\_WebSocketClient\_Destroy(struct WebSocket \*client)](capi-net-websocket-h.md#oh_websocketclient_destroy) | 释放WebSocket连接上下文和资源。 |

## 函数说明

PhonePC/2in1TabletTVWearable

### OH\_WebSocketClient\_Constructor()

PhonePC/2in1TabletTVWearable

```
1. struct WebSocket *OH_WebSocketClient_Constructor(WebSocket_OnOpenCallback onOpen, WebSocket_OnMessageCallback onMessage,WebSocket_OnErrorCallback onError, WebSocket_OnCloseCallback onclose)
```

**描述**

WebSocket客户端的构造函数。

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [WebSocket\_OnOpenCallback](capi-net-websocket-type-h.md#websocket_onopencallback) onOpen | 客户端定义的建立连接消息的回调函数。 |
| [WebSocket\_OnMessageCallback](capi-net-websocket-type-h.md#websocket_onmessagecallback) onMessage | 客户端定义的接收消息的回调函数。 |
| [WebSocket\_OnErrorCallback](capi-net-websocket-type-h.md#websocket_onerrorcallback) onError | 客户端定义的错误消息的回调函数。 |
| [WebSocket\_OnCloseCallback](capi-net-websocket-type-h.md#websocket_onclosecallback) onclose | 客户端定义的关闭消息的回调函数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [struct WebSocket](capi-netstack-websocket.md) \* | 成功返回客户端指针，失败返回为NULL。 |

### OH\_WebSocketClient\_AddHeader()

PhonePC/2in1TabletTVWearable

```
1. int OH_WebSocketClient_AddHeader(struct WebSocket *client, struct WebSocket_Header header)
```

**描述**

将header头信息添加到client客户端request中。

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [struct WebSocket](capi-netstack-websocket.md) \*client | 客户端指针。 |
| [struct WebSocket\_Header](capi-netstack-websocket-header.md) header | Header头信息。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回值为0表示执行成功，返回值不为0表示失败。返回值详细信息可以查看OH\_Websocket\_ErrCode。 |

### OH\_WebSocketClient\_Connect()

PhonePC/2in1TabletTVWearable

```
1. int OH_WebSocketClient_Connect(struct WebSocket *client, const char *url, struct WebSocket_RequestOptions options)
```

**描述**

客户端连接服务端。

**系统能力：** SystemCapability.Communication.NetStack

**需要权限：** ohos.permission.INTERNET

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [struct WebSocket](capi-netstack-websocket.md) \*client | 客户端指针。 |
| const char \*url | 客户端要连接到服务端的地址。 |
| [struct WebSocket\_RequestOptions](capi-netstack-websocket-requestoptions.md) options | 发起连接的可选参数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回值为0表示执行成功，返回值不为0表示失败。返回值详细信息可以查看OH\_Websocket\_ErrCode。 |

### OH\_WebSocketClient\_Send()

PhonePC/2in1TabletTVWearable

```
1. int OH_WebSocketClient_Send(struct WebSocket *client, char *data, size_t length)
```

**描述**

客户端向服务端发送数据。

**系统能力：** SystemCapability.Communication.NetStack

**需要权限：** ohos.permission.INTERNET

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [struct WebSocket](capi-netstack-websocket.md) \*client | 客户端。 |
| char \*data | 客户端发送的数据。 |
| size\_t length | 客户端发送的数据长度。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回值为0表示执行成功，返回值不为0表示失败。返回值详细信息可以查看OH\_Websocket\_ErrCode。 |

### OH\_WebSocketClient\_Close()

PhonePC/2in1TabletTVWearable

```
1. int OH_WebSocketClient_Close(struct WebSocket *client, struct WebSocket_CloseOption options)
```

**描述**

客户端主动关闭WebSocket连接。

**系统能力：** SystemCapability.Communication.NetStack

**需要权限：** ohos.permission.INTERNET

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [struct WebSocket](capi-netstack-websocket.md) \*client | 客户端。 |
| [struct WebSocket\_CloseOption](capi-netstack-websocket-closeoption.md) options | 发起关闭连接的可选参数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回值为0表示执行成功，返回值不为0表示失败。返回值详细信息可以查看OH\_Websocket\_ErrCode。 |

### OH\_WebSocketClient\_Destroy()

PhonePC/2in1TabletTVWearable

```
1. int OH_WebSocketClient_Destroy(struct WebSocket *client)
```

**描述**

释放WebSocket连接上下文和资源。使用方式如下：

1. 调用[WebSocket\_OnCloseCallback](capi-net-websocket-type-h.md#websocket_onclosecallback)订阅WebSocket连接关闭事件，并在该回调函数中调用[OH\_WebSocketClient\_Destroy](capi-net-websocket-h.md#oh_websocketclient_destroy)方法。
2. 调用[OH\_WebSocketClient\_Close](capi-net-websocket-h.md#oh_websocketclient_close)关闭WebSocket连接。

注意

确保触发[WebSocket\_OnCloseCallback](capi-net-websocket-type-h.md#websocket_onclosecallback)回调后再调用该接口，否则系统内存资源被释放后可能出现socket泄露以及连接未关闭的情况。

**系统能力：** SystemCapability.Communication.NetStack

**需要权限：** ohos.permission.INTERNET

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [struct WebSocket](capi-netstack-websocket.md) \*client | 客户端。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回值为0表示执行成功，返回值不为0表示失败。返回值详细信息可以查看OH\_Websocket\_ErrCode。 |
