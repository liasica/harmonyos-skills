---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netstack-http-headerentry
title: Http_HeaderEntry
breadcrumb: API参考 > 系统 > 网络 > Network Kit（网络服务） > C API > 结构体 > Http_HeaderEntry
category: harmonyos-references
scraped_at: 2026-09-02T15:01:56+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:97b44c0ef1ecd9168bf7125275f4d8ef272abb77399fe96bf4ae10e187b108cd
---

```c
typedef struct Http_HeaderEntry {...} Http_HeaderEntry
```

## 概述

请求或者响应的标头的所有键值对。

**起始版本：** 20

**相关模块：** [netstack](capi-netstack.md)

**所在头文件：** [net\_http\_type.h](capi-net-http-type-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| char \*key | 请求或者响应的标头中的键。 |
| [Http\_HeaderValue](capi-netstack-http-headervalue.md) \*value | 请求或者响应的标头中的键对应的值，参考[Http\_HeaderValue](capi-netstack-http-headervalue.md)。 |
| struct Http\_HeaderEntry \*next | 链式存储。指向下一个Http\_HeaderEntry。 |
