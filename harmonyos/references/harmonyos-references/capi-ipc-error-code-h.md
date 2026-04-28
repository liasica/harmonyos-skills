---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ipc-error-code-h
title: ipc_error_code.h
breadcrumb: API参考 > 应用框架 > IPC Kit（进程间通信服务） > C API > 头文件 > ipc_error_code.h
category: harmonyos-references
scraped_at: 2026-04-28T08:06:23+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:070806a352c5ec19c1d2d01f72092d7befb768b27a56f7cd08190d19e40add18
---

## 概述

PhonePC/2in1TabletTVWearable

提供IPC错误码定义。

**引用文件：** <IPCKit/ipc\_error\_code.h>

**库：** libipc\_capi.so

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 12

**相关模块：** [OHIPCErrorCode](capi-ohipcerrorcode.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 枚举

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [OH\_IPC\_ErrorCode](capi-ipc-error-code-h.md#oh_ipc_errorcode) | OH\_IPC\_ErrorCode | IPC消息选项定义。 |

## 枚举类型说明

PhonePC/2in1TabletTVWearable

### OH\_IPC\_ErrorCode

PhonePC/2in1TabletTVWearable

```
1. enum OH_IPC_ErrorCode
```

**描述：**

IPC错误码定义。

**起始版本：** 12

| 枚举值 | 描述 |
| --- | --- |
| OH\_IPC\_SUCCESS = 0 | 执行成功。 |
| OH\_IPC\_ERROR\_CODE\_BASE = 1901000 | 错误码区间起始值。 |
| OH\_IPC\_CHECK\_PARAM\_ERROR = OH\_IPC\_ERROR\_CODE\_BASE | 参数错误。 |
| OH\_IPC\_PARCEL\_WRITE\_ERROR = OH\_IPC\_ERROR\_CODE\_BASE + 1 | 序列化对象写入数据失败。 |
| OH\_IPC\_PARCEL\_READ\_ERROR = OH\_IPC\_ERROR\_CODE\_BASE + 2 | 序列化对象读取数据失败。 |
| OH\_IPC\_MEM\_ALLOCATOR\_ERROR = OH\_IPC\_ERROR\_CODE\_BASE + 3 | 内存分配失败。 |
| OH\_IPC\_CODE\_OUT\_OF\_RANGE = OH\_IPC\_ERROR\_CODE\_BASE + 4 | 命令字超出定义范围[0x01,0x00ffffff]。 |
| OH\_IPC\_DEAD\_REMOTE\_OBJECT = OH\_IPC\_ERROR\_CODE\_BASE + 5 | 远端对象死亡。 |
| OH\_IPC\_INVALID\_USER\_ERROR\_CODE = OH\_IPC\_ERROR\_CODE\_BASE + 6 | 用户自定义错误码超出范围[1900001, 1999999]。 |
| OH\_IPC\_INNER\_ERROR = OH\_IPC\_ERROR\_CODE\_BASE + 7 | IPC内部错误。 |
| OH\_IPC\_ERROR\_CODE\_MAX = OH\_IPC\_ERROR\_CODE\_BASE + 1000 | 错误码区间最大值。 |
| OH\_IPC\_USER\_ERROR\_CODE\_MIN = 1909000 | 用户自定义错误码最小值。 |
| OH\_IPC\_USER\_ERROR\_CODE\_MAX = 1909999 | 用户自定义错误码最大值。 |
