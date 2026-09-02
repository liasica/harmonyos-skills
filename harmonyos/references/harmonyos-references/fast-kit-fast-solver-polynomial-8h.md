---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/fast-kit-fast-solver-polynomial-8h
title: fast_solver_polynomial.h
breadcrumb: API参考 > 系统 > 基础功能 > FAST Kit（算法加速服务） > C API > 头文件和结构体 > 头文件 > fast_solver_polynomial.h
category: harmonyos-references
scraped_at: 2026-09-02T15:02:07+08:00
doc_updated_at: 2026-09-01
content_hash: sha256:2f5ec5284ed6fc3057ffb1b259716a712bf9bff85f31b713d2e6623d369da999
---

## 概述

多项式零点求解器相关数据结构及函数定义。

**引用文件：** <FASTKit/fast\_solver\_polynomial.h>

**库：** libfast\_solver.so

**系统能力：** SystemCapability.FAST.Core

**起始版本：** 26.0.0

**相关模块：** [FAST](fast-kit-fast.md)

## 汇总

### 结构体

| 名称 | 描述 |
| --- | --- |
| struct [FAST\_Poly](fast-kit--fast-poly.md) | 定义稀疏格式多项式的数据结构。 |

### 类型定义

| 名称 | 描述 |
| --- | --- |
| typedef struct [FAST\_Poly](fast-kit--fast-poly.md) [FAST\_Poly](fast-kit-fast.md#fast_poly) | 定义稀疏格式多项式的数据结构。 |

### 函数

| 名称 | 描述 |
| --- | --- |
| [FAST\_ErrorCode](fast-kit-fast.md#fast_errorcode-1) [HMS\_FAST\_PolyRoot\_ComputeRoots](fast-kit-fast.md#hms_fast_polyroot_computeroots) (const [FAST\_Poly](fast-kit--fast-poly.md) \*poly, const size\_t maxRootCount, double \*root, size\_t \*rootCount) | 计算多项式的给定数量的实根。 |
| [FAST\_ErrorCode](fast-kit-fast.md#fast_errorcode-1) [HMS\_FAST\_PolyRoot\_ComputeSingle](fast-kit-fast.md#hms_fast_polyroot_computesingle) (const [FAST\_Poly](fast-kit--fast-poly.md) \*poly, double \*root) | 计算多项式的绝对值最大的实根。 |
| [FAST\_ErrorCode](fast-kit-fast.md#fast_errorcode-1) [HMS\_FAST\_PolyRoot\_ComputeRootIntervals](fast-kit-fast.md#hms_fast_polyroot_computerootintervals) (const [FAST\_Poly](fast-kit--fast-poly.md) \*poly, const size\_t maxRootCount, double \*leftBoundary, double \*rightBoundary, size\_t \*rootCount) | 计算多项式给定数量的实根的隔离区间，输出每个实根的左右边界。 |
