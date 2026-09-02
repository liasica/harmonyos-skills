---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_f_i_d_o2___capability_array
title: FIDO2_CapabilityArray
breadcrumb: API参考 > 系统 > 安全 > Online Authentication Kit（在线认证服务） > C API > 结构体 > FIDO2_CapabilityArray
category: harmonyos-references
scraped_at: 2026-09-02T15:01:45+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:342e7dd6445948c057d3b18f61f5864715a02691d846639617e3f316839bca93
---

## 概述

描述能力数组。

**起始版本：** 6.0.0(20)

**相关模块：** [FIDO2（通行密钥服务）](passkey.md)

**所在头文件：** [fido2\_api.h](onlineauthentication_capi_header_fido2.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| uint32\_t [number](_f_i_d_o2___capability_array.md#number) | 能力数组长度。 |
| [FIDO2\_Capability](_f_i_d_o2___capability.md) \* [capability](_f_i_d_o2___capability_array.md#capability) | 能力的数组。 |

## 结构体成员变量说明

### capability

```cpp
FIDO2_Capability* FIDO2_CapabilityArray::capability
```

**描述**

能力数组。

### number

```cpp
uint32_t FIDO2_CapabilityArray::number
```

**描述**

能力数组长度。
