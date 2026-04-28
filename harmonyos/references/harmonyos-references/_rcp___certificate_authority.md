---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___certificate_authority
title: Rcp_CertificateAuthority
breadcrumb: API参考 > 系统 > 网络 > Remote Communication Kit（远场通信服务） > C API > 结构体 > Rcp_CertificateAuthority
category: harmonyos-references
scraped_at: 2026-04-28T08:08:58+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:126e4a85d5792ea73374998655cf61d51ea02864e07095b45c175e6f92c6835d
---

## 概述

PhonePC/2in1TabletTVWearable

用于验证远程服务器标识的证书颁发机构（CA）。

**起始版本：** 5.0.0(12)

**相关模块：** [RemoteCommunication](remote-communication-overview.md)

**所在头文件：** [rcp.h](rcp_8h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| char \* [content](_rcp___certificate_authority.md#content) | 用于验证对等的证书颁发机构证书捆绑包。应采用PEM格式。 |
| char \* [filePath](_rcp___certificate_authority.md#filepath) | 用于验证对等方的证书颁发机构证书文件的路径。文件应为PEM格式。 |
| char \* [folderPath](_rcp___certificate_authority.md#folderpath) | 包含用于验证对等项的多个CA证书的目录的路径。 此目录中的文件应为PEM格式。  文件必须以主题名称的哈希和扩展名“.0”命名。 |

## 结构体成员变量说明

PhonePC/2in1TabletTVWearable

### content

PhonePC/2in1TabletTVWearable

```
1. char* Rcp_CertificateAuthority::content
```

**描述**

用于验证对等的证书颁发机构证书捆绑包。它应采用PEM格式。

### filePath

PhonePC/2in1TabletTVWearable

```
1. char* Rcp_CertificateAuthority::filePath
```

**描述**

用于验证对等方的证书颁发机构证书文件的路径。文件应为PEM格式。

### folderPath

PhonePC/2in1TabletTVWearable

```
1. char* Rcp_CertificateAuthority::folderPath
```

**描述**

包含用于验证对等项的多个CA证书的目录的路径。 此目录中的文件应为PEM格式。

文件必须以主题名称的哈希和扩展名“.0”命名。
