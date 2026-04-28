---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-print-print-stringlist
title: Print_StringList
breadcrumb: API参考 > 系统 > 基础功能 > Basic Services Kit（基础服务） > C API > 结构体 > Print_StringList
category: harmonyos-references
scraped_at: 2026-04-28T08:09:54+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:3f31147130672549922726316554ffa2e0c1d41f233f2a25f52a1b15935137d9
---

```
1. typedef struct {...} Print_StringList
```

## 概述

PhonePC/2in1Tablet

表示字符串列表。

**起始版本：** 12

**相关模块：** [OH\_Print](capi-oh-print.md)

**所在头文件：** [ohprint.h](capi-ohprint-h.md)

## 汇总

PhonePC/2in1Tablet

### 成员变量

PhonePC/2in1Tablet

| 名称 | 描述 |
| --- | --- |
| uint32\_t count | 字符串数量。 |
| char \*\*list | 字符串指针数组。 |
