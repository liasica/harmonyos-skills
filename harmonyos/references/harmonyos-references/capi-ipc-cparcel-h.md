---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ipc-cparcel-h
title: ipc_cparcel.h
breadcrumb: API参考 > 应用框架 > IPC Kit（进程间通信服务） > C API > 头文件 > ipc_cparcel.h
category: harmonyos-references
scraped_at: 2026-09-02T15:01:37+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:544376a8b7b63de8b191ea801f29bf0cdde25223e2e7304dcc2ba8c3780d8d28
---

## 概述

提供IPC序列化/反序列化C接口，用于在IPC通信过程中对数据进行序列化和反序列化操作。

对应的开发指南及样例可参考[IPC与RPC通信开发指导(C/C++)](../harmonyos-guides/ipc-capi-development-guideline.md)。

**引用文件：** <IPCKit/ipc\_cparcel.h>

**库：** libipc\_capi.so

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 12

**相关模块：**[OHIPCParcel](capi-ohipcparcel.md)

## 汇总

### 结构体

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [OHIPCParcel](capi-ohipcparcel-ohipcparcel.md) | OHIPCParcel | IPC序列化对象。 |
| [OHIPCRemoteProxy](capi-ohipcparcel-ohipcremoteproxy.md) | OHIPCRemoteProxy | IPC远端代理对象。 |
| [OHIPCRemoteStub](capi-ohipcparcel-ohipcremotestub.md) | OHIPCRemoteStub | IPC远端服务对象。 |

