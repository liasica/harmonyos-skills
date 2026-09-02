---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___server_authentication
title: Rcp_ServerAuthentication
breadcrumb: API参考 > 系统 > 网络 > Remote Communication Kit（远场通信服务） > C API > 结构体 > Rcp_ServerAuthentication
category: harmonyos-references
scraped_at: 2026-09-02T15:01:59+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:6451a80b8648e6bcf238efa1de177b2a471ecfe01c1681c3858050b2d0caa5d4
---

## 概述

服务器身份验证。

**起始版本：** 5.0.0(12)

**相关模块：** [RemoteCommunication](remote-communication-overview.md)

**所在头文件：** [rcp.h](rcp_8h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| [Rcp\_Credential](_rcp___credential.md) [credential](_rcp___server_authentication.md#credential) | 服务器的凭据。 |
| [Rcp\_AuthenticationType](remote-communication-overview.md#rcp_authenticationtype) [authenticationType](_rcp___server_authentication.md#authenticationtype) | 服务器的身份验证类型。如果未设置，请与服务器协商。 |

## 结构体成员变量说明

### authenticationType

```cpp
Rcp_AuthenticationType Rcp_ServerAuthentication::authenticationType
```

**描述**

服务器的身份验证类型。如果未设置，请与服务器协商。

### credential

```cpp
Rcp_Credential Rcp_ServerAuthentication::credential
```

**描述**

服务器的凭据。
