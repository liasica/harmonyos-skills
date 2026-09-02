---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_f_g___mat4x4
title: FG_Mat4x4
breadcrumb: API参考 > 图形 > Graphics Accelerate Kit（图形加速服务） > C API > 头文件和结构体 > 结构体 > FG_Mat4x4
category: harmonyos-references
scraped_at: 2026-09-02T15:02:48+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:89cfd65e066ab7b55a3e901c19e167231d51a427df5d2702bc33796f80155374
---

## 概述

此结构体描述列主序4x4矩阵。列主序是指在连续的线性内存地址中，优先按列遍历矩阵元素。

**起始版本：** 5.0.0(12)

**相关模块：** [GraphicsAccelerate](_graphics_accelerate.md)

**所在头文件：** [frame\_generation\_base.h](frame__generation__base_8h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| float [data](_f_g___mat4x4.md#data) [16U] | 4x4列主序矩阵元素值组成的一维数组：  | a11 a12 a13 a14 |  | a21 a22 a23 a24 |  | a31 a32 a33 a34 |  | a41 a42 a43 a44 |  data[16] = {a11, a21, a31, a41, a12, a22, a32, a42, a13, a23, a33, a43, a14, a24, a34, a44} |

## 结构体成员变量说明

### data

```c
float FG_Mat4x4::data[16U]
```

**描述**

4x4列主序矩阵元素值组成的一维数组：

```c
     | a11 a12 a13 a14 |
A  = | a21 a22 a23 a24 |
     | a31 a32 a33 a34 |
     | a41 a42 a43 a44 |
data[16] = {a11, a21, a31, a41, a12, a22, a32, a42, a13, a23, a33, a43, a14, a24, a34, a44}
```
