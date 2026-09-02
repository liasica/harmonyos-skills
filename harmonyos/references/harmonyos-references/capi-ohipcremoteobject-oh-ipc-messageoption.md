---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ohipcremoteobject-oh-ipc-messageoption
title: OH_IPC_MessageOption
breadcrumb: API参考 > 应用框架 > IPC Kit（进程间通信服务） > C API > 结构体 > OH_IPC_MessageOption
category: harmonyos-references
scraped_at: 2026-09-02T15:01:37+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:83931accb540c789842a4eed0c95de54a95b493ee9e02baa3fea9b7b63dd312a
---

```c
typedef struct {...} OH_IPC_MessageOption
```

## 概述

IPC消息选项定义，用于配置IPC通信过程中的请求参数。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 12

**相关模块：** [OHIPCRemoteObject](capi-ohipcremoteobject.md)

**所在头文件：** [ipc\_cremote\_object.h](capi-ipc-cremote-object-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| [OH\_IPC\_RequestMode](capi-ipc-cremote-object-h.md#oh_ipc_requestmode) mode | 消息请求模式，用于指定IPC消息的请求方式。可选择同步模式或异步模式，同步模式适用于需要等待返回结果的场景，异步模式适用于不需要等待结果的场景。设置同步模式后，调用会阻塞当前线程等待返回结果；设置异步模式后，调用会立即返回，不等待结果。在C语言中必须显式初始化此成员。推荐初始化为同步模式（当需要获取返回结果时），或异步模式（当不需要返回结果时）。 |
| uint32\_t timeout | RPC预留参数，在RPC通信场景下可设置超时时间，该参数对IPC通信无效，使用IPC时可忽略此参数，单位：s。取值范围为[0, 4294967295]。在RPC场景下，推荐根据业务需求设置合理的超时时间，避免长时间阻塞。超时后RPC调用会失败并返回超时错误。在C语言中必须显式初始化此成员，推荐初始化为0。 |
| void\* reserved | 保留参数，必须传入NULL。传入非空指针时可能导致接口调用失败或未定义行为。 |
