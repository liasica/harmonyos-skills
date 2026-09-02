---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/pen-handwrite-headerfile-declare
title: native_handwrite_api.h
breadcrumb: API参考 > 系统 > 硬件 > Pen Kit（手写笔服务） > C API > 头文件和结构体 > 头文件 > native_handwrite_api.h
category: harmonyos-references
scraped_at: 2026-09-02T15:02:13+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:8a8be1aeb8a970458f15b901ab2c19ca1c98f87e4945ffedf6eac2e8a0eb0d30
---

## 概述

声明用于对外提供手写能力。

**库：** libhandwrite\_ndk.z.so

**引用文件：** <handwrite/native\_handwrite\_api.h>

**系统能力：** SystemCapability.Stylus.Handwrite

**起始版本：** 6.0.0(20)

**相关模块：** [HandWrite](pen-handwrite-c.md)

## 汇总

### 结构体

| 名称 | 描述 |
| --- | --- |
| struct [HandWrite\_HistoricalPoint](pen-handwrite-struct-historicalpoint.md) | 定义历史触摸点信息的结构体。 |

### 枚举

| 名称 | 描述 |
| --- | --- |
| [Handwrite\_ErrCode](pen-handwrite-c.md#handwrite_errcode) {  E\_NO\_ERROR = 0,  E\_PARAMS = 401,  E\_INNER\_ERROR = 1010400001,  E\_PERMISSION = 201  } | 定义手写错误码。 |

### 函数

| 名称 | 函数 |
| --- | --- |
| int32\_t [HMS\_HandWrite\_GetPredictPoint](pen-handwrite-c.md#hms_handwrite_getpredictpoint)(const [HandWrite\_HistoricalPoint](pen-handwrite-struct-historicalpoint.md) \*event, int32\_t size, float \*predictPointX, float \*predictPointY) | 此接口用于获取预测点。 |

### 函数

| 名称 | 函数 |
| --- | --- |
| int32\_t [HMS\_HandWrite\_SetRefreshDelayOff](pen-handwrite-c.md#hms_handwrite_setrefreshdelayoff)(const char\* xcomponentId, const bool enable) | 此接口用于笔记类应用提升手写笔书写时延。 |
