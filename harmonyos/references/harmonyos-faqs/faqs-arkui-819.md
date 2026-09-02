---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-819
title: 实现图标点击的动效
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 实现图标点击的动效
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:22+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:5abb4b80d539b8c5e56ff39cff93d56a233867193805e1203f0961336f853d08
---

## 问题现象

如何给点击事件添加动画效果，以提升用户的使用体验？

## 背景知识

* [onTouch](../harmonyos-references/ts-universal-events-touch.md#ontouch)是组件的通用事件，当手指触碰屏幕时会触发该回调。它有一个touchType类型的参数，当值为Down时表示手指按下时触发，当值为Up时表示手指抬起时触发。
* UIContext组件中的[keyframeAnimateTo](../harmonyos-references/ts-keyframeanimateto.md)方法可以用来设置关键帧动画，以实现点击图标的动画效果。

## 解决方案

1. 创建Stack父组件，在其中定义Text文本和Progress进度条组件，实现基本样式效果。
2. 在Progress组件中实现onTouch方法，根据事件类型（Down或Up）调整文本字体大小、按钮尺寸和进度条长度等样式属性，并通过keyframeAnimateTo定义相应的关键帧动画。

```ts
@Entry
@Component
struct ClickAnimationPage {
  length: number = 60;
  @State nLength: number = 60;
  @State fontSizeInfoClick: number = 10;
  @State fontSizeInfoPerformance: number = 15;
  @State valueInfo: number = 0;
  @State count: number = 1;
  @State fontSizeInfoProgress: number = 18;
  uiContext: UIContext | undefined = undefined;

  aboutToAppear(): void {
    this.uiContext = this.getUIContext?.();
  }

  onPageShow(): void {
    this.length = 60;
    setTimeout(() => {
      this.length = 70;
    }, 50);
  }

  build() {
    Column() {
      Row() {
        Text('X')
          .fontColor(Color.Black).fontWeight(700).fontSize(13);
        Text(this.count.toString())
          .fontColor(Color.Black).fontWeight(700).fontSize(this.fontSizeInfoProgress);
      };
      Stack() {
        Column() {
          Text('点击').fontSize(this.fontSizeInfoPerformance).fontColor(Color.White);
        }
        .opacity(0.8)
        .width(this.nLength)
        .height(this.nLength)
        .borderRadius(this.nLength / 2)
        .backgroundColor(Color.Orange)
        .justifyContent(FlexAlign.Center);
        Column() {
          Progress({ value: this.valueInfo, total: 100, type: ProgressType.Ring })
            .width(this.nLength)
            .height(this.nLength)
            .color(Color.Blue)
            .style({ strokeWidth: 5 })
            .onTouch((event: TouchEvent) => {
              if (TouchType.Up === event.type) {
                // 用户可在这自定义实现动画效果
                this.nLength = 60;
                this.fontSizeInfoClick = 10;
                this.fontSizeInfoPerformance = 15;
                this.fontSizeInfoProgress = 15;
                this.valueInfo = 0;
                if (!this.uiContext) {
                  return;
                }
                this.uiContext.keyframeAnimateTo({ iterations: 3 }, [
                  {
                    duration: 100, event: () => {
                    this.valueInfo = 0;
                  }
                  },
                  {
                    duration: 100, event: () => {
                    this.valueInfo = 100;
                  }
                  }
                ]);
              }
              if (TouchType.Down === event.type) {
                // 用户可在这自定义实现动画效果
                this.nLength = 50;
                this.fontSizeInfoClick = 7;
                this.fontSizeInfoPerformance = 10;
                this.fontSizeInfoProgress = 18;
                this.valueInfo = 0;
                ++this.count;
                if (!this.uiContext) {
                  return;
                }
                this.uiContext.keyframeAnimateTo({ iterations: 3 }, [
                  {
                    duration: 100, event: () => {
                    this.valueInfo = 0;
                  }
                  },
                  {
                    duration: 100, event: () => {
                    this.valueInfo = 100;
                  }
                  }
                ]);
              }
            });
        }
        .width(60)
        .height(60)
        .justifyContent(FlexAlign.Center);
      };
    }
    .justifyContent(FlexAlign.Center)
    .alignItems(HorizontalAlign.Center)
    .width('100%')
    .height('100%');
  }
}
```
