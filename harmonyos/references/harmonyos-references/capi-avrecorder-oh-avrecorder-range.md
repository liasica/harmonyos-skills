---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avrecorder-oh-avrecorder-range
title: OH_AVRecorder_Range
breadcrumb: API参考 > 媒体 > Media Kit（媒体服务） > C API > 结构体 > OH_AVRecorder_Range
category: harmonyos-references
scraped_at: 2026-09-02T15:02:36+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:41d0d1c854e1e157ae1e2990693b1636dcfecba3ab1b3abe2499d96009fcc1f7
---

```c
typedef struct OH_AVRecorder_Range {...} OH_AVRecorder_Range;
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
