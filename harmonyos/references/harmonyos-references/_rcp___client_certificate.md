---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___client_certificate
title: Rcp_ClientCertificate
breadcrumb: API参考 > 系统 > 网络 > Remote Communication Kit（远场通信服务） > C API > 结构体 > Rcp_ClientCertificate
category: harmonyos-references
scraped_at: 2026-04-28T08:08:59+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:968c97cae04dc4c0a908b930e1fa595aeb682069599b4faa7f57ac00898c9f2f
---

## 概述

PhonePC/2in1TabletTVWearable

发送到远程服务器的客户端证书，远程服务器将使用它来验证客户端的标识。

**起始版本：** 5.0.0(12)

**相关模块：** [RemoteCommunication](remote-communication-overview.md)

**所在头文件：** [rcp.h](rcp_8h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| char \* [content](_rcp___client_certificate.md#content) | 客户端证书内容。它应采用“PEM”、“DER”或“P12”格式。 |
| char \* [filePath](_rcp___client_certificate.md#filepath) | 客户端证书的路径。文件的格式应为“PEM”、“DER”或“P12”格式。 |
| char \* [key](_rcp___client_certificate.md#key) | 客户端证书私钥的文件名。 |
| char \* [keyPassword](_rcp___client_certificate.md#keypassword) | 客户端证书私钥的密码。 |
| [Rcp\_CertType](remote-communication-overview.md#rcp_certtype)[type](_rcp___client_certificate.md#type) | 客户端证书类型。 |

## 结构体成员变量说明

PhonePC/2in1TabletTVWearable

### content

PhonePC/2in1TabletTVWearable

```
1. char* Rcp_ClientCertificate::content
```

**描述**

客户端证书内容。它应采用“PEM”、“DER”或“P12”格式。

### filePath

PhonePC/2in1TabletTVWearable

```
1. char* Rcp_ClientCertificate::filePath
```

**描述**

客户端证书的路径。文件的格式应为“PEM”、“DER”或“P12”格式。

### key

PhonePC/2in1TabletTVWearable

```
1. char* Rcp_ClientCertificate::key
```

**描述**

客户端证书私钥的文件名。

### keyPassword

PhonePC/2in1TabletTVWearable

```
1. char* Rcp_ClientCertificate::keyPassword
```

**描述**

客户端证书私钥的密码。

### type

PhonePC/2in1TabletTVWearable

```
1. Rcp_CertType Rcp_ClientCertificate::type
```

**描述**

客户端证书类型。
