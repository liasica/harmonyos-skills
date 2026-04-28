---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ipc-cskeleton-h
title: ipc_cskeleton.h
breadcrumb: API参考 > 应用框架 > IPC Kit（进程间通信服务） > C API > 头文件 > ipc_cskeleton.h
category: harmonyos-references
scraped_at: 2026-04-28T08:06:22+08:00
doc_updated_at: 2026-03-17
content_hash: sha256:39e91fcab81e6356e02cded053447c7f8ebf8cdbbbfe316a448b6c97c7d181d8
---

## 概述

PhonePC/2in1TabletTVWearable

提供IPC框架tokenId、凭据、PID/UID、线程池配置等功能C接口。

**引用文件：** <IPCKit/ipc\_cskeleton.h>

**库：** libipc\_capi.so

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 12

**相关模块：** [OHIPCSkeleton](capi-ohipcskeleton.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 函数

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [void OH\_IPCSkeleton\_JoinWorkThread(void)](capi-ipc-cskeleton-h.md#oh_ipcskeleton_joinworkthread) | 当前线程加入IPC工作线程池。 |
| [void OH\_IPCSkeleton\_StopWorkThread(void)](capi-ipc-cskeleton-h.md#oh_ipcskeleton_stopworkthread) | 当前线程退出IPC工作线程池。 |
| [uint64\_t OH\_IPCSkeleton\_GetCallingTokenId(void)](capi-ipc-cskeleton-h.md#oh_ipcskeleton_getcallingtokenid) | 获取调用方TokenId。该接口需要在IPC上下文中调用，否则返回自身TokenId。 |
| [uint64\_t OH\_IPCSkeleton\_GetFirstTokenId(void)](capi-ipc-cskeleton-h.md#oh_ipcskeleton_getfirsttokenid) | 获取首调者TokenId。 |
| [uint64\_t OH\_IPCSkeleton\_GetSelfTokenId(void)](capi-ipc-cskeleton-h.md#oh_ipcskeleton_getselftokenid) | 获取自身TokenId。 |
| [uint64\_t OH\_IPCSkeleton\_GetCallingPid(void)](capi-ipc-cskeleton-h.md#oh_ipcskeleton_getcallingpid) | 获取调用方进程ID。该接口需要在IPC上下文中调用，否则返回当前进程ID。 |
| [uint64\_t OH\_IPCSkeleton\_GetCallingUid(void)](capi-ipc-cskeleton-h.md#oh_ipcskeleton_getcallinguid) | 获取调用方用户ID。该接口需要在IPC上下文中调用，否则返回当前用户ID。 |
| [int OH\_IPCSkeleton\_IsLocalCalling(void)](capi-ipc-cskeleton-h.md#oh_ipcskeleton_islocalcalling) | 判断是否正在进行本地调用。 |
| [int OH\_IPCSkeleton\_SetMaxWorkThreadNum(const int maxThreadNum)](capi-ipc-cskeleton-h.md#oh_ipcskeleton_setmaxworkthreadnum) | 设置最大工作线程数。 |
| [int OH\_IPCSkeleton\_ResetCallingIdentity(char \*\*identity, int32\_t \*len, OH\_IPC\_MemAllocator allocator)](capi-ipc-cskeleton-h.md#oh_ipcskeleton_resetcallingidentity) | 重置调用方身份凭证为自身进程的身份凭证（包括tokenid、UID和PID信息），并返回调用方的凭证信息。 该信息主要用于OH\_IPCSkeleton\_SetCallingIdentity接口调用。 |
| [int OH\_IPCSkeleton\_SetCallingIdentity(const char \*identity)](capi-ipc-cskeleton-h.md#oh_ipcskeleton_setcallingidentity) | 恢复调用方凭证信息至IPC上下文中。 |
| [int OH\_IPCSkeleton\_IsHandlingTransaction(void)](capi-ipc-cskeleton-h.md#oh_ipcskeleton_ishandlingtransaction) | 是否正在处理IPC请求。 |

## 函数说明

PhonePC/2in1TabletTVWearable

### OH\_IPCSkeleton\_JoinWorkThread()

PhonePC/2in1TabletTVWearable

```
1. void OH_IPCSkeleton_JoinWorkThread(void)
```

**描述：**

当前线程加入IPC工作线程池。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 12

### OH\_IPCSkeleton\_StopWorkThread()

PhonePC/2in1TabletTVWearable

```
1. void OH_IPCSkeleton_StopWorkThread(void)
```

**描述：**

当前线程退出IPC工作线程池。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 12

### OH\_IPCSkeleton\_GetCallingTokenId()

PhonePC/2in1TabletTVWearable

```
1. uint64_t OH_IPCSkeleton_GetCallingTokenId(void)
```

**描述：**

获取调用方TokenId。该接口需要在IPC上下文中调用，否则返回自身TokenId。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 12

**返回：**

| 类型 | 说明 |
| --- | --- |
| uint64\_t | 返回调用方TokenId。 |

### OH\_IPCSkeleton\_GetFirstTokenId()

PhonePC/2in1TabletTVWearable

```
1. uint64_t OH_IPCSkeleton_GetFirstTokenId(void)
```

**描述：**

获取首调者TokenId。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 12

**返回：**

| 类型 | 说明 |
| --- | --- |
| uint64\_t | 返回首调者TokenId。 |

### OH\_IPCSkeleton\_GetSelfTokenId()

PhonePC/2in1TabletTVWearable

```
1. uint64_t OH_IPCSkeleton_GetSelfTokenId(void)
```

**描述：**

获取自身TokenId。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 12

**返回：**

| 类型 | 说明 |
| --- | --- |
| uint64\_t | 返回自身TokenId。 |

### OH\_IPCSkeleton\_GetCallingPid()

PhonePC/2in1TabletTVWearable

```
1. uint64_t OH_IPCSkeleton_GetCallingPid(void)
```

**描述：**

获取调用方进程ID。该接口需要在IPC上下文中调用，否则返回当前进程ID。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 12

**返回：**

| 类型 | 说明 |
| --- | --- |
| uint64\_t | 返回调用方进程ID。 |

### OH\_IPCSkeleton\_GetCallingUid()

PhonePC/2in1TabletTVWearable

```
1. uint64_t OH_IPCSkeleton_GetCallingUid(void)
```

**描述：**

获取调用方用户ID。该接口需要在IPC上下文中调用，否则返回当前用户ID。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 12

**返回：**

| 类型 | 说明 |
| --- | --- |
| uint64\_t | 返回调用方用户ID。 |

### OH\_IPCSkeleton\_IsLocalCalling()

PhonePC/2in1TabletTVWearable

```
1. int OH_IPCSkeleton_IsLocalCalling(void)
```

**描述：**

判断是否正在进行本地调用。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 12

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 正在进行本地调用，返回1；否则，返回0。 |

### OH\_IPCSkeleton\_SetMaxWorkThreadNum()

PhonePC/2in1TabletTVWearable

```
1. int OH_IPCSkeleton_SetMaxWorkThreadNum(const int maxThreadNum)
```

**描述：**

设置最大工作线程数。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const int maxThreadNum | maxThreadNum 最大工作线程数，默认16，范围:[1, 32]。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 成功返回[OH\_IPC\_ErrorCode#OH\_IPC\_SUCCESS](capi-ipc-error-code-h.md#oh_ipc_errorcode)；  参数错误返回[OH\_IPC\_ErrorCode#OH\_IPC\_CHECK\_PARAM\_ERROR](capi-ipc-error-code-h.md#oh_ipc_errorcode)；  其它情况返回[OH\_IPC\_ErrorCode#OH\_IPC\_INNER\_ERROR](capi-ipc-error-code-h.md#oh_ipc_errorcode)。 |

### OH\_IPCSkeleton\_ResetCallingIdentity()

PhonePC/2in1TabletTVWearable

```
1. int OH_IPCSkeleton_ResetCallingIdentity(char **identity, int32_t *len, OH_IPC_MemAllocator allocator)
```

**描述：**

重置调用方身份凭证为自身进程的身份凭证（包括tokenid、UID和PID信息），并返回调用方的凭证信息。 该信息主要用于OH\_IPCSkeleton\_SetCallingIdentity接口调用。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 12

**参数:**

| 参数项 | 描述 |
| --- | --- |
| char \*\*identity | identity 用于存储调用凭证的内存地址，该内存由用户提供的分配器进行内存分配，用户使用完后需要主动释放，不能为空。 |
| int32\_t \*len | len 写入identity的数据长度，不能为空。 |
| [OH\_IPC\_MemAllocator](capi-ipc-cparcel-h.md#oh_ipc_memallocator) allocator | allocator 用户指定的用来分配identity的内存分配器，不能为空。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 成功返回[OH\_IPC\_ErrorCode#OH\_IPC\_SUCCESS](capi-ipc-error-code-h.md#oh_ipc_errorcode)；  参数错误返回[OH\_IPC\_ErrorCode#OH\_IPC\_CHECK\_PARAM\_ERROR](capi-ipc-error-code-h.md#oh_ipc_errorcode)；  内存分配失败返回[OH\_IPC\_ErrorCode#OH\_IPC\_MEM\_ALLOCATOR\_ERROR](capi-ipc-error-code-h.md#oh_ipc_errorcode)；  其它情况返回[OH\_IPC\_ErrorCode#OH\_IPC\_INNER\_ERROR](capi-ipc-error-code-h.md#oh_ipc_errorcode)。 |

### OH\_IPCSkeleton\_SetCallingIdentity()

PhonePC/2in1TabletTVWearable

```
1. int OH_IPCSkeleton_SetCallingIdentity(const char *identity)
```

**描述：**

恢复调用方凭证信息至IPC上下文中。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const char \*identity | identity 调用方凭证，不能为空。来源于OH\_IPCSkeleton\_ResetCallingIdentity的返回值。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 成功返回[OH\_IPC\_ErrorCode#OH\_IPC\_SUCCESS](capi-ipc-error-code-h.md#oh_ipc_errorcode)；  参数错误返回[OH\_IPC\_ErrorCode#OH\_IPC\_CHECK\_PARAM\_ERROR](capi-ipc-error-code-h.md#oh_ipc_errorcode)；  其它情况返回[OH\_IPC\_ErrorCode#OH\_IPC\_INNER\_ERROR](capi-ipc-error-code-h.md#oh_ipc_errorcode)。 |

### OH\_IPCSkeleton\_IsHandlingTransaction()

PhonePC/2in1TabletTVWearable

```
1. int OH_IPCSkeleton_IsHandlingTransaction(void)
```

**描述：**

是否正在处理IPC请求。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 12

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 正在处理IPC请求，返回1；否则，返回0。 |
