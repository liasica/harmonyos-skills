---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-scan-scan-scannerdevice
title: Scan_ScannerDevice
breadcrumb: API参考 > 系统 > 基础功能 > Basic Services Kit（基础服务） > C API > 结构体 > Scan_ScannerDevice
category: harmonyos-references
scraped_at: 2026-04-28T08:09:55+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:ec9682caec249d93c2aae81932c398206799f095e93b623bb4db74f00adb5593
---

```
1. typedef struct {...} Scan_ScannerDevice
```

## 概述

PhonePC/2in1Tablet

表示扫描仪设备信息

**起始版本：** 12

**相关模块：** [OH\_Scan](capi-oh-scan.md)

**所在头文件：** [ohscan.h](capi-ohscan-h.md)

## 汇总

PhonePC/2in1Tablet

### 成员变量

PhonePC/2in1Tablet

| 名称 | 描述 |
| --- | --- |
| const char\* scannerId | 扫描仪ID |
| const char\* manufacturer | 扫描仪制造商 |
| const char\* model | 扫描仪型号 |
| const char\* discoverMode | 扫描仪发现模式 |
| const char\* serialNumber | 扫描仪序列号 |
