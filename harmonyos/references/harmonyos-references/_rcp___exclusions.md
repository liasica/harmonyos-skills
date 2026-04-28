---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___exclusions
title: Rcp_Exclusions
breadcrumb: API参考 > 系统 > 网络 > Remote Communication Kit（远场通信服务） > C API > 结构体 > Rcp_Exclusions
category: harmonyos-references
scraped_at: 2026-04-28T08:09:03+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:d734eedf3895fe9e3473d143619179d2f49b29b4ae7a1222430e76beca5cce1a
---

## 概述

PhonePC/2in1TabletTVWearable

代理配置中用于过滤不使用代理的urls。

如果[Rcp\_Request.url](_rcp___request.md#url)匹配[Rcp\_Exclusions](_rcp___exclusions.md)规则，则[Rcp\_Request](_rcp___request.md)不会使用代理。

**起始版本：** 5.0.0(12)

**相关模块：** [RemoteCommunication](remote-communication-overview.md)

**所在头文件：** [rcp.h](rcp_8h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [Rcp\_ExclusionsValueType](remote-communication-overview.md#rcp_exclusionsvaluetype)[type](_rcp___exclusions.md#type) | 表示union中使用的数据类型。 |
| union {  [Rcp\_Urls](_rcp___urls.md) \* [urls](_rcp___exclusions.md#urls)  [Rcp\_ExclusionFunction](remote-communication-overview.md#rcp_exclusionfunction) [exclusionFunction](_rcp___exclusions.md#exclusionfunction)  } | Urls。链式存储url。  回调函数。通过回调函数过滤url。 |

## 结构体成员变量说明

PhonePC/2in1TabletTVWearable

### exclusionFunction

PhonePC/2in1TabletTVWearable

```
1. Rcp_ExclusionFunction Rcp_Exclusions::exclusionFunction
```

**描述**

通过回调过滤。

### type

PhonePC/2in1TabletTVWearable

```
1. Rcp_ExclusionsValueType Rcp_Exclusions::type
```

**描述**

表示union中使用的数据类型。

### urls

PhonePC/2in1TabletTVWearable

```
1. Rcp_Urls* Rcp_Exclusions::urls
```

**描述**

Urls。
