---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_f_i_d_o2___capability
title: FIDO2_Capability
breadcrumb: API参考 > 系统 > 安全 > Online Authentication Kit（在线认证服务） > C API > 结构体 > FIDO2_Capability
category: harmonyos-references
scraped_at: 2026-04-28T08:07:29+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:7064719894ff6b8e2f23ca8a7ea42b11f8dd0f7519b1140e6d2f99493aa86537
---

## 概述

通行密钥能力的结构体。

**起始版本：** 6.0.0(20)

**相关模块：** [FIDO2](passkey.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| [FIDO2\_ClientCapability](passkey.md#fido2_clientcapability-1) [capability](_f_i_d_o2___capability.md#capability) | 通行密钥的能力。 |
| bool [isSupported](_f_i_d_o2___capability.md#issupported) | 是否支持。如果为true表示支持，false表示不支持。 |

## 结构体成员变量说明

### capability

```
1. FIDO2_ClientCapability FIDO2_Capability::capability
```

**描述**

通行密钥的能力。

### isSupported

```
1. bool FIDO2_Capability::isSupported
```

**描述**

是否支持。如果为true表示支持，false表示不支持。
