---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netstack-http-headervalue
title: Http_HeaderValue
breadcrumb: API参考 > 系统 > 网络 > Network Kit（网络服务） > C API > 结构体 > Http_HeaderValue
category: harmonyos-references
scraped_at: 2026-09-02T15:01:56+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:838134a5234b54efbb05af62b47d87b596d74d3a9ed05ec47cb84339c2dd60f0
---

```c
typedef struct Http_HeaderValue {...} Http_HeaderValue
```

## 概述

请求或者响应的标头映射的值类型。

**起始版本：** 20

**相关模块：** [netstack](capi-netstack.md)

**所在头文件：** [net\_http\_type.h](capi-net-http-type-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| char \*value | 标头键值对的值。 |
| struct Http\_HeaderValue \*next | 链式存储。指向下一个Http\_HeaderValue。 |
