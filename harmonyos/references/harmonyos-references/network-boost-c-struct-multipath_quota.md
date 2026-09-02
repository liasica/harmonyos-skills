---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/network-boost-c-struct-multipath_quota
title: NetworkBoost_MultiPathQuota
breadcrumb: API参考 > 系统 > 网络 > Network Boost Kit（网络加速服务） > C API > 结构体 > NetworkBoost_MultiPathQuota
category: harmonyos-references
scraped_at: 2026-09-02T15:01:57+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:2127568dd546a90e18a1d98e4811e52bac967d7763ebdee41f6934e845e25f00
---

## 概述

应用配额信息，包含应用已使用配额信息和剩余配额信息。

**起始版本：** 6.0.2(22)

**相关模块：** [NetworkBoost](network-boost-c-overview.md)

**所在头文件：** [network\_boost\_handover.h](network-boost-c-files-handover.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| [NetworkBoost\_MultiPathQuotaInfo](network-boost-c-struct-multipath_quotainfo.md) [used](network-boost-c-struct-multipath_quota.md#used) | 应用已使用配额信息。 |
| [NetworkBoost\_MultiPathQuotaInfo](network-boost-c-struct-multipath_quotainfo.md) [remaining](network-boost-c-struct-multipath_quota.md#remaining) | 应用剩余使用配额信息。 |

## 结构体成员变量说明

## used

```c
NetworkBoost_MultiPathQuotaInfo NetworkBoost_MultiPathQuota::used
```

**描述**

表明应用已使用配额信息。

## remaining

```c
NetworkBoost_MultiPathQuotaInfo NetworkBoost_MultiPathQuota::remaining
```

**描述**

应用剩余使用配额信息。
