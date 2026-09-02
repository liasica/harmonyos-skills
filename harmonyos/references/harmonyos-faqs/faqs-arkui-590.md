---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-590
title: 如何解决Video组件全屏播放时，自定义控制器显示异常的问题
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 如何解决Video组件全屏播放时，自定义控制器显示异常的问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:01+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:e778a70de7a700a33ec22608bfe6a183cd6be1d1afc4356411ebb6bc2c3722c1
---

## 问题现象

自定义Video组件控制条样式，当Video组件横屏全屏时，发现自定义的控制器被隐藏。

通过Text组件定义一个名为“这是一个全屏按钮”的视频控制器。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/83/v3/VGnl-t3yRGGJ_vzde1_u5A/zh-cn_image_0000002658791779.png "点击放大")

点击“这是一个全屏按钮”视频控制器，将视频进行横屏全屏播放。横屏后“这是一个全屏按钮”控制器会消失。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/57/v3/4H0xXu5USaScbB3wjgu7Jg/zh-cn_image_0000002628552402.png "点击放大")

问题代码示例参考如下：

```ts
import { window } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  @State private isFullScreen: boolean = false;
  @State videoSrc: Resource = $rawfile('videoTest.mp4');
  @State previewUri: Resource = $r('app.media.img_1');
  private controller = new VideoController();

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
        .objectFit(ImageFit.Contain)
        .autoPlay(false)
        .id('video_news_detail')
        .alignRules({
          top: { anchor: '__container__', align: VerticalAlign.Top }
        });
      // 期望自定义的控制组件在全屏状态下保持可见
      Text('这是一个全屏按钮')
        .fontColor(Color.White)
        .onClick(() => {
          if (this.isFullScreen) {
            this.controller.exitFullscreen();
          } else {
            this.controller.requestFullscreen(true);
          }
        })
        .id('a')
        .alignRules({
          top: { anchor: '__container__', align: VerticalAlign.Top }
        });
    }
    .align(Alignment.Bottom)
    .width('100%')
    .aspectRatio(16 / 9);
  }

  // 更改屏幕方向landscape为true横屏，false竖屏
  changeOrientation(landscape: boolean) {
    window.getLastWindow(this.getUIContext().getHostContext()).then((lastWindow) => {
      lastWindow.setPreferredOrientation(landscape ? window.Orientation.LANDSCAPE : window.Orientation.PORTRAIT);
    });
  }
}
```

## 效果预览

修改完成后，竖屏播放效果：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/N0-M6xvcTrabmzgjB3M9dA/zh-cn_image_0000002628392512.png "点击放大")

点击“全屏”按钮进入横屏播放效果：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/39/v3/56_qIb1xTFOETlPMxCWgCQ/zh-cn_image_0000002658911729.png "点击放大")

视频横屏后，控制器依旧存在。

## 背景知识

* [Video组件](../harmonyos-references/ts-media-components-video.md)只能实现较简单场景下的视频播放，一般较复杂的视频播放功能推荐使用[AVPlayer](../harmonyos-guides/video-playback.md)。
* 通过自定义组件的[点击事件](../harmonyos-references/ts-universal-events-click.md#onclick12)实现视频的控制器时，控制器可通过Video组件自带的[VideoController](../harmonyos-references/ts-media-components-video.md#videocontroller)的[this.controller.exitFullscreen()](../harmonyos-references/ts-media-components-video.md#exitfullscreen)以及[this.controller.requestFullscreen(true)](../harmonyos-references/ts-media-components-video.md#requestfullscreen)方法实现全屏播放。但是该全屏方法是VideoController自带的方法，只会将视频进行全屏展示，从而导致视频全屏后控制器组件消失。

## 解决方案

采用自定义组件封装Video组件的VideoController方法：

1. 采用[Stack组件](../harmonyos-references/ts-container-stack.md)将“自定义控制器”与视频播放器Video组件重叠，除了全屏方法外，其它方法依旧采用自定义组件封装Video组件的VideoController方法实现。
2. 通过[window.getLastWindow](../harmonyos-references/arkts-apis-window-f.md#windowgetlastwindow9)方法获取窗口信息。
3. 再通过[setPreferredOrientation()](../harmonyos-references/arkts-apis-window-window.md#setpreferredorientation9)方法设置窗口的显示方向。
4. 窗口横屏后，Video组件通过自适应宽高实现横屏下全屏播放且自定义控制条仍然存在的效果。

```ts
import { window } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  @State private isFullScreen: boolean = false;
  @State videoSrc: Resource = $rawfile('videoTest.mp4'); // 视频文件资源需要替换为本地资源
  @State previewUri: Resource = $r('app.media.img_1'); // 视频封面资源需要替换为本地资源
  private controller = new VideoController();
  @State curRate: PlaybackSpeed = PlaybackSpeed.Speed_Forward_1_00_X;

  aboutToAppear(): void {
    window.getLastWindow(this.getUIContext().getHostContext(), (err, data) => {
      data?.setWindowLayoutFullScreen(true); // 设置沉浸式布局
    });
  }

  build() {
    Column() {
      Stack() {
        Video({
          src: this.videoSrc,
          previewUri: this.previewUri,
          controller: this.controller
        })
          .width('100%')
          .loop(false)
          .controls(false)
          .objectFit(ImageFit.Contain)
          .autoPlay(false)
          .id('video_news_detail');
        // 自定义的控制器
        Row() {
          Text('start').onClick(() => {
            this.controller.start(); // 开始播放
          }).margin(5).fontColor(Color.White);
          Text('pause').onClick(() => {
            this.controller.pause(); // 暂停播放
          }).margin(5).fontColor(Color.White);
          Text('0.75').onClick(() => {
            this.curRate = PlaybackSpeed.Speed_Forward_0_75_X; // 0.75倍速播放
          }).margin(5).fontColor(Color.White);
          Text('1').onClick(() => {
            this.curRate = PlaybackSpeed.Speed_Forward_1_00_X; // 原倍速播放
          }).margin(5).fontColor(Color.White);
          Text('2').onClick(() => {
            this.curRate = PlaybackSpeed.Speed_Forward_2_00_X; // 2倍速播放
          }).margin(5).fontColor(Color.White);
          // 修改全屏控制方法，同时删除原问题代码中Video组件的onFullscreenChange判断条件
          Text(this.isFullScreen ? '退出全屏' : '全屏')
            .onClick(() => {
              this.isFullScreen = !this.isFullScreen;
              this.changeOrientation(this.isFullScreen);
            })
            .fontColor(Color.White);
        }
        .margin({ bottom: 20 });
      }
      .height(this.isFullScreen ? '100%' : 260)
      .align(Alignment.Bottom)
      .width('100%');
    }
    .height('100%')
    .backgroundColor(Color.Black)
    .justifyContent(FlexAlign.Center);
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

Q：Video组件没有办法获取到具体的进度条内容，取不到值应该如何解决？

A：可使用功能更齐全的[AVPlayer](../harmonyos-guides/video-playback.md)。

Q：横屏播放后页面的导航条依旧存在，如何去除导航条？

A：采用沉浸模式去除导航条即可，具体参考链接如下：[开发应用沉浸式效果](../harmonyos-guides/arkts-develop-apply-immersive-effects.md)。

## 总结

该自定义视频控制器的方案仅适用于页面仅包含Video组件的情况，若该页面下还有除Video组件和视频控制器组件外的其它组件，则不建议使用该方式，会导致布局错乱，建议使用AVPlayer。
