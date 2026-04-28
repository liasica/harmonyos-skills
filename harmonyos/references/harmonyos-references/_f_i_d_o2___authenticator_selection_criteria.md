---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_f_i_d_o2___authenticator_selection_criteria
title: FIDO2_AuthenticatorSelectionCriteria
breadcrumb: API参考 > 系统 > 安全 > Online Authentication Kit（在线认证服务） > C API > 结构体 > FIDO2_AuthenticatorSelectionCriteria
category: harmonyos-references
scraped_at: 2026-04-28T08:07:29+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:8a4f268cc13de0b46bf1b928fe34316bf5bcfdd444a5247261e5298e8a28db3e
---

## 概述

由webAuthn依赖方指定，与认证器有关。

**起始版本：** 6.0.0(20)

**相关模块：** [FIDO2](passkey.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| [FIDO2\_AuthenticatorAttachment](passkey.md#fido2_authenticatorattachment-1) [authenticatorAttachment](_f_i_d_o2___authenticator_selection_criteria.md#authenticatorattachment) | 认证器信息（平台、漫游）。默认值为FIDO2\_PLATFORM。可选。 |
| const char \* [residentKey](_f_i_d_o2___authenticator_selection_criteria.md#residentkey) | 常驻键。默认空。可选。 |
| bool [requireResidentKey](_f_i_d_o2___authenticator_selection_criteria.md#requireresidentkey) | 是否需要常驻键，true代表需要常驻键，false代表不需要。默认值为false。可选。 |
| [FIDO2\_UserVerificationRequirement](passkey.md#fido2_userverificationrequirement-1) [userVerification](_f_i_d_o2___authenticator_selection_criteria.md#userverification) | 用户认证需求枚举。默认值为preferred。可选。 |

## 结构体成员变量说明

### authenticatorAttachment

```
1. FIDO2_AuthenticatorAttachment FIDO2_AuthenticatorSelectionCriteria::authenticatorAttachment
```

**描述**

认证器信息（平台、漫游）。可选。

### requireResidentKey

```
1. bool FIDO2_AuthenticatorSelectionCriteria::requireResidentKey
```

**描述**

是否需要常驻键，true代表需要常驻键，false代表不需要。默认值为false。可选。

### residentKey

```
1. const char* FIDO2_AuthenticatorSelectionCriteria::residentKey
```

**描述**

常驻键。可选。

### userVerification

```
1. FIDO2_UserVerificationRequirement FIDO2_AuthenticatorSelectionCriteria::userVerification
```

**描述**

用户认证需求枚举。默认值为preferred。可选。
