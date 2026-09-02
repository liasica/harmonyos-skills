---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/rcp_quic_h
title: rcp_quic.h
breadcrumb: API参考 > 系统 > 网络 > Remote Communication Kit（远场通信服务） > C API > 头文件 > rcp_quic.h
category: harmonyos-references
scraped_at: 2026-09-02T15:01:57+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:9d3fc736515f1a1c0dff39ac12fae27af2db37a2ed329a8067d488b655ddc021
---

## 概述

声明quic协议相关的API。提供基本的函数、结构体和const定义。

**引用文件：** <RemoteCommunicationKit/rcp\_quic.h>

**库：** librcp\_quic.so

**系统能力：** SystemCapability.Collaboration.RemoteCommunication

**起始版本：** 26.0.0

**相关模块：** [RemoteCommunication](remote-communication-overview.md)

## 汇总

### 结构体

| 名称 | 描述 |
| --- | --- |
| struct [Rcp\_QuicSlist](_rcp___quic_slist.md) | 链表数据结构。 |
| struct [Rcp\_QuicIpAddress](_rcp___quic_ipaddress.md) | 用于存储IP地址的数据结构。 |
| struct [Rcp\_QuicIoVec](_rcp___quic_io_vec.md) | 用于存储二进制内容的数据结构。 |
| struct [Rcp\_QuicStreamData](_rcp___quic_stream_data.md) | quic连接中用于接收流式数据的存储结构。 |

### 宏定义

