---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1487
title: 粒子动画的常见应用场景
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 粒子动画的常见应用场景
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:27+08:00
doc_updated_at: 2026-08-20
content_hash: sha256:5d6e88bea396b61387bac5befb5e78b2496abfb2f16fc868795245d455d4457d
---

## 问题现象

开发者在使用粒子动画时，可能会遇到以下几类典型场景：

* 场景一：粒子动画在应用切换至后台后重新回到前台时，如何恢复播放？
* 场景二：如何实现粒子动画与用户手指移动同步的跟手效果？
* 场景三：如何在粒子上浮时模拟自然的左右随机抖动？

针对以上场景，该如何实现？

## 背景知识

* [粒子动画 (Particle)](../harmonyos-references/ts-particle-animation.md)：粒子动画是在一定范围内随机生成的大量粒子产生运动而组成的动画。
* [PanGesture](../harmonyos-references/ts-basic-gestures-pangesture.md)：滑动手势事件，当滑动的最小距离达到设定的最小值时触发滑动手势事件。
* [onForeground()](../harmonyos-guides/uiability-lifecycle.md#onforeground)：在UIAbility切换至前台时且UIAbility的UI可见之前，系统触发onForeground回调。
* [if/else：条件渲染](../harmonyos-guides/arkts-rendering-control-ifelse.md)：ArkTS提供了渲染控制能力。条件渲染可根据应用状态，使用if、else和else if渲染相应的UI内容。

## 解决方案

* 场景一：粒子动画在应用切换至后台后重新回到前台时，如何恢复播放？

  可以通过if/else条件渲染控制组件的展示，并结合UIAbility的onForeground和onBackground方法管理组件的显示状态。
  1. 在UIAbility的onForeground和onBackground方法中，通过AppStorage设置状态标识。

     ```ts
     import { ConfigurationConstant, UIAbility } from '@kit.AbilityKit';
     import { hilog } from '@kit.PerformanceAnalysisKit';
     import { window } from '@kit.ArkUI';

     const DOMAIN = 0x0000;

     export default class EntryAbility extends UIAbility {
       onCreate(): void {
         try {
           this.context.getApplicationContext().setColorMode(ConfigurationConstant.ColorMode.COLOR_MODE_NOT_SET);
         } catch (err) {
           hilog.error(DOMAIN, 'testTag', 'Failed to set colorMode. Cause: %{public}s', JSON.stringify(err));
         }
         hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onCreate');
       }

       onDestroy(): void {
         hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onDestroy');
       }

       onWindowStageCreate(windowStage: window.WindowStage): void {
         // Main window is created, set main page for this ability
         hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onWindowStageCreate');

         windowStage.loadContent('pages/Index', (err) => {
           if (err.code) {
             hilog.error(DOMAIN, 'testTag', 'Failed to load the content. Cause: %{public}s', JSON.stringify(err));
             return;
           }
           hilog.info(DOMAIN, 'testTag', 'Succeeded in loading the content.');
         });
       }

       onWindowStageDestroy(): void {
         // Main window is destroyed, release UI related resources
         hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onWindowStageDestroy');
       }

       onForeground(): void {
         // Ability has brought to foreground
         hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onForeground');
         AppStorage.setOrCreate('flag', true);
       }

       onBackground(): void {
         // Ability has back to background
         hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onBackground');
         AppStorage.setOrCreate('flag', false);
       }
     };
     ```
  2. 在页面中使用@StorageLink获取该状态标识，通过if语句判断是否渲染Particle组件。当应用进入后台时，onBackground将标识设为false；恢复到前台时，onForeground将其设为true，此时组件重新渲染，粒子动画得以重新播放。

     ```ts
     @Entry
     @Component
     struct ParticleExample {
       @StorageLink('flag') flag: boolean | undefined = undefined;

       build() {
         Stack() {
           Text()
             .width(300).height(300).backgroundColor('rgb(240, 250, 255)');
           if (this.flag) {
             Particle({
               particles: [
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
                   color: {
                     range: ['rgb(39, 135, 217)', 'rgb(0, 74, 175)'], // 初始颜色范围
                   },
                 },
               ]
             })
               .width(250).height(250);
           }
         }.width('100%').height('100%').align(Alignment.Center);
       }
     }
     ```
* 场景二：如何实现粒子动画与用户手指移动同步的跟手效果？
  1. 使用状态变量（如imageWidth、imageHeight、positionX、positionY）控制粒子图像的大小及发射器的位置。
  2. 通过Particle组件实现粒子动画效果，配置粒子图像、生命周期、颜色、透明度、缩放、加速度等属性。
  3. 动态调整发射器参数：利用Particle提供的emitter接口，实时更新发射位置、发射率、发射形状等配置。
  4. 通过手势控制粒子发射器位置：使用PanGesture手势监听器实现拖动操作，在onActionUpdate中更新发射器位置与发射率，在onActionEnd中停止粒子发射。

  ```ts
  @Entry
  @Component
  struct ParticleFollowExample {
    imageWidth: number = 40;
    imageHeight: number = 40;
    positionX: number = 100;
    positionY: number = 0;
    @State emitterProperties: Array<EmitterProperty> = [
      {
        index: 0,
        emitRate: 0, // 每秒发射粒子数
        position: { x: this.positionX, y: this.positionY }, // 设置粒子发射器位置
        size: { width: 20, height: 20 }
      }
    ];

    build() {
      Column() {
        Stack() {
          Particle({
            particles: [
              {
                emitter: {
                  particle: {
                    type: ParticleType.IMAGE, // 粒子类型
                    config: {
                      src: $r('app.media.startIcon'), // 此处仅为示例，请开发者替换为可用图片
                      size: [this.imageWidth, this.imageHeight],
                      objectFit: ImageFit.Contain
                    },
                    lifetime: 1400, // 单个粒子的生命周期
                    lifetimeRange: 200, // 粒子生命周期取值范围
                    count: -1, // 粒子总数
                  },
                  emitRate: 0,
                  shape: ParticleEmitterShape.CIRCLE, // 发射器形状
                  size: [20, 20],
                  position: [100, 100]
                },
                color: {
                  range: [Color.White, Color.White]
                },
                opacity: {
                  range: [1.0, 1.0],
                  updater: {
                    type: ParticleUpdater.CURVE,
                    config: [
                      {
                        from: 1.0,
                        to: 0,
                        startMillis: 0,
                        endMillis: 1600,
                        curve: Curve.Linear
                      }
                    ]
                  }
                },
                scale: {
                  range: [1.0, 1.0],
                  updater: {
                    type: ParticleUpdater.CURVE,
                    config: []
                  }
                },
                acceleration: {
                  speed: {
                    range: [300, 400],
                    updater: {
                      type: ParticleUpdater.RANDOM,
                      config: [0, 0]
                    }
                  },
                  angle: {
                    range: [0, 360],
                    updater: {
                      type: ParticleUpdater.RANDOM,
                      config: [0, 0]
                    }
                  }
                },
                spin: {
                  range: [0, 360],
                  updater: {
                    type: ParticleUpdater.CURVE,
                    config: [
                      {
                        from: 0,
                        to: 360,
                        startMillis: 0,
                        endMillis: 1500,
                        curve: Curve.EaseIn
                      }
                    ]
                  }
                },
              },
            ]
          })
            .width('100%').height('100%')
            .emitter(this.emitterProperties)
            .gesture(
              PanGesture()
                .onActionUpdate((event: GestureEvent) => {
                  // 动态调整粒子发射器的位置
                  if (event && event.fingerList.length > 0) {
                    this.positionX = event.fingerList[0].localX;
                    this.positionY = event.fingerList[0].localY;
                    this.emitterProperties = [{
                      index: 0,
                      emitRate: 100,
                      position: { x: this.positionX, y: this.positionY },
                      size: { width: 20, height: 20 }
                    }];
                  }
                })
                .onActionEnd(() => {
                  this.emitterProperties = [{
                    index: 0,
                    emitRate: 0,
                    position: { x: this.positionX, y: this.positionY },
                    size: { width: 20, height: 20 }
                  }];
                })
            );
        }.width('100%')
        .height('100%')
        .align(Alignment.Center);
      }.width('100%')
      .height('100%');
    }
  }
  ```
* 场景三：如何在粒子上浮时模拟自然的左右随机抖动？
  1. 使用Particle组件实现粒子动画效果，包括配置粒子图像、生命周期、颜色、透明度、缩放和加速度等属性。
  2. 通过添加粒子扰动场，在粒子运动过程中施加干扰，从而实现粒子左右抖动的效果。

  ```ts
  const LIFE_TIME: number = 1000;

  @Entry
  @Component
  struct ParticleMoveExample {
    imageWidth: number = 40;
    imageHeight: number = 40;
    cnt: number = -1;
    positionX: number = 200;
    positionY: number = 500;

    build() {
      Column() {
        Stack() {
          Particle({
            particles: [
              {
                emitter: {
                  particle: {
                    type: ParticleType.IMAGE, // 粒子类型
                    config: {
                      src: $r('app.media.startIcon'),
                      size: [this.imageWidth, this.imageHeight],
                      objectFit: ImageFit.Contain
                    },
                    lifetime: LIFE_TIME, // 单个粒子的生命周期
                    lifetimeRange: 100, // 粒子生命周期取值范围
                    count: this.cnt, // 粒子总数
                  },
                  emitRate: 3,
                  shape: ParticleEmitterShape.CIRCLE, // 发射器形状
                  size: [20, 20],
                  position: [this.positionX, this.positionY]
                },
                opacity: {
                  range: [1.0, 1.0],
                  updater: {
                    type: ParticleUpdater.CURVE,
                    config: [
                      {
                        from: 1.0,
                        to: 0,
                        startMillis: 0,
                        endMillis: LIFE_TIME,
                        curve: Curve.Linear
                      }
                    ]
                  }
                },
                scale: {
                  range: [1.0, 1.0],
                  updater: {
                    type: ParticleUpdater.CURVE,
                    config: [
                      {
                        from: 1,
                        to: 0.2,
                        startMillis: 0,
                        endMillis: LIFE_TIME,
                        curve: Curve.EaseIn
                      }
                    ]
                  }
                },
                velocity: {
                  speed: [300, 400],
                  angle: [-90, -90]
                },
                acceleration: {
                  speed: {
                    range: [300, 400],
                    updater: {
                      type: ParticleUpdater.RANDOM,
                      config: [0, 0]
                    }
                  },
                  angle: {
                    range: [-90, -90],
                    updater: {
                      type: ParticleUpdater.RANDOM,
                      config: [0, 0]
                    }
                  }
                },
                spin: {
                  range: [0, 0],
                  updater: {
                    type: ParticleUpdater.RANDOM,
                    config: [-60, 60]
                  }
                },
              }
            ]
          })
            .disturbanceFields([{
              // 增加扰动场
              strength: 5,
              shape: DisturbanceFieldShape.RECT,
              size: { width: 900, height: 900 },
              position: { x: this.positionX, y: this.positionY },
              feather: 15,
              noiseScale: 10,
              noiseFrequency: 15,
              noiseAmplitude: 5
            }])
            .width('100%').height('100%');
        }.width('100%')
        .height('100%')
        .align(Alignment.Center);
      }.width('100%')
      .height('100%');
    }
  }
  ```
