---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-assettype-asset-syncresult
title: Asset_SyncResult
breadcrumb: API参考 > 系统 > 安全 > Asset Store Kit（关键资产存储服务） > C API > 结构体 > Asset_SyncResult
category: harmonyos-references
scraped_at: 2026-04-28T08:06:48+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:3febc0213d2620611ec6e51ec396c76a01e1b3b8d031f46b28a966f0c0091720
---

```
1. typedef struct {...} Asset_SyncResult
```

## 概述

PhonePC/2in1TabletTVWearable

关键资产同步结果。

**起始版本：** 20

**相关模块：** [AssetType](capi-assettype.md)

**所在头文件：** [asset\_type.h](capi-asset-type-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| int32\_t resultCode | 关键资产同步的结果码。 |
| uint32\_t totalCount | 触发同步的关键资产总数。 |
| uint32\_t failedCount | 关键资产同步失败的数量。 |
