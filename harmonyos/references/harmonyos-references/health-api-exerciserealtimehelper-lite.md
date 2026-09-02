---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/health-api-exerciserealtimehelper-lite
title: exerciseRealtimeHelper (实时运动数据类型常量)(Lite)
breadcrumb: API参考 > 应用服务 > Health Service Kit（运动健康服务） > ArkTS API > 运动健康数据类型常量及模型定义 > exerciseRealtimeHelper (实时运动数据类型常量)(Lite)
category: harmonyos-references
scraped_at: 2026-09-02T15:02:55+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:5b9c51ed3e2b7e005e924dd4743cc525bafe9b2af299af3b1009e7ed63b7a9e6
---

本模块提供实时运动数据类型常量。

**起始版本：** 6.1.1(24)

## 导入模块

```javascript
import healthStore  from '@hms.health.store';
```

**说明** 

此模块为healthStore子模块，需通过healthStore.exerciseRealtimeHelper方式使用。

## 常量

**系统能力：** SystemCapability.Health.HealthStore.Lite

**起始版本：** 6.1.1(24)

**模型约束：** 此接口仅可在FA模型下使用。

| 名称 | 类型 | 只读 | 说明 |
| --- | --- | --- | --- |
| REALTIME\_KEY\_ACTIVE\_TIME | string | 是 | 锻炼时长（运动过程中身体处于活跃状态时长），单位：s 。  支持羽毛球、爬楼、网球、匹克球、足球。 |
| REALTIME\_KEY\_AEROBIC\_TRAINING\_STRESS | string | 是 | 单次运动对身体有氧系统产生的训练刺激等级，刺激等级越高刺激取值越大，取值范围：[0.0, 5.0]。  支持羽毛球、爬楼、网球、匹克球、足球。 |
| REALTIME\_KEY\_ANAEROBIC\_TRAINING\_STRESS | string | 是 | 单次运动对身体无氧系统产生的训练刺激等级，刺激等级越高刺激取值越大，取值范围：[0.0, 5.0]。  支持羽毛球、爬楼、网球、匹克球、足球。 |
| REALTIME\_KEY\_HEART\_RATE | string | 是 | 心率，单位：bpm。  支持羽毛球、爬楼、网球、匹克球、足球。 |
| REALTIME\_KEY\_DURATION | string | 是 | 运动时间，单位：s。  支持羽毛球、爬楼、网球、匹克球、足球。 |
| REALTIME\_KEY\_TOTAL\_CALORIES | string | 是 | 总消耗热量，单位：cal。  支持羽毛球、爬楼、网球、匹克球、足球。 |
| REALTIME\_KEY\_ACTIVE\_CALORIE | string | 是 | 活动热量，单位：cal。  支持羽毛球、爬楼、网球、匹克球、足球。 |
| REALTIME\_KEY\_AVG\_SHOT\_SPEED | string | 是 | 平均拍速，单位：km/h。  支持羽毛球。 |
| REALTIME\_KEY\_SHOTS | string | 是 | 挥拍次数。  支持羽毛球。 |
| REALTIME\_KEY\_MAX\_CONTINUOUS\_RALLY | string | 是 | 最长连续对打回合数。  支持羽毛球、网球、匹克球。 |
| REALTIME\_KEY\_FOREHAND\_STROKE | string | 是 | 正手击球次数，单位：次。  支持羽毛球。 |
| REALTIME\_KEY\_BACKHAND\_STROKE | string | 是 | 反手击球次数，单位：次。  支持羽毛球。 |
| REALTIME\_KEY\_SMASH | string | 是 | 杀球次数，单位：次。  支持羽毛球。 |
| REALTIME\_KEY\_HIGH\_CLEAR | string | 是 | 高远球次数，单位：次。  支持羽毛球。 |
| REALTIME\_KEY\_MAX\_SHOT\_SPEED | string | 是 | 最大拍速，单位：km/h。  支持羽毛球。 |
| REALTIME\_KEY\_OVERHAND\_STROKE | string | 是 | 上手击球次数，单位：次。  支持羽毛球。 |
| REALTIME\_KEY\_UNDERHAND\_STROKE | string | 是 | 下手击球次数，单位：次。  支持羽毛球。 |
| REALTIME\_KEY\_TOTAL\_STEPS | string | 是 | 运动步数，单位：步。  支持爬楼。 |
| REALTIME\_KEY\_FLOORS | string | 是 | 楼层数。  支持爬楼。 |
| REALTIME\_KEY\_AVG\_FLOOR\_SPEED | string | 是 | 爬楼速度，单位：层/分钟。  支持爬楼。 |
| REALTIME\_KEY\_FOREHAND | string | 是 | 正手击球次数，单位：次。  支持网球、匹克球。 |
| REALTIME\_KEY\_BACKHAND | string | 是 | 反手击球次数，单位：次。  支持网球、匹克球。 |
| REALTIME\_KEY\_SWING\_TIMES | string | 是 | 挥拍次数，单位：次。  支持网球、匹克球。 |
| REALTIME\_KEY\_GOALS\_TIMES | string | 是 | 进球次数，单位：次。  支持足球。 |
| REALTIME\_KEY\_ASSISTS\_TIMES | string | 是 | 助攻次数。  支持足球。 |
