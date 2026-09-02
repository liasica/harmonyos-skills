---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_f_i_d_o2___public_key_credential_user_entity
title: FIDO2_PublicKeyCredentialUserEntity
breadcrumb: API参考 > 系统 > 安全 > Online Authentication Kit（在线认证服务） > C API > 结构体 > FIDO2_PublicKeyCredentialUserEntity
category: harmonyos-references
scraped_at: 2026-09-02T15:01:45+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:59402f5b1088c3863306f0510ebc4aeb29e0f3545a7557df7d797caea065cf09
---

## 概述

创建新凭据时用户的属性。

**起始版本：** 6.0.0(20)

**相关模块：** [FIDO2（通行密钥服务）](passkey.md)

**所在头文件：** [fido2\_api.h](onlineauthentication_capi_header_fido2.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| [Uint8Buff](_uint8_buff.md) [id](_f_i_d_o2___public_key_credential_user_entity.md#id) | 凭据的标识符。 |
| char \* [displayName](_f_i_d_o2___public_key_credential_user_entity.md#displayname) | 前台显示的用户名。长度限制0到512。 |
| char \* [name](_f_i_d_o2___public_key_credential_user_entity.md#name) | 用户名。长度限制0到512。 |

## 结构体成员变量说明

### displayName

```cpp
char* FIDO2_PublicKeyCredentialUserEntity::displayName
```

**描述**

前台显示的用户名。

### id

```cpp
Uint8Buff FIDO2_PublicKeyCredentialUserEntity::id
```

**描述**

凭据的标识符。

### name

```cpp
char* FIDO2_PublicKeyCredentialUserEntity::name
```

**描述**

用户名。
