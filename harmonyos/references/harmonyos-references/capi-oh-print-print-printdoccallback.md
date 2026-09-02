---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-print-print-printdoccallback
title: Print_PrintDocCallback
breadcrumb: API参考 > 系统 > 基础功能 > Basic Services Kit（基础服务） > C API > 结构体 > Print_PrintDocCallback
category: harmonyos-references
scraped_at: 2026-09-02T15:02:05+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:9ad5c6878180f7c95be075daa82ad73c90dca234b8c2f367e0b45cb66e4326ee
---

```cpp
typedef struct {...} Print_PrintDocCallback
```

## 概述

表示打印文档回调结构体。用于 C/C++ 原生应用向打印框架提供文件生成和任务状态接收能力。

**起始版本：** 13

**相关模块：** [OH\_Print](capi-oh-print.md)

**所在头文件：** [ohprint.h](capi-ohprint-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| [Print\_OnStartLayoutWrite](capi-ohprint-h.md#print_onstartlayoutwrite) startLayoutWriteCb | 打印开始布局写入回调。当打印任务开始布局时，系统将调用此回调函数，要求应用写入打印文件内容。 |
| [Print\_OnJobStateChanged](capi-ohprint-h.md#print_onjobstatechanged) jobStateChangedCb | 打印任务状态变化回调。当打印任务状态发生变化时，系统将调用此回调函数通知应用打印任务状态变更。 |
