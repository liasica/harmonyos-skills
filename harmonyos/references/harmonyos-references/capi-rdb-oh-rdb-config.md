---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-rdb-oh-rdb-config
title: OH_Rdb_Config
breadcrumb: API参考 > 应用框架 > ArkData（方舟数据管理） > C API > 结构体 > OH_Rdb_Config
category: harmonyos-references
scraped_at: 2026-04-28T07:59:36+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:68ec348d2f3759ac0dbef684ce2dafb35b02a0df1fec4d5600470a0925c09763
---

```
1. typedef struct  {...} OH_Rdb_Config
```

## 概述

PhonePC/2in1TabletTVWearable

管理关系数据库配置。

**起始版本：** 10

**相关模块：** [RDB](capi-rdb.md)

**所在头文件：** [relational\_store.h](capi-relational-store-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| int selfSize | 该结构体的大小。 |
| const char\* dataBaseDir | 数据库文件路径。 |
| const char\* storeName | 数据库名称。 |
| const char\* bundleName | 应用包名。 |
| const char\* moduleName | 应用模块名。 |
| bool isEncrypt | 指定数据库是否加密。true表示加密，false表示不加密。 |
| int securityLevel | 设置数据库安全级别[OH\_Rdb\_SecurityLevel](capi-relational-store-h.md#oh_rdb_securitylevel)。 |
| int area | 设置数据库安全区域等级[Rdb\_SecurityArea](capi-relational-store-h.md#rdb_securityarea)  **起始版本：** 11 |
