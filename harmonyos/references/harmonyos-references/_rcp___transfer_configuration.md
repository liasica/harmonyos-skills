---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___transfer_configuration
title: Rcp_TransferConfiguration
breadcrumb: API参考 > 系统 > 网络 > Remote Communication Kit（远场通信服务） > C API > 结构体 > Rcp_TransferConfiguration
category: harmonyos-references
scraped_at: 2026-04-28T08:09:10+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:f61ea0fb62384fb63de179e7408774b52a4a76305d2f070089cbd8df90936af9
---

## 概述

PhonePC/2in1TabletTVWearable

传输配置。

**起始版本：** 5.0.0(12)

**相关模块：** [RemoteCommunication](remote-communication-overview.md)

**所在头文件：** [rcp.h](rcp_8h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| bool [autoRedirect](_rcp___transfer_configuration.md#autoredirect) | 是否自动遵循HTTP重定向响应。默认为True。 |
| [Rcp\_Timeout](_rcp___timeout.md)[timeout](_rcp___transfer_configuration.md#timeout) | 超时配置。如果未设置此选项，将应用默认超时。 |
| bool [assumesHTTP3Capable](_rcp___transfer_configuration.md#assumeshttp3capable) | 是否假定目标服务器支持HTTP/3。默认值为false。 |
| [Rcp\_PathPreference](remote-communication-overview.md#rcp_pathpreference)[pathPreference](_rcp___transfer_configuration.md#pathpreference) | 请求路径首选项。 |

## 结构体成员变量说明

PhonePC/2in1TabletTVWearable

### assumesHTTP3Capable

PhonePC/2in1TabletTVWearable

```
1. bool Rcp_TransferConfiguration::assumesHTTP3Capable
```

**描述**

是否假定目标服务器支持HTTP/3。默认值为false。

### autoRedirect

PhonePC/2in1TabletTVWearable

```
1. bool Rcp_TransferConfiguration::autoRedirect
```

**描述**

是否自动遵循HTTP重定向响应。默认为True。

### pathPreference

PhonePC/2in1TabletTVWearable

```
1. Rcp_PathPreference Rcp_TransferConfiguration::pathPreference
```

**描述**

请求路径首选项。

### timeout

PhonePC/2in1TabletTVWearable

```
1. Rcp_Timeout Rcp_TransferConfiguration::timeout
```

**描述**

超时配置。如果未设置此选项，将应用默认超时。如果已配置，则使用配置的超时时间。
