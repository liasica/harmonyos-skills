---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___header_value
title: Rcp_HeaderValue
breadcrumb: API参考 > 系统 > 网络 > Remote Communication Kit（远场通信服务） > C API > 结构体 > Rcp_HeaderValue
category: harmonyos-references
scraped_at: 2026-09-02T15:01:59+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:80585a8777cc7973df7073a8355f33e0c8b457e84a7082ff5d4386ce5b703c9b
---

## 概述

请求或响应的标头映射的值类型。

**起始版本：** 5.0.0(12)

**相关模块：** [RemoteCommunication](remote-communication-overview.md)

**所在头文件：** [rcp.h](rcp_8h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| char \* [value](_rcp___header_value.md#value) | 标头键值对的值。 |
| struct [Rcp\_HeaderValue](_rcp___header_value.md) \* [next](_rcp___header_value.md#next) | 链式存储。指向下一个[Rcp\_HeaderValue](_rcp___header_value.md)。 |

## 结构体成员变量说明

### next

```cpp
struct Rcp_HeaderValue* Rcp_HeaderValue::next
```

**描述**

链式存储。指向下一个[Rcp\_HeaderValue](_rcp___header_value.md)。

### value

```cpp
char* Rcp_HeaderValue::value
```

**描述**

标头键值对的值。
