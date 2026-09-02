---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/pen-handwrite-c
title: HandWrite
breadcrumb: API参考 > 系统 > 硬件 > Pen Kit（手写笔服务） > C API > 模块 > HandWrite
category: harmonyos-references
scraped_at: 2026-09-02T15:02:13+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:cd223610eab9d46ee1122efc3c926711e8846cf50994f2929e082ece63688eeb
---

## 概述

该模块对外提供手写能力。

**系统能力：** SystemCapability.Stylus.Handwrite

**起始版本：** 6.0.0(20)

## 汇总

### 文件

| 名称 | 描述 |
| --- | --- |
| [native\_handwrite\_api.h](pen-handwrite-headerfile-declare.md) | 声明用于对外提供手写能力。 |

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
| int32\_t [HMS\_HandWrite\_GetPredictPoint](pen-handwrite-c.md#hms_handwrite_getpredictpoint)(const [HandWrite\_HistoricalPoint](pen-handwrite-struct-historicalpoint.md)\* event,  int32\_t size, float \*predictPointX, float \*predictPointY) | 此接口用于获取预测点。 |

### 函数

| 名称 | 函数 |
| --- | --- |
| int32\_t [HMS\_HandWrite\_SetRefreshDelayOff](pen-handwrite-c.md#hms_handwrite_setrefreshdelayoff)(const char\* xcomponentId, const bool enable) | 此接口用于提升手写笔书写时延。 |

## 枚举类型说明

### Handwrite\_ErrCode

```c
enum Handwrite_ErrCode
```

**描述**

定义手写错误码。

**起始版本：** 6.0.0(20)

| 枚举值 | 描述 |
| --- | --- |
| E\_NO\_ERROR = 0 | 执行成功。 |
| E\_PARAMS = 401 | 输入参数无效。 |
| E\_INNER\_ERROR = 1010400001 | 系统内部错误，相关资源加载失败。 |
| E\_PERMISSION = 201 | 权限校验失败。  **起始版本：** 26.0.0 |

## 函数说明

### HMS\_HandWrite\_GetPredictPoint()

```c
int32_t HMS_HandWrite_GetPredictPoint(const HandWrite_HistoricalPoint* event,
    int32_t size, float *predictPointX, float *predictPointY)
```

**描述**

此接口用于获取预测点。

**起始版本：** 6.0.0(20)

| 名称 | 描述 |
| --- | --- |
| event | 指示输入的历史点。 |
| size | 历史点的个数。 |
| predictPointX | 接收预测点X坐标的指针。 |
| predictPointY | 接收预测点Y坐标的指针。 |

**返回：** 手写错误码HandWrite\_ErrCode：

E\_NO\_ERROR 0 - 执行成功。

E\_PARAMS 401 - 输入参数无效。

E\_INNER\_ERROR 1010400001 - 系统内部错误，相关资源加载失败。

## 函数说明

### HMS\_HandWrite\_SetRefreshDelayOff()

```c
int32_t HMS_HandWrite_SetRefreshDelayOff(const char* xcomponentId, const bool enable)
```

**描述**

此接口用于笔记类应用提升手写笔书写时延。

**起始版本：** 26.0.0

| 名称 | 描述 |
| --- | --- |
| xcomponentId | 自绘制控件的id。 |
| enable | 启用或禁用加速功能。 |

**返回：** 手写错误码HandWrite\_ErrCode：

E\_NO\_ERROR 0 - 执行成功。

E\_PERMISSION 201 - 权限校验失败。

E\_INNER\_ERROR 1010400001 - 系统内部错误，相关资源加载失败。
