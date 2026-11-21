---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ohipcparcel-ohipcparcel
title: OHIPCParcel
breadcrumb: API参考 > 应用框架 > IPC Kit（进程间通信服务） > C API > 结构体 > OHIPCParcel
category: harmonyos-references
scraped_at: 2026-11-21T09:14:55+08:00
doc_updated_at: 2026-11-20
content_hash: sha256:594377b244c3d1a2861bcaf0f4bcc3462d94eb8be6e530fa4bbee39a61a7ca8b
---

```c
typedef struct OHIPCParcel OHIPCParcel
```

## 概述

IPC序列化对象，用于在跨进程通信中序列化和反序列化数据。该对象需要通过相关函数创建和销毁，开发者需要遵循对象的生命周期管理规范，正确管理内存资源。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 12

**相关模块：** [OHIPCParcel](capi-ohipcparcel.md)

**所在头文件：** [ipc\_cparcel.h](capi-ipc-cparcel-h.md)
