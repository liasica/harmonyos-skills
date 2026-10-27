---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/arkui-kit-faq-0008
title: Slider组件常见问题
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 常见问题 > Slider组件常见问题
category: harmonyos-faqs
scraped_at: 2026-10-28T07:46:59+08:00
doc_updated_at: 2026-10-20
content_hash: sha256:7b2368310366dddfbc7541cdfc13b6a9c8858bda8490e087ce3bcf7df738a7ee
---

**Q：使用Slider组件，如何让滑块在中间可正、负向滑动，且已滑动部分的颜色从中间开始？**

**A**：实现Slider组件滑块正、负向滑动需要用到contentModifier方法，定制Slider内容区。自定义滑轨、滑块以及事件。

* 滑轨可以通过linearGradient实现，在指定渐变色颜色时，开始和结束设置相同的颜色就能实现多段颜色效果。参考代码如下：

  ```ts
  // 自定义滑轨
      Row()
        .width('100%')
        .height(8)
        .borderRadius(4)
        // 通过渐变色实现滑轨-已滑动部分-滑轨，colors索引0滑轨颜色，索引1和索引2已滑动部分颜色，索引3滑轨颜色
        .linearGradient({
          angle: 90,
          colors: [
            [$r('sys.color.ohos_id_color_component_normal'),
              config.value <= 0 ? (0.5 - config.value / config.min / 2) : 0.5],
            [$r('sys.color.ohos_id_color_emphasize'), config.value <= 0 ? (0.5 - config.value / config.min / 2) : 0.5],
            [$r('sys.color.ohos_id_color_emphasize'), config.value >= 0 ? (0.5 + config.value / config.max / 2) : 0.5],
            [$r('sys.color.ohos_id_color_component_normal'),
              config.value >= 0 ? (0.5 + config.value / config.max / 2) : 0.5]
          ]
        });
  ```
