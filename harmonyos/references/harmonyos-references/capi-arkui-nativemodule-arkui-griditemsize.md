---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-griditemsize
title: ArkUI_GridItemSize
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 结构体 > ArkUI_GridItemSize
category: harmonyos-references
scraped_at: 2026-09-02T15:01:25+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:068fbed98c7062da5e5c154679b056f2b505bd816dde9df0d905572a13143e3a
---

```c
typedef struct {...} ArkUI_GridItemSize
```

## 概述

定义Grid布局选项[OH\_ArkUI\_GridLayoutOptions\_RegisterGetIrregularSizeByIndexCallback](capi-grid-h.md#oh_arkui_gridlayoutoptions_registergetirregularsizebyindexcallback)回调返回值结构体，用于通过GridItem索引指定不规则GridItem占用的行数和列数。

**起始版本：** 22

**相关模块：** [ArkUI\_NativeModule](capi-arkui-nativemodule.md)

**所在头文件：** [grid.h](capi-grid-h.md)

**相关示例：** [native\_type\_sample](https://gitcode.com/HarmonyOS_Samples/guide-snippets/tree/master/ArkUISample/NativeTypeSample)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| uint32\_t rowSpan | GridItem占用的行数，用于设置GridItem在行方向上的跨度。取值范围：[1, +∞)，设置为0时按1处理；Grid横向布局时，超过Grid实际行数的值按实际行数处理。 |
| uint32\_t columnSpan | GridItem占用的列数，用于设置GridItem在列方向上的跨度。取值范围：[1, +∞)，设置为0时按1处理；Grid纵向布局时，超过Grid实际列数的值按实际列数处理。 |
