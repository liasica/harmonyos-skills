---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1366
title: 设置屏幕为常亮状态
breadcrumb: FAQ > 应用框架开发 > UI框架 > 窗口管理 > 设置屏幕为常亮状态
category: harmonyos-faqs
scraped_at: 2026-09-02T15:03:52+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:983364af8c571184399d00d82005e3f90dea9b418e55dd6759ee9e93ff6e16d2
---

## 问题现象

在投屏场景下，用户没有屏幕交互操作，也不希望手机跟随系统设置的休眠时间自动熄屏，而是保持屏幕常亮，该如何设置屏幕为常亮状态？

如何在用户长时间没有进行屏幕交互的情况下，设置手机屏幕常亮？

## 背景知识

* [Window](../harmonyos-references/arkts-apis-window-window.md)：当前窗口实例，窗口管理器管理的基本单元。
* [setWindowKeepScreenOn](../harmonyos-references/arkts-apis-window-window.md#setwindowkeepscreenon9)：设置屏幕是否为常亮状态，使用callback异步回调。

**说明** 

设置保持屏幕常亮的窗口需在前台才能生效，在后台时不生效。

## 解决方案

遇到用户长时间没有屏幕交互的场景，例如视频播放、投屏、导航等场景，为了避免息屏影响用户体验。可以通过setWindowKeepScreenOn接口，将入参isKeepScreenOn属性设置为true来保证屏幕常亮。具体步骤如下：

1. 获取当前屏幕窗口对象。
2. 调用setWindowKeepScreenOn方法设置窗口保持屏幕常亮状态，默认不会常亮。

视频播放时设置屏幕常亮，视频暂停时取消屏幕常亮。

```ts
import { window } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
export struct SetScreenStatePage {
  private controller: VideoController = new VideoController();
  private previewUris: Resource = $r('app.media.startIcon');
  private innerResource: Resource = $r('app.media.videoTest');

  setScreenState(isKeepScreenOn: boolean) {
    // 获取当前窗口实例
    window.getLastWindow(this.getUIContext().getHostContext()).then((curWindow) => {
      // 设置屏幕是否常亮
      curWindow.setWindowKeepScreenOn(isKeepScreenOn, (err: BusinessError) => {
        if (err.code) {
          console.error(`Failed to set the screen. Cause code: ${err.code}, message: ${err.message}`);
          return;
        }
        console.info(`Succeeded in setting the screen ${isKeepScreenOn}.`);
      });
    }).catch((err: string) => {
      console.error(`Failed to obtain the top window.. Cause code:: ${err}`);
    });
  }

  build() {
    Stack({ alignContent: Alignment.TopStart }) {
      Video({
        src: this.innerResource,
        previewUri: this.previewUris,
        controller: this.controller
      })
        .controls(true)
        .autoPlay(false)
        .objectFit(ImageFit.Contain)
        .onStart(() => {
          this.setScreenState(true);
          console.info('视频播放时设置屏幕常亮');
        })
        .onPause(() => {
          this.setScreenState(false);
          console.info('视频暂停时恢复系统息屏');
        });
    }
  }
}
```

运行结果如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/75/v3/zSsADk5yQaW3XisAueK1eg/zh-cn_image_0000002628761922.png "点击放大")

## 常见FAQ

Q：为什么设置了屏幕常亮，但是在APP里依然会息屏。

A：仅在必要场景（导航、视频播放、绘画、游戏等场景）下，设置该属性为true；退出上述场景后，应当重置该属性为false；其他场景（无屏幕互动、音频播放等）下，不使用该接口；系统检测到非规范使用该接口时，可能会恢复自动熄屏功能。

Q：录音场景下，setWindowKeepScreenOn接口会不会被系统管控？

A：录音场景系统不会管控屏幕常亮，跟随业务设置。
