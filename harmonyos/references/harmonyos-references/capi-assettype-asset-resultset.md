---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-assettype-asset-resultset
title: Asset_ResultSet
breadcrumb: API参考 > 系统 > 安全 > Asset Store Kit（关键资产存储服务） > C API > 结构体 > Asset_ResultSet
category: harmonyos-references
scraped_at: 2026-09-02T15:01:40+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:4d643a0092be7e0dd54c80fb28eda207305fdf057e1b39d859121aa8e57d10b5
---

```c
typedef struct {...} Asset_ResultSet
```

## 概述

多条关键资产的查询结果。

**起始版本：** 11

**相关模块：** [AssetType](capi-assettype.md)

**所在头文件：** [asset\_type.h](capi-asset-type-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| uint32\_t count | 关键资产的条数。 |
| [Asset\_Result](capi-assettype-asset-result.md) \*results | 指向关键资产数组的指针。 |
