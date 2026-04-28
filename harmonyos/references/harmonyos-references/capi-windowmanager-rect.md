---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-windowmanager-rect
title: WindowManager_Rect
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 结构体 > WindowManager_Rect
category: harmonyos-references
scraped_at: 2026-04-28T08:04:38+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:8a237224f442f5911386989acc4051f831c53d500dfecdccf7d77a61f47e3349
---

```
1. typedef struct {...} WindowManager_Rect
```

## 概述

PhonePC/2in1TabletTVWearable

定义窗口矩形结构体，包含窗口位置和宽高信息。

**起始版本：** 15

**相关模块：** [WindowManager](capi-windowmanager.md)

**所在头文件：** [oh\_window\_comm.h](capi-oh-window-comm-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| int32\_t posX | 窗口的x轴，单位为px，该参数为整数。 |
| int32\_t posY | 窗口的y轴，单位为px，该参数为整数。 |
| uint32\_t width | 窗口的宽度，单位为px，该参数为整数。 |
| uint32\_t height | 窗口的高度，单位为px，该参数为整数。 |
