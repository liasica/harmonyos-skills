---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netstack-http-clientcert
title: Http_ClientCert
breadcrumb: API参考 > 系统 > 网络 > Network Kit（网络服务） > C API > 结构体 > Http_ClientCert
category: harmonyos-references
scraped_at: 2026-09-02T15:01:56+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:0a0eaab5d5e52fb923d00bf62dfda9c5a3b73d5671f7b921821d64e870877b3c
---

```c
typedef struct Http_ClientCert {...} Http_ClientCert
```

## 概述

发送到服务端的客户端证书配置，服务端将通过客户端证书校验客户端身份。

**起始版本：** 20

**相关模块：** [netstack](capi-netstack.md)

**所在头文件：** [net\_http\_type.h](capi-net-http-type-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| char \*certPath | 证书路径。 |
| [Http\_CertType](capi-net-http-type-h.md#http_certtype) type | 证书类型，默认是PEM，参考[Http\_CertType](capi-net-http-type-h.md#http_certtype)。 |
| char \*keyPath | 证书密钥的路径。 |
| char \*keyPassword | 证书密钥的密码。 |