### 函数

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [typedef void\* (\*OH\_IPC\_MemAllocator)(int32\_t len)](capi-ipc-cparcel-h.md#oh_ipc_memallocator) | [OH\_IPC\_MemAllocator](capi-ipc-cparcel-h.md#oh_ipc_memallocator) | 内存分配函数类型。 |
| [OHIPCParcel\* OH\_IPCParcel\_Create(void)](capi-ipc-cparcel-h.md#oh_ipcparcel_create) | - | 创建OHIPCParcel对象，对象可序列化大小不能超过204800字节。 |
| [void OH\_IPCParcel\_Destroy(OHIPCParcel \*parcel)](capi-ipc-cparcel-h.md#oh_ipcparcel_destroy) | - | 销毁OHIPCParcel对象。 |
| [int OH\_IPCParcel\_GetDataSize(const OHIPCParcel \*parcel)](capi-ipc-cparcel-h.md#oh_ipcparcel_getdatasize) | - | 获取OHIPCParcel对象包含的数据的大小。 |
| [int OH\_IPCParcel\_GetWritableBytes(const OHIPCParcel \*parcel)](capi-ipc-cparcel-h.md#oh_ipcparcel_getwritablebytes) | - | 获取OHIPCParcel对象可以写入的字节数。 |
| [int OH\_IPCParcel\_GetReadableBytes(const OHIPCParcel \*parcel)](capi-ipc-cparcel-h.md#oh_ipcparcel_getreadablebytes) | - | 获取OHIPCParcel对象还可以读取的字节数。 |
| [int OH\_IPCParcel\_GetReadPosition(const OHIPCParcel \*parcel)](capi-ipc-cparcel-h.md#oh_ipcparcel_getreadposition) | - | 获取OHIPCParcel对象当前读取位置。 |
| [int OH\_IPCParcel\_GetWritePosition(const OHIPCParcel \*parcel)](capi-ipc-cparcel-h.md#oh_ipcparcel_getwriteposition) | - | 获取OHIPCParcel对象当前写入位置。 |
| [int OH\_IPCParcel\_RewindReadPosition(OHIPCParcel \*parcel, uint32\_t newReadPos)](capi-ipc-cparcel-h.md#oh_ipcparcel_rewindreadposition) | - | 重置OHIPCParcel对象读取位置。 |
| [int OH\_IPCParcel\_RewindWritePosition(OHIPCParcel \*parcel, uint32\_t newWritePos)](capi-ipc-cparcel-h.md#oh_ipcparcel_rewindwriteposition) | - | 重置OHIPCParcel对象写入位置。 |
| [int OH\_IPCParcel\_WriteInt8(OHIPCParcel \*parcel, int8\_t value)](capi-ipc-cparcel-h.md#oh_ipcparcel_writeint8) | - | 向OHIPCParcel对象写入一个int8\_t值。 |
| [int OH\_IPCParcel\_ReadInt8(const OHIPCParcel \*parcel, int8\_t \*value)](capi-ipc-cparcel-h.md#oh_ipcparcel_readint8) | - | 从OHIPCParcel对象中读取一个int8\_t值。 |
| [int OH\_IPCParcel\_WriteInt16(OHIPCParcel \*parcel, int16\_t value)](capi-ipc-cparcel-h.md#oh_ipcparcel_writeint16) | - | 向OHIPCParcel对象写入一个int16\_t值。 |
| [int OH\_IPCParcel\_ReadInt16(const OHIPCParcel \*parcel, int16\_t \*value)](capi-ipc-cparcel-h.md#oh_ipcparcel_readint16) | - | 从OHIPCParcel对象中读取一个int16\_t值。 |
| [int OH\_IPCParcel\_WriteInt32(OHIPCParcel \*parcel, int32\_t value)](capi-ipc-cparcel-h.md#oh_ipcparcel_writeint32) | - | 向OHIPCParcel对象写入一个int32\_t值。 |
| [int OH\_IPCParcel\_ReadInt32(const OHIPCParcel \*parcel, int32\_t \*value)](capi-ipc-cparcel-h.md#oh_ipcparcel_readint32) | - | 从OHIPCParcel对象中读取一个int32\_t值。 |
| [int OH\_IPCParcel\_WriteInt64(OHIPCParcel \*parcel, int64\_t value)](capi-ipc-cparcel-h.md#oh_ipcparcel_writeint64) | - | 向OHIPCParcel对象写入一个int64\_t值。 |
| [int OH\_IPCParcel\_ReadInt64(const OHIPCParcel \*parcel, int64\_t \*value)](capi-ipc-cparcel-h.md#oh_ipcparcel_readint64) | - | 从OHIPCParcel对象中读取一个int64\_t值。 |
| [int OH\_IPCParcel\_WriteUint8(OHIPCParcel \*parcel, uint8\_t value)](capi-ipc-cparcel-h.md#oh_ipcparcel_writeuint8) | - | 向OHIPCParcel对象写入一个uint8\_t值。 |
| [int OH\_IPCParcel\_ReadUint8(const OHIPCParcel \*parcel, uint8\_t \*value)](capi-ipc-cparcel-h.md#oh_ipcparcel_readuint8) | - | 从OHIPCParcel对象中读取一个uint8\_t值。 |
| [int OH\_IPCParcel\_WriteUint16(OHIPCParcel \*parcel, uint16\_t value)](capi-ipc-cparcel-h.md#oh_ipcparcel_writeuint16) | - | 向OHIPCParcel对象写入一个uint16\_t值。 |
| [int OH\_IPCParcel\_ReadUint16(const OHIPCParcel \*parcel, uint16\_t \*value)](capi-ipc-cparcel-h.md#oh_ipcparcel_readuint16) | - | 从OHIPCParcel对象中读取一个uint16\_t值。 |
| [int OH\_IPCParcel\_WriteUint32(OHIPCParcel \*parcel, uint32\_t value)](capi-ipc-cparcel-h.md#oh_ipcparcel_writeuint32) | - | 向OHIPCParcel对象写入一个uint32\_t值。 |
| [int OH\_IPCParcel\_ReadUint32(const OHIPCParcel \*parcel, uint32\_t \*value)](capi-ipc-cparcel-h.md#oh_ipcparcel_readuint32) | - | 从OHIPCParcel对象中读取一个uint32\_t值。 |
| [int OH\_IPCParcel\_WriteUint64(OHIPCParcel \*parcel, uint64\_t value)](capi-ipc-cparcel-h.md#oh_ipcparcel_writeuint64) | - | 向OHIPCParcel对象写入一个uint64\_t值。 |
| [int OH\_IPCParcel\_ReadUint64(const OHIPCParcel \*parcel, uint64\_t \*value)](capi-ipc-cparcel-h.md#oh_ipcparcel_readuint64) | - | 从OHIPCParcel对象中读取一个uint64\_t值。 |
| [int OH\_IPCParcel\_WriteFloat(OHIPCParcel \*parcel, float value)](capi-ipc-cparcel-h.md#oh_ipcparcel_writefloat) | - | 向OHIPCParcel对象写入一个float值。 |
| [int OH\_IPCParcel\_ReadFloat(const OHIPCParcel \*parcel, float \*value)](capi-ipc-cparcel-h.md#oh_ipcparcel_readfloat) | - | 从OHIPCParcel对象中读取一个float值。 |
| [int OH\_IPCParcel\_WriteDouble(OHIPCParcel \*parcel, double value)](capi-ipc-cparcel-h.md#oh_ipcparcel_writedouble) | - | 向OHIPCParcel对象写入一个double值。 |
| [int OH\_IPCParcel\_ReadDouble(const OHIPCParcel \*parcel, double \*value)](capi-ipc-cparcel-h.md#oh_ipcparcel_readdouble) | - | 从OHIPCParcel对象中读取一个double值。 |
| [int OH\_IPCParcel\_WriteString(OHIPCParcel \*parcel, const char \*str)](capi-ipc-cparcel-h.md#oh_ipcparcel_writestring) | - | 向OHIPCParcel对象写入字符串，包含字符串结束符。 |
| [const char\* OH\_IPCParcel\_ReadString(const OHIPCParcel \*parcel)](capi-ipc-cparcel-h.md#oh_ipcparcel_readstring) | - | 从OHIPCParcel对象读取字符串，用户可通过strlen获取字符串长度。 |
| [int OH\_IPCParcel\_WriteBuffer(OHIPCParcel \*parcel, const uint8\_t \*buffer, int32\_t len)](capi-ipc-cparcel-h.md#oh_ipcparcel_writebuffer) | - | 向OHIPCParcel对象写入指定长度的内存信息。 |
| [const uint8\_t\* OH\_IPCParcel\_ReadBuffer(const OHIPCParcel \*parcel, int32\_t len)](capi-ipc-cparcel-h.md#oh_ipcparcel_readbuffer) | - | 从OHIPCParcel对象读取指定长度的内存信息。 |
| [int OH\_IPCParcel\_WriteRemoteStub(OHIPCParcel \*parcel, const OHIPCRemoteStub \*stub)](capi-ipc-cparcel-h.md#oh_ipcparcel_writeremotestub) | - | 向OHIPCParcel对象写入OHIPCRemoteStub对象。 |
| [OHIPCRemoteStub\* OH\_IPCParcel\_ReadRemoteStub(const OHIPCParcel \*parcel)](capi-ipc-cparcel-h.md#oh_ipcparcel_readremotestub) | - | 从OHIPCParcel对象读取OHIPCRemoteStub对象。 |
| [int OH\_IPCParcel\_WriteRemoteProxy(OHIPCParcel \*parcel, const OHIPCRemoteProxy \*proxy)](capi-ipc-cparcel-h.md#oh_ipcparcel_writeremoteproxy) | - | 向OHIPCParcel对象写入OHIPCRemoteProxy对象。 |
| [OHIPCRemoteProxy\* OH\_IPCParcel\_ReadRemoteProxy(const OHIPCParcel \*parcel)](capi-ipc-cparcel-h.md#oh_ipcparcel_readremoteproxy) | - | 从OHIPCParcel对象读取OHIPCRemoteProxy对象。 |
| [int OH\_IPCParcel\_WriteFileDescriptor(OHIPCParcel \*parcel, int32\_t fd)](capi-ipc-cparcel-h.md#oh_ipcparcel_writefiledescriptor) | - | 向OHIPCParcel对象写入文件描述符。 |
| [int OH\_IPCParcel\_ReadFileDescriptor(const OHIPCParcel \*parcel, int32\_t \*fd)](capi-ipc-cparcel-h.md#oh_ipcparcel_readfiledescriptor) | - | 从OHIPCParcel对象读取文件描述符。 |
| [int OH\_IPCParcel\_Append(OHIPCParcel \*parcel, const OHIPCParcel \*data)](capi-ipc-cparcel-h.md#oh_ipcparcel_append) | - | OHIPCParcel对象数据拼接。 |
| [int OH\_IPCParcel\_WriteInterfaceToken(OHIPCParcel \*parcel, const char \*token)](capi-ipc-cparcel-h.md#oh_ipcparcel_writeinterfacetoken) | - | 向OHIPCParcel对象写入接口描述符，用于接口身份校验。 |
| [int OH\_IPCParcel\_ReadInterfaceToken(const OHIPCParcel \*parcel, char \*\*token, int32\_t \*len, OH\_IPC\_MemAllocator allocator)](capi-ipc-cparcel-h.md#oh_ipcparcel_readinterfacetoken) | - | 从OHIPCParcel对象读取接口描述符信息，用于接口身份校验。 |

## 函数说明

### OH\_IPC\_MemAllocator()

```c
typedef void* (*OH_IPC_MemAllocator)(int32_t len)
```

**描述：**

内存分配函数类型，用于IPC通信中自定义内存分配策略。常用于需要特殊内存管理的场景，例如：共享内存传输、内存池管理、限制内存使用上限等。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| int32\_t len | 申请内存的长度，单位：字节。取值原则：必须大于0。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| void\* | 成功返回分配的内存地址；失败返回NULL。 |

### OH\_IPCParcel\_Create()

```c
OHIPCParcel* OH_IPCParcel_Create(void)
```

**描述：**

创建OHIPCParcel对象，用于IPC通信中的数据序列化。

调用此函数：

* 在内存中分配并初始化一个OHIPCParcel对象。
* 对象初始状态为空，对象可序列化大小不能超过204800字节。
* 返回对象指针用于后续的数据读写操作。
* 不支持多线程并发访问同一对象。
* 典型使用流程：[OH\_IPCParcel\_Create](capi-ipc-cparcel-h.md#oh_ipcparcel_create) → 数据读写操作 → [OH\_IPCParcel\_Destroy](capi-ipc-cparcel-h.md#oh_ipcparcel_destroy)。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 12

**返回：**

| 类型 | 说明 |
| --- | --- |
| OHIPCParcel\* | 成功返回OHIPCParcel对象指针；失败返回NULL。 |

### OH\_IPCParcel\_Destroy()

```c
void OH_IPCParcel_Destroy(OHIPCParcel *parcel)
```

**描述：**

销毁OHIPCParcel对象。

调用此函数：

* 释放OHIPCParcel对象占用的内存缓冲区。
* 清除对象内部的所有数据。释放对象自身的内存。
* 传入的指针将变为无效指针，不应再被使用。
* 使用前检查：确保没有其他线程正在使用该对象。
* 指针置空：销毁后建议将指针置为NULL，避免悬垂指针。
* 必须与[OH\_IPCParcel\_Create](capi-ipc-cparcel-h.md#oh_ipcparcel_create)方法配对使用。
* 销毁时机：确保已读取完所有需要的数据后再销毁。
* 多次销毁：禁止对同一对象多次调用销毁函数。
* 只能销毁由[OH\_IPCParcel\_Create](capi-ipc-cparcel-h.md#oh_ipcparcel_create)创建的对象。
* 销毁后不能再访问该对象。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OHIPCParcel](capi-ohipcparcel.md) \*parcel | 需要销毁OHIPCParcel对象的指针，不能为空。 |

### OH\_IPCParcel\_GetDataSize()

```c
int OH_IPCParcel_GetDataSize(const OHIPCParcel *parcel)
```

**描述：**

获取OHIPCParcel对象包含的数据的大小。常用于监控数据传输进度、检查是否超过IPC序列化大小限制、调试数据读写过程等场景。

调用此函数：

* 计算Parcel对象中已写入数据的总字节数。
* 返回已写入数据的总大小值。
* 保持读写位置和数据内容不变。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [OHIPCParcel](capi-ohipcparcel.md) \*parcel | OHIPCParcel对象的指针，不能为空。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回Parcel对象已写入数据的累计大小，单位：字节，参数不合法时返回-1。 |

### OH\_IPCParcel\_GetWritableBytes()

```c
int OH_IPCParcel_GetWritableBytes(const OHIPCParcel *parcel)
```

**描述：**

获取OHIPCParcel对象可以写入的字节数。常用于检查是否还有空间写入更多数据、防止写入溢出、批量写入前预检查等场景。

调用此函数：

* 计算Parcel对象剩余可写入空间的大小。
* 返回可写字节数值。
* 不改变Parcel对象的读写位置或数据内容。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [OHIPCParcel](capi-ohipcparcel.md) \*parcel | OHIPCParcel对象的指针，不能为空。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回可写字节数大小，单位：字节，参数不合法时返回-1。 |

### OH\_IPCParcel\_GetReadableBytes()

```c
int OH_IPCParcel_GetReadableBytes(const OHIPCParcel *parcel)
```

**描述：**

获取OHIPCParcel对象还可以读取的字节数。常用于检查还有多少数据可读、循环读取数据、调试数据读取过程等场景。

调用此函数：

* 计算Parcel对象中未读取数据的字节数。
* 返回可读字节数值。
* 不改变Parcel对象的读写位置或数据内容。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [OHIPCParcel](capi-ohipcparcel.md) \*parcel | OHIPCParcel对象的指针，不能为空。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回可读字节数大小，单位：字节，参数不合法时返回-1。 |

### OH\_IPCParcel\_GetReadPosition()

```c
int OH_IPCParcel_GetReadPosition(const OHIPCParcel *parcel)
```

**描述：**

获取OHIPCParcel对象当前读取位置。常用于记录读取位置以便后续恢复、配合RewindReadPosition实现重复读取、调试数据读取进度等场景。

调用此函数：

* 返回Parcel对象当前的读取位置值。
* 不改变读取位置或数据内容。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [OHIPCParcel](capi-ohipcparcel.md) \*parcel | OHIPCParcel对象的指针，不能为空。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回当前读位置，单位：字节，参数不合法时返回-1。 |

### OH\_IPCParcel\_GetWritePosition()

```c
int OH_IPCParcel_GetWritePosition(const OHIPCParcel *parcel)
```

**描述：**

获取OHIPCParcel对象当前写入位置。常用于记录写入位置、配合RewindWritePosition修正写入错误、调试数据写入进度等场景。

调用此函数：

* 返回Parcel对象当前的写入位置值。
* 不改变写入位置或数据内容。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [OHIPCParcel](capi-ohipcparcel.md) \*parcel | OHIPCParcel对象的指针，不能为空。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回当前写入位置，单位：字节。参数不合法时返回-1。 |

### OH\_IPCParcel\_RewindReadPosition()

```c
int OH_IPCParcel_RewindReadPosition(OHIPCParcel *parcel, uint32_t newReadPos)
```

**描述：**

重置OHIPCParcel对象的读取位置到指定位置。常用于需要重复解析数据的场景。

调用此函数：

* 读取位置指针移动到newReadPos指定的位置，必须在[0, 当前数据大小]范围内。
* 已写入的数据保持不变。
* 后续读取操作从新位置开始。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OHIPCParcel](capi-ohipcparcel.md) \*parcel | OHIPCParcel对象的指针，不能为空。 |
| uint32\_t newReadPos | 新的读取位置，范围：[0，当前数据大小]，单位：字节。超出范围时返回OH\_IPC\_CHECK\_PARAM\_ERROR错误。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 成功返回[OH\_IPC\_ErrorCode#OH\_IPC\_SUCCESS](capi-ipc-error-code-h.md#oh_ipc_errorcode)；  参数不合法时返回[OH\_IPC\_ErrorCode#OH\_IPC\_CHECK\_PARAM\_ERROR](capi-ipc-error-code-h.md#oh_ipc_errorcode)。 |

### OH\_IPCParcel\_RewindWritePosition()

```c
int OH_IPCParcel_RewindWritePosition(OHIPCParcel *parcel, uint32_t newWritePos)
```

**描述：**

重置OHIPCParcel对象的写入位置到指定位置。常用于写入数据后发现前序数据错误需要修正、实现数据的分段重写、撤销部分写入操作等场景。

调用此函数：

* 写入位置指针移动到newWritePos指定的位置，必须在[0, 当前数据大小]范围内。
* 重置位置可能导致部分数据被覆盖或无效，需谨慎使用。
* 后续写入操作从新位置开始。
* 重置写入位置不影响读取位置。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OHIPCParcel](capi-ohipcparcel.md) \*parcel | OHIPCParcel对象的指针，不能为空。 |
| uint32\_t newWritePos | 新的写入位置，范围：[0, 当前数据大小]，单位：字节。超出范围时返回OH\_IPC\_CHECK\_PARAM\_ERROR错误。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 成功返回[OH\_IPC\_ErrorCode#OH\_IPC\_SUCCESS](capi-ipc-error-code-h.md#oh_ipc_errorcode)；  参数不合法时返回[OH\_IPC\_ErrorCode#OH\_IPC\_CHECK\_PARAM\_ERROR](capi-ipc-error-code-h.md#oh_ipc_errorcode)。 |

### OH\_IPCParcel\_WriteInt8()

```c
int OH_IPCParcel_WriteInt8(OHIPCParcel *parcel, int8_t value)
```

**描述：**

向OHIPCParcel写入一个int8\_t值。不支持多线程并发访问同一对象。写入数据受IPC序列化总大小限制（参见[OH\_IPCParcel\_Create](capi-ipc-cparcel-h.md#oh_ipcparcel_create)）。

* 必须与[OH\_IPCParcel\_ReadInt8](capi-ipc-cparcel-h.md#oh_ipcparcel_readint8)方法配对使用。
* 调用顺序：先调用OH\_IPCParcel\_WriteInt()写入数据，接收端再调用[OH\_IPCParcel\_ReadInt8](capi-ipc-cparcel-h.md#oh_ipcparcel_readint8)读取数据。
* 未正确配对：如果未按顺序调用或读取类型不匹配，会导致读取失败或数据错误。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OHIPCParcel](capi-ohipcparcel.md) \*parcel | OHIPCParcel对象的指针，不能为空。 |
| int8\_t value | 要写入的int8\_t数据值，用于IPC通信数据序列化。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 成功返回[OH\_IPC\_ErrorCode#OH\_IPC\_SUCCESS](capi-ipc-error-code-h.md#oh_ipc_errorcode)；  参数不合法时返回[OH\_IPC\_ErrorCode#OH\_IPC\_CHECK\_PARAM\_ERROR](capi-ipc-error-code-h.md#oh_ipc_errorcode)；  写入失败返回[OH\_IPC\_ErrorCode#OH\_IPC\_PARCEL\_WRITE\_ERROR](capi-ipc-error-code-h.md#oh_ipc_errorcode)。 |

### OH\_IPCParcel\_ReadInt8()

```c
int OH_IPCParcel_ReadInt8(const OHIPCParcel *parcel, int8_t *value)
```

**描述：**

从OHIPCParcel对象中读取int8\_t值。不支持多线程并发访问同一对象。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [OHIPCParcel](capi-ohipcparcel.md) \*parcel | OHIPCParcel对象的指针，不能为空。 |
| int8\_t \*value | 用于存储读取到的int8\_t数据的指针，不能为空。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 成功返回[OH\_IPC\_ErrorCode#OH\_IPC\_SUCCESS](capi-ipc-error-code-h.md#oh_ipc_errorcode)；  参数不合法时返回[OH\_IPC\_ErrorCode#OH\_IPC\_CHECK\_PARAM\_ERROR](capi-ipc-error-code-h.md#oh_ipc_errorcode)；  读取失败返回[OH\_IPC\_ErrorCode#OH\_IPC\_PARCEL\_READ\_ERROR](capi-ipc-error-code-h.md#oh_ipc_errorcode)。 |

### OH\_IPCParcel\_WriteInt16()

```c
int OH_IPCParcel_WriteInt16(OHIPCParcel *parcel, int16_t value)
```

**描述：**

向OHIPCParcel对象写入int16\_t值。写入数据受IPC序列化总大小限制（参见[OH\_IPCParcel\_Create](capi-ipc-cparcel-h.md#oh_ipcparcel_create)）。

* 必须与[OH\_IPCParcel\_ReadInt16](capi-ipc-cparcel-h.md#oh_ipcparcel_readint16)方法配对使用。
* 调用顺序：先调用OH\_IPCParcel\_WriteInt16()写入数据，接收端再调用[OH\_IPCParcel\_ReadInt16](capi-ipc-cparcel-h.md#oh_ipcparcel_readint16)读取数据。
* 未正确配对：如果未按顺序调用或读取类型不匹配，会导致读取失败或数据错误。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OHIPCParcel](capi-ohipcparcel.md) \*parcel | OHIPCParcel对象的指针，不能为空。 |
| int16\_t value | 要写入的int16\_t数据值，用于IPC通信数据序列化。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 成功返回[OH\_IPC\_ErrorCode#OH\_IPC\_SUCCESS](capi-ipc-error-code-h.md#oh_ipc_errorcode)；  参数不合法时返回[OH\_IPC\_ErrorCode#OH\_IPC\_CHECK\_PARAM\_ERROR](capi-ipc-error-code-h.md#oh_ipc_errorcode)；  写入失败返回[OH\_IPC\_ErrorCode#OH\_IPC\_PARCEL\_WRITE\_ERROR](capi-ipc-error-code-h.md#oh_ipc_errorcode)。 |

### OH\_IPCParcel\_ReadInt16()

```c
int OH_IPCParcel_ReadInt16(const OHIPCParcel *parcel, int16_t *value)
```

**描述：**

从OHIPCParcel对象读取int16\_t值。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [OHIPCParcel](capi-ohipcparcel.md) \*parcel | OHIPCParcel对象的指针，不能为空。 |
| int16\_t \*value | 用于存储读取到的int16\_t数据的指针，不能为空。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 成功返回[OH\_IPC\_ErrorCode#OH\_IPC\_SUCCESS](capi-ipc-error-code-h.md#oh_ipc_errorcode)；  参数不合法时返回[OH\_IPC\_ErrorCode#OH\_IPC\_CHECK\_PARAM\_ERROR](capi-ipc-error-code-h.md#oh_ipc_errorcode)；  读取失败返回[OH\_IPC\_ErrorCode#OH\_IPC\_PARCEL\_READ\_ERROR](capi-ipc-error-code-h.md#oh_ipc_errorcode)。 |

### OH\_IPCParcel\_WriteInt32()

```c
int OH_IPCParcel_WriteInt32(OHIPCParcel *parcel, int32_t value)
```

**描述：**

向OHIPCParcel对象写入int32\_t值。写入数据受IPC序列化总大小限制（参见[OH\_IPCParcel\_Create](capi-ipc-cparcel-h.md#oh_ipcparcel_create)）。

* 必须与[OH\_IPCParcel\_ReadInt32](capi-ipc-cparcel-h.md#oh_ipcparcel_readint32)方法配对使用。
* 调用顺序：先调用WriteInt()写入数据，接收端再调用[OH\_IPCParcel\_ReadInt32](capi-ipc-cparcel-h.md#oh_ipcparcel_readint32)读取数据。
* 未正确配对：如果未按顺序调用或读取类型不匹配，会导致读取失败或数据错误。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OHIPCParcel](capi-ohipcparcel.md) \*parcel | OHIPCParcel对象的指针，不能为空。 |
| int32\_t value | 要写入的int32\_t数据值，用于IPC通信数据序列化。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 成功返回[OH\_IPC\_ErrorCode#OH\_IPC\_SUCCESS](capi-ipc-error-code-h.md#oh_ipc_errorcode)；  参数不合法时返回[OH\_IPC\_ErrorCode#OH\_IPC\_CHECK\_PARAM\_ERROR](capi-ipc-error-code-h.md#oh_ipc_errorcode)；  写入失败返回[OH\_IPC\_ErrorCode#OH\_IPC\_PARCEL\_WRITE\_ERROR](capi-ipc-error-code-h.md#oh_ipc_errorcode)。 |

### OH\_IPCParcel\_ReadInt32()

```c
int OH_IPCParcel_ReadInt32(const OHIPCParcel *parcel, int32_t *value)
```

**描述：**

从OHIPCParcel对象读取int32\_t值。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [OHIPCParcel](capi-ohipcparcel.md) \*parcel | OHIPCParcel对象的指针，不能为空。 |
| int32\_t \*value | 存储读取数据的指针，不能为空。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 成功返回[OH\_IPC\_ErrorCode#OH\_IPC\_SUCCESS](capi-ipc-error-code-h.md#oh_ipc_errorcode)；  参数不合法时返回[OH\_IPC\_ErrorCode#OH\_IPC\_CHECK\_PARAM\_ERROR](capi-ipc-error-code-h.md#oh_ipc_errorcode)；  读取失败返回[OH\_IPC\_ErrorCode#OH\_IPC\_PARCEL\_READ\_ERROR](capi-ipc-error-code-h.md#oh_ipc_errorcode)。 |

### OH\_IPCParcel\_WriteInt64()

```c
int OH_IPCParcel_WriteInt64(OHIPCParcel *parcel, int64_t value)
```

**描述：**

向OHIPCParcel对象写入int64\_t值。写入数据受IPC序列化总大小限制（参见[OH\_IPCParcel\_Create](capi-ipc-cparcel-h.md#oh_ipcparcel_create)）。

* 必须与[OH\_IPCParcel\_ReadInt64](capi-ipc-cparcel-h.md#oh_ipcparcel_readint64)方法配对使用。
* 调用顺序：先调用WriteInt()写入数据，接收端再调用[OH\_IPCParcel\_ReadInt64](capi-ipc-cparcel-h.md#oh_ipcparcel_readint64)读取数据。
* 未正确配对：如果未按顺序调用或读取类型不匹配，会导致读取失败或数据错误。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OHIPCParcel](capi-ohipcparcel.md) \*parcel | OHIPCParcel对象的指针，不能为空。 |
| int64\_t value | 要写入的int64\_t数据值，用于IPC通信数据序列化。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 成功返回[OH\_IPC\_ErrorCode#OH\_IPC\_SUCCESS](capi-ipc-error-code-h.md#oh_ipc_errorcode)；  参数不合法时返回[OH\_IPC\_ErrorCode#OH\_IPC\_CHECK\_PARAM\_ERROR](capi-ipc-error-code-h.md#oh_ipc_errorcode)；  写入失败返回[OH\_IPC\_ErrorCode#OH\_IPC\_PARCEL\_WRITE\_ERROR](capi-ipc-error-code-h.md#oh_ipc_errorcode)。 |

### OH\_IPCParcel\_ReadInt64()

```c
int OH_IPCParcel_ReadInt64(const OHIPCParcel *parcel, int64_t *value)
```

**描述：**

从OHIPCParcel对象读取int64\_t值。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [OHIPCParcel](capi-ohipcparcel.md) \*parcel | OHIPCParcel对象的指针，不能为空。 |
| int64\_t \*value | 存储读取数据的指针，不能为空。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 成功返回[OH\_IPC\_ErrorCode#OH\_IPC\_SUCCESS](capi-ipc-error-code-h.md#oh_ipc_errorcode)；  参数不合法时返回[OH\_IPC\_ErrorCode#OH\_IPC\_CHECK\_PARAM\_ERROR](capi-ipc-error-code-h.md#oh_ipc_errorcode)；  读取失败返回[OH\_IPC\_ErrorCode#OH\_IPC\_PARCEL\_READ\_ERROR](capi-ipc-error-code-h.md#oh_ipc_errorcode)。 |

### OH\_IPCParcel\_WriteUint8()

```c
int OH_IPCParcel_WriteUint8(OHIPCParcel *parcel, uint8_t value)
```

**描述：**

向OHIPCParcel对象写入uint8\_t值。写入数据受IPC序列化总大小限制（参见[OH\_IPCParcel\_Create](capi-ipc-cparcel-h.md#oh_ipcparcel_create)）。

* 必须与[OH\_IPCParcel\_ReadUint8](capi-ipc-cparcel-h.md#oh_ipcparcel_readuint8)方法配对使用。
* 调用顺序：先调用WriteUint()写入数据，接收端再调用[OH\_IPCParcel\_ReadUint8](capi-ipc-cparcel-h.md#oh_ipcparcel_readuint8)读取数据。
* 未正确配对：如果未按顺序调用或读取类型不匹配，会导致读取失败或数据错误。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OHIPCParcel](capi-ohipcparcel.md) \*parcel | OHIPCParcel对象的指针，不能为空。 |
| uint8\_t value | 要写入的uint8\_t数据值，用于IPC通信数据序列化。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 成功返回[OH\_IPC\_ErrorCode#OH\_IPC\_SUCCESS](capi-ipc-error-code-h.md#oh_ipc_errorcode)；  参数不合法时返回[OH\_IPC\_ErrorCode#OH\_IPC\_CHECK\_PARAM\_ERROR](capi-ipc-error-code-h.md#oh_ipc_errorcode)；  写入失败返回[OH\_IPC\_ErrorCode#OH\_IPC\_PARCEL\_WRITE\_ERROR](capi-ipc-error-code-h.md#oh_ipc_errorcode)。 |

### OH\_IPCParcel\_ReadUint8()

```c
int OH_IPCParcel_ReadUint8(const OHIPCParcel *parcel, uint8_t *value)
```

**描述：**

从OHIPCParcel对象读取uint8\_t值。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [OHIPCParcel](capi-ohipcparcel.md) \*parcel | OHIPCParcel对象的指针，不能为空。 |
| uint8\_t \*value | 存储读取数据的指针，不能为空。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 成功返回[OH\_IPC\_ErrorCode#OH\_IPC\_SUCCESS](capi-ipc-error-code-h.md#oh_ipc_errorcode)；  参数不合法时返回[OH\_IPC\_ErrorCode#OH\_IPC\_CHECK\_PARAM\_ERROR](capi-ipc-error-code-h.md#oh_ipc_errorcode)；  读取失败返回[OH\_IPC\_ErrorCode#OH\_IPC\_PARCEL\_READ\_ERROR](capi-ipc-error-code-h.md#oh_ipc_errorcode)。 |

### OH\_IPCParcel\_WriteUint16()

```c
int OH_IPCParcel_WriteUint16(OHIPCParcel *parcel, uint16_t value)
```

**描述：**

向OHIPCParcel对象写入uint16\_t值。写入数据受IPC序列化总大小限制（参见[OH\_IPCParcel\_Create](capi-ipc-cparcel-h.md#oh_ipcparcel_create)）。

* 必须与[OH\_IPCParcel\_ReadUint16](capi-ipc-cparcel-h.md#oh_ipcparcel_readuint16)方法配对使用。
* 调用顺序：先调用WriteUint()写入数据，接收端再调用[OH\_IPCParcel\_ReadUint16](capi-ipc-cparcel-h.md#oh_ipcparcel_readuint16)读取数据。
* 未正确配对：如果未按顺序调用或读取类型不匹配，会导致读取失败或数据错误。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OHIPCParcel](capi-ohipcparcel.md) \*parcel | OHIPCParcel对象的指针，不能为空。 |
| uint16\_t value | 要写入的uint16\_t数据值，用于IPC通信数据序列化。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 成功返回[OH\_IPC\_ErrorCode#OH\_IPC\_SUCCESS](capi-ipc-error-code-h.md#oh_ipc_errorcode)；  参数不合法时返回[OH\_IPC\_ErrorCode#OH\_IPC\_CHECK\_PARAM\_ERROR](capi-ipc-error-code-h.md#oh_ipc_errorcode)；  写入失败返回[OH\_IPC\_ErrorCode#OH\_IPC\_PARCEL\_WRITE\_ERROR](capi-ipc-error-code-h.md#oh_ipc_errorcode)。 |

### OH\_IPCParcel\_ReadUint16()

```c
int OH_IPCParcel_ReadUint16(const OHIPCParcel *parcel, uint16_t *value)
```

**描述：**

从OHIPCParcel对象读取uint16\_t值。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [OHIPCParcel](capi-ohipcparcel.md) \*parcel | OHIPCParcel对象的指针，不能为空。 |
| uint16\_t \*value | 存储读取数据的指针，不能为空。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 成功返回[OH\_IPC\_ErrorCode#OH\_IPC\_SUCCESS](capi-ipc-error-code-h.md#oh_ipc_errorcode)；  参数不合法时返回[OH\_IPC\_ErrorCode#OH\_IPC\_CHECK\_PARAM\_ERROR](capi-ipc-error-code-h.md#oh_ipc_errorcode)；  读取失败返回[OH\_IPC\_ErrorCode#OH\_IPC\_PARCEL\_READ\_ERROR](capi-ipc-error-code-h.md#oh_ipc_errorcode)。 |

### OH\_IPCParcel\_WriteUint32()

```c
int OH_IPCParcel_WriteUint32(OHIPCParcel *parcel, uint32_t value)
```

**描述：**

向OHIPCParcel对象写入uint32\_t值。写入数据受IPC序列化总大小限制（参见[OH\_IPCParcel\_Create](capi-ipc-cparcel-h.md#oh_ipcparcel_create)）。

* 必须与[OH\_IPCParcel\_ReadUint32](capi-ipc-cparcel-h.md#oh_ipcparcel_readuint32)方法配对使用。
* 调用顺序：先调用WriteUint()写入数据，接收端再调用[OH\_IPCParcel\_ReadUint32](capi-ipc-cparcel-h.md#oh_ipcparcel_readuint32)读取数据。
* 未正确配对：如果未按顺序调用或读取类型不匹配，会导致读取失败或数据错误。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OHIPCParcel](capi-ohipcparcel.md) \*parcel | OHIPCParcel对象的指针，不能为空。 |
| uint32\_t value | 要写入的uint32\_t数据值，用于IPC通信数据序列化。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 成功返回[OH\_IPC\_ErrorCode#OH\_IPC\_SUCCESS](capi-ipc-error-code-h.md#oh_ipc_errorcode)；  参数不合法时返回[OH\_IPC\_ErrorCode#OH\_IPC\_CHECK\_PARAM\_ERROR](capi-ipc-error-code-h.md#oh_ipc_errorcode)；  写入失败返回[OH\_IPC\_ErrorCode#OH\_IPC\_PARCEL\_WRITE\_ERROR](capi-ipc-error-code-h.md#oh_ipc_errorcode)。 |

### OH\_IPCParcel\_ReadUint32()

```c
int OH_IPCParcel_ReadUint32(const OHIPCParcel *parcel, uint32_t *value)
```

**描述：**

从OHIPCParcel对象读取uint32\_t值。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [OHIPCParcel](capi-ohipcparcel.md) \*parcel | OHIPCParcel对象的指针，不能为空。 |
| uint32\_t \*value | 存储读取数据的指针，不能为空。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 成功返回[OH\_IPC\_ErrorCode#OH\_IPC\_SUCCESS](capi-ipc-error-code-h.md#oh_ipc_errorcode)；  参数不合法时返回[OH\_IPC\_ErrorCode#OH\_IPC\_CHECK\_PARAM\_ERROR](capi-ipc-error-code-h.md#oh_ipc_errorcode)；  读取失败返回[OH\_IPC\_ErrorCode#OH\_IPC\_PARCEL\_READ\_ERROR](capi-ipc-error-code-h.md#oh_ipc_errorcode)。 |

### OH\_IPCParcel\_WriteUint64()

```c
int OH_IPCParcel_WriteUint64(OHIPCParcel *parcel, uint64_t value)
```

**描述：**

向OHIPCParcel对象写入uint64\_t值。写入数据受IPC序列化总大小限制（参见[OH\_IPCParcel\_Create](capi-ipc-cparcel-h.md#oh_ipcparcel_create)）。

* 必须与[OH\_IPCParcel\_ReadUint64](capi-ipc-cparcel-h.md#oh_ipcparcel_readuint64)方法配对使用。
* 调用顺序：先调用WriteUint()写入数据，接收端再调用[OH\_IPCParcel\_ReadUint64](capi-ipc-cparcel-h.md#oh_ipcparcel_readuint64)读取数据。
* 未正确配对：如果未按顺序调用或读取类型不匹配，会导致读取失败或数据错误。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OHIPCParcel](capi-ohipcparcel.md) \*parcel | OHIPCParcel对象的指针，不能为空。 |
| uint64\_t value | 要写入的uint64\_t数据值，用于IPC通信数据序列化。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 成功返回[OH\_IPC\_ErrorCode#OH\_IPC\_SUCCESS](capi-ipc-error-code-h.md#oh_ipc_errorcode)；  参数不合法时返回[OH\_IPC\_ErrorCode#OH\_IPC\_CHECK\_PARAM\_ERROR](capi-ipc-error-code-h.md#oh_ipc_errorcode)；  写入失败返回[OH\_IPC\_ErrorCode#OH\_IPC\_PARCEL\_WRITE\_ERROR](capi-ipc-error-code-h.md#oh_ipc_errorcode)。 |

### OH\_IPCParcel\_ReadUint64()

```c
int OH_IPCParcel_ReadUint64(const OHIPCParcel *parcel, uint64_t *value)
```

**描述：**

从OHIPCParcel对象读取uint64\_t值。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [OHIPCParcel](capi-ohipcparcel.md) \*parcel | OHIPCParcel对象的指针，不能为空。 |
| uint64\_t \*value | 存储读取数据的指针，不能为空。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 成功返回[OH\_IPC\_ErrorCode#OH\_IPC\_SUCCESS](capi-ipc-error-code-h.md#oh_ipc_errorcode)；  参数不合法时返回[OH\_IPC\_ErrorCode#OH\_IPC\_CHECK\_PARAM\_ERROR](capi-ipc-error-code-h.md#oh_ipc_errorcode)；  读取失败返回[OH\_IPC\_ErrorCode#OH\_IPC\_PARCEL\_READ\_ERROR](capi-ipc-error-code-h.md#oh_ipc_errorcode)。 |

### OH\_IPCParcel\_WriteFloat()

```c
int OH_IPCParcel_WriteFloat(OHIPCParcel *parcel, float value)
```

**描述：**

向OHIPCParcel对象写入float值。写入数据受IPC序列化总大小限制（参见[OH\_IPCParcel\_Create](capi-ipc-cparcel-h.md#oh_ipcparcel_create)）。

* 必须与[OH\_IPCParcel\_ReadFloat](capi-ipc-cparcel-h.md#oh_ipcparcel_readfloat)方法配对使用。
* 调用顺序：先调用WriteFloat()写入数据，接收端再调用[OH\_IPCParcel\_ReadFloat](capi-ipc-cparcel-h.md#oh_ipcparcel_readfloat)读取数据。
* 未正确配对：如果未按顺序调用或读取类型不匹配，会导致读取失败或数据错误。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OHIPCParcel](capi-ohipcparcel.md) \*parcel | OHIPCParcel对象的指针，不能为空。 |
| float value | 要写入的float数据值，用于IPC通信数据序列化。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 成功返回[OH\_IPC\_ErrorCode#OH\_IPC\_SUCCESS](capi-ipc-error-code-h.md#oh_ipc_errorcode)；  参数不合法时返回[OH\_IPC\_ErrorCode#OH\_IPC\_CHECK\_PARAM\_ERROR](capi-ipc-error-code-h.md#oh_ipc_errorcode)；  写入失败返回[OH\_IPC\_ErrorCode#OH\_IPC\_PARCEL\_WRITE\_ERROR](capi-ipc-error-code-h.md#oh_ipc_errorcode)。 |

### OH\_IPCParcel\_ReadFloat()

```c
int OH_IPCParcel_ReadFloat(const OHIPCParcel *parcel, float *value)
```

**描述：**

从OHIPCParcel对象读取float值。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [OHIPCParcel](capi-ohipcparcel.md) \*parcel | OHIPCParcel对象的指针，不能为空。 |
| float \*value | 存储读取数据的指针，不能为空。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 成功返回[OH\_IPC\_ErrorCode#OH\_IPC\_SUCCESS](capi-ipc-error-code-h.md#oh_ipc_errorcode)；  参数不合法时返回[OH\_IPC\_ErrorCode#OH\_IPC\_CHECK\_PARAM\_ERROR](capi-ipc-error-code-h.md#oh_ipc_errorcode)；  读取失败返回[OH\_IPC\_ErrorCode#OH\_IPC\_PARCEL\_READ\_ERROR](capi-ipc-error-code-h.md#oh_ipc_errorcode)。 |

### OH\_IPCParcel\_WriteDouble()

```c
int OH_IPCParcel_WriteDouble(OHIPCParcel *parcel, double value)
```

**描述：**

向OHIPCParcel对象写入double值。写入数据受IPC序列化总大小限制（参见[OH\_IPCParcel\_Create](capi-ipc-cparcel-h.md#oh_ipcparcel_create)）。

* 必须与[OH\_IPCParcel\_ReadDouble](capi-ipc-cparcel-h.md#oh_ipcparcel_readdouble)方法配对使用。
* 调用顺序：先调用WriteDouble()写入数据，接收端再调用[OH\_IPCParcel\_ReadDouble](capi-ipc-cparcel-h.md#oh_ipcparcel_readdouble)读取数据。
* 未正确配对：如果未按顺序调用或读取类型不匹配，会导致读取失败或数据错误。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OHIPCParcel](capi-ohipcparcel.md) \*parcel | OHIPCParcel对象的指针，不能为空。 |
| double value | 要写入的double数据值，用于IPC通信数据序列化。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 成功返回[OH\_IPC\_ErrorCode#OH\_IPC\_SUCCESS](capi-ipc-error-code-h.md#oh_ipc_errorcode)；  参数不合法时返回[OH\_IPC\_ErrorCode#OH\_IPC\_CHECK\_PARAM\_ERROR](capi-ipc-error-code-h.md#oh_ipc_errorcode)；  写入失败返回[OH\_IPC\_ErrorCode#OH\_IPC\_PARCEL\_WRITE\_ERROR](capi-ipc-error-code-h.md#oh_ipc_errorcode)。 |

### OH\_IPCParcel\_ReadDouble()

```c
int OH_IPCParcel_ReadDouble(const OHIPCParcel *parcel, double *value)
```

**描述：**

从OHIPCParcel对象读取double值。调用此函数后，从当前读取位置读取8字节的double值，读取位置自动后移8字节，读取到的值存储到value指针指向的内存中。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [OHIPCParcel](capi-ohipcparcel.md) \*parcel | OHIPCParcel对象的指针，不能为空。 |
| double \*value | 存储读取数据的指针，不能为空。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 成功返回[OH\_IPC\_ErrorCode#OH\_IPC\_SUCCESS](capi-ipc-error-code-h.md#oh_ipc_errorcode)；  参数不合法时返回[OH\_IPC\_ErrorCode#OH\_IPC\_CHECK\_PARAM\_ERROR](capi-ipc-error-code-h.md#oh_ipc_errorcode)；  读取失败返回[OH\_IPC\_ErrorCode#OH\_IPC\_PARCEL\_READ\_ERROR](capi-ipc-error-code-h.md#oh_ipc_errorcode)。 |

### OH\_IPCParcel\_WriteString()

```c
int OH_IPCParcel_WriteString(OHIPCParcel *parcel, const char *str)
```

**描述：**

向OHIPCParcel对象写入字符串，包括字符串结束符。写入数据受IPC序列化总大小限制（参见[OH\_IPCParcel\_Create](capi-ipc-cparcel-h.md#oh_ipcparcel_create)）。

调用此函数：

* 将字符串内容(包括结束符'\0')写入到OHIPCParcel对象的当前写入位置。
* 写入位置自动后移(字符串长度+1)字节。
* 字符串数据被序列化存储在Parcel对象中，无需调用者管理。
* 写入的字符串长度受IPC序列化大小限制(参见[OH\_IPCParcel\_Create](capi-ipc-cparcel-h.md#oh_ipcparcel_create)，最大204800字节)。
* str参数不能为空，否则会返回参数错误。
* 编码说明：字符串应为有效的UTF-8或ASCII编码。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OHIPCParcel](capi-ohipcparcel.md) \*parcel | OHIPCParcel对象的指针，不能为空。 |
| const char \*str | 写入字符串，用于IPC通信中的字符串数据传输，不能为空。长度范围[0, 204800]，单位：字节（含结束符，实际长度受parcel已写入数据与结束符开销的动态影响）。写入的字符串长度受IPC序列化大小限制（参见[OH\_IPCParcel\_Create](capi-ipc-cparcel-h.md#oh_ipcparcel_create)）。超出限制时返回OH\_IPC\_PARCEL\_WRITE\_ERROR错误。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 成功返回[OH\_IPC\_ErrorCode#OH\_IPC\_SUCCESS](capi-ipc-error-code-h.md#oh_ipc_errorcode)；  参数不合法时返回[OH\_IPC\_ErrorCode#OH\_IPC\_CHECK\_PARAM\_ERROR](capi-ipc-error-code-h.md#oh_ipc_errorcode)；  写入失败返回[OH\_IPC\_ErrorCode#OH\_IPC\_PARCEL\_WRITE\_ERROR](capi-ipc-error-code-h.md#oh_ipc_errorcode)。 |

### OH\_IPCParcel\_ReadString()

```c
const char* OH_IPCParcel_ReadString(const OHIPCParcel *parcel)
```

**描述：**

从OHIPCParcel对象读取字符串，用户可通过strlen获取字符串长度。

调用此函数：

1. 从当前读取位置读取字符串内容。
2. 返回字符串的内存地址指针。
3. 读取位置自动后移到字符串结束符之后。
4. 返回的字符串内存由Parcel对象管理，无需调用者释放。
5. 字符串有效性与Parcel对象绑定，销毁Parcel后字符串失效。
6. 参数不合法或读取失败时返回NULL，需检查返回值。
7. 可通过strlen获取长度，直接使用返回的指针访问字符串内容。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [OHIPCParcel](capi-ohipcparcel.md) \*parcel | OHIPCParcel对象的指针，不能为空。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| const char\* | 成功返回读取字符串地址；参数不合法或读取失败时返回NULL。 |

### OH\_IPCParcel\_WriteBuffer()

```c
int OH_IPCParcel_WriteBuffer(OHIPCParcel *parcel, const uint8_t *buffer, int32_t len)
```

**描述：**

向OHIPCParcel对象写入指定长度的内存信息。常用于写入二进制数据、图片数据、自定义结构体、共享内存内容等场景。写入数据受IPC序列化总大小限制（参见[OH\_IPCParcel\_Create](capi-ipc-cparcel-h.md#oh_ipcparcel_create)）。

调用此函数：

* 将buffer指向的内存数据写入到OHIPCParcel对象的当前写入位置。
* 写入位置自动后移len字节。
* 内存数据被序列化存储在Parcel对象中。
* buffer必须提前分配足够的内存空间，且内存有效。
* len取值范围[0, parcel可写字节数]，超出范围会返回错误。
* buffer不能为空，否则会返回参数错误。
* 写入的数据应在调用期间保持有效，写入完成后无限制。
* 写入完成后，buffer内存由调用者自行管理，Parcel内部存储副本。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OHIPCParcel](capi-ohipcparcel.md) \*parcel | OHIPCParcel对象的指针，不能为空。 |
| const uint8\_t \*buffer | 写入内存的起始地址，要写入的数据缓冲区的起始地址，指向需要通过IPC传输的二进制数据，不能为空。缓冲区必须提前分配好足够的内存空间。 |
| int32\_t len | 写入信息长度，单位：字节，取值范围[0, parcel可写字节数]。写入数据大小受IPC序列化大小限制（参见[OH\_IPCParcel\_Create](capi-ipc-cparcel-h.md#oh_ipcparcel_create)）。传入负数时返回OH\_IPC\_CHECK\_PARAM\_ERROR；超出可写字节数时返回OH\_IPC\_PARCEL\_WRITE\_ERROR错误。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 成功返回[OH\_IPC\_ErrorCode#OH\_IPC\_SUCCESS](capi-ipc-error-code-h.md#oh_ipc_errorcode)；  参数不合法时返回[OH\_IPC\_ErrorCode#OH\_IPC\_CHECK\_PARAM\_ERROR](capi-ipc-error-code-h.md#oh_ipc_errorcode)；  写入失败返回[OH\_IPC\_ErrorCode#OH\_IPC\_PARCEL\_WRITE\_ERROR](capi-ipc-error-code-h.md#oh_ipc_errorcode)。 |

### OH\_IPCParcel\_ReadBuffer()

```c
const uint8_t* OH_IPCParcel_ReadBuffer(const OHIPCParcel *parcel, int32_t len)
```

**描述：**

从OHIPCParcel对象读取指定长度内存信息。常用于读取二进制数据、图片数据、自定义结构体、共享内存内容等场景。

调用此函数：

* 从当前读取位置读取len字节的内存数据，len取值范围[0, parcel可读字节数]，超出范围会返回NULL。
* 返回指向Parcel对象内部存储数据的指针。
* 读取位置自动后移len字节。
* 返回的内存由Parcel对象管理，无需调用者释放。
* 生命周期：数据有效性与Parcel对象绑定，销毁Parcel后数据失效。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [OHIPCParcel](capi-ohipcparcel.md) \*parcel | OHIPCParcel对象的指针，不能为空。 |
| int32\_t len | 读取内存的长度，单位：字节，取值范围[0, parcel当前剩余可读字节数]。超出可读字节数时返回NULL。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| const uint8\_t\* | 成功返回读取到的内存地址；参数不合法或len超过parcel可读长度时返回NULL。 |

### OH\_IPCParcel\_WriteRemoteStub()

```c
int OH_IPCParcel_WriteRemoteStub(OHIPCParcel *parcel, const OHIPCRemoteStub *stub)
```

**描述：**

向OHIPCParcel对象写入OHIPCRemoteStub对象。常用于跨进程传递服务对象、实现IPC服务端的远程调用、服务对象共享等场景。写入数据受IPC序列化总大小限制（参见[OH\_IPCParcel\_Create](capi-ipc-cparcel-h.md#oh_ipcparcel_create)）。

调用此函数：

* 将OHIPCRemoteStub对象的引用信息写入到OHIPCParcel对象中，写入位置自动后移。
* Stub对象的引用信息被序列化存储。
* 调用顺序：先调用WriteRemoteStub()写入Stub对象，接收端再调用[OH\_IPCParcel\_ReadRemoteStub](capi-ipc-cparcel-h.md#oh_ipcparcel_readremotestub)读取。
* 未正确配对：如果未按顺序调用或未配对使用，会导致接收端无法正确获取Stub对象引用，影响IPC通信建立。
* 对象有效性：stub不能为空，必须为有效的OHIPCRemoteStub对象指针，否则会返回参数错误。
* 引用管理：写入后Stub对象的引用计数增加，需确保Stub对象生命周期足够。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OHIPCParcel](capi-ohipcparcel.md) \*parcel | OHIPCParcel对象的指针，不能为空。 |
| const [OHIPCRemoteStub](capi-ohipcparcel-ohipcremotestub.md) \*stub | 需要写入的OHIPCRemoteStub对象指针，不能为空。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 成功返回[OH\_IPC\_ErrorCode#OH\_IPC\_SUCCESS](capi-ipc-error-code-h.md#oh_ipc_errorcode)；  参数不合法时返回[OH\_IPC\_ErrorCode#OH\_IPC\_CHECK\_PARAM\_ERROR](capi-ipc-error-code-h.md#oh_ipc_errorcode)；  写入失败返回[OH\_IPC\_ErrorCode#OH\_IPC\_PARCEL\_WRITE\_ERROR](capi-ipc-error-code-h.md#oh_ipc_errorcode)。 |

### OH\_IPCParcel\_ReadRemoteStub()

```c
OHIPCRemoteStub* OH_IPCParcel_ReadRemoteStub(const OHIPCParcel *parcel)
```

**描述：**

从OHIPCParcel对象读取OHIPCRemoteStub对象。常用于跨进程接收服务对象、实现IPC服务端的远程调用、服务对象共享等场景。

调用此函数：

* 从当前读取位置读取Stub对象的引用信息。
* 返回OHIPCRemoteStub对象的指针。
* 读取位置自动后移。
* 必须与[OH\_IPCParcel\_WriteRemoteStub](capi-ipc-cparcel-h.md#oh_ipcparcel_writeremotestub)方法配对使用。
* 返回的Stub对象指针由系统管理，需按IPC规范使用。
* 读取失败时返回NULL，需检查返回值。
* 通常用于接收服务端传递的Stub对象，用于建立IPC通信。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [OHIPCParcel](capi-ohipcparcel.md) \*parcel | OHIPCParcel对象的指针，不能为空。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| OHIPCRemoteStub\* | 成功返回OHIPCRemoteStub对象指针；失败返回NULL。 |

### OH\_IPCParcel\_WriteRemoteProxy()

```c
int OH_IPCParcel_WriteRemoteProxy(OHIPCParcel *parcel, const OHIPCRemoteProxy *proxy)
```

**描述：**

向OHIPCParcel对象写入OHIPCRemoteProxy对象。常用于跨进程传递代理对象、实现IPC客户端的远程调用、代理对象共享等场景。写入数据受IPC序列化总大小限制（参见[OH\_IPCParcel\_Create](capi-ipc-cparcel-h.md#oh_ipcparcel_create)）。

调用此函数：

* 将OHIPCRemoteProxy对象的引用信息写入到OHIPCParcel对象中。
* 写入位置自动后移。
* Proxy对象的引用信息被序列化存储。
* 调用顺序：先调用[OH\_IPCParcel\_WriteRemoteProxy](capi-ipc-cparcel-h.md#oh_ipcparcel_writeremoteproxy)写入Proxy对象，接收端再调用[OH\_IPCParcel\_ReadRemoteProxy](capi-ipc-cparcel-h.md#oh_ipcparcel_readremoteproxy)读取。
* 未正确配对：如果未按顺序调用或未配对使用，会导致接收端无法正确获取Proxy对象引用，影响IPC通信建立。
* 对象有效性：proxy不能为空，必须为有效的OHIPCRemoteProxy对象指针，否则会返回参数错误。
* 引用管理：写入后Proxy对象的引用计数增加，需确保Proxy对象生命周期足够。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OHIPCParcel](capi-ohipcparcel.md) \*parcel | OHIPCParcel对象的指针，不能为空。 |
| const [OHIPCRemoteProxy](capi-ohipcparcel-ohipcremoteproxy.md) \*proxy | 需要写入的OHIPCRemoteProxy对象指针，不能为空。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 成功返回[OH\_IPC\_ErrorCode#OH\_IPC\_SUCCESS](capi-ipc-error-code-h.md#oh_ipc_errorcode)；  参数不合法时返回[OH\_IPC\_ErrorCode#OH\_IPC\_CHECK\_PARAM\_ERROR](capi-ipc-error-code-h.md#oh_ipc_errorcode)；  写入失败返回[OH\_IPC\_ErrorCode#OH\_IPC\_PARCEL\_WRITE\_ERROR](capi-ipc-error-code-h.md#oh_ipc_errorcode)。 |

### OH\_IPCParcel\_ReadRemoteProxy()

```c
OHIPCRemoteProxy* OH_IPCParcel_ReadRemoteProxy(const OHIPCParcel *parcel)
```

**描述：**

从OHIPCParcel对象读取OHIPCRemoteProxy对象。常用于跨进程接收代理对象、实现IPC客户端的远程调用、代理对象共享等场景。

调用此函数：

* 从当前读取位置读取Proxy对象的引用信息。
* 返回OHIPCRemoteProxy对象的指针。
* 读取位置自动后移。
* 必须与[OH\_IPCParcel\_WriteRemoteProxy](capi-ipc-cparcel-h.md#oh_ipcparcel_writeremoteproxy)方法配对使用。
* 返回的Proxy对象指针由系统管理，需按IPC规范使用。
* 读取失败时返回NULL，需检查返回值。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [OHIPCParcel](capi-ohipcparcel.md) \*parcel | OHIPCParcel对象的指针，不能为空。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| OHIPCRemoteProxy\* | 成功返回OHIPCRemoteProxy对象指针；失败返回NULL。 |

### OH\_IPCParcel\_WriteFileDescriptor()

```c
int OH_IPCParcel_WriteFileDescriptor(OHIPCParcel *parcel, int32_t fd)
```

**描述：**

向OHIPCParcel对象写入文件描述符。常用于跨进程传递文件句柄、共享内存文件描述符、管道文件描述符等场景。写入数据受IPC序列化总大小限制（参见[OH\_IPCParcel\_Create](capi-ipc-cparcel-h.md#oh_ipcparcel_create)）。

调用此函数：

* 将文件描述符的副本写入到OHIPCParcel对象中。
* 写入位置自动后移。
* 文件描述符信息被序列化存储，可在IPC通信中传递。
* 调用顺序：先调用[OH\_IPCParcel\_WriteFileDescriptor](capi-ipc-cparcel-h.md#oh_ipcparcel_writefiledescriptor)写入文件描述符。
* 接收端再调用[OH\_IPCParcel\_ReadFileDescriptor](capi-ipc-cparcel-h.md#oh_ipcparcel_readfiledescriptor)读取。
* 未正确配对：如果未按顺序调用或未配对使用，会导致接收端无法获取正确的文件描述符，影响跨进程文件共享和访问。
* 文件描述符有效性：fd必须为有效的非负整数文件描述符。
* 资源管理：写入后原文件描述符仍由调用者管理，需自行关闭。
* 权限传递：接收端获得的文件描述符具有相同的访问权限。
* 系统限制：文件描述符传递受系统限制，某些特殊文件描述符可能无法传递。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OHIPCParcel](capi-ohipcparcel.md) \*parcel | OHIPCParcel对象的指针，不能为空。 |
| int32\_t fd | 要写入的文件描述符，取值原则：有效的文件描述符，为非负整数。传入负数或无效文件描述符时返回OH\_IPC\_CHECK\_PARAM\_ERROR错误。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 成功返回[OH\_IPC\_ErrorCode#OH\_IPC\_SUCCESS](capi-ipc-error-code-h.md#oh_ipc_errorcode)；  参数不合法时返回[OH\_IPC\_ErrorCode#OH\_IPC\_CHECK\_PARAM\_ERROR](capi-ipc-error-code-h.md#oh_ipc_errorcode)；  写入失败返回[OH\_IPC\_ErrorCode#OH\_IPC\_PARCEL\_WRITE\_ERROR](capi-ipc-error-code-h.md#oh_ipc_errorcode)。 |

### OH\_IPCParcel\_ReadFileDescriptor()

```c
int OH_IPCParcel_ReadFileDescriptor(const OHIPCParcel *parcel, int32_t *fd)
```

**描述：**

从OHIPCParcel对象读取文件描述符。常用于跨进程接收文件句柄、共享内存文件描述符、管道文件描述符等场景。不支持多线程并发访问同一对象。

调用此函数：

* 从当前读取位置读取文件描述符信息。
* 返回一个新的有效的文件描述符。
* 读取位置自动后移。
* 新文件描述符指向与原文件相同的资源，继承原文件描述符的访问权限。
* 必须与[OH\_IPCParcel\_WriteFileDescriptor](capi-ipc-cparcel-h.md#oh_ipcparcel_writefiledescriptor)方法配对使用。
* 读取到的文件描述符需要由接收方管理，使用完毕后应关闭。
* 返回的文件描述符应检查是否有效(非负值)。
* 文件描述符的生命周期独立于Parcel对象。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [OHIPCParcel](capi-ohipcparcel.md) \*parcel | OHIPCParcel对象的指针，不能为空。 |
| int32\_t \*fd | 存储读取文件描述符的指针，不能为空。读取前需确保parcel中已写入有效的文件描述符数据。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 成功返回[OH\_IPC\_ErrorCode#OH\_IPC\_SUCCESS](capi-ipc-error-code-h.md#oh_ipc_errorcode)；  参数不合法时返回[OH\_IPC\_ErrorCode#OH\_IPC\_CHECK\_PARAM\_ERROR](capi-ipc-error-code-h.md#oh_ipc_errorcode)；  读取失败返回[OH\_IPC\_ErrorCode#OH\_IPC\_PARCEL\_READ\_ERROR](capi-ipc-error-code-h.md#oh_ipc_errorcode)。 |

### OH\_IPCParcel\_Append()

```c
int OH_IPCParcel_Append(OHIPCParcel *parcel, const OHIPCParcel *data)
```

**描述：**

OHIPCParcel对象数据拼接。常用于合并多个Parcel的数据、数据包组装、分段写入数据的合并等场景。拼接数据受IPC序列化总大小限制（参见[OH\_IPCParcel\_Create](capi-ipc-cparcel-h.md#oh_ipcparcel_create)）。

调用此函数：

* 将源Parcel对象(data)中的数据复制并追加到目标Parcel对象(parcel)的当前写入位置。
* 写入位置自动后移追加数据的字节数。
* 源Parcel对象的读取位置和内容保持不变。
* 追加操作会复制源数据到目标Parcel，内存由目标Parcel管理。
* 拼接后的数据总大小不能超过IPC序列化限制(参见[OH\_IPCParcel\_Create](capi-ipc-cparcel-h.md#oh_ipcparcel_create))。
* parcel和data参数均不能为空，否则会返回参数错误。
* 两个参数必须为由[OH\_IPCParcel\_Create](capi-ipc-cparcel-h.md#oh_ipcparcel_create)创建的有效对象。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OHIPCParcel](capi-ohipcparcel.md) \*parcel | OHIPCParcel对象的指针，不能为空。 |
| const [OHIPCParcel](capi-ohipcparcel.md) \*data | data源OHIPCParcel对象的指针，不能为空。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 成功返回[OH\_IPC\_ErrorCode#OH\_IPC\_SUCCESS](capi-ipc-error-code-h.md#oh_ipc_errorcode)；  参数不合法时返回[OH\_IPC\_ErrorCode#OH\_IPC\_CHECK\_PARAM\_ERROR](capi-ipc-error-code-h.md#oh_ipc_errorcode)；  拼接失败返回[OH\_IPC\_ErrorCode#OH\_IPC\_PARCEL\_WRITE\_ERROR](capi-ipc-error-code-h.md#oh_ipc_errorcode)。 |

### OH\_IPCParcel\_WriteInterfaceToken()

```c
int OH_IPCParcel_WriteInterfaceToken(OHIPCParcel *parcel, const char *token)
```

**描述：**

向OHIPCParcel对象写入接口描述符，用于接口身份校验。常用于IPC通信中的安全验证场景，例如：防止恶意进程发送伪造请求、确保消息发送到正确的服务接口、多接口服务中区分不同的接口调用。不支持多线程并发访问同一对象。写入数据受IPC序列化总大小限制（参见[OH\_IPCParcel\_Create](capi-ipc-cparcel-h.md#oh_ipcparcel_create)）。

调用此函数：

* 将接口描述符字符串写入到OHIPCParcel对象的当前写入位置。
* 写入位置自动后移相应的字节数。
* 接口描述符数据被序列化存储在Parcel对象中。
* 接口描述符字符串长度不能超过Parcel剩余可写空间。
* 调用顺序：客户端先调用[OH\_IPCParcel\_WriteInterfaceToken](capi-ipc-cparcel-h.md#oh_ipcparcel_writeinterfacetoken)写入接口描述符，服务端再调用[OH\_IPCParcel\_ReadInterfaceToken](capi-ipc-cparcel-h.md#oh_ipcparcel_readinterfacetoken)读取并校验。
* 如果未按顺序调用或未配对使用，会导致接口身份校验失败，请求可能被拒绝或发送到错误的接口，造成接口混淆。
* token参数不能为空，否则会返回参数错误。
* 建议在写入其他请求数据前先写入接口描述符。
* 接口描述符应为接口的全限定名或唯一标识字符串。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OHIPCParcel](capi-ohipcparcel.md) \*parcel | OHIPCParcel对象的指针，不能为空。 |
| const char \*token | 需要写入的接口描述符信息，不能为空。接口描述符通常为接口的全限定名或唯一标识字符串，用于接口身份校验。字符串长度范围[0, parcel剩余可写空间]，单位：字节。超出限制时返回OH\_IPC\_PARCEL\_WRITE\_ERROR错误。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 成功返回[OH\_IPC\_ErrorCode#OH\_IPC\_SUCCESS](capi-ipc-error-code-h.md#oh_ipc_errorcode)；  参数不合法时返回[OH\_IPC\_ErrorCode#OH\_IPC\_CHECK\_PARAM\_ERROR](capi-ipc-error-code-h.md#oh_ipc_errorcode)；  写入失败返回[OH\_IPC\_ErrorCode#OH\_IPC\_PARCEL\_WRITE\_ERROR](capi-ipc-error-code-h.md#oh_ipc_errorcode)。 |

### OH\_IPCParcel\_ReadInterfaceToken()

```c
int OH_IPCParcel_ReadInterfaceToken(const OHIPCParcel *parcel, char **token, int32_t *len, OH_IPC_MemAllocator allocator)
```

**描述：**

从OHIPCParcel对象读取接口描述符信息，用于接口身份校验。

调用此函数：

* 必须与[OH\_IPCParcel\_WriteInterfaceToken](capi-ipc-cparcel-h.md#oh_ipcparcel_writeinterfacetoken)方法配对使用。
* 从当前读取位置读取接口描述符字符串。
* 通过用户提供的allocator分配内存存储描述符。
* 返回描述符地址和长度。
* 读取位置自动后移。
* token内存由用户提供的allocator分配，使用后必须主动释放。
* 即使函数返回失败，也需要检查token是否为空并释放。
* 未正确释放token会导致内存泄漏。
* 建议在处理请求前先校验接口描述符。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [OHIPCParcel](capi-ohipcparcel.md) \*parcel | OHIPCParcel对象的指针，不能为空。 |
| char \*\*token | 用于存储接口描述符信息的内存地址，该内存由用户提供的分配器进行内存分配，用户使用完后需要主动释放，不能为空。接口返回失败时，用户依然需要判断该内存是否为空，并主动释放，否则会造成内存泄漏。 |
| int32\_t \*len | 存储读取接口描述符的长度（包括结束符），单位：字节，不能为空。 |
| [OH\_IPC\_MemAllocator](capi-ipc-cparcel-h.md#oh_ipc_memallocator) allocator | 用户指定的用来分配token的内存分配器，不能为空。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 成功返回[OH\_IPC\_ErrorCode#OH\_IPC\_SUCCESS](capi-ipc-error-code-h.md#oh_ipc_errorcode)；  参数不合法时返回[OH\_IPC\_ErrorCode#OH\_IPC\_CHECK\_PARAM\_ERROR](capi-ipc-error-code-h.md#oh_ipc_errorcode)；读取失败返回[OH\_IPC\_ErrorCode#OH\_IPC\_PARCEL\_READ\_ERROR](capi-ipc-error-code-h.md#oh_ipc_errorcode)。 |
