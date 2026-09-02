---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_f_i_d_o2___capability
title: FIDO2_Capability
breadcrumb: API参考 > 系统 > 安全 > Online Authentication Kit（在线认证服务） > C API > 结构体 > FIDO2_Capability
category: harmonyos-references
scraped_at: 2026-09-02T15:01:45+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:17c8458ff78b3a2a73218103259ce75b233f5000d766579669003c0485c5849d
---

## 概述

通行密钥能力的结构体。

**起始版本：** 6.0.0(20)

**相关模块：** [FIDO2（通行密钥服务）](passkey.md)

**所在头文件：** [fido2\_api.h](onlineauthentication_capi_header_fido2.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| [FIDO2\_ClientCapability](passkey.md#fido2_clientcapability-1) [capability](_f_i_d_o2___capability.md#capability) | 通行密钥的能力。 |
| bool [isSupported](_f_i_d_o2___capability.md#issupported) | 是否支持。如果为true表示支持，false表示不支持。 |

## 结构体成员变量说明

### capability

```cpp
FIDO2_ClientCapability FIDO2_Capability::capability
```

**描述**

通行密钥的能力。

### isSupported

```cpp
bool FIDO2_Capability::isSupported
```

**描述**

是否支持。如果为true表示支持，false表示不支持。
