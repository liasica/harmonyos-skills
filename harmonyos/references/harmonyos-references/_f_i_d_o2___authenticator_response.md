---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_f_i_d_o2___authenticator_response
title: FIDO2_AuthenticatorResponse
breadcrumb: API参考 > 系统 > 安全 > Online Authentication Kit（在线认证服务） > C API > 结构体 > FIDO2_AuthenticatorResponse
category: harmonyos-references
scraped_at: 2026-09-02T15:01:45+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:94d80325375a64e3b5483e5ad96b8d7cafb6869f6bb890eb593b3ba39e9cd7f2
---

## 概述

定义获取认证器断言响应的结构体。

**起始版本：** 6.0.0(20)

**相关模块：** [FIDO2（通行密钥服务）](passkey.md)

**所在头文件：** [fido2\_api.h](onlineauthentication_capi_header_fido2.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| [Uint8Buff](_uint8_buff.md) [authenticatorData](_f_i_d_o2___authenticator_response.md#authenticatordata) | 身份认证器数据。 |
| [Uint8Buff](_uint8_buff.md) [signature](_f_i_d_o2___authenticator_response.md#signature) | FIDO2认证的签名信息。 |
| [Uint8Buff](_uint8_buff.md) [userHandle](_f_i_d_o2___authenticator_response.md#userhandle) | 用户句柄（用户ID）。默认值为空。长度限制0到4096。可选。 |
| [Uint8Buff](_uint8_buff.md) [clientDataJson](_f_i_d_o2___authenticator_response.md#clientdatajson) | 获取客户端数据，表示WebAuthn依赖方和客户端的上下文绑定，包含类型、挑战值及源等数据。 |

## 结构体成员变量说明

### authenticatorData

```cpp
Uint8Buff FIDO2_AuthenticatorResponse::authenticatorData
```

**描述**

身份认证器数据。

### clientDataJson

```cpp
Uint8Buff FIDO2_AuthenticatorResponse::clientDataJson
```

**描述**

获取客户端数据，表示WebAuthn依赖方和客户端的上下文绑定，包含类型、挑战值及源等数据。

### signature

```cpp
Uint8Buff FIDO2_AuthenticatorResponse::signature
```

**描述**

FIDO2认证的签名信息。

### userHandle

```cpp
Uint8Buff FIDO2_AuthenticatorResponse::userHandle
```

**描述**

用户句柄。可选。
