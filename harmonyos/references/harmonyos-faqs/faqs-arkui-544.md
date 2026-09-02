---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-544
title: 文章内嵌套的视频点击全屏后，视频上下出现大量黑边
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 文章内嵌套的视频点击全屏后，视频上下出现大量黑边
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:01+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:926bf3a9bf27891256ecd50c05d810036014844785f8028522728a22510fb715
---

## 问题现象

文章内嵌套的视频点击全屏后，视频组件未横屏全屏播放。

## 背景知识

[Video](../harmonyos-references/ts-media-components-video.md#video-1)组件：用于播放视频文件并控制其播放状态的组件。

## 问题定位

排查代码中Video组件是否在[onFullscreenChange](../harmonyos-references/ts-media-components-video.md#onfullscreenchange)方法中监听视频是否进入全屏状态，并检查是否在进入全屏状态时通过[setPreferredOrientation](../harmonyos-references/arkts-apis-window-window.md#setpreferredorientation9)调整页面显示方向。

## 分析结论

未在代码中使用onFullscreenChange监听视频组件是否进入全屏状态并使用setPreferredOrientation主动改变页面显示方向，导致视频点击全屏后，未能横屏全屏播放。

## 修改建议

使用onFullscreenChange监听视频组件是否进入全屏状态，在监听到进入全屏状态时使用setPreferredOrientation调整页面为横屏显示，在监听到视频组件退出全屏状态时使用setPreferredOrientation调整页面为竖屏显示。具体示例代码如下：

```screen
import { common } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';

@Entry
@Component
struct VideoHeightError {
  controller: VideoController = new VideoController();
  private curRate: PlaybackSpeed = PlaybackSpeed.Speed_Forward_1_00_X;
  context = this.getUIContext().getHostContext() as common.UIAbilityContext;
  private windowClass: window.Window = this.context.windowStage.getMainWindowSync();

  build() {
    Navigation() {
      Scroll() {
        Column() {
          Stack({ alignContent: Alignment.Bottom }) {
            Video({
              // 视频资源实际开发需替换为实际视频资源
              src: $rawfile('example.mp4'),
              currentProgressRate: this.curRate,
              controller: this.controller
            })
              .width('100%')
              .height(300)
              .objectFit(ImageFit.Contain)
              .controls(true)
              .onFullscreenChange((e?: FullscreenObject) => {
                if (e != undefined) {
                  if (e.fullscreen == true) {
                    this.windowClass.setPreferredOrientation(window.Orientation.LANDSCAPE);
                  } else {
                    this.windowClass.setPreferredOrientation(window.Orientation.PORTRAIT);
                  }
                }
              });
          };
        };
      }
      .width('100%')
      .height('100%');
    }
    .mode(NavigationMode.Stack);
  }
}

interface FullscreenObject {
  fullscreen: boolean;
}
```
