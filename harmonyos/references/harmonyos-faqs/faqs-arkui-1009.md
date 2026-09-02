---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1009
title: 如何在全局自定义Builder中实现动画效果
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 如何在全局自定义Builder中实现动画效果
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:25+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:e4a3d0a231bbef2eac21428e7d5dffd0587226380e1f5673242305a1f195a54f
---

## 问题现象

在全局自定义Builder函数中，通过修改组件的属性，如何实现动画效果？问题代码示例参考如下：

```ts
@Builder
function bottomViewBuilder() {
  Column() {
    Image($r('app.media.start_branding_light_icon'))
      .width(150)
  }
  .padding({ bottom: AppStorage.get('bottomRectHeight') as number })
  .justifyContent(FlexAlign.End)
  .backgroundColor($r('app.color.background_color_level2'))
  .width(windowWidth)
  .height(windowHeight - adHeight)
  .animation({
    duration: 1000,
    curve: Curve.Linear,
    playMode: PlayMode.Normal
  })
  .onAppear(() => {
  })
}
```

以上代码中windowWidth、windowHeight、adHeight为全局变量，当全局变量修改时，无法触发动画效果。

## 背景知识

* [实现属性动画](../harmonyos-guides/arkts-attribute-animation-apis.md)：通过可动画属性改变引起UI上产生的连续视觉效果，即为属性动画。属性动画是最基础易懂的动画，ArkUI提供三种动画接口[animateTo](../harmonyos-references/arkts-apis-uicontext-uicontext.md#animateto)、[animation](../harmonyos-references/ts-animatorproperty.md#animation)和[keyframeAnimateTo](../harmonyos-references/ts-keyframeanimateto.md)驱动组件属性按照动画曲线等动画参数进行连续的变化，产生属性动画。
* [Builder函数](../harmonyos-guides/arkts-builder.md)：该函数分为[全局自定义构建函数](../harmonyos-guides/arkts-builder.md#全局自定义构建函数)和[私有自定义构建函数](../harmonyos-guides/arkts-builder.md#私有自定义构建函数)两种形式，全局函数调用时，无法直接通过this指针调用父组件的状态变量，必须通过传参的方式调用@Component父组件内声明的状态变量。同时，如果@Builder传入的参数是两个或两个以上，不会触发动态渲染UI，也就不会触发动画渲染。

## 解决方案

* **方案一**：采用animateTo的方式实现全局自定义构建函数的动画效果。
  1. 由于Builder函数的参数限制，若需实现由多个参数触发的动画效果，建议将多个参数封装为可深度观测的类，通过[@Observed/@ObjectLink](../harmonyos-guides/arkts-observed-and-objectlink.md)、[@ObservedV2/@Trace](../harmonyos-guides/arkts-new-observedv2-and-trace.md)修饰类，实现深度观测，并传递至Builder内。
  2. 将传递的参数绑定可动画的属性，即可在属性修改时触发动画效果。
  3. 在animateTo内绑定动画的参数，并修改可动画的属性。

  ```ts
  @Builder
  function bottomViewBuilderOne(simple: AnimatesOne) {
    Column() {
      Image($r('app.media.startIcon'))
        .width(150);
    }
    .padding({ bottom: AppStorage.get('bottomRectHeight') as number })
    .justifyContent(FlexAlign.End)
    .width(simple.windowWidth)
    .height(simple.windowHeight - simple.adHeight)
    .onAppear(() => {
    });
  }

  // 动画属性只支持状态变量的修改，同时由于Builder的传参限制，建议封装为一个可深度观测的类
  class AnimatesOne {
    @Track windowWidth: number = 100;
    @Track windowHeight: number = 100;
    @Track adHeight: number = 0;
  }

  @Entry
  @Component
  struct OptionOne {
    @State simple: AnimatesOne = new AnimatesOne();

    build() {
      Column() {
        Text('开始动画')
          .onClick(() => {
            this.getUIContext()?.animateTo({
              duration: 2000,
              curve: Curve.Linear,
              iterations: -1,
              playMode: PlayMode.Normal,
              onFinish: () => {
                console.info('play end');
              }
            }, () => {
              this.simple.windowWidth = 200;
              this.simple.adHeight = 50;
            });
          });
        bottomViewBuilderOne(this.simple);
      };
    }
  }
  ```
* **方案二**：采用animation属性动画，实现方式与方案一类似，将方案一的步骤3的动画参数绑定在animation内。

  ```ts
  @Builder
  function bottomViewBuilderTwo(simple: AnimatesTwo) {
    Column() {
      Image($r('app.media.startIcon'))
        .width(150);
    }
    .padding({ bottom: AppStorage.get('bottomRectHeight') as number })
    .justifyContent(FlexAlign.End)
    .width(simple.windowWidth)
    .height(simple.windowHeight - simple.adHeight)
    .animation({
      duration: 3000,
      iterations: -1,
      curve: Curve.Linear,
      playMode: PlayMode.Normal
    })
    .onAppear(() => {
    });
  }

  class AnimatesTwo {
    @Track windowWidth: number = 100;
    @Track windowHeight: number = 100;
    @Track adHeight: number = 0;
  }

  @Entry
  @Component
  struct OptionTwo {
    @State simple: AnimatesTwo = new AnimatesTwo();

    build() {
      Column() {
        Text('开始动画')
          .onClick(() => {
            this.simple.windowWidth = 200;
            this.simple.adHeight = 50;
          });
        bottomViewBuilderTwo(this.simple);
      };
    }
  }
  ```

  效果预览：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e9/v3/07aaHNNOSW2jy-qOkLmbpg/zh-cn_image_0000002658804043.png "点击放大")

  由于全局自定义函数的Builder的父容器Column组件没有设置宽高限制，导致Column组件自适应子组件大小，所以Text组件也跟随移动。
