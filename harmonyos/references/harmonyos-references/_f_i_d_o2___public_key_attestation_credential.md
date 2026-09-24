---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_f_i_d_o2___public_key_attestation_credential
title: FIDO2_PublicKeyAttestationCredential
breadcrumb: API参考 > 系统 > 安全 > Online Authentication Kit（在线认证服务） > C API > 结构体 > FIDO2_PublicKeyAttestationCredential
category: harmonyos-references
scraped_at: 2026-09-25T07:11:32+08:00
doc_updated_at: 2026-09-24
content_hash: sha256:5871e917d4448848ca0f8eba2ae087336308074a38a32fc57d8321aab4434c66
---

## 概述

定义获取注册结果结构体。

**起始版本：** 6.0.0(20)

**相关模块：** [FIDO2（通行密钥服务）](passkey.md)

**所在头文件：** [fido2\_api.h](onlineauthentication_capi_header_fido2.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| [Uint8Buff](_uint8_buff.md) [rawId](_f_i_d_o2___public_key_attestation_credential.md#rawid) | 原始凭据标识符。 |
| [FIDO2\_AuthenticatorAttestationResponse](_f_i_d_o2___authenticator_attestation_response.md) [response](_f_i_d_o2___public_key_attestation_credential.md#response) | 认证器证明响应。 |
| [FIDO2\_AuthenticatorAttachment](passkey.md#fido2_authenticatorattachment-1) [authenticatorAttachment](_f_i_d_o2___public_key_attestation_credential.md#authenticatorattachment) | 认证器信息（FIDO2\_PLATFORM表示平台，FIDO2\_CROSS\_PLATFORM表示漫游）。默认值为FIDO2\_PLATFORM。可选。 |
| const char \* [id](_f_i_d_o2___public_key_attestation_credential.md#id) | 凭据的标识符。对于每种类型的凭据，标识符的要求都是不同的。 |
| const char \* [type](_f_i_d_o2___public_key_attestation_credential.md#type) | 该属性以JSON字符串形式返回接口对象中用于指定凭据类型的插槽，该插槽用于指定此对象所表示的凭据类型。 |
| [AuthenticationExtensionsClientOutputs](_authentication_extensions_client_outputs.md) [clientExtensionResults](_f_i_d_o2___public_key_attestation_credential.md#clientextensionresults) | 客户端扩展结果。当前版本不支持扩展，因此占位符始终为NULL，必须将clientExtensionResults键对应的值解析为{}。 |

## 结构体成员变量说明

### authenticatorAttachment

```cpp
FIDO2_AuthenticatorAttachment FIDO2_PublicKeyAttestationCredential::authenticatorAttachment
```

**描述**

认证器信息（平台、漫游）。默认值为FIDO2\_PLATFORM。可选。

### clientExtensionResults

```cpp
AuthenticationExtensionsClientOutputs FIDO2_PublicKeyAttestationCredential::clientExtensionResults
```

**描述**

客户端扩展结果。当前版本不支持扩展，因此占位符始终为NULL，必须将clientExtensionResults键对应的值解析为{}。

### id

```cpp
const char* FIDO2_PublicKeyAttestationCredential::id
```

**描述**

凭据的标识符。对于每种类型的凭据，标识符的要求都是不同的。

### rawId

```cpp
Uint8Buff FIDO2_PublicKeyAttestationCredential::rawId
```

**描述**

原始凭据标识符。

### response

```cpp
FIDO2_AuthenticatorAttestationResponse FIDO2_PublicKeyAttestationCredential::response
```

**描述**

认证器证明响应。

### type

```cpp
const char* FIDO2_PublicKeyAttestationCredential::type
```

**描述**

该属性以JSON字符串形式返回接口对象中用于指定凭据类型的插槽，该插槽用于指定此对象所表示的凭据类型。
