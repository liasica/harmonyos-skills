---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/health-api-healthfields-lite
title: healthFields (运动健康数据字段)(Lite)
breadcrumb: API参考 > 应用服务 > Health Service Kit（运动健康服务） > ArkTS API > 运动健康数据类型常量及模型定义 > healthFields (运动健康数据字段)(Lite)
category: harmonyos-references
scraped_at: 2026-11-12T09:57:20+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:20117d96c77cce0f603e1310575192e6a3f8925369c80cc2844e5b34d9403ab1
---

本模块提供运动健康数据字段列表。

**起始版本：** 6.1.1(24)

## 导入模块

```javascript
import healthStore from '@hms.health.store';
```

**说明** 

此模块为healthStore子模块，需通过healthStore.healthFields方式使用。

## Altitude

海拔详情数据字段列表，继承[healthStore.SequencePoint](health-api-healthstore-lite.md#sequencepoint)。

**系统能力：** SystemCapability.Health.HealthStore.Lite

**起始版本：** 6.1.1(24)

**模型约束：** 此接口仅可在FA模型下使用。

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| altitude | number | 否 | 否 | 海拔。  单位：m |

## ExerciseHeartRate

运动心率详情数据字段列表，继承[healthStore.SequencePoint](health-api-healthstore-lite.md#sequencepoint)。

**系统能力：** SystemCapability.Health.HealthStore.Lite

**起始版本：** 6.1.1(24)

**模型约束：** 此接口仅可在FA模型下使用。

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| bpm | number | 否 | 否 | 运动心率详情。  单位：次/分钟  取值范围：(0, 255) |

## Speed

速度详情数据字段列表，继承[healthStore.SequencePoint](health-api-healthstore-lite.md#sequencepoint)。

**系统能力：** SystemCapability.Health.HealthStore.Lite

**起始版本：** 6.1.1(24)

**模型约束：** 此接口仅可在FA模型下使用。

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| speed | number | 否 | 否 | 速度详情。  单位：米/秒  取值范围：[0, ∞) |

## QuantitySummary

统计基类数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore.Lite

**起始版本：** 26.0.1

**模型约束：** 此接口仅可在FA模型下使用。

| **名称** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| avg | number | 是 | 平均值，取值范围：[0, ∞)。 |
| max | number | 是 | 最大值，取值范围：[0, ∞)。 |
| min | number | 否 | 最小值，默认值：0，取值范围：[0, ∞)。 |

## ExerciseHeartRateSummary

type ExerciseHeartRateSummary = QuantitySummary

运动心率统计数据字段列表，继承自QuantitySummary基础类型。

**系统能力：** SystemCapability.Health.HealthStore.Lite

**起始版本：** 26.0.1

**模型约束：** 此接口仅可在FA模型下使用。

| **类型** | **说明** |
| --- | --- |
| [QuantitySummary](health-api-healthfields-lite.md#quantitysummary) | 统计基类数据字段列表。 |

## HeartRateZonesSummary

心率区间统计数据字段数据列表。

**系统能力：** SystemCapability.Health.HealthStore.Lite

**起始版本：** 26.0.1

**模型约束：** 此接口仅可在FA模型下使用。

| **名称** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| heartRateZones | number | 是 | 心率区间统计值，取值范围：[0,2]。  0为最大心率区间，1为储备心率区间，2为乳酸阈心率区间。 |

## SkiDurationSummary

滑雪时长统计数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore.Lite

**起始版本：** 26.0.1

**模型约束：** 此接口仅可在FA模型下使用。

| **名称** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| skiDuration | number | 是 | 滑雪时长，单位：s。 |

## TrainingLoadSummary

训练负荷数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore.Lite

**起始版本：** 26.0.1

**模型约束：** 此接口仅可在FA模型下使用。

| **名称** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| trainingLoad | number | 是 | 有氧训练负荷和有氧训练负荷的总和。 |
| aerobic | number | 是 | 有氧训练负荷。 |
| anaerobic | number | 是 | 无氧训练负荷。 |

## TrainingStressSummary

训练压力统计数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore.Lite

**起始版本：** 26.0.1

**模型约束：** 此接口仅可在FA模型下使用。

| **名称** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| aerobic | number | 是 | 有氧训练压力。 |
| anaerobic | number | 是 | 无氧训练压力。 |

## CalorieSummary

热量统计数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore.Lite

**起始版本：** 26.0.1

**模型约束：** 此接口仅可在FA模型下使用。

| **名称** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| totalCalories | number | 是 | 运动消耗总热量，包含基础代谢和活动那个消耗，单位：cal，取值范围：(0, ∞)。 |
| activeCalories | number | 否 | 运动主动消耗的热量，单位：cal，取值范围：(0, ∞)。 |

## DistanceSummary

距离统计数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore.Lite

**起始版本：** 26.0.1

**模型约束：** 此接口仅可在FA模型下使用。

| **名称** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| totalDistance | number | 是 | 总距离，单位：m，取值范围：(0, ∞)。 |

## AltitudeSummary

海拔统计数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore.Lite

**起始版本：** 26.0.1

**模型约束：** 此接口仅可在FA模型下使用。

| **名称** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| max | number | 是 | 最高海拔，单位：m。 |
| min | number | 是 | 最低海拔，单位：m。 |
| avg | number | 否 | 平均海拔，单位：m。 |
| totalAscent | number | 否 | 累计上升的海拔，单位：m，取值范围：[0, ∞)。 |
| totalDescent | number | 否 | 累计下降的海拔，单位：m，取值范围：[0, ∞)。 |

## SkiSpeedSummary

type SkiSpeedSummary = Omit<QuantitySummary, 'min'>

滑雪速度统计数据字段列表，继承自统计基类数据字段列表中min以外字段。

**系统能力：** SystemCapability.Health.HealthStore.Lite

**起始版本：** 26.0.1

**模型约束：** 此接口仅可在FA模型下使用。

| **类型** | **说明** |
| --- | --- |
| Omit<[QuantitySummary](health-api-healthfields-lite.md#quantitysummary), 'min'> | 统计基类数据字段列表min以外字段。 |

## SpeedSummary

type SpeedSummary = QuantitySummary

速度统计数据字段列表，继承自QuantitySummary基础类型。

**系统能力：** SystemCapability.Health.HealthStore.Lite

**起始版本：** 26.0.1

**模型约束：** 此接口仅可在FA模型下使用。

| **类型** | **说明** |
| --- | --- |
| [QuantitySummary](health-api-healthfields-lite.md#quantitysummary) | 统计基类数据字段列表。 |

## CadenceSummary

type CadenceSummary = QuantitySummary

步频统计数据字段列表，继承自QuantitySummary基础类型。

**系统能力：** SystemCapability.Health.HealthStore.Lite

**起始版本：** 26.0.1

**模型约束：** 此接口仅可在FA模型下使用。

| **类型** | **说明** |
| --- | --- |
| [QuantitySummary](health-api-healthfields-lite.md#quantitysummary) | 统计基类数据字段列表。 |

## AnalogPowerSummary

type AnalogPowerSummary = Omit<QuantitySummary, 'max'>

模拟功率统计数据字段列表，继承自统计基类数据字段列表中min以外字段。

**系统能力：** SystemCapability.Health.HealthStore.Lite

**起始版本：** 26.0.1

**模型约束：** 此接口仅可在FA模型下使用。

| **类型** | **说明** |
| --- | --- |
| Omit<[QuantitySummary](health-api-healthfields-lite.md#quantitysummary), 'max'> | 统计基类数据字段列表max以外字段。 |

## RunPaceZoneSummary

配速区间统计数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore.Lite

**起始版本：** 26.0.1

**模型约束：** 此接口仅可在FA模型下使用。

| **名称** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| runPaceZoneConfig | string | 是 | 配速区间值。 |
| runPaceZoneStatistics | string | 是 | 配速区间统计时长。 |

## RunningFormSummary

跑姿统计数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore.Lite

**起始版本：** 26.0.1

**模型约束：** 此接口仅可在FA模型下使用。

| **名称** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| avgGroundContactTime | number | 是 | 平均触地时间，单位：ms，取值范围：[0, 5000]。 |
| avgVerticalOscillation | number | 否 | 平均垂直振幅，单位：cm，默认值：0。 |
| avgGcTimeBalance | number | 否 | 平均左右触地平衡，单位：%（返回数据为左脚的触地平衡，右脚需自行计算，二者之和为100%），默认值：0。 |

## StepSummary

步数统计数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore.Lite

**起始版本：** 26.0.1

**模型约束：** 此接口仅可在FA模型下使用。

| **名称** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| totalSteps | number | 是 | 总步数。 |

## TurnsSummary

转弯统计数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore.Lite

**起始版本：** 26.0.1

**模型约束：** 此接口仅可在FA模型下使用。

| **名称** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| totalTurnNumber | number | 是 | 总转弯次数，取值范围：[0,9999]。 |
| longRadiusTurn | number | 是 | 中长弯次数，取值范围：[0,9999]。 |
| shortRadiusTurn | number | 是 | 短弯次数，取值范围：[0,9999]。 |
| turnFrequency | number | 否 | 平均转弯频率，单位：次/分钟，取值范围：[0,200]。 |
| leftTurnCount | number | 否 | 左转次数，取值范围：[0,9999]。 |
| rightTurnCount | number | 否 | 右转次数，取值范围：[0,9999]。 |

## TemperatureSummary

温度统计数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore.Lite

**起始版本：** 26.0.1

**模型约束：** 此接口仅可在FA模型下使用。

| **名称** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| temperature | number | 是 | 温度，单位：℃。 |

## SkiPisteRegionSummary

雪道区域统计数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore.Lite

**起始版本：** 26.0.1

**模型约束：** 此接口仅可在FA模型下使用。

| **名称** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| skiPisteRegion | number | 是 | 雪道所属的地区，取值范围：[0,3]。  0代表无效，1代表欧洲，2代表日本，3代表北美。 |

## RunwayRatioSummary

雪道占比统计数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore.Lite

**起始版本：** 26.0.1

**模型约束：** 此接口仅可在FA模型下使用。

| **名称** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| novice | number | 是 | 新手道占比，取值范围：[1,100]。 |
| beginner | number | 是 | 初级道占比，取值范围：[1,100]。 |
| intermediate | number | 是 | 中级道占比，取值范围：[1,100]。 |
| advanced | number | 是 | 高级道占比，取值范围：[1,100]。 |

## SkiTechStatsSummary

滑雪技术统计数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore.Lite

**起始版本：** 26.0.1

**模型约束：** 此接口仅可在FA模型下使用。

| **名称** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| falls | number | 是 | 摔倒次数，取值范围：[0,9999]。 |
| skidding | number | 是 | 搓雪次数，取值范围：[0,100]。 |
| skiddingRatio | number | 是 | 搓雪占比，取值范围：[0,100]。 |
| steering | number | 是 | 走刃次数，取值范围：[0,9999]。 |
| steeringRatio | number | 是 | 走刃占比，取值范围：[0,100]。 |
| carving | number | 是 | 卡宾次数，取值范围：[0,9999]。 |
| carvingRatio | number | 是 | 卡宾占比，取值范围：[0,100]。 |
| turnRoundness | number | 是 | 弯形圆润度，取值范围：[0,100]。 |
| turnSymmetry | number | 是 | 弯形对称度，取值范围：[0,100]。 |
| averageParallelism | number | 是 | 平均平行率，取值范围：[0,100]。 |
| averageEdgingSync | number | 是 | 平均立刃同步率，取值范围：[0,100]。 |
| averageEdgeAngle | number | 是 | 平均立刃，单位：°，取值范围：[0,90]。 |
| maxEdgeAngle | number | 是 | 最大立刃，单位：°，取值范围：[0,90]。 |
| earlyMovementIndex | number | 是 | 提前移动指数，取值范围：[0,100]。 |
| earlyWeightTransfer | number | 是 | 提前重心变化，取值范围：[0,100]。 |
| earlyEdging | number | 是 | 提前立刃启动动作在整个转弯周期中所占的时间比例，取值范围：[0,100]。 |
| progressiveEdging | number | 是 | 渐进式立刃，单位：°/s，取值范围：[0,100]。 |
| outsideSkiPressureIndex | number | 是 | 外侧压感指数，单位：kg，取值范围：[0,100]。 |
| pressureSmoothnessIndex | number | 是 | 压力平滑指数，取值范围：[0,100]。 |

## InclineSummary

坡度统计数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore.Lite

**起始版本：** 26.0.1

**模型约束：** 此接口仅可在FA模型下使用。

| **名称** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| maxSlopePercent | number | 是 | 最大坡度，单位：%。 |
| minSlopePercent | number | 否 | 最小坡度，单位：%。 |
| maxSlopeDegree | number | 是 | 最大坡度，单位：°。 |
| avgSlopeDegree | number | 是 | 平均坡度，单位：°。 |
| avgUphillSlope | number | 是 | 平均上坡坡度，单位：%。 |
| avgDownhillSlope | number | 是 | 平均下坡坡度，单位：%。 |

## GForceSummary

type GForceSummary = Omit<QuantitySummary, 'min'>

G-Force统计数据字段列表，继承自统计基类数据字段列表中min以外字段。

**系统能力：** SystemCapability.Health.HealthStore.Lite

**起始版本：** 26.0.1

**模型约束：** 此接口仅可在FA模型下使用。

| **类型** | **说明** |
| --- | --- |
| Omit<[QuantitySummary](health-api-healthfields-lite.md#quantitysummary), 'min'> | 统计基类数据字段列表min以外字段。 |

## SkiTripTimeSummary

滑雪趟数统计数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore.Lite

**起始版本：** 26.0.1

**模型约束：** 此接口仅可在FA模型下使用。

| **名称** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| tripTimes | number | 是 | 滑雪总趟数。 |

## SwingSpeedSummary

type SwingSpeedSummary = Omit<QuantitySummary, 'min'>

挥拍速度统计数据字段列表，继承自统计基类数据字段列表中min以外字段。

**系统能力：** SystemCapability.Health.HealthStore.Lite

**起始版本：** 26.0.1

**模型约束：** 此接口仅可在FA模型下使用。

| **类型** | **说明** |
| --- | --- |
| Omit<[QuantitySummary](health-api-healthfields-lite.md#quantitysummary), 'min'> | 统计基类数据字段列表min以外字段。 |

## ServeSummary

发球统计数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore.Lite

**起始版本：** 26.0.1

**模型约束：** 此接口仅可在FA模型下使用。

| **名称** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| serve | number | 是 | 发球次数，取值范围：[0,10000]。 |

## PadelFeature

笼式网球特性统计数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore.Lite

**起始版本：** 26.0.1

**模型约束：** 此接口仅可在FA模型下使用。

| **名称** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| bandeja | number | 是 | 班德哈次数，取值范围：[0,10000]。 |
| vibora | number | 是 | 维博拉次数，取值范围：[0,10000]。 |
| forehandShot | number | 是 | 正手击球次数，取值范围：[0,10000]。 |
| forehandSmash | number | 是 | 正手高压球次数，取值范围：[0,10000]。 |
| forehandDrop | number | 是 | 正手吊小球次数，取值范围：[0,10000]。 |
| forehandBajada | number | 是 | 正手巴哈达次数，取值范围：[0,10000]。 |
| forehandDrive | number | 是 | 正手抽球次数，取值范围：[0,10000]。 |
| forehandBackspin | number | 是 | 正手下旋球次数，取值范围：[0,10000]。 |
| forehandVolley | number | 是 | 正手截击次数，取值范围：[0,10000]。 |
| backhandShot | number | 是 | 反手击球次数，取值范围：[0,10000]。 |
| backhandSmash | number | 是 | 反手高压球次数，取值范围：[0,10000]。 |
| backhandBajada | number | 是 | 反手巴哈达次数，取值范围：[0,10000]。 |
| backhandDrop | number | 是 | 反手吊小球次数，取值范围：[0,10000]。 |
| backhandDrive | number | 是 | 反手抽球次数，取值范围：[0,10000]。 |
| backhandBackspin | number | 是 | 反手下旋球次数，取值范围：[0,10000]。 |
| backhandVolley | number | 是 | 反手截击次数，取值范围：[0,10000]。 |

## RecoveryTimeSummary

恢复时间统计数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore.Lite

**起始版本：** 26.0.1

**模型约束：** 此接口仅可在FA模型下使用。

| **名称** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| recoveryTime | number | 是 | 恢复时间，单位：min。 |

## TechStatsSummary

技术数据统计数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore.Lite

**起始版本：** 26.0.1

**模型约束：** 此接口仅可在FA模型下使用。

| **名称** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| swingTimes | number | 是 | 挥拍次数，取值范围：[0,20000]。 |
| maxContinuousRally | number | 是 | 最长连拍次数，取值范围：[0,10000]。 |
| movementDistance | number | 是 | 移动距离，单位：m，取值范围：[0,99999]。 |

## ScoreStatsSummary

分数数据统计数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore.Lite

**起始版本：** 26.0.1

**模型约束：** 此接口仅可在FA模型下使用。

| **名称** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| setsWon | number | 是 | 获胜盘数，取值范围：[0,256]。 |
| totalSets | number | 是 | 总盘数，取值范围：[0,256]。 |

## GroupSummary

力量训练组数详情数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore.Lite

**起始版本：** 6.1.1(24)

**模型约束：** 此接口仅可在FA模型下使用。

| **名称** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| trainingWeight | number[] | 是 | 训练重量，数组长度最大为10。 |
| groupCount | number[] | 是 | 训练组数，数组长度最大为10。 |
| groupTime | number[] | 是 | 每组训练用时，数组长度最大为10。 |

## ActionSummary

力量训练动作详情数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore.Lite

**起始版本：** 6.1.1(24)

**模型约束：** 此接口仅可在FA模型下使用。

| **名称** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| actionName | string | 是 | 动作名称，长度不能超过50个字节。 |
| groupRestingTime | number | 是 | 组间休息时间。 |
| actionTimes | number | 否 | 当前训练动作组数，默认值为0，取值范围[0,10]。 |
| trainingVolume | number | 否 | 总训练重量，默认值为0。 |
| weightUnit | 'kg' | 'lbs' | 否 | 训练重量单位，默认为'kg'。 |
| groups | [GroupSummary](health-api-healthfields-lite.md#groupsummary)[] | 是 | 训练组数详情。 |

## BadmintonDetail

羽毛球详情数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore.Lite

**起始版本：** 6.1.1(24)

**模型约束：** 此接口仅可在FA模型下使用。

| **名称** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| exerciseHeartRate | [ExerciseHeartRate](health-api-healthfields-lite.md#exerciseheartrate)[] | 否 | 运动心率详情列表，若未填写，默认为空。 |

## BadmintonSummary

羽毛球统计数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore.Lite

**起始版本：** 6.1.1(24)

**模型约束：** 此接口仅可在FA模型下使用。

| **名称** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| startTime | number | 是 | 运动开始时间，Unix时间戳，单位：ms。 |
| totalTime | number | 是 | 运动总时长，单位：s。 |
| targetDuration | number | 否 | 目标运动时长，单位：s，默认值：0。 |
| avgHeartRate | number | 否 | 运动全程平均心率，单位：bpm，默认值：0。 |
| maxHeartRate | number | 否 | 运动过程最高心率，单位：bpm，默认值：0。 |
| mHeartrateZoneType | number | 否 | 心率区间类型，0为最大心率区间，1为储备心率区间，默认值：0。 |
| startHeartRate | number | 否 | 恢复心率测量初始时的心率，单位：bpm，默认值：0。 |
| endHeartRate | number | 否 | 恢复心率测量结束时的心率，单位：bpm，默认值：0。 |
| loadPeakLevel | number | 否 | 运动负荷峰值等级，等级越大运动效果越好，默认值：0。 |
| aerobicTrainingStress | number | 否 | 有氧训练压力值，量化有氧运动负荷程度，取值范围：[0.0, 5.0]，默认值：0。 |
| anaerobicTrainingStress | number | 否 | 无氧训练压力值，量化无氧运动负荷程度，取值范围：[0.0, 5.0]，默认值：0。 |
| recoveryTime | number | 否 | 预估恢复时间，单位：h，默认值：0。 |
| totalCalories | number | 是 | 运动消耗总热量，包含基础代谢与活动消耗，单位：cal，取值范围：(0, ∞)。 |
| activeCalorie | number | 是 | 运动主动消耗的热量，不含基础代谢，单位：cal，取值范围：(0, ∞)。 |
| avgShotSpeed | number | 否 | 平均击球速度，单位：km/h，取值范围：[0,500]，默认值：0。 |
| maxShotSpeed | number | 否 | 最高击球速度，单位：km/h，取值范围：[0,500]，默认值：0。 |
| shots | number | 否 | 总击球次数，取值范围：[0,20000]，默认值：0。 |
| maxContinuousRally | number | 否 | 最长连续对打回合数，取值范围：[0,10000]，默认值：0。 |
| forehandStroke | number | 否 | 正手击球次数，取值范围：[0,10000]，默认值：0。 |
| backhandStroke | number | 否 | 反手击球次数，取值范围：[0,10000]，默认值：0。 |
| overhandStroke | number | 否 | 上手击球次数，如发球、扣杀准备动作，取值范围：[0,10000]，默认值：0。 |
| underhandStroke | number | 否 | 下手击球次数，如挑球、切球，取值范围：[0,10000]，默认值：0。 |
| smash | number | 否 | 扣杀次数，取值范围：[0,10000]，默认值：0。 |
| highClear | number | 否 | 高远球次数，取值范围：[0,10000]，默认值：0。 |

## SoccerDetail

足球详情数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore.Lite

**起始版本：** 6.1.1(24)

**模型约束：** 此接口仅可在FA模型下使用。

| **名称** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| exerciseHeartRate | [ExerciseHeartRate](health-api-healthfields-lite.md#exerciseheartrate)[] | 否 | 运动心率详情列表，若未填写，默认为空。 |

## SoccerSummary

足球统计数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore.Lite

**起始版本：** 6.1.1(24)

**模型约束：** 此接口仅可在FA模型下使用。

| **名称** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| startTime | number | 是 | 运动开始时间，Unix时间戳，单位：ms。 |
| totalTime | number | 是 | 运动总时长，单位：s。 |
| targetDuration | number | 否 | 目标运动时长，单位：s，默认值：0。 |
| avgHeartRate | number | 否 | 运动全程平均心率，单位：bpm，默认值：0。 |
| maxHeartRate | number | 否 | 运动过程最高心率，单位：bpm，默认值：0。 |
| mHeartrateZoneType | number | 否 | 心率区间类型，0为最大心率区间，1为储备心率区间，默认值：0。 |
| startHeartRate | number | 否 | 恢复心率测量初始时的心率，单位：bpm，默认值：0。 |
| endHeartRate | number | 否 | 恢复心率测量结束时的心率，单位：bpm，默认值：0。 |
| loadPeakLevel | number | 否 | 运动负荷峰值等级，等级越大运动效果越好，默认值：0。 |
| aerobicTrainingStress | number | 否 | 有氧训练压力值，量化有氧运动负荷程度，取值范围：[0.0, 5.0]，默认值：0。 |
| anaerobicTrainingStress | number | 否 | 无氧训练压力值，量化无氧运动负荷程度，取值范围：[0.0, 5.0]，默认值：0。 |
| recoveryTime | number | 否 | 预估恢复时间，单位：h，默认值：0。 |
| totalCalories | number | 是 | 运动消耗总热量，包含基础代谢与活动消耗，单位：cal，取值范围：(0, ∞)。 |
| activeCalorie | number | 是 | 运动主动消耗的热量，不含基础代谢，单位：cal，取值范围：(0, ∞)。 |
| goalsTimes | number | 否 | 进球次数，取值范围：[0,10000]，默认值：0。 |
| assistsTimes | number | 否 | 助攻次数，取值范围：[0,10000]，默认值：0。 |
| savesTimes | number | 否 | 扑救次数，取值范围：[0,10000]，默认值：0。  **起始版本：** 26.0.1 |
| jumpTimes | number | 否 | 跳跃次数，取值范围：[0,10000]，默认值：0。  **起始版本：** 26.0.1 |
| sprintTimes | number | 否 | 冲刺次数，取值范围：[0,10000]，默认值：0。  **起始版本：** 26.0.1 |
| turnSpeedUpTimes | number | 否 | 转身加速次数，取值范围：[0,10000]，默认值：0。  **起始版本：** 26.0.1 |
| swerveSpeedUpTimes | number | 否 | 变向加速次数，取值范围：[0,10000]，默认值：0。  **起始版本：** 26.0.1 |
| playerPosition | number | 否 | 球员站位，取值范围：[0,100]，默认值：0。  0表示左前锋，1表示右前锋，2表示中锋，3表示后卫，4表示前腰，5表示守门员，6表示球童，7表示中场，8表示中后卫，9表示后腰，10表示左后卫，11表示左边卫，12表示左前卫，13表示左边锋，14表示摄影师，15表示裁判员，16表示右后卫，17表示右边卫，18表示右前卫，19表示右边锋，20表示影锋，21表示替补球员，22表示清道夫。  **起始版本：** 26.0.1 |
| maxJumpHeight | number | 否 | 最大跳跃高度，单位：cm，默认值：0。  **起始版本：** 26.0.1 |
| maxAcceleration | number | 否 | 最大加速度，取值范围：[0,10000]，默认值：0。  **起始版本：** 26.0.1 |
| goalConceded | number | 否 | 失球次数，取值范围：[0,10000]，默认值：0。  **起始版本：** 26.0.1 |

## StrengthTrainingSummary

力量训练统计数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore.Lite

**起始版本：** 6.1.1(24)

**模型约束：** 此接口仅可在FA模型下使用。

| **名称** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| startTime | number | 是 | 运动开始时间，Unix时间戳，单位：ms。 |
| totalTime | number | 是 | 运动总时长，单位：s。 |
| targetDuration | number | 否 | 目标运动时长，单位：s，默认值：0。 |
| avgHeartRate | number | 否 | 运动全程平均心率，单位：bpm，默认值：0。 |
| maxHeartRate | number | 否 | 运动过程最高心率，单位：bpm，默认值：0。 |
| mHeartrateZoneType | number | 否 | 心率区间类型，0为最大心率区间，1为储备心率区间，默认值：0。 |
| startHeartRate | number | 否 | 恢复心率测量初始时的心率，单位：bpm，默认值：0。 |
| endHeartRate | number | 否 | 恢复心率测量结束时的心率，单位：bpm，默认值：0。 |
| loadPeakLevel | number | 否 | 运动负荷峰值等级，等级越大运动效果越好，默认值：0。 |
| aerobicTrainingStress | number | 否 | 有氧训练压力值，量化有氧运动负荷程度，取值范围：[0.0, 5.0]，默认值：0。 |
| anaerobicTrainingStress | number | 否 | 无氧训练压力值，量化无氧运动负荷程度，取值范围：[0.0, 5.0]，默认值：0。 |
| recoveryTime | number | 否 | 预估恢复时间，单位：h，默认值：0。 |
| totalCalories | number | 是 | 运动消耗总热量，包含基础代谢与活动消耗，单位：cal，取值范围：(0, ∞)。 |
| activeCalorie | number | 是 | 运动主动消耗的热量，不含基础代谢，单位：cal，取值范围：(0, ∞)。 |
| actionCount | number | 否 | 动作个数，默认值：0。 |
| totalTrainingVolume | number | 否 | 训练总容量，单位：kg，默认值：0。 |
| actionGroups | number | 否 | 总组数，默认值：0。 |
| rpe | number | 否 | 主观疲劳等级，值越大疲劳等级越高，取值范围：[1,10]，默认值：0。 |
| actions | [healthFields.ActionSummary](health-api-healthfields-lite.md#actionsummary)[] | 否 | 动作类型组数，默认为空。 |

## StrengthTrainingDetail

力量训练锻炼记录详情数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore.Lite

**起始版本：** 6.1.1(24)

**模型约束：** 此接口仅可在FA模型下使用。

| **名称** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| heartRate | [ExerciseHeartRate](health-api-healthfields-lite.md#exerciseheartrate)[] | 否 | 运动心率详情列表，若未填写，默认为空。 |

## TennisSummary

网球统计数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore.Lite

**起始版本：** 6.1.1(24)

**模型约束：** 此接口仅可在FA模型下使用。

| **名称** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| startTime | number | 是 | 运动开始时间，Unix时间戳，单位：ms。 |
| totalTime | number | 是 | 运动总时长，单位：s。 |
| targetDuration | number | 否 | 目标运动时长，单位：s，默认值：0。 |
| avgHeartRate | number | 否 | 运动全程平均心率，单位：bpm，默认值：0。 |
| maxHeartRate | number | 否 | 运动过程最高心率，单位：bpm，默认值：0。 |
| mHeartrateZoneType | number | 否 | 心率区间类型，0为最大心率区间，1为储备心率区间，默认值：0。 |
| startHeartRate | number | 否 | 恢复心率测量初始时的心率，单位：bpm，默认值：0。 |
| endHeartRate | number | 否 | 恢复心率测量结束时的心率，单位：bpm，默认值：0。 |
| loadPeakLevel | number | 否 | 运动负荷峰值等级，等级越大运动效果越好，默认值：0。 |
| aerobicTrainingStress | number | 否 | 有氧训练压力值，量化有氧运动负荷程度，取值范围：[0.0, 5.0]，默认值：0。 |
| anaerobicTrainingStress | number | 否 | 无氧训练压力值，量化无氧运动负荷程度，取值范围：[0.0, 5.0]，默认值：0。 |
| recoveryTime | number | 否 | 预估恢复时间，单位：h，默认值：0。 |
| totalCalories | number | 是 | 运动消耗总热量，包含基础代谢与活动消耗，单位：cal，取值范围：(0, ∞)。 |
| activeCalorie | number | 是 | 运动主动消耗的热量，不含基础代谢，单位：cal，取值范围：(0, ∞)。 |
| forehand | number | 否 | 所有正手方向的击球次数，默认值：0。 |
| forehandTopspin | number | 否 | 正手上旋球次数，取值范围：[0,10000]，默认值：0。  **起始版本：** 26.0.1 |
| forehandFlat | number | 否 | 正手平击次数，取值范围：[0,10000]，默认值：0。  **起始版本：** 26.0.1 |
| forehandBackspin | number | 否 | 正手削球次数，取值范围：[0,10000]，默认值：0。  **起始版本：** 26.0.1 |
| forehandVolley | number | 否 | 正手截击次数，取值范围：[0,10000]，默认值：0。  **起始版本：** 26.0.1 |
| forehandSmash | number | 否 | 正手高压球次数，取值范围：[0,10000]，默认值：0。  **起始版本：** 26.0.1 |
| backhand | number | 否 | 所有反手方向的击球次数，默认值：0。 |
| backhandTopspin | number | 否 | 反手上旋球次数，取值范围：[0,10000]，默认值：0。  **起始版本：** 26.0.1 |
| backhandBackspin | number | 否 | 反手削球次数，取值范围：[0,10000]，默认值：0。  **起始版本：** 26.0.1 |
| backhandVolley | number | 否 | 反手截击次数，取值范围：[0,10000]，默认值：0。  **起始版本：** 26.0.1 |
| backhandSmash | number | 否 | 反手高压球次数，取值范围：[0,10000]，默认值：0。  **起始版本：** 26.0.1 |
| swingTimes | number | 是 | 总挥拍次数(包含所有正手发球，正手击球，反手击球次数)。 |
| maxContinuousRally | number | 是 | 最长连续击球次数。 |
| serve | number | 否 | 发球次数，取值范围：[0,10000]，默认值：0。  **起始版本：** 26.0.1 |
| avgShotSpeed | number | 否 | 平均挥拍速度，单位：km/h，取值范围：[0,500]，默认值：0。  **起始版本：** 26.0.1 |
| maxShotSpeed | number | 否 | 最大挥拍速度，单位：km/h，取值范围：[0,500]，默认值：0。  **起始版本：** 26.0.1 |

## TennisDetail

网球详情数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore.Lite

**起始版本：** 6.1.1(24)

**模型约束：** 此接口仅可在FA模型下使用。

| **名称** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| exerciseHeartRate | [ExerciseHeartRate](health-api-healthfields-lite.md#exerciseheartrate)[] | 否 | 运动心率详情列表，若未填写，默认为空。 |

## StairClimbSummary

爬楼统计数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore.Lite

**起始版本：** 6.1.1(24)

**模型约束：** 此接口仅可在FA模型下使用。

| **名称** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| startTime | number | 是 | 运动开始时间，Unix时间戳，单位：ms。 |
| totalTime | number | 是 | 运动总时长，单位：s。 |
| targetDuration | number | 否 | 目标运动时长，单位：s，默认值：0。 |
| avgHeartRate | number | 否 | 运动全程平均心率，单位：bpm，默认值：0。 |
| maxHeartRate | number | 否 | 运动过程最高心率，单位：bpm，默认值：0。 |
| mHeartrateZoneType | number | 否 | 心率区间类型，0为最大心率区间，1为储备心率区间，默认值：0。 |
| startHeartRate | number | 否 | 恢复心率测量初始时的心率，单位：bpm，默认值：0。 |
| endHeartRate | number | 否 | 恢复心率测量结束时的心率，单位：bpm，默认值：0。 |
| loadPeakLevel | number | 否 | 运动负荷峰值等级，等级越大运动效果越好，默认值：0。 |
| aerobicTrainingStress | number | 否 | 有氧训练压力值，量化有氧运动负荷程度，取值范围：[0.0, 5.0]，默认值：0。 |
| anaerobicTrainingStress | number | 否 | 无氧训练压力值，量化无氧运动负荷程度，取值范围：[0.0, 5.0]，默认值：0。 |
| recoveryTime | number | 否 | 预估恢复时间，单位：h，默认值：0。 |
| totalCalories | number | 是 | 运动消耗总热量，包含基础代谢与活动消耗，单位：cal，取值范围：(0, ∞)。 |
| activeCalorie | number | 是 | 运动主动消耗的热量，不含基础代谢，单位：cal，取值范围：(0, ∞)。 |
| totalSteps | number | 是 | 运动总步数。 |
| elevationGain | number | 是 | 累计爬升。 |
| floors | number | 否 | 爬楼层数，默认值：0。 |
| avgFloorSpeed | number | 否 | 平均每分钟楼层数。 |
| stairs | number | 否 | 台阶数，取值范围：[0,79999]，默认值：0。  **起始版本：** 26.0.1 |

## StairClimbDetail

爬楼详情数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore.Lite

**起始版本：** 6.1.1(24)

**模型约束：** 此接口仅可在FA模型下使用。

| **名称** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| exerciseHeartRate | [ExerciseHeartRate](health-api-healthfields-lite.md#exerciseheartrate)[] | 否 | 运动心率详情列表，若未填写，默认为空。 |

## PickleBallSummary

匹克球统计数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore.Lite

**起始版本：** 6.1.1(24)

**模型约束：** 此接口仅可在FA模型下使用。

| **名称** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| startTime | number | 是 | 运动开始时间，Unix时间戳，单位：ms。 |
| totalTime | number | 是 | 运动总时长，单位：s。 |
| targetDuration | number | 否 | 目标运动时长，单位：s，默认值：0。 |
| avgHeartRate | number | 否 | 运动全程平均心率，单位：bpm，默认值：0。 |
| maxHeartRate | number | 否 | 运动过程最高心率，单位：bpm，默认值：0。 |
| mHeartrateZoneType | number | 否 | 心率区间类型，0为最大心率区间，1为储备心率区间，默认值：0。 |
| startHeartRate | number | 否 | 恢复心率测量初始时的心率，单位：bpm，默认值：0。 |
| endHeartRate | number | 否 | 恢复心率测量结束时的心率，单位：bpm，默认值：0。 |
| loadPeakLevel | number | 否 | 运动负荷峰值等级，等级越大运动效果越好，默认值：0。 |
| aerobicTrainingStress | number | 否 | 有氧训练压力值，量化有氧运动负荷程度，取值范围：[0.0, 5.0]，默认值：0。 |
| anaerobicTrainingStress | number | 否 | 无氧训练压力值，量化无氧运动负荷程度，取值范围：[0.0, 5.0]，默认值：0。 |
| recoveryTime | number | 否 | 预估恢复时间，单位：h，默认值：0。 |
| totalCalories | number | 是 | 运动消耗总热量，包含基础代谢与活动消耗，单位：cal，取值范围：(0, ∞)。 |
| activeCalorie | number | 是 | 运动主动消耗的热量，不含基础代谢，单位：cal，取值范围：(0, ∞)。 |
| forehand | number | 否 | 所有正手方向的击球次数，默认值：0。 |
| forehandDink | number | 否 | 正手网前吊球次数，取值范围：[0,10000]，默认值：0。  **起始版本：** 26.0.1 |
| forehandBackspin | number | 否 | 正手削球次数，取值范围：[0,10000]，默认值：0。  **起始版本：** 26.0.1 |
| forehandVolley | number | 否 | 正手截击次数，取值范围：[0,10000]，默认值：0。  **起始版本：** 26.0.1 |
| forehandDrive | number | 否 | 正手抽球次数，取值范围：[0,10000]，默认值：0。  **起始版本：** 26.0.1 |
| backhand | number | 否 | 所有反手方向的击球次数，默认值：0。 |
| backhandDink | number | 否 | 反手网前吊球次数，取值范围：[0,10000]，默认值：0。  **起始版本：** 26.0.1 |
| backhandBackspin | number | 否 | 反手削球次数，取值范围：[0,10000]，默认值：0。  **起始版本：** 26.0.1 |
| backhandVolley | number | 否 | 反手截击次数，取值范围：[0,10000]，默认值：0。  **起始版本：** 26.0.1 |
| backhandDrive | number | 否 | 反手抽球次数，取值范围：[0,10000]，默认值：0。  **起始版本：** 26.0.1 |
| swingTimes | number | 否 | 总挥拍次数(包含所有正手发球，正手击球，反手击球次数)，默认值：0。 |
| swingSpeed | number | 否 | 挥拍速度，单位：km/h，取值范围：[0,500]，默认值：0。  **起始版本：** 26.0.1 |
| maxContinuousRally | number | 否 | 最长连续击球次数，默认值：0。 |
| avgShotSpeed | number | 否 | 平均挥拍速度，单位：km/h，取值范围：[0,500]，默认值：0。  **起始版本：** 26.0.1 |
| maxShotSpeed | number | 否 | 最大挥拍速度，单位：km/h，取值范围：[0,500]，默认值：0。  **起始版本：** 26.0.1 |

## PickleBallDetail

匹克球详情数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore.Lite

**起始版本：** 6.1.1(24)

**模型约束：** 此接口仅可在FA模型下使用。

| **名称** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| exerciseHeartRate | [ExerciseHeartRate](health-api-healthfields-lite.md#exerciseheartrate)[] | 否 | 运动心率详情列表，若未填写，默认为空。 |

## OutdoorSnowboardSummary

户外单板滑雪统计数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore.Lite

**起始版本：** 26.0.1

**模型约束：** 此接口仅可在FA模型下使用。

| **名称** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| skiDuration | [SkiDurationSummary](health-api-healthfields-lite.md#skidurationsummary) | 是 | 滑雪时长统计。 |
| exerciseHeartRate | [ExerciseHeartRateSummary](health-api-healthfields-lite.md#exerciseheartratesummary) | 否 | 运动心率统计。 |
| heartRateZone | [HeartRateZonesSummary](health-api-healthfields-lite.md#heartratezonessummary) | 是 | 心率区间统计。 |
| trainingLoad | [TrainingLoadSummary](health-api-healthfields-lite.md#trainingloadsummary) | 是 | 训练负荷统计。 |
| trainingStress | [TrainingStressSummary](health-api-healthfields-lite.md#trainingstresssummary) | 是 | 训练压力统计。 |
| recoveryTime | [RecoveryTimeSummary](health-api-healthfields-lite.md#recoverytimesummary) | 是 | 恢复时间统计。 |
| calorie | [CalorieSummary](health-api-healthfields-lite.md#caloriesummary) | 是 | 热量统计。 |
| distance | [DistanceSummary](health-api-healthfields-lite.md#distancesummary) | 是 | 距离统计。 |
| speed | [SkiSpeedSummary](health-api-healthfields-lite.md#skispeedsummary) | 是 | 滑雪速度统计。 |
| tripTimes | [SkiTripTimeSummary](health-api-healthfields-lite.md#skitriptimesummary) | 是 | 滑雪趟数统计。 |
| incline | Omit<[InclineSummary](health-api-healthfields-lite.md#inclinesummary), ‘avgSlopeDegree’ |‘avgUphillSlope’ | ‘avgDownhillSlope’> | 是 | 滑雪坡度统计。 |
| turns | Omit<[TurnsSummary](health-api-healthfields-lite.md#turnssummary), ‘totalTurnNumber’> | 是 | 转弯统计。 |
| gForce | [GForceSummary](health-api-healthfields-lite.md#gforcesummary) | 是 | G-Force统计。 |
| altitude | Omit<[AltitudeSummary](health-api-healthfields-lite.md#altitudesummary), ‘totalAscent’>; | 是 | 海拔统计。 |
| skiPisteRegion | [SkiPisteRegionSummary](health-api-healthfields-lite.md#skipisteregionsummary) | 是 | 雪道区域统计。 |
| temperature | [TemperatureSummary](health-api-healthfields-lite.md#temperaturesummary) | 是 | 温度统计。 |
| runwayRatio | [RunwayRatioSummary](health-api-healthfields-lite.md#runwayratiosummary) | 是 | 雪道统计。 |
| skiTechStats | [SkiTechStatsSummary](health-api-healthfields-lite.md#skitechstatssummary) | 是 | 滑雪技术数据统计。 |

## OutdoorSnowboardDetail

户外单板滑雪详情数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore.Lite

**起始版本：** 26.0.1

**模型约束：** 此接口仅可在FA模型下使用。

| **名称** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| exerciseHeartRate | [ExerciseHeartRate](health-api-healthfields-lite.md#exerciseheartrate)[] | 否 | 运动心率详情列表，若未填写，默认为空。 |

## OutdoorSkiingSummary

type OutdoorSkiingSummary = OutdoorSnowboardSummary

户外双板滑雪统计数据字段列表，继承自户外单板滑雪。

**系统能力：** SystemCapability.Health.HealthStore.Lite

**起始版本：** 26.0.1

**模型约束：** 此接口仅可在FA模型下使用。

| **类型** | **说明** |
| --- | --- |
| [OutdoorSnowboardSummary](health-api-healthfields-lite.md#outdoorsnowboardsummary) | 户外单板滑雪统计数据字段。 |

## OutdoorSkiingDetail

type OutdoorSkiingDetail = OutdoorSnowboardDetail

户外双板滑雪详情数据字段列表，继承自户外单板滑雪。

**系统能力：** SystemCapability.Health.HealthStore.Lite

**起始版本：** 26.0.1

**模型约束：** 此接口仅可在FA模型下使用。

| **类型** | **说明** |
| --- | --- |
| [OutdoorSnowboardDetail](health-api-healthfields-lite.md#outdoorsnowboarddetail) | 户外单板滑雪详情数据字段列表。 |

## IndoorSnowboardSummary

室内单板滑雪统计数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore.Lite

**起始版本：** 26.0.1

**模型约束：** 此接口仅可在FA模型下使用。

| **名称** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| skiDuration | [SkiDurationSummary](health-api-healthfields-lite.md#skidurationsummary) | 是 | 滑雪时长统计。 |
| exerciseHeartRate | [ExerciseHeartRateSummary](health-api-healthfields-lite.md#exerciseheartratesummary) | 否 | 运动心率统计。 |
| heartRateZone | [HeartRateZonesSummary](health-api-healthfields-lite.md#heartratezonessummary) | 是 | 心率区间统计。 |
| trainingLoad | [TrainingLoadSummary](health-api-healthfields-lite.md#trainingloadsummary) | 是 | 训练负荷统计。 |
| trainingStress | [TrainingStressSummary](health-api-healthfields-lite.md#trainingstresssummary) | 是 | 训练压力统计。 |
| recoveryTime | [RecoveryTimeSummary](health-api-healthfields-lite.md#recoverytimesummary) | 是 | 恢复时间统计。 |
| calorie | [CalorieSummary](health-api-healthfields-lite.md#caloriesummary) | 是 | 热量统计。 |
| distance | [DistanceSummary](health-api-healthfields-lite.md#distancesummary) | 是 | 距离统计。 |
| speed | [SkiSpeedSummary](health-api-healthfields-lite.md#skispeedsummary) | 是 | 滑雪速度统计。 |
| tripTimes | [SkiTripTimeSummary](health-api-healthfields-lite.md#skitriptimesummary) | 是 | 滑雪趟数统计。 |
| incline | Omit<[InclineSummary](health-api-healthfields-lite.md#inclinesummary), ‘avgSlopeDegree’ |‘avgUphillSlope’ | ‘avgDownhillSlope’> | 是 | 滑雪坡度统计。 |
| turns | Omit<[TurnsSummary](health-api-healthfields-lite.md#turnssummary), ‘totalTurnNumber’> | 是 | 转弯统计。 |
| skiTechStats | [SkiTechStatsSummary](health-api-healthfields-lite.md#skitechstatssummary) | 是 | 滑雪技术数据统计。 |

## IndoorSnowboardDetail

室内单板滑雪详情数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore.Lite

**起始版本：** 26.0.1

**模型约束：** 此接口仅可在FA模型下使用。

| **名称** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| exerciseHeartRate | [ExerciseHeartRate](health-api-healthfields-lite.md#exerciseheartrate)[] | 否 | 运动心率详情列表，若未填写，默认为空。 |

## IndoorSkiingSummary

type IndoorSkiingSummary = IndoorSnowboardSummary

室内双板滑雪统计数据字段列表，继承自室内单板滑雪。

**系统能力：** SystemCapability.Health.HealthStore.Lite

**起始版本：** 26.0.1

**模型约束：** 此接口仅可在FA模型下使用。

| **类型** | **说明** |
| --- | --- |
| [IndoorSnowboardSummary](health-api-healthfields-lite.md#indoorsnowboardsummary) | 室内单板滑雪统计数据字段列表。 |

## IndoorSkiingDetail

type IndoorSkiingDetail = IndoorSnowboardDetail

室内双板滑雪详情数据字段列表，继承自室内单板滑雪。

**系统能力：** SystemCapability.Health.HealthStore.Lite

**起始版本：** 26.0.1

**模型约束：** 此接口仅可在FA模型下使用。

| **类型** | **说明** |
| --- | --- |
| [IndoorSnowboardDetail](health-api-healthfields-lite.md#indoorsnowboarddetail) | 室内单板滑雪详情数据字段列表。 |

## CrossCountrySkiingSummary

越野滑雪统计数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore.Lite

**起始版本：** 26.0.1

**模型约束：** 此接口仅可在FA模型下使用。

| **名称** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| exerciseHeartRate | [ExerciseHeartRateSummary](health-api-healthfields-lite.md#exerciseheartratesummary) | 否 | 运动心率统计。 |
| heartRateZone | [HeartRateZonesSummary](health-api-healthfields-lite.md#heartratezonessummary) | 是 | 心率区间统计。 |
| trainingLoad | [TrainingLoadSummary](health-api-healthfields-lite.md#trainingloadsummary) | 是 | 训练负荷统计。 |
| trainingStress | [TrainingStressSummary](health-api-healthfields-lite.md#trainingstresssummary) | 是 | 训练压力统计。 |
| recoveryTime | [RecoveryTimeSummary](health-api-healthfields-lite.md#recoverytimesummary) | 是 | 恢复时间统计。 |
| calorie | [CalorieSummary](health-api-healthfields-lite.md#caloriesummary) | 是 | 热量统计。 |
| distance | [DistanceSummary](health-api-healthfields-lite.md#distancesummary) | 是 | 距离统计。 |
| speed | [SkiSpeedSummary](health-api-healthfields-lite.md#skispeedsummary) | 是 | 滑雪速度统计。 |
| altitude | [AltitudeSummary](health-api-healthfields-lite.md#altitudesummary) | 是 | 海拔统计。 |
| temperature | [TemperatureSummary](health-api-healthfields-lite.md#temperaturesummary) | 是 | 温度统计。 |
| skiTechStats | [SkiTechStatsSummary](health-api-healthfields-lite.md#skitechstatssummary) | 是 | 滑雪技术数据统计。 |

## CrossCountrySkiingDetail

越野滑雪详情数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore.Lite

**起始版本：** 26.0.1

**模型约束：** 此接口仅可在FA模型下使用。

| **名称** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| exerciseHeartRate | [ExerciseHeartRate](health-api-healthfields-lite.md#exerciseheartrate)[] | 否 | 运动心率详情列表，若未填写，默认为空。 |

## SkiMountaineeringSummary

滑雪登山统计数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore.Lite

**起始版本：** 26.0.1

**模型约束：** 此接口仅可在FA模型下使用。

| **名称** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| exerciseHeartRate | [ExerciseHeartRateSummary](health-api-healthfields-lite.md#exerciseheartratesummary) | 否 | 运动心率统计。 |
| heartRateZone | [HeartRateZonesSummary](health-api-healthfields-lite.md#heartratezonessummary) | 是 | 心率区间统计。 |
| trainingLoad | [TrainingLoadSummary](health-api-healthfields-lite.md#trainingloadsummary) | 是 | 训练负荷统计。 |
| trainingStress | [TrainingStressSummary](health-api-healthfields-lite.md#trainingstresssummary) | 是 | 训练压力统计。 |
| recoveryTime | [RecoveryTimeSummary](health-api-healthfields-lite.md#recoverytimesummary) | 是 | 恢复时间统计。 |
| calorie | [CalorieSummary](health-api-healthfields-lite.md#caloriesummary) | 是 | 热量统计。 |
| distance | [DistanceSummary](health-api-healthfields-lite.md#distancesummary) | 是 | 距离统计。 |
| speed | [SkiSpeedSummary](health-api-healthfields-lite.md#skispeedsummary) | 是 | 滑雪速度统计。 |
| incline | Omit<[InclineSummary](health-api-healthfields-lite.md#inclinesummary), maxSlopeDegree |avgSlopeDegree> | 是 | 滑雪坡度统计。 |
| altitude | [AltitudeSummary](health-api-healthfields-lite.md#altitudesummary) | 是 | 海拔统计。 |
| temperature | [TemperatureSummary](health-api-healthfields-lite.md#temperaturesummary) | 是 | 温度统计。 |
| skiTechStats | [SkiTechStatsSummary](health-api-healthfields-lite.md#skitechstatssummary) | 是 | 滑雪技术数据统计。 |

## SkiMountaineeringDetail

滑雪登山详情数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore.Lite

**起始版本：** 26.0.1

**模型约束：** 此接口仅可在FA模型下使用。

| **名称** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| exerciseHeartRate | [ExerciseHeartRate](health-api-healthfields-lite.md#exerciseheartrate)[] | 否 | 运动心率详情列表，若未填写，默认为空。 |

## PadelSummary

笼式网球统计数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore.Lite

**起始版本：** 26.0.1

**模型约束：** 此接口仅可在FA模型下使用。

| **名称** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| exerciseHeartRate | [ExerciseHeartRateSummary](health-api-healthfields-lite.md#exerciseheartratesummary) | 否 | 运动心率统计。 |
| heartRateZone | [HeartRateZonesSummary](health-api-healthfields-lite.md#heartratezonessummary) | 是 | 心率区间统计。 |
| trainingLoad | [TrainingLoadSummary](health-api-healthfields-lite.md#trainingloadsummary) | 是 | 训练负荷统计。 |
| trainingStress | [TrainingStressSummary](health-api-healthfields-lite.md#trainingstresssummary) | 是 | 训练压力统计。 |
| recoveryTime | [RecoveryTimeSummary](health-api-healthfields-lite.md#recoverytimesummary) | 是 | 恢复时间统计。 |
| calorie | [CalorieSummary](health-api-healthfields-lite.md#caloriesummary) | 是 | 热量统计。 |
| serve | [ServeSummary](health-api-healthfields-lite.md#servesummary) | 是 | 发球统计。 |
| swingSpeed | [SwingSpeedSummary](health-api-healthfields-lite.md#swingspeedsummary) | 是 | 挥拍速度统计。 |
| padelFeature | [PadelFeature](health-api-healthfields-lite.md#padelfeature) | 是 | 笼式网球特征统计。 |
| techStats | [TechStatsSummary](health-api-healthfields-lite.md#techstatssummary) | 是 | 技术数据统计。 |
| scoreStats | [ScoreStatsSummary](health-api-healthfields-lite.md#scorestatssummary) | 是 | 得分数据统计。 |

## PadelDetail

笼式网球详情数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore.Lite

**起始版本：** 26.0.1

**模型约束：** 此接口仅可在FA模型下使用。

| **名称** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| exerciseHeartRate | [ExerciseHeartRate](health-api-healthfields-lite.md#exerciseheartrate)[] | 否 | 运动心率详情列表，若未填写，默认为空。 |

## PilatesSummary

普拉提统计数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore.Lite

**起始版本：** 26.0.1

**模型约束：** 此接口仅可在FA模型下使用。

| **名称** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| exerciseHeartRate | [ExerciseHeartRateSummary](health-api-healthfields-lite.md#exerciseheartratesummary) | 否 | 运动心率统计。 |
| heartRateZone | [HeartRateZonesSummary](health-api-healthfields-lite.md#heartratezonessummary) | 是 | 心率区间统计。 |
| trainingLoad | [TrainingLoadSummary](health-api-healthfields-lite.md#trainingloadsummary) | 是 | 训练负荷统计。 |
| trainingStress | [TrainingStressSummary](health-api-healthfields-lite.md#trainingstresssummary) | 是 | 训练压力统计。 |
| recoveryTime | [RecoveryTimeSummary](health-api-healthfields-lite.md#recoverytimesummary) | 是 | 恢复时间统计。 |
| calorie | [CalorieSummary](health-api-healthfields-lite.md#caloriesummary) | 是 | 热量统计。 |

## PilatesDetail

普拉提详情数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore.Lite

**起始版本：** 26.0.1

**模型约束：** 此接口仅可在FA模型下使用。

| **名称** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| exerciseHeartRate | [ExerciseHeartRate](health-api-healthfields-lite.md#exerciseheartrate)[] | 否 | 运动心率详情列表，若未填写，默认为空。 |

## FreeTrainingSummary

自由训练统计数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore.Lite

**起始版本：** 26.0.1

**模型约束：** 此接口仅可在FA模型下使用。

| **名称** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| exerciseHeartRate | [ExerciseHeartRateSummary](health-api-healthfields-lite.md#exerciseheartratesummary) | 否 | 运动心率统计。 |
| heartRateZone | [HeartRateZonesSummary](health-api-healthfields-lite.md#heartratezonessummary) | 是 | 心率区间统计。 |
| trainingLoad | [TrainingLoadSummary](health-api-healthfields-lite.md#trainingloadsummary) | 是 | 训练负荷统计。 |
| trainingStress | [TrainingStressSummary](health-api-healthfields-lite.md#trainingstresssummary) | 是 | 训练压力统计。 |
| recoveryTime | [RecoveryTimeSummary](health-api-healthfields-lite.md#recoverytimesummary) | 是 | 恢复时间统计。 |
| calorie | [CalorieSummary](health-api-healthfields-lite.md#caloriesummary) | 是 | 热量统计。 |

## FreeTrainingDetail

自由训练详情数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore.Lite

**起始版本：** 26.0.1

**模型约束：** 此接口仅可在FA模型下使用。

| **名称** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| exerciseHeartRate | [ExerciseHeartRate](health-api-healthfields-lite.md#exerciseheartrate)[] | 否 | 运动心率详情列表，若未填写，默认为空。 |

## RunningSummary

户外跑步统计数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore.Lite

**起始版本：** 26.0.1

**模型约束：** 此接口仅可在FA模型下使用。

| **名称** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| exerciseHeartRate | [ExerciseHeartRateSummary](health-api-healthfields-lite.md#exerciseheartratesummary) | 否 | 运动心率统计。 |
| heartRateZone | [HeartRateZonesSummary](health-api-healthfields-lite.md#heartratezonessummary) | 是 | 心率区间统计。 |
| trainingLoad | [TrainingLoadSummary](health-api-healthfields-lite.md#trainingloadsummary) | 是 | 训练负荷统计。 |
| trainingStress | [TrainingStressSummary](health-api-healthfields-lite.md#trainingstresssummary) | 是 | 训练压力统计。 |
| recoveryTime | [RecoveryTimeSummary](health-api-healthfields-lite.md#recoverytimesummary) | 是 | 恢复时间统计。 |
| calorie | [CalorieSummary](health-api-healthfields-lite.md#caloriesummary) | 是 | 热量统计。 |
| speed | [SpeedSummary](health-api-healthfields-lite.md#speedsummary) | 是 | 速度统计。 |
| cadence | [CadenceSummary](health-api-healthfields-lite.md#cadencesummary) | 是 | 步频统计。 |
| step | [StepSummary](health-api-healthfields-lite.md#stepsummary) | 是 | 步数统计。 |
| altitude | [AltitudeSummary](health-api-healthfields-lite.md#altitudesummary) | 是 | 海拔统计。 |
| distance | [DistanceSummary](health-api-healthfields-lite.md#distancesummary) | 是 | 距离统计。 |
| analogPower | [AnalogPowerSummary](health-api-healthfields-lite.md#analogpowersummary) | 否 | 模拟功率统计。 |
| runningForm | [RunningFormSummary](health-api-healthfields-lite.md#runningformsummary) | 否 | 跑姿统计。 |
| runPaceZone | [RunPaceZoneSummary](health-api-healthfields-lite.md#runpacezonesummary) | 否 | 配速区间统计。 |

## RunningDetail

户外跑步详情数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore.Lite

**起始版本：** 26.0.1

**模型约束：** 此接口仅可在FA模型下使用。

| **名称** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| exerciseHeartRate | [ExerciseHeartRate](health-api-healthfields-lite.md#exerciseheartrate)[] | 否 | 运动心率详情列表，若未填写，默认为空。 |

## CyclingSummary

户外骑行统计数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore.Lite

**起始版本：** 26.0.1

**模型约束：** 此接口仅可在FA模型下使用。

| **名称** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| exerciseHeartRate | [ExerciseHeartRateSummary](health-api-healthfields-lite.md#exerciseheartratesummary) | 否 | 运动心率统计。 |
| heartRateZone | [HeartRateZonesSummary](health-api-healthfields-lite.md#heartratezonessummary) | 是 | 心率区间统计。 |
| trainingLoad | [TrainingLoadSummary](health-api-healthfields-lite.md#trainingloadsummary) | 是 | 训练负荷统计。 |
| trainingStress | [TrainingStressSummary](health-api-healthfields-lite.md#trainingstresssummary) | 是 | 训练压力统计。 |
| recoveryTime | [RecoveryTimeSummary](health-api-healthfields-lite.md#recoverytimesummary) | 是 | 恢复时间统计。 |
| calorie | [CalorieSummary](health-api-healthfields-lite.md#caloriesummary) | 是 | 热量统计。 |
| speed | [SpeedSummary](health-api-healthfields-lite.md#speedsummary) | 是 | 速度统计。 |
| altitude | [AltitudeSummary](health-api-healthfields-lite.md#altitudesummary) | 是 | 海拔统计。 |
| distance | [DistanceSummary](health-api-healthfields-lite.md#distancesummary) | 是 | 距离统计。 |

## CyclingDetail

户外骑行详情数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore.Lite

**起始版本：** 26.0.1

**模型约束：** 此接口仅可在FA模型下使用。

| **名称** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| exerciseHeartRate | [ExerciseHeartRate](health-api-healthfields-lite.md#exerciseheartrate)[] | 否 | 运动心率详情列表，若未填写，默认为空。 |
