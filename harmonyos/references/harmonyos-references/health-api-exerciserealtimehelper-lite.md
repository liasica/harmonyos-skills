---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/health-api-exerciserealtimehelper-lite
title: exerciseRealtimeHelper (实时运动数据类型常量)(Lite)
breadcrumb: API参考 > 应用服务 > Health Service Kit（运动健康服务） > ArkTS API > 运动健康数据类型常量及模型定义 > exerciseRealtimeHelper (实时运动数据类型常量)(Lite)
category: harmonyos-references
scraped_at: 2026-11-12T09:57:21+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:38e121d88ad05429b8bc06def2494b211d57ab711b08f0d5e3d8a46a320448ea
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
| REALTIME\_KEY\_SUNRISE\_TIME\_HOUR | string | 是 | 日出时间，单位：h。  支持滑雪。  **起始版本：** 26.0.1。 |
| REALTIME\_KEY\_SUNRISE\_TIME\_MIN | string | 是 | 日出时间，单位：min。  支持滑雪。  **起始版本：** 26.0.1。 |
| REALTIME\_KEY\_SUNSET\_TIME\_HOUR | string | 是 | 日落时间，单位：h。  支持滑雪。  **起始版本：** 26.0.1。 |
| REALTIME\_KEY\_SUNSET\_TIME\_MIN | string | 是 | 日落时间，单位：min。  支持滑雪。  **起始版本：** 26.0.1。 |
| REALTIME\_KEY\_SKIING\_DISTANCE | string | 是 | 滑雪滑行距离，单位：km。  **起始版本：** 26.0.1。 |
| REALTIME\_KEY\_DISTANCE | string | 是 | 运动距离，单位：m。  支持滑雪。  **起始版本：** 26.0.1。 |
| REALTIME\_KEY\_SKIING\_MAX\_SPEED | string | 是 | 滑雪最大速度，单位：km/h。  **起始版本：** 26.0.1。 |
| REALTIME\_KEY\_SKIING\_AVERAGE\_SPEED | string | 是 | 滑雪平均速度，单位：km/h。  **起始版本：** 26.0.1。 |
| REALTIME\_KEY\_SKIING\_VERTICAL\_SPEED | string | 是 | 滑雪垂直速度，单位：km/h。  **起始版本：** 26.0.1。 |
| REALTIME\_KEY\_SKI\_TRIP\_TIMES | string | 是 | 滑雪趟数。 |
| REALTIME\_KEY\_SKIING\_MAX\_SLOPE\_DEGREE | string | 是 | 滑雪最大坡度，单位：°。  **起始版本：** 26.0.1。 |
| REALTIME\_KEY\_SKIING\_AVG\_SLOPE\_DEGREE | string | 是 | 滑雪平均坡度，单位：°。  **起始版本：** 26.0.1。 |
| REALTIME\_KEY\_SKIING\_TOTAL\_TURN\_NUMBER | string | 是 | 滑雪转弯次数。  **起始版本：** 26.0.1。 |
| REALTIME\_KEY\_SKIING\_TOTAL\_MID\_LONG\_TURN | string | 是 | 滑雪中长转弯次数。  **起始版本：** 26.0.1。 |
| REALTIME\_KEY\_SKIING\_TOTAL\_SHORT\_LONG\_TURN | string | 是 | 滑雪短转弯次数。  **起始版本：** 26.0.1。 |
| REALTIME\_KEY\_SKIING\_TOTAL\_AVG\_TURN\_FREQ | string | 是 | 滑雪平均转弯频率,单位：次/min。  **起始版本：** 26.0.1。 |
| REALTIME\_KEY\_SKIING\_MAX\_GFORCE | string | 是 | 滑雪最大G-force，即滑雪者滑行或过弯时身体承受的最大惯性力。  **起始版本：** 26.0.1。 |
| REALTIME\_KEY\_SKIING\_AVG\_GFORCE | string | 是 | 滑雪平均G-force，即滑雪者滑行或过弯时身体承受的平均惯性力。  **起始版本：** 26.0.1。 |
| REALTIME\_KEY\_TOTAL\_ALTITUDE | string | 是 | 当前海拔，单位：m。  支持滑雪。  **起始版本：** 26.0.1。 |
| REALTIME\_KEY\_TOTAL\_DESCEND | string | 是 | 累计下降的海拔，单位：m。  支持滑雪。  **起始版本：** 26.0.1。 |
| REALTIME\_KEY\_TOTAL\_RISE | string | 是 | 累计上升的海拔，单位：m。  支持滑雪。  **起始版本：** 26.0.1。 |
| REALTIME\_KEY\_LOCATION\_LONGITUDE | string | 是 | 所在位置的经度，单位：°。  支持滑雪。  **起始版本：** 26.0.1。 |
| REALTIME\_KEY\_LOCATION\_LATITUDE | string | 是 | 所在位置的纬度，单位：°。  支持滑雪。  **起始版本：** 26.0.1。 |
| REALTIME\_KEY\_SKIING\_FALLS | string | 是 | 滑雪摔倒次数。  **起始版本：** 26.0.1。 |
| REALTIME\_KEY\_SKIING\_SKIDDING | string | 是 | 滑雪搓雪次数。 |
| REALTIME\_KEY\_SKIING\_SKIDDING\_RATIO | string | 是 | 滑雪搓雪占比，单位：%。  **起始版本：** 26.0.1。 |
| REALTIME\_KEY\_SKIING\_STEERING | string | 是 | 滑雪走刃次数。  **起始版本：** 26.0.1。 |
| REALTIME\_KEY\_SKIING\_STEERING\_RATIO | string | 是 | 滑雪走刃占比，单位：%。  **起始版本：** 26.0.1。 |
| REALTIME\_KEY\_SKIING\_CARVING | string | 是 | 滑雪卡宾次数。  **起始版本：** 26.0.1。 |
| REALTIME\_KEY\_SKIING\_CARVING\_RATIO | string | 是 | 滑雪卡宾占比，单位：%。  **起始版本：** 26.0.1。 |
| REALTIME\_KEY\_SKIING\_TURN\_ROUNDNESS | string | 是 | 滑雪弯形圆润度。  **起始版本：** 26.0.1。 |
| REALTIME\_KEY\_SKIING\_TURN\_SYMMETRY | string | 是 | 滑雪弯形对称度。  **起始版本：** 26.0.1。 |
| REALTIME\_KEY\_SKIING\_AVERAGE\_PARALLELISM | string | 是 | 滑雪平均平行率。  **起始版本：** 26.0.1。 |
| REALTIME\_KEY\_SKIING\_AVERAGE\_EDGING\_SYNC | string | 是 | 滑雪平均立刃同步率。  **起始版本：** 26.0.1。 |
| REALTIME\_KEY\_SKIING\_AVERAGE\_EDGE\_ANGLE | string | 是 | 滑雪平均立刃角度，单位：°。  **起始版本：** 26.0.1。 |
| REALTIME\_KEY\_SKIING\_MAX\_EDGE\_ANGLE | string | 是 | 滑雪最大立刃角度，单位：°。  **起始版本：** 26.0.1。 |
| REALTIME\_KEY\_SKIING\_EARLY\_MOVEMENT\_INDEX | string | 是 | 滑雪提前移动指数。  **起始版本：** 26.0.1。 |
| REALTIME\_KEY\_SKIING\_EARLY\_WEIGHT\_TRANSFER | string | 是 | 滑雪提前重心变化指数。  **起始版本：** 26.0.1。 |
| REALTIME\_KEY\_SKIING\_EARLY\_EDGING | string | 是 | 滑雪提前立刃指数。  **起始版本：** 26.0.1。 |
| REALTIME\_KEY\_SKIING\_PROGRESSIVE\_EDGING | string | 是 | 滑雪渐进式立刃指数。  **起始版本：** 26.0.1。 |
| REALTIME\_KEY\_SKIING\_OUTSIDE\_SKI\_PRESSURE\_INDEX | string | 是 | 滑雪外侧压感指数。  **起始版本：** 26.0.1。 |
| REALTIME\_KEY\_SKIING\_PRESSURE\_SMOOTHNESS\_INDEX | string | 是 | 滑雪压力平滑指数。  **起始版本：** 26.0.1。 |
| REALTIME\_KEY\_SERVE | string | 是 | 发球次数。  支持笼式网球。  **起始版本：** 26.0.1。 |
| REALTIME\_KEY\_SWING\_SPEED | string | 是 | 挥拍速度，单位：km/h。  支持笼式网球。  **起始版本：** 26.0.1。 |
| REALTIME\_KEY\_BANDEJA | string | 是 | 班德哈次数。  支持笼式网球。  **起始版本：** 26.0.1。 |
| REALTIME\_KEY\_VIBORA | string | 是 | 维博拉次数。  支持笼式网球。  **起始版本：** 26.0.1。 |
| REALTIME\_KEY\_FOREHAND\_SHOT | string | 是 | 正手击球次数。  支持笼式网球。  **起始版本：** 26.0.1。 |
| REALTIME\_KEY\_FOREHAND\_SMASH | string | 是 | 正手高压球次数。  支持笼式网球。  **起始版本：** 26.0.1。 |
| REALTIME\_KEY\_FOREHAND\_DROP | string | 是 | 正手吊小球次数。  支持笼式网球。  **起始版本：** 26.0.1。 |
| REALTIME\_KEY\_FOREHAND\_BAJADA | string | 是 | 正手巴哈达次数。  支持笼式网球。  **起始版本：** 26.0.1。 |
| REALTIME\_KEY\_FOREHAND\_DRIVE | string | 是 | 正手抽球次数。  支持笼式网球。  **起始版本：** 26.0.1。 |
| REALTIME\_KEY\_FOREHAND\_BACKSPIN | string | 是 | 正手下旋球次数。  支持笼式网球。  **起始版本：** 26.0.1。 |
| REALTIME\_KEY\_FOREHAND\_VOLLEY | string | 是 | 正手截击次数。  支持笼式网球。  **起始版本：** 26.0.1。 |
| REALTIME\_KEY\_BACKHAND\_SHOT | string | 是 | 反手击球次数。  支持笼式网球。  **起始版本：** 26.0.1。 |
| REALTIME\_KEY\_BACKHAND\_SMASH | string | 是 | 反手高压球次数。  支持笼式网球。  **起始版本：** 26.0.1。 |
| REALTIME\_KEY\_BACKHAND\_BAJADA | string | 是 | 反手巴哈达次数。  支持笼式网球。  **起始版本：** 26.0.1。 |
| REALTIME\_KEY\_BACKHAND\_DROP | string | 是 | 反手吊小球次数。  支持笼式网球。  **起始版本：** 26.0.1。 |
| REALTIME\_KEY\_BACKHAND\_DRIVE | string | 是 | 反手抽球次数。  支持笼式网球。  **起始版本：** 26.0.1。 |
| REALTIME\_KEY\_BACKHAND\_BACKSPIN | string | 是 | 反手下旋球次数。  支持笼式网球。  **起始版本：** 26.0.1。 |
| REALTIME\_KEY\_BACKHAND\_VOLLEY | string | 是 | 反手截击次数。  支持笼式网球。  **起始版本：** 26.0.1。 |
| REALTIME\_KEY\_MOVEMENT\_DISTANCE | string | 是 | 运动过程中的移动距离，单位：m。  支持笼式网球。  **起始版本：** 26.0.1。 |
| REALTIME\_KEY\_SETS\_WON | string | 是 | 获胜局数。  支持笼式网球。  **起始版本：** 26.0.1。 |
| REALTIME\_KEY\_TOTAL\_SETS | string | 是 | 总局数。  支持笼式网球。  **起始版本：** 26.0.1。 |
