---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_f_i_d_o2___public_key_credential_descriptor
title: FIDO2_PublicKeyCredentialDescriptor
breadcrumb: API参考 > 系统 > 安全 > Online Authentication Kit（在线认证服务） > C API > 结构体 > FIDO2_PublicKeyCredentialDescriptor
category: harmonyos-references
scraped_at: 2026-09-02T15:01:45+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:39864354df123d94904cef12ccd02d8fc4bf92c6be6fc6d02073142655000ed3
---

## 概述

用于注册或认证凭据的参数。

**起始版本：** 6.0.0(20)

**相关模块：** [FIDO2（通行密钥服务）](passkey.md)

**所在头文件：** [fido2\_api.h](onlineauthentication_capi_header_fido2.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| [FIDO2\_PublicKeyCredentialType](passkey.md#fido2_publickeycredentialtype-1) [type](_f_i_d_o2___public_key_credential_descriptor.md#type) | 凭证类型。 |
| [Uint8Buff](_uint8_buff.md) [id](_f_i_d_o2___public_key_credential_descriptor.md#id) | 凭据标识符。 |
| [FIDO2\_AuthenticatorTransportArray](_f_i_d_o2___authenticator_transport_array.md) [transports](_f_i_d_o2___public_key_credential_descriptor.md#transports) | 定义身份认证器访问类型数组。 |

## 结构体成员变量说明

### id

```cpp
Uint8Buff FIDO2_PublicKeyCredentialDescriptor::id
```

**描述**

凭据标识符。

### transports

```cpp
FIDO2_AuthenticatorTransportArray FIDO2_PublicKeyCredentialDescriptor::transports
```

**描述**

定义身份认证器访问类型数组。

### type

```cpp
FIDO2_PublicKeyCredentialType FIDO2_PublicKeyCredentialDescriptor::type
```

**描述**

凭证类型。
