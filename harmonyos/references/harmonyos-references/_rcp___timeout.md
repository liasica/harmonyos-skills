---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___timeout
title: Rcp_Timeout
breadcrumb: API参考 > 系统 > 网络 > Remote Communication Kit（远场通信服务） > C API > 结构体 > Rcp_Timeout
category: harmonyos-references
scraped_at: 2026-09-02T15:01:59+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:5457042589659f6627a84a85fd6dbb81694c484b967d4d342b98a214b517b36a
---

## 概述

请求的超时配置。

**起始版本：** 5.0.0(12)

**相关模块：** [RemoteCommunication](remote-communication-overview.md)

**所在头文件：** [rcp.h](rcp_8h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| uint32\_t [connectMs](_rcp___timeout.md#connectms) | 连接超时时间。默认值为60000毫秒。 |
| uint32\_t [transferMs](_rcp___timeout.md#transferms) | 传输超时时间。默认值为60000毫秒。 |

## 结构体成员变量说明

### connectMs

```cpp
uint32_t Rcp_Timeout::connectMs
```

**描述**

连接超时时间。默认值为60000毫秒。

### transferMs

```cpp
uint32_t Rcp_Timeout::transferMs
```

**描述**

传输超时时间。默认值为60000毫秒。
