---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-particle-animation
title: 粒子动画
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 使用动画 > 粒子动画
category: harmonyos-guides
scraped_at: 2026-04-29T13:28:13+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:850a8212b335a83839b446d52647d0f9ce176352ade9af95dbc25550348cf04e
---

[粒子动画](../harmonyos-references/ts-particle-animation.md)是通过在限定区域内随机生成大量粒子的运动，进而组合成的动画效果，通过Particle组件来实现。动画的基本构成元素为单个粒子，这些粒子可以表现为圆点或图片等形式。开发者能够通过对粒子在颜色、透明度、大小、速度、加速度、自旋角度等多个维度上的动态变化做动画，以营造特定的氛围，例如模拟下雪场景时，飘舞的雪花实际上是由一个个雪花粒子的动画效果所构成。

粒子动画的简单实现如下所示。

```
1. @Entry
2. @Component
3. struct ParticleExample {
4. build() {
5. Stack() {
6. Text()
7. .width(300).height(300).backgroundColor('rgb(240, 250, 255)')
8. Particle({ particles: [
9. {
10. emitter: {
11. particle: {
12. type: ParticleType.POINT, // 粒子类型
13. config: {
14. radius: 5 // 圆点半径
15. },
16. count: 100, // 粒子总数
17. },
18. },
19. color:{
20. range:['rgb(39, 135, 217)','rgb(0, 74, 175)'], // 初始颜色范围
21. },
22. },
23. ]
24. }).width(250).height(250)
25. }.width('100%').height('100%').align(Alignment.Center)
26. }
27. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/40/v3/quArRT6UR8Sw7m2NAEIXlg/zh-cn_image_0000002589244291.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052810Z&HW-CC-Expire=86400&HW-CC-Sign=D02E22141FD7A722CA7806584CF1931C4816C1D91C082D7F4CC36B92E56A7139)

## 实现粒子发射器

粒子发射器（Particle Emitter）主要定义粒子的初始属性（如类型和位置），控制粒子的生成速率，以及管理粒子的生命周期。可通过[emitter](../harmonyos-references/ts-particle-animation.md#emitter12)方法调整粒子发射器的位置、发射速率和发射窗口的大小，实现发射器位置的动态更新。

```
1. // ...
2. @State emitterProperties: Array<EmitterProperty> = [
3. {
4. index: 0,
5. emitRate: 100,
6. position: { x: 60, y: 80 },
7. size: { width: 200, height: 200 }
8. }
9. ]

11. Particle(...).width(300).height(300).emitter(this.emitterProperties) // 动态调整粒子发射器的位置
12. // ...
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0/v3/pDoPM8GWTFCdZ8Eg8s_B2Q/zh-cn_image_0000002558764484.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052810Z&HW-CC-Expire=86400&HW-CC-Sign=D889B8979005085D681106B2A2A96CED88A48248033F809FD73918EC564E345B)

## 设置粒子颜色

可以通过[range](../harmonyos-references/ts-particle-animation.md#particlecolorpropertyoptions)来确定粒子的初始颜色范围，而[distributionType](../harmonyos-references/ts-particle-animation.md#particlecolorpropertyoptions)则用于指定粒子初始颜色随机值的分布方式，具体可选择均匀分布或者高斯（正态）分布。

```
1. // ...
2. color: {
3. range: ['rgb(39, 135, 217)','rgb(0, 74, 175)'], // 初始颜色范围
4. distributionType: DistributionType.GAUSSIAN // 初始颜色随机值分布
5. },
6. // ...
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/46/v3/CnKppd12ROuDM60O32qeGA/zh-cn_image_0000002558604828.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052810Z&HW-CC-Expire=86400&HW-CC-Sign=F34554822706A5B0DE92277808C6B9DD9CC6CFEAEB0E4C002F4A8409EB776A60)

## 粒子的生命周期

粒子的生命周期（Lifecycle）是粒子从生成至消亡的整个过程，用于确定粒子的存活时间长度。粒子的生命周期可通过设置[EmitterParticleOptions](../harmonyos-references/ts-particle-animation.md#emitterparticleoptions18)的lifetime和lifetimeRange属性来指定。

```
1. // ...
2. emitter: {
3. particle: {
4. // ...
5. lifetime: 300, // 粒子生命周期，单位ms
6. lifetimeRange: 100 // 粒子生命周期取值范围，单位ms
7. },
8. emitRate: 10, // 每秒发射粒子数
9. position: [0, 0],
10. shape: ParticleEmitterShape.RECTANGLE // 发射器形状
11. },
12. color: {
13. range: ['rgb(39, 135, 217)','rgb(0, 74, 175)'], // 初始颜色范围
14. },
15. // ...
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/95/v3/STXWq2ErSdy3-WGz_n6LGA/zh-cn_image_0000002589324353.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052810Z&HW-CC-Expire=86400&HW-CC-Sign=05C8AB80767419A76F857396C31FE387BF7ED717AD207BBA3FA2FCF70ABB5046)

## 设置粒子扰动场

扰动场（Disturbance Field）是一种影响粒子运动的机制。通过在粒子所在的空间区域内施加特定的力，扰动场能够改变粒子的轨迹和行为，进而实现更为复杂和自然的动画效果。扰动场的配置可以通过[disturbanceFields](../harmonyos-references/ts-particle-animation.md#disturbancefields12)方法来完成。

```
1. // ...
2. Particle({ particles: [
3. {
4. emitter: // ...
5. color: // ...
6. scale: {
7. range: [0.0, 0.0],
8. updater: {
9. type: ParticleUpdater.CURVE,
10. config: [
11. {
12. from: 0.0,
13. to: 0.5,
14. startMillis: 0,
15. endMillis: 3000,
16. curve: Curve.EaseIn
17. }
18. ]
19. }
20. },
21. acceleration: { // 加速度的配置，从大小和方向两个维度变化，speed表示加速度大小，angle表示加速度方向
22. speed: {
23. range: [3, 9],
24. updater: {
25. type: ParticleUpdater.RANDOM,
26. config: [1, 20]
27. }
28. },
29. angle: {
30. range: [90, 90]
31. }
32. }

34. }
35. ]
36. }).width(300).height(300).disturbanceFields([{
37. strength: 10,
38. shape: DisturbanceFieldShape.RECT,
39. size: { width: 100, height: 100 },
40. position: { x: 100, y: 100 },
41. feather: 15,
42. noiseScale: 10,
43. noiseFrequency: 15,
44. noiseAmplitude: 5
45. }])
46. // ...
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/af/v3/xxW3dZ8FQxuNrDGKZARwzg/zh-cn_image_0000002589244293.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052810Z&HW-CC-Expire=86400&HW-CC-Sign=788D5AFCF48A643450CE960A598E0531C6331AC42EAB1998E8494CB4D786AF66)
