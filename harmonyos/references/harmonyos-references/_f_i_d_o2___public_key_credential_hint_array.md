---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_f_i_d_o2___public_key_credential_hint_array
title: FIDO2_PublicKeyCredentialHintArray
breadcrumb: API参考 > 系统 > 安全 > Online Authentication Kit（在线认证服务） > C API > 结构体 > FIDO2_PublicKeyCredentialHintArray
category: harmonyos-references
scraped_at: 2026-04-28T08:07:32+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:91b377f3fd60c59240a70d973c953fcd7738cd3ad31e96dd2ef34554165015b5
---

## 概述

认证方式指示数组。

**起始版本：** 6.0.0(20)

**相关模块：** [FIDO2](passkey.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| uint32\_t [hintNum](_f_i_d_o2___public_key_credential_hint_array.md#hintnum) | 认证方式指示数目。 |
| [FIDO2\_PublicKeyCredentialHint](passkey.md#fido2_publickeycredentialhint-1) \* [hints](_f_i_d_o2___public_key_credential_hint_array.md#hints) | 认证方式指示列表。 |

## 结构体成员变量说明

### hintNum

```
1. uint32_t FIDO2_PublicKeyCredentialHintArray::hintNum
```

**描述**

认证方式指示数目。

### hints

```
1. FIDO2_PublicKeyCredentialHint* FIDO2_PublicKeyCredentialHintArray::hints
```

**描述**

认证方式指示列表。
