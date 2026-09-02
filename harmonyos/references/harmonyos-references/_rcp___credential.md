---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___credential
title: Rcp_Credential
breadcrumb: API参考 > 系统 > 网络 > Remote Communication Kit（远场通信服务） > C API > 结构体 > Rcp_Credential
category: harmonyos-references
scraped_at: 2026-09-02T15:01:58+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:86be066675a05a27a805288560bd59936ebc2297a718e11dcabbb4790105e67d
---

## 概述

服务器身份验证中使用的身份验证凭据，包括用户名和密码。

**起始版本：** 5.0.0(12)

**相关模块：** [RemoteCommunication](remote-communication-overview.md)

**所在头文件：** [rcp.h](rcp_8h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| char \* [username](_rcp___credential.md#username) | 凭据的用户名。默认值为""。 |
| char \* [password](_rcp___credential.md#password) | 凭据的密码。默认值为""。 |

## 结构体成员变量说明

### password

```cpp
char* Rcp_Credential::password
```

**描述**

凭据的密码。默认值为""。

### username

```cpp
char* Rcp_Credential::username
```

**描述**

凭据的用户名。默认值为""。
