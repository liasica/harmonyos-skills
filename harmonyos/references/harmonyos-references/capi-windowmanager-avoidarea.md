---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-windowmanager-avoidarea
title: WindowManager_AvoidArea
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 结构体 > WindowManager_AvoidArea
category: harmonyos-references
scraped_at: 2026-09-02T15:01:24+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:ca4b7873c12e0536d0d7808de57e21763d1b739979f96ba9ac04a03d8b94c948
---

```c
typedef struct {...} WindowManager_AvoidArea
```

## 概述

定义避让区域结构体。

**起始版本：** 15

**相关模块：** [WindowManager](capi-windowmanager.md)

**所在头文件：** [oh\_window\_comm.h](capi-oh-window-comm-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| [WindowManager\_Rect](capi-windowmanager-rect.md) topRect | 避让区域的顶部矩形。 |
| [WindowManager\_Rect](capi-windowmanager-rect.md) leftRect | 避让区域的左侧矩形。 |
| [WindowManager\_Rect](capi-windowmanager-rect.md) rightRect | 避让区域的右侧矩形。 |
| [WindowManager\_Rect](capi-windowmanager-rect.md) bottomRect | 避让区域的底部矩形。 |
