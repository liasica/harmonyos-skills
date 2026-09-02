---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1198
title: Slider组件自定义气泡开发
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > Slider组件自定义气泡开发
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:07+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:c4c012cf0232f21c4e49e07f971d9a4ebb5d89adc8d87d392745ca0eda4877bf
---

## 问题现象

在开发自定义Slider组件过程中，气泡提示功能的定制是良好用户体验的关键环节。在开发过程中，我们通常会遇到以下几类具体场景。

**场景一**：样式与行为定制需求。如何自定义气泡样式、监听气泡行为？

**场景二**：动态内容更新需求。如何实现一个带刻度的Slider组件，在滑块滑动过程中，Slider气泡可动态更新UI内容？

**场景三**：内容完整展示需求。如何实现一个Slider气泡，气泡内显示较长文本时，可确保内容完整展示，不被截断？

## 背景知识

* [Slider](../harmonyos-references/ts-basic-components-slider.md)：滑动条组件，通常用于快速调节设置值，如音量调节、亮度调节等应用场景。通过配置[showTips](../harmonyos-references/ts-basic-components-slider.md#showtips)为true，可查看气泡基础样式，具体可见[示例1](../harmonyos-references/ts-basic-components-slider.md#示例1滑动条基础样式)。
* [气泡提示（Popup）](../harmonyos-guides/arkts-popup-and-menu-components-popup.md)：Popup属性可绑定在组件上显示气泡弹窗提示，设置弹窗内容、交互逻辑和显示状态。
* [bindPopup](../harmonyos-references/ts-universal-attributes-popup.md#bindpopup)：为组件绑定Popup气泡，API介绍请参考：[Popup控制](../harmonyos-references/ts-universal-attributes-popup.md)。

## 解决方案

针对上述问题，我们的核心目标是：构建一个高度可定制的Slider气泡提示组件。为实现此目标，解决方案将围绕三个层面系统展开：

* **层次一**、整体布局层。
  + 容器结构：采用[Stack](../harmonyos-references/ts-container-stack.md)层叠布局，将Slider与气泡组件叠加显示。
  + 气泡实现方式：可使用showTips(false)关闭系统气泡，选择系统Popup组件或自定义组件比如[Text](../harmonyos-references/ts-basic-components-text.md)模拟气泡。
  + 组件位置控制：基于Slider滑块位置计算气泡偏移量，使用[position](../harmonyos-references/ts-universal-attributes-location.md#position)控制气泡位置。
* **层次二**、气泡基础样式层。
  + 内容自定义：在Popup组件或Text组件中实现气泡内容、文本内容的自定义。
  + 样式自定义：同样，上述方式自定义的气泡支持背景色、文字颜色、圆角、内边距等样式的灵活配置。
  + 位置微调：使用[offset](../harmonyos-references/ts-universal-attributes-location.md#offset)实现位置的微调，以便气泡与滑块对齐。
* **层次三**、气泡交互行为层。
  + 显隐控制：使用[if/else：条件渲染](../harmonyos-guides/arkts-rendering-control-ifelse.md)动态控制气泡的显示与隐藏。
  + 交互识别：基于[SliderChangeMode](../harmonyos-references/ts-basic-components-slider.md#sliderchangemode枚举说明)滑动模式识别，识别气泡行为。
  + 定时管理：使用[setTimeout](../harmonyos-references/js-apis-timer.md#settimeout)定时器管理气泡的延迟隐藏。

具体实现方案。

基于以上框架，我们按照“从共性到个性”的顺序，横向梳理每个场景的具体实现步骤：

* **场景一**：实现气泡样式自定义、行为监听。

  此场景是基础能力构建，其实现逻辑贯穿上述三个层次：

  1. 整体布局层。采用Stack层叠布局，使用Text组件模拟气泡，基于Slider滑块位置计算气泡偏移量并通过position控制气泡位置。
  2. 气泡基础样式层。在自定义的Text组件中实现气泡内容、文本内容的自定义。
  3. 气泡交互行为层。使用if/else条件渲染动态控制气泡的显隐，基于SliderChangeMode滑动模式识别，识别气泡行为。使用setTimeout定时器管理气泡的延迟隐藏。
  4. 气泡消失事件的监听，消失后进行业务逻辑处理。

  ```ts
  @Entry
  @Component
  struct CustomSliderPage1 {
    tipOffsetY: number = -28;
    hideDelay: number = 400;
    @State sliderValue: number = 30;
    @State tipShow: boolean = false;
    @State tipX: number = 0;
    @State animatedTipX: number = 0; // 动画的平滑位置
    private sliderWidth: number = 340;
    private blockSize: number = 20;
    private hideTask: number = -1;
    private lastUpdateTime: number = Date.now(); // 防抖动控制

    // 基于Slider滑块位置计算气泡偏移量
    private calculateExactPosition(value: number): number {
      const percent = value / 100;
      const blockCenter = percent * (this.sliderWidth - this.blockSize) + (this.blockSize / 2);
      const tipWidth = 40;
      return Math.max(0, Math.min(blockCenter - (tipWidth / 2), this.sliderWidth - tipWidth));
    }

    private showTip(value: number) {
      const now = Date.now();

      // 防抖动：如果更新太频繁，限制更新频率
      if (now - this.lastUpdateTime < 16) {
        return;
      }

      this.lastUpdateTime = now;
      this.sliderValue = value;

      // 计算精确位置
      const newTipX = this.calculateExactPosition(value);

      // 使用动画平滑过渡
      this.getUIContext()?.animateTo({
        duration: 30,
        curve: Curve.EaseOut
      }, () => {
        this.tipX = newTipX;
        this.animatedTipX = newTipX;
      });

      this.tipShow = true;
    }

    // 气泡消失事件的监听，消失后进行业务逻辑处理。
    onTipsHide() {
      console.info(`气泡已消失，最终值=${this.sliderValue}`);
      // 这里写业务逻辑
    }

    // 使用setTimeout定时器管理气泡的延迟隐藏。
    private delayedHideTip() {
      clearTimeout(this.hideTask);
      this.hideTask = setTimeout(() => {
        this.getUIContext()?.animateTo({
          duration: 100,
          curve: Curve.EaseOut
        }, () => {
          const finalX = this.calculateExactPosition(this.sliderValue);
          this.tipX = finalX;
          this.animatedTipX = finalX;
        });
        setTimeout(() => {
          this.tipShow = false;
          this.onTipsHide();
        }, 50);
      }, this.hideDelay);
    }

    build() {
      Column({ space: 50 }) {
        // 采用Stack层叠布局，将Slider与气泡组件叠加显示。
        Stack() {
          Slider({
            value: this.sliderValue,
            min: 0,
            max: 100,
            step: 1
          })
            .width(this.sliderWidth)
            .height(40)
            .showTips(false)
            // 基于SliderChangeMode滑动模式识别，识别气泡行为。
            .onChange((v: number, mode: SliderChangeMode) => {
              if (mode === SliderChangeMode.Moving ||
                mode === SliderChangeMode.Click) {
                this.showTip(v);
              } else if (mode === SliderChangeMode.End) {
                this.delayedHideTip();
              }
            });
          // 使用if/else：条件渲染动态控制气泡的显示与隐藏。
          if (this.tipShow) {
            // 使用Text模拟气泡。在自定义气泡上实现需要的内容与样式。使用position控制气泡位置。
            Text(`${this.sliderValue}`)
              .fontSize(16)
              .fontColor(Color.White)
              .backgroundColor(Color.Grey)
              .borderRadius(6)
              .padding({
                left: 8,
                right: 8,
                top: 4,
                bottom: 4
              })
              .position({ x: this.animatedTipX, y: this.tipOffsetY });
          }
        }
        .width(this.sliderWidth)
        .height(60);
      }
      .width('100%')
      .height('100%')
      .padding(34);
    }
  }
  ```

  效果预览：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0e/v3/_AbsFYa8QHuuoLVp92MIsA/zh-cn_image_0000002658952787.png "点击放大")
* **场景二**：滑块移动时的动态UI展示。

  此场景在场景一的基础上，增强了内容刷新的功能：

  继承基本布局与交互方案：使用Column布局和条件渲染显隐控制，保持基础的交互识别逻辑。

  关键增强：将气泡实现方式升级为Popup组件，通过@Builder自定义丰富的气泡内容；在Slider的onChange回调中，实时同步更新气泡内容，实现UI的动态刷新。

  ```ts
  @Entry
  @Component
  struct CustomSliderPage2 {
    @State isTipShow: boolean = true;
    @State tipsOffset: number = 0;
    @State offsetY: number = 0;
    @State value: number = 0;
    @State beginX: number = 0;
    private slideWidth: number = 340;
    private slideStepSize: number = 5;
    private blockSize: number = 32;
    // 需要将app.media.background替换为实际资源值。
    private imgArr: string[] =
      ['app.media.background', 'app.media.background', 'app.media.background', 'app.media.background',
        'app.media.background', 'app.media.background',
        'app.media.background', 'app.media.background', 'app.media.background', 'app.media.background'];

    // 基于Slider滑块位置计算气泡偏移量
    private showTip(value: number) {
      this.isTipShow = true;
      let percent = Number((value / 100).toFixed(2));
      this.tipsOffset =
        Math.round(this.getUIContext().px2vp(this.beginX)) + (this.slideWidth - 8) * percent + (0.8 - percent) * 5;
    }

    // @Builder自定义气泡内容。
    @Builder
    popupBuilder() {
      Column() {
        Image($r(this.imgArr[this.value / 10]))
          .height(10)
          .margin({ top: 10 });
        Row({ space: 2 }) {
          Text(`第${this.value / 10 + 1}条`).fontSize(10)
            .fontSize(14);
        }.height(50).padding(5);
      }.width(60);
    }

    build() {
      Column() {
        Slider({
          style: SliderStyle.OutSet,
          step: 10,
          direction: Axis.Horizontal,
          value: this.value
        })
          .showSteps(true)
          .stepSize(this.slideStepSize)
          .stepColor('#660a59f7')
          .height(50)
          .width(this.slideWidth)
          .selectedColor(Color.Green)
          .trackColor('#ffb8b0b0')
          .trackThickness(5)
          .blockSize({ width: 12, height: 12 })
          .blockColor(Color.White)
          .selectedColor('#0A59F7')
          .onAreaChange((oldValue: Area, newValue: Area) => {
            this.offsetY = 0;
            this.beginX = Math.round(Number(newValue.globalPosition.x));
            this.showTip(this.value);
          })
          // 基于SliderChangeMode滑动模式识别，识别气泡行为。
          .onChange((value: number, mode: SliderChangeMode) => {
            this.value = value;
            switch (mode) {
              case SliderChangeMode.Begin:
              case SliderChangeMode.Moving:
                this.showTip(value);
                break;
            }
          });
        // 使用if/else：条件渲染动态控制气泡的显示与隐藏。
        if (this.isTipShow) {
          Row() {
          }
          .width(this.blockSize)
          .height(this.blockSize)
          .position({ x: this.tipsOffset, y: this.offsetY })
          // 绑定系统Popup组件实现气泡
          .bindPopup(true, {
            builder: this.popupBuilder,
            placement: Placement.Bottom,
            mask: false,
            arrowOffset: 0,
            popupColor: Color.White,
            enableArrow: true,
            arrowPointPosition: ArrowPointPosition.CENTER,
            radius: 10,
          });
        }
      }
      .alignItems(HorizontalAlign.Center)
      .padding({
        top: 10
      })
      .height('100%')
      .width('100%');
    }
  }
  ```

  效果预览：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/af/v3/oU_7N39fQzO0Az50x8nI1w/zh-cn_image_0000002658832825.png "点击放大")
* **场景三**：气泡内容长文本展示。

  此场景在场景二的基础上，聚焦长文本样式的增强：

  继承布局方案：保持Stack层叠布局和Popup气泡实现方式。

  关键增强：使用Popup组件自带的长文本滚动逻辑，通过AvoidanceMode.COVER\_TARGET避免目标遮挡。以确保长文本能充分的展示。

  ```ts
  @Entry
  @Component
  struct CustomSliderPage3 {
    @State showPopup: boolean = false;
    @State sliderWidth: number = 0;
    @State sliderValue: number = 0;

    // @Builder自定义气泡内容。
    @Builder
    CustomPopup() {
      Column() {
        Scroll() {
          Text('')
            .height(50)
            .borderRadius('50%');
        }.width(200)
        .height(100);
      }.padding(10);
    }

    // 基于Slider滑块位置计算气泡偏移量，同时确保在边界内。
    getSliderPosition(): number {
      const position = this.sliderWidth / 100 * this.sliderValue - this.sliderWidth / 2;
      const maxOffset = this.sliderWidth / 2 - 9;
      const minOffset = -this.sliderWidth / 2 + 9;

      return Math.max(minOffset, Math.min(maxOffset, position));
    }

    build() {
      Column() {
        // 采用Stack层叠布局，将Slider与气泡组件叠加显示。
        Stack() {
          Slider({ value: $$this.sliderValue, style: SliderStyle.NONE })
            .enabled(false)
            .width('90%')
            // 基于SliderChangeMode滑动模式识别，识别气泡行为。
            .onChange((value: number, mode: SliderChangeMode) => {
              if (mode === SliderChangeMode.Begin || mode === SliderChangeMode.Moving ||
                mode === SliderChangeMode.Click) {
                this.showPopup = true;
              } else {
                this.showPopup = false;
              }
            })
            .onSizeChange((oldSize, newSize) => {
              this.sliderWidth = newSize.width as number;
            });

          Circle({ width: 18, height: 18 })
          // 使用offset实现位置的微调，以便气泡与滑块对齐。
            .offset({ x: this.getSliderPosition() })
            .fill('#fff')
            .hitTestBehavior(HitTestMode.None)
            .borderRadius('50%')
            .shadow({ radius: 10, color: Color.Gray })
            // 绑定系统Popup组件实现气泡
            .bindPopup(this.showPopup, {
              builder: this.CustomPopup(),
              placement: Placement.Bottom,
              enableArrow: false,
              mask: false,
              avoidTarget: AvoidanceMode.COVER_TARGET,
              message: 'popup message '.repeat(200)
            });
        }
        .onTouch((e) => {
          if (e.type === TouchType.Down) {
            let touchX = e.touches[0].x;
            // 边界限制，确保滑块在滑动条范围内
            const minX = 0;
            const maxX = this.sliderWidth;

            if (touchX < minX) {
              touchX = minX;
            }
            if (touchX > maxX) {
              touchX = maxX;
            }

            this.sliderValue = (touchX / this.sliderWidth) * 100;
            this.showPopup = true;
          }
          if (e.type === TouchType.Move) {
            let touchX = e.touches[0].x;
            const minX = 0;
            const maxX = this.sliderWidth;

            if (touchX < minX) {
              touchX = minX;
            }
            if (touchX > maxX) {
              touchX = maxX;
            }
            this.sliderValue = (touchX / this.sliderWidth) * 100;
            this.showPopup = true;
          }
        });
      }
      .width('100%')
      .height('100%');
    }
  }
  ```

  效果预览：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/46/v3/kNAHI96hS72IfsdIMT81dQ/zh-cn_image_0000002628593584.png "点击放大")
