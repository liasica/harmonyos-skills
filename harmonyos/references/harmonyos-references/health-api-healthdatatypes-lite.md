---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/health-api-healthdatatypes-lite
title: healthDataTypes (运动健康数据类型常量)(Lite)
breadcrumb: API参考 > 应用服务 > Health Service Kit（运动健康服务） > ArkTS API > 运动健康数据类型常量及模型定义 > healthDataTypes (运动健康数据类型常量)(Lite)
category: harmonyos-references
scraped_at: 2026-11-12T09:57:19+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:55c5a73cc7490ef4dd40c76a0f440e4f9178fc4121202f437fca4fc43f1dc44e
---

本模块提供运动健康数据类型常量。

**起始版本：** 6.1.1(24)

## 导入模块

```javascript
import healthStore from '@hms.health.store';
```

**说明** 

此模块为healthStore子模块，需通过healthStore.healthDataTypes方式使用。

## 常量

**系统能力：** SystemCapability.Health.HealthStore.Lite

**起始版本：** 6.1.1(24)

**模型约束：** 此接口仅可在FA模型下使用。

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| WORKOUT | [healthStore.DataType](health-api-healthstore-lite.md#datatype) | 锻炼记录数据类型。 |
| WORKOUT\_SUMMARY | [healthStore.DataType](health-api-healthstore-lite.md#datatype) | 锻炼记录统计数据类型。 |
| WORKOUT\_DETAIL | [healthStore.DataType](health-api-healthstore-lite.md#datatype) | 锻炼记录详情数据类型。 |
| WORKOUT\_REALTIME | [healthStore.DataType](health-api-healthstore-lite.md#datatype) | 锻炼实时数据类型。 |
| BADMINTON | [healthStore.SubDataType](health-api-healthstore-lite.md#subdatatype) | 羽毛球子数据类型。 |
| PICKLEBALL | [healthStore.SubDataType](health-api-healthstore-lite.md#subdatatype) | 匹克球子数据类型。 |
| SOCCER | [healthStore.SubDataType](health-api-healthstore-lite.md#subdatatype) | 足球子数据类型。 |
| STAIR\_CLIMBING | [healthStore.SubDataType](health-api-healthstore-lite.md#subdatatype) | 爬楼子数据类型。 |
| STRENGTH\_TRAINING | [healthStore.SubDataType](health-api-healthstore-lite.md#subdatatype) | 力量训练子数据类型。 |
| TENNIS | [healthStore.SubDataType](health-api-healthstore-lite.md#subdatatype) | 网球子数据类型。 |
| OUTDOOR\_SNOWBOARD | [healthStore.SubDataType](health-api-healthstore-lite.md#subdatatype) | 户外单板滑雪子数据类型。  **起始版本：** 26.0.1 |
| INDOOR\_SNOWBOARD | [healthStore.SubDataType](health-api-healthstore-lite.md#subdatatype) | 室内单板滑雪子数据类型。  **起始版本：** 26.0.1 |
| OUTDOOR\_SKIING | [healthStore.SubDataType](health-api-healthstore-lite.md#subdatatype) | 户外双板滑雪子数据类型。  **起始版本：** 26.0.1 |
| INDOOR\_SKIING | [healthStore.SubDataType](health-api-healthstore-lite.md#subdatatype) | 室内双板滑雪子数据类型。  **起始版本：** 26.0.1 |
| CROSS\_COUNTRY\_SKIING | [healthStore.SubDataType](health-api-healthstore-lite.md#subdatatype) | 越野滑雪子数据类型。  **起始版本：** 26.0.1 |
| SKI\_MOUNTAINEERING | [healthStore.SubDataType](health-api-healthstore-lite.md#subdatatype) | 滑雪登山子数据类型。  **起始版本：** 26.0.1 |
| PADEL | [healthStore.SubDataType](health-api-healthstore-lite.md#subdatatype) | 笼式网球子数据类型。  **起始版本：** 26.0.1 |
| PILATES | [healthStore.SubDataType](health-api-healthstore-lite.md#subdatatype) | 普拉提子数据类型。  **起始版本：** 26.0.1 |
| RUNNING | [healthStore.SubDataType](health-api-healthstore-lite.md#subdatatype) | 户外跑步子数据类型。  **起始版本：** 26.0.1 |
| FREE\_TRAINING | [healthStore.SubDataType](health-api-healthstore-lite.md#subdatatype) | 自由训练子数据类型。  **起始版本：** 26.0.1 |
| CYCLING | [healthStore.SubDataType](health-api-healthstore-lite.md#subdatatype) | 户外骑行子数据类型。  **起始版本：** 26.0.1 |
