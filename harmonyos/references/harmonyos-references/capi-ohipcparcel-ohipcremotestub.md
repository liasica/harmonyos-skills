---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ohipcparcel-ohipcremotestub
title: OHIPCRemoteStub
breadcrumb: API参考 > 应用框架 > IPC Kit（进程间通信服务） > C API > 结构体 > OHIPCRemoteStub
category: harmonyos-references
scraped_at: 2026-09-02T14:52:03+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:0e301eaddc01fc33405376702c6da2d0c8a9ca85576c12e35387037d2f0f211b
---

```c
typedef struct OHIPCRemoteStub OHIPCRemoteStub;
```

## 概述

IPC远端服务对象。该结构体用于在服务端表示一个远端服务，作为IPC通信中服务端的服务代理，用于处理客户端的请求并实现跨进程通信。OHIPCRemoteStub是IPC Kit提供的核心结构体，使用OHIPCRemoteStub可以简化IPC服务开发流程，提供统一的请求处理机制，帮助开发者快速实现跨进程通信能力。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 12

**相关模块：**[OHIPCParcel](capi-ohipcparcel.md)

**所在头文件：** [ipc\_cparcel.h](capi-ipc-cparcel-h.md)
