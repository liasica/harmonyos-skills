---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1583
title: Slider设置渐变色常见场景
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > Slider设置渐变色常见场景
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:12+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:3a951ecb5d75c3316d897d25b3604476689c9b19c9476a612efa0ee0868651eb
---

## 问题现象

Slider组件设置渐变色效果可能遇到以下场景：

场景一：Slider组件如何将滑块设置为渐变色效果？

场景二：Slider组件如何将滑动条设置为渐变色效果？

场景三：Slider组件如何将滑轨设置为渐变色效果？

预期效果：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ae/v3/29sD7EIlTny0_VGTIZWbcw/zh-cn_image_0000002658969517.png)

实际效果：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cb/v3/8qNdbAeESIuSdmtx_DkBGg/zh-cn_image_0000002628610298.png)

场景四：如何实现Slider组件滑动条颜色为渐变色时，滑动条颜色不压缩？

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/55/v3/zmr0eDP1S42DRTwfjH7NFQ/zh-cn_image_0000002658849561.png "点击放大")

## 背景知识

* [Slider](../harmonyos-references/ts-basic-components-slider.md)：滑动条组件，通常用于快速调节设置值，如音量调节、亮度调节等应用场景。
* [trackColor](../harmonyos-references/ts-basic-components-slider.md#trackcolor)：设置滑轨的背景颜色。
* [selectedColor](../harmonyos-references/ts-basic-components-slider.md#selectedcolor18)：设置滑轨的已滑动部分颜色。

## 解决方案

场景一：滑块设置为渐变色效果，可参考官网示例：[滑块设置渐变色](../harmonyos-references/ts-basic-components-slider.md#示例8滑块设置渐变色)。

场景二：滑动条设置为渐变色效果，可参考官网示例：[设置滑动条渐变色](../harmonyos-references/ts-basic-components-slider.md#示例4设置滑动条渐变色)。

场景三：实现滑轨设置渐变色效果，有以下三种方案：

* 方案一：从API version 23开始，新增[trackColorMetrics](../harmonyos-references/ts-basic-components-slider.md#trackcolormetrics23)接口。详见官网示例：[设置滑轨的背景颜色](../harmonyos-references/ts-basic-components-slider.md#示例9设置滑轨的背景颜色)。
* 方案二：设置滑轨背景色为渐变色，将已滑动区域颜色设为透明，透出下层滑轨背景的渐变色，从而实现整个滑轨颜色统一。示例代码如下：

  ```ts
  @Entry
  @Component
  struct PageLinearGradientOne {
    @State trackColor: LinearGradient = new LinearGradient([
      { color: '#0A59F7', offset: 0 },
      { color: '#F1F3F5', offset: 0.5 },
      { color: '#FE0000', offset: 1 }
    ]);

    build() {
      Column() {
        Slider({ style: SliderStyle.OutSet, value: 50 })
          .trackColor(this.trackColor) // 设置滑轨背景为渐变色
          .selectedColor(Color.Transparent) // 设置滑轨已滑动部分为透明色
          .onChange((value: number) => {
            console.info(value.toString());
          });
      }.margin({ top: 12, bottom: 12 });
    }
  }
  ```

  效果如图：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/84/v3/vQMeW6llTPOiBfC-bQOZmA/zh-cn_image_0000002628770196.png "点击放大")
* 方案三：将滑轨的背景颜色及已滑动部分颜色均设置成渐变色。示例代码如下：

  ```ts
  @Entry
  @Component
  struct PageLinearGradientTwo {
    @State trackColor: LinearGradient = new LinearGradient([
      { color: '#0A59F7', offset: 0 },
      { color: '#F1F3F5', offset: 0.5 },
      { color: '#FE0000', offset: 1 }
    ]);
    @State selectedColor: LinearGradient = new LinearGradient([
      { color: '#ff88f70a', offset: 0 },
      { color: '#ff0a0a0a', offset: 0.5 },
      { color: '#ff03fdfd', offset: 1 }
    ]);

    build() {
      Column() {
        Slider({ style: SliderStyle.OutSet, value: 50 })
          .trackColor(this.trackColor) // 设置滑轨背景为渐变色
          .selectedColor(this.selectedColor) // 设置滑轨已滑动部分为渐变色
          .onChange((value: number) => {
            console.info(value.toString());
          });
      }.margin({ top: 12, bottom: 12 });
    }
  }
  ```

  效果如图：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/71/v3/Q7HSykl3TEeXBUYJaOrfdA/zh-cn_image_0000002658969519.png "点击放大")
* 场景四：当滑轨的背景颜色为渐变色时，滑块滑动过程中未选择部分的颜色渐变不会产生压缩效果。因此，为了实现滑轨已选择部分为渐变色且不压缩，可以将滑轨的背景颜色设置为渐变色，并通过设置reverse属性为true来将滑动条取值范围设置为反向，从而将已选择部分和未选择部分替换，实现渐变色不压缩的效果。

  ```ts
  @Entry
  @Component
  struct SliderExample {
    @State selectValue: number = 40;
    @State colorGradient: LinearGradient =
      new LinearGradient([{ color: '#ff0a0a0a', offset: 0 }, { color: '#fff80303', offset: 1 }]);
    @State value: number = 60;

    build() {
      Column({ space: 8 }) {
        Row() {
          Slider({
            value: this.selectValue,
            min: 0,
            max: 100,
            style: SliderStyle.OutSet,
            // 设置滑动条取值范围为反向
            reverse: true
          })
          // 设置滑轨的背景颜色为渐变色
            .trackColor(this.colorGradient)
            // 设置滑轨的已滑动部分颜色为白色，排除干扰
            .selectedColor(Color.White)
            .onChange((value: number) => {
              this.selectValue = value;
              // 滑动取值范围取反后，使用总体减去已选择数值为现在选择数值
              this.value = 100 - this.selectValue;
            })
            .trackThickness(10)
            .blockSize({ width: 10, height: 10 })
          // toFixed(0)将滑动条返回值处理为整数精度
          Text(this.value.toFixed(0)).fontSize(12)
        }
        .width('80%')
      }.width('100%')
    }
  }
  ```

  效果如下：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/6kthIcYCR2uoW8s8KqI9uw/zh-cn_image_0000002628610300.png "点击放大")
