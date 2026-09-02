---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_f_i_d_o2___public_key_credential_hint_array
title: FIDO2_PublicKeyCredentialHintArray
breadcrumb: API参考 > 系统 > 安全 > Online Authentication Kit（在线认证服务） > C API > 结构体 > FIDO2_PublicKeyCredentialHintArray
category: harmonyos-references
scraped_at: 2026-09-02T15:01:45+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:f73b3ca833ea5335576c0c1cf1cd7695bdbfc29d25004d7a0d05a0b3f0fc1d7f
---

## 概述

认证方式指示数组。

**起始版本：** 6.0.0(20)

**相关模块：** [FIDO2（通行密钥服务）](passkey.md)

**所在头文件：** [fido2\_api.h](onlineauthentication_capi_header_fido2.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| uint32\_t [hintNum](_f_i_d_o2___public_key_credential_hint_array.md#hintnum) | 认证方式指示数目。 |
| [FIDO2\_PublicKeyCredentialHint](passkey.md#fido2_publickeycredentialhint-1) \* [hints](_f_i_d_o2___public_key_credential_hint_array.md#hints) | 认证方式指示列表。 |

## 结构体成员变量说明

### hintNum

```cpp
uint32_t FIDO2_PublicKeyCredentialHintArray::hintNum
```

**描述**

认证方式指示数目。

### hints

```cpp
FIDO2_PublicKeyCredentialHint* FIDO2_PublicKeyCredentialHintArray::hints
```

**描述**

认证方式指示列表。
