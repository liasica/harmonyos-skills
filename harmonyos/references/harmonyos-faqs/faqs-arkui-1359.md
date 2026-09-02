---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1359
title: 如何实现长按进度动画
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 如何实现长按进度动画
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:21+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:ea7259bae54d7042858a928033ccc3ffc00c3bc75dff269da50464a0115a5006
---

## 问题现象

如何实现长按图标，显示环形动态进度完成效果。

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/12/v3/knUBfI_gRlu8t475kpT1gA/zh-cn_image_0000002628601994.png "点击放大")

## 背景知识

* [LongPressGesture](../harmonyos-references/ts-basic-gestures-longpressgesture.md#longpressgesture-1)，长按手势，设置repeat和duration可实现长按时周期性触发回调。onAction，为LongPress手势识别成功回调；onActionEnd，为长按手势抬起后回调。
* [Progress](../harmonyos-references/ts-basic-components-progress.md)，进度条组件，用于显示内容加载或操作处理等进度。配置[ProgressType](../harmonyos-references/ts-basic-components-progress.md#progresstype8枚举说明)，可以实现不同进度条样式，如线性、环形、环形、胶囊形等。

## 解决方案

1. 创建环形Progress组件，设置动态当前进度值this.progressValue。

   ```ts
   Progress({ value: this.progressValue, total: 100, type: ProgressType.Ring })
     .color(Color.Green)
     .width(120)
     .style({ strokeWidth: 5, enableSmoothEffect: true })
     .backgroundColor(Color.Transparent)
   ```
2. 给按钮组件设置长按手势，设置repeat周期，让Progress组件的当前进度值this.progressValue逐渐增大，实现进度条逐渐加载的动效。

   ```ts
   Button('Press').gesture(
     LongPressGesture({ repeat: true, duration: 10 }) // 设置10毫秒重复周期
       .onAction((event: GestureEvent | undefined) => {
         if (event && this.progressValue <= 100) {
           clearInterval(this.animationId);
           this.animationId = null;
           this.progressValue++; // 每次重复当前进度逐渐增加
         }
       })
   ```
3. 抬手调用中，通过setInterval设置周期，让Progress组件的当前进度值this.progressValue逐渐减小，实现进度条逐渐减少的动效。

   ```ts
   .onActionEnd(() => {
     this.animationId = setInterval(() => {
       this.progressValue--; // 每次重复当前进度逐渐减小
       if (this.progressValue <= 0) {
         clearInterval(this.animationId);
       }
     }, 10);
   })
   ```
4. 完整示例参考如下：

   ```ts
   @Entry
   @Component
   struct ProgressRing {
     @State progressValue: number = 0;
     @State animationId: number | null = null;

     build() {
       Column() {
         Stack() {
           Progress({ value: this.progressValue, total: 100, type: ProgressType.Ring })
             .color(Color.Green)
             .width(120)
             .style({ strokeWidth: 5, enableSmoothEffect: true })
             .backgroundColor(Color.Transparent)

           Button('Press').gesture(
             LongPressGesture({ repeat: true, duration: 10 }) // 设置10毫秒重复周期
               .onAction((event: GestureEvent | undefined) => {
                 if (event && this.progressValue <= 100) {
                   clearInterval(this.animationId);
                   this.animationId = null;
                   this.progressValue++; // 每次重复当前进度逐渐增加
                 }
               })

               .onActionEnd(() => {
                 this.animationId = setInterval(() => {
                   this.progressValue--; // 每次重复当前进度逐渐减小
                   if (this.progressValue <= 0) {
                     clearInterval(this.animationId);
                   }
                 }, 10);
               })
           )
             .backgroundColor(Color.Green)
         }
         .margin({ top: 40 })
       }
       .width('100%')
     }
   }
   ```
