---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/network-boost-c-struct-network_qos_array
title: NetworkBoost_NetworkQosArray
breadcrumb: API参考 > 系统 > 网络 > Network Boost Kit（网络加速服务） > C API > 结构体 > NetworkBoost_NetworkQosArray
category: harmonyos-references
scraped_at: 2026-09-02T15:01:57+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:0414705d8201e08ffb6bbc6465012e8a4b14cf841e7b9ce811113ade66b3ddd4
---

## 概述

网络质量变化的详细信息。

**起始版本：** 5.1.0(18)

**相关模块：** [NetworkBoost](network-boost-c-overview.md)

**所在头文件：** [network\_boost\_quality.h](network-boost-c-files-quality.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| uint32\_t [pathNum](network-boost-c-struct-network_qos_array.md#pathnum) | 网络质量信息中的路径数量，取值范围 [1, 4]。 |
| [NetworkBoost\_NetworkQos](network-boost-c-struct-network_qos.md) [networkQos](network-boost-c-struct-network_qos_array.md#networkqos) [[NETBOOST\_MAX\_PATH\_NUM](network-boost-c-overview.md#netboost_max_path_num)] | 多条路径的网络质量信息，每一项为一条路径的网络质量信息，取值范围 [0, pathNum-1]。 |

## 结构体成员变量说明

### networkQos

```c
NetworkBoost_NetworkQos NetworkBoost_NetworkQosArray::networkQos[NETBOOST_MAX_PATH_NUM]
```

**描述**

多条路径的网络质量信息，每一项为一条路径的网络质量信息，取值范围 [0, pathNum-1]。

### pathNum

```c
uint32_t NetworkBoost_NetworkQosArray::pathNum
```

**描述**

网络质量信息中的路径数量，取值范围 [1, 4]。
