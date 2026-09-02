---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-location-location-basicinfo
title: Location_BasicInfo
breadcrumb: API参考 > 应用服务 > Location Kit（位置服务） > C API > 结构体 > Location_BasicInfo
category: harmonyos-references
scraped_at: 2026-09-02T15:02:57+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:31b1fd2c33bd855f330b7a6b4595798a02610212236b255153fc03b7ff753e25
---

```c
typedef struct Location_BasicInfo {...} Location_BasicInfo
```

## 概述

定义位置基本信息的结构体。

**起始版本：** 13

**相关模块：** [Location](capi-location.md)

**所在头文件：** [oh\_location\_type.h](capi-oh-location-type-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| double latitude | 表示纬度信息，正值表示北纬，负值表示南纬。取值范围为-90到90。仅支持WGS84坐标系。 |
| double longitude | 表示经度信息，正值表示东经，负值表示西经。取值范围为-180到180。仅支持WGS84坐标系。 |
| double altitude | 表示高度信息，单位米。 |
| double accuracy | 表示精度信息，单位米。 |
| double speed | 表示速度信息，单位米每秒。 |
| double direction | 表示航向信息。单位是“度”，取值范围为0到360。 |
| int64\_t timeForFix | 表示位置时间戳，UTC格式。 |
| int64\_t timeSinceBoot | 表示获取位置的时间戳，值表示从本次开机到获取位置所经过的时间，单位为纳秒。 |
| double altitudeAccuracy | 表示高度信息的精度，单位米。 |
| double speedAccuracy | 表示速度信息的精度，单位米每秒。 |
| double directionAccuracy | 表示航向信息的精度。单位是“度”，取值范围为0到360。 |
| int64\_t uncertaintyOfTimeSinceBoot | 表示位置时间戳的不确定度，单位为纳秒。 |
| [Location\_SourceType](capi-oh-location-type-h.md#location_sourcetype) locationSourceType | 表示定位结果的来源。详细定义请参考[Location\_SourceType](capi-oh-location-type-h.md#location_sourcetype)。 |
