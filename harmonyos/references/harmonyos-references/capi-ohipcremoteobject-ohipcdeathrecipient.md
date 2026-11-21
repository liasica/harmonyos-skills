---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ohipcremoteobject-ohipcdeathrecipient
title: OHIPCDeathRecipient
breadcrumb: API参考 > 应用框架 > IPC Kit（进程间通信服务） > C API > 结构体 > OHIPCDeathRecipient
category: harmonyos-references
scraped_at: 2026-11-21T09:14:56+08:00
doc_updated_at: 2026-11-20
content_hash: sha256:5d6e3322fae8ac179823e5796468a9547f1ac1c2c5097fa920a3c97a8dce89bb
---

```c
typedef struct OHIPCDeathRecipient OHIPCDeathRecipient
```

## 概述

IPC死亡通知对象，用于监听IPC远程对象的死亡事件。创建OHIPCDeathRecipient对象后，必须注册到[OHIPCRemoteObject](capi-ohipcremoteobject.md)对象才能生效；若未注册，将无法监听死亡事件。当远程进程意外终止或主动销毁时，注册了死亡监听的本地进程将收到死亡通知回调，从而及时释放相关资源或进行错误处理。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 12

**相关模块：** [OHIPCRemoteObject](capi-ohipcremoteobject.md)

**所在头文件：** [ipc\_cremote\_object.h](capi-ipc-cremote-object-h.md)
