---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-assettype-asset-value
title: Asset_Value
breadcrumb: API参考 > 系统 > 安全 > Asset Store Kit（关键资产存储服务） > C API > 结构体 > Asset_Value
category: harmonyos-references
scraped_at: 2026-04-28T08:06:47+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:26af02a6b9a535d6ef289df017665b7142bb427c56379d6d88d39762d398c656
---

```
1. typedef union {...} Asset_Value
```

## 概述

PhonePC/2in1TabletTVWearable

关键资产属性内容。

**起始版本：** 11

**相关模块：** [AssetType](capi-assettype.md)

**所在头文件：** [asset\_type.h](capi-asset-type-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| bool boolean | 该字段用于传入bool类型的关键资产。 |
| uint32\_t u32 | 该字段用于传入uint32类型的关键资产。 |
| [Asset\_Blob](capi-assettype-asset-blob.md) blob | 该字段用于传入bytes类型的关键资产。 |
