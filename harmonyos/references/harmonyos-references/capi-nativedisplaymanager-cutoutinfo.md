---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-nativedisplaymanager-cutoutinfo
title: NativeDisplayManager_CutoutInfo
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 结构体 > NativeDisplayManager_CutoutInfo
category: harmonyos-references
scraped_at: 2026-09-02T15:01:24+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:1b8f6882343823bcebfa473ffa55b953e7049069a7b00253046f3b1b34318e37
---

```c
typedef struct {...} NativeDisplayManager_CutoutInfo
```

## 概述

挖孔屏、刘海屏、瀑布屏等不可用屏幕区域信息。

**起始版本：** 12

**相关模块：** [OH\_DisplayManager](capi-oh-displaymanager.md)

**所在头文件：** [oh\_display\_info.h](capi-oh-display-info-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| int32\_t boundingRectsLength | 挖孔屏、刘海屏等不可用屏幕区域的数量。 |
| [NativeDisplayManager\_Rect](capi-nativedisplaymanager-rect.md)\* boundingRects | 挖孔屏、刘海屏等不可用屏幕区域的边界矩形。 |
| [NativeDisplayManager\_WaterfallDisplayAreaRects](capi-nativedisplaymanager-waterfalldisplayarearects.md) waterfallDisplayAreaRects | 瀑布屏曲面部分显示区域。 |
