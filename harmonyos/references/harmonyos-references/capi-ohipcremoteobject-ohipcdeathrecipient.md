---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ohipcremoteobject-ohipcdeathrecipient
title: OHIPCDeathRecipient
breadcrumb: API参考 > 应用框架 > IPC Kit（进程间通信服务） > C API > 结构体 > OHIPCDeathRecipient
category: harmonyos-references
scraped_at: 2026-09-02T14:52:03+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:861ed27d13269fc341f4628fe18db598d0158ff7bb0858a2508c19c50c54c7f2
---

```c
typedef struct OHIPCDeathRecipient OHIPCDeathRecipient
```

## 概述

IPC死亡通知对象，用于监听IPC远程对象的死亡事件。创建OHIPCDeathRecipient对象后，必须注册到OHIPCRemoteObject对象才能生效；若未注册，将无法监听死亡事件。当远程进程意外终止或主动销毁时，注册了死亡监听的本地进程将收到死亡通知回调，从而及时释放相关资源或进行错误处理。

**起始版本：** 12

**相关模块：** [OHIPCRemoteObject](capi-ohipcremoteobject.md)

**所在头文件：** [ipc\_cremote\_object.h](capi-ipc-cremote-object-h.md)
