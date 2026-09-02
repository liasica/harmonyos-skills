---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1547
title: 自定义Slider滑块
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 自定义Slider滑块
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:23+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:2a0f6820de7c955b5e4fce7afc8f6b82203867a38f30063bf45d63eb86e61573
---

## 问题现象

场景一：在Slider组件中，如何实现滑块内部内容的自定义？

场景二：在Slider组件中，如何让其在左边显示图片，并且滑动滑条时图片可以相应切换？

场景三：在Slider组件中，如何实现滑动条上覆盖一个滑动圈，圈内显示滑动的数值？

## 背景知识

* [Slider](../harmonyos-references/ts-basic-components-slider.md)滑动条组件，通常用于快速调节设置值，如音量调节、亮度调节等应用场景。[onChange](../harmonyos-references/ts-basic-components-slider.md#onchange)：Slider拖动或点击时触发此事件回调。[blockStyle](../harmonyos-references/ts-basic-components-slider.md#blockstyle10)：设置滑块形状参数。
* [hitTestBehavior](../harmonyos-references/ts-universal-attributes-hit-test-behavior.md#hittestbehavior)：设置组件的触摸测试类型。hitTestBehavior属性设置为Transparent时，自身和子节点都响应触摸测试，不会阻塞兄弟节点的触摸测试，不会影响祖先节点的触摸测试。

## 解决方案

* 场景一：采用Stack容器，在Slider上层覆盖一个与滑块等大且同位于圆角矩形的[Row](../harmonyos-references/ts-container-row.md)组件承载自定义内容；通过Slider的onChange获取滑动百分比，结合其宽度与边距计算X轴偏移量，并动态赋给Row的[offset](../harmonyos-references/ts-universal-attributes-location.md#offset)，实现两者同步移动。完整代码如下：

  ```ts
  @Entry
  @Component
  struct SliderExample {
    private slideMargin: number = 4;
    @State tipsOffset: number = this.slideMargin;
    private slideWidth: number = 340;
    private blockWidth: number = 60;
    private blockHeight: number = 20;

    build() {
      Column() {
        Stack({ alignContent: Alignment.Start }) {
          Slider({ style: SliderStyle.OutSet, value: 0 })
            .width(this.slideWidth)
            .blockSize({ width: this.blockWidth, height: this.blockHeight })
            .blockColor(Color.Transparent)
            .blockStyle({
              type: SliderBlockType.SHAPE,
              shape: new Rect({ width: this.blockWidth, height: this.blockHeight }).radius(5)
            })
            .onChange((value: number) => {
              this.showTip(value);
            });

          Row() {
            Text('自定义')
              .fontSize(10);
          }
          .width(this.blockWidth)
          .height(this.blockHeight)
          .borderRadius(5)
          .hitTestBehavior(HitTestMode.Transparent)
          .backgroundColor(Color.Grey)
          .justifyContent(FlexAlign.Center)
          .offset({
            x: this.tipsOffset
          });
        }
        .margin({ left: 30, top: 300 });
      };
    }

    private showTip(value: number) {
      let percent = Number((value / 100).toFixed(2));
      this.tipsOffset = this.slideMargin + (this.slideWidth - this.blockWidth - this.slideMargin * 2) * percent;
    }
  }
  ```

  实现效果如下：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2a/v3/bJN22_adQu6b9gmp3_mCLw/zh-cn_image_0000002628609226.png "点击放大")
* 场景二：实现Slider滑动切换图片的效果，通过[overlay](../harmonyos-references/ts-universal-attributes-overlay.md)为Slider绑定图片，并监听onChange事件，根据滑动返回的value值动态切换对应图片。完整代码如下：

  ```ts
  @Entry
  @Component
  struct SliderDemo {
    @State icon: string = 'sys.media.AI_phone';
    iconList: Array<string> = ['sys.media.AI_translate', 'sys.media.AI_circle_viewfinder', 'sys.media.AI_retouch',
      'sys.media.battery_bolt_fill', 'sys.media.AI_phone', 'sys.media.calendar_badge_play', 'sys.media.battery_bolt_fill'];
    @Builder
    OverlayNode() {
      Column() {
        Image($r(this.icon)) // 可根据实际情况引用资源
      }.width(40).height(40).alignItems(HorizontalAlign.Center).margin({ left: 10 })
    };
    build() {
      Column() {
        Slider({ style: SliderStyle.NONE, value: 20 })
          .overlay(this.OverlayNode(), { align: Alignment.Start })
          .trackThickness(60)
          .trackColor('#e0e0e0')
          .selectedColor(Color.White)
          .width('90%')
          .margin({ left: '5%', top: '40%' })
          .blockStyle({ type: SliderBlockType.IMAGE, image: $r(this.icon) }) // 可根据实际情况引用资源
          .onChange(value => {
            if (value < 20) {
              this.icon = this.iconList[0];
            } else if (value >= 20 && value <= 30) {
              this.icon = this.iconList[1];
            } else if (value > 30 && value <= 40) {
              this.icon = this.iconList[2];
            } else if (value > 40 && value <= 50) {
              this.icon = this.iconList[3];
            } else if (value > 50 && value <= 60) {
              this.icon = this.iconList[4];
            } else if (value > 60 && value <= 70) {
              this.icon = this.iconList[5];
            } else {
              this.icon = this.iconList[6];
            };
          });
      }
      .width('100%')
      .height('100%')
      .backgroundColor('#ffececec')
    }
  }
  ```

  实现效果如下：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fb/v3/H0aEZifMQuSwOBJpcEYqSQ/zh-cn_image_0000002628769124.png "点击放大")
* 场景三：监听Slider组件的onChange事件，获取滑动条的数值用[Text](../harmonyos-references/ts-basic-components-text.md)显示出来，再通过offset属性使Text位置和滑块的位置一致，使用[animation](../harmonyos-references/ts-animatorproperty.md)设置Text位置改变时的动画效果。完整代码如下：

  ```ts
  const BLOCK_DEFAULT_BORDER_WIDTH = 4;

  @Entry
  @Component
  struct SliderPage1 {
    @State isTipShow: boolean = false;
    @State tipsOffset: number = 0;
    @State value: string = '0';
    private slideHeight: number = 310;
    private blockSize: number = 50;
    private tipHeight: number = 50;
    private hideTipTask?: number;
    @State sliderChangeMode: SliderChangeMode = SliderChangeMode.Begin;

    // 显示提示框并计算偏移量
    private showTip(value: number) {
      this.isTipShow = true;
      let percent = Number((value / 100).toFixed(2));
      // 计算提示框的偏移量:滑块移动距离 - 提示框居中所需的偏移量
      this.tipsOffset = (this.slideHeight - this.blockSize - BLOCK_DEFAULT_BORDER_WIDTH * 2) * percent -
        (this.tipHeight / 2 - (this.blockSize / 2 + BLOCK_DEFAULT_BORDER_WIDTH));
    }

    private hideTip() {
      clearTimeout(this.hideTipTask);
      this.hideTipTask = setTimeout(() => {
        this.isTipShow = false;
      }, 3000);
    }

    build() {
      Column() {
        Slider({ direction: Axis.Horizontal, style: SliderStyle.InSet })
          .width(this.slideHeight)
          .trackThickness(50)
          .blockSize({ width: this.blockSize, height: this.blockSize })
          .sliderInteractionMode(SliderInteraction.SLIDE_AND_CLICK)
          .onChange((value: number, mode: SliderChangeMode) => {
            this.value = Number((value).toFixed()).toString();
            // 根据不同的变化模式执行不同操作
            switch (mode) {
              case SliderChangeMode.Begin:
                this.sliderChangeMode = SliderChangeMode.Begin;
                this.showTip(value);
                break;
              case SliderChangeMode.Moving:
                this.sliderChangeMode = SliderChangeMode.Moving;
                this.showTip(value);
                break;
              case SliderChangeMode.Click:
                this.sliderChangeMode = SliderChangeMode.Click;
                this.showTip(value);
                break;
              case SliderChangeMode.End:
                this.sliderChangeMode = SliderChangeMode.End;
                this.hideTip();
                break;
            }
          });
        // 显示当前滑块数值的提示文本
        Text(this.value)
          .fontSize(20)
          .height(this.tipHeight)
          .width(this.tipHeight)
          // 设置偏移量，使提示框跟随滑块移动
          .offset({ x: this.tipsOffset, y: -50 })
          .fontColor(Color.Black)
          .textAlign(TextAlign.Center)
          .backgroundColor(Color.Transparent)
          .borderRadius(25)
          // 设置点击测试行为为透明，使提示框不拦截点击事件
          .hitTestBehavior(HitTestMode.Transparent)
          // 添加动画效果
          .animation({
            duration: this.sliderChangeMode === SliderChangeMode.Moving ? 50 : 340,
            curve: Curve.FastOutSlowIn,
            iterations: 1,
            playMode: PlayMode.Normal
          });
      }
      .alignItems(HorizontalAlign.Start)
      .padding(20)
      .height('100%')
      .width('100%');
    }
  }
  ```

  实现效果如下：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/72/v3/Muo-vrXVR5G2j5bn98OmAQ/zh-cn_image_0000002658968443.png "点击放大")

## 常见FAQ

Q：如何去除Slider组件的滑块阴影？

A：通过配置Slider组件的blockStyle属性，将type设置为SliderBlockType.SHAPE，并自定义圆形滑块，可以有效去除滑块的阴影部分。
