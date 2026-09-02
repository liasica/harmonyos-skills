---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1151
title: 图片进度条的实现方案
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 图片进度条的实现方案
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:06+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:b729487bc22323dc832012cf0ce48f1193f8bcea451025e423df62dfcba11ed0
---

## 问题现象

如何实现图片进度条功能？未加载时图片进度条是灰色，加载过程中图片进度条由灰色变成彩色，加载完成后图片进度条完全变成彩色。

## 背景知识

* 层叠布局通过[Stack](../harmonyos-guides/arkts-layout-development-stack-layout.md)容器组件实现位置的固定定位与层叠，容器中的子元素依次入栈，后一个子元素覆盖前一个子元素，子元素可以叠加，也可以设置位置。
* [clipShape](../harmonyos-references/ts-universal-attributes-sharp-clipping.md#clipshape12)可以按指定的形状对当前组件进行裁剪。

## 解决方案

场景一：

1. aboutToAppear生命周期中启动定时器，每150ms触发一次，通过增加状态变量progress从0.0到1.0控制图片变化进度。

   ```screen
   aboutToAppear() {
     this.timer = setInterval(() => {
       this.progress = Math.min(1, this.progress + 0.05);
       if (this.progress >= 1) {
         clearInterval(this.timer);
       }
     }, 150);
   }
   ```
2. 使用Stack叠加两张内容相同但颜色不同的图片比如灰色和彩色，彩色图片始终完整显示在底层，灰色图片通过clipShape进行裁剪，裁剪宽度随progress变化。

   ```screen
   Stack({ alignContent: Alignment.Start }) {
     Image(this.grayImage)
       .width('100%')
       .height('100%')
       .objectFit(ImageFit.Contain)

     Image(this.colorImage)
       .width('100%')
       .height('100%')
       .objectFit(ImageFit.Contain)
       .clip(true)
       .clipShape(new Rect({
         width: `${this.progress * 100}%`,
         height: '100%'
       }));
   }
   .width(300)
   .height(300)
   ```

完整示例参考如下：

```screen
@Entry
@Component
struct ImageProgress {
  @State progress: number = 0.0;
  private grayImage: Resource = $r('app.media.start'); // 对应灰色图片
  private colorImage: Resource = $r('app.media.final'); // 对应彩色图片
  private timer: number = 0;

  aboutToAppear() {
    this.timer = setInterval(() => {
      this.progress = Math.min(1, this.progress + 0.05);
      if (this.progress >= 1) {
        clearInterval(this.timer);
      }
    }, 150);
  }

  aboutToDisappear() {
    clearInterval(this.timer);
  }

  build() {
    Column() {
      Stack({ alignContent: Alignment.Start }) {
        Image(this.grayImage)
          .width('100%')
          .height('100%')
          .objectFit(ImageFit.Contain)

        Image(this.colorImage)
          .width('100%')
          .height('100%')
          .objectFit(ImageFit.Contain)
          .clip(true)
          .clipShape(new Rect({
            width: `${this.progress * 100}%`,
            height: '100%'
          }));
      }
      .width(300)
      .height(300)

      StackSample()
    }
    .width('100%')
    .height('100%')
    .justifyContent(FlexAlign.Center)
  }
}

@Component
export struct StackSample {
  build() {

    Column() {
      Stack() {
        Image($r('app.media.feature_mine_dibu')).width(100);

        Image($r('app.media.feature_mine_jindutiao')).width(70);
      }
      .alignContent(Alignment.Start)
      .width('100%')
      .margin({ top: 50, left: 50 })
      .height(5)
    }
    .justifyContent(FlexAlign.Center)
  }
}
```

场景二：

可以通过采用Stack堆叠两张图片的方式，可以设置第一张图片的宽度为指定值，第二张图片通过当前值直接计算出来宽度，即可实现双图片堆叠彩色进度条功能。

```screen
@Component
export struct StackSample {
  build() {

    Column() {
      Stack() {
        Image($r('app.media.feature_mine_dibu')).width(100);

        Image($r('app.media.feature_mine_jindutiao')).width(70);
      }
      .alignContent(Alignment.Start)
      .width('100%')
      .margin({ top: 50, left: 50 })
      .height(5)
    }
    .justifyContent(FlexAlign.Center)
  }
}
```
