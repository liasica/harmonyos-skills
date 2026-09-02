---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-performance-31
title: 横竖屏切换卡顿
breadcrumb: FAQ > 应用质量 > 技术质量 > 性能 > 横竖屏切换卡顿
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:51+08:00
doc_updated_at: 2026-07-30
content_hash: sha256:e4e20794e1e8716cd5e674eba897c8794d04136f7388b1a35ad0a56e3a6a0e3a
---

## 问题现象

场景一：静态页面或视频播放页面在平板横竖屏切换时卡顿，不够流畅。

场景二：在页面aboutToAppear中调用setPreferredOrientation设置横屏，在aboutToDisappear中设置竖屏，横竖屏切换时感官上出现卡顿。

## 背景知识

[横竖屏切换](../best-practices/bpta-landscape-and-portrait-development.md)：横竖屏切换功能实现应用内既支持竖屏显示也支持横屏显示的效果。在窗口旋转时，屏幕尺寸变化会导致界面重新布局。为提高横竖屏切换的流畅度，需进行性能优化。

## 问题定位

场景一：

1. 检查是否有页面监听了窗口旋转事件，在接收到事件后触发状态变量的更新，并且该页面没有在aboutToDisappear页面销毁时注销监听事件。
2. 检查是否对文字使用零宽字符，如果该页面上的文字使用了零宽字符，会导致每个字符被转成图片，会带来额外的绘制负载。
3. 检查图片是否使用autoResize属性，当前旋转页面存在一些图片，未经合理的裁剪，图片过大会导致旋转卡顿。
4. 排查当前页面是否存在一些冗余的OnAreaChange事件、模糊或者一些线性变化linearGradient的属性，这些都比较耗时。
5. 检查是否调用window.getLastWindow的方式获取窗口实例出现延迟。

场景二：

