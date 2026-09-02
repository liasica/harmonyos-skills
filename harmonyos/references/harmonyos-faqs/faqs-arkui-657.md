---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-657
title: Video组件实现横竖屏切换和全屏播放
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > Video组件实现横竖屏切换和全屏播放
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:02+08:00
doc_updated_at: 2026-07-30
content_hash: sha256:d31c39ceb757323b91ce377f3c5d247a07423bf349a2049e9841abcd1091140f
---

## 问题现象

在应用中使用Video组件播放视频时，如何实现横竖屏切换并达到全屏播放效果？

## 背景知识

* [Video](../harmonyos-references/ts-media-components-video.md#video-1)是用于播放视频文件并控制其播放状态的组件，其属性[controls](../harmonyos-references/ts-media-components-video.md#controls)可以设置控制视频播放的默认控制栏是否显示。Video组件的控制器对象VideoController的[requestFullscreen](../harmonyos-references/ts-media-components-video.md#requestfullscreen)与[exitFullscreen](../harmonyos-references/ts-media-components-video.md#exitfullscreen)可用于进入/退出全屏播放。Video组件扩展能力相对较弱，如果开发者想自定义视频播放，请参考[视频播放](../harmonyos-guides/video-playback.md)。
* [Window](../harmonyos-references/arkts-apis-window-window.md)（窗口）的[setPreferredOrientation](../harmonyos-references/arkts-apis-window-window.md#setpreferredorientation9)方法用于设置主窗口的显示方向属性，应用可通过调用此方法实现横竖屏切换。同时，应用还可通过[setWindowLayoutFullScreen](../harmonyos-references/arkts-apis-window-window.md#setwindowlayoutfullscreen9)方法设置主窗口或子窗口的布局是否为沉浸式布局。

## 解决方案

Video组件实现视频横竖屏切换与全屏播放，主要有两种实现思路：

* 通过Video组件默认控制栏的全屏按钮触发全屏，并同步将窗口方向切换为横屏。此外，可以通过调用VideoController的requestFullscreen方法实现相同的全屏效果。
* 通过应用扩展布局，并在全屏切换窗口方向为横屏，同时隐藏避让区（状态栏与导航栏），实现窗口全屏布局的沉浸式效果。

无论采用哪种方案，都需要调用setPreferredOrientation调整窗口方向为横屏，否则全屏播放时仍会保持竖屏方向布局。

方案一：使用默认控制栏实现全屏播放。该方案利用Video组件的默认控制栏实现全屏播放功能。当用户点击默认控制栏中的全屏按钮时，视频会进入全屏模式，并切换窗口方向为横屏。退出全屏时，窗口方向恢复为竖屏。这种方式实现简单，适合不需要自定义播放控制界面的场景。示例代码如下：

```ts
import { window } from '@kit.ArkUI';
import { common } from '@kit.AbilityKit';

@Entry
@Component
struct VideoDemo1 {
  private controller: VideoController = new VideoController();
  private context = this.getUIContext().getHostContext() as common.UIAbilityContext;
  private windowClass = (this.context as common.UIAbilityContext).windowStage.getMainWindowSync();

  // 窗口方向切换（横竖屏切换）
  private setOrientation(orientation: Orientation) {
    this.windowClass.setPreferredOrientation(orientation).then(() => {
      console.info('setWindowOrientation: ' + orientation + ' Succeeded.');
    }).catch((err: BusinessError<void>) => {
      console.info('setWindowOrientation: ' + orientation + ' Failed. Cause: ' + err.message);
    });
  }

  build() {
    Column() {
      Video({
        src: $rawfile('video1.mp4'), // 替换为您的本地视频文件路径
        controller: this.controller
      })
        .width('100%')
        .height(300)
        .controls(true) // 使用默认控制栏
        .objectFit(ImageFit.Contain)
          // 全屏状态变化时自动切换横竖屏
          // 当视频切换到全屏播放时，若没有将窗口切换到横屏，将会是一个竖屏全屏播放效果
        .onFullscreenChange((event) => {
          if (event.fullscreen) {
            this.setOrientation(window.Orientation.LANDSCAPE); // 横屏
          } else {
            this.setOrientation(window.Orientation.PORTRAIT); // 竖屏
          }
        });
    }
    .width('100%')
    .height('100%');
  }
}
```

方案二：通过窗口沉浸式布局实现全屏播放。该方案适用于需要自定义控制栏的场景。通过窗口沉浸式布局，同时调整窗口方向为横屏，隐藏状态栏和导航栏，以实现沉浸式的全屏播放效果。退出全屏时，窗口方向恢复为竖屏，状态栏和导航栏恢复显示。示例代码如下：

```ts
import { window } from '@kit.ArkUI';
import { common } from '@kit.AbilityKit';

@Entry
@Component
struct VideoDemo2 {
  private controller = new VideoController();
  private context = this.getUIContext().getHostContext() as common.UIAbilityContext;
  private windowClass = (this.context as common.UIAbilityContext).windowStage.getMainWindowSync();
  // 记录当前是否全屏状态
  @State private isFullScreen: boolean = false;

  build() {
    Stack() {
      Video({
        src: $rawfile('video1.mp4'), // 替换为您的本地视频文件路径
        controller: this.controller
      })
        .width('100%')
        .height(this.isFullScreen ? '100%' : 300)
        .objectFit(ImageFit.Contain)
        .autoPlay(true)
        .loop(true)
        .controls(false);
      // 自定义的控制器，全屏切换
      Row() {
        Text(this.isFullScreen ? '退出全屏' : '进入全屏')
          .fontColor(Color.White);
      }
      .border({ color: Color.White, width: 1 })
      .margin({ bottom: 15 })
      .zIndex(1)
      .onClick(() => {
        this.isFullScreen = !this.isFullScreen;
        this.toggleWindowOrientationAndFullscreen(this.isFullScreen);
      });
    }
    .alignContent(Alignment.Bottom)
    .width('100%');
  }

  // 切换窗口方向、设置窗口全屏布局、控制避让区显隐
  private toggleWindowOrientationAndFullscreen(isFullScreen: boolean) {
    // 1. 窗口方向切换（横竖屏切换）
    let orientation = isFullScreen ? window.Orientation.LANDSCAPE : window.Orientation.PORTRAIT;
    this.windowClass.setPreferredOrientation(orientation).then(() => {
      console.info('setWindowOrientation: ' + orientation + ' Succeeded.');
    }).catch((err: BusinessError<void>) => {
      console.info('setWindowOrientation: ' + orientation + ' Failed. Cause: ' + err.message);
    });
    // 2. 设置窗口全屏布局
    this.windowClass.setWindowLayoutFullScreen(isFullScreen).then(() => {
      console.info('Succeeded in setting the window layout to full-screen mode.');
    }).catch((err: BusinessError<void>) => {
      console.error(`Failed to set the window layout to full-screen mode. Code is ${err.code}, message is ${err.message}`);
    });
    // 3. 设置状态栏显隐
    this.windowClass.setSpecificSystemBarEnabled('status', !isFullScreen).then(() => {
      console.info('Succeeded in setting the status bar to be invisible.');
    }).catch((err: BusinessError<void>) => {
      console.error(`Failed to set the status bar to be invisible. Code is ${err.code}, message is ${err.message}`);
    });
    // 4. 设置导航区域显隐
    this.windowClass.setSpecificSystemBarEnabled('navigationIndicator', !isFullScreen).then(() => {
      console.info('Succeeded in setting the navigation indicator to be invisible.');
    }).catch((err: BusinessError<void>) => {
      console.error(`Failed to set the navigation indicator to be invisible. Code is ${err.code}, message is ${err.message}`);
    });
  }
}
```

## 总结

以上两种方案均能实现Video组件的横竖屏切换与全屏播放功能。方案一利用系统默认控制栏的全屏播放能力，实现简单快捷，适合基础播放场景。方案二通过窗口沉浸式布局和避让区的显隐控制，更适合需要定制界面与交互的场景。开发者可根据实际场景选择适合的实现方式。

## 常见FAQ

Q：当Tabs栏中的视频切换为横屏全屏播放时，如何隐藏Tabs栏？

A：在TabContent中进行视频播放时，若切换至横屏全屏，Tabs栏会随之旋转并仍保留在页面上。要解决此问题，可以在进入全屏时隐藏Tabs栏，退出全屏时再将其显示出来。

```ts
@Entry
@Component
struct TabsView {
  @State isFullScreen: boolean = false;

  build() {
    Tabs() {
      // todo
    }
    .visibility(this.isFullScreen ? Visibility.None : Visibility.Visible); // 需要使用None，隐藏但不参与布局，不进行占位。
  }
}
```

Q：应用采取[组件安全区布局方案](../harmonyos-guides/arkts-develop-apply-immersive-effects.md#组件安全区方案)实现全屏时，Video组件配置expandSafeArea属性有什么限制？

A：[Video组件](../harmonyos-references/ts-media-components-video.md)在使用expandSafeArea扩展安全区域时，组件视频显示内容区域不支持扩展。
