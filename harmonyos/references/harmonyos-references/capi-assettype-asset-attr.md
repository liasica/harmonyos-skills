---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-assettype-asset-attr
title: Asset_Attr
breadcrumb: API参考 > 系统 > 安全 > Asset Store Kit（关键资产存储服务） > C API > 结构体 > Asset_Attr
category: harmonyos-references
scraped_at: 2026-04-28T08:06:48+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:e93fdc000aac003c35c26170c72a1b7fb0e733f7701ab130bfda1033a5bbddce
---

```
1. typedef struct {...} Asset_Attr
```

## 概述

PhonePC/2in1TabletTVWearable

关键资产属性。

**起始版本：** 11

**相关模块：** [AssetType](capi-assettype.md)

**所在头文件：** [asset\_type.h](capi-asset-type-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| uint32\_t tag | 关键资产属性名称。 |
| [Asset\_Value](capi-assettype-asset-value.md) value | 关键资产属性内容。 |
