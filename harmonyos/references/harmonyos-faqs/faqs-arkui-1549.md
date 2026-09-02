---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1549
title: 如何解决打断无限循环动画后，动画失效问题
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 如何解决打断无限循环动画后，动画失效问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:24+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:15ea41d47f7eb27a9dfb868c3a6e89747b20218e0e76d93a9cf333acf17545f7
---

## 问题现象

第一次触发无限循环动画后，快速连续多次点击打断该无限循环动画，再次点击就无法看到动画了。

## 背景知识

[animateTo](../harmonyos-references/arkts-apis-uicontext-uicontext.md#animateto)：指定由于闭包代码导致的状态变化插入过渡动效。接口参数有两个，分别是value和event，其中value指定[AnimateParam对象](../harmonyos-references/ts-explicit-animation.md#animateparam对象说明)（包括时长、[Curve](../harmonyos-references/js-apis-curve.md#curve)等）event为动画的闭包函数，闭包内变量改变产生的属性动画将遵循相同的动画参数。

## 问题定位

对动画的执行机制进行排查，确认在动画打断过程中是否存在多次叠加的情况，从而导致动画未能正常显示。

## 分析结论

动画并未真正消失，而是在每次打断过程中被持续叠加，由于叠加的动画实例过多，彼此之间相互覆盖或干扰，导致在视觉上表现不明显，从而给人以动画消失的错觉。

## 修改结论

首先，应设置一个duration为0的动画，用于确保在每次动画被中断时，能够清除前一次的动画实例，避免动画叠加；该动画的属性值需设置为一个与上一次动画最终状态不同的指定值，以确保状态的更新和正确清除。随后，再创建一个用于实现所需初始动画效果的动画实例，以确保动画表现符合预期。

```ts
if (this.isRecording) {
  // 设置一个duration为0的动画停掉上一次动画
  this.getUIContext().animateTo({ duration: 0, iterations: 1, playMode: PlayMode.Normal }, () => {
    // 这里的opacityValue不可以和上一次设置的终止0.1相同
    this.opacityValue = 0.2;
  });
  this.isRecording = false;
  // 再创建需要的动画
  this.getUIContext().animateTo({ duration: 0, iterations: 1, playMode: PlayMode.Normal }, () => {
    this.opacityValue = 1;
  });
} else {
  this.isRecording = true;
  this.getUIContext().animateTo({ duration: 1500, iterations: -1, }, () => {
    this.opacityValue = 0.1;
  });
}
```

完整示例参考如下：

```ts
@Entry
@Component
struct Page {
  @State opacityValue: number = 1;
  @State isRecording: boolean = false;

  build() {
    Row() {
      Column() {
        Text(this.isRecording ? 'Hello World' : 'Welcome')
          .fontSize(50)
          .fontWeight(FontWeight.Bold)
          .opacity(this.opacityValue)
          .textAlign(TextAlign.Center)
          .fontColor('#000')
          .onClick(() => {
            if (this.isRecording) {
              // 设置一个duration为0的动画停掉上一次动画
              this.getUIContext().animateTo({ duration: 0, iterations: 1, playMode: PlayMode.Normal }, () => {
                // 这里的opacityValue不可以和上一次设置的终止0.1相同
                this.opacityValue = 0.2;
              });
              this.isRecording = false;
              // 再创建需要的动画
              this.getUIContext().animateTo({ duration: 0, iterations: 1, playMode: PlayMode.Normal }, () => {
                this.opacityValue = 1;
              });
            } else {
              this.isRecording = true;
              this.getUIContext().animateTo({ duration: 1500, iterations: -1, }, () => {
                this.opacityValue = 0.1;
              });
            }
          });
      }
      .width('100%');
    }
    .height('100%');
  }
}
```