* 滑块可以通过设置[offset](../harmonyos-references/ts-universal-attributes-location.md#offset)实现，根据Slider值设置对应的偏移量，确保滑块位置和滑轨已滑部分对应。给滑块添加滑动手势，在手势回调中分别设置triggerChange触发Slider变化。参考代码如下：

  ```ts
  // 自定义滑块
      Circle({ width: 20, height: 20 })
        .id('circle')
        .fill('#fff')
        .borderRadius('50%')
        .shadow({ radius: 10, color: Color.Gray })
        .offset({ x: config.value / config.max * ((config.contentModifier as MySliderStyle).sliderWidth / 2) }) // 设置滑块偏移量
        .gesture(
          PanGesture({ direction: PanDirection.Horizontal, distance: 1 })
            .onActionStart(() => {
              config.triggerChange(config.value, SliderChangeMode.Begin); // 按下滑块
              (config.contentModifier as MySliderStyle).lastOffsetX = 0;
            })
            .onActionUpdate((even) => {
              // 根据滑动距离计算value值
              config.value = config.value +
              Math.round((even.offsetX - (config.contentModifier as MySliderStyle).lastOffsetX) /
              (config.contentModifier as MySliderStyle).sliderWidth * 200);
              config.triggerChange(config.value, SliderChangeMode.Moving);
              (config.contentModifier as MySliderStyle).lastOffsetX = even.offsetX;
            })
            .onActionEnd(() => {
              config.triggerChange(config.value, SliderChangeMode.End); // 离开滑块
            })
        );
  ```
* 点击Slider内容区设置滑动条的值可以通过onTouch实现，当even.type === TouchType.Down时获取按下时的坐标进行计算即可。添加事件分发后，按下可以继续拖动滑块。

  ```ts
  .onTouch((even) => {
      // 点击滑轨修改滑动条值
      if (even.type === TouchType.Down) {
        config.value = Math.round(even.touches[0].x / (config.contentModifier as MySliderStyle).sliderWidth * 200) - 100;
        config.triggerChange(config.value, SliderChangeMode.Click);
      }
    })
    .onChildTouchTest(() => {
      // 事件分发，点击滑轨后可以继续拖动滑块
      return { strategy: TouchTestStrategy.FORWARD_COMPETITION, id: 'circle' };
    });
  ```

完整代码如下：

```ts
@Entry
@Component
struct CustomSlider {
  @State sliderValue: number = 0;
  @State sliderWidth: number = 0;

  build() {
    Column({ space: 10 }) {
      Slider({ value: $$this.sliderValue, min: -100, max: 100 })
        .contentModifier(new MySliderStyle(this.sliderWidth))
        .padding(20)
        .onSizeChange((oldSize, newSize) => {
          // 组件宽度-padding*2就是滑动条的宽度
          this.sliderWidth = (newSize.width as number) - 40;
        });
      Text(`sliderValue:${this.sliderValue}`).fontSize(30);
      Button('+')
        .fontSize(30)
        .size({ width: 50, height: 50 })
        .borderRadius('50%')
        .onClick(() => {
          if (this.sliderValue + 10 > 100) {
            this.sliderValue = 100;
          } else {
            this.sliderValue += 10;
          }
        });
      Button('-')
        .fontSize(30)
        .size({ width: 50, height: 50 })
        .borderRadius('50%')
        .onClick(() => {
          if (this.sliderValue - 10 < -100) {
            this.sliderValue = -100;
          } else {
            this.sliderValue -= 10;
          }
        });
    }
    .height('100%')
    .width('100%');
  }
}

class MySliderStyle implements ContentModifier<SliderConfiguration> {
  sliderWidth: number = 0;
  lastOffsetX: number = 0;

  constructor(sliderWidth: number) {
    this.sliderWidth = sliderWidth;
  }

  applyContent(): WrappedBuilder<[SliderConfiguration]> {
    return wrapBuilder(buildSlider);
  }
}

@Builder
function buildSlider(config: SliderConfiguration) {
  Stack() {
    // 自定义滑轨
    Row()
      .width('100%')
      .height(8)
      .borderRadius(4)
      // 通过渐变色实现滑轨-已滑动部分-滑轨，colors索引0滑轨颜色，索引1和索引2已滑动部分颜色，索引3滑轨颜色
      .linearGradient({
        angle: 90,
        colors: [
          [$r('sys.color.ohos_id_color_component_normal'),
            config.value <= 0 ? (0.5 - config.value / config.min / 2) : 0.5],
          [$r('sys.color.ohos_id_color_emphasize'), config.value <= 0 ? (0.5 - config.value / config.min / 2) : 0.5],
          [$r('sys.color.ohos_id_color_emphasize'), config.value >= 0 ? (0.5 + config.value / config.max / 2) : 0.5],
          [$r('sys.color.ohos_id_color_component_normal'),
            config.value >= 0 ? (0.5 + config.value / config.max / 2) : 0.5]
        ]
      });
    // 自定义滑块
    Circle({ width: 20, height: 20 })
      .id('circle')
      .fill('#fff')
      .borderRadius('50%')
      .shadow({ radius: 10, color: Color.Gray })
      .offset({ x: config.value / config.max * ((config.contentModifier as MySliderStyle).sliderWidth / 2) }) // 设置滑块偏移量
      .gesture(
        PanGesture({ direction: PanDirection.Horizontal, distance: 1 })
          .onActionStart(() => {
            config.triggerChange(config.value, SliderChangeMode.Begin); // 按下滑块
            (config.contentModifier as MySliderStyle).lastOffsetX = 0;
          })
          .onActionUpdate((even) => {
            // 根据滑动距离计算value值
            config.value = config.value +
            Math.round((even.offsetX - (config.contentModifier as MySliderStyle).lastOffsetX) /
            (config.contentModifier as MySliderStyle).sliderWidth * 200);
            config.triggerChange(config.value, SliderChangeMode.Moving);
            (config.contentModifier as MySliderStyle).lastOffsetX = even.offsetX;
          })
          .onActionEnd(() => {
            config.triggerChange(config.value, SliderChangeMode.End); // 离开滑块
          })
      );
  }
  .onTouch((even) => {
    // 点击滑轨修改滑动条值
    if (even.type === TouchType.Down) {
      config.value = Math.round(even.touches[0].x / (config.contentModifier as MySliderStyle).sliderWidth * 200) - 100;
      config.triggerChange(config.value, SliderChangeMode.Click);
    }
  })
  .onChildTouchTest(() => {
    // 事件分发，点击滑轨后可以继续拖动滑块
    return { strategy: TouchTestStrategy.FORWARD_COMPETITION, id: 'circle' };
  });
}
```

运行效果图如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d1/v3/81PqUXFaRaW5Wzt85sKOTw/zh-cn_image_0000002793770213.png "点击放大")。
