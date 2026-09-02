---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-553
title: 视频全屏时，侧滑返回不是退出全屏，而是退出视频播放页
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 视频全屏时，侧滑返回不是退出全屏，而是退出视频播放页
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:16+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:d4109e4206e118e1911772e88e439d8d31f9c29f8807d96e30419100d43612e3
---

## 问题现象

应用进入视频播放页，默认是非全屏播放，点击切换成全屏后，侧滑返回，不是退出全屏状态，而是直接返回了上一页，退出了播放页面。

## 背景知识

[onBackPress](../harmonyos-references/ts-custom-component-lifecycle.md#onbackpress)：自定义组件的onBackPress生命周期，当用户点击返回按钮（包括侧滑返回）触发。支持重载：返回true表示页面自己处理返回逻辑，不进行页面路由；返回false表示使用默认的路由返回逻辑，不设置返回值按照false处理。

## 问题定位

1. 查看日志，当侧滑返回时，在应用日志里检索关键字“backpress”，忽略大小写。

   ```screen
   15572-15572   C03900/com.xxx.xx/Ace          com.xxx.xx           I     [(100000:100000:scope)] router consumed backpressed event
   ```

   该日志表示系统路由处理了一次返回事件，侧滑返回上一页是默认的路由逻辑。
2. 对比业界用户体验做的好的视频应用，在全屏状态下，侧滑返回，首先会退出全屏状态，再次侧滑才会返回上一页，检索其首次侧滑时的日志。

   ```screen
   18551-22699   C03900/xx.xx.xx/Ace          xx.xx.xx     I     [(-1:100000:singleton)] [xx.xx.xx][entry][100000]: OnBackPressed called
   18551-18551   C03922/xx.x...AceNavigation  xx.xx.xx     I     [(100000:100000:scope)] navigation user onBackPress return true
   18551-18551   C03900/xx.xx.xx/Ace          xx.xx.xx     I     [(100000:100000:scope)] Navigation consumed backpressed event
   ```

   日志表明应用重载了onBackPress生命周期回调，返回true，由应用页面自己处理了这次返回逻辑，系统不再执行页面路由。

## 分析结论

由于应用页面没有额外处理全屏时的侧滑返回事件，用户侧滑返回时，默认执行系统路由返回上一页。

## 修改建议

如需在视频全屏状态时，侧滑返回先退出全屏，而不返回上一页，需要重载页面组件的onBackPress生命周期回调。在回调里，判断是否全屏播放状态，是则退出全屏，不执行路由逻辑，否则执行路由返回。

参考代码：

```screen
import { common } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';
@Entry
@Component
struct VideoPage {
  @State fullScreenVideo: boolean = false;

  setVideoFullScreen(fullScreenVideo: boolean): void {
    this.fullScreenVideo = fullScreenVideo;
    let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
    let windowClass = (context as common.UIAbilityContext).windowStage.getMainWindowSync();
    windowClass.setPreferredOrientation(this.fullScreenVideo?
      window.Orientation.LANDSCAPE : window.Orientation.PORTRAIT);
  }

  onBackPress() {
    if (this.fullScreenVideo) {
      // 退出全屏
      this.setVideoFullScreen(false);
      return true;
    } else {
      // 系统默认返回逻辑，返回上一页
      return false;
    }
  }

  build() {
    Row() {
      Column() {
        MyVideo({ fullScreenVideo: this.fullScreenVideo })
          .onClick(() => {
            this.setVideoFullScreen(!this.fullScreenVideo);
          })
      }
      .width('100%')
    }
    .height('100%')
  }
}

@Component
struct MyVideo {
  @Link fullScreenVideo: boolean;
  build() {
    Row() {
      // 此处使用Text组件模拟三方视频组件
      Text(this.fullScreenVideo? '现在是全屏' : '现在是竖屏')
        .textAlign(TextAlign.Center)
        .fontSize(50)
        .width('100%')
        .height(this.fullScreenVideo? '100%' : 200)
    }
  }
}
```
