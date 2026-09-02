---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-network-132
title: 如何定位WebSocket连接异常断开
breadcrumb: FAQ > 系统开发 > 网络 > 网络（Network） > 如何定位WebSocket连接异常断开
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:37+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:771cc9178201571d40cf6eb81ed27a611257e9957d2ec9a6c6a2db086a7df119
---

## 问题现象

场景一：在建立WebSocket连接时失败。

场景二：WebSocket连接成功后，过段时间异常断开，并且断开时间相对固定。

场景三：WebSocket连接成功，但是在收发消息时异常断开，断开时间不固定。

## 背景知识

* **心跳机制**：WebSocket默认开启心跳检测，需要服务器对客户端发送的Ping帧回复Pong，否则客户端会自动断开连接，默认超时时间为30s，可参考使用WebSocket访问网络[场景介绍](../harmonyos-guides/websocket-connection.md#场景介绍)的说明事项。
* **wireshark**：一款强大的网络协议分析工具，用于捕获和分析网络数据包，帮助用户深入理解和调试网络通信问题。
* **lws callback事件**：WebSocket连接基于[libwebsockets](https://gitcode.com/openharmony/third_party_libwebsockets)开源库实现，在hilog日志中会打印底层连接的回调事件lws callback reason is [lws\_callback\_reasons]，callback详情描述可参考libwebsockets官网[User Callback](https://libwebsockets.org/lws-api-doc-main/html/group__usercb.html)介绍。

## 问题定位

1. 开启[on('open')](../harmonyos-references/js-apis-websocket.md#onopen)、[on('close')](../harmonyos-references/js-apis-websocket.md#onclose)、[on('error')](../harmonyos-references/js-apis-websocket.md#onerror)监听事件，并在回调事件内打印日志，以提供报错信息。
2. 确认连接断开的时间规律，分析hilog日志及网络数据包：

* WebSocket在连接过程中断开，未正常建立连接，搜索Lws client connection error关键词，判断连接失败原因，比如：
  + Lws client connection error conn fail: 110中的110在网络通信中代表连接超时，需要检查网络连接是否正常、服务器地址是否可达等问题。

    ```txt
    01-17 17:08:34.585   44111-44643   C015B0/om.test...cket/NETSTACK  com.test....bsocket  I     [websocket_exec.cpp:466] lws callback reason is 1
    01-17 17:08:34.585   44111-44643   C015B0/om.test...cket/NETSTACK  com.test....bsocket  I     [websocket_exec.cpp:332] Lws client connection error conn fail: 110
    ...
    01-17 17:08:34.588   44111-44111   A03D00/om.test...bsocket/JSAPP  com.test....bsocket  E     Websocket Client on error, error:{"code":200,"data":"0"}
    ```
  + Lws client connection error Timed out waiting SSL表示SSL认证卡住，需要检查服务地址是ws还是wss，服务器证书是否有效、SSL\TLS协议是否一致等问题。

    ```txt
    01-17 16:55:05.609   35392-35392   C015B0/om.test...cket/NETSTACK  com.test....bsocket  I     [websocket_exec.cpp:723] ConnectCallback connect success
    ...
    01-17 16:55:20.650   35392-35878   C015B0/om.test...cket/NETSTACK  com.test....bsocket  I     [websocket_exec.cpp:466] lws callback reason is 1
    01-17 16:55:20.650   35392-35878   C015B0/om.test...cket/NETSTACK  com.test....bsocket  I     [websocket_exec.cpp:332] Lws client connection error Timed out waiting SSL
    01-17 16:55:20.655   35392-35392   A03D00/om.test...bsocket/JSAPP  com.test....bsocket  E     Websocket Client on error, error:{"code":200,"data":"0"}
    ```
* WebSocket在连接成功后，固定时长断开。比如连接总是运行60s、30s后断开，检查客户端和服务器设置的心跳超时时间：
  + 客户端会自动启用心跳机制，默认30s发送Ping帧，当客户端收到服务端响应的Pong帧，维持连接。lws callback reason is 9代表客户端已接收到Pong帧数据包：

    ```txt
    01-17 15:33:35.384   49856-50626   C015B0/om.test...cket/NETSTACK  com.test....bsocket  I     [websocket_exec.cpp:555] PingInterval is 30,  PongTimeout is 30
    ...
    01-17 16:46:55.036   49856-30249   C015B0/om.test...cket/NETSTACK  com.test....bsocket  I     [websocket_exec.cpp:466] lws callback reason is 10
    01-17 16:46:55.084   49856-30249   C015B0/om.test...cket/NETSTACK  com.test....bsocket  I     [websocket_exec.cpp:466] lws callback reason is 9
    01-17 16:47:25.086   49856-30249   C015B0/om.test...cket/NETSTACK  com.test....bsocket  I     [websocket_exec.cpp:466] lws callback reason is 10
    01-17 16:47:25.135   49856-30249   C015B0/om.test...cket/NETSTACK  com.test....bsocket  I     [websocket_exec.cpp:466] lws callback reason is 9
    ```
  + 当网络抖动等原因，服务器未回复Pong帧导致心跳检测失败，客户端自动关闭连接，触发on('close')事件，回调的error message为The link is down。

    ```txt
    01-17 18:45:37.620   16507-51025   C015B0/om.test...cket/NETSTACK  com.test....bsocket  I     [websocket_exec.cpp:466] lws callback reason is 10
    01-17 18:46:07.619   16507-51025   C015B0/om.test...cket/NETSTACK  com.test....bsocket  I     [websocket_exec.cpp:466] lws callback reason is 75
    01-17 18:46:07.619   16507-51025   C015B0/om.test...cket/NETSTACK  com.test....bsocket  E     [websocket_exec.cpp:427] The link is down, onError
    01-17 18:46:07.622   16507-16507   A03D00/om.test...bsocket/JSAPP  com.test....bsocket  E     Websocket Client on error, error:{"code":200,"data":"0"}
    01-17 18:46:07.623   16507-16507   A03D00/om.test...bsocket/JSAPP  com.test....bsocket  I     Websocket Client on close, code is 0, reason is The link is down
    ```
* WebSocket在连接成功后，随机断开。抓包分析TCP交互，在wireshark中使用ip.src == [服务器ip地址] || ip.dst == [服务器ip地址]过滤数据包，率先发送[FIN, ACK]数据包的为主动断开方。比如下图为101.201.\*\*.\*\*服务端主动断开连接，再结合业务日志分析具体的断开原因。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/UasGFTf_SAWnR23YhVnVEQ/zh-cn_image_0000002658970475.png "点击放大")

## 分析结论

WebSocket连接异常断开通常有多种原因，需要结合hilog日志及网络数据包分析断开原因。通常60s固定时长断开为客户端心跳机制主动断开，需要检查网络链路是否通畅及服务器是否回复Pong帧。

## 修改建议

1. 如果服务器自行实现了心跳检测，不会回复Pong帧，可以将[WebSocketRequestOptions](../harmonyos-references/js-apis-websocket.md#websocketrequestoptions)的pingInterval参数置为0，关闭客户端默认的心跳检测。
2. 如果是网络抖动导致的连接失败或随机断开，参考[如何优化WebSocket长连接在弱网环境下的重连效率与心跳机制](faqs-network-84.md)。
