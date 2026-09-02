---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-cm-native-type-h
title: cm_native_type.h
breadcrumb: API参考 > 系统 > 安全 > Device Certificate Kit（设备证书服务） > C API > 头文件 > cm_native_type.h
category: harmonyos-references
scraped_at: 2026-09-02T15:01:45+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:4ae7e9a5845e020317205d386ee55e25b644b0242f1d9d4afbf26881e4d4bbf4
---

## 概述

提供CertManager中的枚举变量、结构体定义、宏定义和错误码。

**引用文件：** <device\_certificate/certmanager/cm\_native\_type.h>

**库：** libohcert\_manager.z.so

**系统能力：** SystemCapability.Security.CertificateManager

**起始版本：** 22

**相关模块：** [CertManagerType](capi-certmanagertype.md)

## 汇总

### 结构体

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [OH\_CM\_Blob](capi-certmanagertype-oh-cm-blob.md) | OH\_CM\_Blob | 定义存放数据的结构体类型。 |
| [OH\_CM\_Credential](capi-certmanagertype-oh-cm-credential.md) | OH\_CM\_Credential | 定义证书凭据详情的结构体类型。 |
| [OH\_CM\_CredentialDetailList](capi-certmanagertype-oh-cm-credentialdetaillist.md) | OH\_CM\_CredentialDetailList | 定义证书凭据详情列表的结构体类型。 |
| [OH\_CM\_UkeyInfo](capi-certmanagertype-oh-cm-ukeyinfo.md) | OH\_CM\_UkeyInfo | 定义USB证书凭据信息的结构体类型。 |

### 枚举

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [OH\_CM\_ErrorCode](capi-cm-native-type-h.md#oh_cm_errorcode) | OH\_CM\_ErrorCode | 错误码。 |
| [OH\_CM\_CertificatePurpose](capi-cm-native-type-h.md#oh_cm_certificatepurpose) | OH\_CM\_CertificatePurpose | 证书凭据用途类型。 |

### 宏定义

| 名称 | 描述 |
| --- | --- |
| OH\_CM\_MAX\_LEN\_CERTIFICATE\_CHAIN 24588 | 证书链最大长度，单位：Byte。  **起始版本：** 22 |
| OH\_CM\_MAX\_LEN\_URI 256 | URI最大长度，单位：Byte。  **起始版本：** 22 |
| OH\_CM\_MAX\_LEN\_CERT\_ALIAS 129 | 证书别名的最大长度，单位：Byte。  **起始版本：** 22 |
| OH\_CM\_MAX\_LEN\_TYPE\_NAME 1025 | 证书类型最大长度，单位：Byte。  **起始版本：** 22 |

## 枚举类型说明

### OH\_CM\_ErrorCode

```c
enum OH_CM_ErrorCode
```

**描述**

错误码。

**起始版本：** 22

| 枚举项 | 描述 |
| --- | --- |
| OH\_CM\_SUCCESS = 0 | 成功。 |
| OH\_CM\_HAS\_NO\_PERMISSION = 201 | 权限校验失败。 |
| OH\_CM\_CAPABILITY\_NOT\_SUPPORTED = 801 | 设备不支持。 |
| OH\_CM\_INNER\_FAILURE = 17500001 | 内部错误。可能原因：1.IPC通信失败；2.内存操作错误；3.文件操作错误。 |
| OH\_CM\_NOT\_FOUND = 17500002 | 证书不存在。 |
| OH\_CM\_INVALID\_CERT\_FORMAT = 17500003 | 密钥库格式无效或密钥库密码不正确。 |
| OH\_CM\_MAX\_CERT\_COUNT\_REACHED = 17500004 | 证书或凭据数量达到上限。 |
| OH\_CM\_NO\_AUTHORIZATION = 17500005 | 应用未经用户授权。 |
| OH\_CM\_DEVICE\_ENTER\_ADVSECMODE = 17500007 | 设备进入坚盾守护模式。该模式下CA证书安装操作受限。 |
| OH\_CM\_STORE\_PATH\_NOT\_SUPPORTED = 17500009 | 不支持指定的证书存储路径。 |
| OH\_CM\_ACCESS\_UKEY\_SERVICE\_FAILED = 17500010 | USB证书凭据访问失败。 |
| OH\_CM\_PARAMETER\_VALIDATION\_FAILED = 17500011 | 参数校验失败，例如参数格式或参数范围无效。 |

### OH\_CM\_CertificatePurpose

```c
enum OH_CM_CertificatePurpose
```

**描述**

证书凭据用途类型。

**起始版本：** 22

| 枚举项 | 描述 |
| --- | --- |
| OH\_CM\_CERT\_PURPOSE\_DEFAULT = 0 | 默认用途，用于凭据签名。 |
| OH\_CM\_CERT\_PURPOSE\_ALL = 1 | 所有用途，用于查询凭据功能。 |
| OH\_CM\_CERT\_PURPOSE\_SIGN = 2 | 签名用途。 |
| OH\_CM\_CERT\_PURPOSE\_ENCRYPT = 3 | 加密用途。 |
