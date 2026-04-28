---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/network-boost-c-struct-multipath_quota
title: NetworkBoost_MultiPathQuota
breadcrumb: API参考 > 系统 > 网络 > Network Boost Kit（网络加速服务） > C API > 结构体 > NetworkBoost_MultiPathQuota
category: harmonyos-references
scraped_at: 2026-04-28T08:08:53+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:045c4e5c7c586ccaa9cc243ec4e834c07d02222cb957241ea581ca47264ece2d
---

## 概述

PhonePC/2in1Tablet

应用配额信息，包含应用已使用配额信息和剩余配额信息。

**起始版本：** 6.0.2(22)

**相关模块：** [NetworkBoost](network-boost-c-overview.md)

**所在头文件：** [network\_boost\_handover.h](network-boost-c-files-handover.md)

## 汇总

PhonePC/2in1Tablet

### 成员变量

PhonePC/2in1Tablet

| 名称 | 描述 |
| --- | --- |
| [NetworkBoost\_MultiPathQuotaInfo](network-boost-c-struct-multipath_quotainfo.md) [used](network-boost-c-struct-multipath_quota.md#used) | 应用已使用配额信息。 |
| [NetworkBoost\_MultiPathQuotaInfo](network-boost-c-struct-multipath_quotainfo.md) [remaining](network-boost-c-struct-multipath_quota.md#remaining) | 应用剩余使用配额信息。 |

## 结构体成员变量说明

PhonePC/2in1Tablet

## used

PhonePC/2in1Tablet

```
1. NetworkBoost_MultiPathQuotaInfo NetworkBoost_MultiPathQuota::used
```

**描述**

表明应用已使用配额信息。

## remaining

PhonePC/2in1Tablet

```
1. NetworkBoost_MultiPathQuotaInfo NetworkBoost_MultiPathQuota::remaining
```

**描述**

应用剩余使用配额信息。
