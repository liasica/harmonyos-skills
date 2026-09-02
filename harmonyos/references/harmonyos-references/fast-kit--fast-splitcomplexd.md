---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/fast-kit--fast-splitcomplexd
title: FAST_SplitComplexD
breadcrumb: API参考 > 系统 > 基础功能 > FAST Kit（算法加速服务） > C API > 头文件和结构体 > 结构体 > FAST_SplitComplexD
category: harmonyos-references
scraped_at: 2026-09-02T15:02:07+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:55a71f7a8e977732f7e918919523ecf068b59e43c3ebc907780162382db833ca
---

## 概述

定义双精度浮点复数信号的数据结构（分离格式：实部和虚部分开存储）。

**系统能力：** SystemCapability.FAST.Core

**起始版本：** 6.1.1(24)

**相关模块：** [FAST](fast-kit-fast.md)

**所在头文件：** [fast\_dsp\_common.h](fast-kit-fast-dsp-common-8h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| double\* [real](fast-kit--fast-splitcomplexd.md#real) | 实部数组指针。 |
| double\* [imag](fast-kit--fast-splitcomplexd.md#imag) | 虚部数组指针。 |

## 结构体成员变量说明

### imag

```c
double* FAST_SplitComplexD::imag
```

**描述**

指向虚部数组的指针。数组长度应与实部数组相同，存储复数信号的虚部数据。

### real

```c
double* FAST_SplitComplexD::real
```

**描述**

指向实部数组的指针。数组长度应与虚部数组相同，存储复数信号的实部数据。
