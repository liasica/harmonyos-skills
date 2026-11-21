---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/health-litewearable-realtime-manage
title: 管理运动实时数据
breadcrumb: 指南 > 应用服务 > Health Service Kit（运动健康服务） > 应用开发 > LiteWearable应用开发 > 管理运动实时数据
category: harmonyos-guides
scraped_at: 2026-11-21T09:12:28+08:00
doc_updated_at: 2026-11-20
content_hash: sha256:804de5e68b0c94e22f029f40d7e5816b6ac5b0bef3b2e9e5e4d71fb02fa17046
---

运动实时数据是指用户在运动过程中由穿戴设备持续采集、并按一定频率实时上报的动态数据。

本文介绍在运动过程中穿戴设备可显示的所有动态数据，以及对动态数据的订阅/写入的能力。

从API版本6.1.1(24)开始，支持爬楼、羽毛球、匹克球、力量训练、足球、网球。

从API版本26.0.1开始，支持户外骑行，户外跑步、滑雪、笼式网球、普拉提、自由训练。

## 运动类型

### 笼式网球

| **名称** | **类型** | 只读 | **说明** |
| --- | --- | --- | --- |
| activeCalorie | number | 是 | 运动主动消耗的热量，不含基础代谢，单位：cal，取值范围：(0, ∞)。 |
| activeTime | number | 是 | 活跃时长。单位：s |
| aerobicTrainingStress | number | 是 | 有氧训练压力值，量化有氧运动负荷程度，取值范围：[0.0, 5.0]，默认值：0。 |
| anaerobicTrainingStress | number | 是 | 无氧训练压力值，量化无氧运动负荷程度，取值范围：[0.0, 5.0]，默认值：0。 |
| duration | number | 是 | 运动时长。单位：s |
| heartRate | number | 是 | 运动心率。单位：次/分钟 |
| totalCalories | number | 是 | 运动消耗总热量，包含基础代谢与活动消耗，单位：cal，取值范围：(0, ∞)。 |
| avgShotSpeed | number | 否 | 平均挥拍速度。 |
| backhand | number | 否 | 反手击球次数。 |
| backhandBackspin | number | 否 | 反手下旋球次数。 |
| backhandBajada | number | 否 | 反手巴哈达次数。 |
| backhandDrive | number | 否 | 反手抽球次数。 |
| backhandDrop | number | 否 | 反手吊小球次数。 |
| backhandSmash | number | 否 | 反手高压球次数。 |
| backhandVolley | number | 否 | 反手截击次数。 |
| bandeja | number | 否 | 班德哈次数。 |
| forehand | number | 否 | 正手击球次数。 |
| forehandBackspin | number | 否 | 正手下旋球次数。 |
| forehandBajada | number | 否 | 正手巴哈达次数。 |
| forehandDrive | number | 否 | 正手抽球次数。 |
| forehandDrop | number | 否 | 正手吊小球次数。 |
| forehandSmash | number | 否 | 正手高压球次数。 |
| forehandVolley | number | 否 | 正手截击次数。 |
| maxContinuousRally | number | 否 | 最长连拍次数。 |
| maxShotSpeed | number | 否 | 最大挥拍速度。 |
| movementDistance | number | 否 | 移动距离。单位：m |
| serve | number | 否 | 发球次数。 |
| swingTimes | number | 否 | 挥拍次数。 |
| vibora | number | 否 | 维博拉次数。 |

### 力量训练

| **名称** | **类型** | 只读 | **说明** |
| --- | --- | --- | --- |
| activeCalorie | number | 是 | 运动主动消耗的热量，不含基础代谢，单位：cal，取值范围：(0, ∞)。 |
| activeTime | number | 是 | 活跃时长。单位：s |
| aerobicTrainingStress | number | 是 | 有氧训练压力值，量化有氧运动负荷程度，取值范围：[0.0, 5.0]，默认值：0。 |
| anaerobicTrainingStress | number | 是 | 无氧训练压力值，量化无氧运动负荷程度，取值范围：[0.0, 5.0]，默认值：0。 |
| duration | number | 是 | 运动时长。单位：s |
| heartRate | number | 是 | 运动心率。单位：次/分钟 |
| totalCalories | number | 是 | 运动消耗总热量，包含基础代谢与活动消耗，单位：cal，取值范围：(0, ∞)。 |

