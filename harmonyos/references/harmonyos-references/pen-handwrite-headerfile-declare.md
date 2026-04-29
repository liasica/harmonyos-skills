---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/pen-handwrite-headerfile-declare
title: native_handwrite_api.h
breadcrumb: API参考 > 系统 > 硬件 > Pen Kit（手写笔服务） > C API > 头文件和结构体 > 头文件 > native_handwrite_api.h
category: harmonyos-references
scraped_at: 2026-04-29T14:01:41+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:37c911833d492c6209359ca3e66f0dd67ce7a170be78abdf3bf2030421c69297
---

## 概述

PhonePC/2in1Tablet

声明用于对外提供手写能力。

**库：** libhandwrite\_ndk.z.so

**引用文件：** <handwrite/native\_handwrite\_api.h>

**系统能力：** SystemCapability.Stylus.Handwrite

**起始版本：** 6.0.0(20)

**相关模块：** [HandWrite](pen-handwrite-c.md)

## 汇总

PhonePC/2in1Tablet

### 结构体

PhonePC/2in1Tablet

| 名称 | 描述 |
| --- | --- |
| struct [HandWrite\_HistoricalPoint](pen-handwrite-struct-historicalpoint.md) | 定义历史触摸点信息的结构体。 |

### 枚举

PhonePC/2in1Tablet

| 名称 | 描述 |
| --- | --- |
| enum [HandWrite\_ErrCode](pen-handwrite-c.md#handwrite_errcode) {  E\_NO\_ERROR = 0,  E\_PARAMS = 401,  E\_INNER\_ERROR = 1010400001  } | 定义手写错误码。 |

### 函数

PhonePC/2in1Tablet

| 名称 | 函数 |
| --- | --- |
| int32\_t [HMS\_HandWrite\_GetPredictPoint](pen-handwrite-c.md#hms_handwrite_getpredictpoint)(const [HandWrite\_HistoricalPoint](pen-handwrite-struct-historicalpoint.md) \*event, int32\_t size, float \*predictPointX, float \*predictPointY) | 此接口用于获取预测点。 |
