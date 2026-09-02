---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-performance-20
title: 点击页签，页面切换响应慢
breadcrumb: FAQ > 应用质量 > 技术质量 > 性能 > 点击页签，页面切换响应慢
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:51+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:643a00f4de834e4b59a78a52e0cbce2a1d01f9fa66e89db4b5ba692ddf5a73d2
---

## 问题现象

应用内用于切换不同页面的tab页签，在连续点击切换页面时不流畅、响应慢。

## 背景知识

* [组合手势（GestureGroup）](../harmonyos-guides/arkts-gesture-events-combined-gestures.md)：组合手势由多种单一手势组合而成，通过在GestureGroup中使用不同的[GestureMode](../harmonyos-references/ts-combined-gestures.md#gesturemode枚举说明)来声明该组合手势的类型，支持[顺序识别](../harmonyos-guides/arkts-gesture-events-combined-gestures.md#顺序识别)、[并行识别](../harmonyos-guides/arkts-gesture-events-combined-gestures.md#并行识别)和[互斥识别](../harmonyos-guides/arkts-gesture-events-combined-gestures.md#互斥识别)三种类型。

  ```typescript
  GestureGroup(mode:GestureMode, gesture:GestureType[])
  // mode：为GestureMode枚举类。用于声明该组合手势的类型。
  // gesture：由多个手势组合而成的数组。用于声明组合成该组合手势的各个手势。
  ```
* [点击手势（TapGesture）](../harmonyos-guides/arkts-gesture-events-single-gesture.md#点击手势tapgesture)：点击手势支持单次点击和多次点击，拥有两个可选参数：count和fingers。如果配置多次点击，**上一次抬起和下一次按下的超时时间为300毫秒**。

  ```typescript
  TapGesture(value?:{count?:number, fingers?:number})
  // count：声明该点击手势识别的连续点击次数。默认值为1，若设置小于1的非法值会被转化为默认值。
  // fingers：用于声明触发点击的手指数量，最小值为1，最大值为10，默认值为1。当配置多指时，若第一根手指按下300毫秒内未有足够的手指数按下则手势识别失败。
  ```

## 问题定位

1. 本地尝试复现问题，使用DevEco Profiler中[Frame分析](../harmonyos-guides/ide-insight-session-frame.md)工具抓取点击切换tab页面时的Trace信息。选取User Events泳道以及应用包名泳道。![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/67/v3/EHh_VeUtS36MA6wNgObFgw/zh-cn_image_0000002628555054.png "点击放大")
2. 点击User Events泳道，对照每组手势，计算在下方Details中的duration可以发现在每次点击tab页签后，都需要等待300ms以上时间应用才会开始处理页面切换，因此使用时有不流畅、响应慢的现象。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/1PIXSPtiRuesQckYOwqEPg/zh-cn_image_0000002628395150.png "点击放大")
3. 搜索关键词**GestureMode.Exclusive**，应用组合手势使用的是互斥识别，且双击识别在前，单击识别在后，这导致用户每次单击切换时需要等待300ms，超过双击手势两次点击间隔的阈值后才会被判定为单击手势，触发单击切换后续操作。

   ```typescript
   @Entry
   @Component
   struct ClickDemo {
     @State singleCount: number = 0;
     @State doubleCount: number = 0;

     build() {
       Column() {
         Text(`Exclusive gesture\n tapGesture count is 1:${this.singleCount}\n tapGesture count is 2: ${this.doubleCount} \n`)
           .fontSize(28)
       }
       .justifyContent(FlexAlign.Center)
       .height('100%')
       .width('100%')
       // 以下组合手势为互斥识别，双击手势识别在前，每次单击后会有300ms延迟，单击次数才会+1。
       .gesture(
         GestureGroup(GestureMode.Exclusive,
           TapGesture({ count: 2 })
             .onAction(() => {
               this.doubleCount++;
               }),
           TapGesture({ count: 1 })
             .onAction(() => {
               this.singleCount++;
             })
         )
       )
     }
   }
   ```

## 分析结论

应用tab页签双击和单击具有不同业务逻辑，使用组合手势中的互斥识别，且先绑定了双击识别，导致每次单击手势必须等待300ms，双击手势识别失败后才会被识别成功。而两次点击间隔不超过300ms时会优先识别为双击手势，触发应用绑定的双击手势业务流程。

## 修改建议

1. 建议应用采用[并行识别](../harmonyos-guides/arkts-gesture-events-combined-gestures.md#并行识别)，以在一个Column组件上绑定点击手势和双击手势组成的并行识别手势为例，由于单击手势和双击手势是并行识别，因此两个手势可以同时进行识别，二者互不干涉，从而避免单击后需等待300ms双击判定造成的响应延迟，优化用户使用体验。

   ```typescript
   @Entry
   @Component
   struct ClickDemo {
     @State singleCount: number = 0;
     @State doubleCount: number = 0;

     build() {
       Column() {
         Text(`Parallel gesture\n tapGesture count is 1:${this.singleCount}\n tapGesture count is 2: ${this.doubleCount} \n`)
           .fontSize(28)
       }
       .justifyContent(FlexAlign.Center)
       .height('100%')
       .width('100%')
       // 以下组合手势为并行识别，单击手势识别成功后，若在规定时间内再次点击，双击手势也会识别成功。
       .gesture(
         GestureGroup(GestureMode.Parallel,
           TapGesture({ count: 1 })
             .onAction(() => {
               this.singleCount++;
             }),
           TapGesture({ count: 2 })
             .onAction(() => {
               this.doubleCount++;
             })
         )
       )
     }
   }
   ```
2. 建议应用将原有双击手势绑定的业务功能换绑为其他手势，如下滑、侧滑等，在tab页区域仅识别单击操作，以避免300ms间隔判定带来的卡顿。
