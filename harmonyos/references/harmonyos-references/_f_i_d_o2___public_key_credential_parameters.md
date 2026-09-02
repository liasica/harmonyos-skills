---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_f_i_d_o2___public_key_credential_parameters
title: FIDO2_PublicKeyCredentialParameters
breadcrumb: API参考 > 系统 > 安全 > Online Authentication Kit（在线认证服务） > C API > 结构体 > FIDO2_PublicKeyCredentialParameters
category: harmonyos-references
scraped_at: 2026-09-02T15:01:45+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:f2af1a4d9df35d7f3466ff460c6d18fcf59057fa3c228cbb11b5c96d434ae07e
---

## 概述

认证凭据的附加参数。

**起始版本：** 6.0.0(20)

**相关模块：** [FIDO2（通行密钥服务）](passkey.md)

**所在头文件：** [fido2\_api.h](onlineauthentication_capi_header_fido2.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| [FIDO2\_PublicKeyCredentialType](passkey.md#fido2_publickeycredentialtype-1) [type](_f_i_d_o2___public_key_credential_parameters.md#type) | PublicKey凭证类型。 |
| [FIDO2\_Algorithm](passkey.md#fido2_algorithm-1) [alg](_f_i_d_o2___public_key_credential_parameters.md#alg) | 凭证所使用的密码算法。 |

## 结构体成员变量说明

### alg

```cpp
FIDO2_Algorithm FIDO2_PublicKeyCredentialParameters::alg
```

**描述**

凭证所使用的密码算法。

### type

```cpp
FIDO2_PublicKeyCredentialType FIDO2_PublicKeyCredentialParameters::type
```

**描述**

PublicKey凭证类型。
