---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/pen-handwrite-struct-historicalpoint
title: HandWrite_HistoricalPoint
breadcrumb: API参考 > 系统 > 硬件 > Pen Kit（手写笔服务） > C API > 头文件和结构体 > 结构体 > HandWrite_HistoricalPoint
category: harmonyos-references
scraped_at: 2026-09-02T15:02:13+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:59ebbeeacd4627cebe9c080a60a6304c38fa2d40a898d23673bef6aafad4b0cf
---

## 概述

定义历史触摸点信息的结构体。

**系统能力：** SystemCapability.Stylus.HandWrite

**起始版本：** 6.0.0(20)

**相关模块：** [HandWrite](pen-handwrite-c.md)

**所在头文件：** [native\_handwrite\_api.h](pen-handwrite-headerfile-declare.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| float [x](pen-handwrite-struct-historicalpoint.md#x) | 历史触摸点的X坐标，相对于被触摸元素左边缘，单位：像素。 |
| float [y](pen-handwrite-struct-historicalpoint.md#y) | 历史触摸点的Y坐标，相对于被触摸元素上边缘，单位：像素。 |
| int64\_t [timeStamp](pen-handwrite-struct-historicalpoint.md#timestamp) | 当前历史触摸点的时间戳，单位：ns。 |
| float [force](pen-handwrite-struct-historicalpoint.md#force) | 当前历史触摸点的压力值。 |

## 结构体成员变量说明

### x

```c
float HandWrite_HistoricalPoint::x
```

**描述**

历史触摸点的X坐标，相对于被触摸元素左边缘。

### y

```c
float HandWrite_HistoricalPoint::y
```

**描述**

历史触摸点的Y坐标，相对于被触摸元素上边缘。

### timeStamp

```c
int64_t HandWrite_HistoricalPoint::timeStamp
```

**描述**

当前历史触摸点的时间戳，单位为ns。

### force

```c
float HandWrite_HistoricalPoint::force
```

**描述**

当前历史触摸点的压力值。