| 名称 | 描述 |
| --- | --- |
| [RCP\_QUIC\_IP\_MAX\_LEN](remote-communication-overview.md#rcp_quic_ip_max_len) 40 | quic连接的IP地址的最大长度。 |

### 类型定义

| 名称 | 描述 |
| --- | --- |
| typedef void [Rcp\_QuicConn](remote-communication-overview.md#rcp_quicconn) | quic连接实例的类型。 |
| typedef void [Rcp\_QuicSession](remote-communication-overview.md#rcp_quicsession) | quic会话的类型，可以管理多个连接实例。 |
| typedef struct [Rcp\_QuicSlist](_rcp___quic_slist.md) [Rcp\_QuicSlist](remote-communication-overview.md#rcp_quicslist) | 链表数据结构。 |
| typedef enum [RCP\_QuicIpResolve](remote-communication-overview.md#rcp_quicipresolve) [RCP\_QuicIpResolve](remote-communication-overview.md#rcp_quicipresolve) | 请求DNS解析时使用的IP解析类型。 |
| typedef struct [Rcp\_QuicIpAddress](_rcp___quic_ipaddress.md) [Rcp\_QuicIpAddress](remote-communication-overview.md#rcp_quicipaddress) | 用于存储IP地址的数据结构。 |
| typedef [Rcp\_QuicIpAddress](_rcp___quic_ipaddress.md) (\*[Rcp\_QuicDynamicDnsRuleFunction](remote-communication-overview.md#rcp_quicdynamicdnsrulefunction)) ([Rcp\_QuicConn](remote-communication-overview.md#rcp_quicconn) \*conn, void \*userObject, const char \*host, uint16\_t port) | 自定义DNS解析回调函数，根据主机名和端口返回IP地址。 |
| typedef enum [Rcp\_QuicConnOpt](remote-communication-overview.md#rcp_quicconnopt) | quic连接选项类型，用于配置连接的各种参数和回调函数。 |
| typedef enum [Rcp\_QuicStreamOpt](remote-communication-overview.md#rcp_quicstreamopt) | quic流选项类型，用于配置流的各种参数和回调函数。 |
| typedef enum [Rcp\_QuicConnInfo](remote-communication-overview.md#rcp_quicconninfo) | quic连接信息类型。用于查询连接的各种信息。 |
| typedef enum [Rcp\_QuicStreamInfo](remote-communication-overview.md#rcp_quicstreaminfo) | quic流信息类型。用于查询流的各种信息。 |
| typedef enum [Rcp\_QuicErrorCode](remote-communication-overview.md#rcp_quicerrorcode) | quic请求中可能出现的错误码。 |
| typedef enum [Rcp\_QuicStreamDirection](remote-communication-overview.md#rcp_quicstreamdirection) | quic流的方向类型。 |
| typedef enum [Rcp\_QuicStreamShutdown](remote-communication-overview.md#rcp_quicstreamshutdown) | quic流的关闭操作的类型。用于指定关闭流的读或写方向。 |
| typedef struct [Rcp\_QuicIoVec](_rcp___quic_io_vec.md) [Rcp\_QuicIoVec](remote-communication-overview.md#rcp_quiciovec) | 用于存储二进制内容的数据结构。 |
| typedef struct [Rcp\_QuicStreamData](_rcp___quic_stream_data.md) [Rcp\_QuicStreamData](remote-communication-overview.md#rcp_quicstreamdata) | quic连接中用于接收流式数据的存储结构。 |
| typedef [Rcp\_QuicErrorCode](remote-communication-overview.md#rcp_quicerrorcode) (\*[Rcp\_QuicConnectionOnCertAuthority](remote-communication-overview.md#rcp_quicconnectiononcertauthority)) ([Rcp\_QuicConn](remote-communication-overview.md#rcp_quicconn) \*conn, void \*userObject, const unsigned char \*const \*certs, const size\_t \*certLens, size\_t certsCount) | 证书校验的回调函数。在quic建链时，用于自定义校验对端证书。 |
| typedef void (\*[Rcp\_QuicConnectionOnSessionTicketUpdate](remote-communication-overview.md#rcp_quicconnectiononsessionticketupdate)) ([Rcp\_QuicConn](remote-communication-overview.md#rcp_quicconn) \*conn, void \*userObject, const char \*sessionTicket, size\_t length) | quic会话票据更新回调函数。在quic会话中票据更新时触发，返回新的票据。仅客户端触发。 |
| typedef void (\*[Rcp\_QuicConnectionOnConnected](remote-communication-overview.md#rcp_quicconnectiononconnected)) ([Rcp\_QuicConn](remote-communication-overview.md#rcp_quicconn) \*conn, void \*userObject) | quic连接成功回调函数。quic连接成功建立时触发该函数。 |
| typedef void (\*[Rcp\_QuicConnectionOnError](remote-communication-overview.md#rcp_quicconnectiononerror)) ([Rcp\_QuicConn](remote-communication-overview.md#rcp_quicconn) \*conn, void \*userObject, [Rcp\_QuicErrorCode](remote-communication-overview.md#rcp_quicerrorcode) errCode, const char \*errDetail) | quic连接失败回调函数。quic连接建立失败时触发该函数，返回失败原因。 |
| typedef void (\*[Rcp\_QuicConnectionOnClosed](remote-communication-overview.md#rcp_quicconnectiononclosed)) ([Rcp\_QuicConn](remote-communication-overview.md#rcp_quicconn) \*conn, void \*userObject) | quic连接关闭回调函数。quic连接关闭时触发，通知连接已关闭。 |
| typedef void (\*[Rcp\_QuicConnectionOnStreamInbound](remote-communication-overview.md#rcp_quicconnectiononstreaminbound)) ([Rcp\_QuicConn](remote-communication-overview.md#rcp_quicconn) \*conn, void \*userObject, uint64\_t streamId) | quic连接中入站流回调函数。当quic连接中对端创建流时触发，处理对端发起的流，设置流的选项和回调。 |
| typedef void (\*[Rcp\_QuicStreamOnEvent](remote-communication-overview.md#rcp_quicstreamonevent)) ([Rcp\_QuicConn](remote-communication-overview.md#rcp_quicconn) \*conn, void \*userObject, uint64\_t streamId, [Rcp\_QuicErrorCode](remote-communication-overview.md#rcp_quicerrorcode) errCode, const char \*errDetail) | quic连接中流事件回调函数。当quic连接中的流发生事件时触发，用于处理流的状态变化和错误。 |
| typedef uint64\_t (\*[Rcp\_QuicStreamOnReceiveData](remote-communication-overview.md#rcp_quicstreamonreceivedata)) ([Rcp\_QuicConn](remote-communication-overview.md#rcp_quicconn) \*conn, void \*userObject, uint64\_t streamId, const [Rcp\_QuicStreamData](remote-communication-overview.md#rcp_quicstreamdata) \*streamData) | quic连接中流数据接收回调函数。当quic连接中接收到流数据时触发，用于处理接收到的数据。 |

### 枚举

| 名称 | 描述 |
| --- | --- |
| [RCP\_QuicIpResolve](remote-communication-overview.md#rcp_quicipresolve) {  RCP\_QUIC\_IP\_RESOLVE\_WHATEVER = 0, RCP\_QUIC\_IP\_RESOLVE\_V4, RCP\_QUIC\_IP\_RESOLVE\_V6  } | 请求DNS解析时使用的IP解析类型。 |
| [Rcp\_QuicConnOpt](remote-communication-overview.md#rcp_quicconnopt) { RCP\_QUIC\_CONN\_IP\_ADDRESS = 0, RCP\_QUIC\_CONN\_IP\_RESOLVE, RCP\_QUIC\_CONN\_DNS\_FUNCTION, RCP\_QUIC\_CONN\_ON\_CONNECTED\_FUNCTION, RCP\_QUIC\_CONN\_ON\_ERROR\_FUNCTION, RCP\_QUIC\_CONN\_ON\_CLOSED\_FUNCTION, RCP\_QUIC\_CONN\_STREAM\_INBOUND\_FUNCTION, RCP\_QUIC\_CONN\_CONNECT\_TIMEOUT\_MS, RCP\_QUIC\_CONN\_IDLE\_TIMEOUT\_MS, RCP\_QUIC\_TLS\_CERT\_AUTHORITY\_FUNCTION = 1000, RCP\_QUIC\_TLS\_CERT\_AUTHORITY\_CONTENT, RCP\_QUIC\_TLS\_SESSION\_TICKET\_UPDATE\_FUNCTION, RCP\_QUIC\_TLS\_SESSION\_TICKET\_CONTENT, RCP\_QUIC\_TP\_INITIAL\_MAX\_BIDIRECTIONAL\_STREAMS = 2000, RCP\_QUIC\_TP\_INITIAL\_MAX\_DATA, RCP\_QUIC\_TP\_INITIAL\_MAX\_STREAMDATA\_BIDIRECTIONAL\_LOCAL, RCP\_QUIC\_TP\_INITIAL\_MAX\_STREAMDATA\_BIDIRECTIONAL\_REMOTE, RCP\_QUIC\_TP\_INITIAL\_MAX\_STREAMDATA\_UNIDIRECTIONAL, RCP\_QUIC\_TP\_INITIAL\_MAX\_UNIDIRECTIONAL\_STREAMS} | quic连接选项类型。 |
| [Rcp\_QuicStreamOpt](remote-communication-overview.md#rcp_quicstreamopt) { RCP\_QUIC\_STREAM\_EVENT\_FUNCTION = 0, RCP\_QUIC\_STREAM\_DATA\_FUNCTION, RCP\_QUIC\_INBOUND\_STREAM\_USER\_OBJECT, RCP\_QUIC\_STREAM\_SND\_BUFFER\_SIZE\_KB} | quic连接中配置流选项。 |
| [Rcp\_QuicConnInfo](remote-communication-overview.md#rcp_quicconninfo) { RCP\_INFO\_CONN\_GET\_LOCALADDR = 0, RCP\_INFO\_CONN\_GET\_PEERADDR, RCP\_INFO\_CONN\_DNS\_TIME\_MS, RCP\_INFO\_CONN\_CONNECT\_TIME\_MS, RCP\_INFO\_CONN\_SCID, RCP\_INFO\_CONN\_DCID } | quic连接中的信息类型。 |
| [Rcp\_QuicStreamInfo](remote-communication-overview.md#rcp_quicstreaminfo) { RCP\_INFO\_STREAM\_SND\_BUFFER\_SIZE\_KB = 0 } | quic流中的信息类型。 |
| [Rcp\_QuicErrorCode](remote-communication-overview.md#rcp_quicerrorcode) { RCP\_QUIC\_ERROR\_CODE\_SUCCESS = 0, RCP\_QUIC\_PERMISSION\_DENIED = 201, RCP\_QUIC\_ERROR\_CODE\_FAILED = 1007920001, RCP\_QUIC\_ERROR\_CODE\_INVALID\_PARAM = 1007920002, RCP\_QUIC\_ERROR\_CODE\_INVALID\_STATE = 1007920003, RCP\_QUIC\_ERROR\_CODE\_OUT\_OF\_MEM = 1007920004, RCP\_QUIC\_ERROR\_CODE\_CLOSE\_FROM\_PEER = 1007920005, RCP\_QUIC\_ERROR\_CODE\_HANDSHAKE\_TIMEOUT = 1007920006, RCP\_QUIC\_ERROR\_CODE\_NETWORK\_IDLE\_TIMEOUT = 1007920007, RCP\_QUIC\_ERROR\_INVALID\_FRAME = 1007920008, RCP\_QUIC\_ERROR\_CODE\_SEND\_PENDING = 1007920009, RCP\_QUIC\_ERROR\_CODE\_FINALIZE\_PENDING = 1007920010, RCP\_QUIC\_ERROR\_CODE\_NETWORK\_UNREACHABLE = 1007920011, RCP\_QUIC\_ERROR\_CODE\_ENCRYPT\_ERROR = 1007920012, RCP\_QUIC\_ERROR\_CODE\_BUFFER\_TOO\_SMALL = 1007920013, RCP\_QUIC\_ERROR\_CODE\_EAGAIN = 1007920015, RCP\_QUIC\_ERROR\_CODE\_STREAM\_CLOSED = 1007920018, RCP\_QUIC\_ERROR\_CODE\_STREAM\_RESET\_RECEIVED = 1007920019, RCP\_QUIC\_ERROR\_CODE\_STREAM\_STOP\_SENDING\_RECEIVED = 1007920020 } | quic请求中可能出现的错误码。 |
| [Rcp\_QuicStreamDirection](remote-communication-overview.md#rcp_quicstreamdirection) { RCP\_QUIC\_STREAM\_BIDI = 0, RCP\_QUIC\_STREAM\_UNI } | quic流的方向类型。 |
| [Rcp\_QuicStreamShutdown](remote-communication-overview.md#rcp_quicstreamshutdown) { RCP\_QUIC\_STREAM\_SHUTDOWN\_READ = 1, RCP\_QUIC\_STREAM\_SHUTDOWN\_WRITE = 2 } | quic流的关闭操作的类型。用于指定关闭流的读或写方向。 |

### 函数

| 名称 | 描述 |
| --- | --- |
| [Rcp\_QuicErrorCode](remote-communication-overview.md#rcp_quicerrorcode) [HMS\_Rcp\_QuicConnSetOpt](remote-communication-overview.md#hms_rcp_quicconnsetopt) ([Rcp\_QuicConn](remote-communication-overview.md#rcp_quicconn) \*conn, [Rcp\_QuicConnOpt](remote-communication-overview.md#rcp_quicconnopt) opt, const void \*optVal, uint32\_t optLen) | 设置quic连接选项。用于设置连接的各种参数和回调函数。 |
| [Rcp\_QuicErrorCode](remote-communication-overview.md#rcp_quicerrorcode) [HMS\_Rcp\_QuicConnGetInfo](remote-communication-overview.md#hms_rcp_quicconngetinfo) ([Rcp\_QuicConn](remote-communication-overview.md#rcp_quicconn) \*conn, [Rcp\_QuicConnInfo](remote-communication-overview.md#rcp_quicconninfo) info, void \*infoVal, uint32\_t \*infoLen) | 获取quic连接信息。用于建立quic连接成功后，获取相关quic连接信息。 |
| [Rcp\_QuicErrorCode](remote-communication-overview.md#rcp_quicerrorcode) [HMS\_Rcp\_QuicStreamSetOpt](remote-communication-overview.md#hms_rcp_quicstreamsetopt) ([Rcp\_QuicConn](remote-communication-overview.md#rcp_quicconn) \*conn, uint64\_t streamId, [Rcp\_QuicStreamOpt](remote-communication-overview.md#rcp_quicstreamopt) opt, const void \*optVal, uint32\_t optLen) | 设置quic连接中流的参数。 |
| [Rcp\_QuicErrorCode](remote-communication-overview.md#rcp_quicerrorcode) [HMS\_Rcp\_QuicStreamGetInfo](remote-communication-overview.md#hms_rcp_quicstreamgetinfo) ([Rcp\_QuicConn](remote-communication-overview.md#rcp_quicconn) \*conn, uint64\_t streamId, [Rcp\_QuicStreamInfo](remote-communication-overview.md#rcp_quicstreaminfo) info, void \*infoVal, uint32\_t \*infoLen) | 获取quic连接中streamId对应流的信息。 |
| [Rcp\_QuicSession](remote-communication-overview.md#rcp_quicsession) \*[HMS\_Rcp\_QuicCreateSession](remote-communication-overview.md#hms_rcp_quiccreatesession) () | 创建quic会话对象。一个quic会话中可以管理多个quic连接。 |
| void [HMS\_Rcp\_QuicDestroySession](remote-communication-overview.md#hms_rcp_quicdestroysession) ([Rcp\_QuicSession](remote-communication-overview.md#rcp_quicsession) \*session) | 销毁quic会话对象。释放quic会话资源。 |
| [Rcp\_QuicConn](remote-communication-overview.md#rcp_quicconn) \*[HMS\_Rcp\_QuicConnCreate](remote-communication-overview.md#hms_rcp_quicconncreate) (char \*alpn, void \*userObject) | 创建quic连接对象。 |
| [Rcp\_QuicErrorCode](remote-communication-overview.md#rcp_quicerrorcode) [HMS\_Rcp\_QuicConnConnect](remote-communication-overview.md#hms_rcp_quicconnconnect) ([Rcp\_QuicSession](remote-communication-overview.md#rcp_quicsession) \*session, [Rcp\_QuicConn](remote-communication-overview.md#rcp_quicconn) \*conn, const char \*serverName, uint16\_t port) | 发起quic连接握手。握手结果通过连接回调通知。 |
| [Rcp\_QuicErrorCode](remote-communication-overview.md#rcp_quicerrorcode) [HMS\_Rcp\_QuicConnDestroy](remote-communication-overview.md#hms_rcp_quicconndestroy) ([Rcp\_QuicConn](remote-communication-overview.md#rcp_quicconn) \*conn) | 销毁quic连接对象。释放quic连接资源。 |
| [Rcp\_QuicErrorCode](remote-communication-overview.md#rcp_quicerrorcode) [HMS\_Rcp\_QuicConnStreamOpen](remote-communication-overview.md#hms_rcp_quicconnstreamopen) ([Rcp\_QuicConn](remote-communication-overview.md#rcp_quicconn) \*conn, [Rcp\_QuicStreamDirection](remote-communication-overview.md#rcp_quicstreamdirection) direction, uint64\_t \*streamId, void \*userObject) | 在quic连接中打开一个quic流。quic连接建立成功后才能打开quic流。 |
| [Rcp\_QuicErrorCode](remote-communication-overview.md#rcp_quicerrorcode) [HMS\_Rcp\_QuicConnStreamSend](remote-communication-overview.md#hms_rcp_quicconnstreamsend) ([Rcp\_QuicConn](remote-communication-overview.md#rcp_quicconn) \*conn, uint64\_t streamId, const [Rcp\_QuicIoVec](_rcp___quic_io_vec.md) \*ioVec, uint32\_t ioVecCount, bool fin) | 通过quic流发送数据。 |
| [Rcp\_QuicErrorCode](remote-communication-overview.md#rcp_quicerrorcode) [HMS\_Rcp\_QuicConnStreamWantRead](remote-communication-overview.md#hms_rcp_quicconnstreamwantread) ([Rcp\_QuicConn](remote-communication-overview.md#rcp_quicconn) \*conn, uint64\_t streamId) | 触发quic流数据读取回调。 |
| [Rcp\_QuicErrorCode](remote-communication-overview.md#rcp_quicerrorcode) [HMS\_Rcp\_QuicConnStreamReset](remote-communication-overview.md#hms_rcp_quicconnstreamreset) ([Rcp\_QuicConn](remote-communication-overview.md#rcp_quicconn) \*conn, uint64\_t streamId, uint64\_t appErr) | 重置quic流。立即终止流，丢弃所有未发送和已接收的数据。 |
| [Rcp\_QuicErrorCode](remote-communication-overview.md#rcp_quicerrorcode) [HMS\_Rcp\_QuicConnStreamShutdown](remote-communication-overview.md#hms_rcp_quicconnstreamshutdown) ([Rcp\_QuicConn](remote-communication-overview.md#rcp_quicconn) \*conn, uint64\_t streamId, [Rcp\_QuicStreamShutdown](remote-communication-overview.md#rcp_quicstreamshutdown) flag, uint64\_t appErr) | 关闭连接中streamId对应流的读或写。 |
| [Rcp\_QuicStreamDirection](remote-communication-overview.md#rcp_quicstreamdirection) [HMS\_Rcp\_QuicStreamGetDirection](remote-communication-overview.md#hms_rcp_quicstreamgetdirection) (uint64\_t streamId) | 获取quic流的方向类型。 |
| void [HMS\_Rcp\_QuicFreeSlist](remote-communication-overview.md#hms_rcp_quicfreeslist) ([Rcp\_QuicSlist](_rcp___quic_slist.md) \*list) | 释放[Rcp\_QuicSlist](_rcp___quic_slist.md)链表，释放链表中的所有节点和数据。 |
