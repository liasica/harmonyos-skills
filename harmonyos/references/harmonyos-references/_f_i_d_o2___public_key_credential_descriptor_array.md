---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_f_i_d_o2___public_key_credential_descriptor_array
title: FIDO2_PublicKeyCredentialDescriptorArray
breadcrumb: API参考 > 系统 > 安全 > Online Authentication Kit（在线认证服务） > C API > 结构体 > FIDO2_PublicKeyCredentialDescriptorArray
category: harmonyos-references
scraped_at: 2026-04-28T08:07:32+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:9c78c35c07ce6ae26b44eff3bb0aeee100cfe2740471f7e8ae82b90aee9ff2a5
---

## 概述

PublicKey凭证描述符数组。

**起始版本：** 6.0.0(20)

**相关模块：** [FIDO2](passkey.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| uint32\_t [allowCredentiallNum](_f_i_d_o2___public_key_credential_descriptor_array.md#allowcredentiallnum) | 允许凭证数目。 |
| [FIDO2\_PublicKeyCredentialDescriptor](_f_i_d_o2___public_key_credential_descriptor.md) \* [allowCredentials](_f_i_d_o2___public_key_credential_descriptor_array.md#allowcredentials) | 认证凭据的附加参数列表。默认值为[]。 |

## 结构体成员变量说明

### allowCredentiallNum

```
1. uint32_t FIDO2_PublicKeyCredentialDescriptorArray::allowCredentiallNum
```

**描述**

允许凭证数目。

### allowCredentials

```
1. FIDO2_PublicKeyCredentialDescriptor* FIDO2_PublicKeyCredentialDescriptorArray::allowCredentials
```

**描述**

认证凭据的附加参数列表。默认值为[]。
