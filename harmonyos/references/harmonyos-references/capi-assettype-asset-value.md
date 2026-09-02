---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-assettype-asset-value
title: Asset_Value
breadcrumb: API参考 > 系统 > 安全 > Asset Store Kit（关键资产存储服务） > C API > 结构体 > Asset_Value
category: harmonyos-references
scraped_at: 2026-09-02T15:01:40+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:396f2a809720c391539b39529cd078b8f9cdee7899ee51899615cab5f3989253
---

```c
typedef union {...} Asset_Value
```

## 概述

关键资产属性的值（内容）。

**起始版本：** 11

**相关模块：** [AssetType](capi-assettype.md)

**所在头文件：** [asset\_type.h](capi-asset-type-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| bool boolean | 该字段用于传入bool类型的属性值。 |
| uint32\_t u32 | 该字段用于传入uint32类型的属性值。 |
| [Asset\_Blob](capi-assettype-asset-blob.md) blob | 该字段用于传入bytes类型的属性值。 |
