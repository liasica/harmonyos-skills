---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-scan-scan-picturescanprogress
title: Scan_PictureScanProgress
breadcrumb: API参考 > 系统 > 基础功能 > Basic Services Kit（基础服务） > C API > 结构体 > Scan_PictureScanProgress
category: harmonyos-references
scraped_at: 2026-04-28T08:09:55+08:00
doc_updated_at: 2026-04-03
content_hash: sha256:59ea59a6e375b817a3da011b4a133c93399ad68afc4038aeb348a86a3c34dfb4
---

```
1. typedef struct {...} Scan_PictureScanProgress
```

## 概述

PhonePC/2in1Tablet

表示扫描仪扫描图片的进度

**起始版本：** 12

**相关模块：** [OH\_Scan](capi-oh-scan.md)

**所在头文件：** [ohscan.h](capi-ohscan-h.md)

## 汇总

PhonePC/2in1Tablet

### 成员变量

PhonePC/2in1Tablet

| 名称 | 描述 |
| --- | --- |
| int32\_t progress | 图片的扫描进度，从0到100，单位：百分比。 |
| int32\_t fd | 扫描仪文件句柄 |
| bool isFinal | 指示该图像是否为最后扫描的图像。true表示该图像是最后扫描的图像，false表示该图像不是最后扫描的图像。 |
