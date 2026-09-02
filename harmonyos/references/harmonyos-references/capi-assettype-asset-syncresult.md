---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-assettype-asset-syncresult
title: Asset_SyncResult
breadcrumb: API参考 > 系统 > 安全 > Asset Store Kit（关键资产存储服务） > C API > 结构体 > Asset_SyncResult
category: harmonyos-references
scraped_at: 2026-09-02T15:01:40+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:b4657c66bf82a0e1fc45a8ac716e05a10de5e217b08ad2f77132a897af321647
---

```c
typedef struct {...} Asset_SyncResult
```

## 概述

关键资产同步结果。

**起始版本：** 20

**相关模块：** [AssetType](capi-assettype.md)

**所在头文件：** [asset\_type.h](capi-asset-type-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| int32\_t resultCode | 关键资产同步的结果码。同步成功时结果码为0，同步失败时结果码参考[Asset\_ResultCode](capi-asset-type-h.md#asset_resultcode)。 |
| uint32\_t totalCount | 触发同步的关键资产总数。 |
| uint32\_t failedCount | 关键资产同步失败的数量。 |
