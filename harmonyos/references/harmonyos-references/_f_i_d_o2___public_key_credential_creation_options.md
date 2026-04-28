---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_f_i_d_o2___public_key_credential_creation_options
title: FIDO2_PublicKeyCredentialCreationOptions
breadcrumb: API参考 > 系统 > 安全 > Online Authentication Kit（在线认证服务） > C API > 结构体 > FIDO2_PublicKeyCredentialCreationOptions
category: harmonyos-references
scraped_at: 2026-04-28T08:07:31+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:7be353f9ad234b83f20f8e8533ab3d5594578d819f8c71536a9cd4443a5d4cc4
---

## 概述

创建新的认证凭据的选项。

**起始版本：** 6.0.0(20)

**相关模块：** [FIDO2](passkey.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| [FIDO2\_PublicKeyCredentialRpEntity](_f_i_d_o2___public_key_credential_rp_entity.md) [rp](_f_i_d_o2___public_key_credential_creation_options.md#rp) | 创建新凭据时的依赖方属性。 |
| [FIDO2\_PublicKeyCredentialUserEntity](_f_i_d_o2___public_key_credential_user_entity.md) [user](_f_i_d_o2___public_key_credential_creation_options.md#user) | 创建新凭据时用户的属性。 |
| [Uint8Buff](_uint8_buff.md) [challenge](_f_i_d_o2___public_key_credential_creation_options.md#challenge) | 挑战值。 |
| [FIDO2\_CredentialCreationOptionArray](_f_i_d_o2___credential_creation_option_array.md) [pubKeyCredParams](_f_i_d_o2___public_key_credential_creation_options.md#pubkeycredparams) | 认证凭据的附加参数数组。 |
| uint32\_t [timeout](_f_i_d_o2___public_key_credential_creation_options.md#timeout) | 注册操作最长时间，单位为毫秒。默认为300000（5分钟）。可选。 |
| [FIDO2\_PublicKeyCredentialDescriptorArray](_f_i_d_o2___public_key_credential_descriptor_array.md) [excludeCredentials](_f_i_d_o2___public_key_credential_creation_options.md#excludecredentials) | FIDO服务器已注册的凭据列表。默认值为[]。可选。 |
| [FIDO2\_AuthenticatorSelectionCriteria](_f_i_d_o2___authenticator_selection_criteria.md) [authenticatorSelection](_f_i_d_o2___public_key_credential_creation_options.md#authenticatorselection) | 身份认证器相关配置项。 |
| [FIDO2\_PublicKeyCredentialHintArray](_f_i_d_o2___public_key_credential_hint_array.md) [hints](_f_i_d_o2___public_key_credential_creation_options.md#hints) | 认证方式指示。默认值为[]。可选。 |
| [FIDO2\_AttestationConveyancePreference](passkey.md#fido2_attestationconveyancepreference-1) [attestation](_f_i_d_o2___public_key_credential_creation_options.md#attestation) | 凭据传递首选项。默认值为none，可选。 |
| [FIDO2\_AttestationFormatsArray](_f_i_d_o2___attestation_formats_array.md) [attestationFormats](_f_i_d_o2___public_key_credential_creation_options.md#attestationformats) | 依赖方可以使用此选项指定有关认证方使用的证明声明格式的偏好。默认值为[]。 |
| char \* [extensions](_f_i_d_o2___public_key_credential_creation_options.md#extensions) | 扩展名必须是表示Map<string, Object>对象的JSON字符串。默认空。可选。 |

## 结构体成员变量说明

### attestation

```
1. FIDO2_AttestationConveyancePreference FIDO2_PublicKeyCredentialCreationOptions::attestation
```

**描述**

凭据传递首选项。默认值为none，可选。

### attestationFormats

```
1. FIDO2_AttestationFormatsArray FIDO2_PublicKeyCredentialCreationOptions::attestationFormats
```

**描述**

依赖方可以使用此选项指定有关认证方使用的证明声明格式的偏好。默认值为[]。

### authenticatorSelection

```
1. FIDO2_AuthenticatorSelectionCriteria FIDO2_PublicKeyCredentialCreationOptions::authenticatorSelection
```

**描述**

身份认证器相关配置项。

### challenge

```
1. Uint8Buff FIDO2_PublicKeyCredentialCreationOptions::challenge
```

**描述**

挑战。

### excludeCredentials

```
1. FIDO2_PublicKeyCredentialDescriptorArray FIDO2_PublicKeyCredentialCreationOptions::excludeCredentials
```

**描述**

FIDO服务器已注册的凭据列表。默认值为[]。可选。

### extensions

```
1. char* FIDO2_PublicKeyCredentialCreationOptions::extensions
```

**描述**

扩展名必须是表示Map<string, Object>对象的JSON字符串。可选。

### hints

```
1. FIDO2_PublicKeyCredentialHintArray FIDO2_PublicKeyCredentialCreationOptions::hints
```

**描述**

认证方式指示。默认值为[]。可选。

### pubKeyCredParams

```
1. FIDO2_CredentialCreationOptionArray FIDO2_PublicKeyCredentialCreationOptions::pubKeyCredParams
```

**描述**

认证凭据的附加参数数组。

### rp

```
1. FIDO2_PublicKeyCredentialRpEntity FIDO2_PublicKeyCredentialCreationOptions::rp
```

**描述**

创建新凭据时的依赖方属性。

### timeout

```
1. uint32_t FIDO2_PublicKeyCredentialCreationOptions::timeout
```

**描述**

注册操作最长时间，单位为毫秒。可选。

### user

```
1. FIDO2_PublicKeyCredentialUserEntity FIDO2_PublicKeyCredentialCreationOptions::user
```

**描述**

创建新凭据时用户的属性。
