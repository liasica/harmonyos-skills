---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/health-api-healthdatatypes
title: healthDataTypes(运动健康数据类型常量)
breadcrumb: API参考 > 应用服务 > Health Service Kit（运动健康服务） > ArkTS API > 运动健康数据类型常量及模型定义 > healthDataTypes(运动健康数据类型常量)
category: harmonyos-references
scraped_at: 2026-04-28T08:16:50+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:88a64bff50786d9ed4afd07796677feb936cbc2df7d28b9656f4e832d7bc0439
---

本模块提供运动健康数据类型常量。

**起始版本：** 5.0.0(12)

## 导入模块

PhoneTabletWearable

```
1. import { healthStore } from '@kit.HealthServiceKit';
```

说明

此模块为healthStore子模块，需通过healthStore.healthDataTypes方式使用。

## 常量

PhoneTabletWearable

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| BLOOD\_OXYGEN\_SATURATION | [healthStore.DataType](health-api-healthstore.md#datatype) | 血氧数据类型。 |
| BLOOD\_PRESSURE | [healthStore.DataType](health-api-healthstore.md#datatype) | 血压数据类型。 |
| BODY\_TEMPERATURE | [healthStore.DataType](health-api-healthstore.md#datatype) | 体温数据类型。 |
| DAILY\_ACTIVITIES | [healthStore.DataType](health-api-healthstore.md#datatype) | 日常活动数据类型。 |
| EMOTION | [healthStore.DataType](health-api-healthstore.md#datatype) | 情绪数据类型。  **起始版本：** 5.1.0(18) |
| HEART\_RATE | [healthStore.DataType](health-api-healthstore.md#datatype) | 动态心率数据类型。 |
| HEART\_RATE\_VARIABILITY | [healthStore.DataType](health-api-healthstore.md#datatype) | 心率变异性数据类型。  **起始版本：** 5.1.0(18) |
| HEIGHT | [healthStore.DataType](health-api-healthstore.md#datatype) | 身高数据类型。 |
| RESTING\_HEART\_RATE | [healthStore.DataType](health-api-healthstore.md#datatype) | 静息心率数据类型。 |
| SKIN\_TEMPERATURE | [healthStore.DataType](health-api-healthstore.md#datatype) | 皮肤体温数据类型。 |
| STRESS | [healthStore.DataType](health-api-healthstore.md#datatype) | 压力数据类型。 |
| WEIGHT | [healthStore.DataType](health-api-healthstore.md#datatype) | 体重数据类型。 |
| SLEEP\_RECORD | [healthStore.DataType](health-api-healthstore.md#datatype) | 夜间睡眠数据类型。 |
| SLEEP\_NAP\_RECORD | [healthStore.DataType](health-api-healthstore.md#datatype) | 零星小睡数据类型。 |
| WORKOUT | [healthStore.DataType](health-api-healthstore.md#datatype) | 锻炼记录数据类型。 |
| ADVENTURES | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 户外探险子数据类型。 |
| AEROBICS | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 健美操子数据类型。 |
| AIR\_WALKER | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 漫步机子数据类型。 |
| ARCHERY | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 射箭子数据类型。 |
| BADMINTON | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 羽毛球子数据类型。 |
| BALLET | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 芭蕾舞子数据类型。 |
| BASEBALL | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 棒球子数据类型。 |
| BASKETBALL | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 篮球子数据类型。 |
| BEACH\_SOCCER | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 沙滩足球子数据类型。 |
| BEACH\_VOLLEYBALL | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 沙滩排球子数据类型。 |
| BELLY\_DANCE | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 肚皮舞子数据类型。 |
| BIATHLON | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 冬季两项子数据类型。 |
| BMX | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | BMX自行车子数据类型。 |
| BODY\_COMBAT | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 搏击操子数据类型。 |
| BOWLING | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 保龄球子数据类型。 |
| BOXING | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 拳击子数据类型。 |
| BREATH\_HOLDING\_TEST | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 闭气测试子数据类型。 |
| BREATH\_HOLDING\_TRAIN | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 闭气训练子数据类型。 |
| BUNGEE\_JUMPING | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 蹦极子数据类型。 |
| CANOEING | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 皮划艇子数据类型。 |
| CORE\_TRAINING | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 核心训练子数据类型。 |
| CRICKET | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 板球子数据类型。 |
| CROSS\_COUNTRY\_SKIING | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 越野滑雪子数据类型。 |
| CROSS\_FIT | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | Cross fit子数据类型。 |
| CURLING | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 冰壶子数据类型。 |
| CYCLING | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 户外骑行子数据类型。 |
| DANCE | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 舞蹈子数据类型。 |
| DARTS | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 飞镖子数据类型。 |
| DIVING | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 自由潜水子数据类型。 |
| DODGE\_BALL | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 躲避球子数据类型。 |
| DRAGON\_BOAT | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 龙舟子数据类型。 |
| DRIFTING | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 漂流子数据类型。 |
| ELLIPTICAL | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 椭圆机子数据类型。 |
| ESPORTS | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 电子竞技子数据类型。 |
| FENCING | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 击剑子数据类型。 |
| FISHING | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 钓鱼子数据类型。 |
| FREE\_SPARRING | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 自由搏击子数据类型。 |
| FREE\_TRAINING | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 自由训练子数据类型。 |
| FRISBEE | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 飞盘子数据类型。 |
| FUNCTIONAL\_TRAINING | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 功能性训练子数据类型。 |
| GATEBALL | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 门球子数据类型。 |
| GOLF\_COURSE\_MODEL | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 高尔夫场地模式子数据类型。 |
| GOLF\_PRACTICE | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 高尔夫练习场模式子数据类型。 |
| HANDBALL | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 手球子数据类型。 |
| HIIT | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | HIIT子数据类型。 |
| HIKING | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 徒步子数据类型。 |
| HOCKEY | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 曲棍球子数据类型。 |
| HORSE\_RIDING | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 骑马子数据类型。 |
| HULA\_HOOP | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 呼啦圈子数据类型。 |
| HUNTING | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 对战游戏子数据类型。 |
| ICE\_HOCKEY | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 冰球子数据类型。 |
| INDOOR\_CYCLING | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 室内骑行子数据类型。 |
| INDOOR\_RUNNING | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 室内跑步子数据类型。 |
| INDOOR\_WALKING | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 室内步行子数据类型。 |
| JAZZ\_DANCE | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 爵士舞子数据类型。 |
| JUMPING\_ROPE | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 跳绳子数据类型。 |
| KARATE | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 空手道子数据类型。 |
| KENDO | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 剑道子数据类型。 |
| KITE\_FLYING | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 放风筝子数据类型。 |
| LATIN\_DANCE | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 拉丁舞子数据类型。 |
| MARTIAL\_ARTS | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 武术子数据类型。 |
| MOTORBOAT | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 摩托艇子数据类型。 |
| MOUNTAIN\_HIKE | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 登山子数据类型。 |
| OBSTACLE\_RACE | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 障碍赛子数据类型。 |
| OPEN\_WATER\_SWIM | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 开放水域游泳子数据类型。 |
| ORIENTEERING | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 定向越野子数据类型。 |
| PADEL | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 笼式网球子数据类型。 |
| PARACHUTE | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 跳伞子数据类型。 |
| PARALLEL\_BARS | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 双杠子数据类型。 |
| PARKOUR | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 跑酷子数据类型。 |
| PHYSICAL\_TRAINING | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 体能训练子数据类型。 |
| PILATES | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 普拉提子数据类型。 |
| PLAYGROUND\_RACE | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 操场赛跑子数据类型。 |
| PLAZA\_DANCING | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 广场舞子数据类型。 |
| POOL | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 台球子数据类型。 |
| POOL\_SWIM | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 泳池游泳子数据类型。 |
| RACING\_CAR | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 赛车子数据类型。 |
| ROCK\_CLIMBING | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 攀岩子数据类型。 |
| ROLLER\_SKATING | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 轮滑子数据类型。 |
| ROWER | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 划船机子数据类型。 |
| ROWING | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 赛艇子数据类型。 |
| RUGBY | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 橄榄球子数据类型。 |
| RUNNING | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 户外跑步子数据类型。 |
| SAILBOAT | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 帆船子数据类型。 |
| SCUBA\_DIVING | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 水肺潜水子数据类型。 |
| SENSE\_SPORT | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 体感运动子数据类型。 |
| SEPAKTAKRAW | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 藤球子数据类型。 |
| SHUTTLECOCK | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 毽球子数据类型。 |
| SINGLE\_BAR | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 单杠子数据类型。 |
| SKATEBOARD | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 滑板子数据类型。 |
| SKATING | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 滑冰子数据类型。 |
| SKIING | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 滑雪子数据类型。 |
| SLED | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 滑雪橇子数据类型。 |
| SNOWBOARDING | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 单板滑雪子数据类型。 |
| SNOWMOBILE | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 雪地摩托子数据类型。 |
| SOCCER | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 足球子数据类型。 |
| SOFTBALL | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 垒球子数据类型。 |
| SPINNING | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 动感单车子数据类型。 |
| SQUASH | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 壁球子数据类型。 |
| STAIR\_CLIMBING | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 爬楼子数据类型。 |
| STEPPER | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 踏步机子数据类型。 |
| STREET\_DANCE | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 街舞子数据类型。 |
| STRENGTH\_TRAINING | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 力量训练子数据类型。 |
| SUP | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 桨板冲浪子数据类型。 |
| SURFING | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 冲浪子数据类型。 |
| SWINGING | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 秋千子数据类型。 |
| TABLE\_TENNIS | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 乒乓球子数据类型。 |
| TAEKWONDO | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 跆拳道子数据类型。 |
| TAI\_CHI | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 太极拳子数据类型。 |
| TENNIS | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 网球子数据类型。 |
| TRAIL\_RUNNING | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 越野跑子数据类型。 |
| TRIATHLON | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 铁人三项子数据类型。 |
| TUG\_OF\_WAR | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 拔河子数据类型。 |
| VOLLEYBALL | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 排球子数据类型。 |
| WALKING | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 户外步行子数据类型。 |
| YOGA | [healthStore.SubDataType](health-api-healthstore.md#subdatatype) | 瑜伽子数据类型。 |
