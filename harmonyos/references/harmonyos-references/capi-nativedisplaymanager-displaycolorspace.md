---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-nativedisplaymanager-displaycolorspace
title: NativeDisplayManager_DisplayColorSpace
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 结构体 > NativeDisplayManager_DisplayColorSpace
category: harmonyos-references
scraped_at: 2026-09-02T15:01:24+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:51ffb69b6f0635d08d7d0f1d45cc1c3b6e42c6c83165a1e57f8cb86cd77845f8
---

```c
typedef struct {...} NativeDisplayManager_DisplayColorSpace
```

## 概述

显示设备支持的色域类型信息。

**起始版本：** 14

**相关模块：** [OH\_DisplayManager](capi-oh-displaymanager.md)

**所在头文件：** [oh\_display\_info.h](capi-oh-display-info-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| uint32\_t colorSpaceLength | 显示设备支持的色域类型数量。 |
| uint32\_t\* colorSpaces | 指向显示设备支持的色域类型数组的指针。 |
