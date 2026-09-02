---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-709
title: 使用animator动画实现Progress宽高变化效果
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 使用animator动画实现Progress宽高变化效果
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:17+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:37fa71bf75835b8a763b4a1e87cf6f552f301f386447a4832c23312bc92aea10
---

## 问题现象

使用Progress组件实现其上下移动时，可以动态修改Progress组件的宽高值的效果，但移动过程中Progress组件的宽高值并未发生变化。

问题代码示例参考如下：

```ts
@Entry
@Component
struct Index {
  @State cameraTranslateY: number = 0
  @State cameraBtnSize: number = 65
  @State isTranslate: boolean = false // 是否已经向下平移

  aboutToAppear(): void {
  }

  clickEvent() {
    if (this.isTranslate) {
      this.getUIContext().animateTo({ duration: 6000, iterations: 1, playMode: PlayMode.Alternate }, () => {
        this.cameraTranslateY = 0
        this.cameraBtnSize = 65
      })
    } else {
      this.getUIContext().animateTo({ duration: 6000, iterations: 1, playMode: PlayMode.Alternate }, () => {
        this.cameraTranslateY = 100
        this.cameraBtnSize = 50
      })
    }
    this.isTranslate = !this.isTranslate
  }

  build() {
    RelativeContainer() {
      Text('点击Progress组件即可看到效果')
        .alignRules({
          top: { anchor: '__container__', align: VerticalAlign.Top },
          middle: { anchor: '__container__', align: HorizontalAlign.Center }
        })
        .margin({ top: 60 })
      Row() {
        Progress({ value: 50, total: 100, type: ProgressType.Ring })
          .width(this.cameraBtnSize + 30)
          .aspectRatio(1)
          .color('#FFA04F')
          .backgroundColor('#F3F3F3')
          .style({ strokeWidth: 3 })
          .padding(15)
          .onClick(() => {
            this.clickEvent()
          })
      }
      .width(this.cameraBtnSize + 30)
      .aspectRatio(1)
      .alignRules({
        center: { anchor: '__container__', align: VerticalAlign.Center },
        middle: { anchor: '__container__', align: HorizontalAlign.Center }
      })
      .backgroundColor(Color.Grey)
      .translate({
        y: this.cameraTranslateY
      })

    }
    .width('100%')
    .height('100%')
    .backgroundColor(Color.White)
  }
}
```

问题效果预览：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/73/v3/m-3pLsCmSoelKV9KNKTUpw/zh-cn_image_0000002658914211.gif "点击放大")

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/wClgeBw5Qsmp9YNxY-1C6w/zh-cn_image_0000002628394996.gif "点击放大")

## 背景知识

* [@ohos.animator (动画)](../harmonyos-references/js-apis-animator.md)：本模块提供组件动画效果，包括定义动画、启动动画和以相反的顺序播放动画等。
* [animateTo](../harmonyos-references/arkts-apis-uicontext-uicontext.md#animateto)：UIContext提供animateTo接口来指定由于闭包代码导致的状态变化插入过渡动效。
* [aspectRatio](../harmonyos-references/ts-universal-attributes-layout-constraints.md#aspectratio)：指定当前组件的宽高比，aspectRatio=width/height。
* [translate](../harmonyos-references/ts-page-transition-animation.md#translate)：设置页面转场时的平移效果。

## 解决方案

使用@ohos.animator(动画)和显式动画（animateTo）创建并配置动画，通过translate设置页面转场时的平移效果，最后使用点击事件控制动画的播放形式从而实现Progress组件动态变化效果。

```ts
import { AnimatorResult } from '@kit.ArkUI';

@Entry
@Component
struct ProgressDemo {
  @State cameraTranslateY: number = 0;
  @State cameraBtnSize: number = 65;
  @State isTranslate: boolean = false; // 是否已经向下平移
  private backAnimator: AnimatorResult | undefined = undefined;
  // 创建动画
  create() {
    this.backAnimator = this.getUIContext().createAnimator({
      duration: 6000,
      easing: 'ease',
      delay: 0,
      fill: 'forwards',
      direction: 'normal',
      iterations: 1,
      begin: 100,
      end: 50
    });
    this.backAnimator.onFinish = () => {
      console.info('backAnimator onfinish');
    };
    this.backAnimator.onRepeat = () => {
      console.info('backAnimator repeat');
    };
    this.backAnimator.onCancel = () => {
      console.info('backAnimator cancel');
    };
    this.backAnimator.onFrame = (value: number) => {
      this.cameraBtnSize = value;
    };
  };
  // 页面即将出现时调用
  aboutToAppear(): void {
    this.create();
  };

  build() {
    RelativeContainer() {
      Text('点击Progress组件即可看到效果')
        .alignRules({
          top: { anchor: '__container__', align: VerticalAlign.Top },
          middle: { anchor: '__container__', align: HorizontalAlign.Center }
        })
        .margin({ top: 60 });
      Row() {
        Progress({ value: 50, total: 100, type: ProgressType.Ring })
          .width(this.cameraBtnSize + 30)
          .aspectRatio(1) // 设置宽高比
          .color('#FFA04F')
          .backgroundColor('#F3F3F3')
          .style({ strokeWidth: 3 })
          .padding(15)
          .onClick(() => { // 点击事件处理
            this.isTranslate = !this.isTranslate;
            if (this.isTranslate) {
              this.getUIContext().animateTo({ duration: 6000, iterations: 1, playMode: PlayMode.Alternate }, () => {
                this.cameraTranslateY = 100;
              });
              this.backAnimator?.play();
            } else {
              this.getUIContext().animateTo({ duration: 6000, iterations: 1, playMode: PlayMode.Alternate }, () => {
                this.cameraTranslateY = 0;
              });
              this.backAnimator?.reverse();
            }
          });
      }
      .width(this.cameraBtnSize + 30)
      .aspectRatio(1)
      .alignRules({
        center: { anchor: '__container__', align: VerticalAlign.Center },
        middle: { anchor: '__container__', align: HorizontalAlign.Center }
      })
      .backgroundColor(Color.Grey)
      .translate({
        y: this.cameraTranslateY
      })
    }
    .width('100%')
    .height('100%')
    .backgroundColor(Color.White)
  }
}
```
