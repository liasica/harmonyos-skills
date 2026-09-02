---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-734
title: TextPicker组件如何禁止响应事件
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > TextPicker组件如何禁止响应事件
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:03+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:d28047537e67aee868eec0a99a36e773f06b3dc18b04ccbcb8e06dfd0c7a8b0d
---

## 问题现象

TextPicker组件如何禁止所有响应事件，或者禁止指定响应事件？

## 背景知识

* [enabled](../harmonyos-references/ts-universal-attributes-enable.md#enabled)：用于控制事件交互，值为true表示组件可交互，值为false表示组件不可交互。
* [onGestureJudgeBegin](../harmonyos-references/ts-gesture-customize-judge.md#ongesturejudgebegin)：用于自定义手势判定。

## 解决方案

1. 禁止组件的全部响应事件，可以配置enabled属性值为false使TextPicker组件不可交互，不响应事件。

   ```screen
   @Entry
   @Component
   struct TextPickerExample1 {
     private select: number = 1;
     private fruits: string[] = ['AAAAA', 'BBBBBBBBBBBBB', 'CCCC', 'DDDDDDDD', 'EEE'];

     build() {
       Column() {
         TextPicker({
           range: this.fruits,
           selected: this.select,
           value: this.fruits[this.select]
         })
           // 核心代码：交互能力（false）
           .enabled(false)
           .margin({ bottom: 30 })
       }
       .width('100%')
       .height('100%')
       .justifyContent(FlexAlign.Center)
     }
   }
   ```

   效果预览：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f8/v3/J9yH8ZgURXK_hwdbLJmQpQ/zh-cn_image_0000002658794593.png "点击放大")
2. 禁止组件指定的响应事件，可以通过onGestureJudgeBegin自定义手势判定函数，自主决定是否响应。如下相关代码实现了当前TextPicker的选中项点击事件被禁止，而不影响对其他手势事件的响应。

   ```screen
   @Entry
   @Component
   struct TextPickerExample2 {
     private select: number = 0;
     private fruits: string[] = ['AAAAA', 'BBBBBBBBBBBBB', 'CCCC', 'DDDDDDDD', 'EEE'];

     build() {
       Column() {
         TextPicker({
           range: this.fruits,
           selected: this.select,
           value: this.fruits[this.select]
         })
           .margin({ bottom: 30 })
             // 核心代码：判断是否为点击事件，使用长按做对比
           .gesture(
             LongPressGesture()
               .tag('longPress1') // 设置长按手势标志
               .onAction(() => {
                 console.info('长按longPress');
               })
           )
           .gesture(
             TapGesture()
               .tag('tap1') // 设置点击手势标志
               .onAction(() => {
                 console.info('点击tap1');
               })
           )
           .onGestureJudgeBegin((gestureInfo: GestureInfo, event: BaseGestureEvent) => {
             if (gestureInfo.type === GestureControl.GestureType.TAP_GESTURE) {
               // 返回REJECT会使点击手势失败
               console.info(`REJECT 点击已禁用  event: ${event}`);
               return GestureJudgeResult.REJECT;
             } else {
               // 返回CONTINUE将保持系统判定。
               console.info(`CONTINUE 保持系统判定`);
               return GestureJudgeResult.CONTINUE;
             }
           });
       }
       .width('100%')
       .height('100%')
       .justifyContent(FlexAlign.Center);
     }
   }
   ```

   效果预览：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f/v3/kaYeAGqgSA6oT0E67IfBhw/zh-cn_image_0000002628555226.gif "点击放大")

   以长按手势为例，区分是否禁用对应的手势。代码中设置点击手势标志：“点击tap1”无打印，长按手势标志打印：“长按longPress”。

   日志如下：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/af/v3/FIITL8SZTjGzuUADcSZJeg/zh-cn_image_0000002658914549.png)

## 总结

若需全局禁用组件交互行为，建议优先使用enabled属性，该属性可直接禁用所有事件响应。对于需要选择性禁用特定交互事件的场景，可通过onGestureJudgeBegin方法进行自定义是否响应特定事件。
