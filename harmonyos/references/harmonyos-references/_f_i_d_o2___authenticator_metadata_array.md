---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_f_i_d_o2___authenticator_metadata_array
title: FIDO2_AuthenticatorMetadataArray
breadcrumb: API参考 > 系统 > 安全 > Online Authentication Kit（在线认证服务） > C API > 结构体 > FIDO2_AuthenticatorMetadataArray
category: harmonyos-references
scraped_at: 2026-09-02T15:01:45+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:6781adb3cec9d450b01afd0c811c03f8928d692b1cca7917999ada2958a1404e
---

## 概述

描述支持的认证器数组。

**起始版本：** 6.0.0(20)

**相关模块：** [FIDO2（通行密钥服务）](passkey.md)

**所在头文件：** [fido2\_api.h](onlineauthentication_capi_header_fido2.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| uint32\_t [number](_f_i_d_o2___authenticator_metadata_array.md#number) | 认证器数目。 |
| [FIDO2\_AuthenticatorMetadata](_f_i_d_o2___authenticator_metadata.md) \* [authenticators](_f_i_d_o2___authenticator_metadata_array.md#authenticators) | 认证器支持的扩展。 |

## 结构体成员变量说明

### authenticators

```cpp
FIDO2_AuthenticatorMetadata* FIDO2_AuthenticatorMetadataArray::authenticators
```

**描述**

认证器支持的扩展。

### number

```cpp
uint32_t FIDO2_AuthenticatorMetadataArray::number
```

**描述**

认证器数目。
