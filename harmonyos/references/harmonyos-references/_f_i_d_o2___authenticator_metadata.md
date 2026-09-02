---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_f_i_d_o2___authenticator_metadata
title: FIDO2_AuthenticatorMetadata
breadcrumb: API参考 > 系统 > 安全 > Online Authentication Kit（在线认证服务） > C API > 结构体 > FIDO2_AuthenticatorMetadata
category: harmonyos-references
scraped_at: 2026-09-02T15:01:45+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:177210bd1b8fb0c478b22c9066908242c4d6c60705331b6d14bb4d16db230362
---

## 概述

认证器元数据。

**起始版本：** 6.0.0(20)

**相关模块：** [FIDO2（通行密钥服务）](passkey.md)

**所在头文件：** [fido2\_api.h](onlineauthentication_capi_header_fido2.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| [Uint8Buff](_uint8_buff.md) [aaguid](_f_i_d_o2___authenticator_metadata.md#aaguid) | 认证器的唯一标识符。 |
| [FIDO2\_Uvm](passkey.md#fido2_uvm-1) [uvm](_f_i_d_o2___authenticator_metadata.md#uvm) | 支持的认证器类型。 |
| bool [isAvailable](_f_i_d_o2___authenticator_metadata.md#isavailable) | 认证器是否可用。如果返回true，则表示认证器可用；返回false，表示认证器不可用。 |

## 结构体成员变量说明

### aaguid

```cpp
Uint8Buff FIDO2_AuthenticatorMetadata::aaguid
```

**描述**

认证器的唯一标识符。

### isAvailable

```cpp
bool FIDO2_AuthenticatorMetadata::isAvailable
```

**描述**

认证器是否可用。如果返回true，则表示认证器可用；返回false，表示认证器不可用。

### uvm

```cpp
FIDO2_Uvm FIDO2_AuthenticatorMetadata::uvm
```

**描述**

支持的认证器类型。
