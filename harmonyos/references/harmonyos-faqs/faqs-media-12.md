---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-media-12
title: Tab页切换视频未暂停播放
breadcrumb: FAQ > 媒体开发 > 音频和视频 > 媒体（Media ） > Tab页切换视频未暂停播放
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:44+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:8f0bb75c8897e09e2210645422576ecb6aa38ff389f15093e8e38ed56dad252e
---

## 问题现象

应用从视频播放页面切换到其他Tab页，视频未暂停播放。

## 背景知识

* [AVPlayer播放视频](../harmonyos-guides/video-playback.md)：功能较完善的音视频播放ArkTS/JS API，集成了流媒体和本地资源解析，媒体资源解封装，视频解码和渲染功能，适用于对媒体资源进行端到端播放的场景，可直接播放mp4、mkv等格式的视频文件。
* [Tabs](../harmonyos-guides/arkts-navigation-tabs.md)：通过页签进行内容视图切换的容器组件，每个页签对应一个内容视图。[onChange](../harmonyos-references/ts-container-tabs.md#onchange)为Tab页签切换后触发的事件。

## 问题定位

1. 根据现象判断，应用在切换到其他页面时没有在监听到页面变化时进行视频播放暂停处理。
2. 验证判断：
   * 通过关键词(start|pause|status|Player|tab|onChange)过滤日志，如下所示：

     ```shell
     07-01 10:31:39.011   20804-20973   C03900/com.leh...video/Ace             I     [a92ab1488b010a2 0 0][(100000:100000:scope)] Media player start to play.
     07-01 10:31:39.013   20804-20973   C02B2B/com.leh...MonitorClient         I     [a92ab1488b010a2 0 0]#83 0x04B6E0 StartClick
     07-01 10:31:39.014   20804-20969   C02B2B/com.leh...rServiceProxy         I     [a92ab1488b010a2 0 0]#726 0x15E100 surfaceFormat is !
     07-01 10:31:39.112   20804-20970   C03906/com.leh...ideo/AceVideo         I     [(100000:100000:scope)] trigger mediaPlayer play
     07-01 10:31:39.112   20804-20970   C03900/com.leh...video/Ace             I     [(100000:100000:scope)] Media player start to play.
     07-01 10:31:39.776   20804-20804   C03906/com.leh...ideo/AceVideo         I     [(100000:100000:scope)] Player current status is PREPARED.
     07-01 10:31:39.777   20804-20804   C01406/com.leh...ideo/OHOS::RS         I     RSNode::AddChild, Id: 89352499626093, SurfaceNode:[Id: 89352499626092, name: MediaPlayerSurface]
     07-01 10:31:39.777   20804-20943   C03906/com.leh...ideo/AceVideo         I     [(100000:100000:scope)] trigger mediaPlayer play
     07-01 10:31:39.777   20804-20943   C03900/com.leh...video/Ace             I     [(100000:100000:scope)] Media player start to play.
     07-01 10:31:39.811   20804-20804   C03906/com.leh...ideo/AceVideo         I     [(100000:100000:scope)] start render frame size:[720.00 x 1280.00]
     07-01 10:31:39.877   20804-20804   C03906/com.leh...ideo/AceVideo         I     [(100000:100000:scope)] Player current status is STARTED.
     07-01 10:31:40.540   20804-20937   C03F00/com.leh...o/ArkCompiler         I     [gc] SmartGC: app cold start just finished
     07-01 10:31:46.543   20804-20937   C03F00/com.leh...o/ArkCompiler         I     [gc] SmartGC: app cold start finished
     07-01 10:31:53.932   20804-20804   C03915/com.leh...deo/AceSwiper         I     [(100000:100000:scope)] Swiper start property animation with offsetX: 1260.000000, offsetY: 0.000000
     07-01 10:31:53.939   20804-20804   C03915/com.leh...deo/AceSwiper         I     [(100000:100000:scope)] FireAnimationStartEvent, index: 1, targetIndex: 0, id:57
     07-01 10:31:54.188   20804-20804   C03915/com.leh...deo/AceSwiper         I     [(100000:100000:scope)] FireAnimationEndEvent index: 0, currentOffset: has_value 1, value 0.000000vp, isForce: 0, aniStartCalledCount 1, id:57
     07-01 10:31:57.740   20804-20804   C03951/com.leh...InputKeyFlow          I     [(100000:100000:scope)] InputTracking id:29922, touch test hitted node info: fingerId: 0{ tag: TabBar, depth: 11 };{ tag: Column, depth: 12 };{ tag: Button, depth: 13 };
     07-01 10:31:57.769   20804-20804   C03916/com.leh...video/AceTabs         I     [(100000:100000:scope)] Clicked tabBarIndex: 1
     ```
   * 日志“Clicked tabBarIndex: 1”中可以看出Tab页的切换，但后面没有视频状态的变化日志。

## 分析结论

应用缺少在页面变化时对正在播放的视频进行暂停处理能力，或处理视频暂停的逻辑未放在正确的位置，导致应用在前台时即使切换Tab页也会一直播放视频。

## 修改建议

在Tab页切换的onChange事件中或监听页面切换的方法里加入对视频播放的暂停控制能力。参考代码：

```ts
@Entry
@Component
struct onChangePause {
  private tabController: TabsController = new TabsController();
  private vController: VideoController = new VideoController();
  @State currentIndex: number = 0;
  private videoSrc: string = "EXAMPLE_URL";

  @Builder
  tabBuilder(targetIndex: number, title: string) {
    Column() {
      Text(title)
        .fontColor(this.currentIndex === targetIndex ? '#1698CE' : '#6B6B6B')
    }
    .width('100%')
    .height(50)
    .justifyContent(FlexAlign.Center)
  }

  build() {
    Column() {
      Tabs({ barPosition: BarPosition.Start, index: this.currentIndex, controller: this.tabController }) {
        TabContent() {
          Column() {
            Video({
              src: this.videoSrc,
              controller: this.vController
            })
              .objectFit(ImageFit.Contain)
          }.width('100%').height('100%').backgroundColor('#00CB87')
        }.tabBar(this.tabBuilder(0, '首页'))

        TabContent() {
          Column().width('100%').height('100%').backgroundColor('#F1F3F5')
        }.tabBar(this.tabBuilder(1, '我的'))
      }
      .barPosition(BarPosition.End)
      .onChange((index: number) => {
        // currentIndex控制TabContent显示页签
        if (this.currentIndex != index) {
          this.vController.pause();
        }
        this.currentIndex = index;
      })
    }
    .height('100%')
    .width('100%')
    .justifyContent(FlexAlign.SpaceAround)
  }
}
```
