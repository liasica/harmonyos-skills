---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/health-api-healthfields-lite
title: healthFields (运动健康数据字段)(Lite)
breadcrumb: API参考 > 应用服务 > Health Service Kit（运动健康服务） > ArkTS API > 运动健康数据类型常量及模型定义 > healthFields (运动健康数据字段)(Lite)
category: harmonyos-references
scraped_at: 2026-09-02T15:02:55+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:7232cb706f7175725ed38af82688ddd3520cf295dbc38fd87565a8cfbc2e206c
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
| totalCalories | number | 是 | 运动消耗总卡路里，包含基础代谢与活动消耗，单位：cal，取值范围：(0, ∞)。 |
| activeCalorie | number | 是 | 运动主动消耗的卡路里，不含基础代谢，单位：cal，取值范围：(0, ∞)。 |
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
| totalCalories | number | 是 | 运动消耗总卡路里，包含基础代谢与活动消耗，单位：cal，取值范围：(0, ∞)。 |
| activeCalorie | number | 是 | 运动主动消耗的卡路里，不含基础代谢，单位：cal，取值范围：(0, ∞)。 |
| goalsTimes | number | 否 | 进球次数，取值范围：[0,10000]，默认值：0。 |
| assistsTimes | number | 否 | 助攻次数，取值范围：[0,10000]，默认值：0。 |

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
| totalCalories | number | 是 | 运动消耗总卡路里，包含基础代谢与活动消耗，单位：cal，取值范围：(0, ∞)。 |
| activeCalorie | number | 是 | 运动主动消耗的卡路里，不含基础代谢，单位：cal，取值范围：(0, ∞)。 |
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
| totalCalories | number | 是 | 运动消耗总卡路里，包含基础代谢与活动消耗，单位：cal，取值范围：(0, ∞)。 |
| activeCalorie | number | 是 | 运动主动消耗的卡路里，不含基础代谢，单位：cal，取值范围：(0, ∞)。 |
| forehand | number | 否 | 所有正手方向的击球次数，默认值：0。 |
| backhand | number | 否 | 所有反手方向的击球次数，默认值：0。 |
| swingTimes | number | 是 | 总挥拍次数(包含所有正手发球，正手击球，反手击球次数)。 |
| maxContinuousRally | number | 是 | 最长连续击球次数。 |

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
| totalCalories | number | 是 | 运动消耗总卡路里，包含基础代谢与活动消耗，单位：cal，取值范围：(0, ∞)。 |
| activeCalorie | number | 是 | 运动主动消耗的卡路里，不含基础代谢，单位：cal，取值范围：(0, ∞)。 |
| totalSteps | number | 是 | 运动总步数。 |
| elevationGain | number | 是 | 累计爬升。 |
| floors | number | 否 | 爬楼层数，默认值：0。 |
| avgFloorSpeed | number | 是 | 平均每分钟楼层数。 |

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
| totalCalories | number | 是 | 运动消耗总卡路里，包含基础代谢与活动消耗，单位：cal，取值范围：(0, ∞)。 |
| activeCalorie | number | 是 | 运动主动消耗的卡路里，不含基础代谢，单位：cal，取值范围：(0, ∞)。 |
| forehand | number | 否 | 所有正手方向的击球次数，默认值：0。 |
| backhand | number | 否 | 所有反手方向的击球次数，默认值：0。 |
| swingTimes | number | 否 | 总挥拍次数(包含所有正手发球，正手击球，反手击球次数)，默认值：0。 |
| maxContinuousRally | number | 否 | 最长连续击球次数，默认值：0。 |

## PickleBallDetail

匹克球详情数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore.Lite

**起始版本：** 6.1.1(24)

**模型约束：** 此接口仅可在FA模型下使用。

| **名称** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| exerciseHeartRate | [ExerciseHeartRate](health-api-healthfields-lite.md#exerciseheartrate)[] | 否 | 运动心率详情列表，若未填写，默认为空。 |
