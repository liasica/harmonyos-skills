---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_f_i_d_o2___attestation_formats_array
title: FIDO2_AttestationFormatsArray
breadcrumb: API参考 > 系统 > 安全 > Online Authentication Kit（在线认证服务） > C API > 结构体 > FIDO2_AttestationFormatsArray
category: harmonyos-references
scraped_at: 2026-04-28T08:07:28+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:19313c8d7e4dc110e9b9d615ea322fc93548b83f2df54aad60740f24c0727e4c
---

## 概述

依赖方的数组可以使用此成员指定一个关于认证方使用的证明语句格式的首选项。

**起始版本：** 6.0.0(20)

**相关模块：** [FIDO2](passkey.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| uint32\_t [attestationFormatsNum](_f_i_d_o2___attestation_formats_array.md#attestationformatsnum) | PubKeyCredParam个数。 |
| char \*\* [attestationFormats](_f_i_d_o2___attestation_formats_array.md#attestationformats) | 认证凭据的附加参数列表。 |

## 结构体成员变量说明

### attestationFormats

```
1. char** FIDO2_AttestationFormatsArray::attestationFormats
```

**描述**

认证凭据的附加参数列表。

### attestationFormatsNum

```
1. uint32_t FIDO2_AttestationFormatsArray::attestationFormatsNum
```

**描述**

认证凭据的附加参数列表长度。
