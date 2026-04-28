---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-scan-scan-scanneroptions
title: Scan_ScannerOptions
breadcrumb: API参考 > 系统 > 基础功能 > Basic Services Kit（基础服务） > C API > 结构体 > Scan_ScannerOptions
category: harmonyos-references
scraped_at: 2026-04-28T08:09:56+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:4dfde99822975149d904a3c7a77811fa0f0267f84264fe9230ae801a44694133
---

```
1. typedef struct {...} Scan_ScannerOptions
```

## 概述

PhonePC/2in1Tablet

表示一个扫描仪的所有参数选项

**起始版本：** 12

**相关模块：** [OH\_Scan](capi-oh-scan.md)

**所在头文件：** [ohscan.h](capi-ohscan-h.md)

## 汇总

PhonePC/2in1Tablet

### 成员变量

PhonePC/2in1Tablet

| 名称 | 描述 |
| --- | --- |
| char\*\* titles | 选项标题 |
| char\*\* descriptions | 选项描述 |
| char\*\* ranges | 选项可设置的范围 |
| int32\_t optionCount | 可设置的参数选项数量 |
