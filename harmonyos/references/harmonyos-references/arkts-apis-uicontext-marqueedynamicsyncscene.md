---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-marqueedynamicsyncscene
title: Class (MarqueeDynamicSyncScene)
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS API > UI界面 > @ohos.arkui.UIContext (UIContext) > Class (MarqueeDynamicSyncScene)
category: harmonyos-references
scraped_at: 2026-09-02T15:00:49+08:00
doc_updated_at: 2026-09-01
content_hash: sha256:1f61170a178da29ffcd70b217920dbabc1ebac118a4045aabb08965be79c3075
---

提供Marquee组件动态帧率的配置能力，支持在Marquee组件运行动画时动态调节帧率，优化性能和功耗，适用于需要在跑马灯场景中平衡动画流畅度和系统资源消耗的场景。

**说明** 

* 本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 本Class首批接口从API version 14开始支持。
* MarqueeDynamicSyncScene继承自[DynamicSyncScene](arkts-apis-uicontext-dynamicsyncscene.md)，对应[Marquee](ts-basic-components-marquee.md)的动态帧率场景。

## 属性

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| type | [MarqueeDynamicSyncSceneType](arkts-apis-uicontext-e.md#marqueedynamicsyncscenetype14) | 是 | 否 | Marquee的动态帧率场景类型。用于指定Marquee组件的动态帧率场景模式，不同场景类型对应不同的帧率调节策略，详见MarqueeDynamicSyncSceneType。 |

**示例：**

```ts
import { MarqueeDynamicSyncSceneType, MarqueeDynamicSyncScene } from '@kit.ArkUI';

@Entry
@Component
struct MarqueeExample {
  @State start: boolean = false;
  @State src: string = '';
  @State marqueeText: string = 'Running Marquee';
  private fromStart: boolean = true;
  private step: number = 10;
  private loop: number = Number.POSITIVE_INFINITY;
  controller: TextClockController = new TextClockController();
  convertToTime(value: number): string {
    let date = new Date(Number(value + '000'));
    let hours = date.getHours().toString().padStart(2, '0');
    let minutes = date.getMinutes().toString().padStart(2, '0');
    let seconds = date.getSeconds().toString().padStart(2, '0');
    return hours + ':' + minutes + ':' + seconds;
  }
  @State frameRateRange: ExpectedFrameRateRange = { min: 0, max: 120, expected: 30 };
  private scenes: MarqueeDynamicSyncScene[] = [];

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Marquee({
        start: this.start,
        step: this.step,
        loop: this.loop,
        fromStart: this.fromStart,
        src: this.marqueeText + this.src
      })
        .marqueeUpdateStrategy(MarqueeUpdateStrategy.PRESERVE_POSITION)
        .width(300)
        .height(80)
        .fontColor('#FFFFFF')
        .fontSize(48)
        .fontWeight(700)
        .backgroundColor('#182431')
        .margin({ bottom: 40 })
        .id('dynamicMarquee')
        .onAppear(()=>{
          this.scenes = this.getUIContext().requireDynamicSyncScene('dynamicMarquee') as MarqueeDynamicSyncScene[];
        })
      Button('Start')
        .onClick(() => {
          this.start = true;
          this.controller.start();
          this.scenes.forEach((scene: MarqueeDynamicSyncScene) => {
            if (scene.type === MarqueeDynamicSyncSceneType.ANIMATION) {
              scene.setFrameRateRange(this.frameRateRange);
            }
          });
        })
        .width(120)
        .height(40)
        .fontSize(16)
        .fontWeight(500)
        .backgroundColor('#007DFF')
      TextClock({ timeZoneOffset: -8, controller: this.controller })
        .format('hms')
        .onDateChange((value: number) => {
          this.src = this.convertToTime(value);
        })
        .margin(20)
        .fontSize(30)
    }
    .width('100%')
    .height('100%')
  }
}
```
