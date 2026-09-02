---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-sensor-sensor-subscriptionid
title: Sensor_SubscriptionId
breadcrumb: API参考 > 系统 > 硬件 > Sensor Service Kit（传感器服务） > C API > 结构体 > Sensor_SubscriptionId
category: harmonyos-references
scraped_at: 2026-09-02T14:52:39+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:ae48a392d6115afdac7ac8b54d17bdb7a3c21bd5937b969ba8c3a40e354fb231
---

```c
typedef struct Sensor_SubscriptionId Sensor_SubscriptionId
```

## 概述

定义传感器订阅ID结构体，用于唯一标识传感器订阅请求。该结构体用于标识一个传感器订阅操作，包含传感器类型、订阅的具体订阅条件等信息。开发者可以通过传感器订阅ID来管理传感器的订阅生命周期，包括激活、去激活和查询订阅状态等操作。

在订阅传感器数据时，作为订阅请求的参数，用于标识订阅关系，在查询已订阅的传感器信息时，用于获取对应的订阅状态和数据，在取消传感器订阅时，用于指定需要取消的订阅。

**起始版本：** 11

**相关模块：** [Sensor](capi-sensor.md)

**所在头文件：** [oh\_sensor\_type.h](capi-oh-sensor-type-h.md)
