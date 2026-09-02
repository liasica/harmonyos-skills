---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___quic_slist
title: Rcp_QuicSlist
breadcrumb: API参考 > 系统 > 网络 > Remote Communication Kit（远场通信服务） > C API > 结构体 > Rcp_QuicSlist
category: harmonyos-references
scraped_at: 2026-09-02T15:01:59+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:01fe3e6dc872a4221c8a6df22cbd613bf1a697abcb7eccca5a96c6cc9c389a33
---

## 概述

链表数据结构。

**起始版本：** 26.0.0

**相关模块：** [RemoteCommunication](remote-communication-overview.md)

**所在头文件：** [rcp\_quic.h](rcp_quic_h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| char \*[data](_rcp___quic_slist.md#data) | 字符串数据内容指针。 |
| struct [Rcp\_QuicSlist \*](_rcp___quic_slist.md) [next](_rcp___quic_slist.md#next) | 下一个数据内容节点指针。 |

## 结构体成员变量说明

### data

```cpp
char* Rcp_QuicSlist::data
```

**描述**

字符串数据内容指针。

### next

```cpp
struct Rcp_QuicSlist *Rcp_QuicSlist::next
```

**描述**

下一个数据内容节点指针。
