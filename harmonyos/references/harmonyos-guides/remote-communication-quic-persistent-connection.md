---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/remote-communication-quic-persistent-connection
title: QUIC长连接接收消息推送
breadcrumb: 指南 > 系统 > 网络 > Remote Communication Kit（远场通信服务） > 使用QUIC协议进行网络通信 > QUIC长连接接收消息推送
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:06+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:d8955e13cbac04bf75e4d5bc4c722bd33aa7f3a5d973d629f469be06438c53e9
---

从26.0.0版本开始，新增支持QUIC长连接能力。

QUIC长连接基于QUIC（Quick UDP Internet Connections）协议实现，相比传统的TCP协议，QUIC在速度、灵活性和稳定性方面更具备核心优势。QUIC长连接在即时通讯、实时推送、在线协作等场景中具有广泛应用，能够显著提升通信效率和用户体验。远场通信服务提供[QUIC长连接API](../harmonyos-references/rcp_quic_h.md)，为开发者提供高效、可靠的端云通信能力。

在服务端主动推送消息的场景下，QUIC长连接通过无队头阻塞的多路复用及更少的握手次数，有效优化传统HTTP/1.1及HTTP/2协议中的队头阻塞与多次握手问题，降低网络延迟和资源消耗。此外，QUIC长连接能够保持连接的持久性，减少连接建立和断开频率，进一步提升通信效率。

## 接收长连接服务端消息推送

1. 在.cpp文件导入模块。

   ```cpp
   #include "RemoteCommunicationKit/rcp_quic.h"
   #include <stdio.h>
   #include <stdlib.h>
   #include <string.h>
   ```
2. 在CMakeLists.txt文件中添加以下lib依赖包（具体请见[C API开发准备](remote-communication-preparations.md#c-api开发准备)）。

   ```cpp
   librcp_quic.so
   ```
3. 自定义全局变量，可用于QUIC连接与流配置。

   ```cpp
   uint64_t g_StreamId = 0;
   uint64_t userData = 0;
   char *alpn = "h3";
   const char *serverName = "www.example.com"; // 示例代码，仅用于展示调用，实际运行请替换为真实的QUIC协议服务端地址
   uint64_t serverPort = 443; // 示例代码，仅用于展示调用，实际运行请替换为真实端口
   ```
4. 自定义回调方法，用于后续步骤注册监听事件，可在回调中补充需要的业务逻辑。

   ```cpp
   // 连接成功时触发
   void OnConnectedImpl(Rcp_QuicConn *conn, void *userObject) {
       (void)conn;
       if (userObject == NULL) {
           return;
       }
   }

   // 异常发生时触发
   void OnErrorImpl(Rcp_QuicConn *conn, void *userObject, Rcp_QuicErrorCode errCode, const char *errDetail) {
       (void)conn;
       if (errCode == 0 || userObject == NULL || errDetail == NULL) {
           return;
       }
   }

   // 连接关闭时触发
   void OnClosedImpl(Rcp_QuicConn *conn, void *userObject) {
       (void)conn;
       if (userObject == NULL) {
           return;
       }
   }

   // 接收到对端传输数据时触发，需要返回接收到的数据大小
   void OnReceiveDataImpl(Rcp_QuicConn *conn, void *userObject, uint64_t streamId,
                          const Rcp_QuicStreamData *streamData) {
       (void)conn;
       (void)streamId;
       (void)userObject;
       uint64_t totalBytes = 0;
       for (uint32_t i = 0; i < streamData->iovLen; i++) {
           totalBytes += streamData->iov[i].length;
       }
       return totalBytes;
   }

   // 接收到流事件时触发
   void onQuicStreamEventImpl(Rcp_QuicConn *conn, void *userObject, uint64_t streamId, Rcp_QuicErrorCode errCode,
                              const char *errDetail) {
       (void)conn;
       (void)userObject;
       (void)streamId;
       (void)errCode;
       (void)errDetail;
   }

   // 接收到对端创建流时触发
   void OnStreamInboundImpl(Rcp_QuicConn *conn, void *userObject, uint64_t streamId) {
       (void)conn;
       (void)userObject;
       g_StreamId = streamId;
   }
   ```
5. 初始化QUIC配置项。

   ```cpp
   // 创建QUIC会话对象，用于管理全局资源
   Rcp_QuicSession *session = HMS_Rcp_QuicCreateSession();
   // 创建QUIC连接对象，需要指定ALPN协议和用户对象
   Rcp_QuicConn *conn = HMS_Rcp_QuicConnCreate(alpn, &userData);
   // 设置连接建立成功时的回调
   HMS_Rcp_QuicConnSetOpt(conn, RCP_QUIC_CONN_ON_CONNECTED_FUNCTION, &OnConnectedImpl, 0);
   // 设置发生错误时的回调
   HMS_Rcp_QuicConnSetOpt(conn, RCP_QUIC_CONN_ON_ERROR_FUNCTION, &OnErrorImpl, 0);
   // 设置连接关闭时的回调
   HMS_Rcp_QuicConnSetOpt(conn, RCP_QUIC_CONN_ON_CLOSED_FUNCTION, &OnClosedImpl, 0);
   // 设置服务端创建流时的回调
   HMS_Rcp_QuicConnSetOpt(conn, RCP_QUIC_CONN_STREAM_INBOUND_FUNCTION, &OnStreamInboundImpl, 0);
   ```
6. 与服务端进行连接。

   ```cpp
   HMS_Rcp_QuicConnConnect(session, conn, serverName, serverPort);
   ```
7. 服务端主动创建流，客户端接收到OnStreamInboundImpl回调后，为返回的对端流streamId设置监听事件。

   ```cpp
   HMS_Rcp_QuicStreamSetOpt(conn, g_StreamId, RCP_QUIC_STREAM_EVENT_FUNCTION, &onQuicStreamEventImpl, 0);
   HMS_Rcp_QuicStreamSetOpt(conn, g_StreamId, RCP_QUIC_STREAM_DATA_FUNCTION, &OnReceiveDataImpl, 0);
   ```
8. 业务完成后，关闭连接并释放资源。

   ```cpp
   // 关闭流
   uint64_t appErr = 0; // 自定义业务状态码，服务端在流关闭时可以接收到此状态码用于对关闭原因进行判断
   HMS_Rcp_QuicConnStreamShutdown(conn, g_StreamId, RCP_QUIC_STREAM_SHUTDOWN_WRITE, appErr);
   HMS_Rcp_QuicConnStreamShutdown(conn, g_StreamId, RCP_QUIC_STREAM_SHUTDOWN_READ, appErr);

   // 销毁连接对象，关闭所有流并释放连接资源
   if (conn != NULL) {
       HMS_Rcp_QuicConnDestroy(conn);
   }

   // 销毁会话对象，释放QUIC全局资源
   if (session != NULL) {
       HMS_Rcp_QuicDestroySession(session);
   }
   ```
