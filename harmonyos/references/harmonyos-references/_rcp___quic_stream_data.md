---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___quic_stream_data
title: Rcp_QuicStreamData
breadcrumb: API参考 > 系统 > 网络 > Remote Communication Kit（远场通信服务） > C API > 结构体 > Rcp_QuicStreamData
category: harmonyos-references
scraped_at: 2026-09-02T15:01:59+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:17ed31a82ab9e4492e0740289ba35e575526a93ebf7926d53fa6add34f0e929b
---

## 概述

quic连接中用于接收流式数据的存储结构。

**起始版本：** 26.0.0

**相关模块：** [RemoteCommunication](remote-communication-overview.md)

**所在头文件：** [rcp\_quic.h](rcp_quic_h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| [Rcp\_QuicIoVec](_rcp___quic_io_vec.md) \*[iov](_rcp___quic_stream_data.md#iov) | 指向[Rcp\_QuicIoVec](_rcp___quic_io_vec.md)结构体数组的指针。 |
| uint32\_t [iovLen](_rcp___quic_stream_data.md#iovlen) | [Rcp\_QuicIoVec](_rcp___quic_io_vec.md)结构体数组的长度。 |
| bool [fin](_rcp___quic_stream_data.md#fin) | 标记是否为流式传输的最后数据。true表示是流式传输的最后数据，false表示不是流式传输的最后数据。 |

## 结构体成员变量说明

### iov

```cpp
Rcp_QuicIoVec* Rcp_QuicStreamData::iov
```

**描述**

指向[Rcp\_QuicIoVec](_rcp___quic_io_vec.md)结构体数组的指针。

### iovLen

```cpp
uint32_t Rcp_QuicStreamData::iovLen
```

**描述**

[Rcp\_QuicIoVec](_rcp___quic_io_vec.md)结构体数组的长度。

### fin

```cpp
bool Rcp_QuicStreamData::fin
```

**描述**

标记是否为流式传输的最后数据。true表示是流式传输的最后数据，false表示不是流式传输的最后数据。