### 自由训练

| **名称** | **类型** | 只读 | **说明** |
| --- | --- | --- | --- |
| activeCalorie | number | 是 | 运动主动消耗的热量，不含基础代谢，单位：cal，取值范围：(0, ∞)。 |
| activeTime | number | 是 | 活跃时长。单位：s |
| aerobicTrainingStress | number | 是 | 有氧训练压力值，量化有氧运动负荷程度，取值范围：[0.0, 5.0]，默认值：0。 |
| anaerobicTrainingStress | number | 是 | 无氧训练压力值，量化无氧运动负荷程度，取值范围：[0.0, 5.0]，默认值：0。 |
| duration | number | 是 | 运动时长。单位：s |
| heartRate | number | 是 | 运动心率。单位：次/分钟 |
| totalCalories | number | 是 | 运动消耗总热量，包含基础代谢与活动消耗，单位：cal，取值范围：(0, ∞)。 |

### 普拉提

| **名称** | **类型** | 只读 | **说明** |
| --- | --- | --- | --- |
| activeCalorie | number | 是 | 运动主动消耗的热量，不含基础代谢，单位：cal，取值范围：(0, ∞)。 |
| activeTime | number | 是 | 活跃时长。单位：s |
| aerobicTrainingStress | number | 是 | 有氧训练压力值，量化有氧运动负荷程度，取值范围：[0.0, 5.0]，默认值：0。 |
| anaerobicTrainingStress | number | 是 | 无氧训练压力值，量化无氧运动负荷程度，取值范围：[0.0, 5.0]，默认值：0。 |
| duration | number | 是 | 运动时长。单位：s |
| heartRate | number | 是 | 运动心率。单位：次/分钟 |
| totalCalories | number | 是 | 运动消耗总热量，包含基础代谢与活动消耗，单位：cal，取值范围：(0, ∞)。 |

### 户外滑雪

| **名称** | **类型** | 只读 | **说明** |
| --- | --- | --- | --- |
| activeCalorie | number | 是 | 运动主动消耗的热量，不含基础代谢，单位：cal，取值范围：(0, ∞)。 |
| activeTime | number | 是 | 活跃时长。单位：s |
| aerobicTrainingStress | number | 是 | 有氧训练压力值，量化有氧运动负荷程度，取值范围：[0.0, 5.0]，默认值：0。 |
| anaerobicTrainingStress | number | 是 | 无氧训练压力值，量化无氧运动负荷程度，取值范围：[0.0, 5.0]，默认值：0。 |
| duration | number | 是 | 运动时长。单位：s |
| heartRate | number | 是 | 运动心率。单位：次/分钟 |
| totalCalories | number | 是 | 运动消耗总热量，包含基础代谢与活动消耗，单位：cal，取值范围：(0, ∞)。 |
| averageEdgeAngle | number | 否 | 平均立刃。单位：° |
| averageEdgingSync | number | 否 | 平均立刃同步率。 |
| averageParallelism | number | 否 | 平均平行率。 |
| averageSpeed | number | 是 | 平均速度。单位：m/s |
| avgGForce | number | 是 | 平均G-Force。 |
| avgTurnFreq | number | 是 | 平均转弯频率。单位：次/分钟 |
| carving | number | 否 | 卡宾次数。 |
| carvingRatio | number | 否 | 卡宾占比。 |
| distance | number | 是 | 距离统计。单位：m |
| earlyEdging | number | 否 | 提前立刃启动动作在整个转弯周期中所占的时间比例。 |
| earlyMovementIndex | number | 否 | 提前移动指数。 |
| earlyWeightTransfer | number | 否 | 提前重心变化。 |
| falls | number | 否 | 摔倒次数。 |
| latitude | number | 是 | 纬度。单位：度 |
| leftTurnCount | number | 是 | 左转次数。 |
| longitude | number | 是 | 经度。单位：度 |
| maxEdgeAngle | number | 否 | 最大立刃。单位：° |
| maxGForce | number | 是 | 最大G-Force。 |
| maxSpeed | number | 是 | 最大速度。单位：m/s |
| midLongTurn | number | 是 | 中长弯次数。 |
| outsideSkiPressureIndex | number | 否 | 外侧压感指数。单位：kg |
| pressureSmoothnessIndex | number | 否 | 压力平滑指数。 |
| progressiveEdging | number | 否 | 渐进式立刃。单位：°/s |
| rightTurnCount | number | 是 | 右转次数。 |
| shortRadiusTurn | number | 是 | 短弯次数。 |
| skiAvgSlopeDegree | number | 是 | 平均坡度。单位：° |
| skidding | number | 否 | 搓雪次数。 |
| skiddingRatio | number | 否 | 搓雪占比。 |
| skiingCount | number | 是 | 滑雪趟数。 |
| skiingDistance | number | 是 | 滑行距离。单位：m |
| skiingMaxSlope | number | 是 | 滑雪最大坡度。 |
| skiingTime | number | 是 | 滑行时间。单位：ms |
| steering | number | 否 | 走刃次数。 |
| steeringRatio | number | 否 | 走刃占比。 |
| totalAltitude | number | 是 | 累计爬升。单位：m |
| totalAvgTurnFreq | number | 是 | 总平均转弯频率。单位：次/分钟 |
| totalDescend | number | 是 | 累计下降。单位：m |
| totalMidLongTurn | number | 是 | 中长弯总次数。 |
| totalShortRadiusTurn | number | 是 | 短弯总次数。 |
| totalTurnNumber | number | 是 | 总转弯次数。 |
| turnNumber | number | 是 | 转弯次数。 |
| turnRoundness | number | 否 | 弯形圆润度。 |
| turnSymmetry | number | 否 | 弯形对称度。 |

