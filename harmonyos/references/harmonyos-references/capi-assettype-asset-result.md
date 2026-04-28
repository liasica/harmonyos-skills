---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-assettype-asset-result
title: Asset_Result
breadcrumb: API参考 > 系统 > 安全 > Asset Store Kit（关键资产存储服务） > C API > 结构体 > Asset_Result
category: harmonyos-references
scraped_at: 2026-04-28T08:06:48+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:15b442e7d641ac9fcf4914726ba64c3473001867f2f4f3eb91add063090ba83a
---

```
1. typedef struct {...} Asset_Result
```

## 概述

PhonePC/2in1TabletTVWearable

关键资产查询结果，用于定义一条关键资产。

**起始版本：** 11

**相关模块：** [AssetType](capi-assettype.md)

**所在头文件：** [asset\_type.h](capi-asset-type-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| uint32\_t count | 关键资产属性的个数。 |
| [Asset\_Attr](capi-assettype-asset-attr.md) \*attrs | 指向关键资产属性数组的指针。 |
