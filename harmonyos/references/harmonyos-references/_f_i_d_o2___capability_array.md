---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_f_i_d_o2___capability_array
title: FIDO2_CapabilityArray
breadcrumb: API参考 > 系统 > 安全 > Online Authentication Kit（在线认证服务） > C API > 结构体 > FIDO2_CapabilityArray
category: harmonyos-references
scraped_at: 2026-04-28T08:07:30+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:95bf62b2e3ce7af409e8ae245ce05e26f852cfdefca1c21e7730e2fd740b0665
---

## 概述

描述能力数组。

**起始版本：** 6.0.0(20)

**相关模块：** [FIDO2](passkey.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| uint32\_t [number](_f_i_d_o2___capability_array.md#number) | 能力的数量。 |
| [FIDO2\_Capability](_f_i_d_o2___capability.md) \* [capability](_f_i_d_o2___capability_array.md#capability) | 能力的数组。 |

## 结构体成员变量说明

### capability

```
1. FIDO2_Capability* FIDO2_CapabilityArray::capability
```

**描述**

能力数组。

### number

```
1. uint32_t FIDO2_CapabilityArray::number
```

**描述**

能力数组长度。
