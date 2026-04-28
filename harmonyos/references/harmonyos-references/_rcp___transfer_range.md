---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___transfer_range
title: Rcp_TransferRange
breadcrumb: API参考 > 系统 > 网络 > Remote Communication Kit（远场通信服务） > C API > 结构体 > Rcp_TransferRange
category: harmonyos-references
scraped_at: 2026-04-28T08:09:11+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:23c120d6624a466cc0e17c8dc6425a8bb31351ba040d876df465274db1b853b8
---

## 概述

PhonePC/2in1TabletTVWearable

HTTP传输范围。该设置将转换为HTTP Range标头。具有范围标头的HTTP请求要求服务器仅发送回HTTP响应的一部分。

**起始版本：** 5.0.0(12)

**相关模块：** [RemoteCommunication](remote-communication-overview.md)

**所在头文件：** [rcp.h](rcp_8h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| int64\_t [from](_rcp___transfer_range.md#from) | 传输起始位置。 |
| bool [hasZeroFrom](_rcp___transfer_range.md#haszerofrom) | 是否从零开始。 |
| int64\_t [to](_rcp___transfer_range.md#to) | 传输结束位置。 |
| bool [hasZeroTo](_rcp___transfer_range.md#haszeroto) | 是否以零结束。 |
| struct [Rcp\_TransferRange](_rcp___transfer_range.md) \* [next](_rcp___transfer_range.md#next) | 链式存储。指向下一个[Rcp\_TransferRange](_rcp___transfer_range.md)。 |

## 结构体成员变量说明

PhonePC/2in1TabletTVWearable

### from

PhonePC/2in1TabletTVWearable

```
1. int64_t Rcp_TransferRange::from
```

**描述**

传输起始位置。

### hasZeroFrom

PhonePC/2in1TabletTVWearable

```
1. bool Rcp_TransferRange::hasZeroFrom
```

**描述**

请求范围是否从零开始。

### hasZeroTo

PhonePC/2in1TabletTVWearable

```
1. bool Rcp_TransferRange::hasZeroTo
```

**描述**

是否以零结束。

### next

PhonePC/2in1TabletTVWearable

```
1. struct Rcp_TransferRange* Rcp_TransferRange::next
```

**描述**

链式存储。指向下一个[Rcp\_TransferRange](_rcp___transfer_range.md)。

### to

PhonePC/2in1TabletTVWearable

```
1. int64_t Rcp_TransferRange::to
```

**描述**

传输结束位置。
