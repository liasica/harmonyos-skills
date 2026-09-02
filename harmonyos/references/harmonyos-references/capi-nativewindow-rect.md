---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-nativewindow-rect
title: Rect
breadcrumb: API参考 > 图形 > ArkGraphics 2D（方舟2D图形服务） > C API > 结构体 > Rect
category: harmonyos-references
scraped_at: 2026-09-02T15:02:46+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:3826df69f2aeffa1bafc0949c06500c664339b76cfb050c5a7689ac248627cfd
---

```c
struct Rect { ... }
```

## 概述

如果rects是空指针nullptr，默认Buffer大小为脏区。

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
