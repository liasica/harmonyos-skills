---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___transfer_range
title: Rcp_TransferRange
breadcrumb: API参考 > 系统 > 网络 > Remote Communication Kit（远场通信服务） > C API > 结构体 > Rcp_TransferRange
category: harmonyos-references
scraped_at: 2026-09-02T15:01:59+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:7b2049712e57a25d173742f70b349b9377fd852bc54650fae59a95328311d4ee
---

## 概述

HTTP传输范围。该设置将转换为HTTP Range标头。具有范围标头的HTTP请求要求服务器仅发送回HTTP响应的一部分。

**起始版本：** 5.0.0(12)

**相关模块：** [RemoteCommunication](remote-communication-overview.md)

**所在头文件：** [rcp.h](rcp_8h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| int64\_t [from](_rcp___transfer_range.md#from) | 传输起始位置。 |
| bool [hasZeroFrom](_rcp___transfer_range.md#haszerofrom) | 是否从零开始。true表示从零开始，false表示不从零开始。默认值为false。 |
| int64\_t [to](_rcp___transfer_range.md#to) | 传输结束位置。 |
| bool [hasZeroTo](_rcp___transfer_range.md#haszeroto) | 是否以零结束。true表示以零结束，false表示不以零结束。默认值为false。 |
| struct [Rcp\_TransferRange](_rcp___transfer_range.md) \* [next](_rcp___transfer_range.md#next) | 链式存储。指向下一个[Rcp\_TransferRange](_rcp___transfer_range.md)。 |

## 结构体成员变量说明

### from

```cpp
int64_t Rcp_TransferRange::from
```

**描述**

传输起始位置。

### hasZeroFrom

```cpp
bool Rcp_TransferRange::hasZeroFrom
```

**描述**

请求范围是否从零开始。true表示从零开始，false表示不从零开始。默认值为false。

### hasZeroTo

```cpp
bool Rcp_TransferRange::hasZeroTo
```

**描述**

是否以零结束。true表示以零结束，false表示不以零结束。默认值为false。

### next

```cpp
struct Rcp_TransferRange* Rcp_TransferRange::next
```

**描述**

链式存储。指向下一个[Rcp\_TransferRange](_rcp___transfer_range.md)。

### to

```cpp
int64_t Rcp_TransferRange::to
```

**描述**

传输结束位置。
