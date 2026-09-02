---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-747
title: 如何实现自定义Video组件的控制栏功能
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 如何实现自定义Video组件的控制栏功能
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:20+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:950ae28b3288dea866377b4b5ba0b55c3d6a245ddda2074ce52d7f011e753c99
---

## 问题现象

在HarmonyOS应用开发中，使用Video组件进行视频播放时，其自带的控制器（controls）样式固定，可能无法满足特定的UI设计需求。开发者常常需要实现自定义样式的播放/暂停按钮、进度条、音量控制、全屏切换等功能。

## 背景知识

[Video组件](../harmonyos-guides/arkts-common-components-video-player.md)是HarmonyOS提供的基础视频播放组件，通过[VideoController](../harmonyos-references/ts-media-components-video.md#videocontroller)可以便捷地控制视频的播放、暂停、进度调整、全屏等行为。要实现个性化的播放器界面需要将Video组件的[controls](../harmonyos-references/ts-media-components-video.md#controls)属性设置为false以隐藏默认控制器，然后组合使用基础组件（如[Button](../harmonyos-references/ts-basic-components-button.md)、[Slider](../harmonyos-references/ts-basic-components-slider.md)、[Text](../harmonyos-references/ts-basic-components-text.md)）与VideoController的API，自行构建控制栏的布局与交互逻辑。

## 解决方案

Video组件控制栏功能的自定义主要是通过将VideoController与各种基础组件结合实现，以下将分解四个常见自定义场景，详细说明其实现原理并提供关键代码片段。

* **场景一：自定义进度条**。
  + **实现原理：** 基于[Slider组件](../harmonyos-references/ts-basic-components-slider.md)，通过[setCurrentTime](../harmonyos-references/ts-media-components-video.md#setcurrenttime)属性设置视频播放的进度跳转。
  + **关键代码：**

    ```ts
    Slider({
      value: this.currentTime,
      min: 0,
      max: this.durationTime
    })
      .onChange((value: number) => {
        this.controller.setCurrentTime(value); // 设置视频播放的进度跳转到value处
      })
      .width('65%');
    ```
* **场景二：自定义显示视频剩余时长**。
  + **实现原理：** 通过[onUpdate](../harmonyos-references/ts-media-components-video.md#onupdate)和[onPrepared](../harmonyos-references/ts-media-components-video.md#onprepared)事件获取视频总长并监听视频进度变化，在onUpdate事件中计算并更新剩余时长（总时长-当前时间）后，通过[Text组件](../harmonyos-references/ts-basic-components-text.md)进行展示。
  + **关键代码：**

    ```ts
    .onPrepared((event) => {
      if (event) {
        this.durationTime = event.duration;
        this.restTime = event.duration; // 获取视频总长
      }
    })
    .onUpdate((event) => {
      if (event) {
        this.currentTime = event.time;
        this.restTime = this.durationTime - event.time; // 剩余时长等于总长减去当前位置
      }
    });
    ```

    ```ts
    // 展示剩余时长
    Text(`${this.restTime.toString()}s`)
      .width('10%')
      .fontColor(Color.White);
    ```
* **场景三：自定义音量调节**。
  + **实现原理：** 基于Slider组件可实现自定义音量调节，需将其与[@ohos.multimedia.avVolumePanel](../harmonyos-references/ohos-multimedia-avvolumepanel.md)模块的[AVVolumePanel](../harmonyos-references/ohos-multimedia-avvolumepanel.md#avvolumepanel)系统音量面板结合使用。具体地，将Slider的当前值（value）绑定到AVVolumePanel的volumeLevel属性。当用户拖动滑块时，此操作将完成对系统音量的实际调节。
  + **关键代码：**

    ```ts
    Slider({
      value: $$this.voiceValue,
      min: 0,
      max: 15
    })
      .rotate({
        z: 1,
        angle: -90
      })
      .height(150)
      .width(150);
    ```

    ```ts
    AVVolumePanel({
      volumeLevel: this.voiceValue,
      volumeParameter: {
        position: {
          x: 100,
          y: 200
        }
      }
    });
    ```
* **场景四：自定义横竖屏切换**。
  + **实现原理：** 通过[window.getLastWindow()](../harmonyos-references/arkts-apis-window-f.md#windowgetlastwindow9)方法获取窗口信息，再通过[setPreferredOrientation()](../harmonyos-references/arkts-apis-window-window.md#setpreferredorientation9)方法设置窗口的显示方向。
  + **关键代码：**

    ```ts
    // 修改全屏控制方法，同时删除原问题代码中Video组件的onFullscreenChange判断条件
    Text(this.isFullScreen ? '退出全屏' : '全屏')
      .onClick(() => {
        this.isFullScreen = !this.isFullScreen;
        this.changeOrientation(this.isFullScreen);
      })
      .width('15%')
      .fontColor(Color.White);
    ```

    ```ts
    // 更改屏幕方向landscape为true横屏，false竖屏
    changeOrientation(landscape: boolean) {
      window.getLastWindow(this.getUIContext().getHostContext()).then((lastWindow) => {
        lastWindow.setPreferredOrientation(landscape ? window.Orientation.LANDSCAPE : window.Orientation.PORTRAIT);
      });
    }
    ```

完整示例参考如下：

```ts
import { window } from '@kit.ArkUI';
import { AVVolumePanel } from '@kit.AudioKit';

@Entry
@Component
struct VideoControlPage {
  @State private isFullScreen: boolean = false;
  @State videoSrc: Resource = $rawfile('videoTest.mp4'); // 视频文件资源需要替换为本地资源
  @State previewUri: Resource = $r('app.media.foreground'); // 视频封面资源需要替换为本地资源
  private controller = new VideoController();
  @State currentTime: number = 0;
  @State voiceValue: number = 5;
  @State durationTime: number = 100;
  @State play: boolean = false;
  @State restTime: number = 0;

  aboutToAppear(): void {
    this.durationTime = 29;
  }

  build() {
    Stack() {
      Video({
        src: this.videoSrc,
        previewUri: this.previewUri,
        controller: this.controller
      })
        .width('100%')
        .height('100%')
        .loop(false)
        .controls(false)
        .onFullscreenChange((event) => {
          this.isFullScreen = event.fullscreen;
          this.changeOrientation(this.isFullScreen);
        })
        .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.TOP, SafeAreaEdge.BOTTOM])
        .objectFit(ImageFit.Contain)
        .autoPlay(false)
        .id('video_news_detail')
        .onPrepared((event) => {
          if (event) {
            this.durationTime = event.duration;
            this.restTime = event.duration; // 获取视频总长
          }
        })
        .onUpdate((event) => {
          if (event) {
            this.currentTime = event.time;
            this.restTime = this.durationTime - event.time; // 剩余时长等于总长减去当前位置
          }
        });
      // 音量控制器
      Row() {
        Slider({
          value: $$this.voiceValue,
          min: 0,
          max: 15
        })
          .rotate({
            z: 1,
            angle: -90
          })
          .height(150)
          .width(150);
      }
      .margin({ bottom: this.isFullScreen ? 50 : 200 })
      .width('100%')
      .height(200)
      .justifyContent(FlexAlign.Start)
      .zIndex(1);

      // 自定义的控制器
      Row() {
        Text(this.play ? '暂停' : '播放').onClick(() => {
          this.play = !this.play;
          if (this.play) {
            this.controller.start(); // 开始播放
          } else {
            this.controller.pause(); // 暂停播放
          }
        }).margin(5).fontColor(Color.White)
          .width('10%');
        Slider({
          value: this.currentTime,
          min: 0,
          max: this.durationTime
        })
          .onChange((value: number) => {
            this.controller.setCurrentTime(value); // 设置视频播放的进度跳转到value处
          })
          .width('65%');
        // 展示剩余时长
        Text(`${this.restTime.toString()}s`)
          .width('10%')
          .fontColor(Color.White);
        // 修改全屏控制方法，同时删除原问题代码中Video组件的onFullscreenChange判断条件
        Text(this.isFullScreen ? '退出全屏' : '全屏')
          .onClick(() => {
            this.isFullScreen = !this.isFullScreen;
            this.changeOrientation(this.isFullScreen);
          })
          .width('15%')
          .fontColor(Color.White);
      }
      .zIndex(2);

      AVVolumePanel({
        volumeLevel: this.voiceValue,
        volumeParameter: {
          position: {
            x: 100,
            y: 200
          }
        }
      });
    }
    .align(Alignment.Bottom)
    .width('100%');
  }

  // 更改屏幕方向landscape为true横屏，false竖屏
  changeOrientation(landscape: boolean) {
    window.getLastWindow(this.getUIContext().getHostContext()).then((lastWindow) => {
      lastWindow.setPreferredOrientation(landscape ? window.Orientation.LANDSCAPE : window.Orientation.PORTRAIT);
    });
  }

}
```

## 常见FAQ

Q：横屏播放后页面的底部导航条依旧存在，如何去除底部导航条？

A：采用沉浸模式去除导航条即可，具体参考链接如下：[开发应用沉浸式效果](../harmonyos-guides/arkts-develop-apply-immersive-effects.md)。

Q：Video组件默认控制器的进度条如何自定义？

A：Video组件默认控制器的进度条。若有其他需求，可隐藏默认控制器并自定义控制器的样式或功能。
