---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-641
title: 如何实现手风琴动画
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 如何实现手风琴动画
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:23+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:00714b52d4d27096cf06de822b31be8b371cfa69e194d8947e734db78f73674f
---

## 问题现象

如何实现手风琴展示的动画效果。

## 背景知识

* [animateTo](../harmonyos-references/arkts-apis-uicontext-uicontext.md#animateto)：显式动画是一个用于平滑过渡动画的方法，通常用于在UI元素中实现平滑的移动、缩放或其他变化效果。它允许你指定一个目标值，并以指定的时间和曲线进行动画过渡。
* [onTouch](../harmonyos-references/ts-universal-events-touch.md#ontouch)：手指触摸动作触发该回调。鼠标左键按下时对应的事件也会转化成触摸事件并触发该回调。

## 解决方案

实现思路如下：

1. 页面布局实现：通过Flex布局创建一个弹性容器，利用ForEach遍历widths数组，生成多个子组件。
2. 动画效果实现：使用onTouch事件监听用户的触摸操作。在手指离开时，利用animateTo实现宽度的还原动画，使元素宽度逐步恢复至默认状态。在手指按下时，对目标元素的宽度进行更新，并借助animateTo实现宽度变化的动画效果，从而实现手风琴动画效果。

完整示例参考如下：

```ts
@Entry
@Component
struct ShadesDemo {
  @State widths: string[] = ['20%', '20%', '20%', '20%', '20%']; // 初始宽度数组
  @State colors: number[] = [Color.Green, Color.Blue, Color.Yellow, Color.Red, Color.Orange];

  build() {
    Flex({ direction: FlexDirection.Row }) {
      ForEach(this.widths, (_: string, index: number) => {
        Column() {
          Image('')
            .width('100%')
            .height('100%')
            .draggable(false)
            .backgroundColor(this.colors[index]);
        }
        .width(this.widths[index])
        .height(300)
        .onTouch((event: TouchEvent) => {
          // 手指离开组件时还原宽度
          if (event.type === TouchType.Up) {
            this.getUIContext().animateTo({ duration: 300, curve: Curve.Ease }, () => {
              this.widths = ['20%', '20%', '20%', '20%', '20%'];
            });
          } else {
            // 手指触摸组件时触发宽度更新
            this.updateWidths(index);
          }
        });
      }, (_: string, index: number) => index.toString());
    };
  }

  private updateWidths(activeIndex: number) {
    this.getUIContext().animateTo({ duration: 300, curve: Curve.Ease }, () => {
      this.widths = this.widths.map((_, idx) =>
      idx === activeIndex ? '60%' : '10%'
      );
    });
  }
}
```
