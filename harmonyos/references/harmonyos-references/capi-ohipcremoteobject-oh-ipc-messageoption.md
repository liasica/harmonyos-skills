---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ohipcremoteobject-oh-ipc-messageoption
title: OH_IPC_MessageOption
breadcrumb: API参考 > 应用框架 > IPC Kit（进程间通信服务） > C API > 结构体 > OH_IPC_MessageOption
category: harmonyos-references
scraped_at: 2026-04-28T08:06:23+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:4b47be363d9ab557898f4eba19ac44dbc03251f510b4dd1eece01d23d6bc0419
---

```
1. typedef struct {...} OH_IPC_MessageOption
```

## 概述

PhonePC/2in1TabletTVWearable

IPC消息选项定义。

**起始版本：** 12

**相关模块：** [OHIPCRemoteObject](capi-ohipcremoteobject.md)

**所在头文件：** [ipc\_cremote\_object.h](capi-ipc-cremote-object-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [OH\_IPC\_RequestMode](capi-ipc-cremote-object-h.md#oh_ipc_requestmode) mode | 消息请求模式。 |
| uint32\_t timeout | RPC预留参数，该参数对IPC无效。 |
| void\* reserved | 保留参数，必须为空 |
