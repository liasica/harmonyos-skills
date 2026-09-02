---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-network-138
title: 是否可以用手机作为Socket服务器
breadcrumb: FAQ > 系统开发 > 网络 > 网络（Network） > 是否可以用手机作为Socket服务器
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:37+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:31569af8eddd2a2d0e3c62ddf144cd7ff600b27b6e47ee5c29ff301fa02abc19
---

## 问题现象

在开启本地Socket服务后，是否可以用手机作为Socket服务器？

## 解决方案

* [Socket 连接](../harmonyos-guides/socket-connection.md)：Socket连接主要是通过Socket进行数据传输，支持TCP/UDP/Multicast/TLS协议。
* 基本概念：
  + Socket：套接字，就是对网络中不同主机上的应用进程之间进行双向通信的端点的抽象。
  + TCP：传输控制协议（Transmission Control Protocol）。是一种面向连接的、可靠的、基于字节流的传输层通信协议。
  + UDP：用户数据报协议（User Datagram Protocol）。是一个简单的面向消息的传输层，不需要连接。
  + Multicast：多播，基于UDP的一种通信模式，用于实现组内所有设备之间广播形式的通信。
  + LocalSocket：本地套接字，IPC(Inter-Process Communication)进程间通信的一种，实现设备内进程之间相互通信，无需网络。
  + TLS：安全传输层协议(Transport Layer Security)。用于在两个通信应用程序之间提供保密性和数据完整性。

可以[通过Local Socket Server进行数据传输](../harmonyos-guides/socket-connection.md#应用通过local-socket-server进行数据传输)的方式来实现使用手机作为Socket服务器。
