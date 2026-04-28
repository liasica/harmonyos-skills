---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ffrt-ffrt-mutex-t
title: ffrt_mutex_t
breadcrumb: API参考 > 系统 > 基础功能 > Function Flow Runtime Kit > C API > 结构体 > ffrt_mutex_t
category: harmonyos-references
scraped_at: 2026-04-28T08:10:09+08:00
doc_updated_at: 2026-03-12
content_hash: sha256:5f4e587b6ce90a404da52d4e97d0173e420a004693ecfabe0ac3f36e1b447679
---

```
1. typedef struct {...} ffrt_mutex_t
```

## 概述

PhonePC/2in1TabletTVWearable

FFRT互斥锁结构。

**起始版本：** 10

**相关模块：** [FFRT](capi-ffrt.md)

**所在头文件：** [type\_def.h](capi-type-def-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| uint32\_t storage[(ffrt\_mutex\_storage\_size + sizeof(uint32\_t) - 1) / sizeof(uint32\_t)] | FFRT互斥锁占用空间 |
