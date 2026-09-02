---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ohipcparcel-ohipcremoteproxy
title: OHIPCRemoteProxy
breadcrumb: API参考 > 应用框架 > IPC Kit（进程间通信服务） > C API > 结构体 > OHIPCRemoteProxy
category: harmonyos-references
scraped_at: 2026-09-02T14:52:03+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:669ab1825939f0d99f02342176497633b18e7d6fc1ee6d6b9e77834496407356
---

```c
typedef struct OHIPCRemoteProxy OHIPCRemoteProxy
```

## 概述

IPC（进程间通信）远端代理对象，用于在客户端代理远端服务的能力，实现跨进程通信。该对象封装了远端服务的引用，支持向远端服务发送请求和接收响应。适用于需要跨进程调用服务能力的场景，例如跨进程服务调用、系统服务访问、跨应用数据共享等典型应用。使用该对象可以简化跨进程通信的实现，提高开发效率。

**起始版本：** 12

**相关模块：**[OHIPCParcel](capi-ohipcparcel.md)

**所在头文件：** [ipc\_cparcel.h](capi-ipc-cparcel-h.md)
