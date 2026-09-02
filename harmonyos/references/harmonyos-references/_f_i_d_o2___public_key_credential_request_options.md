---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_f_i_d_o2___public_key_credential_request_options
title: FIDO2_PublicKeyCredentialRequestOptions
breadcrumb: API参考 > 系统 > 安全 > Online Authentication Kit（在线认证服务） > C API > 结构体 > FIDO2_PublicKeyCredentialRequestOptions
category: harmonyos-references
scraped_at: 2026-09-02T15:01:45+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:6fbe6c2d2178f88e454d73eadb234327e0b4b99372f512959129105632c92ee7
---

## 概述

定义通行密钥认证请求参数。

**起始版本：** 6.0.0(20)

**相关模块：** [FIDO2（通行密钥服务）](passkey.md)

**所在头文件：** [fido2\_api.h](onlineauthentication_capi_header_fido2.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| [Uint8Buff](_uint8_buff.md) [challenge](_f_i_d_o2___public_key_credential_request_options.md#challenge) | 获取挑战值。 |
| uint32\_t [timeout](_f_i_d_o2___public_key_credential_request_options.md#timeout) | 超时时间。单位为ms。默认为300000（5分钟），限制为0到600000（10分钟）。可选。 |
| char \* [rpId](_f_i_d_o2___public_key_credential_request_options.md#rpid) | 依赖方标识（如域名等）。默认空。可选。 |
| [FIDO2\_PublicKeyCredentialDescriptorArray](_f_i_d_o2___public_key_credential_descriptor_array.md) [allowCredentials](_f_i_d_o2___public_key_credential_request_options.md#allowcredentials) | 认证凭据的附加参数列表。默认空列表。可选。 |
| [FIDO2\_UserVerificationRequirement](passkey.md#fido2_userverificationrequirement-1) [userVerification](_f_i_d_o2___public_key_credential_request_options.md#userverification) | 用户认证需求枚举。默认值为FIDO2\_PREFERRED。可选。 |
| [FIDO2\_PublicKeyCredentialHintArray](_f_i_d_o2___public_key_credential_hint_array.md) [hints](_f_i_d_o2___public_key_credential_request_options.md#hints) | 认证方式指示。默认值为[]。可选。 |
| char \* [extensions](_f_i_d_o2___public_key_credential_request_options.md#extensions) | 扩展名必须是表示Map<string, Object> object的JSON字符串。默认空。可选，最小长度为0字符，最大长度为2048字符。 |

## 结构体成员变量说明

### allowCredentials

```cpp
FIDO2_PublicKeyCredentialDescriptorArray FIDO2_PublicKeyCredentialRequestOptions::allowCredentials
```

**描述**

认证凭据的附加参数列表。可选。

### challenge

```cpp
Uint8Buff FIDO2_PublicKeyCredentialRequestOptions::challenge
```

**描述**

获取挑战值。

### extensions

```cpp
char* FIDO2_PublicKeyCredentialRequestOptions::extensions
```

**描述**

扩展名必须是表示Map<string, Object> object的JSON字符串。可选。

### hints

```cpp
FIDO2_PublicKeyCredentialHintArray FIDO2_PublicKeyCredentialRequestOptions::hints
```

**描述**

认证方式指示。默认值为[]。可选。

### rpId

```cpp
char* FIDO2_PublicKeyCredentialRequestOptions::rpId
```

**描述**

依赖方标识。可选。

### timeout

```cpp
uint32_t FIDO2_PublicKeyCredentialRequestOptions::timeout
```

**描述**

超时时间。单位为ms。默认为300000（5分钟），限制为0到600000（10分钟）。可选。

### userVerification

```cpp
FIDO2_UserVerificationRequirement FIDO2_PublicKeyCredentialRequestOptions::userVerification
```

**描述**

用户认证需求枚举。默认值为FIDO2\_PREFERRED。可选。
