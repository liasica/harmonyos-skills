---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ipc-cremote-object-h
title: ipc_cremote_object.h
breadcrumb: API参考 > 应用框架 > IPC Kit（进程间通信服务） > C API > 头文件 > ipc_cremote_object.h
category: harmonyos-references
scraped_at: 2026-04-28T08:06:21+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:a3f4dbfb74d0249ef8fda78fabc20fa67a79b8563751ba41f17883846c6a1e9e
---

## 概述

PhonePC/2in1TabletTVWearable

提供远端对象创建、销毁、数据发送、远端对象死亡状态监听等功能的C接口。

**引用文件：** <IPCKit/ipc\_cremote\_object.h>

**库：** libipc\_capi.so

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 12

**相关模块：** [OHIPCRemoteObject](capi-ohipcremoteobject.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 结构体

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [OH\_IPC\_MessageOption](capi-ohipcremoteobject-oh-ipc-messageoption.md) | - | IPC消息选项定义。 |
| [OHIPCDeathRecipient](capi-ohipcremoteobject-ohipcdeathrecipient.md) | OHIPCDeathRecipient | 死亡通知对象。 |

### 枚举

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [OH\_IPC\_RequestMode](capi-ipc-cremote-object-h.md#oh_ipc_requestmode) | OH\_IPC\_RequestMode | IPC请求模式定义。 |

### 函数

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [typedef int (\*OH\_OnRemoteRequestCallback)(uint32\_t code, const OHIPCParcel \*data, OHIPCParcel \*reply, void \*userData)](capi-ipc-cremote-object-h.md#oh_onremoterequestcallback) | OH\_OnRemoteRequestCallback | Stub端用于处理远端数据请求的回调函数。 |
| [typedef void (\*OH\_OnRemoteDestroyCallback)(void \*userData)](capi-ipc-cremote-object-h.md#oh_onremotedestroycallback) | OH\_OnRemoteDestroyCallback | 用于监听对象销毁的回调函数。 |
| [OHIPCRemoteStub\* OH\_IPCRemoteStub\_Create(const char \*descriptor, OH\_OnRemoteRequestCallback requestCallback, OH\_OnRemoteDestroyCallback destroyCallback, void \*userData)](capi-ipc-cremote-object-h.md#oh_ipcremotestub_create) | - | 创建OHIPCRemoteStub对象。 |
| [void OH\_IPCRemoteStub\_Destroy(OHIPCRemoteStub \*stub)](capi-ipc-cremote-object-h.md#oh_ipcremotestub_destroy) | - | 销毁OHIPCRemoteStub对象。 |
| [void OH\_IPCRemoteProxy\_Destroy(OHIPCRemoteProxy \*proxy)](capi-ipc-cremote-object-h.md#oh_ipcremoteproxy_destroy) | - | 销毁OHIPCRemoteProxy对象。 |
| [int OH\_IPCRemoteProxy\_SendRequest(const OHIPCRemoteProxy \*proxy, uint32\_t code, const OHIPCParcel \*data, OHIPCParcel \*reply, const OH\_IPC\_MessageOption \*option)](capi-ipc-cremote-object-h.md#oh_ipcremoteproxy_sendrequest) | - | IPC消息发送函数。 |
| [int OH\_IPCRemoteProxy\_GetInterfaceDescriptor(OHIPCRemoteProxy \*proxy, char \*\*descriptor, int32\_t \*len, OH\_IPC\_MemAllocator allocator)](capi-ipc-cremote-object-h.md#oh_ipcremoteproxy_getinterfacedescriptor) | - | 从Stub端获取接口描述符。 |
| [typedef void (\*OH\_OnDeathRecipientCallback)(void \*userData)](capi-ipc-cremote-object-h.md#oh_ondeathrecipientcallback) | OH\_OnDeathRecipientCallback | 远端OHIPCRemoteStub对象死亡通知的回调函数类型。 |
| [typedef void (\*OH\_OnDeathRecipientDestroyCallback)(void \*userData)](capi-ipc-cremote-object-h.md#oh_ondeathrecipientdestroycallback) | OH\_OnDeathRecipientDestroyCallback | OH\_OnDeathRecipient对象销毁回调函数类型。 |
| [OHIPCDeathRecipient\* OH\_IPCDeathRecipient\_Create(OH\_OnDeathRecipientCallback deathRecipientCallback, OH\_OnDeathRecipientDestroyCallback destroyCallback, void \*userData)](capi-ipc-cremote-object-h.md#oh_ipcdeathrecipient_create) | - | 创建OHIPCDeathRecipient对象。 |
| [void OH\_IPCDeathRecipient\_Destroy(OHIPCDeathRecipient \*recipient)](capi-ipc-cremote-object-h.md#oh_ipcdeathrecipient_destroy) | - | 销毁OHIPCDeathRecipient对象。 |
| [int OH\_IPCRemoteProxy\_AddDeathRecipient(OHIPCRemoteProxy \*proxy, OHIPCDeathRecipient \*recipient)](capi-ipc-cremote-object-h.md#oh_ipcremoteproxy_adddeathrecipient) | - | 向OHIPCRemoteProxy对象添加死亡监听，用于接收远端OHIPCRemoteStub对象死亡的回调通知。 |
| [int OH\_IPCRemoteProxy\_RemoveDeathRecipient(OHIPCRemoteProxy \*proxy, OHIPCDeathRecipient \*recipient)](capi-ipc-cremote-object-h.md#oh_ipcremoteproxy_removedeathrecipient) | - | 移除向OHIPCRemoteProxy对象已经添加的死亡监听。 |
| [int OH\_IPCRemoteProxy\_IsRemoteDead(const OHIPCRemoteProxy \*proxy)](capi-ipc-cremote-object-h.md#oh_ipcremoteproxy_isremotedead) | - | 判断OHIPCRemoteProxy对象对应的远端OHIPCRemoteStub对象是否死亡。 |

## 枚举类型说明

PhonePC/2in1TabletTVWearable

### OH\_IPC\_RequestMode

PhonePC/2in1TabletTVWearable

```
1. enum OH_IPC_RequestMode
```

**描述：**

IPC请求模式定义。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| OH\_IPC\_REQUEST\_MODE\_SYNC = 0 | 同步请求模式。 |
| OH\_IPC\_REQUEST\_MODE\_ASYNC = 1 | 异步请求模式。 |

## 函数说明

PhonePC/2in1TabletTVWearable

### OH\_OnRemoteRequestCallback()

PhonePC/2in1TabletTVWearable

```
1. typedef int(*OH_OnRemoteRequestCallback)(uint32_t code, const OHIPCParcel *data, OHIPCParcel *reply, void *userData)
```

**描述：**

Stub端用于处理远端数据请求的回调函数。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 12

**参数:**

| 参数项 | 描述 |
| --- | --- |
| uint32\_t code | code 用户自定义通讯命令字，范围：[0x01, 0x00ffffff]。 |
| const [OHIPCParcel](capi-ohipcparcel.md) \*data | data 请求数据对象指针，不会为空，函数内不允许释放。 |
| [OHIPCParcel](capi-ohipcparcel.md) \*reply | reply 回应数据对象指针，不会为空，函数内不允许释放。如果函数返回错误，该值不允许写入数据。 |
| void \*userData | userData 用户私有数据，可以为空。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 成功返回[OH\_IPC\_ErrorCode#OH\_IPC\_SUCCESS](capi-ipc-error-code-h.md#oh_ipc_errorcode)；  否则返回用户自定义错误码或系统错误码，自定义错误码范围：[1909001, 1909999]；  如果用户自定义错误码超出范围，将返回[OH\_IPC\_ErrorCode#OH\_IPC\_INVALID\_USER\_ERROR\_CODE](capi-ipc-error-code-h.md#oh_ipc_errorcode)。 |

### OH\_OnRemoteDestroyCallback()

PhonePC/2in1TabletTVWearable

```
1. typedef void(*OH_OnRemoteDestroyCallback)(void *userData)
```

**描述：**

用于监听对象销毁的回调函数。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 12

**参数:**

| 参数项 | 描述 |
| --- | --- |
| void \*userData | userData 用户私有数据，可以为空。 |

### OH\_IPCRemoteStub\_Create()

PhonePC/2in1TabletTVWearable

```
1. OHIPCRemoteStub* OH_IPCRemoteStub_Create(const char *descriptor, OH_OnRemoteRequestCallback requestCallback, OH_OnRemoteDestroyCallback destroyCallback, void *userData)
```

**描述：**

创建OHIPCRemoteStub对象。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 12

**参数:**

| 参数项 | 描述 |
| --- | --- |
| const char \*descriptor | descriptor OHIPCRemoteStub对象描述符，不能为空。 |
| [OH\_OnRemoteRequestCallback](capi-ipc-cremote-object-h.md#oh_onremoterequestcallback) requestCallback | requestCallback 数据请求处理函数，不能为空。 |
| [OH\_OnRemoteDestroyCallback](capi-ipc-cremote-object-h.md#oh_onremotedestroycallback) destroyCallback | destroyCallback对象销毁回调函数，可以为空。 |
| void \*userData | userData用户私有数据，可以为空。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| OHIPCRemoteStub\* | 成功返回OHIPCRemoteStub对象指针，否则返回NULL。 |

### OH\_IPCRemoteStub\_Destroy()

PhonePC/2in1TabletTVWearable

```
1. void OH_IPCRemoteStub_Destroy(OHIPCRemoteStub *stub)
```

**描述：**

销毁OHIPCRemoteStub对象。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 12

**参数:**

| 参数项 | 描述 |
| --- | --- |
| [OHIPCRemoteStub](capi-ohipcparcel-ohipcremotestub.md) \*stub | stub 要销毁的OHIPCRemoteStub对象指针。 |

### OH\_IPCRemoteProxy\_Destroy()

PhonePC/2in1TabletTVWearable

```
1. void OH_IPCRemoteProxy_Destroy(OHIPCRemoteProxy *proxy)
```

**描述：**

销毁OHIPCRemoteProxy对象。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 12

**参数:**

| 参数项 | 描述 |
| --- | --- |
| [OHIPCRemoteProxy](capi-ohipcparcel-ohipcremoteproxy.md) \*proxy | proxy 要销毁的OHIPCRemoteProxy对象指针。 |

### OH\_IPCRemoteProxy\_SendRequest()

PhonePC/2in1TabletTVWearable

```
1. int OH_IPCRemoteProxy_SendRequest(const OHIPCRemoteProxy *proxy, uint32_t code, const OHIPCParcel *data, OHIPCParcel *reply, const OH_IPC_MessageOption *option)
```

**描述：**

IPC消息发送函数。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 12

**参数:**

| 参数项 | 描述 |
| --- | --- |
| const [OHIPCRemoteProxy](capi-ohipcparcel-ohipcremoteproxy.md) \*proxy | proxy OHIPCRemoteProxy对象指针，不能为空。 |
| uint32\_t code | code 用户定义的IPC命令字，范围：[0x01, 0x00ffffff]。 |
| const [OHIPCParcel](capi-ohipcparcel.md) \*data | data 请求数据对象指针，不能为空。 |
| [OHIPCParcel](capi-ohipcparcel.md) \*reply | reply 回应数据对象指针，同步请求时，不能为空；异步请求时，可以为空。 |
| const [OH\_IPC\_MessageOption](capi-ohipcremoteobject-oh-ipc-messageoption.md) \*option | option消息选项指针，可以为空，为空时按同步处理。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 发送成功返回[OH\_IPC\_ErrorCode#OH\_IPC\_SUCCESS](capi-ipc-error-code-h.md#oh_ipc_errorcode)；  参数不合法时返回[OH\_IPC\_ErrorCode#OH\_IPC\_CHECK\_PARAM\_ERROR](capi-ipc-error-code-h.md#oh_ipc_errorcode)；  远端OHIPCRemoteStub对象死亡返回[OH\_IPC\_ErrorCode#OH\_IPC\_DEAD\_REMOTE\_OBJECT](capi-ipc-error-code-h.md#oh_ipc_errorcode)；  code超出范围返回[OH\_IPC\_ErrorCode#OH\_IPC\_CODE\_OUT\_OF\_RANGE](capi-ipc-error-code-h.md#oh_ipc_errorcode)；  其它返回[OH\_IPC\_ErrorCode#OH\_IPC\_INNER\_ERROR](capi-ipc-error-code-h.md#oh_ipc_errorcode)或用户自定义错误码。 |

### OH\_IPCRemoteProxy\_GetInterfaceDescriptor()

PhonePC/2in1TabletTVWearable

```
1. int OH_IPCRemoteProxy_GetInterfaceDescriptor(OHIPCRemoteProxy *proxy, char **descriptor, int32_t *len, OH_IPC_MemAllocator allocator)
```

**描述：**

从Stub端获取接口描述符。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 12

**参数:**

| 参数项 | 描述 |
| --- | --- |
| [OHIPCRemoteProxy](capi-ohipcparcel-ohipcremoteproxy.md) \*proxy | proxy OHIPCRemoteProxy对象指针，不能为空。 |
| char \*\*descriptor | descriptor 用于存储描述符的内存地址，该内存由用户提供的分配器进行内存分配，用户使用完后需要主动释放，不能为空。 接口返回失败时，用户依然需要判断该内存是否为空，并主动释放，否则会造成内存泄漏。 |
| int32\_t \*len | len 写入descriptor的数据长度，包含结束符，不能为空。 |
| [OH\_IPC\_MemAllocator](capi-ipc-cparcel-h.md#oh_ipc_memallocator) allocator | allocator 用户指定的用来分配descriptor的内存分配器，不能为空。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 发送成功返回[OH\_IPC\_ErrorCode#OH\_IPC\_SUCCESS](capi-ipc-error-code-h.md#oh_ipc_errorcode)；  参数错误返回[OH\_IPC\_ErrorCode#OH\_IPC\_CHECK\_PARAM\_ERROR](capi-ipc-error-code-h.md#oh_ipc_errorcode)；  远端OHIPCRemoteStub对象死亡返回[OH\_IPC\_ErrorCode#OH\_IPC\_DEAD\_REMOTE\_OBJECT](capi-ipc-error-code-h.md#oh_ipc_errorcode)；  内存分配失败返回[OH\_IPC\_ErrorCode#OH\_IPC\_MEM\_ALLOCATOR\_ERROR](capi-ipc-error-code-h.md#oh_ipc_errorcode)；  序列化读失败返回[OH\_IPC\_ErrorCode#OH\_IPC\_PARCEL\_READ\_ERROR](capi-ipc-error-code-h.md#oh_ipc_errorcode)或用户自定义错误码。 |

### OH\_OnDeathRecipientCallback()

PhonePC/2in1TabletTVWearable

```
1. typedef void (*OH_OnDeathRecipientCallback)(void *userData)
```

**描述：**

远端OHIPCRemoteStub对象死亡通知的回调函数类型。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 12

**参数:**

| 参数项 | 描述 |
| --- | --- |
| void \*userData | userData 用户私有数据指针，可以为空。 |

### OH\_OnDeathRecipientDestroyCallback()

PhonePC/2in1TabletTVWearable

```
1. typedef void (*OH_OnDeathRecipientDestroyCallback)(void *userData)
```

**描述：**

OHIPCDeathRecipient对象销毁回调函数类型。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 12

**参数:**

| 参数项 | 描述 |
| --- | --- |
| void \*userData | userData 用户私有数据指针，可以为空。 |

### OH\_IPCDeathRecipient\_Create()

PhonePC/2in1TabletTVWearable

```
1. OHIPCDeathRecipient* OH_IPCDeathRecipient_Create(OH_OnDeathRecipientCallback deathRecipientCallback, OH_OnDeathRecipientDestroyCallback destroyCallback, void *userData)
```

**描述：**

创建远端OHIPCRemoteStub对象死亡通知对象OHIPCDeathRecipient。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 12

**参数:**

| 参数项 | 描述 |
| --- | --- |
| [OH\_OnDeathRecipientCallback](capi-ipc-cremote-object-h.md#oh_ondeathrecipientcallback) deathRecipientCallback | deathRecipientCallback 远端OHIPCRemoteStub对象死亡通知的回调处理函数，不能为空。 |
| [OH\_OnDeathRecipientDestroyCallback](capi-ipc-cremote-object-h.md#oh_ondeathrecipientdestroycallback) destroyCallback | destroyCallback 对象销毁回调处理函数，可以为空。 |
| void \*userData | userData 用户私有数据指针，可以为空。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| OHIPCDeathRecipient\* | 成功返回OHIPCDeathRecipient对象指针；否则返回NULL。 |

### OH\_IPCDeathRecipient\_Destroy()

PhonePC/2in1TabletTVWearable

```
1. void OH_IPCDeathRecipient_Destroy(OHIPCDeathRecipient *recipient)
```

**描述：**

销毁OHIPCDeathRecipient对象。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 12

**参数:**

| 参数项 | 描述 |
| --- | --- |
| [OHIPCDeathRecipient](capi-ohipcremoteobject-ohipcdeathrecipient.md) \*recipient | recipient 要销毁的OHIPCDeathRecipient对象指针。 |

### OH\_IPCRemoteProxy\_AddDeathRecipient()

PhonePC/2in1TabletTVWearable

```
1. int OH_IPCRemoteProxy_AddDeathRecipient(OHIPCRemoteProxy *proxy, OHIPCDeathRecipient *recipient)
```

**描述：**

向OHIPCRemoteProxy对象添加死亡监听，用于接收远端OHIPCRemoteStub对象死亡的回调通知。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 12

**参数:**

| 参数项 | 描述 |
| --- | --- |
| [OHIPCRemoteProxy](capi-ohipcparcel-ohipcremoteproxy.md) \*proxy | proxy 需要添加死亡通知的OHIPCRemoteProxy对象指针，不能为空。 |
| [OHIPCDeathRecipient](capi-ohipcremoteobject-ohipcdeathrecipient.md) \*recipient | recipient 用于接收远程对象死亡通知的死亡对象指针，不能为空。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 成功返回[OH\_IPC\_ErrorCode#OH\_IPC\_SUCCESS](capi-ipc-error-code-h.md#oh_ipc_errorcode)；  参数错误返回[OH\_IPC\_ErrorCode#OH\_IPC\_CHECK\_PARAM\_ERROR](capi-ipc-error-code-h.md#oh_ipc_errorcode)；  其它返回[OH\_IPC\_ErrorCode#OH\_IPC\_INNER\_ERROR](capi-ipc-error-code-h.md#oh_ipc_errorcode)。 |

### OH\_IPCRemoteProxy\_RemoveDeathRecipient()

PhonePC/2in1TabletTVWearable

```
1. int OH_IPCRemoteProxy_RemoveDeathRecipient(OHIPCRemoteProxy *proxy, OHIPCDeathRecipient *recipient)
```

**描述：**

移除向OHIPCRemoteProxy对象已经添加的死亡监听。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 12

**参数:**

| 参数项 | 描述 |
| --- | --- |
| [OHIPCRemoteProxy](capi-ohipcparcel-ohipcremoteproxy.md) \*proxy | proxy 需要移除死亡通知的OHIPCRemoteProxy对象指针，不能为空。 |
| [OHIPCDeathRecipient](capi-ohipcremoteobject-ohipcdeathrecipient.md) \*recipient | recipient用于接收远程对象死亡通知的死亡对象指针，不能为空。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 成功返回[OH\_IPC\_ErrorCode#OH\_IPC\_SUCCESS](capi-ipc-error-code-h.md#oh_ipc_errorcode)；  参数错误返回[OH\_IPC\_ErrorCode#OH\_IPC\_CHECK\_PARAM\_ERROR](capi-ipc-error-code-h.md#oh_ipc_errorcode)；  其它返回[OH\_IPC\_ErrorCode#OH\_IPC\_INNER\_ERROR](capi-ipc-error-code-h.md#oh_ipc_errorcode)。 |

### OH\_IPCRemoteProxy\_IsRemoteDead()

PhonePC/2in1TabletTVWearable

```
1. int OH_IPCRemoteProxy_IsRemoteDead(const OHIPCRemoteProxy *proxy)
```

**描述：**

判断OHIPCRemoteProxy对象对应的远端OHIPCRemoteStub对象是否死亡。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 12

**参数:**

| 参数项 | 描述 |
| --- | --- |
| const [OHIPCRemoteProxy](capi-ohipcparcel-ohipcremoteproxy.md) \*proxy | proxy 需要判断远端是否死亡的OHIPCRemoteProxy对象指针，不能为空。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 远端OHIPCRemoteStub对象死亡返回1；否则，返回0。参数非法时，说明其远端OHIPCRemoteStub对象不存在，返回1。 |
