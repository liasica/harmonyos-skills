---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_f_i_d_o2___credential_creation_options
title: FIDO2_CredentialCreationOptions
breadcrumb: API参考 > 系统 > 安全 > Online Authentication Kit（在线认证服务） > C API > 结构体 > FIDO2_CredentialCreationOptions
category: harmonyos-references
scraped_at: 2026-09-02T15:01:45+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:73891df7310b2d94de78ce94e1b119382a859f1350bed51bf77e4abbfbc7ea63
---

## 概述

凭据请求的选项。

**起始版本：** 6.0.0(20)

**相关模块：** [FIDO2（通行密钥服务）](passkey.md)

**所在头文件：** [fido2\_api.h](onlineauthentication_capi_header_fido2.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| [FIDO2\_CredentialMediationRequirement](passkey.md#fido2_credentialmediationrequirement-1) [mediation](_f_i_d_o2___credential_creation_options.md#mediation) | 该操作是否需要用户参与。 |
| [FIDO2\_PublicKeyCredentialCreationOptions](_f_i_d_o2___public_key_credential_creation_options.md) [publicKey](_f_i_d_o2___credential_creation_options.md#publickey) | publicKey凭证请求的选项。 |

## 结构体成员变量说明

### mediation

```cpp
FIDO2_CredentialMediationRequirement FIDO2_CredentialCreationOptions::mediation
```

**描述**

操作是否需要用户参与。

### publicKey

```cpp
FIDO2_PublicKeyCredentialCreationOptions FIDO2_CredentialCreationOptions::publicKey
```

**描述**

publicKey凭证请求的选项。