在横屏页面的aboutToAppear方法中调用[setPreferredOrientation](../harmonyos-references/arkts-apis-window-window.md#setpreferredorientation9)设置横屏，在aboutToDisappear方法中设置竖屏。由于方向设置在页面生命周期回调中执行，页面转场与方向旋转存在时间差，导致感官上出现卡顿。

## 分析结论

场景一：

* 页面在旋转的页面以外存在其他页面监听了窗口变化等事件，会接收到事件并触发状态变量的更新和组件刷新，导致旋转卡顿。
* 在旋转过程绘制中，由于生成文字缓存非常耗时，所以会把文字转成图片，但是如果该页面上的文字使用了零宽字符，会导致每个字符被转成图片，会带来额外的绘制负载，导致旋转卡顿。
* 当前旋转页面存在一些图片，未经合理的裁剪，图片过大，导致旋转时重绘这些图片耗时过大，出现卡顿现象。
* 当前页面存在一些冗余的OnAreaChange事件、模糊或者一些线性变化linearGradient的属性或者其他耗时操作，这些操作在旋转页面时会重建，导致旋转卡顿。
* 由于getLastWindow底层原因，需要经过查找获取实例，一定程度上会有性能损耗，可能会出现已经发生横屏或者竖屏切换的情况下，状态栏还没切换的情况。

场景二：

在aboutToAppear和aboutToDisappear中调用setPreferredOrientation设置屏幕方向时，方向切换与页面转场动画不同步，页面先完成转场再触发方向旋转，导致视觉上出现卡顿。该问题不属于性能问题，而是方向设置时机不当导致的功能故障。

## 修改建议

场景一：

* 如果在旋转的页面以外存在其他页面没有被销毁，并且监听了窗口变化等事件，会接收到事件并触发状态变量的更新和组件刷新。此时需要使用ArkUI的冻结能力，将页面配置冻结属性，使其在在页面不可见状态下不触发其子组件状态变量的更新。
* 在旋转过程绘制中，由于生成文字缓存非常耗时，所以会把文字转成图片，但是如果该页面上的文字使用了零宽字符，会导致每个字符被转成图片，会带来额外的绘制负载。该场景可以使用[wordBreak](../harmonyos-references/ts-basic-components-text.md#wordbreak11)属性替代。
* 如果当前旋转页面存在一些图片，未经合理的裁剪，图片过大，可以对图片设置[autoResize](../harmonyos-references/ts-basic-components-image.md#autoresize)属性，使图片裁剪到合适的大小进行绘制。
* 排查当前页面的耗时操作，根据是否必须使用来决定进行适当优化，推荐采用多线程并发，可参考[多线程并发概述](../harmonyos-guides/multi-thread-concurrency-overview.md)。
* 调用window.getLastWindow的方式获取窗口实例出现延迟，此类场景的同步要求较高情况下，可以使用[windowStage.getMainWindowSync](../harmonyos-references/arkts-apis-window-windowstage.md#getmainwindowsync9)的同步方式获取窗口实例。

场景二：

通过[NavDestination](../harmonyos-guides/arkts-navigation-architecture.md#navdestination子页面容器)的[preferredOrientation](../harmonyos-references/ts-basic-components-navdestination.md#preferredorientation19)属性声明式设置页面方向，配合[customTransition](../harmonyos-references/ts-basic-components-navdestination.md#customtransition15)添加转场动画，使方向切换与页面转场同步进行，改善视觉卡顿。

示例代码如下：

Index.ets：

```ts
import { LandscapePage } from './LandscapePage';
import { PortraitPage } from './PortraitPage';

@Entry
@Component
struct ExamplePage {
  private stack: NavPathStack = new NavPathStack();

  aboutToAppear(): void {
    this.stack.pushPath({ name: "portrait" });
  }

  @Builder
  MyPageMap(name: string) {
    if (name === 'portrait') {
      PortraitPage();
    } else {
      LandscapePage();
    }
  }

  build() {
    Navigation(this.stack) {
    }
    .width('100%')
    .height('100%')
    .hideNavBar(true)
    .navDestination(this.MyPageMap)
  }
}
```

PortraitPage.ets：

```ts
import { window } from '@kit.ArkUI';

@Component
export struct PortraitPage {
  private info: string = '';
  private stack: NavPathStack | undefined = undefined;

  build() {
    NavDestination() {
      Stack({ alignContent: Alignment.Center }) {
        Button('push LANDSCAPE page').onClick(() => {
          this.stack?.pushPath({ name: 'landscape' }, true);
        })
      }.width('100%').height('100%')
    }
    .width('100%').height('100%')
    .title('竖屏页面')
    .preferredOrientation(window.Orientation.PORTRAIT)
    .backgroundColor(Color.White)
    .onResult((result: ESObject) => {
      if (result !== null && typeof result === 'string') {
        this.info = result;
      }
    })
    .onReady((ctx: NavDestinationContext) => {
      this.stack = ctx.pathStack;
    })
  }
}
```

LandscapePage.ets：

```ts
import { window } from '@kit.ArkUI';

type voidFunc = () => void;

@Component
export struct LandscapePage {
  private stack: NavPathStack | undefined = undefined;
  @State rotateAngle: string = '0deg';
  @State currentOpacity: number = 1;

  build() {
    NavDestination() {
      Stack({ alignContent: Alignment.Center }) {
        Button('push PORTRAIT page').onClick(() => {
          this.stack?.pushPath({ name: 'portrait' });
        })
      }.width('100%').height('100%')
    }
    .width('100%').height('100%')
    .title('横屏页面')
    .preferredOrientation(window.Orientation.LANDSCAPE)
    .backgroundColor(Color.White)
    .opacity(this.currentOpacity)
    .ignoreLayoutSafeArea([LayoutSafeAreaType.SYSTEM], [LayoutSafeAreaEdge.TOP, LayoutSafeAreaEdge.BOTTOM])
    .onReady((ctx: NavDestinationContext) => {
      this.stack = ctx.pathStack;
    })
    .rotate({ angle: this.rotateAngle })
    .customTransition(
      (op: NavigationOperation, isEnter: boolean): Array<NavDestinationTransition> | undefined => {
        const TRANSITION_DURATION: number = 300;
        const ANGLE_DEFAULT: string = '0deg';
        const ANGLE_TILT: string = '-30deg';
        let transitionOneEvent: voidFunc | undefined = undefined;

        if (op === NavigationOperation.PUSH) {
          if (isEnter) {
            this.currentOpacity = 0;
            this.rotateAngle = ANGLE_TILT;
            transitionOneEvent = () => {
              this.rotateAngle = ANGLE_DEFAULT;
              this.currentOpacity = 1;
            }
          } else {
            this.currentOpacity = 0;
          }
        } else if (op === NavigationOperation.POP) {
          if (isEnter) {
            this.rotateAngle = ANGLE_DEFAULT;
          } else {
            this.currentOpacity = 1;
            transitionOneEvent = () => {
              this.rotateAngle = ANGLE_TILT;
              this.currentOpacity = 0;
            }
          }
        }

        if (transitionOneEvent === undefined) {
          return undefined;
        }

        let transitionOne: NavDestinationTransition = {
          duration: TRANSITION_DURATION,
          delay: 0,
          curve: Curve.EaseOut,
          event: transitionOneEvent,
          onTransitionEnd: () => {}
        };
        return [transitionOne];
      })
  }
}
```
