---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-particle-animation
title: 粒子动画 (Particle)
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 动画 > 粒子动画 (Particle)
category: harmonyos-references
scraped_at: 2026-04-28T08:02:19+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:ea1de5ce481fc70d9c593b5f649d47a3a54b50709b2e45b94b0a684f6140029c
---

粒子动画是在一定范围内随机生成的大量粒子产生运动而组成的动画。动画元素是一个个粒子，这些粒子可以是圆点、图片。通过对粒子在颜色、透明度、大小、速度、加速度、自旋角度等维度变化做动画，来营造一种氛围感，比如下雪的动效，雪花飘舞就相当于一个个雪花粒子在做动画。

粒子动画的效果通过Particle组件展现。

说明

* 该组件从API version 10开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。
* Particle在息屏之后再次打开或者切换后台再次唤起，粒子动画会自动暂停。

## 子组件

PhonePC/2in1TabletTVWearable

无

## 接口

PhonePC/2in1TabletTVWearable

```
1. interface ParticleInterface {
2. <
3. PARTICLE extends ParticleType,
4. COLOR_UPDATER extends ParticleUpdater,
5. OPACITY_UPDATER extends ParticleUpdater,
6. SCALE_UPDATER extends ParticleUpdater,
7. ACC_SPEED_UPDATER extends ParticleUpdater,
8. ACC_ANGLE_UPDATER extends ParticleUpdater,
9. SPIN_UPDATER extends ParticleUpdater
10. >(particles: Particles<
11. PARTICLE,
12. COLOR_UPDATER,
13. OPACITY_UPDATER,
14. SCALE_UPDATER,
15. ACC_SPEED_UPDATER,
16. ACC_ANGLE_UPDATER,
17. SPIN_UPDATER
18. >): ParticleAttribute;
19. }
```

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| particles | [Particles](ts-particle-animation.md#particles18)<  [PARTICLE](ts-particle-animation.md#particletype),  [COLOR\_UPDATER](ts-particle-animation.md#particleupdater),  [OPACITY\_UPDATER](ts-particle-animation.md#particleupdater),  [SCALE\_UPDATER](ts-particle-animation.md#particleupdater),  [ACC\_SPEED\_UPDATER](ts-particle-animation.md#particleupdater),  [ACC\_ANGLE\_UPDATER](ts-particle-animation.md#particleupdater),  [SPIN\_UPDATER](ts-particle-animation.md#particleupdater)  > | 否 | 否 | 粒子动画的集合，详见[Particles](ts-particle-animation.md#particles18)属性说明。 |

## 属性

PhonePC/2in1TabletTVWearable

除支持[通用属性](ts-component-general-attributes.md)外还支持以下属性：

### disturbanceFields12+

PhonePC/2in1TabletTVWearable

disturbanceFields(fields: Array<DisturbanceFieldOptions>)

设置扰动场。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fields | Array<[DisturbanceFieldOptions](ts-particle-animation.md#disturbancefieldoptions12)> | 是 | 扰动场数组。 |

### emitter12+

PhonePC/2in1TabletTVWearable

emitter(value: Array<EmitterProperty>)

支持发射器位置动态更新

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | Array<[EmitterProperty](ts-particle-animation.md#emitterproperty12)> | 是 | 需要更新的emitter参数数组 |

### rippleFields22+

PhonePC/2in1TabletTVWearable

rippleFields(fields: Array<RippleFieldOptions>|undefined)

设置粒子波动场。波动场会对影响范围内的粒子施加按波形变化的力，产生类似波纹扩散的效果。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fields | Array<[RippleFieldOptions](ts-particle-animation.md#ripplefieldoptions22)>|undefined | 是 | 粒子波动场数组。通过数组形式可以设置多个粒子波动场。当设置为undefined时，表示无波动场。 |

### velocityFields22+

PhonePC/2in1TabletTVWearable

velocityFields(fields: Array<VelocityFieldOptions>|undefined)

设置粒子速度场。速度场会对影响范围内的粒子施加一个力，使粒子在原有速度的基础上叠加速度场指定的速度。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fields | Array<[VelocityFieldOptions](ts-particle-animation.md#velocityfieldoptions22)>|undefined | 是 | 粒子速度场数组。通过数组形式可设置多个粒子速度场。设置为undefined时表示无速度场。 |

## 事件

PhonePC/2in1TabletTVWearable

支持[通用事件](ts-component-general-events.md)。

## ParticleOptions

PhonePC/2in1TabletTVWearable

```
1. interface ParticleOptions<
2. PARTICLE extends ParticleType,
3. COLOR_UPDATER extends ParticleUpdater,
4. OPACITY_UPDATER extends ParticleUpdater,
5. SCALE_UPDATER extends ParticleUpdater,
6. ACC_SPEED_UPDATER extends ParticleUpdater,
7. ACC_ANGLE_UPDATER extends ParticleUpdater,
8. SPIN_UPDATER extends ParticleUpdater
9. > {
10. emitter: EmitterOptions<PARTICLE>;
11. color?: ParticleColorPropertyOptions<COLOR_UPDATER>;
12. opacity?: ParticlePropertyOptions<number, OPACITY_UPDATER>;
13. scale?: ParticlePropertyOptions<number, SCALE_UPDATER>;
14. velocity?: VelocityOptions;
15. acceleration?: AccelerationOptions<ACC_SPEED_UPDATER, ACC_ANGLE_UPDATER>;
16. spin?: ParticlePropertyOptions<number, SPIN_UPDATER>;
17. }
```

设置粒子参数。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| emitter | [EmitterOptions](ts-particle-animation.md#emitteroptions)<[PARTICLE](ts-particle-animation.md#particletype)> | 否 | 否 | 粒子发射器配置。 |
| color | [ParticleColorPropertyOptions](ts-particle-animation.md#particlecolorpropertyoptions)<[COLOR\_UPDATER](ts-particle-animation.md#particleupdater)> | 否 | 是 | 粒子颜色配置。  **说明**：  默认值：{ range:[Color.White,Color.White] } 。图片粒子不支持设置颜色。 |
| opacity | [ParticlePropertyOptions](ts-particle-animation.md#particlepropertyoptions)<number, [OPACITY\_UPDATER](ts-particle-animation.md#particleupdater)> | 否 | 是 | 粒子透明度配置。  默认值：{ range:[1.0,1.0] } |
| scale | [ParticlePropertyOptions](ts-particle-animation.md#particlepropertyoptions)<number, [SCALE\_UPDATER](ts-particle-animation.md#particleupdater)> | 否 | 是 | 粒子大小配置。  默认值：{ range:[1.0,1.0] } |
| velocity | [VelocityOptions](ts-particle-animation.md#velocityoptions18) | 否 | 是 | 粒子速度配置。  **说明**：  speed表示速度大小。angle表示速度的方向（单位为角度），以元素几何中心为坐标原点，水平方向为X轴，正数表示顺时针方向旋转角度。  默认值：{ speed:[0.0,0.0],angle:[0.0,0.0] } |
| acceleration | [AccelerationOptions](ts-particle-animation.md#accelerationoptions18)<[ACC\_SPEED\_UPDATER](ts-particle-animation.md#particleupdater), [ACC\_ANGLE\_UPDATER](ts-particle-animation.md#particleupdater)> | 否 | 是 | 粒子加速度配置。  **说明**：  speed表示加速度大小，angle表示加速度方向（单位为角度）。  默认值：{ speed:{range:[0.0,0.0]},angle:{range:[0.0,0.0]} } |
| spin | [ParticlePropertyOptions](ts-particle-animation.md#particlepropertyoptions)<number, [SPIN\_UPDATER](ts-particle-animation.md#particleupdater)> | 否 | 是 | 粒子自旋角度配置。  默认值：{range:[0.0,0.0]}  方向：正数表示顺时针旋转，负数表示逆时针旋转。 |

## EmitterOptions

PhonePC/2in1TabletTVWearable

```
1. interface EmitterOptions<PARTICLE extends ParticleType> {
2. particle: EmitterParticleOptions<PARTICLE>;
3. emitRate?: number;
4. shape?: ParticleEmitterShape;
5. position?: ParticleTuple<Dimension, Dimension>;
6. size?: ParticleTuple<Dimension, Dimension>;
7. annulusRegion?: ParticleAnnulusRegion;
8. }
```

粒子发射器的配置。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| particle | [EmitterParticleOptions](ts-particle-animation.md#emitterparticleoptions18)<[PARTICLE](ts-particle-animation.md#particletype)> | 否 | 否 | 粒子配置。  -type表示粒子类型，可以选择图片或者是点。  -config表示对应类型的配置。  -config类型和type值有关联：  1. 如果type为ParticleType.POINT，则config类型为[PointParticleParameters](ts-particle-animation.md#pointparticleparameters) 。  2. 如果type为ParticleType.IMAGE，则config类型为[ImageParticleParameters](ts-particle-animation.md#imageparticleparameters) 。  -count表示发射的粒子总数，count取值>=-1，当count为-1表示粒子总数无限大。  -lifetime表示单个粒子的生命周期，默认值1000（即1000ms，1s），lifetime>=-1，当lifetime为-1表示粒子生命周期无限大。当lifetime<-1，取默认值。  **说明**：如果不需要动画一直播放，建议不要将生命周期设置为-1，可能对性能造成较大影响。  lifetimeRange表示粒子生命周期取值范围，设置lifetimeRange后粒子的生命周期为[lifetime-lifetimeRange, lifetime+lifetimeRange]中间的一个随机整数。lifetimeRange默认值为0，取值范围为[0, +∞）。设置为负值时取默认值。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| emitRate | number | 否 | 是 | 发射器发射速率（即每秒发射粒子数）。 默认值：5，小于0时取默认值5。emitRate值超过5000时会极大影响性能，建议设置参数小于5000。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| shape | [ParticleEmitterShape](ts-particle-animation.md#particleemittershape) | 否 | 是 | 发射器形状。  默认值：ParticleEmitterShape.RECTANGLE  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| position | [ParticleTuple](ts-particle-animation.md#particletuple18)<[Dimension](ts-types.md#dimension10), [Dimension](ts-types.md#dimension10)> | 否 | 是 | 发射器位置（距离组件左上角的位置。第一个参数为x方向上的相对偏移，第二个参数为y轴方向相对偏移。）  默认值：[0.0, 0.0]  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| size | [ParticleTuple](ts-particle-animation.md#particletuple18)<[Dimension](ts-types.md#dimension10), [Dimension](ts-types.md#dimension10)> | 否 | 是 | 发射窗口的大小。第一个参数为发射器宽，第二个参数为发射器高。  默认值：['100%','100%'](即发射窗口占满Particle组件)  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| annulusRegion20+ | [ParticleAnnulusRegion](ts-particle-animation.md#particleannulusregion20) | 否 | 是 | 环形发射器参数。需要发射器形状为环形（即shape参数为ParticleEmitterShape.ANNULUS）时才生效，且对于环形发射器，形状信息必须通过annulusRegion参数指定，position和size不生效。  **元服务API：** 从API version 20开始，该接口支持在元服务中使用。 |

## ParticleConfigs

PhonePC/2in1TabletTVWearable

设置粒子配置项。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| [ParticleType.POINT] | [PointParticleParameters](ts-particle-animation.md#pointparticleparameters) | 否 | 否 | 点状粒子配置。 |
| [ParticleType.IMAGE] | [ImageParticleParameters](ts-particle-animation.md#imageparticleparameters) | 否 | 否 | 图片粒子配置。 |

## PointParticleParameters

PhonePC/2in1TabletTVWearable

设置粒子半径。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| radius | [VP](ts-types.md#vp10) | 否 | 否 | 粒子半径。  默认值：0，小于0时取默认值0。 |

## ImageParticleParameters

PhonePC/2in1TabletTVWearable

设置图片选项。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| src | [ResourceStr](ts-types.md#resourcestr) | 否 | 否 | 图片路径，支持本地图片和网络图片，引用方式请参考[加载图片资源](../harmonyos-guides/arkts-graphics-display.md#加载图片资源)。  暂不支持svg图片类型。  src未发生变化时，会优先使用缓存的资源，无法动态切换资源。如需动态切换资源建议切换为不同的src。 |
| size | [ParticleTuple](ts-particle-animation.md#particletuple18)<[Dimension](ts-types.md#dimension10), [Dimension](ts-types.md#dimension10)> | 否 | 否 | 图像尺寸。  默认值：[0, 0] |
| objectFit | [ImageFit](ts-appendix-enums.md#imagefit) | 否 | 是 | 图片显示模式。 |

## ParticleColorPropertyOptions

PhonePC/2in1TabletTVWearable

```
1. interface ParticleColorPropertyOptions<UPDATER extends ParticleUpdater> {
2. range: ParticleTuple<ResourceColor, ResourceColor>;
3. distributionType?: DistributionType;
4. updater?: ParticleColorUpdaterOptions<UPDATER>;
5. }
```

设置粒子颜色属性更新器配置。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| range | [ParticleTuple](ts-particle-animation.md#particletuple18)<[ResourceColor](ts-types.md#resourcecolor), [ResourceColor](ts-types.md#resourcecolor)> | 否 | 否 | 粒子初始颜色区间，粒子发射器生成粒子的初始颜色在range区间随机取值。  默认值：range:[Color.White,Color.White]  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| distributionType12+ | [DistributionType](ts-particle-animation.md#distributiontype12) | 否 | 是 | 粒子初始颜色随机值分布，允许用户选择颜色随机值生成的分布类型，支持均匀分布或正态（高斯）分布。  默认值：DistributionType.UNIFORM  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| updater | [ParticleColorUpdaterOptions](ts-particle-animation.md#particlecolorupdateroptions18)<[UPDATER](ts-particle-animation.md#particleupdater)> | 否 | 是 | 颜色属性变化配置。颜色属性变化类型type有三类：  1、当type为ParticleUpdater.NONE，表示无变化，则config类型为[ParticleColorPropertyUpdaterConfigs](ts-particle-animation.md#particlecolorpropertyupdaterconfigs)[ParticleUpdater.NONE]。  2、type为ParticleUpdater.RANDOM，表示随机变化，则config类型为[ParticleColorPropertyUpdaterConfigs](ts-particle-animation.md#particlecolorpropertyupdaterconfigs)[ParticleUpdater.RANDOM]。  3、type为ParticleUpdater.CURVE,表示按动画曲线变化，则config类型为[ParticleColorPropertyUpdaterConfigs](ts-particle-animation.md#particlecolorpropertyupdaterconfigs)[ParticleUpdater.CURVE]。  默认值：type默认为 ParticleUpdater.NONE。  **说明**：  当type为ParticleUpdater.RANDOM或者ParticleUpdater.CURVE时，updater中颜色配置的优先级高于range中的颜色配置。在updater配置的动画时间周期内，以updater中的颜色配置来变化；在updater配置的动画时间周期外，以range中的颜色配置来变化。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |

## ParticleColorPropertyUpdaterConfigs

PhonePC/2in1TabletTVWearable

设置粒子颜色属性更新器的配置。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| [ParticleUpdater.NONE] | void | 否 | 否 | 无变化。 |
| [ParticleUpdater.RANDOM] | [ParticleColorOptions](ts-particle-animation.md#particlecoloroptions18) | 否 | 否 | 表示变化方式为均匀变化的时候，在区间内随机生成一个差值。r、g、b、a四个颜色通道每秒分别使用差值叠加当前颜色值，生成目标颜色值。实现颜色随机变化的效果。 |
| [ParticleUpdater.CURVE] | Array<[ParticlePropertyAnimation](ts-particle-animation.md#particlepropertyanimation)<[ResourceColor](ts-types.md#resourcecolor)>> | 否 | 否 | 表示变化方式为曲线变化时，颜色变化的配置。数组类型表示当前属性可以设置多段动画，如0ms-3000ms，3000ms-5000ms，5000ms-8000ms分别设置动画。 |

## ParticlePropertyOptions

PhonePC/2in1TabletTVWearable

```
1. interface ParticlePropertyOptions<TYPE, UPDATER extends ParticleUpdater> {
2. range: ParticleTuple<TYPE, TYPE>;
3. updater?: ParticleUpdaterOptions<TYPE, UPDATER>;
4. }
```

设置粒子属性选项。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| range | [ParticleTuple](ts-particle-animation.md#particletuple18)<[TYPE](ts-particle-animation.md#particleupdater), [TYPE](ts-particle-animation.md#particleupdater)> | 否 | 否 | 粒子初始属性值区间，粒子发射器生成粒子的属性值在range区间随机取值。  **说明**  各项属性的非法输入取默认值，当最大值小于最小值的时候取默认区间。TYPE为number。  不同属性的默认值不同：  1、opacity属性：range:[1.0,1.0]，取值范围为[0, 1]，默认值为1.0。  2、scale属性：range:[1.0,1.0]，取值范围为[0, 10000]，默认值为1.0。  3、acceleration加速度speed属性：range:[0.0,0.0]，取值范围为[0, 10000]，默认值为0.0。  4、acceleration加速度angle属性：range:[0.0,0.0]，取值范围为[-10000, 10000]，默认值为0.0。  5、spin属性：range:[0.0,0.0]，取值范围为[-10000, 10000]，默认值为0.0。 |
| updater | [ParticleUpdaterOptions](ts-particle-animation.md#particleupdateroptions18)<[TYPE](ts-particle-animation.md#particleupdater), [UPDATER](ts-particle-animation.md#particleupdater)> | 否 | 是 | 属性变化配置。属性变化类型type有三类：  1、当type为ParticleUpdater.NONE，表示无变化，则config类型为[ParticlePropertyUpdaterConfigs](ts-particle-animation.md#particlepropertyupdaterconfigs)[ParticleUpdater.NONE]。  2、当type为ParticleUpdater.RANDOM，表示变化类型为随机变化，则config类型为[ParticlePropertyUpdaterConfigs](ts-particle-animation.md#particlepropertyupdaterconfigs)[ParticleUpdater.RANDOM]。  3、当type为ParticleUpdater.CURVE，表示变化类型为曲线变化，则config类型为[ParticlePropertyUpdaterConfigs](ts-particle-animation.md#particlepropertyupdaterconfigs)[ParticleUpdater.CURVE]  默认值：type默认为ParticleUpdater.NONE。 |

## ParticlePropertyUpdaterConfigs

PhonePC/2in1TabletTVWearable

```
1. interface ParticlePropertyUpdaterConfigs<T> {
2. [ParticleUpdater.NONE]: void;
3. [ParticleUpdater.RANDOM]: ParticleTuple<T, T>;
4. [ParticleUpdater.CURVE]: Array<ParticlePropertyAnimation<T>>;
5. }
```

设置粒子属性更新器配置。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| [ParticleUpdater.NONE] | void | 否 | 否 | 无变化。 |
| [ParticleUpdater.RANDOM] | [ParticleTuple](ts-particle-animation.md#particletuple18)<T, T> | 否 | 否 | 表示变化方式为匀速变化时，每秒的变化差值为设置区间随机生成的值。  目标属性值为当前属性值叠加变化差值。如当前属性值为0.2，config取[0.1,1.0]:  1、如果变化差值在区间[0.1,1.0]取随机值0.5，则目标属性值为0.2+0.5 = 0.7；  2、变化差值也可以取负值。如当前属性值为0.2，config为 [-3.0,2.0],如果变化差值在区间[-3.0,2.0]取随机值-2.0，则目标属性值为0.2-2.0 = -1.8。  **说明：**  config配置的是变化差值的取值范围，差值的最大最小值没有约束。但是如果当前属性值叠加差值大于属性最大值，目标属性值取属性最大值；如果当前属性值叠加差值小于属性最小值，目标属性值取属性最小值。T为number。  例如：opacity的取值范围[0.0,1.0]则当当前属性值叠加差值超过1.0，则取1.0。 |
| [ParticleUpdater.CURVE] | Array<[ParticlePropertyAnimation](ts-particle-animation.md#particlepropertyanimation)<T>> | 否 | 否 | 表示变化方式为曲线变化时，属性变化的配置。数组类型表示当前属性可以设置多段动画，如0ms-3000ms，3000ms-5000ms，5000ms-8000ms分别设置动画。T为number。 |

## ParticlePropertyAnimation

PhonePC/2in1TabletTVWearable

```
1. interface ParticlePropertyAnimation<T> {
2. from: T;
3. to: T;
4. startMillis: number;
5. endMillis: number;
6. curve?: Curve | ICurve;
7. }
```

设置粒子属性生命周期。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| from | T | 否 | 否 | 属性起始值。非法输入取对应属性的默认值。 |
| to | T | 否 | 否 | 属性目标值。非法输入取对应属性的默认值。 |
| startMillis | number | 否 | 否 | 动画开始时间。  单位：毫秒。  取值范围：[0, +∞)。 |
| endMillis | number | 否 | 否 | 动画结束时间。  单位：毫秒。  取值范围：[0, +∞)。 |
| curve | [Curve](ts-appendix-enums.md#curve) | [ICurve](js-apis-curve.md#icurve9) | 否 | 是 | 设置动画曲线。  默认值：Curve.Linear |

## ParticleType

PhonePC/2in1TabletTVWearable

粒子类型。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| POINT | 'point' | 点状粒子 |
| IMAGE | 'image' | 图片粒子 |

## ParticleEmitterShape

PhonePC/2in1TabletTVWearable

粒子发射器形状。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| RECTANGLE | 'rectangle' | 粒子发射器为矩形。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| CIRCLE | 'circle' | 粒子发射器为圆形。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| ELLIPSE | 'ellipse' | 粒子发射器为椭圆形。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| ANNULUS20+ | 'annulus' | 粒子发射器为环形。  **元服务API：** 从API version 20开始，该接口支持在元服务中使用。 |

## DistributionType12+

PhonePC/2in1TabletTVWearable

初始颜色随机值分布类型。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| UNIFORM | 0 | 初始颜色随机值分布为均匀分布。 |
| GAUSSIAN | 1 | 初始颜色随机值分布为高斯分布。 |

## ParticleUpdater

PhonePC/2in1TabletTVWearable

粒子变化类型。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| NONE | 'none' | 无变化 |
| RANDOM | 'random' | 随机变化 |
| CURVE | 'curve' | 动画曲线变化 |

## DisturbanceFieldOptions12+

PhonePC/2in1TabletTVWearable

设置粒子扰动场参数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| strength | number | 否 | 是 | 场强，表示场从中心向外的排斥力的强度，默认值0。正数表示排斥力方向朝外，负数表示吸引力，方向朝内。  取值范围：(-∞, +∞)。 |
| shape | [DisturbanceFieldShape](ts-particle-animation.md#disturbancefieldshape12) | 否 | 是 | 场的形状。  默认为DisturbanceFieldShape.RECT。 |
| size | [SizeT](js-apis-arkui-graphics.md#sizett12)<number> | 否 | 是 | 场的大小。  默认值 {width:0，height:0}。  width和height的取值范围：[0, +∞)。 |
| position | [PositionT](js-apis-arkui-graphics.md#positiont12)<number> | 否 | 是 | 场的位置。  默认值{x:0，y:0}。  x、y的取值范围：(-∞, +∞)。 |
| feather | number | 否 | 是 | 羽化值，表示场从中心点到场边缘的衰减程度，取值范围0到100的整数，如果0则表示场是一个刚体，所有范围内的粒子都被排斥在外。羽化值越大场的缓和程度越大，场范围内出现越多靠近中心点的粒子。  默认值为0。 |
| noiseScale | number | 否 | 是 | 噪声尺度，用于控制噪声图案的整体大小，取值大于等于0。  默认值1。 |
| noiseFrequency | number | 否 | 是 | 噪声频率，频率越大噪声越细腻，取值大于等于0。  默认值1。 |
| noiseAmplitude | number | 否 | 是 | 噪声振幅，噪声的波动的范围，振幅越大噪音之间差异越大。取值大于等于0。  默认值1。 |

## DisturbanceFieldShape12+

PhonePC/2in1TabletTVWearable

粒子形状。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| RECT | 0 | 长方形。 |
| CIRCLE | 1 | 圆。 |
| ELLIPSE | 2 | 椭圆。 |

## EmitterProperty12+

PhonePC/2in1TabletTVWearable

设置发射器属性。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| index | number | 否 | 否 | 索引，取整，按初始化参数中发射器的数组索引指定对应的发射器。异常默认值为0。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| emitRate | number | 否 | 是 | 发射器发射速率，即每秒发射粒子的数量。  未传入时保持其当前的发射速率， 传入值小于0时取默认值5。emitRate值超过5000时会极大影响性能，建议设置参数小于5000。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| position | [PositionT](js-apis-arkui-graphics.md#positiont12)<number> | 否 | 是 | 发射器位置的数组，只支持number类型。  未传入时保持其当前的发射器位置。需传入两个有效参数，若其中一个为异常值，则position不生效。  x、y的取值范围：(-∞, +∞)。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| size | [SizeT](js-apis-arkui-graphics.md#sizett12)<number> | 否 | 是 | 发射窗口的大小，只支持number类型。  未传入时保持其当前发射窗口大小。需传入两个有效参数且都大于0，若其中一个为异常值，则size不生效。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| annulusRegion20+ | [ParticleAnnulusRegion](ts-particle-animation.md#particleannulusregion20) | 否 | 是 | 环形发射器参数。需要对应index的发射器形状为环形才生效。  **元服务API：** 从API version 20开始，该接口支持在元服务中使用。 |

## ParticleTuple18+

PhonePC/2in1TabletTVWearable

```
1. declare type ParticleTuple<T1, T2> = [T1, T2];
```

粒子元组，表示定义一些动画参数的类型。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 说明 |
| --- | --- |
| [T1, T2] | 一些动画参数的类型，可能是任何类型。 |

## Particles18+

PhonePC/2in1TabletTVWearable

```
1. interface Particles<
2. PARTICLE extends ParticleType,
3. COLOR_UPDATER extends ParticleUpdater,
4. OPACITY_UPDATER extends ParticleUpdater,
5. SCALE_UPDATER extends ParticleUpdater,
6. ACC_SPEED_UPDATER extends ParticleUpdater,
7. ACC_ANGLE_UPDATER extends ParticleUpdater,
8. SPIN_UPDATER extends ParticleUpdater
9. > {
10. particles: Array<
11. ParticleOptions<
12. PARTICLE,
13. COLOR_UPDATER,
14. OPACITY_UPDATER,
15. SCALE_UPDATER,
16. ACC_SPEED_UPDATER,
17. ACC_ANGLE_UPDATER,
18. SPIN_UPDATER
19. >
20. >;
21. }
```

粒子动画的集合。

说明

为规范匿名对象的定义，API 18版本修改了此处的元素定义。其中，保留了历史匿名对象的起始版本信息，会出现外层元素@since版本号高于内层元素版本号的情况，但这不影响接口的使用。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| particles10+ | Array<  ParticleOptions<  PARTICLE,  COLOR\_UPDATER,  OPACITY\_UPDATER,  SCALE\_UPDATER,  ACC\_SPEED\_UPDATER,  ACC\_ANGLE\_UPDATER,  SPIN\_UPDATER  >  > | 否 | 否 | 粒子动画的集合。每一个的粒子动画（[ParticleOptions](ts-particle-animation.md#particleoptions)）包含粒子发射，同时可配置粒子的颜色、透明度、大小、速度、加速度与旋转速度，旋转速度，详见[ParticleOptions](ts-particle-animation.md#particleoptions)属性说明。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |

## VelocityOptions18+

PhonePC/2in1TabletTVWearable

粒子速度配置。

说明

为规范匿名对象的定义，API 18版本修改了此处的元素定义。其中，保留了历史匿名对象的起始版本信息，会出现外层元素@since版本号高于内层元素版本号的情况，但这不影响接口的使用。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| speed10+ | [ParticleTuple](ts-particle-animation.md#particletuple18)<number, number> | 否 | 否 | 表示速度大小。  默认值：{range:[0.0,0.0]}  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| angle10+ | [ParticleTuple](ts-particle-animation.md#particletuple18)<number, number> | 否 | 否 | 表示速度的方向（单位为角度）。以元素几何中心为坐标原点，水平方向为X轴，正数表示顺时针方向旋转角度。  默认值：{range:[0.0,0.0]}  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |

## AccelerationOptions18+

PhonePC/2in1TabletTVWearable

```
1. declare interface AccelerationOptions<
2. ACC_SPEED_UPDATER extends ParticleUpdater,
3. ACC_ANGLE_UPDATER extends ParticleUpdater
4. > {
5. speed?: ParticlePropertyOptions<number, ACC_SPEED_UPDATER>;
6. angle?: ParticlePropertyOptions<number, ACC_ANGLE_UPDATER>;
7. }
```

粒子加速度配置。

说明

为规范匿名对象的定义，API 18版本修改了此处的元素定义。其中，保留了历史匿名对象的起始版本信息，会出现外层元素@since版本号高于内层元素版本号的情况，但这不影响接口的使用。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| speed10+ | [ParticlePropertyOptions](ts-particle-animation.md#particlepropertyoptions)<number, [ACC\_SPEED\_UPDATER](ts-particle-animation.md#particleupdater)> | 否 | 是 | 表示加速度大小。  默认值：{range:[0.0,0.0]}  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| angle10+ | [ParticlePropertyOptions](ts-particle-animation.md#particlepropertyoptions)<number, [ACC\_ANGLE\_UPDATER](ts-particle-animation.md#particleupdater)> | 否 | 是 | 表示加速度方向（单位为角度）。  默认值：{range:[0.0,0.0]}  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |

## EmitterParticleOptions18+

PhonePC/2in1TabletTVWearable

```
1. interface EmitterParticleOptions<PARTICLE extends ParticleType> {
2. type: PARTICLE;
3. config: ParticleConfigs[PARTICLE];
4. count: number;
5. lifetime?: number;
6. lifetimeRange?: number;
7. }
```

粒子配置。

说明

为规范匿名对象的定义，API 18版本修改了此处的元素定义。其中，保留了历史匿名对象的起始版本信息，会出现外层元素@since版本号高于内层元素版本号的情况，但这不影响接口的使用。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| type10+ | [PARTICLE](ts-particle-animation.md#particletype) | 否 | 否 | 表示粒子类型，可以选择图片或者是点。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| config10+ | [ParticleConfigs](ts-particle-animation.md#particleconfigs)[PARTICLE] | 否 | 否 | 表示对应类型的配置。  config类型和type值有关联：  1. 如果type为ParticleType.POINT，则config类型为[PointParticleParameters](ts-particle-animation.md#pointparticleparameters) 。  2. 如果type为ParticleType.IMAGE，则config类型为[ImageParticleParameters](ts-particle-animation.md#imageparticleparameters) 。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| count10+ | number | 否 | 否 | 表示发射的粒子总数，count取值>=-1,当count为-1表示粒子总数无限大。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| lifetime10+ | number | 否 | 是 | 表示单个粒子的生命周期，默认值1000（即1000ms，1s），lifetime>=-1。当lifetime为-1表示粒子生命周期无限大。当lifetime<-1，取默认值。  **说明**：如果不需要动画一直播放，建议不要将生命周期设置为-1，可能对性能造成较大影响。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| lifetimeRange12+ | number | 否 | 是 | 表示粒子生命周期取值范围，设置lifetimeRange后粒子的生命周期为[lifetime-lifetimeRange, lifetime+lifetimeRange]中间的一个随机整数。lifetimeRange默认值为0，取值范围为0到正无穷。设置为负值时取默认值。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |

## ParticleUpdaterOptions18+

PhonePC/2in1TabletTVWearable

```
1. interface ParticleUpdaterOptions<TYPE, UPDATER extends ParticleUpdater> {
2. type: UPDATER;
3. config: ParticlePropertyUpdaterConfigs<TYPE>[UPDATER];
4. }
```

颜色属性变化配置。

说明

为规范匿名对象的定义，API 18版本修改了此处的元素定义。其中，保留了历史匿名对象的起始版本信息，会出现外层元素@since版本号高于内层元素版本号的情况，但这不影响接口的使用。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| type10+ | [UPDATER](ts-particle-animation.md#particleupdater) | 否 | 否 | 表示颜色属性变化类型。  默认值：type默认为ParticleUpdater.NONE。 **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| config10+ | [ParticlePropertyUpdaterConfigs](ts-particle-animation.md#particlepropertyupdaterconfigs)<[TYPE](ts-particle-animation.md#particleupdater)>[[UPDATER](ts-particle-animation.md#particleupdater)] | 否 | 否 | 属性变化配置。属性变化类型type有三类：  1、当type为ParticleUpdater.NONE，表示无变化，则config类型为[ParticlePropertyUpdaterConfigs](ts-particle-animation.md#particlepropertyupdaterconfigs)[ParticleUpdater.NONE]。  2、当type为ParticleUpdater.RANDOM，表示变化类型为随机变化，则config类型为[ParticlePropertyUpdaterConfigs](ts-particle-animation.md#particlepropertyupdaterconfigs)[ParticleUpdater.RANDOM]。  3、当type为ParticleUpdater.CURVE，表示变化类型为曲线变化，则config类型为[ParticlePropertyUpdaterConfigs](ts-particle-animation.md#particlepropertyupdaterconfigs)[ParticleUpdater.CURVE]。 **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |

## ParticleColorUpdaterOptions18+

PhonePC/2in1TabletTVWearable

```
1. interface ParticleColorUpdaterOptions<UPDATER extends ParticleUpdater> {
2. type: UPDATER;
3. config: ParticleColorPropertyUpdaterConfigs[UPDATER];
4. }
```

颜色属性变化配置。

说明

为规范匿名对象的定义，API 18版本修改了此处的元素定义。其中，保留了历史匿名对象的起始版本信息，会出现外层元素@since版本号高于内层元素版本号的情况，但这不影响接口的使用。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| type10+ | [UPDATER](ts-particle-animation.md#particleupdater) | 否 | 否 | 表示颜色属性变化类型。  默认值：type默认为 ParticleUpdater.NONE。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| config10+ | [ParticleColorPropertyUpdaterConfigs](ts-particle-animation.md#particlecolorpropertyupdaterconfigs)[[UPDATER](ts-particle-animation.md#particleupdater)] | 否 | 否 | 颜色属性变化类型type有三类：  1、当type为ParticleUpdater.NONE，表示无变化，则config类型为[ParticleColorPropertyUpdaterConfigs](ts-particle-animation.md#particlecolorpropertyupdaterconfigs)[ParticleUpdater.NONE]。  2、type为ParticleUpdater.RANDOM，表示随机变化，则config类型为[ParticleColorPropertyUpdaterConfigs](ts-particle-animation.md#particlecolorpropertyupdaterconfigs)[ParticleUpdater.RANDOM]。  3、type为ParticleUpdater.CURVE,表示按动画曲线变化，则config类型为[ParticleColorPropertyUpdaterConfigs](ts-particle-animation.md#particlecolorpropertyupdaterconfigs)[ParticleUpdater.CURVE]。  **说明**：  当type为ParticleUpdater.RANDOM或者ParticleUpdater.CURVE时，updater中颜色配置的优先级高于range中的颜色配置。在updater配置的动画时间周期内，以updater中的颜色配置来变化；在updater配置的动画时间周期前，以range中的颜色配置来变化。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |

## ParticleColorOptions18+

PhonePC/2in1TabletTVWearable

颜色变化方式为均匀变化的时候，在区间内随机生成一个差值。r、g、b、a四个颜色通道每秒分别使用差值叠加当前颜色值，生成目标颜色值。实现颜色随机变化的效果。

说明

为规范匿名对象的定义，API 18版本修改了此处的元素定义。其中，保留了历史匿名对象的起始版本信息，会出现外层元素@since版本号高于内层元素版本号的情况，但这不影响接口的使用。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| r10+ | [ParticleTuple](ts-particle-animation.md#particletuple18)<number, number> | 否 | 否 | r颜色通道的差值。 **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| g10+ | [ParticleTuple](ts-particle-animation.md#particletuple18)<number, number> | 否 | 否 | g颜色通道的差值。 **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| b10+ | [ParticleTuple](ts-particle-animation.md#particletuple18)<number, number> | 否 | 否 | b颜色通道的差值。 **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| a10+ | [ParticleTuple](ts-particle-animation.md#particletuple18)<number, number> | 否 | 否 | a颜色通道的差值。 **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |

## ParticleAnnulusRegion20+

PhonePC/2in1TabletTVWearable

用于设置环形发射器区域的配置信息。

说明

* outerRadius、innerRadius小于零或使用百分比单位时，会按零进行处理。
* 当outerRadius小于innerRadius时（即外圆半径小于内圆半径时），会将当前较小的值作为新的内圆半径，将较大的值作为新的外圆半径。
* 当endAngle小于startAngle时（即结束角度小于起始角度时），会将当前较小的值作为新的起始角度，将较大的值作为新的结束角度。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/qfwQY0aYTqqKTY1sEGosBA/zh-cn_image_0000002583440075.png?HW-CC-KV=V1&HW-CC-Date=20260428T000217Z&HW-CC-Expire=86400&HW-CC-Sign=E7985903570B0F0DA3DD19B0161A26BA00995923635D414175A0C60B2EEA4F4A)

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| center | [PositionT](js-apis-arkui-graphics.md#positiont12)<[LengthMetrics](js-apis-arkui-graphics.md#lengthmetrics12)> | 否 | 是 | 圆环的圆心坐标，组件的左上角为坐标原点。默认值：{x:LengthMetrics.percent(0.5),y:LengthMetrics.percent(0.5)} |
| outerRadius | [LengthMetrics](js-apis-arkui-graphics.md#lengthmetrics12) | 否 | 否 | 圆环的外圆半径。 |
| innerRadius | [LengthMetrics](js-apis-arkui-graphics.md#lengthmetrics12) | 否 | 否 | 圆环的内圆半径。 |
| startAngle | number | 否 | 是 | 圆环的起始角度。  单位：度  默认值：0 |
| endAngle | number | 否 | 是 | 圆环的结束角度。  单位：度  默认值：360 |

## Vector2T<T>22+

PhonePC/2in1TabletTVWearable

type Vector2T<T> = Vector2T<T>

定义Vector2T类型。其中Vector2T类型包含x和y两个属性值。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 说明 |
| --- | --- |
| [Vector2T<T>](js-apis-arkui-graphics.md#vector2tt12) | 用于表示T类型的包含x和y两个值的向量。x表示向量x轴方向的值。y表示向量y轴方向的值。  单位：vp |

## FieldRegion22+

PhonePC/2in1TabletTVWearable

用于设置粒子场的区域信息。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**模型约束：** 此接口仅可在Stage模型下使用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| shape | [DisturbanceFieldShape](ts-particle-animation.md#disturbancefieldshape12) | 否 | 是 | 粒子场的区域形状。  默认值：DisturbanceFieldShape.RECT |
| position | [PositionT](js-apis-arkui-graphics.md#positiont12)<number> | 否 | 是 | 粒子场的区域中心位置。坐标单位为vp。  默认值：{x:0, y:0} |
| size | [SizeT](js-apis-arkui-graphics.md#sizett12)<number> | 否 | 是 | 粒子场的区域大小。值的单位为vp。  默认值：{width:0, height:0}  取值范围：  width：[0, +∞)  height：[0, +∞)  当size的width（或height）设置为负值时取width（或height）的默认值。 |

## RippleFieldOptions22+

PhonePC/2in1TabletTVWearable

用于描述粒子波动场信息的参数。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**模型约束：** 此接口仅可在Stage模型下使用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| amplitude | number | 否 | 是 | 描述粒子波动场波的幅值。幅值越大，波动场的力越大。  取值范围：[0, +∞)  默认值：0  设置为负值时取默认值。 |
| wavelength | number | 否 | 是 | 描述粒子波动场的波长，即一个波周期的变化距离。波长越大，则随距离的变化，波的变化越慢，波动越不明显。  取值范围：[0, +∞)  默认值：0  设置为负值时取默认值。 |
| waveSpeed | number | 否 | 是 | 描述粒子波动场的波速。波速越大，则随时间的变化，波的变化越快，波动越明显。  取值范围：[0, +∞)  默认值：0  设置为负值时取默认值。 |
| attenuation | number | 否 | 是 | 描述粒子波动场波的衰减系数。衰减系数越大，则随时间的变化，波的衰减越快。  取值范围：[0, 1]  默认值：0.0  设置的数值不在范围内时取默认值。 |
| center | [PositionT](js-apis-arkui-graphics.md#positiont12)<number> | 否 | 是 | 粒子波动场产生力的中心位置。组件的左上角为坐标原点。坐标单位为vp。  默认值：{x:0, y:0} |
| region | [FieldRegion](ts-particle-animation.md#fieldregion22) | 否 | 是 | 粒子波动场影响的区域信息，其中区域信息包括区域形状、区域大小以及区域中心位置。  默认值：{shape:DisturbanceFieldShape.RECT, position:{x:0, y:0}, size:{width:0, height:0}} |

## VelocityFieldOptions22+

PhonePC/2in1TabletTVWearable

用于描述粒子速度场信息的参数。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| velocity | [Vector2T](ts-particle-animation.md#vector2tt22)<number> | 否 | 是 | 粒子速度场的各方向速度值。粒子只有在速度场作用范围内时获得该速度，离开速度场范围后不受该速度场影响，不获得该额外的速度。  默认值：{x:0, y:0} |
| region | [FieldRegion](ts-particle-animation.md#fieldregion22) | 否 | 是 | 粒子速度场影响的区域信息，其中区域信息包括区域形状、区域大小以及区域中心位置。  默认值：{shape:DisturbanceFieldShape.RECT, position:{x:0, y:0}, size:{width:0, height:0}} |

## 示例

PhonePC/2in1TabletTVWearable

### 示例1（圆形初始化粒子）

描述粒子动画基础用法，通过圆形初始化粒子。

```
1. @Entry
2. @Component
3. struct ParticleExample {
4. build() {
5. Stack() {
6. Text()
7. .width(300).height(300).backgroundColor(Color.Black)
8. Particle({
9. particles: [
10. {
11. emitter: {
12. particle: {
13. type: ParticleType.POINT, // 粒子类型
14. config: {
15. radius: 10 // 圆点半径
16. },
17. count: 500, // 粒子总数
18. lifetime: 10000, // 粒子生命周期，单位ms
19. lifetimeRange: 100 // 粒子生命周期取值范围，单位ms
20. },
21. emitRate: 10, // 每秒发射粒子数
22. position: [0, 0],
23. shape: ParticleEmitterShape.RECTANGLE // 发射器形状
24. },
25. color: {
26. range: [Color.Red, Color.Yellow], // 初始颜色范围
27. distributionType: DistributionType.GAUSSIAN, // 初始颜色随机值分布
28. updater: {
29. type: ParticleUpdater.CURVE, // 变化方式为曲线变化
30. config: [
31. {
32. from: Color.White, // 变化起始值
33. to: Color.Pink, // 变化终点值
34. startMillis: 0, // 开始时间
35. endMillis: 3000, // 结束时间
36. curve: Curve.EaseIn // 变化曲线
37. },
38. {
39. from: Color.Pink,
40. to: Color.Orange,
41. startMillis: 3000,
42. endMillis: 5000,
43. curve: Curve.EaseIn
44. },
45. {
46. from: Color.Orange,
47. to: Color.Pink,
48. startMillis: 5000,
49. endMillis: 8000,
50. curve: Curve.EaseIn
51. },
52. ]
53. }
54. },
55. opacity: {
56. range: [0.0, 1.0], // 粒子透明度的初始值从【0.0到1.0】随机产生
57. updater: {
58. type: ParticleUpdater.CURVE,
59. config: [
60. {
61. from: 0.0,
62. to: 1.0,
63. startMillis: 0,
64. endMillis: 3000,
65. curve: Curve.EaseIn
66. },
67. {
68. from: 1.0,
69. to: 0.0,
70. startMillis: 5000,
71. endMillis: 10000,
72. curve: Curve.EaseIn
73. }
74. ]
75. }
76. },
77. scale: {
78. range: [0.0, 0.0],
79. updater: {
80. type: ParticleUpdater.CURVE,
81. config: [
82. {
83. from: 0.0,
84. to: 0.5,
85. startMillis: 0,
86. endMillis: 3000,
87. curve: Curve.EaseIn
88. }
89. ]
90. }
91. },
92. acceleration: {
93. // 加速度的配置，从大小和方向两个维度变化，speed表示加速度大小，angle表示加速度方向
94. speed: {
95. range: [3, 9],
96. updater: {
97. type: ParticleUpdater.RANDOM, // Speed的变化方式是随机变化
98. config: [1, 20]
99. }
100. },
101. angle: {
102. range: [90, 90]
103. }
104. }

106. }
107. ]
108. }).width(300).height(300)
109. }.width('100%').height('100%').align(Alignment.Center)
110. }
111. }
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/Animation/entry/src/main/ets/pages/particle/template1/Index.ets#L15-L127)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cb/v3/g9UqsKmqS0K4YKHswK6Ipg/zh-cn_image_0000002552960030.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000217Z&HW-CC-Expire=86400&HW-CC-Sign=DB335B7CCF0E30C089793B8A80B1B8997C142AB017ECCB218E99A168163E39AD)

### 示例2（图片初始化粒子）

描述粒子动画基础用法，通过图片初始化粒子。

```
1. @Entry
2. @Component
3. struct ParticleExample {
4. @State
5. myCount: number = 100
6. flag: boolean = false;

8. build() {
9. Column() {
10. Stack() {
11. Particle({
12. particles: [
13. {
14. emitter: {
15. particle: {
16. type: ParticleType.IMAGE,
17. config: {
18. src: $r("app.media.book"),
19. size: [10, 10]
20. },
21. count: this.myCount,
22. lifetime: 10000,
23. lifetimeRange: 100
24. },
25. emitRate: 3,
26. shape: ParticleEmitterShape.CIRCLE
27. },
28. color: {
29. range: [Color.White, Color.White]
30. },
31. opacity: {
32. range: [1.0, 1.0],
33. updater: {
34. type: ParticleUpdater.CURVE,
35. config: [
36. {
37. from: 0,
38. to: 1.0,
39. startMillis: 0,
40. endMillis: 6000
41. },
42. {
43. from: 1.0,
44. to: 0,
45. startMillis: 6000,
46. endMillis: 10000
47. }
48. ]
49. }
50. },
51. scale: {
52. range: [0.1, 1.0],
53. updater: {
54. type: ParticleUpdater.CURVE,
55. config: [
56. {
57. from: 0,
58. to: 1.5,
59. startMillis: 0,
60. endMillis: 8000,
61. curve: Curve.EaseIn
62. }

64. ]
65. }
66. },
67. acceleration: {
68. speed: {
69. range: [3, 9],
70. updater: {
71. type: ParticleUpdater.CURVE,
72. config: [
73. {
74. from: 10,
75. to: 20,
76. startMillis: 0,
77. endMillis: 3000,
78. curve: Curve.EaseIn
79. },
80. {
81. from: 10,
82. to: 2,
83. startMillis: 3000,
84. endMillis: 8000,
85. curve: Curve.EaseIn
86. }
87. ]
88. }
89. },
90. angle: {
91. range: [0, 180],
92. updater: {
93. type: ParticleUpdater.CURVE,
94. config: [{
95. from: 1,
96. to: 2,
97. startMillis: 0,
98. endMillis: 1000,
99. curve: Curve.EaseIn
100. },
101. {
102. from: 50,
103. to: -50,
104. startMillis: 1000,
105. endMillis: 3000,
106. curve: Curve.EaseIn
107. },
108. {
109. from: 3,
110. to: 5,
111. startMillis: 3000,
112. endMillis: 8000,
113. curve: Curve.EaseIn
114. }
115. ]
116. }
117. }
118. },
119. spin: {
120. range: [0.1, 1.0],
121. updater: {
122. type: ParticleUpdater.CURVE,
123. config: [
124. {
125. from: 0,
126. to: 360,
127. startMillis: 0,
128. endMillis: 8000,
129. curve: Curve.EaseIn
130. }
131. ]
132. }
133. },
134. }
135. , {
136. emitter: {
137. particle: {
138. type: ParticleType.IMAGE,
139. config: {
140. src: $r('app.media.heart'),
141. size: [10, 10]
142. },
143. count: this.myCount,
144. lifetime: 10000,
145. lifetimeRange: 100
146. },
147. emitRate: 3,
148. shape: ParticleEmitterShape.CIRCLE
149. },
150. color: {
151. range: [Color.White, Color.White]
152. },
153. opacity: {
154. range: [1.0, 1.0],
155. updater: {
156. type: ParticleUpdater.CURVE,
157. config: [
158. {
159. from: 0,
160. to: 1.0,
161. startMillis: 0,
162. endMillis: 6000
163. },
164. {
165. from: 1.0,
166. to: 0,
167. startMillis: 6000,
168. endMillis: 10000
169. }
170. ]
171. }
172. },
173. scale: {
174. range: [0.1, 1.0],
175. updater: {
176. type: ParticleUpdater.CURVE,
177. config: [
178. {
179. from: 0,
180. to: 2.0,
181. startMillis: 0,
182. endMillis: 10000,
183. curve: Curve.EaseIn
184. }

186. ]
187. }
188. },
189. acceleration: {
190. speed: {
191. range: [3, 9],
192. updater: {
193. type: ParticleUpdater.CURVE,
194. config: [
195. {
196. from: 10,
197. to: 20,
198. startMillis: 0,
199. endMillis: 3000,
200. curve: Curve.EaseIn
201. },
202. {
203. from: 10,
204. to: 2,
205. startMillis: 3000,
206. endMillis: 8000,
207. curve: Curve.EaseIn
208. }
209. ]
210. }
211. },
212. angle: {
213. range: [0, 180],
214. updater: {
215. type: ParticleUpdater.CURVE,
216. config: [{
217. from: 1,
218. to: 2,
219. startMillis: 0,
220. endMillis: 1000,
221. curve: Curve.EaseIn
222. },
223. {
224. from: 50,
225. to: -50,
226. startMillis: 0,
227. endMillis: 3000,
228. curve: Curve.EaseIn
229. },
230. {
231. from: 3,
232. to: 5,
233. startMillis: 3000,
234. endMillis: 10000,
235. curve: Curve.EaseIn
236. }
237. ]
238. }
239. }
240. },
241. spin: {
242. range: [0.1, 1.0],
243. updater: {
244. type: ParticleUpdater.CURVE,
245. config: [
246. {
247. from: 0,
248. to: 360,
249. startMillis: 0,
250. endMillis: 10000,
251. curve: Curve.EaseIn
252. }
253. ]
254. }
255. },
256. }, {
257. emitter: {
258. particle: {
259. type: ParticleType.IMAGE,
260. config: {
261. src: $r('app.media.sun'),
262. size: [10, 10]
263. },
264. count: this.myCount,
265. lifetime: 10000,
266. lifetimeRange: 100
267. },
268. emitRate: 3,
269. shape: ParticleEmitterShape.CIRCLE
270. },
271. color: {
272. range: [Color.White, Color.White]
273. },
274. opacity: {
275. range: [1.0, 1.0],
276. updater: {
277. type: ParticleUpdater.CURVE,
278. config: [
279. {
280. from: 0,
281. to: 1.0,
282. startMillis: 0,
283. endMillis: 6000
284. },
285. {
286. from: 1.0,
287. to: 0,
288. startMillis: 6000,
289. endMillis: 10000
290. }
291. ]
292. }
293. },
294. scale: {
295. range: [0.1, 1.0],
296. updater: {
297. type: ParticleUpdater.CURVE,
298. config: [
299. {
300. from: 0,
301. to: 2.0,
302. startMillis: 0,
303. endMillis: 10000,
304. curve: Curve.EaseIn
305. }

307. ]
308. }
309. },
310. acceleration: {
311. speed: {
312. range: [3, 9],
313. updater: {
314. type: ParticleUpdater.CURVE,
315. config: [
316. {
317. from: 10,
318. to: 20,
319. startMillis: 0,
320. endMillis: 3000,
321. curve: Curve.EaseIn
322. },
323. {
324. from: 10,
325. to: 2,
326. startMillis: 3000,
327. endMillis: 8000,
328. curve: Curve.EaseIn
329. }
330. ]
331. }
332. },
333. angle: {
334. range: [0, 180],
335. updater: {
336. type: ParticleUpdater.CURVE,
337. config: [{
338. from: 1,
339. to: 2,
340. startMillis: 0,
341. endMillis: 1000,
342. curve: Curve.EaseIn
343. },
344. {
345. from: 50,
346. to: -50,
347. startMillis: 1000,
348. endMillis: 3000,
349. curve: Curve.EaseIn
350. },
351. {
352. from: 3,
353. to: 5,
354. startMillis: 3000,
355. endMillis: 8000,
356. curve: Curve.EaseIn
357. }
358. ]
359. }
360. }
361. },
362. spin: {
363. range: [0.1, 1.0],
364. updater: {
365. type: ParticleUpdater.CURVE,
366. config: [
367. {
368. from: 0,
369. to: 360,
370. startMillis: 0,
371. endMillis: 10000,
372. curve: Curve.EaseIn
373. }
374. ]
375. }
376. },
377. }
378. ]
379. }).width(300).height(300)

381. }.width(500).height(500).align(Alignment.Center)
382. }.width("100%").height("100%")

384. }
385. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cc/v3/jhWW9iH3QUKOcdaTr0vK3w/zh-cn_image_0000002583480031.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000217Z&HW-CC-Expire=86400&HW-CC-Sign=7BBBCF7111B5CFF26C441B50AAF96E9DAD88BA62233BC869632DAAA47DB800BB)

### 示例3（粒子扰动场的干扰下运动轨迹发生变化）

该示例主要演示如何通过粒子扰动场的干扰下来实现运动轨迹发生变化的效果。

```
1. @Entry
2. @Component
3. struct ParticleExample3 {
4. build() {
5. Stack() {
6. Text()
7. .width(300).height(300).backgroundColor(Color.Black)
8. Particle({
9. particles: [
10. {
11. emitter: {
12. particle: {
13. type: ParticleType.POINT, // 粒子类型
14. config: {
15. radius: 10 // 圆点半径
16. },
17. count: 500, // 粒子总数
18. lifetime: 10000 // 粒子生命周期，单位ms
19. },
20. emitRate: 10, // 每秒发射粒子数
21. position: [0, 0],
22. shape: ParticleEmitterShape.RECTANGLE // 发射器形状
23. },
24. color: {
25. range: [Color.Red, Color.Yellow], // 初始颜色范围
26. updater: {
27. type: ParticleUpdater.CURVE, // 变化方式为曲线变化
28. config: [
29. {
30. from: Color.White, // 变化起始值
31. to: Color.Pink, // 变化终点值
32. startMillis: 0, // 开始时间
33. endMillis: 3000, // 结束时间
34. curve: Curve.EaseIn // 变化曲线
35. },
36. {
37. from: Color.Pink,
38. to: Color.Orange,
39. startMillis: 3000,
40. endMillis: 5000,
41. curve: Curve.EaseIn
42. },
43. {
44. from: Color.Orange,
45. to: Color.Pink,
46. startMillis: 5000,
47. endMillis: 8000,
48. curve: Curve.EaseIn
49. },
50. ]
51. }
52. },
53. opacity: {
54. range: [0.0, 1.0], // 粒子透明度的初始值从[0.0,1.0]随机产生
55. updater: {
56. type: ParticleUpdater.CURVE,
57. config: [
58. {
59. from: 0.0,
60. to: 1.0,
61. startMillis: 0,
62. endMillis: 3000,
63. curve: Curve.EaseIn
64. },
65. {
66. from: 1.0,
67. to: 0.0,
68. startMillis: 5000,
69. endMillis: 10000,
70. curve: Curve.EaseIn
71. }
72. ]
73. }
74. },
75. scale: {
76. range: [0.0, 0.0],
77. updater: {
78. type: ParticleUpdater.CURVE,
79. config: [
80. {
81. from: 0.0,
82. to: 0.5,
83. startMillis: 0,
84. endMillis: 3000,
85. curve: Curve.EaseIn
86. }
87. ]
88. }
89. },
90. acceleration: {
91. // 加速度的配置，从大小和方向两个维度变化，speed表示加速度大小，angle表示加速度方向
92. speed: {
93. range: [3, 9],
94. updater: {
95. type: ParticleUpdater.RANDOM,
96. config: [1, 20]
97. }
98. },
99. angle: {
100. range: [90, 90]
101. }
102. }

104. }
105. ]
106. }).width(300).height(300).disturbanceFields([{
107. strength: 10,
108. shape: DisturbanceFieldShape.RECT,
109. size: { width: 100, height: 100 },
110. position: { x: 100, y: 100 },
111. feather: 15,
112. noiseScale: 10,
113. noiseFrequency: 15,
114. noiseAmplitude: 5
115. }])
116. }.width('100%').height('100%').align(Alignment.Center)
117. }
118. }
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/Animation/entry/src/main/ets/pages/particle/template3/Index.ets#L15-L134)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/15/v3/fOXGJRwSTF-9CtFLb9w5hw/zh-cn_image_0000002552800382.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000217Z&HW-CC-Expire=86400&HW-CC-Sign=DA0B46C8EE8CA66D99A5BEACCE0999472065A4D60AF685DE161BF622FBB304BF)

### 示例4（调整粒子发射器位置）

通过emitter()调整粒子发射器的位置。

```
1. @Entry
2. @Component
3. struct ParticleExample4 {
4. @State emitterProperties: Array<EmitterProperty> = [
5. {
6. index: 0,
7. emitRate: 100,
8. position: { x: 60, y: 80 },
9. size: { width: 200, height: 200 }
10. }
11. ];

13. build() {
14. Stack() {
15. Text()
16. .width(300).height(300).backgroundColor(Color.Black)
17. Particle({
18. particles: [
19. {
20. emitter: {
21. particle: {
22. type: ParticleType.POINT, // 粒子类型
23. config: {
24. radius: 5 // 圆点半径
25. },
26. count: 400, // 粒子总数
27. lifetime: -1 // 粒子的生命周期，-1表示粒子生命周期无限大
28. },
29. emitRate: 10, // 每秒发射粒子数
30. position: [0, 0], // 粒子发射位置
31. shape: ParticleEmitterShape.CIRCLE // 发射器形状
32. },
33. color: {
34. range: [Color.Red, Color.Yellow], // 初始颜色范围
35. updater: {
36. type: ParticleUpdater.CURVE, // 变化方式为曲线变化
37. config: [
38. {
39. from: Color.White,
40. to: Color.Pink,
41. startMillis: 0,
42. endMillis: 3000,
43. curve: Curve.EaseIn
44. },
45. {
46. from: Color.Pink,
47. to: Color.Orange,
48. startMillis: 3000,
49. endMillis: 5000,
50. curve: Curve.EaseIn
51. },
52. {
53. from: Color.Orange,
54. to: Color.Pink,
55. startMillis: 5000,
56. endMillis: 8000,
57. curve: Curve.EaseIn
58. },
59. ]
60. }
61. },
62. },
63. ]
64. })
65. .width(300)
66. .height(300)
67. .emitter(this.emitterProperties)
68. }.width('100%').height('100%').align(Alignment.Center)
69. }
70. }
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/Animation/entry/src/main/ets/pages/particle/template4/Index.ets#L15-L86)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b1/v3/uSkJHORpSIGUDRB6Sq0HDw/zh-cn_image_0000002583440077.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000217Z&HW-CC-Expire=86400&HW-CC-Sign=8EE676A1E67073C7F98568E31C91E4F9A5CA2D3E995F78111F0F81F31FB863E5)

### 示例5（环形发射器创建）

该示例实现了粒子动画环形发射器每隔一秒钟沿着圆弧30度递增，周期性发射粒子，直至布满整个圆环。

```
1. import { LengthMetrics } from '@kit.ArkUI';

3. @Entry
4. @Component
5. struct ParticleExample5 {
6. build() {
7. Stack() {
8. Text()
9. .width(300).height(300).backgroundColor(Color.Black)
10. Particle({
11. particles: [
12. {
13. emitter: {
14. particle: {
15. type: ParticleType.POINT, // 粒子类型
16. config: {
17. radius: 5 // 圆点半径
18. },
19. count: 2000, // 粒子总数
20. lifetime: 10000, // 粒子生命周期，单位ms
21. lifetimeRange: 100 // 粒子生命周期取值范围，单位ms
22. },
23. emitRate: 100, // 每秒发射粒子数
24. shape: ParticleEmitterShape.ANNULUS, // 环形发射器
25. annulusRegion:{
26. center:{x:LengthMetrics.percent(0.5),y:LengthMetrics.percent(0.5)}, // 圆环的圆心坐标
27. innerRadius:LengthMetrics.vp(100), // 圆环的外圆半径
28. outerRadius:LengthMetrics.vp(120), // 圆环的内圆半径
29. startAngle:0, // 圆环的起始角度
30. endAngle:360 // 圆环的结束角度
31. }
32. },
33. color: {
34. range: [Color.Pink, Color.White],
35. },
36. opacity: {
37. range: [0.0, 1.0],
38. updater: {
39. type: ParticleUpdater.CURVE,
40. config: [
41. {
42. from: 0.0,
43. to: 1.0,
44. startMillis: 0,
45. endMillis: 3000,
46. curve: Curve.EaseIn
47. },
48. {
49. from: 1.0,
50. to: 0.0,
51. startMillis: 5000,
52. endMillis: 10000,
53. curve: Curve.EaseIn
54. }
55. ]
56. }
57. },
58. scale: {
59. range: [0.0, 0.0],
60. updater: {
61. type: ParticleUpdater.CURVE,
62. config: [
63. {
64. from: 0.0,
65. to: 0.5,
66. startMillis: 0,
67. endMillis: 3000,
68. curve: Curve.EaseIn
69. }
70. ]
71. }
72. },
73. }
74. ]
75. }).width(300).height(300)
76. }.width('100%').height('100%').align(Alignment.Center)
77. }
78. }
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/Animation/entry/src/main/ets/pages/particle/template5/Index.ets#L15-L94)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2e/v3/VSRrYPoeQc-1HhjOOvI6Bw/zh-cn_image_0000002552960032.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000217Z&HW-CC-Expire=86400&HW-CC-Sign=BD8B594BEC8946F11F7525634A4DF445AA1871957A8F8697D66DF0BF618ED3E2)

### 示例6（环形发射器更新）

描述粒子动画环形发射器更新的基础用法。

```
1. import { LengthMetrics } from '@kit.ArkUI';

3. @Entry
4. @Component
5. struct ParticleExample6 {

7. @State radius: number = 1;
8. @State shape: ParticleEmitterShape = ParticleEmitterShape.ANNULUS;
9. @State emitRate: number = 200;
10. @State count: number = 2000;
11. private timerID: number = -1;
12. private centerX: LengthMetrics = LengthMetrics.percent(0.5);
13. private centerY: LengthMetrics = LengthMetrics.percent(0.5);
14. private inRadius: LengthMetrics = LengthMetrics.vp(120);
15. private outRadius: LengthMetrics = LengthMetrics.vp(120);
16. private startAngle: number = 0;
17. private endAngle: number = 90;
18. @State emitterProperties: Array<EmitterProperty> = [
19. {
20. index: 0,
21. emitRate: 100,
22. annulusRegion: {
23. center:{x:this.centerX, y: this.centerY}, // 圆环的圆心坐标
24. outerRadius: this.outRadius, // 圆环的外圆半径
25. innerRadius: this.inRadius, // 圆环的内圆半径
26. startAngle: -90, // 圆环的起始角度
27. endAngle: 0 // 圆环的结束角度
28. }
29. }
30. ]
31. @State region: ParticleAnnulusRegion = {
32. center:{x:this.centerX, y: this.centerY},
33. outerRadius: this.outRadius,
34. innerRadius: this.inRadius,
35. startAngle: -90,
36. endAngle: 0
37. }

39. aboutToDisappear(): void {
40. // 页面销毁时清除计时器
41. if (this.timerID != -1) {
42. clearInterval(this.timerID);
43. }
44. }

46. build() {
47. Column({ space: 10}) {
48. Stack() {
49. Text()
50. .width(300).height(300).backgroundColor(Color.Black)

52. Particle({
53. particles: [
54. {
55. emitter: {
56. particle: {
57. type: ParticleType.POINT, // 粒子类型
58. config: {
59. radius: this.radius // 圆点半径
60. },
61. count: this.count, // 粒子总数
62. lifetime: -1 // 粒子的生命周期，-1表示粒子生命周期无限大
63. },
64. emitRate: this.emitRate, // 每秒发射粒子数
65. shape: this.shape, // 发射器形状
66. annulusRegion: this.region
67. },
68. color: {
69. range: [Color.White, Color.Pink], // 初始颜色范围
70. },
71. },
72. ]
73. }).width('100%')
74. .height('100%')
75. .emitter(this.emitterProperties)
76. .onClick(()=>{
77. // 清除已有定时器
78. if (this.timerID != -1) {
79. clearInterval(this.timerID);
80. }

82. // 创建定时器（每秒更新）
83. this.timerID = setInterval(() => {
84. this.emitterProperties = [
85. {
86. index: 0,
87. emitRate: this.emitRate,
88. annulusRegion: {
89. center:{x:this.centerX, y: this.centerY},
90. outerRadius: this.outRadius,
91. innerRadius: this.inRadius,
92. startAngle: this.startAngle,
93. endAngle: this.endAngle
94. }
95. }
96. ];
97. if (this.endAngle >= 270) {
98. if (this.timerID != -1) {
99. clearInterval(this.timerID);
100. }
101. return;
102. }
103. // 更新角度值（30度/秒）
104. this.startAngle += 30;
105. this.endAngle += 30;
106. }, 1000);

108. })
109. }
110. .width('100%')
111. .height('100%')
112. .align(Alignment.Center)
113. }
114. }
115. }
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/Animation/entry/src/main/ets/pages/particle/template6/Index.ets#L15-L131)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/EU_6qyETRNCZp8D7WLhbdA/zh-cn_image_0000002583480033.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000217Z&HW-CC-Expire=86400&HW-CC-Sign=2774A86F1FDAF8CD0C9A60DCA92B2420394F19A950B78AA1489774EBB28718BA)

### 示例7（设置波动场和速度场）

从API version 22开始，支持设置粒子波动场和速度场。该示例演示如何通过rippleFields接口设置粒子波动场，产生类似波纹扩散的效果。通过velocityFields接口设置粒子速度场，使粒子在原有速度的基础上叠加速度场指定的速度。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct ParticleExample {
5. @State count: number = 1000
6. @State particle: EmitterParticleOptions<ParticleType> = {
7. type: ParticleType.POINT, // 粒子类型
8. config: {
9. radius: 1 // 圆点半径
10. },
11. count: this.count, // 粒子总数
12. lifetime: 9000, // 粒子生命周期，单位ms
13. lifetimeRange: 100 // 粒子生命周期取值范围，单位ms
14. }
15. build() {
16. Column() {
17. Text('波动场')
18. .fontSize(30)
19. .fontWeight(FontWeight.Bold)
20. Stack() {
21. Text()
22. .width(300).height(300).backgroundColor(Color.Black)
23. Particle({
24. particles: [
25. {
26. emitter: {
27. particle: this.particle,
28. emitRate: 10000, // 每秒发射粒子数
29. position: [0, 0],
30. shape: ParticleEmitterShape.RECTANGLE // 发射器形状
31. },
32. color: {
33. range: [Color.White, Color.White], // 初始颜色范围
34. },
35. scale: {
36. range: [0.2, 1.5], // 初始大小范围
37. },
38. opacity : {
39. range: [0.2, 0.8], // 初始透明度范围
40. }
41. }
42. ]
43. }).width(300).height(300)
44. .rippleFields([
45. {
46. amplitude: 120, // 波动场幅值
47. wavelength: 500, // 波动场的波长
48. waveSpeed: 220, // 波动场的波速
49. center: { x: 150, y: 150 }, // 波动场的力的中心
50. attenuation: 0, // 波动场随时间的衰减系数
51. region: {
52. // 波动场的影响区域
53. shape: DisturbanceFieldShape.RECT, // 波动场影响区域的形状
54. position: { x: 150, y: 150 }, // 波动场影响区域的区域中心
55. size: { width: 300, height: 300 } // 波动场影响区域的大小
56. }
57. }
58. ])
59. }.width("100%").height(300).align(Alignment.Center)
60. Text('速度场')
61. .fontSize(30)
62. .fontWeight(FontWeight.Bold)
63. Stack() {
64. Text()
65. .width(300).height(300).backgroundColor(Color.Black)
66. Particle({
67. particles: [
68. {
69. emitter: {
70. particle: {
71. type: ParticleType.POINT, // 粒子类型
72. config: {
73. radius: 2 // 圆点半径
74. },
75. count: 1000, // 粒子总数
76. lifetime: 1000, // 粒子生命周期，单位ms
77. lifetimeRange: 0 // 粒子生命周期取值范围，单位ms
78. },
79. emitRate: 120, // 每秒发射粒子数
80. position: [0, 0],
81. size: [300, 300],
82. shape: ParticleEmitterShape.RECTANGLE // 发射器形状
83. },
84. color: {
85. range: [Color.White, Color.White], // 初始颜色范围
86. },
87. opacity: {
88. range: [1.0, 1.0],
89. updater: {
90. type: ParticleUpdater.CURVE, // 透明度按曲线变化
91. config: [
92. {
93. from: 1.0,
94. to: 0.0,
95. startMillis: 0,
96. endMillis: 1000,
97. curve: Curve.EaseIn
98. }
99. ]
100. }
101. },
102. }
103. ]
104. }).width(300).height(300)
105. .margin({ top: 30 })
106. .velocityFields([
107. {
108. velocity: { x: 100, y: 0 }, // 速度场的速度值
109. region: {
110. // 速度场的影响区域
111. shape: DisturbanceFieldShape.RECT, // 速度场影响区域的形状
112. position: { x: 150, y: 150 }, // 速度场影响区域的区域中心
113. size: { width: 200, height: 200 } // 速度场影响区域的大小
114. }
115. }
116. ])
117. }.width("100%").height(300).align(Alignment.Center)
118. }
119. }
120. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5b/v3/1oCehukTRCiRzk3tYWNTBw/zh-cn_image_0000002552800384.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000217Z&HW-CC-Expire=86400&HW-CC-Sign=D467E79B3445AD46ADF9D0964A46782BE3FE8D6EAC52A86973C5E924B3E6BFE4)
