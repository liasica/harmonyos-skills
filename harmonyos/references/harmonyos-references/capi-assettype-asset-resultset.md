---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-assettype-asset-resultset
title: Asset_ResultSet
breadcrumb: API参考 > 系统 > 安全 > Asset Store Kit（关键资产存储服务） > C API > 结构体 > Asset_ResultSet
category: harmonyos-references
scraped_at: 2026-04-28T08:06:48+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:8f5564d748fd1bd76739372c64c477c39dd63fc7cd0524098f782fcb5c59a26d
---

```
1. typedef struct {...} Asset_ResultSet
```

## 概述

PhonePC/2in1TabletTVWearable

关键资产查询结果集合，用于定义多条关键资产。

**起始版本：** 11

**相关模块：** [AssetType](capi-assettype.md)

**所在头文件：** [asset\_type.h](capi-asset-type-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| uint32\_t count | 关键资产的条数。 |
| [Asset\_Result](capi-assettype-asset-result.md) \*results | 指向关键资产数组的指针。 |
