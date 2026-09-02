---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netstack-netstack-certificatepinning
title: NetStack_CertificatePinning
breadcrumb: API参考 > 系统 > 网络 > Network Kit（网络服务） > C API > 结构体 > NetStack_CertificatePinning
category: harmonyos-references
scraped_at: 2026-09-02T15:01:56+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:2353d9171c521807f41840325c1a2a42dac141e52b60eb0cf53a6cb49b0c8ac4
---

```c
typedef struct NetStack_CertificatePinning {...} NetStack_CertificatePinning
```

## 概述

定义证书锁定信息。

**起始版本：** 12

**相关模块：** [netstack](capi-netstack.md)

**所在头文件：** [net\_ssl\_c\_type.h](capi-net-ssl-c-type-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| [NetStack\_CertificatePinningKind](capi-net-ssl-c-type-h.md#netstack_certificatepinningkind) kind | 证书锁定类型。 |
| [NetStack\_HashAlgorithm](capi-net-ssl-c-type-h.md#netstack_hashalgorithm) hashAlgorithm | 哈希算法。 |
| char \*publicKeyHash | 哈希值。 |
