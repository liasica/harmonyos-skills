---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___connection_configuration
title: Rcp_ConnectionConfiguration
breadcrumb: API参考 > 系统 > 网络 > Remote Communication Kit（远场通信服务） > C API > 结构体 > Rcp_ConnectionConfiguration
category: harmonyos-references
scraped_at: 2026-04-28T08:09:01+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:ef27063c986b44b58e9673936debc5790a85d0d8881275472abc6c6c38058501
---

## 概述

PhonePC/2in1TabletTVWearable

连接配置。

**起始版本：** 5.0.0(12)

**相关模块：** [RemoteCommunication](remote-communication-overview.md)

**所在头文件：** [rcp.h](rcp_8h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| long [maxConnectionsPerHost](_rcp___connection_configuration.md#maxconnectionsperhost) | 每台主机的最大连接数。  取值范围：1~2147483647。  默认值：6。 |
| long [maxTotalConnections](_rcp___connection_configuration.md#maxtotalconnections) | 最大总连接数。  取值范围：1~2147483647。  默认值为 64。 |
| long [maxCacheConnections](_rcp___connection_configuration.md#maxcacheconnections) | 最大缓存连接数。  取值范围：1~2147483647。  默认值为 64。 |

## 结构体成员变量说明

PhonePC/2in1TabletTVWearable

### maxCacheConnections

PhonePC/2in1TabletTVWearable

```
1. long Rcp_ConnectionConfiguration::maxCacheConnections
```

**描述**

最大缓存连接数。

### maxConnectionsPerHost

PhonePC/2in1TabletTVWearable

```
1. long Rcp_ConnectionConfiguration::maxConnectionsPerHost
```

**描述**

每台主机的最大连接数。

### maxTotalConnections

PhonePC/2in1TabletTVWearable

```
1. long Rcp_ConnectionConfiguration::maxTotalConnections
```

**描述**

最大总连接数。范围由long决定。
