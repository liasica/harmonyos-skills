---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-scan-scan-scanneroptions
title: Scan_ScannerOptions
breadcrumb: API参考 > 系统 > 基础功能 > Basic Services Kit（基础服务） > C API > 结构体 > Scan_ScannerOptions
category: harmonyos-references
scraped_at: 2026-09-02T15:02:05+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:4b0cb21f5ada0f21df3e13cc04b197df0242b087a82b54110c45f5a9768422cf
---

```cpp
typedef struct {...} Scan_ScannerOptions
```

## 概述

表示一个扫描仪的可设置参数选项，用于配置扫描仪的参数，支持配置选项标题、描述、可设置范围及选项数量。每个选项由一组标题（titles）、描述（descriptions）和可设置范围（ranges）组成，三者以平行数组的形式存储，optionCount 表示选项的总数量，开发者可通过索引 i（需满足 0 ≤ i < optionCount）同时访问 titles[i]、descriptions[i] 和 ranges[i] 来获取第 i 个选项的完整信息。需保证 titles、descriptions、ranges 三者的数组长度一致且等于 optionCount，否则可能无法正确获取选项的完整信息。

**起始版本：** 12

**相关模块：** [OH\_Scan](capi-oh-scan.md)

**所在头文件：** [ohscan.h](capi-ohscan-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| char\*\* titles | 选项标题 |
| char\*\* descriptions | 选项描述 |
| char\*\* ranges | 选项可设置的范围 |
| int32\_t optionCount | 选项数量 |
