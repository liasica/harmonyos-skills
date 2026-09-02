---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netstack-netstack-certificates
title: NetStack_Certificates
breadcrumb: API参考 > 系统 > 网络 > Network Kit（网络服务） > C API > 结构体 > NetStack_Certificates
category: harmonyos-references
scraped_at: 2026-09-02T15:01:56+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:941e8c6df6de6e2297e21a51ee055c77986fd0de525e605a44533dcf64bdc77d
---

```c
typedef struct NetStack_Certificates {...} NetStack_Certificates
```

## 概述

定义证书信息。

**起始版本：** 12

**相关模块：** [netstack](capi-netstack.md)

**所在头文件：** [net\_ssl\_c\_type.h](capi-net-ssl-c-type-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| char \*\*content | 证书的PEM内容。 |
| size\_t length | 证书数量。 |
