---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ffrt-ffrt-cond-t
title: ffrt_cond_t
breadcrumb: API参考 > 系统 > 基础功能 > Function Flow Runtime Kit > C API > 结构体 > ffrt_cond_t
category: harmonyos-references
scraped_at: 2026-04-28T08:10:10+08:00
doc_updated_at: 2026-03-12
content_hash: sha256:8a7412f0aa5c5b11954d4d8986d8b1cbea6a8d15cb754f970e699e4dd92b33ab
---

```
1. typedef struct {...} ffrt_cond_t
```

## 概述

PhonePC/2in1TabletTVWearable

FFRT条件变量结构。

**起始版本：** 10

**相关模块：** [FFRT](capi-ffrt.md)

**所在头文件：** [type\_def.h](capi-type-def-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| uint32\_t storage[(ffrt\_cond\_storage\_size + sizeof(uint32\_t) - 1) / sizeof(uint32\_t)] | FFRT条件变量占用空间 |
