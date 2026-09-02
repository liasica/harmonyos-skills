---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netstack-netstack-certblob
title: NetStack_CertBlob
breadcrumb: API参考 > 系统 > 网络 > Network Kit（网络服务） > C API > 结构体 > NetStack_CertBlob
category: harmonyos-references
scraped_at: 2026-09-02T15:01:56+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:d0668ca9cb356231498caf90d3f4fc87268fd157207f9e2340e2d471c9bca736
---

```c
struct NetStack_CertBlob {...}
```

## 概述

证书数据结构体。

**起始版本：** 11

**相关模块：** [netstack](capi-netstack.md)

**所在头文件：** [net\_ssl\_c\_type.h](capi-net-ssl-c-type-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| enum [NetStack\_CertType](capi-net-ssl-c-type-h.md#netstack_certtype) type | 证书类型。 |
| uint32\_t size | 证书内容长度。单位：Byte。 |
| uint8\_t \*data | 证书内容。 |
