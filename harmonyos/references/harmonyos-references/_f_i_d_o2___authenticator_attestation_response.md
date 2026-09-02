---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_f_i_d_o2___authenticator_attestation_response
title: FIDO2_AuthenticatorAttestationResponse
breadcrumb: API参考 > 系统 > 安全 > Online Authentication Kit（在线认证服务） > C API > 结构体 > FIDO2_AuthenticatorAttestationResponse
category: harmonyos-references
scraped_at: 2026-09-02T15:01:45+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:9baed856ab76f5900453e462c6f4d94babfd2e909f60b86e5a987aeaa4787241
---

## 概述

认证器声明响应。

**起始版本：** 6.0.0(20)

**相关模块：** [FIDO2（通行密钥服务）](passkey.md)

**所在头文件：** [fido2\_api.h](onlineauthentication_capi_header_fido2.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| [Uint8Buff](_uint8_buff.md) [attestationObject](_f_i_d_o2___authenticator_attestation_response.md#attestationobject) | 注册凭证的响应报文中，用于向服务器证明新生成密钥对合法性的数据结构。 |
| [Uint8Buff](_uint8_buff.md) [clientDataJson](_f_i_d_o2___authenticator_attestation_response.md#clientdatajson) | 获取客户端数据，表示WebAuthn依赖方和客户端的上下文绑定，包含类型、挑战值及源等数据。 |
| [Uint8Buff](_uint8_buff.md) [publicKey](_f_i_d_o2___authenticator_attestation_response.md#publickey) | 注册时生成的公钥数据，包含公钥算法类型和密钥参数，用于服务器保存并后续验证认证签名。 |
| [Uint8Buff](_uint8_buff.md) [authenticatorData](_f_i_d_o2___authenticator_attestation_response.md#authenticatordata) | 认证器数据，包含依赖方ID哈希、用户存在/已验证标志位、签名计数器、凭证数据等信息，用于验证认证响应的合法性。 |
| [FIDO2\_Algorithm](passkey.md#fido2_algorithm-1) [publicKeyAlgorithm](_f_i_d_o2___authenticator_attestation_response.md#publickeyalgorithm) | 密码算法。 |
| [FIDO2\_AuthenticatorTransportArray](_f_i_d_o2___authenticator_transport_array.md) [transports](_f_i_d_o2___authenticator_attestation_response.md#transports) | 定义身份认证器访问类型数组。 |

## 结构体成员变量说明

### attestationObject

```cpp
Uint8Buff FIDO2_AuthenticatorAttestationResponse::attestationObject
```

**描述**

注册凭证的响应报文中，用于向服务器证明新生成密钥对合法性的数据结构。

### authenticatorData

```cpp
Uint8Buff FIDO2_AuthenticatorAttestationResponse::authenticatorData
```

**描述**

认证器数据，包含依赖方ID哈希、用户存在/已验证标志位、签名计数器、凭证数据等信息，用于验证认证响应的合法性。

### clientDataJson

```cpp
Uint8Buff FIDO2_AuthenticatorAttestationResponse::clientDataJson
```

**描述**

获取客户端数据，表示WebAuthn依赖方和客户端的上下文绑定，包含类型、挑战值及源等数据。

### publicKey

```cpp
Uint8Buff FIDO2_AuthenticatorAttestationResponse::publicKey
```

**描述**

注册时生成的公钥数据，包含公钥算法类型和密钥参数，用于服务器保存并后续验证认证签名。

### publicKeyAlgorithm

```cpp
FIDO2_Algorithm FIDO2_AuthenticatorAttestationResponse::publicKeyAlgorithm
```

**描述**

密码算法。

### transports

```cpp
FIDO2_AuthenticatorTransportArray FIDO2_AuthenticatorAttestationResponse::transports
```

**描述**

定义身份认证器访问类型数组。
