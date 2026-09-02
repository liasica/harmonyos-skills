---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/network-boost-c-struct-net_handle
title: NetworkBoost_NetHandle
breadcrumb: API参考 > 系统 > 网络 > Network Boost Kit（网络加速服务） > C API > 结构体 > NetworkBoost_NetHandle
category: harmonyos-references
scraped_at: 2026-09-02T15:01:57+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:5979b3a8ea8c9f11a9f93161962945bd96aa520e736f908ebdf8ad60f53800f7
---

## 概述

NetHandle信息。

**起始版本：** 5.1.0(18)

**相关模块：** [NetworkBoost](network-boost-c-overview.md)

**所在头文件：** [network\_boost\_handover.h](network-boost-c-files-handover.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| int32\_t [netId](network-boost-c-struct-net_handle.md#netid) | 网络ID，为网络唯一标识，该参数通常由系统自动分配。 |

## 结构体成员变量说明

### netId

```c
int32_t NetworkBoost_NetHandle::netId
```

**描述**

网络ID。