### 室内滑雪

| **名称** | **类型** | 只读 | **说明** |
| --- | --- | --- | --- |
| activeCalorie | number | 是 | 运动主动消耗的热量，不含基础代谢，单位：cal，取值范围：(0, ∞)。 |
| activeTime | number | 是 | 活跃时长。单位：s |
| aerobicTrainingStress | number | 是 | 有氧训练压力值，量化有氧运动负荷程度，取值范围：[0.0, 5.0]，默认值：0。 |
| anaerobicTrainingStress | number | 是 | 无氧训练压力值，量化无氧运动负荷程度，取值范围：[0.0, 5.0]，默认值：0。 |
| duration | number | 是 | 运动时长。单位：s |
| heartRate | number | 是 | 运动心率。单位：次/分钟 |
| totalCalories | number | 是 | 运动消耗总热量，包含基础代谢与活动消耗，单位：cal，取值范围：(0, ∞)。 |
| averageEdgeAngle | number | 否 | 平均立刃。单位：° |
| averageEdgingSync | number | 否 | 平均立刃同步率。 |
| averageParallelism | number | 否 | 平均平行率。 |
| averageSpeed | number | 是 | 平均速度。单位：m/s |
| avgTurnFreq | number | 是 | 平均转弯频率。单位：次/分钟 |
| carving | number | 否 | 卡宾次数。 |
| carvingRatio | number | 否 | 卡宾占比。 |
| distance | number | 是 | 距离统计。单位：m |
| earlyEdging | number | 否 | 提前立刃启动动作在整个转弯周期中所占的时间比例。 |
| earlyMovementIndex | number | 否 | 提前移动指数。 |
| earlyWeightTransfer | number | 否 | 提前重心变化。 |
| falls | number | 否 | 摔倒次数。 |
| leftTurnCount | number | 是 | 左转次数。 |
| maxEdgeAngle | number | 否 | 最大立刃。单位：° |
| maxSpeed | number | 是 | 最大速度。单位：m/s |
| outsideSkiPressureIndex | number | 否 | 外侧压感指数。单位：kg |
| pressureSmoothnessIndex | number | 否 | 压力平滑指数。 |
| progressiveEdging | number | 否 | 渐进式立刃。单位：°/s |
| rightTurnCount | number | 是 | 右转次数。 |
| skiAvgSlopeDegree | number | 是 | 平均坡度。单位：° |
| skidding | number | 否 | 搓雪次数。 |
| skiddingRatio | number | 否 | 搓雪占比。 |
| skiingCount | number | 是 | 滑雪趟数。 |
| skiingDistance | number | 是 | 滑行距离。单位：m |
| skiingMaxSlope | number | 是 | 滑雪最大坡度。 |
| skiingTime | number | 是 | 滑行时间。单位：ms |
| steering | number | 否 | 走刃次数。 |
| steeringRatio | number | 否 | 走刃占比。 |
| totalAvgTurnFreq | number | 是 | 总平均转弯频率。单位：次/分钟 |
| totalDescend | number | 是 | 累计下降。单位：m |
| totalTurnNumber | number | 是 | 总转弯次数。 |
| turnNumber | number | 是 | 转弯次数。 |
| turnRoundness | number | 否 | 弯形圆润度。 |
| turnSymmetry | number | 否 | 弯形对称度。 |

