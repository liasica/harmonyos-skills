---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-nativedisplaymanager-cutoutinfo
title: NativeDisplayManager_CutoutInfo
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 结构体 > NativeDisplayManager_CutoutInfo
category: harmonyos-references
scraped_at: 2026-04-28T08:04:39+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:ee163380faf3b4d915e59254b3bda0e20ad78a15367b419618d4e6b9cd46e0e7
---

```
1. typedef struct {...} NativeDisplayManager_CutoutInfo
```

## 概述

PhonePC/2in1TabletTVWearable

挖孔屏、刘海屏、瀑布屏等不可用屏幕区域信息。

**起始版本：** 12

**相关模块：** [OH\_DisplayManager](capi-oh-displaymanager.md)

**所在头文件：** [oh\_display\_info.h](capi-oh-display-info-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| int32\_t boundingRectsLength | 挖孔屏、刘海屏不可用屏幕区域长度。 |
| [NativeDisplayManager\_Rect](capi-nativedisplaymanager-rect.md)\* boundingRects | 挖孔屏、刘海屏等区域的边界矩形。 |
| [NativeDisplayManager\_WaterfallDisplayAreaRects](api-nativedisplaymanager-waterfalldisplayarearects.md) waterfallDisplayAreaRects | 瀑布屏曲面部分显示区域。 |
