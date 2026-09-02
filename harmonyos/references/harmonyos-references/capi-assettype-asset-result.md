---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-assettype-asset-result
title: Asset_Result
breadcrumb: API参考 > 系统 > 安全 > Asset Store Kit（关键资产存储服务） > C API > 结构体 > Asset_Result
category: harmonyos-references
scraped_at: 2026-09-02T15:01:40+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:0f1b3e443469320945058d6338370996eb8522d1ac00d414caa3743321264687
---

```c
typedef struct {...} Asset_Result
```

## 概述

单条关键资产的查询结果。

**起始版本：** 11

**相关模块：** [AssetType](capi-assettype.md)

**所在头文件：** [asset\_type.h](capi-asset-type-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| uint32\_t count | 关键资产属性的个数。 |
| [Asset\_Attr](capi-assettype-asset-attr.md) \*attrs | 指向关键资产属性数组的指针。 |
