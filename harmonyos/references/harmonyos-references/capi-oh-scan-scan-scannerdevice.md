---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-scan-scan-scannerdevice
title: Scan_ScannerDevice
breadcrumb: API参考 > 系统 > 基础功能 > Basic Services Kit（基础服务） > C API > 结构体 > Scan_ScannerDevice
category: harmonyos-references
scraped_at: 2026-09-02T15:02:05+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:dbe4ce5c6f6c4a33d57f1690abfb2d8ce9dfa9f9ff56d5a1cc9ea54380910ee6
---

```cpp
typedef struct {...} Scan_ScannerDevice
```

## 概述

Scan\_ScannerDevice表示扫描仪设备信息，包含扫描仪 ID、制造商、型号、发现模式和序列号等属性，用于在扫描仪发现流程中获取设备详情，开发者可通过扫描仪发现相关接口获取该结构体以选择目标扫描仪设备进行扫描操作。相关模块设计逻辑请参见[OH\_Scan](capi-oh-scan.md)。

**起始版本：** 12

**相关模块：** [OH\_Scan](capi-oh-scan.md)

**所在头文件：** [ohscan.h](capi-ohscan-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| const char\* scannerId | 扫描仪 ID。 |
| const char\* manufacturer | 扫描仪制造商。 |
| const char\* model | 扫描仪型号。 |
| const char\* discoverMode | 扫描仪发现模式，表示扫描仪设备被系统发现的方式。值为"TCP"时，表示扫描仪通过网络发现；值为"USB"时，表示扫描仪通过 USB 连接发现。 |
| const char\* serialNumber | 扫描仪序列号。 |
