---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-nativedisplaymanager-rect
title: NativeDisplayManager_Rect
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 结构体 > NativeDisplayManager_Rect
category: harmonyos-references
scraped_at: 2026-09-02T15:01:24+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:2152c751025bc565427fdef90df717f862bbb34e51f61bf281270679cf4b1642
---

```c
typedef struct {...} NativeDisplayManager_Rect
```

## 概述

矩形区域。

**起始版本：** 12

**相关模块：** [OH\_DisplayManager](capi-oh-displaymanager.md)

**所在头文件：** [oh\_display\_info.h](capi-oh-display-info-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| int32\_t left | 矩形区域的左边界，单位为px。 |
| int32\_t top | 矩形区域的上边界，单位为px。 |
| uint32\_t width | 矩形区域的宽度，单位为px。 |
| uint32\_t height | 矩形区域的高度，单位为px。 |
