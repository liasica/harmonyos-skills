---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netstack-http-requestoptions
title: Http_RequestOptions
breadcrumb: API参考 > 系统 > 网络 > Network Kit（网络服务） > C API > 结构体 > Http_RequestOptions
category: harmonyos-references
scraped_at: 2026-04-28T08:08:41+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:7d15c6ee5ae1f4fe5e21f1a0ad0cadde67b93f05981b05fe62658ff89c4825ee
---

```
1. typedef struct Http_RequestOptions {...} Http_RequestOptions
```

## 概述

PhonePC/2in1TabletTVWearable

定义HTTP请求配置的结构体。

**起始版本：** 20

**相关模块：** [netstack](capi-netstack.md)

**所在头文件：** [net\_http\_type.h](capi-net-http-type-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| const char \*method | HTTP请求方法。 |
| uint32\_t priority | HTTP请求优先级。 |
| [Http\_Headers](capi-netstack-http-headers.md) \*headers | HTTP请求头，指向Http\_Headers的指针，参考[Http\_Headers](capi-netstack-http-headers.md)。 |
| uint32\_t readTimeout | 读取超时时间。 |
| uint32\_t connectTimeout | 连接超时时间。 |
| [Http\_HttpProtocol](capi-net-http-type-h.md#http_httpprotocol) httpProtocol | 使用的协议，参考[Http\_HttpProtocol](capi-net-http-type-h.md#http_httpprotocol)。 |
| [Http\_Proxy](capi-netstack-http-proxy.md) \*httpProxy | 代理配置信息，表示是否使用代理，默认不使用代理，参考[Http\_Proxy](capi-netstack-http-proxy.md)。 |
| const char \*caPath | 证书路径，如果设置了此参数，系统将使用用户指定路径的CA证书（开发者需保证该路径下CA证书的可访问性），否则将使用系统预设CA证书。 |
| int64\_t resumeFrom | 用于设置下载起始位置，该参数只能用于GET方法，不要用于其他。 |
| int64\_t resumeTo | 用于设置下载结束位置，该参数只能用于GET方法，不要用于其他。 |
| [Http\_ClientCert](capi-netstack-http-clientcert.md) \*clientCert | 传输客户端证书配置信息，参考[Http\_ClientCert](capi-netstack-http-clientcert.md)。 |
| const char \*dnsOverHttps | 设置使用HTTPS协议的服务器进行DNS解析。 |
| [Http\_AddressFamilyType](capi-net-http-type-h.md#http_addressfamilytype) addressFamily | 支持解析目标域名时限定地址类型，参考[Http\_AddressFamilyType](capi-net-http-type-h.md#http_addressfamilytype)。 |
