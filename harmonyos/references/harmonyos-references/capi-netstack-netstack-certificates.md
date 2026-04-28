---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netstack-netstack-certificates
title: NetStack_Certificates
breadcrumb: API参考 > 系统 > 网络 > Network Kit（网络服务） > C API > 结构体 > NetStack_Certificates
category: harmonyos-references
scraped_at: 2026-04-28T08:08:38+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:79fb1e9ab55742522384c3746c6e9275187bc02e9790d164ce91fa723ea1a907
---

```
1. typedef struct NetStack_Certificates {...} NetStack_Certificates
```

## 概述

PhonePC/2in1TabletTVWearable

定义证书信息。

**起始版本：** 12

**相关模块：** [netstack](capi-netstack.md)

**所在头文件：** [net\_ssl\_c\_type.h](capi-net-ssl-c-type-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| char \*\*content | 证书的PEM内容。 |
| size\_t length | 证书数量。 |
