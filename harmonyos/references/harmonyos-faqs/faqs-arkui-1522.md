---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1522
title: 实现红包雨效果
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 实现红包雨效果
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:18+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:66af0cc4054d14479a84f72f19ab245cf6051dd82cb32077803e178755214471
---

## 问题现象

在HarmonyOS系统中，如何实现红包雨的动画效果呢？

## 背景知识

* 帧动画[animator](../harmonyos-guides/arkts-animator.md)具备逐帧回调的特性，便于开发者在每一帧中处理需调整的属性。通过向应用提供onFrame逐帧回调，帧动画使开发者能够在应用的每一帧设置属性值，从而实现组件属性值变化的自然过渡，营造出动画效果。
* [AnimatorOptions](../harmonyos-references/js-apis-animator.md#animatoroptions)用于定义动画选项。

## 解决方案

1. 创建RedPacketModel类，添加属性用于设置红包的位置，添加getRandomNumber方法用于设置红包出现的间隔。

   ```ts
   @Observed
   class RedPacketModel {
     x: number = 0;
     y: number = -90;
     imageWidth: number = 0;
     delay: number = 0;

     constructor(index: number, imageWidth: number, delay?: number,) {
       this.x = 10 + (imageWidth) * (index - 1) + 10 * index;
       if (delay) {
         this.delay = delay * 1000;
       }
     }

     static getRandomNumber(min: number, max: number) {
       let rand = cryptoFramework.createRandom();
       // 设置生成随机数的字节长度为1
       let randData = rand.generateRandomSync(1);
       // 自定义范围(0-10之内)
       let numRan: number = Math.fround(randData.data[0] * 10 / 2550);
       let num = Math.floor(numRan * (max - min + 1)) + min;
       return num;
     }
   }
   ```
2. 定义RedPacket组件，使用AnimatorOptions设置动画的参数，并通过create方法创建动画，并在animatorResult的onFrame回调方法中设置红包的纵坐标。

   ```ts
   // 创建一个帧动画
   this.animatorResult = this.getUIContext().createAnimator(animatorOption);
   // 接收帧回调，并设置红包的纵坐标
   this.animatorResult.onFrame = (progress: number) => {
     this.model.y = progress;
   };
   ```
3. 在父组件RedPacketRain中创建RedPacketModel并通过ForEach循环渲染即可。

   ```ts
   ForEach(this.redPacketModels, (model: RedPacketModel) => {
     RedPacket({
       model: model,
       imageWidth: this.imageWidth
     });
   });
   ```

完整示例参考如下：

```ts
import { AnimatorOptions } from '@ohos.animator';
import { AnimatorResult, window } from '@kit.ArkUI';
import cryptoFramework from '@ohos.security.cryptoFramework';
@Observed
class RedPacketModel {
  x: number = 0;
  y: number = -90;
  imageWidth: number = 0;
  delay: number = 0;

  constructor(index: number, imageWidth: number, delay?: number,) {
    this.x = 10 + (imageWidth) * (index - 1) + 10 * index;
    if (delay) {
      this.delay = delay * 1000;
    }
  }

  static getRandomNumber(min: number, max: number) {
    let rand = cryptoFramework.createRandom();
    // 设置生成随机数的字节长度为1
    let randData = rand.generateRandomSync(1);
    // 自定义范围(0-10之内)
    let numRan: number = Math.fround(randData.data[0] * 10 / 2550);
    let num = Math.floor(numRan * (max - min + 1)) + min;
    return num;
  }
}
@Component
struct RedPacket {
  @ObjectLink model: RedPacketModel;
  @Link imageWidth: number;
  animatorResult: AnimatorResult | undefined = undefined;

  aboutToAppear(): void {

    let animatorOption: AnimatorOptions = {
      duration: 2000 + (RedPacketModel.getRandomNumber(0, 255) % 250 / 100) * 1000,
      delay: this.model.delay,
      easing: 'linear',
      iterations: 1,
      fill: 'forwards',
      direction: 'normal',
      begin: -90,
      end: 840
    };
    // 创建一个帧动画
    this.animatorResult = this.getUIContext().createAnimator(animatorOption);
    // 接收帧回调，并设置红包的纵坐标
    this.animatorResult.onFrame = (progress: number) => {
      this.model.y = progress;
    };
  }

  build() {
    Stack() {
      Image($r('app.media.startIcon')); // 此处仅为样例，请开发者更换为可用图片
    }
    .width(this.imageWidth)
    .height(this.imageWidth)
    .position({ x: this.model.x, y: this.model.y })
    .onAppear(() => {
      this.animatorResult?.play();
    });
  }
}

@Entry
@Component
struct RedPacketRain {
  @State redPacketModels: RedPacketModel[] = [];
  @State imageWidth: number = 0;

  aboutToAppear(): void {
    window.getLastWindow(this.getUIContext().getHostContext()).then((data) => {
      let properties = data?.getWindowProperties();
      let w = this.getUIContext().px2vp(properties.windowRect.width);
      this.imageWidth = (w - 12 * 4) / 4.0;
      for (let index = 0; index < 30; index++) {
        this.redPacketModels.push(new RedPacketModel(1, this.imageWidth, index));
        this.redPacketModels.push(new RedPacketModel(2, this.imageWidth, index));
        this.redPacketModels.push(new RedPacketModel(3, this.imageWidth, index));
        this.redPacketModels.push(new RedPacketModel(4, this.imageWidth, index));
      }
    });
  }

  build() {
    Stack() {
      ForEach(this.redPacketModels, (model: RedPacketModel) => {
        RedPacket({
          model: model,
          imageWidth: this.imageWidth
        });
      });
    }
    .height('100%')
    .width('100%')
    .clip(true);
  }
}
```
