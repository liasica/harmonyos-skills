---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-rdb-oh-rdb-config
title: OH_Rdb_Config
breadcrumb: API参考 > 应用框架 > ArkData（方舟数据管理） > C API > 结构体 > OH_Rdb_Config
category: harmonyos-references
scraped_at: 2026-09-02T15:00:43+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:dea391704e3dd660de2c4273e7c3de9f30fb31e29e4dda6f45a52010f14a8cee
---

```c
typedef struct  {...} OH_Rdb_Config
```

## 概述

管理关系数据库配置。

**起始版本：** 10

**相关模块：** [RDB](capi-rdb.md)

**所在头文件：** [relational\_store.h](capi-relational-store-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| int selfSize | 该结构体的大小。 |
| const char\* dataBaseDir | 数据库文件所在目录。完整路径由dataBaseDir与storeName组合而成，完整路径总长度不超过1024个字符。不能为空。 |
| const char\* storeName | 数据库名称，不能为空且不能包含路径分隔符/。 |
| const char\* bundleName | 应用包名，不能为空。 |
| const char\* moduleName | 应用模块名，不能为空。 |
| bool isEncrypt | 指定数据库是否加密。true表示加密，false表示不加密。 |
| int securityLevel | 数据库安全级别[OH\_Rdb\_SecurityLevel](capi-relational-store-h.md#oh_rdb_securitylevel)。 |
| int area | 数据库安全区域等级[Rdb\_SecurityArea](capi-relational-store-h.md#rdb_securityarea)  **起始版本：** 11 |
