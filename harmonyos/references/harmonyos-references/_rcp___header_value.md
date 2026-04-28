---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___header_value
title: Rcp_HeaderValue
breadcrumb: API参考 > 系统 > 网络 > Remote Communication Kit（远场通信服务） > C API > 结构体 > Rcp_HeaderValue
category: harmonyos-references
scraped_at: 2026-04-28T08:09:04+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:ac53ee630d6ecec508800ef1d3d7f95ef01c398dc148dc1a0ac807af68bdea54
---

## 概述

PhonePC/2in1TabletTVWearable

请求或响应的标头映射的值类型。

**起始版本：** 5.0.0(12)

**相关模块：** [RemoteCommunication](remote-communication-overview.md)

**所在头文件：** [rcp.h](rcp_8h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| char \* [value](_rcp___header_value.md#value) | 标头键值对的值。 |
| struct [Rcp\_HeaderValue](_rcp___header_value.md) \* [next](_rcp___header_value.md#next) | 链式存储。指向下一个[Rcp\_HeaderValue](_rcp___header_value.md)。 |

## 结构体成员变量说明

PhonePC/2in1TabletTVWearable

### next

PhonePC/2in1TabletTVWearable

```
1. struct Rcp_HeaderValue* Rcp_HeaderValue::next
```

**描述**

链式存储。指向下一个[Rcp\_HeaderValue](_rcp___header_value.md)。

### value

PhonePC/2in1TabletTVWearable

```
1. char* Rcp_HeaderValue::value
```

**描述**

标头键值对的值。
