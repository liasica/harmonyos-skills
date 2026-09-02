---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-avsession-28
title: 播控中心的播放状态错误
breadcrumb: FAQ > 媒体开发 > 音频和视频 > 音视频播控（AVSession） > 播控中心的播放状态错误
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:45+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:56bf0a4f06a4330776e950d62c96530889f2aa0787392efaa2176e6bf8472c34
---

## 问题现象

应用内视频已暂停，但是播控中心的播放状态仍然显示播放状态。

## 背景知识

[媒体播放状态](../harmonyos-guides/using-avsession-developer.md#基本概念)（AVPlaybackState）：用于描述媒体播放状态的相关属性，包含当前媒体的播放状态（state）、播放位置（position）、播放倍速（speed）、缓冲时间（bufferedTime）、循环模式（loopMode）、是否收藏（isFavorite）、正在播放的媒体Id（activeItemId）、自定义媒体数据（extras）等属性。

## 问题定位

1. 查看日志信息进行分析：全局搜索StreamClientState，找到应用内暂停视频（音频流）的上下文信息。

   ```txt
   06-06 10:49:47.022 38012 38735 I C02B87/com.***/AudioRenderer: [Pause]StreamClientState for Renderer::Pause. id: 108907
   ```
2. 进一步搜索SetAVPlaybackState关键词，可见在应用内视频暂停后，应用将播控中心的播放状态设置为setAVplaybackstate：2（播放状态）。

   ```txt
   06-06 10:49:47.302 38012 38012 I C02B91/com.***/AVSession: [AVSessionPostTask]AVSessionEventHandler create new: SetAVPlaybackState
   06-06 10:49:47.307 38012 38827 I C02B91/com.***/AVSession: [SetAVPlaybackState]SetAVPlaybackState:2
   ```

## 分析结论

应用内视频暂停后却将播放状态设置为播放，导致播控中心的状态栏显示有误。

## 修改建议

建议应用按照合理的逻辑设置播控中心的播放状态。

```ts
import { avSession as AVSessionManager } from '@kit.AVSessionKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct avSessionExample {
  message: string = 'hello world';
  @State currentState: AVSessionManager.AVPlaybackState = {
    state: AVSessionManager.PlaybackState.PLAYBACK_STATE_INITIAL, // 播放状态。
    position: {
      elapsedTime: 0, // 已经播放的位置，以ms为单位。
      updateTime: new Date().getTime(), // 应用更新当前位置时的时间戳，以ms为单位。
    },
  };
  @State elapsedTime: number = 0;
  @State updateTime: number = 0;
  context = this.getUIContext().getHostContext() as Context;
  type: AVSessionManager.AVSessionType = 'video';
  session: AVSessionManager.AVSession | null = null;
  controller: VideoController = new VideoController();

  aboutToAppear(): void {
    this.initAvsession();
  }

  aboutToDisappear(): void {
    this.destroySession();
  }

  async initAvsession() {
    // 创建并激活媒体会话
    this.session = await AVSessionManager.createAVSession(this.context, 'SESSION_NAME', this.type);
    this.setAVMetadata();
    this.registerSessionListener();
    this.session.activate();
  }

  private registerSessionListener() {
    this.session!.on('play', () => {
      console.info(`on play , do pause task`);
      this.controller.start();
    });
    this.session!.on('pause', () => {
      this.controller.pause();
    });
  }

  // 设置播放状态
  private setAVPlaybackState(currentState: AVSessionManager.AVPlaybackState) {
    this.session!.setAVPlaybackState(currentState, (err) => {
      if (err) {
        console.error(`Failed to set AVPlaybackState. Code: ${err.code}, message: ${err.message}`);
      } else {
        console.info(`SetAVPlaybackState successfully`);
      }
    });
  }

  // 设置元数据
  private setAVMetadata() {
    let metadata: AVSessionManager.AVMetadata = {
      assetId: '0',
      title: 'TITLE',
      mediaImage: 'IMAGE',
      duration: 91000,
    };
    this.session!.setAVMetadata(metadata).then(() => {
      console.info(`SetAVMetadata successfully`);
    }).catch((err: BusinessError) => {
      console.error(`Failed to set AVMetadata. Code: ${err.code}, message: ${err.message}`);
    });
  }

  async destroySession() {
    this.session?.off('play');
    this.session?.off('pause');
    this.session?.destroy();
  }

  build() {
    Column() {
      Video({
        src: $r('app.media.videoTest'),
        controller: this.controller,
      })
        .width('100%')
        .height(300)
        .onStart(() => {
          console.info('onStart');
          this.currentState.state = AVSessionManager.PlaybackState.PLAYBACK_STATE_PLAY;
          this.updateTime = new Date().getTime();
          this.currentState.position = { elapsedTime: this.elapsedTime, updateTime: this.updateTime };
          this.setAVPlaybackState(this.currentState);
        })
        .onPause(() => {
          console.info('onPause');
          this.currentState.state = AVSessionManager.PlaybackState.PLAYBACK_STATE_PAUSE;
          this.updateTime = new Date().getTime();
          this.currentState.position = { elapsedTime: this.elapsedTime, updateTime: this.updateTime };
          this.setAVPlaybackState(this.currentState);
        })
        .onSeeked((playbackInfo: PlaybackInfo) => {
          console.info('onSeeked');
          this.elapsedTime = playbackInfo.time * 1000;
          this.updateTime = new Date().getTime();
          this.currentState.position = { elapsedTime: this.elapsedTime, updateTime: this.updateTime };
          this.setAVPlaybackState(this.currentState);
        })
        .onUpdate((playbackInfo: PlaybackInfo) => {
          console.info('onUpdate');
          this.elapsedTime = playbackInfo.time * 1000;
          this.currentState.position = { elapsedTime: this.elapsedTime, updateTime: this.updateTime };
        })
    }
    .width('100%')
    .height('100%')
  }
}
```
