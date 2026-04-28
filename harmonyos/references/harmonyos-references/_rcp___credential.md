---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___credential
title: Rcp_Credential
breadcrumb: API参考 > 系统 > 网络 > Remote Communication Kit（远场通信服务） > C API > 结构体 > Rcp_Credential
category: harmonyos-references
scraped_at: 2026-04-28T08:09:02+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:2c98ac6f9bc477030644de3a098a0dd9fc5d88a7d300a1a37e34579341f75576
---

## 概述

PhonePC/2in1TabletTVWearable

服务器身份验证中使用的身份验证凭据，包括用户名和密码。

**起始版本：** 5.0.0(12)

**相关模块：** [RemoteCommunication](remote-communication-overview.md)

**所在头文件：** [rcp.h](rcp_8h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| char \* [username](_rcp___credential.md#username) | 凭据的用户名。默认值为""。 |
| char \* [password](_rcp___credential.md#password) | 凭据的密码。默认值为""。 |

## 结构体成员变量说明

PhonePC/2in1TabletTVWearable

### password

PhonePC/2in1TabletTVWearable

```
1. char* Rcp_Credential::password
```

**描述**

凭据的密码。默认值为""。

### username

PhonePC/2in1TabletTVWearable

```
1. char* Rcp_Credential::username
```

**描述**

凭据的用户名。默认值为""。
