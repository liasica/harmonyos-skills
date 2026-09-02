---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-sensor-sensor-subscriber
title: Sensor_Subscriber
breadcrumb: API参考 > 系统 > 硬件 > Sensor Service Kit（传感器服务） > C API > 结构体 > Sensor_Subscriber
category: harmonyos-references
scraped_at: 2026-09-02T14:52:39+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:0082be18b1282c56c00bc5660682bd251580046f98e20084cf1ef325a006f8e9
---

```c
typedef struct Sensor_Subscriber Sensor_Subscriber
```

## 概述

用于注册传感器数据订阅的订阅者信息结构体，包含订阅回调函数和用户数据。使用该结构体可以指定传感器订阅者的参数，订阅成功后，将接收传感器的数据更新。

**起始版本：** 11

**相关模块：** [Sensor](capi-sensor.md)

**所在头文件：** [oh\_sensor\_type.h](capi-oh-sensor-type-h.md)