### 越野滑雪

| **名称** | **类型** | 只读 | **说明** |
| --- | --- | --- | --- |
| activeCalorie | number | 是 | 运动主动消耗的热量，不含基础代谢，单位：cal，取值范围：(0, ∞)。 |
| activeTime | number | 是 | 活跃时长。单位：s |
| aerobicTrainingStress | number | 是 | 有氧训练压力值，量化有氧运动负荷程度，取值范围：[0.0, 5.0]，默认值：0。 |
| anaerobicTrainingStress | number | 是 | 无氧训练压力值，量化无氧运动负荷程度，取值范围：[0.0, 5.0]，默认值：0。 |
| duration | number | 是 | 运动时长。单位：s |
| heartRate | number | 是 | 运动心率。单位：次/分钟 |
| totalCalories | number | 是 | 运动消耗总热量，包含基础代谢与活动消耗，单位：cal，取值范围：(0, ∞)。 |
| averageEdgeAngle | number | 否 | 平均立刃。单位：° |
| averageEdgingSync | number | 否 | 平均立刃同步率。 |
| averageParallelism | number | 否 | 平均平行率。 |
| averageSpeed | number | 是 | 平均速度。单位：m/s |
| carving | number | 否 | 卡宾次数。 |
| carvingRatio | number | 否 | 卡宾占比。 |
| distance | number | 是 | 距离统计。单位：m |
| earlyEdging | number | 否 | 提前立刃启动动作在整个转弯周期中所占的时间比例。 |
| earlyMovementIndex | number | 否 | 提前移动指数。 |
| earlyWeightTransfer | number | 否 | 提前重心变化。 |
| falls | number | 否 | 摔倒次数。 |
| latitude | number | 是 | 纬度。单位：度 |
| longitude | number | 是 | 经度。单位：度 |
| maxEdgeAngle | number | 否 | 最大立刃。单位：° |
| outsideSkiPressureIndex | number | 否 | 外侧压感指数。单位：kg |
| pressureSmoothnessIndex | number | 否 | 压力平滑指数。 |
| progressiveEdging | number | 否 | 渐进式立刃。单位：°/s |
| skidding | number | 否 | 搓雪次数。 |
| skiddingRatio | number | 否 | 搓雪占比。 |
| steering | number | 否 | 走刃次数。 |
| steeringRatio | number | 否 | 走刃占比。 |
| totalAltitude | number | 是 | 累计爬升。单位：m |
| totalDescend | number | 是 | 累计下降。单位：m |
| totalRise | number | 是 | 累计爬升。单位：m |
| turnRoundness | number | 否 | 弯形圆润度。 |
| turnSymmetry | number | 否 | 弯形对称度。 |

### 滑雪登山

