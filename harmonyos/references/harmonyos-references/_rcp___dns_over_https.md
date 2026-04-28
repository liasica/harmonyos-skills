---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___dns_over_https
title: Rcp_DnsOverHttps
breadcrumb: API参考 > 系统 > 网络 > Remote Communication Kit（远场通信服务） > C API > 结构体 > Rcp_DnsOverHttps
category: harmonyos-references
scraped_at: 2026-04-28T08:09:01+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:76b2fe9057e91c9a7073821e1a8a57919b06dea2050fc48bc1492169867dbc2b
---

## 概述

PhonePC/2in1TabletTVWearable

HTTPS上的DNS配置如果设置，则首选由DOH dns服务器解析的地址。

**起始版本：** 5.0.0(12)

**相关模块：** [RemoteCommunication](remote-communication-overview.md)

**所在头文件：** [rcp.h](rcp_8h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| const char \* [url](_rcp___dns_over_https.md#url) | DOH服务器的URL。 |
| bool [skipCertificatesValidation](_rcp___dns_over_https.md#skipcertificatesvalidation) | 判断是否跳过证书验证。默认值为false。 |

## 结构体成员变量说明

PhonePC/2in1TabletTVWearable

### skipCertificatesValidation

PhonePC/2in1TabletTVWearable

```
1. bool Rcp_DnsOverHttps::skipCertificatesValidation
```

**描述**

判断是否跳过证书验证。默认值为false。

### url

PhonePC/2in1TabletTVWearable

```
1. const char* Rcp_DnsOverHttps::url
```

**描述**

DOH服务器的URL。
