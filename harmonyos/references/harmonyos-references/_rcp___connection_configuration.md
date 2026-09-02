---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___connection_configuration
title: Rcp_ConnectionConfiguration
breadcrumb: API参考 > 系统 > 网络 > Remote Communication Kit（远场通信服务） > C API > 结构体 > Rcp_ConnectionConfiguration
category: harmonyos-references
scraped_at: 2026-09-02T15:01:58+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:3039813c00a61c64b48e79e267b8bfde5ebf3df630804b29c7d5a140c8c38d1b
---

## 概述

连接配置。

**起始版本：** 5.0.0(12)

**相关模块：** [RemoteCommunication](remote-communication-overview.md)

**所在头文件：** [rcp.h](rcp_8h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| long [maxConnectionsPerHost](_rcp___connection_configuration.md#maxconnectionsperhost) | 每台主机的最大连接数。  取值范围：1~2147483647。  默认值：6。 |
| long [maxTotalConnections](_rcp___connection_configuration.md#maxtotalconnections) | 最大总连接数。  取值范围：1~2147483647。  默认值为 64。 |
| long [maxCacheConnections](_rcp___connection_configuration.md#maxcacheconnections) | 最大缓存连接数。  取值范围：1~2147483647。  默认值为 64。 |

## 结构体成员变量说明

### maxCacheConnections

```cpp
long Rcp_ConnectionConfiguration::maxCacheConnections
```

**描述**

最大缓存连接数。

### maxConnectionsPerHost

```cpp
long Rcp_ConnectionConfiguration::maxConnectionsPerHost
```

**描述**

每台主机的最大连接数。

### maxTotalConnections

```cpp
long Rcp_ConnectionConfiguration::maxTotalConnections
```

**描述**

最大总连接数。范围由long决定。
