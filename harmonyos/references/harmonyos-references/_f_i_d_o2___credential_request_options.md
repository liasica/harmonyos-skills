---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_f_i_d_o2___credential_request_options
title: FIDO2_CredentialRequestOptions
breadcrumb: API参考 > 系统 > 安全 > Online Authentication Kit（在线认证服务） > C API > 结构体 > FIDO2_CredentialRequestOptions
category: harmonyos-references
scraped_at: 2026-09-02T15:01:45+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:d81bc951cc8a78ce7dc1a8e7b2894bf3822b0dd63b5f0de23a16f8bd66ff85e2
---

## 概述

认证信息字典对象。

**起始版本：** 6.0.0(20)

**相关模块：** [FIDO2（通行密钥服务）](passkey.md)

**所在头文件：** [fido2\_api.h](onlineauthentication_capi_header_fido2.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| [FIDO2\_CredentialMediationRequirement](passkey.md#fido2_credentialmediationrequirement-1) [mediation](_f_i_d_o2___credential_request_options.md#mediation) | 操作是否需要用户参与。 |
| [FIDO2\_PublicKeyCredentialRequestOptions](_f_i_d_o2___public_key_credential_request_options.md) [publicKey](_f_i_d_o2___credential_request_options.md#publickey) | publicKey凭证请求的选项。 |

## 结构体成员变量说明

### mediation

```cpp
FIDO2_CredentialMediationRequirement FIDO2_CredentialRequestOptions::mediation
```

**描述**

用户介入要求。

### publicKey

```cpp
FIDO2_PublicKeyCredentialRequestOptions FIDO2_CredentialRequestOptions::publicKey
```

**描述**

publicKey凭证请求的选项。
