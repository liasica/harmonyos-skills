---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-particle-animation
title: 粒子动画
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 使用动画 > 粒子动画
category: harmonyos-guides
scraped_at: 2026-11-21T09:11:09+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:5633c639619f5ee84ec1dbef1f723c924cec158ca5063d91b0580ebede5b57c9
---

[粒子动画](../harmonyos-references/ts-particle-animation.md)是通过在限定区域内随机生成大量粒子的运动，进而组合成的动画效果，通过Particle组件来实现。动画的基本构成元素为单个粒子，这些粒子可以表现为圆点或图片等形式。开发者能够通过对粒子在颜色、透明度、大小、速度、加速度、自旋角度等多个维度上的动态变化做动画，以营造特定的氛围，例如模拟下雪场景时，飘舞的雪花实际上是由一个个雪花粒子的动画效果所构成。

粒子动画的简单实现如下所示。

```ts
@Entry
@Component
struct ParticleExample {
  build() {
    Stack() {
      Text()
        .width(300).height(300).backgroundColor('rgb(240, 250, 255)')
      Particle({ particles: [
        {
          emitter: {
            particle: {
              type: ParticleType.POINT, // 粒子类型
              config: {
                radius: 5 // 圆点半径
              },
              count: 100, // 粒子总数
            },
          },
          color:{
            range:['rgb(39, 135, 217)','rgb(0, 74, 175)'], // 初始颜色范围
          },
        },
      ]
      }).width(250).height(250)
    }.width('100%').height('100%').align(Alignment.Center)
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7d/v3/wdu5dzDFQvOIez-tNtelWg/zh-cn_image_0000002793036848.gif?HW-CC-KV=V1&HW-CC-Date=20261121T010945Z&HW-CC-Expire=31536000000&HW-CC-Sign=5568BB5B1B9BA8C35FE98CCB1BF5EBA6319564A6A2855C1E8FEA5324D4B6B929)

## 实现粒子发射器

粒子发射器（Particle Emitter）主要定义粒子的初始属性（如类型和位置），控制粒子的生成速率，以及管理粒子的生命周期。可通过[emitter](../harmonyos-references/ts-particle-animation.md#emitter12)方法调整粒子发射器的位置、发射速率和发射窗口的大小，实现发射器位置的动态更新。

```ts
// ...
@State emitterProperties: Array<EmitterProperty> = [
  {
    index: 0,
    emitRate: 100,
    position: { x: 60, y: 80 },
    size: { width: 200, height: 200 }
  }
]

Particle(...).width(300).height(300).emitter(this.emitterProperties) // 动态调整粒子发射器的位置
// ...
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/03/v3/Txx9PXLYTfaJGoX01diOLA/zh-cn_image_0000002792876878.gif?HW-CC-KV=V1&HW-CC-Date=20261121T010945Z&HW-CC-Expire=31536000000&HW-CC-Sign=4470949D52B26EA393E50F898DA2D8055C62322E4BD8666CDC1DC3771B50D5CC)

## 设置粒子颜色

可以通过[range](../harmonyos-references/ts-particle-animation.md#particlecolorpropertyoptions)来确定粒子的初始颜色范围，而[distributionType](../harmonyos-references/ts-particle-animation.md#particlecolorpropertyoptions)则用于指定粒子初始颜色随机值的分布方式，具体可选择均匀分布或者高斯（正态）分布。

```ts
// ...
color: {
  range: ['rgb(39, 135, 217)','rgb(0, 74, 175)'], // 初始颜色范围
  distributionType: DistributionType.GAUSSIAN // 初始颜色随机值分布
},
// ...
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3f/v3/-ZJ4bRk_QGKbX5yujfsF2A/zh-cn_image_0000002821836783.gif?HW-CC-KV=V1&HW-CC-Date=20261121T010945Z&HW-CC-Expire=31536000000&HW-CC-Sign=7597DD669E2867BC229E1E7FB3F515C833BF0C14D79884657A9C0F8D16C198A9)

## 粒子的生命周期

粒子的生命周期（Lifecycle）是粒子从生成至消亡的整个过程，用于确定粒子的存活时间长度。粒子的生命周期可通过设置[EmitterParticleOptions](../harmonyos-references/ts-particle-animation.md#emitterparticleoptions18)的lifetime和lifetimeRange属性来指定。

```ts
// ...
emitter: {
  particle: {
    // ...
    lifetime: 300, // 粒子生命周期，单位ms
    lifetimeRange: 100 // 粒子生命周期取值范围，单位ms
  },
  emitRate: 10, // 每秒发射粒子数
  position: [0, 0],
  shape: ParticleEmitterShape.RECTANGLE // 发射器形状
},
color: {
  range: ['rgb(39, 135, 217)','rgb(0, 74, 175)'], // 初始颜色范围
},
// ...
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/10/v3/x9bc2ojcT4Sm52n4hZEQzw/zh-cn_image_0000002821756787.gif?HW-CC-KV=V1&HW-CC-Date=20261121T010945Z&HW-CC-Expire=31536000000&HW-CC-Sign=BCADE4E6086C56EA49294E7565C0C01A4CE469357B8DB90F7E9119DDBAB04855)

## 设置粒子扰动场

扰动场（Disturbance Field）是一种影响粒子运动的机制。通过在粒子所在的空间区域内施加特定的力，扰动场能够改变粒子的轨迹和行为，进而实现更为复杂和自然的动画效果。扰动场的配置可以通过[disturbanceFields](../harmonyos-references/ts-particle-animation.md#disturbancefields12)方法来完成。

```ts
// ...
Particle({ particles: [
  {
    emitter: // ...
    color: // ...
    scale: {
      range: [0.0, 0.0],
      updater: {
        type: ParticleUpdater.CURVE,
        config: [
          {
            from: 0.0,
            to: 0.5,
            startMillis: 0,
            endMillis: 3000,
            curve: Curve.EaseIn
          }
        ]
      }
    },
    acceleration: { // 加速度的配置，从大小和方向两个维度变化，speed表示加速度大小，angle表示加速度方向
      speed: {
        range: [3, 9],
        updater: {
          type: ParticleUpdater.RANDOM,
          config: [1, 20]
        }
      },
      angle: {
        range: [90, 90]
      }
    }

  }
]
}).width(300).height(300).disturbanceFields([{
  strength: 10,
  shape: DisturbanceFieldShape.RECT,
  size: { width: 100, height: 100 },
  position: { x: 100, y: 100 },
  feather: 15,
  noiseScale: 10,
  noiseFrequency: 15,
  noiseAmplitude: 5
}])
// ...
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/33/v3/_iCsFyCFR122vYXZ5ukYFw/zh-cn_image_0000002793036850.gif?HW-CC-KV=V1&HW-CC-Date=20261121T010945Z&HW-CC-Expire=31536000000&HW-CC-Sign=EF55883260C46DC89FB6B36B38814F9D6C5C2284ADD02AB787B44EA42A709AD9)