| **名称** | **类型** | 只读 | **说明** |
| --- | --- | --- | --- |
| activeCalorie | number | 是 | 运动主动消耗的热量，不含基础代谢，单位：cal，取值范围：(0, ∞)。 |
| activeTime | number | 是 | 活跃时长。单位：s |
| aerobicTrainingStress | number | 是 | 有氧训练压力值，量化有氧运动负荷程度，取值范围：[0.0, 5.0]，默认值：0。 |
| anaerobicTrainingStress | number | 是 | 无氧训练压力值，量化无氧运动负荷程度，取值范围：[0.0, 5.0]，默认值：0。 |
| duration | number | 是 | 运动时长。单位：s |
| heartRate | number | 是 | 运动心率。单位：次/分钟 |
| totalCalories | number | 是 | 运动消耗总热量，包含基础代谢与活动消耗，单位：cal，取值范围：(0, ∞)。 |
| skiingTime | number | 是 | 滑行时间。单位：ms |
| distance | number | 是 | 距离统计。单位：m |
| skiingDistance | number | 是 | 滑行距离。单位：m |
| maxSpeed | number | 是 | 最大速度。单位：m/s |
| averageSpeed | number | 是 | 平均速度。单位：m/s |
| skiingCount | number | 是 | 滑雪趟数。 |
| skiingMaxSlope | number | 是 | 滑雪最大坡度。 |
| skiAvgSlopeDegree | number | 是 | 平均坡度。单位：° |
| turnNumber | number | 是 | 转弯次数。 |
| totalTurnNumber | number | 是 | 总转弯次数。 |
| midLongTurn | number | 是 | 中长弯次数。 |
| totalMidLongTurn | number | 是 | 中长弯总次数。 |
| shortRadiusTurn | number | 是 | 短弯次数。 |
| totalShortRadiusTurn | number | 是 | 短弯总次数。 |
| avgTurnFreq | number | 是 | 平均转弯频率。单位：次/分钟 |
| totalAvgTurnFreq | number | 是 | 总平均转弯频率。单位：次/分钟 |
| avgGForce | number | 是 | 平均G-Force。 |
| totalAltitude | number | 是 | 累计爬升。单位：m |
| totalDescend | number | 是 | 累计下降。单位：m |
| longitude | number | 是 | 经度。单位：度 |
| latitude | number | 是 | 纬度。单位：度 |
| leftTurnCount | number | 是 | 左转次数。 |
| rightTurnCount | number | 是 | 右转次数。 |
| maxGForce | number | 是 | 最大G-Force。 |
| falls | number | 否 | 摔倒次数。 |
| skidding | number | 否 | 搓雪次数。 |
| skiddingRatio | number | 否 | 搓雪占比。 |
| steering | number | 否 | 走刃次数。 |
| steeringRatio | number | 否 | 走刃占比。 |
| carving | number | 否 | 卡宾次数。 |
| carvingRatio | number | 否 | 卡宾占比。 |
| turnRoundness | number | 否 | 弯形圆润度。 |
| turnSymmetry | number | 否 | 弯形对称度。 |
| averageParallelism | number | 否 | 平均平行率。 |
| averageEdgingSync | number | 否 | 平均立刃同步率。 |
| averageEdgeAngle | number | 否 | 平均立刃。单位：° |
| maxEdgeAngle | number | 否 | 最大立刃。单位：° |
| earlyMovementIndex | number | 否 | 提前移动指数。 |
| earlyWeightTransfer | number | 否 | 提前重心变化。 |
| earlyEdging | number | 否 | 提前立刃启动动作在整个转弯周期中所占的时间比例。 |
| progressiveEdging | number | 否 | 渐进式立刃。单位：°/s |
| outsideSkiPressureIndex | number | 否 | 外侧压感指数。单位：kg |
| pressureSmoothnessIndex | number | 否 | 压力平滑指数。 |

### 户外跑步

