---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/fast-kit--fast-rect
title: FAST_Rect
breadcrumb: API参考 > 系统 > 基础功能 > FAST Kit（算法加速服务） > C API > 头文件和结构体 > 结构体 > FAST_Rect
category: harmonyos-references
scraped_at: 2026-04-28T08:10:04+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:56bc6c93952581491498b0516d0cba7aa86350f7feed197acb1eb3122a64f728
---

## 概述

PhonePC/2in1Tablet

定义矩形的数据结构（坐标系说明：X轴从左到右递增，Y轴从上到下递增）。

**系统能力：** SystemCapability.FAST.Core

**起始版本：** 6.0.2(22)

**相关模块：** [FAST](fast-kit-fast.md)

**所在头文件：** [fast\_solver\_rect\_partition.h](fast-kit-fast-solver-rect-partition-8h.md)

## 汇总

PhonePC/2in1Tablet

### 成员变量

PhonePC/2in1Tablet

| 名称 | 描述 |
| --- | --- |
| int32\_t [left](fast-kit--fast-rect.md#left) | 横坐标左边界（）。 |
| int32\_t [top](fast-kit--fast-rect.md#top) | 纵坐标上边界（）。 |
| int32\_t [right](fast-kit--fast-rect.md#right) | 横坐标右边界（）。 |
| int32\_t [bottom](fast-kit--fast-rect.md#bottom) | 纵坐标下边界（）。 |

## 结构体成员变量说明

PhonePC/2in1Tablet

### bottom

PhonePC/2in1Tablet

```
1. int32_t FAST_Rect::bottom
```

**描述**

纵坐标下边界。

### left

PhonePC/2in1Tablet

```
1. int32_t FAST_Rect::left
```

**描述**

横坐标左边界。

### right

PhonePC/2in1Tablet

```
1. int32_t FAST_Rect::right
```

**描述**

横坐标右边界。

### top

PhonePC/2in1Tablet

```
1. int32_t FAST_Rect::top
```

**描述**

纵坐标上边界。
