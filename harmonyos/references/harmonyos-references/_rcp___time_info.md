---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___time_info
title: Rcp_TimeInfo
breadcrumb: API参考 > 系统 > 网络 > Remote Communication Kit（远场通信服务） > C API > 结构体 > Rcp_TimeInfo
category: harmonyos-references
scraped_at: 2026-09-02T15:01:59+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:c7cdcebfde9a944fe1dc9bb77c2b0771dcc835bcee1f268e4241855f27007ff2
---

## 概述

响应计时信息。

它将在[Rcp\_Response.timeInfo](_rcp___response.md#timeinfo)中被收集，[Rcp\_TracingConfiguration.collectTimeInfo](_rcp___tracing_configuration.md#collecttimeinfo)决定是否收集它。

**起始版本：** 5.0.0(12)

**相关模块：** [RemoteCommunication](remote-communication-overview.md)

**所在头文件：** [rcp.h](rcp_8h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| double [totalTime](_rcp___time_info.md#totaltime) | HTTP传输（包括名称解析、TCP连接等）的总时间（毫秒）。 |
| double [nameLookUpTime](_rcp___time_info.md#namelookuptime) | 从请求开始到完成远程主机名解析所用的时间（以毫秒为单位）。 |
| double [connectTime](_rcp___time_info.md#connecttime) | 从请求开始到建立与远程主机（或代理）的连接的时间（以毫秒为单位）。 |
| double [preTransferTime](_rcp___time_info.md#pretransfertime) | 从请求开始到准备就绪进行数据传输所花费的时间（以毫秒为单位）。 |
| double [fileTime](_rcp___time_info.md#filetime) | 从远程文件的上次修改时间开始的时间（以毫秒为单位）。 |
| double [startTransferTime](_rcp___time_info.md#starttransfertime) | 从开始到接收到第一个字节所花费的时间（以毫秒为单位）。 |
| double [redirectTime](_rcp___time_info.md#redirecttime) | 所有重定向步骤（包括名称查找、连接等）所用的时间（毫秒）。 |
| double [tlsHandshakeTime](_rcp___time_info.md#tlshandshaketime) | 从请求开始到建立与远程主机（或代理）的TLS握手的时间（以毫秒为单位）。 |

## 结构体成员变量说明

### connectTime

```cpp
double Rcp_TimeInfo::connectTime
```

**描述**

从请求开始到建立与远程主机（或代理）的连接时间（以毫秒为单位）。

### fileTime

```cpp
double Rcp_TimeInfo::fileTime
```

**描述**

从远程文件的上次修改时间开始的时间（以毫秒为单位）。

### nameLookUpTime

```cpp
double Rcp_TimeInfo::nameLookUpTime
```

**描述**

从请求开始到完成远程主机名解析所用的时间（以毫秒为单位）。

### preTransferTime

```cpp
double Rcp_TimeInfo::preTransferTime
```

**描述**

从请求开始到准备就绪进行数据传输所花费的时间（以毫秒为单位）。

### redirectTime

```cpp
double Rcp_TimeInfo::redirectTime
```

**描述**

所有重定向步骤（包括名称查找、连接等）所用的时间（毫秒）。

### startTransferTime

```cpp
double Rcp_TimeInfo::startTransferTime
```

**描述**

从开始到接收到第一个字节所花费的时间（以毫秒为单位）。

### tlsHandshakeTime

```cpp
double Rcp_TimeInfo::tlsHandshakeTime
```

**描述**

从请求开始到建立与远程主机（或代理）的TLS握手的时间（以毫秒为单位）。

### totalTime

```cpp
double Rcp_TimeInfo::totalTime
```

**描述**

HTTP传输（包括名称解析、TCP连接等）的总时间（毫秒）。