| **名称** | **类型** | 只读 | **说明** |
| --- | --- | --- | --- |
| activeCalorie | number | 是 | 运动主动消耗的热量，不含基础代谢，单位：cal，取值范围：(0, ∞)。 |
| activeTime | number | 是 | 活跃时长。单位：s |
| aerobicTrainingStress | number | 是 | 有氧训练压力值，量化有氧运动负荷程度，取值范围：[0.0, 5.0]，默认值：0。 |
| anaerobicTrainingStress | number | 是 | 无氧训练压力值，量化无氧运动负荷程度，取值范围：[0.0, 5.0]，默认值：0。 |
| duration | number | 是 | 运动时长。单位：s |
| heartRate | number | 是 | 运动心率。单位：次/分钟 |
| totalCalories | number | 是 | 运动消耗总热量，包含基础代谢与活动消耗，单位：cal，取值范围：(0, ∞)。 |
| GCTimeBalance | number | 是 | 左右触地平衡。单位：% |
| analogPower | number | 是 | 模拟功率统计。 |
| averagePace | number | 是 | 平均配速。单位：s/km |
| cadence | number | 是 | 步频。单位：步数/分钟 |
| distance | number | 是 | 距离统计。单位：m |
| groundContactTime | number | 是 | 触地时间。单位：ms |
| latitude | number | 是 | 纬度。单位：度 |
| longitude | number | 是 | 经度。单位：度 |
| pace | number | 是 | 配速。单位：s/km |
| realAvgAnalogPower | number | 是 | 实际平均模拟功率。 |
| step | number | 是 | 步数。 |
| totalAltitude | number | 是 | 累计爬升。单位：m |
| totalDescend | number | 是 | 累计下降。单位：m |
| totalRise | number | 是 | 累计爬升。单位：m |
| verticalOscillation | number | 是 | 垂直振幅。单位：cm |

### 户外骑行

| **名称** | **类型** | 只读 | **说明** |
| --- | --- | --- | --- |
| activeCalorie | number | 是 | 运动主动消耗的热量，不含基础代谢，单位：cal，取值范围：(0, ∞)。 |
| activeTime | number | 是 | 活跃时长。单位：s |
| aerobicTrainingStress | number | 是 | 有氧训练压力值，量化有氧运动负荷程度，取值范围：[0.0, 5.0]，默认值：0。 |
| anaerobicTrainingStress | number | 是 | 无氧训练压力值，量化无氧运动负荷程度，取值范围：[0.0, 5.0]，默认值：0。 |
| duration | number | 是 | 运动时长。单位：s |
| heartRate | number | 是 | 运动心率。单位：次/分钟 |
| totalCalories | number | 是 | 运动消耗总热量，包含基础代谢与活动消耗，单位：cal，取值范围：(0, ∞)。 |
| analogCadence | number | 是 | 模拟踏频。单位：转/分钟 |
| analogPower | number | 是 | 模拟功率统计。 |
| averageSpeed | number | 是 | 平均速度。单位：m/s |
| avgAnalogCadence | number | 是 | 平均模拟踏频。单位：转/分钟 |
| distance | number | 是 | 距离统计。单位：m |
| inclination | number | 是 | 坡度。单位：% |
| latitude | number | 是 | 纬度。单位：度 |
| longitude | number | 是 | 经度。单位：度 |
| maxSpeed | number | 是 | 最大速度。单位：m/s |
| realAvgAnalogPower | number | 是 | 实际平均模拟功率。 |
| speed | number | 是 | 速度详情。单位：m/s |
| totalAltitude | number | 是 | 累计爬升。单位：m |
| totalDescend | number | 是 | 累计下降。单位：m |
| totalRise | number | 是 | 累计爬升。单位：m |

### 匹克球

| **名称** | **类型** | 只读 | **说明** |
| --- | --- | --- | --- |
| activeCalorie | number | 是 | 运动主动消耗的热量，不含基础代谢，单位：cal，取值范围：(0, ∞)。 |
| activeTime | number | 是 | 活跃时长。单位：s |
| aerobicTrainingStress | number | 是 | 有氧训练压力值，量化有氧运动负荷程度，取值范围：[0.0, 5.0]，默认值：0。 |
| anaerobicTrainingStress | number | 是 | 无氧训练压力值，量化无氧运动负荷程度，取值范围：[0.0, 5.0]，默认值：0。 |
| duration | number | 是 | 运动时长。单位：s |
| heartRate | number | 是 | 运动心率。单位：次/分钟 |
| totalCalories | number | 是 | 运动消耗总热量，包含基础代谢与活动消耗，单位：cal，取值范围：(0, ∞)。 |
| forehandDink | number | 否 | 正手网前吊球次数。 |
| forehandBackspin | number | 否 | 正手削球次数。 |
| forehandVolley | number | 否 | 正手截击次数。 |
| forehandDrive | number | 否 | 正手抽球次数。 |
| backhandDink | number | 否 | 反手网前吊球次数。 |
| backhandBackspin | number | 否 | 反手削球次数。 |
| backhandVolley | number | 否 | 反手截击次数。 |
| backhandDrive | number | 否 | 反手抽球次数。 |
| swingSpeed | number | 否 | 挥拍速度。单位：km/h |
| swingTimes | number | 否 | 总挥拍次数，包含所有正手发球、正手击球、反手击球次数。 |
| maxContinuousRally | number | 否 | 最长连续击球次数。 |
| forehand | number | 否 | 所有正手方向的击球次数。 |
| backhand | number | 否 | 所有反手方向的击球次数。 |
| avgShotSpeed | number | 否 | 平均挥拍速度。单位：km/h |
| maxShotSpeed | number | 否 | 最大挥拍速度。单位：km/h |

