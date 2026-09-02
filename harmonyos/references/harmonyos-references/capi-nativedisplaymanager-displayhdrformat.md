---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-nativedisplaymanager-displayhdrformat
title: NativeDisplayManager_DisplayHdrFormat
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 结构体 > NativeDisplayManager_DisplayHdrFormat
category: harmonyos-references
scraped_at: 2026-09-02T15:01:24+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:75ef87d0cf54db841c982b3e18d955428d86508aa5838e884a5d064130e5a2ee
---

```c
typedef struct {...} NativeDisplayManager_DisplayHdrFormat
```

## 概述

显示设备支持的所有HDR格式。

**起始版本：** 14

**相关模块：** [OH\_DisplayManager](capi-oh-displaymanager.md)

**所在头文件：** [oh\_display\_info.h](capi-oh-display-info-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| uint32\_t hdrFormatLength | 显示设备支持的HDR格式数量。 |
| uint32\_t\* hdrFormats | 指向显示设备支持的HDR格式数组的指针。 |
