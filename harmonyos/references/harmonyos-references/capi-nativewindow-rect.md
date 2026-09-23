---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-nativewindow-rect
title: Rect
breadcrumb: API参考 > 图形 > ArkGraphics 2D（方舟2D图形服务） > C API > 结构体 > Rect
category: harmonyos-references
scraped_at: 2026-09-24T06:55:06+08:00
doc_updated_at: 2026-09-23
content_hash: sha256:e298aa3fbc7b8146bf06207dc4d0967e843b8a17011011f75a0131e18e8011d1
---

```c
struct Rect { ... }
```

## 概述

定义矩形区域的结构体，包含矩形框的起始坐标和宽高信息。

**相关模块：** [NativeWindow](capi-nativewindow.md)

**所在头文件：** [external\_window.h](capi-external-window-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| int32\_t x | 矩形框起始x坐标。 |
| int32\_t y | 矩形框起始y坐标。 |
| uint32\_t w | 矩形框宽度。 |
| uint32\_t h | 矩形框高度。 |
