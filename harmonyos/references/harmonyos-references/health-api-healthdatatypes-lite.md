---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/health-api-healthdatatypes-lite
title: healthDataTypes (运动健康数据类型常量)(Lite)
breadcrumb: API参考 > 应用服务 > Health Service Kit（运动健康服务） > ArkTS API > 运动健康数据类型常量及模型定义 > healthDataTypes (运动健康数据类型常量)(Lite)
category: harmonyos-references
scraped_at: 2026-09-02T15:02:55+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:59bb5de9064f63f036517478aa2096ee84abe0980e2911611e424caa865544d3
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
