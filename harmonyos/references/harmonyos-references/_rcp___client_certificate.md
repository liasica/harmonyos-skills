---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___client_certificate
title: Rcp_ClientCertificate
breadcrumb: API参考 > 系统 > 网络 > Remote Communication Kit（远场通信服务） > C API > 结构体 > Rcp_ClientCertificate
category: harmonyos-references
scraped_at: 2026-09-02T15:01:58+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:5814daeadc1cdaff3b5cbbe9fd54939bec6257aab016f7ef6a04449a2a07dee9
---

## 概述

发送到远程服务器的客户端证书，远程服务器将使用它来验证客户端的标识。

**起始版本：** 5.0.0(12)

**相关模块：** [RemoteCommunication](remote-communication-overview.md)

**所在头文件：** [rcp.h](rcp_8h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| char \* [content](_rcp___client_certificate.md#content) | 客户端证书内容。它应采用PEM、DER或P12格式。 |
| char \* [filePath](_rcp___client_certificate.md#filepath) | 客户端证书的路径。文件的格式应为PEM、DER或P12格式。 |
| char \* [key](_rcp___client_certificate.md#key) | 客户端证书私钥的文件名。 |
| char \* [keyPassword](_rcp___client_certificate.md#keypassword) | 客户端证书私钥的密码。 |
| [Rcp\_CertType](remote-communication-overview.md#rcp_certtype) [type](_rcp___client_certificate.md#type) | 客户端证书类型。 |

## 结构体成员变量说明

### content

```cpp
char* Rcp_ClientCertificate::content
```

**描述**

客户端证书内容。它应采用“PEM”、“DER”或“P12”格式。

### filePath

```cpp
char* Rcp_ClientCertificate::filePath
```

**描述**

客户端证书的路径。文件的格式应为“PEM”、“DER”或“P12”格式。

### key

```cpp
char* Rcp_ClientCertificate::key
```

**描述**

客户端证书私钥的文件名。

### keyPassword

```cpp
char* Rcp_ClientCertificate::keyPassword
```

**描述**

客户端证书私钥的密码。

### type

```cpp
Rcp_CertType Rcp_ClientCertificate::type
```

**描述**

客户端证书类型。
