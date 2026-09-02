---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-windowmanager-rect
title: WindowManager_Rect
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 结构体 > WindowManager_Rect
category: harmonyos-references
scraped_at: 2026-09-02T15:01:24+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:4118d8f647b8b47ed0d5b2d1e5c880460db09ab10c3a1439e7bd2398212da772
---

```c
typedef struct {...} WindowManager_Rect
```

## 概述

定义窗口矩形结构体，包含窗口位置和宽高信息。

**起始版本：** 15

**相关模块：** [WindowManager](capi-windowmanager.md)

**所在头文件：** [oh\_window\_comm.h](capi-oh-window-comm-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| int32\_t posX | 窗口的x轴坐标，单位为px，该参数为整数。 |
| int32\_t posY | 窗口的y轴坐标，单位为px，该参数为整数。 |
| uint32\_t width | 窗口的宽度，单位为px，该参数为整数。 |
| uint32\_t height | 窗口的高度，单位为px，该参数为整数。 |
