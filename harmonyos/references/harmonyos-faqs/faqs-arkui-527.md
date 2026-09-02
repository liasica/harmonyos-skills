---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-527
title: 如何实现滑块移动并跟随滑块进度显示不同的内容UI
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 如何实现滑块移动并跟随滑块进度显示不同的内容UI
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:01+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:1c96547cae462110ffd51cd6a2bd72c7435b2dc1ef6c3ea8769db72dfb03940f
---

## 问题现象

如何实现带刻度滑动进度条在滑动过程中，滑动到不同的刻度值位置，跟随显示不同的UI，并且显示内容可以自定义？

## 背景知识

可以根据滑块[Slider](../harmonyos-references/ts-basic-components-slider.md)来实现该滑动功能，并使用[showSteps](../harmonyos-references/ts-basic-components-slider.md#showsteps)属性显示刻度值。

## 解决方案

1. 按照滑块的大小设置一个跟随的透明滑块，跟Slider滑块动作保持一致。
2. 滑块跟随Slider滑块运动，计算滑块在屏幕中的位置。
3. 将Popup绑定到Stack滑块，跟随Slider滑块运动。

参考以下demo:

```ts
@Entry
@Component
struct SliderPage {
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

  // 滑块跟随Slider滑块运动，计算滑块在屏幕中的位置
  private showTip(value: number) {
    this.isTipShow = true;
    let percent = Number((value / 100).toFixed(2));
    this.tipsOffset =
      Math.round(this.getUIContext().px2vp(this.beginX)) + (this.slideWidth - 8) * percent + (0.8 - percent) * 5;
  }

  // popup构造器定义弹框内容
  @Builder
  popupBuilder() {
    Column() {
      Image($r(this.imgArr[this.value / 10]))
        .height(10)
        .margin({ top: 10 });
      Row({ space: 2 }) {
        Text(`第${this.value / 10 + 1}条`).fontSize(10)
          .fontSize(16);
      }.height(50).padding(5);
    }.width(60);
  }

  build() {
    Column() {
      if (this.isTipShow) {
        // 按照滑块的大小设置一个跟随的透明滑块，跟Slider滑块动作保持一致，设置当前块的大小保持跟Slider滑块大小一致，代码如下：
        Stack() {
        }
        .width(this.blockSize)
        .height(this.blockSize)
        // tipsOffset：Slider滑块位置的横坐标，offsetY：Slider滑块位置的纵坐标
        .position({ x: this.tipsOffset, y: this.offsetY })
        // 将Popup绑定到Stack滑块，跟随Slider滑块运动
        .bindPopup(true, {
          builder: this.popupBuilder,
          placement: Placement.Bottom,
          mask: false,
          // 指向绑定的组件
          arrowOffset: 0,
          popupColor: Color.White,
          enableArrow: true,
          arrowPointPosition: ArrowPointPosition.CENTER,
          radius: 10,
        });
      }
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
        .blockSize({ width: 10, height: 10 })
        .blockColor(Color.White)
        .selectedColor('#0A59F7')
        .id('slider')
        .onAreaChange((oldValue: Area, newValue: Area) => {
          this.offsetY = 0;
          this.beginX = Math.round(Number(newValue.globalPosition.x));
          this.showTip(this.value);
          console.info('--- Area Change');
        })
        .onChange((value: number, mode: SliderChangeMode) => {
          this.value = value;
          switch (mode) {
            case SliderChangeMode.Begin:
            case SliderChangeMode.Moving:
              this.showTip(value);
              break;
          }
        });
    }
    .alignItems(HorizontalAlign.Center)
    .padding({
      top: 10
    })
    .height('100%')
    .width('100%')
    .backgroundColor('#ffe7e6e6');
  }
}
```
