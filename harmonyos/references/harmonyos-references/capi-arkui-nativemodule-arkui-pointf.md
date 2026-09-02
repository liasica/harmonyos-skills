---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-pointf
title: ArkUI_PointF
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 结构体 > ArkUI_PointF
category: harmonyos-references
scraped_at: 2026-09-02T15:01:23+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:6da38f2db98289335aa231f8ffb9e88d1cfd189e7d43b7617fff490b5e0daf92
---

```c
typedef struct {...} ArkUI_PointF
```

## 概述

定义一个二维坐标点结构体，用于描述组件位置或偏移等坐标信息，坐标以浮点类型存储。

**起始版本：** 24

**相关模块：** [ArkUI\_NativeModule](capi-arkui-nativemodule.md)

**所在头文件：** [native\_type\_visual.h](capi-native-type-visual-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| float x | x轴坐标，单位为px。取值范围：(-∞, +∞)。 |
| float y | y轴坐标，单位为px。取值范围：(-∞, +∞)。 |