### 足球

| **名称** | **类型** | 只读 | **说明** |
| --- | --- | --- | --- |
| activeCalorie | number | 是 | 运动主动消耗的热量，不含基础代谢，单位：cal，取值范围：(0, ∞)。 |
| activeTime | number | 是 | 活跃时长。单位：s |
| aerobicTrainingStress | number | 是 | 有氧训练压力值，量化有氧运动负荷程度，取值范围：[0.0, 5.0]，默认值：0。 |
| anaerobicTrainingStress | number | 是 | 无氧训练压力值，量化无氧运动负荷程度，取值范围：[0.0, 5.0]，默认值：0。 |
| duration | number | 是 | 运动时长。单位：s |
| heartRate | number | 是 | 运动心率。单位：次/分钟 |
| totalCalories | number | 是 | 运动消耗总热量，包含基础代谢与活动消耗，单位：cal，取值范围：(0, ∞)。 |
| jumpTimes | number | 否 | 跳跃次数。 |
| sprintTimes | number | 否 | 冲刺次数。 |
| turnSpeedUpTimes | number | 否 | 转身加速次数。 |
| swerveSpeedUpTimes | number | 否 | 变向加速次数。 |
| playerPosition | number | 否 | 球员站位。0表示左前锋，1表示右前锋，2表示中锋，3表示后卫，4表示前腰，5表示守门员，6表示球童，7表示中场，8表示中后卫，9表示后腰，10表示左后卫，11表示左边卫，12表示左前卫，13表示左边锋，14表示摄影师，15表示裁判员，16表示右后卫，17表示右边卫，18表示右前卫，19表示右边锋，20表示影锋，21表示替补球员，22表示清道夫。 |
| goalsTimes | number | 否 | 进球次数。 |
| assistsTimes | number | 否 | 助攻次数。 |
| savesTimes | number | 否 | 扑救次数。 |
| maxJumpHeight | number | 否 | 最大跳跃高度。单位：cm |
| maxAcceleration | number | 否 | 最大加速度。 |
| goalConceded | number | 否 | 失球次数。 |

### 羽毛球

| **名称** | **类型** | 只读 | **说明** |
| --- | --- | --- | --- |
| activeCalorie | number | 是 | 运动主动消耗的热量，不含基础代谢，单位：cal，取值范围：(0, ∞)。 |
| activeTime | number | 是 | 活跃时长。单位：s |
| aerobicTrainingStress | number | 是 | 有氧训练压力值，量化有氧运动负荷程度，取值范围：[0.0, 5.0]，默认值：0。 |
| anaerobicTrainingStress | number | 是 | 无氧训练压力值，量化无氧运动负荷程度，取值范围：[0.0, 5.0]，默认值：0。 |
| duration | number | 是 | 运动时长。单位：s |
| heartRate | number | 是 | 运动心率。单位：次/分钟 |
| totalCalories | number | 是 | 运动消耗总热量，包含基础代谢与活动消耗，单位：cal，取值范围：(0, ∞)。 |
| avgShotSpeed | number | 否 | 平均击球速度。单位：km/h |
| maxShotSpeed | number | 否 | 最高击球速度。单位：km/h |
| shots | number | 否 | 总击球次数。 |
| maxContinuousRally | number | 否 | 最长连续对打回合数。 |
| forehandStroke | number | 否 | 正手击球次数。 |
| backhandStroke | number | 否 | 反手击球次数。 |
| overhandStroke | number | 否 | 上手击球次数，如发球、扣杀准备动作。 |
| underhandStroke | number | 否 | 下手击球次数，如挑球、切球。 |
| smash | number | 否 | 扣杀次数。 |
| highClear | number | 否 | 高远球次数。 |

