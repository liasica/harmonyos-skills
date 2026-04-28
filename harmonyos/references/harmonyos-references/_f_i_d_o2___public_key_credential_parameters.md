---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_f_i_d_o2___public_key_credential_parameters
title: FIDO2_PublicKeyCredentialParameters
breadcrumb: API参考 > 系统 > 安全 > Online Authentication Kit（在线认证服务） > C API > 结构体 > FIDO2_PublicKeyCredentialParameters
category: harmonyos-references
scraped_at: 2026-04-28T08:07:32+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:bfd78a5d2b21c31c844d7891f955886a5468effb61fd49d7a1d0cdc805488c49
---

## 概述

认证凭据的附加参数。

**起始版本：** 6.0.0(20)

**相关模块：** [FIDO2](passkey.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| [FIDO2\_PublicKeyCredentialType](passkey.md#fido2_publickeycredentialtype-1) [type](_f_i_d_o2___public_key_credential_parameters.md#type) | PublicKey凭证类型。 |
| [FIDO2\_Algorithm](passkey.md#fido2_algorithm-1) [alg](_f_i_d_o2___public_key_credential_parameters.md#alg) | 算法。 |

## 结构体成员变量说明

### alg

```
1. FIDO2_Algorithm FIDO2_PublicKeyCredentialParameters::alg
```

**描述**

算法。

### type

```
1. FIDO2_PublicKeyCredentialType FIDO2_PublicKeyCredentialParameters::type
```

**描述**

PublicKey凭证类型。
