---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-clouddisk-oh-clouddisk-dehydrateinfo
title: OH_CloudDisk_DehydrateInfo
breadcrumb: API参考 > 应用框架 > Core File Kit（文件基础服务） > C API > 结构体 > OH_CloudDisk_DehydrateInfo
category: harmonyos-references
scraped_at: 2026-11-12T09:55:07+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:a387dad40d6efedd6483763f29d056284c407b02464647811bcd0c0acafe9ee2
---

```c
typedef struct OH_CloudDisk_DehydrateInfo {...} OH_CloudDisk_DehydrateInfo
```

## 概述

脱水授权信息。

**起始版本：** 26.0.1

**相关模块：** [CloudDisk](capi-clouddisk.md)

**所在头文件：** [oh\_cloud\_disk\_manager.h](capi-oh-cloud-disk-manager-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| [CloudDisk\_PathInfo](capi-clouddisk-clouddisk-pathinfo.md) filePath | 同步根内相对文件路径。  **起始版本：** 26.0.1 |
| bool allow | 是否允许脱水。true表示允许对该文件执行脱水；false表示不允许脱水，应用应跳过该文件的脱水操作。  **起始版本：** 26.0.1 |
