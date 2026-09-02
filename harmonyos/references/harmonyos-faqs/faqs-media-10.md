---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-media-10
title: 视频无法进行倍速播放
breadcrumb: FAQ > 媒体开发 > 音频和视频 > 媒体（Media ） > 视频无法进行倍速播放
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:44+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:99d17c90a2a209ed4ea4174198f2ae139b5c4dcc1447a68cd30c4e8ec049213b
---

## 问题现象

长按视频界面显示倍速播放状态，但实际仍保持原速播放。

## 背景知识

[视频播放 (Video)](../harmonyos-guides/arkts-common-components-video-player.md)：Video组件用于播放视频文件并控制其播放状态，常用于短视频和应用内部视频的列表页面。

## 问题定位

搜索关键字SetSpeed，查看是否有修改视频倍速的日志，如果没有相关关键词SetSpeed，说明没有修改视频倍速。下面的日志为成功设置倍速的样例，先设置视频为二倍速，四秒后松开长按变回原速。

```screen
06-12 20:03:32.970   546-11001     C02b22/AudioSinkFilter          media_service         I     (SetSpeed(), 256): AudioSinkFilter::SetSpeed in, speed is 2.000
06-12 20:03:32.971   546-11001     C02b22/HiStreamer               media_service         I     [ASSP]:SetSpeed entered.
06-12 20:03:32.971   546-11001     C02b87/AudioRenderer            media_service         I     [SetSpeed]set speed 2.000000
06-12 20:03:32.971   546-11001     C02b8b/AudioSpeed               media_service         I     [SetSpeed]SetSpeed 2.000000
06-12 20:03:32.971   546-11001     C02b22/AudioSinkFilter          media_service         I     (SetSpeed(), 263): AudioSinkFilter::SetSpeed out
06-12 20:03:32.971   546-11001     C02b3a/MediaDemuxer             media_service         I     (SetSpeed(), 2167): Speed=2.000000
06-12 20:03:37.015   546-11001     C02b22/AudioSinkFilter          media_service         I     (SetSpeed(), 256): AudioSinkFilter::SetSpeed in, speed is 1.000
06-12 20:03:37.015   546-11001     C02b22/HiStreamer               media_service         I     [ASSP]:SetSpeed entered.
06-12 20:03:37.015   546-11001     C02b87/AudioRenderer            media_service         I     [SetSpeed]set speed 1.000000
06-12 20:03:37.015   546-11001     C02b8b/AudioSpeed               media_service         I     [SetSpeed]SetSpeed 1.000000
06-12 20:03:37.015   546-11001     C02b22/AudioSinkFilter          media_service         I     (SetSpeed(), 263): AudioSinkFilter::SetSpeed out
06-12 20:03:37.015   546-11001     C02b3a/MediaDemuxer             media_service         I     (SetSpeed(), 2167): Speed=1.000000
```

## 分析结论

应用未成功修改视频倍速。

## 修改建议

修改视频倍速相关代码逻辑。以Video组件为例：

```screen
import { window } from '@kit.ArkUI';

@Entry
@Component
struct VideoPlayer {
  source: string | Resource = $r('app.media.videoTest');  //视频资源位置
  public controller: VideoController = new VideoController();
  @State speed: number = 1;
  @State isShowSpeedDialog: boolean = false;

  aboutToAppear(): void {
    window.getLastWindow(this.getUIContext().getHostContext(), (err, data) => { // 获取window实例
      let windowClass = data;
      windowClass.setPreferredOrientation(window.Orientation.LANDSCAPE); // 横屏
    });
  }

  build() {
    Stack({ alignContent: Alignment.TopStart }) {
      Column() {
        Video({
          src: this.source,
          controller: this.controller,
          currentProgressRate: this.speed,
        })
          .height('100%')
          .controls(false)
          .autoPlay(true)
          .objectFit(ImageFit.Contain)
          .loop(false)
          .gesture(
            LongPressGesture({ repeat: true })
              .onAction(() => {
                this.speed = PlaybackSpeed.Speed_Forward_2_00_X; // 设置二倍速
                this.isShowSpeedDialog = true; // 弹出视频倍速中的弹框
              })
              .onActionEnd(() => {
                this.speed = PlaybackSpeed.Speed_Forward_1_00_X; // 松手恢复原速
                this.isShowSpeedDialog = false; // 关闭视频倍速弹框
              })
          )
      }
      .height('100%')
      .backgroundColor(Color.Black)

      if (this.isShowSpeedDialog === true){
        Column() {
          Column() {
            Text('倍速播放中')
              .fontSize(20)
          }
          .padding(10)
          .backgroundColor('#575757')
          .margin({ top: 80 })
          .width(160)
          .opacity(0.6)
          .borderRadius(10)
        }
        .width('100%')
      }
    }
  }
}
```
