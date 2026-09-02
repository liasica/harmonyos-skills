---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-998
title: 如何让Slider不显示进度变化动画
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 如何让Slider不显示进度变化动画
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:05+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:4b6fc022479a4fef9312e1793da15fc2a43927f25a980de41f5e22940268186d
---

## 问题现象

Slider在点击和长按某个位置时，如何让进度直接展示，不显示进度变化动画？

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/ZkkJTh5jR_6ArUusJmuy_Q/zh-cn_image_0000002658804037.png "点击放大")

## 背景知识

* [Slider](../harmonyos-references/ts-basic-components-slider.md)：滑动条组件，通常用于快速调节设置值。可以通过[SliderOptions](../harmonyos-references/ts-basic-components-slider.md#slideroptions对象说明)滑动条信息对象设置value控制当前进度值。
* [enabled](../harmonyos-references/ts-universal-attributes-enable.md#enabled)可以设置组件是否可交互。当未设置enabled时，组件默认可交互。
* [onAreaChange](../harmonyos-references/ts-universal-component-area-change-event.md#onareachange)组件区域变化时触发该回调。仅会响应由布局变化所导致的组件大小、位置发生变化时的回调。可以在组件加载完成时获取组件的宽高等信息。
* [onTouch](../harmonyos-references/ts-universal-events-touch.md#ontouch)手指触摸动作触发该回调。通过该回调可以得到触摸事件的类型[TouchType](../harmonyos-references/ts-appendix-enums.md#touchtype)和触点信息[TouchObject](../harmonyos-references/ts-universal-events-touch.md#touchobject)等。

## 解决方案

可以禁用Slider原本的交互逻辑，通过其他事件修改Slider的进度值value，让滑块直接跳转到进度值对应的位置，从而不显示动画，具体步骤如下：

1. 首先给Slider的值设置一个状态变量，通过enabled属性设置为false，禁用Slider原本的交互逻辑。在Slider外加一层容器组件。

   ```ts
   Row() {
     Slider({ value: this.value })
       .backgroundColor('#f1f3f5')
       .enabled(false);
   }
   ```
2. [Row](../harmonyos-references/ts-container-row.md)未设置宽度或高度时，在主轴或交叉轴方向上自适应子组件大小。通过onAreaChange可以直接获取到滑动条组件的宽度，当滑动条的style为[SliderStyle](../harmonyos-references/ts-basic-components-slider.md#sliderstyle枚举说明).OutSet时，左右间距分别为[blockSize](../harmonyos-references/ts-basic-components-slider.md#blocksize10)宽度的一半（SliderStyle.OutSet时blockSize默认宽高18vp），滑动条组件宽度减18vp可以得到滑动条的长度。

   ```ts
   .onAreaChange((oldValue: Area, newValue: Area) => {
     // 计算得到滑动条的长度（18是滑动条的左右边距）
     this.sliderLength = (newValue.width as number) - 18;
   })
   ```
3. 给Slider外的容器组件添加触摸事件，根据触摸时x的坐标计算当前按下位置在整个滑动条的占比，再用最大值计算出按下时滑动条所在的值。通过这种方式修改value不会出现动画效果。

   ```ts
   .onTouch((e) => {
     // 按下时触发
     if (e.type === TouchType.Down) {
       // 通过触摸位置和滑动条长度计算占比，得到滑动条的值（9是滑动条的左边距）
       this.value = (e.touches[0].x - 9) / this.sliderLength * 100;
       console.info((e.touches[0].x - 9).toString());
     }
     // 拖动触发
     if (e.type === TouchType.Move) {
       this.value = (e.touches[0].x - 9) / this.sliderLength * 100;
       console.info((e.touches[0].x - 9).toString());
     }
   });
   ```

完整代码如下：

```ts
@Entry
@Component
struct SliderExample {
  @State value: number = 10; // 滑动条的值
  sliderLength: number = 0; // 滑动条的长度

  build() {
    Column() {
      Row() {
        Slider({ value: this.value })
          .backgroundColor('#f1f3f5')
          .enabled(false);
      }
      .onAreaChange((oldValue: Area, newValue: Area) => {
        // 计算得到滑动条的长度（18是滑动条的左右边距）
        this.sliderLength = (newValue.width as number) - 18;
      })
      .onTouch((e) => {
        // 按下时触发
        if (e.type === TouchType.Down) {
          // 通过触摸位置和滑动条长度计算占比，得到滑动条的值（9是滑动条的左边距）
          this.value = (e.touches[0].x - 9) / this.sliderLength * 100;
          console.info((e.touches[0].x - 9).toString());
        }
        // 拖动触发
        if (e.type === TouchType.Move) {
          this.value = (e.touches[0].x - 9) / this.sliderLength * 100;
          console.info((e.touches[0].x - 9).toString());
        }
      });
    };
  }
}
```