### 网球

| **名称** | **类型** | 只读 | **说明** |
| --- | --- | --- | --- |
| activeCalorie | number | 是 | 运动主动消耗的热量，不含基础代谢，单位：cal，取值范围：(0, ∞)。 |
| activeTime | number | 是 | 活跃时长。单位：s |
| aerobicTrainingStress | number | 是 | 有氧训练压力值，量化有氧运动负荷程度，取值范围：[0.0, 5.0]，默认值：0。 |
| anaerobicTrainingStress | number | 是 | 无氧训练压力值，量化无氧运动负荷程度，取值范围：[0.0, 5.0]，默认值：0。 |
| duration | number | 是 | 运动时长。单位：s |
| heartRate | number | 是 | 运动心率。单位：次/分钟 |
| totalCalories | number | 是 | 运动消耗总热量，包含基础代谢与活动消耗，单位：cal，取值范围：(0, ∞)。 |
| serve | number | 否 | 发球次数。 |
| forehand | number | 否 | 所有正手方向的击球次数。 |
| forehandTopspin | number | 否 | 正手上旋球次数。 |
| forehandFlat | number | 否 | 正手平击次数。 |
| forehandBackspin | number | 否 | 正手削球次数。 |
| forehandVolley | number | 否 | 正手截击次数。 |
| backhand | number | 否 | 所有反手方向的击球次数。 |
| backhandTopspin | number | 否 | 反手上旋球次数。 |
| backhandBackspin | number | 否 | 反手削球次数。 |
| backhandVolley | number | 否 | 反手截击次数。 |
| swingTimes | number | 否 | 总挥拍次数，包含所有正手发球、正手击球、反手击球次数。 |
| maxContinuousRally | number | 否 | 最长连续击球次数。 |
| forehandSmash | number | 否 | 正手高压球次数。 |
| backhandSmash | number | 否 | 反手高压球次数。 |
| avgShotSpeed | number | 否 | 平均挥拍速度。单位：km/h |
| maxShotSpeed | number | 否 | 最大挥拍速度。单位：km/h |

### 爬楼

| **名称** | **类型** | 只读 | **说明** |
| --- | --- | --- | --- |
| activeCalorie | number | 是 | 运动主动消耗的热量，不含基础代谢，单位：cal，取值范围：(0, ∞)。 |
| activeTime | number | 是 | 活跃时长。单位：s |
| aerobicTrainingStress | number | 是 | 有氧训练压力值，量化有氧运动负荷程度，取值范围：[0.0, 5.0]，默认值：0。 |
| anaerobicTrainingStress | number | 是 | 无氧训练压力值，量化无氧运动负荷程度，取值范围：[0.0, 5.0]，默认值：0。 |
| duration | number | 是 | 运动时长。单位：s |
| heartRate | number | 是 | 运动心率。单位：次/分钟 |
| totalCalories | number | 是 | 运动消耗总热量，包含基础代谢与活动消耗，单位：cal，取值范围：(0, ∞)。 |
| totalRise | number | 是 | 累计爬升。单位：m |
| floors | number | 否 | 爬楼层数。 |
| avgFloorSpeed | number | 否 | 平均每分钟楼层数。 |
| stairs | number | 否 | 台阶数。 |
| totalSteps | number | 否 | 运动总步数。 |

## 订阅/写入实时运动数据

开启运动后，可通过[onData](../harmonyos-references/health-api-healthservice-lite.md#ondata)接口订阅运动中产生的实时数据，并通过[sendData](../harmonyos-references/health-api-healthservice-lite.md#ondata)写入实时数据，具体用法请参考[管理运动](health-litewearable-sport-linkage-manage.md)。
