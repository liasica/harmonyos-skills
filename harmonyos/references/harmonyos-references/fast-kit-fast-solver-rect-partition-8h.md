---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/fast-kit-fast-solver-rect-partition-8h
title: fast_solver_rect_partition.h
breadcrumb: API参考 > 系统 > 基础功能 > FAST Kit（算法加速服务） > C API > 头文件和结构体 > 头文件 > fast_solver_rect_partition.h
category: harmonyos-references
scraped_at: 2026-04-29T14:00:45+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:81a3029a090f9a74fd98f02f31400f7ee1a25eaa3a825ddeb9514e1c79dd77e1
---

## 概述

PhonePC/2in1Tablet

矩形划分求解器相关数据结构及函数定义。

**引用文件：** <FASTKit/fast\_solver\_rect\_partition.h>

**库：** libfast\_solver.so

**系统能力：** SystemCapability.FAST.Core

**起始版本：** 6.0.2(22)

**相关模块：** [FAST](fast-kit-fast.md)

## 汇总

PhonePC/2in1Tablet

### 结构体

PhonePC/2in1Tablet

| 名称 | 描述 |
| --- | --- |
| struct [FAST\_Rect](fast-kit--fast-rect.md) | 定义矩形的数据结构（坐标系说明：X轴从左到右递增，Y轴从上到下递增）。 |

### 类型定义

PhonePC/2in1Tablet

| 名称 | 描述 |
| --- | --- |
| typedef struct [FAST\_Rect](fast-kit--fast-rect.md) [FAST\_Rect](fast-kit-fast.md#fast_rect) | 定义矩形的数据结构。 |
| typedef struct [FAST\_RectPartitionConfig](fast-kit-fast.md#fast_rectpartitionconfig) [FAST\_RectPartitionConfig](fast-kit-fast.md#fast_rectpartitionconfig) | 矩形划分求解器的不透明配置。 |

### 函数

PhonePC/2in1Tablet

| 名称 | 描述 |
| --- | --- |
| FAST\_EXPORT [FAST\_ErrorCode](fast-kit-fast.md#fast_errorcode-1) [HMS\_FAST\_RectPartition\_CreateConfig](fast-kit-fast.md#hms_fast_rectpartition_createconfig) ([FAST\_RectPartitionConfig](fast-kit-fast.md#fast_rectpartitionconfig) \*\*config) | 创建矩形划分求解器的不透明配置。 |
| FAST\_EXPORT void [HMS\_FAST\_RectPartition\_DestroyConfig](fast-kit-fast.md#hms_fast_rectpartition_destroyconfig) ([FAST\_RectPartitionConfig](fast-kit-fast.md#fast_rectpartitionconfig) \*config) | 销毁矩形划分求解器的不透明配置。 |
| FAST\_EXPORT [FAST\_ErrorCode](fast-kit-fast.md#fast_errorcode-1) [HMS\_FAST\_RectPartition\_SetAlgo](fast-kit-fast.md#hms_fast_rectpartition_setalgo) ([FAST\_RectPartitionConfig](fast-kit-fast.md#fast_rectpartitionconfig) \*config, const char \*name) | 设置矩形划分求解器使用的算法。目前仅支持扫描线算法“SweepLineAlgo”，输出数量尽可能少（不保证最优性）的不相交矩形集合，复杂度为。 |
| FAST\_EXPORT [FAST\_ErrorCode](fast-kit-fast.md#fast_errorcode-1) [HMS\_FAST\_RectPartition\_Solve](fast-kit-fast.md#hms_fast_rectpartition_solve) ([FAST\_RectPartitionConfig](fast-kit-fast.md#fast_rectpartitionconfig) \*config, size\_t size, const [FAST\_Rect](fast-kit--fast-rect.md) \*origin, [FAST\_Rect](fast-kit--fast-rect.md) \*result, size\_t \*resultSize) | 在指定不透明配置下解决矩形划分问题。函数接收若干个彼此不相交的矩形作为输入，计算出覆盖相同区域的矩形划分方案，并使输出的矩形数量尽可能少。  **说明**：  1. 输入须保证矩形两两不相交（即任意两个矩形满足： 或 或或 ），否则函数返回FAST\_ERROR\_CODE\_ILLEGAL\_INPUT。  2. 函数保证输出矩形的数量小于等于输入矩形的数量。 |
