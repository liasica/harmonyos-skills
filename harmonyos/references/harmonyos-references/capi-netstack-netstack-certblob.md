---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netstack-netstack-certblob
title: NetStack_CertBlob
breadcrumb: API参考 > 系统 > 网络 > Network Kit（网络服务） > C API > 结构体 > NetStack_CertBlob
category: harmonyos-references
scraped_at: 2026-04-28T08:08:37+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:30add5046434d18118b4ea010390173c86529bfa2e91e2a502380f3c7dc5d110
---

```
1. struct NetStack_CertBlob {...}
```

## 概述

PhonePC/2in1TabletTVWearable

证书数据结构体。

**起始版本：** 11

**相关模块：** [netstack](capi-netstack.md)

**所在头文件：** [net\_ssl\_c\_type.h](capi-net-ssl-c-type-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| enum [NetStack\_CertType](capi-net-ssl-c-type-h.md#netstack_certtype) type | 证书类型。 |
| uint32\_t size | 证书内容长度。 |
| uint8\_t \*data | 证书内容。 |
