---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/health-api-healthstore
title: healthStore(运动健康数据服务)
breadcrumb: API参考 > 应用服务 > Health Service Kit（运动健康服务） > ArkTS API > healthStore(运动健康数据服务)
category: harmonyos-references
scraped_at: 2026-04-28T08:16:50+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:c49709b04090a8cb4cfe0fd6936dca0052c233d0faf1ac5192b5181a6a4b4254
---

本模块提供运动健康数据服务。

**起始版本：** 5.0.0(12)

## 导入模块

PhoneTabletWearable

```
1. import { healthStore } from '@kit.HealthServiceKit';
```

## AggregateMetrics

PhoneTabletWearable

type AggregateMetrics = Partial<Record<[AggregateMetricScope](health-api-healthstore.md#aggregatemetricscope), number>>

聚合策略。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| max | number | 否 | 是 | 最大值聚合，若未填写，则不查询此聚合类型。 |
| min | number | 否 | 是 | 最小值聚合，若未填写，则不查询此聚合类型。 |
| avg | number | 否 | 是 | 平均值聚合，若未填写，则不查询此聚合类型。 |
| sum | number | 否 | 是 | 累计值聚合，若未填写，则不查询此聚合类型。 |
| last | number | 否 | 是 | 最新值聚合，若未填写，则不查询此聚合类型。 |
| count | number | 否 | 是 | 计数聚合，若未填写，则不查询此聚合类型。 |

## AggregateMetricScope

PhoneTabletWearable

type AggregateMetricScope = 'max' | 'min' | 'avg' | 'sum' | 'last' | 'count'

聚合策略类型。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 类型 | **说明** |
| --- | --- |
| 'max' | 统计最大值。 |
| 'min' | 统计最小值。 |
| 'avg' | 统计平均值。 |
| 'sum' | 统计累计值。 |
| 'last' | 统计最新值。 |
| 'count' | 计数。 |

## AggregateRequest

PhoneTabletWearable

AggregateRequest<T extends Record<string, [AggregateMetrics](health-api-healthstore.md#aggregatemetrics)> = Record<string, [AggregateMetrics](health-api-healthstore.md#aggregatemetrics)>>

聚合查询请求类，继承Omit<[DataReadRequest](health-api-healthstore.md#datareadrequest), 'startTime' | 'endTime'>。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| dataType | [DataType](health-api-healthstore.md#datatype) | 否 | 否 | 聚合查询的数据类型。 |
| metrics | Partial<Record<keyof T, [AggregateMetricScope](health-api-healthstore.md#aggregatemetricscope)[]>> | 否 | 否 | 聚合策略。 |
| groupBy | [GroupOption](health-api-healthstore.md#groupoption) | 否 | 否 | 聚合分组选项。 |

## AggregateResult

PhoneTabletWearable

AggregateResult<T extends Record<string, [AggregateMetrics](health-api-healthstore.md#aggregatemetrics)> = Record<string, [AggregateMetrics](health-api-healthstore.md#aggregatemetrics)>>

聚合查询结果类，继承Omit<[SampleDataBase](health-api-healthstore.md#sampledatabase), 'dataSourceId'>。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| fields | Pick<T, keyof T> | 否 | 否 | 聚合查询字段。 |

## AppInfo

PhoneTabletWearable

应用信息类。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| bundleName | string | 是 | 是 | 调用方的应用包名，若未填写，默认为调用方包名。 |
| appId | string | 是 | 是 | 调用方的应用的OAuth 2.0客户端ID(client\_id)，若未填写，默认为调用方client\_id。 |
| appName | string | 是 | 是 | 调用方的应用名称，长度小于256字节。首次若未填写，默认为'CoreServiceExtAbility'，更新需要调用[updateDataSource](health-api-healthstore.md#healthstoreupdatedatasource)接口。 |
| version | string | 是 | 是 | 调用方的应用版本信息，长度小于256字节。首次若未填写，默认为空，更新需要调用[updateDataSource](health-api-healthstore.md#healthstoreupdatedatasource)接口。 |

## AuthorizationBase

PhoneTabletWearable

授权信息基类。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 名称 | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| readDataTypes | [DataType](health-api-healthstore.md#datatype)[] | 否 | 否 | 读数据类型。 |
| writeDataTypes | [DataType](health-api-healthstore.md#datatype)[] | 否 | 否 | 写数据类型。 |

## AuthorizationRequest

PhoneTabletWearable

授权请求参数类型，继承[AuthorizationBase](health-api-healthstore.md#authorizationbase)。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 名称 | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| readDataTypes | [DataType](health-api-healthstore.md#datatype)[] | 否 | 否 | 读数据类型。  **元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。 |
| writeDataTypes | [DataType](health-api-healthstore.md#datatype)[] | 否 | 否 | 写数据类型。  **元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。 |
| scopes | string[] | 否 | 是 | 非数据类型权限，使用scope授权，请参见[OAuth权限](../harmonyos-guides/health-cloudsync.md#oauth权限)，若未填写，默认为空。  **起始版本：** 5.1.0(18)  **元服务API：** 从版本5.1.0(18)开始，该接口支持在元服务中使用。 |

## AuthorizationResponse

PhoneTabletWearable

授权响应返回类型，继承[AuthorizationBase](health-api-healthstore.md#authorizationbase)。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 名称 | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| readDataTypes | [DataType](health-api-healthstore.md#datatype)[] | 否 | 否 | 授权成功的读数据类型，其对应权限在[应用申请权限](../harmonyos-guides/health-apply.md)和用户授权权限的交集中。  **元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。 |
| writeDataTypes | [DataType](health-api-healthstore.md#datatype)[] | 否 | 否 | 授权成功的写数据类型，其对应权限在[应用申请权限](../harmonyos-guides/health-apply.md)和用户授权权限的交集中。  **元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。 |
| scopes | string[] | 否 | 是 | 非数据类型权限，使用scope授权，请参见[OAuth权限](../harmonyos-guides/health-cloudsync.md#oauth权限)，若未填写，默认为空。  **起始版本：** 5.1.0(18)  **元服务API：** 从版本5.1.0(18)开始，该接口支持在元服务中使用。 |

## DataReadRequest

PhoneTabletWearable

读取请求参数基类，继承[DataRequest](health-api-healthstore.md#datarequest)。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| count | number | 否 | 是 | 读取数据的条数，若未填写，默认为无条数限制。  取值范围：[1, ∞) |
| offset | number | 否 | 是 | 相对于当前位置的偏移，若未填写，默认为0，无偏移。 |
| sortOrder | [SortOrder](health-api-healthstore.md#sortorder) | 否 | 是 | 排序顺序，若未填写，默认为升序。 |

## DataRequest

PhoneTabletWearable

请求参数基类。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| startLocalDate | string | 否 | 否 | 数据的开始本地日期，格式'MM/DD/YYYY'。  **元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。 |
| endLocalDate | string | 否 | 否 | 数据的结束本地日期，格式'MM/DD/YYYY'。  **元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。 |
| startTime | number | 否 | 否 | 请求的开始时间，Unix时间戳，以毫秒为单位。  该参数在Wearable设备上暂不生效，仅支持返回最新一条数据。  取值范围：(0, ∞) |
| endTime | number | 否 | 否 | 请求的结束时间，Unix时间戳，以毫秒为单位。  该参数在Wearable设备上暂不生效，仅支持返回最新一条数据。  取值范围：(0, ∞) |
| dataSourceOptions | [DataSourceOptions](health-api-healthstore.md#datasourceoptions) | 否 | 是 | 请求关联的数据源信息，若未填写，默认为无数据源限制。 |

## DataSource

PhoneTabletWearable

数据源。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| dataSourceId | string | 是 | 否 | 数据源的标识，由平台生成，无法更改，长度小于256字节。 |
| deviceInfo | [DeviceInfo](health-api-healthstore.md#deviceinfo) | 是 | 是 | 设备信息，若未填写，默认为空。 |
| appInfo | [AppInfo](health-api-healthstore.md#appinfo) | 是 | 是 | 应用信息，若未填写，默认为调用方应用信息。 |

## DataSourceBase

PhoneTabletWearable

type DataSourceBase = Omit<DataSource, 'dataSourceId'>

数据源的基类，用于插入数据源。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| deviceInfo | [DeviceInfo](health-api-healthstore.md#deviceinfo) | 是 | 是 | 设备信息，若未填写，默认为空。 |
| appInfo | [AppInfo](health-api-healthstore.md#appinfo) | 是 | 是 | 应用信息，若未填写，默认为调用方应用信息。 |

## DataSourceOptions

PhoneTabletWearable

数据源选项类，用于查询和删除。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| dataSourceId | string | 否 | 是 | 数据源的标识，由平台生成，无法更改，若未填写，默认为空。 |
| deviceUniqueId | string | 否 | 是 | 设备的UniqueId，若未填写，默认为空。 |
| appBundleName | string | 否 | 是 | 应用包名，若未填写，默认为空。 |
| appId | string | 否 | 是 | 应用的OAuth 2.0客户端ID(client\_id)，若未填写，默认为空。 |

## DataSourceReadRequest

PhoneTabletWearable

读取数据源请求。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| dataSourceId | string | 否 | 是 | 数据源的唯一标识（dataSourceId与bundleName、deviceUniqueId不能同时填写）。 |
| bundleName | string | 否 | 是 | 应用包名（仅当未填写dataSourceId时可填写）。 |
| deviceUniqueId | string | 否 | 是 | 设备UniqueId（仅当未填写dataSourceId时可填写）。 |

## DataType

PhoneTabletWearable

定义数据类型的类，每个数据类型字段都有唯一的id来标识。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 名称 | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| id | number | 是 | 否 | 数据类型唯一标识值。 |
| name | string | 是 | 是 | 数据类型的名称，若未填写，默认匹配id对应的名称。 |

## DeviceCategory

PhoneTabletWearable

设备类型枚举对象。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| MANUAL\_INPUT | '000' | 手动输入。 |
| SMART\_PHONE | '00E' | 手机。 |
| WEARABLE\_WATCH | '06D' | 手表。 |
| WEARABLE\_BAND | '06E' | 手环。 |
| SMART\_HEADPHONES | '082' | 智能耳机。 |
| HDK\_WEIGHT\_SCALE | '0CB' | 体脂秤。 |
| HDK\_BLOOD\_SUGAR\_MONITOR | '086' | 血糖仪。 |
| HDK\_BLOOD\_PRESSURE\_MONITOR | '02B' | 血压计。 |
| HDK\_HEART\_RATE\_MONITOR | '088' | 心率计。 |
| HDK\_THERMOMETER | '0B3' | 体温计。 |
| HDK\_BLOOD\_OXYGEN\_MONITOR | '0B4' | 血氧仪。 |
| HDK\_ROPE\_SKIPPING | '095' | 跳绳。 |
| HDK\_TREADMILL | '08F' | 跑步机。 |
| HDK\_EXERCISE\_BIKE | '0BF' | 动感单车。 |
| HDK\_ROWING\_MACHINE | '0C1' | 划船机。 |
| HDK\_ELLIPTICAL\_MACHINE | '0C0' | 椭圆机。 |
| HDK\_WALKING\_MACHINE | '092' | 漫步机。 |
| SPORTS\_GENIE | 'A12' | 跑姿监测设备。 |

## DeviceInfo

PhoneTabletWearable

设备信息类。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| uniqueId | string | 是 | 否 | 设备UniqueId，唯一标识，长度小于256字节。 |
| udid | string | 是 | 是 | 设备udid，若未填写，默认为空。 |
| name | string | 是 | 是 | 设备名称，长度小于256字节。(插入数据源时必填) |
| category | [DeviceCategory](health-api-healthstore.md#devicecategory) | 是 | 是 | 设备类型，需与productId匹配。(插入数据源时必填) |
| productId | string | 是 | 是 | 生态设备的华为全场景产品ID，需与category匹配，长度小于256字节。(插入数据源时必填)  例如手动输入场景：  category: [DeviceCategory](health-api-healthstore.md#devicecategory).MANUAL\_INPUT  productId: '0062' |
| model | string | 是 | 是 | 设备的型号名称，若未填写，默认为空。 |
| manufacturer | string | 是 | 是 | 设备的制造商信息，若未填写，默认为空。 |
| mac | string | 是 | 是 | 设备mac地址，若未填写，默认为空。 |
| sn | string | 是 | 是 | 设备sn地址，若未填写，默认为空。 |
| hardwareVersion | string | 是 | 是 | 设备硬件版本，若未填写，默认为空。 |
| softwareVersion | string | 是 | 是 | 设备软件版本，若未填写，默认为空。 |
| firmwareVersion | string | 是 | 是 | 设备固件版本，若未填写，默认为空。 |

## ExerciseSequence

PhoneTabletWearable

ExerciseSequence<K extends Record<string, [ExerciseSummary](health-api-healthstore.md#exercisesummary)> = Record<string, [ExerciseSummary](health-api-healthstore.md#exercisesummary)>,DK extends Record<string, [SequencePoint](health-api-healthstore.md#sequencepoint)[]> = Record<string, [SequencePoint](health-api-healthstore.md#sequencepoint)[]>>

锻炼记录数据类，继承[SampleDataBase](health-api-healthstore.md#sampledatabase)。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 名称 | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| exerciseType | [SubDataType](health-api-healthstore.md#subdatatype) | 否 | 否 | 锻炼记录子数据类型。 |
| duration | number | 否 | 是 | 锻炼时长，单位毫秒，若未填写，默认为结束时间减去开始时间。  取值范围：(0, ∞) |
| summaries | Pick<K, keyof K> | 否 | 否 | 统计数据，锻炼记录关联的统计数据类型参考[exerciseSequenceHelper](health-api-exercisedequencehelper.md)定义的模型。 |
| details | Pick<DK, keyof DK> | 否 | 是 | 详情数据，锻炼记录关联的详情数据类型参考[exerciseSequenceHelper](health-api-exercisedequencehelper.md)定义的模型，若未填写，默认为空。 |

## ExerciseSequenceDeleteRequest

PhoneTabletWearable

删除锻炼记录请求类，继承Omit<[DataRequest](health-api-healthstore.md#datarequest), 'startLocalDate' | 'endLocalDate'>。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 名称 | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| exerciseType | [SubDataType](health-api-healthstore.md#subdatatype) | [SubDataType](health-api-healthstore.md#subdatatype)[] | null | 否 | 否 | 锻炼记录子数据类型。若为空时，删除所有类型。 |

## ExerciseSequenceReadRequest

PhoneTabletWearable

ExerciseSequenceReadRequest<DK extends Record<string, [SequencePoint](health-api-healthstore.md#sequencepoint)[]> = Record<string, [SequencePoint](health-api-healthstore.md#sequencepoint)[]>>

读取锻炼记录请求类，继承Omit<[DataReadRequest](health-api-healthstore.md#datareadrequest), 'startLocalDate' | 'endLocalDate'>。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 名称 | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| exerciseType | [SubDataType](health-api-healthstore.md#subdatatype) | [SubDataType](health-api-healthstore.md#subdatatype)[] | null | 否 | 否 | 锻炼记录子数据类型，为空时查询所有类型。 |
| readOptions | [SequenceReadOptions](health-api-healthstore.md#sequencereadoptions)<DK> | 否 | 是 | 详情数据选项，若未填写，默认为不查询详情数据。 |

## ExerciseSummary

PhoneTabletWearable

锻炼记录统计数据类。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 名称 | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| [P: string] | [HealthValueType](health-api-healthstore.md#healthvaluetype) | [PaceValueType](health-api-healthstore.md#pacevaluetype) | 否 | 否 | 统计数据字段。 |

## GroupOption

PhoneTabletWearable

聚合分组选项。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 名称 | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| unitType | [GroupUnitType](health-api-healthstore.md#groupunittype) | 否 | 否 | 聚合策略（分组单元）。 |
| duration | number | 否 | 是 | 每个分组的单元数量，若未填写，默认为1，每个分组仅有一个单元，当前按天聚合只支持duration为1。 |

## GroupUnitType

PhoneTabletWearable

聚合策略（分组单元）枚举对象。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| DAY | 3 | 按天聚合。 |

## HealthSequence

PhoneTabletWearable

HealthSequence<K extends Record<string, [HealthValueType](health-api-healthstore.md#healthvaluetype)> = Record<string, [HealthValueType](health-api-healthstore.md#healthvaluetype)>,DK extends Record<string, [SequencePoint](health-api-healthstore.md#sequencepoint)[]> = Record<string, [SequencePoint](health-api-healthstore.md#sequencepoint)[]>>

健康记录数据类，继承[SampleDataBase](health-api-healthstore.md#sampledatabase)。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 名称 | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| summaries | Pick<K, keyof K> | 否 | 否 | 统计数据，健康记录关联的统计数据类型参考[healthSequenceHelper](health-api-healthsequencehelper.md)定义的模型。 |
| details | Pick<DK, keyof DK> | 否 | 是 | 详情数据，健康记录关联的详情数据类型参考[healthSequenceHelper](health-api-healthsequencehelper.md)定义的模型，若未填写，默认为空。 |

## HealthSequenceDeleteRequest

PhoneTabletWearable

删除健康记录请求类，继承Omit<[DataRequest](health-api-healthstore.md#datarequest), 'startLocalDate' | 'endLocalDate'>。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 名称 | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| healthSequenceDataType | [DataType](health-api-healthstore.md#datatype) | [DataType](health-api-healthstore.md#datatype)[] | 否 | 否 | 健康数据类型。 |

## HealthSequenceReadRequest

PhoneTabletWearable

HealthSequenceReadRequest<DK extends Record<string, [SequencePoint](health-api-healthstore.md#sequencepoint)[]> = Record<string, [SequencePoint](health-api-healthstore.md#sequencepoint)[]>>

读取健康记录请求类，继承Omit<[DataReadRequest](health-api-healthstore.md#datareadrequest), 'startLocalDate' | 'endLocalDate'>。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 名称 | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| healthSequenceDataType | [DataType](health-api-healthstore.md#datatype) | [DataType](health-api-healthstore.md#datatype)[] | 否 | 否 | 健康数据类型。 |
| readOptions | [SequenceReadOptions](health-api-healthstore.md#sequencereadoptions)<DK> | 否 | 是 | 详情数据选项，若未填写，默认为不查询详情数据。 |

## HealthValueType

PhoneTabletWearable

type HealthValueType = number | string | boolean | undefined

运动健康数据值类型。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 类型 | **说明** |
| --- | --- |
| number | 表示值类型为数字，可取任意值。 |
| string | 表示值类型为字符串，可取任意值。 |
| boolean | 表示值类型为布尔类型，可取true或false，具体含义以实际使用场景为准。 |
| undefined | 表示值类型为undefined，取值为空。  **起始版本：** 6.0.1(21) |

## PaceValueType

PhoneTabletWearable

type PaceValueType = Record<string, number>

配速数据类型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 类型 | **说明** |
| --- | --- |
| Record<string, number> | 配速数据字段。 |

## SampleDataBase

PhoneTabletWearable

健康数据基类。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 名称 | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| dataType | [DataType](health-api-healthstore.md#datatype) | 否 | 否 | 数据类型。  **元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。 |
| dataSourceId | string | 否 | 否 | 数据源唯一标识值。 |
| localDate | string | 否 | 否 | 数据的本地日期，格式'MM/DD/YYYY'。  **元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。 |
| startTime | number | 否 | 否 | 数据开始时间，Unix时间戳，以毫秒为单位。  取值范围：(0, ∞)  **元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。 |
| endTime | number | 否 | 否 | 数据结束时间，Unix时间戳，以毫秒为单位。  取值范围：(0, ∞)  **元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。 |
| timeZone | string | 否 | 否 | 数据所在的时区，格式为+0800。  **元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。 |
| modifiedTime | number | 否 | 否 | 创建或修改时间，Unix时间戳，以毫秒为单位。  取值范围：(0, ∞) |

## SamplePoint

PhoneTabletWearable

SamplePoint<K extends Record<string, [HealthValueType](health-api-healthstore.md#healthvaluetype)> = Record<string, [HealthValueType](health-api-healthstore.md#healthvaluetype)>>

数据采样点，继承[SampleDataBase](health-api-healthstore.md#sampledatabase)。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 名称 | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| fields | Pick<K, keyof K> | 否 | 否 | 数据的字段，数据类型对应的字段参考[samplePointHelper](health-api-samplepointhelper.md)定义的模型。 |

## SamplePointDeleteRequest

PhoneTabletWearable

type SamplePointDeleteRequest = UnixTimeBasedDataDeleteRequest

删除数据采样点请求类型，继承Omit<[DataRequest](health-api-healthstore.md#datarequest), 'startLocalDate' | 'endLocalDate'>。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 名称 | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| dataType | [DataType](health-api-healthstore.md#datatype) | [DataType](health-api-healthstore.md#datatype)[] | 否 | 否 | 待删除的数据类型。 |

## SamplePointReadRequest

PhoneTabletWearable

SamplePointReadRequest<FK extends Record<string, [HealthValueType](health-api-healthstore.md#healthvaluetype)> = Record<string, [HealthValueType](health-api-healthstore.md#healthvaluetype)>>

读取数据采样点请求类，继承Omit<[DataReadRequest](health-api-healthstore.md#datareadrequest), 'startLocalDate' | 'endLocalDate'>。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 名称 | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| samplePointDataType | [DataType](health-api-healthstore.md#datatype)| [DataType](health-api-healthstore.md#datatype)[] | 否 | 否 | 查询的数据类型。 |
| fields | Partial<Pick<FK, keyof FK>> | 否 | 是 | 要读取的字段列表，若samplePointDataType参数为数组，fields字段不能设置，数据类型对应的字段参考[samplePointHelper](health-api-samplepointhelper.md)定义的模型。若为空，则用于读取所有字段。 |

## SequencePoint

PhoneTabletWearable

运动健康数据详情点。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 名称 | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| startTime | number | 否 | 否 | 数据开始时间，Unix时间戳，以毫秒为单位。  取值范围：(0, ∞) |
| [P: string] | [HealthValueType](health-api-healthstore.md#healthvaluetype) | 否 | 否 | 详情数据点字段。 |

## SequenceReadOptions

PhoneTabletWearable

SequenceReadOptions<DK extends Record<string, [SequencePoint](health-api-healthstore.md#sequencepoint)[]> = Record<string, [SequencePoint](health-api-healthstore.md#sequencepoint)[]>>

读取运动健康记录详情数据选项类。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 名称 | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| withDetails | boolean | 否 | 是 | 是否读取全部详情。true为读取全部详情，false为不读取详情，若未填写，则withPartialDetails参数生效。 |
| withPartialDetails | (keyof DK)[] | 否 | 是 | 读取部分详情数据类型（若需要读取部分详情，withDetails参数不能填写），锻炼记录与健康记录关联的详情数据类型分别参考[exerciseSequenceHelper](health-api-exercisedequencehelper.md)与[healthSequenceHelper](health-api-healthsequencehelper.md)定义的模型。 |

## SequenceValueType

PhoneTabletWearable

type SequenceValueType = number | string | boolean | object

运动健康数据值类型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 类型 | **说明** |
| --- | --- |
| number | 表示值类型为数字，可取任意值。 |
| string | 表示值类型为字符串，可取任意值。 |
| boolean | 表示值类型为布尔类型，可取true或false，具体含义以实际使用场景为准。 |
| object | 表示值类型为对象，可取任意值。 |

## SortOrder

PhoneTabletWearable

结果排序类型枚举对象。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| ASC | 0 | 升序。 |
| DESC | 1 | 降序。 |

## SubDataType

PhoneTabletWearable

type SubDataType = DataType

子数据类型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 名称 | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| id | number | 是 | 否 | 子数据类型唯一标识值。 |
| name | string | 是 | 是 | 子数据类型的名称，若未填写，默认匹配id对应的名称。 |

## UnixTimeBasedDataDeleteRequest

PhoneTabletWearable

基于Unix时间戳的删除请求基类，继承Omit<[DataRequest](health-api-healthstore.md#datarequest), 'startLocalDate' | 'endLocalDate'>。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 名称 | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| dataType | [DataType](health-api-healthstore.md#datatype) | [DataType](health-api-healthstore.md#datatype)[] | 否 | 否 | 待删除的数据类型。 |

## healthStore.init

PhoneTabletWearable

init(context: common.Context): Promise<void>

Health Service初始化接口，使用Promise异步方式，其他接口调用前需先初始化，仅首次调用需要。

该接口从API 19 Release开始，支持Wearable设备开发。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| context | [common.Context](js-apis-inner-application-context.md#context) | 是 | 上下文，目前只支持[UIAbility](js-apis-app-ability-uiability.md)或[UIExtensionAbility](js-apis-app-ability-uiextensionability.md)的上下文环境。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无结果返回的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[运动健康服务ArkTS API错误码](errorcode-healthservice.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [401](errorcode-healthservice.md#section401-参数不合法) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;2. Incorrect parameter types. |

**示例：**

```
1. import { healthStore } from '@kit.HealthServiceKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. try {
5. // 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext
6. await healthStore.init(this.getUIContext().getHostContext());
7. hilog.info(0x0000, 'testTag', 'Succeeded in initing.');
8. } catch (err) {
9. hilog.error(0x0000, 'testTag', `Failed to init. Code: ${err.code}, message: ${err.message}`);
10. }
```

## healthStore.insertDataSource

PhoneTabletWearable

insertDataSource(dataSource: DataSourceBase): Promise<string>

插入指定的数据源，使用Promise异步方式。

**系统能力：** SystemCapability.Health.HealthStore

**设备行为差异：** 该接口在Phone、Tablet中可正常调用，在Wearable中返回1002700001错误码。

**起始版本：** 5.0.0(12)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| dataSource | [DataSourceBase](health-api-healthstore.md#datasourcebase) | 是 | 构造的数据源。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<string> | Promise对象，返回数据源唯一标识符（dataSourceId）。 |

**错误码：**

以下错误码的详细介绍请参见[运动健康服务ArkTS API错误码](errorcode-healthservice.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [201](errorcode-healthservice.md#section201-鉴权失败) | Permission verification failed. |
| [401](errorcode-healthservice.md#section401-参数不合法) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;2. Incorrect parameter types; 3.Parameter verification failed. |
| [1002700001](errorcode-healthservice.md#section1002700001-系统内部错误) | System internal error. |
| [1002700002](errorcode-healthservice.md#section1002700002-数据库异常) | Database processing error. |
| [1002701001](errorcode-healthservice.md#section1002701001-网络错误) | Network error. The network is unavailable. |
| [1002702001](errorcode-healthservice.md#section1002702001-账号未登录) | Account error. The user has not logged in with HUAWEI ID. |
| [1002702002](errorcode-healthservice.md#section1002702002-账号异常) | Account error. Failed to obtain account information with HUAWEI ID. |
| [1002703001](errorcode-healthservice.md#section1002703001-用户隐私未同意) | User privacy is not agreed. |

说明

上述接口调用前，需先使用[init](health-api-healthstore.md#healthstoreinit)方法进行初始化。

**示例：**

```
1. import { healthStore } from '@kit.HealthServiceKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. let dataSource: healthStore.DataSourceBase = {
5. deviceInfo: {
6. uniqueId: 'test',
7. name: 'test', // 插入数据源时此字段必填
8. category: healthStore.DeviceCategory.WEARABLE_BAND, // 插入数据源时此字段必填
9. productId: '0554', // 插入数据源时此字段必填
10. model: 'lotana',
11. manufacturer: 'HUAWEI',
12. mac: 'testDeviceMac',
13. sn: 'testDeviceSn',
14. hardwareVersion: '1',
15. softwareVersion: '2',
16. firmwareVersion: '3',
17. udid: ''
18. }
19. }

21. try {
22. const dataSourceId = await healthStore.insertDataSource(dataSource);
23. hilog.info(0x0000, 'testTag', `Succeeded in inserting dataSource, the dataSourceId is ${dataSourceId}.`);
24. } catch (err) {
25. hilog.error(0x0000, 'testTag', `Failed to insert dataSource. Code: ${err.code}, message: ${err.message}`);
26. }
```

## healthStore.readDataSource

PhoneTabletWearable

readDataSource(request: DataSourceReadRequest): Promise<DataSource[]>

读取数据源，使用Promise异步方式。

**系统能力：** SystemCapability.Health.HealthStore

**设备行为差异：** 该接口在Phone、Tablet中可正常调用，在Wearable中返回1002700001错误码。

**起始版本：** 5.0.0(12)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| request | [DataSourceReadRequest](health-api-healthstore.md#datasourcereadrequest) | 是 | 读取数据源请求。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[DataSource](health-api-healthstore.md#datasource)[]> | Promise对象，返回[DataSource](health-api-healthstore.md#datasource)数组。 |

**错误码：**

以下错误码的详细介绍请参见[运动健康服务ArkTS API错误码](errorcode-healthservice.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [201](errorcode-healthservice.md#section201-鉴权失败) | Permission verification failed. |
| [401](errorcode-healthservice.md#section401-参数不合法) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;2. Incorrect parameter types; 3.Parameter verification failed. |
| [1002700001](errorcode-healthservice.md#section1002700001-系统内部错误) | System internal error. |
| [1002700002](errorcode-healthservice.md#section1002700002-数据库异常) | Database processing error. |
| [1002701001](errorcode-healthservice.md#section1002701001-网络错误) | Network error. The network is unavailable. |
| [1002702001](errorcode-healthservice.md#section1002702001-账号未登录) | Account error. The user has not logged in with HUAWEI ID. |
| [1002702002](errorcode-healthservice.md#section1002702002-账号异常) | Account error. Failed to obtain account information with HUAWEI ID. |
| [1002703001](errorcode-healthservice.md#section1002703001-用户隐私未同意) | User privacy is not agreed. |

说明

上述接口调用前，需先使用[init](health-api-healthstore.md#healthstoreinit)方法进行初始化。

**示例：**

```
1. import { healthStore } from '@kit.HealthServiceKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. let readSourceRequest: healthStore.DataSourceReadRequest = {
5. deviceUniqueId: 'testudidupdate'
6. }

8. try {
9. let dataSources = await healthStore.readDataSource(readSourceRequest);
10. dataSources.forEach((dataSource) => {
11. hilog.info(0x0000, 'testTag', `Succeeded in reading dataSource, the dataSourceId is ${dataSource.dataSourceId}.`);
12. });
13. } catch (err) {
14. hilog.error(0x0000, 'testTag', `Failed to read dataSource. Code: ${err.code}, message: ${err.message}`);
15. }
```

## healthStore.updateDataSource

PhoneTabletWearable

updateDataSource(dataSource: DataSource): Promise<void>

更新数据源，使用Promise异步方式。

**系统能力：** SystemCapability.Health.HealthStore

**设备行为差异：** 该接口在Phone、Tablet中可正常调用，在Wearable中返回1002700001错误码。

**起始版本：** 5.0.0(12)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| dataSource | [DataSource](health-api-healthstore.md#datasource) | 是 | 待更新的数据源。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无结果返回的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[运动健康服务ArkTS API错误码](errorcode-healthservice.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [201](errorcode-healthservice.md#section201-鉴权失败) | Permission verification failed. |
| [401](errorcode-healthservice.md#section401-参数不合法) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;2. Incorrect parameter types; 3.Parameter verification failed. |
| [1002700001](errorcode-healthservice.md#section1002700001-系统内部错误) | System internal error. |
| [1002700002](errorcode-healthservice.md#section1002700002-数据库异常) | Database processing error. |
| [1002701001](errorcode-healthservice.md#section1002701001-网络错误) | Network error. The network is unavailable. |
| [1002702001](errorcode-healthservice.md#section1002702001-账号未登录) | Account error. The user has not logged in with HUAWEI ID. |
| [1002702002](errorcode-healthservice.md#section1002702002-账号异常) | Account error. Failed to obtain account information with HUAWEI ID. |
| [1002703001](errorcode-healthservice.md#section1002703001-用户隐私未同意) | User privacy is not agreed. |

说明

上述接口调用前，需先使用[init](health-api-healthstore.md#healthstoreinit)方法进行初始化。

**示例：**

```
1. import { healthStore } from '@kit.HealthServiceKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. let newDataSource: healthStore.DataSource = {
5. deviceInfo: {
6. uniqueId: 'test',
7. name: 'test',
8. category: healthStore.DeviceCategory.WEARABLE_BAND,
9. productId: '0554',
10. model: 'lotana',
11. manufacturer: 'HUAWEI',
12. mac: 'testDeviceMac',
13. sn: 'testDeviceSn',
14. hardwareVersion: '1',
15. softwareVersion: '2',
16. firmwareVersion: '3',
17. // 修改udid
18. udid: 'updateudid'
19. },
20. // 此处dataSourceId值为开发步骤插入数据源时，返回的dataSourceId
21. dataSourceId: 'xxx'
22. }

24. try {
25. await healthStore.updateDataSource(newDataSource);
26. hilog.info(0x0000, 'testTag', 'Succeeded in updating dataSource.');
27. } catch (err) {
28. hilog.error(0x0000, 'testTag', `Failed to update dataSource. Code: ${err.code}, message: ${err.message}`);
29. }
```

## healthStore.saveData

PhoneTabletWearable

saveData(sampleData: SamplePoint[] | SamplePoint): Promise<void>

保存数据采样点，使用Promise异步方式。

**系统能力：** SystemCapability.Health.HealthStore

**设备行为差异：** 该接口在Phone、Tablet中可正常调用，在Wearable中返回1002700001错误码。

**起始版本：** 5.0.0(12)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| sampleData | [SamplePoint](health-api-healthstore.md#samplepoint)[] | [SamplePoint](health-api-healthstore.md#samplepoint) | 是 | 单个数据采样点或数据采样点数组。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无结果返回的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[运动健康服务ArkTS API错误码](errorcode-healthservice.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [201](errorcode-healthservice.md#section201-鉴权失败) | Permission verification failed. |
| [401](errorcode-healthservice.md#section401-参数不合法) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;2. Incorrect parameter types; 3.Parameter verification failed. |
| [1002700001](errorcode-healthservice.md#section1002700001-系统内部错误) | System internal error. |
| [1002700002](errorcode-healthservice.md#section1002700002-数据库异常) | Database processing error. |
| [1002701001](errorcode-healthservice.md#section1002701001-网络错误) | Network error. The network is unavailable. |
| [1002702001](errorcode-healthservice.md#section1002702001-账号未登录) | Account error. The user has not logged in with HUAWEI ID. |
| [1002702002](errorcode-healthservice.md#section1002702002-账号异常) | Account error. Failed to obtain account information with HUAWEI ID. |
| [1002703001](errorcode-healthservice.md#section1002703001-用户隐私未同意) | User privacy is not agreed. |

说明

上述接口调用前，需先使用[init](health-api-healthstore.md#healthstoreinit)方法进行初始化。

**示例：**

```
1. import { healthStore } from '@kit.HealthServiceKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. let samplePoint: healthStore.SamplePoint = {
5. dataType: healthStore.samplePointHelper.bodyTemperature.DATA_TYPE,
6. startTime: 1698633801000,
7. endTime: 1698633801000,
8. localDate: '10/30/2023',
9. timeZone: '+0800',
10. modifiedTime: 1698633801000,
11. // insertDataSource插入数据源接口返回的DataSourceId
12. dataSourceId: 'xxx',
13. fields: {
14. bodyTemperature: 39
15. }
16. }

18. try {
19. await healthStore.saveData(samplePoint);
20. hilog.info(0x0000, 'testTag', 'Succeeded in saving data.');
21. } catch (err) {
22. hilog.error(0x0000, 'testTag', `Failed to save data. Code: ${err.code}, message: ${err.message}`);
23. }
```

## healthStore.saveData

PhoneTabletWearable

saveData(exerciseSequence: ExerciseSequence[] | ExerciseSequence): Promise<void>

保存锻炼记录数据，使用Promise异步方式。

**系统能力：** SystemCapability.Health.HealthStore

**设备行为差异：** 该接口在Phone、Tablet中可正常调用，在Wearable中返回1002700001错误码。

**起始版本：** 5.0.0(12)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| exerciseSequence | [ExerciseSequence](health-api-healthstore.md#exercisesequence)[] | [ExerciseSequence](health-api-healthstore.md#exercisesequence) | 是 | 单个锻炼记录或锻炼记录数组。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无结果返回的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[运动健康服务ArkTS API错误码](errorcode-healthservice.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [201](errorcode-healthservice.md#section201-鉴权失败) | Permission verification failed. |
| [401](errorcode-healthservice.md#section401-参数不合法) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;2. Incorrect parameter types; 3.Parameter verification failed. |
| [1002700001](errorcode-healthservice.md#section1002700001-系统内部错误) | System internal error. |
| [1002700002](errorcode-healthservice.md#section1002700002-数据库异常) | Database processing error. |
| [1002701001](errorcode-healthservice.md#section1002701001-网络错误) | Network error. The network is unavailable. |
| [1002702001](errorcode-healthservice.md#section1002702001-账号未登录) | Account error. The user has not logged in with HUAWEI ID. |
| [1002702002](errorcode-healthservice.md#section1002702002-账号异常) | Account error. Failed to obtain account information with HUAWEI ID. |
| [1002703001](errorcode-healthservice.md#section1002703001-用户隐私未同意) | User privacy is not agreed. |

说明

上述接口调用前，需先使用[init](health-api-healthstore.md#healthstoreinit)方法进行初始化。

**示例：**

```
1. import { healthStore } from '@kit.HealthServiceKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. // 构造跑步记录
5. const startTime = 1698040800000; // 2023-10-23 14:00:00
6. const endTime = 1698042600000; // 2023-10-23 14:30:00

8. const runningSequence: healthStore.exerciseSequenceHelper.running.Model = {
9. dataType: healthStore.exerciseSequenceHelper.DATA_TYPE,
10. // insertDataSource插入数据源接口返回的DataSourceId
11. dataSourceId: 'xxx',
12. startTime: startTime, // 2023-10-23 14:00:00
13. endTime: endTime, // 2023-10-23 14:30:00
14. localDate: '10/23/2023',
15. timeZone: '+0800',
16. modifiedTime: new Date().getTime(),
17. exerciseType: healthStore.exerciseSequenceHelper.running.EXERCISE_TYPE,
18. duration: 1800000,
19. summaries: {
20. distance: {
21. totalDistance: 2000
22. },
23. calorie: {
24. totalCalories: 20
25. },
26. speed: {
27. avg: 5,
28. max: 6
29. }
30. },
31. details: {
32. exerciseHeartRate: [
33. {
34. startTime: startTime,
35. bpm: 88
36. },
37. {
38. startTime: startTime + 5000,
39. bpm: 89
40. }
41. ],
42. speed: [
43. {
44. startTime: startTime,
45. speed: 2.5
46. },
47. {
48. startTime: startTime + 5000,
49. speed: 2.3
50. }
51. ],
52. altitude: [
53. {
54. startTime: startTime,
55. altitude: 100
56. },
57. {
58. startTime: startTime + 5000,
59. altitude: 101
60. }
61. ]
62. }
63. };
64. try {
65. await healthStore.saveData(runningSequence);
66. hilog.info(0x0000, 'testTag', 'Succeeded in saving data.');
67. } catch (err) {
68. hilog.error(0x0000, 'testTag', `Failed to save data. Code: ${err.code}, message: ${err.message}`);
69. }
```

## healthStore.saveData

PhoneTabletWearable

saveData(healthSequence: HealthSequence[] | HealthSequence): Promise<void>

保存健康记录数据，使用Promise异步方式。

**系统能力：** SystemCapability.Health.HealthStore

**设备行为差异：** 该接口在Phone、Tablet中可正常调用，在Wearable中返回1002700001错误码。

**起始版本：** 5.0.0(12)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| healthSequence | [HealthSequence](health-api-healthstore.md#healthsequence)[] | [HealthSequence](health-api-healthstore.md#healthsequence) | 是 | 单个健康记录或健康记录数组。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无结果返回的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[运动健康服务ArkTS API错误码](errorcode-healthservice.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [201](errorcode-healthservice.md#section201-鉴权失败) | Permission verification failed. |
| [401](errorcode-healthservice.md#section401-参数不合法) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;2. Incorrect parameter types; 3.Parameter verification failed. |
| [1002700001](errorcode-healthservice.md#section1002700001-系统内部错误) | System internal error. |
| [1002700002](errorcode-healthservice.md#section1002700002-数据库异常) | Database processing error. |
| [1002701001](errorcode-healthservice.md#section1002701001-网络错误) | Network error. The network is unavailable. |
| [1002702001](errorcode-healthservice.md#section1002702001-账号未登录) | Account error. The user has not logged in with HUAWEI ID. |
| [1002702002](errorcode-healthservice.md#section1002702002-账号异常) | Account error. Failed to obtain account information with HUAWEI ID. |
| [1002703001](errorcode-healthservice.md#section1002703001-用户隐私未同意) | User privacy is not agreed. |

说明

上述接口调用前，需先使用[init](health-api-healthstore.md#healthstoreinit)方法进行初始化。

**示例：**

```
1. import { healthStore } from '@kit.HealthServiceKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. let healthSequence: healthStore.healthSequenceHelper.sleepRecord.Model = {
5. summaries: {
6. fallAsleepTime: 1695740400000, // 2023-09-26 23:00:00
7. wakeupTime: 1695769200000, // 2023-09-27 7:00:00
8. sleepScore: 80,
9. wakeCount: 2,
10. sleepType: 1,
11. shallowDuration: 14400,
12. deepDuration: 7200,
13. dreamDuration: 7200,
14. wakeDuration: 0,
15. duration: 28800
16. },
17. dataType: healthStore.healthSequenceHelper.sleepRecord.DATA_TYPE,
18. // insertDataSource插入数据源接口返回的DataSourceId
19. dataSourceId: 'xxx',
20. localDate: '09/26/2023',
21. startTime: 1695740400000,
22. endTime: 1695769200000,
23. timeZone: '+0800',
24. modifiedTime: 1695769200000,
25. details: {
26. sleepSegment: [
27. {
28. startTime: 1695740400000, // 2023-09-26 23:00:00
29. endTime: 1695747600000, // 2023-09-27 01:00:00
30. sleepStatus: 2
31. },
32. {
33. startTime: 1695747600000, // 2023-09-27 01:00:00
34. endTime: 1695754800000, // 2023-09-27 03:00:00
35. sleepStatus: 1
36. },
37. {
38. startTime: 1695754800000, // 2023-09-27 03:00:00
39. endTime: 1695762000000, // 2023-09-27 05:00:00
40. sleepStatus: 3
41. },
42. {
43. startTime: 1695762000000, // 2023-09-27 05:00:00
44. endTime: 1695769200000, // 2023-09-27 07:00:00
45. sleepStatus: 2
46. }
47. ]
48. }
49. }
50. try {
51. await healthStore.saveData(healthSequence);
52. hilog.info(0x0000, 'testTag', 'Succeeded in saving data.');
53. } catch (err) {
54. hilog.error(0x0000, 'testTag', `Failed to save data. Code: ${err.code}, message: ${err.message}`);
55. }
```

## healthStore.readData

PhoneTabletWearable

readData<T extends SamplePoint>(request: SamplePointReadRequest): Promise<T[]>

读取数据采样点，使用Promise异步方式。

该接口从API 19 Release开始，支持Wearable设备开发。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| request | [SamplePointReadRequest](health-api-healthstore.md#samplepointreadrequest) | 是 | 读取数据采样点请求，查询时间跨度范围为31天。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<T[]> | Promise对象，T继承[SamplePoint](health-api-healthstore.md#samplepoint)，返回数据采样点数组。 |

**错误码：**

以下错误码的详细介绍请参见[运动健康服务ArkTS API错误码](errorcode-healthservice.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [201](errorcode-healthservice.md#section201-鉴权失败) | Permission verification failed. |
| [401](errorcode-healthservice.md#section401-参数不合法) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;2. Incorrect parameter types; 3.Parameter verification failed. |
| [1002700001](errorcode-healthservice.md#section1002700001-系统内部错误) | System internal error. |
| [1002700002](errorcode-healthservice.md#section1002700002-数据库异常) | Database processing error. |
| [1002701001](errorcode-healthservice.md#section1002701001-网络错误) | Network error. The network is unavailable. |
| [1002702001](errorcode-healthservice.md#section1002702001-账号未登录) | Account error. The user has not logged in with HUAWEI ID. |
| [1002702002](errorcode-healthservice.md#section1002702002-账号异常) | Account error. Failed to obtain account information with HUAWEI ID. |
| [1002703001](errorcode-healthservice.md#section1002703001-用户隐私未同意) | User privacy is not agreed. |

说明

上述接口调用前，需先使用[init](health-api-healthstore.md#healthstoreinit)方法进行初始化。

**示例：**

```
1. import { healthStore } from '@kit.HealthServiceKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. let samplePointReadRequest: healthStore.SamplePointReadRequest = {
5. samplePointDataType: healthStore.samplePointHelper.bodyTemperature.DATA_TYPE,
6. startTime: 1698633801000,
7. endTime: 1698633801000,
8. fields: {
9. bodyTemperature: 39
10. }
11. }

13. try {
14. let samplePoints = await healthStore.readData(samplePointReadRequest);
15. samplePoints.forEach((samplePoint) => {
16. hilog.info(0x0000, 'testTag', `Succeeded in reading data, the bodyTemperature is ${samplePoint.fields.bodyTemperature}.`);
17. });
18. } catch (err) {
19. hilog.error(0x0000, 'testTag', `Failed to read data. Code: ${err.code}, message: ${err.message}`);
20. }
```

## healthStore.readData

PhoneTabletWearable

readData<T extends ExerciseSequence>(request: ExerciseSequenceReadRequest): Promise<T[]>

读取锻炼记录数据，使用Promise异步方式。

该接口从API 19 Release开始，支持Wearable设备开发。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| request | [ExerciseSequenceReadRequest](health-api-healthstore.md#exercisesequencereadrequest) | 是 | 读取锻炼记录请求，查询时间跨度范围为31天。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<T[]> | Promise对象，T继承[ExerciseSequence](health-api-healthstore.md#exercisesequence)，返回锻炼记录数组。 |

**错误码：**

以下错误码的详细介绍请参见[运动健康服务ArkTS API错误码](errorcode-healthservice.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [201](errorcode-healthservice.md#section201-鉴权失败) | Permission verification failed. |
| [401](errorcode-healthservice.md#section401-参数不合法) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;2. Incorrect parameter types; 3.Parameter verification failed. |
| [1002700001](errorcode-healthservice.md#section1002700001-系统内部错误) | System internal error. |
| [1002700002](errorcode-healthservice.md#section1002700002-数据库异常) | Database processing error. |
| [1002701001](errorcode-healthservice.md#section1002701001-网络错误) | Network error. The network is unavailable. |
| [1002702001](errorcode-healthservice.md#section1002702001-账号未登录) | Account error. The user has not logged in with HUAWEI ID. |
| [1002702002](errorcode-healthservice.md#section1002702002-账号异常) | Account error. Failed to obtain account information with HUAWEI ID. |
| [1002703001](errorcode-healthservice.md#section1002703001-用户隐私未同意) | User privacy is not agreed. |

说明

上述接口调用前，需先使用[init](health-api-healthstore.md#healthstoreinit)方法进行初始化。

**示例：**

```
1. import { healthStore } from '@kit.HealthServiceKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. // 查询跑步记录
5. const startTime = 1698040800000; // 2023-10-23 14:00:00
6. const endTime = 1698042600000; // 2023-10-23 14:30:00

8. const sequenceReadRequest: healthStore.ExerciseSequenceReadRequest<healthStore.exerciseSequenceHelper.running.DetailFields> = {
9. startTime: startTime,
10. endTime: endTime,
11. exerciseType: healthStore.exerciseSequenceHelper.running.EXERCISE_TYPE,
12. count: 1,
13. sortOrder: 1,
14. readOptions: {
15. withPartialDetails: ['exerciseHeartRate', 'altitude']
16. }
17. };
18. try {
19. const runningSequences = await healthStore.readData<healthStore.exerciseSequenceHelper.running.Model>(sequenceReadRequest);
20. hilog.info(0x0000, 'testTag', 'Succeeded in reading data.');
21. runningSequences.forEach((runningSequence) => {
22. hilog.info(0x0000, 'testTag', `the start time is ${runningSequence.startTime}.`);
23. hilog.info(0x0000, 'testTag', `the end time is ${runningSequence.endTime}.`);
24. Object.keys(runningSequence.summaries).forEach((key) => {
25. Object.keys(runningSequence.summaries[key]).forEach((fieldName) => {
26. hilog.info(0x0000, 'testTag', `the summaries of ${key} field ${fieldName} is ${runningSequence.summaries[key][fieldName]}.`);
27. });
28. });
29. });
30. } catch (err) {
31. hilog.error(0x0000, 'testTag', `Failed to read data. Code: ${err.code}, message: ${err.message}`);
32. }
```

## healthStore.readData

PhoneTabletWearable

readData<T extends HealthSequence>(request: HealthSequenceReadRequest): Promise<T[]>

读取健康记录数据，使用Promise异步方式。

该接口从API 19 Release开始，支持Wearable设备开发。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| request | [HealthSequenceReadRequest](health-api-healthstore.md#healthsequencereadrequest) | 是 | 读取健康记录请求，查询时间跨度范围为31天。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<T[]> | Promise对象，T继承[HealthSequence](health-api-healthstore.md#healthsequence)，返回健康记录数组。 |

**错误码：**

以下错误码的详细介绍请参见[运动健康服务ArkTS API错误码](errorcode-healthservice.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [201](errorcode-healthservice.md#section201-鉴权失败) | Permission verification failed. |
| [401](errorcode-healthservice.md#section401-参数不合法) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;2. Incorrect parameter types; 3.Parameter verification failed. |
| [1002700001](errorcode-healthservice.md#section1002700001-系统内部错误) | System internal error. |
| [1002700002](errorcode-healthservice.md#section1002700002-数据库异常) | Database processing error. |
| [1002701001](errorcode-healthservice.md#section1002701001-网络错误) | Network error. The network is unavailable. |
| [1002702001](errorcode-healthservice.md#section1002702001-账号未登录) | Account error. The user has not logged in with HUAWEI ID. |
| [1002702002](errorcode-healthservice.md#section1002702002-账号异常) | Account error. Failed to obtain account information with HUAWEI ID. |
| [1002703001](errorcode-healthservice.md#section1002703001-用户隐私未同意) | User privacy is not agreed. |

说明

上述接口调用前，需先使用[init](health-api-healthstore.md#healthstoreinit)方法进行初始化。

**示例：**

```
1. import { healthStore } from '@kit.HealthServiceKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. let healthSequenceReadRequest: healthStore.HealthSequenceReadRequest = {
5. healthSequenceDataType: healthStore.healthSequenceHelper.sleepRecord.DATA_TYPE,
6. startTime: 1695740400000,
7. endTime: 1695769200000,
8. readOptions: {
9. withDetails: true
10. }
11. }
12. try {
13. const healthSequences = await healthStore.readData(healthSequenceReadRequest);

15. hilog.info(0x0000, 'testTag', 'Succeeded in reading data.');
16. healthSequences.forEach((healthSequence) => {
17. hilog.info(0x0000, 'testTag', `the start time is ${healthSequence.startTime}.`);
18. hilog.info(0x0000, 'testTag', `the end time is ${healthSequence.endTime}.`);
19. Object.keys(healthSequence.summaries).forEach((key) => {
20. hilog.info(0x0000, 'testTag', `the summaries of ${key} is ${healthSequence.summaries[key]}.`);
21. });
22. });
23. } catch (err) {
24. hilog.error(0x0000, 'testTag', `Failed to read data. Code: ${err.code}, message: ${err.message}`);
25. }
```

## healthStore.deleteData

PhoneTabletWearable

deleteData(request: SamplePointDeleteRequest | SamplePointDeleteRequest[]): Promise<void>

删除数据采样点，使用Promise异步方式。

**系统能力：** SystemCapability.Health.HealthStore

**设备行为差异：** 该接口在Phone、Tablet中可正常调用，在Wearable中返回1002700001错误码。

**起始版本：** 5.0.0(12)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| request | [SamplePointDeleteRequest](health-api-healthstore.md#samplepointdeleterequest) | [SamplePointDeleteRequest](health-api-healthstore.md#samplepointdeleterequest)[] | 是 | 删除数据采样点请求。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无结果返回的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[运动健康服务ArkTS API错误码](errorcode-healthservice.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [201](errorcode-healthservice.md#section201-鉴权失败) | Permission verification failed. |
| [401](errorcode-healthservice.md#section401-参数不合法) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;2. Incorrect parameter types; 3.Parameter verification failed. |
| [1002700001](errorcode-healthservice.md#section1002700001-系统内部错误) | System internal error. |
| [1002700002](errorcode-healthservice.md#section1002700002-数据库异常) | Database processing error. |
| [1002701001](errorcode-healthservice.md#section1002701001-网络错误) | Network error. The network is unavailable. |
| [1002702001](errorcode-healthservice.md#section1002702001-账号未登录) | Account error. The user has not logged in with HUAWEI ID. |
| [1002702002](errorcode-healthservice.md#section1002702002-账号异常) | Account error. Failed to obtain account information with HUAWEI ID. |
| [1002703001](errorcode-healthservice.md#section1002703001-用户隐私未同意) | User privacy is not agreed. |

说明

上述接口调用前，需先使用[init](health-api-healthstore.md#healthstoreinit)方法进行初始化。

**示例：**

```
1. import { healthStore } from '@kit.HealthServiceKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. let samplePointDeleteRequest: healthStore.SamplePointDeleteRequest = {
5. dataType: healthStore.samplePointHelper.bodyTemperature.DATA_TYPE,
6. startTime: 1698633801000,
7. endTime: 1698633801000
8. }

10. try {
11. await healthStore.deleteData(samplePointDeleteRequest);
12. hilog.info(0x0000, 'testTag', 'Succeeded in deleting data.');
13. } catch (err) {
14. hilog.error(0x0000, 'testTag', `Failed to delete data. Code: ${err.code}, message: ${err.message}`);
15. }
```

## healthStore.deleteData

PhoneTabletWearable

deleteData(request: ExerciseSequenceDeleteRequest | ExerciseSequenceDeleteRequest[]): Promise<void>

删除锻炼记录数据，使用Promise异步方式。

**系统能力：** SystemCapability.Health.HealthStore

**设备行为差异：** 该接口在Phone、Tablet中可正常调用，在Wearable中返回1002700001错误码。

**起始版本：** 5.0.0(12)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| request | [ExerciseSequenceDeleteRequest](health-api-healthstore.md#exercisesequencedeleterequest) | [ExerciseSequenceDeleteRequest](health-api-healthstore.md#exercisesequencedeleterequest)[] | 是 | 删除锻炼记录请求。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无结果返回的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[运动健康服务ArkTS API错误码](errorcode-healthservice.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [201](errorcode-healthservice.md#section201-鉴权失败) | Permission verification failed. |
| [401](errorcode-healthservice.md#section401-参数不合法) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;2. Incorrect parameter types; 3.Parameter verification failed. |
| [1002700001](errorcode-healthservice.md#section1002700001-系统内部错误) | System internal error. |
| [1002700002](errorcode-healthservice.md#section1002700002-数据库异常) | Database processing error. |
| [1002701001](errorcode-healthservice.md#section1002701001-网络错误) | Network error. The network is unavailable. |
| [1002702001](errorcode-healthservice.md#section1002702001-账号未登录) | Account error. The user has not logged in with HUAWEI ID. |
| [1002702002](errorcode-healthservice.md#section1002702002-账号异常) | Account error. Failed to obtain account information with HUAWEI ID. |
| [1002703001](errorcode-healthservice.md#section1002703001-用户隐私未同意) | User privacy is not agreed. |

说明

上述接口调用前，需先使用[init](health-api-healthstore.md#healthstoreinit)方法进行初始化。

**示例：**

```
1. import { healthStore } from '@kit.HealthServiceKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. let exerciseSequenceDeleteRequest: healthStore.ExerciseSequenceDeleteRequest= {
5. exerciseType: healthStore.exerciseSequenceHelper.running.EXERCISE_TYPE,
6. startTime: 1698633801000,
7. endTime: 1698633801000
8. }
9. try {
10. await healthStore.deleteData(exerciseSequenceDeleteRequest);
11. hilog.info(0x0000, 'testTag', 'Succeeded in deleting data.');
12. } catch (err) {
13. hilog.error(0x0000, 'testTag', `Failed to delete data. Code: ${err.code}, message: ${err.message}`);
14. }
```

## healthStore.deleteData

PhoneTabletWearable

deleteData(request: HealthSequenceDeleteRequest | HealthSequenceDeleteRequest[]): Promise<void>

删除健康记录数据，使用Promise异步方式。

**系统能力：** SystemCapability.Health.HealthStore

**设备行为差异：** 该接口在Phone、Tablet中可正常调用，在Wearable中返回1002700001错误码。

**起始版本：** 5.0.0(12)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| request | [HealthSequenceDeleteRequest](health-api-healthstore.md#healthsequencedeleterequest) | [HealthSequenceDeleteRequest](health-api-healthstore.md#healthsequencedeleterequest)[] | 是 | 删除健康记录请求。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无结果返回的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[运动健康服务ArkTS API错误码](errorcode-healthservice.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [201](errorcode-healthservice.md#section201-鉴权失败) | Permission verification failed. |
| [401](errorcode-healthservice.md#section401-参数不合法) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;2. Incorrect parameter types; 3.Parameter verification failed. |
| [1002700001](errorcode-healthservice.md#section1002700001-系统内部错误) | System internal error. |
| [1002700002](errorcode-healthservice.md#section1002700002-数据库异常) | Database processing error. |
| [1002701001](errorcode-healthservice.md#section1002701001-网络错误) | Network error. The network is unavailable. |
| [1002702001](errorcode-healthservice.md#section1002702001-账号未登录) | Account error. The user has not logged in with HUAWEI ID. |
| [1002702002](errorcode-healthservice.md#section1002702002-账号异常) | Account error. Failed to obtain account information with HUAWEI ID. |
| [1002703001](errorcode-healthservice.md#section1002703001-用户隐私未同意) | User privacy is not agreed. |

说明

上述接口调用前，需先使用[init](health-api-healthstore.md#healthstoreinit)方法进行初始化。

**示例：**

```
1. import { healthStore } from '@kit.HealthServiceKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. const healthSequenceDeleteRequest: healthStore.HealthSequenceDeleteRequest = {
5. healthSequenceDataType: healthStore.healthSequenceHelper.sleepRecord.DATA_TYPE,
6. startTime: 1695740400000,
7. endTime: 1695769200000
8. }
9. try {
10. await healthStore.deleteData(healthSequenceDeleteRequest);
11. hilog.info(0x0000, 'testTag', 'Succeeded in deleting data.');
12. } catch (err) {
13. hilog.error(0x0000, 'testTag', `Failed to delete data. Code: ${err.code}, message: ${err.message}`);
14. }
```

## healthStore.deleteData

PhoneTabletWearable

deleteData(samplePoint: SamplePoint | SamplePoint[]): Promise<void>

删除指定数据采样点，使用Promise异步方式。

**系统能力：** SystemCapability.Health.HealthStore

**设备行为差异：** 该接口在Phone、Tablet中可正常调用，在Wearable中返回1002700001错误码。

**起始版本：** 5.0.0(12)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| samplePoint | [SamplePoint](health-api-healthstore.md#samplepoint) | [SamplePoint](health-api-healthstore.md#samplepoint)[] | 是 | 单个数据采样点或数据采样点数组。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无结果返回的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[运动健康服务ArkTS API错误码](errorcode-healthservice.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [201](errorcode-healthservice.md#section201-鉴权失败) | Permission verification failed. |
| [401](errorcode-healthservice.md#section401-参数不合法) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;2. Incorrect parameter types; 3.Parameter verification failed. |
| [1002700001](errorcode-healthservice.md#section1002700001-系统内部错误) | System internal error. |
| [1002700002](errorcode-healthservice.md#section1002700002-数据库异常) | Database processing error. |
| [1002701001](errorcode-healthservice.md#section1002701001-网络错误) | Network error. The network is unavailable. |
| [1002702001](errorcode-healthservice.md#section1002702001-账号未登录) | Account error. The user has not logged in with HUAWEI ID. |
| [1002702002](errorcode-healthservice.md#section1002702002-账号异常) | Account error. Failed to obtain account information with HUAWEI ID. |
| [1002703001](errorcode-healthservice.md#section1002703001-用户隐私未同意) | User privacy is not agreed. |

说明

上述接口调用前，需先使用[init](health-api-healthstore.md#healthstoreinit)方法进行初始化。

**示例：**

```
1. import { healthStore } from '@kit.HealthServiceKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. try {
5. let samplePointReadRequest: healthStore.SamplePointReadRequest = {
6. samplePointDataType: healthStore.samplePointHelper.bodyTemperature.DATA_TYPE,
7. startTime: 1698633801000,
8. endTime: 1698633801000
9. }
10. let samplePoints: healthStore.SamplePoint[] = await healthStore.readData(samplePointReadRequest);
11. for (let index = 0; index < samplePoints.length; index++) {
12. const samplePoint = samplePoints[index];
13. await healthStore.deleteData(samplePoint);
14. }
15. hilog.info(0x0000, 'testTag', 'Succeeded in deleting data.');
16. } catch (err) {
17. hilog.error(0x0000, 'testTag', `Failed to delete data. Code: ${err.code}, message: ${err.message}`);
18. }
```

## healthStore.deleteData

PhoneTabletWearable

deleteData(exerciseSequence: ExerciseSequence | ExerciseSequence[]): Promise<void>

删除指定锻炼记录数据，使用Promise异步方式。

**系统能力：** SystemCapability.Health.HealthStore

**设备行为差异：** 该接口在Phone、Tablet中可正常调用，在Wearable中返回1002700001错误码。

**起始版本：** 5.0.0(12)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| exerciseSequence | [ExerciseSequence](health-api-healthstore.md#exercisesequence) | [ExerciseSequence](health-api-healthstore.md#exercisesequence)[] | 是 | 单个锻炼记录或锻炼记录数组。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无结果返回的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[运动健康服务ArkTS API错误码](errorcode-healthservice.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [201](errorcode-healthservice.md#section201-鉴权失败) | Permission verification failed. |
| [401](errorcode-healthservice.md#section401-参数不合法) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;2. Incorrect parameter types; 3.Parameter verification failed. |
| [1002700001](errorcode-healthservice.md#section1002700001-系统内部错误) | System internal error. |
| [1002700002](errorcode-healthservice.md#section1002700002-数据库异常) | Database processing error. |
| [1002701001](errorcode-healthservice.md#section1002701001-网络错误) | Network error. The network is unavailable. |
| [1002702001](errorcode-healthservice.md#section1002702001-账号未登录) | Account error. The user has not logged in with HUAWEI ID. |
| [1002702002](errorcode-healthservice.md#section1002702002-账号异常) | Account error. Failed to obtain account information with HUAWEI ID. |
| [1002703001](errorcode-healthservice.md#section1002703001-用户隐私未同意) | User privacy is not agreed. |

说明

上述接口调用前，需先使用[init](health-api-healthstore.md#healthstoreinit)方法进行初始化。

**示例：**

```
1. import { healthStore } from '@kit.HealthServiceKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. // 删除跑步
5. try {
6. const sequenceReadRequest: healthStore.ExerciseSequenceReadRequest<healthStore.exerciseSequenceHelper.running.DetailFields> = {
7. startTime: 1698040800000,
8. endTime: 1698042600000,
9. exerciseType: healthStore.exerciseSequenceHelper.running.EXERCISE_TYPE
10. };
11. const runningSequences = await healthStore.readData<healthStore.exerciseSequenceHelper.running.Model>(sequenceReadRequest);
12. for (let index = 0; index < runningSequences.length; index++) {
13. const runningSequence = runningSequences[index];
14. await healthStore.deleteData(runningSequence);
15. }
16. hilog.info(0x0000, 'testTag', 'Succeeded in deleting data.');
17. } catch (err) {
18. hilog.error(0x0000, 'testTag', `Failed to delete data. Code: ${err.code}, message: ${err.message}`);
19. }
```

## healthStore.deleteData

PhoneTabletWearable

deleteData(healthSequence: HealthSequence | HealthSequence[]): Promise<void>

删除指定健康记录数据，使用Promise异步方式。

**系统能力：** SystemCapability.Health.HealthStore

**设备行为差异：** 该接口在Phone、Tablet中可正常调用，在Wearable中返回1002700001错误码。

**起始版本：** 5.0.0(12)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| healthSequence | [HealthSequence](health-api-healthstore.md#healthsequence) | [HealthSequence](health-api-healthstore.md#healthsequence)[] | 是 | 单个健康记录或健康记录数组。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无结果返回的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[运动健康服务ArkTS API错误码](errorcode-healthservice.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [201](errorcode-healthservice.md#section201-鉴权失败) | Permission verification failed. |
| [401](errorcode-healthservice.md#section401-参数不合法) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;2. Incorrect parameter types; 3.Parameter verification failed. |
| [1002700001](errorcode-healthservice.md#section1002700001-系统内部错误) | System internal error. |
| [1002700002](errorcode-healthservice.md#section1002700002-数据库异常) | Database processing error. |
| [1002701001](errorcode-healthservice.md#section1002701001-网络错误) | Network error. The network is unavailable. |
| [1002702001](errorcode-healthservice.md#section1002702001-账号未登录) | Account error. The user has not logged in with HUAWEI ID. |
| [1002702002](errorcode-healthservice.md#section1002702002-账号异常) | Account error. Failed to obtain account information with HUAWEI ID. |
| [1002703001](errorcode-healthservice.md#section1002703001-用户隐私未同意) | User privacy is not agreed. |

说明

上述接口调用前，需先使用[init](health-api-healthstore.md#healthstoreinit)方法进行初始化。

**示例：**

```
1. import { healthStore } from '@kit.HealthServiceKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. try {
5. let healthSequenceReadRequest: healthStore.HealthSequenceReadRequest = {
6. healthSequenceDataType: healthStore.healthSequenceHelper.sleepRecord.DATA_TYPE,
7. startTime: 1695740400000,
8. endTime: 1695769200000
9. }
10. const healthSequences = await healthStore.readData(healthSequenceReadRequest);
11. for (let index = 0; index < healthSequences.length; index++) {
12. const healthSequence = healthSequences[index];
13. await healthStore.deleteData(healthSequence);
14. }
15. hilog.info(0x0000, 'testTag', 'Succeeded in deleting data.');
16. } catch (err) {
17. hilog.error(0x0000, 'testTag', `Failed to delete data. Code: ${err.code}, message: ${err.message}`);
18. }
```

## healthStore.aggregateData

PhoneTabletWearable

aggregateData<T extends AggregateResult>(request: AggregateRequest | AggregateRequest[]): Promise<T[]>

聚合查询，使用Promise异步方式。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Health.HealthStore

**设备行为差异：** 该接口在Phone、Tablet中可正常调用，在Wearable中返回1002700001错误码。

**起始版本：** 5.0.0(12)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| request | [AggregateRequest](health-api-healthstore.md#aggregaterequest) | [AggregateRequest](health-api-healthstore.md#aggregaterequest)[] | 是 | 聚合统计查询请求。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<T[]> | Promise对象，T继承[AggregateResult](health-api-healthstore.md#aggregateresult)，返回聚合查询结果数组。 |

**错误码：**

以下错误码的详细介绍请参见[运动健康服务ArkTS API错误码](errorcode-healthservice.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [201](errorcode-healthservice.md#section201-鉴权失败) | Permission verification failed. |
| [401](errorcode-healthservice.md#section401-参数不合法) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;2. Incorrect parameter types; 3.Parameter verification failed. |
| [1002700001](errorcode-healthservice.md#section1002700001-系统内部错误) | System internal error. |
| [1002700002](errorcode-healthservice.md#section1002700002-数据库异常) | Database processing error. |
| [1002701001](errorcode-healthservice.md#section1002701001-网络错误) | Network error. The network is unavailable. |
| [1002702001](errorcode-healthservice.md#section1002702001-账号未登录) | Account error. The user has not logged in with HUAWEI ID. |
| [1002702002](errorcode-healthservice.md#section1002702002-账号异常) | Account error. Failed to obtain account information with HUAWEI ID. |
| [1002703001](errorcode-healthservice.md#section1002703001-用户隐私未同意) | User privacy is not agreed. |

说明

上述接口调用前，需先使用[init](health-api-healthstore.md#healthstoreinit)方法进行初始化。

**示例：**

```
1. import { healthStore } from '@kit.HealthServiceKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. let aggregateRequest: healthStore.AggregateRequest<healthStore.samplePointHelper.dailyActivities.AggregateFields> = {
5. dataType: healthStore.samplePointHelper.dailyActivities.DATA_TYPE,
6. metrics: {
7. step: ['sum'],
8. calorie: ['sum'],
9. distance: ['sum'],
10. climbHighAltitude:['sum'],
11. isIntensity: ['sum'],
12. isStand: ['sum']
13. },
14. groupBy: {
15. unitType: 3,
16. duration: 0
17. },
18. startLocalDate: '10/30/2023',
19. endLocalDate: '10/30/2023'
20. }

22. try {
23. const aggregateResults = await healthStore.aggregateData<healthStore.samplePointHelper.dailyActivities.AggregateResult>(aggregateRequest);

25. hilog.info(0x0000, 'testTag', 'Succeeded in reading data.');
26. aggregateResults.forEach((aggregateResult) => {
27. hilog.info(0x0000, 'testTag', `the start time is ${aggregateResult.startTime}.`);
28. hilog.info(0x0000, 'testTag', `the end time is ${aggregateResult.endTime}.`);
29. Object.keys(aggregateResult.fields).forEach((fieldName) => {
30. hilog.info(0x0000, 'testTag', `the sum of ${fieldName} is ${aggregateResult.fields[fieldName].sum}.`);
31. });
32. });
33. } catch (err) {
34. hilog.error(0x0000, 'testTag', `Failed to read data. Code: ${err.code}, message: ${err.message}`);
35. }
```

## healthStore.requestAuthorizations

PhoneTabletWearable

requestAuthorizations(context: common.UIAbilityContext, request: AuthorizationRequest): Promise<AuthorizationResponse>

用户授权，使用Promise异步方式。

该接口从API 19 Release开始，支持Wearable设备开发。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| context | [common.UIAbilityContext](js-apis-inner-application-uiabilitycontext.md#uiabilitycontext-1) | 是 | UIAbility上下文。 |
| request | [AuthorizationRequest](health-api-healthstore.md#authorizationrequest) | 是 | 授权请求参数，确保授权参数中的权限已在申请运动健康服务时勾选。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[AuthorizationResponse](health-api-healthstore.md#authorizationresponse)> | Promise对象，返回授权响应结果。 |

**错误码：**

以下错误码的详细介绍请参见[运动健康服务ArkTS API错误码](errorcode-healthservice.md)，其他错误码请参见[华为账号服务ArkTS错误码](account-api-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [201](errorcode-healthservice.md#section201-鉴权失败) | Permission verification failed. |
| [401](errorcode-healthservice.md#section401-参数不合法) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;2. Incorrect parameter types; 3.Parameter verification failed. |

说明

上述接口调用前，需先使用[init](health-api-healthstore.md#healthstoreinit)方法进行初始化。

**示例：**

```
1. import { healthStore } from '@kit.HealthServiceKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { common } from '@kit.AbilityKit';

5. let authorizationParameter: healthStore.AuthorizationRequest = {
6. readDataTypes: [healthStore.exerciseSequenceHelper.DATA_TYPE, healthStore.samplePointHelper.heartRate.DATA_TYPE],
7. writeDataTypes: [healthStore.exerciseSequenceHelper.DATA_TYPE, healthStore.samplePointHelper.heartRate.DATA_TYPE]
8. }

10. try {
11. // 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext
12. let authorizationResponse = await healthStore.requestAuthorizations(this.getUIContext().getHostContext() as common.UIAbilityContext, authorizationParameter);

14. hilog.info(0x0000, 'testTag', 'Succeeded in requesting authorization.');
15. authorizationResponse.writeDataTypes.forEach(dataType => {
16. hilog.info(0x0000, 'testTag', `grantedWriteDataType is : ${dataType.name}`);
17. });
18. authorizationResponse.readDataTypes.forEach(dataType => {
19. hilog.info(0x0000, 'testTag', `grantedReadDataTypes is : ${dataType.name}`);
20. });
21. } catch (err) {
22. hilog.error(0x0000, 'testTag', `Failed to request authorization. Code: ${err.code}, message: ${err.message}`);
23. }
```

## healthStore.getAuthorizations

PhoneTabletWearable

getAuthorizations(request: AuthorizationRequest): Promise<AuthorizationResponse>

查询权限，使用Promise异步方式。

该接口从API 19 Release开始，支持Wearable设备开发。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| request | [AuthorizationRequest](health-api-healthstore.md#authorizationrequest) | 是 | 查询权限请求参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[AuthorizationResponse](health-api-healthstore.md#authorizationresponse)> | Promise对象，返回查询权限结果。 |

**错误码：**

以下错误码的详细介绍请参见[运动健康服务ArkTS API错误码](errorcode-healthservice.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [201](errorcode-healthservice.md#section201-鉴权失败) | Permission verification failed. |
| [401](errorcode-healthservice.md#section401-参数不合法) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;2. Incorrect parameter types; 3.Parameter verification failed. |
| [1002701001](errorcode-healthservice.md#section1002701001-网络错误) | Network error. The network is unavailable. |
| [1002702001](errorcode-healthservice.md#section1002702001-账号未登录) | Account error. The user has not logged in with HUAWEI ID. |
| [1002702002](errorcode-healthservice.md#section1002702002-账号异常) | Account error. Failed to obtain account information with HUAWEI ID. |

说明

上述接口调用前，需先使用[init](health-api-healthstore.md#healthstoreinit)方法进行初始化。

**示例：**

```
1. import { healthStore } from '@kit.HealthServiceKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. let queryAuthorizationRequest: healthStore.AuthorizationRequest = {
5. readDataTypes: [healthStore.exerciseSequenceHelper.DATA_TYPE, healthStore.samplePointHelper.heartRate.DATA_TYPE],
6. writeDataTypes: [healthStore.exerciseSequenceHelper.DATA_TYPE, healthStore.samplePointHelper.heartRate.DATA_TYPE]
7. }

9. try {
10. let queryAuthorizationResponse = await healthStore.getAuthorizations(queryAuthorizationRequest);

12. hilog.info(0x0000, 'testTag', 'Succeeded in getting authorization.');
13. queryAuthorizationResponse.writeDataTypes.forEach(dataType => {
14. hilog.info(0x0000, 'testTag', `grantedWriteDataType is : ${dataType.name}`);
15. });
16. queryAuthorizationResponse.readDataTypes.forEach(dataType => {
17. hilog.info(0x0000, 'testTag', `grantedReadDataTypes is : ${dataType.name}`);
18. });
19. } catch (err) {
20. hilog.error(0x0000, 'testTag', `Failed to get authorization. Code: ${err.code}, message: ${err.message}`);
21. }
```

## healthStore.cancelAuthorizations

PhoneTabletWearable

cancelAuthorizations(): Promise<void>

用户取消授权，使用Promise异步方式。

该接口从API 19 Release开始，支持Wearable设备开发。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无结果返回的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[运动健康服务ArkTS API错误码](errorcode-healthservice.md)，其他错误码请参见[华为账号服务ArkTS错误码](account-api-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [201](errorcode-healthservice.md#section201-鉴权失败) | Permission verification failed. |

说明

上述接口调用前，需先使用[init](health-api-healthstore.md#healthstoreinit)方法进行初始化。

**示例：**

```
1. import { healthStore } from '@kit.HealthServiceKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. try {
5. await healthStore.cancelAuthorizations();
6. hilog.info(0x0000, 'testTag', 'Succeeded in canceling authorization.');
7. } catch (err) {
8. hilog.error(0x0000, 'testTag', `Failed to cancel authorization. Code: ${err.code}, message: ${err.message}`);
9. }
```

## healthStore.syncAll

PhoneTabletWearable

syncAll(): Promise<void>

用户主动触发数据同步，使用Promise异步方式。

**系统能力：** SystemCapability.Health.HealthStore

**设备行为差异：** 该接口在Phone、Tablet中可正常调用，在Wearable中返回801错误码。

**起始版本：** 5.1.0(18)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无结果返回的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[运动健康服务ArkTS API错误码](errorcode-healthservice.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [201](errorcode-healthservice.md#section201-鉴权失败) | Permission verification failed. |
| [801](errorcode-healthservice.md#section801-该设备不支持此api) | Capability not supported. Failed to call the API due to limited device capabilities. |
| [1002700001](errorcode-healthservice.md#section1002700001-系统内部错误) | System internal error. |
| [1002700002](errorcode-healthservice.md#section1002700002-数据库异常) | Database processing error. |
| [1002701001](errorcode-healthservice.md#section1002701001-网络错误) | Network error. The network is unavailable. |
| [1002702001](errorcode-healthservice.md#section1002702001-账号未登录) | Account error. The user has not logged in with HUAWEI ID. |
| [1002702002](errorcode-healthservice.md#section1002702002-账号异常) | Account error. Failed to obtain account information with HUAWEI ID. |
| [1002703001](errorcode-healthservice.md#section1002703001-用户隐私未同意) | User privacy is not agreed. |

说明

上述接口调用前，需先使用[init](health-api-healthstore.md#healthstoreinit)方法进行初始化。

**示例：**

```
1. import { healthStore } from '@kit.HealthServiceKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. try {
5. await healthStore.syncAll();
6. hilog.info(0x0000, 'testTag', 'Succeeded in synchronizing data.');
7. } catch (err) {
8. hilog.error(0x0000, 'testTag', `Failed to synchronize data. Code: ${err.code}, message: ${err.message}`);
9. }
```

## healthStore.on('serviceDie')

PhoneTabletWearable

on(type: 'serviceDie', callback: Callback<void>): void

订阅Health Service Kit进程销毁通知，使用Callback异步回调。

该接口从API 19 Release开始，支持Wearable设备开发。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.1.0(18)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| type | string | 是 | Health Service Kit进程状态的回调类型，支持的事件为：'serviceDie'，当Health Service Kit进程销毁时，触发该事件。 |
| callback | Callback<void> | 是 | 无返回结果的回调函数。 |

说明

上述接口调用前，需先使用[init](health-api-healthstore.md#healthstoreinit)方法进行初始化。

**示例：**

```
1. import { healthStore } from '@kit.HealthServiceKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. healthStore.on('serviceDie', () => {
5. hilog.info(0x0000, 'testTag', 'Succeeded in monitoring the process death.');
6. });
```

## healthStore.off('serviceDie')

PhoneTabletWearable

off(type: 'serviceDie', callback?: Callback<void>): void

取消订阅Health Service Kit进程销毁通知，使用Callback异步回调。

该接口从API 19 Release开始，支持Wearable设备开发。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.1.0(18)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| type | string | 是 | Health Service Kit进程状态的回调类型，支持的事件为：'serviceDie'，当Health Service Kit进程销毁时，触发该事件。 |
| callback | Callback<void> | 否 | 无返回结果的回调函数。  - callback为空：取消所有callback回调。  - callback非空：取消指定的callback回调。 |

说明

上述接口调用前，需先使用[init](health-api-healthstore.md#healthstoreinit)方法进行初始化。

**示例：**

```
1. import { healthStore } from '@kit.HealthServiceKit';

3. healthStore.off('serviceDie');
```
