---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-avsession-21
title: 应用内直播切换后台后声音正常但无播控组件
breadcrumb: FAQ > 媒体开发 > 音频和视频 > 音视频播控（AVSession） > 应用内直播切换后台后声音正常但无播控组件
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:45+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:69dd78b93c828f859db678a7ced4f9b8bf05a974b005e38b17a265d0963b52ec
---

## 问题现象

在应用内打开直播，切换直播界面至后台时，音频播放仍能正常持续，听觉体验无中断。然而，系统并未触发预期的播控中心。

## 背景知识

* [AVSession Kit](../harmonyos-guides/avsession-overview.md)：音视频播控服务是系统提供的音视频管控服务，用于统一管理系统中所有音视频行为，帮助开发者快速构建音视频统一展示和控制能力。
* 应用[接入AVSession](../harmonyos-guides/avsession-access-scene.md#接入流程)流程分为如下几个步骤：
  1. 确定应用需要创建的会话类型，创建对应的会话，不同类型决定了播控中心展示的控制模板样式。
  2. 按需创建后台任务。
  3. 设置必要的元数据（Metadata），以在播控中心展示相应的信息，包括不限于：当前媒体的ID（assetId），上一首媒体的ID（previousAssetId），下一首媒体的ID（nextAssetId），标题（title），专辑作者（author），专辑名称（album），词作者（writer），媒体时长（duration）等属性。
  4. 设置播放相关的状态，包括不限于：当前媒体的播放状态（state）、播放位置（position）、播放倍速（speed）、缓冲时间（bufferedTime）、循环模式（loopMode）、是否收藏（isFavorite）、正在播放的媒体Id（activeItemId）、自定义媒体数据（extras）等属性。
  5. 按需注册不同的控制命令，包括不限于：播放/暂停、上下一首、快进快退、收藏、循环模式、进度条。应用退出或者无对应业务时，注销会话。

## 问题定位

1. 查看问题日志信息进行分析，全局搜索关键词AVSession，可见此时当前的AVSession会话焦点（Session Focus）指向了另一个应用（进程ID：1654），并且有且只有这一个最高优先级媒体会话。

   ```screen
   08-12 16:32:27.873 1654 22650 I C02B91/av_session/AVSession: [GetAllSessionDescriptors]GetAllSessionDescriptors with size=1, topSession:com.***
   ```
2. 全局搜索代码关键词AVSessionManager进行定位，发现应用并未通过AVSessionManager接口创建并激活媒体会话。

## 分析结论

应用并未创建、接入AVSession会话，导致当应用进入后台时，看不到相应的播控中心。

## 修改建议

建议应用正确[创建并接入AVSession](../harmonyos-guides/avsession-access-scene.md#接入流程)，确保设置正确的元数据，且至少注册一条控制命令，否则播控中心不显示当前应用接入的播控中心。参考示例如下：

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

应用如需长时间后台播放，则还需按需[创建后台任务](../harmonyos-guides/avsession-access-scene.md#创建后台任务)。
