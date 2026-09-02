---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-effectkit-oh-filter-colormatrix
title: OH_Filter_ColorMatrix
breadcrumb: API参考 > 图形 > ArkGraphics 2D（方舟2D图形服务） > C API > 结构体 > OH_Filter_ColorMatrix
category: harmonyos-references
scraped_at: 2026-09-02T15:02:46+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:782a65ae275442d396a418eda69da91b2363b1a2443ff8648ad774bddb32cf08
---

```c
struct OH_Filter_ColorMatrix {
    // ...
};
```

## 概述

定义一个用来创建滤镜效果的矩阵。

**起始版本：** 12

**相关模块：** [effectKit](capi-effectkit.md)

**所在头文件：** [effect\_types.h](capi-effect-types-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| float val[20] | 自定义颜色矩阵，值是一个5\*4的数组。 |
