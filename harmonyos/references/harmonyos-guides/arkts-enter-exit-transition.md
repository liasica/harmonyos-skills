---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-enter-exit-transition
title: 出现/消失转场
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 使用动画 > 转场动画 > 出现/消失转场
category: harmonyos-guides
scraped_at: 2026-09-05T06:14:02+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:13b9b29e6438f99ae801402c205b043a1d61731c7630ef11a758bf18de08824e
---

[transition](../harmonyos-references/ts-transition-animation-component.md)是基础的组件转场接口，用于实现一个组件出现或者消失时的动画效果。可以通过[TransitionEffect10+对象说明](../harmonyos-references/ts-transition-animation-component.md#transitioneffect10对象说明)的组合使用，定义出各式效果。

**表1** 转场效果接口

| 转场效果 | 说明 | 动画 |
| --- | --- | --- |
| IDENTITY | 禁用转场效果。 | 无。 |
| OPACITY | 默认的转场效果，透明度转场。 | 出现时透明度从0到1，消失时透明度从1到0。 |
| SLIDE | 滑动转场效果。 | 出现时从窗口左侧滑入，消失时从窗口右侧滑出。 |
| translate | 通过设置组件平移创建转场效果。 | 出现时，平移参数的值从translate接口设置的值变化为默认值0，消失时从默认值0变化为translate接口设置的值。 |
| rotate | 通过设置组件旋转创建转场效果。 | 出现时，旋转参数的值从rotate接口设置的值变化为默认值0，消失时从默认值0变化为rotate接口设置的值。 |
| opacity | 通过设置透明度参数创建转场效果。 | 出现时，透明度参数的值从opacity设置的值变化为透明度默认值1，消失时从透明度默认值1变化为opacity设置的值。 |
| move | 通过[TransitionEdge](../harmonyos-references/ts-transition-animation-component.md#transitionedge10)创建从窗口哪条边缘出来的效果。 | 出现时从TransitionEdge方向滑入，消失时滑出到TransitionEdge方向。 |
| asymmetric | 通过此方法组合非对称的出现消失转场效果，即出现、消失为两套独立不同的动画，效果不互为逆过程。具体使用可参考[asymmetric](../harmonyos-references/ts-transition-animation-component.md#asymmetric10)。  - appear：出现转场的效果。  - disappear：消失转场的效果。 | 出现时采用appear设置的TransitionEffect出现效果，消失时采用disappear设置的[TransitionEffect](../harmonyos-references/ts-transition-animation-component.md#transitioneffect10对象说明)消失效果。 |
| combine | 组合其他TransitionEffect。 | 组合其他TransitionEffect，一起生效。 |
| animation | 定义转场效果的动画参数：  - 如果不定义会跟随[animateTo](../harmonyos-references/ts-explicit-animation.md)的动画参数。  - 不支持通过控件的animation接口配置动画参数。  - TransitionEffect中animation的onFinish不生效。 | 调用顺序是从上往下，上面TransitionEffect的animation也会作用到下面TransitionEffect。 |

1. 创建TransitionEffect。

   ```typescript
   // 出现时会是所有出现转场效果的叠加，消失时会是所有消失转场效果的叠加
   // 说明各个effect跟随的动画参数
   private effect: TransitionEffect =
     TransitionEffect.OPACITY // 创建了透明度转场效果，这里没有调用animation接口，会跟随animateTo的动画参数
       // 通过combine方法，添加缩放转场效果，并指定了springMotion(0.6, 1.2)曲线
       .combine(TransitionEffect.scale({ x: 0, y: 0 }).animation({ curve: curves.springMotion(0.6, 1.2) }))
       // 添加旋转转场效果，这里的动画参数会跟随上面的TransitionEffect，也就是springMotion(0.6, 1.2)
       .combine(TransitionEffect.rotate({ angle: 90 }))
       // 添加平移转场效果，动画参数会跟随其之上带animation的TransitionEffect，也就是springMotion(0.6, 1.2)
       .combine(TransitionEffect.translate({ x: 150, y: 150 }))
       // 添加move转场效果，并指定了springMotion曲线
       .combine(TransitionEffect.move(TransitionEdge.END)).animation({curve: curves.springMotion()})
       // 添加非对称的转场效果，由于这里没有设置animation，会跟随上面的TransitionEffect的animation效果，也就是springMotion
       .combine(TransitionEffect.asymmetric(TransitionEffect.scale({
         x: 0,
         y: 0
       }), TransitionEffect.rotate({ angle: 90 })));
   ```
2. 将转场效果通过[transition](../harmonyos-references/ts-transition-animation-component.md)接口设置到组件。

   ```ts
   Text('test')
     .transition(this.effect)
   ```
3. 新增或者删除组件触发转场。

   ```ts
   @State isPresent: boolean = true;
   // ...
   if (this.isPresent) {
     Text('test')
       .transition(this.effect)
   }
   // ...
   // 控制新增或者删除组件
   // 方式一：将控制变量放到animateTo闭包内，未通过animation接口定义动画参数的TransitionEffect将跟随animateTo的动画参数
   this.getUIContext()?.animateTo({ curve: curves.springMotion() }, () => {
     this.isPresent = false;
   })

   // 方式二：直接控制删除或者新增组件，动画参数由TransitionEffect的animation接口配置
   this.isPresent = false;
   ```

完整的示例代码和效果如下，示例中采用直接删除或新增组件的方式触发转场，也可以替换为在[animateTo](../harmonyos-references/ts-explicit-animation.md)闭包内改变控制变量触发转场。

```typescript
import { curves } from '@kit.ArkUI';

@Entry
@Component
struct TransitionEffectDemo {
  @State isPresent: boolean = false;
  // 第一步：创建TransitionEffect
  private effect: TransitionEffect =
    // 创建默认透明度转场效果，并指定了springMotion(0.6, 0.8)曲线
    TransitionEffect.OPACITY.animation({
      curve: curves.springMotion(0.6, 0.8)
    })// 通过combine方法，这里的动画参数会跟随上面的TransitionEffect，也就是springMotion(0.6, 0.8)
      .combine(TransitionEffect.scale({
        x: 0,
        y: 0
      }))// 添加旋转转场效果，这里的动画参数会跟随上面带animation的TransitionEffect，也就是springMotion(0.6, 0.8)
      .combine(TransitionEffect.rotate({ angle: 90 }))// 添加平移转场效果，这里的动画参数使用指定的springMotion()
      .combine(TransitionEffect.translate({ y: 150 })
        .animation({ curve: curves.springMotion() }))// 添加move转场效果，这里的动画参数会跟随上面的TransitionEffect，也就是springMotion()
      .combine(TransitionEffect.move(TransitionEdge.END));

  build() {
    Stack() {
      if (this.isPresent) {
        Column() {
          Text('ArkUI')
            .fontWeight(FontWeight.Bold)
            .fontSize(20)
            .fontColor(Color.White)
        }
        .justifyContent(FlexAlign.Center)
        .width(150)
        .height(150)
        .borderRadius(10)
        .backgroundColor(0xf56c6c)
        // 第二步：将转场效果通过transition接口设置到组件
        .transition(this.effect)
      }

      // 边框
      Column()
        .width(155)
        .height(155)
        .border({
          width: 5,
          radius: 10,
          color: Color.Black
        })

      // 第三步：新增或者删除组件触发转场，控制新增或者删除组件
      Button('Click')
        .margin({ top: 320 })
        .onClick(() => {
          this.isPresent = !this.isPresent;
        })
    }
    .width('100%')
    .height('60%')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/g93ql4jXRXOEV2aqfI485A/zh-cn_image_0000002712403982.gif)

对多个组件添加转场效果时，可以在[animation](../harmonyos-references/ts-animatorproperty.md#animation)动画参数中配置不同的delay值，实现组件渐次出现消失的效果：

```typescript
const ITEM_COUNTS = 9;
const ITEM_COLOR = '#ED6F21';
const INTERVAL = 30;
const DURATION = 300;

@Entry
@Component
struct Index1 {
  @State isGridShow: boolean = false;
  private dataArray: number[] = new Array(ITEM_COUNTS);

  aboutToAppear(): void {
    for (let i = 0; i < ITEM_COUNTS; i++) {
      this.dataArray[i] = i;
    }
  }

  build() {
    Stack() {
      if (this.isGridShow) {
        Grid() {
          ForEach(this.dataArray, (item: number, index: number) => {
            GridItem() {
              Stack() {
                Text((item + 1).toString())
              }
              .size({ width: 50, height: 50 })
              .backgroundColor(ITEM_COLOR)
              .transition(TransitionEffect.OPACITY
                .combine(TransitionEffect.scale({ x: 0.5, y: 0.5 }))// 对每个方格的转场添加delay，实现组件的渐次出现消失效果
                .animation({ duration: DURATION, curve: Curve.Friction, delay: INTERVAL * index }))
              .borderRadius(10)
            }
            // 消失时，如果不对方格的所有父控件添加转场效果，则方格的消失转场不会生效
            // 此处让方格的父控件在出现消失转场时一直以0.99的透明度显示，使得方格的转场效果不受影响
            .transition(TransitionEffect.opacity(0.99))
          }, (item: number) => item.toString())
        }
        .columnsTemplate('1fr 1fr 1fr')
        .rowsGap(15)
        .columnsGap(15)
        .size({ width: 180, height: 180 })
        // 消失时，如果不对方格的所有父控件添加转场效果，则方格的消失转场不会生效
        // 此处让父控件在出现消失转场时一直以0.99的透明度显示，使得方格的转场效果不受影响
        .transition(TransitionEffect.opacity(0.99))
      }
    }
    .size({ width: '100%', height: '100%' })
    .onClick(() => {
      this.getUIContext()?.animateTo({
        duration: DURATION + INTERVAL * (ITEM_COUNTS - 1),
        curve: Curve.Friction
      }, () => {
        this.isGridShow = !this.isGridShow;
      })
    })
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c6/v3/B73jxOAHTseYrRbVJZutAg/zh-cn_image_0000002742122931.gif)
