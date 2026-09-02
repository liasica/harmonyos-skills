---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-nativewindow-region
title: Region
breadcrumb: API参考 > 图形 > ArkGraphics 2D（方舟2D图形服务） > C API > 结构体 > Region
category: harmonyos-references
scraped_at: 2026-09-02T15:02:47+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:9cfc1e90233a47a1b2fca7fc823d97e3ae0f18db70c3d01afbdaf88c18c8e2f9
---

```c
typedef struct Region {...} Region
```

## 概述

表示本地窗口OHNativeWindow需要更新内容的矩形区域（脏区）。

**起始版本：** 8

**相关模块：** [NativeWindow](capi-nativewindow.md)

**所在头文件：** [external\_window.h](capi-external-window-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| [Rect](capi-nativewindow-rect.md)\* rects | 如果rects是空指针nullptr，默认Buffer大小为脏区。 |
| int32\_t rectNumber | 如果rectNumber为0，默认Buffer大小为脏区。 |
