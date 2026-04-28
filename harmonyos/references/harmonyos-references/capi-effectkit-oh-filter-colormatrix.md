---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-effectkit-oh-filter-colormatrix
title: OH_Filter_ColorMatrix
breadcrumb: API参考 > 图形 > ArkGraphics 2D（方舟2D图形服务） > C API > 结构体 > OH_Filter_ColorMatrix
category: harmonyos-references
scraped_at: 2026-04-28T08:15:15+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:c59a800cef196bedb4f07b516fc382d80fb64eafc19b519de151193c360853f1
---

```
1. struct OH_Filter_ColorMatrix {...}
```

## 概述

PhonePC/2in1TabletTVWearable

定义一个用来创建滤镜效果的矩阵。

**起始版本：** 12

**相关模块：** [effectKit](capi-effectkit.md)

**所在头文件：** [effect\_types.h](capi-effect-types-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| float val[20] | 自定义颜色矩阵，值是一个5\*4的数组。 |
