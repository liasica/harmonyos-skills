---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_f_i_d_o2___public_key_credential_rp_entity
title: FIDO2_PublicKeyCredentialRpEntity
breadcrumb: API参考 > 系统 > 安全 > Online Authentication Kit（在线认证服务） > C API > 结构体 > FIDO2_PublicKeyCredentialRpEntity
category: harmonyos-references
scraped_at: 2026-09-02T15:01:45+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:b7b564fe1e9a6ab3a9d70093be4858854167de02a6e7800a2306f4b15bfab75b
---

## 概述

创建新凭据时依赖方的属性。

**起始版本：** 6.0.0(20)

**相关模块：** [FIDO2（通行密钥服务）](passkey.md)

**所在头文件：** [fido2\_api.h](onlineauthentication_capi_header_fido2.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| char \* [id](_f_i_d_o2___public_key_credential_rp_entity.md#id) | 依赖方标识符。默认值为空。长度限制0到512。 |
| char \* [name](_f_i_d_o2___public_key_credential_rp_entity.md#name) | 依赖方名称。 长度限制0到512。 |

## 结构体成员变量说明

### id

```cpp
char* FIDO2_PublicKeyCredentialRpEntity::id
```

**描述**

依赖方标识符。

### name

```cpp
char* FIDO2_PublicKeyCredentialRpEntity::name
```

**描述**

依赖方名称。
