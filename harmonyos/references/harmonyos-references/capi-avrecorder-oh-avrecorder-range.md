---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avrecorder-oh-avrecorder-range
title: OH_AVRecorder_Range
breadcrumb: API参考 > 媒体 > Media Kit（媒体服务） > C API > 结构体 > OH_AVRecorder_Range
category: harmonyos-references
scraped_at: 2026-09-15T07:08:15+08:00
doc_updated_at: 2026-09-14
content_hash: sha256:d7405315ffe531160211fac96d4ca64d7a795df1646b5feca252e928d31eb189
---

```c
typedef struct OH_AVRecorder_Range {...} OH_AVRecorder_Range
```

## 概述

表示AVRecorder相关参数（如比特率、帧率等）的取值范围，用于限定录制参数的可配置范围。开发者可通过[OH\_AVRecorder\_GetAvailableEncoder](capi-avrecorder-h.md#oh_avrecorder_getavailableencoder)接口获取编码器相关参数取值范围，并在min和max所界定的范围内设置参数值，以确保配置有效。

**起始版本：** 18

**相关模块：** [AVRecorder](capi-avrecorder.md)

**所在头文件：** [avrecorder\_base.h](capi-avrecorder-base-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| int32\_t min | AVRecorder相关参数取值范围的最小值。单位与所描述的参数一致。 |
| int32\_t max | AVRecorder相关参数取值范围的最大值。单位与所描述的参数一致。 |
