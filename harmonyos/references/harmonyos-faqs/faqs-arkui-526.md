---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-526
title: 如何实现唱片机指针摆动动画效果
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 如何实现唱片机指针摆动动画效果
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:23+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:df01b9bdcf2ebf61a8c1d1eb0ec18a27208560f55a0229fe767ddbe5b7c03159
---

## 问题现象

如何实现如下效果：页面中包含播放按钮和指针图片，当点击播放时，指针图片逆时针偏移，当点击暂停时，指针图片恢复至原来位置。

## 背景知识

* UIContext提供[animateTo](../harmonyos-references/arkts-apis-uicontext-uicontext.md#animateto)接口来指定由于闭包代码导致的状态变化插入过渡动效。
* [rotate](../harmonyos-references/ts-universal-attributes-transformation.md#rotate)是HarmonyOS提供的一种通用属性，用于设置组件旋转效果。

## 解决方案

1. 给需要添加动画的组件添加rotate属性，设置组件的旋转角度。

   ```ts
   .rotate({ angle: this.rotateAngle, centerX: 30, centerY: 100 }); // 图片旋转属性
   ```
2. 在animateTo显式动画的闭包函数中判断当前打开状态，设置旋转角度。

   ```ts
   // 显式动画执行，逆时针旋转30度
   this.getUIContext().animateTo({
     duration: 800,
     curve: Curve.Friction,
     delay: 300,
     iterations: 1, // 设置-1表示动画无限循环
     playMode: PlayMode.Alternate,
     expectedFrameRateRange: {
       min: 20,
       max: 120,
       expected: 90,
     }
   }, () => {
     if (this.flag) {
       this.rotateAngle = -30;
     } else {
       this.rotateAngle = 0;
     }
   });
   ```

   完整示例参考如下：

   ```ts
   @Entry
   @Component
   struct AttrAnimationExample {
     @State rotateAngle: number = 0; // 旋转弧度
     @State flag: boolean = false; // 是否播放

     build() {
       Column() {
         Stack() {
           Row() {
             Text('唱片机内容').fontSize(16);
           }
           .width('100%')
           .height(200)
           .backgroundColor('#87CEEB')
           .justifyContent(FlexAlign.Center);

           Row() {
             Image($r('app.media.startIcon')) // 此处仅为样例，请开发者更换为可用图片
               .width(60)
               .height(100)
               .rotate({ angle: this.rotateAngle, centerX: 30, centerY: 100 }); // 图片旋转属性
           }
           .alignItems(VerticalAlign.Bottom)
           .width('100%')
           .justifyContent(FlexAlign.End)
           .height(200);
         };

         // 播放/暂停按钮
         Button(this.flag ? '暂停' : '播放').onClick(() => {
           this.flag = !this.flag;
           // 显式动画执行，逆时针旋转30度
           this.getUIContext().animateTo({
             duration: 800,
             curve: Curve.Friction,
             delay: 300,
             iterations: 1, // 设置-1表示动画无限循环
             playMode: PlayMode.Alternate,
             expectedFrameRateRange: {
               min: 20,
               max: 120,
               expected: 90,
             }
           }, () => {
             if (this.flag) {
               this.rotateAngle = -30;
             } else {
               this.rotateAngle = 0;
             }
           });
         })
           .margin({ top: 40 });
       }
       .padding({ left: 12, right: 12 })
       .height('100%')
       .width('100%');
     }
   }
   ```
