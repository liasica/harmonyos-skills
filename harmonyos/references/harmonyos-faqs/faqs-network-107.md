---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-network-107
title: TLSSocket中on('close')和on('error')事件的触发条件
breadcrumb: FAQ > 系统开发 > 网络 > 网络（Network） > TLSSocket中on('close')和on('error')事件的触发条件
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:37+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:6e7546c0518753669fd9e841288a4be53ef33ad88cc3f82ec14ff1c33e983daf
---

## 问题现象

TLSSocket中，on('close')和on('error')分别用于订阅关闭和error事件，二者的触发条件分别有哪些？

## 背景知识

[TLSSocket](../harmonyos-references/js-apis-socket.md#tlssocket9)是一种基于TLS/SSL协议的安全网络通信套接字，用于在客户端与服务器之间建立加密的数据传输通道，确保数据的机密性和完整性。

## 解决方案

* TLSSocket的[on('close')](../harmonyos-references/js-apis-socket.md#onconnect--close9)用于订阅TLSSocket的关闭事件，可以在此回调中执行资源释放、状态更新等操作。其触发条件主要表现在当一个TLSSocket成功建立连接并完成对网络资源的请求后，若在一段时间内业务侧未对该Socket进行任何操作，系统会根据配置的超时机制自动关闭该Socket连接，以释放资源。
* TLSSocket的[on('error')](../harmonyos-references/js-apis-socket.md#onerror9)用于订阅TLSSocket连接的error事件，可以在此回调中处理错误，例如重试连接或提醒用户。其触发条件可能性较多，常见的有以下几种：
  + SYN包丢失：客户端发送的SYN（同步序列编号）包因为网络拥塞、路由异常或防火墙规则等原因未能到达服务器，导致连接无法建立。
  + SYN-ACK包丢失：服务器在接收SYN包后回复的SYN-ACK包由于网络问题或中间设备的过滤规则在网络传输过程中丢失，导致客户端无法完成三次握手。
  + ACK包丢失：客户端在接收SYN-ACK后发送的ACK包丢失，导致服务器端认为客户端未正确接收到SYN-ACK包，从而拒绝连接。
  + 超时重传机制失效：TCP协议存在超时重传机制，但如果网络延迟极高或者重传次数过多且均失败，最终也会导致连接建立失败。
  + 端口不可达：如果目标服务器上的对应端口未开放或被防火墙拦截，服务器将返回ICMP端口不可达的错误消息，而非正常的SYN-ACK响应。
  + 资源限制：服务器或客户端因为资源不足（如文件描述符耗尽、内存不足等）而无法正常处理连接请求，导致连接失败。

## 常见FAQ

Q：可以使用哪种方式处理TLSSocket的重连？

A：通过监听TLSSocket对象的方式处理重连。可以在on('error')事件的回调中处理error，不同网络原因导致的error，业务侧会收到不同的错误反馈，然后根据错误原因进行处理。

Q：在监听同一个TLSSocket对象时，通过on('error')监听应用后台运行返回前台后或息屏几秒再开屏后，会触发两次错误码为2303505的错误回调，可能是什么原因？

A：[错误码2303505](../harmonyos-references/errorcode-net-socket.md#section2303505-tls系统调用错误)为TLS系统调用错误，由于网络问题而导致通信失败。根据日志进行排查，原因是发送一次TLSSocket请求，会收到两次错误响应，即第一次是通过已建立的加密连接接收服务器发送的数据时所收到的错误通知，第二次是通过已建立的加密连接发送数据时所收到的错误通知。

Q：通过socket.TCPSocket的connect连接指定ip和port，API返回错误码[2301004](../harmonyos-references/errorcode-net-socket.md#section2301004-系统调用中断)。

A：设备和手机要连接在同一个网段。

Q：频繁触发Socket发送数据，提示2301004错误，error回调返回error.code=4。

A：发送频率比较高需要使用多线程，而TaskPool和Worker的作用就是为应用程序提供一个多线程的运行环境。也可以通过合并数据，降低发送频率。

Q：TLSSocket在应用进入后台后多久后会断连？

A：应用进入后台两秒就会断连。

Q：2in1 PC对于网络的事件监控可以使用Linux的iptables机制吗？可以直接转发或者读取网卡流量吗？

A：iptables是Linux系统内置的包过滤防火墙工具；HarmonyOS支持的设置防火墙规则，参考：[使用网络防火墙](../harmonyos-guides/net-netfirewall.md)。
