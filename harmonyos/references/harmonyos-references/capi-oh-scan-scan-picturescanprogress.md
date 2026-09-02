---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-scan-scan-picturescanprogress
title: Scan_PictureScanProgress
breadcrumb: API参考 > 系统 > 基础功能 > Basic Services Kit（基础服务） > C API > 结构体 > Scan_PictureScanProgress
category: harmonyos-references
scraped_at: 2026-09-02T15:02:05+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:36a372ed41077bdd7c1bebff4b3e3de961cb1a6df6452f6bc8c4c825cd06a1a0
---

```cpp
typedef struct {...} Scan_PictureScanProgress
```

## 概述

表示扫描仪扫描图片的进度。该结构体包含进度值（progress）、文件描述符（fd）及是否为最后扫描的图片（isFinal），适用于需要在应用中实时跟踪图片扫描状态、获取扫描结果文件的场景。详细实现机制请参见 [OH\_Scan](capi-oh-scan.md)。

**起始版本：** 12

**相关模块：** [OH\_Scan](capi-oh-scan.md)

**所在头文件：** [ohscan.h](capi-ohscan-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| int32\_t progress | 图片的扫描进度，取值范围[0, 100]，单位：百分比。0 表示扫描刚开始，100 表示扫描完成。 |
| int32\_t fd | 扫描仪扫描图片的文件描述符，用于读取扫描仪传输的图片数据。仅当 progress 为 100 时，该 fd 为有效文件描述符。 |
| bool isFinal | 指示该图片是否为最后扫描的图片。true 表示是最后扫描的图片，false 表示不是最后扫描的图片。 |
