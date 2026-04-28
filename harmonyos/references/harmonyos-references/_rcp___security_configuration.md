---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___security_configuration
title: Rcp_SecurityConfiguration
breadcrumb: API参考 > 系统 > 网络 > Remote Communication Kit（远场通信服务） > C API > 结构体 > Rcp_SecurityConfiguration
category: harmonyos-references
scraped_at: 2026-04-28T08:09:08+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:4e527f31feae804bc941858e9d351a47a95b4339a1062b6e0a404450998a774a
---

## 概述

PhonePC/2in1TabletTVWearable

请求的安全配置。

**起始版本：** 5.0.0(12)

**相关模块：** [RemoteCommunication](remote-communication-overview.md)

**所在头文件：** [rcp.h](rcp_8h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [Rcp\_RemoteValidationType](remote-communication-overview.md#rcp_remotevalidationtype)[remoteValidationType](_rcp___security_configuration.md#remotevalidationtype) | 远端认证方法类型。 |
| [Rcp\_CertificateAuthority](_rcp___certificate_authority.md)[certificateAuthority](_rcp___security_configuration.md#certificateauthority) | 用于验证远程服务器标识的证书颁发机构（CA）。默认值为“system”，如果未设置此字段，将使用system CA验证远程服务器的标识。 |
| [Rcp\_ClientCertificate](_rcp___client_certificate.md)[certificate](_rcp___security_configuration.md#certificate) | 发送到远程服务器的客户端证书，远程服务器将使用它来验证客户端的标识。 |
| [Rcp\_ServerAuthentication](_rcp___server_authentication.md)[serverAuthentication](_rcp___security_configuration.md#serverauthentication) | 服务器身份验证设置。默认情况下不进行身份验证。 |

## 结构体成员变量说明

PhonePC/2in1TabletTVWearable

### certificate

PhonePC/2in1TabletTVWearable

```
1. Rcp_ClientCertificate Rcp_SecurityConfiguration::certificate
```

**描述**

发送到远程服务器的客户端证书，远程服务器将使用它来验证客户端的标识。

### certificateAuthority

PhonePC/2in1TabletTVWearable

```
1. Rcp_CertificateAuthority Rcp_SecurityConfiguration::certificateAuthority
```

**描述**

用于验证远程服务器标识的证书颁发机构（CA）。默认值为“system”，如果未设置此字段，将使用system CA验证远程服务器的标识。

### remoteValidationType

PhonePC/2in1TabletTVWearable

```
1. Rcp_RemoteValidationType Rcp_SecurityConfiguration::remoteValidationType
```

**描述**

远端认证方法类型。

### serverAuthentication

PhonePC/2in1TabletTVWearable

```
1. Rcp_ServerAuthentication Rcp_SecurityConfiguration::serverAuthentication
```

**描述**

服务器身份验证设置。默认情况下不进行身份验证。
