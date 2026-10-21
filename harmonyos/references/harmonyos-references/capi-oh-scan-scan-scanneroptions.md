---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-scan-scan-scanneroptions
title: Scan_ScannerOptions
breadcrumb: API参考 > 系统 > 基础功能 > Basic Services Kit（基础服务） > C API > 结构体 > Scan_ScannerOptions
category: harmonyos-references
scraped_at: 2026-10-22T07:09:24+08:00
doc_updated_at: 2026-10-21
content_hash: sha256:628bb62edd12ff84e4e515966dec8555d6bf38ef3a53a4deb76e7934b5150df7
---

```cpp
typedef struct {...} Scan_ScannerOptions
```

## 概述

表示一个扫描仪的可设置参数选项，用于配置扫描仪的参数，支持配置选项标题、描述、可设置范围及选项数量。每个选项由一组标题（titles）、描述（descriptions）和可设置范围（ranges）组成，三者以平行数组的形式存储，optionCount表示选项的总数量，开发者可通过索引i（需满足0 ≤ i < optionCount）同时访问titles[i]、descriptions[i] 和ranges[i] 来获取第i个选项的完整信息。需保证titles、descriptions、ranges三者的数组长度一致且等于optionCount，否则可能无法正确获取选项的完整信息。

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
