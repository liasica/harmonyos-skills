---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_f_i_d_o2___credential_request_options
title: FIDO2_CredentialRequestOptions
breadcrumb: API参考 > 系统 > 安全 > Online Authentication Kit（在线认证服务） > C API > 结构体 > FIDO2_CredentialRequestOptions
category: harmonyos-references
scraped_at: 2026-09-25T07:11:32+08:00
doc_updated_at: 2026-09-24
content_hash: sha256:0df5b4d95305adf687ec90619ef65641513c02a2dc261422ec22b5291318bbc4
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

操作是否需要用户参与。

### publicKey

```cpp
FIDO2_PublicKeyCredentialRequestOptions FIDO2_CredentialRequestOptions::publicKey
```

**描述**

publicKey凭证请求的选项。
