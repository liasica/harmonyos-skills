---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_f_i_d_o2___attestation_formats_array
title: FIDO2_AttestationFormatsArray
breadcrumb: API参考 > 系统 > 安全 > Online Authentication Kit（在线认证服务） > C API > 结构体 > FIDO2_AttestationFormatsArray
category: harmonyos-references
scraped_at: 2026-09-02T15:01:45+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:bab157406d26df5102742257768ce423b2953bb024beb1c7b0cd80ce9a5862a5
---

## 概述

依赖方的数组可以使用此成员指定一个关于认证方使用的证明语句格式的首选项。

**起始版本：** 6.0.0(20)

**相关模块：** [FIDO2（通行密钥服务）](passkey.md)

**所在头文件：** [fido2\_api.h](onlineauthentication_capi_header_fido2.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| uint32\_t [attestationFormatsNum](_f_i_d_o2___attestation_formats_array.md#attestationformatsnum) | 认证凭据的附加参数列表长度。取值范围：[0, 10]。 |
| char \*\* [attestationFormats](_f_i_d_o2___attestation_formats_array.md#attestationformats) | 认证凭据的附加参数列表。 |

## 结构体成员变量说明

### attestationFormats

```cpp
char** FIDO2_AttestationFormatsArray::attestationFormats
```

**描述**

认证凭据的附加参数列表。

### attestationFormatsNum

```cpp
uint32_t FIDO2_AttestationFormatsArray::attestationFormatsNum
```

**描述**

认证凭据的附加参数列表长度。
