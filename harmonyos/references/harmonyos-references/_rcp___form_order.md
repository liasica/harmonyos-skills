---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___form_order
title: Rcp_FormOrder
breadcrumb: API参考 > 系统 > 网络 > Remote Communication Kit（远场通信服务） > C API > 结构体 > Rcp_FormOrder
category: harmonyos-references
scraped_at: 2026-09-02T15:01:58+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:155bb6da5fa2aca82a73d1dbca699b7256cf33994c5853c961b1c3a75d9d567f
---

## 概述

表单发送顺序。key数组的顺序代表表单顺序。

**起始版本：** 26.0.0

**相关模块：** [RemoteCommunication](remote-communication-overview.md)

**所在头文件：** [rcp.h](rcp_8h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| const char \* const \*[keys](_rcp___form_order.md#keys) | 元素为key的数组。 |
| size\_t [size](_rcp___form_order.md#size) | key的个数。 |

## 结构体成员变量说明

### keys

```cpp
const char * const * Rcp_FormOrder::keys
```

**描述**

元素为key的数组。

### size

```cpp
size_t Rcp_FormOrder::size
```

**描述**

key的个数。
