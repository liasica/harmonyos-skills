---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___quic_io_vec
title: Rcp_QuicIoVec
breadcrumb: API参考 > 系统 > 网络 > Remote Communication Kit（远场通信服务） > C API > 结构体 > Rcp_QuicIoVec
category: harmonyos-references
scraped_at: 2026-09-02T15:01:59+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:969bde1087d5e4a7ea0e527d51b134dfb4401e398798b8000ce5fd63442f4e0d
---

## 概述

用于存储二进制内容的数据结构。

**起始版本：** 26.0.0

**相关模块：** [RemoteCommunication](remote-communication-overview.md)

**所在头文件：** [rcp\_quic.h](rcp_quic_h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| uint8\_t \*[data](_rcp___quic_io_vec.md#data) | 指向数据内容的指针。 |
| uint64\_t [length](_rcp___quic_io_vec.md#length) | 数据内容长度。 |

## 结构体成员变量说明

### data

```cpp
uint8_t* Rcp_QuicIoVec::data
```

**描述**

指向数据内容的指针。

### length

```cpp
uint64_t Rcp_QuicIoVec::length
```

**描述**

数据内容长度。
