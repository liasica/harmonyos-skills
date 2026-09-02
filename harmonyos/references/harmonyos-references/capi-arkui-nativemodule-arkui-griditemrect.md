---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-griditemrect
title: ArkUI_GridItemRect
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 结构体 > ArkUI_GridItemRect
category: harmonyos-references
scraped_at: 2026-09-02T15:01:25+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:0ca34f73b20ff11813348bbd3e7c66f353edc61057faed3053f51d01d02c4b2f
---

```c
typedef struct {...} ArkUI_GridItemRect
```

## 概述

定义Grid布局选项[OH\_ArkUI\_GridLayoutOptions\_RegisterGetRectByIndexCallback](capi-grid-h.md#oh_arkui_gridlayoutoptions_registergetrectbyindexcallback)回调返回值结构体，用于通过GridItem索引指定该GridItem在Grid中的起始行列位置和占用的行列数。

**起始版本：** 22

**相关模块：** [ArkUI\_NativeModule](capi-arkui-nativemodule.md)

**所在头文件：** [grid.h](capi-grid-h.md)

**相关示例：** [native\_type\_sample](https://gitcode.com/HarmonyOS_Samples/guide-snippets/tree/master/ArkUISample/NativeTypeSample)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| uint32\_t rowStart | GridItem行起始位置，从0开始计数，用于确定GridItem在Grid中的起始行。 |
| uint32\_t columnStart | GridItem列起始位置，从0开始计数，用于确定GridItem在Grid中的起始列。 |
| uint32\_t rowSpan | GridItem占用的行数，用于设置GridItem在行方向上的跨度。 |
| uint32\_t columnSpan | GridItem占用的列数，用于设置GridItem在列方向上的跨度。 |
