---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-assettype-asset-blob
title: Asset_Blob
breadcrumb: API参考 > 系统 > 安全 > Asset Store Kit（关键资产存储服务） > C API > 结构体 > Asset_Blob
category: harmonyos-references
scraped_at: 2026-04-28T08:06:47+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:86f144dbc95a76d42d62ca9219f3f51ff041b3856059106b4f1d06a11565c071
---

```
1. typedef struct {...} Asset_Blob
```

## 概述

PhonePC/2in1TabletTVWearable

二进制数组类型，即不定长的字节数组。

**起始版本：** 11

**相关模块：** [AssetType](capi-assettype.md)

**所在头文件：** [asset\_type.h](capi-asset-type-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| uint32\_t size | 表示字节数组的大小。 |
| uint8\_t \*data | 指向字节数组的指针。 |
