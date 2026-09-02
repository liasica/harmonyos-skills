---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-assettype-asset-attr
title: Asset_Attr
breadcrumb: API参考 > 系统 > 安全 > Asset Store Kit（关键资产存储服务） > C API > 结构体 > Asset_Attr
category: harmonyos-references
scraped_at: 2026-09-02T15:01:40+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:96fd47ef64160b2eb5d41a92bf14c81ac439e74717a3d02daaa75c1e4cf882ff
---

```c
typedef struct {...} Asset_Attr
```

## 概述

关键资产属性，属性由标签和值组成，以键值对的形式存在。

**起始版本：** 11

**相关模块：** [AssetType](capi-assettype.md)

**所在头文件：** [asset\_type.h](capi-asset-type-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| uint32\_t tag | 关键资产属性的标签。 |
| [Asset\_Value](capi-assettype-asset-value.md) value | 关键资产属性的值（内容）。 |
