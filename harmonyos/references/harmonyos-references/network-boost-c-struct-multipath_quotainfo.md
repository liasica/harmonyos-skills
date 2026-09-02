---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/network-boost-c-struct-multipath_quotainfo
title: NetworkBoost_MultiPathQuotaInfo
breadcrumb: API参考 > 系统 > 网络 > Network Boost Kit（网络加速服务） > C API > 结构体 > NetworkBoost_MultiPathQuotaInfo
category: harmonyos-references
scraped_at: 2026-09-02T15:01:57+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:5e801a78088726fdb350462c3a76e94dbda0c679c294d316812b77a7d99050e8
---

## 概述

多网配额信息，包含配额次数信息和时长信息。

**起始版本：** 6.0.2(22)

**相关模块：** [NetworkBoost](network-boost-c-overview.md)

**所在头文件：** [network\_boost\_handover.h](network-boost-c-files-handover.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| uint16\_t [count](network-boost-c-struct-multipath_quotainfo.md#count) | 配额次数信息。 |
| uint16\_t [duration](network-boost-c-struct-multipath_quotainfo.md#duration) | 配额时长信息，单位为s。 |

## 结构体成员变量说明

## count

```c
uint16_t NetworkBoost_MultiPathQuotaInfo::count
```

**描述**

配额次数信息。

## duration

```c
uint16_t NetworkBoost_MultiPathQuotaInfo::duration
```

**描述**

配额时长信息，单位为s。
