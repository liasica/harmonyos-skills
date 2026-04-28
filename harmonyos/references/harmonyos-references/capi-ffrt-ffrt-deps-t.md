---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ffrt-ffrt-deps-t
title: ffrt_deps_t
breadcrumb: API参考 > 系统 > 基础功能 > Function Flow Runtime Kit > C API > 结构体 > ffrt_deps_t
category: harmonyos-references
scraped_at: 2026-04-28T08:10:08+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:e5397357a420189dc242f7efa37aab3bb167b9446c4ecd96d362752e6a72866e
---

```
1. typedef struct {...} ffrt_deps_t
```

## 概述

PhonePC/2in1TabletTVWearable

依赖结构定义。

**起始版本：** 10

**相关模块：** [FFRT](capi-ffrt.md)

**所在头文件：** [type\_def.h](capi-type-def-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| uint32\_t len | 依赖数量 |
| const [ffrt\_dependence\_t\*](capi-ffrt-ffrt-dependence-t.md) items | 依赖数据 |
